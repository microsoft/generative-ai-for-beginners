# 使用 Meta 家族模型构建

## 介绍

本课将涵盖：

- 探索两个主要的 Meta 家族模型 - Llama 3.1 和 Llama 3.2
- 理解每个模型的使用案例和场景
- 通过代码示例展示每个模型的独特功能

## Meta 家族模型

在本课中，我们将探索来自 Meta 家族或“Llama 群”的两个模型 - Llama 3.1 和 Llama 3.2。

这些模型有不同的变体，并可在 GitHub 模型市场获得。以下是有关使用 GitHub 模型进行[AI 模型原型设计](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)的更多详细信息。

模型变体：  
- Llama 3.1 - 70B 指令版  
- Llama 3.1 - 405B 指令版  
- Llama 3.2 - 11B 视觉指令版  
- Llama 3.2 - 90B 视觉指令版  

*注意：Llama 3 也在 GitHub 模型上可用，但本课不涵盖此内容*

## Llama 3.1

Llama 3.1 拥有 4050 亿参数，属于开源大语言模型（LLM）类别。

该模型是之前发布的 Llama 3 的升级版，提供了：

- 更大的上下文窗口 - 128k 令牌对比 8k 令牌  
- 更大的最大输出令牌数 - 4096 对比 2048  
- 更好的多语言支持 - 由于训练令牌数增加  

这些使 Llama 3.1 能够处理更复杂的生成式 AI 应用场景，包括：  
- 原生函数调用 - 能够调用 LLM 工作流之外的外部工具和函数  
- 更好的 RAG 性能 - 基于更大的上下文窗口  
- 合成数据生成 - 能够为微调等任务创建有效的数据

### 原生函数调用

Llama 3.1 已进行了微调，更有效地执行函数或工具调用。它还内置了两个工具，模型能基于用户提示识别需要使用的工具。这些工具是：

- **Brave Search** - 可用于通过网络搜索获取最新信息，如天气  
- **Wolfram Alpha** - 用于更复杂的数学计算，无需自己编写函数  

你也可以创建自己的自定义工具供 LLM 调用。

在下面的代码示例中：

- 我们在系统提示中定义了可用的工具（brave_search, wolfram_alpha）。
- 发送询问某个城市天气的用户提示。
- LLM 会调用 Brave Search 工具，调用形式如 `<|python_tag|>brave_search.call(query="Stockholm weather")`。

*注意：该示例仅展示了工具调用，若需获得结果，需在 Brave API 页面创建免费账户并定义调用函数本身。*

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

尽管 Llama 3.1 是大语言模型，但其缺乏多模态能力——即无法使用图像等不同类型的输入作为提示并给出响应。Llama 3.2 具备此能力。其特性还包括：

- 多模态能力 - 能够同时评估文本和图像提示  
- 小到中等规模变体（11B 和 90B） - 提供灵活的部署选项  
- 仅文本变体（1B 和 3B） - 允许模型部署于边缘/移动设备，并支持低延迟  

多模态支持代表了开源模型领域的重大进步。下面的代码示例接受图像和文本提示，获取 Llama 3.2 90B 对该图像的分析。

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
  
## 学习不会止步于此，继续前进之旅

完成本课后，请查看我们的[生成式 AI 学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，继续提升你的生成式 AI 知识！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意自动翻译可能存在错误或不准确之处。请以原始语言的原文文件为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而导致的任何误解或错误解释，我们不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->