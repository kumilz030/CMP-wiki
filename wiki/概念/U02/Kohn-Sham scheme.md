---
type: 概念
aliases: [Kohn-Sham 方法, Kohn-Sham method, quasi-particles, 準粒子]
topic: density functional theory
unit: U02
order: "AW03C-01"
kind: method
sources:
  - "[[來源-AW03C]]"
  - "[[來源-AW03H-teaser]]"
prereqs: ["[[second Hohenberg-Kohn theorem]]"]
tags: [U02]
---

# Kohn-Sham scheme

## Definition
Kohn-Sham scheme（Kohn-Sham 方法）：把交互作用的多電子問題，**精確地**轉換成一組不交互作用的 quasi-particles（準粒子）的單粒子問題。準粒子的密度等於真實系統的基態密度（[[來源-AW03C]] slide 2）。實際的 DFT 幾乎都在這個框架下進行（[[來源-AW03C]] 主題頁）。

## Mathematical form
見 [[Kohn-Sham equations]]。

## Physical meaning
和原本的 Hamiltonian 逐項對照（[[來源-AW03C]] slide 3）：

| 原本的 Schrödinger Hamiltonian | Kohn-Sham Hamiltonian |
|---|---|
| 電子的動能 | 準粒子的動能 |
| 受原子核的 Coulomb 位勢作用 | 受原子核的 Coulomb 位勢作用 |
| 電子之間的 Coulomb 作用 | 和其他所有準粒子的平均靜態分布作用（Hartree） |
| — | 再加上一個「神秘的」exchange-correlation potential |

- 結果是數學簡單得多，但必須知道 $V_{xc}$（[[來源-AW03C]] slide 3）。
- 行星類比（[[來源-AW03H-teaser]] slides 16–17）：
  - 把行星之間的交互作用關掉，加一個精心選擇的外加靜態場，就能重現每顆行星的精確運動；
  - 存在一個 universal generator 能找出這個「magic field」，對應的就是 universal XC functional。

## Figure
```mermaid
flowchart LR
  A["交互作用的電子<br/>（耦合的微分方程）"] -->|"精確轉換"| B["不交互作用的準粒子<br/>＋ V_H ＋ V_ext ＋ V_xc"]
  B --> C["同一個基態密度 ρ"]
```
自繪，依據 [[來源-AW03C]] slides 2–3。

## Validity and common misconceptions
- 「精確轉換」的前提是知道精確的 $V_{xc}$；實際上它必須近似（見 [[exchange-correlation functional]]）。
- 準粒子不是真實電子，所以它們的軌域與能量沒有嚴格的物理意義（見 [[Kohn-Sham equations]]）。

## Related equations
- [[Kohn-Sham equations]]

## Related concepts
- 上層：[[density functional theory]]
- 相關：[[Hartree potential]]、[[exchange-correlation functional]]、[[self-consistent field]]
- 邏輯鏈：[[HK theorems justify the Kohn-Sham scheme]]

## Conflicts and differences

## Supplementary notes (not from source)
- 主題頁的思考題（用 DFT 研究太陽系）和 teaser 的行星類比是同一個想法：用不交互作用的系統加上有效場，重現交互作用系統的結果。

## Sources
- 原站：https://www.compmatphys.org/topics/kohn-sham-equations/
