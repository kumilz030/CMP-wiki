#!/usr/bin/env python3
"""從原站抓主題頁、講義 PDF 與字幕到 raw/（只新增、不覆蓋；AGENTS.md §1）。

用法：
  python3 scripts/fetch_topic.py --list                      # 列出單元與主題（slug）
  python3 scripts/fetch_topic.py --unit setting-the-stage    # 抓整個單元
  python3 scripts/fetch_topic.py --topic kohn-sham-equations # 抓單一主題（可重複）
  加 --no-subs 不抓字幕；加 --dry-run 只列出會抓什麼；加 --refresh-pages 重寫主題頁摘要（講義與字幕仍然不覆蓋）。

輸出：
  raw/pages/<slug>.md      主題頁的代號、預估時間、影片與講義連結、頁面文字
  raw/<原檔名>.pdf          講義（保留原站檔名）
  raw/subs/<slug>_<影片id>.<lang>.vtt   影片字幕（有才會有；YouTube 多半是自動字幕）
"""
import argparse
import html
import re
import shutil
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
COURSE = "https://www.compmatphys.org/courses/compmatphys/"
UA = "Mozilla/5.0 (compatible; cmp-wiki-fetch)"
DELAY = 0.5


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def course_outline():
    """回傳 [(lesson_slug, [topic_slug, ...]), ...]，依原站順序。"""
    s = get(COURSE).decode("utf-8", "ignore")
    out, seen = [], set()
    for kind, slug in re.findall(r'href="https://www\.compmatphys\.org/(lessons|topics)/([^"/]+)/?"', s):
        if kind == "lessons":
            if not out or out[-1][0] != slug:
                out.append((slug, []))
        elif out and slug not in seen:
            seen.add(slug)
            out[-1][1].append(slug)
    return out


def text_of(fragment):
    fragment = re.sub(r"<(script|style)\b.*?</\1>", "", fragment, flags=re.S)
    fragment = re.sub(r"<br\s*/?>|</p>|</li>|</h\d>", "\n", fragment)
    t = html.unescape(re.sub(r"<[^>]+>", " ", fragment))
    lines = [re.sub(r"[ \t]+", " ", l).strip() for l in t.splitlines()]
    return "\n".join(l for l in lines if l)


def clean_text(t):
    """去掉 tag 殘片，並在討論區之前截斷：討論區有其他學員的帳號與 email，不可保存（AGENTS.md §6-5）。"""
    t = re.sub(r'^[^\n]*id="ld-tab-content-\d+">\n?', "", t)
    cut = re.search(r"^Home › Forums", t, re.M)
    return t[:cut.start()].rstrip() if cut else t


def parse_topic(slug):
    url = f"https://www.compmatphys.org/topics/{slug}/"
    s = get(url).decode("utf-8", "ignore")
    title = html.unescape((re.search(r"<title>(.*?)</title>", s, re.S) or [None, slug])[1]).split(" - compmatphys")[0].strip()
    i = s.find('class="ld-tab-content')  # 主題內容的 tabpanel（之前是 CSS 與側欄目錄）
    j = s.rfind("ld-content-actions")  # 第一個是頂端導覽，內容在最後一個之前
    body = s[i:j] if i > 0 else s
    code = re.search(r"page code ([A-Z]{2}\d{2}[A-Z])", body)
    etime = re.search(r"expected time:\s*([^<]+)", body)
    frames = [html.unescape(u) for u in re.findall(r'<iframe[^>]+?(?:data-src|src)="([^"]+)"', body) if "about:blank" not in u]
    videos = [u for u in frames if "vimeo" in u or "youtube" in u]
    # Elementor 影片元件把網址放在 data-settings 的 JSON 裡，不是 iframe
    flat = html.unescape(body).replace("\\/", "/").replace("\\", "")
    for yid in re.findall(r'youtube_url":"https://www\.youtube\.com/watch\?v=([A-Za-z0-9_-]{6,})', flat):
        videos.append(f"https://www.youtube.com/embed/{yid}")
    for vid in re.findall(r'(?:vimeo_url":"https://vimeo\.com/|vimeo\.com/external/)(\d{6,})', flat):
        videos.append(f"https://player.vimeo.com/video/{vid}")
    videos = list(dict.fromkeys(videos))
    pdfs = sorted({html.unescape(u) for u in re.findall(r'href="([^"]+\.pdf)"', body)})
    return {
        "slug": slug, "url": url, "title": title,
        "code": code.group(1) if code else None,
        "time": etime.group(1).strip() if etime else None,
        "videos": videos, "forms": [u for u in frames if "docs.google.com/forms" in u],
        "pdfs": pdfs, "text": clean_text(text_of(body)),
    }


def video_url(u):
    m = re.search(r"vimeo\.com/video/(\d+)", u)
    if m:
        return m.group(1), f"https://player.vimeo.com/video/{m.group(1)}"
    m = re.search(r"youtube\.com/embed/([A-Za-z0-9_-]{6,})", u)
    if m and m.group(1) != "live_stream":
        return m.group(1), f"https://www.youtube.com/watch?v={m.group(1)}"
    return None, None


def fetch_subs(slug, videos, dry):
    if not shutil.which("yt-dlp"):
        print("  （沒有 yt-dlp，略過字幕）")
        return
    subs = RAW / "subs"
    for v in videos:
        vid, url = video_url(v)
        if not vid:
            continue
        if list(subs.glob(f"{slug}_{vid}.*")):
            print(f"  字幕已存在：{vid}")
            continue
        if dry:
            print(f"  [dry-run] 字幕 {url}")
            continue
        subs.mkdir(parents=True, exist_ok=True)
        r = subprocess.run(
            ["yt-dlp", "--skip-download", "--write-subs", "--write-auto-subs", "--sub-langs", "en.*,en",
             "--sub-format", "vtt", "--ignore-no-formats-error", "--referer", "https://www.compmatphys.org/",
             "-o", str(subs / f"{slug}_{vid}.%(ext)s"), url],
            capture_output=True, text=True, timeout=180,
        )
        got = list(subs.glob(f"{slug}_{vid}.*"))
        print(f"  字幕 {vid}：{', '.join(p.name for p in got) if got else '無（' + (r.stderr.strip().splitlines() or ['no subtitles'])[-1][:80] + '）'}")
        time.sleep(DELAY)


def fetch(slug, subs, dry, refresh=False):
    t = parse_topic(slug)
    time.sleep(DELAY)
    print(f"- {slug}  code={t['code']}  time={t['time']}  videos={len(t['videos'])}  pdfs={len(t['pdfs'])}")
    page = RAW / "pages" / f"{slug}.md"
    if page.exists() and not refresh:
        print("  主題頁已存在，不覆蓋")
    elif dry:
        print(f"  [dry-run] 寫 {page.relative_to(ROOT)}")
    else:
        page.parent.mkdir(parents=True, exist_ok=True)
        lines = [f"# {t['title']}", "", f"- url: {t['url']}", f"- code: {t['code'] or '（無）'}",
                 f"- expected time: {t['time'] or '（無）'}", "- videos:"]
        lines += [f"  - {v}" for v in t["videos"]] or ["  - （無）"]
        lines += ["- pdfs:"] + ([f"  - {p}" for p in t["pdfs"]] or ["  - （無）"])
        lines += ["- forms:"] + ([f"  - {f}" for f in t["forms"]] or ["  - （無）"])
        lines += ["", "## Page text", "", t["text"], ""]
        page.write_text("\n".join(lines), encoding="utf-8")
    for u in t["pdfs"]:
        dest = RAW / Path(urllib.request.url2pathname(u.split("/")[-1])).name
        if dest.exists():
            print(f"  講義已存在：{dest.name}")
            continue
        if dry:
            print(f"  [dry-run] 下載 {u}")
            continue
        try:
            data = get(u.replace("http://", "https://", 1))
        except Exception as e:  # noqa: BLE001
            print(f"  ✗ 下載失敗 {u}：{e}")
            continue
        if not data.startswith(b"%PDF"):
            print(f"  ✗ 不是 PDF：{u}")
            continue
        RAW.mkdir(exist_ok=True)
        dest.write_bytes(data)
        print(f"  講義：{dest.name}（{len(data) // 1024} KB）")
        time.sleep(DELAY)
    if subs:
        fetch_subs(slug, t["videos"], dry)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--unit")
    ap.add_argument("--topic", action="append", default=[])
    ap.add_argument("--no-subs", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--refresh-pages", action="store_true", help="重寫主題頁摘要（講義與字幕仍然不覆蓋）")
    a = ap.parse_args()
    outline = course_outline()
    if a.list:
        for i, (lesson, topics) in enumerate(outline):
            print(f"[{i:02d}] {lesson}")
            for tp in topics:
                print(f"     {tp}")
        return 0
    slugs = list(a.topic)
    if a.unit:
        match = [t for l, t in outline if l == a.unit]
        if not match:
            print(f"找不到單元 {a.unit}；用 --list 查看", file=sys.stderr)
            return 1
        # PRD §3「Out of scope」：webinar、exit、project 相關主題不抓；要抓請用 --topic 明確指定
        skip = re.compile(r"^(webinar|exit|for-project|only-for-project|upload-your-answer)")
        slugs += [s for s in match[0] if not skip.match(s)]
    if not slugs:
        ap.print_help()
        return 1
    for s in slugs:
        fetch(s, not a.no_subs, a.dry_run, a.refresh_pages)
    return 0


if __name__ == "__main__":
    sys.exit(main())
