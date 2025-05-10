# 使用 Mistral 模型进行构建

## 简介

本课程将涵盖：
- 探索不同的 Mistral 模型
- 理解每个模型的用例和场景
- 代码示例展示每个模型的独特功能。

## Mistral 模型

在本课程中，我们将探索 3 种不同的 Mistral 模型：
**Mistral Large**，**Mistral Small** 和 **Mistral Nemo**。

每个模型都可以在 Github Model 市场免费获取。本笔记本中的代码将使用这些模型来运行代码。有关使用 Github Models 进行 [AI 模型原型设计](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) 的更多详细信息，请参阅此处。

## Mistral Large 2 (2407)
Mistral Large 2 目前是 Mistral 的旗舰模型，专为企业使用而设计。

该模型是对原始 Mistral Large 的升级，提供了
- 更大的上下文窗口 - 128k 对比 32k
- 在数学和编码任务上的更好性能 - 平均准确率 76.9% 对比 60.4%
- 增强的多语言性能 - 包括语言：英语，法语，德语，西班牙语，意大利语，葡萄牙语，荷兰语，俄语，中文，日语，韩语，阿拉伯语和印地语。

凭借这些功能，Mistral Large 在以下方面表现出色
- *检索增强生成 (RAG)* - 由于更大的上下文窗口
- *函数调用* - 该模型具有原生函数调用功能，允许与外部工具和 API 集成。这些调用可以并行或按顺序进行。
- *代码生成* - 该模型在 Python，Java，TypeScript 和 C++ 生成方面表现出色。

### 使用 Mistral Large 2 的 RAG 示例

在本示例中，我们使用 Mistral Large 2 对文本文档运行 RAG 模式。问题用韩语编写，询问作者在上大学前的活动。

它使用 Cohere Embeddings Model 为文本文档和问题创建嵌入。对于此示例，它使用 faiss Python 包作为向量存储。

发送给 Mistral 模型的提示包括问题以及与问题相似的检索块。然后，模型提供自然语言响应。

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
Mistral Small 是 Mistral 模型系列中的另一个模型，属于高级/企业类别。正如名称所示，该模型是一个小型语言模型 (SLM)。使用 Mistral Small 的优点是：
- 与 Mistral 的其他大语言模型（如 Mistral Large 和 NeMo）相比，成本节省 - 价格下降 80%
- 低延迟 - 相比 Mistral 的大语言模型，响应速度更快
- 灵活性 - 可以在不同的环境中部署，对所需资源的限制较少。

Mistral Small 适用于：
- 基于文本的任务，如摘要，情感分析和翻译。
- 由于其成本效益，频繁请求的应用程序
- 低延迟的代码任务，如代码审查和代码建议

## 比较 Mistral Small 和 Mistral Large 

为了展示 Mistral Small 和 Large 之间的延迟差异，请运行以下单元格。

您应该会看到响应时间差异在 3-5 秒之间。同时请注意，在相同提示下的响应长度和风格。

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

与本课程中讨论的其他两个模型相比，Mistral NeMo 是唯一一个带有 Apache2 许可证的免费模型。

它被视为 Mistral 早期开源大语言模型（LLM）Mistral 7B 的升级版本。

NeMo 模型的其他一些特性包括：

- *更高效的分词：* 该模型使用 Tekken 分词器而不是更常用的 tiktoken 分词器。这使得它在更多语言和代码上的表现更好。

- *微调：* 基础模型可用于微调。这为需要微调的用例提供了更大的灵活性。

- *原生函数调用* - 与 Mistral Large 类似，该模型经过函数调用的训练。这使其成为首批支持原生函数调用的开源模型之一。

### 比较分词器

在本示例中，我们将比较 Mistral NeMo 和 Mistral Large 在分词方面的处理方式。

两个示例使用相同的提示，但您会发现 NeMo 返回的标记数量少于 Mistral Large。

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

## 学习之旅不会在这里停止，继续前行

完成本课程后，请访问我们的 [生成式 AI 学习集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) 以继续提升您的生成式 AI 知识！
