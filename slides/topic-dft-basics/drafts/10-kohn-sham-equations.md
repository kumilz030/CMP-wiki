---
cards: [Kohn-Sham equations]
layout: equation
---
# Kohn-Sham Equations
> 實際要解的單粒子方程式；密度由能量最低的 $N$ 個軌域組成〔Kohn-Sham equations〕

$$
\hat H_{KS}\,\phi_i=\epsilon_i\,\phi_i,\qquad
\rho(\vec r)=\sum_{i=1}^{N}\phi_i^*(\vec r)\,\phi_i(\vec r)
$$

$$
\hat H_{KS}=\hat T_0+\hat V_H+\hat V_{ext}+\hat V_{xc}
$$

grid: $\hat T_0$ :: 不交互作用粒子的動能 | $\hat V_H$ :: $\frac{e^2}{4\pi\varepsilon_0}\int\frac{\rho(\vec r')}{|\vec r-\vec r'|}\,d\vec r'$ | $\hat V_{ext}$ :: external potential | $\hat V_{xc}$ :: $V_{xc}=\frac{\delta E_{xc}[\rho]}{\delta\rho}$〔Kohn-Sham equations〕

- 成立條件：Born-Oppenheimer、基態、非相對論、自旋未極化；$E_{xc}$ 精確時密度才精確〔Kohn-Sham equations〕
- $\phi_i$、$\epsilon_i$ 屬於準粒子，不是真實電子〔Kohn-Sham equations〕
