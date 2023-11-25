# 検索アプリケーションの構築 

[![生成AIと大規模言語モデル入門](../../images/08-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](TBD)

> **ビデオは近日公開予定

LLMはチャットボットやテキスト生成以外にもある。エンベッディングを使って検索アプリケーションを構築することも可能だ。エンベッディングはベクトルとも呼ばれるデータの数値表現で、データのセマンティック検索に使用できます。

このレッスンでは、私たちの教育スタートアップのための検索アプリケーションを構築します。私たちのスタートアップは、発展途上国の学生に無料で教育を提供する非営利団体です。私たちのスタートアップは、生徒がAIについて学ぶために利用できるYouTubeの動画を数多く持っています。私たちのスタートアップは、学生が質問を入力してYouTube動画を検索できる検索アプリケーションを作りたいと考えています。

例えば、学生が「Jupyter Notebooksとは何ですか」や「Azure MLとは何ですか」と入力すると、検索アプリケーションはその質問に関連するYouTube動画のリストを返し、さらに良いことに、検索アプリケーションは動画の中で質問の答えがある場所へのリンクを返します。

## はじめに

このレッスンでは

- セマンティック検索とキーワード検索
- テキストエンベッディングとは何か。
- テキストエンベッディングインデックスの作成。
- テキストエンベッディングインデックスの検索。

## 学習目標

このレッスンを修了すると、次のことができるようになります：

- セマンティック検索とキーワード検索の違いを説明できる。
- テキストエンベッディングとは何かを説明できる。
- エンベッディングを使ってデータを検索するアプリケーションを作る。

## なぜ検索アプリケーションを作るのか？

検索アプリケーションを作成することで、エンベッディングを使ってデータを検索する方法を理解することができます。また、生徒が情報をすばやく見つけるために使用できる検索アプリケーションを構築する方法を学びます。

このレッスンには、Microsoft [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1?WT.mc_id=academic-105485-koreyst) YouTube チャンネルの YouTube トランスクリプトの埋め込みインデックスが含まれています。AI Showは、AIと機械学習について教えるYouTubeチャンネルです。埋め込みインデックスには、2023年10月までのYouTubeトランスクリプトのエンベッディングが含まれています。あなたは、エンベッディング・インデックスを使用して、私たちのスタートアップのための検索アプリケーションを構築します。検索アプリケーションは、質問に対する答えがあるビデオ内の場所へのリンクを返します。これは、生徒が必要な情報を素早く見つけるための素晴らしい方法です。

以下は、「azure mlでrstudioを使えますか」という質問に対するセマンティッククエリの例です。YouTubeのURLを確認してください。URLにはタイムスタンプが含まれており、質問の答えがあるビデオの場所に移動できることがわかります。

![「Azure MLでrstudioを使えるか」という質問に対するセマンティッククエリ](../../images/query-results.png?WT.mc_id=academic-105485-koreyst)

## セマンティック検索とは？

セマンティック検索とは何だろう？セマンティック検索とは、クエリに含まれる単語の意味（セマンティクス）を使って関連する結果を返す検索テクニックです。

セマンティック検索の例を挙げましょう。セマンティック検索は、あなたが車について「夢見ている」のではなく、「理想の車」を探していることを理解します。セマンティック検索はあなたの意図を理解し、適切な結果を返します。一方、キーワード検索は文字通り車に関する夢を検索するもので、しばしば無関係な結果を返します。

## エンベッディングとは？

[エンベッディング](https://en.wikipedia.org/wiki/Word_embedding?WT.mc_id=academic-105485-koreyst)は、[自然言語処理](https://en.wikipedia.org/wiki/Natural_language_processing?WT.mc_id=academic-105485-koreyst)で使われるテキスト表現手法です。エンベッディングはテキストの意味的な数値表現です。エンベッディングは、機械が理解しやすいようにデータを表現するために使われます。 テキストエンベッディングを構築するためのモデルはたくさんありますが、このレッスンでは、OpenAIのエンベッディングモデルを使ってエンベッディングを生成することに焦点を当てます。

以下のテキストは、AI Show YouTubeチャンネルのエピソードの1つからのトランスクリプトです：

```text
今日はAzure Machine Learningについて学びます。
```

このテキストをOpenAIのエンベッディングAPIに渡すと、1536個の数字からなるエンベッディングが返される。ベクトル内の各数値は、テキストの異なる側面を表しています。簡潔にするために、ベクター内の最初の10個の数字を示します。

```python
[-0.006655829958617687, 0.0026128944009542465, 0.008792596869170666, -0.02446001023054123, -0.008540431968867779, 0.022071078419685364, -0.010703742504119873, 0.003311325330287218, -0.011632772162556648, -0.02187200076878071, ...]
```

## エンベッディングインデックスはどのように作成されていますか？

このレッスンのエンベッディングインデックスは、一連のPythonスクリプトで作成されています。スクリプトは、このレッスンの`scripts`フォルダー内の[README](../../scripts/README.md)に説明があります。エンベッディング・インデックスはあなたのために用意されているので、このレッスンを完了するためにこれらのスクリプトを実行する必要はありません。

スクリプトは以下の操作を行います：

1. [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1?WT.mc_id=academic-105485-koreyst)プレイリストの各 YouTube ビデオのトランスクリプトがダウンロードされます。
2. [OpenAI Functions](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling)を使って、YouTubeのトランスクリプトの最初の3分間から発言者名を抽出します。各動画の話者名は`embedding_index_3m.json`というエンベッディング・インデックスに格納される。
3. トランスクリプトのテキストは、**3分のテキストセグメント**にチャンクされる。セグメントには、次のセグメントと重なる約20語が含まれ、セグメントのエンベッディングが切断されないようにし、より良い検索コンテキストを提供します。
4. 各テキストセグメントは、OpenAI Chat API に渡され、テキストを 60 単語に要約します。要約はエンベッディングインデックス `embedding_index_3m.json` にも格納される。
5. 最後に、セグメントテキストはOpenAIのエンベッディングAPIに渡される。エンベッディング API は、セグメントのセマンティックな意味を表す 1536 個の数値からなるベクトルを返す。セグメントとOpenAIのエンベッディングベクターは、エンベッディングインデックス `embedding_index_3m.json` に格納される。

### ベクターデータベース

レッスンを簡単にするために、埋め込みインデックスは `embedding_index_3m.json` という名前のJSONファイルに格納され、Pandas Dataframeにロードされる。しかし、本番では、エンベッディングインデックスは、[Azure Cognitive Search](https://learn.microsoft.com/training/modules/improve-search-results-vector-search?WT.mc_id=academic-105485-koreyst), [Redis](https://cookbook.openai.com/examples/vector_databases/redis/readme?WT.mc_id=academic-105485-koreyst), [Pinecone](https://cookbook.openai.com/examples/vector_databases/pinecone/readme?WT.mc_id=academic-105485-koreyst), [Weaviate](https://cookbook.openai.com/examples/vector_databases/weaviate/readme?WT.mc_id=academic-105485-koreyst) のようなベクトルデータベースに格納されるでしょう。

## コサイン類似度を理解する

テキストエンベッディングについて学びました。次のステップは、テキストエンベッディングを使ってデータを検索する方法、特に余弦類似度を用いて与えられたクエリと最も類似したエンベッディングを見つける方法を学ぶことです。

### コサイン類似度とは？

コサイン類似度は2つのベクトル間の類似度のメジャーで、「最近傍探索」とも呼ばれます。コサイン類似度検索を行うには、OpenAIのエンベッディングAPIを使ってクエリテキストをベクトル化する必要があります。次に、クエリのベクトルとエンベッディングインデックスの各ベクトルのコサイン類似度を計算します。エンベッディングインデックスは、YouTubeのトランスクリプトのテキストセグメントごとにベクトルを持っていることを覚えておいてください。最後に、コサイン類似度で結果をソートし、コサイン類似度が最も高いテキストセグメントが、クエリと最も類似していることになります。

数学的な観点から、余弦類似度は多次元空間に投影された2つのベクトル間の角度の余弦をメジャーします。このメジャーは有益で、2つのドキュメントがサイズの関係でユークリッド距離で離れていても、それらの間の角度は小さく、したがってコサイン類似度は高くなります。余弦類似度方程式についての詳細は、[余弦類似度](https://en.wikipedia.org/wiki/Cosine_similarity?WT.mc_id=academic-105485-koreyst)を参照してください。

## 最初の検索アプリケーションを作る

次に、エンベッディングを使った検索アプリケーションの作り方を学びます。この検索アプリケーションでは、学生が質問を入力してビデオを検索できるようにします。検索アプリケーションは、質問に関連するビデオのリストを返します。検索アプリケーションはまた、質問の答えがあるビデオの場所へのリンクを返します。

このソリューションは、Python 3.10以降を使用して、Windows 11、macOS、Ubuntu 22.04でビルドおよびテストされました。Pythonは[python.org](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)からダウンロードできます。

## 課題 - 検索アプリケーションの構築、学生を可能にするために

このレッスンの最初にスタートアップを紹介しました。今度は、学生が評価のために検索アプリケーションを構築できるようにする番です。

この課題では、検索アプリケーションを構築するために使用するAzure OpenAIサービスを作成します。以下の Azure OpenAI Services を作成します。この課題を完了するには、Azure サブスクリプションが必要です。

### Azure Cloud Shell を起動します。

1. [Azure ポータル](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) にサインインします。
2. Azure ポータルの右上にある Cloud Shell アイコンを選択します。
3. 環境タイプに **Bash** を選択します。

#### リソースグループの作成

> ここでは、East USの "semantic-video-search "というリソースグループを使用します。
> リソースグループの名前は変更できますが、リソースの場所を変更する場合は、[モデル利用可能テーブル]を確認してください、
> [モデル利用可能テーブル](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst)を確認してください。

```shell
az group create --name semantic-video-search --location eastus
```

#### Azure OpenAI Service リソースの作成

Azure Cloud Shell から以下のコマンドを実行して、Azure OpenAI Service リソースを作成します。

```shell
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

#### このアプリケーションで使用するエンドポイントとキーを取得する

Azure Cloud Shell から以下のコマンドを実行して、Azure OpenAI Service リソースのエンドポイントとキーを取得します。

```shell
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

#### OpenAI エンベッディングモデルのデプロイ

Azure Cloud Shell から、以下のコマンドを実行して、OpenAI Embedding モデルをデプロイします。

```shell
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name text-embedding-ada-002 \
    --model-name text-embedding-ada-002 \
    --model-version "2"  \
    --model-format OpenAI \
    --scale-settings-scale-type "Standard"
```

## ソリューション

GitHub Codespacesで[solution notebook](../../solution.ipynb?WT.mc_id=academic-105485-koreyst)を開き、Jupyter Notebookの指示に従ってください。

ノートブックを実行すると、クエリーを入力するよう促されます。入力ボックスは以下のようになります：

![クエリを入力する入力ボックス](../../images/notebook-search.png?WT.mc_id=academic-105485-koreyst)

## 素晴らしい仕事！学習を続ける 

このレッスンを終えたら、[生成AI学習コレクション](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)をチェックして、生成AI知識のレベルアップを続けましょう！

レッスン9では、[画像生成アプリケーションの構築](../../../09-building-image-applications/translations/ja/README.md)の方法を見ていきます！
