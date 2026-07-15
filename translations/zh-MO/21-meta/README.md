# 使用 Meta 家族模型構建

## 介紹

本課程將涵蓋：

- 探討兩個主要的 Meta 家族模型 - Llama 3.1 和 Llama 3.2
- 理解每個模型的使用案例和應用場景
- 代碼範例展示每個模型的獨特功能


## Meta 家族模型

在本課程中，我們將探討來自 Meta 家族或「Llama 群」的兩個模型 - Llama 3.1 和 Llama 3.2。

這些模型有不同變體，並可在 [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 中獲得。

> **注意：**GitHub Models 將於 2026 年 7 月底退休。這裡有更多關於使用 [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) 進行 AI 模型原型開發的詳細資訊。

模型變體：
- Llama 3.1 - 70B 指令模式
- Llama 3.1 - 405B 指令模式
- Llama 3.2 - 11B 視覺指令模式
- Llama 3.2 - 90B 視覺指令模式

*注意：Llama 3 也在 Microsoft Foundry Models 中提供，但本課程不涵蓋該模型*

## Llama 3.1

Llama 3.1 擁有 4050 億參數，屬於開源大語言模型（LLM）類別。

該模型是先前發佈的 Llama 3 的升級版，提供了：

- 更大的上下文視窗 - 128k 令牌對比 8k 令牌
- 更大的最大輸出令牌數 - 4096 對比 2048
- 更好的多語言支援 - 由於訓練令牌數增加

這些功能使 Llama 3.1 能夠處理更複雜的生成式 AI 應用案例，包括：
- 原生函數調用 - 能夠呼叫 LLM 工作流程之外的外部工具和函數
- 更好的檢索式生成（RAG）性能 - 因為上下文視窗更大
- 合成數據生成 - 能夠為微調等任務創建有效數據

### 原生函數調用

Llama 3.1 經過微調，使其在函數或工具調用方面更為有效。它內建兩個工具，模型可以根據使用者的提示識別需要使用的工具。這些工具是：

- **Brave Search** - 可用於透過網頁搜尋獲取最新資訊，例如天氣
- **Wolfram Alpha** - 可用於進行更複雜的數學計算，因此不需要自己撰寫函數

您也可以建立自己的自訂工具，讓 LLM 可以呼叫。

在以下代碼範例中：

- 我們在系統提示中定義可用工具（brave_search、wolfram_alpha）。
- 傳送一個詢問某城市天氣的使用者提示。
- LLM 將以呼叫 Brave Search 工具的方式回應，格式類似 `<|python_tag|>brave_search.call(query="Stockholm weather")`

*注意：這個範例只展示了工具調用，若您想取得結果，需要在 Brave API 頁面建立免費帳號並定義該函數本身。*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# 從你的 Microsoft Foundry 項目「概覽」頁面獲取這些資訊
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

雖然是 LLM，Llama 3.1 的一個限制是缺乏多模態能力。換言之，它無法使用影像等不同類型輸入作為提示並提供回應。這正是 Llama 3.2 的主要功能之一。這些功能還包括：

- 多模態 - 能夠處理文字和影像提示
- 小到中型規模變體（11B 和 90B） - 提供靈活的部署選項
- 僅文字變體（1B 和 3B） - 允許模型部署於邊緣/行動裝置並提供低延遲

多模態支援是開源模型領域的一大進步。下面的代碼範例同時接受影像和文字提示，以取得 Llama 3.2 90B 對影像的分析。


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

# 從你的 Microsoft Foundry 專案的「概覽」頁面取得這些資訊
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

## 持續學習，旅程不止於此

完成本課程後，請查看我們的 [生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，繼續提升你的生成式 AI 知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->