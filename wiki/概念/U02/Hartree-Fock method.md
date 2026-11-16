---
type: 概念
aliases: [HF, Hartree-Fock, Hartree-Fock 方法]
topic: density functional theory
unit: U02
order: "AW02E-01"
kind: method
sources:
  - "[[來源-AW02E]]"
  - "[[來源-AW03E]]"
  - "[[來源-AW03F]]"
prereqs: ["[[Slater determinant]]", "[[Born-Oppenheimer approximation]]"]
tags: [U02]
---

# Hartree-Fock method

## Definition
Hartree-Fock（HF）方法：在所有 Slater determinants 中，找能量最低的那一個，作為多電子基態的近似（[[來源-AW02E]] slides 5–6）。它和 DFT 並列 [[three levels of approximation]] 的 level 2（[[來源-AW02E]] slide 2）。

## Mathematical form
HF 基態是一個 Slater determinant（[[來源-AW03E]] slide 4）：
$$
|\Psi_0^{HF}\rangle=\frac{1}{\sqrt{N!}}
\begin{vmatrix}
\Psi_1(\vec\alpha_1) & \Psi_1(\vec\alpha_2) & \cdots & \Psi_1(\vec\alpha_N)\\
\vdots & & \ddots & \vdots\\
\Psi_N(\vec\alpha_1) & \Psi_N(\vec\alpha_2) & \cdots & \Psi_N(\vec\alpha_N)
\end{vmatrix}
$$
符號說明：$\Psi_i$ 是單電子軌域，$\vec\alpha_j$ 是第 $j$ 個電子的空間＋自旋座標。

## Physical meaning
- 在「所有可能波函數的空間」裡，HF 基態被限制在 Slater determinants 這個子集內，所以一般不等於精確基態（[[來源-AW02E]] slides 3–6）。
- HF 依定義包含精確的 exchange，但沒有 correlation（[[來源-AW03F]] slide 3）。HF 能量和精確能量的差，就是量子力學中 correlation 的定義（[[來源-AW03E]] slide 5）。
- HF 本身對固體不太準，所以不太直接使用；但它是 post-HF 方法的起點（[[來源-AW02E]] slide 11）。

## Figure
```mermaid
flowchart LR
  A["所有可能的波函數"] --> B["反對稱的波函數<br/>（含精確基態）"]
  B --> C["Slater determinants<br/>（含 HF 基態）"]
```
自繪，依據 [[來源-AW02E]] slides 3–6（集合由大到小）。

## Validity and common misconceptions
- 誤解：「HF 是獨立電子近似，所以完全沒有電子間的作用」。HF 有平均場的電子作用與精確 exchange，缺的是 correlation（[[來源-AW03F]] slide 3）。

## Related equations
- [[Hamiltonian of a solid]]

## Related concepts
- 上層：[[three levels of approximation]]
- 相關：[[Slater determinant]]、[[post-Hartree-Fock methods]]、[[exchange and correlation]]、[[HF versus DFT]]

## Conflicts and differences

## Supplementary notes (not from source)
- 物化角度的 HF 推導（Fock operator、自洽場）見 pchem-wiki 的相關頁面。

## Sources
- 原站：https://www.compmatphys.org/topics/post-hartree-fock-methods/
