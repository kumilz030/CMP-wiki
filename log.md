# Log

只往後加，不改舊紀錄。格式見 AGENTS.md §5。

## [2026-11-16] setup | 建庫（M0）：沿用 mse-wiki 架構；AGENTS.md（規則）、PRD.md、DESIGN.md、README.md、skills（ingest-topic、query、lint、publish）、範本（標題英文）、scripts（fetch_topic、extract_text、lint、hooks）、Quartz＋GitHub Pages 部署設定
## [2026-11-16] lint | M0 檢查：lint 對 11 種錯誤案例全部報錯、單頁 hook 正常、Quartz 手機版與 Mermaid 正常。修正 fetch_topic.py（主題頁文字改從內容區擷取、截掉討論區的他人帳號與 email、抓 Elementor 影片、單元模式略過 webinar/exit/project、字幕加 --ignore-no-formats-error、新增 --refresh-pages）；index 的 AI 說明改成 Obsidian 註解、首頁標題改 Home。發現講義是掃描影像，OCR 與出處粒度待決定（PRD §9）
## [2026-11-16] setup | 講義改用投影片編號出處：extract_text.py 把講義切成投影片（s<K>.txt），掃描或亂碼文字層用 tesseract OCR（psm 3 才抓得到標題）；lint 改驗證 slide 編號、模糊比對引號原文、擋 p.N；AGENTS、DESIGN、PRD、範本、skills、README 同步。測試：AW02A 5 張、AW03C 3 張投影片，lint 6 個案例全部正確
