---
type: 方程式
aliases: [HC=SCE, 廣義本徵值問題, secular equation]
topic: density functional theory
unit: U02
sources:
  - "[[來源-AW03G]]"
  - "[[來源-AW03G-bis]]"
  - "[[來源-basis-sets-1]]"
prereqs: ["[[basis set]]", "[[Kohn-Sham equations]]"]
tags: [U02]
---

# generalized eigenvalue problem HC=SCE

## Equation
$$
HC=SCE,\qquad
H_{\gamma\delta}=\langle\chi_\gamma|\hat H_{KS}|\chi_\delta\rangle,\qquad
S_{\gamma\delta}=\langle\chi_\gamma|\chi_\delta\rangle
$$
（[[來源-AW03G]] slide 6）

符號說明：
- $H$：所有基底函數之間的 KS Hamiltonian 矩陣元素；
- $S$：overlap matrix（基底函數的內積）；
- $C$：方陣，每一行是一組要找的係數 $c^i_\alpha$；
- $E$：對角矩陣，對角線是要找的本徵值 $\epsilon_i$；
- 矩陣大小 $M\times M$，$M$ 是基底函數數（[[來源-AW03G-bis]] slide 26）。

## Conditions of validity
- 單粒子軌域已截斷成 $M$ 個基底函數的有限展開（[[來源-AW03G-bis]] slides 10–11）。
- 一般的（不正交的）基底；若基底正交，$S$ 是對角矩陣，問題較簡單（[[來源-basis-sets-1]] slide 18）。
- $M$ 必須大於佔據軌域數 $N$（[[來源-AW03G-bis]] slide 26）。

## Origin
把 $\phi_i\approx\sum_kc^i_k\chi_k$ 代入 $\hat H_{KS}\phi_i=\epsilon_i\phi_i$，分別用每個 $\langle\chi_j|$ 左乘（[[來源-AW03G-bis]] slides 12–25）。逐步推導見 [[推導-HC=SCE from a basis set expansion]]。

## How to use
- $H$ 與 $S$ 可以一次算好（給定 $\hat H_{KS}$），然後對角化得到 $C$ 與 $E$（[[來源-AW03G]] slide 6）。
- 矩陣對角化是大多數程式的主要工作，占掉大部分計算時間（[[來源-basis-sets-1]] slide 18）。所以基底越大，計算越貴。
- 因為 $\hat H_{KS}$ 依賴 $\rho$，每一輪 [[self-consistent field]] 都要重建 $H$ 再對角化一次。

## Common mistakes
- 忘了 $S$：只有正交基底才能寫成一般的本徵值問題 $HC=CE$。

## Conflicts and differences

## Supplementary notes (not from source)

## Sources
- 原站：https://www.compmatphys.org/topics/numerical-solution-methods/
