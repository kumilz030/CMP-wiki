---
type: 來源
code: basis-sets-1
unit: U02
url: https://www.compmatphys.org/topics/optional-basis-sets-in-more-depth/
raw:
  - 1_planewaves_2014_handouts_3p.pdf
date_added: 2026-11-16
tags: [U02, optional]
---

# (optional) basis sets in more depth · part 1: plane waves

## Basic info
- 原站主題頁：https://www.compmatphys.org/topics/optional-basis-sets-in-more-depth/
- 講義：`1_planewaves_2014_handouts_3p.pdf`（本機，不公開；64 張投影片，2014 年版，選讀）
- 影片：Vimeo 10 支（basis set intro、atomic orbital、plane-wave、pseudopotential、APW、LAPW、PAW 等）；字幕：無
- 單元：U02 density functional theory
- 注意：投影片 slides 11 與 21 提到「recapitulation of week 6」等，是舊版課程的週次。

## Summary
1. basis set 的一般概念（[[來源-basis-sets-1]] slides 14–19）：
   - HF 與 DFT 都需要表示單粒子軌域，常用作法是展開成 basis；
   - 單粒子函數空間是無窮維，實際上在夠準時截斷；
   - 展開後問題變成 generalized eigenvalue problem $HC=SCE$，基底正交時 $S$ 是對角矩陣；
   - 矩陣對角化是大多數程式的主要工作，也占掉大部分計算時間。
2. 三大類基底：atomic orbitals、plane waves、augmented plane waves（[[來源-basis-sets-1]] slide 20）。
3. atomic orbital basis（GTO、STO）的出發點是「分子是稍微變形的原子」；可能有 basis set superposition error（BSSE）（[[來源-basis-sets-1]] slides 23–24）。
4. plane-wave basis 的出發點是「原子集合是稍微變形的自由電子」。要用到 Fourier transform、reciprocal space、reciprocal lattice、Brillouin zone、Bloch's theorem 等觀念（[[來源-basis-sets-1]] slides 27–35）。
5. Bloch's theorem：單粒子波函數 $\Psi(\vec r)=e^{i\vec k\cdot\vec r}u^n_{\vec k}(\vec r)$，其中 $u$ 有晶格週期性。$\vec k$（在第一 Brillouin zone 內）和能帶指標 $n$ 可作為量子數；把 $u$ 展開成平面波，波函數就能寫成 $\sum_{\vec K}c^{n,\vec k}_{\vec K}e^{i(\vec k+\vec K)\cdot\vec r}$。只有密度需要晶格週期性，波函數不需要（[[來源-basis-sets-1]] slides 36–37）。
6. Brillouin zone sampling：密度要在 Brillouin zone 的每個 $\vec k$ 計算，實際上用有限個取樣點、各配權重 $w_k$ 的 quadrature 近似。只取 $\vec k=(0,0,0)$ 的叫 $\Gamma$-point calculation，對大單胞、半導體、單一原子或分子是不錯的近似（[[來源-basis-sets-1]] slides 43–46）。
7. basis set size（[[來源-basis-sets-1]] slides 49–54）：
   - 要描述的特徵越陡，需要的平面波越多；
   - 用最大動能截斷：$\frac12|\vec K|^2\le E_{max}$（等於限制最大的倒晶格向量）；
   - 最快的變化在原子核附近的 core region；
   - basis 大小只由盒子體積和 cutoff 決定。$E_{max}$ 越大，basis 越大、越準、越貴；同樣的 $E_{max}$，大的盒子需要更多平面波。
8. pseudopotentials：core electrons 束縛深、局域在核附近、換環境也幾乎不變；valence 波函數為了和 core 正交，在核附近劇烈振盪。PSP 減少要處理的電子數，也大幅減少需要的基底函數（[[來源-basis-sets-1]] slides 55–57）。
9. 平面波的優缺點（[[來源-basis-sets-1]] slides 58–59）：
   - 優點：適合週期系統（孤立分子要包很大的真空）；所有元素用同一組基底；容易測試收斂。
   - 缺點：pseudopotential 可能造成不物理的假象，而且未必出現在預期的性質上。
10. 所以 pseudopotential 需要驗證（Garrity et al. 2014、Lejaeghere et al. 2014）（[[來源-basis-sets-1]] slide 61）。

## Notation
| 這份來源 | 知識庫統一符號 | 意義 |
|---|---|---|
| $\vec K$ | $\vec K$ | reciprocal lattice vector |
| $\vec k$、$n$ | $\vec k$、$n$ | Bloch 波向量（第一 Brillouin zone 內）、能帶指標 |
| $u^n_{\vec k}(\vec r)$ | $u_{n\vec k}(\vec r)$ | 具晶格週期性的 Bloch 函數 |
| $E_{max}$ | $E_{cut}$ | plane-wave cutoff energy（講義用原子單位，$\frac12|\vec K|^2$） |
| $w_k$ | $w_{\vec k}$ | k-point 權重 |

## Pages created or updated
- 新增：[[plane-wave basis set]]、[[Bloch's theorem]]、[[k-point sampling]]、[[cutoff energy]]
- 更新：[[basis set]]、[[pseudopotential]]

## Quizzes and exercises
- 講義內的小練習：k-point sampling 用更多取樣點時會發生什麼（[[來源-basis-sets-1]] slide 44）。

## To verify
- reciprocal space、reciprocal lattice、Brillouin zone 在 U05 electronic structure 會正式介紹，本頁只在 plane-wave 的脈絡下提到。
