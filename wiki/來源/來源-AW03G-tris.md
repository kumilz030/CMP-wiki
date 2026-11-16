---
type: 來源
code: AW03G
unit: U02
url: https://www.compmatphys.org/topics/numerical-solution-methods/
raw:
  - AW03G-tris-allelectron-vs-pseudpotential_handouts.pdf
date_added: 2026-11-16
tags: [U02]
---

# AW03G-tris · all-electron methods vs. pseudopotential methods

## Basic info
- 原站主題頁：https://www.compmatphys.org/topics/numerical-solution-methods/ （第二支影片）
- 講義：`AW03G-tris-allelectron-vs-pseudpotential_handouts.pdf`（本機，不公開；12 張投影片）
- 單元：U02 density functional theory

## Summary
1. lemma 1：把一個函數分解成 basis functions 的和時，原函數和基底函數在性質上差越多，需要的基底函數就越多；講義以方波與三角波的 Fourier 展開示意（[[來源-AW03G-tris]] slides 2–3）。
2. lemma 2：DFT 計算的時間會隨基底函數的數目快速增加（[[來源-AW03G-tris]] slide 4）。
3. 波函數在原子核附近變化劇烈，例如 3d 軌域的徑向結構（[[來源-AW03G-tris]] slide 6）。兩類方法用不同方式減少基底函數：
   - all-electron methods：選擇長得像結果的基底函數。例子是 LAPW、APW+lo、LMTO、部分 local orbitals 方法；講義示意原子附近和原子之間用不同函數描述（[[來源-AW03G-tris]] slides 7–8）；
   - pseudopotential methods：改解一個「假想的晶體」，它只在有興趣的區域（離原子核遠的地方）和真實晶體一樣。示意圖是：在截斷半徑 $r_c$ 內，用平滑的 $\Psi_{pseudo}$、$V_{pseudo}$ 取代劇烈振盪的真實波函數與 $-Z/r$ 位勢；$r_c$ 外兩者相同。例子是 plane waves、PAW、部分 local orbitals 方法（[[來源-AW03G-tris]] slides 10–12）。

## Notation
| 這份來源 | 知識庫統一符號 | 意義 |
|---|---|---|
| $r_c$ | $r_c$ | pseudopotential 的截斷半徑 |
| $\Psi_{pseudo}$、$V_{pseudo}$ | $\tilde\psi$、$V_{PP}$ | 平滑化後的波函數與位勢 |

## Pages created or updated
- 新增：[[all-electron method]]、[[pseudopotential]]

## Quizzes and exercises
- 無

## To verify
- 無
