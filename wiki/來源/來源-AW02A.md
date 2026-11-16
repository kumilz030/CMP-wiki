---
type: 來源
code: AW02A
unit: U02
url: https://www.compmatphys.org/topics/a-dft-teaser/
raw:
  - AW02A_DFT-teaser_handouts.pdf
date_added: 2026-11-16
tags: [U02]
---

# AW02A · a DFT teaser

## Basic info
- 原站主題頁：https://www.compmatphys.org/topics/a-dft-teaser/
- 講義：`AW02A_DFT-teaser_handouts.pdf`（本機，不公開；5 張投影片）
- 影片：YouTube 1 支（約 6 分鐘，長演講的片段；完整版見 [[來源-AW03H-teaser]]）；字幕：YouTube 限流，未取得
- 預估時間：10 分鐘
- 單元：U02 density functional theory

## Summary
1. 主題頁說，DFT 的基本想法可以用一個不含數學的故事說清楚，請學員看完後把這個訊息記在心裡，再讀這一章的其他部分（[[來源-AW02A]] 主題頁）。
2. 講義的比喻：一邊是一個超大型實驗設施，另一邊是一群顧問（「The Delusion Factory」）。顧問用一個簡單的電路模型，就能重現大設施的量測結果（[[來源-AW02A]] slides 3–4）。
3. 對應到 DFT（[[來源-AW02A]] slide 4）：
   - 難以求解的 many-body Schrödinger equation $\hat{\mathcal H}\Psi(\vec r_1,\dots,\vec r_N)=E\Psi(\vec r_1,\dots,\vec r_N)$；
   - 經由 DFT，換成 single-particle Kohn-Sham equations $\hat{\mathcal H}_{KS}\phi(\vec r)=E\phi(\vec r)$；
   - 用 LAPW、PAW、grids 等方法求解，對應的程式有 VASP、QE、WIEN2k 等。
4. 最後一張投影片在電路中標出一個關鍵元件，並在箭頭旁標上「XC?」：轉換成功的關鍵是 exchange-correlation（[[來源-AW02A]] slide 5）。

## Notation
| 這份來源 | 知識庫統一符號 | 意義 |
|---|---|---|
| $\hat{\mathcal H}$ | $\hat H$ | many-body Hamiltonian |
| $\hat{\mathcal H}_{KS}$ | $\hat H_{KS}$ | Kohn-Sham Hamiltonian |
| $\phi(\vec r)$ | $\phi_i(\vec r)$ | single-particle（Kohn-Sham）軌域 |

## Pages created or updated
- 新增：[[density functional theory]]

## Quizzes and exercises
- 無

## To verify
- 「Delusion Factory」故事的細節只在影片中；講義只有圖。
