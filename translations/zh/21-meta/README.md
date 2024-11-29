# 使用Meta家族模型构建

## 介绍

本课将涵盖：

- 探索Meta家族的两个主要模型 - Llama 3.1 和 Llama 3.2
- 了解每个模型的使用案例和场景
- 代码示例展示每个模型的独特特性

## Meta家族模型

在本课中，我们将探索Meta家族或“Llama Herd”中的两个模型 - Llama 3.1 和 Llama 3.2

这些模型有不同的变体，可以在Github Model市场上获取。这里有更多关于使用Github Models来[原型化AI模型](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)的详细信息。

模型变体：
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*注意：Llama 3也可以在Github Models上获取，但本课不涉及*

## Llama 3.1

拥有4050亿参数的Llama 3.1属于开源LLM类别。

该模型是对早期版本Llama 3的升级，提供了：

- 更大的上下文窗口 - 128k tokens对比8k tokens
- 更大的最大输出tokens - 4096对比2048
- 更好的多语言支持 - 由于训练tokens的增加

这些使得Llama 3.1在构建GenAI应用时能够处理更复杂的用例，包括：
- 原生函数调用 - 能够调用LLM工作流之外的外部工具和函数
- 更好的RAG性能 - 由于更高的上下文窗口
- 合成数据生成 - 能够为诸如微调等任务创建有效的数据

### 原生函数调用

Llama 3.1经过微调后在进行函数或工具调用时更为有效。它还有两个内置工具，模型可以根据用户的提示识别需要使用这些工具。这些工具是：

- **Brave Search** - 可用于通过网络搜索获取最新信息，如天气
- **Wolfram Alpha** - 可用于更复杂的数学计算，因此无需自己编写函数

你也可以创建自己的自定义工具供LLM调用。

在下面的代码示例中：

- 我们在系统提示中定义了可用的工具（brave_search, wolfram_alpha）。
- 发送一个用户提示，询问某个城市的天气。
- LLM将通过Brave Search工具发出一个工具调用，类似于`<|python_tag|>brave_search.call(query="Stockholm weather")`

*注意：此示例仅进行工具调用，如果你想获取结果，需要在Brave API页面创建一个免费账户并定义函数本身`

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

尽管是一个LLM，Llama 3.1的一个限制是多模态性。即能够使用不同类型的输入（如图像）作为提示并提供响应。这种能力是Llama 3.2的主要特性之一。这些特性还包括：

- 多模态性 - 能够评估文本和图像提示
- 小到中等大小的变体（11B和90B） - 提供灵活的部署选项
- 仅文本变体（1B和3B） - 允许模型部署在边缘/移动设备上，并提供低延迟

多模态支持代表了开源模型世界中的一大进步。下面的代码示例同时接收图像和文本提示，以从Llama 3.2 90B中获取图像分析。

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

## 学习不会止步于此，继续探索之旅

完成本课后，请查看我们的[生成式AI学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，继续提升你的生成式AI知识！

**免责声明**：  
本文档是使用机器翻译服务翻译的。虽然我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原文档视为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用此翻译而产生的任何误解或误读，我们概不负责。