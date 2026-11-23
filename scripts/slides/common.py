"""topic-slides 流程共用的小工具（.agents/workflows/topic-slides.md）。"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WIKI = ROOT / "wiki"
SITE = "https://kumilz030.github.io/CMP-wiki/"
LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")


def wiki_pages():
    """頁名 → 檔案路徑（全庫頁名唯一，AGENTS.md §2）。"""
    return {p.stem: p for p in WIKI.rglob("*.md")}


def site_url(path: Path) -> str:
    """wiki 檔案在 Quartz 網站上的網址（空白換成 -）。"""
    rel = path.relative_to(WIKI).with_suffix("").as_posix()
    return SITE + rel.replace(" ", "-")


def listed_pages(sources_md: Path):
    """sources.md 中以 [[頁名]] 列出的頁，保持順序、不重複。"""
    seen, out = set(), []
    for m in LINK_RE.finditer(sources_md.read_text(encoding="utf-8")):
        name = m.group(1).strip()
        if name not in seen:
            seen.add(name)
            out.append(name)
    return out


def split_frontmatter(text: str):
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            return text[4:end], text[end + 4:].lstrip("\n")
    return "", text


def sections(body: str):
    """## 標題 → 內容。"""
    out, cur, buf = {}, None, []
    for line in body.splitlines():
        if line.startswith("## "):
            if cur is not None:
                out[cur] = "\n".join(buf).strip()
            cur, buf = line[3:].strip(), []
        elif cur is not None:
            buf.append(line)
    if cur is not None:
        out[cur] = "\n".join(buf).strip()
    return out
