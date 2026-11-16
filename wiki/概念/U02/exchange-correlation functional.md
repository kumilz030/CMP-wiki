---
type: 概念
aliases: [XC functional, XC-functional, 交換相關泛函, E_xc, exchange-correlation potential, V_xc, Jacob's ladder]
topic: density functional theory
unit: U02
order: "AW03D-01"
kind: quantity
sources:
  - "[[來源-AW03D]]"
  - "[[來源-AW03C]]"
  - "[[來源-AW03F]]"
  - "[[來源-AW02A]]"
  - "[[來源-lets-play-w3a]]"
prereqs: ["[[Kohn-Sham scheme]]", "[[exchange and correlation]]"]
tags: [U02]
---

# exchange-correlation functional

## Definition
exchange-correlation functional（XC-functional，交換相關泛函）$E_{xc}[\rho]$：Kohn-Sham 方法裡收納所有無法精確處理的部分（exchange 與 correlation）的密度泛函。它對應的位勢是 $V_{xc}=\delta E_{xc}/\delta\rho$（[[來源-AW03C]] slide 2）。

## Mathematical form
$$
V_{xc}(\vec r)=\frac{\delta E_{xc}[\rho]}{\delta\rho(\vec r)}
$$
最簡單的近似是 LDA：$E_{xc}^{LDA}[\rho]=\int\rho(\vec r)\,\varepsilon_{xc}(\rho(\vec r))\,d\vec r$（[[來源-AW03D]] slide 2），見 [[local density approximation]]。

## Physical meaning
- 一定存在一個唯一的 XC-functional，但形式未知。真正的泛函要能解釋所有固態物理與化學，所以會非常「病態」，沒有希望寫成封閉式（[[來源-AW03D]] slide 2）。講義用一張不連續、跳來跳去的能量對密度曲線來示意（[[來源-AW03D]] slide 3）。
- 只能「猜」：找能抓住真實泛函大部分特徵、而且對盡量多的密度都接近的簡單解析式（[[來源-AW03D]] slides 2–3）。最簡單的是 LDA，延伸是 GGA（[[來源-AW03D]] slide 2）。
- 這是 DFT 唯一的本質近似（[[來源-lets-play-w3a]] slide 1），也是 teaser 中「XC?」標的關鍵（[[來源-AW02A]] slide 5）。
- 精確的 $E_{xc}$ 包含精確的 exchange 與 correlation；LDA 只含部分 exchange 與部分 correlation，而且要改進它「需要黑魔法」（[[來源-AW03F]] slides 3–5）。
- 實作：在 Quantum ESPRESSO 用 `input_dft` 選擇（例如 `'LDA'`、`'PBE'`）。pseudopotential 是針對特定 XC 做的，不要混用（[[來源-lets-play-w3a]] slide 1）。

## Figure
無

## Validity and common misconceptions
- 誤解：「LDA 只能用在密度均勻的系統」。它是一個 postulate，實際上對很多固體表現不錯；但準確度無法事先保證（[[來源-AW03F]] slide 13：DFT 有「uncontrolled noise」）。

## Related equations
- [[Kohn-Sham equations]]

## Related concepts
- 上層：[[Kohn-Sham scheme]]
- 子頁：[[local density approximation]]、[[generalized gradient approximation]]
- 相關：[[exchange and correlation]]、[[HF versus DFT]]、[[pseudopotential]]

## Conflicts and differences
- 符號：AW03C、AW03D 的講義把 XC 能量泛函寫成 $V_{xc}[\rho]$（[[來源-AW03D]] slide 2），AW03F 寫成 $E_{xc}[\rho]$（[[來源-AW03F]] slide 3）。本知識庫統一用 $E_{xc}[\rho]$ 表示能量泛函，$V_{xc}(\vec r)$ 表示位勢。

## Supplementary notes (not from source)
- **Jacob's ladder**（主題頁要學員讀 Mattson 2002 的 *Science* Perspective 後自己解釋）：一般的說法是由 Perdew 提出，把 XC 近似依用到的資訊排成階梯：
  - LDA（只用 $\rho$）；
  - GGA（加上 $\nabla\rho$）；
  - meta-GGA（加上動能密度）；
  - hybrid（加入部分精確 exchange）；
  - 再往上用到未佔據軌域。

  越高階通常越準、越貴。這段是一般知識，不是講義內容。
- 講義 slide 4 的選讀（arXiv:1212.0944）是一篇關於「尋找 universal XC functional」的綜述。

## Sources
- 原站：https://www.compmatphys.org/topics/xc-functional/
