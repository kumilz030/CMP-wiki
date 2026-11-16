---
type: 概念
aliases: [平行化, parallel computing, 平行計算, FLOPS, TOP500]
topic: setting the stage
unit: U01
order: "AW01G-02"
kind: concept
sources:
  - "[[來源-AW01G]]"
prereqs: ["[[Moore's law]]"]
tags: [U01]
---

# parallelization

## Definition
parallelization（平行化）：把計算分給很多處理器核心同時執行。在 clock speed 停滯之後，靠平行化讓 wall time（實際耗時）的計算速度持續提升（[[來源-AW01G]] slide 6）。

## Mathematical form
衡量指標是 FLOPS（每秒浮點運算次數）；講義的圖是歷年最快電腦的 Rmax（實測 FLOPS），縱軸從 $10^{-3}$ 到 $10^{20}$，呈對數直線上升（[[來源-AW01G]] slide 6）。
- 1 PFLOPS $=10^{15}$ FLOPS。

## Physical meaning
- 計算科學的獨特之處：用 N. Marzari 的話說，計算科學的「實驗室」每 2 年就倍增，這在顯微鏡或光譜儀上做不到（[[來源-AW01G]] slide 7）。講義舉的例子：
  - 15 年前的頂尖論文，現在是課堂上的練習；
  - 一台像樣的 HPC 系統，一天就能重做 1995 年以前所有的計算文獻（[[來源-AW01G]] slide 7）。
- TOP500 每年更新 2 次，列出全球最快的 500 台電腦（[[來源-AW01G]] slide 10）。
  - 講義當時的第一名是 Sunway TaihuLight（中國無錫）：約 1065 萬核心、93 PFLOPS、耗電 15.4 MW（[[來源-AW01G]] slide 10）。
  - 主題頁另外連到 2026 年第一名的資訊（[[來源-AW01G]] 主題頁）。
- 一般人能用到最快的電腦，通常是學校的計算叢集，或區域、國家級計算中心（[[來源-AW01G]] 主題頁）。

## Figure
無（講義的圖來自外部網站，不轉載）

## Validity and common misconceptions
- 平行化的速度提升有前提：程式要能把工作切開。不是每一種計算都能隨核心數線性加速。這是一般知識，講義沒有討論。

## Related equations
- 無

## Related concepts
- 上層：[[Moore's law]]
- 相關：[[Quantum ESPRESSO]]、[[virtual machine]]
- 邏輯鏈：[[quantum mechanics plus computing power enables materials simulation]]

## Conflicts and differences
- TOP500 第一名會變：講義是 Sunway TaihuLight，主題頁連到的是 2026 年的第一名（[[來源-AW01G]] slide 10；[[來源-AW01G]] 主題頁）。

## Supplementary notes (not from source)

## Sources
- 原站：https://www.compmatphys.org/topics/hardware/
