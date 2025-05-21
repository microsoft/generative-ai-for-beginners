<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T10:51:54+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "zh"
}
-->
# 使用 Mistral 模型构建

## 介绍

本课程将涵盖：
- 探索不同的 Mistral 模型
- 了解每个模型的用例和场景
- 代码示例展示每个模型的独特功能

## Mistral 模型

在本课程中，我们将探索三种不同的 Mistral 模型：**Mistral Large**、**Mistral Small** 和 **Mistral Nemo**。

这些模型均可在 Github 模型市场免费获取。本笔记本中的代码将使用这些模型来运行代码。这里有更多关于使用 Github 模型进行 [AI 模型原型设计](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) 的详细信息。

## Mistral Large 2 (2407)

Mistral Large 2 目前是 Mistral 的旗舰模型，专为企业使用而设计。

该模型是对原始 Mistral Large 的升级，提供了：
- 更大的上下文窗口 - 128k 对比 32k
- 更好的数学和编码任务性能 - 平均准确率 76.9% 对比 60.4%
- 提升的多语言性能 - 包括英语、法语、德语、西班牙语、意大利语、葡萄牙语、荷兰语、俄语、中文、日语、韩语、阿拉伯语和印地语

凭借这些功能，Mistral Large 擅长：
- *检索增强生成 (RAG)* - 由于更大的上下文窗口
- *函数调用* - 该模型具有本地函数调用功能，可与外部工具和 API 集成。可以并行或按顺序依次进行调用。
- *代码生成* - 在 Python、Java、TypeScript 和 C++ 生成方面表现出色。

### 使用 Mistral Large 2 的 RAG 示例

在此示例中，我们使用 Mistral Large 2 在文本文档上运行 RAG 模式。问题以韩语写成，询问作者在大学前的活动。

它使用 Cohere Embeddings Model 来创建文本文档和问题的嵌入。在此示例中，它使用 faiss Python 包作为向量存储。

发送到 Mistral 模型的提示包括问题和与问题相似的检索到的块。然后模型提供自然语言响应。

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

Mistral Small 是 Mistral 模型家族中的另一款模型，属于高级/企业类别。顾名思义，该模型是一个小型语言模型 (SLM)。使用 Mistral Small 的优势在于：
- 与 Mistral LLMs（如 Mistral Large 和 NeMo）相比，节省成本 - 价格下降 80%
- 低延迟 - 相较于 Mistral 的 LLMs 响应更快
- 灵活 - 可以在不同环境中部署，对所需资源的限制较少

Mistral Small 非常适合：
- 基于文本的任务，如总结、情感分析和翻译
- 由于其成本效益，适用于频繁请求的应用程序
- 低延迟代码任务，如代码审查和建议

## 比较 Mistral Small 和 Mistral Large

为了显示 Mistral Small 和 Large 之间的延迟差异，请运行以下单元格。

你应该看到响应时间在 3-5 秒之间的差异。还要注意相同提示下的响应长度和风格。

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

与本课程讨论的其他两个模型相比，Mistral NeMo 是唯一具有 Apache2 许可证的免费模型。

它被视为 Mistral 早期开源 LLM，Mistral 7B 的升级版。

NeMo 模型的其他一些功能包括：

- *更高效的标记化：* 该模型使用 Tekken 标记器，而不是更常用的 tiktoken。这使其在更多语言和代码上表现更好。

- *微调：* 基础模型可用于微调。这为需要微调的用例提供了更大的灵活性。

- *本地函数调用* - 与 Mistral Large 类似，该模型经过函数调用训练。这使其成为首批具备此功能的开源模型之一。

### 比较标记器

在此示例中，我们将查看 Mistral NeMo 如何处理标记化与 Mistral Large 的比较。

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

## 学习不会止步于此，继续你的旅程

完成本课程后，请查看我们的 [生成式 AI 学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) 以继续提升你的生成式 AI 知识！

**免责声明**：
本文档是使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)翻译的。虽然我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原始文档的母语版本视为权威来源。对于关键信息，建议使用专业的人力翻译。对于因使用此翻译而产生的任何误解或误释，我们概不负责。