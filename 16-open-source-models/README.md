## Introduction

The world of open-source LLMs is exciting and constantly evolving. This lesson aims to provide an in-depth look at open source models. If you are looking for information on how proprietary models compare to open source models, go to the ["Exploring and Comparing Different LLMs" lesson](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). This lesson will also cover the topic of fine-tuning but a more detailed explanation can be found in the ["Fine-Tuning LLMs" lesson](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Learning goals

- Gain an understanding of open source Models
- Understanding the benefits of working with open source Models
- Exploring the open models available on Hugging Face and the Azure AI Studio

## What are Open Source Models?

Open source software has played a crucial role in the growth of technology across various fields.The Open Source Initiative (OSI) has defined [10 criteria for software](https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) to be classified as open source. The source code must be openly shared under a license approved by the OSI.

While the development of LLMs has similar elements to developing software, the process is not exactly the same. This has brought much discussion in the community on the definition of open source in the context of LLMs. For a model to be aligned with the traditional definition of open source the following information should be publicly available:

- Datasets used to train the model.
- Full model weights as a part of the training.
- The evaluation code.
- The fine-tuning code.
- Full model weights and training metrics.

There are currently only a few models that match this criteria. The [OLMo model created by Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) is one that fits this category.

For this lesson, we will refer to the models as "open models" going forward as they may not match the criteria above at the time of writing.

## Benefits of Open Models

**Highly Customizable** - Since open models are released with detailed training information, researchers and developers can modify the model's internals. This enables the creation of highly specialized models that are fine-tuned for a specific task or area of study. Some examples of this is code generation, mathematical operations and biology.

**Cost** - The cost per token for using and deploying these models is lower than that of proprietary models. When building Generative AI applications, looking at performance vs price when working with these models on your use case should be done.

![Model Cost](./images/model-price.png?WT.mc_id=academic-105485-koreyst)
Source: Artifical Anayslsis

**Flexibility** - Working with open models enables you do be flexible on in terms of using different models or combining them. An example of this is the [HuggingChat Assistants ](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst) where a users can select the model being used directly in the user interface:

![Choose Model](./images/choose-model.png?WT.mc_id=academic-105485-koreyst)

## Exploring Different Open Models

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), developed by Meta is an open model that is optimized for chat based applications. This is due to its fine-tuning method, which included a large amount of dialogue and human feedback.. With this method, the model produces more results that are aligned to human expectation which provides a better user experience.

Some examples of fine-tuned versions of Llama include [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), which specializes in Japanese and [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), which is an enhanced version of the base model.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst)is an open model with a strong focus of high performance and efficiency. It uses the Mixture-of-Experts approach which combines a group of specialized expert models into one system where depending on the input, certain models are selected to be used. This makes the computation more effective as models are only addressing the inputs they are specalized in.

Some examples of fine-tuned versions of Mistral include [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), which is focused on the medical domain and [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), which performs mathematical computation.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) is an LLM created by the Technology Innovation Institute (**TII**) .The Falcon-40B was trained on 40 billion parameters which has been shown to perform better than GPT-3 with less compute budget. This is dues to its use of the FlashAttention algorirth and multiquery attention that enables it to cut down on the memory requirements at inference time. With this reduced inference time, the Falcon-40B is suitable for chat applications.

Some examples of fine-tuned versions of Falcon are the [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), an assistant built on open models and [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), which delivers higher performance than the base model.

## How to Choose

There is no one answer for choosing an open model. A good place to start is by using the Azure AI Studio's filter by task feature. This will help you understand what types of tasks the model has been trained for. Hugging Face also maintains an LLM Leaderboard which shows you the best performing models base on certain metrics.

When looking to compare LLMs across the different types, [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) is another great resource:

![Model Quality](./images/model-quality.png?WT.mc_id=academic-105485-koreyst)
Source: Artifical Analysis

If working on a specific use case, searching for fine-tuned versions that are focused on the same area can be effective. Experimenting with multiple open models to see how they perform according to your and your users' expectations is another good practice

## Next Steps

The best part about open models is that you can get started working with them pretty quickly. Check out the [Azure AI Studio Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) , which features a specific Hugging Face collection with these models we discussed here.

## Learning does not stop here, continue the Journey

After completing this lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue leveling up your Generative AI knowledge!
