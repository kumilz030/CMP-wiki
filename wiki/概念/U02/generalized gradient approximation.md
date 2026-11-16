---
type: 概念
aliases: [GGA, 廣義梯度近似, PBE, Perdew-Burke-Ernzerhof]
topic: density functional theory
unit: U02
order: "AW03D-03"
kind: approximation
sources:
  - "[[來源-AW03D]]"
  - "[[來源-lets-play-w3a]]"
  - "[[來源-lets-play-w3b]]"
  - "[[來源-basis-sets-2]]"
prereqs: ["[[local density approximation]]"]
tags: [U02]
---

# generalized gradient approximation

## Definition
Generalized Gradient Approximation（GGA，廣義梯度近似）：LDA 的延伸（[[來源-AW03D]] slide 2）。Perdew-Burke-Ernzerhof（PBE）是常用的 GGA XC-functional（[[來源-lets-play-w3a]] slide 1）。

## Mathematical form
講義只寫了名稱，沒有寫出式子（[[來源-AW03D]] slide 2）。

## Physical meaning
- 在 Quantum ESPRESSO 中用 `input_dft='PBE'` 選擇（[[來源-lets-play-w3a]] slide 1）。
- 本課程的實作一律使用 PBE，除非另有說明（[[來源-lets-play-w3b]] slide 3）。
- 準確度（Lejaeghere et al. 2014，元素晶體）：PBE 的平衡體積系統性高估約 3.8%，bulk modulus 系統性低估約 4.7%（[[來源-basis-sets-2]] slides 57–58）。

## Figure
無

## Validity and common misconceptions
- pseudopotential 要和選的 GGA 一致：PBE 計算就用 PBE 的 pseudopotential（[[來源-lets-play-w3b]] slide 3）。

## Related equations
- 無

## Related concepts
- 上層：[[exchange-correlation functional]]
- 相關：[[local density approximation]]、[[pseudopotential]]
- 實作：[[實作-w3 convergence testing]]

## Conflicts and differences

## Supplementary notes (not from source)
- 一般知識：GGA 的 $\varepsilon_{xc}$ 除了局部密度 $\rho$ 之外，還用到密度梯度 $\nabla\rho$，所以叫「gradient」approximation。

## Sources
- 原站：https://www.compmatphys.org/topics/xc-functional/
