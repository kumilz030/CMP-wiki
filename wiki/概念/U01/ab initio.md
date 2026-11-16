---
type: 概念
aliases: [第一原理, first principles, ab initio model, 第一原理模型]
topic: setting the stage
unit: U01
order: "AW01B-01"
kind: concept
sources:
  - "[[來源-AW01B]]"
  - "[[來源-AW01E]]"
prereqs: []
tags: [U01]
---

# ab initio

## Definition
ab initio（拉丁文「從頭開始」），也叫 first principles（第一原理）。一個能描述大量自然現象的數學模型，如果它的出發點在該領域的語言裡已經無法再化約成更基本的概念，就稱為 ab initio model（第一原理模型）（[[來源-AW01B]] 主題頁）。

## Mathematical form
對固體與材料來說，ab initio model 的出發點是 Schrödinger equation（薛丁格方程式）：
$$
\hat H\,\Psi = E\,\Psi
$$
符號說明：$\hat H$ 是系統的 Hamiltonian（漢米爾頓算符），$\Psi$ 是波函數，$E$ 是能量（[[來源-AW01B]] slide 5）。單位制與各項的寫法在 U02 再處理。

## Physical meaning
- 科學想做的事，是「把觀察到的自然現象，在數學模型裡重新建出來」（[[來源-AW01B]] slides 3、5）。講義的比喻是：真實的蘋果樹，和電腦螢幕上重建出來的蘋果樹（[[來源-AW01B]] slide 2）。
- 講義的例子是金屬 Hf：從巨觀樣品，到晶體結構、原子堆積，再從 $\hat H\Psi=E\Psi$ 出發算出一個可以和實驗比對的量 $V_{zz}$（[[來源-AW01B]] slides 4–5）。
- 主題頁說，每個科學領域都以建立 ab initio model 為目標（[[來源-AW01B]] 主題頁）。
- 「ab initio」是相對於某個領域的語言而言：主題頁請學員想想，為什麼 quantum physics 和 classical mechanics 都能稱為 ab initio model（[[來源-AW01B]] 主題頁）。
- 對材料而言，ab initio simulation 就是 trial-and-error（嘗試錯誤）與 rational design（理性設計）的分水嶺（[[來源-AW01E]] slide 10）。

## Figure
無

## Validity and common misconceptions
- 誤解：「ab initio 就是沒有任何近似」。定義講的是**出發點**不能再化約，不是計算過程沒有近似；實際計算的近似會在 U02 的 DFT 中出現。
- 「ab initio」是針對特定現象與語言而言，不是絕對的。

## Related equations
- 無（Schrödinger equation 在 U02 開頁）

## Related concepts
- 相關：[[solid]]（固體必須用 quantum physics 描述）
- 相關：[[materials design from thought]]、[[theory versus simulation]]
- 邏輯鏈：[[quantum mechanics plus computing power enables materials simulation]]

## Conflicts and differences

## Supplementary notes (not from source)
- ⚠️待查證：$V_{zz}$ 在固態物理中常用來表示原子核位置的 electric field gradient（電場梯度）主分量，Hf 是常見的例子；講義只有符號，這個解讀是一般知識，尚未和影片核對。
- 物化的角度見 pchem-wiki 中與 Schrödinger equation 相關的頁面。

## Sources
- 原站：https://www.compmatphys.org/topics/the-ab-initio-way/
