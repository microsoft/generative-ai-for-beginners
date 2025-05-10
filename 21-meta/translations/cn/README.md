# 使用 Meta 家族模型进行构建

## 简介

本课程将涵盖：

- 探索两个主要的 Meta 家族模型 - Llama 3.1 和 Llama 3.2
- 理解每个模型的用例和场景
- 代码示例展示每个模型的独特功能

## Meta 家族模型

在本课程中，我们将探索两个来自 Meta 家族或“Llama 群”中的模型 - Llama 3.1 和 Llama 3.2

这些模型有不同的变体，并在 GitHub Model 市场可用。有关使用 GitHub Models 进行 [AI 模型原型设计](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) 的更多详细信息，请参阅此处。

模型变体：
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*注意：Llama 3 也在 GitHub Models 上可用，但本课程不涵盖*

## Llama 3.1

拥有 4050 亿参数，Llama 3.1 属于开源 LLM 类别。

该模型是对早期发布的 Llama 3 的升级，提供了：

- 更大的上下文窗口 - 128k 令牌 对比 8k 令牌
- 更大的最大输出令牌 - 4096 对比 2048
- 更好的多语言支持 - 由于训练令牌的增加

这些功能使 Llama 3.1 在构建生成式 AI 应用程序时能够处理更复杂的用例，包括：
- 原生函数调用 - 能够调用 LLM 工作流之外的外部工具和函数
- 更好的 RAG 性能 - 由于更大的上下文窗口
- 合成数据生成 - 能够为微调等任务创建有效数据

### 原生函数调用

Llama 3.1 经过微调，能够更有效地进行函数或工具调用。它还具有两个内置工具，模型可以根据用户提示识别是否需要使用这些工具。这些工具包括：

- **Brave Search** - 可以通过执行网络搜索来获取最新的信息，如天气
- **Wolfram Alpha** - 可以用于更复杂的数学计算，因此不需要编写自己的函数

您还可以创建 LLM 可以调用的自定义工具。

在下面的代码示例中：

- 我们在系统提示中定义了可用的工具（brave_search, wolfram_alpha）。
- 发送一个用户提示，询问某个城市的天气。
- LLM 将响应一个对 Brave Search 工具的调用，看起来像这样 `<|python_tag|>brave_search.call(query="Stockholm weather")`

*注意：此示例仅进行工具调用，如果您想获取结果，需要在 Brave API 页面创建一个免费账户并定义该函数*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "meta-llama-3.1-405b-instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)


tool_prompt=f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Environment: ipython
Tools: brave_search, wolfram_alpha
Cutting Knowledge Date: December 2023
Today Date: 23 July 2024

You are a helpful assistant<|eot_id|>
"""

messages = [
    SystemMessage(content=tool_prompt),
    UserMessage(content="What is the weather in Stockholm?"),

]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```

## Llama 3.2

尽管 Llama 3.1 是一个 LLM，但它的一个限制是多模态性。也就是说，它能够使用不同类型的输入（如图像）作为提示并提供响应。这种能力是 Llama 3.2 的主要特性之一。这些特性还包括：

- 多模态性 - 能够评估文本和图像提示
- 小到中等大小的变体（11B 和 90B） - 这提供了灵活的部署选项
- 仅文本的变体（1B 和 3B） - 这允许模型部署在边缘/移动设备上并提供低延迟

多模态支持在开源模型领域是一个重要的进步。下面的代码示例结合了图像和文本提示，以获取 Llama 3.2 90B 对图像的分析。

### 多模态支持与 Llama 3.2

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    SystemMessage,
    UserMessage,
    TextContentItem,
    ImageContentItem,
    ImageUrl,
    ImageDetailLevel,
)
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "Llama-3.2-90B-Vision-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(
            content="You are a helpful assistant that describes images in details."
        ),
        UserMessage(
            content=[
                TextContentItem(text="What's in this image?"),
                ImageContentItem(
                    image_url=ImageUrl.load(
                        image_file="sample.jpg",
                        image_format="jpg",
                        detail=ImageDetailLevel.LOW)
                ),
            ],
        ),
    ],
    model=model_name,
)

print(response.choices[0].message.content)
```

## 学习之旅不会在这里停止，继续前行

完成本课程后，请查看我们的 [生成式 AI 学习集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) 以持续提升您的生成式 AI 技能！

