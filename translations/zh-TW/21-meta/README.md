# 使用 Meta 家族模型構建

## 介紹

本課程將涵蓋：

- 探討兩個主要的 Meta 家族模型——Llama 3.1 和 Llama 3.2
- 理解每個模型的使用案例和情境
- 代碼範例展示每個模型的獨特功能


## Meta 家族模型

在本課程中，我們將探索來自 Meta 家族或「Llama 群」的兩個模型——Llama 3.1 和 Llama 3.2。

這些模型有不同的版本，並可在 [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 中取得。

> **注意：** GitHub Models 將於 2026 年 7 月底退役。這裡有更多關於使用 [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) 進行 AI 模型原型設計的詳細資訊。

模型變體：
- Llama 3.1 - 70B 指令型
- Llama 3.1 - 405B 指令型
- Llama 3.2 - 11B 視覺指令型
- Llama 3.2 - 90B 視覺指令型

*注意：Llama 3 也在 Microsoft Foundry Models 中可用，但本課程不包含相關內容*

## Llama 3.1

Llama 3.1 擁有 4050 億參數，歸類為開源大型語言模型（LLM）。

這個模型是早期版本 Llama 3 的升級版本，具備：

- 更大的上下文窗口 —— 128k 代幣 vs 8k 代幣
- 更大的最大輸出代幣數 —— 4096 vs 2048
- 更好的多語言支持 —— 由於訓練代幣數的增加

這些特性讓 Llama 3.1 能夠在構建生成式 AI 應用時處理更複雜的使用情境，包括：
- 原生函數調用 —— 能夠呼叫 LLM 工作流程之外的外部工具和函數
- 更好的 RAG 性能 —— 借助更大的上下文窗口
- 合成數據生成 —— 能夠為微調等任務創建有效數據

### 原生函數調用

Llama 3.1 經過微調，更善於進行函數或工具調用。模型內建兩個工具，能根據使用者提示判斷是否需要使用。這些工具包括：

- **Brave Search** —— 可用於執行網頁搜尋以獲取最新資訊，如天氣
- **Wolfram Alpha** —— 用於更複雜的數學計算，無需自行撰寫函數

你也可以創建自訂工具供 LLM 調用。

在以下代碼範例中：

- 我們在系統提示中定義可用工具（brave_search, wolfram_alpha）。
- 發送一個詢問特定城市天氣的使用者提示。
- LLM 將回應一個調用 Brave Search 工具的指令，形式看起來像 `<|python_tag|>brave_search.call(query="Stockholm weather")`

*注意：此範例只做工具呼叫，如果想獲得結果，您需要在 Brave API 頁面上註冊免費帳號並自行定義函數。*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# 從您的 Microsoft Foundry 項目「總覽」頁面取得這些資訊
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Meta-Llama-3.1-405B-Instruct"

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

儘管是 LLM，Llama 3.1 的一個限制是缺乏多模態能力。也就是無法使用像圖片這類不同類型的輸入作為提示並給出回應。這正是 Llama 3.2 的主要功能之一。這些功能還包括：

- 多模態 —— 能夠同時處理文本和圖像提示
- 小至中型尺寸變體（11B 和 90B）—— 提供靈活的部署選項，
- 純文本變體（1B 和 3B）—— 允許模型部署在邊緣/行動裝置，提供低延遲

多模態支持是開源模型領域的一大進展。下面的代碼範例使用了圖像和文本提示，來從 Llama 3.2 90B 獲取對圖像的分析。


### 使用 Llama 3.2 的多模態支持

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

# 從您的 Microsoft Foundry 專案「總覽」頁面取得這些資料
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
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

## 學習不止於此，繼續前行

完成本課程後，請查看我們的 [生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，繼續提升你的生成式 AI 知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->