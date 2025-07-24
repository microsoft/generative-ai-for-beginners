<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T07:03:52+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ja"
}
-->
# このコースの始め方

このコースを始めて、Generative AIで何を作りたいかインスピレーションを得られることをとても楽しみにしています！

成功のために、このページではセットアップ手順、技術要件、そして必要に応じてサポートを受ける方法を説明しています。

## セットアップ手順

このコースを始めるには、以下の手順を完了する必要があります。

### 1. このリポジトリをフォークする

コードを変更したりチャレンジを完了したりするために、[このリポジトリ全体をフォーク](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)して自分のGitHubアカウントにコピーしてください。また、[このリポジトリにスター（🌟）を付ける](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)ことで、関連リポジトリを見つけやすくなります。

### 2. Codespaceを作成する

コード実行時の依存関係の問題を避けるために、このコースは[GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)で実行することを推奨します。

フォークしたリポジトリの`Code`オプションを選択し、**Codespaces**を選んで作成できます。

![Codespace作成ボタンを示すダイアログ](../../../00-course-setup/images/who-will-pay.webp)

### 3. APIキーの保管

APIキーを安全に管理することは、どんなアプリケーションを作る上でも重要です。APIキーをコードに直接保存しないことをおすすめします。公開リポジトリにキーをコミットすると、セキュリティリスクや悪意のある利用による予期せぬコストが発生する可能性があります。  
以下はPython用の`.env`ファイルを作成し、`GITHUB_TOKEN`を追加する手順です。

1. **プロジェクトディレクトリに移動**: ターミナルやコマンドプロンプトを開き、`.env`ファイルを作成したいプロジェクトのルートディレクトリに移動します。

   ```bash
   cd path/to/your/project
   ```

2. **`.env`ファイルを作成**: お好みのテキストエディタで新規ファイル`.env`を作成します。コマンドラインの場合、Unix系システムでは`touch`、Windowsでは`echo`を使えます。

   Unix系システム:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env`ファイルを編集**: `.env`ファイルをテキストエディタ（例：VS Code、Notepad++など）で開き、以下の行を追加します。`your_github_token_here`は実際のGitHubトークンに置き換えてください。

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **ファイルを保存**: 変更を保存してエディタを閉じます。

5. **`python-dotenv`のインストール**: `.env`ファイルから環境変数をPythonアプリケーションに読み込むために、`python-dotenv`パッケージをインストールします。`pip`でインストール可能です。

   ```bash
   pip install python-dotenv
   ```

6. **Pythonスクリプトで環境変数を読み込む**: Pythonスクリプト内で`python-dotenv`を使い、`.env`ファイルから環境変数を読み込みます。

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

これで`.env`ファイルの作成、GitHubトークンの追加、Pythonアプリケーションへの読み込みが完了です。

## ローカルでの実行方法

ローカルでコードを実行するには、[Pythonのいずれかのバージョンをインストール](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)しておく必要があります。

その後、リポジトリをクローンしてください。

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

すべて準備できたら、さっそく始めましょう！

## 任意の手順

### Minicondaのインストール

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst)は、[Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python、およびいくつかのパッケージをインストールするための軽量インストーラーです。  
Condaはパッケージマネージャーで、異なるPythonの[**仮想環境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)やパッケージのセットアップや切り替えを簡単にします。また、`pip`で入手できないパッケージのインストールにも便利です。

[MiniCondaインストールガイド](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst)に従ってセットアップしてください。

Minicondaをインストールしたら、まだなら[リポジトリをクローン](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)します。

次に仮想環境を作成します。Condaで行う場合は、新しい環境ファイル（_environment.yml_）を作成してください。Codespacesを使っている場合は、`.devcontainer`ディレクトリ内に作成し、`.devcontainer/environment.yml`とします。

以下のスニペットで環境ファイルを作成してください。

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

環境ファイルには必要な依存関係が指定されています。`<environment-name>`はConda環境の名前、`<python-version>`は使用したいPythonのバージョン（例：最新のメジャーバージョンは`3`）です。

準備ができたら、以下のコマンドをコマンドラインやターミナルで実行してConda環境を作成します。

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

問題があれば[Conda環境のガイド](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)を参照してください。

### Visual Studio CodeとPython拡張機能の使用

このコースでは、[Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst)エディタに[Pythonサポート拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)をインストールして使うことを推奨します。ただし、必須ではありません。

> **Note**: コースリポジトリをVS Codeで開くと、プロジェクトをコンテナ内でセットアップするオプションが表示されます。これはリポジトリ内の[特別な`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)ディレクトリによるものです。詳細は後述します。

> **Note**: リポジトリをクローンしてVS Codeで開くと、自動的にPythonサポート拡張機能のインストールを提案されます。

> **Note**: VS Codeがリポジトリをコンテナ内で再オープンするよう提案した場合は、ローカルにインストールされたPythonを使うためにこの提案は拒否してください。

### ブラウザでJupyterを使う

ブラウザ内で[ Jupyter環境](https://jupyter.org?WT.mc_id=academic-105485-koreyst)を使ってプロジェクトに取り組むこともできます。クラシックJupyterや[Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst)は、オートコンプリートやコードハイライトなど快適な開発環境を提供します。

ローカルでJupyterを起動するには、ターミナルやコマンドラインでコースディレクトリに移動し、以下を実行してください。

```bash
jupyter notebook
```

または

```bash
jupyterhub
```

これでJupyterが起動し、アクセス用のURLがコマンドラインに表示されます。

URLにアクセスすると、コースのアウトラインが表示され、任意の`*.ipynb`ファイルに移動できます。例：`08-building-search-applications/python/oai-solution.ipynb`

### コンテナでの実行

パソコンやCodespaceにすべてをセットアップする代わりに、[コンテナ](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)を使う方法もあります。コースリポジトリ内の特別な`.devcontainer`フォルダにより、VS Codeがコンテナ内でプロジェクトをセットアップ可能です。Codespaces以外で使う場合はDockerのインストールが必要で、やや手間がかかるため、コンテナの経験がある方にのみおすすめします。

GitHub CodespacesでAPIキーを安全に管理する最良の方法の一つは、Codespace Secretsの利用です。[Codespaces secrets管理](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst)ガイドを参照してください。

## レッスンと技術要件

このコースは6つの概念レッスンと6つのコーディングレッスンで構成されています。

コーディングレッスンではAzure OpenAI Serviceを使用します。コードを実行するにはAzure OpenAIサービスへのアクセス権とAPIキーが必要です。[こちらの申請フォーム](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)からアクセス申請が可能です。

申請処理中は、各コーディングレッスンに付属の`README.md`ファイルでコードと出力を確認できます。

## Azure OpenAI Serviceを初めて使う場合

Azure OpenAI Serviceを初めて使う場合は、[Azure OpenAI Serviceリソースの作成とデプロイ方法](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)のガイドに従ってください。

## OpenAI APIを初めて使う場合

OpenAI APIを初めて使う場合は、[インターフェースの作成と使用方法](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)のガイドを参照してください。

## 他の学習者と交流しよう

公式の[AI Community Discordサーバー](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)に学習者同士が交流できるチャンネルを用意しています。志を同じくする起業家、開発者、学生、Generative AIをレベルアップしたい方々とネットワークを広げる絶好の機会です。

[![Discordチャンネルに参加](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

プロジェクトチームもこのDiscordサーバーに参加し、学習者のサポートを行います。

## 貢献について

このコースはオープンソースの取り組みです。改善点や問題を見つけたら、[プルリクエスト](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)を作成するか、[GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)を報告してください。

プロジェクトチームはすべての貢献を追跡しています。オープンソースへの貢献はGenerative AI分野でのキャリア構築に素晴らしい方法です。

ほとんどの貢献には、貢献物の使用権を当方に付与する権利があることを宣言するContributor License Agreement (CLA)への同意が必要です。詳細は[CLA, Contributor License Agreementのウェブサイト](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)をご覧ください。

重要：このリポジトリの翻訳を行う際は、機械翻訳を使わないようにしてください。コミュニティによる検証を行うため、翻訳に自信のある言語のみでボランティアをお願いします。

プルリクエストを提出すると、CLA-botが自動的にCLAの提出が必要か判定し、PRに適切なラベルやコメントを付けます。ボットの指示に従ってください。CLAの提出は当方のすべてのリポジトリで一度だけ行えば十分です。

このプロジェクトは[Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)を採用しています。詳細はCode of Conduct FAQを読むか、質問やコメントがあれば[Email opencode](opencode@microsoft.com)までご連絡ください。

## さあ、始めましょう

必要な手順を完了したので、まずは[Generative AIとLLMの紹介](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)から始めましょう。

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねます。