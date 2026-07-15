# 本地設置 🖥️

**如果你想在自己電腦上運行所有內容，請使用此指南。**   
你有兩條路徑：**(A) 原生 Python + virtual-env** 或 **(B) VS Code 開發容器搭配 Docker**。  
選擇你覺得較容易的一種——兩者都會帶你完成相同的課程。

## 1.  前置條件

| 工具               | 版本 / 備註                                                                      |
|--------------------|----------------------------------------------------------------------------------|
| **Python**         | 3.10 以上（可從 <https://python.org> 下載）                                      |
| **Git**            | 最新版本（隨 Xcode / Windows Git / Linux 套件管理器一起提供）                   |
| **VS Code**        | 非必需但建議使用 <https://code.visualstudio.com>                               |
| **Docker Desktop** | 僅適用於方案 B。可免費安裝： <https://docs.docker.com/desktop/>                |

> 💡 <strong>技巧</strong> – 在終端機驗證工具版本：  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. 方案 A – 原生 Python（最快）

### 步驟 1  克隆此倉庫

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### 步驟 2 建立並啟用虛擬環境

```bash
python -m venv .venv          # 製作一個
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ 提示符現在應該以 (.venv) 開頭——代表你已進入此環境。

### 步驟 3 安裝相依套件

```bash
pip install -r requirements.txt
```

可直接跳到第 3 節，參考[API 密鑰設定](#3-新增你的-api-金鑰)

## 2. 方案 B – VS Code 開發容器（Docker）

我們為此倉庫和課程設置了一個 <a href="https://containers.dev?WT.mc_id=academic-105485-koreyst">開發容器</a>，其統一運行時支援 Python3、.NET、Node.js 和 Java 開發。相關設定定義於倉庫根目錄的 `.devcontainer/devcontainer.json`。

>**為何選擇此方案？**
>環境與 Codespaces 完全一致，避免依賴漂移。

### 步驟 0 安裝額外軟體

Docker Desktop – 確認可執行 `docker --version`。
VS Code Remote – Containers 擴充功能（ID：ms-vscode-remote.remote-containers）。

### 步驟 1 在 VS Code 開啟倉庫

檔案 ▸ 開啟資料夾…  → generative-ai-for-beginners

VS Code 會偵測到 .devcontainer/ 並跳出提示。

### 步驟 2 重新在容器中打開

點擊「Reopen in Container」。Docker 第一次會建構映像檔（約 3 分鐘）。
當終端機提示符出現，即表示你已在容器內。

## 2. 方案 C – Miniconda

<a href="https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst">Miniconda</a> 是一個輕量級安裝器，用於安裝 <a href="https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst">Conda</a>、Python 以及部分套件。
Conda 本身是一個套件管理器，方便設置及切換不同 Python <a href="https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst"><b>虛擬環境</b></a>與套件。當套件無法透過 `pip` 安裝時也相當有用。

### 步驟 0  安裝 Miniconda

請依照 <a href="https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst">MiniConda 安裝指南</a> 進行安裝。

```bash
conda --version
```

### 步驟 1 建立虛擬環境文件

建立一個新的環境檔案（*environment.yml*）。如果你使用 Codespaces 跟著做，請在 `.devcontainer` 目錄中建立，即 `.devcontainer/environment.yml`。

### 步驟 2 編輯你的環境檔案

在 `environment.yml` 中加入以下內容片段

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

### 步驟 3 建立你的 Conda 環境

在終端機執行以下指令

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer 子路徑只適用於 Codespace 設置
conda activate ai4beg
```

若遇到問題，請參考 <a href="https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst">Conda 環境指南</a>。

## 2 方案 D – 經典 Jupyter / Jupyter Lab（瀏覽器內）

> **適合誰？**  
> 喜愛經典 Jupyter 介面或不想使用 VS Code 執行筆記本的任何人。  

### 步驟 1 確認是否已安裝 Jupyter

要在本機啟動 Jupyter，前往終端機／命令列，切換至課程目錄，然後執行：

```bash
jupyter notebook
```

或是

```bash
jupyterhub
```

這會啟動一個 Jupyter 實例，命令列視窗中會顯示存取網址。

訪問網址後，你應可看到課程大綱並瀏覽任何 `*.ipynb` 檔案。例如 `08-building-search-applications/python/oai-solution.ipynb`。

## 3. 新增你的 API 金鑰

保護你的 API 金鑰安全非常重要。我們建議不要直接將金鑰寫在程式碼中。若未加以保護並推送至公開倉庫，可能會產生安全風險，甚至遭不肖人士濫用帶來意外花費。
這裡有一步步教你如何為 Python 建立 `.env` 檔案並加入 Microsoft Foundry Models 認證：

> **注意：** GitHub Models（及其 `GITHUB_TOKEN` 變數）將在 2026 年 7 月底退役。本指南改使用 <a href="https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst">Microsoft Foundry Models</a>。若想完全離線，可參考 <a href="https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst">Foundry Local</a>。

1. <strong>定位到你的專案目錄</strong>：打開終端機或命令提示字元，切換到你想建立 `.env` 檔案的專案根目錄。

   ```bash
   cd path/to/your/project
   ```

2. **建立 `.env` 檔案**：用你慣用的文字編輯器建立一個新檔案，命名為 `.env`。若使用命令列，可用 `touch`（Unix 系統）或 `echo`（Windows）：

   Unix 系統：

   ```bash
   touch .env
   ```

   Windows：

   ```cmd
   echo . > .env
   ```

3. **編輯 `.env` 檔案**：用文字編輯器打開 `.env`（如 VS Code、Notepad++ 或任何其他編輯器），將以下內容貼入，並以你的 Microsoft Foundry 專案端點和 API 金鑰替代占位符：

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. <strong>保存檔案</strong>：儲存變更並關閉文字編輯器。

5. **安裝 `python-dotenv`**：如果尚未安裝，需安裝 `python-dotenv` 套件以讀取 `.env` 檔中的環境變數到 Python 程式中。可用 `pip` 安裝：

   ```bash
   pip install python-dotenv
   ```

6. **在你的 Python 腳本中加載環境變數**：在 Python 腳本中，使用 `python-dotenv` 套件讀取 `.env` 裡的環境變數：

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

就這樣！你已成功建立 `.env` 檔案，加入了 Microsoft Foundry Models 的認證，並載入到 Python 應用程式中。

🔐 切勿將 .env 提交至版本庫——它已被加入 .gitignore。
詳細的服務商指引請參見 [`providers.md`](03-providers.md)。

## 4. 接下來做什麼？

| 我想要…             | 前往…                                                                 |
|---------------------|------------------------------------------------------------------------|
| 開始第 1 課            | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)   |
| 設定大型語言模型供應商 | [`providers.md`](03-providers.md)                                     |
| 認識其他學習者          | [加入我們的 Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. 疑難排解

| 狀況                                           | 解決方案                                                     |
|-------------------------------------------------|-------------------------------------------------------------|
| 找不到 `python` 命令                             | 安裝後將 Python 加入 PATH，或重新開啟終端機                   |
| Windows 下無法用 `pip` 建構 wheel                  | 執行 `pip install --upgrade pip setuptools wheel` 後重試       |
| 出現 `ModuleNotFoundError: dotenv`                | 執行 `pip install -r requirements.txt`（虛擬環境未安裝套件）    |
| Docker 建構失敗，顯示 *No space left*              | Docker Desktop ▸ <em>設定</em> ▸ <em>資源</em> → 增加磁碟空間                 |
| VS Code 不斷提示重新打開                            | 你可能同時啟用多種方案；請只選擇一個（venv <strong>或</strong> 容器）          |
| OpenAI 回傳 401 / 429 錯誤                          | 檢查 `OPENAI_API_KEY` 值是否正確 / 請求速率限制                  |
| Conda 使用時出錯                                  | 用 `conda install -c microsoft azure-ai-ml` 安裝 Microsoft AI 函式庫 |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->