# Resources For Self-Guided Learning

Di lesson dem build am wit core resources from OpenAI an Microsoft Foundry as reference for di terminology an tutorials. Dis na one non-exhaustive list for una own self-guided learning journey dem. Every link wey dey below dey point to beta, supported material.

## 1. Primary Resources

| Title/Link | Description |
| :--- | :--- |
| [Fine-tuning with OpenAI Models](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | Fine-tuning dey improve few-shot learning by training for more examples pass wetin fit for di prompt - e dey save cost, better response quality, and e allow faster requests. **Get one overview of fine-tuning from OpenAI.** |
| [When to use Microsoft Foundry fine-tuning](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | Understand **wetin fine-tuning be (concept)**, why you suppose consider am, as you go take choose data, an how to measure quality - plus when SFT, DPO, or RFT na correct fit for you. |
| [Customize a model with fine-tuning](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | Di end-to-end **how-to (process)** for fine-tuning inside Microsoft Foundry use di portal, di OpenAI / Foundry Python SDK, or di REST API - e show how to prepare data, train, checkpoints, and how to deploy am. |
| [Continuous fine-tuning](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | Di iterative process wey dem dey select already fine-tuned model as base model an **fine-tune am more** on new sets of training examples. |
| [Fine-tuning with tool (function) calling](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | Fine-tuning your model **wit examples wey dey call tools** dey improve output - e dey make am dey more accurate, consistent, an responses wey resemble each oda for format with less tokens for prompt. |
| [Fine-tuning models: Microsoft Foundry guidance](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | Check **which models wey fit do fine-tuning**, di methods dem support (SFT / DPO / RFT), an di regions wey dem dey available. |
| [Fine-tuning overview: techniques and modalities](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | Compare di three training techniques (SFT, DPO, RFT) an di two modalities (serverless vs. managed compute), plus guidance on how to choose base model an how to start. |
| **Tutorial**: [Fine-tune a model in Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Create sample dataset, prepare for fine-tuning, run fine-tuning job on model wey current dey supported like `gpt-4.1-mini`, an deploy di fine-tuned model for Azure. |
| **Tutorial**: [Fine-tune models with serverless API deployments](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | Customize open an partner models (Phi, Llama, Mistral, an more) to your datasets _wit low-code, UI-based workflow_ inside Microsoft Foundry. |
| **Tutorial**: [Fine-tune Hugging Face models on Azure Databricks](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | Fine-tune Hugging Face model wit `transformers` library on single GPU use Azure Databricks an Hugging Face Trainer. |
| **Training**: [Fine-tune a foundation model with Azure Machine Learning](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | Azure Machine Learning model catalog get plenti open-source models wey you fit fine-tune. E part of di [Azure ML Generative AI Learning Path](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst). |
| **Tutorial**: [Azure OpenAI fine-tuning with Weights & Biases](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | Track an analyze fine-tuning runs for Azure wit W&B. E extend OpenAI fine-tuning guide wit Azure-specific steps an experiment tracking. |

## 2. Secondary Resources

Dis section capture extra resources wey worth to explore, but we no get time to cover for di lesson. Use dem to build your own expertise about dis kain topic.

| Title/Link | Description |
| :--- | :--- |
| **OpenAI Cookbook**: [Data preparation and analysis for chat model fine-tuning](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | Preprocess an analyze chat dataset before fine-tuning: check for format errors, get basic statistics, an estimate token counts (an cost). Pairs wit di [OpenAI fine-tuning guide](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst). |
| **OpenAI Cookbook**: [Fine-tuning for Retrieval Augmented Generation (RAG) with Qdrant](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | Comprehensive example of fine-tuning OpenAI models for RAG, wey dey combine Qdrant an few-shot learning to improve performance an reduce fabrications. |
| **OpenAI Cookbook**: [Fine-tuning GPT with Weights & Biases](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | Use W&B to track model training an fine-tuning. Read dia [OpenAI Fine-Tuning](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst) guide first, den try di Cookbook exercise. |
| **Hugging Face Tutorial**: [How to Fine-Tune LLMs with Hugging Face TRL](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | Fine-tune open LLMs wit Hugging Face TRL, Transformers, an datasets: define use case, set up dev environment, prepare dataset, fine-tune, evaluate, an deploy. |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | No-code / low-code library from Hugging Face for fine-tuning many model types. Run am for your own cloud, on Hugging Face Spaces, or locally wit GUI, CLI, or YAML config. |
| **Unsloth**: [Fine-tuning LLMs Guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | Open-source framework wey dey make local LLM fine-tuning an reinforcement learning easy, wit ready-to-use [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->