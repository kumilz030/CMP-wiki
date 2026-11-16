---
type: 概念
aliases: [all-electron methods, 全電子方法]
topic: density functional theory
unit: U02
order: "AW03G-tris-01"
kind: method
sources:
  - "[[來源-AW03G-tris]]"
  - "[[來源-basis-sets-2]]"
prereqs: ["[[basis set]]"]
tags: [U02]
---

# all-electron method

## Definition
all-electron methods（全電子方法）：保留所有電子（包括 core electrons）與真實的原子核位勢，用「長得像結果」的基底函數來減少需要的基底數目（[[來源-AW03G-tris]] slide 7）。

## Mathematical form
無（細節見 [[augmented plane wave methods]]）

## Physical meaning
- 問題：原子核附近的波函數變化很陡，例如 3d 軌域的徑向結構（[[來源-AW03G-tris]] slide 6）。用和結果差很多的基底去描述，需要非常多基底函數（[[來源-AW03G-tris]] slide 2）。
- 對策：在原子附近和原子之間用不同的函數描述。例子有 LAPW、APW+lo、LMTO，以及部分 local orbital 方法（[[來源-AW03G-tris]] slide 8）。
- LAPW 被視為準確度的「golden standard」：
  - 有疑問時，它給出（該 XC 下）最終的 DFT 答案；
  - 不需要先測試 pseudopotential；
  - 能直接處理原子核附近的效應，例如 core level shifts、hyperfine interactions。

  （[[來源-basis-sets-2]] slide 30）

## Figure
無

## Validity and common misconceptions
- 平均而言，LAPW 和 PW+PP 的速度相當，沒有誰一定比較慢（[[來源-basis-sets-2]] slide 30）。

## Related equations
- [[generalized eigenvalue problem HC=SCE]]

## Related concepts
- 上層：[[basis set]]
- 對照：[[pseudopotential]]
- 細節：[[augmented plane wave methods]]

## Conflicts and differences

## Supplementary notes (not from source)

## Sources
- 原站：https://www.compmatphys.org/topics/numerical-solution-methods/
