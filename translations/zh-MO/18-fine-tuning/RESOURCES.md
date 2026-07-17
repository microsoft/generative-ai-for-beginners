# 自學資源

本課程以 OpenAI 和 Microsoft Foundry 的核心資源作為術語和教程的參考。以下是供您自我學習之用的非完整列表。以下每個連結皆指向當前且受支持的資料。

## 1. 主要資源

| 標題/連結 | 說明 |
| :--- | :--- |
| [使用 OpenAI 模型進行微調](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | 微調透過訓練更多範例，而非只使用 prompt 中的少量示例，提升少量樣本學習效果 — 節省成本、提升回應品質、並實現更低延遲的請求。**取得 OpenAI 的微調概述。** |
| [何時使用 Microsoft Foundry 微調](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | 瞭解<strong>什麼是微調（概念）</strong>、為何應考慮微調、應該使用哪些數據、如何衡量品質 — 以及何時適合使用 SFT、DPO 或 RFT。 |
| [使用微調自訂模型](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | Microsoft Foundry 微調的端到端<strong>操作流程</strong>，涵蓋透過入口網站、OpenAI / Foundry Python SDK 或 REST API 執行微調，包括資料準備、訓練、檢查點與部署。 |
| [連續微調](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | 迭代地選擇已微調模型作為基準模型，並在新的訓練樣本集上<strong>進一步微調</strong>的過程。 |
| [使用工具呼叫（function calling）進行微調](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | 使用工具呼叫示例<strong>微調您的模型</strong>可提升輸出品質 — 產出更準確、一致、格式類似的回應，且使用更少的 prompt 代幣。 |
| [微調模型：Microsoft Foundry 指南](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | 查詢<strong>可微調的模型</strong>、支援的方法（SFT / DPO / RFT）與可用區域。 |
| [微調概述：技術與模式](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | 比較三種訓練技術（SFT、DPO、RFT）及兩種模式（無伺服器與管理運算），並提供基準模型選擇與入門指引。 |
| <strong>教學</strong>：[在 Microsoft Foundry 中微調模型](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | 建立範例資料集，準備微調，執行支持模型（如 `gpt-4.1-mini`）的微調工作，並在 Azure 上部署微調模型。 |
| <strong>教學</strong>：[透過無伺服器 API 部署微調模型](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | 使用 Microsoft Foundry 中的低代碼、UI 基礎工作流程，針對您的數據集定制開源及合作模型（Phi、Llama、Mistral 等）。 |
| <strong>教學</strong>：[在 Azure Databricks 上微調 Hugging Face 模型](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | 使用 `transformers` 庫與 Hugging Face Trainer，在單 GPU 上透過 Azure Databricks 微調 Hugging Face 模型。 |
| <strong>訓練</strong>：[使用 Azure Machine Learning 微調基礎模型](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | Azure Machine Learning 模型目錄提供許多可微調的開源模型。屬於[Azure ML 生成式 AI 學習路徑](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst)的一部分。 |
| <strong>教學</strong>：[使用 Weights & Biases 進行 Azure OpenAI 微調](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | 使用 W&B 在 Azure 上追蹤與分析微調運行。擴充 OpenAI 微調指南並加入 Azure 專用步驟與實驗追蹤。 |

## 2. 次要資源

本節收錄值得探索的額外資源，但課程中未涵蓋。用它們來建立您對此主題的專業知識。

| 標題/連結 | 說明 |
| :--- | :--- |
| **OpenAI Cookbook**：[聊天模型微調的資料準備與分析](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | 在微調前對聊天資料集進行預處理與分析：檢查格式錯誤、取得基本統計數據及估算代幣數量（及成本）。搭配[OpenAI 微調指南](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst)使用。 |
| **OpenAI Cookbook**：[使用 Qdrant 的檢索增強生成（RAG）微調](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | 全面示例微調 OpenAI 模型進行 RAG，整合 Qdrant 與少量示例學習以提高性能並減少錯誤。 |
| **OpenAI Cookbook**：[使用 Weights & Biases 微調 GPT](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | 使用 W&B 追蹤模型訓練與微調。先閱讀其[OpenAI 微調](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst)指南，再試用 Cookbook 練習。 |
| **Hugging Face 教學**：[如何使用 Hugging Face TRL 微調大型語言模型](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | 使用 Hugging Face TRL、Transformers 和 datasets 微調開源大型語言模型：定義用例、設置開發環境、準備資料集、微調、評估與部署。 |
| **Hugging Face**：[AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | Hugging Face 提供的無代碼 / 低代碼微調庫。可在您的雲端、Hugging Face Spaces 或本地以 GUI、CLI 或 YAML 配置執行。 |
| **Unsloth**：[大型語言模型微調指南](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | 一個開源框架，簡化本地大型語言模型的微調與強化學習，並提供即用型[筆記本](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst)。 |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->