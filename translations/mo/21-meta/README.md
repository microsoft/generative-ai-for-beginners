<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:26:59+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "mo"
}
-->
# 使用 Meta 家族模型建構

## 介紹

本課程將涵蓋：

- 探索 Meta 家族的兩個主要模型 - Llama 3.1 和 Llama 3.2
- 理解每個模型的使用案例和情境
- 展示每個模型獨特功能的程式碼範例

## Meta 家族模型

在本課程中，我們將探索來自 Meta 家族或 "Llama Herd" 的兩個模型 - Llama 3.1 和 Llama 3.2。

這些模型有不同的變體，並可在 GitHub 模型市場上取得。這裡有更多關於使用 GitHub 模型進行 [AI 模型原型製作](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) 的詳細資訊。

模型變體：
- Llama 3.1 - 70B 指令
- Llama 3.1 - 405B 指令
- Llama 3.2 - 11B 視覺指令
- Llama 3.2 - 90B 視覺指令

*注意：Llama 3 也可在 GitHub 模型上取得，但不會在本課程中涵蓋*

## Llama 3.1

擁有 4050 億參數的 Llama 3.1 屬於開源 LLM 類別。

此模式是早期版本 Llama 3 的升級，提供：

- 更大的上下文窗口 - 128k tokens vs 8k tokens
- 更大的最大輸出 tokens - 4096 vs 2048
- 更好的多語言支援 - 由於訓練 tokens 的增加

這使得 Llama 3.1 在構建 GenAI 應用程式時能夠處理更複雜的使用案例，包括：
- 原生函數呼叫 - 能夠在 LLM 工作流程之外呼叫外部工具和函數
- 更好的 RAG 表現 - 由於更高的上下文窗口
- 合成數據生成 - 能夠創建有效的數據用於微調等任務

### 原生函數呼叫

Llama 3.1 已被微調以更有效地進行函數或工具呼叫。它還有兩個內建工具，模型可以根據用戶的提示識別需要使用。這些工具是：

- **Brave Search** - 可用於通過網絡搜索獲取最新資訊，如天氣
- **Wolfram Alpha** - 可用於更複雜的數學計算，因此不需要自行撰寫函數

您也可以創建自己的自定義工具，供 LLM 呼叫。

在下面的程式碼範例中：

- 我們在系統提示中定義可用工具（brave_search, wolfram_alpha）。
- 發送一個用戶提示，詢問某城市的天氣。
- LLM 將回應一個工具呼叫到 Brave Search 工具，看起來像這樣 `<|python_tag|>brave_search.call(query="Stockholm weather")`

*注意：此範例僅進行工具呼叫，如果您想獲得結果，您需要在 Brave API 頁面創建一個免費帳戶並定義函數本身*

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

儘管是 LLM，Llama 3.1 的一個限制是多模態性。即，能夠使用不同類型的輸入如圖片作為提示並提供回應。此功能是 Llama 3.2 的主要特色之一。這些功能還包括：

- 多模態性 - 能夠評估文字和圖片提示
- 小至中型尺寸變化（11B 和 90B） - 提供靈活的部署選擇
- 僅文字變化（1B 和 3B） - 允許模型部署在邊緣/移動設備上並提供低延遲

多模態支援代表開源模型世界的一大進步。下面的程式碼範例同時使用圖片和文字提示以獲得 Llama 3.2 90B 的圖片分析。

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

## 學習不止於此，繼續您的旅程

完成本課程後，請查看我們的 [生成式 AI 學習集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) 以繼續提升您的生成式 AI 知識！

**免責聲明**：
本文檔已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們努力追求準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。因使用本翻譯而引起的任何誤解或誤解，我們不承擔責任。