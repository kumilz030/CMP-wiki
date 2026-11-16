---
type: 來源
code: basis-sets-2
unit: U02
url: https://www.compmatphys.org/topics/optional-basis-sets-in-more-depth/
raw:
  - 2_LAPW-PAW_2014_handouts_3p.pdf
date_added: 2026-11-16
tags: [U02, optional]
---

# (optional) basis sets in more depth · part 2: LAPW and PAW

## Basic info
- 原站主題頁：https://www.compmatphys.org/topics/optional-basis-sets-in-more-depth/
- 講義：`2_LAPW-PAW_2014_handouts_3p.pdf`（本機，不公開；67 張投影片，2014 年版，選讀）
- 單元：U02 density functional theory

## Summary
1. 平面波 basis 很大，是因為原子核附近波函數有陡峭的特徵；粗估 Ca 的 3s 就要 108 個平面波。兩種解法（[[來源-basis-sets-2]] slide 4）：
   - 用 pseudopotential 把陡峭特徵去掉；
   - 改用本身就帶有陡峭特徵的基底函數。
2. volume partitioning（[[來源-basis-sets-2]] slides 6–8）：
   - 原子核附近的電子幾乎像自由原子，用類原子的基底最有效率；
   - 離原子核遠處密度平滑、接近自由電子，需要的平面波少得多；
   - 如果把核附近的區域取成球，就叫 muffin-tin spheres；
   - 實現這個想法的方法有 APW、LAPW、APW+lo、LMTO，以及 PAW。
3. APW：球外是平面波，球內是原子型函數，在球面上接起來；但球內函數依賴能量，帶來額外的迴圈（[[來源-basis-sets-2]] slides 10–19）。
4. LAPW：把球內函數在猜測的能量 $E_0$ 附近做 Taylor 展開（linearization），兩組係數由球面上的值與斜率連續決定，得到不依賴能量的基底（[[來源-basis-sets-2]] slides 21–24）。
   - $E_0$ 要接近本徵值，所以對不同原子、不同 $\ell$ 取不同的值；必要時加上 local orbitals（LO）（[[來源-basis-sets-2]] slides 25–26）；
   - 之後的流程和 PW+PP 相同：選精度參數、算 $H$ 與 $S$ 矩陣元素、對角化（[[來源-basis-sets-2]] slide 27）。
5. APW+lo 保留 LAPW 的準確度，但基底較小，快約 10 倍（[[來源-basis-sets-2]] slide 29）。
6. PP+PW 與 LAPW 比較（[[來源-basis-sets-2]] slide 30）：
   - 平均速度相當；
   - PW+PP 數學簡單、benchmark 多，新理論通常先在 PP 程式裡實作；
   - LAPW 不用先測 pseudopotential，是準確度的「golden standard」，也能直接處理原子核附近的效應；
   - 最好的建議通常是「用你最熟的方法」。
7. LMTO 的想法和 LAPW 類似，但把球內原子解接到 Hankel functions；對緊密堆積的固體可以很快（[[來源-basis-sets-2]] slide 31）。
8. PAW（projector augmented wave）（[[來源-basis-sets-2]] slides 34–49）：
   - 把 KS 軌域改寫成三項的和，每一項都能方便地用某種基底表示；
   - 做法是選定 pseudo wave function、all-electron partial waves、pseudo partial waves 與 projector functions，得到轉換算符，再解轉換後的 KS 方程式；
   - projector 的選擇決定 pseudo 波函數多平滑、平面波 basis 多小；產生好的 projector 有點像產生好的 pseudopotential，是一門藝術。
9. 附錄（Lejaeghere et al. 2014）：以 PBE 計算元素晶體與實驗比較（[[來源-basis-sets-2]] slides 56–58、67）：
   - 平衡體積系統性高估約 3.8%；
   - bulk modulus 系統性低估約 4.7%；
   - PAW 與 LAPW（APW+lo）的預測非常接近。
10. 比較兩個程式時用 $\Delta$ 值（兩條 $E(V)$ 曲線之間的面積）；例如 VASP（PAW）對 WIEN2k（APW+lo）$\Delta=1.8$ meV/atom（[[來源-basis-sets-2]] slides 59–60）。

## Notation
| 這份來源 | 知識庫統一符號 | 意義 |
|---|---|---|
| $E_0$ | $E_\ell$ | LAPW 的 linearization energy |
| $\Delta$ | $\Delta$ | 兩個程式的 $E(V)$ 曲線差異指標（meV/atom） |

## Pages created or updated
- 新增：[[augmented plane wave methods]]、[[projector augmented wave method]]
- 更新：[[all-electron method]]、[[pseudopotential]]

## Quizzes and exercises
- 無

## To verify
- 無
