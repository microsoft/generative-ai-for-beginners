# 使用 Meta 系列模型建構

## 簡介

本課程將涵蓋：

- 探索 Meta 兩大系列模型 - Llama 3.1 與 Llama 3.2
- 理解每款模型的應用場景與使用案例
- 程式碼範例展示每款模型的獨特功能

## Meta 系列模型

在本課程中，我們將探索來自 Meta 系列或稱「Llama 群」的兩款模型 - Llama 3.1 與 Llama 3.2。

這些模型有不同的變體，且可於 GitHub Model 市場上取得。以下是關於使用 GitHub Models [以 AI 模型原型製作](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) 的更多詳情。

模型變體：
- Llama 3.1 - 70B 指令型
- Llama 3.1 - 405B 指令型
- Llama 3.2 - 11B 視覺指令型
- Llama 3.2 - 90B 視覺指令型

*註：Llama 3 也於 GitHub Models 提供，但本課程不涵蓋*

## Llama 3.1

擁有 4050 億參數的 Llama 3.1 屬於開源大型語言模型範疇。

該模型是早期推出的 Llama 3 的升級版，提供了：

- 較大語境視窗 - 128k 代幣對比 8k 代幣
- 較大最大輸出代幣數 - 4096 對比 2048
- 更佳的多語言支援 - 因訓練代幣增加

這些功能使 Llama 3.1 能處理更複雜的 GenAI 應用場景，包括：
- 原生函數呼叫 - 能夠呼叫 LLM 工作流程外的外部工具和函數
- 更佳的 RAG 性能 - 因為更大的語境視窗
- 合成資料生成 - 能創造有效資料用於微調等任務

### 原生函數呼叫

Llama 3.1 經過微調，更有效率地呼叫函數或工具。模型內建兩個工具，能根據使用者提示識別並使用。這兩個工具是：

- **Brave Search** - 可用於執行網頁搜尋, 獲取最新資料如天氣
- **Wolfram Alpha** - 可用於更複雜的數學計算，無需自行撰寫函數

您亦可創建自訂工具供 LLM 呼叫。

下面的範例程式碼中：

- 我們在系統提示中定義可用工具（brave_search、wolfram_alpha）
- 傳送使用者提示查詢特定城市天氣
- LLM 將回應呼叫 Brave Search 工具，顯示為 `<|python_tag|>brave_search.call(query="Stockholm weather")`

*註：此範例僅示範呼叫工具，若要取得結果須在 Brave API 頁面免費註冊帳戶並定義函數本體。*

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

雖同為大型語言模型，但 Llama 3.1 有一限制是缺乏多模態能力，即無法使用圖片等多種輸入作為提示並給出回應。這正是 Llama 3.2 的主要特色之一。其功能還包括：

- 多模態 - 能同時評估文本與圖片提示
- 中小型規模變體（11B 與 90B） - 提供彈性部署選項
- 純文字變體（1B 與 3B） - 便於在邊緣/行動裝置部署，且低延遲

多模態支援代表了開源模型世界的一大突破。下方程式碼範例同時接收圖片和文字提示，並由 Llama 3.2 90B 執行圖片分析。

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

完成本課程後，歡迎參考我們的 [生成式 AI 學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升你的生成式 AI 知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件經由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的原文版本應被視為正式且具權威性的資料來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用本翻譯而引致的任何誤解或錯誤詮釋概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->