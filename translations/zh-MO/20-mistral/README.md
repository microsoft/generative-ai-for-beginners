# 使用 Mistral 模型建構

## 導言

本課程將涵蓋：
- 探索不同的 Mistral 模型
- 理解每個模型的使用案例和情境
- 探索展示每個模型獨特功能的程式碼範例。

## Mistral 模型

在本課程中，我們將探索三種不同的 Mistral 模型：
**Mistral Large**、**Mistral Small** 及 **Mistral Nemo**。

這些模型均可於 [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 免費使用。本筆記本中的程式碼將使用這些模型來執行。

> **注意：** GitHub 模型將於 2026 年 7 月底退役。這裡有更多使用 [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) 以原型設計 AI 模型的詳細資訊。


## Mistral Large 2 (2407)
Mistral Large 2 目前是 Mistral 的旗艦模型，設計用於企業級應用。

該模型是對原本 Mistral Large 的升級，提供了
- 更大的上下文視窗 - 128k 對比 32k
- 在數學和編程任務上的更佳表現 - 平均準確度 76.9% 對比 60.4%
- 增強的多語言表現 - 語言包括：英語、法語、德語、西班牙語、意大利語、葡萄牙語、荷蘭語、俄語、中文、日語、韓語、阿拉伯語和印地語。

憑藉這些功能，Mistral Large 擅長於
- *檢索增強生成 (RAG)* - 因為更大的上下文視窗
- <em>函數調用</em> - 此模型擁有原生函數調用功能，允許與外部工具和 API 集成。這些調用可以同時進行，或依序逐個調用。
- <em>程式碼生成</em> - 此模型在 Python、Java、TypeScript 和 C++ 生成方面表現優異。

### 使用 Mistral Large 2 的 RAG 範例

在這個範例中，我們使用 Mistral Large 2 在一個文本文件上執行 RAG 模式。問題以韓文提出，問作者大學前的活動。

它利用 Cohere Embeddings 模型建立文本文件和問題的嵌入。此範例使用 faiss Python 套件作為向量存儲。

發送給 Mistral 模型的提示包含問題與與問題相似的檢索片段，模型隨後提供自然語言的回答。

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

# 從你嘅 Microsoft Foundry 項目「概覽」頁面獲取呢啲資料
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
Mistral Small 是 Mistral 系列中屬於頂級/企業類別的另一個模型。如其名所示，這是一個小型語言模型 (SLM)。使用 Mistral Small 的優點有：
- 與 Mistral 大型模型如 Mistral Large 和 NeMo 相比，具成本節省效益 - 降價約 80%
- 低延遲 - 回應比 Mistral 的大型模型更快
- 靈活 - 可以部署於不同環境，對資源需求限制較少。


Mistral Small 非常適合：
- 文字相關任務，如摘要、情感分析與翻譯。
- 由於成本效益高，適合頻繁要求的應用
- 低延遲程式碼任務，如代碼審查及建議

## 比較 Mistral Small 與 Mistral Large

為展示 Mistral Small 與 Large 的延遲差異，請執行以下儲存格。

你應該會見到回應時間相差約 3-5 秒。另請注意同一提示下回應的長度與風格差異。

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

相較本課程討論的其他兩個模型，Mistral NeMo 是唯一具有 Apache2 授權的免費模型。

它被視為早期 Mistral 開源大型語言模型 Mistral 7B 的升級版。

NeMo 模型的其他特點有：

- *更高效的標記化：* 此模型使用 Tekken 分詞器，優於較常用的 tiktoken。此優勢在更多語言和程式碼表現更好。

- *微調：* 基礎模型可用於微調，使其在需要微調的使用案例中更具彈性。

- <em>原生函數調用</em> - 如同 Mistral Large，此模型經過訓練以支援函數調用，是首批具此特性的開源模型之一。


### 比較分詞器

在此範例中，我們將比較 Mistral NeMo 與 Mistral Large 在標記化處理上的差異。

兩個範例使用相同的提示，但你應該會看到 NeMo 回傳的標記數量較 Mistral Large 少。

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

# 載入 Mistral 詞元化器

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# 對消息列表進行詞元化
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

# 計算詞元的數量
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

# 載入 Mistral 分詞器

model_name = "mistral-large-latest"

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

## 學習不止於此，繼續探索之旅

完成本課程後，請瀏覽我們的[生成式 AI 學習收藏](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，繼續提升你的生成式 AI 知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->