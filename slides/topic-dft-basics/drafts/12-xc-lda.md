---
cards: [exchange-correlation functional, local density approximation]
layout: equation
---
# The XC Functional and LDA
> 精確的 XC-functional 存在但未知；在 DFT 理論內，XC-functional 的選擇是唯一的本質近似〔exchange-correlation functional〕

$$
E_{xc}[\rho]\;\Rightarrow\;E_{xc}^{LDA}[\rho]=\int\rho(\vec r)\,\varepsilon_{xc}\big(\rho(\vec r)\big)\,d\vec r
$$

flow: 把空間切成小體積 -> 每一小塊的局部密度 $\rho$ -> *查均勻電子氣中每個電子的 $\varepsilon_{xc}$〔local density approximation〕

| | 精確的 $E_{xc}$ | LDA |
|---|---|---|
| 性質 | 存在且唯一，非常「病態」 | postulate〔exchange-correlation functional〕〔local density approximation〕 |
| exchange、correlation | 精確 | 部分〔exchange-correlation functional〕 |
