# Outline: DFT basic concepts

- 對象：學過量子力學／物化、第一次接觸 DFT 的學生
- 頁數：15 頁（規格 8–15）
- 敘事線：要解的問題 → 近似的層級 → 兩個定理 → Kohn-Sham 怎麼變得可解 → XC 近似 → 怎麼迭代求解 → 和 HF 比較 → 總結論證
- 只用 `cards/` 的內容；每頁括號內是會用到的卡片。

| # | 標題（英文） | layout | 一句話重點 | 要點 | 卡片 |
|---|---|---|---|---|---|
| 1 | DFT Basics: From Many Electrons to One Density | title | DFT 把多體 Schrödinger 方程式換成單粒子 Kohn-Sham 方程式 | 副標：依據 CMP-wiki 的整理（Computational Materials Physics 課程筆記） | density functional theory |
| 2 | Roadmap: Three Levels of Approximation | flow | 從精確的 Hamiltonian 到預測，要經過三層近似 | exact hamiltonian → Born-Oppenheimer → HF 或 DFT → solution techniques → prediction；這份簡報只走 DFT 這條路 | three levels of approximation |
| 3 | The Problem: Hamiltonian of a Solid | equation | 固體的 Hamiltonian 只有 5 項，但解不出來 | 5 項的意義（兩個動能＋三種 Coulomb 作用，SI）；多體波函數有 3N 個變數；成立條件：非相對論、只有靜電 | Hamiltonian of a solid, density functional theory |
| 4 | Level 1: Born-Oppenheimer Approximation | bullets | 原子核重得多、慢得多，所以先把它凍結 | $M\gg m$ → $v_1\ll v_2$；變數 $4(N_e+N_n)\to 4N_e$；原子核動能消失、核–核項成常數；仍然太難解 | Born-Oppenheimer approximation |
| 5 | Two Tools: Functional and Electron Density | bullets | 泛函吃一個函數、吐一個數；密度只有 3 個變數 | $F[f]$ 的定義與例子；泛函導數 $\delta F_v/\delta\rho=v$；$\rho(\vec r)$＝在 $\vec r$ 找到任一電子的機率；KS 形式 $\rho=\sum\lvert\phi_i\rvert^2$ | functional, electron density |
| 6 | The External Potential | equation | 外位勢完全由原子核決定 | $V_{ext}(\vec r)$ 公式；它是電位不是能量；$E_{ext}=\int V_{ext}\rho\,d\vec r$ | external potential |
| 7 | First Hohenberg-Kohn Theorem | flow | 基態密度與外位勢一對一 | $C:\hat V_{ext}\mapsto\Psi$、$D:\Psi\mapsto\rho$ 都是雙射；推論 $O[\rho]$；限制：非簡併、基態、只保證存在 | first Hohenberg-Kohn theorem |
| 8 | Second Hohenberg-Kohn Theorem | equation | 能量泛函在基態密度有最小值 | $E_{V_{ext}}[\rho]=F_{HK}[\rho]+\int\rho V_{ext}$；$F_{HK}$ 未知；把能量對密度最小化就能找到基態密度 | second Hohenberg-Kohn theorem |
| 9 | Kohn-Sham Scheme: Quasi-particles | compare | 用不交互作用的準粒子，精確重現同一個密度 | 原 Hamiltonian 與 KS Hamiltonian 逐項對照；數學簡單得多，但必須知道 $V_{xc}$；行星類比 | Kohn-Sham scheme |
| 10 | Kohn-Sham Equations | equation | 實際要解的單粒子方程式 | $\hat H_{KS}=\hat T_0+\hat V_H+\hat V_{ext}+\hat V_{xc}$；$\rho=\sum_i^N\lvert\phi_i\rvert^2$；常見錯誤：$\phi_i$、$\epsilon_i$ 不是真實電子 | Kohn-Sham equations |
| 11 | Exchange and Correlation | flow | 從 Hartree product 到精確解，中間隔著 exchange 與 correlation | Hartree product →(exchange)→ Slater determinant（HF）→(correlation)→ exact；HF 有精確 exchange、沒有 correlation | exchange and correlation |
| 12 | The XC Functional and LDA | equation | XC 泛函存在但未知，是 DFT 唯一的本質近似 | 真正的 XC 泛函很「病態」；LDA：$E_{xc}^{LDA}=\int\rho\,\varepsilon_{xc}(\rho)\,d\vec r$（postulate）；延伸 GGA | exchange-correlation functional, local density approximation |
| 13 | Solving It: Self-consistent Field | flow | $\hat H_{KS}$ 依賴 $\rho$，所以要迭代到自洽 | $\rho_{old}$ → $V_{eff}$ → 解 KS → $\rho_{new}$ → 比較，不同就重來 | self-consistent field |
| 14 | HF versus DFT | compare | post-HF 適合小系統、高準確度；DFT 能處理大系統 | exchange／correlation 對照表；post-HF 撞上計算資源的牆；DFT 有無法控制的 noise | HF versus DFT |
| 15 | Summary: Why DFT Works | closing | 精確的定理＋一個近似（XC）＋數值求解 | 論證鏈 6 步：BO → HK1 → HK2 → KS → XC 近似 → SCF；限制：只保證基態、XC 誤差無法事先控制 | HK theorems justify the Kohn-Sham scheme |

## Design notes
- 版面 16:9，鍵盤 ← → 換頁；數學式用 KaTeX。
- 配色沿用 CMP-wiki 網站（DESIGN.md：藍 #2f5d8a、橘 #c0793a）。
- 每頁頁尾列出引用的 wiki 頁，連到公開網站。
- 不放講義截圖；圖只用 HTML／CSS 自己畫的流程方塊（AGENTS.md §6）。
