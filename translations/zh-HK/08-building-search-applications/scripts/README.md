# 轉錄數據準備

轉錄數據準備腳本下載 YouTube 影片的字幕，並將其準備好以供使用 OpenAI 嵌入和函數的語義搜尋範例。

轉錄數據準備腳本已在最新版本的 Windows 11、macOS Ventura 及 Ubuntu 22.04（及更高版本）上測試。

## 建立所需的 Azure OpenAI 服務資源

> [!IMPORTANT]
> 建議您將 Azure CLI 更新至最新版本，以確保與 OpenAI 兼容
> 請參閱 [文件](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. 建立資源群組

> [!NOTE]
> 本說明使用位於 East US 的名為 "semantic-video-search" 的資源群組。
> 您可以更改資源群組名稱，但在更改資源所在位置時，
> 請檢查 [模型可用性表](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst)。

```console
az group create --name semantic-video-search --location eastus
```

1. 建立 Azure OpenAI 服務資源。

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. 取得用於本應用程式的端點和金鑰

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. 部署以下模型：
   - 版本為 `2` 或更新的 `text-embedding-ada-002`，命名為 `text-embedding-ada-002`
   - 名為 `gpt-4o-mini` 的 `gpt-4o-mini`

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
    --deployment-name gpt-4o-mini \
    --model-name gpt-4o-mini \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## 所需軟體

- 安裝 [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) 或更高版本

## 環境變數

執行 YouTube 轉錄數據準備腳本需要以下環境變數。

### Windows 平台

建議將變數新增至您的 `user` 環境變數中。
`Windows 開始選單` > `編輯系統環境變數` > `環境變數` >`[USER] 的使用者變數` > `新增`。

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- 您也可以將環境變數新增到您的 PowerShell設定檔中。

```powershell
$env:AZURE_OPENAI_API_KEY = "<您的 Azure OpenAI 服務 API 金鑰>"
$env:AZURE_OPENAI_ENDPOINT = "<您的 Azure OpenAI 服務端點>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<您的 Azure OpenAI 服務模型部署名稱>"
$env:GOOGLE_DEVELOPER_API_KEY = "<您的 Google 開發者 API 金鑰>"
``` -->

### Linux 和 macOS 平台

建議將以下匯出指令新增到您的 `~/.bashrc` 或 `~/.zshrc` 檔案中。

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## 安裝所需 Python 函式庫

1. 若尚未安裝，請安裝 [git 客戶端](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst)。
1. 從 `終端機` 視窗將範例克隆到您喜歡的資料夾中。

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. 進入 `data_prep` 資料夾。

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. 建立 Python 虛擬環境。

    Windows 平台：

    ```powershell
    python -m venv .venv
    ```

    macOS 和 Linux 平台：

    ```bash
    python3 -m venv .venv
    ```

1. 啟用 Python 虛擬環境。

   Windows 平台：

   ```powershell
   .venv\Scripts\activate
   ```

   macOS 和 Linux 平台：

   ```bash
   source .venv/bin/activate
   ```

1. 安裝所需函式庫。

   Windows 平台：

   ```powershell
   pip install -r requirements.txt
   ```

   macOS 和 Linux 平台：

   ```bash
   pip3 install -r requirements.txt
   ```

## 執行 YouTube 轉錄數據準備腳本

### Windows 平台

```powershell
.\transcripts_prepare.ps1
```

### macOS 和 Linux 平台

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->