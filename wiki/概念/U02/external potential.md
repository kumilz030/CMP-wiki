---
type: 概念
aliases: [外位勢, V_ext]
topic: density functional theory
unit: U02
order: "AW02F-01"
kind: quantity
sources:
  - "[[來源-AW02F]]"
  - "[[來源-AW02F-quiz]]"
  - "[[來源-AW03A]]"
prereqs: ["[[Hamiltonian of a solid]]"]
tags: [U02]
---

# external potential

## Definition
external potential（外位勢）$V_{ext}(\vec r)$：一組固定在 $\vec R_A$ 的原子核在空間點 $\vec r$ 所產生的電位（[[來源-AW02F]] slides 4–6）。

## Mathematical form
$$
V_{ext}(\vec r)=+\frac{1}{4\pi\varepsilon_0}\sum_A\frac{eZ_A}{|\vec r-\vec R_A|}
$$
符號說明（SI）：
- $Z_A$、$\vec R_A$：第 A 個原子核的原子序與位置；
- $e$：基本電荷；
- $\varepsilon_0$：真空介電常數；
- $V_{ext}$ 的單位是 V（J/C），是**電位**，不是能量（[[來源-AW02F]] slide 6；[[來源-AW02F-quiz]] slide 1）。

對應的能量項是 Hamiltonian 中的電子–原子核吸引（[[來源-AW02F]] slides 3–4），寫成 DFT 形式則是（[[來源-AW02F-quiz]] slide 1）：
$$
E_{ext}=\int V_{ext}(\vec r)\,\rho(\vec r)\,d\vec r
$$
這裡的 $\rho$ 是 charge density（$-e$ 乘以機率密度）。

## Physical meaning
- 「external」是從電子的角度說：在 Born-Oppenheimer 之下原子核是固定的，它們提供的電位對電子而言是外加的（[[來源-AW02F]] slides 4–5）。
- $V_{ext}$ 完全由原子核決定，不含任何電子的資訊（[[來源-AW02F-quiz]] slide 1）。
- 它決定了系統：第一 Hohenberg-Kohn 定理說，external potential 與基態密度一對一對應（[[來源-AW03A]] slide 9）。
- $E_{ext}$ 是少數已知精確寫成密度泛函的性質之一（[[來源-AW02F-quiz]] slide 1）。

## Figure
無

## Validity and common misconceptions
- 常見混淆是 $V_{ext}$（電位，$\vec r$ 的函數）、$E_{ext}$（能量，一個數）、$\hat V_{ext}$（算符）。三種寫法都正確，但要清楚自己寫的是哪一個（[[來源-AW02F-quiz]] slide 1）。

## Related equations
- [[Hamiltonian of a solid]]
- [[Kohn-Sham equations]]

## Related concepts
- 相關：[[first Hohenberg-Kohn theorem]]、[[electron density]]、[[functional]]
- 習題：[[習題-AW02F external potential of O2]]

## Conflicts and differences
- 符號慣例：講義的 $V_{ext}$ 是電位（正值）。有些教科書把 $V_{ext}$ 定義成電子感受到的位能（已乘上 $-e$，負值）。讀 $\hat H_{KS}$ 時要注意是哪一種。

## Supplementary notes (not from source)

## Sources
- 原站：https://www.compmatphys.org/topics/the-external-potential/
