---
type: 概念
aliases: [Hartree 位勢, V_H, Hartree term]
topic: density functional theory
unit: U02
order: "AW03C-02"
kind: quantity
sources:
  - "[[來源-AW03C]]"
prereqs: ["[[electron density]]"]
tags: [U02]
---

# Hartree potential

## Definition
Hartree potential $V_H$：一個準粒子感受到的、來自所有電子平均靜態電荷分布的 Coulomb 位勢（[[來源-AW03C]] slides 2–3）。

## Mathematical form
$$
V_H(\vec r)=\frac{e^2}{4\pi\varepsilon_0}\int\frac{\rho(\vec r')}{|\vec r-\vec r'|}\,d\vec r'
$$
（[[來源-AW03C]] slide 2）

符號說明（SI）：$\rho$ 是電子（數目）密度；乘上 $e^2$ 之後 $V_H$ 的單位是能量（J）。

## Physical meaning
- 它取代了原本 Hamiltonian 中電子–電子的 Coulomb 作用，改成「和其他所有準粒子的平均靜態分布作用」（[[來源-AW03C]] slide 3）。
- 它依賴 $\rho$，而 $\rho$ 又由 KS 方程式的解決定，這是需要 [[self-consistent field]] 的原因之一。

## Figure
無

## Validity and common misconceptions
- 用密度算的 Hartree 項包含電子和自己的作用（self-interaction）；精確的 $E_{xc}$ 會抵消這部分，近似的 XC 則不一定。這是一般知識，講義沒有談。

## Related equations
- [[Kohn-Sham equations]]

## Related concepts
- 上層：[[Kohn-Sham scheme]]
- 相關：[[electron density]]、[[exchange-correlation functional]]

## Conflicts and differences
- 單位慣例：講義的 $V_H$ 帶 $e^2$，是能量；而 $V_{ext}$ 不帶 $e$，是電位（見 [[external potential]]）。兩者在 $\hat H_{KS}$ 中並列，讀式子時要注意。

## Supplementary notes (not from source)

## Sources
- 原站：https://www.compmatphys.org/topics/kohn-sham-equations/
