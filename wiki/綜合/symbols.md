---
type: 綜合
aliases: [符號對照表]
topic: 綜合
sources: []
tags: []
---

# symbols

全庫統一符號（AGENTS.md §3-4）。同一符號在不同來源意義不同時，在這裡列出。

## Units
- 原子單位（Hartree）、Rydberg（Quantum ESPRESSO 預設）與 SI：1 Ha = 2 Ry ≈ 27.211 eV（一般常數）。講義的 plane-wave cutoff $\frac12|\vec K|^2\le E_{max}$ 用 Hartree，QE 的 `ecutwfc` 用 Ry。見 [[cutoff energy]]。
- U02 講義的 Hamiltonian 用 SI（$\hbar$、$4\pi\varepsilon_0$ 都寫出來）；AW02D 的版本省略常數。見 [[Hamiltonian of a solid]]。
- U01 的玩具晶體能量寫成 $e^2/d$，是 Gaussian 單位制（Coulomb 常數吸收進單位）；SI 要寫成 $e^2/(4\pi\varepsilon_0 d)$。見 [[total energy]]。

## Symbols
| 符號 | 意義 | 單位 | 首次出現 |
|---|---|---|---|
| $\hat H$ | Hamiltonian（漢米爾頓算符） | 能量 | [[ab initio]] |
| $\Psi$ | 波函數 | — | [[ab initio]] |
| $E$ | 能量本徵值 | 能量 | [[ab initio]] |
| $E_{tot}$ | total energy（總能量） | 能量 | [[total energy]] |
| $e$ | 基本電荷 | C（SI） | [[total energy]] |
| $d$ | U01 玩具晶體的相鄰正負電荷距離（晶格參數） | 長度 | [[total energy]] |
| $V_{zz}$ | AW01B 投影片上由 $\hat H\Psi=E\Psi$ 算出的可觀測量（意義待查證） | — | [[ab initio]] |
| $\vec R_A$、$Z_A$、$M_A$ | 第 A 個原子核的位置、原子序、質量 | m、—、kg | [[Hamiltonian of a solid]] |
| $\vec r_i$、$m_e$ | 第 i 個電子的位置、質量 | m、kg | [[Hamiltonian of a solid]] |
| $N$（$N_e$）、$N_n$ | 電子數、原子核數 | — | [[Born-Oppenheimer approximation]] |
| $V_{ext}(\vec r)$ | external potential（電位，不含 $-e$） | V | [[external potential]] |
| $E_{ext}$ | external potential energy | J | [[external potential]] |
| $\rho(\vec r)$ | 電子密度：一般指機率（數目）密度；AW02F 測驗文件中是 charge density（含 $-e$） | m$^{-3}$ | [[electron density]] |
| $\phi_i$、$\epsilon_i$ | Kohn-Sham 軌域與本徵值 | —、能量 | [[Kohn-Sham equations]] |
| $\hat H_{KS}$ | Kohn-Sham Hamiltonian | 能量 | [[Kohn-Sham equations]] |
| $V_H$ | Hartree potential（講義形式含 $e^2$，單位是能量） | J | [[Hartree potential]] |
| $E_{xc}[\rho]$ | exchange-correlation 能量泛函（AW03C、AW03D 講義寫成 $V_{xc}[\rho]$） | 能量 | [[exchange-correlation functional]] |
| $V_{xc}(\vec r)$ | exchange-correlation potential $=\delta E_{xc}/\delta\rho$ | 能量 | [[exchange-correlation functional]] |
| $\varepsilon_{xc}(\rho)$ | 均勻電子氣每個電子的 XC 能量 | 能量 | [[local density approximation]] |
| $F_{HK}[\rho]$ | Hohenberg-Kohn functional（動能＋電子–電子） | 能量 | [[second Hohenberg-Kohn theorem]] |
| $\chi_\alpha$、$c^i_\alpha$ | 基底函數、展開係數 | — | [[basis set]] |
| $H$、$S$、$C$、$E$ | Hamiltonian 矩陣、overlap 矩陣、係數矩陣、本徵值對角矩陣 | — | [[generalized eigenvalue problem HC=SCE]] |
| $\vec k$、$n$、$\vec K$ | Bloch 波向量、能帶指標、reciprocal lattice vector | m$^{-1}$、—、m$^{-1}$ | [[Bloch's theorem]] |
| $w_{\vec k}$ | k-point 權重 | — | [[k-point sampling]] |
| $E_{max}$（$E_{cut}$） | plane-wave cutoff | Ha（講義）、Ry（QE） | [[cutoff energy]] |
