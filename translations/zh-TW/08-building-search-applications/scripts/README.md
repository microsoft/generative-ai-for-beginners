# 文字轉錄資料準備

文字轉錄資料準備腳本會下載 YouTube 影片的文字稿，並為「使用 OpenAI Embeddings 和 Functions 的語意搜尋範例」做準備。

文字轉錄資料準備腳本已在最新版本的 Windows 11、macOS Ventura 和 Ubuntu 22.04 (及以上版本) 上測試。

## 建立所需的 Azure OpenAI 服務資源

> [!IMPORTANT]
> 建議您將 Azure CLI 更新至最新版本，以確保與 OpenAI 的相容性
> 請參閱 [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. 建立資源群組

> [!NOTE]
> 本說明中使用的資源群組名稱為「semantic-video-search」，位置在 East US。
> 您可以變更資源群組名稱，但若要變更資源位置，
> 請檢查 [模型可用性表](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst)。

```console
az group create --name semantic-video-search --location eastus
```

1. 建立 Azure OpenAI 服務資源。

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. 取得本應用程式使用的端點和金鑰

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. 部署以下模型：
   - 版本為 `2` 或以上的 `text-embedding-ada-002`，並命名為 `text-embedding-ada-002`
   - 命名為 `gpt-5-mini` 的 `gpt-5-mini`

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

## 必要軟體

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) 或以上版本

## 環境變數

執行 YouTube 文字轉錄資料準備腳本時，需要以下環境變數。

### 在 Windows 上

建議將這些變數加入您的 `user` 環境變數。
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > [USER] 的 `User variables` > `New`。

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- 您也可以將環境變數加入 PowerShell 設定檔。

```powershell
$env:AZURE_OPENAI_API_KEY = "<your Azure OpenAI Service API key>"
$env:AZURE_OPENAI_ENDPOINT = "<your Azure OpenAI Service endpoint>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<your Azure OpenAI Service model deployment name>"
$env:GOOGLE_DEVELOPER_API_KEY = "<your Google developer API key>"
``` -->

### 在 Linux 和 macOS 上

建議將以下 export 加入您的 `~/.bashrc` 或 `~/.zshrc` 檔案。

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## 安裝必要的 Python 函式庫

1. 如果尚未安裝，請先安裝 [git 用戶端](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst)。
1. 在 `Terminal` 視窗中，將範例複製 (clone) 到您偏好的資料庫資料夾。

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. 進入 `data_prep` 資料夾。

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. 建立 Python 虛擬環境。

    在 Windows 上：

    ```powershell
    python -m venv .venv
    ```

    在 macOS 和 Linux 上：

    ```bash
    python3 -m venv .venv
    ```

1. 啟動 Python 虛擬環境。

   在 Windows 上：

   ```powershell
   .venv\Scripts\activate
   ```

   在 macOS 和 Linux 上：

   ```bash
   source .venv/bin/activate
   ```

1. 安裝所需的函式庫。

   在 Windows 上：

   ```powershell
   pip install -r requirements.txt
   ```

   在 macOS 和 Linux 上：

   ```bash
   pip3 install -r requirements.txt
   ```

## 執行 YouTube 文字轉錄資料準備腳本

### 在 Windows 上

```powershell
.\transcripts_prepare.ps1
```

### 在 macOS 和 Linux 上

```bash
./transcripts_prepare.sh
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->