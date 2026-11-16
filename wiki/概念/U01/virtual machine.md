---
type: 概念
aliases: [虛擬機, VM, Quantum Mobile]
topic: setting the stage
unit: U01
order: "lets-play-w1-01"
kind: tool
sources:
  - "[[來源-lets-play-w1]]"
prereqs: []
tags: [U01]
---

# virtual machine

## Definition
virtual machine（虛擬機）：在一個作業系統裡模擬另一個作業系統。例如在 Windows 電腦上裝好 virtual machine 後，就有一台 Ubuntu Linux，用起來和真的 Linux 電腦一樣（[[來源-lets-play-w1]] 主題頁）。

## Mathematical form
無

## Physical meaning
- 課程用 virtual machine 提供 DFT 程式，理由是（[[來源-lets-play-w1]] 主題頁）：
  - 每個人的電腦、作業系統、安裝軟體的經驗都不同；
  - 在 virtual machine 裡，每個人的環境完全一樣，出錯時別人可以照同樣的步驟重現。
- 只用於學習：模擬作業系統會占用電腦資源，所以 DFT 程式在 virtual machine 裡一定比較慢。課程的計算不吃重，所以沒關係；真正做研究時通常會改用計算中心（[[來源-lets-play-w1]] 主題頁）。
- virtual machine 由 DFT 程式的開發者製作並測試；Quantum ESPRESSO 用的是 Quantum Mobile（[[來源-lets-play-w1]] 主題頁）。

## Figure
無

## Validity and common misconceptions
- Apple M1（ARM 晶片）不相容 VirtualBox：可以改用 Docker 版的 Quantum Mobile（少一些圖形功能），或 UTM 虛擬機（[[來源-lets-play-w1]] 主題頁）。

## Related equations
- 無

## Related concepts
- 相關：[[Quantum ESPRESSO]]、[[parallelization]]
- 實作：[[實作-w1 prepare your environment]]

## Conflicts and differences

## Supplementary notes (not from source)

## Sources
- 原站：https://www.compmatphys.org/topics/setting-the-stage-prepare-your-environment/
