# 文字起こしデータの準備

文字起こしデータ準備スクリプトは、YouTubeの動画文字起こしをダウンロードし、Semantic Search with OpenAI Embeddings and Functionsサンプルで使用できるように準備します。

文字起こしデータ準備スクリプトは、最新リリースのWindows 11、macOS Ventura、およびUbuntu 22.04（以降）でテスト済みです。

## 必要なAzure OpenAIサービスリソースの作成

> [!IMPORTANT]
> Azure CLIを最新バージョンに更新して、OpenAIとの互換性を確保することをお勧めします
> 詳細は[ドキュメント](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)をご覧ください

1. リソースグループを作成する

> [!NOTE]
> この手順では、東米（East US）にある「semantic-video-search」という名前のリソースグループを使用しています。
> リソースグループ名は変更可能ですが、リソースの場所を変更する場合は、
> [モデル対応表](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst)を確認してください。

```console
az group create --name semantic-video-search --location eastus
```

1. Azure OpenAIサービスリソースを作成します。

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. このアプリケーションで使用するため、エンドポイントとキーを取得します

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. 以下のモデルをデプロイします:
   - `text-embedding-ada-002` バージョン `2` 以上、名前は `text-embedding-ada-002`
   - `gpt-5-mini` 名前は `gpt-5-mini`

```console
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name text-embedding-ada-002 \
    --model-name text-embedding-ada-002 \
    --model-version "2"  \
    --model-format OpenAI \
    --scale-settings-scale-type "Standard"
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name gpt-5-mini \
    --model-name gpt-5-mini \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## 必要なソフトウェア

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) 以上

## 環境変数

YouTube文字起こしデータ準備スクリプトを実行するには、以下の環境変数が必要です。

### Windowsの場合

変数をユーザー環境変数に追加することをお勧めします。
`Windows スタート` > `システム環境変数の編集` > `環境変数` > [USER] の `ユーザー変数` > `新規`。

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- 環境変数をPowerShellプロファイルに追加することもできます。

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### Linux および macOSの場合

以下のエクスポートを `~/.bashrc` または `~/.zshrc` ファイルに追加することをお勧めします。

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## 必要なPythonライブラリのインストール

1. もし未インストールなら、[gitクライアント](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst)をインストールします。
1. `Terminal` ウィンドウから、このサンプルをお好みのリポジトリフォルダーにcloneします。

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep` フォルダーに移動します。

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Pythonの仮想環境を作成します。

    Windowsの場合:

    ```powershell
    python -m venv .venv
    ```

    macOSおよびLinuxの場合:

    ```bash
    python3 -m venv .venv
    ```

1. Python仮想環境を有効化します。

   Windowsの場合:

   ```powershell
   .venv\Scripts\activate
   ```

   macOSおよびLinuxの場合:

   ```bash
   source .venv/bin/activate
   ```

1. 必要なライブラリをインストールします。

   Windowsの場合:

   ```powershell
   pip install -r requirements.txt
   ```

   macOSおよびLinuxの場合:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube文字起こしデータ準備スクリプトの実行

### Windowsの場合

```powershell
.\transcripts_prepare.ps1
```

### macOSおよびLinuxの場合

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の原語版が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や解釈違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->