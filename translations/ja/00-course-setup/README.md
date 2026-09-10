# このコースのはじめに

このコースを始め、生成AIで何を作りたいかインスピレーションを受けることを私たちはとても楽しみにしています！

あなたの成功を確実にするために、このページではセットアップ手順、技術要件、必要に応じたサポートの入手先を説明しています。

## セットアップ手順

このコースを始めるには、以下の手順を完了する必要があります。

### 1. このリポジトリをフォークする

コードを変更したりチャレンジを完了するために、自分のGitHubアカウントに[このリポジトリ全体をフォーク](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)してください。また、[このリポジトリにスター（🌟）を付ける](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)と、関連するリポジトリも見つけやすくなります。

### 2. コードスペースを作成する

依存関係の問題を避けるために、このコースは[GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)で実行することを推奨します。

あなたのフォークで：**Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/ja/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 シークレットを追加する

1. ⚙️ 歯車アイコン -> コマンドパレット -> Codespaces : ユーザーシークレット管理 -> 新しいシークレットを追加。
2. 名前を OPENAI_API_KEY、あなたのキーを貼り付けて、保存。

### 3. 次に何をする？

| したいこと         | 移動先                                                                |
|---------------------|-------------------------------------------------------------------------|
| レッスン1を始める  | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| オフラインで作業   | [`setup-local.md`](02-setup-local.md)                                   |
| LLMプロバイダーを設定 | [`providers.md`](03-providers.md)                                        |
| 他の学習者と交流   | [Discordに参加する](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## トラブルシューティング


| 症状                                     | 解決策                                                           |
|-------------------------------------------|-----------------------------------------------------------------|
| コンテナのビルドが10分以上停止              | **Codespaces ➜ 「コンテナを再構築」**                            |
| `python: command not found`               | ターミナルが接続されていません；<strong>+</strong>をクリック ➜ *bash* を選択   |
| OpenAIからの`401 Unauthorized`            | 間違った、または期限切れの `OPENAI_API_KEY`                     |
| VS Codeで「Dev container mounting…」と表示 | ブラウザタブをリフレッシュ—Codespacesが接続を失うことがある    |
| ノートブックのカーネルが見つからない       | ノートブックメニュー ➜ **Kernel ▸ Select Kernel ▸ Python 3**     |

   Unix系システムの場合：

   ```bash
   touch .env
   ```

   Windowsの場合：

   ```cmd
   echo . > .env
   ```

3. **`.env`ファイルを編集する**：テキストエディター（例：VS Code、Notepad++など）で`.env`ファイルを開きます。実際のMicrosoft Foundry Modelsのエンドポイントとキーに置き換えて、以下の行を追加してください（取得方法は[`providers.md`](03-providers.md)を参照）。

   > **注意：** GitHub Models（およびその`GITHUB_TOKEN`変数）は2026年7月末に廃止されます。代わりに[Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)を使用してください。

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. <strong>ファイルを保存する</strong>：変更を保存してテキストエディターを閉じます。

5. **`python-dotenv`をインストールする**：まだの場合は、`.env`ファイルから環境変数をPythonアプリケーションに読み込むために`python-dotenv`パッケージをインストールしてください。`pip`でインストールできます：

   ```bash
   pip install python-dotenv
   ```

6. **Pythonスクリプトで環境変数を読み込む**：Pythonスクリプト内で、`python-dotenv`を使って`.env`ファイルから環境変数を読み込みます：

   ```python
   from dotenv import load_dotenv
   import os

   # .envファイルから環境変数を読み込みます
   load_dotenv()

   # Microsoft Foundry Modelsの変数にアクセスします
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

以上です！ `.env`ファイルを作成し、Microsoft Foundry Modelsの認証情報を追加し、それをPythonアプリに正常に読み込みました。

## ローカルのコンピューターで実行する方法

ローカル環境でコードを実行するには、何らかのバージョンの[Pythonをインストール](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)している必要があります。

それからリポジトリを利用するには、クローンしてください：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

クローンが完了したら、さっそく始められます！

## オプションの手順

### Minicondaのインストール

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst)は、[Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python、およびいくつかのパッケージをインストールするための軽量インストーラーです。
Condaはパッケージマネージャーであり、異なるPythonの[<strong>仮想環境</strong>](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)やパッケージ間の切り替えを簡単に行えます。また、`pip`で入手できないパッケージのインストールにも便利です。

[MiniCondaインストールガイド](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst)に従ってセットアップできます。

Minicondaをインストールしたら、まだなら[リポジトリをクローン](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)してください。

次に仮想環境を作成する必要があります。Condaでこれを行うには、新しい環境ファイル（_environment.yml_）を作成します。Codespacesを使っている場合は、`.devcontainer`ディレクトリ内つまり`.devcontainer/environment.yml`に作成してください。

下記のスニペットで環境ファイルを埋めてください：

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

Condaの使用中にエラーが出る場合は、端末で以下のコマンドを使って手動でMicrosoft AIライブラリをインストールしてください。

```
conda install -c microsoft azure-ai-ml
```

環境ファイルには必要な依存関係が記されています。`<environment-name>`はあなたが使いたいConda環境の名前、`<python-version>`は使いたいPythonのバージョン（例：`3`はPythonの最新メジャーバージョン）です。


それが終わったら、以下のコマンドをコマンドライン/ターミナルで実行してConda環境を作成できます。

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer サブパスは Codespace セットアップにのみ適用されます
conda activate ai4beg
```

問題が発生した場合は、[Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)を参照してください。

### Pythonサポート拡張機能付きVisual Studio Codeの使用

本講座では、[Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) エディターと [Pythonサポート拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) の使用をお勧めします。ただし、これはあくまでも推奨であり絶対条件ではありません。

> **Note**: VS Codeでコースのリポジトリを開くと、プロジェクトをコンテナ内にセットアップするオプションがあります。これはコースリポジトリ内にある[特別な `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)ディレクトリのためです。詳細は後述します。

> **Note**: リポジトリをクローンしてVS Codeで開くと、自動的にPythonサポート拡張機能のインストールが提案されます。

> **Note**: VS Codeがリポジトリをコンテナで再度開くよう提案した場合、ローカルにインストールされているPythonバージョンを使用するため、そのリクエストを断ってください。

### ブラウザーでJupyterを使用する

ブラウザー内で[ Jupyter環境](https://jupyter.org?WT.mc_id=academic-105485-koreyst)を使ってプロジェクトに取り組むこともできます。クラシックJupyterと[ Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst)の両方は、自動補完やコードの強調表示など、快適な開発環境を提供します。

ローカルでJupyterを起動するには、ターミナル/コマンドラインでコースのディレクトリに移動し、以下を実行してください。

```bash
jupyter notebook
```

または

```bash
jupyterhub
```

これでJupyterインスタンスが起動し、アクセス用のURLがコマンドラインウィンドウに表示されます。

URLにアクセスすると、コースのアウトラインが表示され、任意の `*.ipynb` ファイルに移動できます。例えば、`08-building-search-applications/python/oai-solution.ipynb`などです。

### コンテナでの実行

ご自身のコンピューターやCodespaceにすべてをセットアップする代替手段として、[コンテナ](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)を使用できます。コースリポジトリ内の特別な `.devcontainer` フォルダーにより、VS Codeでコンテナ内にプロジェクトをセットアップできます。Codespaces以外で使用する場合はDockerのインストールが必要で、正直なところ少し手間がかかりますので、コンテナ作業に慣れている方にのみお勧めします。

GitHub CodespacesでAPIキーを安全に管理する最良の方法の一つはCodespace Secretsを使うことです。詳細は [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst)ガイドをご覧ください。


## レッスンと技術要件

このコースには、生成AIの概念を説明する「Learn」レッスンと、可能な限り<strong>Python</strong>と<strong>TypeScript</strong>での実践的なコード例を含む「Build」レッスンがあります。

コーディングレッスンではMicrosoft FoundryのAzure OpenAIを使用します。AzureサブスクリプションとAPIキーが必要です。アクセスはオープンで申請不要なので、[Microsoft Foundryリソースの作成とモデルのデプロイ](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)を行い、エンドポイントとキーを取得してください。

各コーディングレッスンには、実行せずにコードと出力を確認できる `README.md` ファイルも含まれています。

## Azure OpenAIサービスの初回利用

Azure OpenAIサービスを初めて利用する場合は、[Azure OpenAIサービスリソースの作成とデプロイの方法](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)ガイドに従ってください。

## OpenAI APIの初回利用

OpenAI APIを初めて利用する場合は、[インターフェースの作成と使用方法](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)ガイドに従ってください。

## 他の学習者と出会う

公式[AI Community Discordサーバー](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)に他の学習者と出会うチャンネルを開設しました。これは、志を同じくする起業家、クリエイター、学生、生成AIでレベルアップを目指す方々と交流する絶好の機会です。

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

プロジェクトチームもこのDiscordサーバーに常駐しており、学習者のサポートを行います。

## 貢献する

このコースはオープンソースの取り組みです。改善点や問題を見つけた場合は、[Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)を作成するか、[GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)を報告してください。

プロジェクトチームはすべての貢献を追跡します。オープンソースへの貢献は生成AI分野でのキャリア構築に素晴らしい方法です。

多くの貢献は、あなたが貢献物を使用する権利を所有し、実際に使用権を付与していることを示す、Contributor License Agreement (CLA) への同意を必要とします。詳細は[CLA, Contributor License Agreementウェブサイト](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)をご覧ください。

重要: このリポジトリでテキストを翻訳する際は、機械翻訳を使用しないようにしてください。翻訳はコミュニティによって検証されるため、習熟している言語のみで翻訳をボランティアしてください。


プルリクエストを送信すると、CLAボットが自動的にCLAの提出が必要かどうかを判定し、PRに適切な装飾（例：ラベル、コメント）を行います。ボットの指示に従うだけで完了します。CLAを必要とするリポジトリすべてでこれを行うのは一度だけで済みます。

このプロジェクトは [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) を採用しています。詳細は行動規範のFAQをお読みいただくか、追加の質問やコメントがあれば [Email opencode](opencode@microsoft.com) までお問い合わせください。

## はじめに

このコースの必要なステップを完了したので、まずは [Generative AIとLLMの紹介](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) から始めましょう。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->