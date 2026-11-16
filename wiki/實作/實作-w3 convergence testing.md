---
type: 實作
aliases: [收斂測試實作, let's play w3, basis set size and k-mesh]
topic: 實作
unit: U02
software: Quantum ESPRESSO
sources:
  - "[[來源-lets-play-w3a]]"
  - "[[來源-lets-play-w3b]]"
tags: [U02]
---

# Hands-on: convergence testing (w3)

## Goal
以 halite（NaCl）為例，決定能給出可靠結果的 k-mesh 與 basis set 大小（[[來源-lets-play-w3b]] slide 1）。

## Prerequisites
- 會做 [[實作-w2 a basic calculation]]。
- 讀過三個主要關鍵字：XC-functional、k-mesh、basis set size（[[來源-lets-play-w3a]] slides 1–2）。

## Input highlights
- 起始輸入（[[來源-lets-play-w3b]] slides 1–2）：
  - 由 COD 的 cif 經 `cif2cell` 產生；
  - `ecutwfc=66`、`ecutrho=323`（Na pseudopotential 的建議值）；
  - `input_dft='pbe'`；
  - `K_POINTS {automatic} 3 3 3 0 0 0`；
  - `tstress=.true.`，才會輸出壓力。

## Procedure
1. 確認 XC 與 pseudopotential 都是 PBE（[[來源-lets-play-w3b]] slide 3）。
2. 以 pseudopotential 檔頭建議的最小 cutoff 當起點：取 Na（66/323 Ry）與 Cl（45/223 Ry）中較大的值（[[來源-lets-play-w3b]] slide 3）。
3. k-mesh：依序算 1、3、5、7、9、11 的網格，記錄 hydrostatic pressure 與時間（[[來源-lets-play-w3b]] slide 4）。
4. basis：固定 7×7×7、`ecutrho`＝5×`ecutwfc`，掃 `ecutwfc`＝16…200 Ry（[[來源-lets-play-w3b]] slide 5）。
5. 固定 `ecutwfc`=90 Ry，掃倍數 2…10（[[來源-lets-play-w3b]] slides 5–6）。

## Expected results
| 步驟 | 結果 | 選擇 |
|---|---|---|
| k-mesh | 1×1×1：243.81 kbar；3×3×3：3.02；5×5×5：1.23；7×7×7：1.09；11×11×11：1.13 | 7×7×7 |
| ecutwfc | 36 Ry：−268.2 kbar；66：0.9；86：7.1；200：8.0 | 90 Ry |
| ecutrho 倍數 | 4 以上差異都很小（7.4–7.7 kbar） | 5（450 Ry） |

（[[來源-lets-play-w3b]] slides 4–6）

最終設定：7×7×7、`ecutwfc=90` Ry、`ecutrho=450` Ry，壓力收斂到約 1 kbar 以內；較省時的選擇是 5×5×5、76 Ry、304 Ry（[[來源-lets-play-w3b]] slide 6）。

## Pitfalls
- 只算一次看不出結果離譜：1×1×1 很快，但壓力差了兩個數量級（[[來源-lets-play-w3b]] slide 4）。
- k-mesh 收斂時用的是起始 cutoff 66 Ry，其壓力約 1.1 kbar；最後選 90 Ry 後，收斂值約 8 kbar。可見兩個參數都要測（[[來源-lets-play-w3b]] slides 4–5）。
- 不要拿某個 XC 的 pseudopotential 配另一個 XC（[[來源-lets-play-w3a]] slide 1）。
- 每種新晶體都要重做，不能沿用（[[來源-lets-play-w3b]] slide 6）。

## Related concepts
- [[convergence testing]]、[[k-point sampling]]、[[cutoff energy]]、[[pseudopotential]]、[[generalized gradient approximation]]
- 邏輯鏈：[[convergence testing fixes the numerical parameters]]

## Supplementary notes (not from source)
- 用 shell 迴圈和 `sed` 自動產生不同參數的輸入檔，可以省下很多手動編輯；文件也鼓勵學員發展自己的加速方法。這是一般作法。

## Sources
- 原站：https://www.compmatphys.org/topics/density-functional-theory-2-basis-set-size-and-k-mesh/
- 原站：https://www.compmatphys.org/topics/density-functional-theory-2-convergence-testing/
