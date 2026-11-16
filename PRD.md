# CMP-wiki Product Requirements (PRD)

> 給人和 AI 一起看。寫「要做什麼、不做什麼、怎麼驗收」。規則細節在 `AGENTS.md`，操作步驟在 `.claude/skills/*/SKILL.md`，網站外觀在 `DESIGN.md`。
> 狀態：v0.2（2026-11-16，使用者確認；標題改英文）

## 1. Background and goals

- 來源：Stefaan Cottenier 的免費線上課程 *Computational Materials Physics*（https://www.compmatphys.org/courses/compmatphys/），內容是 Density Functional Theory（DFT）的理論，以及用 Quantum ESPRESSO 做的實作。
- 目標：把課程消化成**互相連結的繁中筆記網路**，用來：
  1. 複習理論（定理、近似、方程式及其成立條件）；
  2. 查實作步驟與參數意義（k-mesh、cutoff、收斂測試）；
  3. 看出概念之間的邏輯關係（例如 Hohenberg-Kohn → Kohn-Sham → XC functional）。
- 架構沿用 mse-wiki（pchem → nma → mse 的演變），差別在於：**這次要公開發布**，而且來源是講義加影片，不是課本。

## 2. Users

| 誰 | 需求 |
|---|---|
| 我（化工背景，另有 pchem-wiki、mse-wiki、nma-wiki） | 修課複習、查公式、練實作 |
| 公開網站的讀者 | 用中文快速理解 DFT 概念，並回到原課程看完整內容 |
| AI（Claude Code 等） | 依 `AGENTS.md` 與 skills 維護 wiki |

## 3. Scope

### Phase 1 (pilot): in scope
- 單元 **setting the stage**（AW01B–AW01H）與 **density functional theory**（AW02A–AW03H），包括兩個 optional 主題（basis sets in more depth、back to the teaser）。
- 每個有頁碼代號的主題一個來源頁，概念、方程式、推導依規則分頁。
- 對應的 **let's play**（w1–w3）寫成實作頁；有公開答案的測驗（例如 `AW02F_external-potential_answer-quiz.pdf`）寫成習題頁。
- 建立 repo、規則、範本、lint、hook、skills，以及 GitHub Pages 的自動建置。

### Later
- 其他單元：crystallography、geometry optimization、electronic structure、chemical bonding、elasticity、supercells and surfaces、precision and accuracy、magnetism、phonons、band gaps。等第一階段驗收後，一次加一個單元。

### Out of scope
- webinar（每週直播的錄影與簡報）、project、FAQ、quick start、HPC info（Flanders only）、about you、上傳作業的頁面。
- Google Form 測驗（exit、let's play 的回報表單）：抓不到題目，也不是公開答案。
- **不重新發布原站的著作**：不放講義 PDF、講義截圖、影片，也不轉錄或翻譯整段原文（見 §5）。

## 4. Sources and acquisition

| 來源 | 數量（第一階段） | 怎麼用 |
|---|---|---|
| 主題頁的講義 PDF（`AWxxY_*_handouts.pdf`） | 約 25 份 | 主要內容依據。放進 `raw/`，逐頁擷取文字到 `raw/text/` |
| 主題頁的網頁文字 | 約 30 頁 | 存成 `raw/pages/AWxxY.md`，記錄頁碼代號、預估時間、影片與講義連結 |
| 影片字幕 | Vimeo 講課影片**沒有字幕**（2026-11-16 用 yt-dlp 確認 134603738、182979806）；YouTube 影片只有自動字幕 | 有字幕就抓進 `raw/subs/`，標記為自動字幕、可信度低，只能當輔助，不能當唯一出處 |
| 外部參考（例如 Mattson 2002 *Science*、Kieron Burke 的講座） | 少數 | 原站有引用才列；內容寫進「補充說明」並附原始連結 |

`raw/` **不進 git**（`.gitignore`），只留在本機。

## 5. Public release and copyright

- 原站只標示 "free and open online course" 與 "© Stefaan Cottenier"，查不到 Creative Commons 授權（2026-11-16）。因此公開版本採 **「自己寫的筆記，加上原站連結」**：
  - 頁面內容用自己的話重新整理，不逐句翻譯講義；直接引用原文時，每段不超過一句，並且加引號、標出處。
  - 方程式可以寫（屬於學科內容），但推導要用自己的步驟和說明。
  - 圖片只放自己畫的（Mermaid、SVG、程式產生的圖），不放講義或影片截圖。
  - 每個來源頁與概念頁都附原站主題頁連結；網站 footer 標示課程出處與作者。
- 之後如果作者授權，再評估是否放寬。

## 6. Deliverables

| 檔案／資料夾 | 內容 |
|---|---|
| `README.md` | 給人看：專案介紹、本機預覽、部署 |
| `AGENTS.md` | 給 AI：規則（頁面類型、寫作、引用、公開限制）。`CLAUDE.md` 只匯入它 |
| `.claude/skills/*/SKILL.md` | 操作步驟：`ingest-topic`（匯入）、`query`（問答）、`lint`（健檢）、`publish`（發布） |
| `PRD.md` | 本檔 |
| `DESIGN.md` | 網站的顏色、字體、間距、元件樣式 |
| `wiki/`、`index.md`、`log.md`、`templates/`、`scripts/` | 同 mse-wiki |
| `.github/workflows/deploy.yml`、`.quartz/` | 用 Quartz 建置，部署到 GitHub Pages |

## 7. Acceptance criteria (phase 1)

1. `python3 scripts/lint.py` 0 錯誤：沒有壞連結、重複頁名或孤兒頁，引用的講義頁碼在 `raw/text/` 查得到，`sources:` 與內文一致。
2. 兩個單元每個有頁碼代號的主題都有來源頁；每份講義裡**被定義或實質討論**的概念都有歸屬頁。
3. 每條方程式頁都有「Conditions of validity」。
4. 公開檢查（lint 執行）：
   - `wiki/` 裡沒有來自 `raw/` 的圖片；
   - 沒有超過一句的引號原文；
   - 每個來源頁都有原站連結。
5. GitHub Actions 建置成功，網站上能看到 index、單元頁、數學式（KaTeX）、圖譜與搜尋。
6. 用 `wiki/綜合/knowledge base test questions` 的 10 題測試問答，記錄通過數。

## 8. Milestones

| 階段 | 內容 | 完成條件 |
|---|---|---|
| M0 建庫 | git、`.gitignore`、`AGENTS.md`、範本、lint、hook、skills、`README.md`、`DESIGN.md` | lint 能在空 wiki 上執行 |
| M1 setting the stage | AW01B–AW01H、let's play w1 | 驗收條件 1–4 |
| M2 DFT | AW02A–AW03H、optional、let's play w2–w3 | 驗收條件 1–4 |
| M3 發布 | 建立 GitHub repo `CMP-wiki`、設定 Pages、第一次部署 | 驗收條件 5–6；**push 與公開前先問我** |

## 9. Open issues

- [ ] 原站有些主題頁抓不到影片（例如 the creation of materials from thought、the Schrödinger equation），可能是延遲載入，匯入時要用瀏覽器再確認一次。
- [ ] 網站網址：用 `kumilz030.github.io/CMP-wiki` 還是自訂網域。
- [ ] 要不要寫信請作者授權（目前不需要）。
