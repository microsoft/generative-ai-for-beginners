# 檢索增強生成（RAG）與向量資料庫

[![檢索增強生成（RAG）與向量資料庫](../../../translated_images/zh-TW/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

在搜尋應用課程中，我們簡要學習了如何將自己的資料整合到大型語言模型（LLMs）中。本課程將更深入探討在LLM應用中為您的資料建立基礎的概念、過程原理及資料儲存方法，包括向量嵌入與文本兩者。

> <strong>影片即將推出</strong>

## 簡介

本課程將涵蓋以下內容：

- RAG的介紹，什麼是RAG以及為何在人工智慧（AI）中使用。

- 了解什麼是向量資料庫並為我們的應用程式建立一個。

- 實作示範如何將RAG整合進應用程式。

## 學習目標

完成本課程後，您將能夠：

- 說明RAG在資料檢索與處理中的重要性。

- 設置RAG應用並將您的資料基於LLM。

- 有效地在LLM應用中整合RAG與向量資料庫。

## 我們的場景：用我們自己的資料強化LLM

本課程中，我們想將自己的筆記加入教育新創中，讓聊天機器人能取得更多不同主題的資訊。透過我們的筆記，學習者將能更有效學習並理解不同主題，輔助考試複習。為建立此場景，我們將使用：

- `Azure OpenAI:` 作為建立聊天機器人的LLM

- `AI for beginners' lesson on Neural Networks`: 作為我們基於基礎的資料

- `Azure AI Search` 及 `Azure Cosmos DB:` 向量資料庫用來儲存資料並建立搜尋索引

使用者能根據筆記建立練習測驗、複習快閃卡並將其摘要成簡明的概覽。首先，讓我們來了解什麼是RAG以及它如何運作：

## 檢索增強生成（RAG）

LLM驅動的聊天機器人處理使用者提示來生成回答。它設計為互動式，能夠針對廣泛主題與使用者對話。然而，它的回應僅限於所提供的上下文及其訓練資料。例如，GPT-4的知識截止於2021年9月，表示它無法了解此日期之後發生的事件。此外，訓練LLM的資料不包含機密資訊，如個人筆記或公司的產品手冊。

### RAG（檢索增強生成）的運作方式

![顯示RAG如何運作的圖示](../../../translated_images/zh-TW/how-rag-works.f5d0ff63942bd3a6.webp)

假設您想部署一個能從您的筆記中建立測驗的聊天機器人，您將需要連結知識庫。此時，RAG便能派上用場。RAG的運作如下：

- **知識庫：** 在檢索前，這些文件需被接收與預處理，通常是將大文件拆成較小片段，轉換為文本向量嵌入並存入資料庫。

- **使用者查詢：** 使用者提出問題。

- **檢索：** 當使用者詢問時，嵌入模型從知識庫中擷取相關資訊以提供更多上下文，並將其併入提示中。

- **增強生成：** LLM根據檢索到的資料提升回應。生成的回答不僅基於預訓練資料，也根據新增的上下文相關資訊。檢索到的資料用於增強LLM的回答，之後LLM向使用者回覆答案。

![顯示RAG架構的圖示](../../../translated_images/zh-TW/encoder-decode.f2658c25d0eadee2.webp)

RAG架構採用transformers實現，包含兩部分：編碼器與解碼器。舉例來說，當使用者詢問問題，輸入文字會被「編碼」成抓取單詞意義的向量，這些向量再被「解碼」至文件索引，根據使用者查詢產生新文本。LLM使用編碼器-解碼器模型來生成輸出。

根據論文 [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst)，實作RAG有兩種方式：

- **_RAG-Sequence_** 使用檢索出來的文件預測最佳答案。

- **RAG-Token** 利用文件逐字產生下一個字元，再用它們來回答使用者問題。

### 為什麼要使用RAG？

- **資訊豐富性：** 確保文本回答是即時且最新的，透過存取內部知識庫提升專屬領域的表現。

- 透過利用知識庫中的<strong>可驗證資料</strong>提供回答上下文，降低捏造資料的風險。

- <strong>成本效益高</strong>，相較於微調LLM更經濟實惠。

## 建立知識庫

我們的應用基於個人資料，即AI入門課程中的神經網路部分。

### 向量資料庫

向量資料庫與傳統資料庫不同，是專門設計用來存儲、管理及搜尋嵌入向量的資料庫。它儲存文件的數值表示。將資料分解為數字向量後，我們的AI系統更容易理解與處理資料。

我們將嵌入存入向量資料庫，因LLM輸入的token數有限，不能一次輸入整個嵌入，因此須將資料切塊，當使用者提問時，最相關的嵌入與提示一起回傳。切塊也有助於降低通過LLM的token數量，減少成本。

常用的向量資料庫包括Azure Cosmos DB、Clarifyai、Pinecone、Chromadb、ScaNN、Qdrant及DeepLake。您可以使用Azure CLI用以下指令建立Azure Cosmos DB模型：

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### 從文本到嵌入向量

在儲存資料前，我們需將其轉換為向量嵌入。若您處理大型文件或長文本，可以依預期查詢進行切塊。切塊可以在句子或段落層級。因切塊需靠周圍詞彙推斷意義，您可以為切塊加入額外上下文，例如加入文件標題，或包括切塊前後的一些文字。切塊可依下列方式進行：

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

    # 如果最後一個區塊沒有達到最小長度，仍然將其添加
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

切塊後，我們可以用不同的嵌入模型將文本嵌入。一些可用模型包括：word2vec、OpenAI的ada-002、Azure Computer Vision等。選擇模型會取決於使用語言、編碼內容型態（文本/圖片/音訊）、可編碼的輸入大小與生成嵌入的長度。

以下為使用OpenAI `text-embedding-ada-002`模型嵌入文本的示例：
![詞彙 "cat" 的嵌入向量圖](../../../translated_images/zh-TW/cat.74cbd7946bc9ca38.webp)

## 檢索與向量搜尋

當使用者發問時，檢索器會先將問題用查詢編碼器轉成向量，接著在文件搜尋索引中尋找與該向量相關的文件向量。找到後，將輸入向量與文件向量轉換為文字，再傳遞給LLM。

### 檢索

檢索是系統在索引中快速尋找符合條件文件的過程。檢索器目標是取得可用於提供上下文並讓LLM基於您的資料產生回答的文件。

在資料庫中執行搜尋有多種方式：

- <strong>關鍵字搜尋</strong> - 用於文本搜尋。

- <strong>向量搜尋</strong> - 利用嵌入模型將文件由文本轉為向量，允許使用詞彙意義進行<strong>語義搜尋</strong>。檢索是透過相近向量表示的文件來查詢問題相關文件。

- <strong>混合搜尋</strong> - 結合關鍵字與向量搜尋。

檢索挑戰在於資料庫中若沒有和查詢相似的回答，系統只會回傳最佳匹配資訊。可透過設定最大相關距離或使用混合搜尋來改善。本課程中我們將使用結合向量與關鍵字的混合搜尋，並將資料儲存在包含切塊與嵌入的資料框中。

### 向量相似度

檢索器會在知識庫中搜尋彼此接近的嵌入，也就是最接近的鄰居，因為它們代表相似文本。使用者輸入查詢時，先將查詢嵌入，再與相似嵌入匹配。常用相似度衡量是餘弦相似度，根據兩向量間角度計算。

其他衡量相似度的方法包含歐氏距離（兩向量端點的直線距離）及內積（兩向量對應元素乘積總和）。

### 搜尋索引

檢索前需為知識庫建立搜尋索引。索引儲存嵌入能快速擷取資料庫中最相似切塊。可使用如下方式在本地建立索引：

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# 建立搜尋索引
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# 要查詢索引，可以使用 kneighbors 方法
distances, indices = nbrs.kneighbors(embeddings)
```

### 排序再排序（Re-ranking）

查詢資料庫後，可能會需要將結果依相關性排序。再排序LLM利用機器學習依照優先相關性重新排列搜尋結果。使用Azure AI Search時，會自動使用語義再排序器完成此操作。下圖為利用最近鄰排序的示範：

```python
# 找到最相似的文件
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

## 整合流程

最後步驟是加入LLM，使回答能基於我們的資料。實作如下：

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

    # 結合歷史記錄和使用者輸入
    history.append(user_input)

    # 建立訊息物件
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # 使用回應 API 產生回答
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

## 評估應用程式

### 評估指標

- 確保回答品質自然流暢且具人類語感。

- 基於資料的牢靠性：評估回答是否來自提供的文件。

- 相關性：評估回答是否符合且與所提問題相關。

- 流暢度：回答是否符合語法邏輯。

## 使用RAG（檢索增強生成）與向量資料庫的應用場景

許多場景中，功能呼叫能提升您的應用，如：

- 問答系統：將公司資料基礎於聊天系統，供員工提出問題。

- 推薦系統：建立匹配最相似項目的系統，例如電影、餐廳等。

- 聊天機器人服務：儲存聊天紀錄，根據使用者資料個性化對話。

- 基於向量嵌入的圖片搜尋，有助於圖像辨識與異常偵測。

## 摘要

我們探討了RAG的基本領域，從資料納入應用、使用者查詢到輸出。為簡化RAG開發，您可使用Semanti Kernel、Langchain或Autogen等框架。

## 作業

為繼續學習檢索增強生成（RAG），您可以：

- 使用您選擇的框架建立應用前端。

- 利用LangChain或Semantic Kernel框架，重建您的應用程式。

恭喜完成本課程 👏。

## 學習不止於此，繼續前進

完成本課程後，請查看我們的[生成式AI學習合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升您的生成式AI知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->