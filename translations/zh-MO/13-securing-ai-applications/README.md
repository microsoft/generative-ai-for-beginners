# 保護您的生成式 AI 應用程式

[![保護您的生成式 AI 應用程式](../../../translated_images/zh-MO/13-lesson-banner.14103e36b4bbf173.webp)](https://youtu.be/m0vXwsx5DNg?si=TYkr936GMKz15K0L)

## 介紹

本課程將涵蓋：

- AI 系統背景下的安全性。
- AI 系統的常見風險和威脅。
- 保護 AI 系統的方法與考量。

## 學習目標

完成本課程後，您將了解：

- AI 系統的威脅與風險。
- 保護 AI 系統的常見方法與實務。
- 如何透過實行安全測試來防止意外結果與使用者信任流失。

## 在生成式 AI 背景下，安全性是指什麼？

隨著人工智慧（AI）與機器學習（ML）技術日益影響我們的生活，除了保護客戶資料外，也必須保護 AI 系統本身。AI/ML 被廣泛用於高價值決策過程中，這些產業中錯誤決策可能導致嚴重後果。

以下是需考慮的要點：

- **AI/ML 的影響力**：AI/ML 對日常生活的影響重大，因此保護它們變得非常重要。
- <strong>安全性挑戰</strong>：必須妥善處理 AI/ML 造成的影響，以保護基於 AI 的產品免受惡意者、無論是網絡巨魔還是有組織團體的複雜攻擊。
- <strong>策略性問題</strong>：科技業必須主動面對策略挑戰，以確保長期客戶安全和資料保護。

此外，機器學習模型大多無法辨別惡意輸入與良性異常數據。訓練數據的重要來源是未經策劃、未經審核的公共資料集，允許第三方貢獻。攻擊者不需入侵資料集，便可自由貢獻惡意資料。隨時間推移，低信任度的惡意資料若格式正確，可能轉變成高信任度的可信資料。

因此，確保模型用於決策的資料存儲庫的完整性與保護至關重要。

## 理解 AI 的威脅與風險

就 AI 及相關系統而言，資料中毒是當今最重要的安全威脅。資料中毒是指有人故意改變用於訓練 AI 的資訊，使模型犯錯。由於缺乏標準化的偵測及緩解方法，且我們依賴不可信或未策劃的公共資料集進行訓練，追蹤資料的來源與血緣變得關鍵。否則「垃圾進，垃圾出」的老話不變，導致模型性能受損。

以下是資料中毒如何影響模型的示例：

1. <strong>標籤翻轉</strong>：在二元分類任務中，對部分訓練資料故意翻轉標籤。例如將良性樣本標示為惡意，令模型學習錯誤關聯。\
   <strong>範例</strong>：垃圾郵件過濾器因標籤被操控，錯誤將合法郵件分類為垃圾郵件。
2. <strong>特徵中毒</strong>：攻擊者微妙地修改訓練資料的特徵，引入偏差或誤導模型。\
   <strong>範例</strong>：在產品描述中添加無關關鍵字以操控推薦系統。
3. <strong>資料注入</strong>：將惡意數據注入訓練集，影響模型行為。\
   <strong>範例</strong>：加入虛假用戶評論以扭曲情感分析結果。
4. <strong>後門攻擊</strong>：在訓練資料中悄悄加入隱藏模式（後門）。模型學會辨識該模式，觸發時行為惡意。\
   <strong>範例</strong>：使用帶有後門的影像訓練臉部識別系統，錯誤辨識特定人物。

MITRE Corporation 創建了 [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst)，一個包含對 AI 系統真實攻擊中攻擊者戰術與技術的知識庫。

> AI 啟用的系統中的漏洞與日俱增，因為 AI 的整合擴大了現有系統的攻擊面，超越傳統網絡攻擊。為提升對這些獨特且不斷演變漏洞的認識，我們開發了 ATLAS，該系統基於 MITRE ATT&CK® 框架，其戰術、技術與程序（TTPs）是 ATT&CK 的補充。

類似於廣泛用於傳統網絡安全的 MITRE ATT&CK® 框架以規劃高級威脅模擬場景，ATLAS 提供易於搜尋的 TTPs，幫助更好理解及防禦新興攻擊。

此外，Open Web Application Security Project (OWASP) 創建了利用大型語言模型（LLMs）應用中最嚴重漏洞的「[Top 10 list](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)」。該列表強調前述資料中毒與其他威脅風險，如：

- **提示注入 (Prompt Injection)**：攻擊者透過精心設計的輸入操控大型語言模型，使其偏離預期行為。
- <strong>供應鏈漏洞</strong>：構成 LLM 應用的組件與軟件，例如 Python 模組或外部數據集，可能本身遭到攻擊，導致異常結果、偏見甚至基礎設施漏洞。
- <strong>過度依賴</strong>：LLM 優柔寡斷，常出現幻覺現象，生成不準確或不安全結果。在多個文件案例中，使用者過於信賴這些結果，造成意料之外的現實負面影響。

微軟雲端倡導者 Rod Trent 撰寫了免費電子書 [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst)，深入探討這些及其他新興 AI 威脅，並提供詳細應對指導。

## AI 系統與 LLM 的安全測試

人工智慧（AI）正轉變各領域與產業，為社會帶來新可能與利益。然而，AI 也帶來重要挑戰和風險，如資料隱私、偏見、不可解釋性及潛在誤用。因此，確保 AI 系統安全且負責任至關重要，即遵守倫理與法律標準，且能獲得用戶與利害關係人信賴。

安全測試是評估 AI 系統或 LLM 安全性的過程，透過識別與利用其漏洞來進行。根據測試目的與範圍，開發者、用戶或第三方審核者都可執行。AI 系統與 LLM 最常見的安全測試方法包括：

- <strong>資料清理</strong>：移除或匿名化訓練資料或 AI 系統及 LLM 輸入中的敏感或私密資訊。資料清理即可降低機密與個人資料暴露，防止資料外洩與惡意操控。
- <strong>對抗性測試</strong>：產生並應用對抗性樣本至 AI 系統或 LLM 的輸入輸出，以評估其對對抗攻擊的魯棒性與韌性。對抗性測試有助於識別並減輕攻擊者可能利用的漏洞與弱點。
- <strong>模型驗證</strong>：驗證 AI 系統或 LLM 的模型參數或架構的正確性與完整性。模型驗證可協助偵測與防止模型竊取，確保模型被妥善保護與認證。
- <strong>輸出驗證</strong>：驗證 AI 系統或 LLM 輸出品質及可靠性。輸出驗證可識別並修正惡意操控，確保輸出一致準確。

OpenAI 作為 AI 系統領導者，設置了一系列 _安全評估_，納入紅隊測試網絡計劃，旨在測試 AI 系統輸出以推進 AI 安全。

> 評估範圍從簡單問答測試到更複雜的模擬。以下是 OpenAI 開發的範例評估，用於多角度評估 AI 行為：

#### 說服力

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst)：AI 系統能多好欺騙另一 AI 系統說出秘密詞語？
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst)：AI 系統能多好說服另一 AI 系統捐款？
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst)：AI 系統能多好影響另一 AI 系統支持某政治提案？

#### 隱寫術（隱藏訊息）

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst)：AI 系統能多好傳遞秘密訊息而不被另一 AI 系統發現？
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst)：AI 系統能多好壓縮並解壓消息以藏匿秘密訊息？
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst)：AI 系統能多好在不直接溝通的情況下與另一 AI 系統協調？

### AI 安全

必須致力保護 AI 系統免受惡意攻擊、誤用或非預期後果，這包括採取措施確保 AI 系統的安全性、可靠性及可信度，例如：

- 保護用於訓練及運行 AI 模型的資料與演算法
- 防止未經授權的存取、操控或破壞 AI 系統
- 偵測及減輕 AI 系統中的偏見、歧視或倫理問題
- 確保 AI 決策和行動的問責、透明及可解釋性
- 將 AI 系統的目標與價值對齊至人類及社會

AI 安全對確保 AI 系統和資料的完整性、可用性及機密性至關重要。AI 安全的挑戰與機遇包括：

- 機遇：將 AI 整合至網絡安全策略中，因為 AI 可在識別威脅及提升反應速度上發揮重要角色。AI 可協助自動化及增強網絡攻擊的偵測與緩解，如網絡釣魚、惡意軟體或勒索軟件。
- 挑戰：攻擊者亦可利用 AI 發動複雜攻擊，例如生成假或誤導內容、冒充用戶，或利用 AI 系統中的漏洞。因此，AI 開發者肩負設計堅韌及抗誤用系統的獨特責任。

### 資料保護

大型語言模型（LLMs）可能對其使用資料的隱私和安全構成風險。例如，LLMs 可能記憶並洩漏訓練資料中的敏感資訊，如個人名字、地址、密碼或信用卡號碼。它們也可能被惡意者操控或攻擊，以利用其漏洞或偏見。因此，了解這些風險並採取適當措施保護與 LLMs 使用的資料非常重要。您可以採取以下幾個步驟保護所使用的資料：

- **限制與 LLMs 分享的資料量與種類**：僅共享對預期用途必要且相關的資料，避免分享敏感、機密或個人資料。使用者也應匿名化或加密與 LLMs 共享的資料，例如移除或隱藏任何識別資訊，或使用安全通訊通道。
- **驗證 LLMs 生成的資料**：始終檢查由 LLMs 生成輸出的準確性與品質，確保其不包含任何不當或不合適的資訊。
- <strong>報告並警示任何資料外洩或事故</strong>：對 LLMs 產生可疑或異常活動或行為保持警覺，如生成無關、不準確、冒犯或有害的文本。這可能是資料外洩或安全事件的徵兆。

資料安全、治理與合規對於希望在多雲環境中利用資料與 AI 力量的組織至關重要。保護與治理所有資料是一項複雜且多面的工作。您需要在多個雲端中的不同位置保護與治理不同類型的資料（結構化、非結構化及由 AI 生成的資料），同時需考慮現有及未來的資料安全、治理與 AI 規範。為保護資料，您需採取一些最佳實踐與預防措施，如：

- 使用提供資料保護與隱私功能的雲端服務或平台。
- 使用資料品質與驗證工具檢查資料的錯誤、不一致或異常。
- 使用資料治理與倫理框架，確保資料的負責任且透明使用。

### 模擬真實世界威脅 - AI 紅隊測試


模擬現實世界的威脅現已被視為建立具韌性 AI 系統的標準做法，透過採用相似的工具、策略、程序來識別系統風險並測試防禦者的應對能力。

> AI 紅隊實務已演變為更擴展的意義：它不僅涵蓋對安全漏洞的探測，還包括探測其他系統故障，例如生成潛在有害內容。AI 系統帶來新的風險，紅隊是理解這些新穎風險（例如提示注入與產生無根據內容）的核心。 - [Microsoft AI Red Team building future of safer AI](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

[![紅隊指導與資源](../../../translated_images/zh-MO/13-AI-red-team.642ed54689d7e8a4.webp)]()

以下為塑造 Microsoft AI 紅隊計劃的關鍵見解。

1. **AI 紅隊範圍擴大：**
   AI 紅隊現涵蓋安全和責任 AI (RAI) 成效。傳統上，紅隊聚焦安全面，視模型為攻擊向量（例如竊取基礎模型）。然而，AI 系統帶來新穎安全漏洞（例如提示注入、投毒），需特別關注。除安全外，AI 紅隊亦探查公平性議題（如刻板印象）及有害內容（如美化暴力）。及早識別這些問題有助優先投入防禦。
2. **惡意與善意失效：**
   AI 紅隊考慮來自惡意及善意角度的失效。例如，在對新 Bing 進行紅隊測試時，我們不僅探索惡意對手如何破壞系統，也關心一般用戶如何遇到問題或有害內容。與傳統安全紅隊主要針對惡意攻擊者不同，AI 紅隊涵蓋更廣泛的人物和潛在失效。
3. **AI 系統的動態特性：**
   AI 應用持續演進。在大型語言模型應用中，開發者須適應不斷變化的需求。持續紅隊測試確保持續警覺並調整以應對變化的風險。

AI 紅隊並非包羅萬象，應視為補充措施，配合其他控管如 [基於角色的存取控制 (RBAC)](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/role-based-access-control?WT.mc_id=academic-105485-koreyst)及全面數據管理方案。目標是補足以安全且負責任的 AI 解決方案為核心的安全策略，涵蓋隱私與安全，同時致力減少偏見、有害內容與可能侵蝕使用者信心的誤導資訊。

以下是幾個延伸閱讀，協助您更深入了解紅隊如何協助識別及減輕 AI 系統風險：

- [大型語言模型(LLMs)及其應用之紅隊規劃](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/red-teaming?WT.mc_id=academic-105485-koreyst)
- [什麼是 OpenAI 紅隊網絡？](https://openai.com/blog/red-teaming-network?WT.mc_id=academic-105485-koreyst)
- [AI 紅隊──建構更安全、更負責任 AI 解決方案的關鍵實務](https://rodtrent.substack.com/p/ai-red-teaming?WT.mc_id=academic-105485-koreyst)
- MITRE [ATLAS (人工智慧系統敵對威脅版圖)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst)，一個關於現實世界攻擊 AI 系統時對手所使用策略與技術的知識庫。

## 知識檢核

有效維持數據完整性及防止濫用的好方法是什麼？

1. 對數據存取與管理實施強大的基於角色控管
1. 實施與審核數據標記以防止數據被誤用或濫用
1. 確保您的 AI 架構支持內容過濾

A:1, 雖然這三點都是很好的建議，確保為使用者指派正確的數據存取權限將大大有助於防止 LLM 使用數據的操縱與誤用。

## 🚀 挑戰

深入了解您如何在 AI 時代下[管理與保護敏感資訊](https://learn.microsoft.com/training/paths/purview-protect-govern-ai/?WT.mc_id=academic-105485-koreyst)。

## 做得好，繼續學習

完成本課後，請參閱我們的[生成式 AI 學習收藏](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)以持續提升您的生成式 AI 知識！

轉到第 14 課，我們將探討[生成式 AI 應用生命週期](../14-the-generative-ai-application-lifecycle/README.md?WT.mc_id=academic-105485-koreyst)！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->