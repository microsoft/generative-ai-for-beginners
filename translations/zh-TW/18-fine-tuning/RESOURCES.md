# 自學資源

本課程使用 OpenAI 與 Microsoft Foundry 的核心資源作為術語和教學參考。以下是給您自學之用的非完整資源清單。以下每個連結皆指向最新且受支援的資料。

## 1. 主要資源

| 標題/連結 | 說明 |
| :--- | :--- |
| [使用 OpenAI 模型進行微調](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | 微調透過訓練比提示中可放入更多的範例來改善少量示例學習—節省成本、提升回應品質並降低延遲。**從 OpenAI 獲得微調總覽。** |
| [何時使用 Microsoft Foundry 微調](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | 了解<strong>微調的意義（概念）</strong>、為何要考慮使用，該使用何種資料並如何衡量品質—以及何時適用 SFT、DPO 或 RFT。 |
| [使用微調自訂模型](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | Microsoft Foundry 中使用入口網站、OpenAI / Foundry Python SDK，或 REST API 進行微調的<strong>端到端操作流程</strong>—涵蓋資料準備、訓練、檢查點與部署。 |
| [持續微調](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | 選取已微調模型作為基底，並<strong>進一步微調</strong>以納入新訓練範例的反覆操作流程。 |
| [使用工具（函數）呼叫進行微調](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | 使用包含工具呼叫範例的資料微調模型，可提升輸出質量—更準確、一致且格式相似的回應，並減少 prompt token 使用量。 |
| [微調模型：Microsoft Foundry 指南](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | 查看<strong>可微調模型名單</strong>、支持的方法（SFT / DPO / RFT）及其可用的區域。 |
| [微調總覽：技術與模式](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | 比較三種訓練技術（SFT、DPO、RFT）與兩種運行模式（無伺服器與託管運算），並提供如何選擇基模型與入門的指引。 |
| <strong>教學</strong>：[在 Microsoft Foundry 中微調模型](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | 建立範例資料集、準備微調、在目前受支援模型（如 `gpt-4.1-mini`）上執行微調作業，並將微調模型部署至 Azure。 |
| <strong>教學</strong>：[使用無伺服器 API 部署微調模型](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | 在 Microsoft Foundry 中，利用低程式碼、基於 UI 的工作流程，將開放及合作模型（Phi、Llama、Mistral 等）調整為您專屬的資料集。 |
| <strong>教學</strong>：[在 Azure Databricks 上微調 Hugging Face 模型](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | 使用 Azure Databricks 與 Hugging Face Trainer，在單一 GPU 上利用 `transformers` 函式庫微調 Hugging Face 模型。 |
| <strong>訓練課程</strong>：[使用 Azure 機器學習微調基礎模型](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | Azure 機器學習模型目錄中有許多可微調的開源模型。此課程是[Azure ML 生成式 AI 學習路徑](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst)的一部分。 |
| <strong>教學</strong>：[Azure OpenAI 與 Weights & Biases 微調](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | 在 Azure 上使用 W&B 跟踪和分析微調訓練。擴展 OpenAI 微調指南，加上 Azure 特定步驟與實驗追蹤功能。 |

## 2. 次要資源

本節蒐集值得探索的其他資源，課程中未深入涵蓋。利用這些資源來擴展您在此主題上的專業知識。

| 標題/連結 | 說明 |
| :--- | :--- |
| **OpenAI Cookbook**：[聊天模型微調的資料準備與分析](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | 微調前對聊天資料集進行前處理與分析：檢查格式錯誤、取得基本統計數據，估算 token 數量（及成本）。搭配[OpenAI 微調指南](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst)。 |
| **OpenAI Cookbook**：[使用 Qdrant 的檢索強化生成（RAG）微調](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | 完整範例，示範如何微調 OpenAI 模型應用於 RAG，整合 Qdrant 與少量示例學習以提升效能並減少虛構內容。 |
| **OpenAI Cookbook**：[使用 Weights & Biases 微調 GPT](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | 使用 W&B 跟踪模型訓練與微調。先閱讀他們的[OpenAI 微調](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst)指南，後執行 Cookbook 練習。 |
| **Hugging Face 教學**：[如何使用 Hugging Face TRL 微調大型語言模型](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | 使用 Hugging Face TRL、Transformers 及資料集微調開放 LLM：定義用例、建立開發環境、準備資料集、微調、評估與部署。 |
| **Hugging Face**：[AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | Hugging Face 提供的無程式碼/低程式碼圖書館，可微調多種模型。可在自有雲端、Hugging Face Spaces 或本機透過 GUI、CLI 或 YAML 設定運行。 |
| **Unsloth**：[大型語言模型微調指南](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | 一套開源框架，簡化本地 LLM 微調和強化學習，並附有即用型[筆記本](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst)。 |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->