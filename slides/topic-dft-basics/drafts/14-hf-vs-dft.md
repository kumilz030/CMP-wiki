---
cards: [HF versus DFT]
layout: compare
---
# HF versus DFT
> post-HF 適合小系統、準確度高；DFT 可以處理大系統，但有一些無法控制的「noise」〔HF versus DFT〕

| | Hartree-Fock（＋post-HF） | DFT（精確 $E_{xc}$） | DFT（LDA 等近似） |
|---|---|---|---|
| exchange | 依定義精確 | 精確 | 部分〔HF versus DFT〕 |
| correlation | 依定義沒有；由 post-HF 一步步加入 | 精確 | 部分〔HF versus DFT〕 |
| 結果 | 可系統地逼近精確，但計算很耗時 | 精確 | 近似；改進「需要黑魔法」〔HF versus DFT〕 |

- 兩者的目標都是從 first principles（Schrödinger 或 Dirac equation）直接解出精確結果〔HF versus DFT〕
- post-HF 走逐步逼近的路，但總會撞上「計算資源永遠有限」這道牆；DFT 繞另一條路，可以打到靶心附近〔HF versus DFT〕
