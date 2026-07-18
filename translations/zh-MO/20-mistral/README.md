# 使用 Mistral 模型構建

## 介紹

本課程將涵蓋：
- 探索不同的 Mistral 模型
- 了解每個模型的使用案例和情境
- 探索展示每個模型獨特特性的範例程式碼。

## Mistral 模型

在本課程中，我們將探討 3 個不同的 Mistral 模型：
**Mistral Large**、**Mistral Small** 與 **Mistral Nemo**。

這些模型皆可免費於 [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 使用。本筆記本中的程式碼將使用這些模型來執行。

> **注意：** GitHub Models 將於 2026 年 7 月底退役。這裡有更多使用 [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) 與 AI 模型原型設計的詳細資料。


## Mistral Large 2 (2407)
Mistral Large 2 目前是 Mistral 的旗艦模型，專為企業使用設計。

該模型是原始 Mistral Large 的升級版，提供：
- 更大的上下文視窗 - 128k 對比 32k
- 在數學與程式碼任務上的更佳表現 - 平均準確率 76.9% 對比 60.4%
- 增強的多語言表現 - 支援語言包括：英語、法語、德語、西班牙語、義大利語、葡萄牙語、荷蘭語、俄語、中文、日語、韓語、阿拉伯語及印地語。

憑藉這些功能，Mistral Large 擅長於：
- *檢索增強生成（RAG）* - 得益於更大的上下文視窗
- <em>函式呼叫</em> - 此模型具原生函式呼叫功能，允許與外部工具和 API 整合。這些呼叫可以並行進行，或依序進行。
- <em>程式碼生成</em> - 此模型在 Python、Java、TypeScript 與 C++ 生成上表現優異。

### 使用 Mistral Large 2 的 RAG 範例

此例中，我們使用 Mistral Large 2 以 RAG 模式處理文字文件。問題用韓語書寫，詢問作者在大學前的活動。

它使用 Cohere Embeddings 模型對文字文件及問題建立向量。此範例使用 faiss Python 套件作為向量庫。

傳送給 Mistral 模型的提示包含問題及與問題相似的檢索片段。模型隨後提供自然語言回應。

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

# 從你嘅 Microsoft Foundry 項目「概覽」頁面攞呢啲
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
Mistral Small 是 Mistral 家族中另一款屬於頂級/企業類別的模型。如其名，此模型為小型語言模型（SLM）。使用 Mistral Small 的優點在於：
- 相較於 Mistral 大型語言模型（如 Mistral Large 與 NeMo），成本節省 - 價格降低 80%
- 低延遲 - 較 Mistral 大型語言模型回應更快
- 靈活 - 可跨不同環境部署，對所需資源限制較少。


Mistral Small 適合於：
- 以文字為基礎的任務，如摘要、情感分析與翻譯。
- 因成本效益高而頻繁請求的應用場景
- 低延遲的程式碼任務，如程式碼檢查與建議

## 比較 Mistral Small 與 Mistral Large

為了展示 Mistral Small 與 Large 在延遲上的差異，請執行下列 Cells。

您應會見到 3-5 秒的回應時間差異。同時也請注意相同提示下回應的長度與風格。

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

與本課程討論的其他兩款模型相比，Mistral NeMo 是唯一具備 Apache2 授權的免費模型。

它被視為早期 Mistral 開源大型語言模型 Mistral 7B 的升級版本。

NeMo 模型的其他特點包括：

- *更高效的分詞器：* 此模型採用 Tekken 分詞器，勝過更常用的 tiktoken。這使其在多語言與程式碼上的表現更佳。

- *微調能力：* 基礎模型支持微調，為需要微調的使用案例提供更大彈性。

- <em>原生函式呼叫</em> - 如同 Mistral Large，該模型已經過函式呼叫訓練，使其成為首批擁有此功能的開源模型之一。


### 分詞器比較

在此範例中，我們將觀察 Mistral NeMo 與 Mistral Large 在分詞上的處理差異。

兩個範例都使用相同提示，但你會看到 NeMo 回傳的分詞數量少於 Mistral Large。

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

# 計算分詞數量
print(len(tokens))
```

```python
# 載入所需套件：
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

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# 對訊息清單進行分詞
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

## 學習不止於此，繼續前行

完成本課程後，請查看我們的 [生成式 AI 學習集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升您的生成式 AI 知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->