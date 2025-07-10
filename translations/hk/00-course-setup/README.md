<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T07:02:35+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "hk"
}
-->
# 開始這個課程

我們非常期待你開始這個課程，看看你會被生成式 AI 啟發去創造什麼！

為了確保你的學習順利，這頁面會說明設定步驟、技術需求，以及需要幫助時該去哪裡尋求協助。

## 設定步驟

要開始這個課程，你需要完成以下步驟。

### 1. Fork 這個 Repo

將[整個 repo fork](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)到你自己的 GitHub 帳號，這樣你才能修改程式碼並完成挑戰。你也可以[為這個 repo 加星號 (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)，方便日後找到它和相關的 repo。

### 2. 建立 codespace

為避免執行程式碼時出現相依性問題，我們建議你在[GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)中執行這個課程。

你可以在你 fork 後的 repo 中選擇 `Code` 選項，然後選擇 **Codespaces** 來建立。

![Dialog showing buttons to create a codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. 儲存你的 API 金鑰

在開發任何應用程式時，保護你的 API 金鑰安全非常重要。我們建議不要直接把 API 金鑰寫在程式碼裡。若把這些資訊提交到公開的 repo，可能會造成安全風險，甚至被不法人士濫用導致額外費用。

以下是如何為 Python 建立 `.env` 檔案並加入 `GITHUB_TOKEN` 的逐步教學：

1. **前往你的專案目錄**：打開終端機或命令提示字元，切換到你想建立 `.env` 檔案的專案根目錄。

   ```bash
   cd path/to/your/project
   ```

2. **建立 `.env` 檔案**：使用你喜歡的文字編輯器建立一個名為 `.env` 的新檔案。如果用命令列，可以用 `touch`（Unix 系統）或 `echo`（Windows）：

   Unix 系統：

   ```bash
   touch .env
   ```

   Windows：

   ```cmd
   echo . > .env
   ```

3. **編輯 `.env` 檔案**：用文字編輯器（例如 VS Code、Notepad++ 或其他）打開 `.env` 檔案，加入以下內容，將 `your_github_token_here` 替換成你的 GitHub token：

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **儲存檔案**：儲存並關閉編輯器。

5. **安裝 `python-dotenv`**：如果還沒安裝，你需要安裝 `python-dotenv` 套件，讓 Python 程式能從 `.env` 檔案讀取環境變數。可用 `pip` 安裝：

   ```bash
   pip install python-dotenv
   ```

6. **在 Python 程式中載入環境變數**：在你的 Python 程式碼中，使用 `python-dotenv` 套件載入 `.env` 檔案的環境變數：

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

完成以上步驟後，你就成功建立 `.env` 檔案，加入 GitHub token，並在 Python 應用程式中載入它。

## 如何在本機電腦執行

要在本機電腦執行程式碼，你需要先安裝某個版本的[Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)。

接著，你需要把這個 repo clone 下來：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

確認所有檔案都下載完成後，就可以開始使用了！

## 選擇性步驟

### 安裝 Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是一個輕量級的安裝器，用來安裝 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python 以及一些套件。

Conda 是一個套件管理工具，可以輕鬆建立和切換不同的 Python [**虛擬環境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) 和套件。它也方便安裝一些無法用 `pip` 取得的套件。

你可以參考[MiniConda 安裝指南](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst)來完成安裝。

安裝好 Miniconda 後，如果還沒 clone repo，請先 clone [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)。

接著，你需要建立虛擬環境。使用 Conda 的話，請建立一個環境設定檔（_environment.yml_）。如果你是用 Codespaces，請在 `.devcontainer` 目錄下建立，也就是 `.devcontainer/environment.yml`。

把以下內容填入你的環境設定檔：

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

如果你使用 conda 遇到錯誤，可以在終端機手動安裝 Microsoft AI Libraries，指令如下：

```
conda install -c microsoft azure-ai-ml
```

環境設定檔會指定我們需要的相依套件。`<environment-name>` 是你想用的 Conda 環境名稱，`<python-version>` 是你想用的 Python 版本，例如 `3` 是最新的主要版本。

完成後，你可以在命令列/終端機執行以下指令來建立 Conda 環境：

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

如果遇到問題，可以參考[Conda 環境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

### 使用 Visual Studio Code 搭配 Python 支援擴充功能

我們建議使用[Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst)編輯器，並安裝[Python 支援擴充功能](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)來進行這個課程。不過這只是建議，並非硬性要求。

> **Note**：在 VS Code 開啟課程 repo 時，你可以選擇在容器中設定專案。這是因為課程 repo 裡有[特殊的 `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)目錄。後面會再說明。

> **Note**：當你 clone 並在 VS Code 開啟目錄時，它會自動建議你安裝 Python 支援擴充功能。

> **Note**：如果 VS Code 建議你重新在容器中開啟 repo，請拒絕此請求，以便使用本機安裝的 Python 版本。

### 在瀏覽器中使用 Jupyter

你也可以直接在瀏覽器中使用 [Jupyter 環境](https://jupyter.org?WT.mc_id=academic-105485-koreyst)來開發。無論是經典版 Jupyter 或是 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst)，都提供了自動補全、程式碼高亮等不錯的開發體驗。

要在本機啟動 Jupyter，請打開終端機/命令列，切換到課程目錄，執行：

```bash
jupyter notebook
```

或

```bash
jupyterhub
```

這會啟動一個 Jupyter 服務，命令列視窗會顯示可用的 URL。

打開該 URL 後，你會看到課程大綱，並能瀏覽任何 `*.ipynb` 檔案，例如 `08-building-search-applications/python/oai-solution.ipynb`。

### 在容器中執行

另一個選擇是使用[容器](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)，而課程 repo 裡的特殊 `.devcontainer` 資料夾讓 VS Code 可以在容器中設定專案。

如果不使用 Codespaces，這需要安裝 Docker，且設定上較為繁複，因此我們只建議有容器使用經驗的人採用。

在使用 GitHub Codespaces 時，保護 API 金鑰安全的最佳方法之一是使用 Codespace Secrets。請參考[Codespaces secrets 管理指南](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst)了解更多。

## 課程內容與技術需求

課程包含 6 個概念課程和 6 個程式設計課程。

程式設計課程會使用 Azure OpenAI Service。你需要有 Azure OpenAI 服務的存取權和 API 金鑰才能執行程式碼。你可以透過[填寫申請表](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)來申請存取權。

在等待申請審核期間，每個程式設計課程也會附有 `README.md` 檔案，讓你可以查看程式碼和輸出結果。

## 第一次使用 Azure OpenAI Service

如果你是第一次使用 Azure OpenAI 服務，請參考這份教學，了解如何[建立並部署 Azure OpenAI Service 資源](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)。

## 第一次使用 OpenAI API

如果你是第一次使用 OpenAI API，請參考這份教學，了解如何[建立並使用介面](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)。

## 認識其他學員

我們在官方的 [AI Community Discord 伺服器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)中建立了頻道，方便你認識其他學員。這是與志同道合的創業家、開發者、學生，以及所有想在生成式 AI 領域提升自己的人交流的好地方。

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

專案團隊也會在這個 Discord 伺服器上協助學員。

## 貢獻

這個課程是開源計畫。如果你發現可以改進的地方或有問題，請提出[Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)或回報[GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

專案團隊會追蹤所有貢獻。參與開源是建立生成式 AI 事業的絕佳方式。

大多數貢獻需要你同意一份貢獻者授權協議 (CLA)，聲明你有權利且確實授權我們使用你的貢獻。詳情請參考[CLA，貢獻者授權協議網站](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)。

重要提醒：翻譯此 repo 內的文字時，請勿使用機器翻譯。我們會透過社群驗證翻譯品質，因此請只在你熟悉的語言中自願參與翻譯。

當你提交 pull request 時，CLA-bot 會自動判斷你是否需要提供 CLA，並在 PR 上標示（例如標籤、留言）。只要依照機器人的指示操作即可。你只需在所有使用我們 CLA 的 repo 中做一次。

本專案已採用[Microsoft 開源行為準則](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)。更多資訊請參閱行為準則常見問題，或透過 [Email opencode](opencode@microsoft.com) 聯絡我們。

## 開始吧

既然你已完成完成課程所需的步驟，現在就從[生成式 AI 與大型語言模型的介紹](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)開始吧！

**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。