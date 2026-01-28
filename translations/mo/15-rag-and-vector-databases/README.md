<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2210a0466c812d9defc4df2d9a709ff9",
  "translation_date": "2026-01-18T17:08:50+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "mo"
}
-->
# 檢索增強生成（RAG）與向量資料庫

[![檢索增強生成（RAG）與向量資料庫](../../../../../translated_images/mo/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

在搜尋應用課程中，我們簡要學習了如何將自己的資料整合到大型語言模型（LLMs）中。在本課程中，我們將進一步探討在LLM應用中基於資料的概念、流程機制及儲存資料的方法，包括內嵌向量和文字。

> **影片即將推出**

## 介紹

本課程我們將涵蓋以下內容：

- 介紹RAG，是什麼，及為何在人工智能（AI）中使用。

- 瞭解向量資料庫是什麼並為我們的應用創建一個。

- 介紹如何在應用中實際整合RAG的範例。

## 學習目標

完成本課程後，您將能夠：

- 解釋RAG在資料檢索和處理中的重要性。

- 設定RAG應用並將資料基礎於LLM。

- 在LLM應用中有效整合RAG與向量資料庫。

## 我們的場景：用我們自己的資料增強LLM

在本課程中，我們希望將自己的筆記加入教育新創，讓聊天機器人能夠獲取更多關於不同科目的資訊。利用這些筆記，學習者能更好地研讀並理解不同主題，使複習考試更容易。為了建立此場景，我們將使用：

- `Azure OpenAI：` 我們用來建立聊天機器人的LLM

- `AI初學者神經網絡課程：` 用於為LLM提供資料基礎

- `Azure AI Search` 和 `Azure Cosmos DB：` 向量資料庫用於儲存資料並建立搜尋索引

用戶將能依照筆記創建練習測驗、複習抽認卡並總結成簡明概述。開始前，讓我們先了解什麼是RAG及其運作方式：

## 檢索增強生成（RAG）

由LLM驅動的聊天機器人處理用戶提示來產生回應。它被設計為互動式，能與用戶討論各種主題。然而，其回應僅限於所提供的上下文和基礎訓練資料。例如，GPT-4的知識截止點為2021年9月，表示它不了解此後發生的事件。此外，用於訓練LLM的資料不包含機密資訊，例如個人筆記或公司的產品手冊。

### RAG（檢索增強生成）的運作方式

![說明RAG如何工作的圖](../../../../../translated_images/mo/how-rag-works.f5d0ff63942bd3a6.webp)

假設你想部署一個根據筆記建立測驗的聊天機器人，你將需要連接知識庫。這時候RAG就派上用場。RAG的運作流程如下：

- **知識庫：** 在檢索之前，這些文件需被收錄並預處理，通常是將大型文件拆分成較小區塊、轉換成文字內嵌向量並存入資料庫。

- **使用者查詢：** 用戶提出問題。

- **檢索：** 當用戶提出問題時，內嵌模型從知識庫中檢索相關資訊，以提供更多上下文給提示呈現。

- **增強生成：** LLM基於檢索到的資料強化其回答，讓產生的回應不僅基於預訓練資料，也結合相關的新增上下文。獲得的資料用於增強LLM回應，LLM接著回覆用戶問題。

![說明RAG架構的圖](../../../../../translated_images/mo/encoder-decode.f2658c25d0eadee2.webp)

RAG的架構透過Transformers實現，包含兩部分：編碼器與解碼器。例如，當用戶提出問題時，輸入文字會被「編碼」成捕捉字詞意義的向量，向量再被「解碼」配對文檔索引並根據使用者查詢產生新文字。LLM使用編碼器－解碼器模型來生成輸出。

根據所提出的論文：[Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) 實作RAG有兩個方法：

- **_RAG-Sequence_** 使用檢索到的文件來預測用戶查詢的最佳答案。

- **RAG-Token** 使用文件產生下一個字元，再檢索文件回覆用戶問題。

### 為什麼要使用RAG？ 

- **資訊豐富性：** 確保文字回應最新、即時。因此透過訪問內部知識庫，提升特定領域任務的效能。

- 利用知識庫中的**可驗證資料**提供上下文，減少虛構（幻想）資訊生成。

- 成本效益**優良**，相較於微調LLM更經濟。

## 創建知識庫

我們的應用基於個人資料，即AI初學者神經網絡課程。

### 向量資料庫

相較於傳統資料庫，向量資料庫是一種專門設計來儲存、管理和搜尋內嵌向量的資料庫。它儲存文件的數值向量表示。將資料拆解為數值嵌入，使AI系統更能理解並處理資料。

由於LLM輸入的tokens數量有限，我們將內嵌向量存放於向量資料庫中。您無法將整個內嵌向量直接傳入LLM，因此需要將其拆分成多個區塊，當用戶提出問題時，會回傳最相似問題的嵌入和提示。區塊化也可降低通過LLM的token成本。

一些熱門向量資料庫包括Azure Cosmos DB、Clarifyai、Pinecone、Chromadb、ScaNN、Qdrant和DeepLake。您可以使用Azure CLI創建Azure Cosmos DB模型，指令如下：

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### 從文字到內嵌向量

在儲存資料前，我們需要先將其轉換成向量內嵌再存入資料庫。若處理大型文件或長文字時，可以依預期查詢將資料分塊。分塊可在句子或段落層級進行。因為分塊意義來自周圍字詞，你可加入其他上下文，例如文件標題或分塊前後的文字。資料分塊可如下：

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

    # 如果最後一塊未達最低長度，仍然添加它
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

分塊完成後，我們可以用不同嵌入模型將文字內嵌。可以使用的模型包括：word2vec、OpenAI的ada-002、Azure Computer Vision等。選擇模型會根據你使用的語言、內容型態（文字/圖片/音訊）、可編碼大小和輸出向量長度決定。

以下是一個利用OpenAI的`text-embedding-ada-002`模型的文字內嵌範例：
![cat這個字的內嵌向量圖](../../../../../translated_images/mo/cat.74cbd7946bc9ca38.webp)

## 檢索與向量搜尋

當用戶提出問題時，檢索器會用查詢編碼器把問題轉成向量，接著在我們的文件搜尋索引中搜尋相關向量。搜尋完成後，將輸入向量和文件向量轉成文字並通過LLM處理。

### 檢索

檢索是系統快速尋找符合搜尋條件的文件。檢索器的目標是取得可用來提供上下文、基於你的資料為LLM提供基礎的文件。

有幾種搜尋資料庫方法，例如：

- **關鍵字搜尋**－用於文字搜尋

- **向量搜尋**－用內嵌模型將文件轉成向量表示，允許透過詞義進行**語意搜尋**。檢索會尋找向量表示最接近用戶問題的文件。

- **混合搜尋**－結合關鍵字和向量搜尋。

檢索挑戰在於若資料庫無相似回答，系統則會回傳盡可能最佳資訊。不過可使用設置最大距離相關性或混合搜尋等策略。本課程採用混合搜尋，結合向量與關鍵字搜尋。我們將資料存入包含分塊及內嵌向量的資料框（dataframe）。

### 向量相似度

檢索器會搜尋知識庫中彼此相近的向量，即最近鄰，因為它們代表的文字相似。用戶提出問題後首先內嵌，再比對相似內嵌向量。常用相似度測量是基於兩向量夾角的餘弦相似度。

其他可用相似度測量還包括歐式距離（向量端點之間的直線距離）與內積（兩向量相對應元素乘積之和）。

### 搜尋索引

執行檢索前，我們需為知識庫建立搜尋索引。索引可儲存內嵌向量，在庞大資料庫中快速找出最相似區塊。可於本地建立索引，指令如下：

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# 建立搜尋索引
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# 要查詢索引，您可以使用 kneighbors 方法
distances, indices = nbrs.kneighbors(embeddings)
```

### 再排序

查詢過資料庫後，可能需要將結果排序，按相關性由高到低。再排序的LLM利用機器學習提升搜尋結果的相關性排序。使用Azure AI Search時，再排序會透過語意再排序器自動完成。以下為鄰近點再排名作法範例：

```python
# 搵出最相似嘅文件
distances, indices = nbrs.kneighbors([query_vector])

index = []
# 印出最相似嘅文件
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## 整合所有元素

最後是將LLM整合進來，獲得基於我們資料的回應。我們可以以下方式實現：

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # 將問題轉換成查詢向量
    query_vector = create_embeddings(user_input)

    # 尋找最相似的文檔
    distances, indices = nbrs.kneighbors([query_vector])

    # 將文檔添加到查詢中以提供上下文
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # 結合歷史和用戶輸入
    history.append(user_input)

    # 創建一個訊息物件
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # 使用聊天完成來生成回應
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

- 回應品質：確保口語自然、流暢且接近人類說話。

- 資料基礎的紮實度：評估回應是否來自所提供文件。

- 相關性：評估回應是否匹配且與問題相關。

- 流暢度：回應語法是否通順合理。

## RAG（檢索增強生成）與向量資料庫的使用案例

多種情況下，功能調用可提升你的應用，例如：

- 問答系統：將公司資料基於聊天機器人，讓員工能提問。

- 推薦系統：建立系統配對最相似項目，如電影、餐廳等。

- 聊天機器人服務：儲存聊天紀錄，並根據使用者資料個人化對話。

- 基於向量嵌入的圖片搜尋，適用於影像辨識與異常檢測。

## 總結

我們涵蓋了RAG的基礎範疇，從為應用加入資料、使用者查詢到輸出。為簡化RAG創建，你可以使用Semanti Kernel、Langchain或Autogen這類框架。

## 作業

繼續學習檢索增強生成（RAG）可以：

- 使用你選擇的框架建立應用的前端。

- 利用LangChain或Semantic Kernel框架，重建你的應用。

恭喜完成本課程 👏。

## 學習不止於此，繼續前進

完成本課程後，請參考我們的[生成式AI學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升你的生成式AI知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件係使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。雖然我哋致力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。文件原本之母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我哋對因使用本翻譯而引起之任何誤解或錯誤詮釋概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->