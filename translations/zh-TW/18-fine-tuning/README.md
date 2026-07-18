[![Open Source Models](../../../translated_images/zh-TW/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# 微調您的大型語言模型

使用大型語言模型來構建生成式 AI 應用帶來了新的挑戰。一個關鍵問題是確保模型在生成的內容對於特定使用者請求來說具有響應品質（準確性和相關性）。在之前的課程中，我們討論了像是提示工程和檢索增強生成等技術，這些技術透過_修改現有模型的提示輸入_來嘗試解決這個問題。

在今天的課程中，我們會討論第三種技術，<strong>微調</strong>，它嘗試透過_用額外資料重新訓練模型本身_來解決這個挑戰。讓我們深入細節吧。

## 學習目標

本課程介紹了預訓練語言模型的微調概念，探討此方法的好處與挑戰，並提供何時及如何使用微調來提升生成式 AI 模型表現的指引。

在本課程結束時，您應該能回答以下問題：

- 什麼是語言模型的微調？
- 何時且為何微調是有用的？
- 我如何微調預訓練模型？
- 微調有哪些限制？

準備好了嗎？讓我們開始吧。

## 插圖指南

想在深入了解前先有個大致概念嗎？看看這個插圖指南，它說明了本課程的學習旅程——從學習微調的核心概念與動機，到理解微調過程與最佳實踐。這是一個引人入勝的主題，別忘了查看[資源](./RESOURCES.md?WT.mc_id=academic-105485-koreyst)頁面，獲取更多支持自學的連結！

![微調語言模型的插圖指南](../../../translated_images/zh-TW/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## 什麼是語言模型的微調？

根據定義，大型語言模型是在來自多元來源（包含網路）大量文本上_預訓練_的。正如我們在之前課程中所學，我們需要像是_提示工程_和_檢索增強生成_等技術，以提升模型對使用者提問（「提示」）的回答品質。

一個常見的提示工程技巧是給予模型更多關於期望回答的指引，包含提供_指示_（明確指引）或_給予幾個範例_（隱含指導）。這被稱為_少量示範學習_，但它有兩個限制：

- 模型的詞元限制會限制您能提供的範例數量，並且降低成效。
- 模型詞元成本會讓每個提示加入範例變得昂貴，並限制彈性。

微調是機器學習系統中的一種常用做法，我們會拿到一個已預訓練的模型，並用新資料重新訓練，以提升其在特定任務的效能。在語言模型的語境中，我們可以用_特定任務或應用領域的策劃範例集_來微調預訓練模型，創建一個<strong>客製化模型</strong>，該模型在該任務或領域上可能更準確且相關。微調的一個附帶好處是，它還可以減少少量示範學習所需的範例數量——從而降低詞元使用量與相關成本。

## 何時及為何要微調模型？

在_此處_，當我們談論微調時，指的是<strong>監督式</strong>微調，即透過新增未包含於原始訓練資料集中的<strong>新資料</strong>來重新訓練模型。這和非監督式微調不同，後者是用不同超參數在原始資料上重新訓練。

需要記住的重點是，微調是一項進階技術，需要具備一定程度的專業知識才能獲得理想結果。如果操作不當，可能得不到預期改進，甚至降低模型在目標領域的表現。

因此，在學習「如何」微調語言模型之前，您需要了解「為何」需要採用此路徑，以及「何時」開始微調程序。先問自己以下問題：

- <strong>使用案例</strong>：您的_微調使用案例_是什麼？您希望改進當前預訓練模型的哪個方面？
- <strong>替代方法</strong>：您嘗試過其他技術達成預期目標嗎？用它們建立比較基準。
  - 提示工程：嘗試使用少量示範提示及相關回應範例，評估回答品質。
  - 檢索增強生成：嘗試用檢索出的相關查詢結果增強提示，評估回答品質。
- <strong>成本</strong>：您是否明確識別微調的成本？
  - 可調整性 — 預訓練模型是否允許微調？
  - 工時 — 用於準備訓練資料、評估與優化模型所需努力。
  - 計算資源 — 執行微調工作及部署微調模型所需。
  - 資料 — 取得足夠且品質優良的範例以影響微調成效。
- <strong>效益</strong>：您是否確認微調的效益？
  - 品質 — 微調後的模型是否超越基準模型？
  - 成本 — 是否透過簡化提示降低詞元使用？
  - 擴充性 — 是否能將基礎模型重新用於新領域？

回答完這些問題後，您應能判斷微調是否適合您的使用案例。理想情況下，只有當效益大於成本時，此方法才是有效的。一旦決定繼續，便該思考_如何_微調預訓練模型。

想進一步了解決策過程嗎？觀看[要不要微調？](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## 如何微調預訓練模型？

要微調一個預訓練模型，您需要具備：

- 一個要微調的預訓練模型
- 一個用於微調的資料集
- 一個進行微調作業的訓練環境
- 一個部署微調模型的主機環境

## 在 Microsoft Foundry 上微調

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) 是您今天在 Azure 上微調、部署和管理客製化模型的地方（它整合了原 Azure OpenAI Studio 和 Azure AI Studio）。開始作業前，了解 Foundry 提供的選項及平台建議的最佳實踐相當有幫助。底層是用 **LoRA（低秩適應）** 來高效微調模型，比重新訓練所有權重更快且成本更低。

### 第一步：選擇訓練技術

Foundry 支持三種微調技術。**從監督式微調 (SFT) 開始** —— 它適用範圍最廣。

| 技術 | 功能 | 何時使用 |
| --- | --- | --- |
| **監督式微調 (SFT)** | 針對輸入／輸出範例對進行訓練，讓模型學會產生您想要的回應。 | 大多數任務的預設：領域專精、任務表現、風格與語氣、指令遵循、語言適應。 |
| **直接偏好優化 (DPO)** | 從「更偏好」與「不偏好」回應對學習，使輸出與人類偏好一致。 | 當您有比較反饋，想提升回答品質、安全性與一致性時。 |
| **強化微調 (RFT)** | 利用 _評分者_ 的獎勵信號，透過強化學習優化複雜行為。 | 客觀、有理論推理的領域（數學、化學、物理）且有明確正誤答案。需較多機器學習專業知識。 |

### 第二步：選擇訓練等級

Foundry 讓您選擇訓練如何運行及其地點：

- <strong>標準</strong> — 在您的資源區域訓練並保證資料駐留。適用於資料必須留在特定區域的情況。
- <strong>全球</strong> — 使用您所在區域外的資源，藉此更便宜、更快速排隊（資料和權重會被複製到訓練區域）。沒有資料駐留需求時的良好預設。
- <strong>開發者</strong> — 成本最低，使用閒置容量，無延遲或 SLA 保證（作業可能被中斷並可恢復）。適合試驗用途。

### 第三步：選擇基礎模型

可微調的模型包括 OpenAI 的 `gpt-4o-mini`、`gpt-4o`、`gpt-4.1`、`gpt-4.1-mini` 和 `gpt-4.1-nano`（SFT；4o/4.1 系列亦支持 DPO），推理模型 `o4-mini` 和 `gpt-5`（RFT），還有開源模型如 `Ministral-3B`、`Qwen-32B`、`Llama-3.3-70B-Instruct` 及 `gpt-oss-20b`（在 Foundry 資源上進行 SFT）。務必檢查最新的[微調模型清單](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models)以了解支持的方法、區域和可用性。

> Foundry 提供兩種模式：<strong>無伺服器</strong>（消耗計價，無需管理 GPU 配額，支援 OpenAI 以及選定模型）與<strong>管理計算</strong>（透過 Azure Machine Learning 自帶 VM，支援最多模型種類）。大多數人建議從無伺服器模式開始。

### Foundry 最佳實踐

- **先建立基準。** 在進行微調前，先用提示工程和 RAG 評估基礎模型效能，以證明增益。
- **從小開始，再擴大。** 從 50-100 個高品質範例驗證方法，再擴展到 500+ 以投入生產。品質勝過數量，刪除低品質範例。
- **正確格式化資料。** 訓練與驗證檔案必須是 JSONL 格式、UTF-8 編碼且含 BOM，大小低於 512 MB，採用聊天完成訊息格式。務必包含驗證檔以監控過度擬合。
- **推論時保留訓練系統提示。** 呼叫模型時使用與訓練中相同的系統訊息。
- **評估檢查點 — 不要盲目部署最後一個。** Foundry 保留最後三個訓練週期的檢查點作為可部署版本；根據 `train_loss` / `valid_loss` 與詞元準確度選擇泛化最佳者。
- **比較微調模型與基準時，一起衡量詞元成本與品質。**
- **持續微調迭代。** 您可以在已微調模型上繼續微調新資料（OpenAI 模型支持）。
- **注意主機成本。** 已部署的自訂模型按小時計費，閒置部署 15 天後會被移除——清理不需要的資源。

您可以透過[使用微調自訂模型](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst)的完整演練流程了解，準備好後也可查看[DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst)與[RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst)的相關指南來探索其他技術。

## 微調實務案例

以下資源提供步驟詳盡的教學，引導您實作目前支持模型和策劃資料集的範例。要跟著練習，您需要在特定提供者註冊帳號，並取得相關模型及資料集的存取權。

| 提供者       | 教程                                                                                                                                                                       | 描述                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [如何微調聊天模型](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | 學習如何為特定領域（「食譜助理」）微調最新的 OpenAI 聊天模型，包括準備訓練資料、執行微調作業，並使用微調模型進行推論。                                                                                                                                                                                                                                              |
| Microsoft Foundry | [使用微調自訂模型](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | 學習如何在 Microsoft Foundry 上為當前支援模型（如 `gpt-4.1-mini`）進行微調：準備並上傳訓練及驗證資料，執行微調作業，然後部署並使用新模型。                                                                                                                                                                                                                                                                 |

| Hugging Face | [使用 Hugging Face 微調大型語言模型（LLMs）](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | 這篇部落格文章帶你使用 [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) 函式庫和 [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) 以開放的 [datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) 來微調一個 _open LLM_（例如：`CodeLlama 7B`），在 Hugging Face 平台上操作。 |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [使用 AutoTrain 微調大型語言模型](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain（或稱 AutoTrain Advanced）是 Hugging Face 開發的一個 Python 函式庫，支援多種任務的微調包括 LLM 微調。AutoTrain 是一個免程式碼解決方案，微調可在您自己的雲端、Hugging Face Spaces 或本地端進行。它同時支援基於網頁的圖形介面、命令行介面（CLI）及透過 yaml 配置文件進行訓練。                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [使用 Unsloth 微調大型語言模型](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth 是一個開源框架，支援大型語言模型微調及強化學習（RL）。Unsloth 透過可用的 [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) 簡化了本地端訓練、評估及部署流程。它也支援語音合成（TTS）、BERT 以及多模態模型。若要開始，請閱讀他們的循序漸進 [Fine-tuning LLMs Guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide)。                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## 任務

選擇上述教程中的一個並實際操作。_我們可能會將這些教程的版本在本倉庫的 Jupyter 筆記本中進行複製，只作為參考。請直接使用原始來源以獲取最新版本_。

## 太棒了！繼續學習吧。

完成本課程後，請查看我們的[生成式 AI 學習收藏](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，繼續提升您的生成式 AI 知識！

恭喜!! 您已完成本課程 v2 系列的最終課程！別停止學習與創建。**請查看 [資源](RESOURCES.md?WT.mc_id=academic-105485-koreyst) 頁面，裡面有更多關於此主題的建議列表。

我們的 v1 系列課程也已更新，增加了更多任務與概念。請花點時間溫習您的知識 — 並且歡迎[分享您的問題與回饋](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)，幫助我們為社群改進這些課程。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->