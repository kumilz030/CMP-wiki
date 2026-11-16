---
type: 概念
aliases: [總能量, E_tot]
topic: setting the stage
unit: U01
order: "AW01C-02"
kind: quantity
sources:
  - "[[來源-AW01C]]"
prereqs: ["[[solid]]"]
tags: [U01]
---

# total energy

## Definition
total energy（總能量）$E_{tot}$：系統中所有粒子交互作用能量的總和；講義第一次出現時，是一個玩具晶體每個 cell 的 Coulomb interaction energy，並註明這是本課程會一再出現的重要量（[[來源-AW01C]] slide 17）。

## Mathematical form
二維正負電荷交錯排列的玩具晶體，只算最近鄰（nn）與次近鄰（nnn）電荷對，每個 cell 的能量為：
$$
E_{tot} = \left(-3\sqrt{2} + 2\right)\frac{e^2}{d} \approx -2.24\,\frac{e^2}{d}
$$
符號說明：
- $e$：基本電荷；
- $d$：相鄰正負電荷的距離（晶格參數）；
- 講義用 $e^2/d$ 的寫法，代表採用 Gaussian 單位制，Coulomb 常數吸收進單位裡（[[來源-AW01C]] slides 16–17）。

## Physical meaning
- $E_{tot}<0$ 表示晶體是束縛的（bound），比把電荷分開更穩定（[[來源-AW01C]] slide 18）。
- 下一個問題是：$E_{tot}$ 對 $d$ 的關係給出的最佳晶格參數是多少（[[來源-AW01C]] slide 18）。在之後的單元，「找能量最低的結構」會變成 geometry optimization 的核心；這一句是預告，不是來源內容。

## Figure
無

## Validity and common misconceptions
- 這個式子只是古典 Coulomb 作用的教學用玩具模型（二維、點電荷、只算 nn 與 nnn 電荷對），不是任何真實晶體的能量。
- 真正的 total energy 要用 quantum physics 算（見 [[solid]]）；在 DFT 中它是主要的輸出量之一（U02）。

## Related equations
- 無

## Related concepts
- 上層：[[solid]]
- 相關：[[crystal structure and microstructure]]

## Conflicts and differences

## Supplementary notes (not from source)
- 數值核對：$-3\sqrt2+2 = -2.2426…$，和講義的 $\approx -2.24$ 一致。
- 自己推算時要注意：每個 cell 分到的電荷對數要依共用比例計算，否則會重複計算；講義沒有寫出計算過程。

## Sources
- 原站：https://www.compmatphys.org/topics/solids-as-quantum-systems/
