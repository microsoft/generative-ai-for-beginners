<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T15:04:22+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "ja"
}
-->
# ローカルセットアップ 🖥️

**すべて自分のパソコンで動かしたい場合はこのガイドを使ってください。**  
方法は2つあります：**(A) ネイティブPython + virtual-env** または **(B) VS Code Dev Container（Docker使用）**。  
どちらでもOKです。好きな方を選んでください。どちらも同じレッスンに進めます。

## 1. 必要なもの

| ツール               | バージョン / 備考                                                                      |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10以上（<https://python.org> から入手）                                            |
| **Git**            | 最新版（Xcode / Git for Windows / Linuxパッケージマネージャーに付属）                   |
| **VS Code**        | 任意ですが推奨 <https://code.visualstudio.com>                             |
| **Docker Desktop** | *Bの方法のみ* 必要。無料インストール: <https://docs.docker.com/desktop/>                |

> 💡 **Tip** – ターミナルでツールのバージョン確認:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  オプションA – ネイティブPython（最速）

### Step 1  このリポジトリをクローン

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Step 2 仮想環境を作成して有効化

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ プロンプトの先頭に (.venv) が表示されていれば、仮想環境に入っています。

### Step 3 依存パッケージをインストール

```bash
pip install -r requirements.txt
```

[APIキー](../../../00-course-setup) のセクション3へ進んでください。

## 2. オプションB – VS Code Dev Container（Docker）

このリポジトリとコースは[開発コンテナ](https://containers.dev?WT.mc_id=academic-105485-koreyst)でセットアップされています。Universalランタイムが入っており、Python3、.NET、Node.js、Javaの開発が可能です。関連する設定はリポジトリのルートにある `.devcontainer/` フォルダ内の `devcontainer.json` で定義されています。

>**なぜこれを選ぶ？**
>Codespacesと同じ環境で、依存関係のズレがありません。

### Step 0 追加ツールのインストール

Docker Desktop – ```docker --version``` が動くか確認してください。  
VS Code Remote – Containers拡張機能（ID: ms-vscode-remote.remote-containers）。

### Step 1 VS Codeでリポジトリを開く

ファイル ▸ フォルダーを開く…  → generative-ai-for-beginners

VS Codeが .devcontainer/ を検出し、プロンプトが表示されます。

### Step 2 コンテナで再オープン

「Reopen in Container」をクリック。Dockerがイメージをビルドします（初回は約3分）。  
ターミナルのプロンプトが表示されたら、コンテナ内に入っています。

## 2.  オプションC – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) は [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python、いくつかのパッケージをインストールする軽量インストーラーです。  
Conda自体はパッケージマネージャーで、Pythonの[**仮想環境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)やパッケージの切り替えが簡単にできます。`pip`で入らないパッケージのインストールにも便利です。

### Step 0  Minicondaをインストール

[MiniCondaインストールガイド](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst)に従ってセットアップしてください。

```bash
conda --version
```

### Step 1 仮想環境ファイルを作成

新しい環境ファイル（*environment.yml*）を作成します。Codespacesを使っている場合は `.devcontainer` ディレクトリ内、つまり `.devcontainer/environment.yml` に作成してください。

### Step 2  環境ファイルに内容を追加

`environment.yml` に以下のスニペットを追加してください。

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

### Step 3 Conda環境を作成

下記コマンドをコマンドライン/ターミナルで実行してください。

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

問題が発生した場合は [Conda環境ガイド](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) を参照してください。

## 2  オプションD – クラシックJupyter / Jupyter Lab（ブラウザで実行）

> **どんな人向け？**  
> クラシックなJupyterインターフェースが好きな方や、VS Codeを使わずにノートブックを動かしたい方。

### Step 1  Jupyterがインストールされているか確認

Jupyterをローカルで起動するには、ターミナル/コマンドラインでコースディレクトリに移動し、以下を実行してください。

```bash
jupyter notebook
```

または

```bash
jupyterhub
```

これでJupyterが起動し、アクセス用のURLがコマンドラインに表示されます。

URLにアクセスすると、コースのアウトラインが表示され、任意の `*.ipynb` ファイルに移動できます。例：`08-building-search-applications/python/oai-solution.ipynb`。

## 3. APIキーを追加しよう

APIキーを安全に管理することは、どんなアプリケーションを作る場合でもとても大切です。APIキーをコード内に直接書かないようにしましょう。公開リポジトリにコミットすると、セキュリティ上の問題や、悪用された場合に思わぬコストが発生することもあります。  
ここではPython用に `.env` ファイルを作成し、`GITHUB_TOKEN` を追加する手順を紹介します。

1. **プロジェクトディレクトリに移動**: ターミナルやコマンドプロンプトで、`.env` ファイルを作成したいプロジェクトのルートディレクトリに移動します。

   ```bash
   cd path/to/your/project
   ```

2. **`.env` ファイルを作成**: 好きなテキストエディタで `.env` という新しいファイルを作成します。コマンドラインからなら、Unix系は `touch`、Windowsは `echo` を使えます。

   Unix系:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` ファイルを編集**: `.env` ファイルをテキストエディタ（例: VS Code, Notepad++ など）で開き、下記の行を追加します。`your_github_token_here` を実際のGitHubトークンに置き換えてください。

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **ファイルを保存**: 変更を保存してエディタを閉じます。

5. **`python-dotenv` をインストール**: まだインストールしていない場合は、`python-dotenv` パッケージをインストールしてください。これで `.env` ファイルからPythonアプリに環境変数を読み込めます。`pip` でインストールできます。

   ```bash
   pip install python-dotenv
   ```

6. **Pythonスクリプトで環境変数を読み込む**: Pythonスクリプト内で `python-dotenv` を使い、`.env` ファイルから環境変数を読み込みます。

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

これで完了です！`.env` ファイルを作成し、GitHubトークンを追加し、Pythonアプリで読み込めるようになりました。

🔐 .envは絶対にコミットしないでください—すでに .gitignore に含まれています。  
各プロバイダーの詳細な手順は [`providers.md`](03-providers.md) にあります。

## 4. 次は何をする？

| やりたいこと          | 進む先                                                                  |
|---------------------|-------------------------------------------------------------------------|
| レッスン1を始める      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| LLMプロバイダーを設定 | [`providers.md`](03-providers.md)                                       |
| 他の学習者と交流する | [Discordに参加](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. トラブルシューティング

| 症状                                   | 対処法                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | PythonをPATHに追加、またはインストール後にターミナルを再起動            |
| `pip` でwheelsがビルドできない（Windows）       | `pip install --upgrade pip setuptools wheel` を実行して再試行        |
| `ModuleNotFoundError: dotenv`             | `pip install -r requirements.txt` を実行（環境が未インストール）   |
| Dockerビルド失敗 *No space left*        | Docker Desktop ▸ *設定* ▸ *リソース* → ディスクサイズを増やす |
| VS Codeが再オープンを促し続ける         | 両方のオプションが有効になっている可能性あり。どちらか一方（venv **または** container）を選択|
| OpenAI 401 / 429 エラー                   | `OPENAI_API_KEY` の値やリクエストレート制限を確認             |
| Conda使用時のエラー                        | `conda install -c microsoft azure-ai-ml` でMicrosoft AIライブラリをインストール|

---

**免責事項**：  
本書類はAI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な表現が含まれる場合があります。原文（元の言語の文書）が正式な情報源として扱われるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤認についても、当方は責任を負いかねます。