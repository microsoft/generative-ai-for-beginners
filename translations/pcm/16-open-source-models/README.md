<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85b754d4dc980f270f264d17116d9a5f",
  "translation_date": "2025-12-19T18:13:11+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "pcm"
}
-->
[![Open Source Models](../../../translated_images/16-lesson-banner.6b56555e8404fda1.pcm.png)](https://youtu.be/CuICgfuHFSg?si=x8SpFRUsIxM9dohN)

## Introduction

Di world of open-source LLMs dey exciting and e dey always dey change. Dis lesson wan give una deep look inside open source models. If you dey find info on how proprietary models take compare to open source models, waka go di ["Exploring and Comparing Different LLMs" lesson](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Dis lesson go also talk about fine-tuning but if you want beta explanation, you fit find am for di ["Fine-Tuning LLMs" lesson](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Learning goals

- Make you sabi open source Models well well
- Understand di benefits wey dey work with open source Models
- Explore di open models wey dey for Hugging Face and di Azure AI Studio

## Wetin be Open Source Models?

Open source software don play big role for di growth of technology for different areas. Di Open Source Initiative (OSI) don define [10 criteria for software](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) wey make am open source. Di source code suppose dey openly shared under license wey OSI approve.

Even though di way dem dey develop LLMs get some tins wey resemble software development, di process no be exactly di same. Dis one don cause plenty talk for di community about wetin open source mean for LLMs. For model to follow di traditional open source definition, dis info suppose dey public:

- Datasets wey dem use train di model.
- Full model weights as part of di training.
- Di evaluation code.
- Di fine-tuning code.
- Full model weights and training metrics.

Right now, only small models dey wey fit dis criteria. Di [OLMo model wey Allen Institute for Artificial Intelligence (AllenAI) create](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) na one wey fit dis category.

For dis lesson, we go dey call di models "open models" as dem fit no too match di criteria well well as we dey write dis.

## Benefits of Open Models

**Highly Customizable** - Because open models dey come with detailed training info, researchers and developers fit change di inside parts of di model. Dis one fit make dem create models wey dey very specialized and fine-tuned for one particular work or study area. Some examples na code generation, mathematical operations and biology.

**Cost** - Di cost per token to use and deploy dis models dey cheaper pass proprietary models. When you dey build Generative AI apps, you suppose check performance vs price when you dey use dis models for your own use case.

![Model Cost](../../../translated_images/model-price.3f5a3e4d32ae00b4.pcm.png)
Source: Artificial Analysis

**Flexibility** - To work with open models go give you chance to dey flexible to use different models or join dem together. One example na di [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst) wey user fit choose di model wey dem wan use directly for di user interface:

![Choose Model](../../../translated_images/choose-model.f095d15bbac92214.pcm.png)

## Exploring Different Open Models

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), wey Meta develop, na open model wey dem optimize for chat-based apps. Dis one na because of di fine-tuning method wey dem use, wey get plenty dialogue and human feedback. With dis method, di model dey give results wey match human expectation well well, wey dey give better user experience.

Some fine-tuned versions of Llama na [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), wey specialize for Japanese and [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), wey be beta version of di base model.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) na open model wey focus well well on high performance and efficiency. E dey use Mixture-of-Experts approach wey join group of specialized expert models into one system, so depending on di input, certain models go dey selected to use. Dis one dey make computation more effective as models dey only handle di inputs wey dem sabi well.

Some fine-tuned versions of Mistral na [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), wey focus on medical domain and [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), wey dey do mathematical computation.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) na LLM wey Technology Innovation Institute (**TII**) create. Di Falcon-40B train on 40 billion parameters and e don show say e fit perform better pass GPT-3 with less compute budget. Dis na because e dey use FlashAttention algorithm and multiquery attention wey help reduce memory wey e need when e dey do inference. With dis reduced inference time, Falcon-40B good for chat apps.

Some fine-tuned versions of Falcon na [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), assistant wey dem build on open models and [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), wey get higher performance pass di base model.

## How to Choose

No be only one answer dey for how to choose open model. One good place to start na to use Azure AI Studio's filter by task feature. Dis one go help you sabi di kind tasks wey di model train for. Hugging Face still get LLM Leaderboard wey dey show di best performing models based on certain metrics.

If you wan compare LLMs across different types, [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) na another beta resource:

![Model Quality](../../../translated_images/model-quality.aaae1c22e00f7ee1.pcm.png)
Source: Artificial Analysis

If you dey work on one specific use case, to find fine-tuned versions wey focus on di same area fit work well. To try different open models to see how dem perform based on your and your users' expectations na another good way.

## Next Steps

Di best part about open models be say you fit start to work with dem quick quick. Check out di [Azure AI Foundry Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), wey get one special Hugging Face collection with di models wey we talk about here.

## Learning no stop here, continue di Journey

After you finish dis lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue to improve your Generative AI knowledge!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg sabi say automated translation fit get some mistakes or wrong tins. Di original document wey e dey for im own language na di correct one. If na serious matter, e better make human professional translate am. We no go responsible for any misunderstanding or wrong meaning wey fit come from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->