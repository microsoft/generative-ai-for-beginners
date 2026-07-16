# このコースの始め方

このコースを始め、生成AIで何を作りたいかインスピレーションを受け取ることに、私たちはとてもワクワクしています！

あなたの成功を確実にするために、このページではセットアップの手順、技術要件、および必要な場合のサポート先について説明します。

## セットアップ手順

このコースを始めるには、以下のステップを完了する必要があります。

### 1. このリポジトリをフォークする

[このリポジトリ全体をフォークする](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)ことで、コードの変更やチャレンジの完了が可能になります。また、[このリポジトリにスター（🌟）を付ける](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)と、関連リポジトリを見つけやすくなります。

### 2. コードスペースの作成

依存関係の問題を避けるため、このコースは [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) で実行することをお勧めします。

フォークしたリポジトリで：**コード -> Codespaces -> mainで新規作成**

![コードスペース作成ボタンが表示されたダイアログ](../../../translated_images/ja/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 シークレットの追加

1. ⚙️ ギアアイコン -> コマンドパレット -> Codespaces：ユーザーシークレット管理 -> 新しいシークレットを追加。
2. 名前を OPENAI_API_KEY とし、あなたのキーを貼り付けて保存。

### 3. 次に何をする？

| したいこと                   | 移動先                                                             |
|-----------------------------|--------------------------------------------------------------------|
| レッスン1を始める             | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md) |
| オフラインで作業する           | [`setup-local.md`](02-setup-local.md)                              |
| LLMプロバイダーを設定する      | [`providers.md`](03-providers.md)                                   |
| 他の学習者と交流する            | [私たちのDiscordに参加する](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## トラブルシューティング


| 症状                                        | 修正                                                         |
|---------------------------------------------|--------------------------------------------------------------|
| コンテナのビルドが10分以上停止                 | **Codespaces ➜ 「Rebuild Container」**                          |
| `python: command not found`                   | ターミナルが接続されていません。**+** をクリックし *bash* を選択  |
| OpenAIからの `401 Unauthorized`                | `OPENAI_API_KEY` が間違っているか期限切れ                          |
| VS Codeで「Dev container mounting…」と表示される   | ブラウザタブをリフレッシュ—Codespacesが接続を失うことがあります     |
| ノートブックのカーネルが見つからない              | ノートブックメニュー ➜ **Kernel ▸ Select Kernel ▸ Python 3**   |

   Unix系システム：

   ```bash
   touch .env
   ```

   Windows：

   ```cmd
   echo . > .env
   ```

3. **`.env` ファイルの編集**：テキストエディター（例：VS Code、Notepad++、その他エディター）で `.env` ファイルを開き、以下の行を追加してください。実際の Microsoft Foundry Models のエンドポイントとキーに置き換えます（取得方法は[`providers.md`](03-providers.md) を参照）。

   > **注意:** GitHub Models（およびその `GITHUB_TOKEN` 変数）は2026年7月末で廃止予定です。代わりに [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) を使用してください。

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. <strong>ファイルを保存する</strong>：変更を保存してテキストエディターを閉じます。

5. **`python-dotenv` をインストール**：まだインストールしていない場合、`.env` ファイルから環境変数を Python アプリケーションに読み込むために `python-dotenv` パッケージをインストールしてください。`pip` を使ってインストールできます：

   ```bash
   pip install python-dotenv
   ```

6. **Pythonスクリプトで環境変数を読み込む**：Pythonスクリプト内で、`python-dotenv` パッケージを使って `.env` ファイルから環境変数を読み込みます：

   ```python
   from dotenv import load_dotenv
   import os

   # .envファイルから環境変数を読み込む
   load_dotenv()

   # Microsoft Foundry Modelsの変数にアクセスする
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

以上です！ `.env` ファイルを作成し、Microsoft Foundry Models の認証情報を追加し、Python アプリケーションに読み込むことができました。

## ローカルコンピューターでの実行方法

ローカルでコードを実行するには、何らかのバージョンの [Pythonがインストールされている](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) 必要があります。

その後、リポジトリをクローンする必要があります：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

すべてチェックアウトできたら、すぐに始められます！

## 任意のステップ

### Minicondaのインストール

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) は、[Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python、いくつかのパッケージをインストールするための軽量インストーラーです。
Conda自体はパッケージマネージャーで、異なるPythonの[<strong>仮想環境</strong>](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)やパッケージを簡単にセットアップ・切り替えができます。また、`pip` で入手できないパッケージのインストールにも便利です。

[MiniCondaインストールガイド](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) を参照してセットアップしてください。

Minicondaをインストールしたら、[リポジトリ](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) をクローンします（もしまだの場合）。

次に、仮想環境を作成する必要があります。Condaで行う場合、環境ファイル（_environment.yml_）を作成します。Codespacesを使っている場合は、`.devcontainer` フォルダー内に `.devcontainer/environment.yml` として作成してください。

以下のスニペットで環境ファイルを作成してください：

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

Condaでエラーが発生した場合は、ターミナルで以下のコマンドでMicrosoft AIライブラリを手動でインストールできます。

```
conda install -c microsoft azure-ai-ml
```

環境ファイルは必要な依存関係を指定します。`<environment-name>` はあなたが使いたいConda環境名で、`<python-version>` は使用するPythonのバージョンです。例えば `3` はPythonの最新メジャーバージョンです。

これで準備ができたら、以下のコマンドでConda環境を作成します：

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer サブパスは Codespace セットアップのみに適用されます
conda activate ai4beg
```

問題があれば[Conda環境ガイド](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)を参照してください。

### Pythonサポート拡張機能付きVisual Studio Codeの使用

このコースでは [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) エディターに [Pythonサポート拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) をインストールして使うことを推奨します。ただしこれは必須ではありません。

> <strong>注意</strong>: コースリポジトリをVS Codeで開くと、コンテナ内でプロジェクトをセットアップできるオプションがあります。これはコースリポジトリ内の[特別な `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) ディレクトリによるものです。詳細は後ほど説明します。

> <strong>注意</strong>: リポジトリをクローンしVS Codeで開くと、自動的にPythonサポート拡張機能のインストールを提案されます。

> <strong>注意</strong>: VS Code によるリポジトリのコンテナでの再オープン提案は、ローカルのPythonを使う場合は拒否してください。

### ブラウザでのJupyterの使用

ブラウザ内で [Jupyter環境](https://jupyter.org?WT.mc_id=academic-105485-koreyst) を使ってプロジェクトに取り組むこともできます。クラシックJupyterや [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) は、オートコンプリートやコードハイライトなどの機能で快適な開発環境を提供します。

ローカルでJupyterを起動するには、端末/コマンドラインでコースディレクトリに移動し、次のコマンドを実行します：

```bash
jupyter notebook
```

または

```bash
jupyterhub
```

これによりJupyterのインスタンスが起動し、アクセス用のURLがコマンドライン上に表示されます。

URLにアクセスすると、コースのアウトラインが表示され、任意の `*.ipynb` ファイルへ移動できます。例：`08-building-search-applications/python/oai-solution.ipynb`。

### コンテナーでの実行

コンピューターやCodespaceにすべてセットアップする代わりに、[コンテナ](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)を使用する方法もあります。コースリポジトリ内の特別な `.devcontainer` フォルダにより、VS Codeはコンテナ内でプロジェクトをセットアップ可能です。Codespaces以外でこれを行うにはDockerをインストールしなければならず、正直言って少々複雑なので、コンテナ操作に慣れている方のみお勧めします。

GitHub CodespacesでAPIキーを安全に保持する最良の方法の一つがCodespaceのシークレット機能の使用です。詳細は [Codespacesシークレット管理ガイド](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) をご参照ください。


## レッスンと技術要件

このコースには6つのコンセプトレッスンと6つのコーディングレッスンがあります。

コーディングレッスンではAzure OpenAIサービスを利用します。コードを実行するにはAzure OpenAIサービスへのアクセスとAPIキーが必要です。アクセス申請は [こちらの申請フォーム](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) から行えます。

申請処理中に待つ間も、各コーディングレッスンにはコードと出力を確認できる `README.md` ファイルが含まれています。

## Azure OpenAIサービスを初めて使う場合

Azure OpenAIサービスを初めて使う場合は、こちらのガイドに従って [Azure OpenAIサービスリソースの作成と展開](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) を行ってください。

## OpenAI APIを初めて使う場合

OpenAI APIを初めて使う場合は、こちらのガイドに従って [インターフェースの作成と使用](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst) を行ってください。

## 他の学習者と交流する

公式の [AIコミュニティDiscordサーバー](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) にて、他の学習者と交流できるチャンネルを用意しています。ここは、志を同じくする起業家、開発者、学生、そして生成AIのスキルアップを目指す皆が交流するのに最適な場所です。

[![discordチャンネルに参加する](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

プロジェクトチームもこのDiscordサーバーに参加しており、学習者のサポートを行います。

## 貢献について

このコースはオープンソースの取り組みです。改善点や問題点があれば、[プルリクエスト](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)の作成や[GitHubのイシュー](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)の報告をお願いします。

プロジェクトチームはすべての貢献を追跡しています。オープンソースへの貢献は生成AIでのキャリア構築に素晴らしい方法です。

ほとんどの貢献には、貢献物を使用する権利を実際に持っており、私たちにその権利を付与することに同意する貢献者ライセンス契約（CLA）への同意が必要です。詳細は [CLA、Contributor License Agreement ウェブサイト](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst) をご覧ください。

重要：このリポジトリ内のテキストを翻訳する際は、機械翻訳の利用は避けてください。翻訳はコミュニティによって検証されるため、翻訳に精通している言語のみで翻訳ボランティアをお願いします。

プルリクエストを提出すると、CLAボットが自動でCLAの提出が必要かどうかを判断し、PRに適切なラベルやコメントが付加されます。ボットの指示に従ってください。CLAはすべてのリポジトリで一度だけ対応すれば十分です。


このプロジェクトは [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) を採用しています。詳細については、Code of Conduct FAQをお読みいただくか、ご質問やご意見がありましたら [Email opencode](opencode@microsoft.com) にお問い合わせください。

## 始めましょう

このコースを完了するために必要な手順を終えたので、まずは [introduction to Generative AI and LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) から始めましょう。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->