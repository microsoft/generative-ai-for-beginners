# 面向初学者的生成式人工智能：小语言模型入门
生成式人工智能是人工智能领域中一个令人着迷的分支，专注于创建能够生成新内容的系统。这些内容涵盖文本、图像、音乐乃至完整的虚拟环境。生成式人工智能最激动人心的应用之一便是语言模型领域。

## 什么是小语言模型？

小语言模型（SLM）是大型语言模型（LLM）的缩小版本，继承了 LLM 的架构原理和技术，同时显著降低了计算资源需求。

作为语言模型的子集，小语言模型专门用于生成类人文本。与 GPT-4 等大型模型不同，SLM 更加紧凑高效，非常适合计算资源有限的应用场景。尽管体积小巧，它们仍能执行多种任务。通常 SLM 通过压缩或蒸馏 LLM 获得，旨在保留原模型大部分功能和语言能力。模型体积的缩减降低了整体复杂度，使 SLM 在内存占用和计算需求方面更加高效。经过优化后，SLM 仍可胜任多种自然语言处理（NLP）任务：

- 文本生成：创作连贯且符合语境的句子或段落
- 文本补全：根据给定提示预测并完成句子
- 翻译：实现不同语言间的文本转换
- 摘要：将长篇文本浓缩为简洁易懂的摘要

不过相较于大型模型，其性能和理解深度会有所折衷。

## 小语言模型的工作原理
SLM 通过海量文本数据进行训练。训练过程中，模型学习语言模式和结构，从而生成语法正确且语境贴切的文本。训练流程包含：

- 数据收集：从多种渠道获取大规模文本数据集
- 预处理：清洗整理数据以适应训练需求
- 训练：运用机器学习算法教授模型理解和生成文本
- 微调：针对特定任务优化模型性能

SLM 的发展顺应了资源受限环境（如移动设备或边缘计算平台）对可部署模型的需求，这些场景中全尺寸 LLM 因资源消耗过高而难以应用。通过效率优化，SLM 在性能与易用性之间取得平衡，拓宽了跨领域应用的可行性。

![slm](../../img/slm.png?WT.mc_id=academic-105485-koreyst)

## 学习目标

本课程将结合微软 Phi-3 系列模型，介绍 SLM 在文本内容、视觉和多专家系统（MoE）等不同场景中的应用。

完成本课程后，您应能回答以下问题：

- 什么是 SLM
- SLM 与 LLM 的核心区别
- 微软 Phi-3/3.5 系列模型的特点
- 如何调用微软 Phi-3/3.5 系列模型

准备好了吗？让我们开始探索。

## 大型语言模型（LLM）与小语言模型（SLM）的差异

LLM 和 SLM 均基于概率机器学习的基本原理，在架构设计、训练方法、数据生成流程和模型评估技术等方面具有相似性。但以下关键因素构成了二者的主要区别。

## 小语言模型的应用领域

SLM 具有广泛的应用场景，包括：

- 聊天机器人：提供客户支持及对话服务
- 内容创作：辅助作者生成创意或起草完整文章
- 教育领域：帮助学生完成写作任务或语言学习
- 辅助功能：开发面向残障人士的文本转语音系统

**模型规模**

LLM（如 ChatGPT/GPT-4）的参数规模可达约 1.76 万亿，而 Mistral 7B 等开源 SLM 参数量仅约 70 亿。这种差异源于架构设计和训练流程的不同。例如，ChatGPT 采用编码器-解码器框架中的自注意力机制，而 Mistral 7B 使用滑动窗口注意力机制，这种仅含解码器的架构实现了更高效的训练。架构差异对模型复杂度和性能具有深远影响。

**理解能力**

SLM 通常针对特定领域优化，虽具备高度专业性但跨领域知识理解能力有限。相比之下，LLM 致力于模拟更全面的人类智能水平。通过海量多样化数据集训练，LLM 在跨领域应用中展现出更强的适应性和通用性，因而更适用于自然语言处理和编程等多样化下游任务。

**计算需求**

LLM 的训练和部署需要大量计算资源，通常依赖大规模 GPU 集群。例如从头训练 ChatGPT 可能需要数千个 GPU 持续工作数月。而参数量较小的 SLM（如 Mistral 7B）可在配备中等性能 GPU 的本地机器上完成训练和运行，不过训练仍需要多个 GPU 持续数小时。

**偏差问题**

LLM 的偏差问题主要源于训练数据特性。这些模型通常依赖互联网公开数据，可能对某些群体存在代表性不足、错误标签或受方言、地域差异及语法规则影响的语用偏差。此外，LLM 架构的复杂性可能在不经意间放大偏差，若未仔细微调则难以察觉。而 SLM 基于受限的领域专用数据集训练，固有偏差风险较低（但并非完全免疫）。

**推理效率**

较小的模型体积赋予 SLM 显著的推理速度优势，可在本地硬件上高效生成输出而无需大规模并行计算。反观 LLM 因规模和复杂度，常需大量并行计算资源才能获得可接受的推理时间。在规模化部署时，多用户并发会进一步降低 LLM 的响应速度。


总结起来，尽管 LLM 与 SLM 共享机器学习基础，但在模型规模、资源需求、语境理解、偏差敏感性和推理速度等方面差异显著。这些区别决定了它们分别适用于不同场景：LLM 通用性强但资源消耗大，SLM 则提供领域专用效率与更低计算需求。

（注：本章节将以微软 Phi-3/3.5 系列模型为例介绍 SLM 的应用）

## Phi-3 / Phi-3.5 系列模型介绍

Phi-3 / 3.5 系列主要面向文本、视觉和智能体（MoE）应用场景：

### Phi-3 / 3.5 指令模型

主要用于文本生成、对话完成和内容信息提取等任务。

**Phi-3-mini**

这款 3.8B 参数的语言模型可在 Microsoft Azure AI Studio、Hugging Face 和 Ollama 平台获取。Phi-3 系列模型在关键基准测试中（数值越高越好）显著优于同尺寸及更大规模的语言模型。Phi-3-mini 的表现超越两倍于其尺寸的模型，而 Phi-3-small 和 Phi-3-medium 则优于包括 GPT-3.5 在内的更大模型。

**Phi-3-small & medium**

Phi-3-small 仅需 7B 参数即在语言、推理、编程和数学等多项基准测试中击败 GPT-3.5T。14B 参数的 Phi-3-medium 延续这一优势，性能超越 Gemini 1.0 Pro。

**Phi-3.5-mini**

可视为 Phi-3-mini 的升级版本。在保持参数规模不变的情况下：
- 增强多语言支持（支持 20+ 语言：阿拉伯语、中文、捷克语、丹麦语、荷兰语、英语、芬兰语、法语、德语、希伯来语、匈牙利语、意大利语、日语、韩语、挪威语、波兰语、葡萄牙语、俄语、西班牙语、瑞典语、泰语、土耳其语、乌克兰语）
- 强化长上下文处理能力
3.8B 参数的 Phi-3.5-mini 在多项测试中表现优于同尺寸模型，与两倍尺寸模型持平

### Phi-3 / 3.5 视觉模型

将 Phi-3/3.5 的指令模型视为其理解能力，视觉模型则为 Phi 系列增添了观察世界的"眼睛"。

**Phi-3-Vision**

仅 4.2B 参数的 Phi-3-vision 在通用视觉推理、OCR、表格和图表理解等任务中表现优于 Claude-3 Haiku 和 Gemini 1.0 Pro V 等更大模型。

**Phi-3.5-Vision**

Phi-3.5-Vision 是 Phi-3-Vision 的升级版本：
- 新增多图像输入支持（可同时处理多张输入图像进行推理）
- 在 OCR、表格和图表理解任务中表现优于 Claude-3.5 Sonnet 和 Gemini 1.5 Flash
- 通用视觉知识推理任务达到同等水平

### Phi-3.5-MoE

**混合专家系统（MoE）** 技术使模型能够以更少的计算资源进行预训练，即在相同计算预算下显著扩展模型或数据集规模。具体而言，MoE 模型在预训练期间能更快达到密集模型的同等质量水平。

Phi-3.5-MoE 包含 16 个 3.8B 专家模块，仅需 6.6B 活跃参数即可实现与更大模型相当的推理、语言理解和数学能力。根据不同的应用场景，开发者可选择部署 Phi-3/3.5 系列的不同模型。与 LLM 不同，Phi-3/3.5-mini 或 Phi-3/3.5-Vision 可部署在边缘设备上。

## Phi-3/3.5 系列模型使用方法

我们将根据不同场景演示 Phi-3/3.5 的应用。

![phi3](../../img/phi3.png?WT.mc_id=academic-105485-koreyst)

### 云端 API 推理

**GitHub 模型库**

最直接的调用方式是通过 GitHub Models 快速访问 Phi-3/3.5-Instruct 模型：
- 结合 Azure AI Inference SDK / OpenAI SDK 通过代码调用 API
- 通过 Playground 测试不同效果

- 演示：Phi-3-mini 与 Phi-3.5-mini 在中文场景的效果对比

![phi3](../../img/gh1.png?WT.mc_id=academic-105485-koreyst)

![phi35](../../img/gh2.png?WT.mc_id=academic-105485-koreyst)

**Azure AI Studio**

如需使用视觉和 MoE 模型，可通过 Azure AI Studio 完成调用。具体方法可参考 [Phi-3 Cookbook](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)。

**NVIDIA NIM**

除了 Azure 和 GitHub 的云端解决方案，还可通过 [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) 进行模型调用。NVIDIA 推理微服务提供：
- 单命令部署 AI 模型
- 基于 TensorRT 和 TensorRT-LLM 的优化性能
- Kubernetes 自动扩展
- 标准化 API 支持
- 企业级安全控制

- 演示：[使用 NVIDIA NIM 调用 Phi-3.5-Vision-API](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)

### 本地环境推理

**Hugging Face Transformers**

这个流行的 NLP 库提供：
1. 数千个预训练模型（涵盖文本分类、问答、摘要等任务）
2. 多框架支持（PyTorch/TensorFlow/JAX）
3. 多模态处理能力（CV/音频）
4. 丰富的社区资源

注意：视觉和 MoE 场景需要 GPU 加速，未量化的 CPU 推理效率有限。

- 演示：
  - [调用 Phi-3.5-Instuct](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)
  - [调用 Phi-3.5-Vision](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)
  - [调用 Phi-3.5-MoE](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**

这个本地 LLM 运行平台：
- 支持 Phi 3 等主流模型
- 提供开箱即用的模型包
- 支持 Windows/macOS/Linux
- 执行命令即可运行：

```bash

ollama run phi3.5

```


**ONNX Runtime for GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) 是一个跨平台推理和训练机器学习加速器。ONNX Runtime for Generative AI (GENAI) 是帮助您在各种平台上高效运行生成式 AI 模型的强大工具。

## 什么是 ONNX Runtime？
ONNX Runtime 是一个开源项目，可实现机器学习模型的高性能推理。它支持 Open Neural Network Exchange (ONNX) 格式的模型，该格式是表示机器学习模型的开放标准。ONNX Runtime 推理能够提供更快的用户体验并降低成本，支持来自 PyTorch、TensorFlow/Keras 等深度学习框架的模型，以及 scikit-learn、LightGBM、XGBoost 等传统机器学习库。ONNX Runtime 兼容不同硬件、驱动程序和操作系统，通过利用硬件加速器（如适用）并结合图优化和转换来实现最佳性能。

## 什么是生成式 AI？
生成式 AI 指能够基于训练数据生成新内容（如文本、图像或音乐）的 AI 系统。典型示例包括 GPT-3 等语言模型和 Stable Diffusion 等图像生成模型。ONNX Runtime for GenAI 库为 ONNX 模型提供生成式 AI 循环功能，包括：
- 使用 ONNX Runtime 进行推理
- logits 处理
- 搜索与采样
- KV 缓存管理

## 适用于 GENAI 的 ONNX 运行时
ONNX Runtime for GENAI 扩展了 ONNX Runtime 对生成式 AI 模型的支持能力，主要特性包括：

- **广泛平台支持**：兼容 Windows、Linux、macOS、Android 和 iOS 等平台
- **模型支持**：支持 LLaMA、GPT-Neo、BLOOM 等主流生成式 AI 模型
- **性能优化**：包含针对 NVIDIA GPU、AMD GPU 等硬件加速器的优化
- **易用性**：提供简洁 API 便于应用集成，只需少量代码即可生成文本、图像等内容
- 用户既可调用高层 generate() 方法，也可逐轮运行模型迭代（每次生成一个 token），并能在循环中动态调整生成参数
- 支持贪婪搜索/束搜索及 TopP、TopK 采样来生成 token 序列，内置重复惩罚等 logits 处理机制，同时支持自定义评分规则

## 快速入门
通过以下步骤开始使用 ONNX Runtime for GENAI：

### 安装 ONNX 运行时：
```Python
pip install onnxruntime
```
### 安装 Generative AI Extensions：
```Python
pip install onnxruntime-genai
```

### 运行模型：下面是一个 Python 中的简单示例：
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
### Demo：使用 ONNX Runtime GenAI 调用 Phi-3.5-Vision


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
    
    code += tokenizer_stream.decode(new_token)
    
    print(tokenizer_stream.decode(new_token), end='', flush=True)

```


**其他方法**

除 ONNX Runtime 和 Ollama 的调用方式外，我们还可以基于不同厂商提供的模型调用方法完成量化模型的调用。例如基于 Apple Metal 的 Apple MLX 框架、利用 NPU 的 Qualcomm QNN、基于 CPU/GPU 的 Intel OpenVINO 等。更多内容可参考 [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)。


## 扩展阅读

我们已经学习了 Phi-3/3.5 系列的基础知识，但要深入了解 SLM 还需要更多知识。您可以在 Phi-3 Cookbook 中找到答案。如需进一步学习，请访问 [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)。