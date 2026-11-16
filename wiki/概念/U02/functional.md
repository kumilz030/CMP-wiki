---
type: 概念
aliases: [泛函, functional derivative, 泛函導數]
topic: density functional theory
unit: U02
order: "AW02B-01"
kind: concept
sources:
  - "[[來源-AW02B]]"
prereqs: []
tags: [U02]
---

# functional

## Definition
function（函數）把一個數對應到一個數；functional（泛函）把一個**函數**對應到一個（複）數（[[來源-AW02B]] slides 2–3）。

## Mathematical form
$$
f:\mathbb R\to\mathbb R:\ x\mapsto f(x)
\qquad\qquad
F:\mathcal F\to\mathbb C:\ f\mapsto F[f]
$$
符號說明：$\mathcal F$ 是函數的集合；方括號 $F[f]$ 表示引數是一個函數（[[來源-AW02B]] slide 3）。

講義的例子（[[來源-AW02B]] slide 3）：
- 積分型：$F[f]=\int_{-\infty}^{\infty}f(x)\,e^{-x^2}dx$；
- 取值型：$F[f]=f(0)$。

functional derivative（泛函導數）是函數導數的推廣，例如（[[來源-AW02B]] slide 3）：
$$
F_v[\rho]=\int\rho(\vec r)\,v(\vec r)\,d\vec r
\quad\Rightarrow\quad
\frac{\delta F_v[\rho]}{\delta\rho}=v(\vec r)
$$

## Physical meaning
- 不懂 functional，就沒辦法懂 density functional theory（[[來源-AW02B]] 主題頁）。DFT 的總能量是電子密度這個**函數**的泛函，例如 $E_{V_{ext}}[\rho]$（見 [[second Hohenberg-Kohn theorem]]）。
- 上面的 $F_v[\rho]$ 正是 external potential energy 的形式；它的泛函導數就是位勢本身。這個關係在 Kohn-Sham 方程式中用來從能量泛函得到位勢，例如 $V_{xc}=\delta E_{xc}/\delta\rho$（見 [[Kohn-Sham equations]]）。

## Figure
無

## Validity and common misconceptions
- 誤解：「$F[f]$ 是 $f$ 在某一點的函數值」。泛函的結果取決於整個函數 $f$；$F[f]=f(0)$ 只是剛好只用到一點的特例。

## Related equations
- [[Kohn-Sham equations]]

## Related concepts
- 相關：[[density functional theory]]、[[electron density]]、[[external potential]]

## Conflicts and differences

## Supplementary notes (not from source)
- 物化中熟悉的例子：古典作用量 $S[x(t)]=\int L\,dt$，以及 Schrödinger 方程式的變分形式 $E[\Psi]=\langle\Psi|\hat H|\Psi\rangle/\langle\Psi|\Psi\rangle$，都是泛函。這是一般知識。

## Sources
- 原站：https://www.compmatphys.org/topics/functions-and-functionals/
