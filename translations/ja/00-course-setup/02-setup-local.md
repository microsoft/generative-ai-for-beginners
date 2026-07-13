# ローカルセットアップ 🖥️

**すべてを自分のノートパソコンで実行したい場合は、このガイドを使ってください。**   
選択肢は2つあります：**(A) ネイティブPython + virtual-env** または **(B) Dockerを使ったVS Code Dev Container**。  
どちらでも同じレッスンに到達しますので、簡単に感じるほうを選んでください。

## 1. 前提条件

| ツール               | バージョン / 注意事項                                                         |
|--------------------|-------------------------------------------------------------------------------|
| **Python**         | 3.10以上（<https://python.org>から取得）                                      |
| **Git**            | 最新（Xcode / Git for Windows / Linuxのパッケージマネージャに付属）           |
| **VS Code**        | 任意ですが推奨 <https://code.visualstudio.com>                               |
| **Docker Desktop** | *オプションBのみ* 。無料インストール：<https://docs.docker.com/desktop/>     |

> 💡 <strong>ヒント</strong> – ターミナルでツールを確認：  
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

✅ プロンプトが (.venv) で始まるようになれば、環境内にいることを意味します。

### ステップ3 依存関係をインストール

```bash
pip install -r requirements.txt
```

[APIキーの追加](#3-apiキーの追加) セクション3へスキップ可能

## 2. オプションB – VS Code Dev Container（Docker）

このリポジトリとコースは、Python3、.NET、Node.js、Java開発をサポートできるユニバーサルランタイムを含む[開発用コンテナ](https://containers.dev?WT.mc_id=academic-105485-koreyst)を使用して構成されています。関連設定はこのリポジトリのルートにある `.devcontainer/` フォルダ内の `devcontainer.json` ファイルに記述されています。

>**なぜこれを選ぶの？**
>Codespacesと同一環境で依存関係のずれが起きません。

### ステップ0 追加のインストール

Docker Desktop – ```docker --version``` が動作することを確認してください。
VS Code Remote – Containers拡張機能（ID: ms-vscode-remote.remote-containers）。

### ステップ1 VS Codeでリポジトリを開く

ファイル ▸ フォルダーを開く…  → generative-ai-for-beginners

VS Codeが .devcontainer/ を検出してプロンプトを表示します。

### ステップ2 コンテナで再オープン

「Reopen in Container」をクリック。Dockerがイメージをビルドします（初回は約3分）。
ターミナルプロンプトが表示されたら、コンテナ内にいます。

## 2. オプションC – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) は [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python、およびいくつかのパッケージをインストールするための軽量インストーラーです。
Conda自体はパッケージマネージャであり、異なるPythonの[<strong>仮想環境</strong>](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)やパッケージを簡単に設定・切り替えできます。また、`pip`では利用できないパッケージをインストールする際にも役立ちます。

### ステップ0 Minicondaのインストール

[MiniCondaインストールガイド](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst)に従ってセットアップしてください。

```bash
conda --version
```

### ステップ1 仮想環境ファイルを作成

新しい環境ファイル(*environment.yml*)を作成します。Codespacesを利用している場合は、`.devcontainer`ディレクトリ内、つまり `.devcontainer/environment.yml` に作成してください。

### ステップ2 環境ファイルの内容を記述

下記スニペットを `environment.yml` に追加します

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

### ステップ3 Conda環境の作成

以下のコマンドをコマンドライン/ターミナルで実行します

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer サブパスは Codespace の設定にのみ適用されます
conda activate ai4beg
```

問題があれば [Conda環境のガイド](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)を参照してください。

## 2. オプションD – クラシックJupyter / Jupyter Lab（ブラウザ上）

> **誰向け？**  
> クラシックなJupyterインターフェースが好きな人、VS Codeを使わずにノートブックを実行したい人向け。  

### ステップ1 Jupyterがインストールされていることを確認

Jupyterをローカルで起動するには、ターミナル/コマンドラインでコースディレクトリに移動し、次を実行します：

```bash
jupyter notebook
```

または

```bash
jupyterhub
```

これによりJupyterインスタンスが起動し、アクセス用URLがコマンドラインウィンドウに表示されます。

URLにアクセスすると、コース概要が表示され、`*.ipynb` ファイルを自由に開けます。例えば、`08-building-search-applications/python/oai-solution.ipynb`。

## 3. APIキーの追加

どの種類のアプリケーションを開発する場合でも、APIキーを安全に管理することは重要です。APIキーをコード内に直接保存することは推奨しません。公開リポジトリに鍵情報をコミットすると、セキュリティ問題や悪用による不要な請求が発生する可能性があります。
Microsoft Foundry Modelsの認証情報をPythonの`.env`ファイルに作成し追加する手順を以下に説明します。

> **注意:** GitHub Models（およびその `GITHUB_TOKEN` 変数）は2026年7月末で終了します。このガイドでは代わりに[Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)を使用します。完全オフライン作業を希望する方は[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)を参照してください。

1. <strong>プロジェクトディレクトリへ移動</strong>：ターミナルやコマンドプロンプトで、`.env`ファイルを作成するプロジェクトのルートディレクトリに移動します。

   ```bash
   cd path/to/your/project
   ```

2. **`.env`ファイルを作成**：お好みのテキストエディタで新しいファイル `.env` を作成します。コマンドラインを使う場合は、Unix系システムでは `touch` コマンド、Windowsでは `echo` コマンドを使えます：

   Unix系システム：

   ```bash
   touch .env
   ```

   Windows：

   ```cmd
   echo . > .env
   ```

3. **`.env`ファイルを編集**：テキストエディタ（例：VS Code、Notepad++など）で `.env` を開き、Microsoft FoundryプロジェクトのエンドポイントとAPIキーに置き換えて、以下の行を追加します：

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. <strong>ファイルを保存</strong>：編集内容を保存してテキストエディタを閉じます。

5. **`python-dotenv`をインストール**：まだの場合、`.env`から環境変数をPythonへ読み込むために `python-dotenv` パッケージをインストールします。`pip`でインストール可能です：

   ```bash
   pip install python-dotenv
   ```

6. **Pythonスクリプトで環境変数を読み込み**：Pythonスクリプト内で `python-dotenv` パッケージを使って `.env` ファイルから環境変数をロードします：

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

これで完了です！`.env`ファイルを作成し、Microsoft Foundry Modelsの認証情報を追加し、Pythonアプリケーションに読み込ませることができました。

🔐 `.env`は絶対にコミットしないでください。すでに `.gitignore` に含まれています。
プロバイダーごとの詳細手順は [`providers.md`](03-providers.md) にあります。

## 4. 次は何をする？

| したいこと                 | 行き先                                                              |
|-------------------------|--------------------------------------------------------------------|
| レッスン1を始める         | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md) |
| LLMプロバイダーを設定する | [`providers.md`](03-providers.md)                                   |
| 他の学習者と交流する       | [Discordに参加](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)  |

## 5. トラブルシューティング

| 症状                                     | 対応策                                                               |
|----------------------------------------|---------------------------------------------------------------------|
| `python not found`                     | PythonをPATHに追加するか、インストール後にターミナルを再起動する      |
| `pip`がホイールをビルドできない (Windows) | `pip install --upgrade pip setuptools wheel` を実行後、再試行         |
| `ModuleNotFoundError: dotenv`          | `pip install -r requirements.txt` を実行（環境がインストールされていない場合）|
| Dockerビルド失敗 *No space left*       | Docker Desktop ▸ *Settings* ▸ *Resources* → ディスクサイズを増やす       |
| VS Codeが繰り返し再オープンを促す       | 両方のオプションが有効かもしれません。どちらか一方(venv <strong>または</strong> container)を選択|
| OpenAI 401 / 429 エラー                 | `OPENAI_API_KEY` の値やリクエストのレート制限を確認                    |
| Conda使用時のエラー                    | Microsoft AIライブラリを `conda install -c microsoft azure-ai-ml` でインストール |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->