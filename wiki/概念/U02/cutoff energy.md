---
type: 概念
aliases: [cut-off energy, 截斷能, ecutwfc, ecutrho, basis set size, E_cut, E_max]
topic: density functional theory
unit: U02
order: "basis-sets-1-04"
kind: parameter
sources:
  - "[[來源-basis-sets-1]]"
  - "[[來源-basis-sets-2]]"
  - "[[來源-lets-play-w3a]]"
  - "[[來源-lets-play-w3b]]"
prereqs: ["[[plane-wave basis set]]"]
tags: [U02]
---

# cutoff energy

## Definition
cutoff energy（截斷能）：決定平面波基底大小的參數。只保留動能不超過 $E_{max}$ 的平面波，也就是限制最大的 reciprocal lattice vector（[[來源-basis-sets-1]] slide 51）。

## Mathematical form
$$
\tfrac12|\vec K|^2\le E_{max}
$$
（[[來源-basis-sets-1]] slide 51；原子單位，Hartree）

在邊長 $L$ 的立方盒子中，$\vec K$ 由整數 $(n_1,n_2,n_3)$ 決定，條件等價於 $n_1^2+n_2^2+n_3^2\le E_{max}L^2/(2\pi)^2$。這個形式類似粒子在盒中的推導（[[來源-basis-sets-1]] slide 51）。

## Physical meaning
- 要描述的特徵越陡，需要越多平面波；最快的變化在原子核附近的 core region，來自很硬的原子核位勢（[[來源-basis-sets-1]] slides 49–51）。
- basis 大小只由盒子體積和 cutoff 決定（[[來源-basis-sets-1]] slide 53）：
  - $E_{max}$ 越大：basis 越大、計算越準、也越貴；
  - 相同的 $E_{max}$：盒子越大，需要的平面波越多。
- 粗估：Ca 的 3s 軌域要約 108 個平面波（[[來源-basis-sets-2]] slide 4）。
- Quantum ESPRESSO（單位 Ry）（[[來源-lets-play-w3a]] slide 2）：
  - `ecutwfc`：波函數的 cutoff；
  - `ecutrho`：密度的 cutoff，預設是 `ecutwfc` 的 4 倍；PAW 可能要稍大，ultrasoft pseudopotential 要 8–12 倍。

## Figure
無

## Validity and common misconceptions
- cutoff 必須經過收斂測試，而且是對**物理量**收斂，不只是對能量（[[來源-lets-play-w3b]] slides 4–6）。halite 的例子：
  - `ecutwfc` 從 16 到 200 Ry，壓力從 −5324 kbar 變到 8.0 kbar；
  - 取 90 Ry（`ecutrho`=450 Ry）可在 1 kbar 以內（[[來源-lets-play-w3b]] slides 5–6）。
- pseudopotential 檔頭常有建議的最小 cutoff，可以當起點，但仍要自己測（[[來源-lets-play-w3b]] slide 3）。

## Related equations
- 無

## Related concepts
- 上層：[[plane-wave basis set]]
- 相關：[[basis set]]、[[pseudopotential]]、[[k-point sampling]]、[[convergence testing]]
- 實作：[[實作-w3 convergence testing]]

## Conflicts and differences
- 單位：講義的 $E_{max}$ 是原子單位（Hartree），所以寫成 $\frac12|\vec K|^2$；QE 的 `ecutwfc` 是 Ry（1 Ha = 2 Ry）。

## Supplementary notes (not from source)
- QE 中密度需要較大 cutoff 的原因：密度是波函數的平方，最高 Fourier 分量加倍，動能 cutoff 因此要 4 倍。這是一般知識。

## Sources
- 原站：https://www.compmatphys.org/topics/optional-basis-sets-in-more-depth/
