---
name: lint
description: CMP-wiki 健檢。使用者說「健檢」「lint」或要求檢查知識庫品質時使用。
---

# Health check

1. 執行 `python3 scripts/lint.py`。腳本檢查的項目（結構、標題、連結、出處、公開限制、待查證，見腳本開頭說明）**以腳本結果為準**，不用再人工檢查一遍。
2. AI 只檢查腳本做不到的：
   - 說法互相矛盾、符號或單位制不一致（Ha／Ry／eV）；
   - 被提到很多次卻沒有自己頁面的概念；
   - **公開風險**：段落讀起來像逐句翻譯講義、沒加引號的原文、自繪圖其實是照描講義圖；
   - 建議下一步要匯入什麼。
3. 重跑 [[knowledge base test questions]]：只靠 `index.md` 與 wiki 頁作答，記錄通過數到該頁的「Results」表。
4. **先回報，經使用者同意再修**。修完在 `log.md` 加 `## [YYYY-MM-DD] lint | 結果摘要`，commit：`lint: 摘要（起點 abc1234）`。
