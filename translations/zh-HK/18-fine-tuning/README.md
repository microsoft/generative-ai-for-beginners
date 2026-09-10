[![開源模型](../../../translated_images/zh-HK/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# 微調您的大型語言模型

使用大型語言模型來構建生成式 AI 應用帶來全新的挑戰。其中一個關鍵問題是確保模型針對特定使用者請求生成的內容具有良好的回應質量（準確性和相關性）。在之前的課程中，我們討論了提示工程和檢索增強生成等技術，這些方法試圖通過_修改輸入提示_來解決問題。

在今天的課程中，我們將討論第三種技術，<strong>微調</strong>，它試圖通過_使用額外數據重新訓練模型本身_來解決這一挑戰。讓我們深入了解細節。

## 學習目標

本課程介紹預訓練語言模型的微調概念，探討這種方法的優勢與挑戰，並提供何時及如何利用微調來提升生成式 AI 模型性能的指導。

課程結束時，您應能回答以下問題：

- 什麼是語言模型的微調？
- 微調在什麼時候以及為什麼有用？
- 如何微調預訓練模型？
- 微調有哪些限制？

準備好了嗎？讓我們開始吧。

## 圖解指南

想先了解我們將涵蓋的主要內容再深入學習嗎？請查看這份圖解指南，說明本課程的學習旅程——從學習微調的核心概念與動機，到理解微調過程和執行最佳實踐。這是個引人探索的主題，別忘了查看[資源](./RESOURCES.md?WT.mc_id=academic-105485-koreyst)頁面，獲取更多支持您自主學習的連結！

![語言模型微調圖解指南](../../../translated_images/zh-HK/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## 什麼是語言模型的微調？

按定義，大型語言模型是基於來自包括網際網路在內多元來源的大量文本進行_預訓練_。如我們在之前課程中所學，為提升模型對使用者提問（「提示」）的回應質素，我們需要_提示工程_和_檢索增強生成_等技術。

一種常見的提示工程方法是透過提供_指令_（明確指導）或_幾個示例_（隱含指導）來向模型展示希望得到的回應風格，這稱為_少量學習_。但它有兩個限制：

- 模型的詞元限制會限制您可提供的示例數量，降低成效。
- 模型使用詞元成本高，為每個提示添加示例會花費昂貴且限制靈活性。

微調是機器學習系統中的常用做法——我們拿預訓練模型，並用新數據重新訓練，提升其在特定任務上的表現。對語言模型而言，我們可以用_特定任務或應用領域的精選示例數據_對預訓練模型進行微調，打造出在該任務或領域表現更準確且相關的<strong>定制模型</strong>。微調的額外好處是，它可以減少少量學習所需示例，從而降低詞元使用量與相關成本。

## 何時及為何要微調模型？

在_此_語境下，我們討論的微調是指<strong>監督式</strong>微調，即透過<strong>增加新的數據</strong>（非原始訓練資料）來重新訓練模型。這與非監督式微調不同，後者是在原始數據上、但採用不同超參數重新訓練模型。

需要記住的是，微調是一項進階技巧，需具備一定專業知識才能達到理想效果。若操作不當，可能無法帶來預期改善，甚至降低模型在所針對領域的效能。

因此，在學習「如何」微調語言模型之前，您應該先瞭解「為何」要採用此方式，以及「何時」開始微調流程。可從以下問題開始思考：

- <strong>使用案例</strong>：您微調的_使用案例_是什麼？希望改進目前預訓練模型的哪個方面？
- <strong>替代方案</strong>：您是否嘗試過_其他技術_以達成目標？用它們作為比較基準。
  - 提示工程：嘗試以相關的提示回應示例進行少量提示。評估回應質素。
  - 檢索增強生成：試用以查詢結果增強提示。評估回應質素。
- <strong>成本</strong>：您是否明確評估微調的成本？
  - 可調性——該預訓練模型是否可微調？
  - 工作量——準備訓練數據，評估及優化模型所需的人力。
  - 運算資源——執行微調任務與部署微調模型所需的運算力。
  - 數據——是否有足夠且具質量的示例用於微調，影響效果。
- <strong>收益</strong>：您是否確認微調的收益？
  - 質量——微調模型是否優於基準？
  - 成本——是否能透過簡化提示減少詞元使用？
  - 擴展性——是否能將基礎模型重新用於新領域？

回答這些問題後，您應能判斷微調是否適合您的使用案例。理想情況是當收益高於成本時，此方法才具有效益。決定後，接下來思考_如何_微調該預訓練模型。

想更深入了解決策過程？請觀看[微調還是不微調](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## 如何微調預訓練模型？

微調預訓練模型需具備：

- 可進行微調的預訓練模型
- 用於微調的數據集
- 執行微調任務的訓練環境
- 部署微調模型的主機環境

## 使用 Microsoft Foundry 進行微調

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) 是您今天在 Azure 上微調、部署及管理定制模型的平台（整合了過去的 Azure OpenAI Studio 和 Azure AI Studio）。開始任務前，瞭解 Foundry 提供的選項及平台建議的最佳實踐很有幫助。背後技術使用 **LoRA（低秩適應）** 以高效微調模型，令訓練速度更快、成本更低，不必重新訓練每個權重。

### 步驟一：選擇訓練技術

Foundry 支援三種微調技術。**從監督式微調（SFT）開始**，涵蓋最廣泛場景。

| 技術 | 功能 | 適用時機 |
| --- | --- | --- |
| **監督式微調 (SFT)** | 透過輸入/輸出範例對訓練，讓模型學會產生您期望的回應。 | 預設多數任務：領域專精、任務表現、風格及語氣、指令遵循和語言適應。 |
| **直接偏好優化 (DPO)** | 透過_優劣回應對_學習，使輸出符合人類偏好。 | 當有比較反饋時提升回應質量、安全性及一致性。 |
| **強化微調 (RFT)** | 用_評分者_的獎勵信號，以強化學習優化複雜行為。 | 適用於客觀、重推理領域（數學、化學、物理）有明確對錯答案，需更多機器學習專業知識。 |

### 步驟二：選擇訓練層級

Foundry 讓您選擇訓練地點與方式：

- <strong>標準層級</strong> — 在您資源所在區域訓練，確保資料駐留。必要時使用此選項。
- <strong>全球層級</strong> — 利用區域外容量訓練，成本較低、排程更快（資料及權重會複製到訓練區域）。無資料駐留需求時的良好預設。
- <strong>開發者層級</strong> — 成本最低，使用閒置運算力，無延遲與服務保證（任務可被中斷並續跑）。適合實驗。

### 步驟三：選擇基礎模型

支援微調的模型包括 OpenAI 的 `gpt-4o-mini`、`gpt-4o`、`gpt-4.1`、`gpt-4.1-mini` 與 `gpt-4.1-nano`（SFT；4o/4.1 系列亦支援 DPO），推理模型 `o4-mini` 與 `gpt-5`（RFT），以及開源模型如 `Ministral-3B`、`Qwen-32B`、`Llama-3.3-70B-Instruct` 和 `gpt-oss-20b`（Foundry 資源上的 SFT）。請隨時查閱最新的[微調模型列表](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models)，瞭解支援方法、區域及可用性。

> Foundry 提供兩種模式：<strong>無伺服器模式</strong>（按使用計費，無需管理 GPU 配額，適用 OpenAI 及部分模型）與<strong>管理計算模式</strong>（透過 Azure Machine Learning 自帶 VM，支援更廣泛模型）。大部分人應從無伺服器模式開始。

### Foundry 最佳實踐

- **先建基準。** 在微調之前，先用提示工程和 RAG 評估基礎模型，證明改善效果。
- **從小規模開始，再擴展。** 先用 50-100 個高品質示例驗證方法，生產階段再擴展至 500+。品質勝於數量，剪除低品質示例。
- **正確格式化數據。** 訓練與驗證文件必須是 JSONL、UTF-8 **帶 BOM**、大小小於 512 MB，使用聊天補全訊息格式。務必包含驗證文件以防過度擬合。
- **推理時保留訓練時系統提示。** 調用模型時，使用與訓練時相同的系統訊息。
- **評估檢查點－勿盲目部署最後一個。** Foundry 保留最近三個 epoch 作為可部署檢查點；觀察 `train_loss` / `valid_loss` 及詞元準確度，選擇泛化效果最佳者。
- **比較微調模型與基準時，同時衡量詞元成本與品質。**
- **持續微調迭代。** 可在已微調模型上用新數據繼續微調（OpenAI 模型支援）。
- **注意部署成本。** 已部署的定制模型按小時計費，停用部署超過 15 天會被移除—請清理不需要的資源。

請完成[使用微調定制模型](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst)的完整教學流程，準備好時可參考[DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst)與[RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst)的進階技術指南。

## 微調實戰

以下資源提供逐步教學，演示如何對目前支援的模型及精選數據集進行示範微調。使用它們前，您需擁有相應服務提供者帳號及對應模型與數據集的存取權。

| 提供者         | 教學                                                                                                                                                         | 說明                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [如何微調聊天模型](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)         | 學習如何為特定領域（「食譜助理」）微調近期 OpenAI 聊天模型：準備訓練數據，執行微調任務，並使用微調後模型進行推理。                                                                                                                                                                                                                                                                                                            |
| Microsoft Foundry | [使用微調定制模型](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst)                      | 學習如何在 Microsoft Foundry 的 Azure 平台上微調目前支援的模型（如 `gpt-4.1-mini`）：準備和上傳訓練與驗證數據，運行微調任務，然後部署並使用新模型。                                                                                                                                                                                                                                                                         |

| Hugging Face | [使用 Hugging Face 微調大型語言模型](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | 本博客文章引導您如何使用 [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) 函式庫和 [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) ，搭配 Hugging Face 上的開放[數據集](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) 來微調 _開放大型語言模型_（例如：`CodeLlama 7B`）。 |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [使用 AutoTrain 微調大型語言模型](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain（或稱 AutoTrain Advanced）是 Hugging Face 開發的 Python 函式庫，支援多種任務的微調，包括大型語言模型的微調。AutoTrain 是一個免程式碼解決方案，您可以在自己的雲端、Hugging Face Spaces 或本地端進行微調。它同時支援基於網頁的 GUI、命令列介面 (CLI) 以及透過 yaml 設定檔進行訓練。                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [使用 Unsloth 微調大型語言模型](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth 是一個開源框架，支援大型語言模型微調和強化學習 (RL)。Unsloth 簡化了本地端訓練、評估和部署，並提供現成的[筆記本](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) 可直接使用。它亦支援語音合成 (TTS)、BERT 及多模態模型。欲開始學習，請參閱他們逐步的 [大型語言模型微調指南](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide)。                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## 作業

從上述教學中選擇其中一個並進行學習演練。_我們可能會在此儲存庫中以 Jupyter 筆記本形式複製這些教學的版本，僅供參考。請直接使用原始資源以取得最新版本_。

## 很棒！繼續您的學習之旅。

完成本課程後，請查看我們的 [生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ，繼續提升您的生成式 AI 知識！

恭喜！！您已完成本課程 v2 系列的最終課程！千萬別停止學習與實作。**請參考 [資源](RESOURCES.md?WT.mc_id=academic-105485-koreyst) 頁面，尋找更多相關主題的建議內容。

我們的 v1 課程系列也已更新，增加了更多作業與概念。花點時間刷新您的知識，並請 [分享您的問題與回饋](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)，幫助我們為社群改進這些課程。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->