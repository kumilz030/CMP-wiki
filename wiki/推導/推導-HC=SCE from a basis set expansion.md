---
type: 推導
aliases: [HC=SCE 的推導]
topic: density functional theory
unit: U02
sources:
  - "[[來源-AW03G-bis]]"
tags: [U02]
---

# Derivation: HC=SCE from a basis set expansion

## Goal
從 Kohn-Sham equations 出發，引入有限的 basis set，得到矩陣形式的 [[generalized eigenvalue problem HC=SCE]]（[[來源-AW03G-bis]] 主題頁）。

## Starting point and assumptions
1. Kohn-Sham equations：$\hat H_{KS}|\phi_i\rangle=\epsilon_i|\phi_i\rangle$，$i=1\dots N$（[[來源-AW03G-bis]] slides 6、12）。
2. 每個軌域展開成有限個基底函數：$\phi_i\approx\sum_{k=1}^{M}c^i_k\chi_k$（[[來源-AW03G-bis]] slide 10）。
3. 講義用 $M=2$ 示範：$\phi_i\approx c^i_1\chi_1+c^i_2\chi_2$（[[來源-AW03G-bis]] slide 11）。

## Derivation
**步驟 1：代入展開。**（[[來源-AW03G-bis]] slides 13–14）
$$
\hat H_{KS}\big(c^i_1|\chi_1\rangle+c^i_2|\chi_2\rangle\big)=\epsilon_i\big(c^i_1|\chi_1\rangle+c^i_2|\chi_2\rangle\big)
$$

**步驟 2：用 $\langle\chi_1|$ 左乘。**（[[來源-AW03G-bis]] slide 15）
$$
c^i_1\underbrace{\langle\chi_1|\hat H_{KS}|\chi_1\rangle}_{h_{11}}+c^i_2\underbrace{\langle\chi_1|\hat H_{KS}|\chi_2\rangle}_{h_{12}}
=\epsilon_i\Big(c^i_1\underbrace{\langle\chi_1|\chi_1\rangle}_{s_{11}}+c^i_2\underbrace{\langle\chi_1|\chi_2\rangle}_{s_{12}}\Big)
$$

**步驟 3：用 $\langle\chi_2|$ 左乘。** 同理得到含 $h_{21},h_{22},s_{21},s_{22}$ 的第二條方程式（[[來源-AW03G-bis]] slides 16–19）。

**步驟 4：寫成矩陣。** 一個本徵態是（[[來源-AW03G-bis]] slides 20–22）：
$$
\begin{pmatrix}h_{11}&h_{12}\\h_{21}&h_{22}\end{pmatrix}\begin{pmatrix}c^i_1\\c^i_2\end{pmatrix}
=\epsilon_i\begin{pmatrix}s_{11}&s_{12}\\s_{21}&s_{22}\end{pmatrix}\begin{pmatrix}c^i_1\\c^i_2\end{pmatrix}
$$

**步驟 5：所有本徵態並排。** 把各個 $i$ 的係數排成矩陣 $C$ 的各行，本徵值放進對角矩陣 $E$（[[來源-AW03G-bis]] slides 23–25）。

## Result
$$
HC=SCE
$$
一般情況是 $M\times M$ 的矩陣；基底函數數 $M$ 要大於佔據軌域數 $N$，密度只用到最低的 $N$ 個解：$\rho=\sum_i^N|\phi_i|^2$（[[來源-AW03G-bis]] slide 26）。

## Where each assumption enters
- **有限展開**：步驟 1，讓問題變成有限維。截斷就是數值誤差的來源，見 [[basis set]]。
- **基底不一定正交**：步驟 2 中 $s_{12}\neq0$，所以右邊有 $S$；正交基底時 $S=I$。
- **$M>N$**：Result，要有足夠多的解來填 N 個佔據軌域。

## Supplementary notes (not from source)
- 若 $\hat H_{KS}$ 是 Hermitian，$H$ 也是 Hermitian；若 $S$ 正定，問題可以轉換成標準本徵值問題（例如 Cholesky 分解）。這是一般線性代數知識。

## Sources
- 原站：https://www.compmatphys.org/topics/numerical-solution-methods/
