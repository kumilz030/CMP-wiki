---
type: 概念
aliases: [post-HF, 後 Hartree-Fock 方法, coupled cluster, CCSD(T), MP2, configuration interaction]
topic: density functional theory
unit: U02
order: "AW02E-03"
kind: method
sources:
  - "[[來源-AW02E]]"
  - "[[來源-AW03F]]"
prereqs: ["[[Hartree-Fock method]]"]
tags: [U02]
---

# post-Hartree-Fock methods

## Definition
post-Hartree-Fock methods（後 HF 方法）以 HF 為起點，在 Slater determinants 之外加入更多反對稱函數，逐步逼近精確基態，也就是把 correlation 加回來（[[來源-AW02E]] slides 7–11；[[來源-AW03F]] slide 3）。

## Mathematical form
無（講義只列出方法名稱）

## Physical meaning
- 常用的 post-HF 方法有：coupled cluster（CCSD(T)）、Møller-Plesset perturbation theory（MP2）、configuration interaction（CI）、CASSCF、MRCI 等，屬於量子化學課程的典型主題（[[來源-AW02E]] slide 11）。
- correlation 是一步一步加入的，計算很耗時（[[來源-AW03F]] slide 3）。
- 和 DFT 比較（[[來源-AW03F]] slides 10–13）：
  - post-HF 可以有系統地逼近精確結果，但總會撞上「計算資源永遠有限」這道牆；
  - 所以適合小系統，準確度高。

## Figure
無

## Validity and common misconceptions
- post-HF 適合小系統，DFT 適合大系統（[[來源-AW03F]] slide 13）。

## Related equations
- 無

## Related concepts
- 上層：[[Hartree-Fock method]]
- 相關：[[HF versus DFT]]、[[exchange and correlation]]

## Conflicts and differences

## Supplementary notes (not from source)

## Sources
- 原站：https://www.compmatphys.org/topics/post-hartree-fock-methods/
