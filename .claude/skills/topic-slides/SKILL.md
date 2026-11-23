---
name: topic-slides
description: 只用 CMP-wiki 的內容，把一個主題做成 HTML 教學簡報（Graph 流程：檢索 → 覆蓋率關卡 → 證據卡 → 大綱 → 人工確認 → 逐頁稿 → 忠實度檢查 → 渲染 → 渲染檢查 → AI 審查）。使用者說「做一份 X 的簡報」「/topic-slides X」時使用。
---

# Topic slides

完整流程、每一關能看什麼與不能做什麼，見 `.agents/workflows/topic-slides.md`。照那份檔案逐關執行：

1. 建立 `slides/topic-<slug>/`，寫 `sources.md`（只從 `index.md` 與 wiki 頁挑相關頁）。
2. `python3 scripts/slides/coverage_check.py slides/topic-<slug>`；不過就停下回報。
3. `python3 scripts/slides/make_cards.py slides/topic-<slug>`。
4. 只看 `cards/` 寫 `outline.md`。
5. **停下來請使用者確認大綱**；退回就修大綱或補檢索。
6. 逐頁寫 `drafts/`，優先用表格與圖表元件（格式見 workflow 的 Draft format），每寫完跑 `check_drafts.py`（含版面密度：每頁要有圖表、文字量 ≤ 110），最多 2 輪。
7. `render_deck.py` → `render_check.py --shots <暫存資料夾>`，並逐頁看截圖；字太多溢出就退回逐頁稿縮短，版面問題只改模板。修好檢查漏掉的錯之後，做迴歸測試（把錯放回副本，確認檢查抓得到）。
8. 開一個新的 subagent，只給它 `deck.html` 的文字與被引用的 wiki 頁，請它審查忠實度與覆蓋率；講錯的頁退回逐頁稿。
9. 寫 `report.md`（每一關結果、退回紀錄），交件。commit 依 AGENTS.md §7；push 前先問使用者。
