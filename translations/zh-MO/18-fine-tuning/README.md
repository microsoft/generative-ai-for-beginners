[![開源模型](../../../translated_images/zh-MO/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# 微調你的大型語言模型

利用大型語言模型來構建生成式 AI 應用帶來了新的挑戰。一個關鍵問題是確保模型根據用戶請求生成內容的回應質量（準確性和相關性）。在之前的課程中，我們討論了如提示工程和檢索增強生成等技術，試圖通過_修改現有模型的提示輸入_來解決此問題。

在今天的課程中，我們將討論第三種技術，<strong>微調</strong>，該技術嘗試通過_用額外數據重新訓練模型本身_來解決這一挑戰。讓我們深入了解細節。

## 學習目標

本課程介紹了對預訓練語言模型進行微調的概念，探討了此方法的優點和挑戰，並提供了什麼時候以及如何使用微調以提升生成式 AI 模型表現的指導。

完成本課程後，你應該能回答以下問題：

- 什麼是語言模型的微調？
- 何時以及為什麼微調是有用的？
- 我如何對預訓練模型進行微調？
- 微調有哪些限制？

準備好了嗎？讓我們開始吧。

## 圖解指南

想先了解我們將涵蓋的整體內容嗎？請查看這份圖解指南，描述了本課程的學習旅程——從學習微調的核心概念和動機，到理解執行微調任務的流程和最佳實踐。這是一個迷人的探索主題，別忘了查看[資源](./RESOURCES.md?WT.mc_id=academic-105485-koreyst)頁面以獲取支援自學旅程的更多連結！

![微調語言模型的圖解指南](../../../translated_images/zh-MO/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## 什麼是語言模型的微調？

從定義來看，大型語言模型是基於來自互聯網等多元來源的大量文本進行_預訓練_。正如我們在之前課程中學到的，我們需要諸如_提示工程_和_檢索增強生成_等技巧來提升模型對用戶問題（“提示”）的回答質量。

一種流行的提示工程技巧是通過提供_明確指示_（明確引導）或_給出幾個示例_（隱式引導）來給模型更多關於回應期望的指導。這被稱為_少量示例學習_，但它有二個限制：

- 模型的標記限制可能會限制你能提供的示例數量，並影響效果。
- 模型標記使用成本可能使得每個提示添加示例代價高昂，限制靈活性。

微調是在機器學習系統中常用的做法，我們拿一個預訓練模型用新的數據重新訓練，以提升其在特定任務上的表現。在語言模型的上下文中，我們可以用一組為特定任務或應用領域精心挑選的示例對預訓練模型進行微調，創建一個<strong>定制模型</strong>，使其在該任務或領域上更加準確和相關。微調的一個附加好處是，還能減少少量示例學習所需的示例數量——降低標記使用量及相關成本。

## 何時及為什麼應該微調模型？

在_這裡_談論微調時，我們指的是<strong>監督式</strong>微調，通過<strong>添加原始訓練數據集之外的新數據</strong>重新訓練。這不同於無監督微調方法，無監督微調是在原數據上用不同超參數重新訓練。

需要記住的要點是，微調是一種進階技巧，需要一定專業知識才能達到預期效果。如果操作不當，可能無法帶來期望的改進，甚至會降低模型在你目標領域的表現。

因此，在學習「如何」微調語言模型之前，你需要清楚「為什麼」要走這條路，以及「何時」開始微調流程。先問自己這些問題：

- <strong>用例</strong>：你的_用例_是什麼？你想提升當前預訓練模型的哪一方面？
- <strong>替代方案</strong>：你嘗試過_其他技術_來達到預期結果嗎？用它們建立基準以供比較。
  - 提示工程：嘗試像少量示例提示這類技術，並用相關提示回應示例評估質量。
  - 檢索增強生成：嘗試用檢索到的查詢結果增強提示，評估回答質量。
- <strong>成本</strong>：你是否清楚微調的成本？
  - 可調節性 - 預訓練模型是否支持微調？
  - 努力程度 - 準備訓練數據、評估和完善模型的工作量。
  - 計算資源 - 執行微調任務及部署微調模型所需的計算。
  - 數據 - 是否有足夠且質量好的示例可用於微調。
- <strong>效益</strong>：你是否確認微調的效益？
  - 質量 - 微調後的模型是否優於基線模型？
  - 成本 - 是否通過簡化提示減少了標記使用？
  - 可擴展性 - 是否能將基礎模型用於新領域？

透過回答這些問題，你應該能決定微調是否適合你的用例。理想狀況下，只有在效益大於成本時此方法才成立。確定採用後，該考慮_如何_微調預訓練模型了。

想了解更多決策過程的洞見？觀看[微調還是不微調](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## 我們如何微調預訓練模型？

微調預訓練模型，你需要有：

- 一個可微調的預訓練模型
- 用於微調的數據集
- 運行微調任務的訓練環境
- 部署微調後模型的託管環境

## 在 Microsoft Foundry 上微調

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) 是你今天在 Azure 上微調、部署及管理自訂模型的地方（整合了原 Azure OpenAI Studio 和 Azure AI Studio）。開始任務前，了解 Foundry 提供的選項及平台推薦的最佳實踐十分有幫助。內部實現中，Foundry 採用<strong>LoRA（低秩適應）</strong>來高效微調模型，使訓練比重新訓練所有權重更快且成本更低。

### 步驟1：選擇訓練技術

Foundry 支援三種微調技術。**從 SFT 開始**——它涵蓋最廣泛的場景。

| 技術 | 功能 | 適用時機 |
| --- | --- | --- |
| **監督式微調 (SFT)** | 根據輸入/輸出示例對進行訓練，讓模型學會生成你期望的回答。 | 大多數任務的默認選擇：領域專精、任務性能、風格與語氣、跟隨指令及語言適應。 |
| **直接偏好優化 (DPO)** | 從_偏好與非偏好_回答對中學習，使輸出符合人類偏好。 | 當你有比較性反饋時，用於提升回答質量、安全性與對齊度。 |
| **強化微調 (RFT)** | 利用_評分者_的回饋信號，通過強化學習優化複雜行為。 | 用於目標明確、推理密集的領域（數學、化學、物理），需要更高的機器學習專業知識。 |

### 步驟2：選擇訓練級別

Foundry 讓你選擇訓練運行的方式和地點：

- <strong>標準</strong> - 在你的資源區域內訓練，保證數據駐留。數據必須留在特定區域時使用。
- <strong>全球</strong> - 利用區域外的容量，成本更低且排隊更快（數據與權重會複製到訓練區域）。當數據駐留不是需求時，這是良好預設。
- <strong>開發者</strong> - 最低成本，利用閒置容量，無延遲/SLA 保證（作業可以被搶占和恢復）。適合實驗。

### 步驟3：選擇基礎模型

支援微調的模型包括 OpenAI 的 `gpt-4o-mini`、`gpt-4o`、`gpt-4.1`、`gpt-4.1-mini` 與 `gpt-4.1-nano`（SFT；4o/4.1 系列也支援 DPO）、推理模型 `o4-mini` 和 `gpt-5`（RFT），以及開源模型如 `Ministral-3B`、`Qwen-32B`、`Llama-3.3-70B-Instruct` 和 `gpt-oss-20b`（在 Foundry 資源上進行 SFT）。始終檢查當前的[微調模型清單](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models)以了解支援方法、區域與可用性。

> Foundry 提供兩種模式：<strong>無伺服器</strong>（按消耗計費，無需管理 GPU 配額，支援 OpenAI 及特定模型）和<strong>托管計算</strong>（透過 Azure Machine Learning 自行帶 VM，支援最廣泛模型）。大多數人應從無伺服器開始。

### Foundry 最佳實踐

- **先建立基線。** 在微調前，先用提示工程和 RAG 測量基礎模型表現，便於證明成效。
- **小規模起步，再擴展。** 初期用 50-100 個高品質示例驗證方法，再增加至 500+ 用於生產。品質勝於數量——剔除低質示例。
- **格式正確。** 訓練與驗證文件必須是帶 BOM 的 JSONL，UTF-8 編碼，大小小於 512 MB，使用聊天補全訊息格式。務必包含驗證文件以監控過擬合。
- **在推斷時保留訓練系統提示。** 調用模型時使用與訓練時相同的系統訊息。
- **評估檢查點—不要盲目部署最後一個。** Foundry 保留最後三個訓練週期作為可部署檢查點；透過觀察 `train_loss` / `valid_loss` 和標記準確率選擇最具泛化能力的。
- **比較微調模型與基線時，同時衡量標記成本和質量。**
- **持續迭代的微調。** 可在已微調模型上對新數據進行再次微調（OpenAI 模型支持）。
- **注意託管成本。** 部署的自訂模型按時計費，非活動部署 15 天後會被移除——清理不需要的項目。

參閱[利用微調自訂模型](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst)的端到端實務教程，當準備使用其他技術時，亦可參考[DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst)和[RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst)指南。

## 微調實戰

以下資源提供逐步指導，帶你通過使用已支援模型和經過精心挑選數據集的真實範例。要實作這些，你需要註冊特定服務供應商帳戶，並取得相關模型和數據集的存取權限。

| 服務供應商 | 教學                                                                                                                                                                       | 說明                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OpenAI       | [如何微調聊天模型](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | 學習如何為特定領域（「食譜助手」）微調最新的 OpenAI 聊天模型，包括準備訓練資料、執行微調任務及使用微調後模型進行推論。                                                                                                                                                                                                                                                              |
| Microsoft Foundry | [利用微調自訂模型](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | 學習如何在 Microsoft Foundry 的 Azure 平台上微調目前受支持的模型（如 `gpt-4.1-mini`）：準備及上傳訓練和驗證數據，執行微調任務，然後部署並使用新模型。                                                                                                                                                                                                                   |

| Hugging Face | [用 Hugging Face 微調大型語言模型（LLMs）](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | 本篇博客文章將帶你使用 [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) 函式庫與 [Transformer 強化學習 (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) ，在 Hugging Face 上利用開放[資料集](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst)微調 _開放大型語言模型_ （例如：`CodeLlama 7B`）。 |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [用 AutoTrain 微調大型語言模型](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain（或 AutoTrain Advanced）是 Hugging Face 開發的 Python 函式庫，支援多種任務的微調，包括大型語言模型的微調。AutoTrain 是一個免寫程式碼的解決方案，微調可以在你自己的雲端、Hugging Face Spaces 或本地執行。它同時支援基於網頁的 GUI、命令列介面及使用 yaml 配置檔進行訓練。                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [用 Unsloth 微調大型語言模型](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth 是一個開源框架，支援大型語言模型微調與強化學習（RL）。Unsloth 簡化本地訓練、評估及部署流程，並附有現成使用的[筆記本](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst)。它同時支援文字轉語音（TTS）、BERT 及多模態模型。想開始使用，請參考其逐步指引的[微調大型語言模型指南](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide)。                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## 作業

選擇上面其中一個教學並跟著操作。_我們可能會將這些教學版本複製到本倉庫的 Jupyter 筆記本中僅作參考用途。請直接使用原始資源來獲取最新版本_。

## 幹得好！繼續學習吧。

完成本課程後，請瀏覽我們的 [生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升你的生成式 AI 知識！

恭喜你！！你已完成此課程 v2 系列的最終課程！別停止學習與構建。**請查看 [資源](RESOURCES.md?WT.mc_id=academic-105485-koreyst) 頁面，以獲得更多本主題的額外建議清單。

我們的 v1 系列課程也已更新，增加了更多作業與概念。花點時間複習你的知識吧—也請[分享你的問題與反饋](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)，幫助我們為社群改進這些課程。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->