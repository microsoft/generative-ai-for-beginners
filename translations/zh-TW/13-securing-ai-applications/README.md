# 保護您的生成式 AI 應用程式安全

[![保護您的生成式 AI 應用程式安全](../../../translated_images/zh-TW/13-lesson-banner.14103e36b4bbf173.webp)](https://youtu.be/m0vXwsx5DNg?si=TYkr936GMKz15K0L)

## 介紹

本課程將涵蓋：

- AI 系統背景下的安全性。
- AI 系統的常見風險與威脅。
- 保護 AI 系統的方法與考量。

## 學習目標

完成本課程後，您將了解：

- AI 系統的威脅與風險。
- 常見的 AI 系統安全保護方法與實務。
- 如何透過實施安全測試防止意外結果及使用者信任流失。

## 在生成式 AI 背景下，安全性意味著什麼？

隨著人工智慧（AI）與機器學習（ML）技術日益影響我們生活，保護不僅是客戶資料，還有 AI 系統本身，變得至關重要。AI/ML 越來越多用於高價值決策過程，錯誤決策可能導致嚴重後果的行業尤須關注。

這裡是需要考慮的重點：

- **AI/ML 的影響**：AI/ML 對日常生活有重大影響，因此保障 AI/ML 變得不可或缺。
- <strong>安全挑戰</strong>：AI/ML 帶來的影響需要得到適當關注，以保護基於 AI 的產品免受複雜攻擊，無論是惡意騷擾者或組織團體。
- <strong>策略問題</strong>：科技業必須積極面對策略性挑戰，以確保長期客戶安全與資料保護。

此外，機器學習模型大多無法區分惡意輸入和良性異常資料。大量訓練資料來自未經篩選、未經審查的公開數據集，開放第三方貢獻。攻擊者不需入侵數據集，只要自由參與即可。隨著時間，低信心惡意資料若結構與格式正確，會變成高信心可信資料。

因此，確保您的模型用來做決策的資料存儲完整性與保護至關重要。

## 理解 AI 的威脅與風險

就 AI 相關系統而言，數據中毒是當今最重要的安全威脅。數據中毒指有人故意更改用於訓練 AI 的資訊，導致其出錯。這是因缺乏標準化檢測與緩解方法，加上仰賴不可信或未經篩選的公共數據集。為維護資料完整並防止訓練過程瑕疵，追蹤資料來源與沿革非常重要。否則，「垃圾進，垃圾出」的老話不會有錯，模型效能會受損。

以下是數據中毒對模型影響的例子：

1. <strong>標籤翻轉</strong>：在二元分類任務中，敵手故意翻轉部分訓練數據的標籤。例如，良性樣本被標註為惡意，導致模型學習錯誤關聯。\
   <strong>範例</strong>：垃圾郵件過濾器因標籤被操縱，誤將合法郵件歸為垃圾郵件。
2. <strong>特徵中毒</strong>：攻擊者微妙修改訓練數據的特徵，導入偏見或誤導模型。\
   <strong>範例</strong>：在產品描述中加入無關關鍵字，操控推薦系統。
3. <strong>數據注入</strong>：將惡意資料注入訓練集，影響模型行為。\
   <strong>範例</strong>：引入假用戶評論，偏斜情感分析結果。
4. <strong>後門攻擊</strong>：敵手在訓練資料中嵌入隱藏模式（後門）。模型學會辨識此模式，一旦觸發即可惡意運作。\
   <strong>範例</strong>：臉部辨識系統在後門圖像訓練下誤認特定人物。

MITRE 公司創建了 [ATLAS (人工智慧系統之對抗威脅狀況)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst) 知識庫，匯整真實對 AI 系統攻擊中使用的策略與技術。

> AI 系統中漏洞日增，因 AI 納入使傳統系統攻擊面擴大。我們開發 ATLAS 以提高對這些獨特且持續演化漏洞的認知，因全球社群日益將 AI 融入各類系統。ATLAS 模仿 MITRE ATT&CK® 框架，其策略、技術與程序（TTP）與 ATT&CK 互補。

與廣泛應用於傳統網路安全用以規劃高端威脅模擬場景的 MITRE ATT&CK® 框架類似，ATLAS 提供易於搜尋的 TTP，幫助更好理解與準備防禦新興攻擊。

此外，開放網路應用安全計畫（OWASP）也製作了利用大型語言模型（LLM）應用的「[十大漏洞清單](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)」。該清單凸顯數據中毒等威脅風險，還有其他風險，包括：

- <strong>提示注入</strong>：攻擊者透過巧妙設計輸入操控大型語言模型（LLM），使其行為偏離預期。
- <strong>供應鏈漏洞</strong>：構成 LLM 應用的組件與軟體，例如 Python 模組或外部數據集，可能被入侵，導致意外結果、引入偏見甚或基礎設施漏洞。
- <strong>過度依賴</strong>：LLM 有錯誤生成（幻覺）風險，可能提供不正確或不安全結果。在多次記錄中，人們輕信結果導致真實世界的負面後果。

微軟雲端架構師 Rod Trent 撰寫免費電子書 [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst)，深入探討這些及其他新興 AI 威脅，並提供詳細應對指導。

## AI 系統與大型語言模型的安全測試

人工智慧（AI）正在轉變各領域與產業，為社會帶來新契機與利益。然而，AI 也帶來重大挑戰與風險，如資料隱私、偏見、缺乏解釋性及潛在誤用。因此，確保 AI 系統安全與負責是關鍵，意味著系統須符合法律與倫理標準，並獲得使用者與利害關係人的信任。

安全測試是評估 AI 系統或 LLM 安全性的過程，透過識別並利用其漏洞。此測試可由開發者、使用者或第三方審核者依目的與範圍執行。AI 系統與 LLM 常見的安全測試方法包括：

- <strong>資料淨化</strong>：從 AI 系統或 LLM 的訓練資料或輸入中移除或匿名化敏感或私人資訊。資料淨化可降低機密或個人資料暴露，防止資料外洩與惡意操控。
- <strong>對抗性測試</strong>：生成和應用對抗性範例於 AI 系統或 LLM 的輸入或輸出，以評估其對對抗攻擊的韌性與抵抗力。對抗性測試有助識別並減輕系統可能被攻擊者利用的漏洞和弱點。
- <strong>模型驗證</strong>：驗證 AI 系統或 LLM 的模型參數或架構正確性與完整性。模型驗證有助偵測並防止模型盜用，確保模型安全與身份認證。
- <strong>輸出驗證</strong>：驗證 AI 系統或 LLM 輸出的品質與可靠性。輸出驗證有助識別並糾正惡意操控，確保輸出結果一致且準確。

AI 系統領導者 OpenAI 設置了一系列 _安全評估_，作為其紅隊網絡計畫的一部分，目標是測試 AI 系統輸出，促進 AI 安全。

> 評估範圍從簡單問答測試到更複雜模擬不等。以具體例子來說，以下是 OpenAI 為多角度評估 AI 行為開發的測試示範：

#### 說服能力

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst)：AI 系統能多好地誘導另一個 AI 系統說出秘密詞？
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst)：AI 系統能多好說服另一個 AI 系統捐款？
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst)：AI 系統能多好影響另一個 AI 系統支持政治提案？

#### 隱寫術（隱藏訊息）

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst)：AI 系統能多好在不被另一個 AI 系統察覺下傳遞秘密訊息？
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst)：AI 系統能多好壓縮與解壓訊息以隱藏秘密？
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst)：AI 系統能多好在無直接通訊的情況下與另一個 AI 系統協調？

### AI 安全

我們必須致力保護 AI 系統免受惡意攻擊、誤用或非預期後果。包括確保 AI 系統的安全性、可靠性與可信度，如下：

- 保護用於訓練與執行 AI 模型的資料與演算法
- 防止未經授權的存取、操控或破壞 AI 系統
- 偵測並減輕偏見、歧視或倫理問題
- 確保 AI 決策與行動的問責性、透明度與可解釋性
- 將 AI 系統的目標與人類及社會價值對齊

AI 安全對維護 AI 系統和資料的完整性、可用性與機密性至關重要。AI 安全的挑戰與機會包括：

- 機會：將 AI 納入網路安全策略，可加速威脅識別並改善回應時間。AI 助于自動化及強化釣魚、惡意軟體或勒索軟體等攻擊的偵測與緩解。
- 挑戰：敵手也可利用 AI 發動複雜攻擊，如生成假或誤導內容、冒充用戶或利用 AI 系統漏洞。因此 AI 開發者有獨特責任設計強韌且具抗濫用性的系統。

### 資料保護

LLM 可能威脅其使用的資料隱私與安全。例如，LLM 可能記憶並洩漏敏感訓練資料，如姓名、地址、密碼或信用卡號碼。它們也可能被惡意者操控或攻擊，利用其漏洞或偏見。因此，了解這些風險並採取適當措施保護資料至關重要。可以採取的保護步驟包括：

- **限制與 LLM 分享的資料量與類型**：只分享必要且相關的資料，避免分享敏感、機密或個人資料。用戶也應對分享給 LLM 的資料匿名化或加密，如移除或遮蔽識別資訊，或使用安全通訊通道。
- **驗證 LLM 生成的資料**：始終檢查 LLM 輸出準確性與品質，確保不含不當或不適內容。
- <strong>通報並警示任何資料外洩或事件</strong>：留意 LLM 產生的任何異常或可疑行為，如產生不相關、不準確、冒犯或有害文本，有助於及時發現安全事件。

資料安全、治理與合規對於想要在多雲環境中發揮資料與 AI 力量的組織非常重要。保護與治理所有資料是一項複雜多面向工作。您需要分別保護與治理來自多雲中不同地點的不同類型資料（結構化、非結構化，以及 AI 生成資料），並考量現有及未來的資料安全、治理和 AI 規範。為保護資料，需採用最佳實務與預防措施，例如：

- 使用提供資料保護與隱私功能的雲端服務或平台。
- 使用資料品質與驗證工具檢查資料中錯誤、不一致或異常。
- 使用資料治理與倫理框架，確保資料負責任且透明的使用。

### 模擬真實世界威脅 - AI 紅隊測試


模擬現實世界威脅現在被視為構建具韌性 AI 系統的標準做法，透過使用類似的工具、策略、程序來識別系統風險並測試防禦者的應對能力。

> AI 紅隊演練的實務已發展為更廣泛的意涵：它不僅涵蓋探索安全漏洞，還包括探查其他系統失效，如可能產生有害內容。AI 系統帶來新風險，紅隊演練是了解這些新穎風險的核心，例如提示注入和產生無根據內容。 - [Microsoft AI Red Team building future of safer AI](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

[![Guidance and resources for red teaming](../../../translated_images/zh-TW/13-AI-red-team.642ed54689d7e8a4.webp)]()

以下是塑造 Microsoft AI 紅隊計畫的關鍵見解。

1. **AI 紅隊演練的廣泛範圍：**
   AI 紅隊演練現在涵蓋安全與負責任 AI（RAI）結果。傳統紅隊演練聚焦於安全面，將模型視為攻擊向量（例如竊取底層模型）。但 AI 系統帶來新穎安全漏洞（例如提示注入、中毒），需要特別關注。除了安全外，AI 紅隊還探討公平性問題（例如刻板印象）和有害內容（例如暴力美化）。早期辨識這些議題有助優先分配防禦投資。
2. **惡意與良性失效：**
   AI 紅隊演練考慮來自惡意與良性角度的失效。例如在對新 Bing 進行紅隊測試時，我們不只探索惡意攻擊者如何破壞系統，也關注一般用戶可能遭遇的問題或有害內容。與傳統只聚焦惡意行為者的安全紅隊不同，AI 紅隊涵蓋更廣泛的角色與潛在失效場景。
3. **AI 系統的動態本質：**
   AI 應用持續演變。大型語言模型應用中，開發者會適應變動需求。持續的紅隊演練確保持續警覺並調整因應演變中的風險。

AI 紅隊演練不是全能的，應視為補充額外控制措施的動作，如[基於角色的存取控制(RBAC)](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/role-based-access-control?WT.mc_id=academic-105485-koreyst)及全面資料管理解決方案。它旨在補強專注於使用安全且負責任 AI 解決方案的安全策略，兼顧隱私與安全，同時盡量降低偏見、有害內容和會侵蝕用戶信任的錯誤資訊。

以下是一系列進階閱讀，幫助你更理解紅隊演練如何協助識別及減輕 AI 系統中的風險：

- [大型語言模型(LLMs)及其應用的紅隊規劃](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/red-teaming?WT.mc_id=academic-105485-koreyst)
- [什麼是 OpenAI 紅隊網絡？](https://openai.com/blog/red-teaming-network?WT.mc_id=academic-105485-koreyst)
- [AI 紅隊演練 — 建構更安全與負責任 AI 解決方案的關鍵實務](https://rodtrent.substack.com/p/ai-red-teaming?WT.mc_id=academic-105485-koreyst)
- MITRE [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst)，一個有關現實攻擊中對 AI 系統使用的敵對策略與技術的知識庫。

## 知識檢核

維護資料完整性及防止誤用的良好做法可能是什麼？

1. 為資料存取和資料管理設置強化基於角色的控制
1. 實施並稽核資料標註，以防止資料誤用或誤導
1. 確保你的 AI 基礎設施支持內容過濾

A:1，雖然以上三者建議皆優秀，但確保你為用戶分配正確的資料存取權限，是防止大型語言模型所使用資料遭篡改與誤用的關鍵。

## 🚀 挑戰

更深入閱讀如何在 AI 時代中[治理與保護敏感資訊](https://learn.microsoft.com/training/paths/purview-protect-govern-ai/?WT.mc_id=academic-105485-koreyst)。

## 做得好，繼續學習

完成本課程後，請查看我們的[生成式 AI 學習收藏](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，繼續提升你的生成式 AI 知識！

前往第 14 課，我們將探討[生成式 AI 應用生命週期](../14-the-generative-ai-application-lifecycle/README.md?WT.mc_id=academic-105485-koreyst)！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->