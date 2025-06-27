<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:27:33+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "tw"
}
-->
# 使用 Meta 家族模型進行建構

## 介紹

本課程將涵蓋：

- 探索 Meta 家族的兩個主要模型 - Llama 3.1 和 Llama 3.2
- 理解每個模型的使用案例和場景
- 顯示每個模型獨特功能的代碼範例

## Meta 家族模型

在本課程中，我們將探索 Meta 家族或“Llama 群”中的兩個模型 - Llama 3.1 和 Llama 3.2。

這些模型有不同的變體，可在 GitHub Model 市場上獲得。這裡有更多關於使用 GitHub Models [原型化 AI 模型](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)的詳細信息。

模型變體：
- Llama 3.1 - 70B 指令
- Llama 3.1 - 405B 指令
- Llama 3.2 - 11B 視覺指令
- Llama 3.2 - 90B 視覺指令

*注意：Llama 3 也可在 GitHub Models 上獲得，但不會在本課程中涵蓋*

## Llama 3.1

擁有 4050 億參數的 Llama 3.1 屬於開源 LLM 類別。

該模式是對早期版本 Llama 3 的升級，提供：

- 更大的上下文窗口 - 128k tokens vs 8k tokens
- 更大的最大輸出 tokens - 4096 vs 2048
- 更好的多語言支持 - 由於訓練 tokens 的增加

這使得 Llama 3.1 能夠在構建 GenAI 應用時處理更複雜的使用案例，包括：
- 原生函數調用 - 能夠調用 LLM 工作流程之外的外部工具和函數
- 更好的 RAG 性能 - 由於更高的上下文窗口
- 合成數據生成 - 能夠創建有效的數據以進行微調等任務

### 原生函數調用

Llama 3.1 已經過微調以更有效地進行函數或工具調用。它還有兩個內建工具，模型可以根據用戶的提示識別需要使用這些工具。這些工具是：

- **Brave Search** - 可用於通過網絡搜索獲取最新信息，例如天氣
- **Wolfram Alpha** - 可用於更複雜的數學計算，因此不需要編寫自己的函數。

您還可以創建自己的自定義工具供 LLM 調用。

在下面的代碼範例中：

- 我們在系統提示中定義了可用工具（brave_search, wolfram_alpha）。
- 發送用戶提示，詢問某城市的天氣。
- LLM 將回應一個工具調用，調用 Brave Search 工具，看起來像這樣 `<|python_tag|>brave_search.call(query="Stockholm weather")`

*注意：此範例僅進行工具調用，如果您希望獲得結果，您需要在 Brave API 頁面上創建免費帳戶並定義函數本身*

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

儘管是 LLM，Llama 3.1 的一個限制是多模態性。也就是說，能夠使用不同類型的輸入，如圖像作為提示並提供回應。這種能力是 Llama 3.2 的主要特徵之一。這些特徵還包括：

- 多模態性 - 能夠評估文本和圖像提示
- 小到中等大小的變體（11B 和 90B） - 提供靈活的部署選項，
- 僅文本變體（1B 和 3B） - 允許模型在邊緣/移動設備上部署並提供低延遲

多模態支持代表了開源模型世界的一大進步。下面的代碼範例同時使用圖像和文本提示來獲取 Llama 3.2 90B 的圖像分析。

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

## 學習不止於此，繼續探索之旅

完成本課程後，請查看我們的[生成式 AI 學習集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，以繼續提升您的生成式 AI 知識！

**免責聲明**：
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。應將原始文件的本地語言版本視為權威來源。對於關鍵信息，建議使用專業人工翻譯。對於因使用此翻譯而產生的任何誤解或誤釋，我們不承擔任何責任。