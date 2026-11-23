#!/usr/bin/env python3
"""關卡 9：渲染檢查。用 headless Chrome 打開 deck.html?check=1，讀出每一頁的量測結果：
垂直／水平溢出、太寬的數學式、KaTeX 錯誤、沒渲染的 $。不改任何檔案。

用法：
  python3 scripts/slides/render_check.py slides/topic-<slug>              # 檢查
  python3 scripts/slides/render_check.py slides/topic-<slug> --shots DIR  # 另外逐頁截圖到 DIR（給人或 AI 看版面）
需要 google-chrome（或用環境變數 CHROME 指定）。有問題時 exit 1。
"""
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

CHROME = os.environ.get("CHROME") or shutil.which("google-chrome") or shutil.which("chromium")
FLAGS = ["--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars", "--window-size=1280,720"]


def dump(url):
    r = subprocess.run([CHROME, *FLAGS, "--virtual-time-budget=15000", "--dump-dom", url],
                       capture_output=True, text=True, timeout=120)
    m = re.search(r'<pre id="check-result">(.*?)</pre>', r.stdout, re.S)
    return json.loads(m.group(1).replace("&quot;", '"').replace("&amp;", "&")) if m and m.group(1).strip() else None


def main():
    topic = Path(sys.argv[1]).resolve()
    if not CHROME:
        print("找不到 google-chrome／chromium", file=sys.stderr)
        return 2
    deck = topic / "deck.html"
    res = dump(deck.as_uri() + "?check=1")
    if res is None:
        print("✗ 讀不到檢查結果（頁面腳本沒有執行完）")
        return 1
    bad = [s for s in res["slides"] if s["issues"]]
    if not res.get("katex"):
        print("✗ KaTeX 沒有載入（需要網路連到 cdn.jsdelivr.net）")
    for s in bad:
        print(f"✗ slide {s['slide']:02d}: " + "; ".join(s["issues"]))
    print(f"共 {res['count']} 頁；有問題 {len(bad)} 頁" + ("（通過）" if not bad and res.get("katex") else ""))
    if "--shots" in sys.argv:
        out = Path(sys.argv[sys.argv.index("--shots") + 1])
        out.mkdir(parents=True, exist_ok=True)
        for n in range(1, res["count"] + 1):
            subprocess.run([CHROME, *FLAGS, "--virtual-time-budget=15000", f"--screenshot={out / f'slide-{n:02d}.png'}",
                            deck.as_uri() + f"?slide={n}"], capture_output=True, timeout=120)
        print(f"截圖：{out}")
    return 1 if bad or not res.get("katex") else 0


if __name__ == "__main__":
    sys.exit(main())
