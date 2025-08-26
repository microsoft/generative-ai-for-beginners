<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T15:05:07+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ja"
}
-->
# このコースの始め方

このコースを始めて、生成AIでどんなものを作りたくなるのか、とても楽しみにしています！

あなたの成功のために、このページではセットアップ手順、技術要件、困ったときのサポート先についてまとめています。

## セットアップ手順

コースを始めるには、以下の手順を完了してください。

### 1. このリポジトリをフォークする

[このリポジトリ全体をフォーク](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)して、自分のGitHubアカウントでコードを変更したり、チャレンジを完了できるようにしましょう。また、[スター (🌟) を付ける](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)ことで、関連リポジトリを簡単に見つけられます。

### 2. Codespaceを作成する

コードの依存関係の問題を避けるために、このコースは[GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)で実行することをおすすめします。

自分のフォークで：**Code -> Codespaces -> New on main**

![Codespace作成ボタンのダイアログ](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 シークレットを追加する

1. ⚙️ ギアアイコン -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. 名前をOPENAI_API_KEYにして、キーを貼り付け、保存します。

### 3. 次は何をする？

| やりたいこと         | 移動先                                                                  |
|---------------------|-------------------------------------------------------------------------|
| レッスン1を始める      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| オフラインで作業する   | [`setup-local.md`](02-setup-local.md)                                   |
| LLMプロバイダーを設定する | [`providers.md`](providers.md)                                        |
| 他の学習者と交流する | [Discordに参加](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## トラブルシューティング

| 症状                                   | 対処法                                                             |
|----------------------------------------|--------------------------------------------------------------------|
| コンテナのビルドが10分以上止まる        | **Codespaces ➜ “Rebuild Container”**                               |
| `python: command not found`            | ターミナルが接続されていません。**+** ➜ *bash* をクリック           |
| OpenAIから`401 Unauthorized`           | `OPENAI_API_KEY`が間違っている/期限切れ                            |
| VS Codeが“Dev container mounting…”と表示 | ブラウザタブをリフレッシュ—Codespacesが接続を失うことがあります    |
| Notebookカーネルが見つからない         | Notebookメニュー ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix系システム:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env`ファイルを編集する**: テキストエディタ（例：VS Code, Notepad++など）で`.env`ファイルを開き、以下の行を追加します。`your_github_token_here`は自分のGitHubトークンに置き換えてください。

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **ファイルを保存する**: 変更を保存して、エディタを閉じます。

5. **`python-dotenv`をインストールする**: まだインストールしていない場合は、`python-dotenv`パッケージをインストールして、Pythonアプリケーションで`.env`ファイルの環境変数を読み込めるようにします。`pip`でインストールできます。

   ```bash
   pip install python-dotenv
   ```

6. **Pythonスクリプトで環境変数を読み込む**: Pythonスクリプト内で`python-dotenv`パッケージを使い、`.env`ファイルから環境変数を読み込みます。

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

これで、`.env`ファイルの作成、GitHubトークンの追加、Pythonアプリケーションへの読み込みが完了です。

## パソコンでローカル実行する方法

コードを自分のパソコンで実行するには、[Pythonをインストール](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)しておく必要があります。

リポジトリを使うには、まずクローンします。

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

すべてチェックアウトできたら、すぐに始められます！

## オプション手順

### Minicondaのインストール

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst)は、[Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)やPython、いくつかのパッケージをインストールできる軽量インストーラーです。
Condaはパッケージ管理ツールで、Pythonの[**仮想環境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)やパッケージの切り替えが簡単にできます。`pip`で入手できないパッケージのインストールにも便利です。

[MiniCondaインストールガイド](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst)に従ってセットアップしてください。

Minicondaをインストールしたら、[リポジトリ](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)をクローンします（まだの場合）。

次に、仮想環境を作成します。Condaで新しい環境ファイル(_environment.yml_)を作成してください。Codespacesを使っている場合は、`.devcontainer`ディレクトリ内に作成します（例：`.devcontainer/environment.yml`）。

以下のスニペットで環境ファイルを作成しましょう。

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

もしcondaでエラーが出る場合は、以下のコマンドでMicrosoft AIライブラリを手動でインストールできます。

```
conda install -c microsoft azure-ai-ml
```

環境ファイルには必要な依存関係が記載されています。`<environment-name>`はConda環境の名前、`<python-version>`は使いたいPythonのバージョンです。例えば、`3`は最新のメジャーバージョンです。

これができたら、以下のコマンドでConda環境を作成します。

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

問題があれば[Conda環境ガイド](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)を参照してください。

### Pythonサポート拡張機能付きVisual Studio Codeの利用

このコースでは、[Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst)エディタと[Pythonサポート拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)の利用をおすすめします。ただし、必須ではありません。

> **Note**: コースリポジトリをVS Codeで開くと、プロジェクトをコンテナ内でセットアップするオプションがあります。これは、リポジトリ内の[特別な`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)ディレクトリによるものです。詳細は後ほど。

> **Note**: ディレクトリをクローンしてVS Codeで開くと、Pythonサポート拡張機能のインストールを自動で提案されます。

> **Note**: VS Codeがリポジトリをコンテナで再度開くよう提案した場合は、ローカルのPythonを使うためにこのリクエストを断ってください。

### ブラウザでJupyterを使う

[ブラウザ上のJupyter環境](https://jupyter.org?WT.mc_id=academic-105485-koreyst)でもプロジェクトに取り組めます。クラシックJupyterや[Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst)は、補完やコードハイライトなど快適な開発環境を提供します。

Jupyterをローカルで起動するには、ターミナル/コマンドラインでコースディレクトリに移動し、以下を実行します。

```bash
jupyter notebook
```

または

```bash
jupyterhub
```

これでJupyterが起動し、アクセス用URLがコマンドラインウィンドウに表示されます。

URLにアクセスすると、コースのアウトラインが表示され、任意の`*.ipynb`ファイルに移動できます。例：`08-building-search-applications/python/oai-solution.ipynb`。

### コンテナで実行する

パソコンやCodespaceでセットアップする代わりに、[コンテナ](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)を使う方法もあります。コースリポジトリ内の特別な`.devcontainer`フォルダーにより、VS Codeでプロジェクトをコンテナ内にセットアップできます。Codespaces以外ではDockerのインストールが必要で、少し手間がかかるので、コンテナ経験者向けの方法です。

GitHub CodespacesでAPIキーを安全に管理するには、Codespace Secretsの利用がおすすめです。[Codespaces secrets管理ガイド](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst)を参照してください。

## レッスンと技術要件

コースは6つの概念レッスンと6つのコーディングレッスンで構成されています。

コーディングレッスンではAzure OpenAI Serviceを使用します。コードを実行するにはAzure OpenAIサービスへのアクセスとAPIキーが必要です。[申請フォーム](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)から申請できます。

申請が処理されるまでの間、各コーディングレッスンには`README.md`ファイルがあり、コードや出力を確認できます。

## Azure OpenAI Serviceの初回利用

Azure OpenAIサービスを初めて使う場合は、[Azure OpenAI Serviceリソースの作成とデプロイ方法](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)ガイドに従ってください。

## OpenAI APIの初回利用

OpenAI APIを初めて使う場合は、[インターフェースの作成と利用方法](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)ガイドに従ってください。

## 他の学習者と交流する

公式の[AI Community Discordサーバー](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)に、他の学習者と交流できるチャンネルを用意しています。生成AIに興味のある起業家、開発者、学生などとネットワークを広げる絶好の機会です。

[![Discordチャンネルに参加](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

プロジェクトチームもこのDiscordサーバーで学習者をサポートします。

## 貢献する

このコースはオープンソースプロジェクトです。改善点や問題があれば、[Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)を作成するか、[GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)に記録してください。

プロジェクトチームはすべての貢献を追跡します。オープンソースへの貢献は、生成AI分野でキャリアを築く素晴らしい方法です。

ほとんどの貢献には、Contributor License Agreement (CLA)への同意が必要です。これは、あなたが貢献する権利を持ち、実際に権利を譲渡することを宣言するものです。詳細は[CLA, Contributor License Agreementのウェブサイト](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)をご覧ください。

重要：このリポジトリの翻訳を行う際は、機械翻訳を使用しないでください。翻訳はコミュニティで確認しますので、得意な言語のみでボランティアしてください。

Pull Requestを送信すると、CLA-botが自動的にCLAの提出が必要かどうかを判断し、PRにラベルやコメントを付けます。指示に従ってください。CLAの提出は、弊社CLAを使うすべてのリポジトリで一度だけ必要です。

このプロジェクトは[Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)を採用しています。詳細はCode of Conduct FAQを読むか、[Email opencode](opencode@microsoft.com)までご質問・ご意見をお寄せください。

## さあ、始めましょう
これでこのコースを進めるための必要なステップが完了しました。さっそく、[生成AIとLLMの概要](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)から始めましょう。

---

**免責事項**：
本書類はAI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な表現が含まれる場合があります。原文（元の言語の文書）が正式な情報源として扱われるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤認についても、当方は責任を負いかねます。