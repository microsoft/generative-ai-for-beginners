# 使用 Meta 家族模型构建

## 介绍

本课程将涵盖：

- 探索两个主要的 Meta 家族模型 - Llama 3.1 和 Llama 3.2
- 了解每个模型的用例和应用场景
- 代码示例展示每个模型的独特功能


## Meta 家族模型

在本课程中，我们将探索 Meta 家族或“Llama Herd”中的两个模型——Llama 3.1 和 Llama 3.2。

这些模型有不同的变体，并且可以在[Microsoft Foundry Models 目录](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)中找到。

> **注意：** GitHub Models 将于 2026 年 7 月底退役。有关使用 [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) 进行 AI 模型原型设计的更多详细信息，请参见这里。

模型变体：
- Llama 3.1 - 70B 指令型
- Llama 3.1 - 405B 指令型
- Llama 3.2 - 11B 视觉指令型
- Llama 3.2 - 90B 视觉指令型

*注意：Llama 3 也可在 Microsoft Foundry Models 中获得，但本课程不涉及*

## Llama 3.1

Llama 3.1 拥有 4050 亿参数，属于开源大型语言模型类别。

该模型是早期发布的 Llama 3 的升级版，提供了：

- 更大的上下文窗口 - 128k 令牌对比 8k 令牌
- 更大的最大输出令牌数 - 4096 对比 2048
- 更好的多语言支持 - 由于训练令牌数量增加

这些改进使得 Llama 3.1 能够处理更复杂的构建生成式 AI 应用的用例，包括：
- 原生函数调用 - 能够调用 LLM 工作流程之外的外部工具和函数
- 更好的检索增强生成（RAG）性能 - 受益于更大的上下文窗口
- 合成数据生成 - 能够为微调等任务创建有效数据

### 原生函数调用

Llama 3.1 进行了微调，以更有效地进行函数或工具调用。它还内置了两个工具，模型可以根据用户的提示识别出需要使用这些工具。它们是：

- **Brave Search** - 可以通过网络搜索获取最新信息，比如天气
- **Wolfram Alpha** - 可以进行更复杂的数学计算，因此无需编写您自己的函数

您也可以创建自己的自定义工具，供 LLM 调用。

在下面的代码示例中：

- 我们在系统提示中定义可用工具（brave_search, wolfram_alpha）。
- 发送一个用户提示，询问某个城市的天气。
- LLM 将以调用 Brave Search 工具的形式响应，类似 `<|python_tag|>brave_search.call(query="Stockholm weather")`

*注意：此示例仅调用工具，若想获取结果，您需要在 Brave API 页面创建免费账户并定义该函数本身。*

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

尽管属于大型语言模型，Llama 3.1 的一个限制是缺乏多模态能力。也就是说，它不能使用图像等不同类型的输入作为提示并提供响应。而这正是 Llama 3.2 的主要特性之一。这些特征还包括：

- 多模态能力 - 能够处理文本和图像提示
- 小到中等规模变体（11B 和 90B） - 提供灵活的部署选项
- 纯文本变体（1B 和 3B） - 允许模型在边缘/移动设备上部署，并提供低延迟

多模态支持代表了开源模型领域的一大进步。下面的代码示例使用图像和文本提示，来自 Llama 3.2 90B，对图像进行分析。


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

## 学习永不止步，继续前行

完成本课程后，请查看我们的[生成式 AI 学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，继续提升您的生成式 AI 知识！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->