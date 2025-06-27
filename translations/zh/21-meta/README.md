<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:26:48+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "zh"
}
-->
# 使用Meta家族模型构建

## 介绍

本课将涵盖：

- 探索Meta家族的两个主要模型——Llama 3.1和Llama 3.2
- 理解每个模型的使用案例和场景
- 代码示例展示每个模型的独特功能

## Meta家族模型

在本课中，我们将探索Meta家族或“Llama群”中的两个模型——Llama 3.1和Llama 3.2。

这些模型有不同的变体，可以在GitHub模型市场上获得。有关使用GitHub模型[原型设计AI模型](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)的更多详细信息。

模型变体：
- Llama 3.1 - 70B 指令
- Llama 3.1 - 405B 指令
- Llama 3.2 - 11B 视觉指令
- Llama 3.2 - 90B 视觉指令

*注意：Llama 3也可以在GitHub模型上获得，但不会在本课中涉及*

## Llama 3.1

拥有4050亿参数的Llama 3.1属于开源LLM类别。

该模型是对早期版本Llama 3的升级，提供了：

- 更大的上下文窗口——128k标记对比8k标记
- 更大的最大输出标记——4096对比2048
- 更好的多语言支持——由于训练标记的增加

这些使得Llama 3.1在构建生成式AI应用时能够处理更复杂的使用案例，包括：
- 原生函数调用——能够调用LLM工作流之外的外部工具和函数
- 更好的RAG性能——由于更高的上下文窗口
- 合成数据生成——能够为微调等任务创建有效数据

### 原生函数调用

Llama 3.1已经过微调，以便更有效地进行函数或工具调用。它还具有两个内置工具，模型可以根据用户的提示识别需要使用这些工具。这些工具是：

- **Brave Search** - 可以通过网络搜索获取最新信息，如天气
- **Wolfram Alpha** - 可以用于更复杂的数学计算，因此无需编写自己的函数

您还可以创建自己的自定义工具供LLM调用。

在下面的代码示例中：

- 我们在系统提示中定义了可用的工具（brave_search, wolfram_alpha）。
- 发送用户提示询问某个城市的天气。
- LLM将响应一个工具调用到Brave Search工具，看起来像这样`<|python_tag|>brave_search.call(query="Stockholm weather")`

*注意：此示例仅进行工具调用，如果您想获得结果，需要在Brave API页面创建一个免费账户并定义函数本身*

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

尽管是一个LLM，Llama 3.1的一个限制是多模态性。即能够使用不同类型的输入，如图像作为提示并提供响应。这种能力是Llama 3.2的主要功能之一。这些功能还包括：

- 多模态性——能够评估文本和图像提示
- 小到中等尺寸变体（11B和90B）——提供灵活的部署选项
- 仅文本变体（1B和3B）——允许模型在边缘/移动设备上部署，并提供低延迟

多模态支持代表了开源模型领域的一大步。下面的代码示例同时使用图像和文本提示，从Llama 3.2 90B获得对图像的分析。

### Llama 3.2的多模态支持

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

## 学习不会在这里停止，继续旅程

完成本课后，请查看我们的[生成式AI学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，继续提升您的生成式AI知识！

**免责声明**：
本文档是使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)翻译的。虽然我们努力确保准确性，但请注意自动翻译可能包含错误或不准确之处。原始文档的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用此翻译而引起的任何误解或误读承担责任。