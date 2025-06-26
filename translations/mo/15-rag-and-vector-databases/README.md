<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e2861bbca91c0567ef32bc77fe054f9e",
  "translation_date": "2025-06-25T22:20:43+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "mo"
}
-->
# 檢索增強生成 (RAG) 和向量資料庫

[![檢索增強生成 (RAG) 和向量資料庫](../../../translated_images/15-lesson-banner.ac49e59506175d4fc6ce521561dab2f9ccc6187410236376cfaed13cde371b90.mo.png)](https://aka.ms/gen-ai-lesson15-gh?WT.mc_id=academic-105485-koreyst)

在搜索應用課程中，我們簡要了解了如何將自己的數據整合到大型語言模型 (LLM) 中。在本課程中，我們將深入探討在 LLM 應用中將數據作為基礎的概念、過程的機制以及存儲數據的方法，包括嵌入和文本。

> **影片即將推出**

## 介紹

在本課程中，我們將涵蓋以下內容：

- RAG 的介紹，它是什麼以及為什麼在人工智慧 (AI) 中使用。

- 了解什麼是向量資料庫，並為我們的應用創建一個。

- 一個如何將 RAG 整合到應用中的實際例子。

## 學習目標

完成本課程後，您將能夠：

- 解釋 RAG 在數據檢索和處理中的重要性。

- 設置 RAG 應用並將您的數據作為 LLM 的基礎

- 在 LLM 應用中有效整合 RAG 和向量資料庫。

## 我們的場景：用我們自己的數據增強我們的 LLM

在本課程中，我們希望將自己的筆記添加到教育初創公司中，這樣可以讓聊天機器人獲得更多不同主題的信息。利用我們的筆記，學習者將能夠更好地學習和理解不同的主題，使他們更容易準備考試。為了創建我們的場景，我們將使用：

- `Azure OpenAI:` 我們將用來創建聊天機器人的 LLM

- `AI for beginners' lesson on Neural Networks`：這將是我們將 LLM 作為基礎的數據

- `Azure AI Search` 和 `Azure Cosmos DB:` 向量資料庫來存儲我們的數據並創建搜索索引

用戶將能夠從他們的筆記中創建練習測驗、修訂閃卡並將其總結為簡明的概述。首先，讓我們看看什麼是 RAG 以及它如何運作：

## 檢索增強生成 (RAG)

一個由 LLM 驅動的聊天機器人處理用戶提示以生成回應。它旨在與用戶在廣泛的主題上進行互動。然而，其回應僅限於提供的上下文和其基礎訓練數據。例如，GPT-4 的知識截止日期是 2021 年 9 月，這意味著它缺乏對此期間之後發生的事件的了解。此外，用於訓練 LLM 的數據不包括機密信息，如個人筆記或公司的產品手冊。

### RAGs（檢索增強生成）如何工作

![展示 RAGs 如何工作的圖示](../../../translated_images/how-rag-works.f5d0ff63942bd3a638e7efee7a6fce7f0787f6d7a1fca4e43f2a7a4d03cde3e0.mo.png)

假設您想部署一個從您的筆記中創建測驗的聊天機器人，您將需要與知識庫建立連接。這就是 RAG 的救星之處。RAGs 的運作如下：

- **知識庫：** 在檢索之前，這些文件需要被攝取和預處理，通常是將大型文件分解為更小的塊，將其轉換為文本嵌入並存儲在資料庫中。

- **用戶查詢：** 用戶提出問題

- **檢索：** 當用戶提出問題時，嵌入模型從我們的知識庫中檢索相關信息，以提供更多將被納入提示的上下文。

- **增強生成：** LLM 根據檢索到的數據增強其回應。它允許生成的回應不僅基於預訓練數據，還基於來自添加上下文的相關信息。檢索到的數據用於增強 LLM 的回應。然後，LLM 向用戶的問題返回答案。

![展示 RAGs 架構的圖示](../../../translated_images/encoder-decode.f2658c25d0eadee2377bb28cf3aee8b67aa9249bf64d3d57bb9be077c4bc4e1a.mo.png)

RAGs 的架構是使用由兩部分組成的變壓器實現的：編碼器和解碼器。例如，當用戶提出問題時，輸入文本被“編碼”為捕捉單詞意義的向量，然後向量被“解碼”到我們的文件索引中，並根據用戶查詢生成新文本。LLM 使用編碼器-解碼器模型來生成輸出。

根據所提議的論文：[檢索增強生成在知識密集 NLP（自然語言處理軟體）任務中的應用](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst)，實現 RAG 時的兩種方法是：

- **_RAG-Sequence_** 使用檢索到的文件來預測用戶查詢的最佳答案

- **RAG-Token** 使用文件生成下一個標記，然後檢索它們以回答用戶的查詢

### 為什麼使用 RAGs？

- **信息豐富性：** 確保文本回應是最新的。因此，通過訪問內部知識庫來提高特定領域任務的性能。

- 通過利用知識庫中的**可驗證數據**來減少捏造，為用戶查詢提供上下文。

- **成本效益高**，因為它們比微調 LLM 更經濟。

## 創建知識庫

我們的應用基於我們的個人數據，即 AI 初學者課程中的神經網絡課程。

### 向量資料庫

與傳統資料庫不同，向量資料庫是一種專門設計用於存儲、管理和搜索嵌入向量的資料庫。它存儲文檔的數字表示。將數據分解為數字嵌入，使我們的 AI 系統更容易理解和處理數據。

我們將嵌入存儲在向量資料庫中，因為 LLM 對其接受的輸入標記數量有限制。由於您無法將整個嵌入傳遞給 LLM，我們需要將它們分解為塊，當用戶提出問題時，最像問題的嵌入將與提示一起返回。分塊還可以減少通過 LLM 傳遞的標記數量的成本。

一些流行的向量資料庫包括 Azure Cosmos DB、Clarifyai、Pinecone、Chromadb、ScaNN、Qdrant 和 DeepLake。您可以使用 Azure CLI 使用以下命令創建 Azure Cosmos DB 模型：

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### 從文本到嵌入

在我們存儲數據之前，我們需要將其轉換為向量嵌入，然後再將其存儲在資料庫中。如果您正在處理大型文件或長文本，您可以根據預期的查詢將其分塊。分塊可以在句子級別或段落級別進行。由於分塊從周圍的單詞中得出意義，您可以向塊中添加一些其他上下文，例如，通過添加文檔標題或在塊之前或之後包含一些文本。您可以按以下方式分塊數據：

```python
def split_text(text, max_length, min_length):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if len(' '.join(current_chunk)) < max_length and len(' '.join(current_chunk)) > min_length:
            chunks.append(' '.join(current_chunk))
            current_chunk = []

    # If the last chunk didn't reach the minimum length, add it anyway
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

分塊後，我們可以使用不同的嵌入模型嵌入我們的文本。您可以使用的一些模型包括：word2vec、OpenAI 的 ada-002、Azure Computer Vision 等。選擇要使用的模型將取決於您使用的語言、編碼的內容類型（文本/圖像/音頻）、它可以編碼的輸入大小以及嵌入輸出的長度。

使用 OpenAI 的 `text-embedding-ada-002` 模型嵌入文本的示例如下：
![嵌入詞語貓的圖示](../../../translated_images/cat.74cbd7946bc9ca380a8894c4de0c706a4f85b16296ffabbf52d6175df6bf841e.mo.png)

## 檢索和向量搜索

當用戶提出問題時，檢索器將其轉換為向量，然後使用查詢編碼器在我們的文檔搜索索引中搜索與輸入相關的向量。一旦完成，它將輸入向量和文檔向量都轉換為文本，並將其通過 LLM。

### 檢索

當系統嘗試快速從索引中查找滿足搜索標準的文檔時，就會發生檢索。檢索器的目標是獲取將用於提供上下文並將 LLM 基於您的數據的文檔。

在我們的資料庫中執行搜索有多種方法，例如：

- **關鍵字搜索** - 用於文本搜索

- **語義搜索** - 使用單詞的語義意義

- **向量搜索** - 使用嵌入模型將文檔從文本轉換為向量表示。檢索將通過查詢向量表示最接近用戶問題的文檔來完成。

- **混合** - 關鍵字和向量搜索的組合。

檢索的挑戰在於當資料庫中沒有類似的回應時，系統將返回它們能夠獲得的最佳信息。然而，您可以使用策略，如設置相關性的最大距離或使用混合搜索，結合關鍵字和向量搜索。在本課程中，我們將使用混合搜索，結合向量和關鍵字搜索。我們將數據存儲到一個包含塊和嵌入的數據框的列中。

### 向量相似性

檢索器將在知識資料庫中搜索彼此接近的嵌入，即最近的鄰居，因為它們是相似的文本。在用戶提出查詢的情況下，首先對其進行嵌入，然後與相似的嵌入匹配。常用的測量不同向量相似度的方法是餘弦相似性，它基於兩個向量之間的角度。

我們可以使用其他替代方法來測量相似性，例如歐幾里得距離，它是向量端點之間的直線，和點積，它測量兩個向量對應元素的乘積和。

### 搜索索引

進行檢索時，我們需要在執行搜索之前為我們的知識庫構建搜索索引。索引將存儲我們的嵌入，並且即使在大型資料庫中也能快速檢索最相似的塊。我們可以使用以下方法在本地創建索引：

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### 重新排序

一旦您查詢了資料庫，您可能需要根據最相關的結果對結果進行排序。重新排序 LLM 利用機器學習通過將搜索結果按相關性排序來提高搜索結果的相關性。使用 Azure AI 搜索，重新排序是自動為您完成的，使用語義重新排序器。使用最近鄰居的重新排序工作示例如下：

```python
# Find the most similar documents
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Print the most similar documents
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## 將所有內容整合在一起

最後一步是將我們的 LLM 添加到組合中，以便能夠獲得基於我們數據的回應。我們可以按以下方式實施：

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Convert the question to a query vector
    query_vector = create_embeddings(user_input)

    # Find the most similar documents
    distances, indices = nbrs.kneighbors([query_vector])

    # add documents to query  to provide context
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # combine the history and the user input
    history.append(user_input)

    # create a message object
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": history[-1]}
    ]

    # use chat completion to generate a response
    response = openai.chat.completions.create(
        model="gpt-4",
        temperature=0.7,
        max_tokens=800,
        messages=messages
    )

    return response.choices[0].message

chatbot(user_input)
```

## 評估我們的應用

### 評估指標

- 提供的回應質量，確保其聽起來自然、流暢且像人類

- 數據的基礎性：評估回應是否來自提供的文檔

- 相關性：評估回應是否與所提問題匹配並相關

- 流利度 - 評估回應在語法上是否合理

## 使用 RAG（檢索增強生成）和向量資料庫的用例

有許多不同的用例可以通過函數調用來改進您的應用，例如：

- 問答系統：將您的公司數據作為基礎的聊天，可以用於員工提問。

- 推薦系統：您可以創建一個系統來匹配最相似的值，例如電影、餐館等等。

- 聊天機器人服務：您可以存儲聊天歷史並根據用戶數據個性化對話。

- 基於向量嵌入的圖像搜索，這在進行圖像識別和異常檢測時很有用。

## 總結

我們已經涵蓋了 RAG 的基本領域，從將數據添加到應用程序、用戶查詢到輸出。為簡化 RAG 的創建，您可以使用 Semanti Kernel、Langchain 或 Autogen 等框架。

## 作業

為了繼續學習檢索增強生成 (RAG)，您可以構建：

- 使用您選擇的框架為應用構建前端

- 利用框架，無論是 LangChain 還是 Semantic Kernel，並重新創建您的應用。

恭喜您完成本課程 👏。

## 學習不止於此，繼續旅程

完成本課程後，請查看我們的[生成式 AI 學習集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，繼續提升您的生成式 AI 知識！

**免責聲明**：  
本文檔已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力追求準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應將原始語言的文檔視為權威來源。對於關鍵信息，建議進行專業人工翻譯。對於因使用本翻譯而產生的任何誤解或誤釋，我們概不負責。