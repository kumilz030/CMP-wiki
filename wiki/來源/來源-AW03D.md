---
type: 來源
code: AW03D
unit: U02
url: https://www.compmatphys.org/topics/xc-functional/
raw:
  - AW03D_exchange-correlation_handouts.pdf
date_added: 2026-11-16
tags: [U02]
---

# AW03D · XC-functional

## Basic info
- 原站主題頁：https://www.compmatphys.org/topics/xc-functional/
- 講義：`AW03D_exchange-correlation_handouts.pdf`（本機，不公開；4 張投影片）
- 影片：Vimeo 1 支（主講）；另有 John Perdew 解釋 Jacob's ladder 的選看影片等；字幕：無
- 選讀：Mattson（2002）在 *Science* 的 Perspective，談尋找「divine」exchange-correlation functional。屬於外部著作，下載在本機但不匯入內容。
- 預估時間：35 分鐘
- 單元：U02 density functional theory

## Summary
1. 主題頁說，這支影片講 XC-functional 是什麼、最簡單的幾種怎麼建構，以及 XC-functional 的階層（[[來源-AW03D]] 主題頁）。
2. 一定存在一個唯一的 $V_{xc}[\rho]$，但它的形式未知。真正的泛函會非常「病態」，因為它要能解釋所有固態物理與所有化學，沒有希望寫成封閉式。所以只能猜，去找能抓住真實泛函大部分特徵的封閉式（[[來源-AW03D]] slide 2）。
3. Local Density Approximation（LDA，局域密度近似）是一個「postulate」：$V_{xc}^{LDA}[\rho]=\int\rho(\vec r)\,\varepsilon_{xc}(\rho(\vec r))\,d\vec r$。圖示是把空間切成小體積，每一小塊用相同密度的均勻電子氣的 $\varepsilon_{xc}$（[[來源-AW03D]] slide 2）。
4. 延伸：Generalized Gradient Approximation（GGA，廣義梯度近似）（[[來源-AW03D]] slide 2）。
5. 講義用一張不連續、跳來跳去的 $E_{V_{xc}}$ 對 $\rho$ 圖，示意真正的 XC 泛函可能多病態。它依建構必然存在，但要完全掌握它，等於要完全掌握固態物理與化學。我們只能「希望」存在簡單的解析式，能對盡量多的密度逼近它（[[來源-AW03D]] slide 3）。
6. 選讀：一篇關於尋找 universal XC-functional 的綜述（arXiv:1212.0944）（[[來源-AW03D]] slide 4）。
7. 主題頁請學員讀完 Mattson 的文章後，在討論區用自己的話解釋 DFT 的「Jacob's ladder」（[[來源-AW03D]] 主題頁）。

## Notation
| 這份來源 | 知識庫統一符號 | 意義 |
|---|---|---|
| $V_{xc}[\rho]$ | $E_{xc}[\rho]$ | exchange-correlation 能量泛函（講義寫成 $V_{xc}$） |
| $\varepsilon_{xc}(\rho)$ | $\varepsilon_{xc}(\rho)$ | 均勻電子氣每個電子的 XC 能量 |
| $r_s$ | $r_s$ | 講義附圖橫軸，Wigner-Seitz 半徑（以 bohr 為單位） |

## Pages created or updated
- 新增：[[exchange-correlation functional]]、[[local density approximation]]、[[generalized gradient approximation]]

## Quizzes and exercises
- 討論區問題（不公開答案）：用自己的話解釋 DFT 的 Jacob's ladder。

## To verify
- Jacob's ladder 的內容在 Mattson 的文章與 Perdew 的影片中，講義沒有。
