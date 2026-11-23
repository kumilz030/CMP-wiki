---
cards: [Hamiltonian of a solid, density functional theory]
layout: equation
---
# The Problem: Hamiltonian of a Solid
> 固體的 Hamiltonian 只有五項，但對應的 many-body Schrödinger equation 難解得多〔Hamiltonian of a solid〕〔density functional theory〕

$$
\hat H=
-\sum_A\frac{\hbar^2\nabla^2_{\vec R_A}}{2M_A}
-\sum_i\frac{\hbar^2\nabla^2_{\vec r_i}}{2m_i}
+\frac12\frac{1}{4\pi\varepsilon_0}\sum_{A\neq B}\frac{e^2Z_AZ_B}{|\vec R_A-\vec R_B|}
+\frac12\frac{1}{4\pi\varepsilon_0}\sum_{i\neq j}\frac{e^2}{|\vec r_i-\vec r_j|}
-\frac{1}{4\pi\varepsilon_0}\sum_{i,A}\frac{e^2Z_A}{|\vec r_i-\vec R_A|}
$$

- 五項依序是：原子核動能、電子動能、核–核排斥、電子–電子排斥、電子–原子核吸引（SI）〔Hamiltonian of a solid〕
- 多體波函數 $\Psi$ 有 $3N$ 個空間變數〔density functional theory〕
- 成立條件：非相對論、只考慮靜電 Coulomb 作用、定態（不含時）〔Hamiltonian of a solid〕
- 電子–電子項採 $+e^2$：講義印成 $-e^2$，wiki 判斷是筆誤，尚待查證〔Hamiltonian of a solid〕
