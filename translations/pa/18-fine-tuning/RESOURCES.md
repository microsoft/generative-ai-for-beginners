# ਸਵੈ-ਨਿਰਦੇਸ਼ਿਤ ਸਿੱਖਣ ਲਈ ਸਰੋਤ

ਇਸ ਪਾਠ ਨੂੰ OpenAI ਅਤੇ Microsoft Foundry ਦੇ ਮੁੱਖ ਸਰੋਤਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਤਿਆਰ ਕੀਤਾ ਗਿਆ ਸੀ ਜੋ ਪਦਾਵਲੀ ਅਤੇ ਟਿਊਟੋਰਿਯਲ ਲਈ ਰਹੇ। ਤੁਹਾਡੇ ਆਪਣੇ ਸਵੈ-ਨਿਰਦੇਸ਼ਿਤ ਸਿੱਖਣ ਯਾਤਰਾ ਲਈ ਇਹ ਇਕ ਅਧੂਰਾ ਸੂਚੀ ਹੈ। ਹੇਠਾਂ ਦਿੱਤੇ ਹਰ ਲਿੰਕ ਮੌਜੂਦਾ ਅਤੇ ਸਮਰਥਿਤ ਸਮੱਗਰੀ ਵੱਲ ਸੰਕੇਤ ਕਰਦੇ ਹਨ।

## 1. ਪ੍ਰਮੁੱਖ ਸਰੋਤ

| ਸਿਰਲੇਖ/ਲਿੰਕ | ਵੇਰਵਾ |
| :--- | :--- |
| [OpenAI ਮਾਡਲਾਂ ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) | ਫਾਈਨ-ਟਿਊਨਿੰਗ ਕੁਝ ਉਦਾਹਰਣਾਂ ਦੀ ਸਿੱਖਣ ਉੱਤੇ ਸੁਧਾਰ ਕਰਦਾ ਹੈ ਜਿਵੇਂ ਕਿ ਪ੍ਰੰਪਟ ਵਿੱਚ ਆ ਸਕਣ ਵਾਲੀਆਂ ਉਦਾਹਰਣਾਂ ਨਾਲੋਂ ਬਹੁਤ ਜ਼ਿਆਦਾ ਉਦਾਹਰਣਾਂ 'ਤੇ ਟ੍ਰੇਨਿੰਗ ਕਰ ਕੇ - ਲਾਗਤਾਂ ਬਚਾਉਂਦਾ ਹੈ, ਪ੍ਰਤਿਕ੍ਰਿਆ ਦੀ ਗੁਣਵੱਤਾ ਵਿੱਚ ਸੁਧਾਰ ਕਰਦਾ ਹੈ, ਅਤੇ ਘੱਟ-ਦੇਰੀ ਵਾਲੀਆਂ ਬੇਨਤੀਆਂ ਸਮਰਥਿਤ ਕਰਦਾ ਹੈ। **OpenAI ਤੋਂ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਦਾ ਵੇਰਵਾ ਪ੍ਰਾਪਤ ਕਰੋ।** |
| [Microsoft Foundry ਫਾਈਨ-ਟਿਊਨਿੰਗ ਨੂੰ ਕਦੋਂ ਵਰਤਣਾ](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/fine-tuning-considerations?WT.mc_id=academic-105485-koreyst) | ਜਾਣੋ ਕਿ **ਫਾਈਨ-ਟਿਊਨਿੰਗ ਕੀ ਹੈ (ਸੰਕਲਪ)**, ਇਹ ਕਿਉਂ ਲਾਗੂ ਕਰਨੀ ਚਾਹੀਦੀ ਹੈ, ਕਿਹੜਾ ਡੇਟਾ ਵਰਤਣਾ ਹੈ, ਅਤੇ ਕਿਵੇਂ ਗੁਣਵੱਤਾ ਮਾਪਣੀ ਹੈ - ਨਾਲ ਹੀ ਕਦੋਂ SFT, DPO, ਜਾਂ RFT ਸਹੀ ਚੋਣ ਹੈ। |
| [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਨਾਲ ਮਾਡਲ ਕਸਟਮਾਈਜ਼ ਕਰੋ](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst) | Microsoft Foundry ਵਿੱਚ ਪੋਰਟਲ, OpenAI / Foundry Python SDK, ਜਾਂ REST API ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਦੀ ਸਮੁੱਚੀਕ੍ਰਿਤ **ਟਿੱਪਣੀ (ਪ੍ਰਕਿਰਿਆ)** - ਡੇਟਾ ਤਿਆਰੀ, ਟ੍ਰੇਨਿੰਗ, ਚੈਕਪਾਇੰਟ, ਅਤੇ ਡਿਪਲੋਯਮੈਂਟ ਸਮੇਤ। |
| [ਨਿਰੰਤਰ ਫਾਈਨ-ਟਿਊਨਿੰਗ](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst#perform-continuous-fine-tuning) | ਪਹਿਲਾਂ ਹੀ ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ ਮਾਡਲ ਨੂੰ ਬੇਸ ਮਾਡਲ ਵਜੋਂ ਚੁਣ ਕੇ ਅਤੇ ਨਵੀਆਂ ਪ੍ਰਸ਼ਿਸ਼ਣ ਉਦਾਹਰਣਾਂ 'ਤੇ ਇਸਨੂੰ ਹੋਰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨ ਦੀ ਪੁਨਰਾਵਰਤੀ ਪ੍ਰਕਿਰਿਆ। |
| [ਟੂਲ (ਫੰਕਸ਼ਨ) ਕਾਲਿੰਗ ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-functions?WT.mc_id=academic-105485-koreyst) | ਤੁਹਾਡੇ ਮਾਡਲ ਨੂੰ **ਟੂਲ-ਕਾਲਿੰਗ ਦੇ ਉਦਾਹਰਣਾਂ ਨਾਲ** ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ ਉਹਦੇ ਆਉਟਪੁਟ ਨੂੰ ਸੁਧਾਰਦਾ ਹੈ - ਹੋਰ ਸਹੀ, ਲਗਾਤਾਰ ਅਤੇ ਸਮਾਨ-ਸੰਰਚਿਤ ਜਵਾਬ ਜੋ ਘੱਟ ਪ੍ਰੰਪਟ ਟੋਕਨ ਵਰਤਦੇ ਹਨ। |
| [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਮਾਡਲ: Microsoft Foundry ਗਾਈਡਲਾਈਨ](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) | ਵੇਖੋ **ਕਿਹੜੇ ਮਾਡਲ ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ**, ਉਹਨਾਂ ਦੇ ਸਮਰਥਿਤ ਤਰੀਕੇ (SFT / DPO / RFT), ਅਤੇ ਉਨ੍ਹਾਂ ਦੇ ਉਪਲਬਧ ਖੇਤਰ। |
| [ਫਾਈਨ-ਟਿਊਨਿੰਗ ਦਾ ਸਰਵੇਖਣ: ਤਕਨੀਕਾਂ ਅਤੇ ਮੋਡੈਲਿਟੀਜ਼](https://learn.microsoft.com/azure/ai-foundry/concepts/fine-tuning-overview?WT.mc_id=academic-105485-koreyst) | ਤਿੰਨ ਟ੍ਰੇਨਿੰਗ ਤਕਨੀਕਾਂ (SFT, DPO, RFT) ਅਤੇ ਦੋ ਮੋਡੈਲਿਟੀਜ਼ (ਸਰਵਰਲੇਸ ਵర్సਸ ਪ੍ਰਬੰਧਤ ਕਮਪਿਊਟ) ਦੀ ਤੁਲਨਾ ਕਰੋ, ਬੇਸ ਮਾਡਲ ਚੁਣਨ ਅਤੇ ਸ਼ੁਰੂ ਕਰਨ ਲਈ ਮਦਦ ਨਾਲ। |
| **ਟਿਊਟੋਰੀਅਲ**: [Microsoft Foundry ਵਿੱਚ ਮਾਡਲ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰੋ](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | ਇੱਕ ਨਮੂਨਾ ਡੇਟਾਸੈੱਟ ਬਣਾਓ, ਫਾਈਨ-ਟਿਊਨਿੰਗ ਲਈ ਤਿਆਰੀ ਕਰੋ, ਮੌਜੂਦਾ ਸਮਰਥਿਤ ਮਾਡਲ ਜਿਵੇਂ ਕਿ `gpt-4.1-mini` 'ਤੇ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਜਾਬ ਚਲਾਓ, ਅਤੇ Azure 'ਤੇ ਫਾਈਨ-ਟਿਊਨ ਕੀਤਾ ਮਾਡਲ ਡਿਪਲੋਯ ਕਰੋ। |
| **ਟਿਊਟੋਰੀਅਲ**: [ਸਰਵਰਲੇਸ API ਡਿਪਲੋਯਮੈਂਟ ਨਾਲ ਮਾਡਲ ਫਾਈਨ-ਟਿਊਨ ਕਰੋ](https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-serverless?WT.mc_id=academic-105485-koreyst) | ਖੁੱਲ੍ਹੇ ਅਤੇ ਸਾਥੀ ਮਾਡਲਜ਼ (Phi, Llama, Mistral, ਅਤੇ ਹੋਰ) ਨੂੰ ਤੁਹਾਡੇ ਡੇਟਾਸੈੱਟਾਂ ਦੇ ਅਨੁਕੂਲ ਬਨਾਓ _Microsoft Foundry ਵਿੱਚ ਇਕ ਨੀਵ-ਕੋਡ, UI-ਅਧਾਰਿਤ ਵਰਕਫ਼ਲੋ ਦੀ ਵਰਤੋਂ ਕਰਕੇ।_ |
| **ਟਿਊਟੋਰੀਅਲ**: [Azure Databricks 'ਤੇ Hugging Face ਮਾਡਲ ਫਾਈਨ-ਟਿਊਨ ਕਰੋ](https://learn.microsoft.com/azure/databricks/machine-learning/train-model/huggingface/fine-tune-model?WT.mc_id=academic-105485-koreyst) | Azure Databricks ਅਤੇ Hugging Face Trainer ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਸਿੰਗਲ GPU 'ਤੇ `transformers` ਲਾਇਬ੍ਰੇਰੀ ਨਾਲ Hugging Face ਮਾਡਲ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰੋ। |
| **ਟ੍ਰੇਨਿੰਗ**: [Azure Machine Learning ਨਾਲ ਫੰਡੇਸ਼ਨ ਮਾਡਲ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰੋ](https://learn.microsoft.com/training/modules/finetune-foundation-model-with-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) | Azure Machine Learning ਮਾਡਲ ਕੈਟਾਲਾਗ ਵਿੱਚ ਕਈ ਖੁੱਲ੍ਹੇ ਸਰੋਤ ਵਾਲੇ ਮਾਡਲ ਹਨ ਜੋ ਤੁਸੀਂ ਫਾਈਨ-ਟਿਊਨ ਕਰ ਸਕਦੇ ਹੋ। [Azure ML Generative AI Learning Path](https://learn.microsoft.com/training/paths/work-with-generative-models-azure-machine-learning/?WT.mc_id=academic-105485-koreyst) ਦਾ ਹਿੱਸਾ। |
| **ਟਿਊਟੋਰੀਅਲ**: [Weights & Biases ਨਾਲ Azure OpenAI ਫਾਈਨ-ਟਿਊਨਿੰਗ](https://docs.wandb.ai/guides/integrations/azure-openai-fine-tuning?WT.mc_id=academic-105485-koreyst) | W&B ਨਾਲ Azure 'ਤੇ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਦੌੜਾਂ ਨੂੰ ਟ੍ਰੈਕ ਅਤੇ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰੋ। OpenAI ਫਾਈਨ-ਟਿਊਨਿੰਗ ਗਾਈਡ ਨੂੰ Azure-ਵਿਸ਼ੇਸ਼ ਕਦਮਾਂ ਅਤੇ ਪ੍ਰਯੋਗ ਟ੍ਰੈਕਿੰਗ ਨਾਲ ਵਧਾਉਂਦਾ ਹੈ। |

## 2. ਮਾਧਮਿਕ ਸਰੋਤ

ਇਸ ਭਾਗ ਵਿੱਚ ਹੋਰ ਵਧੀਆ ਸਰੋਤ ਸ਼ਾਮਲ ਕੀਤੇ ਗਏ ਹਨ ਜਿਨ੍ਹਾਂ ਨੂੰ ਸਿੱਖਣ ਲਈ ਸੀਮਤ ਸਮੇਂ ਵਿੱਚ ਕਵਰ ਨਹੀਂ ਕੀਤਾ ਗਿਆ। ਇਨ੍ਹਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਸ ਵਿਸ਼ੇ 'ਤੇ ਆਪਣੀ ਮਾਹਰਤਾ ਬਣਾਓ।

| ਸਿਰਲੇਖ/ਲਿੰਕ | ਵੇਰਵਾ |
| :--- | :--- |
| **OpenAI ਕੂਕਬੁੱਕ**: [ਚੈਟ ਮਾਡਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਲਈ ਡੇਟਾ ਤਿਆਰੀ ਅਤੇ ਵਿਸ਼ਲੇਸ਼ਣ](https://cookbook.openai.com/examples/chat_finetuning_data_prep?WT.mc_id=academic-105485-koreyst) | ਫਾਈਨ-ਟਿਊਨਿੰਗ ਤੋਂ ਪਹਿਲਾਂ ਇੱਕ ਚੈਟ ਡੇਟਾਸੈੱਟ ਨੂੰ ਪ੍ਰੀ-ਪ੍ਰੋਸੈਸ ਅਤੇ ਵਿਸ਼ਲੇਸ਼ਣ ਕਰੋ: ਫਾਰਮੈਟ ਦੀਆਂ ਗਲਤੀਆਂ ਜਾਂਚੋ, ਬੁਨਿਆਦੀ ਅੰਕੜੇ ਪ੍ਰਾਪਤ ਕਰੋ, ਅਤੇ ਟੋਕਨ ਗਿਣਤੀ (ਅਤੇ ਲਾਗਤ) ਦਾ ਅੰਦਾਜ਼ਾ ਲਗਾਓ। [OpenAI ਫਾਈਨ-ਟਿਊਨਿੰਗ ਗਾਈਡ](https://platform.openai.com/docs/guides/fine-tuning?WT.mc_id=academic-105485-koreyst) ਨਾਲ ਜੁੜਿਆ। |
| **OpenAI ਕੂਕਬੁੱਕ**: [Retrieval Augmented Generation (RAG) ਲਈ Qdrant ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ](https://cookbook.openai.com/examples/fine-tuned_qa/ft_retrieval_augmented_generation_qdrant?WT.mc_id=academic-105485-koreyst) | RAG ਲਈ OpenAI ਮਾਡਲਾਂ ਦੀ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਦਾ ਇਕ ਵਿਆਪਕ ਉਦਾਹਰਣ, Qdrant ਅਤੇ ਕੁਝ ਉਦਾਹਰਣ ਸਿੱਖਣ ਦੇ ਏਕਤਾ ਨਾਲ ਪ੍ਰਦਰਸ਼ਨ ਵਧਾਉਂਦਾ ਅਤੇ ਜਾਲਸਾਜ਼ੀਆਂ ਘਟਾਉਂਦਾ। |
| **OpenAI ਕੂਕਬੁੱਕ**: [Weights & Biases ਨਾਲ GPT ਫਾਈਨ-ਟਿਊਨਿੰਗ](https://cookbook.openai.com/examples/third_party/gpt_finetuning_with_wandb?WT.mc_id=academic-105485-koreyst) | ਮਾਡਲ ਟ੍ਰੇਨਿੰਗ ਅਤੇ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਦੀ ਟ੍ਰੈਕਿੰਗ ਲਈ W&B ਦੀ ਵਰਤੋਂ ਕਰੋ। ਪਹਿਲਾਂ ਉਹਨਾਂ ਦੀ [OpenAI ਫਾਈਨ-ਟਿਊਨਿੰਗ](https://docs.wandb.ai/guides/integrations/openai-fine-tuning/?WT.mc_id=academic-105485-koreyst) ਗਾਈਡ ਪੜ੍ਹੋ, ਫਿਰ ਕੂਕਬੁੱਕ ਅਭਿਆਸ ਕਰੋ। |
| **Hugging Face ਟਿਊਟੋਰੀਅਲ**: [Hugging Face TRL ਨਾਲ LLMs ਨੂੰ ਕਿਵੇਂ ਫਾਈਨ-ਟਿਊਨ ਕਰਨਾ ਹੈ](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst) | Hugging Face TRL, Transformers, ਅਤੇ ਡੇਟਾਸੈੱਟਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਖੁੱਲ੍ਹੇ LLMs ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰੋ: ਇਕ ਕੇਸ ਨਿਰਧਾਰਿਤ ਕਰੋ, ਡੈਵ ਵਾਤਾਵਰਣ ਸੈੱਟ ਕਰੋ, ਡੇਟਾਸੈੱਟ ਤਿਆਰ ਕਰੋ, ਫਾਈਨ-ਟਿਊਨ ਕਰੋ, ਮੁਲਾਂਕਣ ਕਰੋ ਅਤੇ ਡਿਪਲੋਯ ਕਰੋ। |
| **Hugging Face**: [AutoTrain Advanced](https://github.com/huggingface/autotrain-advanced?WT.mc_id=academic-105485-koreyst) | Hugging Face ਤੋਂ ਬਿਨਾ-ਕੋਡ / ਲੋ-ਕੋਡ ਲਾਇਬ੍ਰੇਰੀ ਜੋ ਕਈ ਕਿਸਮਾਂ ਦੇ ਮਾਡਲਾਂ ਨੂੰ ਫਾਈਨ-ਟਿਊਨ ਕਰਨ ਲਈ ਹੈ। ਇਸਨੂੰ ਆਪਣੇ ਮੇਘ ਵਿੱਚ ਚਲਾਓ, Hugging Face Spaces 'ਤੇ, ਜਾਂ ਲੋਕਲ GUI, CLI ਜਾਂ YAML ਕੰਫਿਗ ਨਾਲ। |
| **Unsloth**: [LLMs ਫਾਈਨ-ਟਿਊਨਿੰਗ ਗਾਈਡ](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) | ਇਕ ਖੁੱਲ੍ਹਾ ਸਰੋਤ ਫਰੇਮਵਰਕ ਜੋ ਸਥਾਨਕ LLM ਫਾਈਨ-ਟਿਊਨਿੰਗ ਅਤੇ ਰੀਇਨਫੋਰਸਮੈਂਟ ਲਰਨਿੰਗ ਨੂੰ ਸੁਗਮ ਬਣਾਉਂਦਾ ਹੈ, ਤਿਆਰ-ਟੂ-ਯੂਜ਼ [ਨੋਟਬੁੱਕ](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) ਸਮੇਤ। |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->