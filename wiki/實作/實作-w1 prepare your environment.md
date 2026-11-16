---
type: 實作
aliases: [準備計算環境, let's play w1]
topic: 實作
unit: U01
software: Quantum ESPRESSO
sources:
  - "[[來源-lets-play-w1]]"
  - "[[來源-AW01H]]"
  - "[[來源-AW01G]]"
tags: [U01]
---

# Hands-on: prepare your environment (w1)

## Goal
在自己的電腦上準備好一個能用的 DFT 程式（Quantum ESPRESSO），供之後各單元的實作使用（[[來源-lets-play-w1]] 主題頁）。課程要求在下一次回饋 webinar 之前完成（[[來源-AW01H]] 主題頁）。

## Prerequisites
- 知道課程使用 [[Quantum ESPRESSO]]，以及為什麼用 [[virtual machine]]。
- 一台一般的電腦就夠：課程的計算不吃重，在 virtual machine 裡跑也沒關係（[[來源-lets-play-w1]] 主題頁）。

## Input highlights
- 這一步還沒有 DFT 輸入檔。

## Procedure
1. 依作業系統選擇 virtual machine 的方式（[[來源-lets-play-w1]] 主題頁）：
   - Windows、Linux、Intel Mac：VirtualBox＋Quantum Mobile；
   - Apple M1 等 ARM 晶片：Docker 版的 Quantum Mobile，或 UTM 虛擬機。
2. 照原站的「virtual machine for Quantum Espresso (installation instructions)」連結安裝（[[來源-lets-play-w1]] 主題頁）。
3. 記下自己的計算資源：CPU 型號、時脈、RAM、核心數（[[來源-AW01G]] 主題頁）。
4. 收藏 help section 的資源：QE 官網、文件、輸入關鍵字表、pseudopotential 資料庫（SSSP）（[[來源-lets-play-w1]] 主題頁）。

## Expected results
- 打開 virtual machine 後，有一個可以執行 Quantum ESPRESSO 的 Linux 環境，和其他學員的環境完全相同（[[來源-lets-play-w1]] 主題頁）。

## Pitfalls
- 程式在 virtual machine 裡會比較慢，這是正常的；之後做研究時要改用計算中心（[[來源-lets-play-w1]] 主題頁）。
- M1 Mac 不能用 VirtualBox（[[來源-lets-play-w1]] 主題頁）。

## Related concepts
- [[virtual machine]]、[[Quantum ESPRESSO]]、[[parallelization]]

## Supplementary notes (not from source)
- 在原生 Linux 上也可以直接安裝 Quantum ESPRESSO（例如用套件管理員或 conda），但這不是課程建議的做法，跟著課程走時遇到問題比較難比對。

## Sources
- 原站：https://www.compmatphys.org/topics/setting-the-stage-prepare-your-environment/
- 原站：https://www.compmatphys.org/topics/setting-the-stage-help-section/
