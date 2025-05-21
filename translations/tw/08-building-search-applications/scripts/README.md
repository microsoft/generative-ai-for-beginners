<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T10:27:15+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "tw"
}
-->
# 轉錄資料準備

轉錄資料準備腳本會下載 YouTube 視頻轉錄並準備用於使用 OpenAI 嵌入和功能的語義搜索示例。

轉錄資料準備腳本已在最新版本的 Windows 11、macOS Ventura 和 Ubuntu 22.04（及以上版本）上進行測試。

## 建立所需的 Azure OpenAI 服務資源

> [!IMPORTANT]
> 我們建議您將 Azure CLI 更新到最新版本，以確保與 OpenAI 的兼容性
> 請參閱[文檔](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. 建立一個資源群組

> [!NOTE]
> 在這些說明中，我們使用了位於美國東部的名為 "semantic-video-search" 的資源群組。
> 您可以更改資源群組的名稱，但在更改資源位置時，請檢查[模型可用性表](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst)。

```console
az group create --name semantic-video-search --location eastus
```

1. 建立一個 Azure OpenAI 服務資源。

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. 獲取用於此應用程式的端點和金鑰

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. 部署以下模型：
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

## 所需軟體

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) 或更高版本

## 環境變數

運行 YouTube 轉錄資料準備腳本需要以下環境變數。

### 在 Windows 上

建議將變數添加到您的 `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`。

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### 在 Linux 和 macOS 上

建議將以下導出添加到您的 `~/.bashrc` or `~/.zshrc` 文件中。

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## 安裝所需的 Python 庫

1. 如果尚未安裝，請安裝 [git 客戶端](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst)。
1. 從 `Terminal` 視窗中，將示例克隆到您偏好的倉庫資料夾。

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. 導航到 `data_prep` 資料夾。

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. 建立一個 Python 虛擬環境。

    在 Windows 上：

    ```powershell
    python -m venv .venv
    ```

    在 macOS 和 Linux 上：

    ```bash
    python3 -m venv .venv
    ```

1. 啟用 Python 虛擬環境。

   在 Windows 上：

   ```powershell
   .venv\Scripts\activate
   ```

   在 macOS 和 Linux 上：

   ```bash
   source .venv/bin/activate
   ```

1. 安裝所需的庫。

   在 Windows 上：

   ```powershell
   pip install -r requirements.txt
   ```

   在 macOS 和 Linux 上：

   ```bash
   pip3 install -r requirements.txt
   ```

## 運行 YouTube 轉錄資料準備腳本

### 在 Windows 上

```powershell
.\transcripts_prepare.ps1
```

### 在 macOS 和 Linux 上

```bash
./transcripts_prepare.sh
```

**免責聲明**：

本文件使用AI翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)進行翻譯。我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原語言的原始文件為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤讀不承擔責任。