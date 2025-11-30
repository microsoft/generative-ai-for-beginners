<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T10:55:19+00:00",
  "source_file": "AGENTS.md",
  "language_code": "ja"
}
-->
# AGENTS.md

## プロジェクト概要

このリポジトリは、生成AIの基礎とアプリケーション開発を教える21レッスンの包括的なカリキュラムを含んでいます。このコースは初心者向けに設計されており、基本的な概念から実用的なアプリケーションの構築までをカバーしています。

**主要技術:**
- Python 3.9+ と以下のライブラリ: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript (Node.js) と以下のライブラリ: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service、OpenAI API、GitHub Models
- 対話型学習のための Jupyter Notebooks
- 一貫した開発環境を提供する Dev Containers

**リポジトリ構成:**
- 21の番号付きレッスンディレクトリ (00-21)、各ディレクトリにはREADME、コード例、課題が含まれます
- Python、TypeScript、時には .NET の実装例
- 40以上の言語バージョンを含む翻訳ディレクトリ
- `.env` ファイルを使用した集中管理設定 (`.env.copy` をテンプレートとして使用)

## セットアップコマンド

### リポジトリの初期セットアップ

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Python 環境のセットアップ

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Node.js/TypeScript のセットアップ

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container セットアップ (推奨)

このリポジトリには、GitHub Codespaces または VS Code Dev Containers 用の `.devcontainer` 設定が含まれています:

1. GitHub Codespaces または Dev Containers 拡張機能を使用して VS Code でリポジトリを開く
2. Dev Container が自動的に以下を実行:
   - `requirements.txt` から Python 依存関係をインストール
   - ポスト作成スクリプト (`.devcontainer/post-create.sh`) を実行
   - Jupyter カーネルをセットアップ

## 開発ワークフロー

### 環境変数

API アクセスを必要とするすべてのレッスンでは、`.env` に定義された環境変数を使用します:

- `OPENAI_API_KEY` - OpenAI API 用
- `AZURE_OPENAI_API_KEY` - Azure OpenAI Service 用
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI エンドポイント URL
- `AZURE_OPENAI_DEPLOYMENT` - チャット補完モデルのデプロイメント名
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - 埋め込みモデルのデプロイメント名
- `AZURE_OPENAI_API_VERSION` - API バージョン (デフォルト: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Hugging Face モデル用
- `GITHUB_TOKEN` - GitHub Models 用

### Python の例を実行

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### TypeScript の例を実行

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Jupyter Notebooks の実行

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### レッスンの種類に応じた作業

- **「学ぶ」レッスン**: README.md のドキュメントと概念に焦点を当てる
- **「構築する」レッスン**: Python と TypeScript の動作するコード例を含む
- 各レッスンには、理論、コードの解説、ビデオコンテンツへのリンクを含む README.md が付属

## コードスタイルガイドライン

### Python

- 環境変数管理に `python-dotenv` を使用
- API インタラクションには `openai` ライブラリをインポート
- リンティングには `pylint` を使用 (一部の例では簡略化のため `# pylint: disable=all` を含む)
- PEP 8 の命名規則に従う
- API 資格情報は `.env` ファイルに保存し、コード内には含めない

### TypeScript

- 環境変数には `dotenv` パッケージを使用
- 各アプリの `tsconfig.json` で TypeScript を設定
- Azure サービスには `@azure/openai` または `@azure-rest/ai-inference` を使用
- 開発時の自動リロードには `nodemon` を使用
- 実行前にビルド: `npm run build` の後に `npm start`

### 一般的な規約

- コード例はシンプルで教育的なものにする
- 重要な概念を説明するコメントを含める
- 各レッスンのコードは自己完結型で実行可能であること
- 一貫した命名を使用: Azure OpenAI 用に `aoai-`、OpenAI API 用に `oai-`、GitHub Models 用に `githubmodels-`

## ドキュメントガイドライン

### Markdown スタイル

- すべての URL は `[テキスト](../../url)` 形式で余分なスペースを含めない
- 相対リンクは `./` または `../` で始める
- Microsoft ドメインへのリンクには必ずトラッキング ID を含める: `?WT.mc_id=academic-105485-koreyst`
- URL に国別ロケールを含めない (例: `/en-us/` を避ける)
- 画像は `./images` フォルダに保存し、説明的な名前を付ける
- ファイル名には英数字とハイフンを使用

### 翻訳サポート

- リポジトリは GitHub Actions を使用して40以上の言語をサポート
- 翻訳は `translations/` ディレクトリに保存
- 部分的な翻訳は提出しない
- 機械翻訳は受け付けない
- 翻訳された画像は `translated_images/` ディレクトリに保存

## テストと検証

### 提出前のチェック

このリポジトリは GitHub Actions を使用して検証を行います。PR を提出する前に:

1. **Markdown リンクのチェック**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **手動テスト**:
   - Python の例をテスト: 仮想環境を有効化してスクリプトを実行
   - TypeScript の例をテスト: `npm install`、`npm run build`、`npm start`
   - 環境変数が正しく設定されていることを確認
   - API キーがコード例で動作することを確認

3. **コード例**:
   - すべてのコードがエラーなく実行されることを確認
   - 必要に応じて Azure OpenAI と OpenAI API の両方でテスト
   - GitHub Models がサポートされている場合は例を確認

### 自動テストなし

このリポジトリは教育目的のものであり、チュートリアルと例に焦点を当てています。そのため、ユニットテストや統合テストはありません。検証は主に以下を通じて行います:
- コード例の手動テスト
- GitHub Actions による Markdown 検証
- 教育コンテンツのコミュニティレビュー

## プルリクエストガイドライン

### 提出前

1. Python と TypeScript の両方でコード変更をテスト (該当する場合)
2. Markdown 検証を実行 (PR 時に自動トリガー)
3. Microsoft URL にトラッキング ID が含まれていることを確認
4. 相対リンクが有効であることを確認
5. 画像が正しく参照されていることを確認

### PR タイトル形式

- 説明的なタイトルを使用: `[Lesson 06] Fix Python example typo` または `Update README for lesson 08`
- 該当する場合は問題番号を参照: `Fixes #123`

### PR 説明

- 変更内容とその理由を説明
- 関連する問題へのリンクを含める
- コード変更の場合、どの例をテストしたかを明記
- 翻訳 PR の場合、完全な翻訳ファイルを含める

### 貢献要件

- Microsoft CLA に署名 (最初の PR 時に自動)
- リポジトリを自分のアカウントにフォークしてから変更を行う
- 論理的な変更ごとに1つの PR を作成 (無関係な修正を組み合わせない)
- PR は可能な限り小さく、焦点を絞る

## 一般的なワークフロー

### 新しいコード例の追加

1. 該当するレッスンディレクトリに移動
2. `python/` または `typescript/` サブディレクトリに例を作成
3. 命名規則に従う: `{provider}-{example-name}.{py|ts|js}`
4. 実際の API 資格情報でテスト
5. 新しい環境変数がある場合はレッスン README に記載

### ドキュメントの更新

1. レッスンディレクトリ内の README.md を編集
2. Markdown ガイドラインに従う (トラッキング ID、相対リンク)
3. 翻訳の更新は GitHub Actions によって処理される (手動で編集しない)
4. すべてのリンクが有効であることをテスト

### Dev Containers の使用

1. リポジトリには `.devcontainer/devcontainer.json` が含まれる
2. ポスト作成スクリプトが自動的に Python 依存関係をインストール
3. Python と Jupyter 用の拡張機能が事前設定済み
4. 環境は `mcr.microsoft.com/devcontainers/universal:2.11.2` に基づく

## デプロイと公開

これは学習用リポジトリであり、デプロイプロセスはありません。このカリキュラムは以下で利用されます:

1. **GitHub リポジトリ**: コードとドキュメントへの直接アクセス
2. **GitHub Codespaces**: 事前設定された即時開発環境
3. **Microsoft Learn**: 公式学習プラットフォームへのコンテンツ配信
4. **docsify**: Markdown から構築されたドキュメントサイト (`docsifytopdf.js` と `package.json` を参照)

### ドキュメントサイトの構築

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## トラブルシューティング

### よくある問題

**Python のインポートエラー**:
- 仮想環境が有効化されていることを確認
- `pip install -r requirements.txt` を実行
- Python のバージョンが 3.9+ であることを確認

**TypeScript のビルドエラー**:
- 特定のアプリディレクトリで `npm install` を実行
- Node.js のバージョンが互換性があることを確認
- `node_modules` をクリアして再インストール

**API 認証エラー**:
- `.env` ファイルが存在し、正しい値が設定されていることを確認
- API キーが有効で期限切れでないことを確認
- エンドポイント URL が地域に適していることを確認

**環境変数が不足している**:
- `.env.copy` を `.env` にコピー
- 作業中のレッスンに必要な値をすべて入力
- `.env` を更新後、アプリケーションを再起動

## 追加リソース

- [コースセットアップガイド](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [貢献ガイドライン](./CONTRIBUTING.md)
- [行動規範](./CODE_OF_CONDUCT.md)
- [セキュリティポリシー](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [高度なコードサンプル集](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## プロジェクト固有の注意事項

- このリポジトリは **教育目的** に特化しており、実運用コードではありません
- 例は意図的にシンプルで、概念の理解に焦点を当てています
- コード品質は教育的な明確さとバランスを取っています
- 各レッスンは自己完結型で、独立して完了可能です
- リポジトリは複数の API プロバイダーをサポート: Azure OpenAI、OpenAI、GitHub Models
- コンテンツは多言語対応で、自動翻訳ワークフローを備えています
- 質問やサポートのための活発な Discord コミュニティがあります

---

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は責任を負いません。