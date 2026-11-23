---
cards: [self-consistent field]
layout: flow
---
# Solving It: Self-consistent Field
> $\hat H_{KS}$ 依賴 $\rho$，而 $\rho$ 又要解 $\hat H_{KS}$ 才得到，所以要迭代〔self-consistent field〕

cycle: $\rho_{old}$ -> 建出 $V_{eff}$ -> 解 KS 方程式 -> 由 $\phi_i$ 建出 $\rho_{new}$ -> *$\rho_{new}=\rho_{old}$？ || 不相等：$\rho_{old}\Leftarrow\rho_{new}$，重來〔self-consistent field〕

- 相等就完成：Quantum ESPRESSO 的 `calculation='scf'` 就是這個迴圈〔self-consistent field〕
- `conv_thr`（收斂門檻）與 `mixing_beta`（密度混合比例）控制迭代〔self-consistent field〕
