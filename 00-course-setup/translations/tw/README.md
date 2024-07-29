# 開始這門課程

我們非常興奮地期待你開始這門課程，看看你會受到什麼啟發來使用生成式 AI 建構！

為了確保您的成功，本頁概述了設定步驟、技術需求以及在需要時獲取幫助的地方。

## 設定步驟

要開始這門課程，你需要完成以下步驟。

### 1. 複製這個 Repo

[複製這個整個 repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) 到你自己的 GitHub 帳號，以便更改任何程式碼並完成挑戰。你也可以[標記 (🌟) 這個 repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) 以更容易找到它和相關的 repo。

### 2. 建立一個程式碼空間

為了避免在執行程式碼時出現任何相依性問題，我們建議在[GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)中執行本課程。

這可以通過在您分叉的這個 repo 版本上選擇 `程式碼` 選項並選擇 **Codespaces** 選項來建立。

![顯示按鈕以建立程式碼空間的對話框](../../images/who-will-pay.webp?WT.mc_id=academic-105485-koreyst)

### 3. 儲存您的 API 金鑰

保持您的 API 金鑰安全是建構任何類型應用程式時的重要事項。我們建議不要將任何 API 金鑰直接儲存在您的程式碼中。如果將這些詳細資訊提交到公共儲存庫，可能會導致安全問題，甚至在被惡意使用者利用時產生不必要的費用。

## 如何在本地電腦上執行

要在本機電腦上執行程式碼，你需要安裝某個版本的[Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)。

要使用這個儲存庫，你需要複製它:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

一旦你檢查完所有內容，就可以開始了!

### 安裝 Miniconda (可選步驟)

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是一個輕量級的安裝程式，用於安裝 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python 以及一些套件。
Conda 本身是一個套件管理器，使得設定和切換不同的 Python [**虛擬環境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)和套件變得容易。它也方便用於安裝無法通過 `pip` 獲取的套件。

你可以按照[MiniConda 安裝指南](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst)來設定。

安裝 Miniconda 後，你需要複製這個[repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (如果你還沒有的話)

接下來，你需要建立一個虛擬環境。要使用 Conda 來完成此操作，請繼續建立一個新的環境檔案 (_environment.yml_)。如果你正在使用 Codespaces，請在 `.devcontainer` 目錄中建立此檔案，因此為 `.devcontainer/environment.yml`。

請繼續並使用以下程式碼片段填充您的環境文件:

```yml
name: <environment-name>
channels:
 - defaults
dependencies:
- python=<python-version>
- openai
- python-dotenv
```

環境文件指定了我們需要的相依套件。`<environment-name>` 指的是你想用於 Conda 環境的名稱，而 `<python-version>` 是你想使用的 Python 版本，例如，`3` 是最新的 Python 主要版本。

完成後，您可以在命令列/終端機中執行以下命令來建立您的 Conda 環境

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer 子路徑僅適用於 Codespace 設定
conda activate ai4beg
```

請參考[Conda 環境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)如果你遇到任何問題。

### 使用 Visual Studio Code 搭配 Python 支援擴充功能

我們建議在本課程中使用安裝了[Python 支援擴充功能](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)的[Visual Studio Code (VS Code)](http://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst)編輯器。不過，這只是建議，並不是絕對的要求。

> **注意**: 通過在 VS Code 中打開課程儲存庫，你可以選擇在容器中設定專案。這是因為在課程儲存庫中發現的[特殊 `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)目錄。更多內容稍後介紹。

> **注意**: 一旦你複製並在 VS Code 中打開目錄，它會自動建議你安裝一個 Python 支援擴充套件。

> **注意**: 如果 VS Code 建議你在容器中重新開啟這個儲存庫，請拒絕此請求以使用本地安裝的 Python 版本。

### 在瀏覽器中使用 Jupyter

你也可以在瀏覽器中使用[Jupyter 環境](https://jupyter.org?WT.mc_id=academic-105485-koreyst)來進行專案。經典的 Jupyter 和 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst)都提供了相當愉快的開發環境，具有自動完成、程式碼高亮等功能。

要在本地啟動 Jupyter，請前往終端機/命令列，導航到課程目錄，並執行:

```bash
jupyter notebook
```

或

```bash
jupyterhub
```

這將啟動一個 Jupyter 實例，並且訪問它的 URL 將顯示在命令行視窗中。

一旦你訪問該 URL，你應該會看到課程大綱並能夠導航到任何 `*.ipynb` 文件。例如，`08-building-search-applications/python/oai-solution.ipynb`。

### 執行在容器中

設定所有內容在您的電腦或 Codespace 上的替代方法是使用一個[容器](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst)。課程儲存庫中的特殊 `.devcontainer` 資料夾使 VS Code 能夠在容器內設定專案。在 Codespaces 之外，這將需要安裝 Docker，坦白說，這涉及一些工作，因此我們只建議有容器工作經驗的人使用。

使用 GitHub Codespaces 時，保持 API 金鑰安全的最佳方法之一是使用 Codespace Secrets。請按照[Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst)指南來了解更多資訊。

## 課程和技術需求

這門課程有6個概念課和6個程式碼課。

在程式碼課程中，我們使用 Azure OpenAI 服務。您將需要訪問 Azure OpenAI 服務和一個 API 金鑰來執行這段程式碼。您可以通過[完成此申請](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)來申請訪問權限。

在等待您的應用程式處理時，每個編碼課程還包括一個 `README.md` 文件，您可以在其中查看程式碼和輸出。

## 第一次使用 Azure OpenAI 服務

如果這是您第一次使用 Azure OpenAI 服務，請按照此指南了解如何[建立和部署 Azure OpenAI 服務資源](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)。

## 第一次使用 OpenAI API

如果這是您第一次使用 OpenAI API，請按照指南[建立和使用介面](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)。

## 認識其他學習者

我們已經在我們的官方[AI 社群 Discord 伺服器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)中建立了頻道，以便與其他學習者會面。這是一個與其他志同道合的企業家、建構者、學生和任何希望在生成式 AI 中提升的人聯繫的好方法。

[![加入 discord 頻道](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

專案團隊也會在這個 Discord 伺服器上幫助任何學習者。

## 貢獻

這門課程是一個開放原始碼計劃。如果您看到改進的地方或問題，請建立一個[Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)或記錄一個[GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

專案團隊將追蹤所有貢獻。對開放原始碼做出貢獻是建立你在生成式 AI 領域職業生涯的驚人方式。

大多數的貢獻需要您同意貢獻者許可協議（CLA），聲明您有權並實際上授予我們使用您的貢獻的權利。詳情請訪問[CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)。

重要事項: 在翻譯此 repo 中的文字時，請確保不要使用機器翻譯。我們將通過社群驗證翻譯，因此請僅在您精通的語言中自願進行翻譯。

當你提交一個拉取請求時，CLA-bot 會自動判斷你是否需要提供 CLA 並適當地裝飾 PR (例如，標籤、評論)。只需按照 bot 提供的指示操作。你只需在所有使用我們 CLA 的儲存庫中執行一次此操作。

此專案已採用[Microsoft 開放原始碼行為準則](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)。如需更多資訊，請閱讀行為準則常見問題或聯絡[Email opencode](opencode@microsoft.com)以獲取任何其他問題或意見。

## 讓我們開始吧

現在你已經完成了完成這門課程所需的步驟，讓我們開始[介紹生成式 AI 和 LLMs](../../../01-introduction-to-genai/translations/tw/README.md?WT.mc_id=academic-105485-koreyst)。

