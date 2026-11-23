#!/usr/bin/env python3
"""關卡 2：覆蓋率。sources.md 列出的 wiki 頁都要存在，而且至少 3 頁，否則停下。

用法：python3 scripts/slides/coverage_check.py slides/topic-<slug>
"""
import sys
from pathlib import Path

from common import listed_pages, wiki_pages

MIN_PAGES = 3


def main():
    topic = Path(sys.argv[1])
    pages = listed_pages(topic / "sources.md")
    known = wiki_pages()
    missing = [p for p in pages if p not in known]
    found = [p for p in pages if p in known]
    print(f"sources.md 列出 {len(pages)} 頁，wiki 中存在 {len(found)} 頁")
    for p in missing:
        print(f"  ✗ 不存在：[[{p}]]")
    if missing:
        print("結果：退回檢索（sources.md 有不存在的頁）")
        return 1
    if len(found) < MIN_PAGES:
        print(f"結果：停下（相關頁少於 {MIN_PAGES} 頁，wiki 內容不足以做簡報）")
        return 1
    print("結果：通過")
    return 0


if __name__ == "__main__":
    sys.exit(main())
