---
cards: [exchange-correlation functional, local density approximation]
layout: equation
---
# The XC Functional and LDA
> 唯一的 XC-functional 一定存在，但形式未知，只能用近似（LDA、GGA）：XC-functional 的選擇是 DFT 唯一的本質近似〔exchange-correlation functional〕

$$
E_{xc}[\rho]\;\Rightarrow\;E_{xc}^{LDA}[\rho]=\int\rho(\vec r)\,\varepsilon_{xc}\big(\rho(\vec r)\big)\,d\vec r
$$

- 真正的 XC 泛函要能解釋所有固態物理與化學，所以會非常「病態」，沒有希望寫成封閉式〔exchange-correlation functional〕
- LDA 是一個 postulate：每一小塊空間的 XC 能量，等於相同密度的均勻電子氣的 XC 能量〔local density approximation〕
- $\varepsilon_{xc}(\rho)$：密度為 $\rho$ 的均勻電子氣中每個電子的 XC 能量〔local density approximation〕
- LDA 只含部分 exchange 與部分 correlation；延伸是 GGA，要改進「需要黑魔法」〔exchange-correlation functional〕
- 在 Quantum ESPRESSO 用 `input_dft` 選擇，例如 `'LDA'`、`'PBE'`；pseudopotential 是針對特定 XC 做的，不要混用〔exchange-correlation functional〕
