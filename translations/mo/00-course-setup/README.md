<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T14:39:09+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "mo"
}
-->
# 開始這門課程

我們非常期待你開始這門課程，看看你會受到生成式 AI 啟發，打造出什麼有趣的作品！

為了確保你能順利學習，這一頁會說明設定步驟、技術需求，以及遇到問題時可以去哪裡尋求協助。

## 設定步驟

要開始這門課程，你需要完成以下步驟。

### 1. Fork 這個 Repo

[將整個 repo fork](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) 到你自己的 GitHub 帳號，這樣你才能修改程式碼並完成挑戰。你也可以[給這個 repo 加星 (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)，方便日後找到它和相關的 repo。

### 2. 建立 codespace

為了避免執行程式時遇到相依性問題，我們建議你在 [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) 上進行這門課程。

在你的 fork 裡：**Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 新增密鑰

1. ⚙️ 齒輪圖示 -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret。
2. 名稱填 OPENAI_API_KEY，貼上你的金鑰，然後儲存。

### 3. 接下來呢？

| 我想要…              | 前往…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| 開始第一課           | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| 離線操作             | [`setup-local.md`](02-setup-local.md)                                   |
| 設定 LLM 服務商      | [`providers.md`](providers.md)                                          |
| 認識其他學習者       | [加入我們的 Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 疑難排解

| 症狀                                       | 解決方法                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| Container 建置超過 10 分鐘卡住             | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal 沒有連上；點選 **+** ➜ *bash*                          |
| OpenAI 回傳 `401 Unauthorized`            | `OPENAI_API_KEY` 錯誤或過期                                     |
| VS Code 顯示 “Dev container mounting…”    | 重新整理瀏覽器分頁—Codespaces 有時會斷線                        |
| Notebook kernel 不見了                    | Notebook 選單 ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix 系統：

   ```bash
   touch .env
   ```

   Windows：

   ```cmd
   echo . > .env
   ```

3. **編輯 `.env` 檔案**：用文字編輯器（例如 VS Code、Notepad++ 或其他）打開 `.env` 檔案。加入以下這一行，把 `your_github_token_here` 換成你自己的 GitHub token：

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **儲存檔案**：儲存修改後關閉編輯器。

5. **安裝 `python-dotenv`**：如果你還沒安裝，請用 `pip` 安裝 `python-dotenv` 套件，讓 Python 應用程式能從 `.env` 檔案載入環境變數：

   ```bash
   pip install python-dotenv
   ```

6. **在 Python 程式中載入環境變數**：在你的 Python 程式裡，使用 `python-dotenv` 套件載入 `.env` 檔案的環境變數：

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

## 如何在本機執行

如果你想在自己的電腦上執行程式，請先[安裝 Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)。

接著，請將這個 repository 複製下來：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

一切準備好之後，就可以開始囉！

## 選擇性步驟

### 安裝 Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是一個輕量級的 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst) 安裝程式，可以安裝 Python 及一些套件。
Conda 本身是一個套件管理工具，可以輕鬆建立和切換不同的 Python [**虛擬環境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) 和套件。對於安裝 `pip` 沒有的套件也很方便。

你可以參考 [MiniConda 安裝指南](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) 來設定。

安裝好 Miniconda 後，請將 [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) 複製下來（如果還沒做的話）

接下來，你需要建立一個虛擬環境。用 Conda 建立新環境檔案（_environment.yml_）。如果你是在 Codespaces 上操作，請在 `.devcontainer` 目錄下建立，也就是 `.devcontainer/environment.yml`。

請將以下內容加入你的環境檔案：

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

如果你發現用 conda 安裝有問題，可以在終端機手動安裝 Microsoft AI Libraries，指令如下：

```
conda install -c microsoft azure-ai-ml
```

環境檔案會列出我們需要的相依套件。`<environment-name>` 是你想給 Conda 環境取的名字，`<python-version>` 則是你想用的 Python 版本，例如 `3` 代表最新主版本。

完成後，在命令列/終端機執行以下指令建立 Conda 環境：

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

如果遇到問題，可以參考 [Conda 環境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

### 用 Visual Studio Code 和 Python 擴充套件

我們建議你使用 [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) 編輯器，並安裝 [Python 擴充套件](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 來進行這門課程。不過這只是建議，並非強制。

> **Note**: 只要你在 VS Code 裡打開課程 repository，就可以選擇在容器中設定專案。這是因為課程 repository 裡有 [特別的 `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 目錄。後面會再詳細說明。

> **Note**: 當你 clone 並在 VS Code 開啟目錄時，VS Code 會自動建議你安裝 Python 擴充套件。

> **Note**: 如果 VS Code 建議你在容器中重新開啟 repository，請拒絕這個要求，這樣才能用本機安裝的 Python。

### 在瀏覽器中使用 Jupyter

你也可以直接在瀏覽器裡用 [Jupyter 環境](https://jupyter.org?WT.mc_id=academic-105485-koreyst) 來進行專案。無論是經典 Jupyter 還是 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) 都有自動補全、程式碼高亮等方便的開發功能。

要在本機啟動 Jupyter，請打開終端機/命令列，切換到課程目錄，然後執行：

```bash
jupyter notebook
```

或

```bash
jupyterhub
```

這樣就會啟動 Jupyter，命令列視窗會顯示存取網址。

進入網址後，你會看到課程大綱，可以瀏覽任何 `*.ipynb` 檔案。例如 `08-building-search-applications/python/oai-solution.ipynb`。

### 在容器中執行

除了在本機或 Codespace 設定環境外，你也可以用 [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)。課程 repository 裡的 `.devcontainer` 資料夾，讓 VS Code 可以在容器中設定專案。如果不是用 Codespaces，這會需要安裝 Docker，步驟也比較多，所以我們只建議有容器經驗的人使用。

在 GitHub Codespaces 上，最安全的 API 金鑰管理方式之一就是使用 Codespace Secrets。請參考 [Codespaces secrets 管理指南](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) 了解更多。

## 課程內容與技術需求

這門課有 6 個概念課程和 6 個程式實作課程。

在程式實作課程中，我們會用到 Azure OpenAI 服務。你需要有 Azure OpenAI 服務的存取權和 API 金鑰才能執行程式。你可以[填寫申請表](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)來申請存取權。

在等待申請審核期間，每個程式課程也都有 `README.md` 檔案，你可以直接瀏覽程式碼和執行結果。

## 第一次使用 Azure OpenAI 服務

如果你是第一次使用 Azure OpenAI 服務，請參考這份教學：[建立並部署 Azure OpenAI 服務資源](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## 第一次使用 OpenAI API

如果你是第一次使用 OpenAI API，請參考這份教學：[建立並使用介面](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## 認識其他學習者

我們在官方 [AI Community Discord 伺服器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) 建立了頻道，方便大家互相交流。這是認識志同道合的創業者、開發者、學生，以及想精進生成式 AI 的朋友的好方法。

[![加入 discord 頻道](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

專案團隊也會在這個 Discord 伺服器上協助學習者。

## 貢獻

這門課是開源計畫。如果你發現可以改進的地方或有問題，請提出 [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) 或回報 [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

專案團隊會追蹤所有貢獻。參與開源專案是建立生成式 AI 職涯的絕佳方式。

大多數貢獻都需要你同意貢獻者授權協議（CLA），聲明你有權利並同意授權我們使用你的貢獻。詳情請參考 [CLA, Contributor License Agreement 網站](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)。

重要提醒：翻譯本 repo 內容時，請不要使用機器翻譯。我們會透過社群驗證翻譯品質，所以請只翻譯你精通的語言。

當你提交 pull request 時，CLA-bot 會自動判斷你是否需要簽署 CLA，並在 PR 上標註（例如標籤、留言）。只要依照 bot 的指示操作即可。你只需要在所有使用我們 CLA 的 repository 裡做一次這個動作。

本專案採用 [Microsoft 開源行為準則](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)。更多資訊請參閱行為準則 FAQ，或聯絡 [Email opencode](opencode@microsoft.com) 提出其他問題或意見。

## 讓我們開始吧
現在你已經完成了這門課程所需的步驟，讓我們開始吧，先來看看[生成式 AI 和大型語言模型的簡介](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)。

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應視為具權威性的來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。