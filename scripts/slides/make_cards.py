#!/usr/bin/env python3
"""節點 3：證據卡。sources.md 的每一頁 wiki 產生一張卡，卡片只含那一頁、而且只含有出處的段落。

- 照原文複製，不改寫；去掉「Supplementary notes (not from source)」與圖（Mermaid），
  所以簡報只能用到有講義出處的內容。
- 每張卡互相獨立（可以平行產生），一張卡只看一頁。

用法：python3 scripts/slides/make_cards.py slides/topic-<slug>
"""
import re
import sys
from pathlib import Path

from common import ROOT, listed_pages, sections, site_url, split_frontmatter, wiki_pages

KEEP = {
    "概念": ["Definition", "Mathematical form", "Physical meaning", "Validity and common misconceptions", "Conflicts and differences"],
    "方程式": ["Equation", "Conditions of validity", "Origin", "How to use", "Common mistakes", "Conflicts and differences"],
    "推導": ["Goal", "Starting point and assumptions", "Derivation", "Result", "Where each assumption enters"],
    "邏輯鏈": ["Question", "Steps", "Limitations", "Conflicts and differences"],
}


def card_for(name, path):
    fm, body = split_frontmatter(path.read_text(encoding="utf-8"))
    t = re.search(r"^type:\s*(\S+)", fm, re.M)
    ptype = t.group(1) if t else ""
    alias = re.search(r"^aliases:\s*\[(.*)\]", fm, re.M)
    secs = sections(body)
    if ptype in KEEP:
        keep = [(k, secs.get(k, "")) for k in KEEP[ptype]]
    else:  # 綜合頁：全部段落
        keep = list(secs.items())
    lines = [
        f"# Card: {name}",
        "",
        f"- wiki: `{path.relative_to(ROOT).as_posix()}`（type: {ptype or '綜合'}）",
        f"- 網站：{site_url(path)}",
        f"- aliases: {alias.group(1) if alias else ''}",
        "",
    ]
    for title, text in keep:
        text = re.sub(r"```mermaid.*?```\n?(自繪[^\n]*\n?)?", "", text, flags=re.S).strip()
        if text and text not in ("無", "- 無"):
            lines += [f"## {title}", text, ""]
    return "\n".join(lines).rstrip() + "\n"


def main():
    topic = Path(sys.argv[1])
    out = topic / "cards"
    out.mkdir(exist_ok=True)
    known = wiki_pages()
    n = 0
    for name in listed_pages(topic / "sources.md"):
        (out / f"{name}.md").write_text(card_for(name, known[name]), encoding="utf-8")
        n += 1
    print(f"寫入 {n} 張證據卡到 {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
