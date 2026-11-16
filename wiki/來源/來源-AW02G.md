---
type: 來源
code: AW02G
unit: U02
url: https://www.compmatphys.org/topics/the-electron-density/
raw:
  - AW02G_electron-density_handouts.pdf
date_added: 2026-11-16
tags: [U02]
---

# AW02G · the electron density

## Basic info
- 原站主題頁：https://www.compmatphys.org/topics/the-electron-density/
- 講義：`AW02G_electron-density_handouts.pdf`（本機，不公開；7 張投影片）
- 影片：Vimeo 1 支；字幕：無
- 預估時間：20 分鐘
- 單元：U02 density functional theory

## Summary
1. 不懂晶體的（電子）密度是什麼，就不可能懂 DFT（[[來源-AW02G]] 主題頁）。
2. 一個電子：密度算符 $\hat\rho(\vec r)=\delta(\vec r'-\vec r)$，密度 $\rho(\vec r)=\langle\Psi|\hat\rho(\vec r)|\Psi\rangle=|\Psi(\vec r)|^2$，也就是在 $\vec r$ 找到這個電子的機率（[[來源-AW02G]] slide 3）。
3. N 個電子：密度算符是 N 個 δ 函數的和；密度是在 $\vec r$ 找到「任一個」電子的機率，不管其他 N−1 個電子在哪裡。只有當 $\Psi$ 能用單電子波函數 $\varphi$ 寫出時，才等於 $\sum_i|\varphi(\vec r_i)|^2$（[[來源-AW02G]] slide 4）。
4. 電子密度是一個函數：練習題問它的定義域與值域（以兩個無自旋粒子為例），選項是 $\mathbb R^3\to\mathbb C$、$\mathbb R^6\to\mathbb R$、$\mathbb R^6\to\mathbb C$、$\mathbb R^3\to\mathbb R$（[[來源-AW02G]] slides 5–6）。答案被 spoiler 方塊遮住，文字層沒有完整答案（[[來源-AW02G]] slide 7）。

## Notation
| 這份來源 | 知識庫統一符號 | 意義 |
|---|---|---|
| $\hat\rho(\vec r)$ | $\hat\rho(\vec r)$ | density operator |
| $\rho(\vec r)$ | $\rho(\vec r)$ | 電子密度（這裡是機率密度，不含 $-e$） |
| $\varphi$ | $\phi_i$ | 單電子波函數 |

## Pages created or updated
- 新增：[[electron density]]

## Quizzes and exercises
- 主題頁的選擇題（同 slide 6，不公開答案）：電子密度是從哪個集合映到哪個集合的函數？

## To verify
- 練習題答案（講義遮住）。
