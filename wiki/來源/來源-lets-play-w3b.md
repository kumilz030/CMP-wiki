---
type: 來源
code: lets-play-w3b
unit: U02
url: https://www.compmatphys.org/topics/density-functional-theory-2-convergence-testing/
raw:
  - project_03b_convergence-testing_no-GUI.pdf
date_added: 2026-11-16
tags: [U02, 實作]
---

# Let's play w3b · convergence testing

## Basic info
- 原站主題頁：https://www.compmatphys.org/topics/density-functional-theory-2-convergence-testing/
- 文件：`project_03b_convergence-testing_no-GUI.pdf`（本機，不公開；8 頁，`slide N` 即第 N 頁）
- 單元：U02 density functional theory

## Summary
1. 每次開始計算一種新晶體，都必須做收斂測試，才能得到數值上可靠的結果，而不是雜訊（[[來源-lets-play-w3b]] 主題頁；[[來源-lets-play-w3b]] slide 1）。
2. 範例是 halite（岩鹽，NaCl）：從 COD 下載 cif、轉成 QE 輸入檔、下載 Na 與 Cl 的 pseudopotential（也建議改用 SSSP）（[[來源-lets-play-w3b]] slide 1）。
3. 步驟 1：選 XC-functional。課程一律用 PBE，並確認 pseudopotential 也是 PBE 的（[[來源-lets-play-w3b]] slide 3）。步驟 1.5：pseudopotential 檔頭常有建議的最小 cutoff（Na：66/323 Ry，Cl：45/223 Ry），取兩者最大值當起點（[[來源-lets-play-w3b]] slide 3）。
4. 步驟 2：k-mesh。監看 hydrostatic pressure，因為它對數值精度很敏感：它收斂了，比較不敏感的性質也會收斂（[[來源-lets-play-w3b]] slide 4）。結果如下（[[來源-lets-play-w3b]] slide 4）：

   | k-mesh | 壓力（kbar） | 時間（s） |
   |---|---|---|
   | 1×1×1 | 243.81 | 7.44 |
   | 3×3×3 | 3.02 | 11.14 |
   | 5×5×5 | 1.23 | 13.80 |
   | 7×7×7 | 1.09 | 19.14 |
   | 9×9×9 | 1.12 | 28.86 |
   | 11×11×11 | 1.13 | 43.80 |

   1×1×1 很快，但結果離譜；只算一次是看不出來的。選 7×7×7 作為折衷。
5. 步驟 3：basis set size。先固定 `ecutrho`＝5×`ecutwfc`，改變 `ecutwfc`：壓力從 16 Ry 的 −5324 kbar，逐漸到 200 Ry 的 8.0 kbar；86 Ry 已在 1 kbar 以內（7.1 kbar）。取 `ecutwfc=90` Ry（[[來源-lets-play-w3b]] slides 4–5）。再改變倍數（2–10），4 以上差異都很小，取倍數 5，即 `ecutrho=450` Ry（[[來源-lets-play-w3b]] slides 5–6）。
6. 結論：halite 用 7×7×7 k-mesh、`ecutwfc=90` Ry、`ecutrho=450` Ry，壓力收斂到約 1 kbar 以內。若能接受較大雜訊，5×5×5、76 Ry、304 Ry 也可以。精度和速度之間永遠要取捨（[[來源-lets-play-w3b]] slide 6）。
7. 附錄：JARVIS-ML 網站可以粗估 k-mesh 與 cutoff，但還很粗糙；例子中它建議的 k-mesh 比實測需要的低很多（[[來源-lets-play-w3b]] slides 6–7）。

## Notation
| 這份來源 | 知識庫統一符號 | 意義 |
|---|---|---|
| hydrostatic pressure | $P$ | 單胞上的靜水壓（kbar），用來監看收斂 |
| `ecutwfc`、`ecutrho` | $E_{cut}$、$E^{\rho}_{cut}$ | cutoff（Ry） |

## Pages created or updated
- 新增：[[實作-w3 convergence testing]]、[[convergence testing]]

## Quizzes and exercises
- 表單：回報操作是否順利（不公開）。

## To verify
- 無
