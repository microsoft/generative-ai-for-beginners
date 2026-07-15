[![整合功能呼叫](../../../translated_images/zh-HK/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# 生成式 AI 應用程式生命週期

對所有 AI 應用程式來說，一個重要的問題是 AI 功能的相關性，因為 AI 是一個快速發展的領域，要確保您的應用程式保持相關、可靠且穩健，您需要持續監控、評估並改進它。這就是生成式 AI 生命週期的用武之地。

生成式 AI 生命週期是一個指導您開發、部署和維護生成式 AI 應用程式各個階段的框架。它幫助您定義目標、衡量績效、識別挑戰並實現解決方案。它還幫助您將應用程式與您領域和利益相關者的倫理及法律標準對齊。遵循生成式 AI 生命週期，您可以確保應用程式持續提供價值並令使用者滿意。

## 介紹

在本章中，您將會：

- 了解從 MLOps 到 LLMOps 的範式轉移
- LLM 生命週期
- 生命週期工具
- 生命週期計量與評估

## 了解從 MLOps 到 LLMOps 的範式轉移

LLM 是人工智能武庫中的新工具，在分析和生成任務上對應用非常強大，但這種力量對我們如何簡化 AI 和傳統機器學習任務有些影響。

因此，我們需要新的範式以動態且用正確激勵來調整這個工具。我們可以將舊的 AI 應用分類為「機器學習應用」，而新的 AI 應用則稱為「生成式 AI 應用」或簡稱「AI 應用」，反映當時主流的技術和方法。這會在多方面轉變我們的敘述，請參考以下比較。

![LLMOps 與 MLOps 比較](../../../translated_images/zh-HK/01-llmops-shift.29bc933cb3bb0080.webp)

請注意，在 LLMOps 中，我們更關注應用開發者，將整合作為關鍵點，使用「模型即服務」，並考慮以下計量指標。

- 品質：回應品質
- 風險：負責任的 AI
- 誠實：回應的基礎（合理嗎？正確嗎？）
- 成本：解決方案預算
- 延遲：回應每個標記的平均時間

## LLM 生命週期

首先，為了理解生命週期及其變化，下圖是個參考資訊圖表。

![LLMOps 資訊圖](../../../translated_images/zh-HK/02-llmops.70a942ead05a7645.webp)

如您所見，這與傳統 MLOps 生命週期不同。LLM 有許多新需求，像是提示工程、使用不同技術提升品質（微調、RAG、元提示）、負責任 AI 的不同評估責任，以及新的評估指標（品質、風險、誠實、成本與延遲）。

例如，看看我們如何構思。透過提示工程與不同 LLM 展開實驗，探索不同可能性，測試假設是否正確。

注意這不是線性的，而是整合迴圈，有迭代及總體循環。

我們如何探索這些步驟？讓我們詳細介紹如何建立生命週期。

![LLMOps 工作流程](../../../translated_images/zh-HK/03-llm-stage-flows.3a1e1c401235a6cf.webp)

這看起來可能有點複雜，我們先聚焦在三個大步驟。

1. 構思/探索：探索階段，根據商業需求進行探索。製作原型，創建一個 [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) 測試是否對假設足夠有效。
1. 建置/增強：實作階段，開始針對較大數據集評估並實施技術，如微調和 RAG，檢查解決方案的穩健性。如果不足，可重新實作、加入流程新步驟或重組資料。測試流程與規模後，若符合指標，即可準備下一步。
1. 產業化：整合階段，為系統加入監控與警示系統，部署及應用程序集成。

此外，有管理的總體循環，著重於安全、合規與治理。

恭喜，您的 AI 應用已準備好且已上線。若想親身體驗，請查看 [Contoso Chat Demo](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)。

現在，我們可以使用什麼工具？

## 生命週期工具

在工具方面，微軟提供 [Azure AI 平台](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) 和 [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst)，便利且簡化您的生命週期實作。

[Azure AI 平台](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) 讓您可以使用 [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)。Microsoft Foundry（前稱 Azure AI Studio）是一個網頁入口，讓您探索模型、範例和工具，管理資源，並提供 UI 開發流程及 SDK/CLI 代碼優先的開發選項。

![Azure AI 可能性](../../../translated_images/zh-HK/04-azure-ai-platform.80203baf03a12fa8.webp)

Azure AI 讓您使用多種資源來管理操作、服務、專案、向量搜尋和資料庫需求。

![使用 Azure AI 的 LLMOps](../../../translated_images/zh-HK/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

從概念驗證 (POC) 到大規模應用，使用 PromptFlow 建構：

- 從 VS Code 設計並構建應用，利用視覺和功能工具
- 輕鬆測試並微調應用，以確保 AI 品質。
- 使用 Microsoft Foundry 進行整合與迭代，雲端推送與部署實現快速整合。

![使用 PromptFlow 的 LLMOps](../../../translated_images/zh-HK/06-llm-promptflow.a183eba07a3a7fdf.webp)

## 太好了！請繼續學習！

太棒了，現在進一步了解如何構建應用程式，以便將概念應用於 [Contoso Chat App](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)，看看雲端宣導團隊如何將這些概念加入示範中。更多內容，請參閱我們的 [Ignite 專題講座！
](https://www.youtube.com/watch?v=DdOylyrTOWg)

接著查看第 15 課，了解 [檢索增強生成與向量資料庫](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) 如何影響生成式 AI 並打造更吸引人的應用程式！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->