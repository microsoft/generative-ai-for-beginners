# 検索拡張生成 (RAG) とベクターデータベース

[![検索拡張生成 (RAG) とベクターデータベース](../../../translated_images/15-lesson-banner.png?WT.ae1ec4b596c9c2b74121dd24c30143380d4789a9ef381276dbbc9fd5d7abc3d5.ja.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson15-gh?WT.mc_id=academic-105485-koreyst)

検索アプリケーションのレッスンでは、独自のデータを大規模言語モデル (LLM) に統合する方法について簡単に学びました。このレッスンでは、LLM アプリケーションにおけるデータの基盤化、プロセスの仕組み、埋め込みやテキストを含むデータの保存方法について詳しく掘り下げます。

> **ビデオは近日公開予定**

## はじめに

このレッスンでカバーする内容は以下の通りです：

- RAGの概要、AI（人工知能）での使用理由。

- ベクターデータベースの理解とアプリケーションのための作成。

- アプリケーションにRAGを統合する実用的な例。

## 学習目標

このレッスンを完了すると、次のことができるようになります：

- データ検索と処理におけるRAGの重要性を説明する。

- RAGアプリケーションを設定し、データをLLMに基づかせる。

- LLMアプリケーションにおけるRAGとベクターデータベースの効果的な統合。

## 私たちのシナリオ: 独自のデータでLLMを強化

このレッスンでは、教育スタートアップに独自のノートを追加し、チャットボットがさまざまな科目についての情報を得られるようにします。ノートを使用することで、学習者はより良く勉強し、異なるトピックを理解しやすくなり、試験の復習が容易になります。シナリオを作成するために、以下を使用します：

- `Azure OpenAI:` チャットボットを作成するために使用するLLM

- `AI for beginners' lesson on Neural Networks`: これがLLMの基盤となるデータ

- `Azure AI Search` と `Azure Cosmos DB:` ベクターデータベースでデータを保存し、検索インデックスを作成

ユーザーはノートから練習クイズを作成し、復習用のフラッシュカードを作成し、要約して簡潔な概要を得ることができます。始めるにあたり、RAGとは何か、どのように機能するのかを見てみましょう：

## 検索拡張生成 (RAG)

LLMを搭載したチャットボットは、ユーザーのプロンプトを処理して応答を生成します。これは対話型に設計されており、さまざまなトピックでユーザーとやり取りします。しかし、その応答は提供されたコンテキストと基礎的なトレーニングデータに制限されています。たとえば、GPT-4の知識のカットオフは2021年9月であり、それ以降に発生した出来事についての知識はありません。さらに、LLMのトレーニングに使用されるデータには、個人のノートや企業の製品マニュアルのような機密情報は含まれていません。

### RAGs (検索拡張生成) の仕組み

![RAGsの仕組みを示す図](../../../translated_images/how-rag-works.png?WT.fde75879826c169b53e16dc0d0d6691172c75b314400f380d40a9f31244eba0e.ja.mc_id=academic-105485-koreyst)

ノートからクイズを作成するチャットボットを展開したいと仮定します。そのためには、知識ベースへの接続が必要です。ここでRAGが役立ちます。RAGsは次のように動作します：

- **知識ベース:** 検索の前に、これらの文書を取り込み、前処理を行う必要があります。通常、大きな文書を小さなチャンクに分割し、テキスト埋め込みに変換してデータベースに保存します。

- **ユーザーの質問:** ユーザーが質問をします。

- **検索:** ユーザーが質問をしたとき、埋め込みモデルが知識ベースから関連情報を検索し、プロンプトに組み込むためのコンテキストを提供します。

- **拡張生成:** LLMは取得したデータに基づいて応答を強化します。これにより、生成される応答が事前にトレーニングされたデータだけでなく、追加されたコンテキストからの関連情報に基づくようになります。取得したデータはLLMの応答を拡張するために使用されます。その後、LLMはユーザーの質問に対する答えを返します。

![RAGsのアーキテクチャを示す図](../../../translated_images/encoder-decode.png?WT.80c3c9669a10e85d1f7e9dc7f7f0d416a71e16d2f8a6da93267e55cbfbddbf9f.ja.mc_id=academic-105485-koreyst)

RAGsのアーキテクチャは、エンコーダとデコーダの2つの部分からなるトランスフォーマーを使用して実装されます。たとえば、ユーザーが質問をすると、その入力テキストが「エンコード」され、単語の意味を捉えたベクトルに変換され、そのベクトルがドキュメントインデックスに「デコード」され、ユーザーの質問に基づいて新しいテキストを生成します。LLMはエンコーダ-デコーダモデルの両方を使用して出力を生成します。

提案された論文に従ってRAGを実装する際の2つのアプローチ：[知識集約型NLP（自然言語処理ソフトウェア）タスクのための検索拡張生成](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst)は：

- **_RAG-Sequence_** 検索された文書を使用してユーザーの質問に対する最良の答えを予測する

- **RAG-Token** 文書を使用して次のトークンを生成し、それを取得してユーザーの質問に答える

### なぜRAGsを使用するのか？

- **情報の豊かさ:** テキストの応答が最新であることを保証します。したがって、内部知識ベースにアクセスすることで、特定のドメインのタスクでのパフォーマンスを向上させます。

- 知識ベースの**検証可能なデータ**を利用してユーザーの質問にコンテキストを提供することで、虚偽を減らします。

- LLMを微調整するよりも経済的であるため、**費用対効果が高い**です。

## 知識ベースの作成

私たちのアプリケーションは、AI初心者向けカリキュラムのニューラルネットワークレッスンという個人データに基づいています。

### ベクターデータベース

ベクターデータベースは、従来のデータベースとは異なり、埋め込まれたベクトルを保存、管理、検索するために設計された特殊なデータベースです。文書の数値表現を保存します。データを数値埋め込みに分解することで、AIシステムがデータを理解し処理しやすくなります。

埋め込みをベクターデータベースに保存する理由は、LLMが入力として受け入れるトークンの数に制限があるためです。すべての埋め込みをLLMに渡すことはできないため、チャンクに分割する必要があります。ユーザーが質問をしたときに、質問に最も似ている埋め込みがプロンプトとともに返されます。チャンク化は、LLMを通じて渡されるトークンの数を減らし、コストを削減します。

人気のあるベクターデータベースには、Azure Cosmos DB、Clarifyai、Pinecone、Chromadb、ScaNN、Qdrant、DeepLakeなどがあります。Azure CLIを使用して次のコマンドでAzure Cosmos DBモデルを作成できます：

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### テキストから埋め込みへ

データを保存する前に、それをベクトル埋め込みに変換してデータベースに保存する必要があります。大きな文書や長いテキストを扱う場合、予想されるクエリに基づいてチャンク化できます。チャンク化は文レベルまたは段落レベルで行うことができます。チャンク化は周囲の単語から意味を導くため、チャンクに追加のコンテキストを追加することもできます。たとえば、文書のタイトルを追加したり、チャンクの前後にテキストを含めたりすることです。データを次のようにチャンク化できます：

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

チャンク化が完了したら、さまざまな埋め込みモデルを使用してテキストを埋め込むことができます。使用できるモデルには、word2vec、OpenAIのada-002、Azure Computer Visionなどがあります。使用するモデルを選択する際には、使用する言語、エンコードされるコンテンツのタイプ（テキスト/画像/音声）、エンコードできる入力のサイズ、埋め込み出力の長さに依存します。

OpenAIの`text-embedding-ada-002`モデルを使用した埋め込まれたテキストの例は次のとおりです：
![猫の単語の埋め込み](../../../translated_images/cat.png?WT.6f67a41409b2174c6f543273f4a9f8c38b227112a12831da3070e52f13e03818.ja.mc_id=academic-105485-koreyst)

## 検索とベクター検索

ユーザーが質問をしたとき、検索者はそれをクエリエンコーダを使用してベクトルに変換し、入力に関連する文書の検索インデックスを通じて関連するベクトルを検索します。完了すると、入力ベクトルと文書ベクトルの両方をテキストに変換し、LLMに渡します。

### 検索

検索は、システムが検索条件を満たす文書をインデックスから迅速に見つけようとする際に行われます。検索者の目的は、コンテキストを提供し、データに基づいてLLMを基盤とするために使用される文書を取得することです。

データベース内で検索を実行する方法はいくつかあります：

- **キーワード検索** - テキスト検索に使用されます。

- **セマンティック検索** - 単語の意味を使用します。

- **ベクター検索** - 埋め込みモデルを使用して文書をテキストからベクトル表現に変換します。検索は、ユーザーの質問に最も近いベクトル表現を持つ文書をクエリすることで行われます。

- **ハイブリッド** - キーワード検索とベクター検索の両方を組み合わせたもの。

検索の課題は、データベース内にクエリに対する類似の応答がない場合に発生します。その場合、システムは得られる最良の情報を返しますが、関連性の最大距離を設定したり、キーワードとベクター検索の両方を組み合わせたハイブリッド検索を使用したりする戦術を使用できます。このレッスンでは、ベクター検索とキーワード検索の両方を組み合わせたハイブリッド検索を使用します。チャンクと埋め込みを含む列を持つデータフレームにデータを保存します。

### ベクター類似性

検索者は、知識データベース内で近接している埋め込みを検索します。これらは類似したテキストです。ユーザーがクエリを尋ねた場合、それはまず埋め込まれ、類似した埋め込みと一致します。異なるベクトルがどの程度類似しているかを見つけるために使用される一般的な測定基準は、2つのベクトル間の角度に基づくコサイン類似性です。

類似性を測定する他の代替手段として、ベクトルの端点間の直線であるユークリッド距離や、2つのベクトルの対応する要素の積の合計を測定するドット積を使用できます。

### 検索インデックス

検索を行う際には、検索を実行する前に知識ベースの検索インデックスを作成する必要があります。インデックスは埋め込みを保存し、大規模なデータベースでも最も類似したチャンクを迅速に取得できます。インデックスをローカルで作成するには：

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### 再ランキング

データベースをクエリした後、最も関連性のあるものから結果をソートする必要があるかもしれません。再ランキングLLMは、検索結果の関連性を向上させるために、機械学習を利用して最も関連性の高いものから順に並べ替えます。Azure AI Searchを使用すると、セマンティック再ランカーを使用して再ランキングが自動的に行われます。最も近い隣人を使用した再ランキングの例：

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

## すべてをまとめる

最後のステップは、データに基づいた応答を得るためにLLMを組み込むことです。次のように実装できます：

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

## アプリケーションの評価

### 評価指標

- 応答の質を確保し、自然で流暢で人間らしい響きを持つこと。

- データの基盤性：提供された文書からの応答であるかどうかを評価する。

- 関連性：応答が質問に一致し、関連しているかどうかを評価する。

- 流暢さ - 応答が文法的に意味を持つかどうか。

## RAG（検索拡張生成）とベクターデータベースの使用例

関数呼び出しがアプリを改善できるさまざまな使用例があります：

- 質問と回答：会社のデータをチャットに基盤とし、従業員が質問できるようにする。

- レコメンデーションシステム：最も類似した値を一致させるシステムを作成できる場所、例：映画、レストランなど。

- チャットボットサービス：チャット履歴を保存し、ユーザーデータに基づいて会話をパーソナライズする。

- ベクター埋め込みに基づく画像検索、画像認識や異常検出に役立ちます。

## まとめ

データのアプリケーションへの追加、ユーザーのクエリと出力など、RAGの基本的な領域をカバーしました。RAGの作成を簡素化するために、Semanti Kernel、Langchain、Autogenなどのフレームワークを使用できます。

## 課題

検索拡張生成 (RAG) の学習を続けるために、次のことを行うことができます：

- お好みのフレームワークを使用してアプリケーションのフロントエンドを構築する。

- LangChainまたはSemantic Kernelのいずれかのフレームワークを使用して、アプリケーションを再作成する。

レッスンを完了したことをお祝いします 👏。

## 学習はここで終わりません、旅を続けましょう

このレッスンを完了した後、[生成AI学習コレクション](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)をチェックして、生成AIの知識をさらに向上させましょう！

**免責事項**:  
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを期すよう努めておりますが、自動翻訳には誤りや不正確さが含まれる可能性がありますのでご注意ください。原文の言語によるオリジナル文書を権威ある情報源とみなすべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤訳について、当社は責任を負いません。