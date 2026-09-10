# 検索拡張生成（RAG）とベクトルデータベース

[![検索拡張生成（RAG）とベクトルデータベース](../../../translated_images/ja/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

検索アプリケーションのレッスンでは、独自のデータを大規模言語モデル（LLM）に統合する方法を簡単に学びました。本レッスンでは、LLMアプリケーションにデータを基盤づける概念、その仕組み、および埋め込みやテキストの両方を含むデータの保存方法についてさらに深く掘り下げます。

> <strong>ビデオはまもなく公開予定です</strong>

## はじめに

このレッスンでは以下の内容を扱います：

- RAGの紹介、その内容とAI（人工知能）で使用される理由。

- ベクトルデータベースとは何か、その理解とアプリケーション用の作成。

- RAGをアプリケーションに統合する実践的な例。

## 学習目標

このレッスンを修了すると、以下ができるようになります：

- RAGがデータ検索と処理において重要な理由を説明する。

- RAGアプリケーションのセットアップとデータをLLMに基盤づける。

- LLMアプリケーションでのRAGおよびベクトルデータベースの効果的な統合。

## シナリオ：独自のデータでLLMを強化する

このレッスンでは、教育系スタートアップに自分のノートを追加します。これによりチャットボットが様々な科目についてより多くの情報を取得できるようになります。学習者はノートを活用してより良く学習し、異なるトピックを理解しやすくなり、試験の復習が容易になります。シナリオ作成に使用するものは以下です：

- `Azure OpenAI:` チャットボットを作成するために使用するLLM

- `AI for beginners' lesson on Neural Networks`: LLMの基盤となるデータ

- `Azure AI Search` および `Azure Cosmos DB:` データを格納し検索インデックスを作成するベクトルデータベース

ユーザーはノートから練習クイズや復習用フラッシュカードを作成し、簡潔な概要に要約できます。まずRAGとは何か、その仕組みを見てみましょう：

## 検索拡張生成（RAG）

LLM搭載のチャットボットは、ユーザーのプロンプトを処理して応答を生成します。多岐にわたるトピックについてユーザーと対話できるよう設計されていますが、応答は提供されたコンテキストと基礎となるトレーニングデータに限られます。例えば、GPT-4の知識カットオフは2021年9月であり、それ以降の出来事については知識がありません。また、LLMのトレーニングデータには個人のノートや企業の製品マニュアルなどの機密情報は含まれていません。

### RAG（検索拡張生成）の仕組み

![RAGの仕組みを示す図](../../../translated_images/ja/how-rag-works.f5d0ff63942bd3a6.webp)

例えば、ノートからクイズを作成するチャットボットを導入したい場合、ナレッジベースへの接続が必要です。ここでRAGが役立ちます。RAGの動作は以下の通りです：

- **ナレッジベース：** 取得前に、これらの文書は取り込みと前処理が必要で、大きな文書を小さなチャンクに分割し、それをテキスト埋め込みに変換し、データベースに保存します。

- **ユーザーのクエリ：** ユーザーが質問する

- **検索：** ユーザーの質問に対して、埋め込みモデルはナレッジベースから関連情報を取得し、プロンプトに組み込みます。

- **拡張生成：** LLMは取得したデータに基づき応答を強化します。応答は事前学習データだけでなく、追加されたコンテキストからの関連情報に基づき生成されます。LLMはユーザーの質問に対してこの応答を返します。

![RAGのアーキテクチャを示す図](../../../translated_images/ja/encoder-decode.f2658c25d0eadee2.webp)

RAGのアーキテクチャは、エンコーダとデコーダの２つの部分からなるトランスフォーマーを使って実装されます。例えば、ユーザーが質問をすると、入力テキストが単語の意味を捉えたベクトルに「エンコード」され、そのベクトルが「デコード」されて文書インデックスに照合され、ユーザーのクエリに基づく新しいテキストを生成します。LLMはこのエンコーダ・デコーダモデルを用いて出力を生成します。

RAG実装に関する提案論文：[Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) によると、２つのアプローチがあります：

- **_RAG-Sequence_** 取得した文書を使ってユーザー質問に最適な回答を予測

- **RAG-Token** 文書を使って次のトークンを生成し、その後取得してユーザーの質問に回答

### なぜRAGを使うのか？

- **情報の豊富さ：** テキスト応答が最新かつ現状に即していることを保証し、特定ドメインのタスクでの性能が向上します。

- ナレッジベースの<strong>検証可能なデータ</strong>を活用して虚偽の情報を減らし、ユーザーの問い合わせにコンテキストを提供します。

- LLMのファインチューニングよりも<strong>コスト効率が良い</strong>です。

## ナレッジベースの作成

私たちのアプリケーションは個人データ、すなわち「AI for Beginners」のニューラルネットワークレッスンに基づいています。

### ベクトルデータベース

ベクトルデータベースは、従来のデータベースとは異なり、埋め込みベクトルを保存・管理・検索するための専門的なデータベースです。文書の数値表現を格納します。データを数値埋め込みに分解することで、AIシステムがデータを理解しやすくなります。

LLMは入力として受け入れるトークン数に制限があるため、埋め込みをベクトルデータベースに保存します。全ての埋め込みをLLMに渡すことはできないので、チャンクに分割し、ユーザーの質問に最も一致する埋め込みがプロンプトと一緒に返されます。チャンク化はまた、LLMを通過するトークン数のコスト削減にもつながります。

人気のあるベクトルデータベースには、Azure Cosmos DB、Clarifyai、Pinecone、Chromadb、ScaNN、Qdrant、DeepLakeなどがあります。Azure CLIを使ってAzure Cosmos DBモデルを作成するには次のコマンドを使います：

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### テキストから埋め込みへ

データを保存する前に、データをベクトル埋め込みに変換する必要があります。大きな文書や長いテキストの場合、想定されるクエリに基づきチャンクに分割できます。チャンク化は文単位、または段落単位で行えます。チャンクは周囲の単語から意味を導出するため、追加のコンテキスト、例えば文書のタイトルやチャンクの前後の文を加えることもできます。データは次のようにチャンク化できます：

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

    # 最後のチャンクが最小長に達していない場合でも、追加してください
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

チャンク化した後、様々な埋め込みモデルを使ってテキストを埋め込みます。利用可能なモデルには、word2vec、OpenAIのada-002、Azureコンピュータービジョンなど多数あります。どのモデルを選ぶかは使用言語、エンコードするコンテンツの種類（テキスト/画像/音声）、エンコード可能な入力サイズ、埋め込み出力の長さによって異なります。

OpenAIの `text-embedding-ada-002` モデルを用いたテキストの埋め込み例は以下の通りです：
![catという単語の埋め込み](../../../translated_images/ja/cat.74cbd7946bc9ca38.webp)

## 検索とベクトル検索

ユーザーが質問すると、検索器はその質問をクエリエンコーダでベクトルに変換し、文書の検索インデックスを検索して関連するベクトルを探します。検索完了後、入力ベクトルと文書ベクトルをテキストに戻し、それをLLMに渡します。

### 検索

検索は、システムが検索基準に合致する文書を素早く見つける処理です。検索器の目標は、コンテキストを提供し、あなたのデータに基づいたLLMの基盤を作るために使用する文書を取得することです。

データベース内の検索にはいくつかの方法があります：

- <strong>キーワード検索</strong> - テキスト検索で使用されます

- <strong>ベクトル検索</strong> - 文書を埋め込みモデルでテキストからベクトル表現に変換し、単語の意味を利用した<strong>意味検索</strong>が可能になります。検索はユーザーの質問に最も近いベクトル表現を持つ文書をクエリすることで行われます。

- <strong>ハイブリッド</strong> - キーワード検索とベクトル検索の組み合わせ。

検索時の課題の一つは、データベースに類似の応答がない場合です。その場合、システムは可能な限りベストな情報を返しますが、関連性の最大距離を設定したり、キーワードとベクトル検索を組み合わせたハイブリッド検索を使ったりする戦略があります。このレッスンではハイブリッド検索を使用し、チャンクと埋め込みを含むデータフレームにデータを保存します。

### ベクトル類似度

検索器はナレッジデータベース内で類似の埋め込みを探し、最も近い隣接ベクトルを見つけます。ユーザーのクエリは最初に埋め込みされ、類似する埋め込みとマッチングされます。ベクトル間の類似度を測定する一般的な手法はコサイン類似度で、２つのベクトル間の角度を基にします。

類似度の測定には他に、ベクトルの端点間の直線距離であるユークリッド距離や、対応する要素の積の和を計測するドット積も使えます。

### 検索インデックス

検索を行う際、まずナレッジベースのために検索インデックスを構築する必要があります。インデックスは埋め込みを保存し、大規模データベースでも最も類似したチャンクを迅速に取得できます。ローカルでインデックスを作成できます：

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# 検索インデックスを作成する
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# インデックスをクエリするには、kneighbors メソッドを使用できます
distances, indices = nbrs.kneighbors(embeddings)
```

### 再ランク付け

データベースをクエリした後、結果を関連性が高い順に並び替える必要があります。再ランク付けLLMは機械学習を用いて検索結果の関連性を改善し、最も関連性の高い順に並べます。Azure AI Searchではセマンティックランク付けが自動的に行われます。最寄りの近傍法による再ランク付けの例：

```python
# 最も類似したドキュメントを見つける
distances, indices = nbrs.kneighbors([query_vector])

index = []
# 最も類似したドキュメントを印刷する
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## まとめ

最後のステップは、LLMを組み込み、データに基づいた応答を取得することです。実装例は以下の通りです：

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # 質問をクエリベクトルに変換する
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

    # Responses APIを使用して応答を生成する
    response = client.responses.create(
        model="gpt-5-mini",
        max_output_tokens=800,
        input=messages,
        store=False,
    )

    return response.output_text

chatbot(user_input)
```

## アプリケーションの評価

### 評価指標

- 自然で滑らか、人間らしい応答の質

- データの基盤づけ：応答が提供された文書に基づくか評価

- 関連性：応答が質問とマッチし関連しているか評価

- 流暢さ：応答が文法的に意味をなすか

## RAG（検索拡張生成）とベクトルデータベースの利用例

機能呼び出しがアプリを改善できる様々なユースケースが存在します：

- 質問応答：自社データを基にしたチャットで従業員が質問できるシステム。

- レコメンデーションシステム：映画やレストランなど最も類似した価値をマッチングするシステム。

- チャットボットサービス：チャット履歴を保存し、ユーザーデータに基づいて会話をパーソナライズ。

- ベクトル埋め込みによる画像検索、画像認識や異常検知に有用。

## まとめ

RAGの基本領域をカバーしました。データの追加、ユーザークエリ、出力について説明しました。RAGの作成を簡素化するフレームワークとして、Semantic Kernel、Langchain、Autogenなどがあります。

## 課題

検索拡張生成（RAG）の学習を継続するために、以下を作成してください：

- お好みのフレームワークを使ってアプリケーションのフロントエンドを作成

- LangChainまたはSemantic Kernelいずれかのフレームワークを使用し、アプリケーションを再構築

レッスン完了おめでとうございます👏。

## 学習はここで終わりません、旅を続けましょう

レッスン修了後は、[Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) をチェックして、生成AIの知識をさらに深めてください！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->