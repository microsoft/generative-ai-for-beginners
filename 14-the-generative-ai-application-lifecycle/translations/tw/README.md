[![與函式呼叫整合](../../images/14-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson14-gh?WT.mc_id=academic-105485-koreyst)

# 生成式 AI 應用程式生命週期

一個所有 AI 應用程式的重要問題是 AI 功能的相關性，因為 AI 是一個快速發展的領域，為了確保你的應用程式保持相關性、可靠性和穩健性，你需要持續監控、評估和改進它。這就是生成式 AI 生命週期的作用所在。

生成式 AI 生命週期是一個框架，指導你完成開發、部署和維護生成式 AI 應用程式的各個階段。它幫助你定義目標、衡量績效、識別挑戰並實施解決方案。它還幫助你將應用程式與你的領域和利益相關者的倫理和法律標準對齊。通過遵循生成式 AI 生命週期，你可以確保你的應用程式始終提供價值並滿足用戶需求。

## 簡介

在本章中，你將：

- 了解從 MLOps 到 LLMOps 的範式轉變
- LLM 生命週期
- 生命週期工具
- 生命週期度量和評估

## 了解從 MLOps 到 LLMOps 的範式轉變

LLMs 是人工智慧武器庫中的一個新工具，它們在應用程式的分析和生成任務中非常強大，然而這種力量在我們簡化 AI 和經典機器學習任務的方式上有一些後果。

隨著這一點，我們需要一個新的範式來動態地適應這個工具，並提供正確的激勵。我們可以將舊的 AI 應用程式分類為「ML 應用程式」，而將新的 AI 應用程式分類為「GenAI 應用程式」或簡稱「AI 應用程式」，以反映當時使用的主流技術和方法。這在多方面改變了我們的敘述，請看以下比較。

![LLMOps vs. MLOps 比較](../../images/01-llmops-shift.png?WT.mc_id=academic-105485-koreys)

注意，在 LLMOps 中，我們更專注於應用程式開發人員，使用整合作為關鍵點，使用「模型即服務」，並考慮以下指標。

- 品質: 回應品質
- 傷害: 負責任的 AI
- 誠實: 回應的合理性（有道理嗎？正確嗎？）
- 成本: 解決方案預算
- 延遲: 每個 token 回應的平均時間

## LLM 生命週期

首先，為了了解生命週期和修改，讓我們注意下一個資訊圖表。

![LLMOps 資訊圖](../../images/02-llmops.png?WT.mc_id=academic-105485-koreys)

如你所見，這與通常的 MLOps 生命週期不同。LLM 有許多新的需求，如提示、不同的技術來提高品質（微調、RAG、Meta-Prompts）、負責任 AI 的不同評估和責任，最後是新的評估指標（品質、危害、誠實、成本和延遲）。

例如，看看我們如何構思。使用提示工程來實驗各種大型語言模型，以探索可能性來測試他們的假設是否正確。

請注意，這不是線性的，而是整合的迴圈、反覆進行並具有一個總體循環。

我們如何探索這些步驟？讓我們詳細了解如何建構一個生命週期。

![LLMOps 工作流程](../../images/03-llm-stage-flows.png?WT.mc_id=academic-105485-koreys)

這可能看起來有點複雜，讓我們先專注於三個大步驟。

1. 構思/探索: 探索, 在這裡我們可以根據業務需求進行探索。原型設計, 建立一個 [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) 並測試其是否對我們的假設足夠有效。
1. 建構/增強: 實施, 現在, 我們開始評估更大的數據集實施技術, 如微調和RAG, 以檢查我們解決方案的穩健性。如果不夠, 重新實施它, 在流程中添加新步驟或重構數據, 可能會有所幫助。在測試我們的流程和規模後, 如果有效並檢查我們的指標, 它就準備好進入下一步。
1. 操作化: 整合, 現在添加監控和警報系統到我們的系統, 部署和應用整合到我們的應用程式。

然後，我們有管理的總體循環，專注於安全性、合規性和治理。

恭喜你，現在你的 AI 應用程式已準備好並可以運行。要獲得實際操作經驗，請查看[Contoso Chat 展示](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)。

現在，我們可以使用哪些工具？

## 生命週期工具

為了工具，Microsoft 提供了[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys)和[PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst)，以促進並使您的循環易於實施並隨時可用。

[Azure AI Platform](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) 讓你可以使用 [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys)。AI Studio 是一個網頁入口，讓你可以探索模型、範例和工具。管理你的資源、UI 開發流程和 SDK/CLI 選項以進行程式碼優先的開發。

![Azure AI possibilities](../../images/04-azure-ai-platform.png?WT.mc_id=academic-105485-koreys)

Azure AI，允許您使用多個資源，來管理您的操作、服務、專案、向量搜尋和資料庫需求。

![LLMOps 與 Azure AI](../../images/05-llm-azure-ai-prompt.png?WT.mc_id=academic-105485-koreys)

從概念驗證（POC）到大規模應用的構建，使用 PromptFlow:

- 從 VS Code 設計和建構應用程式，使用視覺和功能工具
- 測試和微調您的應用程式，以輕鬆達到高品質 AI。
- 使用 Azure AI Studio 與雲端整合和迭代，快速推送和部署以進行整合。

![LLMOps 與 PromptFlow](../../images/06-llm-promptflow.png?WT.mc_id=academic-105485-koreys)

## 太棒了！繼續學習！

Amazing, 現在了解更多我們如何結構一個應用程式來使用這些概念，請參考 [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)，以檢查 Cloud Advocacy 如何在展示中添加這些概念。欲了解更多內容，請查看我們的 [Ignite breakout session](https://www.youtube.com/watch?v=DdOylyrTOWg)！

現在，查看第15課，了解[檢索增強生成和向量資料庫](../../../15-rag-and-vector-databases/translations/tw/README.md?WT.mc_id=academic-105485-koreyst)如何影響生成式AI並製作更具吸引力的應用程式！

