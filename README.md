# CMP-wiki

Stefaan Cottenier 的免費線上課程 [*Computational Materials Physics*](https://www.compmatphys.org/courses/compmatphys/)（Density Functional Theory 與 Quantum ESPRESSO 實作）的**個人中文筆記**，整理成互相連結的 wiki。

- 內容以繁體中文說明，專有名詞保留英文。
- 這是**非官方**筆記：依據課程講義用自己的話整理，不含原站的講義、影片或截圖。完整內容請到原站閱讀。
- 網站：https://kumilz030.github.io/CMP-wiki/

## What is inside

| 路徑 | 內容 |
|---|---|
| `index.md` | 目錄，也是網站首頁 |
| `wiki/概念/UNN/` | 概念頁，依單元分資料夾（U01 setting the stage、U02 density functional theory…） |
| `wiki/方程式/`、`wiki/推導/` | 方程式（含成立條件）與推導 |
| `wiki/邏輯鏈/` | 「為什麼可以這樣做」的推理鏈，例如 Hohenberg-Kohn → Kohn-Sham |
| `wiki/實作/`、`wiki/習題/` | Quantum ESPRESSO 實作筆記、有公開答案的測驗 |
| `wiki/來源/` | 每個課程主題（頁碼代號如 AW03C）一頁，附原站連結 |
| `wiki/綜合/` | 方程式總表、符號對照、測試題 |

目前進度見 `log.md`；範圍與里程碑見 `PRD.md`。

## Preview locally

需要 Node.js 22 以上與 git。

```bash
bash .quartz/build.sh --serve
```

打開 http://localhost:8080 。只建置不預覽時，拿掉 `--serve`，輸出會放在 `.quartz/public/`。

在 Obsidian 裡直接把這個資料夾當成 vault 打開也可以閱讀。

## Deploy

push 到 `main` 後，GitHub Actions（`.github/workflows/deploy.yml`）會：

1. 執行 `scripts/lint.py`；
2. 用 Quartz 建置網站；
3. 部署到 GitHub Pages。

第一次部署前，要到 repo Settings → Pages → Source 選 **GitHub Actions**。

## Maintaining (for contributors and AI)

- 規則：`AGENTS.md`（Claude Code 透過 `CLAUDE.md` 讀取）
- 操作步驟：`.claude/skills/`（ingest-topic、query、lint、publish）
- 網站外觀：`DESIGN.md`
- 原始資料（講義 PDF 等）放在本機的 `raw/`，**不進 git**。需要時用 `python3 scripts/fetch_topic.py` 從原站抓取。

Python 腳本需要 `pyyaml`；抓字幕需要 `yt-dlp`；擷取講義文字需要 `pdftotext`（poppler-utils）。

## Credits

課程內容 © Stefaan Cottenier，[compmatphys.org](https://www.compmatphys.org/)。本 repo 只是學習筆記，所有錯誤都屬於筆記作者。
