# 使用 Mistral 模型構建

## 介紹

本課程將涵蓋：
- 探索不同的 Mistral 模型
- 了解每個模型的使用案例和場景
- 探索展示各模型獨特功能的代碼範例。

## Mistral 模型

在本課程中，我們將探索三種不同的 Mistral 模型：
**Mistral Large**、**Mistral Small** 和 **Mistral Nemo**。

這些模型均可免費在 [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 使用。本筆記本中的代碼將使用這些模型進行運行。

> **注意：** GitHub Models 將於 2026 年 7 月底退役。這裡有更多關於使用 [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) 以原型開發 AI 模型的詳細資訊。


## Mistral Large 2 (2407)
Mistral Large 2 是目前 Mistral 的旗艦模型，專為企業使用而設計。

該模型是原始 Mistral Large 的升級版本，提供：
- 更大的上下文窗口 - 128k 對比 32k
- 在數學和程式編碼任務中的更佳表現 - 平均準確率 76.9% 對比 60.4%
- 提升的多語言性能 - 支援語言包括：英語、法語、德語、西班牙語、義大利語、葡萄牙語、荷蘭語、俄語、中文、日語、韓語、阿拉伯語和印地語。

凭藉這些特性，Mistral Large 擅長於
- *基於檢索增強生成 (RAG)* - 由於上下文窗口更大
- <em>函數調用</em> - 該模型具備原生函數調用功能，可以集成外部工具和 API。這些調用可以並行執行，也可以依序進行。
- <em>程式碼生成</em> - 該模型在 Python、Java、TypeScript 和 C++ 生成方面表現優異。

### 使用 Mistral Large 2 的 RAG 範例

在此範例中，我們使用 Mistral Large 2 對一份文本文件執行 RAG 模式。問題以韓文撰寫，詢問作者在大學前的活動。

它使用 Cohere Embeddings 模型來對文本文件及問題進行向量嵌入。範例中使用 faiss Python 套件作為向量存儲。

發送給 Mistral 模型的提示詞包含問題以及與問題相似的檢索片段。模型然後提供自然語言回應。

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

# 從你的 Microsoft Foundry 專案的「概覽」頁面取得這些
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # 距離, 索引
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
Mistral Small 是 Mistral 系列中的另一款模型，屬於高級/企業類別。如其名稱所示，該模型是一款小型語言模型（SLM）。使用 Mistral Small 的優勢包括：
- 與 Mistral 的大型語言模型如 Mistral Large 和 NeMo 相比，更節省成本 - 降價 80%
- 低延遲 - 較 Mistral 的大型語言模型響應更快
- 靈活性 - 可在不同環境中部署，對所需資源限制較少


Mistral Small 非常適合於：
- 基於文本的任務，如摘要、情感分析和翻譯
- 頻繁請求的應用案例，因其具成本效益
- 低延遲的程式碼任務，如程式碼審查和建議

## 比較 Mistral Small 與 Mistral Large

為了展示 Mistral Small 與 Large 之間的延遲差異，請運行以下單元格。

你應該會看到響應時間有 3 到 5 秒的差異。也請注意相同提示詞下的回應長度和風格。

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

與本課程中討論的其他兩個模型相比，Mistral NeMo 是唯一擁有 Apache2 授權的免費模型。

它被視為 Mistral 早期開源大型語言模型 Mistral 7B 的升級版。

NeMo 模型的其他特點包括：

- *更高效的分詞：* 該模型使用 Tekken 分詞器，而非更常用的 tiktoken。這使其在更多語言和程式碼上的表現更佳。

- *微調：* 基礎模型支持微調，為需要微調的應用場景提供更大靈活性。

- <em>原生函數調用</em> - 與 Mistral Large 類似，該模型被訓練具備函數調用能力，使其成為首批具此功能的開源模型之一。


### 分詞器比較

在此範例中，我們將觀察 Mistral NeMo 與 Mistral Large 在分詞處理上的差異。

兩個範例使用相同提示詞，但你應該會看到 NeMo 返回的分詞數量少於 Mistral Large。

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

model_name = "mistral-large-latest"

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

# 計算分詞的數量
print(len(tokens))
```

## 學習不止於此，繼續前行

完成本課程後，請查看我們的 [生成式 AI 學習資源](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升你的生成式 AI 知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->