# 開始這門課程

我們非常期待你開始這門課程，看看你會被生成式 AI 啟發去創造什麼！

為確保你的成功，本頁面概述了設定步驟、技術需求，以及有需要時可以獲得幫助的地方。

## 設定步驟

開始上這門課程前，你需要完成以下步驟。

### 1. 分叉這個倉庫

將[整個這個倉庫分叉](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)到你自己的 GitHub 帳號，以便修改程式碼及完成挑戰。你也可以[⭐ 標星這個倉庫](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)，方便日後找到它和相關倉庫。

### 2. 建立一個 codespace

為避免執行程式碼時出現任何相依性問題，我們建議你使用[GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) 來執行這門課程。

在你分叉後的倉庫：**Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/zh-TW/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 新增機密

1. ⚙️ 設定圖示 -> Command Pallete -> Codespaces : 管理使用者機密 -> 新增一個機密。
2. 名稱輸入 OPENAI_API_KEY，貼上你的金鑰，儲存。

### 3. 接下來要做什麼？

| 我想要…           | 前往…                                                                  |
|-------------------|-------------------------------------------------------------------------|
| 開始第 1 課       | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| 離線作業          | [`setup-local.md`](02-setup-local.md)                                   |
| 設定 LLM 提供商     | [`providers.md`](03-providers.md)                                        |
| 認識其他學員       | [加入我們的 Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 疑難排解


| 症狀                                   | 解決方法                                                             |
|----------------------------------------|---------------------------------------------------------------------|
| 容器建置卡住超過 10 分鐘                | **Codespaces ➜ “Rebuild Container”**                               |
| `python: command not found`              | 終端機尚未連接，點擊 **+** ➜ *bash*                                 |
| OpenAI 回傳 `401 Unauthorized`          | `OPENAI_API_KEY` 錯誤或過期                                         |
| VS Code 顯示「Dev container mounting…」 | 重新整理瀏覽器分頁—Codespaces 有時會失去連線                        |
| Notebook kernel 不見                    | Notebook 選單 ➜ **Kernel ▸ Select Kernel ▸ Python 3**               |

   Unix 系統：

   ```bash
   touch .env
   ```

   Windows：

   ```cmd
   echo . > .env
   ```

3. **編輯 `.env` 檔案**：打開 `.env` 檔案，使用文字編輯器 (例如 VS Code、Notepad++ 或其他編輯器)，新增以下行，將 `your_github_token_here` 替換成你的 GitHub 權杖：

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **儲存檔案**：儲存變更並關閉文字編輯器。

5. **安裝 `python-dotenv`**：如果還沒有安裝，你需要安裝 `python-dotenv` 套件，讓 Python 程式能從 `.env` 檔案載入環境變數。你可以用 `pip` 安裝：

   ```bash
   pip install python-dotenv
   ```

6. **在 Python 程式中載入環境變數**：在 Python 程式碼中，使用 `python-dotenv` 套件載入 `.env` 檔案中的環境變數：

   ```python
   from dotenv import load_dotenv
   import os

   # 從 .env 檔案載入環境變數
   load_dotenv()

   # 存取 GITHUB_TOKEN 變數
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

就是這樣！你已成功建立 `.env` 檔案、新增 GitHub 權杖，並在 Python 應用程式中載入。

## 如何在電腦本機執行

若要在電腦本機執行程式碼，你需要先[安裝某版本的 Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)。

接著使用本倉庫，需先複製(clone)到本地：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

確定所有內容準備妥當後，就可以開始了！

## 選用步驟

### 安裝 Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是一個輕量安裝器，用於安裝 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python，以及部分套件。  
Conda 本身是一個套件管理工具，能輕鬆建立並切換不同的 Python [**虛擬環境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) 和套件。對於使用 `pip` 無法取得的套件，Conda 也非常方便。

你可以依照 [MiniConda 安裝指南](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) 進行設定。

安裝 Miniconda 後，如果尚未複製[本倉庫](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)，請先複製。

接下來你需要建立一個虛擬環境。使用 Conda 建立時，請製作一個環境設定檔 (_environment.yml_)。若在 Codespaces 內操作，請將此檔案放在 `.devcontainer` 目錄下，即 `.devcontainer/environment.yml`。

請使用以下程式碼填入你的環境設定檔：

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

如果你在使用 conda 時遇錯誤，可以用終端機執行以下命令手動安裝 Microsoft AI 函式庫。

```
conda install -c microsoft azure-ai-ml
```

環境設定檔裡列出我們需要的依賴項。`<environment-name>` 是你想要給這個 Conda 環境取的名稱，`<python-version>` 是你想使用的 Python 版本，例如 `3` 是最新主版本。

完成後，你可以執行以下命令建立 Conda 環境：

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer 子路徑僅適用於 Codespace 設定
conda activate ai4beg
```

如有問題，請參考 [Conda 環境相關指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

### 使用 Visual Studio Code 搭配 Python 支援外掛

我們建議使用 [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) 編輯器，並安裝 [Python 支援外掛](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 來進行本課程。不過這只是建議，非硬性規定。

> **注意**：打開課程倉庫於 VS Code 時，你可以選擇在容器中設定專案，這是因為課程中有[特別的 `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 資料夾，稍後會再說明。

> **注意**：複製並打開目錄於 VS Code 會自動建議你安裝 Python 支援外掛。

> **注意**：若 VS Code 建議重新在容器中開啟倉庫，請拒絕此請求，以使用本機安裝的 Python 版本。

### 在瀏覽器使用 Jupyter

你也可以直接在瀏覽器使用 [Jupyter 環境](https://jupyter.org?WT.mc_id=academic-105485-koreyst) 工作。無論是經典版 Jupyter 或 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst)，都提供了愉快的開發經驗，包含自動完成、語法高亮等功能。

若要在本機啟動 Jupyter，請打開終端機，切換至課程目錄，執行：

```bash
jupyter notebook
```

或是

```bash
jupyterhub
```

此指令會啟動 Jupyter 執行個體，並在命令列視窗顯示可存取的網址。

進入網址後，你將看到課程大綱，並可瀏覽任何 `*.ipynb` 檔案，例如 `08-building-search-applications/python/oai-solution.ipynb`。

### 在容器中執行

另一個選擇是使用[容器](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)，不論是在電腦或 Codespace 以外。課程中有特別的 `.devcontainer` 資料夾，讓 VS Code 能在容器中設定專案。除 Codespaces 外這需要安裝 Docker，且設定繁複，因此我們建議有容器經驗的人使用。

在 GitHub Codespaces 裡保護 API 金鑰的好方法之一是使用 Codespace Secrets。請依照[Codespaces 機密管理指南](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst)了解詳情。

## 課程內容與技術需求

本課程包含 6 章概念課程與 6 章程式實作課程。

實作課程中，我們使用 Azure OpenAI 服務。你需要有 Azure OpenAI 服務的存取權及 API 金鑰才能執行程式碼。你可以透過[填寫申請表](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)來申請使用。

等待申請審核時，每課程的實作亦附有 `README.md` 檔案，可先瀏覽程式碼和輸出結果。

## 初次使用 Azure OpenAI 服務

若你是第一次使用 Azure OpenAI 服務，請參考本指南如何[建立及部署 Azure OpenAI 服務資源。](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## 初次使用 OpenAI API

若你是第一次使用 OpenAI API，請參考此指南如何[建立及使用介面。](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## 認識其他學員

我們在官方 [AI 社群 Discord 伺服器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)中設立了學員管道，是與其他志同道合的創業家、開發者、學生交流，提升生成式 AI 技能的好地方。

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

課程團隊也會在這個 Discord 伺服器協助學員。

## 參與貢獻

這門課程是開源計畫。如果你發現可改進之處或問題，請提出[拉取請求 (Pull Request)](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)或回報[GitHub 問題 (Issue)](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

課程團隊會追蹤所有貢獻。貢獻開源專案是建立生成式 AI 職涯的絕佳途徑。

大多數貢獻需同意貢獻者授權協議 (CLA)，聲明你有權且同意授權我們使用你的貢獻。詳情請參考 [CLA 貢獻者授權協議網站](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)。

重要提醒：翻譯本倉庫文字時，請勿使用機器翻譯。我們將透過社群審核翻譯品質，請只在你精通的語言自願提供翻譯。

提交拉取請求時，CLA 機器人會自動判定是否需要你提供 CLA，並在 PR 上標記（例如標籤、評論）。請依機器人指示操作，整個平台只需完成一次。

本專案採用 [Microsoft 開源行為守則](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)，詳情請閱讀行為守則常見問題或透過 [Email opencode](opencode@microsoft.com) 連絡我們。

## 讓我們開始吧！
現在您已完成了完成本課程所需的步驟，讓我們開始透過 [生成式 AI 和大型語言模型介紹](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) 來開始學習。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->