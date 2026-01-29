# ローカルセットアップ 🖥️

**すべてを自分のラップトップで実行したい場合は、このガイドを使用してください。**  
2つの方法があります：**(A) ネイティブPython + virtual-env** または **(B) Dockerを使ったVS Code Dev Container**。  
どちらでも簡単に感じる方を選んでください—どちらも同じレッスンに進みます。

## 1. 前提条件

| ツール               | バージョン / 注意事項                                                                 |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10以上（<https://python.org>から入手可能）                                         |
| **Git**            | 最新（Xcode / Git for Windows / Linuxのパッケージマネージャーに含まれています）       |
| **VS Code**        | 任意ですが推奨 <https://code.visualstudio.com>                                       |
| **Docker Desktop** | *オプションBのみ*。無料インストール：<https://docs.docker.com/desktop/>               |

> 💡 **ヒント** – ターミナルでツールを確認：  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. オプションA – ネイティブPython（最速）

### ステップ1 このリポジトリをクローン

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### ステップ2 仮想環境を作成して有効化

```bash
python -m venv .venv          # 1つ作る
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ プロンプトが (.venv) で始まれば、仮想環境内にいることを意味します。

### ステップ3 依存関係をインストール

```bash
pip install -r requirements.txt
```

[APIキーの追加](../../../00-course-setup)のセクション3に進んでください。

## 2. オプションB – VS Code Dev Container（Docker）

このリポジトリとコースは、Python3、.NET、Node.js、Java開発をサポートするユニバーサルランタイムを備えた[開発コンテナ](https://containers.dev?WT.mc_id=academic-105485-koreyst)でセットアップされています。関連設定は、このリポジトリのルートにある `.devcontainer/` フォルダー内の `devcontainer.json` ファイルに定義されています。

>**なぜこれを選ぶのか？**  
>Codespacesと同一の環境で、依存関係のズレがありません。

### ステップ0 追加ツールのインストール

Docker Desktop – `docker --version` が動作することを確認。  
VS Code Remote – Containers 拡張機能（ID: ms-vscode-remote.remote-containers）。

### ステップ1 VS Codeでリポジトリを開く

ファイル ▸ フォルダーを開く… → generative-ai-for-beginners

VS Codeが .devcontainer/ を検出し、プロンプトが表示されます。

### ステップ2 コンテナ内で再オープン

「Reopen in Container」をクリック。Dockerがイメージをビルドします（初回は約3分）。  
ターミナルのプロンプトが表示されたら、コンテナ内にいます。

## 2. オプションC – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst)は、[Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python、およびいくつかのパッケージをインストールするための軽量インストーラーです。  
Conda自体はパッケージマネージャーで、異なるPythonの[**仮想環境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)やパッケージのセットアップと切り替えを簡単にします。`pip`で入手できないパッケージのインストールにも便利です。

### ステップ0 Minicondaをインストール

[MiniCondaインストールガイド](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst)に従ってセットアップしてください。

```bash
conda --version
```

### ステップ1 仮想環境を作成

新しい環境ファイル（*environment.yml*）を作成します。Codespacesを使っている場合は、`.devcontainer`ディレクトリ内に作成し、つまり `.devcontainer/environment.yml` にします。

### ステップ2 環境ファイルに内容を追加

以下のスニペットを `environment.yml` に追加してください。

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

### ステップ3 Conda環境を作成

コマンドライン/ターミナルで以下のコマンドを実行します。

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainerのサブパスはCodespaceのセットアップにのみ適用されます
conda activate ai4beg
```

問題が発生した場合は、[Conda環境ガイド](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)を参照してください。

## 2. オプションD – クラシックJupyter / Jupyter Lab（ブラウザで）

> **対象者**  
> クラシックなJupyterインターフェースが好きな方、またはVS Codeを使わずにノートブックを実行したい方。

### ステップ1 Jupyterがインストールされていることを確認

ローカルでJupyterを起動するには、ターミナル/コマンドラインでコースディレクトリに移動し、以下を実行します。

```bash
jupyter notebook
```

または

```bash
jupyterhub
```

これでJupyterインスタンスが起動し、アクセス用のURLがコマンドラインに表示されます。

URLにアクセスすると、コースのアウトラインが表示され、任意の `*.ipynb` ファイルに移動できます。例：`08-building-search-applications/python/oai-solution.ipynb`。

## 3. APIキーの追加

APIキーを安全に管理することは、どんなアプリケーションを作る上でも重要です。APIキーをコードに直接保存しないことを推奨します。公開リポジトリにコミットすると、セキュリティ問題や悪意のある利用による予期しないコストが発生する可能性があります。  
ここではPython用の `.env` ファイルを作成し、`GITHUB_TOKEN` を追加する手順を説明します。

1. **プロジェクトディレクトリに移動**：ターミナルやコマンドプロンプトを開き、`.env` ファイルを作成したいプロジェクトのルートディレクトリに移動します。

   ```bash
   cd path/to/your/project
   ```

2. **`.env` ファイルを作成**：お好みのテキストエディタで `.env` という名前の新しいファイルを作成します。コマンドラインの場合、Unix系システムでは `touch`、Windowsでは `echo` を使えます。

   Unix系システム：

   ```bash
   touch .env
   ```

   Windows：

   ```cmd
   echo . > .env
   ```

3. **`.env` ファイルを編集**：テキストエディタ（VS Code、Notepad++、その他）で `.env` ファイルを開き、以下の行を追加します。`your_github_token_here` は実際のGitHubトークンに置き換えてください。

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **ファイルを保存**：変更を保存してエディタを閉じます。

5. **`python-dotenv` をインストール**：まだインストールしていない場合は、`.env` ファイルから環境変数をPythonアプリに読み込むために `python-dotenv` パッケージをインストールします。`pip`でインストール可能です。

   ```bash
   pip install python-dotenv
   ```

6. **Pythonスクリプトで環境変数を読み込む**：Pythonスクリプト内で `python-dotenv` パッケージを使い、`.env` ファイルから環境変数を読み込みます。

   ```python
   from dotenv import load_dotenv
   import os

   # .envファイルから環境変数を読み込む
   load_dotenv()

   # GITHUB_TOKEN変数にアクセスする
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

これで完了です！ `.env` ファイルを作成し、GitHubトークンを追加し、Pythonアプリに読み込ませることができました。

🔐 `.env` は絶対にコミットしないでください—すでに `.gitignore` に含まれています。  
プロバイダーごとの詳細な手順は [`providers.md`](03-providers.md) にあります。

## 4. 次に何をする？

| やりたいこと           | 移動先                                                                 |
|---------------------|-------------------------------------------------------------------------|
| レッスン1を始める      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| LLMプロバイダーを設定  | [`providers.md`](03-providers.md)                                       |
| 他の学習者と交流する    | [Discordに参加](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. トラブルシューティング

| 症状                                      | 対処法                                                           |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | PythonをPATHに追加するか、インストール後にターミナルを再起動してください。 |
| `pip` がホイールをビルドできない（Windows） | `pip install --upgrade pip setuptools wheel` を実行してから再試行。       |
| `ModuleNotFoundError: dotenv`             | `pip install -r requirements.txt` を実行（環境がインストールされていません）。 |
| Dockerビルドで *No space left* エラー     | Docker Desktop ▸ *設定* ▸ *リソース* → ディスクサイズを増やしてください。   |
| VS Codeが再オープンを繰り返す             | 両方のオプションが有効になっている可能性があります。どちらか一方（venv **または** コンテナ）を選択してください。 |
| OpenAI 401 / 429 エラー                   | `OPENAI_API_KEY` の値とリクエスト制限を確認してください。           |
| Conda使用時のエラー                      | `conda install -c microsoft azure-ai-ml` でMicrosoft AIライブラリをインストールしてください。 |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語による文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->