# 文字轉錄資料準備

文字轉錄資料準備腳本會下載 YouTube 視頻文字稿並進行整理，以便用於帶有 OpenAI 嵌入式和功能的語義搜索示例。

文字轉錄資料準備腳本已在最新版本 Windows 11、macOS Ventura 和 Ubuntu 22.04（及以上版本）上進行測試。

## 建立所需的 Azure OpenAI 服務資源

> [!IMPORTANT]
> 我們建議您更新 Azure CLI 至最新版本，以確保與 OpenAI 的相容性
> 請參閱 [文件](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. 建立資源群組

> [!NOTE]
> 本指南使用位於東美區的名為 "semantic-video-search" 的資源群組。
> 您可以更改資源群組名稱，但在更改資源位置時，
> 請查閱 [模型可用性表](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst)。

```console
az group create --name semantic-video-search --location eastus
```

1. 建立 Azure OpenAI 服務資源。

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. 取得用於此應用程式的端點和金鑰

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. 部署以下模型：
   - 版本為 `2` 或以上的 `text-embedding-ada-002`，名為 `text-embedding-ada-002`
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

## 必要軟件

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) 或以上版本

## 環境變數

執行 YouTube 文字轉錄資料準備腳本需要以下環境變數。

### 在 Windows 上

建議將變數添加到您的 `user` 環境變數中。
`Windows Start` > `編輯系統環境變數` > `環境變數` > `[USER] 的使用者變數` > `新增`。

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- 你也可以將環境變數加入你的 PowerShell 配置檔案。

```powershell
$env:AZURE_OPENAI_API_KEY = "<你的 Azure OpenAI 服務 API 金鑰>"
$env:AZURE_OPENAI_ENDPOINT = "<你的 Azure OpenAI 服務端點>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<你的 Azure OpenAI 服務模型部署名稱>"
$env:GOOGLE_DEVELOPER_API_KEY = "<你的 Google 開發者 API 金鑰>"
``` -->

### 在 Linux 和 macOS 上

建議將以下匯出命令加入你的 `~/.bashrc` 或 `~/.zshrc` 文件中。

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## 安裝必要的 Python 函式庫

1. 若尚未安裝，請安裝 [git 用戶端](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst)。
1. 從 `終端機` 視窗將範例複製至你偏好的資料夾。

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

1. 啟用 Python 虛擬環境。

   在 Windows 上：

   ```powershell
   .venv\Scripts\activate
   ```

   在 macOS 和 Linux 上：

   ```bash
   source .venv/bin/activate
   ```

1. 安裝所需函式庫。

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
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->