#!/usr/bin/env python3
"""關卡 7：忠實度檢查（程式部分）。不改任何檔案，只回報。

檢查每一頁 drafts/NN-*.md：
  1. 頁數 8–15，而且每一頁都在 outline.md 的表格中；
  2. frontmatter 的 cards: 都存在於 cards/，而且屬於 outline 為這一頁指定的卡片；
  3. 每一行內容（要點、重點句、流程、表格列、編號步驟）都有〔wiki 頁名〕出處，頁名在這一頁的 cards: 中，
     而且那一頁存在於 wiki；
  4. 每個數學式（$...$、$$...$$）去掉空白後，必須原樣出現在這一頁的卡片中；
  5. 數學式以外的數字，必須出現在這一頁的卡片中；
  6. 標題用英文（AGENTS.md §3-11）；
  7. 版面密度（2026-11-23 加入）：title 以外的每一頁至少要有一個圖表元件（flow、stack、grid、cycle、ladder、
     curve、chain）、表格或獨立數學式；文字量（中文字數＋英文詞數，不含數學式與出處）不超過 MAX_TEXT。

用法：python3 scripts/slides/check_drafts.py slides/topic-<slug> [NN ...]
有錯誤時 exit 1。可以只檢查指定的頁（逐頁稿節點的內部 loop 用）。
"""
import re
import sys
from pathlib import Path

from common import split_frontmatter, wiki_pages

CITE_RE = re.compile(r"〔([^〕]+)〕")
CJK_RE = re.compile(r"[㐀-鿿]")
MATH_RE = re.compile(r"\$\$(.+?)\$\$|\$(.+?)\$", re.S)
NUM_RE = re.compile(r"(?<![A-Za-z_])\d+(?:\.\d+)?")
COMP_RE = re.compile(r"^(flow|stack|grid|cycle|ladder|curve|chain):")
MAX_TEXT = 110  # 2026-11-23：使用者回饋文字密度偏高，150 → 110


def text_amount(body):
    """文字量：中文字數＋英文詞數；不含標題、數學式、出處與版面語法。"""
    t = "\n".join(l for l in body.splitlines() if not l.startswith("# "))
    t = CITE_RE.sub("", MATH_RE.sub("", t))
    t = re.sub(r"(?m)^\s*(flow|stack|grid|cycle|ladder|curve|chain):", "", t)
    t = re.sub(r"<->|->|\|\||::|[|*`>#-]", " ", t)
    return len(CJK_RE.findall(t)) + len(re.findall(r"[A-Za-z][A-Za-z0-9'_.()]*", t))


def outline_cards(outline: Path):
    out = {}
    for line in outline.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*(\d+)\s*\|", line)
        if m:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            out[int(m.group(1))] = [c.strip() for c in cells[-1].split(",") if c.strip()]
    return out


def norm_math(s):
    return re.sub(r"\s+", "", s)


def content_lines(body):
    """需要出處的行：要點、重點句、流程、編號步驟、表格資料列（不含表頭與分隔列）。"""
    lines, table_row = [], 0
    for ln, line in enumerate(body.splitlines(), 1):
        s = line.strip()
        if s.startswith("|"):
            table_row += 1
            if table_row >= 3:  # 第 1 列表頭、第 2 列分隔
                lines.append((ln, s))
            continue
        table_row = 0
        if s.startswith(("- ", "> ")) or COMP_RE.match(s) or re.match(r"^\d+\. ", s):
            lines.append((ln, s))
    return lines


DENSITY = {}


def check(topic: Path, only=None):
    drafts = sorted((topic / "drafts").glob("[0-9][0-9]-*.md"))
    outline = outline_cards(topic / "outline.md")
    known = wiki_pages()
    errs = {}

    def err(where, msg):
        errs.setdefault(where, []).append(msg)

    if not only and not 8 <= len(drafts) <= 15:
        err("(全部)", f"頁數 {len(drafts)}，規格是 8–15 頁")
    for d in drafts:
        nn = int(d.name[:2])
        if only and nn not in only:
            continue
        fm, body = split_frontmatter(d.read_text(encoding="utf-8"))
        m = re.search(r"^cards:\s*\[(.*)\]", fm, re.M)
        cards = [c.strip() for c in m.group(1).split(",")] if m else []
        if not cards:
            err(d.name, "frontmatter 缺少 cards:")
        if nn not in outline:
            err(d.name, f"outline.md 沒有第 {nn} 頁")
        for c in cards:
            if not (topic / "cards" / f"{c}.md").exists():
                err(d.name, f"卡片不存在：{c}")
            if nn in outline and c not in outline[nn]:
                err(d.name, f"卡片「{c}」不在 outline 為第 {nn} 頁指定的卡片 {outline[nn]} 中")
        card_text = "\n".join((topic / "cards" / f"{c}.md").read_text(encoding="utf-8")
                              for c in cards if (topic / "cards" / f"{c}.md").exists())
        card_math = norm_math(card_text)
        for ln, line in enumerate(body.splitlines(), 1):
            if line.startswith("#") and CJK_RE.search(line):
                err(d.name, f"第 {ln} 行：標題要用英文")
        for ln, line in content_lines(body):
            cites = CITE_RE.findall(line)
            if not cites:
                err(d.name, f"第 {ln} 行沒有出處：{line[:50]}")
            for c in cites:
                if c not in cards:
                    err(d.name, f"第 {ln} 行引用〔{c}〕，但它不在這一頁的 cards: 中")
                if c not in known:
                    err(d.name, f"第 {ln} 行引用〔{c}〕，wiki 沒有這一頁")
        for mm in MATH_RE.finditer(body):
            expr = mm.group(1) or mm.group(2)
            if norm_math(expr) not in card_math:
                err(d.name, f"數學式不在卡片中：${expr.strip()[:60]}$")
        layout = (re.search(r"^layout:\s*(\S+)", fm, re.M) or [None, "bullets"])[1]
        amount = text_amount(body)
        has_visual = bool(re.search(r"(?m)^\s*(\$\$|\||(flow|stack|grid|cycle|ladder|curve|chain):)", body))
        if layout != "title":
            if not has_visual:
                err(d.name, "沒有圖表、表格或獨立數學式（版面密度規則）→ 退回改成圖表")
            if amount > MAX_TEXT:
                err(d.name, f"文字量 {amount} 超過 {MAX_TEXT}（版面密度規則）→ 退回精簡或改成圖表")
        DENSITY[d.name] = amount
        plain = CITE_RE.sub("", MATH_RE.sub("", body))
        for num in sorted(set(NUM_RE.findall(plain))):
            if num not in card_text:
                err(d.name, f"數字 {num} 不在這一頁的卡片中")
    return errs, len(drafts)


def main():
    topic = Path(sys.argv[1])
    only = {int(x) for x in sys.argv[2:]} or None
    errs, n = check(topic, only)
    for where, es in sorted(errs.items()):
        print(f"✗ {where}")
        for e in es:
            print(f"  - {e}")
    print("文字量：" + "、".join(f"{k[:2]}={v}" for k, v in sorted(DENSITY.items())))
    total = sum(len(v) for v in errs.values())
    print(f"共 {n} 頁；錯誤 {total}" + ("（通過）" if not total else ""))
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
