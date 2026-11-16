---
type: 推導
aliases: [第一 HK 定理的證明, proof of HK1]
topic: density functional theory
unit: U02
sources:
  - "[[來源-AW03A-bis]]"
  - "[[來源-AW03A]]"
tags: [U02]
---

# Derivation: first Hohenberg-Kohn theorem

## Goal
證明映射 $D:\Psi\mapsto\rho$ 是 injective：若 $\Psi\neq\Psi'$，則 $\rho\neq\rho'$（[[來源-AW03A-bis]] slide 3）。結論見 [[first Hohenberg-Kohn theorem]]。

## Starting point and assumptions
1. 只考慮 non-degenerate ground states（[[來源-AW03A-bis]] slide 3）。
2. 反證：假設 $\Psi\neq\Psi'$，但 $\rho=\rho'$（[[來源-AW03A-bis]] slide 3）。
3. $\Psi$ 是 $H$ 的基態，能量 $E_{gs}$；$\Psi'$ 是 $H'$ 的基態，能量 $E'_{gs}$（[[來源-AW03A-bis]] slide 4）。
4. 兩個系統電子數相同。不同的話密度積分就不同，結論是 trivial 的（[[來源-AW03A-bis]] slide 5）。
5. variational principle（變分原理）。

## Derivation
**步驟 1：兩個 Hamiltonian 只差在外位勢。** 電子數相同，所以動能 $T$ 與電子–電子作用 $W$ 相同（[[來源-AW03A-bis]] slide 5）：
$$
H=T+W+V,\quad H'=T+W+V'\quad\Rightarrow\quad H=H'-V'+V
$$

**步驟 2：把 $\Psi'$ 當成 $H$ 的試探函數。** 因為 $\Psi$ 是 $H$ 的非簡併基態，而 $\Psi'\neq\Psi$，變分原理給出嚴格不等式（[[來源-AW03A-bis]] slides 6–8）：
$$
E_{gs}=\langle\Psi|H|\Psi\rangle<\langle\Psi'|H|\Psi'\rangle=\langle\Psi'|H'+V-V'|\Psi'\rangle
=E'_{gs}+\int\rho'(\vec r)\big[v(\vec r)-v'(\vec r)\big]d\vec r
$$
最後一個等號用到：外位勢的期望值只依賴密度（見 [[external potential]]）。

**步驟 3：角色對調。** 以 $\Psi$ 當 $H'$ 的試探函數，同理得到（[[來源-AW03A-bis]] slide 9）：
$$
E'_{gs}<E_{gs}+\int\rho(\vec r)\big[v'(\vec r)-v(\vec r)\big]d\vec r
$$

**步驟 4：相加並代入 $\rho=\rho'$。** 兩個積分項互相抵消（[[來源-AW03A-bis]] slide 10）：
$$
E_{gs}+E'_{gs}<E_{gs}+E'_{gs}
$$

## Result
得到矛盾，所以假設錯誤：不同的基態波函數一定給出不同的密度（[[來源-AW03A-bis]] slide 10）。再加上 $C:\hat V_{ext}\mapsto\Psi$ 本來就是 injective，基態密度與外位勢一對一對應（[[來源-AW03A]] slides 8–9）。原始論文：P. Hohenberg and W. Kohn, Phys. Rev. 136B (1964) 864（[[來源-AW03A-bis]] slide 15）。

## Where each assumption enters
- **非簡併**：步驟 2、3 的嚴格不等號 $<$。若基態簡併，$\Psi'$ 可能也是 $H$ 的基態，只能得到 $\le$，就推不出矛盾。
- **電子數相同**：步驟 1，讓 $T$、$W$ 相同。
- **$\rho=\rho'$**：步驟 4，讓兩個積分項互相抵消。

## Supplementary notes (not from source)
- 上面「為什麼非簡併時是嚴格不等號」的說明，是對講義步驟的補充解釋。

## Sources
- 原站：https://www.compmatphys.org/topics/first-hohenberg-kohn-theorem/
