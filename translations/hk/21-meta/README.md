<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:07:10+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "hk"
}
-->
# 使用 Meta 家族模型構建

## 介紹

本課程將涵蓋：

- 探索兩個主要的 Meta 家族模型 - Llama 3.1 和 Llama 3.2
- 了解每個模型的使用場景和應用情境
- 透過程式碼範例展示各模型的獨特功能

## Meta 家族模型

在本課程中，我們將探索來自 Meta 家族或「Llama Herd」的兩個模型 - Llama 3.1 和 Llama 3.2

這些模型有不同的變體，並且可在 GitHub Model 市場上取得。以下是使用 GitHub Models 來[以 AI 模型進行原型設計](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)的更多細節。

模型變體：
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*注意：Llama 3 也可在 GitHub Models 上取得，但本課程不涵蓋該模型*

## Llama 3.1

擁有 4050 億參數的 Llama 3.1 屬於開源大型語言模型（LLM）類別。

此模型是早期版本 Llama 3 的升級版，提供：

- 更大的上下文視窗 - 128k 代幣對比 8k 代幣
- 更大的最大輸出代幣數 - 4096 對比 2048
- 更佳的多語言支援 - 由於訓練代幣數增加

這些改進使 Llama 3.1 能夠處理更複雜的生成式 AI 應用場景，包括：
- 原生函數調用 - 能夠呼叫 LLM 工作流程外的外部工具和函數
- 更佳的 RAG 表現 - 由於更大的上下文視窗
- 合成數據生成 - 能夠為微調等任務創建有效數據

### 原生函數調用

Llama 3.1 經過微調，能更有效地進行函數或工具調用。它還內建兩個工具，模型能根據使用者的提示判斷是否需要使用這些工具。這些工具包括：

- **Brave Search** - 可用於透過網路搜尋獲取最新資訊，例如天氣
- **Wolfram Alpha** - 可用於更複雜的數學計算，無需自行撰寫函數

你也可以創建自訂工具供 LLM 調用。

以下程式碼範例中：

- 我們在系統提示中定義可用工具（brave_search、wolfram_alpha）
- 傳送一個詢問某城市天氣的使用者提示
- LLM 將回應一個對 Brave Search 工具的調用，形式類似 `<|python_tag|>brave_search.call(query="Stockholm weather")`

*注意：此範例僅示範工具調用，若想取得結果，需在 Brave API 頁面註冊免費帳號並定義該函數本身*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "meta-llama-3.1-405b-instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)


tool_prompt=f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Environment: ipython
Tools: brave_search, wolfram_alpha
Cutting Knowledge Date: December 2023
Today Date: 23 July 2024

You are a helpful assistant<|eot_id|>
"""

messages = [
    SystemMessage(content=tool_prompt),
    UserMessage(content="What is the weather in Stockholm?"),

]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```

## Llama 3.2

儘管 Llama 3.1 是大型語言模型，但其一個限制是多模態能力，也就是能使用不同類型的輸入（如圖片）作為提示並提供回應。這正是 Llama 3.2 的主要特色之一。其他功能還包括：

- 多模態能力 - 能同時處理文字和圖片提示
- 小至中型變體（11B 和 90B） - 提供靈活的部署選項
- 純文字變體（1B 和 3B） - 允許模型部署於邊緣或行動裝置，並提供低延遲

多模態支援代表開源模型領域的一大進步。以下程式碼範例同時使用圖片和文字提示，讓 Llama 3.2 90B 對圖片進行分析。

### Llama 3.2 的多模態支援

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    SystemMessage,
    UserMessage,
    TextContentItem,
    ImageContentItem,
    ImageUrl,
    ImageDetailLevel,
)
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "Llama-3.2-90B-Vision-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(
            content="You are a helpful assistant that describes images in details."
        ),
        UserMessage(
            content=[
                TextContentItem(text="What's in this image?"),
                ImageContentItem(
                    image_url=ImageUrl.load(
                        image_file="sample.jpg",
                        image_format="jpg",
                        detail=ImageDetailLevel.LOW)
                ),
            ],
        ),
    ],
    model=model_name,
)

print(response.choices[0].message.content)
```

## 學習不止於此，繼續你的旅程

完成本課程後，請參考我們的[生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升你的生成式 AI 知識！

**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。