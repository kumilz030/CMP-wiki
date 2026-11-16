---
type: 來源
code: AW03A
unit: U02
url: https://www.compmatphys.org/topics/first-hohenberg-kohn-theorem/
raw:
  - AW03A_1st-HK_handouts.pdf
date_added: 2026-11-16
tags: [U02]
---

# AW03A · first Hohenberg-Kohn theorem

## Basic info
- 原站主題頁：https://www.compmatphys.org/topics/first-hohenberg-kohn-theorem/
- 講義：`AW03A_1st-HK_handouts.pdf`（本機，不公開；9 張投影片）
- 證明的詳細版：[[來源-AW03A-bis]]
- 影片：Vimeo 2 支（主講＋證明）；字幕：無
- 預估時間：30 分鐘
- 單元：U02 density functional theory

## Summary
1. 兩個 Hohenberg-Kohn theorems 是 DFT 的基石（[[來源-AW03A]] 主題頁）。
2. 定義兩個映射（[[來源-AW03A]] slides 2–3）：
   - $C:\hat V_{ext}\mapsto\Psi$（external potential → 基態波函數）；
   - $D:\Psi\mapsto\rho$（波函數 → 密度）。

   依建構方式，兩者都是 surjective（滿射）。要注意集合的定義：這裡只包含「某個 external potential 的基態」波函數，以及由這些波函數得到的密度，不是所有波函數與所有密度。
3. $C$ 是 injective（單射），這不意外；$D$ 也是 injective，這就非常意外了，而這正是 Hohenberg 與 Kohn（1964）的第一定理（[[來源-AW03A]] slides 4–5）。
4. 證明針對 non-degenerate ground states（非簡併基態），用反證法與 variational principle（變分原理）（[[來源-AW03A]] slide 7）；詳見 [[推導-first Hohenberg-Kohn theorem]]。
5. 因此 $C$、$D$ 都是 bijective（雙射），三者之間是一對一關係（[[來源-AW03A]] slide 8）。
6. 定理敘述：基態密度和 external potential 之間有一對一的對應。推論：任何可觀測的基態性質，都能寫成密度的唯一泛函 $\langle\Psi|\hat O|\Psi\rangle=O[\rho]$（[[來源-AW03A]] slide 9）。

## Notation
| 這份來源 | 知識庫統一符號 | 意義 |
|---|---|---|
| $\hat V_{ext}$ | $\hat V_{ext}$ | external potential（算符） |
| $C$、$D$ | $C$、$D$ | 講義定義的兩個映射 |
| $O[\rho]$ | $O[\rho]$ | 可觀測量寫成密度的泛函 |

## Pages created or updated
- 新增：[[first Hohenberg-Kohn theorem]]、[[推導-first Hohenberg-Kohn theorem]]

## Quizzes and exercises
- 討論區（選做）：比較 Wikipedia 等百科對第一定理的說明和影片有什麼異同。

## To verify
- 無
