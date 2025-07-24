<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:08:02+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "ja"
}
-->
# 転写データ準備

転写データ準備スクリプトは、YouTubeの動画の文字起こしをダウンロードし、Semantic Search with OpenAI Embeddings and Functionsのサンプルで使用できるように準備します。

転写データ準備スクリプトは、最新リリースのWindows 11、macOS Ventura、Ubuntu 22.04（以降）でテストされています。

## 必要なAzure OpenAI Serviceリソースの作成

> [!IMPORTANT]
> OpenAIとの互換性を確保するために、Azure CLIを最新バージョンに更新することをお勧めします
> 詳細は[ドキュメント](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)をご覧ください

1. リソースグループを作成します

> [!NOTE]
> この手順では、East USにある「semantic-video-search」という名前のリソースグループを使用しています。
> リソースグループの名前は変更可能ですが、リソースの場所を変更する場合は、
> [モデルの利用可能性テーブル](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst)を確認してください。

```console
az group create --name semantic-video-search --location eastus
```

1. Azure OpenAI Serviceリソースを作成します。

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. このアプリケーションで使用するために、エンドポイントとキーを取得します。

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. 以下のモデルをデプロイします：
   - `text-embedding-ada-002` バージョン `2` 以上、名前は `text-embedding-ada-002`
   - `gpt-35-turbo` バージョン `0613` 以上、名前は `gpt-35-turbo`

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

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) 以上

## 環境変数

YouTubeの転写データ準備スクリプトを実行するには、以下の環境変数が必要です。

### Windowsの場合

`ユーザー`環境変数に追加することを推奨します。  
`Windowsスタート` > `システム環境変数の編集` > `環境変数` > [USER]の`ユーザー環境変数` > `新規`。

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### LinuxおよびmacOSの場合

以下のexport文を`~/.bashrc`または`~/.zshrc`ファイルに追加することを推奨します。

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## 必要なPythonライブラリのインストール

1. まだインストールしていない場合は、[gitクライアント](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst)をインストールします。  
1. `ターミナル`ウィンドウから、サンプルを任意のリポジトリフォルダにクローンします。

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. `data_prep`フォルダに移動します。

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Pythonの仮想環境を作成します。

    Windowsの場合：

    ```powershell
    python -m venv .venv
    ```

    macOSおよびLinuxの場合：

    ```bash
    python3 -m venv .venv
    ```

1. Pythonの仮想環境を有効化します。

   Windowsの場合：

   ```powershell
   .venv\Scripts\activate
   ```

   macOSおよびLinuxの場合：

   ```bash
   source .venv/bin/activate
   ```

1. 必要なライブラリをインストールします。

   Windowsの場合：

   ```powershell
   pip install -r requirements.txt
   ```

   macOSおよびLinuxの場合：

   ```bash
   pip3 install -r requirements.txt
   ```

## YouTube転写データ準備スクリプトの実行

### Windowsの場合

```powershell
.\transcripts_prepare.ps1
```

### macOSおよびLinuxの場合

```bash
./transcripts_prepare.sh
```

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文の言語によるオリジナル文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は一切の責任を負いかねます。