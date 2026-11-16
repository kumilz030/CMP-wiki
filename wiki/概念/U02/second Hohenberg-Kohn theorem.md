---
type: 概念
aliases: [第二 Hohenberg-Kohn 定理, HK2, Hohenberg-Kohn functional, F_HK, 2nd Hohenberg-Kohn theorem]
topic: density functional theory
unit: U02
order: "AW03B-01"
kind: theorem
sources:
  - "[[來源-AW03B]]"
prereqs: ["[[first Hohenberg-Kohn theorem]]", "[[functional]]"]
tags: [U02]
---

# second Hohenberg-Kohn theorem

## Definition
那個對基態密度給出基態總能量的唯一泛函，對任何其他密度都會給出更高的能量（[[來源-AW03B]] slide 2）。

## Mathematical form
總能量泛函可以拆成（[[來源-AW03B]] slide 3）：
$$
E_{V_{ext}}[\rho]=F_{HK}[\rho]+\int\rho(\vec r)\,V_{ext}(\vec r)\,d\vec r
$$
符號說明：
- $F_{HK}[\rho]$：（未知的）Hohenberg-Kohn functional，給出總能量中的動能與電子–電子作用部分；
- 第二項：外位勢的能量；
- 定理的內容：$E_{V_{ext}}[\rho]\ge E_{V_{ext}}[\rho_0]$，等號只在 $\rho=\rho_0$ 成立。

## Physical meaning
- 基態密度 $\rho_0$ 是 $E_{V_{ext}}[\rho]$ 的最小值：講義的圖中，能量曲線在 $\rho_0$ 有極小值；在 $\rho_0$ 沒有極小值的曲線被打叉（[[來源-AW03B]] slides 2–3）。
- 這提示了一個方法：把總能量泛函對密度最小化，就能找到基態密度（[[來源-AW03B]] slide 3）。
- $F_{HK}$ 不依賴 external potential，對所有系統都一樣。這是由拆分形式看出來的推論；它就是後面 XC-functional 要近似的那部分的來源。

## Figure
無

## Validity and common misconceptions
- 主題頁拋出的問題：有人認為第二定理只是第一定理的自然推論。這是課程留給學員討論的問題（[[來源-AW03B]] 主題頁）。
- 定理沒有給出 $F_{HK}$ 的形式；它未知（[[來源-AW03B]] slide 3）。

## Related equations
- [[Kohn-Sham equations]]

## Related concepts
- 上層：[[density functional theory]]
- 相關：[[first Hohenberg-Kohn theorem]]、[[exchange-correlation functional]]、[[Kohn-Sham scheme]]
- 邏輯鏈：[[HK theorems justify the Kohn-Sham scheme]]

## Conflicts and differences

## Supplementary notes (not from source)
- 第二定理是 variational principle 在密度上的版本。它也說明為什麼近似的 XC-functional 可能給出比精確值更低的能量：近似的泛函不再保證變分性質。這是一般知識。

## Sources
- 原站：https://www.compmatphys.org/topics/second-hohenberg-kohn-theorem/
