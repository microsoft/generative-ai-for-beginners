<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T18:56:33+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "zh"
}
-->
# 使用 Mistral 模型构建

## 介绍

本课将涵盖：
- 探索不同的 Mistral 模型
- 了解每个模型的使用场景和适用情况
- 通过代码示例展示每个模型的独特功能

## Mistral 模型

本课将介绍三种不同的 Mistral 模型：
**Mistral Large**、**Mistral Small** 和 **Mistral Nemo**。

这些模型均可在 Github Model 市场免费获取。本笔记本中的代码将使用这些模型进行演示。更多关于使用 Github Models 进行[AI 模型原型设计](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)的详细信息，请参见链接。

## Mistral Large 2 (2407)
Mistral Large 2 是 Mistral 目前的旗舰模型，专为企业级应用设计。

该模型是对原始 Mistral Large 的升级，提供了：
- 更大的上下文窗口——128k 对比 32k
- 在数学和编程任务上的更好表现——平均准确率 76.9% 对比 60.4%
- 提升的多语言性能——支持语言包括：英语、法语、德语、西班牙语、意大利语、葡萄牙语、荷兰语、俄语、中文、日语、韩语、阿拉伯语和印地语

凭借这些特性，Mistral Large 在以下方面表现出色：
- *检索增强生成（RAG）* —— 由于更大的上下文窗口
- *函数调用* —— 该模型支持原生函数调用，允许与外部工具和 API 集成。调用可以并行执行，也可以按顺序依次执行。
- *代码生成* —— 在 Python、Java、TypeScript 和 C++ 代码生成方面表现优异。

### 使用 Mistral Large 2 的 RAG 示例

在此示例中，我们使用 Mistral Large 2 对文本文件执行 RAG 模式。问题用韩语提出，询问作者大学前的活动。

示例中使用 Cohere Embeddings Model 对文本和问题进行向量化。此示例使用 faiss Python 包作为向量存储。

发送给 Mistral 模型的提示包含问题和与问题相似的检索片段，模型随后给出自然语言回答。

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
Mistral Small 是 Mistral 家族中属于高级/企业类别的另一款模型。顾名思义，它是一个小型语言模型（SLM）。使用 Mistral Small 的优势包括：
- 相较于 Mistral Large 和 NeMo 等大型模型，成本节约显著——价格降低约 80%
- 低延迟——响应速度快于 Mistral 的大型模型
- 灵活性强——可在不同环境中部署，对资源需求限制较少

Mistral Small 非常适合：
- 基于文本的任务，如摘要、情感分析和翻译
- 频繁请求的应用场景，因其成本效益高
- 低延迟的代码任务，如代码审查和建议

## Mistral Small 与 Mistral Large 的对比

要展示 Mistral Small 和 Large 在延迟上的差异，请运行以下单元格。

你会看到响应时间相差约 3-5 秒。同时注意相同提示下响应的长度和风格差异。

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

与本课中讨论的另外两个模型相比，Mistral NeMo 是唯一一个采用 Apache2 许可证的免费模型。

它被视为 Mistral 早期开源大型语言模型 Mistral 7B 的升级版。

NeMo 模型的其他特点包括：

- *更高效的分词*：该模型使用 Tekken 分词器，优于更常用的 tiktoken，支持更多语言和代码的更好表现。

- *微调*：基础模型支持微调，适用于需要微调的多样化应用场景。

- *原生函数调用* —— 与 Mistral Large 类似，该模型经过函数调用训练，是首批支持此功能的开源模型之一。

### 分词器对比

本示例将展示 Mistral NeMo 与 Mistral Large 在分词处理上的差异。

两者使用相同的提示，但你会发现 NeMo 返回的 token 数量少于 Mistral Large。

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

## 学习永无止境，继续前行

完成本课后，欢迎访问我们的[生成式 AI 学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持续提升你的生成式 AI 知识！

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。我们不对因使用本翻译而产生的任何误解或误释承担责任。