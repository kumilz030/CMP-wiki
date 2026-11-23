---
cards: [self-consistent field]
layout: flow
---
# Solving It: Self-consistent Field
> 要解 $\hat H_{KS}$ 才能得到 $\rho$，但要先知道 $\rho$ 才寫得出 $\hat H_{KS}$，所以必須迭代求解〔self-consistent field〕

flow: $\rho_{old}$ -> 建出 $V_{eff}$ -> 解 $\hat H_{KS}\phi_i=\epsilon_i\phi_i$ -> 由 $\phi_i$ 建出 $\rho_{new}$ -> $\rho_{new}=\rho_{old}$？〔self-consistent field〕

- 若相等，問題解決；否則令 $\rho_{old}\Leftarrow\rho_{new}$，回到第一步〔self-consistent field〕
- Quantum ESPRESSO 的 `calculation='scf'` 就是做這個迴圈；`conv_thr` 與 `mixing_beta` 控制迭代〔self-consistent field〕
