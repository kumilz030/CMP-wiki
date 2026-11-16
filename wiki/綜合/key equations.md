---
type: 綜合
aliases: [方程式總表]
topic: 綜合
sources: []
tags: []
---

# key equations

每條式子一行：名稱、式子、成立條件、頁面。匯入時更新。

## U01 Setting the stage
| 名稱 | 式子 | 成立條件 | 頁面 |
|---|---|---|---|
| Schrödinger equation（只出現在動機說明） | $\hat H\Psi=E\Psi$ | 非相對論、定態；U02 再詳細處理 | [[ab initio]] |
| 玩具晶體的 total energy | $E_{tot}=\left(-3\sqrt2+2\right)e^2/d\approx-2.24\,e^2/d$ | 古典點電荷、二維、只算 nn 與 nnn 電荷對、Gaussian 單位制 | [[total energy]] |

## U02 Density functional theory
| 名稱 | 式子 | 成立條件 | 頁面 |
|---|---|---|---|
| 固體的 Hamiltonian | 原子核動能＋電子動能＋核–核＋電子–電子＋電子–原子核（SI） | 非相對論、只有靜電作用 | [[Hamiltonian of a solid]] |
| external potential | $V_{ext}(\vec r)=\frac{1}{4\pi\varepsilon_0}\sum_A\frac{eZ_A}{\lvert\vec r-\vec R_A\rvert}$ | 原子核固定（BO） | [[external potential]] |
| electron density | $\rho(\vec r)=\sum_i^N\lvert\phi_i(\vec r)\rvert^2$ | Kohn-Sham（或單電子波函數）形式 | [[electron density]] |
| HK 能量泛函 | $E_{V_{ext}}[\rho]=F_{HK}[\rho]+\int\rho V_{ext}\,d\vec r$ | 基態 | [[second Hohenberg-Kohn theorem]] |
| Kohn-Sham equations | $\hat H_{KS}\phi_i=\epsilon_i\phi_i$，$\hat H_{KS}=\hat T_0+\hat V_H+\hat V_{ext}+\hat V_{xc}$ | BO、基態、非相對論；$E_{xc}$ 需近似 | [[Kohn-Sham equations]] |
| LDA | $E^{LDA}_{xc}[\rho]=\int\rho\,\varepsilon_{xc}(\rho)\,d\vec r$ | postulate | [[local density approximation]] |
| basis set 展開 | $\phi_i=\sum_\alpha c^i_\alpha\chi_\alpha$ | 截斷到 $M$ 項 | [[basis set]] |
| 廣義本徵值問題 | $HC=SCE$ | 有限基底；正交時 $S=I$ | [[generalized eigenvalue problem HC=SCE]] |
| Bloch's theorem | $\Psi(\vec r)=e^{i\vec k\cdot\vec r}u^n_{\vec k}(\vec r)$ | 週期系統 | [[Bloch's theorem]] |
| plane-wave cutoff | $\frac12\lvert\vec K\rvert^2\le E_{max}$ | 原子單位（Ha） | [[cutoff energy]] |
