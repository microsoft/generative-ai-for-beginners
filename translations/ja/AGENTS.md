# AGENTS.md

## プロジェクト概要

このリポジトリには、生成AIの基礎と応用開発を教える21回の包括的なカリキュラムが含まれています。このコースは初心者向けに設計されており、基本概念から本番対応アプリケーションの構築までを網羅しています。

**主要技術：**
- ライブラリ付きPython 3.9+：`openai`、`python-dotenv`、`tiktoken`、`azure-ai-inference`、`pandas`、`numpy`、`matplotlib`
- Node.js用TypeScript/JavaScriptとライブラリ：`openai`（Azure OpenAIのv1エンドポイント+Responses API）、`@azure-rest/ai-inference`（Microsoft Foundry Models）
- Azure OpenAI Service、OpenAI API、Microsoft Foundry Models（GitHub Modelsは2026年7月末で廃止予定）
- インタラクティブラーニング用Jupyterノートブック
- 一貫した開発環境のためのDev Containers

**リポジトリ構成：**
- 21の番号付きレッスンディレクトリ（00-21）にはREADME、コード例、課題を含む
- 複数の実装：Python、TypeScript、時に.NET例
- 40以上の言語版を含むtranslationsディレクトリ
- `.env`ファイルによる集中設定（テンプレートとして`.env.copy`を使用）

## セットアップコマンド

### 初期リポジトリセットアップ

```bash
# リポジトリをクローンする
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# 環境テンプレートをコピーする
cp .env.copy .env
# APIキーとエンドポイントを含む.envファイルを編集する
```

### Python環境セットアップ

```bash
# 仮想環境を作成する
python3 -m venv venv

# 仮想環境を有効にする
# macOS/Linuxの場合：
source venv/bin/activate
# Windowsの場合：
venv\Scripts\activate

# 依存関係をインストールする
pip install -r requirements.txt
```

### Node.js/TypeScriptセットアップ

```bash
# ルートレベルの依存関係をインストールします（ドキュメント用ツールのため）
npm install

# 個々のレッスンのTypeScript例については、特定のレッスンに移動してください：
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Containerセットアップ（推奨）

このリポジトリにはGitHub CodespacesやVS Code Dev Containers用の`.devcontainer`設定が含まれています：

1. GitHub CodespacesまたはDev Containers拡張付きVS Codeでリポジトリを開く
2. Dev Containerが自動的に以下を行います：
   - `requirements.txt`からPython依存関係をインストール
   - ポストクリエイトスクリプト（`.devcontainer/post-create.sh`）を実行
   - Jupyterカーネルをセットアップ

## 開発ワークフロー

### 環境変数

APIアクセスを必要とするすべてのレッスンは`.env`で定義された環境変数を使用します：

- `OPENAI_API_KEY` - OpenAI API用
- `AZURE_OPENAI_API_KEY` - Microsoft FoundryのAzure OpenAI用（Azure OpenAI Serviceは現在Microsoft Foundryの一部です: https://ai.azure.com）
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAIエンドポイントURL（Foundryリソースエンドポイント）
- `AZURE_OPENAI_DEPLOYMENT` - チャット完了モデルのデプロイ名（コースデフォルト：`gpt-5-mini`）
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - 埋め込みモデルのデプロイ名（コースデフォルト：`text-embedding-3-small`）
- `AZURE_OPENAI_API_VERSION` - APIバージョン（デフォルト：`2024-10-21`）
- `HUGGING_FACE_API_KEY` - Hugging Faceモデル用
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry Modelsエンドポイント（マルチプロバイダモデルカタログ）
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry Models APIキー（廃止予定の`GITHUB_TOKEN`に代わるもの）
- `AZURE_INFERENCE_CHAT_MODEL` - サンプリング制御をサポートしない推論モデル以外のモデル（例：`Llama-3.3-70B-Instruct`）、`temperature`例で使用

### モデルの慣例（重要）

- **デフォルトチャットモデルは`gpt-5-mini`<strong> - 現行の非廃止済みの</strong>推論**モデル。2026年時点で古い`gpt-4o-mini`、`gpt-4.1-mini`の温度対応モデルは<em>廃止予定</em>なので、カリキュラムはGPT-5系に標準化しています。
- **推論モデルは`temperature`や`top_p`を拒否**し、`max_output_tokens`（Responses API）/`max_completion_tokens`（チャット完了）を`max_tokens`の代わりに使用しています。`gpt-5-mini`を呼び出すサンプルには`temperature`/`top_p`/`max_tokens`を追加しないでください。
- **`temperature`を示すために<strong>、サンプルはMicrosoft Foundry Modelsエンドポイントの</strong>Llama**モデル（`Llama-3.3-70B-Instruct`）を使用し（`AZURE_INFERENCE_CHAT_MODEL`）、推論モデルはプロンプトエンジニアリング＋推論制御で操作し、サンプリングノブは使いません。
- <strong>ファインチューニング（レッスン18）</strong>は`gpt-4.1-mini`を保持：GPT-5は強化学習ファインチューニング（RFT）のみ対応し、そこで示された教師ありファインチューニング（SFT）は非対応です。
- レッスン20（Mistral）と21（Meta）は`temperature`/`max_tokens`を保持、対象モデルであるMistral/Llamaはこれをサポートしています。

### Python例の実行方法

```bash
# レッスンディレクトリに移動する
cd 06-text-generation-apps/python

# Pythonスクリプトを実行する
python aoai-app.py
```

### TypeScript例の実行方法

```bash
# TypeScriptアプリのディレクトリに移動する
cd 06-text-generation-apps/typescript/recipe-app

# TypeScriptコードをビルドする
npm run build

# アプリケーションを実行する
npm start
```

### Jupyterノートブックの実行方法

```bash
# リポジトリのルートでJupyterを開始する
jupyter notebook

# またはJupyter拡張機能を使用してVS Codeを使用する
```

### 複数タイプのレッスンでの作業

- **「学ぶ」レッスン**：README.mdのドキュメントと概念に注力
- **「作る」レッスン**：PythonとTypeScriptの動作するコード例を含む
- 各レッスンには理論、コード解説、ビデオリンクを含むREADME.mdがある

## コードスタイルガイドライン

### Python

- 環境変数管理に`python-dotenv`を使用
- API操作に`openai`ライブラリをインポート
- リンターに`pylint`を使用（一部例では簡易のため`# pylint: disable=all`あり）
- PEP 8のネーミング規約に従う
- API認証情報は`.env`に保存し、コード内には記述しない

### TypeScript

- 環境変数に`dotenv`パッケージを使用
- 各アプリで`tsconfig.json`にてTypeScript設定
- Azure OpenAIには`openai`パッケージ（クライアントを`/openai/v1/`エンドポイントに設定し`client.responses.create`呼び出し）、Microsoft Foundry Modelsには`@azure-rest/ai-inference`を使用
- 開発には`nodemon`で自動リロード
- 実行前に`npm run build`、次に`npm start`

### 一般的慣例

- コード例はシンプルかつ教育的に
- 主要概念はコメントで説明
- 各レッスンのコードは自己完結的で実行可能
- Azure OpenAIには`aoai-`プレフィックス、OpenAI APIには`oai-`、Microsoft Foundry Modelsには`githubmodels-`プレフィックス（GitHub Models時代からのレガシーネーム）を使う

## ドキュメントガイドライン

### Markdownスタイル

- URLはすべて`[text](../../url)`形式で余分なスペースなしに記述
- 相対リンクは`./`または`../`から始める
- Microsoftドメインのリンクには追跡ID`?WT.mc_id=academic-105485-koreyst`を必ず含める
- 国別ロケールはURLに含めない（例：`/en-us/`は避ける）
- 画像は`./images`フォルダーに説明的な名前で保存
- ファイル名は英数字とダッシュのみ使用

### 翻訳サポート

- リポジトリは40言語以上のGitHub Actionsによる自動翻訳をサポート
- 翻訳は`translations/`ディレクトリに格納
- 部分翻訳は提出しない
- 機械翻訳は受け付けない
- 翻訳済み画像は`translated_images/`ディレクトリに保存

## テストと検証

### 提出前チェック

このリポジトリは検証にGitHub Actionsを使用しています。PRを提出する前に：

1. **Markdownリンクをチェック**：
   ```bash
   # validate-markdown.yml ワークフローは以下をチェックします:
   # - 壊れた相対パス
   # - パスのトラッキングIDの欠如
   # - URLのトラッキングIDの欠如
   # - 国別ロケール付きURL
   # - 壊れた外部URL
   ```

2. <strong>手動テスト</strong>：
   - Python例をテスト：仮想環境をアクティブにしてスクリプトを実行
   - TypeScript例をテスト：`npm install`、`npm run build`、`npm start`
   - 環境変数が正しく設定されているか確認
   - APIキーがコード例で機能するか確認

3. <strong>コード例</strong>：
   - 全てのコードがエラーなしで動作するか確認
   - 対応する場合はAzure OpenAIとOpenAI API両方でテスト
   - Microsoft Foundry Models対応例も検証

### 自動化テストは無し

このリポジトリはチュートリアルと例に焦点を当てた教育用で、ユニットテストや統合テストはありません。検証は主に：
- コード例の手動テスト
- Markdown検証のためのGitHub Actions
- 教育コンテンツのコミュニティレビュー

## プルリクエストガイドライン

### 提出前に

1. 可能な場合はPythonとTypeScript両方でコード変更をテスト
2. Markdown検証を実行（PRで自動トリガー）
3. MicrosoftのURLに追跡IDがあることを確認
4. 相対リンクが正しいことを確認
5. 画像の参照が正しいか確認

### PRタイトル形式

- 説明的なタイトルを使う：例 `[Lesson 06] Python例のタイポ修正` または `レッスン08のREADME更新`
- 該当する場合はイシュー番号を参照：`Fixes #123`

### PR説明

- 何が変更され、なぜかを説明
- 関連するイシューへのリンク
- コード変更の場合、どの例をテストしたかを明記
- 翻訳PRの場合は完全な翻訳のためすべてのファイルを含める

### 貢献要件

- Microsoft CLAに署名（初回PRで自動的に）
- 変更前にリポジトリをフォーク
- 論理的な変更ごとに1つのPR（無関係な修正をまとめない）
- 可能な限りPRは集中かつ小規模に保つ

## よくあるワークフロー

### 新しいコード例の追加

1. 該当のレッスンディレクトリに移動
2. `python/` または `typescript/` サブディレクトリに例を作成
3. 命名規則に従う：`{provider}-{example-name}.{py|ts|js}`
4. 実際のAPI認証情報でテスト
5. 新しい環境変数があればレッスンREADMEに記述

### ドキュメントの更新

1. レッスンディレクトリのREADME.mdを編集
2. Markdownガイドラインに従う（追跡ID、相対リンク）
3. 翻訳はGitHub Actionsで処理（手動編集禁止）
4. リンクがすべて有効かテスト

### Dev Containersの利用

1. リポジトリには`.devcontainer/devcontainer.json`が含まれる
2. ポストクリエイトスクリプトでPython依存関係自動インストール
3. PythonとJupyter用の拡張が事前設定済み
4. 環境は`mcr.microsoft.com/devcontainers/universal:2.11.2`ベース

## デプロイと公開

これは学習用リポジトリであり、デプロイプロセスはありません。カリキュラムは以下で利用されます：

1. **GitHubリポジトリ**：コードとドキュメントに直接アクセス
2. **GitHub Codespaces**：事前設定済みの即時開発環境
3. **Microsoft Learn**：公式学習プラットフォームへ配信される可能性
4. **docsify**：Markdownから構築されたドキュメントサイト（`docsifytopdf.js`と`package.json`を参照）

### ドキュメントサイトの構築

```bash
# ドキュメントからPDFを生成（必要に応じて）
npm run convert
```

## トラブルシューティング

### よくある問題

**Pythonインポートエラー**：
- 仮想環境がアクティブか確認
- `pip install -r requirements.txt`を実行
- Pythonバージョンが3.9以上か確認

**TypeScriptビルドエラー**：
- 該当アプリディレクトリで`npm install`を実行
- Node.jsバージョンが対応しているか確認
- `node_modules`をクリアし再インストールを試みる

**API認証エラー**：
- `.env`ファイルが存在し正しい値か確認
- APIキーが有効か期限切れでないか確認
- エンドポイントURLが地域に合っているか確認

<strong>環境変数が不足している場合</strong>：
- `.env.copy`を`.env`にコピー
- 作業中のレッスンに必要な値をすべて填入
- `.env`を更新後アプリを再起動

## 追加リソース

- [Course Setup Guide](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Contributing Guidelines](./CONTRIBUTING.md)
- [Code of Conduct](./CODE_OF_CONDUCT.md)
- [Security Policy](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Collection of Advanced Code Samples](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## プロジェクト特記事項

- これは<strong>教育用リポジトリ</strong>であり、本番コードではありません
- 例は意図的にシンプルで概念理解に集中しています
- コードの品質は教育的明瞭性とバランスを取っています
- 各レッスンは自己完結型で独立して完了可能
- 複数のAPIプロバイダをサポート：Azure OpenAI、OpenAI、Microsoft Foundry Models、Foundry LocalやOllamaなどのオフラインプロバイダも含む
- コンテンツは多言語対応で自動翻訳ワークフローを採用
- Discord上に活発なコミュニティがあり、質問やサポートが可能

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->