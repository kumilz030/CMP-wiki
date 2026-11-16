---
type: 習題
aliases: [O2 的外位勢]
topic: 習題
unit: U02
sources:
  - "[[來源-AW02F]]"
  - "[[來源-AW02F-quiz]]"
tags: [U02]
---

# Quiz: external potential of the O2 molecule

## Question
寫出氧分子 $\mathrm{O_2}$ 的 external potential（[[來源-AW02F]] 主題頁）。原站要學員先上傳自己的答案，再看討論文件。

## Concepts used
- [[external potential]]
- [[Hamiltonian of a solid]]（電子–原子核項）
- [[electron density]]

## Reasoning
- 先確定粒子數：$\mathrm O$ 的 $Z=8$，所以 $\mathrm{O_2}$ 有 2 個原子核、16 個電子（[[來源-AW02F-quiz]] slide 1）。
- external potential 是**原子核**產生的電位，不含電子的資訊（[[來源-AW02F-quiz]] slide 1）。
- 但問題的「external potential」可以有不同層次的理解：能量、電位、算符、期望值、密度泛函（[[來源-AW02F-quiz]] slide 1）。

## Answer
討論文件列出 5 種寫法，只要知道自己寫的是哪一種，都算正確（[[來源-AW02F-quiz]] slide 1）。以下用自己的符號整理（$j$ 編號原子核，$i$ 編號電子）：

1. 古典能量（最常見，但這是**能量**，單位 J）：
$$E_{ext}=-\frac{1}{4\pi\varepsilon_0}\sum_{j=1}^{2}\sum_{i=1}^{16}\frac{8e^2}{|\vec R_j-\vec r_i|}$$
2. 電位（題目真正問的；是 $\vec r$ 的函數）：
$$V_{ext}(\vec r)=\frac{1}{4\pi\varepsilon_0}\sum_{j=1}^{2}\frac{8e}{|\vec R_j-\vec r|}$$
3. 算符：$\hat V_{ext}=\sum_{i=1}^{16}V_{ext}(\vec r_i)$。
4. 量子期望值：$E_{ext}=-e\langle\Psi|\hat V_{ext}|\Psi\rangle$；乘上 $-e$ 才從電位變成能量。
5. DFT 寫法：$E_{ext}=\int V_{ext}(\vec r)\,\rho(\vec r)\,d\vec r$，$\rho$ 是 charge density。

## Pitfalls
- 把能量（答案 1）當成電位：先檢查單位是 J 還是 J/C（[[來源-AW02F-quiz]] slide 1）。
- 漏掉原子核或電子的數目：要包含**所有** 2 個原子核與 16 個電子（[[來源-AW02F-quiz]] slide 1）。
- 答案 4 忘了乘 $-e$：波函數只給機率，不是電荷（[[來源-AW02F-quiz]] slide 1）。

## Supplementary notes (not from source)
- 答案 1 與答案 2 的關係：$E_{ext}=\sum_i(-e)\,V_{ext}(\vec r_i)$，也就是把每個古典電子的電荷乘上它所在位置的電位再加總。

## Sources
- 原站：https://www.compmatphys.org/topics/the-external-potential/
