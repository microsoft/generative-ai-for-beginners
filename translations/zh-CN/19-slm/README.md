# 面向初学者的生成式 AI 小型语言模型简介
生成式 AI 是人工智能的一个迷人领域，专注于创建能够生成新内容的系统。这些内容可以涵盖文本、图像、音乐甚至整个虚拟环境。生成式 AI 最令人兴奋的应用之一是在语言模型领域。

## 什么是小型语言模型？

小型语言模型（SLM）是大型语言模型（LLM）的缩小版本，利用了许多 LLM 的架构原理和技术，同时显著降低了计算资源的消耗。

SLM 是设计用来生成类人文本的语言模型子集。与其更大的同类——如 GPT-4 不同，SLM 更紧凑高效，适合计算资源有限的应用场景。尽管体积较小，它们仍能执行多种任务。通常，SLM 是通过压缩或蒸馏 LLM 构建的，旨在保留原始模型大部分的功能和语言能力。这种模型规模的缩减降低了整体复杂性，使 SLM 在内存使用和计算需求上更加高效。尽管经过优化，SLM 仍能执行范围广泛的自然语言处理（NLP）任务：

- 文本生成：创建连贯且符合上下文的句子或段落。
- 文本补全：基于给定提示预测并补全文句。
- 翻译：将文本从一种语言转换为另一种语言。
- 摘要：将较长文本浓缩成较短且易于理解的摘要。

尽管相较更大的模型可能在性能或理解深度上有所权衡。

## 小型语言模型如何工作？
SLM 经过大量文本数据训练。在训练过程中，它们学习语言的模式和结构，从而能够生成语法正确且符合上下文的文本。训练过程包括：

- 数据收集：从各种来源收集大量文本数据。
- 预处理：清理和组织数据，使其适合训练。
- 训练：利用机器学习算法教模型如何理解和生成文本。
- 微调：调整模型以提高其在特定任务上的性能。

SLM 发展顺应了对能够部署在资源受限环境（如移动设备或边缘计算平台）的模型日益增长的需求，而因资源消耗大，完整 LLM 在这些环境中往往不切实际。SLM 通过聚焦效率，实现性能和可访问性的平衡，促进了其在各领域的广泛应用。

![slm](../../../translated_images/zh-CN/slm.4058842744d0444a.webp)

## 学习目标

本课旨在介绍 SLM 知识，并结合 Microsoft Phi-3 了解文本内容、视觉和 MoE 等不同场景。

课后你应能回答以下问题：

- 什么是 SLM？
- SLM 与 LLM 有何区别？
- 什么是 Microsoft Phi-3/3.5 家族？
- 如何用 Microsoft Phi-3/3.5 家族进行推理？

准备好了吗？我们开始吧。

## 大型语言模型（LLM）与小型语言模型（SLM）之间的区别

LLM 和 SLM 均基于概率机器学习的基本原理，采用类似的架构设计、训练方法、数据生成流程和模型评估技术。不过，两者有几个关键差异。

## 小型语言模型的应用

SLM 具有广泛应用，包括：

- 聊天机器人：以对话方式提供客户支持和用户互动。
- 内容创作：辅助写作，生成创意甚至起草整篇文章。
- 教育：帮助学生完成写作作业或学习新语言。
- 辅助功能：为残障人士创建工具，如文本转语音系统。

<strong>规模</strong>
  
LLM 和 SLM 之间最主要的区别体现在模型规模上。LLM，如 ChatGPT（GPT-4），参数量估计达 1.76 万亿，而开源 SLM 如 Mistral 7B 的参数量显著较少，仅约 70 亿。此差异主要源于模型架构和训练过程的不同。例如，ChatGPT 在编码器-解码器框架中使用自注意力机制，而 Mistral 7B 采用滑动窗口注意力，使得仅用解码器架构时训练更高效。这种架构差异对模型复杂度和性能有重要影响。

<strong>理解能力</strong>

SLM 通常针对特定领域优化，专业性强，但在跨多个知识领域提供广泛上下文理解方面能力有限。相比之下，LLM 旨在模拟更全面的人类智能。它们通过庞大而多样的数据集训练，表现出较好的通用性和适应性，适用于更多下游任务，如自然语言处理和编程。

<strong>计算需求</strong>

训练和部署 LLM 是资源密集型的，通常需大规模 GPU 集群。例如，从零开始训练 ChatGPT 可能需要数千 GPU 经过长时间运算。相比之下，SLM 参数较少，对计算资源更友好。像 Mistral 7B 可以在配备中等 GPU 的本地机器上训练和运行，尽管训练仍需数小时并跨多个 GPU。

<strong>偏差</strong>

偏差是 LLM 里常见的问题，主要源于训练数据的性质。这些模型通常使用互联网上的原始公共数据，这些数据可能对某些群体的表达不足或误导，标签错误，或者包含受方言、地域差异和语法规则影响的语言偏见。此外，复杂的 LLM 架构有时会无意间加剧偏差，若不经过细致微调，问题可能难以发现。相比之下，SLM 训练于更受限的领域特定数据集，天生对偏差的敏感度低一些，但仍不完全免疫。

<strong>推理速度</strong>

SLM 较小的规模使其在推理速度上具有显著优势，能在本地硬件上高效生成输出，无需大量并行计算。而 LLM 因尺寸庞大和复杂性高，常需大量并行计算资源以达到可接受的响应时间。用户并发量高时，规模化部署的 LLM 反应速度尤为受影响。

总结而言，虽然 LLM 和 SLM 共享机器学习的基础，但在模型大小、资源需求、上下文理解能力、偏差敏感性和推理速度等方面存在显著差异。这些差异反映出它们适用于不同的使用场景，LLM 功能更全面但资源消耗大，而 SLM 在特定领域表现高效且计算需求较低。

***注：本课将以 Microsoft Phi-3 / 3.5 为例介绍 SLM。***

## 介绍 Phi-3 / Phi-3.5 家族

Phi-3 / 3.5 家族主要面向文本、视觉和 Agent (MoE) 应用场景：

### Phi-3 / 3.5 指令型模型

主要用于文本生成、聊天完成和内容信息提取等。

**Phi-3-mini**

该 3.8B 语言模型可在 Microsoft Foundry、Hugging Face 和 Ollama 上获取。Phi-3 模型在主要基准测试中显著优于同等及更大规模的语言模型（见下方基准数据，数值越高越好）。Phi-3-mini 的表现超过了体积两倍的模型，而 Phi-3-small 和 Phi-3-medium 则超越了包括 GPT-3.5 在内的更大模型。

**Phi-3-small & medium**

Phi-3-small 拥有仅 7B 参数，在多项语言、推理、编码及数学基准测试中击败 GPT-3.5T。

拥有 14B 参数的 Phi-3-medium 也延续了这一趋势，击败了 Gemini 1.0 Pro。

**Phi-3.5-mini**

可以视作 Phi-3-mini 的升级版。虽然参数数量保持不变，但增强了多语言支持能力（支持 20 多种语言：阿拉伯语、中文、捷克语、丹麦语、荷兰语、英语、芬兰语、法语、德语、希伯来语、匈牙利语、意大利语、日语、韩语、挪威语、波兰语、葡萄牙语、俄语、西班牙语、瑞典语、泰语、土耳其语、乌克兰语）并加强了对长上下文的支持。

拥有 3.8B 参数的 Phi-3.5-mini 表现优于同尺寸语言模型，与体积两倍模型表现相当。

### Phi-3 / 3.5 视觉模型

可将 Phi-3/3.5 指令模型视作 Phi 的理解能力，而视觉模型则赋予 Phi 观察世界的眼睛。


**Phi-3-Vision**

参数仅 4.2B 的 Phi-3-vision 延续了之前的优势，在常规视觉推理、OCR 以及表格和图表理解任务中表现优于更大模型，如 Claude-3 Haiku 和 Gemini 1.0 Pro V。


**Phi-3.5-Vision**

Phi-3.5-Vision 是 Phi-3-Vision 的升级版，增加了多图像支持。可以理解为视觉能力的提升，不仅能看图，还能看视频。

Phi-3.5-vision 在 OCR、表格和图表理解任务中超过了更大模型如 Claude-3.5 Sonnet 和 Gemini 1.5 Flash，在常规视觉知识推理任务中表现相当。支持多帧输入，即可对多张输入图像进行推理。


### Phi-3.5-MoE

***专家模型混合 (MoE)*** 能让模型以远低于常规计算成本的方式进行预训练，这意味着在相同计算预算下，你可以大幅度扩展模型或数据集规模。尤其是，MoE 模型应能比密集模型更快达到相同质量。

Phi-3.5-MoE 由 16 个 3.8B 专家模块组成。仅 6.6B 激活参数的 Phi-3.5-MoE 在推理、语言理解和数学方面达到了与更大模型相当的水平。

我们可以根据不同场景使用 Phi-3/3.5 家族模型。不同于 LLM，你可以在边缘设备上部署 Phi-3/3.5-mini 或 Phi-3/3.5-Vision。


## 如何使用 Phi-3/3.5 家族模型

我们希望在不同场景中使用 Phi-3/3.5。接下来，我们将基于不同场景演示 Phi-3/3.5 的使用。

![phi3](../../../translated_images/zh-CN/phi3.655208c3186ae381.webp)

### 通过云端 API 推理

**Microsoft Foundry 模型**

> **注意：** GitHub 模型将在 2026 年 7 月底退休， [Microsoft Foundry 模型](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 是直接替代。

Microsoft Foundry 模型是最直接的访问方式。你可以快速通过 Foundry 模型目录访问 Phi-3/3.5-Instruct 模型。结合 Azure AI 推理 SDK / OpenAI SDK，可以通过代码调用 API 完成 Phi-3/3.5-Instruct。也可以通过 Playground 测试不同效果。

- 演示：Phi-3-mini 与 Phi-3.5-mini 在中文场景的效果对比

![phi3](../../../translated_images/zh-CN/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/zh-CN/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

如果想使用视觉和 MoE 模型，也可以使用 Microsoft Foundry 完成调用。如果感兴趣，可以阅读 Phi-3 烹饪书，了解如何通过 Microsoft Foundry 调用 Phi-3/3.5 的 Instruct、Vision、MoE 模型 [点击链接](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

除了基于云的 Microsoft Foundry 模型目录，你还可以使用 [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) 进行相关调用。你可以访问 NVIDIA NIM 来完成 Phi-3/3.5 家族的 API 调用。NVIDIA NIM（NVIDIA 推理微服务）是一套加速推理微服务，旨在帮助开发者高效部署 AI 模型于云端、数据中心及工作站等多种环境。

以下是 NVIDIA NIM 的一些主要特性：

- **易于部署：** NIM 允许通过一条命令部署 AI 模型，方便集成到现有工作流中。

- **优化性能：** 它利用 NVIDIA 预优化的推理引擎，如 TensorRT 和 TensorRT-LLM，以确保低延迟和高吞吐量。
- **可扩展性：** NIM 支持 Kubernetes 上的自动扩展，使其能够有效处理不同的工作负载。
- **安全与控制：** 组织可以通过在自有管理基础设施上自托管 NIM 微服务，保持对其数据和应用的控制。
- **标准 API：** NIM 提供行业标准 API，使构建和集成聊天机器人、AI 助手等 AI 应用变得简便。

NIM 是 NVIDIA AI Enterprise 的一部分，旨在简化 AI 模型的部署和运维，确保它们在 NVIDIA GPU 上高效运行。

- 演示：使用 NVIDIA NIM 调用 Phi-3.5-Vision-API [[点击此链接](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### 本地运行 Phi-3/3.5
针对 Phi-3 或任何类似 GPT-3 的语言模型，推理是指基于输入生成响应或预测的过程。当你向 Phi-3 提供提示或问题时，它会利用其训练好的神经网络，通过分析训练数据中的模式和关系，推断出最可能且相关的响应。

**Hugging Face Transformer**
Hugging Face Transformers 是一个强大的库，专为自然语言处理（NLP）和其他机器学习任务设计。以下是一些关键点：

1. <strong>预训练模型</strong>：提供数千种预训练模型，可用于文本分类、命名实体识别、问答、摘要、翻译和文本生成等多种任务。

2. <strong>框架互操作性</strong>：支持多种深度学习框架，包括 PyTorch、TensorFlow 和 JAX，允许你在一个框架中训练模型，并在另一个框架中使用。

3. <strong>多模态能力</strong>：除了 NLP，Hugging Face Transformers 还支持计算机视觉任务（如图像分类、目标检测）和音频处理任务（如语音识别、音频分类）。

4. <strong>易用性</strong>：库中提供 API 和工具，方便下载和微调模型，适合初学者和专家使用。

5. <strong>社区与资源</strong>：Hugging Face 拥有活跃的社区，提供广泛的文档、教程和指南，帮助用户快速上手并充分利用该库。
[官方文档](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) 或其 [GitHub 仓库](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst)。

这是最常用的方法，但也需要 GPU 加速。毕竟像 Vision 和 MoE 这类场景计算量很大，若未进行量化，在 CPU 上会非常慢。


- 演示：使用 Transformer 调用 Phi-3.5-Instruct [点击此链接](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- 演示：使用 Transformer 调用 Phi-3.5-Vision [点击此链接](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- 演示：使用 Transformer 调用 Phi-3.5-MoE [点击此链接](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) 是一个平台，旨在简化在本地机器上运行大型语言模型（LLM）的过程。它支持多种模型，如 Llama 3.1、Phi 3、Mistral 和 Gemma 2 等。该平台将模型权重、配置和数据捆绑成一个包，简化用户自定义和创建自己的模型。Ollama 支持 macOS、Linux 和 Windows。如果你想实验或部署 LLM，不依赖云服务，Ollama 是最直接的方式。你只需执行以下命令即可。


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) 是微软的离线本地运行时，可以在你自己的硬件上完全运行像 Phi 这样的模型——无需 Azure 订阅、API 密钥或网络连接。它会自动选择最佳的执行提供者（NPU、GPU 或 CPU），并暴露一个兼容 OpenAI 的接口，使现有的 `openai`/Azure AI 推理 SDK 代码几乎无需修改即可指向它。请参阅 [Foundry Local 文档](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) 开始使用。

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

或直接在 Python 中使用 SDK：

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime for GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) 是一个跨平台的机器学习推理和训练加速器。针对生成式 AI 的 ONNX Runtime (GENAI) 是一个强大的工具，帮助你在各种平台上高效运行生成式 AI 模型。

## 什么是 ONNX Runtime？
ONNX Runtime 是一个开源项目，支持高性能推理机器学习模型。它支持 Open Neural Network Exchange (ONNX) 格式，这是一个表示机器学习模型的标准。ONNX Runtime 推理可实现更快的客户体验和更低的成本，支持来自深度学习框架如 PyTorch 和 TensorFlow/Keras，以及经典机器学习库如 scikit-learn、LightGBM、XGBoost 等的模型。ONNX Runtime 兼容多种硬件、驱动和操作系统，通过结合硬件加速器及图优化和变换，提供最佳性能。

## 什么是生成式 AI？
生成式 AI 指能够基于训练数据生成新内容（如文本、图像或音乐）的 AI 系统。示例包括 GPT-3 等语言模型以及 Stable Diffusion 等图像生成模型。ONNX Runtime for GenAI 库提供了生成式 AI 循环支持 ONNX 模型，包括使用 ONNX Runtime 进行推理、logits 处理、搜索和采样以及键值缓存管理。

## ONNX Runtime for GENAI
ONNX Runtime for GENAI 扩展了 ONNX Runtime 的能力，以支持生成式 AI 模型。以下是一些关键特性：

- **广泛的平台支持：** 支持 Windows、Linux、macOS、Android 和 iOS 等多种平台。
- **模型支持：** 支持多种流行的生成式 AI 模型，如 LLaMA、GPT-Neo、BLOOM 等。
- **性能优化：** 针对不同硬件加速器（如 NVIDIA GPU、AMD GPU 等）进行优化。
- **易用性：** 提供便捷的 API 以集成到应用中，允许以最小代码生成文本、图像及其他内容。
- 用户可调用高级的 generate() 方法，或在循环中逐步运行每次模型迭代，生成单个标记，并可在循环内更新生成参数。
- ONNX Runtime 还支持贪心/束搜索和 TopP、TopK 采样生成标记序列，并内置如重复惩罚等 logits 处理。你也可以方便地添加自定义评分。

## 快速入门
开始使用 ONNX Runtime for GENAI，你可以按照以下步骤：

### 安装 ONNX Runtime：
```Python
pip install onnxruntime
```
### 安装生成式 AI 扩展：
```Python
pip install onnxruntime-genai
```

### 运行模型：这里是一个简单的 Python 示例：
```Python
import onnxruntime_genai as og

model = og.Model('path_to_your_model.onnx')

tokenizer = og.Tokenizer(model)

input_text = "Hello, how are you?"

input_tokens = tokenizer.encode(input_text)

output_tokens = model.generate(input_tokens)

output_text = tokenizer.decode(output_tokens)

print(output_text) 
```
### 演示：使用 ONNX Runtime GenAI 调用 Phi-3.5-Vision


```python

import onnxruntime_genai as og

model_path = './Your Phi-3.5-vision-instruct ONNX Path'

img_path = './Your Image Path'

model = og.Model(model_path)

processor = model.create_multimodal_processor()

tokenizer_stream = processor.create_stream()

text = "Your Prompt"

prompt = "<|user|>\n"

prompt += "<|image_1|>\n"

prompt += f"{text}<|end|>\n"

prompt += "<|assistant|>\n"

image = og.Images.open(img_path)

inputs = processor(prompt, images=image)

params = og.GeneratorParams(model)

params.set_inputs(inputs)

params.set_search_options(max_length=3072)

generator = og.Generator(model, params)

while not generator.is_done():

    generator.compute_logits()
    
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    
    output = tokenizer_stream.decode(new_token)
    
    print(tokenizer_stream.decode(new_token), end='', flush=True)

```


<strong>其他</strong>

除了 ONNX Runtime、Ollama 和 Foundry Local 参考方法外，我们还可以基于不同厂商提供的模型参考方法，补全定量模型的参考。例如 Apple MLX 框架配合 Apple Metal、Qualcomm QNN 配合 NPU、Intel OpenVINO 配合 CPU/GPU 等。更多内容可见[Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## 更多内容

我们已经学习了 Phi-3/3.5 系列的基础知识，但想了解更多关于 SLM 的知识，我们需要更多的资料。你可以在 Phi-3 Cookbook 中找到答案。如果想深入学习，请访问 [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->