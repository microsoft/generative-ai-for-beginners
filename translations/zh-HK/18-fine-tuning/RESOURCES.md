# 自學資源

本課程是以 OpenAI 和 Microsoft Foundry 的核心資源為參考，涵蓋專有名詞和教程。以下是供你自學之用的非完整資源列表。以下每個連結均指向最新且受支持的材料。

## 1. 主要資源

| 標題/連結 | 描述 |
| :--- | :--- |
| [使用 OpenAI 模型微調](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | 微調通過訓練遠多於提示中可容納範例的數據來改進少量示例學習，節省成本、提升回應質量，並實現更低延遲的請求。**從 OpenAI 獲取微調概述。** |
| [何時使用 Microsoft Foundry 微調](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | 了解<strong>什麼是微調（概念）</strong>、為何應考慮微調、使用哪些數據以及如何衡量質量 —— 以及何時適合使用 SFT、DPO 或 RFT。 |
| [使用微調自訂模型](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | 在 Microsoft Foundry 中使用門戶、OpenAI / Foundry Python SDK 或 REST API 進行微調的端到端<strong>操作流程</strong> —— 涵蓋數據準備、訓練、檢查點和部署。 |
| [持續微調](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | 選擇已微調模型作為基礎模型，並在新訓練範例集上進行<strong>進一步微調</strong>的迭代過程。 |
| [使用工具（函數）調用微調](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | 用帶有工具調用示例的微調改善模型輸出 —— 使回應更準確、一致、格式相似，且使用更少的提示字元。 |
| [微調模型：Microsoft Foundry 指南](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | 查閱<strong>可微調的模型</strong>、支持的方法（SFT / DPO / RFT）、以及可用的地區。 |
| [微調概述：技術與模式](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | 比較三種訓練技術（SFT、DPO、RFT）與兩種模式（無伺服器與管理式計算），並提供選擇基礎模型及入門指導。 |
| <strong>教程</strong>：[在 Microsoft Foundry 中微調模型](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | 建立示例數據集，準備微調，對目前支援的模型如 `gpt-4.1-mini` 進行微調作業，並在 Azure 上部署微調模型。 |
| <strong>教程</strong>：[使用無伺服器 API 部署微調模型](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | 在 Microsoft Foundry 使用低程式碼的 UI 工作流程，根據你的數據集定制開源和合作夥伴模型（Phi、Llama、Mistral 等）。 |
| <strong>教程</strong>：[在 Azure Databricks 上微調 Hugging Face 模型](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | 使用 `transformers` 庫，在單 GPU 上通過 Azure Databricks 和 Hugging Face Trainer 微調 Hugging Face 模型。 |
| <strong>訓練</strong>：[使用 Azure 機器學習微調基礎模型](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | Azure 機器學習模型目錄提供多款可微調的開源模型。此為 [Azure ML 生成式 AI 學習路徑](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) 的一部分。 |
| <strong>教程</strong>：[使用 Weights & Biases 進行 Azure OpenAI 微調](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | 使用 W&B 跟蹤並分析在 Azure 上的微調執行情況。擴展 OpenAI 微調指南，包含 Azure 特定步驟與實驗追踪。 |

## 2. 次要資源

本節收錄了我們課程中未及涵蓋的其他值得探索的資源，用於建立你在該主題的專業知識。

| 標題/連結 | 描述 |
| :--- | :--- |
| **OpenAI Cookbook**: [聊天模型微調的數據準備與分析](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | 微調前對聊天數據集進行預處理與分析：檢查格式錯誤、基本統計、估算字元數（及成本）。搭配[OpenAI 微調指南](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst)使用。 |
| **OpenAI Cookbook**: [使用 Qdrant 進行檢索增強生成（RAG）的微調](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | 微調 OpenAI 模型以做檢索增強生成的綜合範例，整合 Qdrant 和少量示例學習，提高表現並降低捏造資訊。 |
| **OpenAI Cookbook**: [使用 Weights & Biases 微調 GPT](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | 使用 W&B 追蹤模型訓練與微調。先閱讀他們的[OpenAI 微調指南](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst)，然後嘗試 Cookbook 練習。 |
| **Hugging Face 教程**: [如何用 Hugging Face TRL 微調 LLM](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | 使用 Hugging Face TRL、Transformers 與數據集微調開源 LLM：定義用例、設置開發環境、準備數據集、微調、評估和部署。 |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | Hugging Face 提供的無碼/低碼微調多種模型類型的庫。可在個人雲端、Hugging Face Spaces 或本地透過 GUI、CLI 或 YAML 配置運行。 |
| **Unsloth**: [微調 LLM 指南](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | 一個開源框架，簡化本地 LLM 微調和強化學習，附有可用的[筆記本](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst)。 |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->