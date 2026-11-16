---
name: query
description: 用 CMP-wiki 回答使用者關於 DFT、計算材料物理或課程內容的問題。使用者在這個 repo 裡問概念、公式、實作參數時使用。
---

# Answer a question from the wiki

1. 先讀 `index.md`，再打開相關頁面（順著 `[[連結]]` 與 `prereqs:` 讀）。
2. wiki 不夠時：
   - 先 `grep -ril <關鍵字> raw/text/` 找到講義的頁，只讀那幾頁（必要時看 PDF 影像），不要讀整份；
   - 還是沒有，就明說「知識庫裡沒有」，不要用一般知識冒充課程內容。可以另外標明「以下是一般知識（非來源內容）」再補充。
3. 回答時標出處：wiki 頁 `[[頁名]]`，或講義 `來源-<code> slide N`。
4. 內容值得保存時，問使用者要不要存成 `wiki/綜合/` 的新頁（英文頁名、英文標題）。
5. `log.md` 加一行：`## [YYYY-MM-DD] query | 問題摘要（讀：頁 A、頁 B；引用：來源-AW03C slide 4）`。只有存了新頁才 commit。
