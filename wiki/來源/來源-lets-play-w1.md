---
type: 來源
code: lets-play-w1
unit: U01
url: https://www.compmatphys.org/topics/setting-the-stage-prepare-your-environment/
raw: []
date_added: 2026-11-16
tags: [U01, 實作]
---

# Let's play w1 · setting the stage – prepare your environment

## Basic info
- 原站主題頁：
  - https://www.compmatphys.org/topics/setting-the-stage-prepare-your-environment/
  - 說明資源：https://www.compmatphys.org/topics/setting-the-stage-help-section/
- 講義：無（主題頁文字）。頁面另附一份學員寫的 Mac M1 指南 PDF，未匯入。
- 不納入：HPC info（Flanders only），依 PRD §3 不做。
- 單元：U01 setting the stage（let's play 的第一項）

## Summary
1. 目標：在自己的電腦上得到一個能用的 DFT 程式。困難在於每個人的作業系統、安裝軟體的經驗、想用的程式都不同（[[來源-lets-play-w1]] 主題頁）。
2. 解法：用 virtual machine（虛擬機）跑課程指定的 DFT 程式（[[來源-lets-play-w1]] 主題頁）：
   - virtual machine 是在一個作業系統裡模擬另一個作業系統；
   - 每個人的環境完全相同，任何錯誤都能被別人重現。
3. virtual machine 只用於學習：模擬作業系統會吃掉電腦資源，所以 DFT 程式在 virtual machine 裡一定比較慢；真正做研究時通常會改用計算中心（[[來源-lets-play-w1]] 主題頁）。
4. virtual machine 由各 DFT 程式的開發者製作並測試；目前支援 Quantum ESPRESSO（Quantum Mobile）（[[來源-lets-play-w1]] 主題頁）。
5. Apple M1（ARM 晶片）不相容 VirtualBox，可改用 Docker 版的 Quantum Mobile（少一些圖形功能），或用 UTM 虛擬機（[[來源-lets-play-w1]] 主題頁）。
6. help section 列出 Quantum ESPRESSO 的官網、文件、所有輸入關鍵字，以及 pseudopotential 資料庫（包括 SSSP）（[[來源-lets-play-w1]] 主題頁）。

## Notation
| 這份來源 | 知識庫統一符號 | 意義 |
|---|---|---|
| — | — | 這份來源沒有數學符號 |

## Pages created or updated
- 新增：[[virtual machine]]、[[實作-w1 prepare your environment]]

## Quizzes and exercises
- 無

## To verify
- Quantum Mobile 的實際安裝步驟在另一個頁面（「virtual machine for Quantum Espresso (installation instructions)」的連結），`fetch_topic.py` 依 slug 抓到的是 Flemish 超級電腦的頁面，需要用瀏覽器確認正確網址。
