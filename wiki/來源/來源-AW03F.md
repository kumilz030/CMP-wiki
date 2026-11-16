---
type: 來源
code: AW03F
unit: U02
url: https://www.compmatphys.org/topics/hartree-fock-versus-dft/
raw:
  - AW03F_HF-vs-DFT_handouts.pdf
date_added: 2026-11-16
tags: [U02]
---

# AW03F · Hartree-Fock versus DFT

## Basic info
- 原站主題頁：https://www.compmatphys.org/topics/hartree-fock-versus-dft/
- 講義：`AW03F_HF-vs-DFT_handouts.pdf`（本機，不公開；13 張投影片）
- 影片：Vimeo 1 支；字幕：無
- 預估時間：25 分鐘
- 單元：U02 density functional theory

## Summary
1. post-HF 與 DFT 想解的是同一個問題，這個主題比較兩者的優點與限制（[[來源-AW03F]] 主題頁）。
2. 對照表（[[來源-AW03F]] slides 3–5）：
   - Hartree-Fock：依定義有 exact exchange、沒有 correlation；correlation 要靠 post-HF 一步一步加進去，計算很耗時；
   - 精確的 DFT：$E_{xc}[\rho]$ 包含精確的 exchange 與 correlation，用它解 KS equations 會得到精確結果；
   - 實際的 DFT（LDA）：$E^{LDA}_{xc}[\rho]$ 含有部分 exchange 與部分 correlation，結果是近似的，而且要改進它「需要黑魔法」。
3. 圖像版本（[[來源-AW03F]] slides 7–12）：目標是從 first principles（Schrödinger 或 Dirac equation）出發，直接解出精確結果。
   - post-HF 的路徑會逐步逼近靶心，但總會撞上「計算資源永遠有限」這道牆；
   - DFT 繞另一條路，能打到靶心附近。
4. 結論（[[來源-AW03F]] slide 13）：
   - post-HF：適合小系統，準確度高；
   - DFT：可以處理大系統，但有一些無法控制的「noise」；
   - 選讀：Cohen et al.（2012）。

## Notation
| 這份來源 | 知識庫統一符號 | 意義 |
|---|---|---|
| $E_{xc}[\rho]$ | $E_{xc}[\rho]$ | exchange-correlation 能量泛函（這份講義寫 $E_{xc}$，和 AW03C、AW03D 的 $V_{xc}[\rho]$ 指同一個東西） |

## Pages created or updated
- 新增：[[HF versus DFT]]

## Quizzes and exercises
- 討論區問題（不公開答案）：要預測主題頁連結的那個分子的性質，你會用哪一類方法？為什麼？

## To verify
- 主題頁連結的分子是哪一個（連結指向外部圖片）。
