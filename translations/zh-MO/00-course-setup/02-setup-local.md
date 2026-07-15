# 本地設定 🖥️

**如果你想在自己的筆記型電腦上執行所有程式，請使用此指南。**  
你有兩條路：**(A) 原生 Python + virtual-env** 或 **(B) VS Code 開發容器搭配 Docker**。  
選擇任何一個感覺更簡單的方式——兩者都能完成相同課程內容。

## 1.  前置需求

| 工具               | 版本 / 備註                                                                         |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 以上（可從 <https://python.org> 取得）                                         |
| **Git**            | 最新版本（包含於 Xcode / Git for Windows / Linux 套件管理器中）                      |
| **VS Code**        | 非必要但建議安裝 <https://code.visualstudio.com>                                     |
| **Docker Desktop** | 僅適用於選項 B。免費安裝：<https://docs.docker.com/desktop/>                         |

> 💡 <strong>小提示</strong> – 在終端機中驗證工具：  
> `python --version`，`git --version`，`docker --version`，`code --version`  

## 2.  選項 A – 原生 Python（最快速）

### 步驟 1：克隆此儲存庫

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### 步驟 2：建立並啟動虛擬環境

```bash
python -m venv .venv          # 建立一個
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ 提示符號應該會以 (.venv) 開頭——代表你已進入虛擬環境。

### 步驟 3：安裝依賴

```bash
pip install -r requirements.txt
```

跳至第 3 節的 [API 密鑰](#3-新增你的-api-密鑰)

## 2. 選項 B – VS Code 開發容器（Docker）

我們使用了一個 [開發容器](https://containers.dev?WT.mc_id=academic-105485-koreyst) 來設定此儲存庫與課程，該容器擁有可支援 Python3、.NET、Node.js 與 Java 開發的通用運行環境。相關配置定義在此儲存庫根目錄的 `.devcontainer/` 資料夾下的 `devcontainer.json` 檔案中。

>**為什麼選擇這個？**
>與 Codespaces 環境完全相同；無相依性漂移問題。

### 步驟 0：安裝額外工具

Docker Desktop – 確認可執行 ```docker --version```。
VS Code Remote – Containers 擴充套件（ID: ms-vscode-remote.remote-containers）。

### 步驟 1：在 VS Code 開啟儲存庫

檔案 ▸ 開啟資料夾… → generative-ai-for-beginners

VS Code 會偵測到 .devcontainer/ 並跳出提示。

### 步驟 2：在容器中重新開啟

點選「Reopen in Container」。Docker 將建立映像檔（首次約 3 分鐘）。  
當終端機提示出現，顯示你已進入容器。

## 2.  選項 C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是一個輕量級安裝程式，用於安裝 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python 以及部分套件。  
Conda 本身是一個套件管理工具，能輕鬆設定及切換不同 Python [<strong>虛擬環境</strong>](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) 和套件。對於安裝非 `pip` 可得套件也非常方便。

### 步驟 0：安裝 Miniconda

請依照 [MiniConda 安裝指南](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) 進行安裝。

```bash
conda --version
```

### 步驟 1：建立虛擬環境檔案

建立一個新的環境檔案（*environment.yml*）。如果你使用 Codespaces，請在 `.devcontainer` 資料夾裡建立，即為 `.devcontainer/environment.yml`。

### 步驟 2：填寫你的環境檔案

將以下內容新增到你的 `environment.yml`

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

### 步驟 3：建立你的 Conda 環境

在命令行／終端機中執行以下指令

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer 子路徑只適用於 Codespace 設定
conda activate ai4beg
```

若遇問題，請參考 [Conda 環境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

## 2  選項 D – 傳統 Jupyter / Jupyter Lab（在瀏覽器中）

> **適合誰？**  
> 喜歡傳統 Jupyter 介面，或想在沒有 VS Code 的情況下執行筆記本的人。  

### 步驟 1：確認已安裝 Jupyter

若要本地啟動 Jupyter，請在終端機／命令行中切換到課程目錄，並執行：

```bash
jupyter notebook
```

或

```bash
jupyterhub
```

此操作會啟動一個 Jupyter 實例，並在命令行視窗中顯示訪問網址。

當你訪問該網址後，應該可以看到課程大綱，並能瀏覽任何 `*.ipynb` 檔案。舉例來說，`08-building-search-applications/python/oai-solution.ipynb`。

## 3. 新增你的 API 密鑰

當開發任何應用程式時，保護你的 API 密鑰安全相當重要。我們建議不要將 API 密鑰直接儲存在程式碼內。將敏感資料提交到公開儲存庫可能造成安全問題，甚至被惡意使用導致不必要的費用。
以下是如何為 Python 建立 `.env` 文件並添加 Microsoft Foundry Models 憑證的逐步指南：

> **注意：** GitHub Models（及其 `GITHUB_TOKEN` 變數）將於 2026 年 7 月底退役。本指南改用[Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)。如果喜歡完全離線操作，請參閱 [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)。

1. <strong>導航至專案目錄</strong>：打開你的終端機或命令提示字元，切換到要建立 `.env` 文件的專案根目錄。

   ```bash
   cd path/to/your/project
   ```

2. **建立 `.env` 文件**：使用你喜歡的文字編輯器建立一個新檔案，命名為 `.env`。若使用命令列，可使用 `touch`（Unix 系統）或 `echo`（Windows）：

   Unix 系統：

   ```bash
   touch .env
   ```

   Windows：

   ```cmd
   echo . > .env
   ```

3. **編輯 `.env` 文件**：使用文字編輯器（如 VS Code、Notepad++ 或其他）開啟 `.env` 文件，並加入以下內容，將裡面的占位符替換成你真正的 Microsoft Foundry 專案端點與 API 密鑰：

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. <strong>儲存檔案</strong>：儲存變更並關閉文字編輯器。

5. **安裝 `python-dotenv`**：如果尚未安裝，需要安裝 `python-dotenv` 套件來從 `.env` 文件載入環境變數至你的 Python 應用程式。可使用 `pip` 安裝：

   ```bash
   pip install python-dotenv
   ```

6. **在你的 Python 腳本中載入環境變數**：使用 `python-dotenv` 套件在 Python 腳本中載入 `.env` 文件中的環境變數：

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

就這樣！你已成功建立 `.env` 文件、新增 Microsoft Foundry Models 憑證，並將它們載入你的 Python 應用程式。

🔐 永遠不要提交 .env——它已被加入 .gitignore。
供應商完整指示可參考 [`providers.md`](03-providers.md)。

## 4. 接下來做什麼？

| 我想…          | 前往…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| 開始第 1 課      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| 設定大型語言模型供應商 | [`providers.md`](03-providers.md)                                       |
| 認識其他學員     | [加入我們的 Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. 疑難排解

| 症狀                                   | 解決方法                                                          |
|---------------------------------------|-----------------------------------------------------------------|
| 找不到 `python`                        | 將 Python 加入 PATH，或安裝後重新開啟終端機                      |
| Windows 下 `pip` 無法建置 wheel 套件  | 執行 `pip install --upgrade pip setuptools wheel` 後重試        |
| `ModuleNotFoundError: dotenv`          | 執行 `pip install -r requirements.txt`（虛擬環境未安裝）         |
| Docker 建置失敗 *No space left*        | Docker Desktop ▸ *Settings* ▸ *Resources* → 增加磁碟空間          |
| VS Code 持續提示要重啟                  | 你可能同時啟用了兩個選項；只選擇其中一個（venv <strong>或</strong> 容器）    |
| OpenAI 顯示 401 / 429 錯誤              | 檢查 `OPENAI_API_KEY` 值 / 請求頻率限制                          |
| Conda 使用錯誤                         | 使用 `conda install -c microsoft azure-ai-ml` 安裝 Microsoft AI 函式庫 |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->