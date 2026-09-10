# 使用 Meta 家族模型構建

## 介紹

本課程將涵蓋：

- 探索兩個主要的 Meta 家族模型 - Llama 3.1 和 Llama 3.2
- 了解每個模型的使用案例和場景
- 範例程式碼展示每個模型的獨特功能


## Meta 家族模型

在本課程中，我們將探討來自 Meta 家族或“Llama Herd”的兩個模型——Llama 3.1 與 Llama 3.2。

這些模型有不同的變體，並可在 [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 中取得。

> **注意：** GitHub 模型將於 2026 年 7 月底退役。這裡有更多關於使用 [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) 來進行 AI 模型原型的詳細資訊。

模型變體：
- Llama 3.1 - 70B 指令型
- Llama 3.1 - 405B 指令型
- Llama 3.2 - 11B 視覺指令型
- Llama 3.2 - 90B 視覺指令型

*備註：Llama 3 也在 Microsoft Foundry Models 中可用，但本課程不涵蓋*

## Llama 3.1

Llama 3.1 以 4050 億參數，屬於開源大型語言模型（LLM）類別。

此模型是早期版本 Llama 3 的升級版本，具備：

- 更大的上下文視窗 - 128k 令牌，相較於 8k 令牌
- 更大的最大輸出令牌數 - 4096，相較於 2048
- 更好的多語言支援 - 由於訓練令牌增加

這些功能使 Llama 3.1 能夠處理更複雜的生成式 AI 應用場景，包括：
- 原生函式呼叫 - 能從 LLM 工作流之外呼叫外部工具和函式
- 更佳的 RAG 性能 - 基於更大的上下文視窗
- 合成數據生成 - 能為細調等任務創建有效數據

### 原生函式呼叫

Llama 3.1 已被微調以更有效地進行函式或工具呼叫。它還有兩個內建工具，模型可以根據使用者的提示判斷需要使用這些工具。這些工具是：

- **Brave Search** - 可用於通過網路搜尋獲取最新資訊，如天氣
- **Wolfram Alpha** - 可用於進行較複雜的數學計算，因此不需自行撰寫函式

你也可以創建自己的自訂工具供 LLM 呼叫。

在下面的程式碼範例中：

- 我們在系統提示中定義可用工具 (brave_search, wolfram_alpha)。
- 發送要求特定城市天氣的使用者提示。
- LLM 將回應帶有對 Brave Search 工具的呼叫，格式如下 `<|python_tag|>brave_search.call(query="Stockholm weather")`

*注意：此範例僅示範工具呼叫，若想取得結果，你需在 Brave API 頁面創建免費帳號並定義該函式。*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# 從您的 Microsoft Foundry 專案的「概覽」頁面取得這些資訊
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

儘管 Llama 3.1 屬於大型語言模型，但其無法多模態輸入，即無法使用影像等不同類型輸入作為提示並提供回應，這是其一大限制。Llama 3.2 則提供了這項能力。其他功能包括：

- 多模態 - 能同時評估文字與影像提示
- 小至中型變體 (11B 和 90B) - 提供彈性的部署選擇
- 純文字變體 (1B 和 3B) - 允許模型部署於邊緣或行動裝置，並提供低延遲

多模態支援是在開源模型領域的一大進展。以下程式碼範例同時傳入影像與文字提示，藉由 Llama 3.2 90B 取得影像分析結果。


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

# 從您的 Microsoft Foundry 專案「總覽」頁面取得這些資訊
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

完成本課程後，請查看我們的 [生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升你的生成式 AI 知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->