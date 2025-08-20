<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:07:53+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "tw"
}
-->
# 轉錄資料準備

轉錄資料準備腳本會下載 YouTube 影片的字幕，並將其整理好以供 Semantic Search with OpenAI Embeddings and Functions 範例使用。

轉錄資料準備腳本已在最新版本的 Windows 11、macOS Ventura 及 Ubuntu 22.04（及以上）上測試過。

## 建立所需的 Azure OpenAI 服務資源

> [!IMPORTANT]
> 建議您將 Azure CLI 更新至最新版本，以確保與 OpenAI 的相容性
> 請參考 [文件](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. 建立資源群組

> [!NOTE]
> 本說明中使用的資源群組名稱為「semantic-video-search」，位置在 East US。
> 您可以更改資源群組名稱，但若更改資源位置，
> 請參考 [模型可用性表](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst)。

```console
az group create --name semantic-video-search --location eastus
```

1. 建立 Azure OpenAI 服務資源。

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. 取得此應用程式使用的端點與金鑰

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. 部署以下模型：
   - `text-embedding-ada-002` 版本 `2` 或以上，命名為 `text-embedding-ada-002`
   - `gpt-35-turbo` 版本 `0613` 或以上，命名為 `gpt-35-turbo`

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

## 所需軟體

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) 或以上版本

## 環境變數

執行 YouTube 轉錄資料準備腳本時，需要設定以下環境變數。

### 在 Windows 上

建議將變數加入您的「使用者」環境變數中。
`Windows 開始` > `編輯系統環境變數` > `環境變數` > 選擇 [USER] 的「使用者變數」> `新增`。

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```



### 在 Linux 和 macOS 上

建議將以下 export 指令加入您的 `~/.bashrc` 或 `~/.zshrc` 檔案中。

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## 安裝所需的 Python 函式庫

1. 若尚未安裝，請先安裝 [git 用戶端](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst)。
1. 在 `Terminal` 視窗中，將範例程式碼複製到您偏好的資料夾。

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. 進入 `data_prep` 資料夾。

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. 建立 Python 虛擬環境。

    Windows 上：

    ```powershell
    python -m venv .venv
    ```

    macOS 和 Linux 上：

    ```bash
    python3 -m venv .venv
    ```

1. 啟動 Python 虛擬環境。

   Windows 上：

   ```powershell
   .venv\Scripts\activate
   ```

   macOS 和 Linux 上：

   ```bash
   source .venv/bin/activate
   ```

1. 安裝所需函式庫。

   Windows 上：

   ```powershell
   pip install -r requirements.txt
   ```

   macOS 和 Linux 上：

   ```bash
   pip3 install -r requirements.txt
   ```

## 執行 YouTube 轉錄資料準備腳本

### Windows 上

```powershell
.\transcripts_prepare.ps1
```

### macOS 和 Linux 上

```bash
./transcripts_prepare.sh
```

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。