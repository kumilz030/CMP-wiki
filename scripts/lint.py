#!/usr/bin/env python3
"""CMP-wiki 的確定性檢查（不呼叫任何模型）。

用法：
  python3 scripts/lint.py               # 全庫檢查，有錯誤時 exit 1
  python3 scripts/lint.py --file PATH   # 只檢查一頁（hook 用；不做跨頁檢查）
  python3 scripts/lint.py --find 關鍵字  # 用頁名與 aliases 搜尋既有頁面（開新頁前用）

檢查項目：
  結構：frontmatter、type、資料夾、## 標題和範本一致、標題用英文、帶路徑的連結
  概念頁：wiki/概念/UNN/、order:、kind:、每個單元資料夾有 00 UNN concepts.base
  方程式頁：Conditions of validity 不可空白；邏輯鏈：Steps 至少 3 步且每步有連結
  出處：sources: 與內文一致；[[來源-X]] p.N 的 N 在該來源的講義頁數內；引號原文要真的在那一頁
  公開（AGENTS.md §6）：附圖不可是 raw/ 的檔案、引號原文不超過一句、來源頁要有原站 url:、不可有 email
  全庫：壞連結、重複頁名與 aliases、孤兒頁、⚠️待查證清單
raw/ 不在（例如 GitHub Actions）時，跳過需要 raw/ 的檢查。
"""
import argparse
import hashlib
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"
TEXT = RAW / "text"
ATTACH = WIKI / "附圖"

TEMPLATE_OF = {
    "概念": "概念頁.md",
    "方程式": "方程式頁.md",
    "推導": "推導頁.md",
    "邏輯鏈": "邏輯鏈頁.md",
    "實作": "實作頁.md",
    "習題": "習題頁.md",
    "來源": "來源頁.md",
}
FOLDER_OF = {"方程式": "方程式", "推導": "推導", "邏輯鏈": "邏輯鏈", "實作": "實作", "習題": "習題", "來源": "來源"}
PREFIX_OF = {"推導": "推導-", "實作": "實作-", "習題": "習題-", "來源": "來源-"}
FREE_FOLDERS = ("綜合", "補充")
KINDS = {"theorem", "approximation", "method", "quantity", "concept", "parameter", "tool"}

LINK_RE = re.compile(r"(!?)\[\[([^\]|#]+)(#[^\]|]*)?(\|[^\]]*)?\]\]")
SRC_LINK_RE = re.compile(r"\[\[(來源-[^\]|#]+)")
CITE_RE = re.compile(r"\[\[(來源-[^\]|#]+)(?:\|[^\]]*)?\]\]\s*p\.\s?(\d+)(?:\s?[–-]\s?(\d+))?")
QUOTE_RE = re.compile(r"[\"“]([A-Za-z][^\"”\n]{15,}?)[\"”]")
CJK_RE = re.compile(r"[㐀-鿿豈-﫿]")
EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
MAX_QUOTE_WORDS = 30


# ---------- 讀取 ----------

class Page:
    def __init__(self, path: Path):
        self.path = path
        self.rel = path.relative_to(ROOT).as_posix()
        self.name = path.stem
        raw = path.read_text(encoding="utf-8")
        self.fm, self.body, self.fm_error, self.fm_text = {}, raw, None, ""
        if raw.startswith("---\n"):
            end = raw.find("\n---", 4)
            if end == -1:
                self.fm_error = "frontmatter 沒有結尾的 ---"
            else:
                try:
                    self.fm = yaml.safe_load(raw[4:end]) or {}
                except yaml.YAMLError as e:
                    self.fm_error = f"frontmatter 不是合法 YAML：{e}"
                self.fm_text = raw[4:end]
                self.body = raw[end + 4:]
        elif path.parent != ROOT:
            self.fm_error = "缺少 frontmatter"
        if not isinstance(self.fm, dict):
            self.fm = {}
        self.type = self.fm.get("type")

    def aliases(self):
        a = self.fm.get("aliases") or []
        return [str(x) for x in a] if isinstance(a, list) else [str(a)]

    def heading_lines(self):
        out, in_code = [], False
        for ln, line in enumerate(self.body.splitlines(), 1):
            if line.startswith("```"):
                in_code = not in_code
            elif not in_code and re.match(r"^#{1,6} ", line):
                out.append((ln, line))
        return out

    def headings(self):
        return [l[3:].strip() for _, l in self.heading_lines() if l.startswith("## ")]

    def section(self, title):
        m = re.search(rf"^## {re.escape(title)}\s*$(.*?)(?=^## |\Z)", self.body, re.M | re.S)
        return m.group(1) if m else None

    def links(self):
        text = self.fm_text + "\n" + self.body
        return [(m.group(1) == "!", m.group(2).strip()) for m in LINK_RE.finditer(text)]


def load_pages():
    pages = [Page(p) for p in sorted(WIKI.rglob("*.md"))]
    extra = [Page(ROOT / "index.md")] if (ROOT / "index.md").exists() else []
    return pages, extra


def template_headings():
    out = {}
    for t, f in TEMPLATE_OF.items():
        p = ROOT / "templates" / f
        if p.exists():
            out[t] = [l[3:].strip() for l in p.read_text(encoding="utf-8").splitlines() if l.startswith("## ")]
    return out


def source_pdfs():
    """來源頁名 → 講義 PDF 檔名主幹列表（從來源頁的 raw:）。"""
    out = {}
    for p in (WIKI / "來源").glob("*.md"):
        pg = Page(p)
        raws = pg.fm.get("raw") or []
        raws = raws if isinstance(raws, list) else [raws]
        out[pg.name] = [Path(str(r)).stem for r in raws if str(r).lower().endswith(".pdf")]
    return out


def pdf_pages(stem):
    d = TEXT / stem
    return sorted(int(p.stem[1:]) for p in d.glob("p*.txt")) if d.exists() else []


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.casefold()).strip()


# ---------- 單頁檢查 ----------

def check_citations(page, srcmap):
    errs = []
    if not TEXT.exists():
        return errs
    for ln, line in enumerate(page.body.splitlines(), 1):
        for m in CITE_RE.finditer(line):
            src, a = m.group(1), int(m.group(2))
            b = int(m.group(3)) if m.group(3) else a
            stems = srcmap.get(src)
            if not stems:
                continue  # 沒有講義的來源（例如只有主題頁），無法驗證頁碼
            avail = set()
            for s in stems:
                avail.update(pdf_pages(s))
            if not avail:
                continue
            if a not in avail or b not in avail:
                errs.append(f"第 {ln} 行：[[{src}]] p.{a}{'–' + str(b) if b != a else ''} 超出講義頁數（1–{max(avail)}）")
                continue
            # 同一行的引號原文要真的出現在引用的頁
            for q in QUOTE_RE.finditer(line):
                txt = " ".join((TEXT / s / f"p{n}.txt").read_text(encoding="utf-8")
                               for s in stems for n in range(a, b + 1) if (TEXT / s / f"p{n}.txt").exists())
                if norm(q.group(1)) not in norm(txt):
                    errs.append(f"第 {ln} 行：引號原文「{q.group(1)[:40]}…」不在 [[{src}]] p.{a}")
    return errs


def check_public(page):
    errs = []
    for ln, line in enumerate(page.body.splitlines(), 1):
        for q in QUOTE_RE.finditer(line):
            n = len(q.group(1).split())
            if n > MAX_QUOTE_WORDS:
                errs.append(f"第 {ln} 行：引號原文 {n} 字，超過 {MAX_QUOTE_WORDS} 字（AGENTS.md §6-2：每處不超過一句）")
        if EMAIL_RE.search(line):
            errs.append(f"第 {ln} 行：疑似 email，公開頁面不可放個人資料（§6-5）")
    if page.type == "來源":
        url = str(page.fm.get("url") or "")
        if not url.startswith("https://www.compmatphys.org/"):
            errs.append(f"來源頁的 url: 要是原站主題頁網址，現在是 {url!r}（§6-4）")
    return errs


def check_page(page, tmpl, srcmap):
    errs = []
    if page.fm_error:
        return [page.fm_error]
    for ln, line in page.heading_lines():
        if CJK_RE.search(line):
            errs.append(f"第 {ln} 行：標題要用英文（AGENTS.md §3-11）：{line[:50]}")
    for is_embed, target in page.links():
        if "/" in target and not is_embed:
            errs.append(f"帶路徑的連結 [[{target}]]，請改成只寫頁名")
    if page.path.parent == ROOT:
        return errs
    t = page.type
    folder = page.path.parent.name
    if t in TEMPLATE_OF:
        if t in tmpl and page.headings() != tmpl[t]:
            errs.append(f"## 標題和範本不一致：{page.headings()} ≠ 範本 {tmpl[t]}")
        if t == "概念":
            if page.path.parent.parent.name != "概念" or not re.fullmatch(r"U\d{2}", folder):
                errs.append(f"概念頁要放在 wiki/概念/UNN/，現在在 {page.rel}")
            if str(page.fm.get("unit") or "") != folder:
                errs.append(f"unit: {page.fm.get('unit')!r} 和資料夾 {folder} 不一致")
            order = str(page.fm.get("order") or "")
            if not re.fullmatch(r"[A-Za-z0-9-]+-\d{2}", order):
                errs.append(f"order: 缺少或格式不對（要像 \"AW03C-02\"）：{order!r}")
            if page.fm.get("kind") not in KINDS:
                errs.append(f"kind: 要是 {sorted(KINDS)} 之一，現在是 {page.fm.get('kind')!r}")
        elif FOLDER_OF.get(t) != folder:
            errs.append(f"type: {t} 卻放在 wiki/{folder}/")
        if t in PREFIX_OF and not page.name.startswith(PREFIX_OF[t]):
            errs.append(f"{t}頁的頁名要以「{PREFIX_OF[t]}」開頭")
    elif folder not in FREE_FOLDERS:
        errs.append(f"未知的 type：{t!r}")
    if t == "邏輯鏈":
        steps = [l for l in (page.section("Steps") or "").splitlines() if re.match(r"^\d+\. ", l)]
        if len(steps) < 3:
            errs.append(f"「Steps」至少要 3 步，現在 {len(steps)} 步")
        for l in steps:
            if not LINK_RE.search(l):
                errs.append(f"「Steps」的每一步都要連到一個頁面：{l[:40]}")
    if t == "方程式":
        sec = re.sub(r"（必填.*?）", "", page.section("Conditions of validity") or "").strip()
        if not sec:
            errs.append("「Conditions of validity」是空的")
    if t and t != "來源":
        declared = {re.sub(r"^\[\[|\]\]$", "", str(s)).strip() for s in (page.fm.get("sources") or [])}
        declared.discard("來源-")
        used = set(SRC_LINK_RE.findall(page.body))
        if used - declared:
            errs.append(f"內文引用了但 sources: 沒列：{sorted(used - declared)}")
        if declared - used:
            errs.append(f"sources: 列了但內文沒引用：{sorted(declared - used)}")
    errs += check_citations(page, srcmap)
    errs += check_public(page)
    return errs


# ---------- 全庫檢查 ----------

def raw_hashes():
    if not RAW.exists():
        return {}
    out = {}
    for f in RAW.rglob("*"):
        if f.is_file() and "text" not in f.relative_to(RAW).parts[:1]:
            out[hashlib.sha256(f.read_bytes()).hexdigest()] = f.relative_to(ROOT).as_posix()
    return out


def lint_all():
    pages, extra = load_pages()
    tmpl = template_headings()
    srcmap = source_pdfs()
    report, warnings = {}, []

    def err(where, msg):
        report.setdefault(where, []).append(msg)

    names = {}
    for p in pages:
        names.setdefault(p.name, []).append(p)
    concept_dir = WIKI / "概念"
    if concept_dir.exists():
        for d in sorted(x for x in concept_dir.iterdir() if x.is_dir()):
            if not re.fullmatch(r"U\d{2}", d.name):
                err("(全庫)", f"wiki/概念/{d.name}/ 不是 UNN 格式")
            elif not (d / f"00 {d.name} concepts.base").exists():
                err("(全庫)", f"wiki/概念/{d.name}/ 缺少「00 {d.name} concepts.base」")
    orders = {}
    for p in pages:
        if p.type == "概念" and p.fm.get("order"):
            orders.setdefault(str(p.fm["order"]), []).append(p.name)
    for o, ns in orders.items():
        if len(ns) > 1:
            err("(全庫)", f"order: {o} 重複：{ns}")
    for n, ps in names.items():
        if len(ps) > 1:
            err("(全庫)", f"頁名重複：{n} → {[p.rel for p in ps]}")
    lower_names = {n.casefold() for n in names}
    alias_owner = {}
    for p in pages:
        for a in p.aliases():
            key = a.casefold()
            if key in lower_names and key != p.name.casefold():
                err(p.rel, f"alias「{a}」和另一頁的頁名相同")
            alias_owner.setdefault(key, []).append(p.name)
    for a, owners in alias_owner.items():
        if len(set(owners)) > 1:
            err("(全庫)", f"alias「{a}」重複出現在：{sorted(set(owners))}（可能是重複頁）")
    # 附圖：不可是 raw/ 的檔案（§6-1、§6-3）
    attachments = {f.name for f in ATTACH.glob("*") if f.is_file() and f.name != ".gitkeep"} if ATTACH.exists() else set()
    rh = raw_hashes()
    for f in sorted(ATTACH.glob("*")) if ATTACH.exists() else []:
        if f.is_file() and f.name != ".gitkeep":
            h = hashlib.sha256(f.read_bytes()).hexdigest()
            if h in rh:
                err(f.relative_to(ROOT).as_posix(), f"和 {rh[h]} 相同：原站檔案不可放進 wiki/（§6-1）")
    for f in WIKI.rglob("*"):
        if f.is_file() and f.suffix.lower() in (".pdf", ".vtt", ".srt"):
            err(f.relative_to(ROOT).as_posix(), "wiki/ 裡不可放 PDF 或字幕檔（§6-1）")
    inbound = {p.name: 0 for p in pages}
    for p in pages + extra:
        for is_embed, target in p.links():
            tname = target.split("/")[-1]
            if is_embed or re.search(r"\.(png|jpe?g|gif|svg|webp)$", tname, re.I):
                if tname not in attachments:
                    err(p.rel, f"嵌入的檔案不存在：{target}")
                continue
            if tname not in names:
                err(p.rel, f"壞掉的連結 [[{target}]]")
            elif tname != p.name:
                inbound[tname] += 1
    for p in pages:
        e = check_page(p, tmpl, srcmap)
        if e:
            report.setdefault(p.rel, []).extend(e)
        if inbound.get(p.name, 0) == 0:
            warnings.append(f"{p.rel}：孤兒頁（沒有任何頁連進來）")
    for p in extra:
        e = check_page(p, tmpl, srcmap)
        if e:
            report.setdefault(p.rel, []).extend(e)
    todo = []
    for p in pages:
        for line in p.body.splitlines():
            if "⚠️待查證" in line and not line.strip().endswith("⚠️待查證"):
                todo.append(f"{p.name}：{line.strip()[:100]}")
    if not TEXT.exists():
        warnings.append("找不到 raw/text/：略過講義頁碼與引號原文的驗證")
    return report, warnings, todo, len(pages)


def find(keyword):
    pages, _ = load_pages()
    k = keyword.casefold()
    hits = [p for p in pages if k in p.name.casefold() or any(k in a.casefold() for a in p.aliases())]
    for p in hits:
        print(f"{p.rel}  aliases={p.aliases()}")
    if not hits:
        print("沒有找到；可以開新頁。")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file")
    ap.add_argument("--find")
    args = ap.parse_args()
    if args.find:
        find(args.find)
        return 0
    if args.file:
        path = Path(args.file).resolve()
        if WIKI not in path.parents or path.suffix != ".md":
            return 0
        errs = check_page(Page(path), template_headings(), source_pdfs())
        for e in errs:
            print(f"{path.relative_to(ROOT)}：{e}")
        return 1 if errs else 0
    report, warnings, todo, n = lint_all()
    nerr = sum(len(v) for v in report.values())
    for where, errs in sorted(report.items()):
        print(f"\n✗ {where}")
        for e in errs:
            print(f"  - {e}")
    if warnings:
        print("\n⚠ 警告")
        for w in warnings:
            print(f"  - {w}")
    print(f"\n⚠️待查證（{len(todo)}）")
    for t in todo:
        print(f"  - {t}")
    print(f"\n共 {n} 頁；錯誤 {nerr}、警告 {len(warnings)}")
    return 1 if nerr else 0


if __name__ == "__main__":
    sys.exit(main())
