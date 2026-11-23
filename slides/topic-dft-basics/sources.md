# Sources: DFT basic concepts

- 主題：DFT 的基礎概念（教學簡報）
- 檢索方式：只讀 `index.md` 的「U02 Density functional theory」分類與各頁標題、aliases，不讀 `raw/`。
- 日期：2026-11-23

## Selected pages
從問題到理論、再到怎麼解，依 [[three levels of approximation]] 的順序挑選：

1. [[density functional theory]]：總覽，DFT 把多體問題換成單粒子問題
2. [[three levels of approximation]]：整份簡報的路線圖
3. [[Hamiltonian of a solid]]：要解的問題長什麼樣
4. [[Born-Oppenheimer approximation]]：第一層近似
5. [[functional]]：理解「密度泛函」的前提
6. [[electron density]]：DFT 的核心變數
7. [[external potential]]：HK1 定理中和密度對應的量
8. [[first Hohenberg-Kohn theorem]]：密度 ↔ 外位勢一對一
9. [[second Hohenberg-Kohn theorem]]：能量泛函的最小值原理
10. [[Kohn-Sham scheme]]：用不交互作用的準粒子重現密度
11. [[Kohn-Sham equations]]：實際要解的方程式
12. [[exchange and correlation]]：XC 裡面裝的是什麼
13. [[exchange-correlation functional]]：唯一的本質近似
14. [[local density approximation]]：最簡單的 XC 近似
15. [[self-consistent field]]：KS 方程式為什麼要迭代
16. [[HF versus DFT]]：和量子化學方法的比較
17. [[HK theorems justify the Kohn-Sham scheme]]：把以上串成一條論證

## Not selected (and why)
- basis set、plane-wave basis set、pseudopotential、k-point sampling、cutoff energy、convergence testing：屬於數值求解與實作細節，不是「基礎概念」；可作為下一份簡報的主題。
- generalized gradient approximation、Hartree potential、Slater determinant、post-Hartree-Fock methods、Hartree-Fock method：內容已分別包含在 exchange-correlation functional、Kohn-Sham equations、exchange and correlation、HF versus DFT 的卡片中，避免重複。
