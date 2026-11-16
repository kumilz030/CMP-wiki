---
name: publish
description: 在本機預覽或發布 CMP-wiki 網站（Quartz → GitHub Pages）。使用者說「預覽」「發布」「部署」時使用。
---

# Preview and publish the site

網站只包含 `wiki/` 和 `index.md`（由 `.quartz/build.sh` 複製進 Quartz），`raw/` 不會、也不能進入網站或 git。

## Preview locally
```bash
bash .quartz/build.sh           # 產生 .quartz/public/
bash .quartz/build.sh --serve   # 建置並在 http://localhost:8080 預覽
```
用內建瀏覽器打開預覽，抽查：首頁、一個概念頁的數學式、搜尋、圖譜、footer 的課程出處，以及深色模式。

## Publish
1. `python3 scripts/lint.py` 必須 0 錯誤。
2. 再確認一次公開限制：`git ls-files | grep -iE '\.(pdf|vtt|srt)$|^raw/'` 必須沒有輸出。
3. **push 之前一定要問使用者**，說明這次會公開哪些新頁。得到同意才 `git push`。
4. push 到 `main` 後，GitHub Actions（`.github/workflows/deploy.yml`）會自動建置並部署到 GitHub Pages。在 repo 的 Actions 頁確認建置成功，再打開網站抽查。
5. `log.md` 加 `## [YYYY-MM-DD] publish | 摘要`。

## First-time setup (once)
- 在 GitHub 建立 repo `CMP-wiki`（使用者自己建立，或經使用者同意用 `gh repo create`）。
- repo Settings → Pages → Source 選 **GitHub Actions**。
- `.quartz/quartz.config.ts` 的 `baseUrl` 要和實際網址一致。
