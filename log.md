# Log

只往後加，不改舊紀錄。格式見 AGENTS.md §5。

## [2026-11-16] setup | 建庫（M0）：沿用 mse-wiki 架構；AGENTS.md（規則）、PRD.md、DESIGN.md、README.md、skills（ingest-topic、query、lint、publish）、範本（標題英文）、scripts（fetch_topic、extract_text、lint、hooks）、Quartz＋GitHub Pages 部署設定
## [2026-11-16] lint | M0 檢查：lint 對 11 種錯誤案例全部報錯、單頁 hook 正常、Quartz 手機版與 Mermaid 正常。修正 fetch_topic.py（主題頁文字改從內容區擷取、截掉討論區的他人帳號與 email、抓 Elementor 影片、單元模式略過 webinar/exit/project、字幕加 --ignore-no-formats-error、新增 --refresh-pages）；index 的 AI 說明改成 Obsidian 註解、首頁標題改 Home。發現講義是掃描影像，OCR 與出處粒度待決定（PRD §9）
## [2026-11-16] setup | 講義改用投影片編號出處：extract_text.py 把講義切成投影片（s<K>.txt），掃描或亂碼文字層用 tesseract OCR（psm 3 才抓得到標題）；lint 改驗證 slide 編號、模糊比對引號原文、擋 p.N；AGENTS、DESIGN、PRD、範本、skills、README 同步。測試：AW02A 5 張、AW03C 3 張投影片，lint 6 個案例全部正確
## [2026-11-16] ingest | U01 setting the stage：來源-AW01F-creation、AW01B、AW01C、AW01D、AW01E、AW01F、AW01G、AW01H、lets-play-w1 → 11 概念、1 邏輯鏈、1 實作、測試題 10 題；⚠️待查證 3。extract_text.py 改用投影片左邊框切投影片（舊方法會漏掉只有淺色字的投影片）；講義的 spoiler 方塊下文字層仍在，內容已用自己的話寫入並註明
## [2026-11-16] ingest | U02 density functional theory：來源-AW02A–G、AW02F-quiz、AW03A–H、AW03A-bis、AW03G-bis/tris、AW03H-teaser、basis-sets-1/2、lets-play-w2/w3a/w3b（25 頁）→ 28 概念、3 方程式、2 推導、2 邏輯鏈、2 實作、1 習題、1 綜合（HF versus DFT），測試題增至 19 題；⚠️待查證新增 2（AW02F 投影片 e–e 項符號、QE K_POINTS 位置）。extract_text.py：右邊界取投影片外框、只有 handouts 才切投影片、重做時清掉舊檔；lint 新增 `\,'` 檢查（KaTeX 無法解析）
## [2026-11-16] publish | M3：建立公開 repo kumilz030/CMP-wiki、啟用 GitHub Pages（GitHub Actions）、第一次部署。push 前把 5 個 commit 的作者 email 改成 GitHub noreply（使用者同意的例外），commit 雜湊因此改變，舊→新：96a4abd→407be8d、3072775→894ee42、7e6639a→19b7edc、566133c→b9d9233、c4acf06→e9ad8d0（commit 訊息與上面 log 中的「起點」仍是舊雜湊）
## [2026-11-16] lint | knowledge base test questions 19/19 通過；lint 0 錯誤；⚠️待查證 5
## [2026-11-23] setup | topic-slides workflow（依「10 把你的工作拆成 AI 能做的流程」p.41–47 的 Graph）：`.agents/workflows/topic-slides.md`、`/topic-slides` skill、`scripts/slides/`（coverage_check、make_cards、check_drafts、render_deck、render_check）；產出 `slides/topic-dft-basics/deck.html`（15 頁），忠實度與渲染檢查全過，AI 審查 3 輪後通過，紀錄見該資料夾的 report.md
