<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4b0266fbadbba7ded891b6485adc66d",
  "translation_date": "2025-10-17T23:52:26+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "ja"
}
-->
# 検索拡張生成（RAG）とベクターデータベース

[![検索拡張生成（RAG）とベクターデータベース](../../../translated_images/15-lesson-banner.ac49e59506175d4fc6ce521561dab2f9ccc6187410236376cfaed13cde371b90.ja.png)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

検索アプリケーションのレッスンでは、独自のデータを大規模言語モデル（LLM）に統合する方法について簡単に学びました。このレッスンでは、LLMアプリケーションにおけるデータの基盤化の概念、プロセスの仕組み、および埋め込みやテキストを含むデータを保存する方法についてさらに詳しく掘り下げます。

> **ビデオは近日公開予定**

## はじめに

このレッスンでは以下の内容を学びます：

- RAGの概要、RAGとは何か、そしてAI（人工知能）でなぜ使用されるのか。

- ベクターデータベースの理解と、アプリケーション用のベクターデータベースの作成。

- RAGをアプリケーションに統合する実践的な例。

## 学習目標

このレッスンを完了すると、以下ができるようになります：

- データの検索と処理におけるRAGの重要性を説明する。

- RAGアプリケーションを設定し、LLMにデータを基盤化する。

- LLMアプリケーションにおけるRAGとベクターデータベースの効果的な統合。

## シナリオ: 独自のデータでLLMを強化する

このレッスンでは、教育系スタートアップに独自のノートを追加し、チャットボットがさまざまな科目に関する情報を取得できるようにします。私たちのノートを使用することで、学習者はより良い学習ができ、さまざまなトピックを理解しやすくなり、試験の復習が簡単になります。このシナリオを作成するために以下を使用します：

- `Azure OpenAI:` チャットボットを作成するために使用するLLM

- `AI初心者向けレッスン：ニューラルネットワーク`: LLMを基盤化するデータ

- `Azure AI Search`と`Azure Cosmos DB:` データを保存し、検索インデックスを作成するためのベクターデータベース

ユーザーはノートから練習問題を作成したり、復習用のフラッシュカードを作成したり、簡潔な概要をまとめたりすることができます。まず、RAGとは何か、そしてその仕組みについて見ていきましょう。

## 検索拡張生成（RAG）

LLMを搭載したチャットボットは、ユーザーのプロンプトを処理して応答を生成します。これはインタラクティブに設計されており、幅広いトピックについてユーザーと対話します。しかし、その応答は提供されたコンテキストと基盤となるトレーニングデータに限定されます。例えば、GPT-4の知識のカットオフは2021年9月であり、それ以降に発生したイベントについての知識はありません。さらに、LLMのトレーニングに使用されるデータには、個人的なノートや会社の製品マニュアルなどの機密情報は含まれていません。

### RAG（検索拡張生成）の仕組み

![RAGの仕組みを示す図](../../../translated_images/how-rag-works.f5d0ff63942bd3a638e7efee7a6fce7f0787f6d7a1fca4e43f2a7a4d03cde3e0.ja.png)

例えば、ノートからクイズを作成するチャットボットを展開したい場合、知識ベースへの接続が必要です。ここでRAGが役立ちます。RAGの動作は以下の通りです：

- **知識ベース:** 検索の前に、これらの文書を取り込み、前処理を行う必要があります。通常、大きな文書を小さなチャンクに分割し、テキスト埋め込みに変換してデータベースに保存します。

- **ユーザーのクエリ:** ユーザーが質問をする。

- **検索:** ユーザーが質問をすると、埋め込みモデルが知識ベースから関連情報を検索し、プロンプトに組み込むためのコンテキストを提供します。

- **拡張生成:** LLMは取得したデータを基に応答を強化します。これにより、生成された応答が事前トレーニングデータだけでなく、追加されたコンテキストからの関連情報に基づくものとなります。取得したデータはLLMの応答を拡張するために使用されます。その後、LLMはユーザーの質問に対する回答を返します。

![RAGのアーキテクチャを示す図](../../../translated_images/encoder-decode.f2658c25d0eadee2377bb28cf3aee8b67aa9249bf64d3d57bb9be077c4bc4e1a.ja.png)

RAGのアーキテクチャは、エンコーダーとデコーダーの2つの部分からなるトランスフォーマーモデルを使用して実装されます。例えば、ユーザーが質問をすると、入力テキストが単語の意味を捉えるベクトルに「エンコード」され、そのベクトルが文書インデックスに「デコード」され、ユーザーのクエリに基づいて新しいテキストを生成します。LLMはエンコーダー-デコーダーモデルの両方を使用して出力を生成します。

提案された論文[知識集約型NLPタスクのための検索拡張生成](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst)によると、RAGを実装する際の2つのアプローチは以下の通りです：

- **_RAG-Sequence_** 検索された文書を使用して、ユーザーのクエリに対する最適な回答を予測する。

- **RAG-Token** 文書を使用して次のトークンを生成し、それを取得してユーザーのクエリに回答する。

### RAGを使用する理由

- **情報の豊富さ:** テキスト応答が最新であることを保証します。これにより、内部知識ベースにアクセスすることで、特定の分野のタスクのパフォーマンスが向上します。

- **検証可能なデータ**を使用して、ユーザーのクエリにコンテキストを提供することで、誤情報を減らします。

- LLMを微調整するよりも**コスト効率が良い**。

## 知識ベースの作成

私たちのアプリケーションは、個人的なデータ、つまりAI初心者向けカリキュラムのニューラルネットワークレッスンに基づいています。

### ベクターデータベース

ベクターデータベースは、従来のデータベースとは異なり、埋め込みベクトルを保存、管理、検索するために設計された専門的なデータベースです。文書の数値表現を保存します。データを数値埋め込みに分解することで、AIシステムがデータを理解し処理しやすくなります。

LLMは入力として受け入れるトークンの数に制限があるため、埋め込みをベクターデータベースに保存します。埋め込み全体をLLMに渡すことはできないため、チャンクに分割する必要があります。ユーザーが質問をすると、質問に最も近い埋め込みがプロンプトとともに返されます。チャンク化は、LLMに渡すトークンの数を減らすことでコストを削減するのにも役立ちます。

人気のあるベクターデータベースには、Azure Cosmos DB、Clarifyai、Pinecone、Chromadb、ScaNN、Qdrant、DeepLakeなどがあります。Azure CLIを使用して以下のコマンドでAzure Cosmos DBモデルを作成できます：

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### テキストから埋め込みへ

データを保存する前に、ベクタ埋め込みに変換する必要があります。大きな文書や長いテキストを扱う場合、予想されるクエリに基づいてチャンク化することができます。チャンク化は文レベルや段落レベルで行うことができます。チャンク化は周囲の単語から意味を導き出すため、チャンクに文書のタイトルを追加したり、チャンクの前後にテキストを含めたりして、いくつかのコンテキストを追加することができます。データを以下のようにチャンク化できます：

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

チャンク化された後、さまざまな埋め込みモデルを使用してテキストを埋め込むことができます。使用できるモデルには、word2vec、OpenAIのada-002、Azure Computer Visionなどがあります。使用するモデルの選択は、使用する言語、エンコードされるコンテンツの種類（テキスト/画像/音声）、エンコード可能な入力のサイズ、埋め込み出力の長さによって異なります。

OpenAIの`text-embedding-ada-002`モデルを使用して埋め込まれたテキストの例：
![猫の埋め込み](../../../translated_images/cat.74cbd7946bc9ca380a8894c4de0c706a4f85b16296ffabbf52d6175df6bf841e.ja.png)

## 検索とベクター検索

ユーザーが質問をすると、検索者はクエリエンコーダーを使用して質問をベクトルに変換し、その後、文書検索インデックスを検索して入力に関連する文書のベクトルを見つけます。完了すると、入力ベクトルと文書ベクトルの両方をテキストに変換し、LLMに渡します。

### 検索

検索は、システムが検索条件を満たす文書をインデックスから迅速に見つけようとする際に発生します。検索者の目標は、コンテキストを提供し、LLMをデータに基づかせるために使用される文書を取得することです。

データベース内で検索を行う方法はいくつかあります：

- **キーワード検索** - テキスト検索に使用される。

- **セマンティック検索** - 単語の意味を使用する。

- **ベクター検索** - 埋め込みモデルを使用して文書をテキストからベクトル表現に変換します。検索は、ユーザーの質問に最も近いベクトル表現を持つ文書をクエリすることで行われます。

- **ハイブリッド** - キーワード検索とベクター検索の組み合わせ。

検索における課題は、データベース内にクエリに類似した応答がない場合に発生します。この場合、システムは可能な限り最良の情報を返します。ただし、関連性の最大距離を設定したり、キーワード検索とベクター検索を組み合わせたハイブリッド検索を使用したりする戦術を使用できます。このレッスンでは、キーワード検索とベクター検索を組み合わせたハイブリッド検索を使用します。データをチャンクと埋め込みを含む列を持つデータフレームに保存します。

### ベクター類似性

検索者は知識データベースを検索し、近接している埋め込みを探します。これらは類似したテキストです。ユーザーがクエリを行うと、まず埋め込まれ、次に類似した埋め込みと一致します。異なるベクトルがどれだけ類似しているかを見つけるために使用される一般的な測定方法は、コサイン類似度であり、2つのベクトル間の角度に基づいています。

類似性を測定する他の代替手段として、ベクトルの端点間の直線距離を測定するユークリッド距離や、2つのベクトルの対応する要素の積の合計を測定するドット積があります。

### 検索インデックス

検索を行う際には、検索を実行する前に知識ベースの検索インデックスを構築する必要があります。インデックスは埋め込みを保存し、大規模なデータベースでも最も類似したチャンクを迅速に取得できます。インデックスは以下のようにローカルで作成できます：

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### 再ランキング

データベースをクエリした後、最も関連性の高い結果から並べ替える必要がある場合があります。再ランキングLLMは、機械学習を利用して検索結果の関連性を向上させ、最も関連性の高いものから順に並べ替えます。Azure AI Searchを使用すると、セマンティック再ランキングを使用して自動的に再ランキングが行われます。最近傍を使用した再ランキングの例：

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

最後のステップは、LLMを組み込んで、データに基づいた応答を得られるようにすることです。以下のように実装できます：

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

- 自然で流暢で人間らしい応答が提供されているかどうか。

- データの基盤性：提供された文書からの応答であるかどうかを評価する。

- 関連性：応答が質問に一致し、関連しているかどうかを評価する。

- 流暢さ：応答が文法的に意味をなしているかどうか。

## RAG（検索拡張生成）とベクターデータベースの使用例

関数呼び出しがアプリを改善できるさまざまな使用例があります：

- 質問応答：会社のデータを基盤化して、従業員が質問できるチャットを作成。

- 推薦システム：映画、レストランなど、最も類似した値を一致させるシステムの作成。

- チャットボットサービス：チャット履歴を保存し、ユーザーデータに基づいて会話をパーソナライズ。

- ベクター埋め込みに基づく画像検索。画像認識や異常検出に役立つ。

## まとめ

このレッスンでは、RAGの基本的な領域について、アプリケーションへのデータの追加、ユーザーのクエリ、出力までをカバーしました。RAGの作成を簡素化するために、Semanti Kernel、Langchain、Autogenなどのフレームワークを使用できます。

## 課題

検索拡張生成（RAG）の学習を続けるために、以下を構築してください：

- 好きなフレームワークを使用してアプリケーションのフロントエンドを構築する。

- LangChainまたはSemantic Kernelのいずれかのフレームワークを使用して、アプリケーションを再構築する。

レッスンの完了おめでとうございます 👏。

## 学びはここで終わりません。旅を続けましょう

このレッスンを完了した後は、[生成AI学習コレクション](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)をチェックして、生成AIの知識をさらに深めてください！

---

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解について、当社は責任を負いません。