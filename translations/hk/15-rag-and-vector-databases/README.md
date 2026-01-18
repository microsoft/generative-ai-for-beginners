<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2210a0466c812d9defc4df2d9a709ff9",
  "translation_date": "2026-01-18T17:12:06+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "hk"
}
-->
# 檢索增強生成 (RAG) 與向量資料庫

[![檢索增強生成 (RAG) 與向量資料庫](../../../../../translated_images/hk/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

在搜尋應用課程中，我們曾簡略學習如何將自己的資料整合到大型語言模型（LLMs）中。本課程將進一步深入探討在 LLM 應用中將資料紮根的概念、流程機制及資料儲存方法，包括向量嵌入及文字。

> **影片即將推出**

## 介紹

本課程將涵蓋以下內容：

- 介紹 RAG 是什麼及其在人工智慧 (AI) 中的用途。

- 了解向量資料庫是什麼及為我們的應用建立一個。

- 實作範例示範如何將 RAG 整合到應用中。

## 學習目標

完成本課程後，您將能夠：

- 解釋 RAG 在資料檢索與處理中的重要性。

- 設定 RAG 應用並將資料紮根於 LLM。

- 有效整合 RAG 與向量資料庫於 LLM 應用中。

## 我們的場景：用自己的資料強化 LLM

本課程中，我們想將自己的筆記加入教育新創平台，以便聊天機器人能取得更多不同科目的資訊。利用這些筆記，學習者將能更佳地學習並理解各主題，方便為考試複習。為建立場景，我們將使用：

- `Azure OpenAI:` 我們用來打造聊天機器人的 LLM。

- `AI for beginners' lesson on Neural Networks:` 作為紮根我們 LLM 的資料。

- `Azure AI Search` 與 `Azure Cosmos DB:` 向量資料庫，用以儲存資料並建立搜尋索引。

使用者可根據筆記產生練習測驗、複習閃卡及將內容摘要為簡明總結。開始前，讓我們先了解什麼是 RAG 及其運作方式：

## 檢索增強生成 (RAG)

由 LLM 推動的聊天機器人處理用戶提示以生成回應。它被設計為互動式，能在多種主題與使用者交流。但其回應侷限於所提供的上下文與基礎訓練資料。例如 GPT-4 的知識截止於 2021 年 9 月，意即它不具備該日期後發生事件的知識。另外，訓練 LLM 的資料中不包含機密資訊，如個人筆記或公司的產品手冊。

### RAG（檢索增強生成）的運作方式

![drawing showing how RAGs work](../../../../../translated_images/hk/how-rag-works.f5d0ff63942bd3a6.webp)

假設你想部署一個可以從筆記建立測驗題的聊天機器人，你需要連接到知識庫。此時 RAG 發揮作用。RAG 運作流程如下：

- **知識庫：** 在檢索前，這些文件需被匯入並預處理，通常將大型文件分割成較小的區塊，再轉成文字嵌入並儲存在資料庫中。

- **使用者詢問：** 使用者提出問題。

- **檢索：** 使用者提問時，嵌入模型從知識庫中取回相關資訊，提供更多上下文以納入提示。

- **增強生成：** LLM 根據取回的資料強化回應，不僅基於預訓練的資料，同時結合相關上下文資訊。檢索到的資料用以增強 LLM 的回應，LLM 然後返回答案給使用者。

![drawing showing how RAGs architecture](../../../../../translated_images/hk/encoder-decode.f2658c25d0eadee2.webp)

RAG 架構透過 transformer 實現，由編碼器和解碼器兩部分組成。例如，當用戶提出問題時，輸入文字被「編碼」成捕捉詞意的向量，而這些向量被「解碼」用於文件索引並根據用戶查詢生成新文字。LLM 結合編碼器與解碼器模型生成輸出。

根據提案論文 [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst)，實作 RAG 有兩種方法：

- **_RAG-Sequence_** 使用檢索到的文件預測最佳答覆用戶查詢的答案。

- **RAG-Token** 利用文件產生下一個 token，然後檢索它們以回答用戶查詢。

### 為何要使用 RAG？

- **資訊豐富性：** 確保文字回應為最新且即時。藉由存取內部知識庫，提升特定領域任務的效能。

- 利用知識庫中的 **可驗證數據** 降低捏造資訊，為使用者查詢提供上下文。

- **成本效益佳，** 相較微調 LLM 更經濟。

## 建立知識庫

我們的應用基於個人資料，即 AI 初學者課程中的神經網路單元。

### 向量資料庫

向量資料庫與傳統資料庫不同，是專門設計用於儲存、管理與搜尋嵌入向量的資料庫。它儲存文件的數值表示。將資料轉成數值嵌入使 AI 系統更容易理解與處理資料。

我們將嵌入存於向量資料庫中，因為 LLM 對可接受輸入的 token 數有上限。無法將整個嵌入一次輸入 LLM，因此需將其分塊。當用戶提問時，會回傳與問題最相似的嵌入及提示。分塊也能降低經過 LLM 的 token 代價。

常見的向量資料庫包括 Azure Cosmos DB、Clarifyai、Pinecone、Chromadb、ScaNN、Qdrant 與 DeepLake。你可使用 Azure CLI 下列指令建立 Azure Cosmos DB 模型：

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### 從文字到嵌入向量

儲存資料前，需要將其轉換為向量嵌入再存至資料庫。如果處理大型文件或長文本，可根據預期查詢將其分塊。分塊可於句子層次或段落層次完成。因為分塊須從周圍文字擷取意義，你可加上其他上下文，如文件標題或加上分塊前後的文字。資料分塊方式如下：

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

    # 如果最後一個區塊未達到最短長度，仍然加入該區塊
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

分塊後，我們再使用不同嵌入模型將文字嵌入。一些可用模型包括 word2vec、OpenAI 的 ada-002、Azure Computer Vision 等。選擇模型時會視語言、編碼內容類型（文字/圖片/音訊）、可編碼輸入大小及輸出嵌入長度而定。

以下為使用 OpenAI `text-embedding-ada-002` 模型嵌入「cat」字的示例：
![an embedding of the word cat](../../../../../translated_images/hk/cat.74cbd7946bc9ca38.webp)

## 檢索和向量搜尋

用戶提問時，檢索器使用查詢編碼器將其轉為向量，接著在文件搜尋索引中尋找與輸入相關的向量。一旦完成，將輸入向量和文件向量轉成文字並送入 LLM。

### 檢索

檢索是系統迅速尋找符合搜尋條件的文件。檢索器目標是取得用來提供上下文並將 LLM 紮根於資料的文件。

資料庫內搜尋方法包括：

- **關鍵字搜尋** — 用於文字搜尋。

- **向量搜尋** — 使用嵌入模型將文件從文字轉為向量表示，允許根據詞意的**語意搜尋**。檢索將找出向量表示與用戶問題最接近的文件。

- **混合搜尋** — 關鍵字與向量搜尋結合。

檢索的挑戰是若資料庫中無與查詢相似的回應，系統只能回傳最接近資訊。可使用設定最大相關距離或混合搜尋等策略。本課程使用混合搜尋，結合向量與關鍵字搜尋。我們將資料存入含有分塊及嵌入數據欄位的 dataframe。

### 向量相似度

檢索器會尋找知識庫中彼此靠近的嵌入，即最鄰近的向量，因為它們文本相似。場景中用戶查詢先被嵌入，再與相似嵌入配對。衡量不同向量相似度的常見方法是餘弦相似度（基於兩向量間角度）。

其他可用衡量方法包括歐氏距離（向量端點間直線距離）及點積（兩向量對應元素乘積和）。

### 搜尋索引

執行檢索前，我們需為知識庫建立搜尋索引。索引儲存嵌入，能於大型資料庫迅速找出最相似區塊。我們可在本地建立索引：

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# 建立搜尋索引
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# 要查詢索引，你可以使用kneighbors方法
distances, indices = nbrs.kneighbors(embeddings)
```

### 重新排名

完成資料庫查詢後，可能需按照相關性排序結果。重新排名 LLM 利用機器學習依相關性對搜尋結果排序。使用 Azure AI Search 時，語意重新排名器會自動進行此步驟。下圖示範如何根據最近鄰做重新排名：

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

## 整合所有元素

最後一步是將 LLM 加入組合，讓回應可紮根於我們的資料。可按照以下方式實現：

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

    # 創建一個訊息對象
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

## 應用評估

### 評估指標

- 回應品質：確保回應自然流暢、具人類語感。

- 資料紮根度：評估回應是否源自提供的文件。

- 相關性：評估回應是否與提問相符且相關。

- 流暢度：評估回應語法是否合理。

## RAG（檢索增強生成）與向量資料庫的使用案例

多種使用場合可透過功能呼叫改善應用，例如：

- 問答系統：將公司資料紮根於聊天機器人，供員工提問。

- 推薦系統：建立系統匹配相似項目，如電影、餐廳等。

- 聊天機器人服務：儲存聊天紀錄，根據使用者資料個人化對話。

- 基於向量嵌入的影像搜尋，適用於圖像識別與異常檢測。

## 總結

我們已涵蓋 RAG 的基本範圍，從將資料加入應用、使用者查詢到回應輸出。為簡化 RAG 建置，可使用 Semanti Kernel、Langchain 或 Autogen 等框架。

## 作業

繼續學習 RAG，您可以建置：

- 利用您選擇的框架打造應用前端。

- 運用 LangChain 或 Semantic Kernel 框架重建您的應用。

恭喜您完成課程 👏。

## 學習不止於此，繼續探索旅程

完成本課程後，前往我們的 [生成式 AI 學習集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，持續提升您的生成式 AI 知識！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的內容，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言版本的文件應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用此翻譯而引起的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->