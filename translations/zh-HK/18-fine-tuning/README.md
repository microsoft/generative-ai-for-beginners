[![開源模型](../../../translated_images/zh-HK/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# 微調您的大型語言模型

使用大型語言模型來建立生成式 AI 應用程式帶來了新的挑戰。其中一個關鍵問題是確保模型為特定用戶請求所生成內容的回應質量（準確性和相關性）。在之前的課程中，我們探討了提示工程和檢索增強生成等技術，它們試圖通過_修改輸入提示_的方式來解決這個問題。

今天的課程，我們將討論第三種技術，<strong>微調</strong>，它嘗試通過_使用額外數據重新訓練模型本身_來解決這一挑戰。讓我們深入了解細節。

## 學習目標

本課程介紹了預訓練語言模型的微調概念，探討了這種方法的優點與挑戰，並為您提供何時以及如何使用微調來提升生成式 AI 模型性能的指導。

完成本課程後，您應該能回答以下問題：

- 什麼是語言模型的微調？
- 何時以及為何微調是有用的？
- 如何微調預訓練模型？
- 微調有哪些限制？

準備好了嗎？我們開始吧。

## 插圖指南

想先獲得我們將要涵蓋內容的全貌嗎？看看這份插圖指南，介紹本課程的學習旅程——從學習微調的核心概念和動機，到了解微調任務的流程和最佳實踐。這是一個非常有趣的探索主題，別忘了查看[資源](./RESOURCES.md?WT.mc_id=academic-105485-koreyst)頁面，裡面有更多支援您自學旅程的連結！

![微調語言模型插圖指南](../../../translated_images/zh-HK/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## 什麼是語言模型的微調？

按定義，大型語言模型是預先在來自多元來源（包括網路）的大量文本上進行_預訓練_。正如我們在之前的課程中學到的，我們需要像_提示工程_和_檢索增強生成_這樣的技巧，來提升模型對用戶問題（「提示」）的回應質量。

一種流行的提示工程技術是通過給模型更多引導，比如提供_指示_（明確引導）或_給它幾個範例_（隱式引導），這被稱為_少量示範學習_，但它有兩個限制：

- 模型的詞元限制會限制您可以提供範例的數量，並限制效果。
- 模型詞元成本會使每個提示添加範例變得昂貴，並限制彈性。

微調是機器學習系統中的常見做法，我們用新的數據對預訓練模型重新訓練，以提升其在特定任務上的表現。在語言模型的上下文中，我們可以用針對特定任務或應用領域<strong>精心挑選的範例集</strong>對預訓練模型進行微調，從而創建一個可能對該任務或領域更準確、更具相關性的<strong>自訂模型</strong>。微調的另一個副效益是它可以減少少量示範學習所需的範例數量——從而減少詞元使用及相關成本。

## 何時以及為何要微調模型？

在_此_語境中，當我們談論微調時，我們指的是<strong>監督式</strong>微調，通過<strong>新增未包含於原始訓練數據集的資料</strong>來重新訓練模型。這與無監督式微調不同，後者是在原始數據上以不同的超參數重新訓練模型。

關鍵是要記住，微調是一項需要一定專業知識才能達到預期效果的高階技術。如果操作不當，可能無法帶來預期提升，甚至可能降低模型在目標領域的表現。

因此，在學習「如何」微調語言模型之前，您需要知道「為什麼」選擇這條路徑，以及「何時」開始微調流程。請先問自己以下問題：

- <strong>使用案例</strong>：您的微調_使用案例_是什麼？您希望提升目前預訓練模型的哪個方面？
- <strong>替代方案</strong>：您嘗試過_其他技術_來達成目標嗎？使用它們建立一個基線以便比較。
  - 提示工程：嘗試使用少量示範的相關提示範例。評估回應質量。
  - 檢索增強生成：嘗試用資料檢索結果增強提示。評估回應質量。
- <strong>成本</strong>：您是否已評估微調的成本？
  - 可調整性 - 預訓練模型是否支持微調？
  - 工作量 - 準備訓練數據、評估和優化模型所需的努力。
  - 計算資源 - 執行微調任務與部署微調模型所需資源。
  - 數據 - 拿到足夠且優質的範例來提升微調效果。
- <strong>益處</strong>：您是否確認了微調帶來的益處？
  - 質量 - 微調後的模型是否超越基線？
  - 成本 - 是否因簡化提示降低了詞元使用？
  - 擴展性 - 是否能將基礎模型用於新領域？

透過回答這些問題，您應該能判斷微調是否適合您的使用案例。理想情況下，微調只在益處超過成本時才是合理選擇。決定進行後，就該思考_如何_微調預訓練模型。

想了解更多關於決策過程的見解？觀看 [微調還是不微調](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## 如何微調預訓練模型？

要微調預訓練模型，您需要：

- 一個可微調的預訓練模型
- 一組用於微調的數據集
- 執行微調任務的訓練環境
- 部署微調後模型的託管環境

## 微調實戰

> <strong>注意：</strong>下列教學中引用的 `gpt-35-turbo` / `gpt-3.5-turbo` 已經不再開放推理與微調服務。如果您今天開始新的微調任務，請選擇當前支持的模型，例如 `gpt-4o-mini` 或 `gpt-4.1-mini`。請參閱[微調模型列表](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models)了解目前可微調的模型集合。這些教學中的觀念及步驟仍然適用。

以下資源提供逐步教學，帶您用範例模型和精心挑選的數據集實際操作。完成這些教學時，您需要在特定供應商處有帳號，並可存取相關模型和數據集。

| 供應商      | 教學                                                                                                                                                                       | 說明                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [如何微調聊天模型](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                      | 學習如何針對特定領域（「食譜助理」）微調 `gpt-35-turbo`，包括準備訓練數據、執行微調任務及使用微調後模型進行推理。                                                                                                                                                                                                                                                                                                                |
| Azure OpenAI | [GPT 3.5 Turbo 微調教學](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst)         | 學習如何在 **Azure** 上微調 `gpt-35-turbo-0613` 模型，包含創建並上傳訓練數據、執行微調任務，部署並使用新模型。                                                                                                                                                                                                                                                                                                                |
| Hugging Face | [使用 Hugging Face 微調大型語言模型](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                         | 本文說明如何利用 [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) 函式庫及 [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) 在 Hugging Face 上使用開放[數據集](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst)微調開放的 LLM（例如 `CodeLlama 7B`）。 |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 🤗 AutoTrain | [使用 AutoTrain 微調 LLM](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                                | AutoTrain（或 AutoTrain Advanced）是 Hugging Face 開發的 Python 函式庫，可用於多種任務的微調，包括 LLM 微調。AutoTrain 是無需程式碼的解決方案，微調可在您的雲端、Hugging Face Spaces 或本地進行，支持網頁圖形介面、指令列介面和 yaml 配置文件訓練。                                                                                                            |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 🦥 Unsloth   | [使用 Unsloth 微調 LLM](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                                                | Unsloth 是一個支持 LLM 微調和強化學習（RL）的開源框架。Unsloth 簡化了本地訓練、評估和部署流程，附帶現成可用的[筆記本](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst)。它還支持文字轉語音（TTS）、BERT 及多模態模型。開始前，請閱讀他們分步詳解的[LLM 微調指南](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide)。                                                                     |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
## 作業

從上述教學中選擇一個並跟著操作。我們可能會在本倉庫以 Jupyter 筆記本形式複製這些教學作為參考。請直接使用原始來源以獲得最新版本。

## 做得好！繼續學習。

完成本課程後，請瀏覽我們的[生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升您的生成式 AI 知識！

恭喜！！您已完成本課程 v2 系列的最後一課！別停止學習與創建。**查看[資源](RESOURCES.md?WT.mc_id=academic-105485-koreyst)頁面，了解更多這個主題的建議。

我們的 v1 系列課程也已更新，新增了更多作業和概念。花點時間複習您的知識，並請您[分享問題與反饋](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)，幫助我們為社群改進這些課程。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->