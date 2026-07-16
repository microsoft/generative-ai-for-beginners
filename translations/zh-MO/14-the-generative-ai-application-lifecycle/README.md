[![與功能呼叫整合](../../../translated_images/zh-MO/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# 生成式 AI 應用程式生命周期

對所有 AI 應用程式而言，一個重要的問題是 AI 功能的相關性，因為 AI 是一個快速發展的領域，為了確保您的應用程式保持相關性、可靠性和穩健性，您需要持續監控、評估和改進它。這就是生成式 AI 生命周期發揮作用的地方。

生成式 AI 生命周期是一個指導您開發、部署及維護生成式 AI 應用程式的框架。它幫助您定義目標、衡量績效、識別挑戰並實施解決方案。它也有助於使您的應用程式與您所屬領域及利益相關者的倫理和法律標準保持一致。遵循生成式 AI 生命周期，您可以確保您的應用程式始終提供價值並滿足使用者需求。

## 介紹

在本章節中，您將會：

- 了解從 MLOps 到 LLMOps 的範式轉移
- LLM 的生命周期
- 生命週期工具
- 生命周期指標化與評估

## 了解從 MLOps 到 LLMOps 的範式轉移

LLM 是人工智能武器庫中的新工具，它們在分析和生成任務中非常強大，適用於各種應用，但這種力量對我們如何精簡 AI 和傳統機器學習任務帶來了一些影響。

因此，我們需要一個新的範式去以動態方式適應這項工具，並提供正確的激勵。我們可以將舊的 AI 應用分類為「機器學習應用」（ML Apps），而新的 AI 應用則稱為「生成式 AI 應用」或簡稱「AI 應用」，反映當時使用的主流技術和方法。這樣的轉變在多個方面改變了我們的敘事，請參考以下比較。

![LLMOps 與 MLOps 比較](../../../translated_images/zh-MO/01-llmops-shift.29bc933cb3bb0080.webp)

請注意，在 LLMOps 中，我們更關注應用程式開發者，將整合作為關鍵點，使用「模型即服務」並思考以下指標面向。

- 品質：回應品質
- 危害：負責任的 AI
- 誠實性：回應的依據（合理嗎？正確嗎？）
- 成本：方案預算
- 延遲：平均回應時間（以 token 計）

## LLM 的生命周期

首先，為了理解生命周期及其變更，請查看以下資訊圖表。

![LLMOps 資訊圖](../../../translated_images/zh-MO/02-llmops.70a942ead05a7645.webp)

如您所見，這與傳統 MLOps 的生命周期不同。LLM 有許多新要求，如提示工程、提升品質的不同技術（微調、RAG、元提示）、責任和負責任 AI 的不同評估，最後還有新的評估指標（品質、危害、誠實性、成本和延遲）。

例如，看看我們如何構思，使用提示工程去嘗試多種 LLM，探索測試其假設是否正確的可能性。

注意這不是線性過程，而是整合的迴圈，反覆迭代並有一個總體循環。

我們如何探究這些步驟？讓我們詳細說明如何建立生命周期。

![LLMOps 工作流程](../../../translated_images/zh-MO/03-llm-stage-flows.3a1e1c401235a6cf.webp)

看起來可能有點複雜，讓我們先專注於三個主要步驟。

1. 構思/探索：探索，根據業務需求進行探索。製作原型，創建 [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst)，並測試其對我們的假設是否夠有效。
1. 建構/擴充：實作，接著開始評估較大的資料集，實施像是微調和 RAG 的技術，檢查方案的穩健性。如果不行，重新實作、增加流程步驟或重組資料可能會有所幫助。在測試流程及規模後，如果表現良好並符合指標，即可進入下一階段。
1. 運營化：整合，加入監控和警示系統，部署並將系統整合到應用程式。

之後，是聚焦於安全、合規和治理的管理總體循環。

恭喜，現在您的 AI 應用程式已準備好投入運營。如想親自操作，請參考[Contoso 聊天示範。](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)

接著，我們可以使用哪些工具呢？

## 生命週期工具

就工具而言，微軟提供 [Azure AI 平台](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) 和 [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst)，讓您的生命周期實施更簡易且快速。

[Azure AI 平台](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) 允許您使用 [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)。Microsoft Foundry（原 Azure AI Studio）是一個網頁入口網站，可讓您探索模型、範例及工具，管理資源，使用 UI 開發流程，以及 SDK/CLI 選項進行程式編碼優先的開發。

![Azure AI 的可能性](../../../translated_images/zh-MO/04-azure-ai-platform.80203baf03a12fa8.webp)

Azure AI 讓您能使用多種資源來管理作業、服務、專案、向量搜尋與資料庫需求。

![使用 Azure AI 的 LLMOps](../../../translated_images/zh-MO/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

從概念驗證（POC）到大規模應用，使用 PromptFlow 來建構：

- 從 VS Code 設計與建構應用，使用視覺化及功能性工具
- 輕鬆測試與微調您的應用，提升 AI 品質
- 使用 Microsoft Foundry 進行與雲端的整合及迭代，快速推送與部署

![利用 PromptFlow 的 LLMOps](../../../translated_images/zh-MO/06-llm-promptflow.a183eba07a3a7fdf.webp)

## 太好了！繼續學習！

棒極了，現在請深入了解如何透過 [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst) 結構化應用程式，並檢視雲端推廣如何範例示範這些概念。更多內容，請參考我們的 [Ignite 分場！
](https://www.youtube.com/watch?v=DdOylyrTOWg)

現在，請查看第 15 課，了解 [檢索增強生成與向量資料庫](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) 如何影響生成式 AI 並打造更吸引人的應用程式！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->