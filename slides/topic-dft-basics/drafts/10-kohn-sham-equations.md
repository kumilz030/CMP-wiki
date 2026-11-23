---
cards: [Kohn-Sham equations]
layout: equation
---
# Kohn-Sham Equations
> 實際要解的是一組單粒子方程式；密度由能量最低的 $N$ 個 Kohn-Sham 軌域組成〔Kohn-Sham equations〕

$$
\hat H_{KS}\,\phi_i=\epsilon_i\,\phi_i,\qquad
\rho(\vec r)=\sum_{i=1}^{N}\phi_i^*(\vec r)\,\phi_i(\vec r)
$$

$$
\hat H_{KS}=\hat T_0+\hat V_H+\hat V_{ext}+\hat V_{xc}
$$

- 各項：$\hat T_0$ 動能、$\hat V_H$ Hartree potential、$V_{ext}$ external potential、$V_{xc}$ XC potential〔Kohn-Sham equations〕
- XC 位勢是能量泛函的泛函導數：$V_{xc}=\frac{\delta E_{xc}[\rho]}{\delta\rho}$〔Kohn-Sham equations〕
- 成立條件：Born-Oppenheimer、基態、非相對論、自旋未極化；$E_{xc}$ 必須近似〔Kohn-Sham equations〕
- 常見錯誤：$\phi_i$、$\epsilon_i$ 是準粒子的軌域與能量，不是真實電子的〔Kohn-Sham equations〕
