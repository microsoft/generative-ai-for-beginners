# 使用 Mistral 模型進行構建

## 介紹

本課程將涵蓋：
- 探索不同的 Mistral 模型
- 了解每個模型的使用案例和情境
- 探討展示各模型獨特功能的程式碼範例。

## Mistral 模型

在本課程中，我們將探討 3 種不同的 Mistral 模型：
**Mistral Large**、**Mistral Small** 和 **Mistral Nemo**。

這些模型都可在 [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 免費取得。本筆記本中的程式碼將使用這些模型來執行程式。

> **注意：** GitHub Models 將於 2026 年 7 月底退役。這裡有更多使用 [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) 進行 AI 模型原型設計的詳細資訊。


## Mistral Large 2 (2407)
Mistral Large 2 目前是 Mistral 的旗艦模型，設計用於企業級應用。

該模型是原始 Mistral Large 的升級版，具有以下優點：
- 更大的上下文視窗 - 128k 對比 32k
- 在數學和程式碼任務上的表現更佳 - 平均準確率 76.9% 對比 60.4%
- 多語言性能提升 - 包括語言：英語、法語、德語、西班牙語、義大利語、葡萄牙語、荷蘭語、俄語、中文、日語、韓語、阿拉伯語和印地語。

擁有這些特性，Mistral Large 擅長於
- *檢索增強生成 (RAG)* - 由於更大的上下文視窗
- <em>函數呼叫</em> - 此模型具備原生函數呼叫功能，允許整合外部工具與 API。呼叫可同時進行，也能依序執行。
- <em>程式碼生成</em> - 此模型在 Python、Java、TypeScript 和 C++ 生成上表現出色。

### 使用 Mistral Large 2 的 RAG 範例

在此範例中，我們使用 Mistral Large 2 對一段文字文件執行 RAG 模式。問題以韓文書寫，詢問作者大學前的活動。

它使用 Cohere Embeddings 模型對文字文件及問題進行嵌入。此次範例中，使用 faiss Python 套件作為向量庫。

發送到 Mistral 模型的提示包含問題和與問題相似的檢索段落。模型接著提供自然語言回應。

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

# 從您的 Microsoft Foundry 專案的「概覽」頁面取得這些
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Mistral-large"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]

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
Mistral Small 是 Mistral 家族中屬於高端/企業類別的另一款模型。顧名思義，此模型為小型語言模型（SLM）。使用 Mistral Small 的優點包括：
- 相較於 Mistral 大型語言模型如 Mistral Large 和 NeMo，成本更低 - 價格降低約 80%
- 延遲低 - 比 Mistral 的大型語言模型回應更快
- 靈活 - 可在不同環境部署，所需資源限制較少。


Mistral Small 非常適合：
- 以文字為基礎的任務，如摘要、情感分析和翻譯。
- 成本效益高的應用場景，頻繁發出請求的情況
- 低延遲的程式碼任務，如程式碼審查與建議

## 比較 Mistral Small 和 Mistral Large

為顯示 Mistral Small 和 Large 之間的延遲差異，可執行下列儲存格。

你應該會看到回應時間差異約 3-5 秒。也請注意在相同提示下的回應長度和風格。

```python 

import os 
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Mistral-small"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]

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

endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Mistral-large"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]

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

它被視為 Mistral 早期開源大型語言模型 Mistral 7B 的升級版。

NeMo 模型的其他特點包括：

- *更高效的分詞：* 該模型使用 Tekken 分詞器，而非較常使用的 tiktoken。這提升了更多語言和程式碼的表現。

- *微調能力：* 基礎模型可進行微調。這對需要微調的使用案例提供了更多彈性。

- <em>原生函數呼叫</em> - 如同 Mistral Large，該模型已訓練函數呼叫功能，使其成為首批具有此能力的開源模型之一。


### 分詞器比較

在此範例中，我們將比較 Mistral NeMo 與 Mistral Large 的分詞表現。

兩者都使用相同提示，但你會發現 NeMo 回傳的標記數較 Mistral Large 少。

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

# 對一組訊息進行分詞
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

# 計算詞元數量
print(len(tokens))
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

# 載入 Mistral 的分詞器

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# 對一組訊息列表進行分詞
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

# 計算分詞後的標記數量
print(len(tokens))
```

## 學習不止於此，持續前行

完成本課程後，請參考我們的 [生成式 AI 學習集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升你的生成式 AI 知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->