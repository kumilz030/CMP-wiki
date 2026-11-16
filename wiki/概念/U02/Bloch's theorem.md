---
type: 概念
aliases: [Bloch 定理, Bloch function, Bloch 函數]
topic: density functional theory
unit: U02
order: "basis-sets-1-02"
kind: theorem
sources:
  - "[[來源-basis-sets-1]]"
prereqs: []
tags: [U02]
---

# Bloch's theorem

## Definition
Bloch's theorem（Bloch 定理）：週期晶體中的單粒子波函數，可以寫成一個平面波乘上一個具有晶格週期性的函數 $u$，平面波的波向量 $\vec k$ 在第一 Brillouin zone 內（[[來源-basis-sets-1]] slide 37）。

## Mathematical form
$$
\Psi(\vec r)=e^{i\vec k\cdot\vec r}\,u^n_{\vec k}(\vec r)
$$
（[[來源-basis-sets-1]] slide 37）

符號說明：
- $u^n_{\vec k}(\vec r)$ 具有正晶格的週期性；
- $\vec k$ 與能帶指標 $n$ 可以當成這個單粒子波函數的量子數，寫成 $\Psi^n_{\vec k}(\vec r)$。

## Physical meaning
- 波函數本身不需要有晶格週期性，只有密度需要（[[來源-basis-sets-1]] slide 36）。
- 因為 $u$ 有週期性，可以展開成平面波，所以整個波函數也能寫成平面波的和。這就是 [[plane-wave basis set]] 的基礎（[[來源-basis-sets-1]] slide 37）。
- 需要的基底函數仍然是無限多（[[來源-basis-sets-1]] slide 37），所以要截斷，見 [[cutoff energy]]。

## Figure
無

## Validity and common misconceptions
- 只適用於週期系統（完美晶體）；有缺陷或表面時，要用 supercell 恢復週期性（後面單元）。這是一般知識的預告。

## Related equations
- 無

## Related concepts
- 相關：[[plane-wave basis set]]、[[k-point sampling]]

## Conflicts and differences

## Supplementary notes (not from source)
- 這裡在 basis set 的脈絡下介紹；electronic structure 單元會再談 $\vec k$ 與能帶指標作為「晶體的量子數」。

## Sources
- 原站：https://www.compmatphys.org/topics/optional-basis-sets-in-more-depth/
