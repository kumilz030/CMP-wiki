---
type: 來源
code: AW02F
unit: U02
url: https://www.compmatphys.org/topics/the-external-potential/
raw:
  - AW02F_external-potential_answer-quiz.pdf
date_added: 2026-11-16
tags: [U02, 習題]
---

# AW02F (quiz) · the external potential of the O2 molecule

## Basic info
- 原站主題頁：https://www.compmatphys.org/topics/the-external-potential/ （上傳答案後可看這份討論）
- 文件：`AW02F_external-potential_answer-quiz.pdf`（本機，不公開；1 頁，Stefaan Cottenier，2017-08-23）
- 原站同時提供另一個版本 `03-06_external-potential_answer-quiz.pdf`，內容幾乎相同，未另外匯入。
- 單元：U02 density functional theory

## Summary
1. 題目「寫出 $\mathrm{O_2}$ 分子的 external potential」有 5 種寫法，只要知道自己寫的是什麼，全都正確（[[來源-AW02F-quiz]] slide 1）：
   - 答案 1（最常見）：16 個古典電子和 2 個古典原子核之間的 Coulomb 能量 $E_{ext}$。單位是能量（J），不是電位；
   - 答案 2：2 個原子核在位置 $\vec r$ 產生的電位 $V_{ext}(\vec r)$，完全不含電子的資訊，結果是 $\vec r$ 的函數；
   - 答案 3：量子力學中的算符 $\hat V_{ext}=\sum_{i=1}^{16}V_{ext}(\vec r_i)$；
   - 答案 4：用波函數取期望值，乘上 $-e$ 才從電位變成能量；
   - 答案 5：DFT 寫法 $E_{ext}=\int V_{ext}(\vec r)\rho(\vec r)\,d\vec r$。
2. 答案 5 是少數已知精確寫成密度泛函的性質之一；這裡的 $\rho$ 是 charge density，也就是 $-e$ 乘上機率密度（[[來源-AW02F-quiz]] slide 1）。
3. 常見錯誤：忘了要包含所有原子核（2 個）和所有電子（O 的 $Z=8$，所以整個分子有 16 個電子）（[[來源-AW02F-quiz]] slide 1）。

## Notation
| 這份來源 | 知識庫統一符號 | 意義 |
|---|---|---|
| $E_{ext}$ | $E_{ext}$ | external potential energy（能量） |
| $V_{ext}(\vec r)$ | $V_{ext}(\vec r)$ | external potential（電位） |
| $\hat V_{ext}$ | $\hat V_{ext}$ | external potential operator |
| $\rho(\vec r)$ | $\rho(\vec r)$ | 這份文件裡是 charge density（含 $-e$） |

## Pages created or updated
- 新增：[[習題-AW02F external potential of O2]]
- 更新：[[external potential]]

## Quizzes and exercises
- 本文件就是測驗的公開討論。

## To verify
- 無
