# Card: Kohn-Sham equations

- wiki: `wiki/方程式/Kohn-Sham equations.md`（type: 方程式）
- 網站：https://kumilz030.github.io/CMP-wiki/方程式/Kohn-Sham-equations
- aliases: Kohn-Sham 方程式, KS equations

## Equation
$$
\hat H_{KS}\,\phi_i=\epsilon_i\,\phi_i,\qquad
\rho(\vec r)=\sum_{i=1}^{N}\phi_i^*(\vec r)\,\phi_i(\vec r)
$$
$$
\hat H_{KS}=\hat T_0+\hat V_H+\hat V_{ext}+\hat V_{xc}
=-\frac{\hbar^2}{2m_e}\nabla_i^2+\frac{e^2}{4\pi\varepsilon_0}\int\frac{\rho(\vec r')}{|\vec r-\vec r'|}\,d\vec r'+V_{ext}+V_{xc}
$$
$$
V_{xc}=\frac{\delta E_{xc}[\rho]}{\delta\rho}
$$
（[[來源-AW03C]] slide 2）

符號說明（SI）：
- $\phi_i$：Kohn-Sham 軌域，取能量最低的 $N$ 個；$\epsilon_i$：對應的本徵值；
- $\hat T_0$：不交互作用粒子的動能；
- $\hat V_H$：Hartree potential，見 [[Hartree potential]]；
- $V_{ext}$：external potential，見 [[external potential]]；
- $V_{xc}$：exchange-correlation potential。講義把 XC **能量**泛函寫成 $V_{xc}[\rho]$，本知識庫寫成 $E_{xc}[\rho]$，見 [[exchange-correlation functional]]。

## Conditions of validity
- Born-Oppenheimer approximation（原子核固定）。
- 基態（HK 定理只保證基態密度）。
- 非相對論（Schrödinger 而非 Dirac）。
- 用精確的 $E_{xc}[\rho]$ 時，得到的密度是精確的基態密度；實際上 $E_{xc}$ 必須近似（LDA、GGA…），結果因此是近似的。
- 講義的寫法沒有自旋指標（自旋未極化的形式）。

## Origin
- 依據 [[second Hohenberg-Kohn theorem]]，把總能量泛函對密度最小化，並用一組不交互作用粒子的軌域來表示密度；所有無法精確處理的部分都歸進 $E_{xc}$。這是 [[Kohn-Sham scheme]] 的推導脈絡，講義沒有寫出完整推導。
- Kohn 與 Sham，1965（[[來源-AW03C]] 主題頁）。

## How to use
- $\hat H_{KS}$ 依賴 $\rho$，$\rho$ 又依賴 $\hat H_{KS}$ 的解，所以必須用 [[self-consistent field]] 迭代求解（[[來源-AW03G]] slides 7–8）。
- 把 $\phi_i$ 展開成 [[basis set]] 後，變成矩陣問題 [[generalized eigenvalue problem HC=SCE]]（[[來源-AW03G]] slides 5–6）。

## Common mistakes
- 把 $\phi_i$ 當成真實電子的波函數，或把 $\epsilon_i$ 當成真實電子的能量。它們是 quasi-particles（準粒子）的軌域與能量（[[來源-AW03C]] slide 3）；只有密度（以及由它得到的基態性質）有嚴格的意義。
- 把所有本徵值加起來當成總能量：$\sum_i\epsilon_i$ 不等於總能量（一般知識，講義沒有談）。

## Conflicts and differences
- 符號：講義用 $V_{xc}[\rho]$ 表示 XC 能量泛函，又用 $V_{xc}=\delta V_{xc}[\rho]/\delta\rho$ 表示位勢，同一個字母有兩種意思（[[來源-AW03C]] slide 2）。本知識庫統一寫成 $E_{xc}[\rho]$ 與 $V_{xc}(\vec r)$。
