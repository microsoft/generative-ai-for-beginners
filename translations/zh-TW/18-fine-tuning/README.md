[![開源模型](../../../translated_images/zh-TW/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# 微調您的大型語言模型

使用大型語言模型來構建生成式 AI 應用帶來了新的挑戰。一個關鍵問題是確保模型針對特定用戶請求生成的內容的回應品質（準確性和相關性）。在先前的課程中，我們討論了像提示工程和檢索增強生成等技術，以透過_修改現有模型的提示輸入_來解決該問題。

在今天的課程中，我們將討論第三種技術，<strong>微調</strong>，它試圖透過_使用額外數據重新訓練模型本身_來應對這個挑戰。讓我們深入了解細節。

## 學習目標

本課程介紹預訓練語言模型的微調概念，探討這種方法的優點與挑戰，並提供何時以及如何使用微調以提升生成式 AI 模型性能的指導。

課程結束時，您應該能回答以下問題：

- 什麼是語言模型的微調？
- 何時以及為何微調是有用的？
- 我如何微調一個預訓練模型？
- 微調有哪些限制？

準備好了嗎？讓我們開始吧。

## 圖解指南

想先對我們即將涵蓋的內容有個整體了解嗎？看看這個圖解指南，它描述了本課程的學習旅程—從學習微調的核心概念與動機，到理解微調過程和執行微調任務的最佳實踐。這是一個引人入勝的探索主題，別忘了查看[資源](./RESOURCES.md?WT.mc_id=academic-105485-koreyst)頁面，獲取更多支援您自學之旅的連結！

![語言模型微調圖解指南](../../../translated_images/zh-TW/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## 什麼是語言模型的微調？

從定義上來看，大型語言模型是在來自多種來源（包括網路）的龐大文本資料上_預訓練_的。如我們在前幾課已學的，我們需要像_提示工程_和_檢索增強生成_等技術來提升模型對用戶提問（「提示」）的回應品質。

一個常見的提示工程技巧是透過提供_指示_（明確指引）或_給予一些範例_（隱含指引）給模型，來提供更多回應期望的指導。此方法稱為_少量示範學習_，但有兩個限制：

- 模型的 token 限制可能會限制您能提供的範例數量，進而影響效果。
- 模型 token 成本可能使每個提示都增加範例變得昂貴，限制靈活度。

微調是機器學習系統中常見的做法，我們會拿一個預訓練模型，並用新數據重新訓練它以提升其在特定任務上的表現。在語言模型的情境下，我們可以用_為特定任務或應用領域精心挑選的示例集_來微調預訓練模型，創造一個<strong>自訂模型</strong>，使其對該任務或領域更準確且更相关。微調的附帶好處是它也能減少少量示範學習所需的範例數量—降低 token 使用和相關費用。

## 何時及為何應該微調模型？

在_這個_上下文中，我們談到的微調是指<strong>監督式</strong>微調，即透過<strong>新增非原始訓練資料集內容的數據</strong>來重新訓練模型。這不同於非監督式微調方法，後者是在原始數據上用不同超參數重訓模型。

需要記住的關鍵是，微調是一項進階技術，需要一定的專業知識才能獲得預期結果。若操作不當，可能無法帶來預期的提升，甚至可能降低模型在目標領域的表現。

所以，在學習「如何」微調語言模型之前，您需要知道「為何」要採用這方法，以及「何時」開始微調過程。先問自己這些問題：

- <strong>使用案例</strong>：您的_微調使用案例_是什麼？您想改進當前預訓練模型的哪個方面？
- <strong>替代方案</strong>：您是否嘗試過_其他技術_以達成理想結果？用它們建立比較基準。
  - 提示工程：嘗試如少量示範提示含相關回應範例。評估回應品質。
  - 檢索增強生成：嘗試透過查詢您數據所檢索的結果來增強提示。評估回應品質。
- <strong>成本</strong>：您是否已識別微調的成本？
  - 可微調性 - 該預訓練模型是否支持微調？
  - 工時 - 準備訓練資料、評估與調整模型的工作量。
  - 計算資源 - 進行微調任務和部署微調模型所需的計算資源。
  - 數據 - 是否能取得足夠高品質的示例以產生微調效果。
- <strong>效益</strong>：您是否確認微調的效益？
  - 品質 - 微調後的模型是否優於基準模型？
  - 成本 - 是否能藉由簡化提示降低 token 使用量？
  - 擴展性 - 是否可將基底模型重新用於新領域？

回答完這些問題後，您應能判斷微調是否適合您的使用案例。理想上，當效益超越成本時，方法才是合理的。一旦決定繼續，就該思考_如何_微調該預訓練模型。

想要了解更多決策過程？觀看 [微調還是不微調](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## 我們如何微調預訓練模型？

要微調一個預訓練模型，您需要：

- 一個待微調的預訓練模型
- 一個用於微調的數據集
- 一個執行微調任務的訓練環境
- 一個部署微調後模型的託管環境

## 微調實作

> <strong>注意：</strong>本文部分教程提及的 `gpt-35-turbo` / `gpt-3.5-turbo` 已全面停用推論與微調。如果您今天開始新的微調工作，建議改選目前支援的模型—例如 `gpt-4o-mini` 或 `gpt-4.1-mini`。請參閱[微調模型清單](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models)以了解目前可微調模型。這些教程中的概念和步驟依然適用。

下列資源提供逐步教程，引導您使用選定模型及精心挑選的數據集完成實例。執行這些教程需要在對應服務商有帳號，並可使用相關模型和資料集。

| 服務商       | 教程                                                                                                                                                                         | 說明                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [如何微調聊天模型](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                       | 學習如何微調 `gpt-35-turbo` 用於特定領域（「食譜助手」），包括準備訓練資料、執行微調任務，以及使用微調後模型進行推論。                                                                                                                                                                                                                                                                                                      |
| Azure OpenAI | [GPT 3.5 Turbo 微調教程](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst)       | 學習如何在 **Azure** 上微調 `gpt-35-turbo-0613` 模型，包括建立和上傳訓練資料、執行微調任務、部署並使用新模型。                                                                                                                                                                                                                                                                                                          |
| Hugging Face | [用 Hugging Face 微調 LLM](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                                  | 本部落格將帶您透過 [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) 庫和 [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst)，使用 Hugging Face 上的開放數據集微調開放LLM（例如 `CodeLlama 7B`）。                                                                                                           |
|              |                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 🤗 AutoTrain | [用 AutoTrain 微調 LLM](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                           | AutoTrain（或 AutoTrain Advanced）是 Hugging Face 開發的 Python 函式庫，支持多種任務的微調，包括LLM微調。AutoTrain屬於無需程式碼解決方案，能在您自己的雲端、Hugging Face Spaces 或本地進行。支援基於網頁 GUI、CLI 以及透過 yaml 配置文件的訓練。                                                                                                                                                        |
|              |                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 🦥 Unsloth   | [用 Unsloth 微調 LLM](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                                         | Unsloth 是一個開源框架，支持LLM微調及強化學習（RL）。Unsloth簡化本地訓練、評估與部署，並提供可用的[notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst)。同時支持文字轉語音（TTS）、BERT 及多模態模型。想入門請閱讀其循序漸進的[LLM微調指南](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide)。                                                                                           |
|              |                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
## 作業

選擇上述之一教程並逐步完成它們。_我們可能會在本存儲庫中以 Jupyter 筆記本形式複製這些教程版本供參考，請直接使用原始來源以獲取最新版_。

## 做得好！繼續學習。

完成本課程後，請參考我們的 [生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升您的生成式 AI 知識！

恭喜！！您已完成本課程 v2 系列的最後一課！別停止學習與實踐。**查看[資源](RESOURCES.md?WT.mc_id=academic-105485-koreyst)頁面，獲取更多關於此主題的建議。**

我們的 v1 系列課程也已更新，加入更多作業與概念。花一點時間刷新知識，並歡迎[分享您的問題和反饋](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)，幫助我們為社群改進這些課程。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->