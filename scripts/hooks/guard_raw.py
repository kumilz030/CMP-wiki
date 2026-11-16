#!/usr/bin/env python3
"""PreToolUse hook：保護 raw/，並防止原站檔案進入 wiki/（AGENTS.md §1、§6、§8）。exit 2 = 擋下並回報原因。

Bash 指令先依 ; && || | 換行切成片段，只有「同一個片段」裡同時有修改型指令和 raw/ 路徑才擋，
避免像「sed -i wiki/x.md; grep raw/text」這種讀 raw 的指令被誤擋。
放行：scripts/fetch_topic.py（只新增）、scripts/extract_text.py（產生 raw/text）。
"""
import json
import os
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[2]  # 不用 CLAUDE_PROJECT_DIR：搬資料夾後它可能還指向舊位置
data = json.load(sys.stdin)
tool = data.get("tool_name", "")
inp = data.get("tool_input", {}) or {}

MUTATING = re.compile(
    r"\b(rm|mv|touch|truncate|chmod|tee|mutool|pdfunite|pdfseparate|unlink|shred|rsync|ln)\b"
    r"|\bsed\s+-i|\bgit\s+(rm|mv|checkout|restore|add\s+-f)\b"
)
RAW_PATH = re.compile(r"(^|[\s'\"=/])raw/")
ALLOWED = ("scripts/fetch_topic.py", "scripts/extract_text.py")


def block(msg):
    print(f"已擋下：{msg}（AGENTS.md §1、§6：raw/ 只能由 fetch_topic.py／extract_text.py 新增；原站檔案不可進 wiki/ 或 git）", file=sys.stderr)
    sys.exit(2)


if tool in ("Edit", "Write", "MultiEdit", "NotebookEdit"):
    fp = inp.get("file_path") or inp.get("notebook_path") or ""
    p = Path(fp)
    if not p.is_absolute():
        p = Path(data.get("cwd", root)) / p
    try:
        p.resolve().relative_to(root / "raw")
        block(f"{tool} {fp}")
    except ValueError:
        pass
elif tool == "Bash":
    cmd = inp.get("command", "")
    for seg in re.split(r"&&|\|\||;|\||\n", cmd):
        if any(a in seg for a in ALLOWED) or not RAW_PATH.search(seg):
            continue
        if re.search(r">>?\s*['\"]?\S*raw/", seg):
            block(f"重新導向寫入 raw/：{seg.strip()[:120]}")
        m = re.match(r"\s*cp\b(.*)", seg)
        if m:
            args = m.group(1).split()
            if args and ("raw/" in args[-1] or "wiki/" in args[-1]):
                block(f"從 raw/ 複製或複製到 raw/：{seg.strip()[:120]}")
            continue
        if MUTATING.search(seg):
            block(f"Bash 指令可能修改 raw/ 或把 raw/ 的檔案搬出：{seg.strip()[:120]}")
sys.exit(0)
