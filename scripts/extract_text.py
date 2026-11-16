#!/usr/bin/env python3
"""把 raw/*.pdf 切成投影片並擷取文字（AGENTS.md §1、§3-1）。

輸出（raw/text/<PDF 檔名主幹>/）：
  s<K>.txt      第 K 張投影片的文字（K 從 1 開始，全份講義連續編號）——出處 `slide K` 對應這個檔
  p<N>.txt      第 N 頁的全部文字（各投影片接起來）
  slides.json   每張投影片在哪一頁、哪個位置、文字來源（pdftotext 或 OCR）

切投影片：原站講義是 A4 直式、左欄 3 張投影片、右欄筆記線的 handout。用頁面影像找左欄的
墨水區塊（間隔小於頁高 4% 的區塊合併），每個夠高的區塊算一張投影片。找不到左右欄分隔時，
整頁算一張（例如橫式投影片 PDF、論文）。
擷取文字：先用 pdftotext 擷取該區塊；字數太少（掃描影像）或是亂碼（字型編碼壞掉）就用 tesseract OCR。
OCR 會認錯符號與方程式，所以 raw/text 只用來搜尋與驗證，內容一律對照影像（§3-10）。

只有這支腳本可以寫 raw/text/（hook 放行）。已處理過的 PDF 會略過，加 --force 重做。
需要：pdftoppm、pdftotext（poppler-utils）、tesseract（tesseract-ocr）、Pillow、numpy。
"""
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
DPI = 300
MIN_CHARS = 30  # pdftotext 擷取少於這個字數，就改用 OCR


def page_count(pdf):
    info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
    return int(next(l.split()[-1] for l in info.splitlines() if l.startswith("Pages:")))


def render(pdf, page, tmp):
    base = Path(tmp) / f"pg{page}"
    subprocess.run(["pdftoppm", "-r", str(DPI), "-gray", "-png", "-singlefile",
                    "-f", str(page), "-l", str(page), str(pdf), str(base)], check=True)
    return base.with_suffix(".png")


def find_slides(img):
    """回傳這一頁的投影片區塊 [(x, y, w, h), ...]（像素，DPI 解析度），由上到下。"""
    a = np.array(img.convert("L"))
    H, W = a.shape
    dark = a < 235
    col = dark.mean(0)
    gutter = [x for x in range(int(W * 0.4), int(W * 0.7)) if col[x] < 0.005]
    if H <= W or not gutter:
        return [(0, 0, W, H)]
    right = gutter[0]
    rows = dark[:, :right].mean(1) > 0.01
    bands, start, end, gap = [], None, 0, 0
    for y, v in enumerate(rows):
        if v:
            start = y if start is None else start
            end, gap = y, 0
        elif start is not None:
            gap += 1
            if gap > H * 0.04:
                bands.append((start, end))
                start = None
    if start is not None:
        bands.append((start, end))
    pad = int(H * 0.005)
    boxes = [(0, max(0, s - pad), right, min(H, e + pad) - max(0, s - pad)) for s, e in bands if e - s > H * 0.08]
    # 同一頁的投影片一樣高：標題頁下方的作者欄常被當成另一塊而切掉，所以每塊都撐到最高那塊的高度
    tallest = max((b[3] for b in boxes), default=0)
    return [(x, y, w, min(tallest, H - y)) for x, y, w, h in boxes]


def looks_like_text(t):
    """pdftotext 有時抽出亂碼（字型編碼壞掉，例如「lllll sllss eeee」）：字母種類太少就當作沒有文字。"""
    letters = [c for c in t.lower() if c.isalpha()]
    return len(letters) >= MIN_CHARS and len(set(letters)) >= 12


def pdftotext_box(pdf, page, box):
    x, y, w, h = box
    return subprocess.run(["pdftotext", "-r", str(DPI), "-x", str(x), "-y", str(y), "-W", str(w), "-H", str(h),
                           "-f", str(page), "-l", str(page), "-layout", str(pdf), "-"],
                          capture_output=True, text=True).stdout.strip()


def ocr_box(img, box, tmp):
    x, y, w, h = box
    crop = Path(tmp) / "crop.png"
    img.crop((x, y, x + w, y + h)).save(crop)
    # psm 3（自動版面）：psm 6 會漏掉投影片標題（2026-11-16 用 AW03C 測試）
    return subprocess.run(["tesseract", str(crop), "-", "--psm", "3", "-l", "eng"],
                          capture_output=True, text=True).stdout.strip()


def process(pdf, out):
    out.mkdir(parents=True, exist_ok=True)
    meta, k = [], 0
    with tempfile.TemporaryDirectory() as tmp:
        for page in range(1, page_count(pdf) + 1):
            img = Image.open(render(pdf, page, tmp))
            texts = []
            for slot, box in enumerate(find_slides(img), 1):
                k += 1
                text, method = pdftotext_box(pdf, page, box), "pdftotext"
                if not looks_like_text(text):
                    text, method = ocr_box(img, box, tmp), "ocr"
                (out / f"s{k}.txt").write_text(f"# {pdf.name} slide {k}（p.{page} 第 {slot} 張，{method}）\n{text}\n", encoding="utf-8")
                meta.append({"slide": k, "page": page, "slot": slot, "box": box, "method": method, "chars": len(text)})
                texts.append(f"[slide {k}]\n{text}")
            (out / f"p{page}.txt").write_text(f"# {pdf.name} p.{page}\n" + "\n\n".join(texts) + "\n", encoding="utf-8")
    (out / "slides.json").write_text(json.dumps({"pdf": pdf.name, "slides": meta}, ensure_ascii=False, indent=1), encoding="utf-8")
    return k, sum(m["method"] == "ocr" for m in meta)


def main():
    missing = [t for t in ("pdftoppm", "pdftotext", "pdfinfo", "tesseract") if not shutil.which(t)]
    if missing:
        print(f"缺少工具：{', '.join(missing)}（sudo apt install poppler-utils tesseract-ocr）", file=sys.stderr)
        return 1
    force = "--force" in sys.argv
    total = 0
    for pdf in sorted(RAW.glob("*.pdf")):
        out = RAW / "text" / pdf.stem
        if (out / "slides.json").exists() and not force:
            continue
        n, n_ocr = process(pdf, out)
        print(f"{pdf.name}：{n} 張投影片（OCR {n_ocr} 張）")
        total += n
    print(f"共處理 {total} 張投影片")
    return 0


if __name__ == "__main__":
    sys.exit(main())
