---
type: 來源
code: lets-play-w2
unit: U02
url: https://www.compmatphys.org/topics/density-functional-theory-1-a-basic-calculation/
raw:
  - project_02_basic-calculation-Quantum-Espresso-no-gui.pdf
date_added: 2026-11-16
tags: [U02, 實作]
---

# Let's play w2 · density functional theory 1 – a basic calculation

## Basic info
- 原站主題頁：https://www.compmatphys.org/topics/density-functional-theory-1-a-basic-calculation/
- 文件：`project_02_basic-calculation-Quantum-Espresso-no-gui.pdf`（本機，不公開；6 頁，`slide N` 即第 N 頁）
- 另一份 NanoLab 版說明（`project_02_notes-on-initial-use-of-VNLQE.pdf`）目前不支援，不匯入。
- 單元：U02 density functional theory

## Summary
1. 這是使用 DFT 程式的「基本單元」：拿一個晶體、餵給程式、執行、取出 total energy。不管之後拿 DFT 做什麼，都要先經過這些步驟（[[來源-lets-play-w2]] 主題頁）。
2. 文件只講「怎麼做」，不講「為什麼」；每個步驟的意義會在課程中陸續說明（[[來源-lets-play-w2]] slide 1）。
3. 流程是：在 virtual machine 開 terminal → `conda activate qespresso` → 建工作資料夾 → 從 COD 下載 Si 的 cif 檔 → 用 `cif2cell` 轉成 QE 輸入檔（[[來源-lets-play-w2]] slide 1）。
4. 在輸入檔加入 `&CONTROL` 區塊（`calculation='scf'`、`tprnfor`、`tstress` 等），並在 `&SYSTEM` 補上 `ecutwfc=50`、`ecutrho=200`、`input_dft='pbe'`、smearing 設定（[[來源-lets-play-w2]] slide 2）。
5. 下載 Si 的 PBE PAW pseudopotential（UPF 檔），寫進 `ATOMIC_SPECIES`；在最後加上 `K_POINTS {automatic}`，設 7 7 7 的 k-mesh；用 `pw.x -input basic.in > basic.out` 執行（[[來源-lets-play-w2]] slide 3）。
6. 輸出檔最後要有 `JOB DONE.`。total energy 在前面有驚嘆號的那一行，例如約 −93.45 Ry（[[來源-lets-play-w2]] slide 4）。
7. 附錄：下載 SSSP pseudopotential 函式庫，把 `pseudo_dir` 指到那個資料夾，之後每次只要在 `ATOMIC_SPECIES` 寫檔名（[[來源-lets-play-w2]] slides 5–6）。

## Notation
| 這份來源 | 知識庫統一符號 | 意義 |
|---|---|---|
| `ecutwfc` | $E_{cut}$（波函數） | 波函數的 plane-wave cutoff（Ry） |
| `ecutrho` | $E_{cut}^{\rho}$ | 密度的 cutoff（Ry） |
| `K_POINTS {automatic} 7 7 7 0 0 0` | k-mesh $7\times7\times7$ | k-point sampling |

## Pages created or updated
- 新增：[[實作-w2 a basic calculation]]

## Quizzes and exercises
- 表單：回報操作是否順利（不公開）。

## To verify
- 無
