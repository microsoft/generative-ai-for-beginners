<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df44972d5575ea8cef3c52ee31696d04",
  "translation_date": "2025-12-19T13:24:16+00:00",
  "source_file": "14-the-generative-ai-application-lifecycle/README.md",
  "language_code": "mo"
}
-->
[![Integrating with function calling](../../../translated_images/14-lesson-banner.066d74a31727ac121eeac06376a068a397d8e335281e63ce94130d11f516e46b.mo.png)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# 生成式 AI 應用程式生命週期

對所有 AI 應用程式來說，一個重要的問題是 AI 功能的相關性，因為 AI 是一個快速演變的領域，為了確保您的應用程式保持相關性、可靠性和穩健性，您需要持續監控、評估和改進它。這就是生成式 AI 生命週期的用武之地。

生成式 AI 生命週期是一個指導您開發、部署和維護生成式 AI 應用程式各階段的框架。它幫助您定義目標、衡量績效、識別挑戰並實施解決方案。它還幫助您使應用程式符合您領域和利益相關者的倫理及法律標準。透過遵循生成式 AI 生命週期，您可以確保您的應用程式始終提供價值並滿足使用者需求。

## 介紹

在本章中，您將會：

- 了解從 MLOps 到 LLMOps 的範式轉移
- LLM 生命週期
- 生命週期工具
- 生命週期指標化與評估

## 了解從 MLOps 到 LLMOps 的範式轉移

LLM 是人工智能武器庫中的新工具，它們在應用程式的分析和生成任務中非常強大，但這種力量對我們如何簡化 AI 和傳統機器學習任務帶來了一些影響。

因此，我們需要一個新的範式，以動態且具正確激勵的方式適應這個工具。我們可以將較舊的 AI 應用程式歸類為「ML 應用程式」，而較新的 AI 應用程式則稱為「生成式 AI 應用程式」或簡稱「AI 應用程式」，反映當時主流的技術和方法。這在多方面改變了我們的敘事，請看以下比較。

![LLMOps vs. MLOps comparison](../../../translated_images/01-llmops-shift.29bc933cb3bb0080a562e1655c0c719b71a72c3be6252d5c564b7f598987e602.mo.png)

請注意，在 LLMOps 中，我們更關注應用程式開發者，將整合作為關鍵點，使用「模型即服務」並考慮以下指標：

- 品質：回應品質
- 風險：負責任的 AI
- 誠實：回應的依據性（合理嗎？正確嗎？）
- 成本：解決方案預算
- 延遲：平均回應時間（每個 token）

## LLM 生命週期

首先，為了理解生命週期及其變化，請參考下方資訊圖表。

![LLMOps infographic](../../../translated_images/02-llmops.70a942ead05a7645db740f68727d90160cb438ab71f0fb20548bc7fe5cad83ff.mo.png)

如您所見，這與傳統 MLOps 的生命週期不同。LLM 有許多新需求，如提示工程、提升品質的不同技術（微調、RAG、元提示）、負責任 AI 的不同評估與責任，以及新的評估指標（品質、風險、誠實、成本和延遲）。

例如，看看我們如何構思。使用提示工程來嘗試各種 LLM，探索可能性，測試它們的假設是否正確。

請注意，這不是線性的，而是整合的迴圈，反覆且有一個總體循環。

我們如何探索這些步驟？讓我們詳細了解如何建立生命週期。

![LLMOps Workflow](../../../translated_images/03-llm-stage-flows.3a1e1c401235a6cfa886ed6ba04aa52a096a545e1bc44fa54d7d5983a7201892.mo.png)

這看起來可能有點複雜，先聚焦於三個主要步驟。

1. 構思/探索：探索階段，根據業務需求進行探索。原型設計，建立 [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) 並測試是否對假設足夠有效。
1. 建置/增強：實作階段，開始評估較大資料集，實施技術如微調和 RAG，檢查解決方案的穩健性。如果不行，重新實作、在流程中加入新步驟或重組資料可能有幫助。測試流程和規模後，若運作良好並檢查指標，則準備進入下一步。
1. 運營化：整合階段，加入監控和警示系統，部署並整合到應用程式中。

接著，我們有一個總體的管理循環，專注於安全、合規和治理。

恭喜，現在您的 AI 應用程式已準備好運作。想要實作體驗，請參考 [Contoso Chat Demo.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

那麼，我們可以使用哪些工具呢？

## 生命週期工具

在工具方面，Microsoft 提供了 [Azure AI 平台](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) 和 [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst)，讓您的生命週期實作變得簡單且隨時可用。

[Azure AI 平台](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) 允許您使用 [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys)。AI Studio 是一個網頁入口，讓您探索模型、範例和工具。管理資源、UI 開發流程以及 SDK/CLI 選項，支援以程式碼為先的開發。

![Azure AI possibilities](../../../translated_images/04-azure-ai-platform.80203baf03a12fa8b166e194928f057074843d1955177baf0f5b53d50d7b6153.mo.png)

Azure AI 允許您使用多種資源，管理您的運營、服務、專案、向量搜尋和資料庫需求。

![LLMOps with Azure AI](../../../translated_images/05-llm-azure-ai-prompt.a5ce85cdbb494bdf95420668e3464aae70d8b22275a744254e941dd5e73ae0d2.mo.png)

從概念驗證（POC）到大規模應用，使用 PromptFlow：

- 從 VS Code 設計和建置應用程式，具備視覺化和功能性工具
- 輕鬆測試和微調您的應用程式，確保 AI 品質
- 使用 Azure AI Studio 進行整合和迭代，快速推送和部署

![LLMOps with PromptFlow](../../../translated_images/06-llm-promptflow.a183eba07a3a7fdf4aa74db92a318b8cbbf4a608671f6b166216358d3203d8d4.mo.png)

## 太好了！繼續您的學習！

太棒了，現在進一步了解如何結構化應用程式，使用這些概念於 [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)，看看雲端推廣團隊如何在示範中加入這些概念。更多內容，請參考我們的 [Ignite 分會議！](https://www.youtube.com/watch?v=DdOylyrTOWg)

接著，請查看第 15 課，了解 [檢索增強生成與向量資料庫](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) 如何影響生成式 AI，並打造更具吸引力的應用程式！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件係使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我哋致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我哋對因使用本翻譯而引起之任何誤解或誤釋概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->