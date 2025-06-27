<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-06-26T03:13:04+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "tw"
}
-->
# 使用 Mistral 模型構建

## 介紹

本課程將涵蓋：
- 探索不同的 Mistral 模型
- 了解每個模型的使用情境和案例
- 代碼範例展示每個模型的獨特特徵

## Mistral 模型

在本課程中，我們將探索三種不同的 Mistral 模型：**Mistral Large**、**Mistral Small** 和 **Mistral Nemo**。

這些模型均可在 Github 模型市場免費獲得。本筆記本中的代碼將使用這些模型來運行代碼。這裡有更多關於使用 Github 模型來[原型設計 AI 模型](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)的詳細信息。

## Mistral Large 2 (2407)
Mistral Large 2 是目前 Mistral 的旗艦模型，專為企業用途設計。

此模型是對原始 Mistral Large 的升級，提供了：
- 更大的上下文窗口 - 128k 對比 32k
- 更好的數學和編碼任務性能 - 平均準確率 76.9% 對比 60.4%
- 增強的多語言性能 - 包括語言：英語、法語、德語、西班牙語、意大利語、葡萄牙語、荷蘭語、俄語、中文、日語、韓語、阿拉伯語和印地語。

憑藉這些特性，Mistral Large 在以下方面表現出色：
- *檢索增強生成 (RAG)* - 由於更大的上下文窗口
- *函數調用* - 此模型具有原生函數調用功能，允許與外部工具和 API 集成。這些調用可以並行或按順序進行。
- *代碼生成* - 此模型在 Python、Java、TypeScript 和 C++ 生成方面表現出色。

### 使用 Mistral Large 2 的 RAG 範例

在此範例中，我們使用 Mistral Large 2 在文本文件上運行 RAG 模式。問題以韓語書寫，詢問作者在大學前的活動。

它使用 Cohere Embeddings 模型來創建文本文件和問題的嵌入。對於此範例，它使用 faiss Python 套件作為向量存儲。

發送到 Mistral 模型的提示包括問題和與問題相似的檢索塊。然後模型提供自然語言回應。

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
Mistral Small 是 Mistral 模型家族中另一個在高級/企業類別下的模型。如其名，此模型是一個小型語言模型 (SLM)。使用 Mistral Small 的優勢在於：
- 與 Mistral LLMs 如 Mistral Large 和 NeMo 相比，節省成本 - 價格降低 80%
- 低延遲 - 相比 Mistral 的 LLMs 更快的響應
- 靈活 - 可以在不同環境中部署，對所需資源的限制較少。

Mistral Small 非常適合：
- 基於文本的任務，如摘要、情感分析和翻譯。
- 由於其成本效益，在需要頻繁請求的應用中使用
- 低延遲代碼任務，如審查和代碼建議

## 比較 Mistral Small 和 Mistral Large

為了展示 Mistral Small 和 Large 之間的延遲差異，運行以下單元格。

您應該會看到響應時間之間的差異約為 3-5 秒。還要注意相同提示下的響應長度和風格。

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

與本課程中討論的其他兩個模型相比，Mistral NeMo 是唯一擁有 Apache2 許可的免費模型。

它被視為 Mistral 早期開源 LLM，Mistral 7B 的升級版。

NeMo 模型的其他一些特點包括：

- *更高效的分詞：* 此模型使用 Tekken 分詞器而非更常用的 tiktoken。這使其在更多語言和代碼上表現更佳。

- *微調：* 基礎模型可供微調。這在需要微調的使用情境中提供了更多靈活性。

- *原生函數調用* - 像 Mistral Large 一樣，此模型經過函數調用訓練。這使其成為首批這樣做的開源模型之一。

### 比較分詞器

在此範例中，我們將觀察 Mistral NeMo 如何處理分詞與 Mistral Large 的比較。

兩個範例使用相同的提示，但您應該看到 NeMo 返回的 token 比 Mistral Large 少。

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

## 學習不止於此，繼續學習之旅

完成此課程後，查看我們的[生成式 AI 學習集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，繼續提升您的生成式 AI 知識！

**免責聲明**：
本文件已使用AI翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)進行翻譯。儘管我們努力確保準確性，請注意自動翻譯可能包含錯誤或不準確之處。應將原始文件的母語版本視為權威來源。對於關鍵信息，建議使用專業人工翻譯。對於因使用此翻譯而產生的任何誤解或誤釋，我們不承擔責任。