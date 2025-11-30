<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-17T23:51:59+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ja"
}
-->
# このコースの始め方

このコースを始めて、生成AIを使ってどんなものを作りたくなるかを楽しみにしています！

成功を確実にするために、このページではセットアップ手順、技術的要件、必要に応じてどこで助けを得られるかを説明します。

## セットアップ手順

このコースを始めるには、以下の手順を完了する必要があります。

### 1. このリポジトリをフォークする

[このリポジトリ全体をフォーク](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)して、自分のGitHubアカウントにコピーしてください。これによりコードを変更したり、課題を完了したりすることができます。また、[このリポジトリをスター (🌟) にする](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)ことで、簡単に見つけたり関連するリポジトリを探したりすることができます。

### 2. Codespaceを作成する

コードを実行する際の依存関係の問題を避けるために、このコースを[GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)で実行することをお勧めします。

フォークしたリポジトリで: **Code -> Codespaces -> New on main**

![Codespaceを作成するボタンを表示するダイアログ](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 シークレットを追加する

1. ⚙️ ギアアイコン -> コマンドパレット -> Codespaces : Manage user secret -> 新しいシークレットを追加。
2. 名前をOPENAI_API_KEYに設定し、キーを貼り付けて保存。

### 3. 次に何をする？

| やりたいこと         | 移動先                                                                 |
|---------------------|-------------------------------------------------------------------------|
| レッスン1を始める   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| オフラインで作業する | [`setup-local.md`](02-setup-local.md)                                   |
| LLMプロバイダーを設定する | [`providers.md`](03-providers.md)                                        |
| 他の学習者と交流する | [Discordに参加する](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## トラブルシューティング

| 症状                                     | 解決策                                                           |
|------------------------------------------|------------------------------------------------------------------|
| コンテナのビルドが10分以上かかる          | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`              | ターミナルが接続されていない; **+** ➜ *bash* をクリック          |
| OpenAIから`401 Unauthorized`             | 間違った/期限切れの`OPENAI_API_KEY`                              |
| VS Codeが「Dev container mounting…」を表示 | ブラウザタブを更新—Codespacesが接続を失うことがあります          |
| ノートブックのカーネルが見つからない      | ノートブックメニュー ➜ **Kernel ▸ Select Kernel ▸ Python 3**     |

   Unix系システム:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env`ファイルを編集する**: `.env`ファイルをテキストエディタ（例: VS Code、Notepad++など）で開き、以下の行を追加します。`your_github_token_here`を実際のGitHubトークンに置き換えてください。

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **ファイルを保存する**: 変更を保存し、テキストエディタを閉じます。

5. **`python-dotenv`をインストールする**: まだインストールしていない場合は、`.env`ファイルからPythonアプリケーションに環境変数を読み込むために`python-dotenv`パッケージをインストールする必要があります。`pip`を使用してインストールできます:

   ```bash
   pip install python-dotenv
   ```

6. **Pythonスクリプトで環境変数を読み込む**: Pythonスクリプト内で`python-dotenv`パッケージを使用して`.env`ファイルから環境変数を読み込みます:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

これで完了です！`.env`ファイルを作成し、GitHubトークンを追加し、それをPythonアプリケーションに読み込むことができました。

## コンピュータでローカルに実行する方法

コードをコンピュータでローカルに実行するには、[Pythonのバージョン](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)をインストールする必要があります。

その後、リポジトリを使用するには、クローンする必要があります:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

すべてチェックアウトしたら、すぐに始められます！

## オプションの手順

### Minicondaのインストール

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst)は、[Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python、およびいくつかのパッケージをインストールするための軽量インストーラーです。
Conda自体はパッケージマネージャーであり、異なるPythonの[**仮想環境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)やパッケージを簡単にセットアップおよび切り替えることができます。また、`pip`では利用できないパッケージをインストールする際にも便利です。

[MiniCondaインストールガイド](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst)に従ってセットアップしてください。

Minicondaをインストールしたら、[リポジトリ](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)をクローンする必要があります（まだしていない場合）。

次に、仮想環境を作成する必要があります。Condaを使用してこれを行うには、新しい環境ファイル（_environment.yml_）を作成してください。Codespacesを使用している場合は、`.devcontainer`ディレクトリ内にこれを作成し、`.devcontainer/environment.yml`とします。

以下のスニペットで環境ファイルを埋めてください:

```yml
name: <environment-name>
channels:
  - defaults
  - microsoft
dependencies:
  - python=<python-version>
  - openai
  - python-dotenv
  - pip
  - pip:
      - azure-ai-ml
```

Condaでエラーが発生する場合は、以下のコマンドをターミナルで実行してMicrosoft AIライブラリを手動でインストールできます。

```
conda install -c microsoft azure-ai-ml
```

環境ファイルは必要な依存関係を指定します。`<environment-name>`はConda環境に使用したい名前を指し、`<python-version>`は使用したいPythonのバージョンを指します。例えば、`3`はPythonの最新のメジャーバージョンです。

これが完了したら、以下のコマンドをコマンドライン/ターミナルで実行してConda環境を作成できます。

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

問題が発生した場合は、[Conda環境ガイド](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)を参照してください。

### Pythonサポート拡張機能を備えたVisual Studio Codeの使用

このコースでは、[Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst)エディタと[Pythonサポート拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)を使用することをお勧めします。ただし、これは推奨であり、必須ではありません。

> **Note**: コースリポジトリをVS Codeで開くことで、プロジェクトをコンテナ内でセットアップするオプションがあります。これは、コースリポジトリ内にある[特別な`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)ディレクトリのおかげです。詳細は後述します。

> **Note**: リポジトリをクローンしてVS Codeでディレクトリを開くと、Pythonサポート拡張機能をインストールするように自動的に提案されます。

> **Note**: VS Codeがリポジトリをコンテナ内で再オープンすることを提案した場合、ローカルにインストールされたPythonバージョンを使用するためにこのリクエストを拒否してください。

### ブラウザでJupyterを使用する

[ブラウザ内でJupyter環境](https://jupyter.org?WT.mc_id=academic-105485-koreyst)を使用してプロジェクトに取り組むこともできます。クラシックJupyterや[Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst)は、オートコンプリートやコードハイライトなどの機能を備えた快適な開発環境を提供します。

Jupyterをローカルで開始するには、ターミナル/コマンドラインに移動し、コースディレクトリに移動して以下を実行してください:

```bash
jupyter notebook
```

または

```bash
jupyterhub
```

これによりJupyterインスタンスが開始され、アクセスするためのURLがコマンドラインウィンドウに表示されます。

URLにアクセスすると、コースの概要が表示され、任意の`*.ipynb`ファイルに移動できるようになります。例えば、`08-building-search-applications/python/oai-solution.ipynb`。

### コンテナでの実行

コンピュータやCodespaceでのセットアップの代わりに、[コンテナ](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)を使用することもできます。コースリポジトリ内の特別な`.devcontainer`フォルダにより、VS Codeでプロジェクトをコンテナ内にセットアップすることが可能です。Codespaces以外ではDockerのインストールが必要で、少し手間がかかるため、コンテナの使用経験がある方にのみお勧めします。

GitHub Codespacesを使用する際にAPIキーを安全に保つ最良の方法の1つは、Codespace Secretsを使用することです。[Codespacesのシークレット管理](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst)ガイドに従って詳細を学んでください。

## レッスンと技術的要件

このコースには6つの概念レッスンと6つのコーディングレッスンがあります。

コーディングレッスンではAzure OpenAI Serviceを使用します。このコードを実行するには、Azure OpenAI ServiceへのアクセスとAPIキーが必要です。[この申請書を記入](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)してアクセスを申請できます。

申請が処理されるのを待つ間、各コーディングレッスンにはコードと出力を確認できる`README.md`ファイルが含まれています。

## 初めてAzure OpenAI Serviceを使用する場合

初めてAzure OpenAI Serviceを使用する場合は、[Azure OpenAI Serviceリソースを作成してデプロイする方法](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)に関するガイドに従ってください。

## 初めてOpenAI APIを使用する場合

初めてOpenAI APIを使用する場合は、[インターフェースを作成して使用する方法](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)に関するガイドに従ってください。

## 他の学習者と交流する

公式の[AIコミュニティDiscordサーバー](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)にチャンネルを作成しました。他の学習者と出会う素晴らしい方法です。同じ志を持つ起業家、開発者、学生、生成AIのスキルを向上させたい人々とネットワークを築くことができます。

[![Discordチャンネルに参加する](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

プロジェクトチームもこのDiscordサーバーに参加して、学習者をサポートします。

## 貢献する

このコースはオープンソースの取り組みです。改善点や問題があれば、[プルリクエストを作成](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)するか、[GitHubの問題を報告](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)してください。

プロジェクトチームはすべての貢献を追跡します。オープンソースに貢献することは、生成AI分野でのキャリアを築く素晴らしい方法です。

ほとんどの貢献には、寄稿者ライセンス契約（CLA）に同意する必要があります。これにより、寄稿者が寄稿する権利を持ち、実際に寄稿を使用する権利を付与することを宣言します。詳細については、[CLA、寄稿者ライセンス契約のウェブサイト](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)をご覧ください。

プルリクエストを送信すると、CLAボットが自動的にCLAを提供する必要があるかどうかを判断し、適切にPRを装飾します（例: ラベル、コメント）。ボットが提供する指示に従うだけで、すべてのリポジトリでこれを一度だけ行う必要があります。

このプロジェクトは[Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)を採用しています。詳細については、Code of Conduct FAQを読むか、[Email opencode](opencode@microsoft.com)に追加の質問やコメントを送信してください。

## さあ、始めましょう！
このコースを完了するために必要なステップを終えたので、[生成AIとLLMの紹介](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)から始めましょう。

---

**免責事項**:  
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。