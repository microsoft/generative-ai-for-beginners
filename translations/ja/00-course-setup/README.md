# このコースの始め方

このコースを始めて、ジェネレーティブAIで何を作りたいかに触発されるのを私たちはとても楽しみにしています！

成功を確実にするために、このページではセットアップ手順、技術的要件、および必要に応じてサポートを受ける方法を説明します。

## セットアップ手順

このコースを開始するには、次の手順を完了する必要があります。

### 1. このリポジトリをフォークする

[このリポジトリ全体をフォーク](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)して、ご自身のGitHubアカウントにコピーしてください。コードを変更したりチャレンジを完了したりするために必要です。また、[このリポジトリにスター（🌟）を付ける](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)と、関連リポジトリを見つけやすくなります。

### 2. codespaceを作成する

コードの依存関係の問題を避けるため、このコースは[GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)で実行することを推奨します。

フォークしたリポジトリで：**Code -> Codespaces -> New on main**

![コードスペース作成ボタンを示すダイアログ](../../../translated_images/ja/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 シークレットを追加する

1. ⚙️ 歯車アイコン -> コマンドパレット -> Codespaces : Manage user secret -> 新しいシークレットを追加。
2. 名前にOPENAI_API_KEYを入力し、キーを貼り付けて保存。

### 3. 次は？

| やりたいこと               | 移動先                                                                    |
|----------------------------|---------------------------------------------------------------------------|
| レッスン1を始める          | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)        |
| オフラインで作業する       | [`setup-local.md`](02-setup-local.md)                                     |
| LLMプロバイダーを設定する  | [`providers.md`](03-providers.md)                                         |
| 他の学習者に会う           | [Discordに参加](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## トラブルシューティング

| 症状                                       | 対処法                                                      |
|--------------------------------------------|------------------------------------------------------------|
| コンテナのビルドが10分以上停止している      | **Codespaces ➜ 「Rebuild Container」** を選択               |
| `python: command not found` が表示される    | ターミナルが接続されていないため、**+** をクリックし *bash* を選択 |
| OpenAIから `401 Unauthorized` が返される   | `OPENAI_API_KEY` が間違っているか、期限切れ                 |
| VS Codeで「Dev container mounting…」と表示 | ブラウザのタブを更新。Codespacesが接続を失うことがある      |
| ノートブックのカーネルが存在しない           | ノートブック メニュー ➜ **Kernel ▸ Select Kernel ▸ Python 3** を選択  |

   Unix系システム:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` ファイルを編集**: テキストエディタ（例：VS Code、Notepad++、その他）で `.env` ファイルを開きます。`your_github_token_here` を実際のGitHubトークンに置き換えて、次の行を追加します:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **ファイルを保存**: 変更を保存し、テキストエディタを閉じます。

5. **`python-dotenv` をインストール**: まだの場合は、`python-dotenv` パッケージをインストールしてください。これは `.env` ファイルから環境変数をPythonアプリケーションに読み込むために必要です。`pip` でインストールできます:

   ```bash
   pip install python-dotenv
   ```

6. **Pythonスクリプトで環境変数を読み込む**: Pythonスクリプト内で `python-dotenv` パッケージを使用し、`.env` ファイルから環境変数を読み込みます:

   ```python
   from dotenv import load_dotenv
   import os

   # .envファイルから環境変数を読み込む
   load_dotenv()

   # GITHUB_TOKEN変数にアクセスする
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

これで完了です！`.env` ファイルの作成、GitHubトークンの追加、およびPythonアプリでの読み込みが成功しました。

## コンピューターでローカル実行する方法

コンピューターでコードをローカルに実行するには、[Pythonのいずれかのバージョンがインストールされている必要があります](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)。

その後、リポジトリをクローンしてください。

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

すべて準備できたら、さっそく始めましょう！

## オプションの手順

### Minicondaのインストール

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst)は、[Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python、およびいくつかのパッケージをインストールするための軽量インストーラーです。  
Condaはパッケージマネージャーで、複数のPythonの[**仮想環境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)やパッケージの設定や切り替えを簡単に行えます。`pip` で入手できないパッケージのインストールにも便利です。

[Minicondaインストールガイド](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst)に従いセットアップしてください。

Minicondaをインストールしたら、まだなら[リポジトリをクローン](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)します。

次に仮想環境を作成します。Condaを使う場合は環境ファイル（_environment.yml_）を作成します。Codespacesを使う場合は `.devcontainer` ディレクトリ内に作成し、パスは `.devcontainer/environment.yml` となります。

環境ファイルを以下のスニペットで埋めてください：

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

もしcondaでエラーが発生する場合は、以下のコマンドをターミナルで使ってMicrosoft AIライブラリを手動でインストールできます。

```
conda install -c microsoft azure-ai-ml
```

環境ファイルは必要な依存関係を指定します。 `<environment-name>` は作成したいConda環境名で、`<python-version>` は使用したいPythonのバージョン（例：最新のメジャーバージョン3）です。

これを終えたら、以下のコマンドでConda環境を作成します。

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer のサブパスは Codespace の設定にのみ適用されます
conda activate ai4beg
```

問題がある場合は、[Conda環境のガイド](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)を参照してください。

### Visual Studio CodeとPythonサポート拡張機能の使用

このコースでは、[Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) エディターと [Pythonサポート拡張](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) の利用を推奨しています。ただし必須ではありません。

> **注意**: コースリポジトリをVS Codeで開くと、プロジェクトをコンテナ内にセットアップするオプションがあります。これは、コースリポジトリ内の[特別な `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ディレクトリによるものです。詳細は後述します。

> **注意**: リポジトリをクローンしVS Codeで開くと、自動的にPythonサポート拡張機能のインストールを提案されます。

> **注意**: VS Codeでリポジトリのコンテナでの再オープンを提案された場合は、ローカルのPythonを使うため拒否してください。

### ブラウザでJupyterを使う

ブラウザ上で [Jupyter環境](https://jupyter.org?WT.mc_id=academic-105485-koreyst) を利用することも可能です。クラシックJupyterも[ Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst)も、自動補完やコードハイライトなど使いやすい開発環境を提供します。

ローカルでJupyterを起動するには、ターミナル／コマンドラインでコースディレクトリに移動して次のコマンドを実行：

```bash
jupyter notebook
```

または

```bash
jupyterhub
```

このコマンドでJupyterが起動し、アクセスURLが表示されます。

URLにアクセスするとコースのアウトラインが表示され、任意の `*.ipynb` ファイルに移動できます。例：`08-building-search-applications/python/oai-solution.ipynb`。

### コンテナでの実行

コンピューターやCodespaceでのセットアップの代わりに[コンテナ](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)を使うこともできます。  
コースリポジトリ内の特別な `.devcontainer` フォルダーを使い、VS Codeでプロジェクトをコンテナ内にセットアップ可能です。Codespaces外ではDockerのインストールが必要で多少の作業が発生するため、コンテナ作業経験者にのみ推奨します。

GitHub CodespacesでAPIキーを安全に管理する最善の方法の1つはCodespace Secretsの利用です。詳しくは[Codespaces secret管理ガイド](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst)をご覧ください。

## レッスンと技術的要件

コースには6つのコンセプトレッスンと6つのコーディングレッスンがあります。

コーディングレッスンではAzure OpenAI Serviceを使用します。サービスの利用とAPIキーが必要です。アクセスには[この申請](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)を提出してください。

申請結果を待つ間は、各コーディングレッスンに含まれる `README.md` でコードと出力を確認できます。

## 初めてAzure OpenAI Serviceを使う場合

Azure OpenAI Serviceを初めて使う場合は、以下のガイドに従ってサービスリソースの[作成とデプロイ](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)を行ってください。

## 初めてOpenAI APIを使う場合

OpenAI APIを初めて使う場合は、作成と使用方法についてのガイドを参照してください。[Interfaceの作成と利用](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## 他の学習者に会う

公式の[AIコミュニティDiscordサーバー](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)にて、他の学習者と交流できるチャンネルを作成しました。同じ志を持つ起業家やビルダー、学生、そしてジェネレーティブAIをレベルアップしたい方々とネットワークを築く素晴らしい機会です。

[![Discordチャンネルに参加](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

プロジェクトチームもこのDiscordサーバーで学習者をサポートします。

## 参加する

このコースはオープンソースの取り組みです。改善点や問題を見つけたら、[プルリクエストを作成](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)するか、[GitHubのIssue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)を報告してください。

プロジェクトチームはすべての貢献を追跡しています。オープンソースに貢献することは、ジェネレーティブAIのキャリアを築く素晴らしい方法です。

ほとんどの貢献は、あなたが寄稿物を使用権として当社に許諾する権利を持ち、実際に許諾していることを宣言するコントリビューターライセンス契約（CLA）への同意が必要です。詳細は[CLA、コントリビューターライセンス契約のウェブサイト](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)をご覧ください。

重要：このリポジトリのテキストを翻訳するときは、機械翻訳を使わないでください。コミュニティにより翻訳内容を検証するため、母語が堪能な言語の翻訳者のみボランティアしてください。

プルリクエストを送ると、CLAボットが自動的にCLAの提供が必要か判断し、ラベルやコメントをつけます。指示に従ってください。この操作はすべてのリポジトリで一度だけ行えば十分です。

このプロジェクトは[Microsoftのオープンソース行動規範](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)を採用しています。詳細は行動規範のFAQを読んでください。追加の質問やコメントは[Email opencode](opencode@microsoft.com)へご連絡ください。

## さあ始めましょう！
このコースを完了するために必要なステップを終えたので、まずは[生成AIと大規模言語モデル（LLM）の紹介](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)から始めましょう。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文はその言語における正式な版としてご参照ください。重要な情報については、専門の翻訳者による翻訳を推奨いたします。本翻訳の利用により生じたいかなる誤解や誤訳に対しても、一切の責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
