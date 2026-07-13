# 面向初学者的生成式人工智能小型语言模型介绍
生成式人工智能是人工智能领域中一个令人着迷的分支，专注于创建能够生成新内容的系统。这些内容可以涵盖文本、图像、音乐，甚至整个虚拟环境。生成式人工智能最令人兴奋的应用之一就是语言模型领域。

## 什么是小型语言模型？

小型语言模型（SLM）是大型语言模型（LLM）的缩小版本，借鉴了许多大型语言模型的架构原理和技术，同时显著降低了计算资源需求。

SLM 是一类专注于生成类似人类文本的语言模型子集。与类似 GPT-4 的大型模型相比，SLM 体积更小、效率更高，特别适合计算资源有限的应用场景。尽管规模较小，它们仍能执行多种任务。通常，SLM 是通过压缩或蒸馏大型模型构建的，旨在保留原模型的绝大部分功能和语言能力。模型尺寸的减少降低了整体复杂性，使得 SLM 在内存使用和计算需求方面更加高效。即便如此，SLM 仍然能够执行广泛的自然语言处理（NLP）任务：

- 文本生成：创建连贯且符合上下文的句子或段落。
- 文本补全：根据给定的提示预测并完成句子。
- 翻译：将文本从一种语言转换为另一种语言。
- 摘要：将长文本浓缩成更简短、更易消化的摘要。

尽管相比大型模型性能或理解深度有所折衷。

## 小型语言模型如何工作？
SLM 通过大量文本数据进行训练。在训练过程中，它们学习语言的模式和结构，使其能够生成符合语法且符合上下文的文本。训练过程包括：

- 数据收集：从各种来源收集大量文本数据。
- 预处理：清理并组织数据，使其适合训练。
- 训练：使用机器学习算法教会模型如何理解和生成文本。
- 微调：调整模型以提升在特定任务上的性能。

SLM 的开发顺应了在资源受限环境（如移动设备或边缘计算平台）中部署模型的需求，而大型模型因资源消耗过大而不适用。通过聚焦效率，SLM 实现了性能与可访问性的平衡，促进其在不同领域的广泛应用。

![slm](../../../translated_images/zh-CN/slm.4058842744d0444a.webp)

## 学习目标

本课旨在介绍 SLM 的相关知识，并结合微软的 Phi-3，学习文本内容、视觉和专家混合（MoE）的多种场景。

课程结束时，你应能回答以下问题：

- 什么是 SLM？
- SLM 与 LLM 有何区别？
- 什么是微软 Phi-3/3.5 家族？
- 如何使用微软 Phi-3/3.5 家族进行推理？

准备好了吗？让我们开始吧。

## 大型语言模型（LLM）与小型语言模型（SLM）的区别

LLM 和 SLM 都基于概率机器学习的基础原理，采用相似的架构设计、训练方法、数据生成过程和模型评估技术，但两者在几个关键方面有所不同。

## 小型语言模型的应用

SLM 具备广泛的应用场景，包括：

- 聊天机器人：提供客户支持，并以对话形式与用户互动。
- 内容创作：协助写作者生成创意或起草整篇文章。
- 教育：帮助学生完成写作作业或学习新语言。
- 无障碍：为残障人士创建辅助工具，如文本转语音系统。

<strong>规模</strong>

LLM 与 SLM 的首要区别在于模型规模。LLM（如 ChatGPT（GPT-4））参数估计约为 1.76 万亿，而开源 SLM 如 Mistral 7B 的参数数量显著较少，约为 70 亿。这种差异主要源自模型架构和训练流程的不同。例如，ChatGPT 采用的是带有编码器-解码器框架的自注意力机制，而 Mistral 7B 使用滑动窗口注意力，支持在仅解码器结构中更高效的训练。这种架构差异对模型的复杂度和性能产生深远影响。

<strong>理解能力</strong>

SLM 通常针对特定领域进行优化，因而高度专业化，但在多个领域提供广泛上下文理解的能力可能有限。相较之下，LLM 致力于模拟更加全面的人类智能。LLM 经过海量且多样化的数据训练，旨在在多种领域表现良好，具有更强的适应性和通用性。因此，LLM 更适合处理如自然语言处理和编程等广泛的下游任务。

<strong>计算需求</strong>

LLM 的训练和部署对资源需求极高，通常需要大规模的 GPU 集群，例如从零训练 ChatGPT 可能需要数千 GPU 持续长时间运行。相比之下，参数规模更小的 SLM 对计算资源更加友好。像 Mistral 7B 这样的模型可在具备适度 GPU 能力的本地设备上训练和运行，尽管训练仍需多个 GPU 并持续数小时。

<strong>偏见</strong>

偏见是 LLM 的已知问题，主要由训练数据的性质导致。此类模型通常依赖来自互联网的原始公开数据，这些数据可能低估或错误描述某些群体，含有错误标注，或反映了基于方言、地区差异和语法规则的语言偏见。此外，复杂的 LLM 架构可能无意中加剧偏见，若无细致的微调可能难以察觉。反观 SLM，由于训练数据更受限制且领域特定，因此固有的偏见较小，但仍不可完全避免。

<strong>推理</strong>

SLM 因模型尺寸较小而在推理速度上具有显著优势，能够在本地硬件上高效生成输出，无需大量并行计算资源。LLM 由于体积庞大且复杂，往往需要强大的并行计算支持来保证可接受的推理时间。在多用户并发环境下，LLM 的响应时间会进一步延长，尤其是在大规模部署时。

总结来看，虽然 LLM 和 SLM 都以机器学习为基础，但在模型规模、资源需求、上下文理解能力、偏见敏感度和推理速度方面存在显著差异。这些差异反映了它们在应用场景上的适用性：LLM 功能更为通用但资源密集，SLM 则在特定领域提供更高效、更低计算消耗的解决方案。

***注：本课将以微软 Phi-3 / 3.5 作为例子介绍小型语言模型。***

## 介绍 Phi-3 / Phi-3.5 家族

Phi-3 / 3.5 家族主要面向文本、视觉和专家混合（MoE）应用场景：

### Phi-3 / 3.5 Instruct

主要用于文本生成、聊天补全和内容信息提取等。

**Phi-3-mini**

3.8B 参数量的语言模型可在 Microsoft Azure AI Studio、Hugging Face 和 Ollama 上使用。Phi-3 模型在主要基准测试中显著优于同等或更大规模模型（见下方基准分数，分数越高越好）。Phi-3-mini 的表现优于参数量两倍的模型，而 Phi-3-small 和 Phi-3-medium 则超越包括 GPT-3.5 在内的更大型模型。

**Phi-3-small & medium**

Phi-3-small 拥有仅 7B 参数，却在各种语言、推理、编码和数学基准测试中击败了 GPT-3.5T。

Phi-3-medium 拥有 14B 参数，继续此趋势，并优于 Gemini 1.0 Pro。

**Phi-3.5-mini**

可视为 Phi-3-mini 的升级版。参数数量保持不变，但增强了对多语言的支持（支持 20 多种语言：阿拉伯语、中文、捷克语、丹麦语、荷兰语、英语、芬兰语、法语、德语、希伯来语、匈牙利语、意大利语、日语、韩语、挪威语、波兰语、葡萄牙语、俄语、西班牙语、瑞典语、泰语、土耳其语、乌克兰语）并增强了对长上下文的支持。

3.8B 参数的 Phi-3.5-mini 不仅优于同规模语言模型，还能与参数量是其两倍的模型相媲美。

### Phi-3 / 3.5 Vision

我们可以将 Phi-3/3.5 的 Instruct 模型视为 Phi 的理解能力，Vision 则赋予 Phi “眼睛”去理解世界。

**Phi-3-Vision**

拥有仅 4.2B 参数的 Phi-3-vision 在通用视觉推理任务、OCR 以及表格和图表理解任务上表现优于更大模型，如 Claude-3 Haiku 和 Gemini 1.0 Pro V。

**Phi-3.5-Vision**

Phi-3.5-Vision 是 Phi-3-Vision 的升级版，增加了多图像支持。可以理解为视觉能力的提升，不仅能看图片，还能处理视频。

Phi-3.5-vision 在 OCR、表格和图表理解任务中表现优于更大型模型如 Claude-3.5 Sonnet 和 Gemini 1.5 Flash，并在通用视觉知识推理任务上表现相当。支持多帧输入，即对多张输入图片进行推理。

### Phi-3.5-MoE

***专家混合（Mixture of Experts，MoE）*** 使得模型可以用更少的计算资源完成预训练，这意味着在相同的计算预算下，模型或数据集规模可以显著扩大。尤其是 MoE 模型可在预训练阶段更快达到与密集模型相同的质量水平。

Phi-3.5-MoE 由 16 个 3.8B 参数的专家模块组成。仅具有 6.6B 有效参数的 Phi-3.5-MoE，在推理、语言理解和数学方面达到了与更大模型相似的水平。

我们可以根据不同场景使用 Phi-3/3.5 家族模型。与 LLM 不同，Phi-3/3.5-mini 或 Phi-3/3.5-Vision 可部署于边缘设备。

## 如何使用 Phi-3/3.5 家族模型

我们希望能在不同场景下使用 Phi-3/3.5。接下来将基于不同场景介绍 Phi-3/3.5 的使用。

![phi3](../../../translated_images/zh-CN/phi3.655208c3186ae381.webp)

### 通过云 API 进行推理

**GitHub Models**

GitHub Models 是最直接的方式，你可以快速访问 Phi-3/3.5-Instruct 模型。结合 Azure AI Inference SDK / OpenAI SDK，可通过代码调用 API 完成 Phi-3/3.5-Instruct 的调用。你也可以通过 Playground 进行不同效果的测试。

- 演示：Phi-3-mini 与 Phi-3.5-mini 在中文场景下效果对比

![phi3](../../../translated_images/zh-CN/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/zh-CN/gh2.07d7985af66f178d.webp)

**Azure AI Studio**

如果想使用视觉和 MoE 模型，可通过 Azure AI Studio 完成调用。感兴趣的用户可以阅读 Phi-3 Cookbook，了解如何通过 Azure AI Studio 调用 Phi-3/3.5 Instruct、Vision、MoE [点击这里](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)

**NVIDIA NIM**

除了 Azure 和 GitHub 提供的云端模型目录解决方案外，你还可以使用 [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) 完成相关调用。NVIDIA NIM（NVIDIA 推理微服务）是一套加速推理微服务，旨在帮助开发者高效地在云端、数据中心和工作站等多种环境中部署 AI 模型。

NVIDIA NIM 的一些关键特性：

- **部署简单：** 只需一条命令即可部署 AI 模型，方便集成入现有工作流。
- **性能优化：** 利用 NVIDIA 预优化的推理引擎，如 TensorRT 和 TensorRT-LLM，确保低延迟和高吞吐量。
- **可扩展性：** 支持 Kubernetes 的自动扩缩容，能够有效处理变化的工作负载。
- **安全与控制：** 组织可以通过在自己管理的基础设施上自托管 NIM 微服务来保持对其数据和应用的控制。
- **标准 API：** NIM 提供行业标准的 API，使得构建和集成聊天机器人、AI 助手及其他 AI 应用变得容易。

NIM 是 NVIDIA AI Enterprise 的一部分，旨在简化 AI 模型的部署和运维，确保它们在 NVIDIA GPU 上高效运行。

- 演示：使用 NVIDIA NIM 调用 Phi-3.5-Vision-API [[点击此链接](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### 本地运行 Phi-3/3.5
推理在 Phi-3 或任何类似 GPT-3 的语言模型中，指的是基于输入生成响应或预测的过程。当你向 Phi-3 提供提示或问题时，它会使用其训练过的神经网络通过分析训练数据中的模式和关系，推断最可能且相关的响应。

**Hugging Face Transformer**  
Hugging Face Transformers 是一个强大库，专为自然语言处理（NLP）和其他机器学习任务设计。以下是它的一些关键点：

1. **预训练模型：** 它提供数千个可用于文本分类、命名实体识别、问答、摘要、翻译和文本生成等多任务的预训练模型。

2. **框架互操作性：** 该库支持包括 PyTorch、TensorFlow 和 JAX 在内的多种深度学习框架，允许你在一个框架中训练模型，在另一个框架中使用。

3. **多模态能力：** 除 NLP 外，Hugging Face Transformers 还支持计算机视觉（如图像分类、目标检测）和音频处理（如语音识别、音频分类）任务。

4. **易用性：** 库提供了丰富的 API 和工具，方便下载和微调模型，适合初学者和专家使用。

5. **社区与资源：** Hugging Face 拥有活跃的社区及丰富的文档、教程和指南，助力用户快速上手并发挥最大效能。详见[官方文档](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst)或其[GitHub 仓库](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst)。

这是最常用的方法，但也需要 GPU 加速。毕竟，视觉和 MoE 等场景计算量很大，如果不进行量化，CPU 上运行会非常慢。


- 演示：使用 Transformer 调用 Phi-3.5-Instruct [点击此链接](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- 演示：使用 Transformer 调用 Phi-3.5-Vision [点击此链接](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- 演示：使用 Transformer 调用 Phi-3.5-MoE [点击此链接](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**  
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) 是一个平台，旨在简化在本地机器上运行大型语言模型（LLM）。它支持 Llama 3.1、Phi 3、Mistral、Gemma 2 等多种模型。该平台将模型权重、配置和数据打包成一个单一包，方便用户定制和创建自己的模型。Ollama 可在 macOS、Linux 和 Windows 上使用。如果你想在不依赖云服务的情况下实验或部署 LLM，这是一个非常好的工具。Ollama 是最直接的方式，只需执行以下命令即可。


```bash

ollama run phi3.5

```


**ONNX Runtime for GenAI**  

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) 是一个跨平台的推理与训练机器学习加速器。ONNX Runtime for Generative AI (GENAI) 是一个强大的工具，帮助你高效地在多种平台上运行生成式 AI 模型。

## 什么是 ONNX Runtime？
ONNX Runtime 是一个开源项目，提供高性能的机器学习模型推理。它支持 Open Neural Network Exchange (ONNX) 格式的模型，这是一种表示机器学习模型的标准。ONNX Runtime 推理可以加快客户体验并降低成本，支持来自深度学习框架（如 PyTorch 和 TensorFlow/Keras）以及经典机器学习库（如 scikit-learn、LightGBM、XGBoost 等）的模型。ONNX Runtime 兼容不同硬件、驱动和操作系统，通过硬件加速器结合图优化和转换提供最佳性能。

## 什么是生成式 AI？
生成式 AI 指能够基于训练数据生成新内容（如文本、图像或音乐）的 AI 系统。例子包括语言模型 GPT-3 和图像生成模型 Stable Diffusion。ONNX Runtime for GenAI 库提供生成式 AI 循环支持 ONNX 模型，包括使用 ONNX Runtime 推理、logits 处理、搜索与采样以及 KV 缓存管理。

## ONNX Runtime for GENAI  
ONNX Runtime for GENAI 扩展了 ONNX Runtime 的能力，支持生成式 AI 模型。主要特性包括：

- **广泛平台支持：** 兼容 Windows、Linux、macOS、Android 和 iOS 等多个平台。
- **模型支持：** 支持众多流行的生成式 AI 模型，如 LLaMA、GPT-Neo、BLOOM 等。
- **性能优化：** 针对 NVIDIA GPU、AMD GPU 等多种硬件加速器进行了优化。
- **易用性：** 提供简单易用的 API，方便集成进应用，允许你用最少的代码生成文本、图像及其它内容。
- 用户可以调用高级的 generate() 方法，或者在循环中逐步运行模型，每次生成一个 token，并在循环中可选更新生成参数。
- ONNX Runtime 还支持贪婪/束搜索（greedy/beam search）、TopP、TopK 采样生成 token 序列，内置重复惩罚等 logits 处理功能。同时也可轻松添加自定义评分。

## 快速开始  
你可以按照以下步骤开始使用 ONNX Runtime for GENAI：

### 安装 ONNX Runtime：
```Python
pip install onnxruntime
```


### 安装生成式 AI 扩展：
```Python
pip install onnxruntime-genai
```


### 运行模型：以下是一个简单的 Python 示例：
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

除 ONNX Runtime 和 Ollama 参考方法外，我们还可以基于不同厂商提供的模型参考方法完成量化模型的参考，如配合 Apple Metal 的 Apple MLX 框架、配合 NPU 的 Qualcomm QNN、配合 CPU/GPU 的 Intel OpenVINO 等。你还可以从[Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)获取更多内容。


## 更多

我们已经了解了 Phi-3/3.5 家族的基础知识，但要深入学习 SLM，需要更多知识。你可以在 Phi-3 Cookbook 中找到答案。如需更多学习，请访问[Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->