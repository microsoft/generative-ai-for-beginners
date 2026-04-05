# 使用 Mistral 模型進行建構

## 介紹

本課程將涵蓋：
- 探索不同的 Mistral 模型
- 了解每個模型的應用案例和場景
- 探索展示每個模型獨特功能的程式碼範例。

## Mistral 模型

在本課程中，我們將探索 3 種不同的 Mistral 模型：
**Mistral Large**、**Mistral Small** 和 **Mistral Nemo**。

這些模型皆可在 GitHub 模型市場免費獲取。本筆記本中的程式碼將使用這些模型來執行。下方有更多關於使用 GitHub 模型進行[AI 模型原型設計](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)的詳細資訊。

## Mistral Large 2 (2407)
Mistral Large 2 是目前 Mistral 的旗艦模型，設計用於企業級應用。

此模型是對原始 Mistral Large 的升級，提供以下功能：
- 更大的上下文視窗 - 128k 相較於 32k
- 在數學和程式編寫任務上的更佳表現 - 平均準確率 76.9% 對比 60.4%
- 增強多語言表現 - 支援語言包括：英文、法文、德文、西班牙文、義大利文、葡萄牙文、荷蘭文、俄文、中文、日文、韓文、阿拉伯文和印地文。

有了這些功能，Mistral Large 擅長於：
- *檢索增強生成（RAG）* - 由於較大的上下文視窗
- *函數調用* - 此模型具備原生函數調用能力，允許整合外部工具及 API。這些調用可平行執行，或按順序依次執行。
- *程式碼生成* - 此模型在 Python、Java、TypeScript 和 C++ 生成上表現卓越。

### 使用 Mistral Large 2 的 RAG 範例

在此範例中，我們使用 Mistral Large 2 在文本文件上運行 RAG 模式。問題以韓語書寫，詢問作者大學前的活動。

此範例使用 Cohere Embeddings 模型對文本文件及問題進行嵌入。示範中使用 faiss Python 套件作為向量存儲。

傳送給 Mistral 模型的提示包含問題以及與問題相似檢索出的段落。模型隨後提供自然語言回應。

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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # 距離，索引
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
Mistral Small 是 Mistral 家族中另一款屬於頂級/企業級別的模型。顧名思義，這是一個小型語言模型（SLM）。使用 Mistral Small 的優點包括：
- 相較於 Mistral 大型語言模型如 Mistral Large 和 NeMo，節省成本 - 價格下降 80%
- 低延遲 - 回應速度快於 Mistral 的大型語言模型
- 靈活性高 - 可在不同環境部署，對所需資源的限制較少。

Mistral Small 適合用於：
- 文字型任務，如摘要製作、情感分析和翻譯
- 頻繁請求的應用，成本效益佳
- 低延遲的程式碼任務，如程式碼審查和建議

## 比較 Mistral Small 與 Mistral Large

為展示 Mistral Small 與 Large 在延遲時間上的差異，請執行以下儲存格。

你會看到回應時間差異約為 3-5 秒。同時請注意相同提示下回應長度與風格的不同。

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

與本課程中討論的其他兩款模型相比，Mistral NeMo 是唯一具有 Apache2 授權的免費模型。

它被視為早期 Mistral 開源大型語言模型 Mistral 7B 的升級版。

NeMo 模型的其他特點包括：

- *更高效的分詞：* 此模型使用 Tekken 分詞器，較常用的 tiktoken 具有更佳的多語言及程式碼處理性能。

- *微調：* 基礎模型可用於微調，為需要微調的使用情境提供更多彈性。

- *原生函數調用* - 與 Mistral Large 類似，此模型經過函數調用訓練，使其成為首批具備此功能的開源模型之一。

### 分詞器比較

在此範例中，我們將比較 Mistral NeMo 與 Mistral Large 在分詞上的表現。

兩者皆使用相同提示，但你會看到 NeMo 回傳的 tokens 較少。

```bash
pip install mistral-common
```

```python 
# 匯入所需的套件：
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# 載入 Mistral 分詞器

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# 對訊息列表進行分詞
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

# 計算標記數量
print(len(tokens))
```

```python
# 匯入所需套件：
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# 載入 Mistral 斷詞器

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# 對訊息列表進行斷詞
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

# 計算斷詞數量
print(len(tokens))
```


## 學習不止於此，繼續你的旅程

完成本課程後，請參考我們的[生成式 AI 學習收藏](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升你的生成式 AI 知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->