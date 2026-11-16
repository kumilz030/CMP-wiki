---
type: 來源
code: AW03A
unit: U02
url: https://www.compmatphys.org/topics/first-hohenberg-kohn-theorem/
raw:
  - AW03A-bis_proof-Hohenberg-Kohn-1_handouts.pdf
date_added: 2026-11-16
tags: [U02]
---

# AW03A-bis · proof of the first Hohenberg-Kohn theorem

## Basic info
- 原站主題頁：https://www.compmatphys.org/topics/first-hohenberg-kohn-theorem/ （第二支影片）
- 講義：`AW03A-bis_proof-Hohenberg-Kohn-1_handouts.pdf`（本機，不公開；15 張投影片）
- 單元：U02 density functional theory

## Summary
1. 要證明：若 $\Psi\neq\Psi'$，則 $\rho\neq\rho'$。方法是假設 $\Psi\neq\Psi'$ 但 $\rho=\rho'$，推出矛盾（[[來源-AW03A-bis]] slide 3）。開頭先回顧 $C$、$D$ 映射的問題：兩者是否 injective（[[來源-AW03A-bis]] slide 2）。
2. $\Psi$ 是 $H$ 的基態，能量 $E_{gs}$；$\Psi'$ 是 $H'$ 的基態，能量 $E'_{gs}$（[[來源-AW03A-bis]] slide 4）。
3. 兩者電子數相同（不同的話結論是 trivial 的），所以 $H=T+W+V$、$H'=T+W+V'$，因此 $H=H'-V'+V$（[[來源-AW03A-bis]] slide 5）。
4. 用 variational principle，把 $\Psi'$ 當成 $H$ 的試探函數，得到 $E_{gs}<E'_{gs}+\int\rho'(\vec r)[v(\vec r)-v'(\vec r)]d\vec r$（[[來源-AW03A-bis]] slides 6–8）。
5. 把兩個角色對調再做一次，再把兩式相加，並假設 $\rho=\rho'$，就得到 $E_{gs}+E'_{gs}<E_{gs}+E'_{gs}$，矛盾（[[來源-AW03A-bis]] slides 9–10）。
6. 這個證明只適用於 non-degenerate ground states；最後幾張投影片把結論放回 $C$、$D$ 映射的圖像中（[[來源-AW03A-bis]] slides 11–15）。出處：P. Hohenberg and W. Kohn, Phys. Rev. 136B (1964) 864（[[來源-AW03A-bis]] slide 15）。

## Notation
| 這份來源 | 知識庫統一符號 | 意義 |
|---|---|---|
| $T$、$W$、$V$ | $\hat T$、$\hat V_{ee}$、$\hat V_{ext}$ | 電子動能、電子–電子作用、外位勢 |
| $v(\vec r)$ | $V_{ext}(\vec r)$ | external potential 的函數形式 |
| $E_{gs}$ | $E_0$ | 基態能量 |

## Pages created or updated
- 新增：[[推導-first Hohenberg-Kohn theorem]]

## Quizzes and exercises
- 無

## To verify
- 無
