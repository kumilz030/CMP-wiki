---
type: 概念
aliases: [k-mesh, Brillouin zone sampling, k 點取樣, K_POINTS, Gamma point calculation, Γ point]
topic: density functional theory
unit: U02
order: "basis-sets-1-03"
kind: parameter
sources:
  - "[[來源-basis-sets-1]]"
  - "[[來源-lets-play-w3a]]"
  - "[[來源-lets-play-w3b]]"
  - "[[來源-lets-play-w2]]"
prereqs: ["[[Bloch's theorem]]"]
tags: [U02]
---

# k-point sampling

## Definition
k-point sampling（Brillouin zone sampling，k 點取樣）：密度等性質原本要在 Brillouin zone 的每一個 $\vec k$ 計算，也就是一個積分；實際計算時，用有限個取樣點、各配一個權重 $w_k$ 的 quadrature 來近似（[[來源-basis-sets-1]] slide 43）。

## Mathematical form
$$
\rho(\vec r)=\sum_{\vec k}w_{\vec k}\sum_i n_{i\vec k}\,|\psi_{i\vec k}(\vec r)|^2
$$
（[[來源-basis-sets-1]] slide 43）

符號說明：
- $w_{\vec k}$：取樣點的權重；
- $n_{i\vec k}$：佔據數。

只取 $\vec k=(0,0,0)$（記為 $\Gamma$）的叫 $\Gamma$-point calculation。

## Physical meaning
- 取樣點越多，越接近精確積分（[[來源-lets-play-w3a]] slide 1）。
- $\Gamma$-point 在大單胞、半導體、單一原子或分子時是很好的近似（[[來源-basis-sets-1]] slide 43）：單胞越大，Brillouin zone 越小，少數取樣點就夠了（[[來源-basis-sets-1]] slides 45–46）。
- 在 Quantum ESPRESSO 中，k-mesh 以三維網格設定，例如（[[來源-lets-play-w3a]] slide 1）：
  ```
  K_POINTS {automatic}
   7 7 7 0 0 0
  ```
- 每次 DFT 計算都**必須**確認取樣點夠多：把計算的量對 k-mesh 密度作圖，飽和就代表夠了（[[來源-lets-play-w3a]] slide 1）。

## Figure
無

## Validity and common misconceptions
- k-mesh 太粗時算得很快，但結果可能離譜；只算一次是看不出來的。例如 halite 用 1×1×1 時壓力是 244 kbar，收斂值約 1.1 kbar（[[來源-lets-play-w3b]] slide 4）。
- 但也不能一律用很密的網格：計算時間隨網格密度增加（[[來源-lets-play-w3b]] slide 4）。

## Related equations
- 無

## Related concepts
- 相關：[[Bloch's theorem]]、[[plane-wave basis set]]、[[convergence testing]]、[[cutoff energy]]
- 實作：[[實作-w3 convergence testing]]、[[實作-w2 a basic calculation]]

## Conflicts and differences
- ⚠️待查證：實作文件說 `K_POINTS` 設在 `&ELECTRONS` 區塊（[[來源-lets-play-w3a]] slide 1），但範例輸入檔把它寫在 `ATOMIC_POSITIONS` 之後（[[來源-lets-play-w2]] slide 3）。在 QE 中 `K_POINTS` 是獨立的 card，不屬於 `&ELECTRONS` namelist（依 QE 輸入格式的一般知識），應以範例檔為準。

## Supplementary notes (not from source)
- `7 7 7 0 0 0` 後三個 0 表示網格不位移（Monkhorst-Pack 網格的 offset）。這是 QE 的一般知識。

## Sources
- 原站：https://www.compmatphys.org/topics/density-functional-theory-2-basis-set-size-and-k-mesh/
