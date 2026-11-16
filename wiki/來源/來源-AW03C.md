---
type: 來源
code: AW03C
unit: U02
url: https://www.compmatphys.org/topics/kohn-sham-equations/
raw:
  - AW03C_Kohn-Sham_handouts.pdf
date_added: 2026-11-16
tags: [U02]
---

# AW03C · Kohn-Sham equations

## Basic info
- 原站主題頁：https://www.compmatphys.org/topics/kohn-sham-equations/
- 講義：`AW03C_Kohn-Sham_handouts.pdf`（本機，不公開；3 張投影片）
- 影片：Vimeo 1 支；另有 Kieron Burke 在 CECAM「Teaching the Theory in DFT」學校講 Kohn-Sham equations 的教學影片；字幕：無
- 預估時間：20 分鐘
- 單元：U02 density functional theory

## Summary
1. 實際的 DFT 幾乎都在 Kohn 與 Sham（1965）建立的框架下進行（[[來源-AW03C]] 主題頁）。
2. N 電子系統的精確基態密度可以寫成 $\rho(\vec r)=\sum_{i=1}^{N}\phi_i^*(\vec r)\phi_i(\vec r)$，其中 $\phi_i$ 是 Kohn-Sham equations $\hat H_{KS}\phi_i=\epsilon_i\phi_i$ 能量最低的 N 個解（[[來源-AW03C]] slide 2）。
3. $\hat H_{KS}=\hat T_0+\hat V_H+\hat V_{ext}+\hat V_{xc}$。各項分別是：
   - 動能；
   - Hartree 項 $\frac{e^2}{4\pi\varepsilon_0}\int\frac{\rho(\vec r')}{|\vec r-\vec r'|}d\vec r'$；
   - 外位勢；
   - exchange-correlation 項 $V_{xc}=\delta V_{xc}[\rho]/\delta\rho$。

   （[[來源-AW03C]] slide 2）
4. Kohn-Sham equations 把原本的問題（彼此耦合的微分方程）精確地轉換成單粒子方程式（不再耦合）（[[來源-AW03C]] slide 2）。
5. 和原本的 Hamiltonian 對照：電子換成 quasi-particles（準粒子），它們受原子核的 Coulomb 位勢作用，和其他所有準粒子的平均靜態分布交互作用，再加上一個「神秘的」exchange-correlation potential。數學簡單得多，但必須知道 $V_{xc}$（[[來源-AW03C]] slide 3）。

## Notation
| 這份來源 | 知識庫統一符號 | 意義 |
|---|---|---|
| $\hat T_0$ | $\hat T_0$ | 不交互作用粒子的動能 |
| $\hat V_H$ | $\hat V_H$ | Hartree potential |
| $V_{xc}[\rho]$（泛函） | $E_{xc}[\rho]$ | 講義用 $V_{xc}[\rho]$ 表示 exchange-correlation **能量**泛函；本知識庫寫成 $E_{xc}[\rho]$ |
| $V_{xc}$（位勢） | $V_{xc}(\vec r)$ | exchange-correlation potential，$=\delta E_{xc}/\delta\rho$ |
| $\epsilon_i$ | $\epsilon_i$ | Kohn-Sham 本徵值 |

## Pages created or updated
- 新增：[[Kohn-Sham equations]]、[[Kohn-Sham scheme]]、[[Hartree potential]]

## Quizzes and exercises
- 討論區問題（不公開答案）：怎麼用 DFT 與 Kohn-Sham 方法研究太陽與行星的重力多體系統？

## To verify
- 無
