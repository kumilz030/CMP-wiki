# Card: Born-Oppenheimer approximation

- wiki: `wiki/概念/U02/Born-Oppenheimer approximation.md`（type: 概念）
- 網站：https://kumilz030.github.io/CMP-wiki/概念/U02/Born-Oppenheimer-approximation
- aliases: Born-Oppenheimer 近似, BO approximation, adiabatic principle, 絕熱原理

## Definition
Born-Oppenheimer approximation（又稱 adiabatic principle，絕熱原理）：因為原子核比電子重得多、動得慢得多，所以把原子核的位置「凍結」，只解電子的問題（[[來源-AW02D]] slides 3–4）。這是 [[three levels of approximation]] 中的 level 1（[[來源-AW02D]] slide 2）。

## Mathematical form
凍結原子核後，波函數只剩電子的變數，原子核位置變成參數（[[來源-AW02D]] slide 4）：
$$
\Psi\big(x_1,y_1,z_1,\alpha_1,\dots,x_{N_e},y_{N_e},z_{N_e},\alpha_{N_e};\,[\vec R_1,\dots,\vec R_{N_n}]\big)
$$
符號說明：$(x,y,z)$ 是空間座標，$\alpha$ 是自旋座標，所以每個粒子 4 個變數；$\vec R$ 是原子核位置（參數）。

## Physical meaning
- 古典圖像（[[來源-AW02D]] slide 3）：
  - 原子核與電子受大小相同、方向相反的力 $F$；
  - 加速度分別是 $F/M$ 與 $F/m$；
  - 因為 $M\gg m$，同一段時間 $\Delta t$ 後兩者的速度 $v_1\ll v_2$。
- 結果 1：變數從 $4(N_e+N_n)$ 個減為 $4N_e$ 個（[[來源-AW02D]] slide 4）。
- 結果 2：Hamiltonian 簡化（[[來源-AW02D]] slide 5）：
  - 原子核的動能項被劃掉；
  - 核–核 Coulomb 排斥項變成常數。

  見 [[Hamiltonian of a solid]]。
- 這是很大的簡化，但得到的方程式仍然難解得多，還需要更多近似（[[來源-AW02D]] slide 5）。
- 幾乎所有固體的 DFT 計算都假設它成立（[[來源-AW02D]] 主題頁）。

## Validity and common misconceptions
- 它是近似：主題頁請學員從推導想想哪些情況會失效（[[來源-AW02D]] 主題頁）。講義的進階閱讀談 nonadiabaticity，以及氫鍵的量子特性（[[來源-AW02D]] slide 6）。
- 凍結原子核不代表原子核不動：原子核位置成為參數，可以在 geometry optimization 或 phonon 計算中改變（後面單元）。這是一般知識的延伸。
