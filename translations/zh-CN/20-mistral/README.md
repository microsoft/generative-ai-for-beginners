# 使用 Mistral 模型构建

## 介绍

本课将涵盖：
- 探索不同的 Mistral 模型
- 理解每个模型的使用场景和适用情况
- 探索展示每个模型独特功能的代码示例

## Mistral 模型

在本课中，我们将探索 3 种不同的 Mistral 模型：
**Mistral Large**、**Mistral Small** 和 **Mistral Nemo**。

这些模型均可在 GitHub 模型市场上免费获得。本笔记本中的代码将使用这些模型来运行。有关使用 GitHub 模型进行[人工智能模型原型设计](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)的更多详细信息，请参见链接。

## Mistral Large 2 (2407)
Mistral Large 2 是目前 Mistral 的旗舰模型，专为企业使用设计。

该模型是对原始 Mistral Large 的升级，提供：
- 更大的上下文窗口 — 128k 对比 32k
- 在数学和编码任务上的更好性能 — 平均准确率 76.9% 对比 60.4%
- 增强的多语言性能 — 支持语言包括：英语、法语、德语、西班牙语、意大利语、葡萄牙语、荷兰语、俄语、中文、日语、韩语、阿拉伯语和印地语。

凭借这些功能，Mistral Large 在以下方面表现出色：
- *检索增强生成（RAG）* — 由于更大的上下文窗口
- *函数调用* — 该模型具有原生函数调用功能，允许与外部工具和 API 集成。这些调用可以并行或按顺序依次执行。
- *代码生成* — 在 Python、Java、TypeScript 和 C++ 生成方面表现卓越。

### 使用 Mistral Large 2 的 RAG 示例

在此示例中，我们使用 Mistral Large 2 对文本文件运行 RAG 模式。问题以韩语书写，询问作者大学前的活动。

它使用 Cohere Embeddings 模型对文本文件和问题分别创建嵌入。此示例使用 faiss Python 包作为向量存储。

发送给 Mistral 模型的提示包括问题和与之相似的检索块。模型随后提供自然语言回答。

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

question = "저자가 대학에 오기 전에 주로 했던 두 가지 일은 무엇이었나요?"

question_embedding = embed_client.embed(
    input=[question],
    model=embed_model_name
)

question_embeddings = np.array(question_embedding.data[0].embedding)


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # 距离，索引
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
Mistral Small 是 Mistral 家族中另一款位于高级/企业类别的模型。顾名思义，这是一款小型语言模型（SLM）。使用 Mistral Small 的优势有：
- 与 Mistral LLM（如 Mistral Large 和 NeMo）相比，节省成本 — 价格下降约 80%
- 低延迟 — 相对于 Mistral 的大型语言模型响应更快
- 灵活 — 可以在不同环境中部署，对所需资源的限制较少

Mistral Small 适合：
- 基于文本的任务，如摘要、情感分析和翻译
- 频繁请求的应用场景，因其成本效益
- 低延迟代码任务，如代码审查和建议

## 比较 Mistral Small 和 Mistral Large

要展示 Mistral Small 和 Large 在延迟上的差异，请运行下面的单元格。

您将看到响应时间差异约为 3 到 5 秒。也请注意同一提示下的响应长度和风格差异。

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

与本课讨论的其它两款模型相比，Mistral NeMo 是唯一带有 Apache2 许可证的免费模型。

它被视为 Mistral 早期开源大型语言模型 Mistral 7B 的升级版。

NeMo 模型的其他特点包括：

- *更高效的分词：* 该模型采用 Tekken 分词器，而非常用的 tiktoken。这使其在更多语言和代码上的表现更好。

- *微调：* 基础模型支持微调，允许针对可能需要微调的用例增加灵活性。

- *原生函数调用* — 与 Mistral Large 一样，该模型经过函数调用训练。它是首批开源支持此功能的模型之一，具有独特性。

### 分词器比较

在此示例中，我们将查看 Mistral NeMo 在分词处理上与 Mistral Large 的区别。

两个示例均使用相同提示，但您应会看到 NeMo 返回的标记数少于 Mistral Large。

```bash
pip install mistral-common
```

```python 
# 导入所需的包：
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# 加载 Mistral 分词器

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# 对消息列表进行分词
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
                                "description": "The temperature unit to use. Infer this from the user's location.",
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

# 计算标记数目
print(len(tokens))
```

```python
# 导入所需的包：
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# 加载 Mistral 分词器

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# 对一组消息进行分词
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
                                "description": "The temperature unit to use. Infer this from the user's location.",
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

# 统计令牌数量
print(len(tokens))
```

## 学习不会止步于此，继续前行

完成本课后，请查看我们的[生成式 AI 学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持续提升您的生成式 AI 知识水平！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件通过AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。虽然我们力求准确，但请注意自动翻译可能包含错误或不准确之处。请以原始语言的原文档为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而引起的任何误解或误释，我们不承担任何责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->