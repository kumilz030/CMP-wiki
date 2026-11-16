---
type: 來源
code: AW03H-teaser
unit: U02
url: https://www.compmatphys.org/topics/optional-back-to-the-teaser/
raw:
  - AW03H_DFT-teaser-complete_handouts.pdf
date_added: 2026-11-16
tags: [U02, optional]
---

# (optional) back to the teaser

## Basic info
- 原站主題頁：https://www.compmatphys.org/topics/optional-back-to-the-teaser/
- 講義：`AW03H_DFT-teaser-complete_handouts.pdf`（本機，不公開；43 張投影片，選讀）
- 影片：完整演講（外部連結）；字幕：未取得
- 單元：U02 density functional theory

## Summary
1. 這是 [[來源-AW02A]] 那段 teaser 所屬的完整演講，可以當成本章的總結與複習，也提供幾個理解 DFT 的不同心理圖像（[[來源-AW03H-teaser]] 主題頁）。
2. 開場用一段論文的「方法」段落，裡面都是 DFT 術語（PAW、PBE、VASP、500 eV cutoff、k-point sets、結構最佳化），並問聽眾：你只是認得這些字，還是能解釋它們（[[來源-AW03H-teaser]] slides 2–3）？
3. 行星類比（[[來源-AW03H-teaser]] slides 15–17）：
   - 太陽＋地球是二體問題，有解析解；加上木星就沒有，因為有行星之間的交互作用；
   - DFT 的作法是把行星之間的交互作用關掉，改加一個精心選擇的外加靜態重力場，就能重現每顆行星的精確運動；而且存在一個 universal generator，能為每個問題找出這個「magic field」；
   - 對應到電子：把電子換成不交互作用的 quasi-electrons，它們和原子核交互作用，再加上一個外加的 exchange-correlation field，這個場可由 universal exchange-correlation functional 推導出來。
4. 選擇題：既然波函數包含系統的所有資訊，密度含有多少資訊？講義標出的答案是「和波函數一樣多」，DFT 正是利用這一點，基石是第一 Hohenberg-Kohn 定理（[[來源-AW03H-teaser]] slides 22–23）。
5. 其餘投影片重複本章內容：functional、electron density、HK 定理與證明、LDA、DFT 程式列表（[[來源-AW03H-teaser]] slides 24–41）。

## Notation
| 這份來源 | 知識庫統一符號 | 意義 |
|---|---|---|
| $V_{xc}[\rho]$ | $E_{xc}[\rho]$ | 同 [[來源-AW03D]] |

## Pages created or updated
- 更新：[[density functional theory]]、[[Kohn-Sham scheme]]

## Quizzes and exercises
- 演講中的選擇題（答案見上面第 4 點）。

## To verify
- 無（slide 23 以紅字標出 B 選項，已對照投影片影像）
