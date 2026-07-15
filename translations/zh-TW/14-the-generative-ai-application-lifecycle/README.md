[![與函數調用整合](../../../translated_images/zh-TW/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# 生成式 AI 應用程式生命週期

對於所有 AI 應用程式來說，一個重要的問題是 AI 功能的相關性，因為 AI 是一個快速演進的領域。為了確保您的應用程式持續有效、可靠且穩健，您需要持續監控、評估並改進它。這就是生成式 AI 生命週期的用武之地。

生成式 AI 生命週期是一個指導您開發、部署及維護生成式 AI 應用程式各階段的框架。它幫助您定義目標、衡量效能、識別挑戰並實施解決方案。它也有助於您的應用程式符合領域及利害關係人的倫理和法律標準。透過遵循生成式 AI 生命週期，您可以確保應用程式持續提供價值並滿足使用者需求。

## 介紹

在本章中，您將會：

- 理解從 MLOps 到 LLMOps 的範式轉移
- LLM 生命週期
- 生命週期工具
- 生命週期度量化與評估

## 理解從 MLOps 到 LLMOps 的範式轉移

LLM 是人工智慧武庫中的新工具，它們在分析和生成任務中非常強大，但這種強大能力對我們如何優化 AI 與傳統機器學習任務有些影響。

因此，我們需要一個新的範式來動態適應這個工具，並具備正確的激勵。我們可以將較舊的 AI 應用程式歸類為「機器學習應用程式 (ML Apps)」，而較新的 AI 應用程式則稱為「生成式 AI 應用程式 (GenAI Apps)」或簡稱「AI 應用程式」，以反映當時主流的技術和方法。這在多方面改變了我們的敘述，請參考下列對比。

![LLMOps vs. MLOps 比較](../../../translated_images/zh-TW/01-llmops-shift.29bc933cb3bb0080.webp)

請注意，LLMOps 更重視應用程式開發者，將整合作為核心，採用「模型即服務 (Models-as-a-Service)」，並在度量標準上關注以下幾點。

- 品質：回應品質
- 風險：負責任的 AI
- 誠實度：回應的依據（合理嗎？正確嗎？）
- 成本：解決方案預算
- 延遲：平均每個 token 回應時間

## LLM 生命週期

首先，為了理解生命週期及其改變，我們來看看下面的資訊圖表。

![LLMOps 資訊圖](../../../translated_images/zh-TW/02-llmops.70a942ead05a7645.webp)

如您所見，這與傳統的 MLOps 生命週期不同。LLM 有許多新需求，比如提示工程 (Prompting)、提升品質的各種技術（微調、RAG、元提示）、負責任 AI 下的不同評估與責任，以及新的評估指標（品質、風險、誠實度、成本及延遲）。

例如，看看我們如何進行構思。我們利用提示工程對各種 LLM 進行實驗，探索假設是否可能成立。

請注意這不是線性的，而是整合的迴圈，迭代且伴隨有一個完整的循環。

我們如何探索這些步驟？讓我們詳細探討如何建立一個生命週期。

![LLMOps 工作流程](../../../translated_images/zh-TW/03-llm-stage-flows.3a1e1c401235a6cf.webp)

這可能看起來有點複雜，我們先專注於三個主要步驟。

1. 構思/探索：探索階段，這裡根據業務需要進行探索。進行原型設計，建立一個 [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) 並測試它是否適用於我們的假設。
1. 建置/強化：實作階段，現在開始評估較大資料集，實施如微調和 RAG 等技術，檢測解決方案的穩健性。如果效果不佳，可以重新實作、在流程中新增步驟或重組資料。測試流程和規模後，如果成果符合並達到指標，即可進入下一階段。
1. 營運：整合階段，現在將監控與警報系統加入系統，部署並整合到應用程式中。

接著是管理的整體循環，聚焦於安全性、合規性與治理。

恭喜，現在您的 AI 應用程式已準備好上線並運作。若想實際體驗，請參考 [Contoso 聊天示範](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)。

現在，我們可以使用哪些工具呢？

## 生命週期工具

在工具方面，微軟提供了 [Azure AI 平台](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) 和 [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst)，助您輕鬆實現並運行生命週期。

[Azure AI 平台](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) 讓您可以使用 [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)。Microsoft Foundry（前身為 Azure AI Studio）是一個網頁入口，讓您探索模型、範例及工具，管理資源，並提供 UI 開發流程以及以程式碼優先的 SDK/CLI 選項。

![Azure AI 選項](../../../translated_images/zh-TW/04-azure-ai-platform.80203baf03a12fa8.webp)

Azure AI 讓您使用多項資源，管理作業、服務、專案、向量搜尋及資料庫需求。

![搭配 Azure AI 的 LLMOps](../../../translated_images/zh-TW/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

利用 PromptFlow 從概念驗證 (POC) 到大規模應用程式的構建：

- 從 VS Code 設計並建置應用程式，透過視覺與功能性工具
- 輕鬆測試並微調您的應用程式，以確保 AI 品質
- 利用 Microsoft Foundry 實現與雲端的整合及迭代，快速推送與部署

![搭配 PromptFlow 的 LLMOps](../../../translated_images/zh-TW/06-llm-promptflow.a183eba07a3a7fdf.webp)

## 太棒了！繼續您的學習吧！

很棒，現在進一步了解如何構建應用程式並應用概念，請參考 [Contoso 聊天應用程式](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)，看看 Cloud Advocacy 如何在示範中加入這些概念。更多內容請觀看我們的 [Ignite 專題會議！]
(https://www.youtube.com/watch?v=DdOylyrTOWg)

接著，請查看第 15 課，了解 [檢索增強生成與向量資料庫](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) 如何影響生成式 AI，並製作更具互動性的應用程式！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->