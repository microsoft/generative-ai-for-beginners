# 使用 Meta 家族模型進行建構

## 介紹

本課程將涵蓋：

- 探索兩款主要的 Meta 家族模型 - Llama 3.1 和 Llama 3.2
- 了解每個模型的使用案例與場景
- 示範代碼範例，展示每個模型的獨特功能

## Meta 家族模型

在本課程中，我們將探索 Meta 家族或「Llama 群」中的兩款模型 - Llama 3.1 和 Llama 3.2。

這些模型有不同的變體，並且可在 GitHub Model 市場上使用。以下是使用 GitHub Models 來[原型設計 AI 模型](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)的更多細節。

模型變體：
- Llama 3.1 - 70B 指令版
- Llama 3.1 - 405B 指令版
- Llama 3.2 - 11B 視覺指令版
- Llama 3.2 - 90B 視覺指令版

*注意：Llama 3 也可在 GitHub Models 上取得，但不包含在本課程中介紹*

## Llama 3.1

Llama 3.1 擁有 4050 億參數，屬於開源大型語言模型（LLM）類別。

該模型是對早期版本 Llama 3 的升級，提供：

- 更大的上下文視窗 - 128k 代幣對比 8k 代幣
- 更大的最大輸出代幣數 - 4096 對比 2048
- 更佳的多語言支持 - 由於訓練代幣數增加

這些優勢使 Llama 3.1 能夠處理更複雜的生成式 AI 應用，包括：
- 原生函數調用 - 能力調用 LLM 工作流程外的外部工具與函數
- 更好的檢索輔助生成 (RAG) 表現 - 由於更高的上下文視窗
- 合成數據生成 - 能夠生成有效數據用於微調等任務

### 原生函數調用

Llama 3.1 經過微調，能更有效地進行函數或工具調用。它還內建有兩個工具，模型可以根據使用者的提示判斷需要使用這些工具。這些工具為：

- **Brave Search** - 可用於透過網路搜尋取得即時資訊，如天氣
- **Wolfram Alpha** - 可用於更複雜的數學計算，因此不必自己撰寫函數

您也可以創建自訂工具，讓 LLM 進行呼叫。

在下面的示範代碼中：

- 我們在系統提示中定義可用工具（brave_search、wolfram_alpha）。
- 傳送一個詢問特定城市天氣的使用者提示。
- LLM 將回應一個工具調用給 Brave Search 工具，看起來像這樣 `<|python_tag|>brave_search.call(query="Stockholm weather")`

*注意：此範例僅示範工具呼叫，若您想獲取結果，需在 Brave API 頁面註冊免費帳戶並定義函數本體。*

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

儘管 Llama 3.1 是大型語言模型，但其一項限制是缺乏多模態能力。也就是無法使用例如影像等不同類型的輸入作為提示並給出回應。此能力是 Llama 3.2 的主要特色之一。其他特點包括：

- 多模態能力 - 能夠評估文字與影像提示
- 小型到中型變體（11B 和 90B） - 提供彈性的部署選項
- 僅文字變體（1B 和 3B） - 允許模型部署於邊緣與行動裝置，並提供低延遲

多模態支持代表開源模型領域的一大進步。以下示範範例同時輸入影像與文字提示，取得 Llama 3.2 90B 的影像分析結果。

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

## 學習不會止步於此，持續前行

完成本課程後，請瀏覽我們的[生成式 AI 學習收藏](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，繼續提升您的生成式 AI 知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。雖然我們努力追求準確性，但請注意，自動翻譯可能仍包含錯誤或不準確之處。原始文件之母語版本應被視為權威資料來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯內容而產生的任何誤解或誤譯負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->