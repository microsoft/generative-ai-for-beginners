# 自学资源

本课程参考了 OpenAI 和 Microsoft Foundry 的核心资源，用于术语和教程。以下是非完整的资源列表，供您自学使用。下面的每个链接都指向当前支持的材料。

## 1. 主要资源

| 标题/链接 | 描述 |
| :--- | :--- |
| [使用 OpenAI 模型进行微调](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | 微调通过训练比提示中能容纳的更多样本，提升少量示例学习的效果——节省成本，提升响应质量，并实现更低延迟的请求。**了解 OpenAI 的微调概述。** |
| [何时使用 Microsoft Foundry 微调](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | 理解<strong>什么是微调（概念）</strong>，为什么要考虑微调，使用哪些数据，以及如何衡量质量——并了解何时适合使用 SFT、DPO 或 RFT。 |
| [使用微调自定义模型](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | Microsoft Foundry 中微调的端到端<strong>操作流程（流程）</strong>，涵盖使用门户、OpenAI / Foundry Python SDK 或 REST API 进行数据准备、训练、检查点和部署。 |
| [持续微调](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | 选取已微调模型作为基础模型，并在新训练样本上<strong>进一步微调</strong>的迭代过程。 |
| [带工具（函数）调用的微调](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | 使用<strong>带工具调用示例</strong>微调模型，提升输出——生成更准确、一致、格式相似的响应，并使用更少的提示令牌。 |
| [微调模型：Microsoft Foundry 指南](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | 查询<strong>哪些模型可微调</strong>，它们支持的方法（SFT / DPO / RFT）及其可用区域。 |
| [微调概述：技术和模式](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | 对比三种训练技术（SFT、DPO、RFT）和两种模式（无服务器与托管计算），提供选择基础模型和入门指导。 |
| <strong>教程</strong>: [在 Microsoft Foundry 中微调模型](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | 创建示例数据集，准备微调，在当前支持的模型如 `gpt-4.1-mini` 上运行微调任务，并在 Azure 上部署微调模型。 |
| <strong>教程</strong>: [通过无服务器 API 部署微调模型](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | 使用 Microsoft Foundry 中的低代码、基于 UI 的工作流，为开源和合作伙伴模型（Phi、Llama、Mistral 等）定制数据集。 |
| <strong>教程</strong>: [在 Azure Databricks 上微调 Hugging Face 模型](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | 使用 `transformers` 库、Azure Databricks 和 Hugging Face Trainer，在单个 GPU 上微调 Hugging Face 模型。 |
| <strong>培训</strong>: [使用 Azure 机器学习微调基础模型](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | Azure 机器学习模型目录提供多种开源模型供微调。是 [Azure ML 生成式 AI 学习路径](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) 的一部分。 |
| <strong>教程</strong>: [使用 Weights & Biases 进行 Azure OpenAI 微调](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | 使用 W&B 在 Azure 上跟踪和分析微调运行。扩展了 OpenAI 微调指南，增加 Azure 相关步骤和实验追踪。 |

## 2. 次要资源

本节收录了我们课程中未能覆盖但值得探索的额外资源。利用它们构建您在该主题上的专业知识。

| 标题/链接 | 描述 |
| :--- | :--- |
| **OpenAI Cookbook**: [聊天模型微调的数据准备和分析](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | 微调前对聊天数据集进行预处理和分析：检查格式错误，获取基本统计信息，估计令牌数量（及成本）。配合[OpenAI 微调指南](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst)使用。 |
| **OpenAI Cookbook**: [结合 Qdrant 的检索增强生成（RAG）微调](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | 详尽示例，微调 OpenAI 模型用于 RAG，集成 Qdrant 和少量示例学习以提升性能并减少虚构内容。 |
| **OpenAI Cookbook**: [使用 Weights & Biases 微调 GPT](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | 使用 W&B 跟踪模型训练和微调。先阅读它们的[OpenAI 微调指南](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst)，再尝试 Cookbook 练习。 |
| **Hugging Face 教程**: [如何使用 Hugging Face TRL 微调大语言模型](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | 使用 Hugging Face TRL、Transformers 和数据集进行开源大语言模型微调：定义用例，搭建开发环境，准备数据集，微调，评估和部署。 |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | Hugging Face 出品的无代码/低代码库，用于微调多种模型类型。可在自己的云端、Hugging Face Spaces 或本地通过 GUI、CLI 或 YAML 配置运行。 |
| **Unsloth**: [微调大语言模型指南](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | 一个开源框架，简化本地大语言模型微调和强化学习，附带现成[笔记本](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst)。 |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->