# 使用 Mistral 模型進行構建

## 簡介

本課程將涵蓋：
- 探索不同的 Mistral 模型
- 了解每個模型的使用案例與場景
- 探索展示每個模型獨特功能的程式碼範例

## Mistral 模型介紹

在本課程中，我們將探索 3 種不同的 Mistral 模型：
**Mistral Large**、**Mistral Small** 及 **Mistral Nemo**。

這些模型均可於 [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 免費使用。本筆記本中的程式碼將使用這些模型進行運行。

> **注意：** GitHub Models 將於 2026 年 7 月底停止服務。這裡有更多關於使用 [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) 進行 AI 模型原型設計的詳細資訊。


## Mistral Large 2 (2407)
Mistral Large 2 目前是 Mistral 的旗艦模型，設計用於企業級使用。

此模型是對原始 Mistral Large 的升級，提供了：
- 更大的上下文視窗——128k 對比 32k
- 更佳的數學與編碼任務表現——平均準確率 76.9% 對比 60.4%
- 增強的多語言表現——涵蓋語言包括：英文、法文、德文、西班牙文、意大利文、葡萄牙文、荷蘭文、俄文、中文、日文、韓文、阿拉伯文及印地文。

凭藉這些功能，Mistral Large 擅長於：
- *檢索增強生成（RAG）*——因較大的上下文視窗所致
- <em>函數調用</em> —— 此模型內建函數調用能力，允許與外部工具和 API 整合。這些調用可以同時進行，也可以按序列順序依次執行。
- <em>程式碼生成</em> —— 此模型在 Python、Java、TypeScript 和 C++ 生成方面表現優異。

### 使用 Mistral Large 2 的 RAG 範例

在此範例中，我們使用 Mistral Large 2 對一份文本文件執行 RAG 模式。問題是用韓文寫的，探詢作者大學前的活動。

它使用 Cohere Embeddings 模型對文本文件和問題創建嵌入向量。在本範例中，使用 faiss Python 包作為向量存儲。

發送給 Mistral 模型的提示涵蓋問題及與問題相似的檢索片段，模型隨後提供自然語言回應。

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

# 從你的 Microsoft Foundry 專案的「概覽」頁面獲取這些資料
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
Mistral Small 是 Mistral 系列中另一個處於頂級/企業類別的模型。顧名思義，這是一個小型語言模型（SLM）。使用 Mistral Small 的優勢包括：
- 相較於 Mistral 大型模型（如 Mistral Large 和 NeMo），成本節省——價格降低約 80%
- 低延遲——相較於 Mistral 的大型語言模型有較快的回應速度
- 靈活性高——可於不同環境部署，對所需資源限制較少


Mistral Small 非常適合：
- 基於文本的任務，如摘要、情感分析和翻譯
- 因成本效益可支援頻繁請求的應用
- 低延遲的程式碼任務，如評論及程式碼建議

## Mistral Small 與 Mistral Large 比較

要展示 Mistral Small 與 Large 在延遲上的差異，請執行以下程式碼區塊。

你會看到回應時間相差約 3-5 秒。同時注意兩者對相同提示的回應長度和風格的差異。

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

與本課程中討論的其他兩個模型相比，Mistral NeMo 是唯一一個採用 Apache2 授權的免費模型。

它被視為早期 Mistral 開源大型語言模型 Mistral 7B 的升級版。

NeMo 模型的其他特點包括：

- *更高效的分詞方式：* 該模型使用 Tekken 分詞器，而非更常用的 tiktoken，這使其在多種語言和程式碼上的表現更佳。

- *微調能力：* 基礎模型可作微調，為需要微調的使用案例提供更大彈性。

- <em>原生函數調用</em> —— 與 Mistral Large 類似，該模型訓練了函數調用功能，是首批具備此能力的開源模型之一。


### 分詞器比較

在這個範例中，我們將比較 Mistral NeMo 與 Mistral Large 的分詞處理方式。

兩個範例都使用相同提示，應該會看到 NeMo 返回的詞元數少於 Mistral Large。

```bash
pip install mistral-common
```

```python 
# 載入所需的套件：
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

# 對一串訊息進行分詞
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
# 導入所需套件：
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# 載入 Mistral 詞彙切割器

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# 對訊息列表進行詞彙切割
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

# 計算詞元數目
print(len(tokens))
```

## 學習不止於此，繼續旅程

完成本課程後，請瀏覽我們的 [生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) 持續提升您的生成式 AI 知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->