# AGENTS.md

## プロジェクト概要

このリポジトリには、生成AIの基本とアプリケーション開発を教える包括的な21レッスンのカリキュラムが含まれています。このコースは初心者向けで、基本概念から本番準備が整ったアプリケーションの構築までをカバーしています。

**主要技術：**
- Python 3.9+ とライブラリ：`openai`、`python-dotenv`、`tiktoken`、`azure-ai-inference`、`pandas`、`numpy`、`matplotlib`
- TypeScript/JavaScript、Node.js とライブラリ：`openai`（Azure OpenAI v1エンドポイントおよびResponses API経由）、`@azure-rest/ai-inference`（Microsoft Foundry Models）
- Azure OpenAI Service、OpenAI API、およびMicrosoft Foundry Models（GitHub Modelsは2026年7月末で終了予定）
- 対話的学習用のJupyter Notebooks
- 一貫した開発環境のためのDev Containers

**リポジトリ構成：**
- README、コード例、課題を含む21の番号付きレッスンディレクトリ（00-21）
- 複数実装：Python、TypeScript、および時折.NETの例
- 40以上の言語版があるtranslationsディレクトリ
- `.env`ファイルによる集中管理構成（テンプレートとして`.env.copy`を使用）

## セットアップコマンド

### 初期リポジトリセットアップ

```bash
# リポジトリをクローンする
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# 環境テンプレートをコピーする
cp .env.copy .env
# 自分のAPIキーとエンドポイントで.envを編集する
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
# ルートレベルの依存関係をインストールします（ドキュメントツール用）
npm install

# 個々のレッスンのTypeScript例については、特定のレッスンに移動してください：
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Containerセットアップ（推奨）

リポジトリにはGitHub CodespacesまたはVS Code Dev Containers用の`.devcontainer`構成が含まれています：

1. GitHub CodespacesまたはDev Containers拡張機能を使ってVS Codeでリポジトリを開く
2. Dev Containerは自動的に以下を実行します：
   - `requirements.txt`からPython依存関係をインストール
   - 作成後スクリプト（`.devcontainer/post-create.sh`）を実行
   - Jupyterカーネルを設定

## 開発ワークフロー

### 環境変数

APIアクセスが必要なすべてのレッスンは、`.env`に定義された環境変数を使用します：

- `OPENAI_API_KEY` - OpenAI API用
- `AZURE_OPENAI_API_KEY` - Microsoft FoundryのAzure OpenAI用（Azure OpenAI ServiceはMicrosoft Foundryの一部：https://ai.azure.com）
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAIのエンドポイントURL（Foundryリソースエンドポイント）
- `AZURE_OPENAI_DEPLOYMENT` - チャットコンプリーションモデルのデプロイメント名
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - 埋め込みモデルデプロイメント名
- `AZURE_OPENAI_API_VERSION` - APIバージョン（デフォルト：`2024-10-21`）
- `HUGGING_FACE_API_KEY` - Hugging Faceモデル用
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry Modelsのエンドポイント（マルチプロバイダモデルカタログ）
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry Models APIキー（廃止される`GITHUB_TOKEN`の代替）

### Python例の実行

```bash
# レッスンディレクトリに移動します
cd 06-text-generation-apps/python

# Pythonスクリプトを実行します
python aoai-app.py
```

### TypeScript例の実行

```bash
# TypeScriptアプリケーションのディレクトリに移動します
cd 06-text-generation-apps/typescript/recipe-app

# TypeScriptコードをビルドします
npm run build

# アプリケーションを実行します
npm start
```

### Jupyter Notebooksの実行

```bash
# リポジトリのルートでJupyterを起動する
jupyter notebook

# またはJupyter拡張機能を使ってVS Codeを使用する
```

### レッスンタイプごとの作業方法

- **「Learn」レッスン**：README.mdドキュメントと概念に焦点を当てる
- **「Build」レッスン**：PythonおよびTypeScriptの実用的コード例を含む
- 各レッスンには理論、コード解説、ビデオコンテンツへのリンクを含むREADME.mdがある

## コードスタイルガイドライン

### Python

- 環境変数管理に`python-dotenv`を使用
- API連携に`openai`ライブラリをインポート
- Lintingに`pylint`を使用（一部の例は簡略化のために`# pylint: disable=all`を含む）
- PEP 8の命名規則に従う
- API認証情報は`.env`ファイルに保存し、コード内に書かない

### TypeScript

- 環境変数に`dotenv`パッケージを使用
- 各アプリの`tsconfig.json`でTypeScript構成
- Azure OpenAI用に`openai`パッケージ（クライアントは`/openai/v1/`エンドポイントを指し、`client.responses.create`を呼ぶ）；Microsoft Foundry Models用に`@azure-rest/ai-inference`を使用
- 自動リロードに`nodemon`を使って開発
- 実行前にビルド：`npm run build` の後に `npm start`

### 一般的な規約

- コード例はシンプルで教育的に保つ
- 主要概念を説明するコメントを含める
- 各レッスンのコードは独立していて実行可能であること
- 命名規則は一貫して使用：Azure OpenAIは`aoai-`プレフィックス、OpenAI APIは`oai-`、Microsoft Foundry Modelsは`githubmodels-`（GitHub Models時代からのレガシープレフィックス）

## ドキュメントガイドライン

### Markdownスタイル

- すべてのURLは`[text](../../url)`形式でラップし、余分なスペースを入れない
- 相対リンクは`./`または`../`で始める
- MicrosoftドメインへのすべてのリンクにトラッキングIDを含めること：`?WT.mc_id=academic-105485-koreyst`
- URLに国別ロケールを含めない（`/en-us/`は避ける）
- 画像は`./images`フォルダーに記述的な名前で保存
- ファイル名に英数字とダッシュを使用

### 翻訳サポート

- リポジトリはGitHub Actionsによる40以上の言語をサポート
- 翻訳は`translations/`ディレクトリに保存
- 部分翻訳は提出しないでください
- 機械翻訳は受け付けない
- 翻訳済み画像は`translated_images/`フォルダーに保存

## テストと検証

### 提出前チェック

このリポジトリはGitHub Actionsを使用して検証を行います。PR提出前に：

1. **Markdownリンクのチェック**：
   ```bash
   # validate-markdown.yml ワークフローは以下をチェックします：
   # - 壊れた相対パス
   # - パスに追跡IDがない
   # - URLに追跡IDがない
   # - 国別ロケールを含むURL
   # - 壊れた外部URL
   ```

2. <strong>手動テスト</strong>：
   - Python例のテスト：venvを有効にしてスクリプトを実行
   - TypeScript例のテスト：`npm install`、`npm run build`、`npm start`
   - 環境変数の設定を確認
   - APIキーがコード例で機能するか確認

3. <strong>コード例</strong>：
   - すべてのコードがエラーなしに動作すること
   - 該当する場合、Azure OpenAIとOpenAI APIの両方でテスト
   - サポートされているMicrosoft Foundry Modelsでも動作を検証

### 自動テストなし

本リポジトリはチュートリアルと例に焦点を当てた教育用です。単体テストや統合テストはありません。検証は主に：
- コード例の手動テスト
- MarkdownのGitHub Actionsによる検証
- 教育コンテンツのコミュニティレビュー

## プルリクエストガイドライン

### 提出前に

1. 適用可能な場合、PythonとTypeScriptの両方でコード変更をテスト
2. Markdown検証を実行（PR作成時に自動トリガーされます）
3. すべてのMicrosoftのURLにトラッキングIDが含まれていることを確認
4. 相対リンクが有効であることを確認
5. 画像が正しく参照されていることを確認

### PRタイトルフォーマット

- 説明的なタイトルを使用：`[Lesson 06] Fix Python example typo` または `Update README for lesson 08`
- 適用可能な場合はissue番号を参照：`Fixes #123`

### PR説明

- 変更内容と理由を説明
- 関連するissueへのリンク
- コード変更の場合、テストした例を指定
- 翻訳PRの場合、完全な翻訳のため全ファイルを含める

### 貢献要件

- Microsoft CLAに署名（初回PR時に自動処理）
- 変更前にリポジトリを自分のアカウントにFork
- 1つの論理変更につき1つのPR（無関係な修正をまとめない）
- 可能な限りPRはフォーカスして小さくする

## よくあるワークフロー

### 新しいコード例の追加

1. 該当レッスンディレクトリに移動
2. `python/` または `typescript/` サブディレクトリに例を作成
3. 命名規則に従う：`{provider}-{example-name}.{py|ts|js}`
4. 実際のAPI認証情報でテスト
5. 新しい環境変数はレッスンのREADMEに記載

### ドキュメントの更新

1. レッスンディレクトリ内のREADME.mdを編集
2. Markdownガイドライン（トラッキングID、相対リンク）に従う
3. 翻訳の更新はGitHub Actionsで処理（手動編集しない）
4. すべてのリンクが有効かテスト

### Dev Containersを使った作業

1. リポジトリに`.devcontainer/devcontainer.json`が含まれている
2. 作成後スクリプトでPython依存関係を自動インストール
3. PythonとJupyter用の拡張機能が事前設定済み
4. 環境は`mcr.microsoft.com/devcontainers/universal:2.11.2`ベース

## 展開と公開

これは学習用リポジトリで、展開プロセスはありません。カリキュラムは以下を通じて提供されます：

1. **GitHubリポジトリ**：コードとドキュメントに直接アクセス
2. **GitHub Codespaces**：事前設定された即時開発環境
3. **Microsoft Learn**：公式学習プラットフォームへのコンテンツ配信の可能性あり
4. **docsify**：Markdownから生成されるドキュメントサイト（`docsifytopdf.js`と`package.json`を参照）

### ドキュメントサイトのビルド

```bash
# ドキュメントからPDFを生成する（必要な場合）
npm run convert
```

## トラブルシューティング

### よくある問題

**Pythonのインポートエラー**：
- 仮想環境がアクティブか確認する
- `pip install -r requirements.txt` を実行
- Pythonバージョンが3.9以上か確認

**TypeScriptのビルドエラー**：
- 該当アプリディレクトリで `npm install` を実行
- Node.jsのバージョン互換性を確認
- 必要なら `node_modules` を削除して再インストール

**API認証エラー**：
- `.env`ファイルが存在し、正しい値を持っているか確認
- APIキーが有効で期限切れでないことを確認
- エンドポイントURLが地域に適していることを確認

<strong>環境変数の欠如</strong>：
- `.env.copy` から `.env` にコピー
- 作業するレッスンに必要な全値を入力
- `.env` 編集後はアプリケーションを再起動

## 追加リソース

- [Course Setup Guide](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Contributing Guidelines](./CONTRIBUTING.md)
- [Code of Conduct](./CODE_OF_CONDUCT.md)
- [Security Policy](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Collection of Advanced Code Samples](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## プロジェクト固有の注意事項

- これは<strong>教育用リポジトリ</strong>であり、本番コードではありません
- 例は意図的にシンプルで、概念の教育に焦点を当てています
- コード品質は教育的明快さとバランスをとっています
- 各レッスンは独立して完了可能です
- 複数のAPIプロバイダをサポート：Azure OpenAI、OpenAI、Microsoft Foundry Models、Foundry LocalやOllamaなどのオフラインプロバイダ
- コンテンツは多言語対応し、自動翻訳ワークフローを持つ
- 質問やサポートのための活発なDiscordコミュニティあり

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->