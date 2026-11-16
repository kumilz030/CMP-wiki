#!/usr/bin/env bash
# 建置 CMP-wiki 網站：下載固定版本的 Quartz，只放入 wiki/ 和 index.md（不含 raw/，AGENTS.md §6）
# 用法：bash .quartz/build.sh [--serve]
set -euo pipefail

QUARTZ_VERSION=v4.5.2
HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(dirname "$HERE")"
WORK="$HERE/.build"

if [ ! -d "$WORK/.git" ]; then
  rm -rf "$WORK"
  git clone -q --depth 1 --branch "$QUARTZ_VERSION" https://github.com/jackyzha0/quartz.git "$WORK"
fi
cp "$HERE/quartz.config.ts" "$HERE/quartz.layout.ts" "$WORK/"
cp "$HERE/custom.scss" "$WORK/quartz/styles/custom.scss"

rm -rf "$WORK/content"
mkdir -p "$WORK/content"
cp -r "$ROOT/wiki/." "$WORK/content/"
cp "$ROOT/index.md" "$WORK/content/index.md"
find "$WORK/content" \( -name '*.base' -o -name '.gitkeep' -o -name '*.pdf' \) -delete

cd "$WORK"
[ -d node_modules ] || npm ci --no-audit --no-fund
rm -rf "$HERE/public"
if [ "${1:-}" = "--serve" ]; then
  npx quartz build -o "$HERE/public" --serve
else
  npx quartz build -o "$HERE/public"
fi
