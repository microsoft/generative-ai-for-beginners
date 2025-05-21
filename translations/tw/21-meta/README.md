<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:07:38+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "tw"
}
-->
# 使用 Meta 家族模型构建

## 介绍

本课程将涵盖：

- 探索 Meta 家族的两个主要模型 - Llama 3.1 和 Llama 3.2
- 理解每个模型的使用案例和场景
- 展示每个模型独特功能的代码示例

## Meta 家族模型

在本课程中，我们将探索 Meta 家族或“Llama Herd”的两个模型 - Llama 3.1 和 Llama 3.2

这些模型有不同的变体，可以在 GitHub Model 市场上找到。这里有更多关于使用 GitHub Models进行[AI模型原型设计](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)的详细信息。

模型变体：
- Llama 3.1 - 70B 指令
- Llama 3.1 - 405B 指令
- Llama 3.2 - 11B 视觉指令
- Llama 3.2 - 90B 视觉指令

*注意：Llama 3 也可以在 GitHub Models 上找到，但不会在本课程中涉及*

## Llama 3.1

拥有4050亿参数的 Llama 3.1 属于开源 LLM 类别。

该模式是对早期发布的 Llama 3 的升级，提供：

- 更大的上下文窗口 - 128k tokens 对比 8k tokens
- 更大的最大输出 tokens - 4096 对比 2048
- 更好的多语言支持 - 由于训练 tokens 的增加

这些使得 Llama 3.1 能够在构建 GenAI 应用时处理更复杂的使用案例，包括：
- 本地函数调用 - 能够在 LLM 工作流程之外调用外部工具和函数
- 更好的 RAG 性能 - 由于更高的上下文窗口
- 合成数据生成 - 能够为微调等任务创建有效数据

### 本地函数调用

Llama 3.1 已被微调以更有效地进行函数或工具调用。它还有两个内置工具，模型可以根据用户的提示识别需要使用。这些工具是：

- **Brave Search** - 可以通过进行网络搜索来获取最新信息，例如天气
- **Wolfram Alpha** - 可以用于更复杂的数学计算，因此无需编写自己的函数

您也可以创建自己的自定义工具供 LLM 调用。

在下面的代码示例中：

- 我们在系统提示中定义可用工具（brave_search, wolfram_alpha）。
- 发送一个用户提示，询问某个城市的天气。
- LLM 将响应一个对 Brave Search 工具的调用，看起来像这样 `<|python_tag|>brave_search.call(query="Stockholm weather")`

*注意：此示例仅进行工具调用，如果您想获得结果，需要在 Brave API 页面创建一个免费帐户并定义函数本身*

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

尽管是 LLM，Llama 3.1 的一个限制是多模态性。即能够使用不同类型的输入，如图像作为提示并提供响应。这种能力是 Llama 3.2 的主要功能之一。这些功能还包括：

- 多模态性 - 能够评估文本和图像提示
- 小到中等尺寸的变体（11B 和 90B） - 提供灵活的部署选项
- 仅文本变体（1B 和 3B） - 允许模型在边缘/移动设备上部署并提供低延迟

多模态支持代表了开源模型领域的一大进步。下面的代码示例同时使用图像和文本提示，从 Llama 3.2 90B 获取图像分析。

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

## 学习不止于此，继续探索之旅

完成本课程后，请查看我们的[生成式 AI 学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，继续提升您的生成式 AI 知识！

**免責聲明**：  
本文檔使用AI翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)進行翻譯。我們努力追求準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應將原始語言的文檔視為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對使用此翻譯引起的任何誤解或誤讀不承擔責任。