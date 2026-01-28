<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2210a0466c812d9defc4df2d9a709ff9",
  "translation_date": "2026-01-18T17:15:03+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "tw"
}
-->
# 檢索增強生成 (RAG) 與向量資料庫

[![檢索增強生成 (RAG) 與向量資料庫](../../../../../translated_images/tw/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

在搜尋應用課程中，我們曾簡要了解了如何將自己的資料整合進大型語言模型 (LLM) 中。在本課程中，我們將更深入探討如何在 LLM 應用中將資料接地的概念、該過程的機制以及儲存資料的方法，涵蓋了嵌入向量與文本兩方面。

> **影片即將推出**

## 介紹

本課程將涵蓋以下內容：

- 介紹 RAG 是什麼以及為何在人工智慧 (AI) 中使用它。

- 了解向量資料庫為何物及建立應用所需的向量資料庫。

- 一個將 RAG 整合至應用中的實作範例。

## 學習目標

完成本課程後，您將能：

- 說明 RAG 在資料檢索與處理中的重要性。

- 設定 RAG 應用並將您的資料接地於 LLM。

- 在 LLM 應用中有效整合 RAG 與向量資料庫。

## 我們的情境：用自己的資料強化 LLM

在本課程中，我們想將自己的筆記加入教育新創中，讓聊天機器人能取得不同主題的更多資訊。藉由擁有的筆記，學習者能更好地學習並理解不同主題，方便考試複習。為此，我們將使用：

- `Azure OpenAI:` 我們用來建立聊天機器人的 LLM

- `AI 初學者神經網路課程內容:`作為我們接地 LLM 的資料

- `Azure AI Search` 與 `Azure Cosmos DB:` 用以存儲資料的向量資料庫並建立搜尋索引

使用者能從筆記建立練習測驗及複習用抽認卡，並且生成精簡摘要。開始之前，先來看看 RAG 是什麼，以及它如何運作：

## 檢索增強生成 (RAG)

LLM 驅動的聊天機器人會處理使用者的提示以生成回應，設計上可與使用者就廣泛主題互動。然而，它所能回答的範圍限於提供的上下文及基本訓練資料。例如，GPT-4 的知識截止於 2021 年 9 月，意即其不具備該時間點之後事件的相關知識。而且，訓練 LLM 所用的資料不包括私人筆記或公司產品手冊等機密資訊。

### RAG（檢索增強生成）如何運作

![繪圖說明 RAG 運作原理](../../../../../translated_images/tw/how-rag-works.f5d0ff63942bd3a6.webp)

假設您想部署一個能從筆記中創建測驗的聊天機器人，您需要連結到知識庫，而這正是 RAG 派上用場的地方。RAG 運作流程如下：

- **知識庫：** 在檢索之前，需要進行文件的攝取與預處理，通常將大型文件拆解成較小的區塊，轉換為文字嵌入向量並儲存在資料庫中。

- **使用者查詢：** 使用者提出問題。

- **檢索：** 使用者提問時，嵌入模型會從知識庫中檢索相關資訊，提供更多上下文以納入提示中。

- **增強生成：** LLM 根據檢索到的資料增強回答，使回應不僅基於預先訓練的資料，還包含加強上下文的相關資訊。檢索到的資料用來增強 LLM 回答，LLM 最後返回使用者問題的答案。

![RAG 架構圖示](../../../../../translated_images/tw/encoder-decode.f2658c25d0eadee2.webp)

RAG 架構以 transformer 實現，包含兩個部分：編碼器與解碼器。例如使用者提問時，輸入文本會被「編碼」成捕捉詞義的向量，這些向量「解碼」到我們的文件索引，並根據使用者查詢產生新的文本。LLM 同時使用編碼器-解碼器模型來生成輸出。

根據論文 [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst)，實作 RAG 有兩種方式：

- **_RAG-Sequence_** 使用檢索文件來預測對使用者問題最好的回答。

- **RAG-Token** 使用文件來生成下一個詞元，然後檢索這些詞元來回答使用者的問題。

### 為何要使用 RAG？ 

- **資訊豐富性：** 確保回答是最新且即時的，因此透過存取內部知識庫，提升在特定領域任務的表現。

- 利用知識庫中的**可驗證資料**提供上下文，降低虛構回答的情況。

- 成本效益高，相較於微調 LLM 更為經濟。

## 建立知識庫

我們的應用基於個人資料，即 AI 初學者神經網路課程內容。

### 向量資料庫

向量資料庫與傳統資料庫不同，它是專門設計用來儲存、管理及搜尋嵌入向量的資料庫。它儲存的是文件的數值向量表示。將資料拆解成數值嵌入向量，讓 AI 系統更易於理解及處理資料。

我們將嵌入向量存入向量資料庫，因為 LLM 對輸入的字元數有限制。您無法把所有嵌入向量直接餵入 LLM，必須將它們拆分成區塊，在使用者提問時，只返回與問題最相關的嵌入向量及提示。區塊拆分也可降低使用 LLM 產生的 token 數量及成本。

常見向量資料庫包含 Azure Cosmos DB、Clarifyai、Pinecone、Chromadb、ScaNN、Qdrant 與 DeepLake。您可以使用 Azure CLI 以以下指令建立 Azure Cosmos DB 模型：

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```


### 由文字至嵌入向量

在儲存資料前，需先將文本轉換成向量嵌入再存入資料庫。處理長文件或長文本時，可依預期查詢需求將文本切塊。區塊可為句子層級或段落層級。由於語義來自周圍詞彙，您也可為區塊加上額外上下文，例如加入文件標題，後面或前面加些文字。切塊可如下操作：

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

    # 如果最後一塊未達到最小長度，仍然添加它
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```


切塊完成後，我們使用不同的嵌入模型將文本轉換為向量。一些可用模型包括：word2vec、OpenAI 的 ada-002、Azure 計算視覺等。選擇模型取決於您使用的語言、編碼內容類型（文字、圖片、音訊）、可編碼輸入大小及向量輸出長度。

以下是使用 OpenAI 的 `text-embedding-ada-002` 模型將文字嵌入的範例：

![cat 一詞的嵌入示意圖](../../../../../translated_images/tw/cat.74cbd7946bc9ca38.webp)

## 檢索與向量搜尋

當使用者提問時，檢索器會利用查詢編碼器將查詢轉成向量，然後在文件搜尋索引中尋找與輸入相關的向量。一旦搜尋完成，它將輸入向量與文件向量轉回文字，並傳入 LLM。

### 檢索

檢索是在資料庫索引中快速尋找符合搜尋條件的文件。檢索器的目標是獲取能提供上下文，將 LLM 接地於您的資料的文件。

在資料庫中搜索有多種方式：

- **關鍵字搜尋** — 用於文字搜尋。

- **向量搜尋** — 利用嵌入模型將文件由文字轉成向量表示，實現基於詞義的**語意搜尋**。檢索會挑選與使用者問題向量表示最接近的文件。

- **混合搜尋** — 結合關鍵字與向量搜尋。

檢索面臨的挑戰是當資料庫中沒有與查詢相似的內容時，系統只會回傳最佳資訊，但您可以透過設置最大相關距離或使用結合關鍵字與向量的混合搜尋來改善。本課程將使用混合搜尋，並將資料存入包含區塊及嵌入向量的資料框架。

### 向量相似度

檢索器會尋找知識庫中相近的嵌入向量，也就是最接近的鄰居，因為它們是相似文本。在使用者提問情境中，問題會先被嵌入，然後與類似的嵌入向量配對。普遍用來衡量向量相似度的方法是餘弦相似度（基於兩向量間的角度）。

另一種相似度的衡量方式有歐氏距離（向量端點間的直線距離）以及點積（兩向量對應元素乘積總和）。

### 搜尋索引

執行檢索前，我們需先建立知識庫的搜尋索引。索引會存放嵌入向量，即使資料庫龐大也能快速找出最相近區塊。我們可以用以下程式碼在本機建立索引：

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# 建立搜尋索引
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# 要查詢索引，您可以使用 kneighbors 方法
distances, indices = nbrs.kneighbors(embeddings)
```


### 重新排序

查詢資料庫後，您可能需要將結果按照相關度排序。重新排序的 LLM 會利用機器學習將搜尋結果由高到低排列，以提高相關性。使用 Azure AI Search，重新排序會由語意重新排序器自動完成。以下是以最近鄰重新排序的示意：

```python
# 找出最相似的文件
distances, indices = nbrs.kneighbors([query_vector])

index = []
# 列印出最相似的文件
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```


## 將所有元素整合

最後一步是將 LLM 加入流程，使回應能基於我們的資料。可透過以下方式實作：

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # 將問題轉換為查詢向量
    query_vector = create_embeddings(user_input)

    # 尋找最相似的文件
    distances, indices = nbrs.kneighbors([query_vector])

    # 將文件加入查詢以提供上下文
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # 結合歷史紀錄與用戶輸入
    history.append(user_input)

    # 建立訊息物件
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # 使用聊天補全來生成回應
    response = openai.chat.completions.create(
        model="gpt-4",
        temperature=0.7,
        max_tokens=800,
        messages=messages
    )

    return response.choices[0].message

chatbot(user_input)
```


## 評估應用

### 評估指標

- 回答品質：確保回答自然、流暢且類似人類表達

- 資料接地性：評估回答是否來自提供的文件

- 相關性：評估回答是否符合且與提問相關

- 流暢度：回應語法是否合理

## RAG 與向量資料庫的應用情境

在多種情境下，函式調用能提升您的應用：

- 問答系統：將公司資料接地到聊天機器人，讓員工問問題。

- 推薦系統：建立系統配對最相似的值，如電影、餐館等。

- 聊天機器人服務：儲存聊天記錄並根據使用者資料個性化對話。

- 基於向量嵌入的圖片搜尋，適用於圖像識別與異常檢測。

## 總結

我們涵蓋了 RAG 的基本領域，包含如何將資料加入應用、使用者查詢與輸出。為簡化 RAG 建置，您可使用如 Semantic Kernel、LangChain 或 Autogen 等框架。

## 作業

為持續學習檢索增強生成 (RAG)，您可以嘗試：

- 使用您喜歡的框架構建前端應用

- 利用 LangChain 或 Semantic Kernel 等框架，重建您的應用

恭喜您完成本課程 👏。

## 學習永不止步，繼續邁向新里程碑

完成本課程後，請瀏覽我們的 [生成式 AI 學習收藏](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ，持續提升您的生成式 AI 知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯。本公司雖盡力確保翻譯準確性，但自動翻譯可能包含錯誤或不準確之處。原始語言文件應視為權威版本。對於重要資訊，建議使用專業人工翻譯。本公司不對因使用本翻譯造成的任何誤解或曲解負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->