# このコースを始めるにあたって

私たちは、あなたがこのコースを開始し、生成AIを使って何を作るかインスピレーションを得ることをとても楽しみにしています！

あなたの時間を有意義なものにするために、セットアップの手順、技術的な必要条件、助けが必要なときの方法をまとめたこのページを作成しました。

## セットアップステップ

このコースの受講を開始するには、以下のステップを完了する必要があります。

### 1. このリポジトリをフォークする

[このレポ全体をフォーク](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) して、自分の GitHub アカウントに移動し、コードを変更したり課題を完了したりできるようにします。また、[このレポにスター(🌟)を付ける](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)ことで、このレポや関連するレポを簡単に見つけることができます。

### 2. コードスペースの作成

コードを実行する際の依存関係の問題を避けるために、GitHubのコードスペースでこのコースを実行することをお勧めします。

これは、このリポジトリのフォークしたバージョンで `Code` オプションを選択し、**Codespaces** オプションを選択することで作成できます。

### 3. APIキーの保管

API キーを安全かつセキュアに保つことは、どのようなタイプのアプリケーションを構築する場合でも重要です。API キーを作業中のコードに直接保存しないことをお勧めします。これらの詳細を公開リポジトリにコミットすると、不要なコストや問題が発生する可能性があるからです。

コードスペースを作成するためのボタンを表示するダイアログ](./images/who-will-pay.webp)

## ローカルで実行する方法

あなたのコンピュータ上でローカルにコードを実行するには、何らかのバージョンの[Pythonがインストールされている](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)必要があります。

リポジトリを使用するには、リポジトリをクローンする必要があります：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

これで全てのチェックアウトが完了し、コードの学習と作業を開始できる。

### minicondaのインストール（オプションステップ）

**[miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst)** をインストールする利点があります - 異なるPython **仮想環境**用の `conda` パッケージマネージャをサポートする、かなり軽量なインストールです。`conda` を使えば、異なる Python のバージョンやパッケージのインストールや切り替えが簡単にでき、 `pip` 経由では利用できないパッケージのインストールも可能です。

miniconda をインストールした後、リポジトリをクローンし（まだクローンしていない場合）、このコースで使用する仮想環境を作成する必要があります：

以下のステップを実行する前に、最初に *environment.yml* ファイルがあることを確認してください。environment.yml*ファイルは必要な依存関係を持つconda環境を作成するために使用され、以下のようになります：

```yml
name: <environment-name>
channels:  
 - defaults
dependencies:  
- python=<python-version>  
- openai  
- python-dotenv
```

`<environment-name>`はcondaの環境名、`<python-version>`は使用するPythonのバージョンに置き換えてください。作成した *environment.yml* ファイルをリポジトリの *.devcontainer* フォルダーに置きます。

これで*environment.yml*ファイルが作成できたと思いますので、次のコマンドでconda環境を作成できます：


```bash
conda env create --name ai4beg --file .devcontainer/environment.yml
conda activate ai4beg
```

問題が発生した場合は、[conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) の作成について、このリンクを参照してください。

### Visual Studio Code と Python Extension を使う

カリキュラムを使用する最も良い方法は、[Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) を使って [Visual Studio Code](http://code.visualstudio.com) で開くことでしょう。

> **注意**：VS Codeでディレクトリをクローンして開くと、自動的にPythonの拡張機能をインストールするように指示されます。また、上記のようにminicondaをインストールする必要があります。

> **注意**： もし VS Code がコンテナでリポジトリを再度開くように提案したら、ローカルの Python インストールを使用するためにこれを拒否する必要があります。

### ブラウザでJupyterを使う

自分のコンピュータのブラウザからJupyter環境を使うこともできます。実際、古典的なJupyterもJupyer Hubも、オートコンプリートやコードハイライトなど、非常に便利な開発環境を提供しています。

ローカルでJupyterを起動するには、コースのディレクトリに移動して実行します：

```bash
jupyter notebook
```

or

```bash
jupyterhub
```

`.ipynb`ファイルに移動し、それらを開いて作業を開始することができる。

### コンテナ内での実行

Python をインストールする代わりに、コンテナでコードを実行することもできる。私たちのリポジトリには、このリポジトリ用のコンテナを構築する方法を指示する特別な `.devcontainer` フォルダーが含まれているので、VS Code はコンテナでコードを開き直すことを提案します。これはDockerのインストールが必要で、さらに複雑なので、経験豊富なユーザーにお勧めします。

GitHub Codespaces を使うときに API キーを安全に保つ最善の方法のひとつは、Codespace Secrets を使うことです。[コードスペースのシークレットを管理する](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) 方法については、こちらのガイドに従ってください。

## レッスンと技術要件

このコースには6つのコンセプトレッスンと6つのコーディングレッスンがあります。

コーディングレッスンでは、Azure OpenAI Serviceを使用します。このコードを実行するには、Azure OpenAIサービスへのアクセスとAPIキーが必要です。[このアプリケーションを完了](https://azure.microsoft.com/products/ai-services/openai-service/?WT.mc_id=academic-105485-koreyst)することで、アクセス権の取得を申請できます。

アプリケーションが処理されるのを待つ間、各コーディングレッスンにはコードと出力を見ることができる `README.md` ファイルも含まれています。

## 初めてAzure OpenAIサービスを使う場合

初めて Azure OpenAI サービスを使う場合は、このガイドに従って、[Azure OpenAI Service リソースの作成とデプロイ](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst?WT.mc_id=academic-105485-koreyst) を行ってください。

## 他の学習者に会う

他の学習者に会うために、公式の[AI Community Discordサーバー](https://aka.ms/genai-discord)にチャンネルを作りました。これは、志を同じくする起業家、ビルダー、学生、生成AIでレベルアップを目指す人たちとネットワークを作るのに最適な方法です。

[![ディスコード・チャンネルに参加する](https://dcbadge.vercel.app/api/server/ByRwuEEgH4?WT.mc_id=academic-105485-koreyst)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

プロジェクトチームもこのDiscordサーバーに参加し、学習者をサポートします。

## 貢献する

このコースはオープンソースの取り組みです。改善点や問題点があれば、[Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) を作成するか、[Github issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) を記録してください。

プロジェクトチームはすべての貢献を追跡し、オープンソースへの貢献は生成AIであなたのキャリアを構築する素晴らしい方法です。

ほとんどのコントリビューションでは、コントリビューター・ライセンス契約（CLA）に同意する必要があります。詳細は[CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)をご覧ください。

重要: このリポジトリのテキストを翻訳する場合、機械翻訳を使用しないようにしてください。私たちはコミュニティを通じて翻訳を検証しますので、あなたが精通している言語の翻訳にのみボランティアとして参加してください。

プルリクエストを提出すると、CLAボットが自動的にCLAを提供する必要があるかどうかを判断し、PRを適切に装飾します（ラベルやコメントなど）。ボットが提供する指示に従うだけです。この作業は、CLAを使用しているすべてのリポジトリで一度だけ行う必要があります。

このプロジェクトはマイクロソフトのオープンソース行動規範を採用しています。詳細については、行動規範FAQを読むか、追加の質問やコメントがあれば[Eメール opencode](opencode@microsoft.com)に連絡してください。

## 始めましょう

このコースを完了するために必要なステップを完了したので、[生成AIとLLMの紹介](../../../01-introduction-to-genai/translations/ja/README.md?WT.mc_id=academic-105485-koreyst)を入手して始めましょう。
