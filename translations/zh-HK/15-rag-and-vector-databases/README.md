# 檢索增強生成 (RAG) 與向量資料庫

[![檢索增強生成 (RAG) 與向量資料庫](../../../translated_images/zh-HK/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

在搜尋應用課程中，我們簡要學習了如何將自己的資料整合到大型語言模型（LLM）中。在本課程中，我們將進一步探討在 LLM 應用中紮根您的資料的概念、過程的機制及儲存資料的方法，包括向量嵌入與文本兩部分。

> <strong>影片即將推出</strong>

## 介紹

本課程將涵蓋以下內容：

- RAG 的介紹、其是什麼以及為何在人工智能（AI）中使用。

- 理解什麼是向量資料庫及如何為我們的應用程序創建一個。

- 如何將 RAG 實際整合到應用程式中的範例。

## 學習目標

完成本課程後，您將能：

- 解釋 RAG 在資料檢索與處理上的重要性。

- 設置 RAG 應用並將資料紮根到 LLM。

- 有效整合 RAG 與向量資料庫於 LLM 應用中。

## 我們的場景：用自有資料增強 LLM

本課程中，我們希望將自己的筆記加入教育新創中，讓聊天機器人能取得更多關於不同科目的資訊。利用我們的筆記，學習者能更好地學習並理解各種主題，使考試複習更輕鬆。為創建此場景，我們將使用：

- `Azure OpenAI:` 我們用來創建聊天機器人的 LLM

- `針對初學者的人工智能神經網路課程筆記`：作為我們打底的 LLM 資料

- `Azure AI Search` 及 `Azure Cosmos DB:` 用於儲存資料及建立搜尋索引的向量資料庫

使用者將能夠從筆記中建立練習測驗、複習抽認卡並摘要成簡潔的總覽。開始之前，先來看看什麼是 RAG 以及它的運作方式：

## 檢索增強生成 (RAG)

LLM 驅動的聊天機器人處理使用者提示以生成回應。它旨在具有互動性，並能與使用者就廣泛話題進行交流。然而，它的回應內容受限於提供的上下文與其基礎訓練資料。例如，GPT-4 的知識截止於 2021 年 9 月，這表示它不包含此後發生事件的知識。此外，用於訓練 LLM 的資料不包括私人筆記或公司產品手冊等機密資訊。

### RAG（檢索增強生成）的運作方式

![說明 RAG 運作的圖示](../../../translated_images/zh-HK/how-rag-works.f5d0ff63942bd3a6.webp)

假設您想部署一個可以從筆記中製作測驗的聊天機器人，您需要和知識庫連接。這就是 RAG 發揮作用的地方。RAG 的運作流程如下：

- **知識庫：** 在檢索之前，這些文件需先被攝取並預處理，通常是將大型文件拆解成較小片段，轉換成向量嵌入並存入資料庫。

- **使用者查詢：** 使用者提交問題。

- **檢索：** 當使用者發問，嵌入模型會從知識庫中檢索相關資訊，提供可納入提示的更多上下文。

- **增強生成：** LLM 根據檢索到的資料增強回應。這使得產生的回應不僅基於預訓練資料，還包含新增上下文的相關資訊。檢索到的資料用來強化 LLM 的回應，最終 LLM 回答使用者的問題。

![說明 RAG 架構的圖示](../../../translated_images/zh-HK/encoder-decode.f2658c25d0eadee2.webp)

RAG 的架構使用使用兩部分組成的 Transformer：編碼器與解碼器。例如，當使用者提問時，輸入文字會被「編碼」成捕捉字義的向量，這些向量被「解碼」至我們的文件索引，並根據使用者查詢生成新的文字。LLM 使用編碼器-解碼器模型來生成輸出。

根據發表的論文 [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst)，實現 RAG 有兩種方法：

- **_RAG-Sequence_**：使用檢索到的文件預測使用者查詢的最佳答案。

- **RAG-Token**：利用文件逐步生成下一個標記，再檢索它們以回答使用者的問題。

### 為什麼使用 RAG？ 

- **資訊豐富度：** 確保文字回應更新且即時，透過存取內部知識庫提升領域專門任務的表現。

- 減少虛構內容，利用知識庫中的 <strong>可驗證資料</strong> 提供對使用者查詢的上下文。

- 它 <strong>成本效益高</strong>，相比於微調 LLM 更為經濟。

## 創建知識庫

我們的應用程式基於個人資料，即針對初學者的人工智能神經網路課程。

### 向量資料庫

向量資料庫與傳統資料庫不同，它是一種專門設計來儲存、管理及搜尋嵌入向量的資料庫。它儲存文件的數值表示，將資料拆解為數值嵌入讓我們的 AI 系統更易理解和處理數據。

我們將嵌入儲存在向量資料庫中，因為 LLM 對輸入令牌數量有限制。由於無法將完整嵌入傳遞給 LLM，我們需要將其拆分成多個片段，使用者提問時，會返回最相似的嵌入及提示內容。拆分片段也降低了經過 LLM 的令牌數量，節省成本。

常見的向量資料庫包括 Azure Cosmos DB、Clarifyai、Pinecone、Chromadb、ScaNN、Qdrant 和 DeepLake。您可以透過 Azure CLI 用以下指令建立 Azure Cosmos DB 模型：

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### 從文本轉成嵌入向量

儲存資料前，我們需先將其轉為向量嵌入。如果資料是大型文件或長文本，可以根據預期查詢拆分成片段。拆分可以在句子層級或段落層級進行。由於拆分基於上下文語義，您可為片段加上額外上下文，例如文件標題或片段前後的文字。您可用以下方式拆分資料：

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

    # 如果最後一段未達到最小長度，仍然添加它
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

拆分後，可使用不同嵌入模型將文本向量化。常用模型如 word2vec、OpenAI 的 ada-002、Azure 計算機視覺等。選擇模型取決於您所使用的語言、編碼內容類型（文字/圖像/音訊）、輸入大小限制及輸出嵌入長度。

下面是使用 OpenAI `text-embedding-ada-002` 模型生成的嵌入文本範例：
![詞彙 cat 的嵌入向量](../../../translated_images/zh-HK/cat.74cbd7946bc9ca38.webp)

## 檢索與向量搜尋

使用者提問時，檢索器會使用查詢編碼器將提問轉為向量，再在文件搜尋索引中尋找與此向量相近的相關文件向量。找到後，系統將輸入向量與文件向量轉回文字，並傳入 LLM。

### 檢索

檢索是系統迅速從索引中找出符合搜尋條件的文件。檢索器目標為獲取可以提供上下文、讓 LLM 以您資料為基礎作答的文件。

檢索方法多種多樣，包括：

- <strong>關鍵詞搜尋</strong> — 針對文字搜尋

- <strong>向量搜尋</strong> — 利用嵌入模型將文件從文字轉成向量，讓系統可進行基於單詞意義的 <strong>語意搜尋</strong>。透過查詢向量找出向量空間中最接近使用者問題的文件。

- <strong>混合搜尋</strong> — 結合關鍵詞與向量搜尋。

檢索的挑戰在於若資料庫中無相似回答，系統會回傳最佳資訊。您可以採取設置最大相關距離或使用結合關鍵字與向量搜尋的混合搜尋策略。本課程將使用混合搜尋，我們會將資料存入包含片段及嵌入的資料框架。

### 向量相似度

檢索器會搜尋知識庫中彼此接近的嵌入，也就是最近鄰，因為這些文本相似。在使用者發問的情境中，問題先被編碼為嵌入，然後匹配類似的嵌入。常用衡量向量間相似度的方法是餘弦相似度，基於兩個向量間的角度。

其他測量相似度的方式還有歐氏距離（向量端點間直線距離）以及內積（兩向量對應元素乘積總和）。

### 搜索索引

進行檢索前需為知識庫建立搜索索引。索引會儲存嵌入，讓系統即使面對大型資料庫也能快速取出最相似片段。我們可以本地建立索引，指令如下：

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# 建立搜尋索引
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# 查詢索引時，可以使用kneighbors方法
distances, indices = nbrs.kneighbors(embeddings)
```

### 再排序

查詢資料庫後，您可能需將結果按相關性排序。再排序 LLM 利用機器學習提升搜尋結果的相關度，將結果從高到低排序。使用 Azure AI Search 時，再排序功能由語義再排序器自動完成。以下為鄰近鄰居再排序範例：

```python
# 尋找最相似的文件
distances, indices = nbrs.kneighbors([query_vector])

index = []
# 列印最相似的文件
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## 整合全流程

最後一步是將 LLM 加入，讓回應能以我們的資料為基礎。實作如下：

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

    # 結合歷史和用戶輸入
    history.append(user_input)

    # 建立訊息對象
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # 使用 Responses API 生成回應
    response = client.responses.create(
        model="gpt-4o-mini",
        temperature=0.7,
        max_output_tokens=800,
        input=messages,
        store=False,
    )

    return response.output_text

chatbot(user_input)
```

## 評估我們的應用程式

### 評估指標

- 回應品質：確保回覆自然、流暢且像人類。

- 資料根據性：評估是否回應來自提供的文件。

- 相關性：評估回應與提問是否匹配且相關。

- 流暢度：檢視回應在語法上是否合理。

## 使用 RAG（檢索增強生成）與向量資料庫的應用場景

有許多不同的應用場景中，功能調用能提升您的應用程式，例如：

- 問答系統：將公司資料紮根到聊天機器人，員工可用來詢問問題。

- 推薦系統：建立系統匹配最相似的項目，例如電影、餐廳等。

- 聊天機器人服務：儲存聊天歷史並根據使用者資料個性化對話。

- 基於向量嵌入的圖片搜尋，適用於圖像識別及異常檢測。

## 摘要

我們已涵蓋從將資料加入應用、使用者查詢到回應的 RAG 基本領域。為簡化 RAG 創建，您可以使用 Semanti Kernel、Langchain 或 Autogen 等框架。

## 作業

繼續您的檢索增強生成 (RAG) 學習，可以嘗試：

- 使用您選擇的框架構建應用前端

- 利用 LangChain 或 Semantic Kernel 框架，重新創建您的應用程式。

恭喜您完成本課程 👏。

## 學習不止於此，繼續您的旅程

完成本課程後，請查看我們的 [生成式人工智能學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升您的生成式人工智能知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->