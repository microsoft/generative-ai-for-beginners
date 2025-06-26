<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:27:18+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "hk"
}
-->
# 使用 Meta 家族模型

## 介紹

這節課將涵蓋：

- 探索兩個主要的 Meta 家族模型 - Llama 3.1 和 Llama 3.2
- 了解每個模型的使用案例和場景
- 展示每個模型獨特功能的代碼示例

## Meta 家族模型

在這節課中，我們將探索 Meta 家族或 "Llama Herd" 的兩個模型 - Llama 3.1 和 Llama 3.2

這些模型有不同的變體，並在 GitHub 模型市場上提供。以下是使用 GitHub 模型 [原型化 AI 模型](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) 的更多詳細信息。

模型變體：
- Llama 3.1 - 70B 指令
- Llama 3.1 - 405B 指令
- Llama 3.2 - 11B 視覺指令
- Llama 3.2 - 90B 視覺指令

*注意：Llama 3 也可在 GitHub 模型上獲得，但不會在這節課中涵蓋*

## Llama 3.1

擁有 4050 億參數的 Llama 3.1 屬於開源 LLM 類別。

這個模型是早期版本 Llama 3 的升級，提供：

- 更大的上下文窗口 - 128k 代幣 vs 8k 代幣
- 更大的最大輸出代幣 - 4096 vs 2048
- 更好的多語言支持 - 由於訓練代幣的增加

這些使得 Llama 3.1 在構建 GenAI 應用程序時能夠處理更複雜的用例，包括：
- 本地函數調用 - 能夠調用 LLM 工作流程之外的外部工具和函數
- 更好的 RAG 性能 - 由於更高的上下文窗口
- 合成數據生成 - 能夠創建有效的數據以進行微調等任務

### 本地函數調用

Llama 3.1 已經過微調以更有效地進行函數或工具調用。它還有兩個內建工具，模型可以根據用戶的提示識別需要使用。這些工具是：

- **Brave Search** - 可以通過網絡搜索獲取最新的信息，如天氣
- **Wolfram Alpha** - 可以用於更複雜的數學計算，因此不需要自己編寫函數。

您還可以創建自己的自定義工具，供 LLM 調用。

在下面的代碼示例中：

- 我們在系統提示中定義了可用的工具（brave_search, wolfram_alpha）。
- 發送一個用戶提示，詢問某個城市的天氣。
- LLM 將以對 Brave Search 工具的調用作為回應，看起來像這樣 `<|python_tag|>brave_search.call(query="Stockholm weather")`

*注意：此示例僅進行工具調用，如果您想獲取結果，您需要在 Brave API 頁面上創建一個免費賬戶並定義函數本身*

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

儘管是 LLM，Llama 3.1 的一個限制是多模態性。也就是說，能夠使用不同類型的輸入，如圖像作為提示並提供回應。這種能力是 Llama 3.2 的主要特點之一。這些特點還包括：

- 多模態性 - 能夠評估文本和圖像提示
- 小到中等大小變體（11B 和 90B） - 提供靈活的部署選項，
- 僅限文本變體（1B 和 3B） - 允許模型部署在邊緣/移動設備上並提供低延遲

多模態支持代表了開源模型世界的一大進步。下面的代碼示例同時採用圖像和文本提示，從 Llama 3.2 90B 獲得圖像分析。

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

## 學習不停於此，繼續探索

完成這節課後，查看我們的 [生成式 AI 學習系列](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) 以繼續提升您的生成式 AI 知識！

**免責聲明**：
本文檔是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯的。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業的人類翻譯。我們對使用此翻譯而引起的任何誤解或誤釋不承擔責任。