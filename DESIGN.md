# CMP-wiki Design

> 給人和 AI 一起看。改網站外觀或新增頁面元件時先讀這份。實作在 `.quartz/quartz.config.ts`（顏色、字體）、`.quartz/quartz.layout.ts`（版面）、`.quartz/custom.scss`（細部樣式）。
> 和 pchem-wiki 用同一套 Quartz 版本（v4.5.2）與版面，但換一組顏色，讓兩個網站一眼就分得出來。

## 1. Principles

1. **內容優先**：沒有裝飾性圖片；版面只用來幫助閱讀方程式、出處與連結。
2. **出處看得到**：每頁最下方的 Sources 段、footer 的課程出處，任何寬度下都不能被隱藏。
3. **淺色與深色都要能讀**：每個顏色都有深色模式的對應值。
4. **手機能讀方程式**：長的 `$$` 式子可以左右捲動，不會撐破版面。

## 2. Colors

| Token（Quartz） | 用途 | Light | Dark |
|---|---|---|---|
| `light` | 頁面背景 | `#fbfaf7` | `#15171a` |
| `lightgray` | 邊框、表格線、程式碼背景 | `#e6e4df` | `#2c3036` |
| `gray` | 次要文字、日期、麵包屑 | `#8f8a82` | `#7a808a` |
| `darkgray` | 內文 | `#3f3d39` | `#d6d8dc` |
| `dark` | 標題、粗體 | `#1f1e1c` | `#eceef1` |
| `secondary` | 連結、強調色（藍：電子、波函數） | `#2f5d8a` | `#8db4dc` |
| `tertiary` | 滑過的連結、圖譜目前節點（橘：能量） | `#c0793a` | `#e0a36b` |
| `highlight` | 內部連結底色、行內強調 | `rgba(47, 93, 138, 0.10)` | `rgba(141, 180, 220, 0.12)` |
| `textHighlight` | `==螢光==` | `#f5d76e88` | `#8a6d1088` |

`⚠️待查證` 保留 emoji，不另外上色。

## 3. Typography

| 用途 | 字體 | 備註 |
|---|---|---|
| 標題 | Noto Sans TC | 標題一律英文（AGENTS.md §3-11） |
| 內文 | Noto Sans TC | 中英混排；英文和中文之間空一格 |
| 程式碼、輸入檔 | JetBrains Mono | Quantum ESPRESSO 輸入檔片段 |
| 數學 | KaTeX 預設 | 不改字體 |

- 內文行高 1.7；`##` 標題上方留 2rem、下方加一條 `lightgray` 細線，方便在長頁面中找段落。
- 表格字級比內文小一號（0.92em），表頭用 `lightgray` 底色。

## 4. Spacing and layout

- Quartz 三欄版面：左欄放站名、搜尋、深色模式、檔案樹；中間放內文；右欄放圖譜、目錄、反向連結。
- 寬度小於 800px 時只顯示中欄，左右欄收進選單（Quartz 預設行為）。
- 內文最大寬度沿用 Quartz 預設（約 750px）；`$$` 區塊設 `overflow-x: auto`。
- 頁面內文已經有 `#` 標題，所以不顯示 Quartz 的 ArticleTitle，避免標題重複（同 pchem-wiki）。

## 5. Components

| 元件 | 寫法 | 外觀 |
|---|---|---|
| 出處 | 句末 `（[[來源-AW03C]] p.4）` | 一般內部連結樣式 |
| 原站連結 | 來源頁 Basic info 與各頁 Sources 段的 `原站：<url>` | 外部連結，Quartz 會自動加上箭頭 |
| 自繪圖 | Mermaid 程式碼區塊；或 `wiki/附圖/` 的 SVG，下一行寫圖說「自繪，依據 [[來源-xxx]] p.N」 | Mermaid 跟著淺色或深色主題切換 |
| 非來源內容 | `## Supplementary notes (not from source)` 段落 | 和一般段落相同；靠標題區分 |
| 引用原文 | `"…"`，每處最多一句，後面接出處 | 一般文字（不用 blockquote，避免看起來像大段轉載） |
| footer | 課程出處、作者、GitHub repo | 每頁都顯示 |

## 6. Do not

- 不放講義或影片截圖（AGENTS.md §6）。
- 不自訂 JavaScript；需要互動功能時先寫進 PRD 討論。
- 不換掉 Quartz 的搜尋與圖譜元件。
