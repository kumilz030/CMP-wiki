---
type: 實作
aliases: [基本計算, let's play w2, a basic calculation]
topic: 實作
unit: U02
software: Quantum ESPRESSO
sources:
  - "[[來源-lets-play-w2]]"
tags: [U02]
---

# Hands-on: a basic calculation (w2)

## Goal
完成 DFT 程式的「基本單元」：拿一個晶體（矽）、轉成程式的輸入格式、執行、取出 total energy。之後不論用 DFT 做什麼，都要先會這一步（[[來源-lets-play-w2]] 主題頁）。

## Prerequisites
- 已完成 [[實作-w1 prepare your environment]]，有可用的 Quantum ESPRESSO 環境（[[來源-lets-play-w2]] slide 1）。
- 第一次做時不需要懂每個關鍵字；文件只講「怎麼做」，意義會在課程中陸續說明（[[來源-lets-play-w2]] slide 1）。

## Input highlights
QE 輸入檔要自己補上的重點（[[來源-lets-play-w2]] slides 2–3）：

| 位置 | 關鍵字 | 意義（連到本知識庫） |
|---|---|---|
| `&CONTROL` | `calculation='scf'` | 做一次 [[self-consistent field]] 計算 |
| `&CONTROL` | `tprnfor`、`tstress` | 輸出力與應力（之後的收斂測試會用到壓力） |
| `&SYSTEM` | `ecutwfc=50`、`ecutrho=200` | [[cutoff energy]]（Ry） |
| `&SYSTEM` | `input_dft='pbe'` | [[exchange-correlation functional]]：[[generalized gradient approximation]]（PBE） |
| `&SYSTEM` | `occupations='smearing'` 等 | 佔據數的處理（課程之後說明） |
| `&ELECTRONS` | `conv_thr=1d-08`、`mixing_beta=0.7d0` | SCF 的收斂門檻與密度混合 |
| `ATOMIC_SPECIES` | `Si.pbe-n-kjpaw_psl.1.0.0.UPF` | [[pseudopotential]]（PBE、PAW） |
| 檔尾 | `K_POINTS {automatic}` `7 7 7 0 0 0` | [[k-point sampling]] |

`CELL_PARAMETERS`、`ATOMIC_POSITIONS` 由 `cif2cell` 產生，不要改（[[來源-lets-play-w2]] slide 3）。

## Procedure
1. 在 virtual machine 開 terminal，執行 `conda activate qespresso`，建立 `workQE/basic` 資料夾（[[來源-lets-play-w2]] slide 1）。
2. 從 Crystallography Open Database（COD）下載矽的 cif 檔，用 `cif2cell ... -p quantum-espresso -o basic.in` 轉成 QE 輸入檔（[[來源-lets-play-w2]] slide 1）。
3. 用文字編輯器補上上表的區塊與關鍵字（[[來源-lets-play-w2]] slide 2）。
4. 下載 Si 的 pseudopotential，把檔名寫進 `ATOMIC_SPECIES`；加上 `K_POINTS`（[[來源-lets-play-w2]] slide 3）。
5. 執行 `pw.x -input basic.in > basic.out`，約幾秒到一分鐘（[[來源-lets-play-w2]] slide 3）。
6. （之後一次就好）下載 SSSP 函式庫，用 `pseudo_dir` 指過去（[[來源-lets-play-w2]] slides 5–6）。

## Expected results
- `basic.out` 最後一行附近有 `JOB DONE.`（[[來源-lets-play-w2]] slide 4）。
- total energy 在前面有 `!` 的那一行，例如約 −93.45 Ry（[[來源-lets-play-w2]] slide 4）。

## Pitfalls
- `cif2cell` 只在目前資料夾找 cif 檔，重開 terminal 後要先 `cd` 回去（[[來源-lets-play-w2]] slide 1）。
- 每開一個新 terminal 都要先 `conda activate qespresso`，否則找不到 `pw.x`（[[來源-lets-play-w2]] slide 1）。
- 選 pseudopotential 時要確認它的 XC 和你要的一致（[[來源-lets-play-w2]] slide 3）。
- 這裡的 50 Ry、7×7×7 是範例值，還沒經過 [[convergence testing]]。

## Related concepts
- [[self-consistent field]]、[[cutoff energy]]、[[k-point sampling]]、[[pseudopotential]]、[[total energy]]

## Supplementary notes (not from source)
- total energy 的絕對值本身沒有直接的物理意義（它依賴 pseudopotential）；有意義的是同一設定下不同結構之間的能量差。這是一般知識，後面單元會用到。

## Sources
- 原站：https://www.compmatphys.org/topics/density-functional-theory-1-a-basic-calculation/
