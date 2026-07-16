# 使用 Meta 家族模型构建

## 介绍

本课将涵盖：

- 探索两个主要的 Meta 家族模型 - Llama 3.1 和 Llama 3.2
- 了解每个模型的使用场景和适用情况
- 代码示例展示每个模型的独特功能


## Meta 家族模型

在本课中，我们将探索来自 Meta 家族或“Llama 群”的两个模型 - Llama 3.1 和 Llama 3.2。

这些模型有不同的变体，可在 [Microsoft Foundry Models 目录](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 中找到。

> **注意：** GitHub Models 将于 2026 年 7 月底退休。这里有更多关于使用 [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) 来进行 AI 模型原型设计的详细信息。

模型变体：
- Llama 3.1 - 70B 指令版
- Llama 3.1 - 405B 指令版
- Llama 3.2 - 11B 视觉指令版
- Llama 3.2 - 90B 视觉指令版

*注：Llama 3 也在 Microsoft Foundry Models 中提供，但本课不会涉及*

## Llama 3.1

Llama 3.1 拥有 4050 亿参数，属于开源大型语言模型（LLM）类别。

该模型是早期版本 Llama 3 的升级，提供：

- 更大的上下文窗口 - 128k 令牌相比 8k 令牌
- 更大的最大输出令牌数 - 4096 对比 2048
- 更好的多语言支持 - 因训练令牌增加

这些改进使 Llama 3.1 能处理更复杂的生成式 AI 应用场景，包括：
- 原生函数调用 - 能够调用 LLM 工作流之外的外部工具和函数
- 更好的 RAG 性能 - 由于上下文窗口更大
- 合成数据生成 - 能够创建用于微调等任务的有效数据

### 原生函数调用

Llama 3.1 已微调以更有效地进行函数或工具调用。它还内置了两个工具，模型可以根据用户的提示识别需要使用的工具。这些工具是：

- **Brave Search** - 可以通过网络搜索获取最新信息，如天气
- **Wolfram Alpha** - 可用于更复杂的数学计算，无需自己编写函数

你也可以创建自定义工具供 LLM 调用。

在下面的代码示例中：

- 在系统提示中定义可用工具（brave_search, wolfram_alpha）。
- 发送一个询问某城市天气的用户提示。
- LLM 会以调用 Brave Search 工具的形式响应，如 `<|python_tag|>brave_search.call(query="Stockholm weather")`

*注意：该示例仅演示工具调用，如果你想获取结果，需要在 Brave API 页面创建免费账户并定义函数本身。*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# 从您的 Microsoft Foundry 项目的“概览”页面获取这些信息
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Meta-Llama-3.1-405B-Instruct"

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

尽管是 LLM，Llama 3.1 的一个限制是缺乏多模态性。也就是说，无法使用图像等不同类型输入作为提示并提供响应。这个能力是 Llama 3.2 的主要特性之一。其他特性还包括：

- 多模态性 - 能够处理文本和图像提示
- 小到中等规模变体 (11B 和 90B) - 提供灵活的部署选项
- 仅文本变体 (1B 和 3B) - 允许模型部署在边缘/移动设备上，提供低延迟

多模态支持代表了开源模型领域的一大进步。下面的代码示例使用了图像和文本提示，从 Llama 3.2 90B 得到图像的分析。


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

# 从你的 Microsoft Foundry 项目的“概览”页面获取这些信息
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
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

## 学习不会止步于此，继续前行

完成本课后，请查看我们的 [生成式 AI 学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，继续提升你的生成式 AI 知识！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->