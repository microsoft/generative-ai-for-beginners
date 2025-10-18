<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2a83aac52158c23161046cbd13faa2b",
  "translation_date": "2025-10-17T22:35:28+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "en"
}
-->
[![Open Source Models](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.en.png)](https://youtu.be/CuICgfuHFSg?si=x8SpFRUsIxM9dohN)

## Introduction

The world of open-source LLMs is fascinating and constantly evolving. This lesson aims to provide a detailed overview of open source models. If you're looking for information on how proprietary models compare to open source models, visit the ["Exploring and Comparing Different LLMs" lesson](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). This lesson will also touch on the topic of fine-tuning, but for a more comprehensive explanation, refer to the ["Fine-Tuning LLMs" lesson](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Learning goals

- Understand open source models
- Learn the advantages of working with open source models
- Explore open models available on Hugging Face and Azure AI Studio

## What are Open Source Models?

Open source software has been instrumental in advancing technology across various domains. The Open Source Initiative (OSI) has outlined [10 criteria for software](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) to qualify as open source. The source code must be shared openly under an OSI-approved license.

While developing LLMs shares similarities with software development, the processes are not identical. This has sparked discussions within the community about the definition of open source in the context of LLMs. For a model to meet the traditional definition of open source, the following information should be publicly accessible:

- Datasets used for training the model.
- Complete model weights as part of the training.
- Evaluation code.
- Fine-tuning code.
- Full model weights and training metrics.

Currently, only a few models meet these criteria. The [OLMo model created by Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) is one such example.

For this lesson, we will refer to these models as "open models" moving forward, as they may not fully meet the criteria above at the time of writing.

## Benefits of Open Models

**Highly Customizable** - Open models are released with detailed training information, allowing researchers and developers to modify the model's internals. This enables the creation of highly specialized models tailored to specific tasks or fields of study, such as code generation, mathematical operations, and biology.

**Cost** - The cost per token for using and deploying these models is lower compared to proprietary models. When building Generative AI applications, it's important to evaluate performance versus cost for your specific use case.

![Model Cost](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.en.png)  
Source: Artificial Analysis

**Flexibility** - Open models offer flexibility in using different models or combining them. For example, [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst) allow users to select the model directly within the user interface:

![Choose Model](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.en.png)

## Exploring Different Open Models

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), developed by Meta, is an open model optimized for chat-based applications. Its fine-tuning process involved extensive dialogue and human feedback, enabling the model to produce results that align better with human expectations, enhancing the user experience.

Examples of fine-tuned versions of Llama include [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), which specializes in Japanese, and [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), an enhanced version of the base model.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) is an open model focused on high performance and efficiency. It employs the Mixture-of-Experts approach, combining specialized expert models into one system. Depending on the input, specific models are selected, making computation more efficient as models only address inputs they specialize in.

Examples of fine-tuned versions of Mistral include [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), which focuses on the medical domain, and [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), which specializes in mathematical computation.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) is an LLM developed by the Technology Innovation Institute (**TII**). The Falcon-40B was trained on 40 billion parameters and has demonstrated better performance than GPT-3 with a lower compute budget. This is achieved through the FlashAttention algorithm and multi-query attention, which reduce memory requirements during inference. With its reduced inference time, Falcon-40B is well-suited for chat applications.

Examples of fine-tuned versions of Falcon include [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), an assistant built on open models, and [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), which delivers higher performance than the base model.

## How to Choose

There is no single answer for choosing an open model. A good starting point is using Azure AI Studio's filter by task feature, which helps identify the types of tasks a model has been trained for. Hugging Face also maintains an LLM Leaderboard that highlights the best-performing models based on specific metrics.

For comparing LLMs across different types, [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) is another excellent resource:

![Model Quality](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.en.png)  
Source: Artificial Analysis

If you're working on a specific use case, searching for fine-tuned versions focused on the same area can be effective. Experimenting with multiple open models to evaluate their performance against your and your users' expectations is also a good practice.

## Next Steps

The great thing about open models is that you can start working with them quickly. Explore the [Azure AI Foundry Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), which includes a dedicated Hugging Face collection featuring the models discussed here.

## Learning does not stop here, continue the Journey

After completing this lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue enhancing your Generative AI knowledge!

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.