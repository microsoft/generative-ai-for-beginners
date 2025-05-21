<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T10:52:51+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "tw"
}
-->
# 使用 Mistral 模型构建

## 介绍

本课将涵盖：
- 探索不同的 Mistral 模型
- 了解每个模型的使用案例和场景
- 代码示例展示每个模型的独特功能

## Mistral 模型

在本课中，我们将探索三种不同的 Mistral 模型：**Mistral Large**、**Mistral Small** 和 **Mistral Nemo**。

这些模型都可以在 Github 模型市场上免费获取。本笔记本中的代码将使用这些模型来运行代码。有关使用 Github 模型进行 [AI 模型原型设计](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) 的更多详细信息，请参阅此链接。

## Mistral Large 2 (2407)
Mistral Large 2 目前是 Mistral 的旗舰模型，专为企业使用而设计。

该模型是对原始 Mistral Large 的升级，提供：
- 更大的上下文窗口 - 128k 对比 32k
- 更好的数学和编程任务性能 - 平均准确率为 76.9% 对比 60.4%
- 增强的多语言性能 - 包括英语、法语、德语、西班牙语、意大利语、葡萄牙语、荷兰语、俄语、中文、日语、韩语、阿拉伯语和印地语

凭借这些功能，Mistral Large 在以下方面表现出色：
- *增强检索生成 (RAG)* - 因为有更大的上下文窗口
- *函数调用* - 该模型具有原生函数调用功能，允许与外部工具和 API 集成。这些调用可以并行进行，也可以按顺序一个接一个进行。
- *代码生成* - 该模型在 Python、Java、TypeScript 和 C++ 生成方面表现出色。

### 使用 Mistral Large 2 的 RAG 示例

在此示例中，我们使用 Mistral Large 2 对文本文档运行 RAG 模式。问题用韩文写成，询问作者在上大学前的活动。

它使用 Cohere Embeddings Model 来创建文本文档和问题的嵌入。在此示例中，它使用 faiss Python 包作为向量存储。

发送给 Mistral 模型的提示包括问题和与问题相似的检索块。然后模型提供自然语言响应。

```python 
pip install faiss-cpu
```

```python 
import requests
import numpy as np
import faiss
import os

from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference import EmbeddingsClient

endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-large"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = requests.get('https://raw.githubusercontent.com/run-llama/llama_index/main/docs/docs/examples/data/paul_graham/paul_graham_essay.txt')
text = response.text

chunk_size = 2048
chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
len(chunks)

embed_model_name = "cohere-embed-v3-multilingual" 

embed_client = EmbeddingsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(token)
)

embed_response = embed_client.embed(
    input=chunks,
    model=embed_model_name
)



text_embeddings = []
for item in embed_response.data:
    length = len(item.embedding)
    text_embeddings.append(item.embedding)
text_embeddings = np.array(text_embeddings)


d = text_embeddings.shape[1]
index = faiss.IndexFlatL2(d)
index.add(text_embeddings)

question = "저자가 대학에 오기 전에 주로 했던 두 가지 일은 무엇이었나요?？"

question_embedding = embed_client.embed(
    input=[question],
    model=embed_model_name
)

question_embeddings = np.array(question_embedding.data[0].embedding)


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # distance, index
retrieved_chunks = [chunks[i] for i in I.tolist()[0]]

prompt = f"""
Context information is below.
---------------------
{retrieved_chunks}
---------------------
Given the context information and not prior knowledge, answer the query.
Query: {question}
Answer:
"""


chat_response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content=prompt),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(chat_response.choices[0].message.content)
```

## Mistral Small
Mistral Small 是 Mistral 模型系列中另一个属于高级/企业类别的模型。顾名思义，该模型是一个小型语言模型 (SLM)。使用 Mistral Small 的优势在于：
- 与 Mistral 大型语言模型 (LLM) 如 Mistral Large 和 NeMo 相比，节省成本 - 价格下降 80%
- 低延迟 - 相比 Mistral 的大型语言模型响应更快
- 灵活 - 可以在不同环境中部署，对所需资源的限制较少

Mistral Small 非常适合：
- 基于文本的任务，如摘要、情感分析和翻译
- 由于其成本效益而频繁请求的应用
- 低延迟代码任务，如审查和代码建议

## 比较 Mistral Small 和 Mistral Large

为了展示 Mistral Small 和 Large 之间的延迟差异，运行以下单元格。

你应该会看到响应时间在 3-5 秒之间的差异。还请注意在相同提示下的响应长度和风格。

```python 

import os 
endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-small"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful coding assistant."),
        UserMessage(content="Can you write a Python function to the fizz buzz test?"),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(response.choices[0].message.content)

```

```python 

import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-large"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful coding assistant."),
        UserMessage(content="Can you write a Python function to the fizz buzz test?"),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(response.choices[0].message.content)

```

## Mistral NeMo

与本课讨论的其他两个模型相比，Mistral NeMo 是唯一一个具有 Apache2 许可证的免费模型。

它被视为早期开源大型语言模型 Mistral 7B 的升级版。

NeMo 模型的其他一些特点是：

- *更高效的分词：* 该模型使用 Tekken 分词器，而不是更常用的 tiktoken。这使得它在更多语言和代码上表现更好。

- *微调：* 基础模型可用于微调。这为需要微调的使用案例提供了更多灵活性。

- *原生函数调用* - 像 Mistral Large 一样，该模型经过函数调用训练。这使其成为首批开源模型之一。

### 比较分词器

在此示例中，我们将看看 Mistral NeMo 如何处理与 Mistral Large 的分词。

两个示例使用相同的提示，但你应该看到 NeMo 返回的标记比 Mistral Large 少。

```bash
pip install mistral-common
```

```python 
# Import needed packages:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Load Mistral tokenizer

model_name = "open-mistral-nemo	"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenize a list of messages
tokenized = tokenizer.encode_chat_completion(
    ChatCompletionRequest(
        tools=[
            Tool(
                function=Function(
                    name="get_current_weather",
                    description="Get the current weather",
                    parameters={
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA",
                            },
                            "format": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"],
                                "description": "The temperature unit to use. Infer this from the users location.",
                            },
                        },
                        "required": ["location", "format"],
                    },
                )
            )
        ],
        messages=[
            UserMessage(content="What's the weather like today in Paris"),
        ],
        model=model_name,
    )
)
tokens, text = tokenized.tokens, tokenized.text

# Count the number of tokens
print(len(tokens))
```

```python
# Import needed packages:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Load Mistral tokenizer

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenize a list of messages
tokenized = tokenizer.encode_chat_completion(
    ChatCompletionRequest(
        tools=[
            Tool(
                function=Function(
                    name="get_current_weather",
                    description="Get the current weather",
                    parameters={
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA",
                            },
                            "format": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"],
                                "description": "The temperature unit to use. Infer this from the users location.",
                            },
                        },
                        "required": ["location", "format"],
                    },
                )
            )
        ],
        messages=[
            UserMessage(content="What's the weather like today in Paris"),
        ],
        model=model_name,
    )
)
tokens, text = tokenized.tokens, tokenized.text

# Count the number of tokens
print(len(tokens))
```

## 学习不会止步于此，继续旅程

完成本课后，请查看我们的 [生成式 AI 学习集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) 以继续提升你的生成式 AI 知识！

**免責聲明**：
本文檔已使用AI翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)進行翻譯。儘管我們努力確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。應將原始文檔視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或誤讀不承擔責任。