# 検索アプリケーションの構築

[![生成AIと大規模言語モデルの紹介](../../../translated_images/08-lesson-banner.png?WT.38007baa37b3809836fefd9caf72cba7434d1d1e82074d170c2b066e3c7aa2d0.ja.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson8-gh?WT.mc_id=academic-105485-koreyst)

> > _このレッスンのビデオを見るには、上の画像をクリックしてください_

LLMにはチャットボットやテキスト生成以上の可能性があります。埋め込みを使って検索アプリケーションを構築することも可能です。埋め込みはベクトルとも呼ばれるデータの数値表現であり、データのセマンティック検索に使用できます。

このレッスンでは、私たちの教育スタートアップのために検索アプリケーションを構築します。私たちのスタートアップは、発展途上国の学生に無料で教育を提供する非営利団体です。AIについて学ぶために学生が利用できるYouTube動画が多数あります。学生が質問を入力してYouTube動画を検索できる検索アプリケーションを構築したいと考えています。

例えば、学生が「Jupyter Notebookとは？」や「Azure MLとは？」と入力すると、検索アプリケーションはその質問に関連するYouTube動画のリストを返し、さらにその質問の答えが動画のどこにあるかへのリンクも返します。

## はじめに

このレッスンでは、以下をカバーします：

- セマンティック検索 vs キーワード検索
- テキスト埋め込みとは何か
- テキスト埋め込みインデックスの作成
- テキスト埋め込みインデックスの検索

## 学習目標

このレッスンを完了すると、以下ができるようになります：

- セマンティック検索とキーワード検索の違いを説明する
- テキスト埋め込みが何であるかを説明する
- 埋め込みを使用してデータを検索するアプリケーションを作成する

## なぜ検索アプリケーションを構築するのか？

検索アプリケーションを作成することで、埋め込みを使用してデータを検索する方法を理解できます。また、学生が情報を迅速に見つけるための検索アプリケーションを構築する方法も学べます。

このレッスンには、Microsoft [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) YouTubeチャンネルのYouTubeトランスクリプトの埋め込みインデックスが含まれています。AI ShowはAIと機械学習について教えてくれるYouTubeチャンネルです。埋め込みインデックスには2023年10月までの各YouTubeトランスクリプトの埋め込みが含まれています。この埋め込みインデックスを使用して、私たちのスタートアップのための検索アプリケーションを構築します。検索アプリケーションは、質問の答えが動画のどこにあるかへのリンクを返します。これは学生が必要な情報を迅速に見つけるための素晴らしい方法です。

以下は「Azure MLでrstudioを使うことができますか？」という質問に対するセマンティッククエリの例です。YouTubeのURLを確認すると、質問の答えが動画のどこにあるかを示すタイムスタンプが含まれていることがわかります。

![質問「Azure MLでrstudioを使うことができますか？」のセマンティッククエリ](../../../translated_images/query-results.png?WT.c2bcab091b108e899efca56b2cd996ea8f95145c049888f52ef7495a2b7df665.ja.mc_id=academic-105485-koreyst)

## セマンティック検索とは何か？

では、セマンティック検索とは何でしょうか？セマンティック検索は、クエリ内の単語の意味を使用して関連する結果を返す検索技術です。

ここにセマンティック検索の例があります。車を購入したいと考えているとしましょう。「私の夢の車」と検索すると、セマンティック検索は車についての`dreaming`ではなく、むしろあなたが`ideal`車を購入しようとしていることを理解します。セマンティック検索はあなたの意図を理解し、関連する結果を返します。これに対して`keyword search`は、車についての夢を文字通りに検索し、しばしば関連性のない結果を返します。

## テキスト埋め込みとは何か？

[テキスト埋め込み](https://en.wikipedia.org/wiki/Word_embedding?WT.mc_id=academic-105485-koreyst)は、[自然言語処理](https://en.wikipedia.org/wiki/Natural_language_processing?WT.mc_id=academic-105485-koreyst)で使用されるテキスト表現技術です。テキスト埋め込みは、テキストのセマンティックな数値表現です。埋め込みは、機械が理解しやすい方法でデータを表現するために使用されます。テキスト埋め込みを構築するためのモデルは多数ありますが、このレッスンではOpenAI埋め込みモデルを使用して埋め込みを生成することに焦点を当てます。

例えば、AI Show YouTubeチャンネルのエピソードのトランスクリプトに次のようなテキストがあるとします：

```text
Today we are going to learn about Azure Machine Learning.
```

このテキストをOpenAI埋め込みAPIに渡すと、1536の数値（ベクトルとして知られる）で構成される埋め込みが返されます。ベクトル内の各数値はテキストの異なる側面を表します。簡潔にするために、ベクトル内の最初の10個の数値を以下に示します。

```python
[-0.006655829958617687, 0.0026128944009542465, 0.008792596869170666, -0.02446001023054123, -0.008540431968867779, 0.022071078419685364, -0.010703742504119873, 0.003311325330287218, -0.011632772162556648, -0.02187200076878071, ...]
```

## 埋め込みインデックスはどのように作成されるのか？

このレッスンの埋め込みインデックスは、一連のPythonスクリプトで作成されました。スクリプトと手順は、'scripts'フォルダーの[README](./scripts/README.md?WT.mc_id=academic-105485-koreyst)にあります。このレッスンを完了するためにこれらのスクリプトを実行する必要はありません。埋め込みインデックスは提供されています。

スクリプトは以下の操作を行います：

1. [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1)プレイリスト内の各YouTube動画のトランスクリプトをダウンロードします。
2. [OpenAI Functions](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling?WT.mc_id=academic-105485-koreyst)を使用して、YouTubeトランスクリプトの最初の3分からスピーカー名を抽出しようとします。各動画のスピーカー名は`embedding_index_3m.json`という名前の埋め込みインデックスに保存されます。
3. トランスクリプトテキストは**3分のテキストセグメント**に分割されます。セグメントには次のセグメントから約20語が重複して含まれ、セグメントの埋め込みが切れないようにし、より良い検索コンテキストを提供します。
4. 各テキストセグメントはOpenAI Chat APIに渡され、60語に要約されます。この要約も`embedding_index_3m.json`に保存されます。
5. 最後に、セグメントテキストはOpenAI埋め込みAPIに渡されます。埋め込みAPIは、セグメントのセマンティックな意味を表す1536の数値で構成されたベクトルを返します。セグメントとOpenAI埋め込みベクトルは`embedding_index_3m.json`に保存されます。

### ベクトルデータベース

レッスンを簡単にするために、埋め込みインデックスは`embedding_index_3m.json`という名前のJSONファイルに保存され、Pandas DataFrameにロードされます。しかし、実運用では、埋め込みインデックスは[Azure Cognitive Search](https://learn.microsoft.com/training/modules/improve-search-results-vector-search?WT.mc_id=academic-105485-koreyst)、[Redis](https://cookbook.openai.com/examples/vector_databases/redis/readme?WT.mc_id=academic-105485-koreyst)、[Pinecone](https://cookbook.openai.com/examples/vector_databases/pinecone/readme?WT.mc_id=academic-105485-koreyst)、[Weaviate](https://cookbook.openai.com/examples/vector_databases/weaviate/readme?WT.mc_id=academic-105485-koreyst)などのベクトルデータベースに保存されます。

## コサイン類似性の理解

テキスト埋め込みについて学んだので、次のステップはテキスト埋め込みを使ってデータを検索し、特にコサイン類似性を使って与えられたクエリに最も類似した埋め込みを見つける方法を学ぶことです。

### コサイン類似性とは何か？

コサイン類似性は、2つのベクトル間の類似性を測定する方法であり、`nearest neighbor search`とも呼ばれます。コサイン類似性検索を行うには、OpenAI埋め込みAPIを使用して_クエリ_テキストを_ベクトル化_する必要があります。次に、クエリベクトルと埋め込みインデックス内の各ベクトルとの_コサイン類似性_を計算します。埋め込みインデックスには、各YouTubeトランスクリプトテキストセグメントのベクトルがあります。最後に、コサイン類似性で結果をソートし、コサイン類似性が最も高いテキストセグメントがクエリに最も類似しています。

数学的な観点から見ると、コサイン類似性は多次元空間に投影された2つのベクトル間の角度のコサインを測定します。この測定は有益であり、ユークリッド距離で離れている2つのドキュメントがサイズのために、まだそれらの間に小さな角度を持っている可能性があり、それゆえに高いコサイン類似性を持っている可能性があります。コサイン類似性の方程式に関する詳細情報は、[コサイン類似性](https://en.wikipedia.org/wiki/Cosine_similarity?WT.mc_id=academic-105485-koreyst)をご覧ください。

## 初めての検索アプリケーションの構築

次に、埋め込みを使用して検索アプリケーションを構築する方法を学びます。この検索アプリケーションでは、学生が質問を入力することで動画を検索できます。検索アプリケーションは、質問に関連する動画のリストを返します。また、質問の答えが動画のどこにあるかへのリンクも返します。

このソリューションは、Windows 11、macOS、Ubuntu 22.04でPython 3.10以降を使用して構築およびテストされました。Pythonは[python.org](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)からダウンロードできます。

## 課題 - 学生をサポートするための検索アプリケーションの構築

このレッスンの冒頭で私たちのスタートアップを紹介しました。今度は、学生が自分の評価のために検索アプリケーションを構築できるようにする時です。

この課題では、検索アプリケーションの構築に使用されるAzure OpenAIサービスを作成します。次のAzure OpenAIサービスを作成します。この課題を完了するには、Azureサブスクリプションが必要です。

### Azure Cloud Shellの開始

1. [Azureポータル](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst)にサインインします。
2. Azureポータルの右上隅にあるCloud Shellアイコンを選択します。
3. 環境タイプとして**Bash**を選択します。

#### リソースグループの作成

> これらの手順では、East USにある「semantic-video-search」という名前のリソースグループを使用しています。
> リソースグループの名前を変更することはできますが、リソースの場所を変更する際には、
> [モデルの可用性表](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst)を確認してください。

```shell
az group create --name semantic-video-search --location eastus
```

#### Azure OpenAIサービスリソースの作成

Azure Cloud Shellから次のコマンドを実行して、Azure OpenAIサービスリソースを作成します。

```shell
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

#### このアプリケーションで使用するエンドポイントとキーの取得

Azure Cloud Shellから次のコマンドを実行して、Azure OpenAIサービスリソースのエンドポイントとキーを取得します。

```shell
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

#### OpenAI埋め込みモデルのデプロイ

Azure Cloud Shellから次のコマンドを実行して、OpenAI埋め込みモデルをデプロイします。

```shell
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name text-embedding-ada-002 \
    --model-name text-embedding-ada-002 \
    --model-version "2"  \
    --model-format OpenAI \
    --sku-capacity 100 --sku-name "Standard"
```

## ソリューション

GitHub Codespacesで[ソリューションノートブック](../../../08-building-search-applications/python/aoai-solution.ipynb)を開き、Jupyterノートブックの指示に従ってください。

ノートブックを実行すると、クエリを入力するように促されます。入力ボックスは次のように見えます：

![ユーザーがクエリを入力するための入力ボックス](../../../translated_images/notebook-search.png?WT.2910e3d34815aab8d713050521ac5fcb2436defe66fed016f56b95867eb12fbd.ja.mc_id=academic-105485-koreyst)

## 素晴らしい仕事！学習を続けましょう

このレッスンを完了した後は、[生成AI学習コレクション](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)をチェックして、生成AIの知識をさらに深めましょう！

次のレッスン9では、[画像生成アプリケーションの構築](../09-building-image-applications/README.md?WT.mc_id=academic-105485-koreyst)について学びます！

**免責事項**:  
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを期しておりますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご承知おきください。原文の言語で書かれた文書が信頼できる情報源とみなされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤訳について、当社は責任を負いません。