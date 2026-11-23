# Report: DFT basic concepts

依 `.agents/workflows/topic-slides.md` 執行。每一關的結果與退回紀錄依序記在這裡。

## 1 Retrieval
- `sources.md`：選 17 頁，另列出不選的頁與理由。

## 2 Coverage gate
- `coverage_check.py`：17 頁全部存在 → 通過。

## 3 Evidence cards
- `make_cards.py`：17 張卡（只保留有出處的段落，去掉 Supplementary notes 與圖）。

## 4 Outline
- `outline.md`：初稿 14 頁；自我修正一次：第 13 頁原本把 SCF 與 HF vs DFT 混在一起，拆成兩頁 → 15 頁。

## 5 Human confirmation
- 2026-11-23 使用者確認大綱（15 頁），未退回。

## 6 Page drafts
- 依大綱寫 15 頁 `drafts/`；每頁只用 outline 為它指定的卡片，數學式從卡片原樣複製。

## 7 Faithfulness check (script)
- 第 1 輪：15 頁全部通過（0 錯誤）。
- 關卡自我測試：在副本中故意放入 7 種錯誤（中文標題、無出處、引用非本頁卡片、捏造式子 $E=mc^2$、捏造數字 37、frontmatter 卡片不存在、卡片不在大綱指定範圍），全部被抓到 → 關卡有效。

## 8–9 Render and render check
| 輪 | 結果 | 處理 |
|---|---|---|
| 1 | slide 03「horizontal overflow」 | 量測到 KaTeX 隱藏的 MathML 副本，屬於檢查本身的誤報；修正檢查腳本（排除 `.katex-mathml`），截圖確認可見內容沒有溢出 |
| 2 | 通過 | 人工看截圖：每行重複的出處標籤太吵、字太小、下半頁空白 → 只改版面：出處改成上標編號對應頁尾、放大字級（不改字） |
| 3 | slide 03 數學式過寬 41／57px；slide 10 垂直溢出 60px | 03：版面修正，模板對過寬數學式自動縮小字級；10：依流程「字太多 → 退回逐頁稿縮短」，刪掉「Kohn 與 Sham，1965」一行並縮短「各項」說明，重跑第 10 頁的忠實度檢查（通過） |
| 4 | slide 03 仍寬 4px | 縮字迴圈改成同時量測 KaTeX display 寬度 |
| 5 | 15 頁全部通過 | 逐頁截圖人工確認 |

## 10 AI review (new conversation)
審查者是新開的 subagent，只讀 `deck.html` 與 17 個被引用的 wiki 頁，不讀 drafts、cards、outline、raw，也不能改檔。

| 輪 | 結果 | 處理（退回逐頁稿，只修那頁） |
|---|---|---|
| 1 | 需要修改。11 頁 OK，1 頁有實質問題，3 頁輕微 | **15**：重點句「近似只在一步進來」和 BO 是近似互相矛盾，而且依據是 wiki 的 Supplementary notes → 改寫，並在限制加上數值誤差。**12**：「形式未知：這是唯一的本質近似」主詞不清 → 改成「XC-functional 的選擇」。**3**：「解不出來」誇大 → 改成「難解得多」，並註明 e–e 項 $+e^2$ 待查證。依建議補充：**4** 自旋座標、**5** 重點句、**6** $V_{ext}$ 符號慣例、**10** 自旋未極化、**11** 古典 correlation 定義、**12** pseudopotential 與 XC 要一致。**13**：刪掉 wiki 頁沒有講義出處的「所以叫自洽」。改完後 10、11 頁輕微溢出（11px、4px）→ 退回縮短 → 渲染檢查通過 |
| 2 | 需要修改（只剩 15 頁措辭） | 15：「唯一……此外還有」同一句自相矛盾 → 照建議改寫；11：可選調整也採用 |
| 3 | 通過 | — |

沒採用的建議：在第 13 頁補「basis set → $HC=SCE$」。這要用到大綱沒有指定給第 13 頁的卡片（Kohn-Sham equations），屬於大綱層級的修改，要回到人工確認關卡；審查者同意不列為問題。留作下一版的候選。

## 11 Delivery
- `deck.html`：15 頁。用瀏覽器打開，← → 或點擊換頁，F 全螢幕；網址加 `#N` 可以直接跳到第 N 頁；可以列印成 PDF，一頁一張。
- 最終檢查：忠實度檢查 15/15 通過、渲染檢查 15/15 通過、AI 審查第 3 輪通過。
- 已知限制：
  - KaTeX 與字型從 CDN 載入，離線時數學式不會渲染；
  - 第 3 頁電子–電子項的正負號沿用 wiki 的待查證判斷。
