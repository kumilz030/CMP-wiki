# CMP-wiki Schema

> 這份規則檔是寫給 AI 讀的。Claude Code 透過 `CLAUDE.md` 自動匯入它；其他 AI 請在第一句話就叫它先讀 `AGENTS.md`。
> 本檔只寫**規則**。匯入、問答、健檢、發布的**步驟**放在 `.claude/skills/*/SKILL.md`，遇到對應任務時才讀。範圍與驗收條件見 `PRD.md`，網站外觀見 `DESIGN.md`。
> 架構沿用 mse-wiki（2026-11-15 版）。規則出問題就加一條，並記進最下方的「修訂紀錄」。

## 0. What this wiki is

- 主題：Stefaan Cottenier 的線上課程 *Computational Materials Physics*（https://www.compmatphys.org/courses/compmatphys/），內容是 DFT 理論與 Quantum ESPRESSO 實作。
- 目標：把課程講義消化成互相連結的概念網路。**這個知識庫會公開發布**（GitHub Pages），因此 §6 的公開限制優先於其他所有規則。
- 使用者是化工背景的學生，另外有 pchem-wiki、mse-wiki、nma-wiki。說明文字用繁體中文，專有名詞一律用英文，每頁第一次出現時附上中文，例如：exchange-correlation functional（交換相關泛函）。

## 1. Three layers

| 資料夾 | 內容 | 進 git？ | 誰負責 |
|---|---|---|---|
| `raw/` | 講義 PDF（`AWxxY_*.pdf`，保留原站檔名）、`raw/pages/<slug>.md`（主題頁的代號、影片與講義連結、頁面文字；slug 是原站網址最後一段）、`raw/subs/`（影片字幕） | **否** | 用 `scripts/fetch_topic.py` 新增，只新增、不覆蓋。AI 不改、不刪、不搬（由 hook 擋下） |
| `raw/text/` | 講義逐頁文字：`raw/text/<PDF 檔名主幹>/p3.txt`（p 是 PDF 頁） | 否 | 只由 `scripts/extract_text.py` 產生 |
| `wiki/` | AI 寫的頁面，也是網站內容 | 是 | AI 撰寫與維護 |
| `AGENTS.md`、`PRD.md`、`DESIGN.md` | 規則、規格、外觀 | 是 | 使用者和 AI 一起修訂 |

`templates/` 放頁面範本；`index.md` 是目錄（同時是網站首頁）；`log.md` 是日誌；`scripts/` 放擷取與檢查腳本；`.quartz/` 放網站建置設定。

**頁碼代號**：原站每個主題有一個代號，例如 `AW03C`（第 03 週第 C 個主題）。全庫用這個代號識別來源。同一個主題有多份講義時（例如 `AW03A` 與 `AW03A-bis`），各自建一個來源頁。

## 2. Page types

頁名（檔名）用英文：小寫，專有名詞照慣例大寫（例如 `Kohn-Sham equations.md`、`Born-Oppenheimer approximation.md`）。中文名寫在 frontmatter 的 `aliases`。表示資料類型的中文前綴不改：`推導-`、`實作-`、`習題-`、`來源-`。**頁名全庫不可重複**（連結不帶路徑）。

| 子資料夾 | 類型 | 頁名範例 | 什麼時候開新頁 |
|---|---|---|---|
| `wiki/概念/UNN/` | 概念頁，依單元分資料夾（U01 setting the stage、U02 density functional theory，依原站單元順序編號） | `electron density` | 講義**定義或實質討論**時才開；只是順帶提到就不開 |
| `wiki/方程式/` | 有名字或會反覆用到的式子 | `Kohn-Sham equations`（若和概念頁撞名，方程式頁改名為 `Kohn-Sham equation (form)`） | 講義寫出式子並加以使用時 |
| `wiki/推導/` | 推導或證明 | `推導-first Hohenberg-Kohn theorem` | 講義有推導或證明（例如 AW03A-bis），或使用者要求 |
| `wiki/邏輯鏈/` | 跨概念的推理或計算流程（見 §2.3） | `HK theorems justify the Kohn-Sham scheme` | 講義建立了「因為 A，所以可以 B」的關係時 |
| `wiki/實作/` | let's play 與 hands-on 任務：目的、輸入檔重點、參數意義、預期結果 | `實作-w2 a basic calculation` | 每個納入範圍的 let's play 一頁 |
| `wiki/習題/` | 原站**公開答案**的測驗（answer-quiz PDF） | `習題-AW02F external potential quiz` | 有公開答案時 |
| `wiki/來源/` | 來源頁：每個頁碼代號一頁，兼作該主題的總覽 | `來源-AW03C` | 每次匯入都要寫 |
| `wiki/綜合/` | 方程式總表、符號對照、近似方法比較、問答存檔、測試題 | 英文主題名 | 好的問答結果或跨單元比較 |
| `wiki/補充/` | 課程以外的延伸整理 | 英文主題名 | 使用者要求時 |
| `wiki/附圖/` | **只放自己產生的圖**（見 §6） | 描述性英文檔名 | 需要圖時 |

同一類頁面的 `##` 標題層級與順序必須和範本一致（由 `lint.py` 檢查）。

### 2.1 Splitting pages
1. 講義投影片的**標題與粗體詞**決定哪些詞要有頁（自己一頁，或寫進某頁的 `aliases`）。
2. 同一張投影片一起定義的項目合成一頁；同義詞放進 `aliases`（例如 LDA / local density approximation）。
3. **開新頁前必須先搜尋**：`python3 scripts/lint.py --find 關鍵字`。搜到就擴充原頁，不開新頁。

### 2.2 Concept order and kind
- `order:` 是字串，格式 `"AW03C-KK"`，其中 KK 是同一個代號內依講義出現先後的兩位數序號。
- 每個單元資料夾放一個 `00 UNN concepts.base`（Obsidian Bases，依 `order` 排序）。
- `kind:` 只能選一個：

| kind | 意義 | 例 |
|---|---|---|
| `theorem` | 定理 | Hohenberg-Kohn theorems |
| `approximation` | 近似 | Born-Oppenheimer approximation、LDA |
| `method` | 理論方法或數值方法 | Hartree-Fock、plane-wave basis |
| `quantity` | 物理量或數學物件 | electron density、external potential |
| `concept` | 觀念、框架 | ab initio、functional |
| `parameter` | 計算參數 | k-mesh、cutoff energy |
| `tool` | 軟體、檔案格式 | Quantum ESPRESSO、CIF |

### 2.3 Logic chains
- 用來回答「為什麼可以這樣做」或「計算要按什麼順序做」。頁名寫成一句英文句子，不加前綴，`type: 邏輯鏈`。
- 「Steps」段每一步寫一行：`N. [[頁名]]（kind）：這一步說了什麼（出處）`，至少 3 步。
- 每一步都要有講義出處。講義沒有明講的銜接，寫進「Supplementary notes (not from source)」。

### 2.4 Frontmatter fields
- `topic:`：`index.md` 的分類名。`unit:`：`U01` 等。
- `order:`、`kind:`：只有概念頁需要。
- `code:`（只有來源頁）：頁碼代號；`url:`：原站主題頁網址；`raw:`：講義 PDF 檔名列表（lint 用它驗證引用的頁碼與引號原文）。
- `sources:`：列出內文**實際引用**的來源頁，一行一個，連結要加引號。
- `prereqs:`：要先懂的頁。跨單元或跨 wiki（pchem）的先備關係特別要寫。

## 3. Writing rules

1. **每個實質說法都要有出處**，寫在句末：
   - 講義：`（[[來源-AW03C]] p.4）`，p 是講義 PDF 的頁數；
   - 影片字幕：`（[[來源-AW02A]] 影片 03:15，自動字幕）`；
   - 主題頁文字：`（[[來源-AW03C]] 主題頁）`。
   - 找不到出處的內容標 `⚠️待查證`，不要自己補。
2. **不加料**：不加入來源沒有的數值、例子或結論。依一般知識補充的內容放在「Supplementary notes (not from source)」。
3. **數學式一律用 LaTeX**：行內用 `$...$`，獨立式用 `$$...$$`。符號第一次出現要說明意義與單位，並說明使用的單位制（Hartree 原子單位、Rydberg 或 SI；Quantum ESPRESSO 預設用 Ry）。
4. **符號一致**：全庫照講義的符號（$\rho(\vec r)$、$V_{ext}$、$E_{xc}$、$\hat H$…）；有不一致的地方列在 [[symbols]]。
5. **每條方程式都要寫「Conditions of validity」**，例如：Born-Oppenheimer、非相對論、基態（ground state）、自旋未極化、週期性邊界條件。
6. **連結**：一律用不帶路徑的 `[[頁名]]`。每頁至少連到一個上層概念和一個相關頁。
7. **矛盾不覆蓋**：寫進「Conflicts and differences」，並列不同說法與出處；更正時保留原說法，並註明原因與日期。
8. **一頁一個主題**：正文超過約 800 字，或包含兩個可以獨立查詢的主題，就考慮拆頁。
9. **英文規則**：課名、主題名照原文；頁名用英文；英文和中文之間空一格。
10. **對照頁面影像**：方程式、向量符號、上下標、表格一律對照 PDF 頁面影像（用 Read 看 PDF 該頁），文字擷取只用來搜尋與驗證。
11. **所有標題用英文**：頁面與文件裡的 `#`、`##`、`###` 標題一律用英文（範本已定好 `##` 標題）；標題底下的內容用繁中說明＋英文術語。資料夾名、`type:` 值與頁名的中文前綴（`來源-` 等）不算標題，維持原樣。

## 4. Actions

| 使用者說 | 讀哪個 skill |
|---|---|
| 「匯入 AWxxY」「做 U02」 | `.claude/skills/ingest-topic/SKILL.md` |
| 問問題 | `.claude/skills/query/SKILL.md` |
| 「健檢」 | `.claude/skills/lint/SKILL.md` |
| 「發布」「部署」 | `.claude/skills/publish/SKILL.md` |

**每個動作結束時都要做**：
1. 執行 `python3 scripts/lint.py`，錯誤要修到 0；
2. 在 `log.md` 最後加一行；
3. 依 §7 commit。

## 5. index.md and log.md

- `index.md`：依單元，再依主題分類，每頁一行：`- [[頁名]]（中文）：一句話摘要`。
- `log.md`：只往後加，不改舊紀錄。格式：`## [YYYY-MM-DD] ingest|query|lint|publish|setup | 摘要`。query 行要註明讀了哪些頁、引用了哪些頁。

## 6. Public-release limits (override all other rules)

原站標示 © Stefaan Cottenier，沒有開放授權。所以：
1. **不放原站的檔案**：講義 PDF、截圖、影片、字幕全文都不能進 `wiki/`，也不能進 git。
2. **用自己的話寫**：不逐句翻譯講義。直接引用原文時，每處不超過一句，要加引號並標出處。
3. **圖片只放自己產生的**（Mermaid、SVG、腳本畫的圖），並在圖說寫明「自繪，依據 [[來源-xxx]] p.N」。
4. **每個來源頁都附原站連結**，網站 footer 標示課程出處。
5. 不放個人資料（包括使用者的姓名、email、帳號）。
6. `lint.py` 會檢查：`wiki/` 裡有沒有來自 `raw/` 的檔案、有沒有長段引號原文、來源頁有沒有 `url:`。

## 7. Git and publishing

- 每個動作開始前記下當下的 commit；結束時 commit，訊息和 log.md 那一行一致，並附上起點，例如 `ingest: 來源-AW03C（起點 2c8dd5c）`。
- commit 只 stage AI 自己改的路徑。動手前先看 `git status`。**使用者手動做的修改優先保留**，不要還原。
- **不改寫 git 歷史。push 前要先問使用者**（push 會觸發公開部署）。

## 8. Automatic checks (Claude Code hooks)

`.claude/settings.json` 有兩個 hook：
- 寫入前：擋下對 `raw/` 的修改（`fetch_topic.py`、`extract_text.py` 除外），也擋下把 `raw/` 的檔案複製到 `wiki/`、`git add -f raw/`。Bash 指令裡只要同一段同時出現修改型指令和 `raw/` 字樣就會擋（包括字串內容），要在文件裡寫到 `raw/` 時改用 Edit/Write。
- hook 指令用 `git rev-parse --show-toplevel` 找腳本，腳本用自己的位置找 repo 根目錄，不依賴 `CLAUDE_PROJECT_DIR`（session 換資料夾後它可能還指向舊位置，2026-11-16 實測）。
- 寫入後：對剛寫完的 `wiki/` 頁面跑單頁 lint。

## 9. Relation to other wikis

- 和 pchem-wiki 重疊的內容（Schrödinger equation、Hartree-Fock、量子數），以計算材料物理的角度寫，不重抄推導，只標「物化見 pchem-wiki 的 `頁名`」。
- 和 mse-wiki 重疊的內容（crystal structure、elastic constants），處理方式相同。

## Revision history
- 2026-11-16：初版草稿。沿用 mse-wiki 架構，改動如下：
  - 規則（AGENTS.md）和步驟（skills）分開；
  - 改成公開發布，新增 §6 公開限制，`raw/` 不進 git；
  - 出處從「課本頁碼」改成「頁碼代號＋講義頁」；
  - 依單元分資料夾；
  - `kind` 改成 DFT 適用的類型；
  - 機制鏈改成邏輯鏈；
  - 例題改成實作頁與習題頁。
- 2026-11-16：使用者要求所有標題用英文（§3-11），本檔、PRD 與範本的標題改成英文。
