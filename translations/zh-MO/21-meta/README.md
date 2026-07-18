# 使用 Meta 系列模型進行建構

## 介紹

本課程將涵蓋：

- 探索兩款主要的 Meta 系列模型 - Llama 3.1 與 Llama 3.2
- 了解每個模型的使用案例及場景
- 使用程式碼範例展示各模型的獨特功能


## Meta 系列模型

本課程將探討兩款來自 Meta 系列或稱「Llama 群」的模型 - Llama 3.1 和 Llama 3.2。

這些模型有不同的版本，可在 [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 中取得。

> **注意：** GitHub Models 將於 2026 年 7 月底停用。關於使用 [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) 進行 AI 模型原型開發的詳細訊息，請參閱說明。

模型版本：
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*備註：Llama 3 也可於 Microsoft Foundry Models 取得，但本課程不包括此版本內容*

## Llama 3.1

Llama 3.1 擁有 4050 億參數，屬於開源大型語言模型類別。

該模型是先前版本 Llama 3 的升級版，提供以下改進：

- 更大的上下文視窗 - 128k 代幣，較之前的 8k 代幣大幅提升
- 更大的最大輸出代幣數 - 4096，相較之前的 2048 增加一倍
- 更佳的多語言支援 - 由於訓練代幣數增加

這些改進使 Llama 3.1 能夠處理更複雜的生成式 AI 應用案例，包括：
- 本地函數呼叫 - 能夠在大型語言模型流程之外調用外部工具與函數
- 更優的 RAG 表現 - 受益於更大的上下文視窗
- 合成數據生成 - 能產生有效數據以用於微調等任務

### 本地函數呼叫

Llama 3.1 經過微調，於函數或工具呼叫方面更為高效。它內建兩個工具，模型能根據使用者提示判斷是否應使用這些工具。這些工具包括：

- **Brave Search** - 可用於通過網絡搜索獲取如天氣等即時資訊
- **Wolfram Alpha** - 可用於較複雜的數學計算，無須編寫自訂函數

你也可以建立自定義工具讓大型語言模型調用。

在以下的程式碼示例中：

- 在系統提示中定義可用的工具（brave_search, wolfram_alpha）。
- 傳送詢問某城市天氣的用戶提示。
- 大型語言模型將回應一個工具呼叫給 Brave Search，格式類似 `<|python_tag|>brave_search.call(query="Stockholm weather")`

*注意：此範例僅示範工具呼叫，若想取得結果，需於 Brave API 頁面創建免費帳號並定義函數本體。*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# 從你的Microsoft Foundry項目之「概覽」頁面獲取這些資料
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

Llama 3.1 作為大型語言模型的缺點之一是缺乏多模態支援，即無法使用圖片等不同類型輸入作為提示並提供回應。而 Llama 3.2 的主要功能之一就是具備這項能力。其他特點還包括：

- 多模態能力 - 同時能處理文本與影像提示
- 小型至中型版本（11B 與 90B）- 提供彈性的部署選項
- 僅文字版本（1B 與 3B）- 允許模型部署於邊緣或行動裝置，且延遲低

多模態支援在開源模型領域是一大飛躍。下面的程式碼範例會同時使用影像與文字作為提示，以讓 Llama 3.2 90B 對該圖像進行分析。


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

# 從你的 Microsoft Foundry 項目「概覽」頁面獲取這些資訊
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

## 學習不止於此，繼續旅程

完成本課程後，歡迎瀏覽我們的 [生成式 AI 學習收藏](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升你的生成式 AI 知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->