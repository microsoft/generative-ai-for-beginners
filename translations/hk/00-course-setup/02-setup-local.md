<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T14:47:06+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "hk"
}
-->
# 本地安裝 🖥️

**如果你想喺自己部電腦運行所有嘢，可以跟住呢份指南。**  
你有兩個選擇：**(A) 原生 Python + virtual-env** 或 **(B) VS Code Dev Container 配合 Docker**。  
揀你覺得最方便嗰個—兩條路都可以學到同一樣嘢。

## 1.  先決條件

| 工具                | 版本 / 備註                                                                       |
|---------------------|-----------------------------------------------------------------------------------|
| **Python**          | 3.10 或以上（去 <https://python.org> 下載）                                       |
| **Git**             | 最新版（Xcode / Git for Windows / Linux 套件管理器都會有）                        |
| **VS Code**         | 可選但建議用 <https://code.visualstudio.com>                                      |
| **Docker Desktop**  | *只限* 選項 B。免費安裝：<https://docs.docker.com/desktop/>                       |

> 💡 **提示** – 喺終端機驗證工具：  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  選項 A – 原生 Python（最快捷）

### 步驟 1  複製呢個 repo

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### 步驟 2 建立及啟動虛擬環境

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ 你應該見到提示開頭有 (.venv)—即係你已經入咗個環境。

### 步驟 3 安裝依賴

```bash
pip install -r requirements.txt
```

之後可以跳去第 3 部分 [API 金鑰](../../../00-course-setup)

## 2. 選項 B – VS Code Dev Container（Docker）

我哋為呢個 repo 同課程設置咗一個 [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst)，入面有 Universal runtime，支援 Python3、.NET、Node.js 同 Java 開發。相關設定喺 repo 根目錄嘅 `.devcontainer/` 資料夾入面嘅 `devcontainer.json`。

>**點解要揀呢個？**
>同 Codespaces 完全一樣嘅環境；唔會有依賴唔同步嘅問題。

### 步驟 0 安裝額外工具

Docker Desktop – 確認 ```docker --version``` 可以用。
VS Code Remote – Containers 擴充功能（ID: ms-vscode-remote.remote-containers）。

### 步驟 1 用 VS Code 開 repo

檔案 ▸ 開啟資料夾…  → generative-ai-for-beginners

VS Code 會偵測到 .devcontainer/，然後彈出提示。

### 步驟 2 重新用 container 開啟

撳「Reopen in Container」。Docker 會建構映像（第一次大約 3 分鐘）。
見到終端機提示，就代表你已經喺 container 入面。

## 2.  選項 C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 係一個輕量級安裝程式，用嚟安裝 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python 同少量套件。
Conda 本身係一個套件管理器，方便你設定同切換唔同嘅 Python [**虛擬環境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) 同套件。安裝啲 pip 無嘅套件都好有用。

### 步驟 0  安裝 Miniconda

跟住 [MiniConda 安裝指南](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) 去安裝。

```bash
conda --version
```

### 步驟 1 建立虛擬環境

建立一個新環境檔案（*environment.yml*）。如果你用緊 Codespaces，喺 `.devcontainer` 目錄入面建立，即 `.devcontainer/environment.yml`。

### 步驟 2  填寫環境檔案

將以下內容加落你嘅 `environment.yml`：

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

### 步驟 3 建立 Conda 環境

喺命令列/終端機執行以下指令

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

如果有問題，可以參考 [Conda 環境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

## 2  選項 D – 經典 Jupyter / Jupyter Lab（用瀏覽器）

> **適合邊個？**  
> 鍾意經典 Jupyter 介面或者想唔用 VS Code 都可以 run notebook 嘅人。  

### 步驟 1  確認已安裝 Jupyter

要喺本地啟動 Jupyter，去終端機/命令列，去到課程目錄，然後執行：

```bash
jupyter notebook
```

或者

```bash
jupyterhub
```

咁就會開一個 Jupyter 實例，命令列會顯示登入網址。

入到網址之後，你應該會見到課程大綱，可以揀任何 `*.ipynb` 檔案。例如 `08-building-search-applications/python/oai-solution.ipynb`。

## 3. 加入你的 API 金鑰

開發應用程式時，保護好 API 金鑰好重要。我哋建議唔好直接將 API 金鑰寫入程式碼。如果你將金鑰 commit 去公開 repo，可能會有安全風險，甚至俾人濫用產生額外費用。
以下係點樣為 Python 建立 `.env` 檔案同加入 `GITHUB_TOKEN` 嘅步驟：

1. **去你嘅專案目錄**：開終端機或命令提示字元，去到你想建立 `.env` 檔案嘅專案根目錄。

   ```bash
   cd path/to/your/project
   ```

2. **建立 `.env` 檔案**：用你鍾意嘅文字編輯器建立一個叫 `.env` 嘅新檔案。如果用命令列，可以用 `touch`（Unix 系統）或 `echo`（Windows）：

   Unix 系統：

   ```bash
   touch .env
   ```

   Windows：

   ```cmd
   echo . > .env
   ```

3. **編輯 `.env` 檔案**：用文字編輯器（例如 VS Code、Notepad++ 或其他）打開 `.env`，加以下一行，將 `your_github_token_here` 換成你嘅 GitHub token：

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **儲存檔案**：儲存更改並關閉編輯器。

5. **安裝 `python-dotenv`**：如果未安裝，要用 `pip` 安裝 `python-dotenv`，咁先可以喺 Python 應用程式讀取 `.env` 檔案入面嘅環境變數。

   ```bash
   pip install python-dotenv
   ```

6. **喺 Python 程式載入環境變數**：喺你嘅 Python 程式用 `python-dotenv` 載入 `.env` 檔案入面嘅環境變數：

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

就係咁簡單！你已經成功建立 `.env` 檔案、加入 GitHub token，並載入到 Python 應用程式。

🔐 千祈唔好 commit .env—已經加咗入 .gitignore。
完整供應商指引請睇 [`providers.md`](03-providers.md)。

## 4. 下一步做咩？

| 我想…                | 去…                                                                       |
|----------------------|----------------------------------------------------------------------------|
| 開始第一課           | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)        |
| 設定 LLM 供應商      | [`providers.md`](03-providers.md)                                          |
| 搵其他學員交流       | [加入我哋 Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. 常見問題排解

| 症狀                                      | 解決方法                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | 將 Python 加入 PATH 或安裝後重新開終端機                        |
| `pip` 無法 build wheels（Windows）        | `pip install --upgrade pip setuptools wheel` 再試一次            |
| `ModuleNotFoundError: dotenv`             | 執行 `pip install -r requirements.txt`（環境未安裝）             |
| Docker build 失敗 *No space left*         | Docker Desktop ▸ *設定* ▸ *資源* → 增加磁碟空間                  |
| VS Code 不斷提示要重新開啟                | 可能兩個選項同時啟動；揀一個（venv **或** container）            |
| OpenAI 401 / 429 錯誤                     | 檢查 `OPENAI_API_KEY` 值 / 請求速率限制                          |
| 用 Conda 出錯                             | 用 `conda install -c microsoft azure-ai-ml` 安裝 Microsoft AI 套件|

---

**免責聲明**：  
本文件經由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能會出現錯誤或不準確之處。原始語言的文件應被視為具權威性的來源。如涉及重要資訊，建議尋求專業人工翻譯。本翻譯所引致的任何誤解或曲解，我們概不負責。