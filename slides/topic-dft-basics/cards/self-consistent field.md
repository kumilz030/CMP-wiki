# Card: self-consistent field

- wiki: `wiki/概念/U02/self-consistent field.md`（type: 概念）
- 網站：https://kumilz030.github.io/CMP-wiki/概念/U02/self-consistent-field
- aliases: 自洽場, SCF, scf cycle, self-consistency

## Definition
self-consistent field（SCF，自洽場）問題：要解 $\hat H_{KS}$ 才能得到 $\phi_i$ 與 $\rho$，但要先知道 $\rho$ 才寫得出 $\hat H_{KS}$。所以必須迭代求解（scf-scheme）（[[來源-AW03G]] slide 7）。

## Mathematical form
迭代流程（[[來源-AW03G]] slide 8）：
1. 從 $\rho_{old}$ 建出 $V_{eff}$；
2. 解 $\hat H_{KS}\phi_i=\epsilon_i\phi_i$ 得到 $\phi_i$；
3. 由 $\phi_i$ 建出 $\rho_{new}$；
4. 若 $\rho_{new}=\rho_{old}$，問題解決；否則令 $\rho_{old}\Leftarrow\rho_{new}$，回到 1。

## Physical meaning
- 收斂後的密度和它產生的位勢互相一致，所以叫「自洽」。
- 實作：Quantum ESPRESSO 的 `calculation='scf'` 就是做這個迴圈。輸入檔 `&ELECTRONS` 裡的 `conv_thr`（收斂門檻）與 `mixing_beta`（密度混合比例）控制迭代（[[來源-lets-play-w2]] slides 2、5）。

## Validity and common misconceptions
- 實際上不會直接用 $\rho_{new}$ 取代 $\rho_{old}$，而是兩者混合（mixing），以免振盪不收斂；「相等」也是指差異小於門檻。這是一般知識，對應 QE 的 `mixing_beta`、`conv_thr`。
