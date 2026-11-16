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
從多體 Schrödinger 方程式到可解的 Kohn-Sham 方程式，以及數值求解。依課程順序閱讀：

### Concepts: the problem
- [[density functional theory]]（DFT）：把多體 Schrödinger 方程式換成單粒子 Kohn-Sham 方程式
- [[functional]]（泛函）：把函數對應到數；泛函導數
- [[three levels of approximation]]（三層近似）：exact → Born-Oppenheimer → HF 或 DFT → 數值求解 → prediction
- [[Born-Oppenheimer approximation]]（BO 近似）：凍結原子核；level 1
- [[Hartree-Fock method]]（HF）：Slater determinants 中能量最低者；精確 exchange、無 correlation
- [[Slater determinant]]（Slater 行列式）：自動反對稱的多電子波函數
- [[post-Hartree-Fock methods]]（後 HF）：CCSD(T)、MP2、CI…；小系統、高準確度
- [[external potential]]（外位勢）：原子核產生的電位 $V_{ext}(\vec r)$
- [[electron density]]（電子密度）：在 $\vec r$ 找到任一電子的機率

### Concepts: the theory
- [[first Hohenberg-Kohn theorem]]（HK1）：基態密度 ↔ 外位勢一對一
- [[second Hohenberg-Kohn theorem]]（HK2）：能量泛函在基態密度有最小值；$F_{HK}$
- [[Kohn-Sham scheme]]（Kohn-Sham 方法）：不交互作用的準粒子精確重現密度
- [[Hartree potential]]（Hartree 位勢）：電子平均電荷分布的 Coulomb 位勢
- [[exchange-correlation functional]]（XC 泛函）：唯一的本質近似
- [[local density approximation]]（LDA）：均勻電子氣的局部近似
- [[generalized gradient approximation]]（GGA、PBE）：課程實作預設
- [[exchange and correlation]]（交換與相關）：Hartree product → Slater determinant → exact

### Concepts: solving the equations
- [[basis set]]（基底組）：展開軌域，問題變成矩陣代數
- [[self-consistent field]]（SCF）：ρ → V_eff → φ → ρ 的迭代
- [[all-electron method]]（全電子方法）：用像結果的基底（LAPW…）
- [[pseudopotential]]（贗勢）：只在價電子區域和真實晶體一樣
- [[plane-wave basis set]]（平面波基底）：週期系統的標準選擇
- [[Bloch's theorem]]（Bloch 定理）：$\Psi=e^{i\vec k\cdot\vec r}u(\vec r)$
- [[k-point sampling]]（k-mesh）：Brillouin zone 積分的有限取樣
- [[cutoff energy]]（截斷能）：平面波 basis 大小；`ecutwfc`、`ecutrho`
- [[augmented plane wave methods]]（APW、LAPW、APW+lo、LMTO）：muffin-tin 分區
- [[projector augmented wave method]]（PAW）
- [[convergence testing]]（收斂測試）：每種新晶體都要做

### Equations and derivations
- [[Hamiltonian of a solid]]：固體的 5 項 Hamiltonian
- [[Kohn-Sham equations]]：$\hat H_{KS}\phi_i=\epsilon_i\phi_i$
- [[generalized eigenvalue problem HC=SCE]]：引入 basis set 後的矩陣問題
- [[推導-first Hohenberg-Kohn theorem]]：反證法＋變分原理
- [[推導-HC=SCE from a basis set expansion]]：用兩個基底函數示範

### Synthesis and quizzes
- [[HF versus DFT]]：post-HF 與 DFT 的比較
- [[習題-AW02F external potential of O2]]：外位勢的 5 種正確寫法

### Sources
- [[來源-AW02A]] a DFT teaser
- [[來源-AW02B]] functions and functionals
- [[來源-AW02C]] the Schrödinger equation
- [[來源-AW02D]] the Born-Oppenheimer approximation
- [[來源-AW02E]] (post-)Hartree-Fock method(s)
- [[來源-AW02F]] the external potential；[[來源-AW02F-quiz]] 測驗討論
- [[來源-AW02G]] the electron density
- [[來源-AW03A]] first Hohenberg-Kohn theorem；[[來源-AW03A-bis]] 證明
- [[來源-AW03B]] second Hohenberg-Kohn theorem
- [[來源-AW03C]] Kohn-Sham equations
- [[來源-AW03D]] XC-functional
- [[來源-AW03E]] correlation
- [[來源-AW03F]] Hartree-Fock versus DFT
- [[來源-AW03G]] numerical solution methods；[[來源-AW03G-tris]] all-electron vs. pseudopotential；[[來源-AW03G-bis]] 矩陣代數（選讀）
- [[來源-AW03H]] for later use
- [[來源-basis-sets-1]]、[[來源-basis-sets-2]] (optional) basis sets in more depth
- [[來源-AW03H-teaser]] (optional) back to the teaser
- [[來源-lets-play-w2]]、[[來源-lets-play-w3a]]、[[來源-lets-play-w3b]] let's play w2–w3

## Logic chains
- [[quantum mechanics plus computing power enables materials simulation]]：ab initio → 固體是量子系統 → 方程式解不出來 → 計算能力成長 → rational design（simulation）
- [[HK theorems justify the Kohn-Sham scheme]]：BO → HK1 → HK2 → Kohn-Sham → XC 近似 → basis set ＋ SCF
- [[convergence testing fixes the numerical parameters]]：XC ＋ PP → cutoff 起點 → k-mesh → ecutwfc → ecutrho

## Hands-on
- [[實作-w1 prepare your environment]]：用 virtual machine 準備 Quantum ESPRESSO 環境
- [[實作-w2 a basic calculation]]：矽的第一個 SCF 計算，取出 total energy
- [[實作-w3 convergence testing]]：halite 的 k-mesh 與 cutoff 收斂測試
