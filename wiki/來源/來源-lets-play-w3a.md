---
type: 來源
code: lets-play-w3a
unit: U02
url: https://www.compmatphys.org/topics/density-functional-theory-2-basis-set-size-and-k-mesh/
raw:
  - project_03a_keywords.pdf
date_added: 2026-11-16
tags: [U02, 實作]
---

# Let's play w3a · basis set size and k-mesh

## Basic info
- 原站主題頁：https://www.compmatphys.org/topics/density-functional-theory-2-basis-set-size-and-k-mesh/
- 文件：`project_03a_keywords.pdf`（本機，不公開；2 頁）。原站另有內容相同的 `project_03a_keywords-1.pdf`。
- 影片：2 支（basis set size、k-mesh 的意義）
- 單元：U02 density functional theory

## Summary
1. QE 輸入檔的三個主要關鍵字（[[來源-lets-play-w3a]] slides 1–2）：
   - **XC-functional**：課程說，DFT 中唯一的本質近似是 XC-functional 的選擇。在 `&SYSTEM` 裡用 `input_dft='LDA'` 或 `input_dft='PBE'`（PBE 是常用的 GGA）。
   - **k-mesh**：許多性質是第一 Brillouin zone 上的積分，數值上換成有限取樣點的和。點越多越接近精確解，所以每次計算都必須確認取樣點夠多：把計算的量對取樣點數作圖，飽和就代表夠了。用 `K_POINTS {automatic}` 加三個整數設定網格，例如 `3 3 3 0 0 0`。
   - **basis set size**：KS 軌域展開在無窮維的基底，電腦裡必須截斷，這會限制精度；理想上要截到「再加基底也不明顯影響結果」為止。
2. pseudopotential 是針對特定 XC-functional 做的：QE 預設採用 pseudopotential 的 XC-functional，但會被 `input_dft` 覆蓋。所以要嘛用對應 XC 的 pseudopotential，要嘛不要設 `input_dft`；不要拿某個 XC 的 pseudopotential 去配另一個 XC（[[來源-lets-play-w3a]] slide 1）。
3. `ecutwfc` 決定波函數的 basis 大小；密度用另一組 basis，由 `ecutrho` 決定，預設是 `ecutwfc` 的 4 倍。PAW 可能要稍大，ultrasoft pseudopotential 要大得多（8–12 倍）。好策略是：先固定倍數 4、測出需要的 `ecutwfc`，再提高倍數直到結果不變（[[來源-lets-play-w3a]] slide 2）。

## Notation
| 這份來源 | 知識庫統一符號 | 意義 |
|---|---|---|
| `input_dft` | — | QE 選 XC-functional 的關鍵字 |
| `ecutwfc`、`ecutrho` | $E_{cut}$、$E^{\rho}_{cut}$ | 波函數、密度的 cutoff（Ry） |

## Pages created or updated
- 新增：[[實作-w3 convergence testing]]
- 更新：[[k-point sampling]]、[[cutoff energy]]、[[exchange-correlation functional]]

## Quizzes and exercises
- 無

## To verify
- 文件說 `K_POINTS` 設在 `&ELECTRONS` 區塊；在 QE 輸入檔中它其實是獨立的 card（範例檔也寫在最後），見 [[k-point sampling]] 的「Conflicts and differences」。
