---
type: 概念
aliases: [基底組, basis set method, basis functions, 基底函數]
topic: density functional theory
unit: U02
order: "AW03G-01"
kind: method
sources:
  - "[[來源-AW03G]]"
  - "[[來源-AW03G-tris]]"
  - "[[來源-basis-sets-1]]"
  - "[[來源-lets-play-w3a]]"
prereqs: ["[[Kohn-Sham equations]]"]
tags: [U02]
---

# basis set

## Definition
basis set（基底組）：把未知的單粒子軌域寫成一組已知（選定的）basis functions 的線性組合，問題就從求函數變成求係數（[[來源-AW03G]] slide 5）。固體最常用的求解方法就是 basis set methods，並搭配 reciprocal space（[[來源-AW03G]] slide 3）。

## Mathematical form
$$
\phi_i(\vec r)=\sum_{\alpha=1}^{\infty}c^i_\alpha\,\chi^i_\alpha(\vec r)\;\approx\;\sum_{\alpha=1}^{M}c^i_\alpha\,\chi_\alpha(\vec r)
$$
符號說明：
- $\phi_i$：提供密度的 N 個單粒子函數之一；
- $\chi_\alpha$：已知或選定的基底函數；
- $c^i_\alpha$：要找的係數；
- $M$：截斷後的基底函數個數。

（[[來源-AW03G]] slide 5）

## Physical meaning
- 類比：方波可以用越來越多的 $\frac1K\sin(K\pi x)$ 奇數項逼近（[[來源-AW03G]] slide 4）。
- 截斷的取捨：取夠多的基底函數以求準確，但不要更多，因為這決定計算時間（[[來源-AW03G]] slide 5）。
  - lemma 1：原函數和基底函數在性質上差越多，需要的基底函數越多（[[來源-AW03G-tris]] slide 2）；
  - lemma 2：計算時間隨基底函數數目快速增加（[[來源-AW03G-tris]] slide 4）。
- 引入基底後，KS 方程式變成矩陣問題 [[generalized eigenvalue problem HC=SCE]]（[[來源-AW03G]] slide 6）。矩陣對角化是大多數程式的主要工作，也占掉大部分計算時間（[[來源-basis-sets-1]] slide 18）。
- 基底的種類決定方法的名稱，也決定你能用哪個程式（[[來源-AW03G]] slide 9；[[來源-basis-sets-1]] slide 20）：
  - atomic orbitals（GTO、STO）：「分子是稍微變形的原子」，可能有 basis set superposition error（BSSE）（[[來源-basis-sets-1]] slides 23–24）；
  - plane waves（搭配 pseudopotentials）：見 [[plane-wave basis set]]；
  - augmented plane waves（LAPW、LMTO…）：見 [[augmented plane wave methods]]。
- 實作：basis set 的截斷限制了計算精度，理想上要截到「再加基底也不明顯影響結果」為止（[[來源-lets-play-w3a]] slide 2），見 [[cutoff energy]]、[[convergence testing]]。

## Figure
無

## Validity and common misconceptions
- basis set 是數值近似（[[three levels of approximation]] 的 level 3），和 XC 近似是不同來源的誤差；前者可以靠收斂測試控制。

## Related equations
- [[generalized eigenvalue problem HC=SCE]]
- [[Kohn-Sham equations]]

## Related concepts
- 上層：[[three levels of approximation]]
- 相關：[[self-consistent field]]、[[all-electron method]]、[[pseudopotential]]、[[plane-wave basis set]]

## Conflicts and differences

## Supplementary notes (not from source)

## Sources
- 原站：https://www.compmatphys.org/topics/numerical-solution-methods/
