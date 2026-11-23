# Card: electron density

- wiki: `wiki/概念/U02/electron density.md`（type: 概念）
- 網站：https://kumilz030.github.io/CMP-wiki/概念/U02/electron-density
- aliases: 電子密度, density, ρ(r)

## Definition
electron density（電子密度）$\rho(\vec r)$：在位置 $\vec r$ 找到任一個電子的機率，不管其他 $N-1$ 個電子在哪裡（[[來源-AW02G]] slide 4）。

## Mathematical form
一個電子（[[來源-AW02G]] slide 3）：
$$
\hat\rho(\vec r)=\delta(\vec r'-\vec r),\qquad
\rho(\vec r)=\langle\Psi|\hat\rho(\vec r)|\Psi\rangle=|\Psi(\vec r)|^2
$$
N 個電子（[[來源-AW02G]] slide 4）：
$$
\hat\rho(\vec r)=\sum_{i=1}^{N}\delta(\vec r'-\vec r),\qquad
\rho(\vec r)=\sum_{i=1}^{N}\int\Psi^*(\dots,\vec r_i=\vec r,\dots)\,\Psi(\dots,\vec r_i=\vec r,\dots)\,d\vec r_1\cdots d\vec r_N
$$
積分不包含 $\vec r_i$。只有當 $\Psi$ 能用單電子波函數寫出時，才等於 $\sum_i|\varphi(\vec r_i)|^2$。

Kohn-Sham 形式（[[來源-AW03C]] slide 2）：
$$
\rho(\vec r)=\sum_{i=1}^{N}\phi_i^*(\vec r)\,\phi_i(\vec r)
$$

## Physical meaning
- 不懂晶體的電子密度，就不可能懂 DFT（[[來源-AW02G]] 主題頁）。
- 不論電子有多少個，電子密度都是一個函數；講義用兩個無自旋粒子的練習，問它的定義域與值域（[[來源-AW02G]] slides 5–6）。
- 密度含有的資訊和波函數一樣多，DFT 正是利用這一點，基石是第一 Hohenberg-Kohn 定理（[[來源-AW03H-teaser]] slide 23）。

## Validity and common misconceptions
- 單位與正負號：這頁的 $\rho$ 是機率（數目）密度；在 [[來源-AW02F-quiz]] 的語境中，$\rho$ 是 charge density，要乘上 $-e$。

## Conflicts and differences
- $\rho$ 有兩種用法：機率密度（[[來源-AW02G]] slide 3）與 charge density（[[來源-AW02F-quiz]] slide 1）。引用時要注意單位。
