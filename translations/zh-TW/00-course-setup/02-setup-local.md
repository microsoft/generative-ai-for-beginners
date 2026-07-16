# 本機設定 🖥️

**如果你想在自己的筆記型電腦上執行所有內容，請使用本指南。**   
你有兩種選擇：**(A) 原生 Python + 虛擬環境** 或 **(B) 使用 Docker 的 VS Code 開發容器**。  
選擇你覺得較簡單的方式—兩者都能達成相同課程內容。

## 1.  前置作業

| 工具               | 版本 / 備註                                                                      |
|--------------------|----------------------------------------------------------------------------------|
| **Python**         | 3.10+（可從 <https://python.org> 取得）                                         |
| **Git**            | 最新版（隨 Xcode / Windows Git / Linux 套件管理工具提供）                        |
| **VS Code**        | 可選但推薦安裝 <https://code.visualstudio.com>                                 |
| **Docker Desktop** | 僅選擇B方案需要。免費安裝見：<https://docs.docker.com/desktop/>                 |

> 💡 <strong>小提示</strong> – 在終端機確認工具版本：  
> `python --version`，`git --version`，`docker --version`，`code --version`  

## 2.  A 方案 – 原生 Python（最快速）

### 第一步 克隆此倉庫

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### 第二步 建立並啟動虛擬環境

```bash
python -m venv .venv          # 製作一個
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ 目前提示字元前應該會出現 (.venv)，表示你已進入虛擬環境。

### 第三步 安裝所需套件

```bash
pip install -r requirements.txt
```

直接跳到第3節 [API 金鑰](#3-新增你的-api-金鑰)

## 2. B 方案 – VS Code 開發容器（Docker）

本倉庫及課程採用[開發容器](https://containers.dev?WT.mc_id=academic-105485-koreyst)設定，內含可支援 Python3、.NET、Node.js 與 Java 開發的通用執行環境。相關配置定義於本倉庫根目錄的 `.devcontainer/` 資料夾中 `devcontainer.json` 檔案內。

>**為何選擇此方案？**
>環境與 Codespaces 完全一致，避免依賴相差問題。

### 第零步 安裝必備項目

Docker Desktop – 確認執行 ```docker --version``` 正常。
VS Code Remote – Containers 延伸模組（ID：ms-vscode-remote.remote-containers）。

### 第一步 在 VS Code 開啟倉庫

檔案 ▸ 開啟資料夾… → generative-ai-for-beginners

VS Code 會偵測 .devcontainer/，並跳出提示。

### 第二步 重新在容器中開啟

點選「Reopen in Container」。Docker 首次會花約 3 分鐘完成映像檔建置。
當終端機提示字元出現，即表示已在容器內。

## 2.  C 方案 – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是用來安裝 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python 及部分套件的輕量安裝工具。
Conda 是一個套件管理器，方便設定和切換不同 Python [<strong>虛擬環境</strong>](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)與套件。對於無法透過 `pip` 安裝的套件，它也非常有用。

### 第零步 安裝 Miniconda

請依循 [Miniconda 安裝指南](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) 進行安裝。

```bash
conda --version
```

### 第一步 建立虛擬環境檔案

建立一個新的環境設定檔 (*environment.yml*)。如果你使用 Codespaces，請將檔案放置於 `.devcontainer` 目錄下，即 `.devcontainer/environment.yml`。

### 第二步 填寫環境檔案內容

將以下段落加入你的 `environment.yml`

```yml
name: <environment-name>
channels:
 - defaults
 - microsoft
dependencies:
- python=<python-version>
- openai
- python-dotenv
- pip
- pip:
    - azure-ai-ml

```

### 第三步 建立 Conda 環境

在命令列或終端機執行以下指令

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer 子路徑僅適用於 Codespace 設定
conda activate ai4beg
```

若遇問題，請參考[Conda 環境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

## 2  D 方案 – 傳統 Jupyter / Jupyter Lab（瀏覽器中）

> **適合誰？**  
> 喜歡傳統 Jupyter 介面或想在無需 VS Code 情況下執行筆記本者。  

### 第一步 確認已安裝 Jupyter

想在本機啟動 Jupyter，可開啟終端機/命令列，切換至課程資料夾，執行：

```bash
jupyter notebook
```

或

```bash
jupyterhub
```

這將啟動 Jupyter 實例，且終端機視窗會顯示存取該服務的 URL。

連結該 URL 後，即可看到課程大綱並瀏覽任意 `*.ipynb` 檔案，例如 `08-building-search-applications/python/oai-solution.ipynb`。

## 3. 新增你的 API 金鑰

建立任何應用程式時，確保你的 API 金鑰安全相當重要。我們建議不要將任何 API 金鑰直接寫入程式碼。將這些資訊公開到公開倉庫可能導致安全漏洞，甚至若被惡意使用者濫用，將造成莫名費用支出。
以下為如何為 Python 建立 `.env` 檔，並新增你的 Microsoft Foundry 模型認證的分步教學：

> **注意：** GitHub 模型（及其 `GITHUB_TOKEN` 變數）將於2026年7月底退役。本指南改用 [Microsoft Foundry 模型](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)。想完全離線作業？請參閱 [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)。

1. <strong>前往專案目錄</strong>：開啟終端機或命令提示字元，進入你想建立 `.env` 檔的專案根目錄。

   ```bash
   cd path/to/your/project
   ```

2. **建立 `.env` 檔案**：使用喜歡的文字編輯器建立名為 `.env` 的新檔案。如果使用命令列，可透過 Unix 系統的 `touch` 或 Windows 的 `echo`：

   Unix 系統：

   ```bash
   touch .env
   ```

   Windows 系統：

   ```cmd
   echo . > .env
   ```

3. **編輯 `.env` 檔案**：用文字編輯器（如 VS Code、Notepad++ 或其他編輯器）打開 `.env` 檔，將下列內容加入檔案，並替換佔位符為你的 Microsoft Foundry 專案端點和 API 金鑰：

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. <strong>儲存檔案</strong>：儲存修改後關閉文字編輯器。

5. **安裝 `python-dotenv`**：尚未安裝的話，你須安裝此套件，以將 `.env` 檔中的環境變數載入 Python 應用程式。使用 `pip` 安裝：

   ```bash
   pip install python-dotenv
   ```

6. **在 Python 腳本中載入環境變數**：在你的 Python 程式中運用 `python-dotenv` 套件從 `.env` 載入環境變數：

   ```python
   from dotenv import load_dotenv
   import os

   # 從 .env 檔案載入環境變數
   load_dotenv()

   # 存取 Microsoft Foundry Models 變數
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

就這樣！你已成功建立 `.env` 檔，新增 Microsoft Foundry 模型憑證，並將其載入 Python 應用程式。

🔐 切勿提交 .env 檔案—裡面已在 .gitignore。
各服務提供商完整教學請見 [`providers.md`](03-providers.md)。

## 4. 接下來做什麼？

| 我想…              | 前往…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| 開始第 1 課          | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| 設定 LLM 服務提供商   | [`providers.md`](03-providers.md)                                       |
| 認識其他學員         | [加入我們的 Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. 疑難排解

| 狀況                                       | 解決方法                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| 顯示 `python not found`                     | 將 Python 加入 PATH 或安裝後重新開啟終端機                        |
| Windows 下 `pip` 無法建置 wheels            | 執行 `pip install --upgrade pip setuptools wheel` 後重試         |
| 顯示 `ModuleNotFoundError: dotenv`          | 執行 `pip install -r requirements.txt`（可能沒安裝環境）           |
| Docker 建置失敗，提示 *No space left*      | Docker Desktop ▸ *Settings* ▸ *Resources* → 調大磁碟空間            |
| VS Code 持續提示重啟                        | 可能同時啟用兩種方案；請擇一使用（venv <strong>或</strong> 容器）             |
| OpenAI 401 / 429 錯誤                       | 檢查 `OPENAI_API_KEY` 值及請求頻率限制                            |
| Conda 遇到錯誤                             | 使用 `conda install -c microsoft azure-ai-ml` 安裝 Microsoft AI 庫 |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->