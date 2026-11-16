---
type: 來源
code: AW02D
unit: U02
url: https://www.compmatphys.org/topics/the-born-oppenheimer-approximation/
raw:
  - AW02D_Born-Oppenheimer_handouts.pdf
date_added: 2026-11-16
tags: [U02]
---

# AW02D · the Born-Oppenheimer approximation

## Basic info
- 原站主題頁：https://www.compmatphys.org/topics/the-born-oppenheimer-approximation/
- 講義：`AW02D_Born-Oppenheimer_handouts.pdf`（本機，不公開；6 張投影片）
- 影片：Vimeo 1 支；字幕：無
- 預估時間：20 分鐘
- 單元：U02 density functional theory

## Summary
1. 幾乎所有固體的 DFT 計算都假設 Born-Oppenheimer approximation 成立（[[來源-AW02D]] 主題頁）。
2. 「three levels of approximations」：精確 Hamiltonian → level 1：Born-Oppenheimer → level 2：Hartree-Fock 或 DFT → level 3：solution techniques（求解技術）→ prediction（[[來源-AW02D]] slide 2）。
3. 古典圖像（又稱 adiabatic principle）：原子核與電子受大小相同、方向相反的力，但 $M\gg m$，所以同一段時間內原子核的速度遠小於電子（$v_1\ll v_2$）（[[來源-AW02D]] slide 3）。
4. 因此把原子核位置凍結（[[來源-AW02D]] slides 4–5）：
   - 結果 1：波函數的變數從 $4(N_e+N_n)$ 個減為 $4N_e$ 個，原子核位置變成參數；
   - 結果 2：Hamiltonian 中原子核的動能項消失，核–核排斥項變成常數。
5. Born-Oppenheimer 是很大的簡化，但得到的方程式仍然難解得多，還需要更多近似（[[來源-AW02D]] slide 5）。
6. 進階閱讀：Yonehara et al.（2012）談 nonadiabaticity；Schmidt（2013）談氫鍵的量子特性（[[來源-AW02D]] slide 6）。

## Notation
| 這份來源 | 知識庫統一符號 | 意義 |
|---|---|---|
| $M_i$、$m_i$ | $M$、$m_e$ | 原子核質量、電子質量 |
| $N_e$、$N_n$ | $N_e$、$N_n$ | 電子數、原子核數 |
| $x,y,z,\alpha$ | $\vec r$、自旋 | 每個粒子 3 個空間座標＋1 個自旋座標 |

## Pages created or updated
- 新增：[[Born-Oppenheimer approximation]]、[[three levels of approximation]]、[[Hamiltonian of a solid]]

## Quizzes and exercises
- 討論區問題（不公開答案）：看過推導後，你能想到哪些情況 Born-Oppenheimer approximation 不成立？

## To verify
- 無
