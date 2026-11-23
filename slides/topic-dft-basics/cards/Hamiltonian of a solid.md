# Card: Hamiltonian of a solid

- wiki: `wiki/方程式/Hamiltonian of a solid.md`（type: 方程式）
- 網站：https://kumilz030.github.io/CMP-wiki/方程式/Hamiltonian-of-a-solid
- aliases: 固體的 Hamiltonian, many-body Hamiltonian, many-body Schrödinger equation, 多體 Schrödinger 方程式

## Equation
$$
\hat H=
-\sum_A\frac{\hbar^2\nabla^2_{\vec R_A}}{2M_A}
-\sum_i\frac{\hbar^2\nabla^2_{\vec r_i}}{2m_i}
+\frac12\frac{1}{4\pi\varepsilon_0}\sum_{A\neq B}\frac{e^2Z_AZ_B}{|\vec R_A-\vec R_B|}
+\frac12\frac{1}{4\pi\varepsilon_0}\sum_{i\neq j}\frac{e^2}{|\vec r_i-\vec r_j|}
-\frac{1}{4\pi\varepsilon_0}\sum_{i,A}\frac{e^2Z_A}{|\vec r_i-\vec R_A|}
$$
（[[來源-AW02F]] slide 3）

這個 Hamiltonian 的 Schrödinger equation $\hat H\Psi=E\Psi$ 包含了量子系統的所有資訊（[[來源-AW02C]] 主題頁）。

符號說明（SI）：
- $M_A$、$\vec R_A$、$Z_A$：第 A 個原子核的質量、位置、原子序；
- $m_i$、$\vec r_i$：電子的質量、位置；
- 五項依序是：原子核動能、電子動能、核–核排斥、電子–電子排斥、電子–原子核吸引（[[來源-AW02F]] slide 3）。

## Conditions of validity
- 非相對論（Schrödinger 而非 Dirac）。
- 只考慮靜電 Coulomb 作用（沒有磁性作用、自旋–軌道作用）。
- 定態（不含時）。

## Origin
- [[solid]] 的定義：正原子核和負電子以電磁作用交互作用，並遵守 quantum physics。把所有成對的 Coulomb 作用和各粒子的動能加起來，就是這個 Hamiltonian。
- 影片的第一個問題就是：固體中有哪些交互作用（[[來源-AW02C]] 主題頁）？

## How to use
- 套用 [[Born-Oppenheimer approximation]] 後（[[來源-AW02D]] slide 5）：
  - 第一項（原子核動能）消失；
  - 第三項（核–核排斥）變成常數。
- 最後一項是 N 個電子在原子核電位中的能量，那個電位就是 [[external potential]]（[[來源-AW02F]] slides 4–6）。
- 即使經過 Born-Oppenheimer，剩下的方程式仍然難解得多，所以需要 HF 或 DFT（[[來源-AW02D]] slide 5）。

## Common mistakes
- 忘了 $\frac12$：成對作用加總時，$A\neq B$（或 $i\neq j$）的雙重求和會把每一對算兩次。
- AW02D 的講義寫法省略了 $\hbar^2/2$ 與 $1/4\pi\varepsilon_0$（[[來源-AW02D]] slide 5），兩份講義的單位慣例不同，見下方。

## Conflicts and differences
- ⚠️待查證：AW02F 投影片上，電子–電子項的分子印成 $-e^2$（[[來源-AW02F]] slide 3）。兩個電子同號，Coulomb 作用應該是排斥（$+e^2$）；AW02D 的同一項也是正號（$+\frac12\sum e^2/|\vec r_i-\vec r_j|$，[[來源-AW02D]] slide 5）。本頁採用 $+e^2$，判斷投影片是筆誤，尚未和影片核對。
- 單位慣例：AW02F 用完整 SI 形式（[[來源-AW02F]] slide 3）；AW02D 寫成 $-\sum\nabla^2/M_i-\sum\nabla^2/m_i-\sum\frac{(eZ_i)e}{|\vec R_i-\vec r_j|}+\dots$，省略了常數因子（[[來源-AW02D]] slide 5）。物理內容相同。
