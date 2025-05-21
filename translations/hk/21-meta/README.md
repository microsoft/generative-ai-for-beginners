<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:07:23+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "hk"
}
-->
# 同 Meta 系列模型一起构建

## 介绍

本课将涵盖：

- 探索 Meta 系列的两个主要模型 - Llama 3.1 和 Llama 3.2
- 理解每个模型的使用案例和场景
- 代码示例展示每个模型的独特特性

## Meta 系列模型

在本课中，我们将探索 Meta 系列或称为“Llama Herd”的两个模型 - Llama 3.1 和 Llama 3.2。

这些模型有不同的变体，可以在 GitHub Model 市场上找到。这里有更多关于使用 GitHub Models [与 AI 模型进行原型设计](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)的详细信息。

模型变体：
- Llama 3.1 - 70B 指导
- Llama 3.1 - 405B 指导
- Llama 3.2 - 11B 视觉指导
- Llama 3.2 - 90B 视觉指导

*注意：Llama 3 也可以在 GitHub Models 上找到，但本课不会涉及*

## Llama 3.1

拥有 4050 亿参数的 Llama 3.1 属于开源 LLM 类别。

该模型是对早期发布的 Llama 3 的升级，提供：

- 更大的上下文窗口 - 128k 代币对比 8k 代币
- 更大的最大输出代币 - 4096 对比 2048
- 更好的多语言支持 - 由于训练代币的增加

这些使得 Llama 3.1 能够在构建生成式 AI 应用时处理更复杂的使用案例，包括：
- 本地函数调用 - 能够在 LLM 工作流程之外调用外部工具和函数
- 更好的 RAG 性能 - 由于更高的上下文窗口
- 合成数据生成 - 能够为诸如微调等任务创建有效数据

### 本地函数调用

Llama 3.1 已经过微调，以更有效地进行函数或工具调用。它还具有两个内置工具，模型可以根据用户的提示识别需要使用这些工具。这些工具是：

- **Brave Search** - 可以通过执行网络搜索来获取最新信息，例如天气
- **Wolfram Alpha** - 可以用于更复杂的数学计算，因此无需自己编写函数

你还可以创建自己的自定义工具，LLM 可以调用这些工具。

在下面的代码示例中：

- 我们在系统提示中定义了可用的工具（brave_search, wolfram_alpha）。
- 发送一个用户提示，询问某个城市的天气。
- LLM 将通过工具调用 Brave Search 工具来响应，看起来像这样 `<|python_tag|>brave_search.call(query="Stockholm weather")`

*注意：这个例子只进行工具调用，如果你想获取结果，你需要在 Brave API 页面创建一个免费账户并定义函数本身*

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

尽管是一个 LLM，Llama 3.1 的一个限制是多模态性。也就是说，无法使用不同类型的输入（例如图像）作为提示并提供响应。这种能力是 Llama 3.2 的主要特征之一。这些特征还包括：

- 多模态性 - 能够评估文本和图像提示
- 小到中等大小变体（11B 和 90B） - 提供灵活的部署选项
- 仅文本变体（1B 和 3B） - 允许模型在边缘/移动设备上部署并提供低延迟

多模态支持代表了开源模型世界中的一大进步。下面的代码示例同时使用图像和文本提示，从 Llama 3.2 90B 获取图像分析。

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

## 学习不会止步于此，继续旅程

完成本课后，请查看我们的 [生成式 AI 学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)以继续提升你的生成式 AI 知识！

**免責聲明**：

此文件是使用AI翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)進行翻譯的。我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原語言的文件作為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對於使用此翻譯而引起的任何誤解或誤譯概不負責。