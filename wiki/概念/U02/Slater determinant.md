---
type: 概念
aliases: [Slater 行列式]
topic: density functional theory
unit: U02
order: "AW02E-02"
kind: quantity
sources:
  - "[[來源-AW02E]]"
  - "[[來源-AW03E]]"
prereqs: []
tags: [U02]
---

# Slater determinant

## Definition
Slater determinant（Slater 行列式）：用 N 個單電子軌域組成的行列式來寫 N 電子波函數，因此自動滿足電子（fermion）要求的反對稱性（[[來源-AW03E]] slide 4）。

## Mathematical form
$$
|\Psi_0^{HF}\rangle=\frac{1}{\sqrt{N!}}\det\big[\Psi_i(\vec\alpha_j)\big]_{i,j=1}^{N}
$$
對照不反對稱的 Hartree product（乘積波函數）（[[來源-AW03E]] slide 4）：
$$
|\Psi_0^{H}(\vec\alpha_1,\dots,\vec\alpha_N)\rangle=|\Psi_1(\vec\alpha_1)\Psi_2(\vec\alpha_2)\cdots\Psi_N(\vec\alpha_N)\rangle
$$
符號說明：$\Psi_i$ 是單電子軌域，$\vec\alpha_j$ 是第 $j$ 個電子的空間＋自旋座標。

## Physical meaning
- 所有 Slater determinants 是「所有反對稱波函數」的一個子集（[[來源-AW02E]] slide 5）。
- 從 Hartree product 換成 Slater determinant，能量的下降就是 exchange（[[來源-AW03E]] slide 4）。

## Figure
無

## Validity and common misconceptions
- 一般的反對稱波函數不一定能寫成單一 Slater determinant。精確基態通常不是，所以 post-HF 方法要加入更多反對稱函數（[[來源-AW02E]] slides 6–10）。

## Related equations
- 無

## Related concepts
- 相關：[[Hartree-Fock method]]、[[post-Hartree-Fock methods]]、[[exchange and correlation]]

## Conflicts and differences

## Supplementary notes (not from source)
- 主題頁建議不熟悉 Slater determinant 的學員先看一支 5 分鐘的說明影片（外部連結）。物化角度見 pchem-wiki。

## Sources
- 原站：https://www.compmatphys.org/topics/post-hartree-fock-methods/
