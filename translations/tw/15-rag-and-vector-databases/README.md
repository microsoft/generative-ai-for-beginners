<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e2861bbca91c0567ef32bc77fe054f9e",
  "translation_date": "2025-06-25T22:21:58+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "tw"
}
-->
# 檢索增強生成 (RAG) 和向量資料庫

在搜尋應用程式的課程中，我們簡單學習了如何將您自己的資料整合到大型語言模型 (LLMs) 中。在這堂課中，我們將深入探討在您的 LLM 應用程式中將資料基礎化的概念，過程的機制以及儲存資料的方法，包括嵌入和文本。

> **影片即將推出**

## 介紹

在這堂課中，我們將涵蓋以下內容：

- 介紹 RAG，它是什麼以及為什麼在人工智慧 (AI) 中使用它。

- 了解什麼是向量資料庫並為我們的應用程式創建一個。

- 一個如何將 RAG 整合到應用程式中的實際例子。

## 學習目標

完成這堂課後，您將能夠：

- 解釋 RAG 在資料檢索和處理中的重要性。

- 設置 RAG 應用程式並將您的資料基礎化到 LLM

- 在 LLM 應用程式中有效整合 RAG 和向量資料庫。

## 我們的情境：用我們自己的資料增強 LLMs

在這堂課中，我們希望將自己的筆記添加到教育初創公司中，這樣聊天機器人可以獲取更多關於不同主題的信息。使用我們的筆記，學習者將能夠更好地學習和理解不同的主題，使他們更容易準備考試。為了創建我們的情境，我們將使用：

- `Azure OpenAI:` 我們將用來創建聊天機器人的 LLM

- `AI for beginners' lesson on Neural Networks`：這將是我們基礎化 LLM 的資料

- `Azure AI Search` 和 `Azure Cosmos DB:` 向量資料庫來儲存我們的資料並創建一個搜尋索引

用戶將能夠從他們的筆記中創建練習測驗、修訂閃卡並將其總結為簡明的概述。首先，讓我們來看看什麼是 RAG 以及它如何運作：

## 檢索增強生成 (RAG)

一個由 LLM 驅動的聊天機器人處理用戶提示以生成回應。它旨在與用戶在各種主題上互動。然而，其回應僅限於提供的上下文和其基礎的訓練資料。例如，GPT-4 的知識截止日期是 2021 年 9 月，這意味著它缺乏在此之後發生的事件的知識。此外，用於訓練 LLMs 的資料不包括機密信息，如個人筆記或公司的產品手冊。

### RAGs（檢索增強生成）如何運作

假設您想部署一個從您的筆記中創建測驗的聊天機器人，您將需要一個連接到知識庫的連接。這就是 RAG 的救星之處。RAGs 的運作如下：

- **知識庫：** 在檢索之前，這些文件需要被攝取和預處理，通常是將大型文件分解為較小的塊，轉換為文本嵌入並儲存在資料庫中。

- **用戶查詢：** 用戶提出問題

- **檢索：** 當用戶提出問題時，嵌入模型從我們的知識庫中檢索相關信息，以提供將被納入提示的更多上下文。

- **增強生成：** LLM 根據檢索到的資料增強其回應。這使得生成的回應不僅基於預訓練資料，還基於來自添加的上下文的相關信息。檢索到的資料用於增強 LLM 的回應。然後，LLM 向用戶的問題返回答案。

RAGs 的架構使用由兩部分組成的變壓器實現：編碼器和解碼器。例如，當用戶提出問題時，輸入文本被“編碼”為捕捉單詞意義的向量，然後向量被“解碼”為我們的文件索引，並根據用戶查詢生成新文本。LLM 使用編碼器-解碼器模型生成輸出。

根據提議的論文：[知識密集型 NLP（自然語言處理軟件）任務的檢索增強生成](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) 實現 RAG 的兩種方法是：

- **_RAG-Sequence_** 使用檢索到的文件來預測用戶查詢的最佳答案

- **RAG-Token** 使用文件生成下一個標記，然後檢索它們以回答用戶的查詢

### 為什麼要使用 RAGs？

- **信息豐富性：** 確保文本回應是最新的。因此，通過訪問內部知識庫提高在特定領域任務上的性能。

- 通過利用知識庫中的**可驗證資料**來提供用戶查詢的上下文，減少虛構。

- 它是**成本效益高的**，因為與微調 LLM 相比，它們更經濟。

## 創建知識庫

我們的應用程式基於我們的個人資料，即 AI 初學者課程中的神經網絡課程。

### 向量資料庫

與傳統資料庫不同，向量資料庫是一種專門設計用來儲存、管理和搜尋嵌入向量的資料庫。它儲存文件的數值表示。將資料分解為數值嵌入使得我們的 AI 系統更容易理解和處理資料。

我們將嵌入儲存在向量資料庫中，因為 LLMs 對接受作為輸入的標記數有限制。由於無法將整個嵌入傳遞給 LLM，我們需要將它們分解為塊，當用戶提出問題時，最像問題的嵌入將與提示一起返回。分塊還可以降低通過 LLM 傳遞的標記數量的成本。

一些流行的向量資料庫包括 Azure Cosmos DB、Clarifyai、Pinecone、Chromadb、ScaNN、Qdrant 和 DeepLake。您可以使用以下命令通過 Azure CLI 創建 Azure Cosmos DB 模型：

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### 從文本到嵌入

在儲存資料之前，我們需要將其轉換為向量嵌入，然後再儲存到資料庫中。如果您正在處理大型文件或長文本，可以根據您預期的查詢對它們進行分塊。分塊可以在句子級別或段落級別進行。由於分塊從周圍的單詞中推導出意義，您可以為塊添加一些其他上下文，例如，通過添加文件標題或在塊之前或之後包含一些文本。您可以按如下方式分塊資料：

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

一旦分塊，我們就可以使用不同的嵌入模型嵌入我們的文本。您可以使用的一些模型包括：word2vec、OpenAI 的 ada-002、Azure Computer Vision 等。選擇使用的模型將取決於您使用的語言、編碼的內容類型（文本/圖像/音頻）、它可以編碼的輸入大小以及嵌入輸出的長度。

使用 OpenAI 的 `text-embedding-ada-002` 模型嵌入文本的示例是：

## 檢索和向量搜尋

當用戶提出問題時，檢索器使用查詢編碼器將其轉換為向量，然後在我們的文件搜尋索引中搜尋與輸入相關的文件中的相關向量。完成後，它將輸入向量和文件向量轉換為文本並通過 LLM 傳遞。

### 檢索

檢索發生在系統嘗試快速從索引中找到滿足搜尋標準的文件時。檢索器的目標是獲取將用於提供上下文並將 LLM 基礎化於您的資料的文件。

在我們的資料庫中執行搜尋有幾種方法，例如：

- **關鍵字搜尋** - 用於文本搜尋

- **語義搜尋** - 使用單詞的語義意義

- **向量搜尋** - 使用嵌入模型將文件從文本轉換為向量表示。檢索將通過查詢向量表示最接近用戶問題的文件來完成。

- **混合** - 關鍵字和向量搜尋的組合。

檢索的一個挑戰是當資料庫中沒有類似的回應時，系統將返回他們能夠獲得的最佳信息。然而，您可以使用一些策略，例如設置相關性的最大距離或使用結合關鍵字和向量搜尋的混合搜尋。在這堂課中，我們將使用混合搜尋，即向量和關鍵字搜尋的組合。我們將資料儲存到具有包含塊和嵌入的列的資料框中。

### 向量相似性

檢索器將在知識資料庫中搜尋相近的嵌入，最接近的鄰居，因為它們是相似的文本。在用戶提出查詢的情況下，首先進行嵌入，然後與類似的嵌入進行匹配。常用的測量不同向量相似度的方法是餘弦相似度，它基於兩個向量之間的角度。

我們可以使用其他替代方法來測量相似度，例如歐幾里得距離，即向量端點之間的直線，和點積，它測量兩個向量的對應元素的積的總和。

### 搜尋索引

在進行檢索時，我們需要在執行搜尋之前為知識庫構建搜尋索引。索引將儲存我們的嵌入，並能夠快速檢索最相似的塊，即使在大型資料庫中。我們可以使用本地創建索引：

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### 重新排序

一旦您查詢了資料庫，您可能需要從最相關的結果中對結果進行排序。重新排序 LLM 利用機器學習通過從最相關的排序來提高搜尋結果的相關性。使用 Azure AI 搜尋，重新排序會自動為您完成，使用語義重新排序器。使用最近鄰進行重新排序的示例：

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

## 將所有內容結合在一起

最後一步是將我們的 LLM 添加到組合中，以便能夠獲得基於我們資料的回應。我們可以按如下方式實現：

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

## 評估我們的應用程式

### 評估指標

- 提供的回應質量，確保其聽起來自然、流利且像人類

- 資料的基礎性：評估回應是否來自提供的文件

- 相關性：評估回應是否符合並與所問問題相關

- 流利性 - 回應在語法上是否合理

## 使用 RAG（檢索增強生成）和向量資料庫的用例

有許多不同的用例可以通過函數調用來改進您的應用程式，例如：

- 問答：將您的公司資料基礎化到員工可以用來提問的聊天中。

- 推薦系統：您可以創建一個匹配最相似值的系統，例如電影、餐廳等。

- 聊天機器人服務：您可以儲存聊天記錄並根據用戶資料個性化對話。

- 基於向量嵌入的圖像搜尋，對於進行圖像識別和異常檢測非常有用。

## 總結

我們已經涵蓋了 RAG 的基本領域，從將我們的資料添加到應用程式、用戶查詢和輸出。為了簡化 RAG 的創建，您可以使用 Semanti Kernel、Langchain 或 Autogen 等框架。

## 作業

為了繼續學習檢索增強生成 (RAG)，您可以構建：

- 使用您選擇的框架為應用程式構建前端

- 利用框架，無論是 LangChain 還是 Semantic Kernel，並重新創建您的應用程式。

恭喜您完成了這堂課 👏。

## 學習不止於此，繼續您的旅程

完成這堂課後，查看我們的[生成式 AI 學習集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)以繼續提升您的生成式 AI 知識！

**免責聲明**：  
本文件使用AI翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)進行翻譯。我們努力追求準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對使用此翻譯而產生的任何誤解或誤釋不承擔責任。