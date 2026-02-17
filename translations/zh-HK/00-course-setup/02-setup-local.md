# 本地設定 🖥️

**如果你喜歡在自己的筆記型電腦上運行所有內容，請使用本指南。**  
你有兩條路徑：**(A) 原生 Python + virtual-env** 或 **(B) 使用 Docker 的 VS Code 開發容器**。  
選擇你覺得較簡單的方式——兩者都能達到相同的課程效果。

## 1. 先決條件

| 工具               | 版本 / 備註                                                                        |
|--------------------|-----------------------------------------------------------------------------------|
| **Python**         | 3.10 以上（可從 <https://python.org> 下載）                                        |
| **Git**            | 最新版本（隨 Xcode / Windows Git / Linux 套件管理器附帶）                          |
| **VS Code**        | 可選但推薦 <https://code.visualstudio.com>                                        |
| **Docker Desktop** | *僅限* 選項 B。免費安裝：<https://docs.docker.com/desktop/>                        |

> 💡 **提示** – 在終端機驗證工具：  
> `python --version`、`git --version`、`docker --version`、`code --version`  

## 2. 選項 A – 原生 Python（最快速）

### 步驟 1  克隆此倉庫

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### 步驟 2 建立並啟用虛擬環境

```bash
python -m venv .venv          # 建立一個
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ 提示符現在應該以 (.venv) 開頭——表示你已進入虛擬環境。

### 步驟 3 安裝依賴套件

```bash
pip install -r requirements.txt
```

跳至第 3 節 [API 金鑰](../../../00-course-setup)

## 2. 選項 B – VS Code 開發容器（Docker）

我們使用 [開發容器](https://containers.dev?WT.mc_id=academic-105485-koreyst) 設定此倉庫和課程，該容器具有通用執行環境，可支援 Python3、.NET、Node.js 和 Java 開發。相關配置定義在本倉庫根目錄的 `.devcontainer/` 資料夾中的 `devcontainer.json` 文件。

>**為什麼選擇這個？**  
>環境與 Codespaces 完全相同；無依賴漂移問題。

### 步驟 0 安裝額外工具

Docker Desktop – 確認 ```docker --version``` 可用。  
VS Code Remote – Containers 擴充套件（ID: ms-vscode-remote.remote-containers）。

### 步驟 1 在 VS Code 開啟倉庫

檔案 ▸ 開啟資料夾… → generative-ai-for-beginners

VS Code 會偵測到 .devcontainer/ 並跳出提示。

### 步驟 2 重新在容器中開啟

點擊「Reopen in Container」。Docker 會建立映像檔（第一次約 3 分鐘）。  
當終端機提示出現時，表示你已進入容器內。

## 2. 選項 C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是一個輕量級安裝器，用於安裝 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python 以及部分套件。  
Conda 本身是一個套件管理器，方便設定和切換不同的 Python [**虛擬環境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) 和套件。它也方便安裝 `pip` 無法取得的套件。

### 步驟 0  安裝 Miniconda

請依照 [MiniConda 安裝指南](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) 進行安裝。

```bash
conda --version
```

### 步驟 1 建立虛擬環境檔案

建立一個新的環境檔案 (*environment.yml*)。如果你使用 Codespaces，請在 `.devcontainer` 目錄下建立，即 `.devcontainer/environment.yml`。

### 步驟 2 填寫你的環境檔案

將以下片段加入你的 `environment.yml`

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

在命令列/終端機執行以下指令

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer 子路徑只適用於 Codespace 設定
conda activate ai4beg
```

如遇問題，請參考 [Conda 環境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

## 2. 選項 D – 傳統 Jupyter / Jupyter Lab（瀏覽器中）

> **適合誰？**  
> 喜歡經典 Jupyter 介面或想在不使用 VS Code 的情況下運行筆記本的人。

### 步驟 1 確認已安裝 Jupyter

要在本地啟動 Jupyter，請打開終端機/命令列，切換到課程目錄，執行：

```bash
jupyter notebook
```

或

```bash
jupyterhub
```

這會啟動一個 Jupyter 實例，並在命令列視窗中顯示存取的 URL。

存取該 URL 後，你應該能看到課程大綱並瀏覽任何 `*.ipynb` 檔案。例如，`08-building-search-applications/python/oai-solution.ipynb`。

## 3. 新增你的 API 金鑰

在建立任何類型的應用程式時，保護你的 API 金鑰安全非常重要。我們建議不要直接將任何 API 金鑰存放在程式碼中。將這些資訊提交到公開倉庫可能導致安全問題，甚至被惡意使用而產生不必要的費用。  
以下是如何為 Python 建立 `.env` 檔案並新增 `GITHUB_TOKEN` 的逐步指南：

1. **切換到你的專案目錄**：打開終端機或命令提示字元，切換到你想建立 `.env` 檔案的專案根目錄。

   ```bash
   cd path/to/your/project
   ```

2. **建立 `.env` 檔案**：使用你偏好的文字編輯器建立一個名為 `.env` 的新檔案。如果使用命令列，可以用 `touch`（Unix 系統）或 `echo`（Windows）：

   Unix 系統：

   ```bash
   touch .env
   ```

   Windows：

   ```cmd
   echo . > .env
   ```

3. **編輯 `.env` 檔案**：用文字編輯器（例如 VS Code、Notepad++ 或其他編輯器）打開 `.env` 檔案。加入以下內容，將 `your_github_token_here` 替換成你的實際 GitHub 令牌：

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **儲存檔案**：儲存變更並關閉編輯器。

5. **安裝 `python-dotenv`**：如果尚未安裝，你需要安裝 `python-dotenv` 套件，讓 Python 應用程式能從 `.env` 檔案載入環境變數。可用 `pip` 安裝：

   ```bash
   pip install python-dotenv
   ```

6. **在 Python 腳本中載入環境變數**：在你的 Python 腳本中，使用 `python-dotenv` 套件載入 `.env` 檔案中的環境變數：

   ```python
   from dotenv import load_dotenv
   import os

   # 從 .env 檔案載入環境變數
   load_dotenv()

   # 存取 GITHUB_TOKEN 變數
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

完成！你已成功建立 `.env` 檔案，新增 GitHub 令牌，並將其載入 Python 應用程式。

🔐 千萬不要提交 .env 檔案——它已被加入 .gitignore。  
完整的提供者說明請參考 [`providers.md`](03-providers.md)。

## 4. 下一步？

| 我想要…            | 前往…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| 開始第 1 課         | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| 設定 LLM 提供者     | [`providers.md`](03-providers.md)                                       |
| 認識其他學員        | [加入我們的 Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. 疑難排解

| 症狀                                      | 解決方法                                                        |
|-------------------------------------------|----------------------------------------------------------------|
| 找不到 `python`                           | 將 Python 加入 PATH，或安裝後重新開啟終端機                     |
| Windows 下 `pip` 無法建立 wheels          | 執行 `pip install --upgrade pip setuptools wheel` 後重試       |
| `ModuleNotFoundError: dotenv`             | 執行 `pip install -r requirements.txt`（環境未安裝）            |
| Docker 建置失敗 *No space left*            | Docker Desktop ▸ *設定* ▸ *資源* → 增加磁碟空間                 |
| VS Code 持續提示重新開啟                   | 你可能同時啟用了兩個選項；請選擇一個（venv **或** 容器）         |
| OpenAI 401 / 429 錯誤                      | 檢查 `OPENAI_API_KEY` 值 / 請求速率限制                         |
| 使用 Conda 出錯                           | 使用 `conda install -c microsoft azure-ai-ml` 安裝 Microsoft AI 函式庫 |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->