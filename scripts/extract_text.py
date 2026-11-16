#!/usr/bin/env python3
"""把 raw/*.pdf 逐頁擷取成 raw/text/<PDF 檔名主幹>/p<N>.txt（N 是 PDF 頁）。

只有這支腳本可以寫 raw/text/（hook 放行）。已擷取過的 PDF 會略過，加 --force 重做。
文字擷取會拆亂分式、上下標與表格，所以 raw/text 只用來搜尋與驗證引用，不能當內容依據
（AGENTS.md §3-10）。
"""
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"


def main():
    if not shutil.which("pdftotext"):
        print("需要 pdftotext（poppler-utils）", file=sys.stderr)
        return 1
    force = "--force" in sys.argv
    total = 0
    for pdf in sorted(RAW.glob("*.pdf")):
        out = RAW / "text" / pdf.stem
        if out.exists() and not force:
            continue
        info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
        n = int(next(l.split()[-1] for l in info.splitlines() if l.startswith("Pages:")))
        out.mkdir(parents=True, exist_ok=True)
        for i in range(1, n + 1):
            text = subprocess.run(["pdftotext", "-layout", "-f", str(i), "-l", str(i), str(pdf), "-"],
                                  capture_output=True, text=True).stdout
            (out / f"p{i}.txt").write_text(f"# {pdf.name} p.{i}\n{text}", encoding="utf-8")
        print(f"{pdf.name}：{n} 頁")
        total += n
    print(f"共寫入 {total} 頁到 raw/text/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
