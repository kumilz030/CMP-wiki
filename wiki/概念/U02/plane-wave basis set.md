---
type: 概念
aliases: [plane waves, 平面波基底, PW, PW+PP]
topic: density functional theory
unit: U02
order: "basis-sets-1-01"
kind: method
sources:
  - "[[來源-basis-sets-1]]"
prereqs: ["[[basis set]]", "[[Bloch's theorem]]"]
tags: [U02]
---

# plane-wave basis set

## Definition
plane-wave basis set（平面波基底）：用平面波 $e^{i(\vec k+\vec K)\cdot\vec r}$ 當基底函數來展開 Kohn-Sham 軌域。出發點是「原子的集合是稍微變形的自由電子」（[[來源-basis-sets-1]] slides 27、59）。

## Mathematical form
由 [[Bloch's theorem]]，軌域可寫成平面波的和（[[來源-basis-sets-1]] slide 37）：
$$
\psi^n_{\vec k}(\vec r)=\sum_{\vec K}c^{n,\vec k}_{\vec K}\,e^{i(\vec k+\vec K)\cdot\vec r}
$$
符號說明：
- $\vec K$：reciprocal lattice vector；
- $\vec k$：第一 Brillouin zone 內的波向量；
- $n$：能帶指標。

實際計算時用 [[cutoff energy]] 截斷這個和。

## Physical meaning
- 要先理解的觀念（[[來源-basis-sets-1]] slide 27）：
  - Fourier transform、reciprocal space、plane waves、reciprocal lattice；
  - Wigner-Seitz cell 與 Brillouin zone、Bloch's theorem。
- 優點（[[來源-basis-sets-1]] slides 58–59）：
  - 非常適合週期系統（晶體、溶液）；
  - 所有元素用同一組基底；
  - 收斂性容易測試（只要加大 cutoff）。
- 缺點（[[來源-basis-sets-1]] slides 58–59）：
  - 孤立分子要在周圍放很大的真空；
  - 需要 pseudopotential，而它可能帶來不物理的假象。
- 程式：VASP、Quantum ESPRESSO 等（[[來源-basis-sets-1]] slide 63）。

## Figure
無

## Validity and common misconceptions
- 平面波不像原子軌域，所以描述原子核附近的陡峭特徵需要大量平面波，因此通常搭配 [[pseudopotential]]（[[來源-basis-sets-1]] slides 49–57）。

## Related equations
- [[generalized eigenvalue problem HC=SCE]]

## Related concepts
- 上層：[[basis set]]
- 相關：[[Bloch's theorem]]、[[k-point sampling]]、[[cutoff energy]]、[[pseudopotential]]

## Conflicts and differences

## Supplementary notes (not from source)
- reciprocal space、reciprocal lattice、Brillouin zone 會在 electronic structure 單元正式介紹，到時候再開頁。

## Sources
- 原站：https://www.compmatphys.org/topics/optional-basis-sets-in-more-depth/
