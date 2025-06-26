<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:40:44+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "ja"
}
-->
# このコースを始めるにあたって

このコースを始め、生成AIを使って何を作り出すかを考えるのが楽しみです！

成功を確実にするために、このページではセットアップ手順、技術要件、必要に応じてどこで助けを得るかを説明します。

## セットアップ手順

このコースを受講するには、以下の手順を完了する必要があります。

### 1. このリポジトリをフォークする

コードを変更し、チャレンジを完了するために、このリポジトリ全体を自分のGitHubアカウントに[フォーク](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)してください。また、このリポジトリに[スター(🌟)を付ける](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)ことで、関連するリポジトリを簡単に見つけることができます。

### 2. コードスペースを作成する

コードを実行する際の依存関係の問題を避けるために、このコースを[GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)で実行することをお勧めします。

これは、フォークしたリポジトリで`Code`オプションを選択し、**Codespaces**オプションを選択することで作成できます。

![コードスペースを作成するためのボタンを示すダイアログ](../../../00-course-setup/images/who-will-pay.webp)

### 3. APIキーの保存

どのようなアプリケーションを構築する際にも、APIキーを安全に保つことが重要です。APIキーをコードに直接保存しないことをお勧めします。それらの詳細を公開リポジトリにコミットすると、セキュリティの問題や悪意のあるユーザーによる不正なコストが発生する可能性があります。Python用の`.env`ファイルを作成し、`GITHUB_TOKEN`を追加する手順を以下に示します：

1. **プロジェクトディレクトリに移動**: ターミナルまたはコマンドプロンプトを開き、`.env`ファイルを作成したいプロジェクトのルートディレクトリに移動します。

   ```bash
   cd path/to/your/project
   ```

2. **`.env`ファイルを作成**: お好みのテキストエディタを使用して`.env`という名前の新しいファイルを作成します。コマンドラインを使用する場合は、`touch` (on Unix-based systems) or `echo`（Windowsの場合）を使用できます：

   Unix系システム：
   ```bash
   touch .env
   ```

   Windows：
   ```cmd
   echo . > .env
   ```

3. **`.env`ファイルを編集**: テキストエディタ（例：VS Code、Notepad++など）で`.env`ファイルを開き、以下の行をファイルに追加します。`your_github_token_here`を実際のGitHubトークンに置き換えてください：

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **ファイルを保存**: 変更を保存し、テキストエディタを閉じます。

5. **`python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv`パッケージをインストールして`.env`ファイルから環境変数をPythonアプリケーションにロードします。`pip`を使用してインストールできます：

   ```bash
   pip install python-dotenv
   ```

6. **Pythonスクリプトで環境変数をロード**: Pythonスクリプトで`python-dotenv`パッケージを使用して`.env`ファイルから環境変数をロードします：

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

これで完了です！`.env`ファイルを作成し、GitHubトークンを追加し、それをPythonアプリケーションにロードすることができました。

## コンピュータでローカルに実行する方法

コンピュータでコードをローカルに実行するには、[Pythonのあるバージョンをインストール](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)する必要があります。

その後、リポジトリを使用するためには、クローンする必要があります：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

すべてをチェックアウトしたら、始めることができます！

## オプションのステップ

### Minicondaのインストール

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst)は、[Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python、いくつかのパッケージをインストールするための軽量インストーラーです。
Conda自体はパッケージマネージャーであり、異なるPythonの[**仮想環境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)とパッケージのセットアップと切り替えを簡単に行うことができます。また、`pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`で利用できないパッケージのインストールにも便利です。

以下のスニペットで環境ファイルを設定してください：

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

もしcondaを使用してエラーが発生した場合は、以下のコマンドをターミナルで実行してMicrosoft AI Librariesを手動でインストールできます。

```
conda install -c microsoft azure-ai-ml
```

環境ファイルは必要な依存関係を指定します。`<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3`はPythonの最新の主要バージョンです。

それが完了したら、以下のコマンドをコマンドライン/ターミナルで実行してConda環境を作成できます。

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

問題が発生した場合は、[Conda環境ガイド](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)を参照してください。

### Pythonサポート拡張機能付きのVisual Studio Codeの使用

このコースでは、[Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst)エディタと[Pythonサポート拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)をインストールすることをお勧めします。ただし、これは推奨であり、必須ではありません。

> **注意**: コースリポジトリをVS Codeで開くことで、プロジェクトをコンテナ内で設定するオプションがあります。これは、コースリポジトリ内にある[特別な`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)ディレクトリのためです。詳細は後述します。

> **注意**: ディレクトリをクローンしてVS Codeで開くと、Pythonサポート拡張機能のインストールを自動的に提案します。

> **注意**: VS Codeがリポジトリをコンテナで再開することを提案した場合は、この要求を拒否してローカルにインストールされたPythonのバージョンを使用してください。

### ブラウザでJupyterを使用する

[ブラウザ内でJupyter環境](https://jupyter.org?WT.mc_id=academic-105485-koreyst)を使用してプロジェクトに取り組むこともできます。クラシックJupyterと[Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst)は、オートコンプリートやコードハイライトなどの機能を備えた快適な開発環境を提供します。

ローカルでJupyterを開始するには、ターミナル/コマンドラインに移動し、コースディレクトリに移動して以下を実行します：

```bash
jupyter notebook
```

または

```bash
jupyterhub
```

これによりJupyterインスタンスが開始され、アクセスするためのURLがコマンドラインウィンドウに表示されます。

URLにアクセスすると、コースの概要が表示され、任意の`*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md`ファイルに移動してコードと出力を表示できます。

## 初めてAzure OpenAIサービスを使用する場合

初めてAzure OpenAIサービスを使用する場合は、[Azure OpenAIサービスリソースの作成と展開方法](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)に関するガイドに従ってください。

## 初めてOpenAI APIを使用する場合

初めてOpenAI APIを使用する場合は、[インターフェースの作成と使用方法](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)に関するガイドに従ってください。

## 他の学習者と交流する

公式の[AIコミュニティDiscordサーバー](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)で他の学習者と交流するためのチャンネルを作成しました。これは、同じ志を持つ起業家、開発者、学生、生成AIを学びたい人々とネットワークを築く素晴らしい方法です。

[![Discordチャンネルに参加](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

プロジェクトチームもこのDiscordサーバーに参加し、学習者をサポートします。

## 貢献する

このコースはオープンソースのイニシアティブです。改善点や問題を見つけた場合は、[プルリクエスト](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)を作成するか、[GitHubの問題](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)をログしてください。

プロジェクトチームはすべての貢献を追跡します。オープンソースに貢献することは、生成AIでのキャリアを築くための素晴らしい方法です。

ほとんどの貢献には、貢献者ライセンス契約（CLA）に同意し、貢献する権利があることを宣言する必要があります。詳細については、[CLA、貢献者ライセンス契約ウェブサイト](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)を参照してください。

重要: このリポジトリ内のテキストを翻訳する際には、機械翻訳を使用しないようにしてください。翻訳はコミュニティによって検証されるため、熟練している言語でのみ翻訳にボランティアしてください。

プルリクエストを送信すると、CLAボットが自動的にCLAを提供する必要があるかどうかを判断し、適切にPRを装飾します（例：ラベル、コメント）。ボットが提供する指示に従ってください。CLAを使用しているすべてのリポジトリで一度だけ行う必要があります。

このプロジェクトは[Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)を採用しています。詳細については、行動規範FAQを読むか、追加の質問やコメントがある場合は[Email opencode](opencode@microsoft.com)にお問い合わせください。

## 始めましょう

必要な手順を完了したので、このコースを始めるために[生成AIとLLMの紹介](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)を受けましょう。

**免責事項**:
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確さを追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご承知ください。元の文書が原言語での信頼できる情報源とみなされるべきです。重要な情報については、プロの人間による翻訳をお勧めします。この翻訳の使用により生じる誤解や誤訳について、当社は責任を負いません。