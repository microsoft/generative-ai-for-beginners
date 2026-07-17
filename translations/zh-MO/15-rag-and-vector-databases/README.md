# 檢索增強生成 (RAG) 與向量數據庫

[![檢索增強生成 (RAG) 與向量數據庫](../../../translated_images/zh-MO/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

在搜尋應用課程中，我們簡要了解了如何將自己的數據整合到大型語言模型（LLMs）中。本課程中，我們將進一步探討在您的 LLM 應用中紮根您的數據的概念、流程機制以及數據存儲的方法，包括嵌入向量和文本。

> <strong>視頻即將推出</strong>

## 簡介

本課程將涵蓋以下內容：

- 介紹 RAG 是什麼以及為何在人工智能 (AI) 中使用它。

- 了解什麼是向量數據庫並為我們的應用創建一個。

- 示範如何實際將 RAG 集成到應用中。

## 學習目標

完成本課程後，您將能夠：

- 解釋 RAG 在數據檢索和處理中的重要性。

- 設定 RAG 應用並將您的數據紮根於 LLM 中。

- 有效地在 LLM 應用中整合 RAG 和向量數據庫。

## 我們的情景：用我們的數據增強 LLM

在本課程中，我們想將自己的筆記加入教育新創中，使聊天機器人能夠獲得更多關於不同科目的資訊。利用我們的筆記，學習者將能更好地學習和理解各種主題，令考試複習更輕鬆。為建立本情景，我們將使用：

- `Azure OpenAI:` 我們用來創建聊天機器人的 LLM

- `AI for beginners' lesson on Neural Networks`：將用作紮根我們 LLM 的數據

- `Azure AI Search` 和 `Azure Cosmos DB:` 向量數據庫用來存儲數據及創建搜尋索引

使用者將能夠從他們的筆記中創建練習測驗、複習閃卡並匯總成簡明概要。開始之前，讓我們了解什麼是 RAG 及其運作方式：

## 檢索增強生成 (RAG)

由 LLM 驅動的聊天機器人處理用戶提示以生成回應。其設計為具有互動性，能夠與用戶就廣泛議題進行交流。然而，其回答限於提供的上下文和其基礎訓練數據。例如，GPT-4 的知識截止日期是 2021 年 9 月，也就是說，它不包含此後發生事件的知識。此外，用於訓練 LLM 的數據不包括保密信息如個人筆記或公司產品手冊。

### RAG（檢索增強生成）如何運作

![展示 RAG 如何運作的圖示](../../../translated_images/zh-MO/how-rag-works.f5d0ff63942bd3a6.webp)

假設您想部署一個能根據筆記創建測驗的聊天機器人，則需連接到知識庫。這就是 RAG 發揮作用的地方。RAG 運作流程如下：

- **知識庫：** 在檢索前，這些文檔需要被導入並預處理，通常是將大型文檔拆分為更小的塊，轉換為文本嵌入後存入數據庫。

- **用戶查詢：** 用戶提出問題。

- **檢索：** 當用戶提問時，嵌入模型從知識庫中檢索相關信息，以提供更多上下文，該上下文將被整合入提示中。

- **增強生成：** LLM 基於檢索到的數據增強回應，讓生成的回答不僅基於預訓練數據，還依據補充的上下文資料。檢索到的資料用於強化 LLM 回應，之後 LLM 回答用戶問題。

![展示 RAG 架構的圖示](../../../translated_images/zh-MO/encoder-decode.f2658c25d0eadee2.webp)

RAG 的架構利用變壓器實現，包含兩部分：編碼器和解碼器。例如，當用戶提問時，輸入文字會被「編碼」成捕捉詞義的向量，這些向量再「解碼」成文檔索引，並根據用戶查詢生成新文本。LLM 透過編碼器-解碼器模型共同生成輸出。

實施 RAG 有兩種方法，根據論文 [檢索增強生成用於知識密集型自然語言處理任務](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst)：

- **_RAG-Sequence_**：使用檢索到的文件預測用戶查詢的最佳答案。

- **RAG-Token**：使用文件生成下一個標記，然後再檢索回答用戶查詢。

### 為何使用 RAG？

- **資訊豐富度：** 確保文本回答最新且具時效，從而通過訪問內部知識庫提升特定領域任務的表現。

- 透過利用知識庫中的<strong>可驗證數據</strong>提供上下文，減少虛構內容。

- **成本效益：** 相較於微調 LLM，更經濟實惠。

## 創建知識庫

我們的應用基於我們的個人數據，即 AI For Beginners 課程中的神經網絡課程。

### 向量數據庫

向量數據庫不同於傳統數據庫，是專門設計用來存儲、管理和搜索嵌入向量的數據庫。它存儲文檔的數值表示。將數據拆分為數字嵌入，方便 AI 系統理解和處理資訊。

我們將嵌入向量存於向量數據庫中，因為 LLM 對接受的輸入詞元數有限制。由於無法將整個嵌入向量直接傳入 LLM，我們需將其拆分成塊，當用戶提問時，最相關的嵌入向量會連同提示一同返回。分塊還能減少通過 LLM 處理的詞元數，節省成本。

一些流行的向量數據庫包括 Azure Cosmos DB、Clarifyai、Pinecone、Chromadb、ScaNN、Qdrant 和 DeepLake。您可以使用 Azure CLI 執行以下命令來建立 Azure Cosmos DB 模型：

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### 從文本到嵌入向量

在存儲數據前，我們需要將其轉換為向量嵌入。若處理大型文檔或長文本，您可以根據預期查詢進行分塊。分塊可在句子或段落層面進行。由於分塊基於周圍詞彙推導含義，您還可以給塊添加其他上下文，例如加入文檔標題或在塊前後添加一些文字。分塊方式如下：

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

    # 如果最後一個區塊未達到最小長度，仍然添加它
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

分塊後，我們可以使用不同的嵌入模型對文本進行嵌入。一些可用的模型包括 word2vec、OpenAI 的 ada-002、Azure Computer Vision 等。模型選擇取決於所用語言、編碼內容類型（文本/圖像/音頻）、可編碼的輸入大小及嵌入輸出的長度。

使用 OpenAI 的 `text-embedding-ada-002` 模型嵌入文本的示例：
![單詞 cat 的嵌入向量](../../../translated_images/zh-MO/cat.74cbd7946bc9ca38.webp)

## 檢索和向量搜索

當用戶提問時，檢索器使用查詢編碼器將問題轉成向量，然後在文檔搜尋索引中搜尋與輸入相關的向量。一旦找到，它會將輸入和文檔向量轉回文本，並傳入 LLM。

### 檢索

檢索過程指系統快速尋找符合搜尋條件的文檔。檢索器的目標是取得用來提供上下文，並將 LLM 紮根於您的數據的文檔。

在我們的數據庫中執行搜尋有多種方式，如：

- <strong>關鍵字搜尋</strong> - 用於文本搜尋

- <strong>向量搜尋</strong> - 將文檔從文本轉為向量表示，利用嵌入模型進行<strong>語意搜尋</strong>，基於詞義進行檢索。檢索會找出向量表示最接近用戶問題的文檔。

- <strong>混合搜尋</strong> - 結合關鍵字搜尋與向量搜尋。

如果數據庫中沒有與查詢相似的回答，系統會返回最相符的信息。您可使用設置最大相關距離或混合搜尋策略來改進結果。本課程將使用混合搜尋，將資料存入包含塊及其嵌入向量的資料框中。

### 向量相似度

檢索器會在知識庫中搜尋彼此相近的嵌入向量，即最近鄰，因為這些文本相似。在用戶提問場景中，查詢被嵌入後，與相似嵌入匹配。常用量度向量相似度方法是餘弦相似度，基於兩向量間角度。

其他可用的相似度量包括歐氏距離（向量端點間直線距離）及點積（兩向量對應元素乘積和）。

### 搜索索引

執行檢索前，我們需為知識庫建立搜索索引。索引存儲嵌入向量，能快速檢索出最相似的塊，即使數據庫龐大。我們可以使用以下命令本地創建索引：

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# 建立搜尋索引
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# 如要查詢索引，可以使用 kneighbors 方法
distances, indices = nbrs.kneighbors(embeddings)
```

### 重新排序

查詢數據庫後，您可能需要將結果按相關性排序。重新排序的 LLM 利用機器學習提升搜尋結果相關性，將最相關的排在前面。使用 Azure AI Search，重新排序由語意重新排序器自動完成。以下為基於最近鄰的重新排序示例：

```python
# 搵最相似嘅文件
distances, indices = nbrs.kneighbors([query_vector])

index = []
# 輸出最相似嘅文件
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## 綜合實踐

最後一步是結合 LLM，以便獲得紮根於我們數據的回應。實現方式如下：

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # 將問題轉換為查詢向量
    query_vector = create_embeddings(user_input)

    # 找出最相似的文件
    distances, indices = nbrs.kneighbors([query_vector])

    # 將文件加入查詢以提供上下文
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # 結合歷史記錄和用戶輸入
    history.append(user_input)

    # 建立訊息物件
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # 使用回應 API 產生回應
    response = client.responses.create(
        model="gpt-5-mini",
        max_output_tokens=800,
        input=messages,
        store=False,
    )

    return response.output_text

chatbot(user_input)
```

## 評估我們的應用

### 評估指標

- 回應品質：確保聽起來自然、流暢且像人類。

- 紮根度：評估回答是否來自所提供的文檔。

- 相關性：評估回答是否符合並與問題相關。

- 流暢性：評估語法是否通順合理。

## 使用 RAG (檢索增強生成) 和向量數據庫的應用場景

以下是多種可透過功能呼叫改善您應用的情境：

- 問題與回答：將公司數據紮根於聊天系統，供員工提問。

- 推薦系統：創建匹配最高相似度的系統，例如電影、餐廳等。

- 聊天機器人服務：存儲聊天記錄，基於用戶數據個性化對話。

- 基於向量嵌入的圖像搜尋，用於圖像識別和異常檢測。

## 總結

我們涵蓋了 RAG 的核心領域，從將數據加入應用、用戶查詢到輸出。為簡化 RAG 創建，您可使用 Semanti Kernel、Langchain 或 Autogen 等框架。

## 任務

繼續學習檢索增強生成 (RAG)，您可以：

- 使用您選擇的框架構建應用前端

- 利用 LangChain 或 Semantic Kernel 框架重新創建您的應用。

恭喜您完成本課程 👏。

## 學習不止於此，繼續前行

完成本課程後，請查看我們的 [生成式 AI 學習集錦](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升您的生成式 AI 知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->