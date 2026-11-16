---
type: 來源
code: AW02E
unit: U02
url: https://www.compmatphys.org/topics/post-hartree-fock-methods/
raw:
  - AW02E_post-HF_handouts.pdf
date_added: 2026-11-16
tags: [U02]
---

# AW02E · (post-)Hartree-Fock method(s)

## Basic info
- 原站主題頁：https://www.compmatphys.org/topics/post-hartree-fock-methods/
- 講義：`AW02E_post-HF_handouts.pdf`（本機，不公開；11 張投影片）
- 影片：Vimeo 1 支；字幕：無
- 預估時間：15 分鐘
- 單元：U02 density functional theory

## Summary
1. 量子化學界大量使用 post-Hartree-Fock methods；這個主題說明它們和 DFT 的關係。主題頁提醒學員要先懂 Slater determinant（[[來源-AW02E]] 主題頁）。
2. 用「所有可能波函數的空間」作圖，由大到小（[[來源-AW02E]] slides 3–6）：
   - 精確基態（exact ground state）在這個空間的某一點；
   - 電子是 fermion，所以只看反對稱（antisymmetric）的波函數；
   - 其中更小的一個子集是所有 Slater determinants；
   - Hartree-Fock 基態是這個子集裡能量最低的那個，和精確基態不同。
3. post-HF 方法在 Slater determinants 之外加入更多反對稱函數（圖中的綠點越來越密），逐步逼近精確基態（[[來源-AW02E]] slides 7–10）。
4. HF 方法本身對固體不太準，所以不太直接使用；但它是 post-HF 方法的起點，例如 CCSD(T)、MP2、CI、CASSCF、MRCI，這些是量子化學課程的典型主題（[[來源-AW02E]] slide 11）。

## Notation
| 這份來源 | 知識庫統一符號 | 意義 |
|---|---|---|
| HF ground state | $\Psi^{HF}_0$ | Hartree-Fock 基態 |

## Pages created or updated
- 新增：[[Hartree-Fock method]]、[[Slater determinant]]、[[post-Hartree-Fock methods]]

## Quizzes and exercises
- 無（主題頁另推薦一篇 post-HF 綜述的第 2 節作為選讀）

## To verify
- 無
