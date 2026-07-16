[![開源模型](../../../translated_images/zh-MO/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# 微調你的大型語言模型

使用大型語言模型來打造生成式 AI 應用帶來了新的挑戰。一個重要的問題是確保模型根據用戶請求生成內容時的回應品質（準確性及相關性）。在之前的課程中，我們討論了例如提示工程（prompt engineering）和檢索增強生成（retrieval-augmented generation）等技術，這些方法試圖通過_修改輸入提示_來解決問題。

在今天的課程中，我們將介紹第三種技術，<strong>微調</strong>，它試圖通過_重新訓練模型本身_並添加額外資料來解決這個挑戰。讓我們深入了解細節。

## 學習目標

本課程將介紹預訓練語言模型的微調概念，探討此方法的優點與挑戰，並指導你何時以及如何使用微調來提升生成式 AI 模型的效能。

修完本課程後，你應該能回答以下問題：

- 什麼是語言模型的微調？
- 何時及為何微調是有用的？
- 我如何微調一個預訓練模型？
- 微調有哪些限制？

準備好了嗎？讓我們開始吧。

## 插圖指南

想先掌握本課程涵蓋內容的大致脈絡嗎？看看這張插圖指南，它描述了本課程的學習旅程——從理解微調的核心概念與動機，到了解執行微調的過程及最佳實踐。這是個引人入勝的主題，別忘了查看[資源](./RESOURCES.md?WT.mc_id=academic-105485-koreyst)頁面，裡面有更多連結支援你的自主學習旅程！

![微調語言模型插圖指南](../../../translated_images/zh-MO/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## 什麼是語言模型的微調？

按定義，大型語言模型是在大量來自多元來源（包括網絡）的文本上進行_預訓練_。正如我們在前面課程中學到，為了提升模型對用戶問題（「提示」）回應的質量，我們需要像_提示工程_和_檢索增強生成_等技術。

一種流行的提示工程技術是透過提供_指令_（明確指導）或_給予範例_（隱含指導）來引導模型瞭解期望的回應，這稱為_少量示例學習（few-shot learning）_，但它有兩個限制：

- 模型的 token 限制會限制可提供的範例數量，並限制效果。
- 模型 token 成本可能會使每個提示加入範例的成本變高，限制彈性。

微調是機器學習中的常見做法，我們會拿預訓練模型並用新的資料進行重新訓練，以提升它在特定任務上的表現。在語言模型的背景中，我們可以用_為特定任務或應用領域策劃的範例集_對預訓練模型進行微調，從而創造出在該特定任務或領域上可能更準確且相關的<strong>定制模型</strong>。微調的附帶好處是，它還能減少少量示例學習所需的範例數量——降低 token 使用量和相關成本。

## 何時及為何要微調模型？

在_此_語境中，當我們談論微調時，是指<strong>監督式</strong>微調，透過<strong>添加原始訓練資料集之外的數據</strong>來重新訓練模型。這與非監督式微調不同，後者是用原始資料但改變超參數來重新訓練模型。

需要記住的重點是，微調是一項進階技術，需要一定專業知識以達成預期效果。如果操作不當，可能無法帶來預期的改善，甚至會降低模型在目標領域的表現。

所以，在學習「如何」微調語言模型之前，你需要先知道「為何」選擇這條路，以及「何時」開始微調流程。先問自己這些問題：

- <strong>使用案例</strong>：你的_使用案例_是什麼？你想改善目前預訓練模型的哪個面向？
- <strong>替代方案</strong>：你是否嘗試過_其他技術_來達成目標？把它們用於建立比較基準。
  - 提示工程：嘗試使用少量範例提示，來評估回應品質。
  - 檢索增強生成：嘗試在提示中加入由數據檢索的查詢結果，評估回應品質。
- <strong>成本</strong>：你有評估微調的成本嗎？
  - 可調整性 - 預訓練模型是否支持微調？
  - 工作量 - 編輯訓練資料、評估及優化模型的工作量。
  - 計算資源 - 運行微調任務及部署微調模型所需的計算資源。
  - 數據 - 是否有足夠高質量範例用於微調成效。
- <strong>效益</strong>：你有確認微調的效益嗎？
  - 品質 - 微調後的模型效能是否優於基準？
  - 成本 - 是否透過簡化提示降低 token 使用量？
  - 可擴展性 - 是否能將基礎模型重新用於新領域？

回答這些問題後，你應能判斷微調是否是你使用案例的合適方法。理想上，只有當效益大於成本時此方法才有意義。一旦決定繼續，就該思考_如何_微調預訓練模型。

想瞭解更多決策過程的洞見？觀看[微調還是不微調](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## 我們如何微調預訓練模型？

想微調預訓練模型，你需要具備：

- 可微調的預訓練模型
- 用於微調的數據集
- 運行微調任務的訓練環境
- 部署微調模型的托管環境

## 微調實例

> **注意：** `gpt-35-turbo` / `gpt-3.5-turbo`，在以下某些教程中有提及，已停止提供推理與微調服務。如果你今天要開始新的微調任務，請選擇目前支持的模型——如 `gpt-4o-mini` 或 `gpt-4.1-mini`。可參考[微調模型清單](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) 獲取最新支持的微調模型列表。本教程的概念和步驟仍然適用。

以下資源提供逐步教程，帶你透過選定模型與策劃數據集完成實際示例。要進行這些教程，你需要在特定提供者處註冊帳戶，並取得相關模型和數據集的存取權。

| 提供者       | 教程                                                                                                                                                                         | 說明                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [如何微調聊天模型](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                             | 學習如何微調 `gpt-35-turbo`，針對特定領域（「食譜助理」）準備訓練資料，執行微調任務，並使用微調後的模型做推理。                                                                                                                                                                                                                                                                                                        |
| Azure OpenAI | [GPT 3.5 Turbo 微調教程](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst)               | 學習如何在<strong>Azure</strong>上微調 `gpt-35-turbo-0613` 模型，包括建立與上傳訓練資料，執行微調工作，部署及使用新模型。                                                                                                                                                                                                                                                                                                         |
| Hugging Face | [用 Hugging Face 微調大型語言模型](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | 這篇部落格文章帶你學習如何使用 [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) 庫和 [Transformer 強化學習 (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst)，利用 Hugging Face 的公開[數據集](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst)微調一款開放大型語言模型（例如 `CodeLlama 7B`）。             |
|              |                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 🤗 AutoTrain | [使用 AutoTrain 微調大型語言模型](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain（或 AutoTrain Advanced）是 Hugging Face 開發的 Python 庫，支援多種任務的微調，包括大型語言模型微調。AutoTrain 是無需程式碼的解決方案，可在你自己的雲端、Hugging Face Spaces 或本地環境完成微調。它支援基於網頁的 GUI、命令列介面及透過 yaml 配置文件進行訓練。                                                                                                       |
|              |                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 🦥 Unsloth   | [使用 Unsloth 微調大型語言模型](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                                         | Unsloth 是一個開源框架，支援大型語言模型微調與強化學習（RL）。Unsloth 透過準備好的[筆記本](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst)，簡化本地訓練、評估與部署。它還支援文字轉語音（TTS）、BERT 及多模態模型。若要開始，請閱讀他們的逐步[微調大型語言模型指南](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide)。                                |
|              |                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
## 練習題

從上述教程中選擇一個，依步驟完成。_我們可能會在此存儲庫中的 Jupyter 筆記本中複製這些教程的版本供參考。請直接使用原始資源以取得最新版。_

## 做得好！繼續學習。

完成本課程後，請查看我們的[生成式 AI 學習集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，繼續提升你的生成式 AI 知識！

恭喜！！你已完成本課程的 v2 系列最終課程！請繼續學習與實作。**別忘了查看[資源](RESOURCES.md?WT.mc_id=academic-105485-koreyst)頁面，那裡有更多僅針對此主題的額外建議清單。

我們的 v1 系列課程也已更新，新增更多練習和概念。花點時間回顧你的知識，並請[分享你的問題和反饋](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)，幫助我們為社群改進這些課程。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->