#!/usr/bin/env python3
"""節點 8：渲染 HTML。把已通過檢查的 drafts/ 轉成單一檔案的 deck.html。

只做語法轉換，不改任何一個字：標題、重點句、要點、編號步驟、數學式、流程方塊、表格。
出處〔頁名〕轉成連到 CMP-wiki 網站的小標籤，頁尾列出這一頁用到的卡片。

用法：python3 scripts/slides/render_deck.py slides/topic-<slug>
"""
import html
import json
import re
import sys
from pathlib import Path

from common import split_frontmatter, site_url, wiki_pages

CITE_RE = re.compile(r"〔([^〕]+)〕")
PAGES = wiki_pages()


def esc(s):
    return html.escape(s, quote=False)


CARDS = []  # 目前這一頁的卡片（出處編號用）


def inline(s):
    """行內語法：保留 $...$ 給 KaTeX，**粗體**、`code`、〔出處〕。"""
    parts = re.split(r"(\$[^$]+\$)", s)
    out = []
    for p in parts:
        if p.startswith("$") and p.endswith("$") and len(p) > 1:
            out.append(esc(p))
            continue
        p = esc(p)
        p = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", p)
        p = re.sub(r"`(.+?)`", r"<code>\1</code>", p)
        p = CITE_RE.sub(lambda m: cite(m.group(1)), p)
        out.append(p)
    return "".join(out).strip()


def cite(name):
    """行內出處：上標編號，對應頁尾的編號來源；滑鼠停留時顯示頁名。"""
    url = site_url(PAGES[name]) if name in PAGES else "#"
    n = CARDS.index(name) + 1 if name in CARDS else "?"
    return f'<a class="cite" href="{esc(url)}" title="{esc(name)}" target="_blank" rel="noopener">{n}</a>'


def source_item(name):
    url = site_url(PAGES[name]) if name in PAGES else "#"
    return (f'<a class="src" href="{esc(url)}" target="_blank" rel="noopener">'
            f'<span class="src-n">{CARDS.index(name) + 1}</span>{esc(name)}</a>')


def split_outside_math(spec, sep):
    """依分隔符號切開，但不切 $...$ 裡面的（例如 |\\vec r-\\vec r'| 的絕對值符號）。"""
    out, buf, in_math, i = [], "", False, 0
    while i < len(spec):
        if spec[i] == "$":
            in_math = not in_math
        if not in_math and spec.startswith(sep, i):
            out.append(buf)
            buf, i = "", i + len(sep)
            continue
        buf += spec[i]
        i += 1
    out.append(buf)
    return out


def figcite(cites):
    return f'<div class="figcite">{"".join(cite(c) for c in cites)}</div>' if cites else ""


def component(kind, spec):
    """自繪圖表元件（不放講義截圖，AGENTS.md §6）。只做排版，不改字。"""
    cites = CITE_RE.findall(spec)
    spec = CITE_RE.sub("", spec).strip()
    if kind in ("flow", "cycle"):
        back = ""
        if kind == "cycle" and "||" in spec:
            spec, back = [x.strip() for x in spec.split("||", 1)]
        parts = re.split(r"\s*(<->|->)\s*", spec)
        html_ = []
        for k, part in enumerate(parts):
            if k % 2:
                html_.append(f'<span class="arrow" aria-hidden="true">{"⇄" if part == "<->" else "→"}</span>')
            else:
                hi = part.startswith("*")
                html_.append(f'<div class="box{" hi" if hi else ""}"><span>{inline(part.lstrip("*").strip())}</span></div>')
        out = f'<div class="flow">{"".join(html_)}</div>'
        if kind == "cycle":
            out += f'<div class="cycle-back"><span class="cb-label">{inline(back)}</span></div>'
        return f'<div class="fig">{out}{figcite(cites)}</div>'
    if kind == "stack":
        items = [x.strip() for x in spec.split("->") if x.strip()]
        down = '<div class="down" aria-hidden="true">▼</div>'
        boxes = down.join(f'<div class="box{" hi" if x.startswith("*") else ""}">{inline(x.lstrip("*").strip())}</div>' for x in items)
        return f'<div class="fig"><div class="stack">{boxes}</div>{figcite(cites)}</div>'
    if kind == "grid":
        items = [x.strip() for x in split_outside_math(spec, "|") if x.strip()]
        cards = []
        for x in items:
            t, _, d = x.partition("::")
            cards.append(f'<div class="card"><div class="ct">{inline(t.strip())}</div>' + (f'<div class="cd">{inline(d.strip())}</div>' if d.strip() else "") + "</div>")
        return f'<div class="fig"><div class="grid" style="--n:{len(cards)}">{"".join(cards)}</div>{figcite(cites)}</div>'
    if kind == "ladder":
        items = [x.strip() for x in spec.split("||")]
        rows = ['<div class="axis"></div>']
        for k, x in enumerate(items):
            rows.append(f'<div class="{"gap" if k % 2 else "lvl"}">{inline(x)}</div>')
        return f'<div class="fig"><div class="ladder">{"".join(rows)}</div>{figcite(cites)}</div>'
    if kind == "curve":
        xl, yl, ml = (inline(x.strip()) for x in (spec.split("||") + ["", "", ""])[:3])
        svg = ('<svg viewBox="0 0 400 230" preserveAspectRatio="none" aria-hidden="true">'
               '<path d="M40 10 V200 H390" fill="none" stroke="#8f8a82" stroke-width="2"/>'
               '<path d="M70 30 C120 190, 200 192, 215 192 S320 150, 375 40" fill="none" stroke="#2f5d8a" stroke-width="4"/>'
               '<line x1="214" y1="192" x2="214" y2="200" stroke="#c0793a" stroke-width="3"/>'
               '<circle cx="214" cy="190" r="7" fill="#c0793a"/></svg>')
        return (f'<div class="fig"><div class="curve">{svg}'
                f'<div class="lab" style="left:52px;top:-6px">{yl}</div>'
                f'<div class="lab" style="right:4px;bottom:34px">{xl}</div>'
                f'<div class="lab" style="left:53.5%;bottom:-30px;transform:translateX(-50%);color:#c0793a">{ml}</div>'
                f'</div>{figcite(cites)}</div>')
    if kind == "chain":
        items = [x.strip() for x in split_outside_math(spec, "|") if x.strip()]
        steps = []
        for n, x in enumerate(items, 1):
            tag, _, text = x.partition("::")
            tag = tag.strip()
            hi = tag.startswith("!")  # 「!」標記：這一步引入近似（橘色）
            tag = tag.lstrip("!")
            steps.append(f'<div class="step{" approx" if hi else ""}"><span class="no">{n}</span>'
                         f'<span class="tag">{esc(tag)}</span><span>{inline(text.strip())}</span></div>')
        return f'<div class="fig"><div class="chain">{"".join(steps)}</div>{figcite(cites)}</div>'
    return f"<p>{inline(spec)}</p>"


def render_body(body):
    lines = body.splitlines()
    title, key, blocks = "", "", []
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if not s:
            i += 1
            continue
        if s.startswith("# "):
            title = s[2:].strip()
        elif s.startswith("> "):
            key = s[2:].strip()
        elif s.startswith("$$"):
            buf = [s[2:]]
            while not buf[-1].rstrip().endswith("$$") and i + 1 < len(lines):
                i += 1
                buf.append(lines[i])
            expr = "\n".join(buf).rstrip()[:-2].strip()
            blocks.append(f'<div class="math-block">$${esc(expr)}$$</div>')
        elif re.match(r"^(flow|stack|grid|cycle|ladder|curve|chain):", s):
            kind, spec = s.split(":", 1)
            blocks.append(component(kind, spec))
        elif s.startswith("- ") or re.match(r"^\d+\. ", s):
            ordered = not s.startswith("- ")
            items = []
            while i < len(lines) and (lines[i].strip().startswith("- ") if not ordered else re.match(r"^\d+\. ", lines[i].strip())):
                t = lines[i].strip()
                t = t[2:] if not ordered else re.sub(r"^\d+\.\s", "", t)
                items.append(f"<li>{inline(t)}</li>")
                i += 1
            tag = "ol" if ordered else "ul"
            blocks.append(f"<{tag}>{''.join(items)}</{tag}>")
            continue
        elif s.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in split_outside_math(lines[i].strip().strip("|"), "|")])
                i += 1
            head, data = rows[0], rows[2:]
            th = "".join(f"<th>{inline(c)}</th>" for c in head)
            trs = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in data)
            blocks.append(f'<table class="compare"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>')
            continue
        else:
            blocks.append(f"<p>{inline(s)}</p>")
        i += 1
    return title, key, blocks


def main():
    topic = Path(sys.argv[1])
    drafts = sorted((topic / "drafts").glob("[0-9][0-9]-*.md"))
    deck_title = "DFT Basics"
    slides = []
    for idx, d in enumerate(drafts, 1):
        fm, body = split_frontmatter(d.read_text(encoding="utf-8"))
        layout = (re.search(r"^layout:\s*(\S+)", fm, re.M) or [None, "bullets"])[1]
        cards = [c.strip() for c in re.search(r"^cards:\s*\[(.*)\]", fm, re.M).group(1).split(",")]
        CARDS[:] = cards
        title, key, blocks = render_body(body)
        if idx == 1:
            deck_title = title
        src = "".join(source_item(c) for c in cards)
        slides.append(f'''<section class="slide layout-{layout}" data-n="{idx}" aria-label="{esc(title)}">
  <header><span class="kicker">{idx:02d} / {len(drafts):02d}</span><h1>{inline(title)}</h1></header>
  {f'<div class="key">{inline(key)}</div>' if key else ''}
  <div class="body">{''.join(blocks)}</div>
  <footer><span class="src-label">Sources (CMP-wiki)</span>{src}<span class="credit"><a href="https://kumilz030.github.io/CMP-wiki/">CMP-wiki</a> · Computational Materials Physics 課程的非官方筆記（課程 © Stefaan Cottenier）</span></footer>
</section>''')
    template = (Path(__file__).parent / "deck_template.html").read_text(encoding="utf-8")
    out = template.replace("{{TITLE}}", esc(deck_title)).replace("{{SLIDES}}", "\n".join(slides))
    out = out.replace("{{COUNT}}", json.dumps(len(drafts)))
    (topic / "deck.html").write_text(out, encoding="utf-8")
    print(f"寫入 {topic / 'deck.html'}（{len(drafts)} 頁）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
