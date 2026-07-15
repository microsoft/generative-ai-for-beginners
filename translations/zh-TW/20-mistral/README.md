# 使用 Mistral 模型構建 

## 介紹 

本課程將涵蓋： 
- 探索不同的 Mistral 模型 
- 了解每個模型的使用案例和情境 
- 探索展示每個模型獨特功能的程式碼範例。 

## Mistral 模型 

在本課程中，我們將探索 3 種不同的 Mistral 模型： 
**Mistral Large**、**Mistral Small** 和 **Mistral Nemo**。 

這些模型皆可在 [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 免費取得。本筆記本中的程式碼將使用這些模型來執行。 

> **注意：** GitHub Models 將於 2026 年 7 月底退休。這裡有更多使用 [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) 來快速試驗 AI 模型的詳細資訊。 


## Mistral Large 2 (2407)
Mistral Large 2 是目前 Mistral 的旗艦模型，專為企業使用設計。 

該模型是對原始 Mistral Large 的升級，具備  
- 更大的上下文視窗 - 128k 對比 32k 
- 在數學和編碼任務上的更佳表現 - 平均準確率 76.9% 對比 60.4% 
- 增強的多語言性能 - 支援語言包括：英文、法文、德文、西班牙文、義大利文、葡萄牙文、荷蘭文、俄文、中文、日文、韓文、阿拉伯文及印地文。 

有了這些特性，Mistral Large 擅長於 
- *基於檢索增強生成 (RAG)* - 因為較大的上下文視窗 
- <em>函數呼叫</em> - 該模型具備原生函數呼叫功能，允許與外部工具和 API 整合。這些呼叫可以同時平行進行或依序逐一執行。 
- <em>程式碼生成</em> - 該模型在 Python、Java、TypeScript 及 C++ 的生成方面表現優異。 

### 使用 Mistral Large 2 的 RAG 範例 

在此範例中，我們使用 Mistral Large 2 在文本文件上執行 RAG 模式。問題以韓文書寫，詢問作者大學前的活動。 

它使用 Cohere Embeddings 模型來對文本文件和問題產生嵌入向量。此範例使用 faiss Python 套件作為向量庫。 

傳送給 Mistral 模型的提示包含問題和與問題相似的已檢索文本片段，模型隨後給出自然語言回答。 

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
Mistral Small 是 Mistral 模型家族中的另一款屬於高級／企業類別的模型。如其名所示，這是一款小型語言模型 (SLM)。使用 Mistral Small 的優點是： 
- 與 Mistral 大型語言模型（如 Mistral Large 和 NeMo）相比，節省成本 - 降價 80% 
- 低延遲 - 回應速度比 Mistral 的大型語言模型快 
- 靈活 - 可部署在不同環境中，對所需資源的限制較少。 


Mistral Small 非常適合： 
- 以文本為基礎的任務，如摘要、情感分析和翻譯。 
- 由於成本效益適合頻繁請求的應用 
- 低延遲的程式碼任務，如程式碼審查和建議 

## 比較 Mistral Small 與 Mistral Large 

為了顯示 Mistral Small 和 Large 之間的延遲差異，請執行以下單元格。 

你會看到回應時間差異約為 3-5 秒。同時留意相同提示下的回應長度和風格。  

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

與本課程中討論的其他兩款模型相比，Mistral NeMo 是唯一擁有 Apache2 授權的免費模型。 

它被視為早期 Mistral 開源大型語言模型 Mistral 7B 的升級版。 

NeMo 模型的其他特點包括： 

- *更高效的分詞器：* 此模型使用 Tekken 分詞器，取代較常用的 tiktoken。這提升了對更多語言和程式碼的性能。 

- *微調：* 基礎模型可進行微調，為需要微調的使用案例提供更大彈性。 

- <em>原生函數呼叫</em> - 類似於 Mistral Large，該模型也經過函數呼叫訓練。這使其成為最早支援此功能的開源模型之一。 


### 比較分詞器 

在此範例中，我們將比較 Mistral NeMo 與 Mistral Large 處理分詞的差異。 

兩個範例使用相同提示，但你會看到 NeMo 回傳的 token 數較 Mistral Large 少。 

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

# 計算分詞數量
print(len(tokens))
```

## 學習不止於此，繼續你的旅程

完成本課程後，請參考我們的 [生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升你的生成式 AI 知識！ 

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->