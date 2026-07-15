# 使用 Meta 家族模型構建

## 介紹

本課程將涵蓋：

- 探索兩個主要的 Meta 家族模型 - Llama 3.1 和 Llama 3.2
- 理解每個模型的使用案例和場景
- 代碼示例展示每個模型的獨特功能


## Meta 家族模型

在本課程中，我們將探討 Meta 家族或「Llama Herd」的兩個模型 - Llama 3.1 和 Llama 3.2。

這些模型有不同的變體，並可在 [Microsoft Foundry Models 目錄](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 中使用。

> **注意：** GitHub Models 將於 2026 年 7 月底停止服務。這裡有更多關於使用 [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) 來進行 AI 模型原型製作的詳細資訊。

模型變體：
- Llama 3.1 - 70B 指令式（Instruct）
- Llama 3.1 - 405B 指令式（Instruct）
- Llama 3.2 - 11B 視覺指令式（Vision Instruct）
- Llama 3.2 - 90B 視覺指令式（Vision Instruct）

*注意：Llama 3 也在 Microsoft Foundry Models 中提供，但本課程不涵蓋*

## Llama 3.1

Llama 3.1 擁有 4050 億參數，屬於開源大型語言模型類別。

這個模型是早期 Llama 3 版本的升級，提供了：

- 較大的上下文視窗 - 128k 令牌對比 8k 令牌
- 較大的最大輸出令牌數 - 4096 對比 2048
- 較佳的多語言支持 - 由於訓練令牌數量增加

這些使 Llama 3.1 能夠處理更複雜的生成式 AI 應用案例，包括：
- 原生函數呼叫 - 能夠呼叫外部工具和函數，超出 LLM 工作流程
- 更佳的檢索增強生成（RAG）性能 - 由於更高的上下文視窗
- 合成數據生成 - 能夠為微調等任務創建有效數據

### 原生函數呼叫

Llama 3.1 已經進行微調，使其在函數或工具呼叫上更有效率。它還內建了兩個工具，模型可根據用戶的提示識別需要使用哪一工具。這兩種工具是：

- **Brave Search** - 可用於進行網絡搜索以獲取最新資訊，如天氣
- **Wolfram Alpha** - 可用於更複雜的數學計算，無需自己撰寫函數

你也可以創建自訂工具，讓 LLM 可以呼叫。

在以下代碼示例中：

- 我們在系統提示裡定義了可用工具（brave_search, wolfram_alpha）。
- 傳送用戶提示，詢問某城市的天氣。
- LLM 將回應帶有對 Brave Search 工具的調用，如 `<|python_tag|>brave_search.call(query="Stockholm weather")`

*注意：此範例只展示工具呼叫，若想取得結果，需於 Brave API 頁面免費註冊並定義該函數本身。*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# 從你的 Microsoft Foundry 專案的「概覽」頁面獲取這些資料
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

雖然是大型語言模型，Llama 3.1 的一大限制是缺乏多模態能力。也就是說，無法使用圖片等不同類型的輸入作為提示並給出回應。這正是 Llama 3.2 的主要特色之一。其他特色還包含：

- 多模態能力 - 能同時處理文字和圖片提示
- 小到中等尺寸變體（11B 和 90B） - 提供彈性部署選項
- 純文字變體（1B 和 3B） - 適合部署於邊緣或行動裝置，提供低延遲

多模態支持標誌著開源模型領域的一大進步。以下程式碼示例同時使用圖片和文字提示，從 Llama 3.2 90B 獲取圖片分析結果。


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

# 從你的 Microsoft Foundry 項目的「概覽」頁面獲取這些資料
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

完成本課程後，請查看我們的 [生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升您的生成式 AI 知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->