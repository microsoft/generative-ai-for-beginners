<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8b2d4bb727c877ebf9edff8623d16b9",
  "translation_date": "2025-09-06T10:12:07+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "zh"
}
-->
[![开源模型](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.zh.png)](https://aka.ms/gen-ai-lesson16-gh?WT.mc_id=academic-105485-koreyst)

## 介绍

开源LLM的世界充满了活力并且不断发展。本课程旨在深入探讨开源模型。如果您想了解专有模型与开源模型的比较，请参阅["探索和比较不同LLM"课程](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)。本课程还将涉及微调的主题，但更详细的解释可以在["微调LLM"课程](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst)中找到。

## 学习目标

- 了解开源模型
- 理解使用开源模型的优势
- 探索Hugging Face和Azure AI Studio上的开源模型

## 什么是开源模型？

开源软件在技术领域的增长中发挥了至关重要的作用。开源倡议（OSI）定义了[软件的10个标准](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst)，以将其归类为开源。源代码必须在OSI批准的许可下公开共享。

虽然LLM的开发与软件开发有相似之处，但过程并不完全相同。这引发了社区关于LLM开源定义的广泛讨论。要符合传统开源定义，以下信息应公开：

- 用于训练模型的数据集。
- 训练过程中使用的完整模型权重。
- 评估代码。
- 微调代码。
- 完整的模型权重和训练指标。

目前只有少数模型符合这些标准。[由Allen人工智能研究所（AllenAI）创建的OLMo模型](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst)就是其中之一。

在本课程中，我们将使用“开源模型”这一术语，因为截至撰写本文时，这些模型可能不完全符合上述标准。

## 开源模型的优势

**高度可定制** - 由于开源模型发布了详细的训练信息，研究人员和开发者可以修改模型的内部结构。这使得能够创建针对特定任务或研究领域的高度专业化模型。例如代码生成、数学运算和生物学等领域。

**成本** - 使用和部署这些模型的每个token成本低于专有模型。在构建生成式AI应用时，应根据您的使用场景权衡性能与价格。

![模型成本](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.zh.png)  
来源：Artificial Analysis

**灵活性** - 使用开源模型可以灵活地选择不同的模型或将它们结合使用。例如，[HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst)允许用户直接在界面中选择使用的模型：

![选择模型](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.zh.png)

## 探索不同的开源模型

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst)由Meta开发，是一个针对聊天应用优化的开源模型。这是因为其微调方法包含了大量对话和人类反馈。通过这种方法，模型生成的结果更符合人类期望，从而提供更好的用户体验。

一些微调版本的Llama包括[Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst)，专注于日语，以及[Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst)，这是基础模型的增强版本。

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst)是一个专注于高性能和效率的开源模型。它采用了专家混合（Mixture-of-Experts）方法，将一组专业模型组合成一个系统，根据输入选择特定模型使用。这使得计算更高效，因为模型只处理它们擅长的输入。

一些微调版本的Mistral包括[BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst)，专注于医疗领域，以及[OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst)，用于数学计算。

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst)是由技术创新研究所（**TII**）创建的LLM。Falcon-40B在40亿参数上进行了训练，表现优于GPT-3，同时计算预算更低。这得益于其使用的FlashAttention算法和多查询注意力机制，使得推理时的内存需求减少。由于推理时间缩短，Falcon-40B适合聊天应用。

一些微调版本的Falcon包括[OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst)，一个基于开源模型的助手，以及[GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst)，其性能优于基础模型。

## 如何选择

没有一个统一的答案来选择开源模型。一个好的起点是使用Azure AI Studio的任务过滤功能。这将帮助您了解模型已训练的任务类型。Hugging Face还维护了一个LLM排行榜，显示基于特定指标的最佳表现模型。

如果需要比较不同类型的LLM，[Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst)是另一个很好的资源：

![模型质量](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.zh.png)  
来源：Artificial Analysis

如果针对特定使用场景，寻找专注于相同领域的微调版本可能会更有效。尝试多个开源模型以了解它们是否符合您和用户的期望也是一种好方法。

## 下一步

开源模型的最佳部分是您可以快速开始使用它们。查看[Azure AI Foundry模型目录](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)，其中包含我们在此讨论的Hugging Face集合中的模型。

## 学习不会止步于此，继续探索之旅

完成本课程后，请查看我们的[生成式AI学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，继续提升您的生成式AI知识！

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们尽力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。