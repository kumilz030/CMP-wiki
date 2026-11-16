---
type: 來源
code: AW03G
unit: U02
url: https://www.compmatphys.org/topics/numerical-solution-methods/
raw:
  - AW03G-bis-matrix-algebra_handouts.pdf
date_added: 2026-11-16
tags: [U02]
---

# AW03G-bis · from Kohn-Sham equations to matrix algebra (optional)

## Basic info
- 原站主題頁：https://www.compmatphys.org/topics/numerical-solution-methods/ （選看的第三支影片）
- 講義：`AW03G-bis-matrix-algebra_handouts.pdf`（本機，不公開；26 張投影片，幾乎全是方程式的逐步動畫）
- 單元：U02 density functional theory

## Summary
1. 主題頁說，這支選看影片說明怎麼把解 Kohn-Sham equations 的過程寫成矩陣代數 $HC=SCE$（[[來源-AW03G-bis]] 主題頁）。
2. 從 $\Psi(\vec x_1,\dots,\vec x_N)$ 改走單粒子軌域：密度 $\rho^{KS}(\vec r)=\sum_i^N|\phi_i(\vec r)|^2$，而 $\phi_i$ 滿足 $\hat H_{KS}\phi_i=\epsilon_i\phi_i$（$i=1\dots N$）（[[來源-AW03G-bis]] slides 4–6）。
3. 把 $\phi$ 展開成 basis functions：精確的展開是無窮級數 $\sum_{k=1}^{\infty}c_k\chi_k$，實際截斷到 $M$ 項，$\phi_i\approx\sum_{k=1}^{M}c^i_k\chi_k$。示範用 $M=2$（[[來源-AW03G-bis]] slides 10–11）。
4. 把展開代入 $\hat H_{KS}|\phi_i\rangle=\epsilon_i|\phi_i\rangle$，分別用 $\langle\chi_1|$、$\langle\chi_2|$ 左乘，得到兩條線性方程式。定義 $h_{jk}=\langle\chi_j|\hat H_{KS}|\chi_k\rangle$、$s_{jk}=\langle\chi_j|\chi_k\rangle$（[[來源-AW03G-bis]] slides 12–19）。
5. 把所有本徵態的方程式合併成矩陣形式 $HC=SCE$（[[來源-AW03G-bis]] slides 20–25）：
   - 矩陣大小是 $M\times M$；
   - 基底函數數 $M$ 要大於要填的軌域數 $N$（[[來源-AW03G-bis]] slide 26）。

## Notation
| 這份來源 | 知識庫統一符號 | 意義 |
|---|---|---|
| $h_{jk}$ | $H_{jk}$ | Hamiltonian 矩陣元素 |
| $s_{jk}$ | $S_{jk}$ | overlap 矩陣元素 |
| $M$ | $M$ | 基底函數個數 |
| $N$ | $N$ | 電子（佔據軌域）個數 |

## Pages created or updated
- 新增：[[推導-HC=SCE from a basis set expansion]]、[[generalized eigenvalue problem HC=SCE]]

## Quizzes and exercises
- 無

## To verify
- 無
