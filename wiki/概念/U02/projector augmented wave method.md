---
type: 概念
aliases: [PAW, projector augmented wave, 投影擴增波法]
topic: density functional theory
unit: U02
order: "basis-sets-2-02"
kind: method
sources:
  - "[[來源-basis-sets-2]]"
  - "[[來源-AW03G-tris]]"
  - "[[來源-lets-play-w2]]"
prereqs: ["[[pseudopotential]]", "[[augmented plane wave methods]]"]
tags: [U02]
---

# projector augmented wave method

## Definition
projector augmented wave（PAW）method：把一個 Kohn-Sham 軌域改寫成三項的和，每一項都能方便地用某種基底表示（[[來源-basis-sets-2]] slide 34）。它和 pseudopotential 方法同屬一類（[[來源-AW03G-tris]] slide 12）。

## Mathematical form
PAW Ansatz（[[來源-basis-sets-2]] slide 38）：
$$
\psi_n(\vec r)=\tilde\psi_n(\vec r)+\sum_a\sum_i\big(\phi^a_i(\vec r)-\tilde\phi^a_i(\vec r)\big)\,\langle\tilde p^a_i|\tilde\psi_n\rangle
$$
選定編號的三個物件後，可以寫成三項的和（[[來源-basis-sets-2]] slide 47）：
$$
\psi_n(\vec r)=\tilde\psi_n(\vec r)+\sum_a\psi^a_n(\vec r)-\sum_a\tilde\psi^a_n(\vec r)
$$
- $\tilde\psi$：pseudo wave function，平滑，可用平面波展開；
- $\phi^a_i$、$\tilde\phi^a_i$：原子 $a$ 的 all-electron 與 pseudo partial waves；
- $\tilde p^a_i$：projector functions；
- 求和中 $a$ 跑過單胞內的原子（augmentation spheres），$i$ 跑過基底函數。
## Physical meaning
- 作法（[[來源-basis-sets-2]] slides 38–48）：
  - 選定 pseudo 波函數、all-electron partial waves、pseudo partial waves 與 projectors；
  - 得到一個轉換算符，代入 KS 方程式；
  - 解出 $\tilde\psi$，再組回完整的 all-electron 軌域。
- projector 的選擇決定 pseudo 波函數多平滑，也就決定平面波 basis 多小、計算多快。產生好的 projector 有點像產生好的 pseudopotential，是一門藝術。測試過的 projector 表格，有的是程式的專屬部分（例如 VASP），有的可以跨程式免費使用（[[來源-basis-sets-2]] slide 49）。
- 程式：VASP（[[來源-basis-sets-2]] slide 53）。課程實作用的 Si pseudopotential `Si.pbe-n-kjpaw_psl.1.0.0.UPF` 也是 PAW 型（[[來源-lets-play-w2]] slide 3）。

## Figure
無

## Validity and common misconceptions
- PAW 和 LAPW（APW+lo）對元素晶體的預測非常接近（[[來源-basis-sets-2]] slide 67）。

## Related equations
- [[Kohn-Sham equations]]

## Related concepts
- 上層：[[pseudopotential]]
- 相關：[[augmented plane wave methods]]、[[plane-wave basis set]]

## Conflicts and differences

## Supplementary notes (not from source)
- PAW 由 P. Blöchl（1994）提出；講義 slide 36 引用了他的投影片。檔名中的 `kjpaw` 是一種 PAW 資料集的產生方式（一般知識）。

## Sources
- 原站：https://www.compmatphys.org/topics/optional-basis-sets-in-more-depth/
