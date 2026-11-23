---
cards: [Hamiltonian of a solid, density functional theory]
layout: equation
---
# The Problem: Hamiltonian of a Solid
> 只有五項，但對應的 many-body Schrödinger equation 難解得多〔Hamiltonian of a solid〕〔density functional theory〕

$$
\hat H=
-\sum_A\frac{\hbar^2\nabla^2_{\vec R_A}}{2M_A}
-\sum_i\frac{\hbar^2\nabla^2_{\vec r_i}}{2m_i}
+\frac12\frac{1}{4\pi\varepsilon_0}\sum_{A\neq B}\frac{e^2Z_AZ_B}{|\vec R_A-\vec R_B|}
+\frac12\frac{1}{4\pi\varepsilon_0}\sum_{i\neq j}\frac{e^2}{|\vec r_i-\vec r_j|}
-\frac{1}{4\pi\varepsilon_0}\sum_{i,A}\frac{e^2Z_A}{|\vec r_i-\vec R_A|}
$$

| 項 | 意義 | 套用 Born-Oppenheimer 後 |
|---|---|---|
| 1 | 原子核動能 | 消失〔Hamiltonian of a solid〕 |
| 2 | 電子動能 | 不變〔Hamiltonian of a solid〕 |
| 3 | 核–核排斥 | 變成常數〔Hamiltonian of a solid〕 |
| 4 | 電子–電子排斥 | 不變〔Hamiltonian of a solid〕 |
| 5 | 電子–原子核吸引（電子在 external potential 中的能量） | 不變〔Hamiltonian of a solid〕 |

- 第 4 項：講義印成 $-e^2$，wiki 採 $+e^2$（待查證）〔Hamiltonian of a solid〕
