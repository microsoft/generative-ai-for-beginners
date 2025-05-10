[![开放原始码模型](../../images/16-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson16-gh?WT.mc_id=academic-105485-koreyst)

## 简介

开放原始码 LLMs 的世界令人兴奋且不断演变。本课程旨在深入了解开放原始码模型。如果您正在寻找有关专有模型与开放原始码模型比较的信息，请参阅["探索和比较不同的 LLMs" 课程](../../../02-exploring-and-comparing-different-llms/translations/tw/README.md?WT.mc_id=academic-105485-koreyst)。本课程还将涵盖微调的主题，但更详细的解释可以在["微调 LLMs" 课程](../../../18-fine-tuning/translations/tw/README.md?WT.mc_id=academic-105485-koreyst)中找到。

## 学习目标

- 了解开放原始码模型
- 了解使用开放原始码模型的好处
- 探索 Hugging Face 和 Azure AI Studio 上可用的开放模型

## 什么是开放原始码模型？

开放原始码软件在各个领域的技术发展中扮演了至关重要的角色。开放原始码倡议（OSI）已经定义了[软件的10个标准](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst)，以将其归类为开放原始码。源程序必须在OSI批准的许可下公开共享。

虽然 LLMs 的开发与软件开发有相似的元素，但过程并不完全相同。这在社区中引发了许多关于 LLMs 背景下开放原始码定义的讨论。要使模型符合传统的开放原始码定义，以下信息应该公开可用：

- 用于训练模型的数据集。
- 作为训练的一部分的完整模型权重。
- 评估代码。
- 微调代码。
- 完整模型权重和训练指标。

目前只有少数模型符合此标准。[由Allen Institute for Artificial Intelligence (AllenAI) 创建的OLMo模型](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) 就是其中之一。

在本课程中，我们将这些模型称为「开放模型」，因为在撰写时它们可能不符合上述标准。

## 开放模型的好处

**高度可定制** - 由于开放模型发布时附有详细的训练信息，研究人员和开发人员可以修改模型的内部结构。这使得能够建立即高度专门化的模型，针对特定任务或研究领域进行微调。一些范例包括程序生成器、数学运算和生物学。

**成本** - 使用和部署这些模型的每个 token 成本低于专有模型。在构建生成式 AI 应用程序时，应该在您的使用案例中考量这些模型的性能与价格。

![Model Cost](../../images/model-price.png?WT.mc_id=academic-105485-koreyst)
来源: 人工分析

**灵活性** - 使用开放模型使您在使用不同模型或结合它们方面更加灵活。一个范例是 [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst)，用户可以直接在用户界面中选择所使用的模型:

![选择模型](../../images/choose-model.png?WT.mc_id=academic-105485-koreyst)

## 探索不同的开放模型

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), 由 Meta 开发，是一个针对聊天应用程序优化的开放模型。这是由于其微调方法，包括大量的对话和人类反馈。通过这种方法，模型产生更多符合人类期望的结果，从而提供更好的用户体验。

一些经过微调的Llama版本范例包括专门用于日语的[Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst)和增强版基础模型的[Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst)。

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst)是一个专注于高性能和效率的开放模型。它使用专家混合方法，将一组专门的专家模型组合成一个系统，根据输入选择特定的模型来使用。这使得计算更加有效，因为模型只处理它们专门的输入。

一些微调版本的Mistral范例包括专注于医疗领域的[BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst)和进行数学计算的[OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst)。

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) 是由技术创新研究所（**TII**）创建的 LLM。Falcon-40B 在 400 亿个参数上进行了训练，已显示出在较少计算预算下比 GPT-3 表现更好。这是由于其使用了 FlashAttention 算法和多查询注意力，使其能够在推理时减少内存需求。由于这种减少的推理时间，Falcon-40B 适用于聊天应用程序。

一些 Falcon 微调版本的范例包括 [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst)，一个基于开放模型的助手和 [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst)，其性能高于基础模型。

## 如何选择

选择开放模型没有唯一的答案。一个好的开始是使用 Azure AI Studio 的任务筛选功能。这将帮助你了解模型已经被训练用于哪些类型的任务。Hugging Face 也维护了一个 LLM 排行榜，显示基于某些指标的最佳表现模型。

在比较不同类型的LLM时，[Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) 是另一个很好的资源:

![模型质量](../../images/model-quality.png?WT.mc_id=academic-105485-koreyst)
来源: 人工分析

如果处理特定用例，搜索专注于相同领域的微调版本可能会很有效。尝试多个开放模型，看看它们如何根据你和你的用户的期望表现，也是另一个好做法。

## 下一步

开放模型最棒的部分是你可以很快地开始使用它们。查看 [Azure AI Studio Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)，其中包含我们在此讨论的特定 Hugging Face 集合。

## 学习不止于此，继续旅程

完成本课程后，请查看我们的[生成式 AI 学习集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)以继续提升您的生成式 AI 知识！
