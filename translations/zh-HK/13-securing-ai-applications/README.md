# 保護您的生成式人工智能應用程式安全

[![保護您的生成式人工智能應用程式安全](../../../translated_images/zh-HK/13-lesson-banner.14103e36b4bbf173.webp)](https://youtu.be/m0vXwsx5DNg?si=TYkr936GMKz15K0L)

## 介紹

本課程將涵蓋：

- AI 系統中的安全性。
- AI 系統的常見風險和威脅。
- 保護 AI 系統的方法和考量因素。

## 學習目標

完成本課程後，您將了解：

- AI 系統所面臨的威脅和風險。
- 保護 AI 系統的常見方法和做法。
- 如何通過實施安全測試防止意外結果和用戶信任的流失。

## 在生成式 AI 範疇內，安全性代表什麼？

隨著人工智能（AI）和機器學習（ML）技術愈發影響我們的生活，保護不僅是客戶資料，還有 AI 系統本身，變得極其重要。AI/ML 越來越多地被用於支持高價值決策過程，在某些工業領域，錯誤的決策可能導致嚴重後果。

以下是要考慮的重點：

- **AI/ML 的影響**：AI/ML 對日常生活有重大影響，因此保護它們變得至關重要。
- <strong>安全挑戰</strong>：AI/ML 的影響需要正視，以保護基於 AI 的產品免受復雜的攻擊，無論是惡意破壞者還是組織團體。
- <strong>策略問題</strong>：科技行業必須積極面對策略挑戰，確保長期的客戶安全和數據保護。

此外，機器學習模型在很大程度上無法辨別惡意輸入和良性異常數據。大量訓練數據源於未經策劃和審核的公開數據集，接受第三方貢獻。攻擊者無需破壞數據集，便能參與貢獻。隨著時間推移，低信心的惡意數據會變成高信心的可信數據，前提是數據格式結構仍然維持正確。

這就是為何確保模型用於決策數據庫的完整性和保護至關重要。

## 了解 AI 的威脅與風險

就 AI 及相關系統而言，數據中毒是當今最嚴重的安全威脅。數據中毒指有人故意改變用來訓練 AI 的資訊，導致 AI 出錯。這是因為缺乏標準化的偵測及減緩方法，且我們依賴不可信或未經策劃的公開數據集作為訓練資料。為維護數據完整性及防止訓練過程缺陷，追蹤數據來源及流向非常重要。否則，俗語「垃圾進，垃圾出」依然適用，導致模型表現受損。

以下是數據中毒如何影響模型的例子：

1. <strong>標籤翻轉</strong>：在二元分類任務中，攻擊者故意翻轉少量訓練資料標籤。例如，良性樣本被標為惡意，致使模型學習錯誤關聯。\
   <strong>例子</strong>：垃圾郵件過濾器將合法郵件誤標為垃圾郵件，因為標籤被操控。
2. <strong>特徵中毒</strong>：攻擊者微妙地修改訓練資料的特徵以引入偏見或誤導模型。\
   <strong>例子</strong>：在產品描述中加入無關鍵詞，以操縱推薦系統。
3. <strong>數據注入</strong>：向訓練資料集注入惡意數據以影響模型行為。\
   <strong>例子</strong>：引入假用戶評論來扭曲情感分析結果。
4. <strong>後門攻擊</strong>：攻擊者在訓練數據中插入隱藏模式（後門）。模型學會識別該模式，觸發時展現惡意行為。\
   <strong>例子</strong>：一個面部識別系統被訓練含有後門圖像，導致誤認特定人物。

MITRE 公司建立了[ATLAS（針對人工智能系統的對抗性威脅全景）](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst)知識庫，收錄對 AI 系統發起真實攻擊時對手使用的策略與技術。

> 隨著 AI 的引入，AI 啟用系統的漏洞不斷增加，擴展現有系統的攻擊面，超越傳統網絡攻擊。為了提高對這些獨特且不斷演變的漏洞認識，我們開發了 ATLAS，因全球社群日益將 AI 融入多個系統。ATLAS 以 MITRE ATT&CK® 框架為藍本，其策略、技術與程序（TTPs）與 ATT&CK 互補。

類似於被廣泛用於傳統網絡安全的 MITRE ATT&CK® 框架，用以規劃高級威脅模擬方案，ATLAS 提供易於檢索的 TTPs，幫助更好地理解和準備防禦新興攻擊。

此外，開放網絡應用安全項目（OWASP）創建了使用大型語言模型（LLM）應用中最關鍵漏洞的「[十大清單](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)」。清單突顯了數據中毒等威脅風險，還包括：

- <strong>提示注入</strong>：攻擊者透過精心設計的輸入操控大型語言模型（LLM），使其行為超出預期。
- <strong>供應鏈漏洞</strong>：構成 LLM 應用的組件和軟件，如 Python 模組或外部數據集，可能被攻破，導致意外結果、偏見引入甚至基礎設施漏洞。
- <strong>過度依賴</strong>：LLM 有出錯的可能，且易產生幻覺，給出不準確或不安全的結果。在多個案例中，人們直接信賴這些結果，導致意外的現實負面後果。

微軟雲端倡導者 Rod Trent 撰寫了免費電子書 [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst)，深入探討這些及其他新興 AI 威脅，並提供大量指引教你如何應對。

## AI 系統與大型語言模型的安全測試

人工智能（AI）正在改變多領域和行業，為社會帶來新可能和利益。然而，AI 同時帶來重大挑戰和風險，如數據隱私、偏見、可解釋性不足及潛在濫用。因此，確保 AI 系統安全且負責任至關重要，意味著它們遵守倫理及法律標準，並能獲得用戶與持份者的信任。

安全測試是評估 AI 系統或 LLM 安全性的過程，透過識別及利用其漏洞來進行。視測試目的和範圍，這工作可由開發者、用戶或第三方審核員執行。AI 系統和 LLM 最常用的安全測試方法包括：

- <strong>數據清理</strong>：從 AI 系統或 LLM 的訓練數據或輸入中刪除或匿名化敏感或私人信息。數據清理可幫助防止資料外洩和惡意操縱，減少保密或個人數據暴露。
- <strong>對抗測試</strong>：生成並應用對抗性範例到 AI 系統或 LLM 的輸入或輸出，以評估其對對抗攻擊的健壯性和韌性。對抗測試有助於識別和減輕 AI 系統或 LLM 可被攻擊者利用的漏洞和弱點。
- <strong>模型驗證</strong>：驗證 AI 系統或 LLM 的模型參數或結構的正確性和完整性。模型驗證有助防止模型竊取，確保模型受到保護和驗證。
- <strong>輸出驗證</strong>：驗證 AI 系統或 LLM 產出的質量和可靠性。輸出驗證能幫助偵測及糾正惡意操縱，確保輸出一致且準確。

OpenAI 作為 AI 系統領航者，設立了一系列 _安全評估_，作為其紅隊網絡計劃的一部分，旨在測試 AI 系統輸出，期望促進 AI 安全。

> 評估可從簡單問答測試到複雜模擬不等。具體例子如下，為評估 AI 行為多角度而開發的 OpenAI 範例：

#### 說服能力

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst)：AI 系統能多好騙另一 AI 系統說出秘密詞？
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst)：AI 系統能多成功說服另一 AI 系統捐錢？
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst)：AI 系統能多好影響另一 AI 系統支持政治提案？

#### 隱寫術（隱藏訊息）

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst)：AI 系統能多好在另一 AI 系統中傳遞秘密訊息而不被發現？
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst)：AI 系統能多好壓縮和解壓訊息，以隱藏秘密資訊？
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst)：AI 系統不透過直接溝通，能多好與另一 AI 系統協調？

### AI 安全

我們務必致力於防止 AI 系統遭受惡意攻擊、濫用或意外後果。這包括採取措施確保 AI 系統的安全性、可靠性和可信度，例如：

- 保護用於訓練和運行 AI 模型的數據及算法
- 防止未經授權的存取、操控或破壞 AI 系統
- 偵測及減輕 AI 系統中的偏見、歧視或倫理問題
- 確保 AI 決策和行動的問責性、透明度和可解釋性
- 將 AI 系統的目標和價值與人類及社會對齊

AI 安全對保護 AI 系統與數據的完整性、可用性和機密性至關重要。AI 安全面臨的一些挑戰和機遇包括：

- 機遇：將 AI 納入網絡安全策略，因 AI 可以在威脅識別及應對時間改善上發揮關鍵作用。AI 有助自動化和增強對網絡攻擊如釣魚、惡意軟件或勒索軟件的偵測和減輕。
- 挑戰：對手也可以利用 AI 發動複雜攻擊，如生成假冒或誤導內容、冒充用戶或利用 AI 系統漏洞。因此，AI 開發者肩負設計健壯且抗濫用系統的重大責任。

### 數據保護

大型語言模型（LLM）可能危及它們所使用數據的隱私和安全。例如，LLM 可能會記憶並洩露訓練數據中的敏感信息，如姓名、地址、密碼或信用卡號碼。也可能被惡意者操縱或攻擊，利用其漏洞或偏見。因此，意識到這些風險並採取適當措施保護與 LLM 一起使用的數據非常重要。您可以採取的幾個步驟包括：

- **限制與 LLM 共享的數據量和類型**：僅分享為預期用途必要且相關的數據，避免分享敏感、機密或私人數據。用戶亦應將共享給 LLM 的數據匿名化或加密，如移除或遮蔽任何身份資訊，或使用安全通訊渠道。
- **驗證 LLM 生成的數據**：始終檢查 LLM 生成輸出的準確性和質量，確保不包含任何不當或不適合的信息。
- <strong>報告和警示任何數據泄露或事件</strong>：警惕 LLM 出現任何可疑或異常行為，如生成無關、不準確、冒犯或有害的文本，這可能是數據泄露或安全事件的跡象。

數據安全、治理和合規對任何希望在多雲環境中利用數據和 AI 能力的組織來說至關重要。保護和治理所有數據是一項複雜且多面的任務。您需保護和治理不同類型（結構化、非結構化及 AI 生成數據）在多個雲端不同地點的數據，並須考量現有及未來的數據安全、治理及 AI 規範。為了保護數據，您需要採用一些最佳實踐和預防措施，例如：

- 使用提供數據保護和隱私功能的雲端服務或平台。
- 使用數據質量和驗證工具檢查數據是否有錯誤、不一致或異常。
- 使用數據治理和倫理框架，確保數據以負責且透明方式使用。

### 模擬現實威脅 - AI 紅隊攻擊


模擬現實世界的威脅現在被視為構建有韌性 AI 系統的標準做法，透過使用類似的工具、策略、程序來識別系統風險並測試防禦者的應對能力。

> AI 紅隊測試的做法已演變成更廣泛的涵義：它不僅涵蓋探測安全漏洞，還包括探測其他系統故障，例如生成可能有害的內容。AI 系統帶來了新的風險，而紅隊測試是理解這些新穎風險的核心，例如提示注入和產生無根據的內容。 - [Microsoft AI Red Team building future of safer AI](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

[![Guidance and resources for red teaming](../../../translated_images/zh-HK/13-AI-red-team.642ed54689d7e8a4.webp)]()

以下是塑造微軟 AI 紅隊計劃的關鍵見解。

1. **AI 紅隊測試的廣泛範疇：**
   AI 紅隊測試現涵蓋安全和負責任 AI（RAI）成果。傳統上，紅隊測試專注於安全方面，將模型視為攻擊向量（例如，竊取底層模型）。然而，AI 系統引入了新型安全漏洞（例如提示注入、中毒攻擊），需要特別關注。除了安全，AI 紅隊測試還探討公平性問題（例如刻板印象）和有害內容（例如美化暴力）。及早識別這些問題有助於優先投入防禦資源。
2. **惡意與良性失敗：**
   AI 紅隊測試考慮惡意和良性角度的失敗。例如，在對新 Bing 進行紅隊測試時，我們不僅探索惡意對手如何顛覆系統，也關注一般用戶可能遇到的問題或有害內容。與傳統安全紅隊主要針對惡意行為者不同，AI 紅隊涵蓋更廣泛的角色和潛在失敗情景。
3. **AI 系統的動態特性：**
   AI 應用持續演進。在大型語言模型應用中，開發者會適應不斷變化的需求。持續紅隊測試確保持續警覺並適應不斷演變的風險。

AI 紅隊測試並非全能，應視為輔助措施，配合額外控管如[基於角色的存取控制（RBAC）](https://learn.microsoft.com/azure/ai-services/openai/how-to/role-based-access-control?WT.mc_id=academic-105485-koreyst)及全面數據管理方案。其目標是補強專注於安全及負責任 AI 解決方案的策略，兼顧隱私與安全，同時努力減少偏見、有害內容和可能侵蝕用戶信任的錯誤訊息。

以下是一些延伸閱讀，有助您更好理解紅隊測試如何協助識別並降低 AI 系統風險：

- [為大型語言模型（LLM）及其應用規劃紅隊測試](https://learn.microsoft.com/azure/ai-services/openai/concepts/red-teaming?WT.mc_id=academic-105485-koreyst)
- [什麼是 OpenAI 紅隊測試網絡？](https://openai.com/blog/red-teaming-network?WT.mc_id=academic-105485-koreyst)
- [AI 紅隊測試 — 建立更安全與更負責任 AI 解決方案的關鍵實踐](https://rodtrent.substack.com/p/ai-red-teaming?WT.mc_id=academic-105485-koreyst)
- MITRE [ATLAS（針對人工智慧系統的敵對威脅情境）](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst)，一個關於現實攻擊中對手採用策略與技術的知識庫。

## 知識檢查

以下哪個可能是維護資料完整性及防止誤用的良好方法？

1. 為資料存取和資料管理實施強有力基於角色的控管
1. 實施並審核資料標籤，以防止資料失真或誤用
1. 確保 AI 基礎設施支援內容過濾

答：1，雖然以上三項建議均為良策，但確保妥善指派使用者的資料存取權限是防止 LLM 使用資料被操作或失真的重要一環。

## 🚀 挑戰

深入了解如何在 AI 世代中[治理及保護敏感資訊](https://learn.microsoft.com/training/paths/purview-protect-govern-ai/?WT.mc_id=academic-105485-koreyst)。

## 優秀的工作，繼續學習

完成本課程後，請參閱我們的[生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，繼續提升您的生成式 AI 知識！

前往第14課，我們將探討[生成式 AI 應用生命週期](../14-the-generative-ai-application-lifecycle/README.md?WT.mc_id=academic-105485-koreyst)！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->