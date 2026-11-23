---
cards: [HK theorems justify the Kohn-Sham scheme]
layout: closing
---
# Summary: Why DFT Works
> 不解 $3N$ 維的多體波函數，改解只有 3 個變數的密度與 Kohn-Sham 軌域；DFT 理論本身唯一的本質近似是 XC 泛函的選擇，此外還有 Born-Oppenheimer 與數值方法帶來的近似〔HK theorems justify the Kohn-Sham scheme〕

1. Born-Oppenheimer：凍結原子核，只剩電子在固定的 external potential 中的問題〔HK theorems justify the Kohn-Sham scheme〕
2. 第一 HK 定理：基態密度與 external potential 一對一，基態可觀測量都是密度的唯一泛函 $O[\rho]$〔HK theorems justify the Kohn-Sham scheme〕
3. 第二 HK 定理：總能量泛函在基態密度有最小值，但 $F_{HK}$ 未知〔HK theorems justify the Kohn-Sham scheme〕
4. Kohn-Sham：用不交互作用的準粒子精確重現同一個密度，未知的部分全部收進 $V_{xc}$〔HK theorems justify the Kohn-Sham scheme〕
5. XC 近似（LDA、GGA）：精確的 XC 泛函存在但未知，只能近似；選擇近似的 XC 泛函是唯一的本質近似〔HK theorems justify the Kohn-Sham scheme〕
6. Self-consistent field：$\hat H_{KS}$ 依賴 $\rho$，所以要迭代到自洽〔HK theorems justify the Kohn-Sham scheme〕

- 限制：只保證基態；證明針對 non-degenerate ground states；XC 泛函的誤差無法事先控制；basis set 截斷與 k-point 取樣的數值誤差可以靠 convergence testing 控制〔HK theorems justify the Kohn-Sham scheme〕
