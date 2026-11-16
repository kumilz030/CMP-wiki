---
type: 概念
aliases: [QE, Quantum Espresso, NanoLab, VNL]
topic: setting the stage
unit: U01
order: "AW01H-01"
kind: tool
sources:
  - "[[來源-AW01H]]"
  - "[[來源-lets-play-w1]]"
prereqs: []
tags: [U01]
---

# Quantum ESPRESSO

## Definition
Quantum ESPRESSO（QE）：本課程實作使用的 DFT 程式，可以做 ab initio 計算（[[來源-AW01H]] 主題頁）。

## Mathematical form
無

## Physical meaning
- 能解 Schrödinger equation 的程式很多；課程選 QE 的理由是（[[來源-AW01H]] 主題頁）：
  - 口碑好，開發者與使用者社群大；
  - 能在不同電腦與作業系統上執行；
  - 免費（GPL 授權）。
- QE 用命令列操作。課程原本搭配半商業圖形介面 NanoLab（VNL），同一個介面可以操作不同程式（例如 VASP）。但 2019 年起 VNL 不再對學術免費，課程說明已改成不依賴它（[[來源-AW01H]] 主題頁）。
- 課程透過 [[virtual machine]]（Quantum Mobile）提供統一的 QE 環境（[[來源-lets-play-w1]] 主題頁）。
- 文件資源：官網、說明文件、所有輸入關鍵字，以及 pseudopotential 資料庫（包括 SSSP）（[[來源-lets-play-w1]] 主題頁）。

## Figure
無

## Validity and common misconceptions
- 課程允許改用自己熟悉的其他程式，但說明以 QE 為準（[[來源-AW01H]] 主題頁）。

## Related equations
- 無

## Related concepts
- 相關：[[virtual machine]]、[[parallelization]]
- 實作：[[實作-w1 prepare your environment]]

## Conflicts and differences

## Supplementary notes (not from source)
- QE 的能量單位預設是 Rydberg（Ry），之後讀輸出檔時要注意換算（AGENTS.md §3-3）。

## Sources
- 原站：https://www.compmatphys.org/topics/software-2/
