# 使用 Meta 家族模型構建

## 介紹

本課程將涵蓋：

- 探索兩個主要的 Meta 家族模型 - Llama 3.1 和 Llama 3.2
- 了解每個模型的使用案例和情境
- 代碼範例展示每個模型的獨特功能


## Meta 家族模型

在本課程中，我們將探索來自 Meta 家族或「Llama 群」的兩個模型 - Llama 3.1 和 Llama 3.2。

這些模型有不同變體，並且可在[Microsoft Foundry Models 目錄](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)中獲得。

> **注意：** GitHub Models 將於 2026 年 7 月底退休。這裡有更多關於使用[Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst)來進行 AI 模型原型設計的詳細資訊。

模型變體：
- Llama 3.1 - 70B 指令式
- Llama 3.1 - 405B 指令式
- Llama 3.2 - 11B 視覺指令式
- Llama 3.2 - 90B 視覺指令式

*注意：Llama 3 也在 Microsoft Foundry Models 提供，但本課程不涵蓋*

## Llama 3.1

以 4050 億參數計，Llama 3.1 屬於開源大型語言模型（LLM）類別。

這個模型是早期版本 Llama 3 的升級，提供：

- 更大的上下文窗口 - 128k 字元對比 8k 字元
- 更大的最大輸出字元數 - 4096 對比 2048
- 更佳的多語言支援 - 由於訓練字元數增加

這些功能讓 Llama 3.1 在建立生成式 AI 應用時能處理更複雜的用例，包括：
- 原生函數調用 - 能夠呼叫 LLM 工作流程外的外部工具和函數
- 更好的檢索增強生成（RAG）性能 - 由於更大的上下文窗口
- 合成數據生成 - 能夠為微調等任務創造有效數據

### 原生函數調用

Llama 3.1 已微調以更有效進行函數或工具調用。它還有兩個內建工具，模型可以根據用戶提示判斷需要使用的工具。這些工具有：

- **Brave Search** - 可用於進行網絡搜尋以獲取最新資訊，如天氣
- **Wolfram Alpha** - 可用於更複雜的數學計算，無需自行編寫函數

你也可以建立自己的自定義工具，供 LLM 呼叫。

在下面的程式碼範例中：

- 我們在系統提示中定義可用工具（brave_search, wolfram_alpha）。
- 發送一個詢問特定城市天氣的使用者提示。
- LLM 將以對 Brave Search 工具的調用回應，形式如 `<|python_tag|>brave_search.call(query="Stockholm weather")`

*注意：此範例僅進行工具調用，如欲獲得結果，你需在 Brave API 頁面創建免費帳號並定義函數本身。*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# 從你的 Microsoft Foundry 專案的「概覽」頁面取得這些資訊
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

儘管是 LLM，Llama 3.1 的一個限制是缺乏多模態能力。也就是無法使用不同類型輸入（例如影像）作為提示並提供回應。Llama 3.2 的一大特點便是具備這種能力。其他功能還包括：

- 多模態支持 - 能評估文字和影像提示
- 小到中型規模變體（11B 和 90B） - 提供靈活的部署選擇，
- 僅文字變體（1B 和 3B） - 允許模型部署於邊緣/移動裝置並提供低延遲

多模態支持是開源模型界的一大進步。下面的程式碼範例同時使用影像和文字提示，讓 Llama 3.2 90B 分析該影像。


### Llama 3.2 的多模態支持

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

# 從你的 Microsoft Foundry 專案的「總覽」頁面獲取這些資料
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

完成本課程後，請查看我們的[生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升你的生成式 AI 知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->