# 検索アプリケーションの構築

[![Introduction to Generative AI and Large Language Models](../../images/08-lesson-banner.png?WT.mc_id=academic-105485-yoterada)](https://aka.ms/gen-ai-lesson8-gh?WT.mc_id=academic-105485-koreyst)

LLM は、チャットボットやテキスト生成だけでなく、Embeddings を使った検索アプリケーションの実装も可能です。Embeddings とは、ベクトルと呼ばれるデータの数値表現で、データのセマンティック検索に活用できます。

今回のレッスンでは、教育スタートアップ向けの検索アプリケーションを作ります。スタートアップは、発展途上国の学生に無料教育を提供する非営利団体で、AI について学べる多数の YouTube ビデオを提供しています。そして今、学生が質問を入力するだけで YouTube 動画を検索できるアプリケーションの開発を行う予定です。

例えば、学生が「Jupyter Notebook とは何ですか？」や「Azure ML とは何ですか？」と質問すると、その質問に関連する YouTube 動画のリストを返します。さらに、その質問の回答が動画のどの部分にあるのかを示すリンクも示します。

## はじめに

このレッスンでは、下記の内容について説明します。

- セマンティック検索とキーワード検索の違い
- テキスト埋め込みとは何か
- テキスト埋め込みインデックスの作成方法
- テキスト埋め込みインデックスの検索方法

## 学習目標

このレッスンを修了すると、下記を理解できます：

- セマンティック検索とキーワード検索の違いを理解し、説明できる
- テキスト埋め込みとは何かを理解し、説明できる
- データ検索に Embeddings を使用したアプリケーションを作成できる

## なぜ検索アプリケーションを作るのでしょうか？

実際に検索アプリケーションを作成すると、Embeddings を使用したデータの検索技術を習得できます。また、学生が情報を素早く見つけるための検索アプリケーションの作り方も学べます。

このレッスンでは、Microsoft の [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1?WT.mc_id=academic-105485-yoterada) という YouTube チャンネルから、YouTube の字幕を抜き出し、それを Embedding 検索用のインデックスとして利用する方法について紹介します。AI Show は、AI と機械学習について学べる YouTube チャンネルです。Embedding 用のインデックスは、2023 年 10 月までの各 YouTube にアップロードされた動画の字幕を含めています。この Embedding インデックスを使用して、スタートアップ用の検索アプリケーションを作ります。この検索アプリケーションは、質問の答えが動画のどの部分にあるかを示すリンクも返します。これは、学生が必要な情報を素早く見つけるのに非常に役立ちます。

下記は、「Azure ML で rstudio を使えますか？」という質問に対するセマンティック・クエリの例です。YouTube の URL を見てみると、URL には質問の答えがどの動画のどの部分にあるかを示すタイムスタンプが含まれています。

![Semantic query for the question "can you use rstudio with Azure ML"](../../images/query-results.png?WT.mc_id=academic-105485-yoterada)

## セマンティック検索とは何でしょうか？

セマンティック検索とは、検索クエリ内の単語の意味、つまりセマンティクスを利用して、関連性のある結果を返す検索手法を指します。

セマンティック検索の一例を挙げてみましょう。あなたが車を購入したいと考えている場合、「私が将来乗りたい夢の車」を検索したとします。この場合、セマンティック検索は、あなたが車について「夢」見ているわけではなく、「理想の車」を購入したいという意図を理解します。そして、その意図に関連する結果を返します。これに対して、「キーワード検索」は文字通りに車についての夢を検索し、結果として関連性のない情報を返す確立が高くなります。

## テキスト埋め込み (Embeddings) とは何でしょうか？

[テキストの埋め込み (Embeddings)](https://en.wikipedia.org/wiki/Word_embedding?WT.mc_id=academic-105485-yoterada) は、[自然言語処理](https://en.wikipedia.org/wiki/Natural_language_processing?WT.mc_id=academic-105485-yoterada)において用いられるテキストの表現方法で、テキストの意味を数値表現したものです。この埋め込みは、機械が理解しやすいように数値データとして表現するために使用します。テキスト埋め込みを生成するための AI モデルは多数存在しますが、今回のレッスンでは OpenAI が提供する埋め込みモデルを使用し、埋め込みの作成方法も学びます。

ここで一例を挙げます。たとえば、AI Show の YouTube チャンネルのエピソードの一部を文字起こししたテキストがあるとします。

```text
今日は、Azure Machine Learning について学習します。
```

このテキストを OpenAI の埋め込み API に渡すと、1536 個の数値ベクトルとして埋め込みデータが返ってきます。このベクトルの各数値は、テキストの異なる側面を表現しています。簡単に理解できるように、ベクトルの最初の 10 個の数値を以下に示します。

```text
[
-0.006655829958617687, 0.0026128944009542465,
0.008792596869170666, -0.02446001023054123,
-0.008540431968867779, 0.022071078419685364,
-0.010703742504119873, 0.003311325330287218,　
-0.011632772162556648, -0.02187200076878071,
...
]
```

## 埋め込みインデックスはどのようにして作成するのでしょうか？

このレッスンの埋め込みインデックスは、Python スクリプトを用いて作成しました。スクリプトとその使用方法は、このレッスンの `scripts` フォルダ内の [README](../../scripts/README.md?WT.mc_id=academic-105485-yoterada) に記載しています。埋め込みインデックスはすでに提供されているので、このレッスンを完了するためにこれらのスクリプトを実行する必要はありません。

スクリプト内部では下記の操作を行っています：

1. [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1?WT.mc_id=academic-105485-yoterada) プレイリスト中の各 YouTube 動画の字幕をダウンロードします。
2. [OpenAI の Function Calling](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling?WT.mc_id=academic-105485-yoterada) を使用して、YouTube 字幕の最初から 3 分で発表者の名前を抽出します。各動画の発表者の名前は、`embedding_index_3m.json` という名前の埋め込みインデックスに保存します。
3. その後、字幕テキストは「**3 分間のテキストブロック**」に分割します。各ブロックには、次のブロックから約 20 語を重複して含め、各ブロックの埋め込みが途切れないように、より良い検索コンテキストを提供します。
4. 各テキストブロックを OpenAI の Chat API に渡し、テキストを 60 語に要約します。この要約結果も `embedding_index_3m.json` という埋め込みインデックスに保存します。
5. 最後に、テキストブロックの内容を OpenAI の埋め込み API に渡します。埋め込み API は、ブロックの意味を表現する 1536 個の数値からなるベクトルを返します。テキストブロックと OpenAI の埋め込みベクトルは、`embedding_index_3m.json` という埋め込みインデックスに保存します。

### ベクトル・データベース

今回レッスンをかんたんに進めるため、埋め込みインデックスは `embedding_index_3m.json` という名前の JSON ファイルに保存し、Pandas のデータフレームに読み込みます。しかし、実際の運用環境では、埋め込みインデックスは [Azure AI Search](https://learn.microsoft.com/training/modules/improve-search-results-vector-search?WT.mc_id=academic-105485-yoterada)、[Redis](https://cookbook.openai.com/examples/vector_databases/redis/readme?WT.mc_id=academic-105485-yoterada)、[Pinecone](https://cookbook.openai.com/examples/vector_databases/pinecone/readme?WT.mc_id=academic-105485-yoterada)、[Weaviate](https://cookbook.openai.com/examples/vector_databases/weaviate/readme?WT.mc_id=academic-105485-yoterada) などのベクトル・データベースに保存します。

## コサイン類似度について理解しましょう

テキストの埋め込みについて学んだので、次にテキストの埋め込みを使ってデータを検索します。特にコサイン類似度を使って特定の問い合わせに対して最も類似した埋め込みを見つける方法を学びます。

### コサイン類似度とは何でしょうか？

コサイン類似度は、2 つのベクトル間の類似性を測る指標で、これは「最近傍検索」とも呼ばれます。コサイン類似度検索を行うためには、まず OpenAI の埋め込み API を使って、ユーザから問い合わせされたテキストをベクトル化します。次に、問い合わせされたベクトルと、埋め込みインデックス内の各ベクトルとのコサイン類似度を計算します。埋め込みインデックスには、YouTube の字幕テキストブロックごとにベクトルが存在します。最後に、結果をコサイン類似度でソートします。コサイン類似度が最も高いテキストブロックが、問い合わせされた内容に最も近い内容を表しています。

数学的な観点から見ると、コサイン類似度は多次元空間に投影された 2 つのベクトル間の角度のコサインを測定します。この測定は有益で、2 つのドキュメントが大きさのためにユークリッド距離で離れていても、それらの間の角度が小さいため、コサイン類似度が高くなる可能性があります。コサイン類似度の方程式についての詳細は、[コサイン類似度](https://en.wikipedia.org/wiki/Cosine_similarity?WT.mc_id=academic-105485-yoterada)をご覧ください。

> [!TIP]
> 訳者追記  
> 訳者が日本語で説明している下記の記事もどうぞ参考にご覧ください。
> [Azure OpenAI Embedding モデルを利用し最も関連性の高いドキュメントを見つける方法](https://qiita.com/yoshioterada/items/3e575828368bf3767532)

## 初めての検索アプリケーションの構築

次に、埋め込みを使って検索アプリケーションを実装する方法を学びます。この検索アプリケーションでは、学生が質問を入力してビデオを検索できます。検索アプリケーションは、質問に関連するビデオのリストを返します。さらに、質問に対する回答を含むビデオへのリンクも返します。

このソリューションは、Python 3.10 以上を使用して Windows 11、macOS、Ubuntu 22.04 で作成・テストしました。Python は [python.org](https://www.python.org/downloads/?WT.mc_id=academic-105485-yoterada) からダウンロードできます。

## 課題 - 学生向けの検索アプリケーションを作る

このレッスンの初めにスタートアップについて紹介しました。そしてこれから、学生が自分たちの評価を検索できるアプリケーションを作ります。

この課題では、検索アプリケーションを作るために Azure OpenAI Services を利用します。下記のように Azure OpenAI Services を作成します。この課題を完了するためには、Azure サブスクリプションが事前に必要です。

### Azure Cloud Shell 　の起動

1. [Azure portal](https://portal.azure.com/?WT.mc_id=academic-105485-yoterada) にサインインします
2. Azure portal の右上隅にある Cloud Shell アイコンを選択します
3. 環境の種類として**Bash**を選択します

#### リソースグループを作成する

> この手順では、米国東部に "semantic-video-search" という名前のリソースグループを作成し使用します。
> リソースグループの名前は変更可能ですが、リソースの場所を変更する場合は、
> [モデルの可用性](https://aka.ms/oai/models?WT.mc_id=academic-105485-yoterada)から対象リージョンで利用可能かご確認ください。

> [!TIP]
> 訳者追記  
> 日本では jaapneast のリージョンで OpenAI の text-embedding-ada-002, gpt-35-turbo-0613 のモデルが利用可能です。仮に japaneast で利用できない場合は、他のリージョンで作成してください。

```shell
az group create --name semantic-video-search --location eastus
```

#### Azure OpenAI Service リソースを作成する

Azure Cloud Shell から、下記のコマンドを実行して Azure OpenAI Service リソースを作成します。

```shell
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

#### アプリケーションで使用するためのエンドポイントとキーを取得する

Azure Cloud Shell から、下記のコマンドを実行して Azure OpenAI Service リソースのエンドポイントとキーを取得します。

```shell
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

#### OpenAI Embedding モデルをデプロイする

Azure Cloud Shell から、下記のコマンドを実行して OpenAI Embedding モデルをデプロイします。

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

## 解決策

GitHub Codespaces で[ソリューションのノートブック](../../python/aoai-solution.ipynb?WT.mc_id=academic-105485-yoterada)を開き、Jupyter Notebook の指示に従ってください。

ノートブックを実行すると、質問内容を入力するように求められます。入力ボックスは次のように表示されます。

![Input box for the user to input a query](../../images/notebook-search.png?WT.mc_id=academic-105485-yoterada)

## お疲れ様でした!　学習を続ける

このレッスン修了後、[生成 AI 学習コレクション](https://aka.ms/genai-collection?WT.mc_id=academic-105485-yoterada) をチェックして、Generative AI の知識をレベルアップさせましょう。

次のレッスン 9 では、[画像生成アプリケーションの構築](../../../09-building-image-applications/translations/ja-jp/README.md?WT.mc_id=academic-105485-yoterada)方法について学びます！
