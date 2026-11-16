---
type: 綜合
aliases: [知識庫測試題組]
topic: 綜合
sources: []
tags: []
---

# knowledge base test questions

健檢時重跑（`.claude/skills/lint/SKILL.md`）。回答時只能用 index.md 找頁、讀頁，不能直接讀 raw。

- A 類：答案在單一頁
- B 類：要跨頁組合
- C 類：知識庫沒有，應回答「知識庫裡沒有」
- D 類：容易混淆

## A Single page
| # | 題目 | 應找到的頁 | 答案要點 |
|---|---|---|---|
| A1 | 課程對「固體」的完整定義是什麼？ | [[solid]] | 正原子核＋負電子、電磁交互作用、遵守 quantum physics |
| A2 | 玩具晶體每個 cell 的 Coulomb 能量是多少？正負號代表什麼？ | [[total energy]] | $(-3\sqrt2+2)e^2/d\approx-2.24e^2/d$；負→束縛 |
| A3 | 課程為什麼選 Quantum ESPRESSO？ | [[Quantum ESPRESSO]] | 口碑與社群、跨平台、免費 GPL |
| A4 | Apple M1 電腦要怎麼跑課程的 virtual machine？ | [[virtual machine]] | 不能用 VirtualBox；Docker 版 Quantum Mobile 或 UTM |

## B Multiple pages
| # | 題目 | 應找到的頁 | 答案要點 |
|---|---|---|---|
| B1 | 既然定律都知道了，為什麼現在才能用計算研究材料？ | [[quantum mechanics plus computing power enables materials simulation]]、[[maturity of physics fields]]、[[parallelization]] | 方程式太複雜（Dirac）；計算能力成長、時脈停滯後靠平行化 |
| B2 | 用計算預測的性質，為什麼不一定等於實際材料的性質？ | [[crystal structure and microstructure]]、[[solid]] | 計算主要處理晶體結構；材料性質還取決於 microstructure；solid ≠ material |

## C Not in the wiki
| # | 題目 | 預期回答 |
|---|---|---|
| C1 | Kohn-Sham equations 的形式是什麼？ | 知識庫目前沒有（U02 尚未匯入） |
| C2 | 古典 H 原子的最佳鍵長是多少？ | 講義只提出問題，答案在影片中；知識庫只有標成待查證的一般知識推論 |

## D Easily confused
| # | 題目 | 應找到的頁 | 答案要點 |
|---|---|---|---|
| D1 | 用 DFT 程式算材料是 theory 還是 simulation？ | [[theory versus simulation]] | 課程主張是 simulation（computer experiments） |
| D2 | 「ab initio」是不是代表計算完全沒有近似？ | [[ab initio]] | 不是；指出發點不可再化約，不是過程沒有近似 |

## Results
| 日期 | 通過 | 備註 |
|---|---|---|
