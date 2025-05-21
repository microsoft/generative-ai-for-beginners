<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T10:26:45+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "ja"
}
-->
# トランスクリプションデータ準備

トランスクリプションデータ準備スクリプトは、YouTube動画のトランスクリプトをダウンロードし、Semantic Search with OpenAI Embeddings and Functionsサンプルで使用できるように準備します。

トランスクリプションデータ準備スクリプトは、最新リリースのWindows 11、macOS Ventura、Ubuntu 22.04（以上）でテストされています。

## 必要なAzure OpenAI Serviceリソースの作成

> [!IMPORTANT]
> OpenAIとの互換性を確保するためにAzure CLIを最新バージョンに更新することをお勧めします。
> [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)を参照してください。

1. リソースグループを作成する

> [!NOTE]
> これらの指示では、East USにある「semantic-video-search」という名前のリソースグループを使用しています。
> リソースグループの名前を変更することはできますが、リソースの場所を変更する際には、
> [モデルの利用可能性表](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst)を確認してください。

```console
az group create --name semantic-video-search --location eastus
```

1. Azure OpenAI Serviceリソースを作成する。

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. このアプリケーションで使用するためのエンドポイントとキーを取得する

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. 以下のモデルをデプロイする:
   - `text-embedding-ada-002` version `2` or greater, named `text-embedding-ada-002`
   - `gpt-35-turbo` version `0613` or greater, named `gpt-35-turbo`

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
    --deployment-name gpt-35-turbo \
    --model-name gpt-35-turbo \
    --model-version "0613"  \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## 必要なソフトウェア

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)以上

## 環境変数

YouTubeトランスクリプションデータ準備スクリプトを実行するために、以下の環境変数が必要です。

### Windowsの場合

変数を`user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`に追加することをお勧めします。

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### LinuxとmacOSの場合

以下のエクスポートを`~/.bashrc` or `~/.zshrc`ファイルに追加することをお勧めします。

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## 必要なPythonライブラリのインストール

1. [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst)をまだインストールしていない場合はインストールします。
1. `Terminal`ウィンドウから、サンプルを希望するリポジトリフォルダにクローンします。

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep`フォルダに移動します。

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Python仮想環境を作成します。

    Windowsの場合:

    ```powershell
    python -m venv .venv
    ```

    macOSとLinuxの場合:

    ```bash
    python3 -m venv .venv
    ```

1. Python仮想環境を有効にします。

   Windowsの場合:

   ```powershell
   .venv\Scripts\activate
   ```

   macOSとLinuxの場合:

   ```bash
   source .venv/bin/activate
   ```

1. 必要なライブラリをインストールします。

   Windowsの場合:

   ```powershell
   pip install -r requirements.txt
   ```

   macOSとLinuxの場合:

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTubeトランスクリプションデータ準備スクリプトを実行する

### Windowsの場合

```powershell
.\transcripts_prepare.ps1
```

### macOSとLinuxの場合

```bash
./transcripts_prepare.sh
```

**免責事項**:
この文書はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確さを追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご承知おきください。元の言語で書かれた文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤った解釈については、責任を負いません。