# このコースを始めるにあたって

このコースを始めて、生成AIを使ってどんなものを作れるか、ぜひ体験してみてください！

成功を確実にするために、このページではセットアップ手順、技術要件、必要な場合のサポートの受け方を説明します。

## セットアップ手順

このコースを始めるには、以下の手順を完了する必要があります。

### 1. リポジトリをフォークする

[このリポジトリ全体をフォーク](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)して、自分のGitHubアカウントでコードを変更し、チャレンジを完了できるようにします。また、このリポジトリを[スター（🌟）](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)することで、関連するリポジトリを見つけやすくなります。

### 2. コードスペースを作成する

コードを実行する際の依存関係の問題を避けるために、このコースを[GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)で実行することをお勧めします。

これは、フォークしたリポジトリの`Code`オプションを選択し、**Codespaces**オプションを選択することで作成できます。

![コードスペースを作成するためのボタンを示すダイアログ](../../../00-course-setup/images/who-will-pay.webp)

### 3. APIキーの保管

アプリケーションを構築する際には、APIキーを安全に保管することが重要です。APIキーをコードに直接保存しないことをお勧めします。これらの情報を公開リポジトリにコミットすると、セキュリティ問題や悪意のあるユーザーによる不正なコストが発生する可能性があります。

## コンピュータでローカルに実行する方法

コンピュータでコードをローカルに実行するには、[Pythonのインストール](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)が必要です。

その後、リポジトリを使用するには、クローンする必要があります:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

すべてがチェックアウトされたら、開始できます！

### Minicondaのインストール（オプション）

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst)は、[Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python、およびいくつかのパッケージをインストールするための軽量インストーラーです。
Conda自体はパッケージマネージャーであり、異なるPython[**仮想環境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)やパッケージのセットアップと切り替えを簡単にします。`pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`で利用できないパッケージのインストールにも便利です。

以下のスニペットで環境ファイルを作成してください:

```yml
name: <environment-name>
channels:
 - defaults
dependencies:
- python=<python-version>
- openai
- python-dotenv
- azure-ai-inference

```

環境ファイルには必要な依存関係が指定されています。`<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3`はPythonの最新のメジャーバージョンです。

それが完了したら、以下のコマンドをコマンドライン/ターミナルで実行してConda環境を作成できます。

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

問題が発生した場合は、[Conda環境ガイド](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)を参照してください。

### Pythonサポート拡張機能を備えたVisual Studio Codeの使用

このコースでは、[Visual Studio Code (VS Code)](http://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst)エディターを使用し、[Pythonサポート拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)をインストールすることをお勧めします。ただし、これはあくまで推奨であり、必須要件ではありません。

> **Note**: コースリポジトリをVS Codeで開くと、プロジェクトをコンテナ内で設定するオプションがあります。これは、コースリポジトリ内にある[特別な`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)ディレクトリによるものです。詳細は後ほど説明します。

> **Note**: ディレクトリをクローンしてVS Codeで開くと、Pythonサポート拡張機能をインストールするように自動で提案されます。

> **Note**: VS Codeがリポジトリをコンテナで再オープンすることを提案した場合、ローカルにインストールされたPythonのバージョンを使用するために、この要求を拒否してください。

### ブラウザでJupyterを使用する

[Jupyter環境](https://jupyter.org?WT.mc_id=academic-105485-koreyst)を使用して、ブラウザ内でプロジェクトに取り組むこともできます。クラシックJupyterおよび[Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst)の両方が、オートコンプリートやコードハイライトなどの機能を備えた快適な開発環境を提供します。

ローカルでJupyterを開始するには、ターミナル/コマンドラインに移動し、コースディレクトリにナビゲートして、以下を実行してください:

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

While you wait for your application to be processed, each coding lesson also includes a `README.md`ファイルに移動してコードと出力を表示することができます。

## Azure OpenAIサービスを初めて使用する場合

Azure OpenAIサービスを初めて使用する場合は、[Azure OpenAIサービスリソースを作成してデプロイする方法](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)に関するガイドに従ってください。

## OpenAI APIを初めて使用する場合

OpenAI APIを初めて使用する場合は、[インターフェースの作成と使用方法](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)に関するガイドに従ってください。

## 他の学習者と交流する

公式の[AIコミュニティDiscordサーバー](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)に、他の学習者と出会うためのチャンネルを作成しました。これは、生成AIでスキルアップを目指す、志を同じくする起業家、開発者、学生などとネットワークを築く素晴らしい方法です。

[![Discordチャンネルに参加する](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

プロジェクトチームもこのDiscordサーバーに参加して学習者をサポートします。

## 貢献する

このコースはオープンソースの取り組みです。改善点や問題点を見つけた場合は、[プルリクエスト](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)を作成するか、[GitHubの問題](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)をログしてください。

プロジェクトチームはすべての貢献を追跡します。オープンソースに貢献することは、生成AIでのキャリアを築くための素晴らしい方法です。

ほとんどの貢献には、貢献者ライセンス契約（CLA）に同意する必要があります。これは、あなたがその権利を持ち、実際に貢献を使用する権利を私たちに与えることを宣言するものです。詳細については、[CLA、貢献者ライセンス契約のウェブサイト](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)を参照してください。

プルリクエストを提出すると、CLA-botが自動的にCLAを提供する必要があるかどうかを判断し、PRに適切な装飾を施します（例：ラベル、コメント）。ボットが提供する指示に従ってください。CLAを提供するのは、すべてのリポジトリで一度だけ必要です。

このプロジェクトは、[Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)を採用しています。詳細は、行動規範FAQを読むか、[Email opencode](opencode@microsoft.com)に質問やコメントを送信してください。

## 始めましょう

コースを完了するために必要な手順を完了したので、[生成AIとLLMの紹介](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)から始めましょう。

**免責事項**:  
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを追求していますが、自動翻訳には誤りや不正確さが含まれる場合がありますのでご注意ください。原文はその言語における権威ある情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤訳について、当社は責任を負いません。