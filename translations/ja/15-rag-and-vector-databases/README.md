<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2210a0466c812d9defc4df2d9a709ff9",
  "translation_date": "2026-01-18T17:20:19+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "ja"
}
-->
# Retrieval Augmented Generation (RAG) とベクトルデータベース

[![Retrieval Augmented Generation (RAG) とベクトルデータベース](../../../../../translated_images/ja/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

検索アプリケーションのレッスンでは、独自のデータを大規模言語モデル（LLM）に統合する方法を簡単に学びました。このレッスンでは、LLMアプリケーションにおけるデータのグラウンディングの概念、そのプロセスの仕組み、エンベディングとテキストの両方を含むデータの保存方法についてさらに詳しく掘り下げます。

> **ビデオ近日公開予定**

## はじめに

このレッスンでは以下の内容を扱います：

- RAGの紹介、その意味とAI（人工知能）で使用される理由

- ベクトルデータベースとは何かを理解し、アプリケーション用に作成する

- RAGをアプリケーションに統合する実践例

## 学習目標

このレッスンを修了後、以下ができるようになります：

- データの検索および処理におけるRAGの重要性を説明する

- RAGアプリケーションをセットアップし、データをLLMにグラウンドする

- LLMアプリケーションにおけるRAGとベクトルデータベースの効果的な統合

## シナリオ：自分のデータでLLMを強化する

このレッスンでは、自分のノートを教育系スタートアップに追加し、チャットボットが各教科についてより多くの情報を得られるようにしたいと考えています。ノートを活用することで、学習者は各トピックをよりよく学習・理解でき、試験勉強がしやすくなります。シナリオ作成には次のものを使用します：

- `Azure OpenAI:` チャットボット作成に利用するLLM

- `AI初心者向けのニューラルネットワークレッスン:` LLMにグラウンドするデータ

- `Azure AI Search` と `Azure Cosmos DB:` ベクトルデータベースとしてデータを保存し検索インデックスを作成

ユーザーはノートから練習問題や復習フラッシュカードを作成し、要約して簡潔な概要を得ることができます。始めるにあたり、RAGとは何か、およびその動作について見てみましょう：

## Retrieval Augmented Generation (RAG)

LLMを搭載したチャットボットは、ユーザープロンプトを処理して応答を生成します。インタラクティブで様々なテーマでユーザーとやりとりできます。ただし、応答は提供された文脈と基盤トレーニングデータに限定されます。例えば、GPT-4の知識カットオフは2021年9月で、それ以降の出来事には対応していません。さらに、LLM訓練に使われるデータには個人的なノートや会社のマニュアルなど機密情報は含まれていません。

### RAG（Retrieval Augmented Generation）の仕組み

![RAGの仕組みを示す図](../../../../../translated_images/ja/how-rag-works.f5d0ff63942bd3a6.webp)

ノートからクイズを作成するチャットボットを展開するとします。この場合、ナレッジベースへの接続が必要になります。ここでRAGが役立ちます。RAGの動作は以下の通りです：

- **ナレッジベース:** 検索の前に文書が取り込まれ、通常は大きな文書を小さなチャンクに分割し、テキストエンベディングに変換してデータベースに保存します。

- **ユーザークエリ:** ユーザーが質問する。

- **検索（Retrieval）：** クエリが入力されると、エンベディングモデルがナレッジベースから関連情報を検索し、それをプロンプトに組み込みます。

- **強化生成（Augmented Generation）：** LLMが取得データを基に応答を強化します。これにより、応答は事前訓練データだけでなく、追加された文脈に基づく関連情報に基づいて生成されます。LLMはその後、ユーザーの質問に対して回答を返します。

![RAGのアーキテクチャを示す図](../../../../../translated_images/ja/encoder-decode.f2658c25d0eadee2.webp)

RAGのアーキテクチャは、エンコーダーとデコーダーの2つで構成されるトランスフォーマーを使用して実装されます。たとえば、ユーザーが質問すると、入力テキストは意味を捉えるベクトルに「エンコード」され、これが文書インデックスに「デコード」されてユーザークエリに基づく新しいテキストを生成します。LLMはエンコーダーデコーダーモデルを使用して出力を生成します。

提案された論文「[Retrieval-Augmented Generation for Knowledge intensive NLP Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst)」によると、RAG実装には以下の2つのアプローチがあります：

- **_RAG-Sequence_**：取得した文書を用いてユーザークエリに対して最も適切な回答を予測する

- **RAG-Token**：文書を使って次のトークンを生成し、その後に文書を取得してユーザーの質問に答える

### なぜRAGを使うのか？

- **情報の豊富さ:** テキスト応答が最新の情報に基づき、ドメイン固有タスクのパフォーマンスを向上させます。

- **検証可能なデータ**を使った文脈提供によって虚偽情報を減らします。

- **コスト効率:** LLMのファインチューニングよりも経済的です。

## ナレッジベースの作成

今回のアプリケーションは個人データ、つまりAI初心者向けニューラルネットワークレッスンに基づいています。

### ベクトルデータベース

ベクトルデータベースは従来のデータベースとは異なり、埋め込みベクトルを保存・管理し検索するために特化したデータベースです。文書の数値表現を保存します。データを数値エンベディングに分解することで、AIシステムが理解・処理しやすくなります。

LLMは入力できるトークン数に制限があるため、エンベディング全体を一度に渡せません。そこでチャンクに分割し、ユーザーの質問に最も関連するエンベディングをプロンプトと共に返す仕組みが必要になります。チャンク分割はトークン数の削減によるコスト節約にも役立ちます。

代表的なベクトルデータベースにはAzure Cosmos DB、Clarifyai、Pinecone、Chromadb、ScaNN、Qdrant、DeepLakeがあります。Azure CLIでAzure Cosmos DBモデルを作成するには以下のコマンドを使用します：

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### テキストからエンベディングへ

データを保存する前に、テキストをベクトルエンベディングに変換します。長い文書や大きなテキストは、想定されるクエリに基づいてチャンクに分割可能です。チャンクは文や段落単位で行われます。周囲の言葉から意味を推測するため、チャンクに文書タイトルや前後のテキストなど付加情報を加えることも可能です。例えば次のようにチャンク分割します：

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

    # 最後のチャンクが最小長に達していなくても、とにかく追加してください
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

チャンク化したテキストは様々なエンベディングモデルを使ってベクトル化できます。利用モデル例にはword2vec、OpenAIのada-002、Azure Computer Visionなどがあり、言語、コンテンツ種別（テキスト/画像/音声）、入力サイズおよび出力エンベディング長により選択します。

OpenAIの`text-embedding-ada-002`モデルによる例：
![catという単語のエンベディング](../../../../../translated_images/ja/cat.74cbd7946bc9ca38.webp)

## 検索とベクトル検索

ユーザーが質問すると、検索器はクエリエンコーダーを使って質問をベクトル化し、文書検索インデックスで関連ベクトルを探します。見つかった入力ベクトルと文書ベクトルはテキストに変換され、LLMに渡されます。

### 検索（Retrieval）

検索はインデックスから条件に合う文書を素早く探すことです。検索器の目的は、文脈を提供しLLMにデータをグラウンドするための文書を得ることです。

検索方法例：

- **キーワード検索** - テキスト検索に使用

- **ベクトル検索** - 文書をテキストからエンベディングに変換し、単語の意味に基づく**意味検索**を実現。ユーザークエリに最も近いベクトルの文書を探す。

- **ハイブリッド** - キーワード検索とベクトル検索の組み合わせ

データベースに類似回答がない場合、最良の情報を返しますが、関連性の最大距離設定やキーワードとベクトル検索を組み合わせたハイブリッド検索で対応可能です。本レッスンではハイブリッド検索を使い、チャンクとエンベディングを列に持つデータフレームに保存します。

### ベクトル類似度

検索器は類似するエンベディング、すなわち近い隣接ベクトルを探します。ユーザーのクエリはベクトル化され類似ベクトルとマッチングされます。代表的な類似度測定には、2つのベクトル間の角度に基づくコサイン類似度を使います。

他にも、エウクリッド距離（ベクトルの端点間の直線距離）やドット積（対応する要素積の総和）なども類似度測定に利用できます。

### 検索インデックス

検索時にはナレッジベースのために検索インデックスを作成します。インデックスはエンベディングを保存し、大規模データベース中でも類似チャンクを素早く引き出せます。ローカルでのインデックス作成は以下で可能です：

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# 検索インデックスを作成する
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# インデックスをクエリするには、kneighborsメソッドを使用できます
distances, indices = nbrs.kneighbors(embeddings)
```

### 再ランキング

検索後の結果を関連度で並べ替えることがあります。再ランキングLLMは機械学習を使い検索結果を重要順に並べ直します。Azure AI Searchでは、意味的再ランキングが自動で行われます。近傍法での再ランキング例：

```python
# 最も類似した文書を見つける
distances, indices = nbrs.kneighbors([query_vector])

index = []
# 最も類似した文書を出力する
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## 全体のまとめ

最後のステップはLLMを加えて、データに基づいた応答を得ることです。実装例：

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # 質問をクエリベクターに変換する
    query_vector = create_embeddings(user_input)

    # 最も類似したドキュメントを見つける
    distances, indices = nbrs.kneighbors([query_vector])

    # コンテキストを提供するためにドキュメントをクエリに追加する
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # 履歴とユーザー入力を結合する
    history.append(user_input)

    # メッセージオブジェクトを作成する
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # チャット補完を使って応答を生成する
    response = openai.chat.completions.create(
        model="gpt-4",
        temperature=0.7,
        max_tokens=800,
        messages=messages
    )

    return response.choices[0].message

chatbot(user_input)
```

## アプリケーション評価

### 評価指標

- 応答の質：自然で流暢かつ人間らしいか

- グラウンディングの程度：応答が提供元文書に基づくか

- 関連性: 応答が質問内容に合っているか

- 流暢さ：文法的に意味が通っているか

## RAG（Retrieval Augmented Generation）やベクトルデータベースのユースケース

さまざまなユースケースで機能コールがアプリ改善に役立ちます：

- 質問応答：社内データをチャットにグラウンドし社員が質問可能にする

- レコメンデーションシステム：映画やレストランなど類似度の高いものをマッチング

- チャットボットサービス：チャット履歴を保存しユーザーごとに会話パーソナライズ

- 画像検索：ベクトルエンベディングを使い画像認識や異常検知に活用

## まとめ

RAGの基礎、データ追加、ユーザークエリ、アウトプットについて学びました。RAG構築を簡素化するためSemanti Kernel、Langchain、Autogenなどのフレームワークを使うこともできます。

## 課題

Retrieval Augmented Generation (RAG) の学習を続けるために以下を構築しましょう：

- 好きなフレームワークを使ってアプリケーションのフロントエンドを作成

- LangChain または Semantic Kernel などのフレームワークを使い、アプリケーションを再構築

レッスン完了おめでとうございます 👏

## 学びはここで終わりません、旅を続けましょう

レッスン修了後は、[Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) をご覧いただき、ジェネレーティブAIの知識をさらに深めてください！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確さには努めておりますが、自動翻訳には誤りや不正確な表現が含まれる可能性があります。正確な情報は原文のネイティブ言語版をご参照ください。重要な情報については、専門の人間による翻訳を推奨いたします。本翻訳の利用による誤解や誤訳に関して、当方は一切の責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->