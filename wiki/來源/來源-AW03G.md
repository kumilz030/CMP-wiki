---
type: 來源
code: AW03G
unit: U02
url: https://www.compmatphys.org/topics/numerical-solution-methods/
raw:
  - AW03G_numerical-solution_handouts.pdf
date_added: 2026-11-16
tags: [U02]
---

# AW03G · numerical solution methods

## Basic info
- 原站主題頁：https://www.compmatphys.org/topics/numerical-solution-methods/
- 講義：`AW03G_numerical-solution_handouts.pdf`（本機，不公開；10 張投影片）
- 同主題的另外兩份講義：[[來源-AW03G-tris]]（all-electron 與 pseudopotential）、[[來源-AW03G-bis]]（選讀：矩陣代數）
- 影片：Vimeo 3 支；字幕：無
- 預估時間：25 分鐘
- 單元：U02 density functional theory

## Summary
1. 寫出 Kohn-Sham equations 與 XC-functional 之後，還要把方程式解出來。這個主題講 basis set 方法、self-consistency 問題，以及能解 KS equations 的程式（[[來源-AW03G]] 主題頁）。
2. 任何能解 HF 或 KS equations 的數值方法都可以，例如在實空間格點上求解；固體最常用的是 basis set methods，並搭配 reciprocal space（[[來源-AW03G]] slide 3）。
3. 類比：方波可以用越來越多的 $\frac1K\sin(K\pi x)$ 奇數項逼近（[[來源-AW03G]] slide 4）。同樣地，把 KS 軌域展開成 $\phi_i(\vec r)=\sum_\alpha c^i_\alpha\chi^i_\alpha(\vec r)$（[[來源-AW03G]] slide 5）：
   - $\chi$ 是選定的 basis function；
   - 係數 $c$ 是要找的未知數；
   - 無窮級數要截斷：取夠多的基底函數以求準確，但不要更多，因為這決定計算時間。
4. 引入 basis set 後，問題變成矩陣代數 $HC=SCE$（[[來源-AW03G]] slide 6）：
   - $H$ 是基底函數之間的 KS Hamiltonian 矩陣元素；
   - $S$ 是 overlap matrix；
   - 這兩者可以一次算好。
5. self-consistent field 問題：要知道 $\rho$ 才寫得出 $\hat H_{KS}$，但要解 $\hat H_{KS}$ 才得到 $\phi_i$ 與 $\rho$，所以要用迭代（scf-scheme）（[[來源-AW03G]] slide 7）。流程圖（[[來源-AW03G]] slide 8）：
   - 由 $\rho_{old}$ 建 $V_{eff}$；
   - 解 $H_{KS}\phi_i=\epsilon_i\phi_i$；
   - 由 $\phi_i$ 建 $\rho_{new}$；
   - 比較 $\rho_{new}$ 與 $\rho_{old}$：不相等就以 $\rho_{new}$ 取代 $\rho_{old}$ 重來，相等就完成。
6. basis function 的種類決定方法的名稱，也決定你能用哪個程式（[[來源-AW03G]] slide 9）：
   - localized basis functions（GTO、STO）；
   - plane waves（搭配 pseudopotentials）；
   - augmented plane waves（LAPW、LMTO…）。
7. 更多程式列在 Wikipedia 的量子化學與固態物理軟體列表（[[來源-AW03G]] slide 10）。主題頁另外列出 Quantum ESPRESSO、ABINIT、CRYSTAL、VASP、WIEN2k 的綜述論文作為選讀（[[來源-AW03G]] 主題頁）。

## Notation
| 這份來源 | 知識庫統一符號 | 意義 |
|---|---|---|
| $\chi^i_\alpha$ | $\chi_\alpha$ | basis function |
| $c^i_\alpha$ | $c^i_\alpha$ | 展開係數 |
| $H$、$S$、$C$、$E$ | $H$、$S$、$C$、$E$ | Hamiltonian 矩陣、overlap 矩陣、係數矩陣、對角的本徵值矩陣 |
| $V_{eff}$ | $V_{eff}$ | KS 方程式中的有效位勢（$V_H+V_{ext}+V_{xc}$） |

## Pages created or updated
- 新增：[[basis set]]、[[self-consistent field]]、[[generalized eigenvalue problem HC=SCE]]

## Quizzes and exercises
- 表單：回報自己用過哪些 DFT 或量子化學程式（不公開）。

## To verify
- 無
