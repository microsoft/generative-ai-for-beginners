[![Open Source Models](../../../translated_images/16-lesson-banner.png?WT.a9a13a59f0350adb5846e88fb3aba98cd4c6cb3297e78cb7100938f45b7dac47.zh.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson16-gh?WT.mc_id=academic-105485-koreyst)

## 介绍

开源大型语言模型（LLM）的世界充满活力并不断发展。本课旨在深入了解开源模型。如果您想了解专有模型与开源模型的比较，请访问["探索和比较不同的LLM"课程](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)。本课还将涵盖微调的主题，但更详细的解释可以在["微调LLM"课程](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst)中找到。

## 学习目标

- 了解开源模型
- 理解使用开源模型的好处
- 探索在Hugging Face和Azure AI Studio上可用的开源模型

## 什么是开源模型？

开源软件在各个领域的技术发展中发挥了重要作用。开源倡议（OSI）定义了[软件的10个标准](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst)以被归类为开源。源代码必须在OSI批准的许可证下公开共享。

虽然LLM的开发与软件开发有相似之处，但过程并不完全相同。这引起了社区关于在LLM背景下开源定义的广泛讨论。为了使模型符合传统的开源定义，以下信息应该公开可用：

- 用于训练模型的数据集。
- 作为训练一部分的完整模型权重。
- 评估代码。
- 微调代码。
- 完整的模型权重和训练指标。

目前只有少数模型符合此标准。[由Allen Institute for Artificial Intelligence (AllenAI)创建的OLMo模型](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst)就是其中之一。

在本课中，我们将继续将这些模型称为“开源模型”，因为在撰写本文时它们可能不符合上述标准。

## 开源模型的好处

**高度可定制** - 由于开源模型发布了详细的训练信息，研究人员和开发人员可以修改模型的内部结构。这使得可以创建高度专业化的模型，以针对特定任务或研究领域进行微调。一些例子包括代码生成、数学运算和生物学。

**成本** - 使用和部署这些模型的每个token成本低于专有模型。在构建生成式AI应用程序时，应该根据您的用例权衡性能与价格。

![Model Cost](../../../translated_images/model-price.png?WT.473bad4fe5bdb7014798275047130c0949da1e4a3d6f379037bedf68ef1d5e42.zh.mc_id=academic-105485-koreyst)
来源: Artificial Analysis

**灵活性** - 使用开源模型可以让您在使用不同模型或组合模型方面更加灵活。一个例子是[HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst)，用户可以在用户界面中直接选择正在使用的模型：

![Choose Model](../../../translated_images/choose-model.png?WT.50da8a7caba083003bcf9f71017d17715f032acff67359c11c9886597ca3efdc.zh.mc_id=academic-105485-koreyst)

## 探索不同的开源模型

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst)由Meta开发，是一个针对聊天应用优化的开源模型。这是由于其微调方法，包括大量对话和人类反馈。通过这种方法，模型生成的结果更符合人类期望，从而提供更好的用户体验。

Llama的一些微调版本包括专注于日语的[Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst)和增强版的[Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst)。

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst)是一个专注于高性能和效率的开源模型。它使用专家混合方法，将一组专门的专家模型组合成一个系统，根据输入选择使用某些模型。这使得计算更加有效，因为模型只处理它们专长的输入。

Mistral的一些微调版本包括专注于医疗领域的[BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst)和执行数学运算的[OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst)。

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst)是由技术创新研究所（TII）创建的LLM。Falcon-40B在40亿参数上进行了训练，表现优于计算预算较低的GPT-3。这是因为它使用了FlashAttention算法和多查询注意力，使其在推理时减少了内存需求。由于推理时间减少，Falcon-40B适合用于聊天应用。

Falcon的一些微调版本包括基于开源模型构建的[OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst)和性能优于基础模型的[GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst)。

## 如何选择

没有一个标准答案来选择开源模型。一个好的起点是使用Azure AI Studio的按任务筛选功能。这将帮助您了解模型已被训练的任务类型。Hugging Face还维护了一个LLM排行榜，显示了基于某些指标的最佳表现模型。

在比较不同类型的LLM时，[Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst)是另一个很好的资源：

![Model Quality](../../../translated_images/model-quality.png?WT.bffdb0b01a3f3205153df83585941f90a153017f607dbcfad9cde5369764f203.zh.mc_id=academic-105485-koreyst)
来源: Artifical Analysis

如果正在处理特定用例，寻找专注于相同领域的微调版本可能会很有效。尝试多个开源模型以查看它们是否符合您和用户的期望是另一种好做法。

## 下一步

开源模型的最佳部分是您可以很快开始使用它们。查看[Azure AI Studio模型目录](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)，其中包含我们在此讨论的这些模型的特定Hugging Face集合。

## 学习不止于此，继续学习之旅

完成本课后，请查看我们的[生成式AI学习集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，继续提升您的生成式AI知识！

**免责声明**：
本文档使用基于机器的AI翻译服务进行翻译。虽然我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原始语言的文档视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而引起的任何误解或误读，我们不承担责任。