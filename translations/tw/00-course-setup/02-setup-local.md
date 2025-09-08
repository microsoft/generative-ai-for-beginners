<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T14:54:58+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "tw"
}
-->
# 本地安裝 🖥️

**如果你想在自己的筆電上執行所有內容，請參考這份指南。**  
你有兩種選擇：**(A) 原生 Python + virtual-env** 或 **(B) VS Code Dev Container 搭配 Docker**。  
選擇你覺得最簡單的方式——兩種方法都能學到相同的內容。

## 1.  先決條件

| 工具                | 版本 / 備註                                                                       |
|---------------------|-----------------------------------------------------------------------------------|
| **Python**          | 3.10 以上（從 <https://python.org> 下載）                                         |
| **Git**             | 最新版（Xcode / Git for Windows / Linux 套件管理員都會附帶）                      |
| **VS Code**         | 選用但推薦 <https://code.visualstudio.com>                                        |
| **Docker Desktop**  | *僅限* 選項 B。免費安裝：<https://docs.docker.com/desktop/>                       |

> 💡 **提示** – 在終端機驗證工具：  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  選項 A – 原生 Python（最快速）

### 步驟 1  複製這個 repo

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### 步驟 2 建立並啟用虛擬環境

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ 提示字元現在應該會以 (.venv) 開頭——這表示你已經進入虛擬環境。

### 步驟 3 安裝相依套件

```bash
pip install -r requirements.txt
```

跳到第 3 節 [API 金鑰](../../../00-course-setup)

## 2. 選項 B – VS Code Dev Container（Docker）

我們為這個 repository 和課程設置了一個 [開發容器](https://containers.dev?WT.mc_id=academic-105485-koreyst)，它有一個通用執行環境，支援 Python3、.NET、Node.js 和 Java 開發。相關設定寫在本 repo 根目錄的 `.devcontainer/` 資料夾下的 `devcontainer.json` 檔案中。

>**為什麼選這個？**
>環境和 Codespaces 完全一致；不會有相依性偏差。

### 步驟 0 安裝額外工具

Docker Desktop – 確認 ```docker --version``` 可以執行。
VS Code Remote – Containers 擴充套件（ID: ms-vscode-remote.remote-containers）。

### 步驟 1 用 VS Code 開啟 repo

檔案 ▸ 開啟資料夾…  → generative-ai-for-beginners

VS Code 會偵測到 .devcontainer/ 並跳出提示。

### 步驟 2 重新在容器中開啟

點選「Reopen in Container」。Docker 會建立映像檔（第一次約 3 分鐘）。
當終端機出現提示字元時，你就已經在容器裡了。

## 2.  選項 C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是一個輕量級安裝程式，可以安裝 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python 以及一些套件。
Conda 本身是一個套件管理工具，可以輕鬆建立和切換不同的 Python [**虛擬環境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) 和套件。對於安裝 `pip` 沒有的套件也很方便。

### 步驟 0  安裝 Miniconda

依照 [MiniConda 安裝指南](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) 進行安裝。

```bash
conda --version
```

### 步驟 1 建立虛擬環境

建立一個新的環境檔案（*environment.yml*）。如果你是在 Codespaces 上操作，請在 `.devcontainer` 目錄下建立，也就是 `.devcontainer/environment.yml`。

### 步驟 2  編輯你的環境檔案

將以下內容加入你的 `environment.yml`

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

在命令列/終端機執行下列指令

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

如果遇到問題，請參考 [Conda 環境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

## 2  選項 D – 經典 Jupyter / Jupyter Lab（瀏覽器執行）

> **適合誰？**  
> 喜歡經典 Jupyter 介面，或想在不安裝 VS Code 的情況下執行 notebook 的人。  

### 步驟 1  確認已安裝 Jupyter

要在本地啟動 Jupyter，請打開終端機/命令列，切換到課程目錄，然後執行：

```bash
jupyter notebook
```

或

```bash
jupyterhub
```

這會啟動 Jupyter，並在命令列視窗顯示可存取的網址。

進入網址後，你應該會看到課程大綱，並能瀏覽任何 `*.ipynb` 檔案。例如：`08-building-search-applications/python/oai-solution.ipynb`。

## 3. 新增你的 API 金鑰

在開發任何應用程式時，保護你的 API 金鑰非常重要。我們建議不要直接把 API 金鑰寫在程式碼裡。如果把這些資訊提交到公開的 repository，可能會有安全風險，甚至被有心人士濫用產生額外費用。
以下是如何為 Python 建立 `.env` 檔案並加入 `GITHUB_TOKEN` 的步驟說明：

1. **切換到你的專案目錄**：打開終端機或命令提示字元，切換到你想建立 `.env` 檔案的專案根目錄。

   ```bash
   cd path/to/your/project
   ```

2. **建立 `.env` 檔案**：用你喜歡的文字編輯器建立一個名為 `.env` 的新檔案。如果用命令列，可以用 `touch`（Unix 系統）或 `echo`（Windows）：

   Unix 系統：

   ```bash
   touch .env
   ```

   Windows：

   ```cmd
   echo . > .env
   ```

3. **編輯 `.env` 檔案**：用文字編輯器（如 VS Code、Notepad++ 或其他）打開 `.env` 檔案。加入下列內容，將 `your_github_token_here` 換成你自己的 GitHub token：

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **儲存檔案**：儲存後關閉編輯器。

5. **安裝 `python-dotenv`**：如果還沒安裝，請用 `pip` 安裝 `python-dotenv` 套件，讓 Python 應用程式能從 `.env` 檔案載入環境變數：

   ```bash
   pip install python-dotenv
   ```

6. **在 Python 程式中載入環境變數**：在你的 Python 程式中，使用 `python-dotenv` 套件從 `.env` 檔案載入環境變數：

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

這樣就完成了！你已經成功建立 `.env` 檔案、加入 GitHub token，並在 Python 應用程式中載入它。

🔐 千萬不要提交 .env——它已經在 .gitignore 裡了。
完整的服務商說明請參考 [`providers.md`](03-providers.md)。

## 4. 接下來呢？

| 我想要…             | 前往…                                                                  |
|---------------------|------------------------------------------------------------------------|
| 開始第一課          | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| 設定 LLM 服務商     | [`providers.md`](03-providers.md)                                       |
| 認識其他學員        | [加入我們的 Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. 疑難排解

| 狀況                                       | 解決方法                                                         |
|--------------------------------------------|------------------------------------------------------------------|
| `python not found`                         | 將 Python 加入 PATH 或安裝後重新開啟終端機                        |
| `pip` 無法建立 wheels（Windows）           | 執行 `pip install --upgrade pip setuptools wheel` 後重試          |
| `ModuleNotFoundError: dotenv`              | 執行 `pip install -r requirements.txt`（環境未安裝）               |
| Docker 建置失敗 *No space left*            | Docker Desktop ▸ *設定* ▸ *資源* → 增加磁碟空間                    |
| VS Code 一直提示重新開啟                   | 可能同時啟用了兩種選項；請擇一（venv **或** container）            |
| OpenAI 401 / 429 錯誤                      | 檢查 `OPENAI_API_KEY` 值 / 請求速率限制                            |
| 使用 Conda 發生錯誤                        | 用 `conda install -c microsoft azure-ai-ml` 安裝 Microsoft AI 套件 |

---

**免責聲明**：  
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能會包含錯誤或不準確之處。原始語言的文件應視為具權威性的來源。對於重要資訊，建議採用專業人工翻譯。因使用本翻譯而產生的任何誤解或誤釋，我們概不負責。