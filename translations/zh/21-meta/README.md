<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:06:47+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "zh"
}
-->
# 使用 Meta 家族模型构建

## 介绍

本课将涵盖：

- 探索 Meta 家族的两个主要模型——Llama 3.1 和 Llama 3.2  
- 了解每个模型的使用场景和适用情况  
- 通过代码示例展示每个模型的独特功能  

## Meta 家族模型

本课将介绍 Meta 家族或称“Llama Herd”的两个模型——Llama 3.1 和 Llama 3.2。

这些模型有不同的变体，并且可以在 GitHub Model 市场上获取。以下是关于如何使用 GitHub Models 来[用 AI 模型进行原型设计](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)的更多信息。

模型变体：  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*注意：Llama 3 也可在 GitHub Models 上使用，但本课不涉及该模型*

## Llama 3.1

Llama 3.1 拥有 4050 亿参数，属于开源大型语言模型（LLM）类别。

该模型是对早期版本 Llama 3 的升级，提供了：

- 更大的上下文窗口——128k 令牌，相比之前的 8k 令牌  
- 更大的最大输出令牌数——4096，相比之前的 2048  
- 更好的多语言支持——得益于训练令牌数量的增加  

这些改进使 Llama 3.1 能够处理更复杂的生成式 AI 应用场景，包括：  
- 原生函数调用——能够调用 LLM 工作流之外的外部工具和函数  
- 更优的 RAG 性能——得益于更大的上下文窗口  
- 合成数据生成——能够为微调等任务创建有效数据  

### 原生函数调用

Llama 3.1 经过微调，能更有效地进行函数或工具调用。它内置了两个工具，模型可以根据用户的提示识别并调用它们。这些工具是：

- **Brave Search**——可用于通过网络搜索获取最新信息，如天气  
- **Wolfram Alpha**——可用于更复杂的数学计算，无需自己编写函数  

你也可以创建自定义工具供 LLM 调用。

下面的代码示例中：

- 在系统提示中定义了可用工具（brave_search，wolfram_alpha）。  
- 发送一个询问某城市天气的用户提示。  
- LLM 会响应一个调用 Brave Search 工具的请求，形式类似 `<|python_tag|>brave_search.call(query="Stockholm weather")`。

*注意：此示例仅展示工具调用，如果想获取结果，需要在 Brave API 页面创建免费账户并定义相应函数。*

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

尽管 Llama 3.1 是一个大型语言模型，但它的一个限制是缺乏多模态能力，即无法使用图像等不同类型的输入作为提示并给出响应。Llama 3.2 的主要特点之一就是具备这种能力。其功能还包括：

- 多模态——能够同时处理文本和图像提示  
- 小到中等规模变体（11B 和 90B）——提供灵活的部署选项  
- 纯文本变体（1B 和 3B）——支持边缘/移动设备部署，延迟低  

多模态支持是开源模型领域的一大进步。下面的代码示例展示了如何使用 Llama 3.2 90B 同时输入图像和文本提示，获取对图像的分析。

### Llama 3.2 的多模态支持

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

## 学习永不止步，继续前行

完成本课后，欢迎访问我们的[生成式 AI 学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，继续提升你的生成式 AI 知识！

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们概不负责。