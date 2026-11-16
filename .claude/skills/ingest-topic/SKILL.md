---
name: ingest-topic
description: 把 compmatphys.org 的一個主題（頁碼代號如 AW03C）或整個單元匯入 CMP-wiki。使用者說「匯入 AWxxY」「做 U02」「匯入 setting the stage」時使用。
---

# Ingest a topic or unit

規則以 `AGENTS.md` 為準；這裡只寫步驟。一次匯入一個主題（或使用者指定的一個單元）。

## 1. Prepare
1. `git status` 確認沒有使用者未 commit 的修改要保留；記下起點 `git rev-parse --short HEAD`。
2. 對照 `PRD.md` §3，確認這個主題在範圍內。
3. 抓原站資料（只新增、不覆蓋）：
   ```bash
   python3 scripts/fetch_topic.py --topic <slug>      # 或 --unit <lesson-slug>
   python3 scripts/extract_text.py
   ```
   `--list` 可以列出所有 slug。抓不到影片或講義時，用內建瀏覽器打開主題頁確認（可能是延遲載入），結果寫進來源頁的「To verify」。

## 2. Read
1. 讀 `raw/pages/<slug>.md`：代號、預估時間、影片、講義、表單。
2. 讀整份講義：先用 `raw/text/<PDF 主幹>/s*.txt`（OCR）找內容與投影片編號，**方程式、符號、表格一律用 Read 看 PDF 該頁的影像，不可從 OCR 文字抄**（AGENTS.md §3-10）。
3. 有字幕（`raw/subs/`）就讀，但只能當輔助；自動字幕的術語常常聽錯。
4. 先用 3–5 點跟使用者報告重點，問有沒有要特別強調的（使用者已指定範圍時可省略）。

## 3. Write
1. **來源頁** `wiki/來源/來源-<code>.md`（範本 `templates/來源頁.md`）：`url:`、`raw:` 必填；整篇重寫，不往後追加。
2. **概念頁**：每個新詞先 `python3 scripts/lint.py --find <英文或中文>`，搜到就擴充原頁。新頁放 `wiki/概念/UNN/`，給 `order:`（`"<code>-KK"`）與 `kind:`。
3. **方程式、推導、邏輯鏈、實作、習題頁**：依 AGENTS.md §2 的條件判斷要不要開頁。
4. 每個實質說法加出處 `（[[來源-<code>]] slide N）`（投影片編號看 `raw/text/<PDF 主幹>/slides.json`）。**用自己的話寫**，直接引用原文時每處最多一句（AGENTS.md §6）。
5. 需要圖時自己畫（Mermaid 優先），不放講義截圖。
6. 所有 `#` 標題用英文；內容用繁中說明＋英文術語，術語每頁第一次出現時附中文。

## 4. Update the synthesis pages
- `index.md`：在對應單元下每頁一行。
- [[key equations]]、[[symbols]]：加入新式子與新符號。
- 有新的「因為 A 所以 B」關係，就寫或延伸邏輯鏈。

## 5. Check and record
1. `python3 scripts/lint.py`，錯誤修到 0。孤兒頁的警告也要處理（在 index 或相關頁加連結）。
2. `log.md` 最後加一行：`## [YYYY-MM-DD] ingest | 來源-<code> → N 概念、N 方程式…；⚠️待查證 N`。
3. 只 stage 自己改的檔案，commit 訊息和 log 那一行一致，並附上起點：`ingest: 來源-<code>（起點 abc1234）`。**不要 push**。
