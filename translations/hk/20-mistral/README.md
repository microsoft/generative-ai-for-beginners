<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T18:56:56+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "hk"
}
-->
# 使用 Mistral 模型構建

## 介紹

本課程將涵蓋：  
- 探索不同的 Mistral 模型  
- 了解每個模型的使用場景和應用情境  
- 透過程式碼範例展示各模型的獨特功能  

## Mistral 模型

在本課程中，我們將探索三款不同的 Mistral 模型：  
**Mistral Large**、**Mistral Small** 以及 **Mistral Nemo**。

這些模型均可在 Github Model 市場免費取得。本筆記本中的程式碼將使用這些模型來執行。更多關於使用 Github Models 來[以 AI 模型進行原型設計](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)的資訊，請參考該連結。

## Mistral Large 2 (2407)

Mistral Large 2 是目前 Mistral 的旗艦模型，專為企業使用而設計。

此模型是原始 Mistral Large 的升級版，提供：  
- 更大的上下文視窗 — 128k 對比 32k  
- 在數學與程式編碼任務上的更佳表現 — 平均準確率 76.9% 對比 60.4%  
- 提升的多語言能力 — 支援語言包括：英語、法語、德語、西班牙語、義大利語、葡萄牙語、荷蘭語、俄語、中文、日語、韓語、阿拉伯語及印地語。

憑藉這些特點，Mistral Large 擅長於：  
- *檢索增強生成（RAG）* — 由於更大的上下文視窗  
- *函數呼叫* — 此模型具備原生函數呼叫功能，允許與外部工具和 API 整合。這些呼叫可同時平行執行，或依序逐一執行。  
- *程式碼生成* — 在 Python、Java、TypeScript 和 C++ 生成方面表現優異。

### 使用 Mistral Large 2 的 RAG 範例

在此範例中，我們使用 Mistral Large 2 針對一份文本文件執行 RAG 模式。問題以韓文撰寫，詢問作者大學前的活動。

此範例使用 Cohere Embeddings Model 來建立文本文件及問題的向量表示。範例中使用 faiss Python 套件作為向量資料庫。

傳送給 Mistral 模型的提示包含問題及與問題相似的檢索片段，模型隨後提供自然語言回應。

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

Mistral Small 是 Mistral 家族中屬於高階/企業類別的另一款模型。顧名思義，這是一款小型語言模型（SLM）。使用 Mistral Small 的優點包括：  
- 相較於 Mistral 大型語言模型（如 Mistral Large 和 NeMo）節省成本 — 價格降低約 80%  
- 低延遲 — 回應速度較 Mistral 的大型語言模型快  
- 靈活性高 — 可在不同環境部署，對所需資源限制較少

Mistral Small 非常適合：  
- 文字相關任務，如摘要、情感分析及翻譯  
- 頻繁請求的應用，因其成本效益高  
- 低延遲的程式碼任務，如程式碼審查與建議

## Mistral Small 與 Mistral Large 的比較

為了展示 Mistral Small 與 Large 在延遲上的差異，請執行以下程式碼區塊。

你應該會看到回應時間相差約 3-5 秒，並且注意相同提示下回應的長度與風格差異。

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

與本課程中討論的其他兩款模型相比，Mistral NeMo 是唯一採用 Apache2 授權的免費模型。

它被視為 Mistral 早期開源大型語言模型 Mistral 7B 的升級版。

NeMo 模型的其他特點包括：

- *更高效的分詞器：* 此模型使用 Tekken 分詞器，取代較常用的 tiktoken，提升多語言及程式碼的處理效能。

- *微調能力：* 基礎模型可用於微調，為需要微調的應用場景提供更大彈性。

- *原生函數呼叫* — 與 Mistral Large 類似，此模型經過函數呼叫訓練，是首批具備此功能的開源模型之一。

### 分詞器比較

在此範例中，我們將比較 Mistral NeMo 與 Mistral Large 在分詞上的差異。

兩個範例使用相同提示，但你會發現 NeMo 回傳的 token 數量較 Mistral Large 少。

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

## 學習不止於此，繼續前行

完成本課程後，請參考我們的[生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升你的生成式 AI 知識！

**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。