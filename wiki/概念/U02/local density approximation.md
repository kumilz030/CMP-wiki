---
type: 概念
aliases: [LDA, 局域密度近似]
topic: density functional theory
unit: U02
order: "AW03D-02"
kind: approximation
sources:
  - "[[來源-AW03D]]"
  - "[[來源-AW03F]]"
prereqs: ["[[exchange-correlation functional]]"]
tags: [U02]
---

# local density approximation

## Definition
Local Density Approximation（LDA，局域密度近似）：**假設**（postulate）每一小塊空間的 XC 能量，等於相同密度的均勻電子氣的 XC 能量（[[來源-AW03D]] slide 2）。

## Mathematical form
$$
E_{xc}[\rho]\;\Rightarrow\;E_{xc}^{LDA}[\rho]=\int\rho(\vec r)\,\varepsilon_{xc}\big(\rho(\vec r)\big)\,d\vec r
$$
（[[來源-AW03D]] slide 2；講義寫成 $V_{xc}$）

符號說明：$\varepsilon_{xc}(\rho)$ 是密度為 $\rho$ 的均勻電子氣中每個電子的 XC 能量。講義附圖畫的是 $\varepsilon_{xc}$ 對 $r_s$（bohr，對數軸）的曲線，單位是 Ry（[[來源-AW03D]] slide 2）。

## Physical meaning
- 圖示是把空間切成小體積，每一小塊依它的局部密度 $\rho$，查均勻電子氣的 $\varepsilon_{xc}$（[[來源-AW03D]] slide 2）。
- LDA 含有部分 exchange 與部分 correlation，所以解 KS 方程式得到的是近似結果；要改進「需要黑魔法」（[[來源-AW03F]] slides 4–5）。

## Figure
無

## Validity and common misconceptions
- 它是一個「postulate」，不是推導出來的（[[來源-AW03D]] slide 2）。最自然的適用情況是密度變化緩慢的系統；在原子的「表面」與分子的重疊區域，近似最差（一般知識；teaser 完整版也引用了 Kohn-Sham 1965 原文中類似的說法）。

## Related equations
- [[Kohn-Sham equations]]

## Related concepts
- 上層：[[exchange-correlation functional]]
- 相關：[[generalized gradient approximation]]、[[HF versus DFT]]

## Conflicts and differences

## Supplementary notes (not from source)
- 一般知識：LDA 常低估晶格常數、高估結合能（overbinding）；GGA（例如 PBE）通常修正一部分。

## Sources
- 原站：https://www.compmatphys.org/topics/xc-functional/
