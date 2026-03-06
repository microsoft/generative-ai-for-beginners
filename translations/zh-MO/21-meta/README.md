# 使用 Meta 系列模型構建

## 介紹

本課程將涵蓋：

- 探索兩大 Meta 系列模型 - Llama 3.1 與 Llama 3.2  
- 了解每個模型的使用案例與場景  
- 以程式碼範例展示每個模型的獨特功能  

## Meta 系列模型

在本課程中，我們將探索來自 Meta 系列或「Llama 群」的兩個模型 - Llama 3.1 與 Llama 3.2。

這些模型有不同變體，並在 GitHub Model 市場提供。以下是使用 GitHub Models [與 AI 模型進行原型設計](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) 的更多詳情。

模型變體：  
- Llama 3.1 - 70B 指令模式  
- Llama 3.1 - 405B 指令模式  
- Llama 3.2 - 11B 視覺指令模式  
- Llama 3.2 - 90B 視覺指令模式  

*注意：Llama 3 也可於 GitHub Models 獲得，但本課程不涵蓋*

## Llama 3.1

擁有 4050 億參數的 Llama 3.1 屬於開源大型語言模型 (LLM) 範疇。

此模型是早期版本 Llama 3 的升級，提供了：

- 更大的上下文視窗 - 128k 代幣 相較於 8k 代幣  
- 更大的最大輸出代幣數 - 4096 相較於 2048  
- 更佳的多語言支援 - 由於訓練代幣數量提升  

這些功能使 Llama 3.1 能夠處理更複雜的 GenAI 應用，如：  
- 原生函數呼叫 - 能夠在 LLM 工作流程之外呼叫外部工具與函數  
- 更佳的 RAG 表現 - 憑藉更大的上下文視窗  
- 合成數據生成 - 能為微調等任務創建有效數據  

### 原生函數呼叫

Llama 3.1 已進行微調，使其在函數或工具呼叫方面更有效。它還內建兩個模型可根據使用者提示識別並使用的工具，這些工具是：

- **Brave Search** - 用於透過網路搜尋獲得即時資訊，如天氣  
- **Wolfram Alpha** - 用於更複雜的數學計算，無需自行編寫函數  

你也可以創建自己的自訂工具，供 LLM 呼叫。

以下程式碼範例中：

- 我們在系統提示中定義可用工具（brave_search, wolfram_alpha）。  
- 傳送詢問某城市天氣的使用者提示。  
- LLM 將以工具呼叫回應 Brave Search，格式如 `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*注意：此範例僅進行工具呼叫，如需獲取結果，須先於 Brave API 頁面註冊免費帳號並定義該函數。*

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

雖為大型語言模型，Llama 3.1 的一大限制是缺乏多模態能力。換言之，無法使用圖片等不同種類輸入並提供回應。這正是 Llama 3.2 的主要特色之一。其他特點包括：

- 多模態能力 - 可處理文字與圖片提示  
- 中小型變體（11B 與 90B） - 提供靈活部署選項  
- 僅文字變體（1B 與 3B） - 可部署於邊緣 / 行動裝置，具備低延遲  

此多模態支援是開源模型領域一大進步。以下程式碼範例同時採用圖片與文字提示，從 Llama 3.2 90B 取得圖片分析。

### 使用 Llama 3.2 的多模態支援

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

## 學習不止步，持續旅程

完成本課程後，請參閱我們的 [生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升你的生成式 AI 知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言版本之文件應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們對因使用此翻譯而引致之任何誤解或誤譯不負責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->