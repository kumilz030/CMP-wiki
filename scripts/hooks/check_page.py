#!/usr/bin/env python3
"""PostToolUse hook：寫完 wiki/ 的頁面後跑單頁檢查，有錯就回報給 AI（exit 2）。"""
import json
import os
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[2]  # 不用 CLAUDE_PROJECT_DIR：搬資料夾後它可能還指向舊位置
data = json.load(sys.stdin)
fp = (data.get("tool_input") or {}).get("file_path", "")
if not fp.endswith(".md"):
    sys.exit(0)
p = Path(fp) if Path(fp).is_absolute() else Path(data.get("cwd", root)) / fp
try:
    p.resolve().relative_to(root / "wiki")
except ValueError:
    sys.exit(0)
r = subprocess.run([sys.executable, str(root / "scripts/lint.py"), "--file", str(p)], capture_output=True, text=True)
if r.returncode:
    print("單頁檢查發現問題，請修正：\n" + r.stdout + r.stderr, file=sys.stderr)
    sys.exit(2)
sys.exit(0)
