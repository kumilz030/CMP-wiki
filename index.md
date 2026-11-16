---
title: Home
---

# CMP-wiki

> 這是 Stefaan Cottenier 的免費線上課程 [*Computational Materials Physics*](https://www.compmatphys.org/courses/compmatphys/) 的個人中文筆記，內容依據該課程的講義整理，並非官方教材。完整內容（影片、講義、練習）請到原站閱讀。

%% 給 AI：回答問題前先讀這份。依單元分類，每頁一行摘要。健檢用的題組見 knowledge base test questions。（Obsidian 註解，網站上不顯示） %%

## Synthesis
- [[key equations]]（方程式總表）：各單元的重要式子、成立條件與頁面
- [[symbols]]（符號對照表）：全庫統一符號與單位制
- [[knowledge base test questions]]（知識庫測試題組）：健檢時重跑

## U01 Setting the stage
為什麼要用量子力學與電腦來研究材料。依課程順序閱讀：

### Concepts
- [[ab initio]]（第一原理）：出發點無法再化約的數學模型；材料的出發點是 $\hat H\Psi=E\Psi$
- [[solid]]（固體）：正原子核＋負電子、電磁交互作用、遵守 quantum physics 的系統
- [[total energy]]（總能量）：玩具晶體的 Coulomb 能量 $E_{tot}\approx-2.24\,e^2/d$；本課程最重要的量之一
- [[crystal structure and microstructure]]（晶體結構與顯微組織）：材料性質＝晶體結構＋顯微組織；本課程主要處理前者
- [[maturity of physics fields]]（物理領域的成熟度）：公理已知但方程式解不出來（Dirac 1929）
- [[materials design from thought]]（從構想設計材料）：從 trial-and-error 走向 rational design
- [[theory versus simulation]]（理論與模擬）：量子材料計算是 simulation（computer experiments）
- [[Moore's law]]（摩爾定律）：計算能力指數成長；時脈約 2005 年後停滯
- [[parallelization]]（平行化）：時脈停滯後靠平行化提速；FLOPS、TOP500
- [[Quantum ESPRESSO]]（QE）：課程使用的 DFT 程式
- [[virtual machine]]（虛擬機）：Quantum Mobile 提供統一的學習環境

### Sources
- [[來源-AW01F-creation]] the creation of materials from thought
- [[來源-AW01B]] the ab initio way
- [[來源-AW01C]] solids as quantum systems
- [[來源-AW01D]] so what's the problem?
- [[來源-AW01E]] advantages
- [[來源-AW01F]] theory versus computation
- [[來源-AW01G]] hardware
- [[來源-AW01H]] software
- [[來源-lets-play-w1]] let's play w1：prepare your environment

## U02 Density functional theory
（尚未匯入）

## Logic chains
- [[quantum mechanics plus computing power enables materials simulation]]：ab initio → 固體是量子系統 → 方程式解不出來 → 計算能力成長 → rational design（simulation）

## Hands-on
- [[實作-w1 prepare your environment]]：用 virtual machine 準備 Quantum ESPRESSO 環境
