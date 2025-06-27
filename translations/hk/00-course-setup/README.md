<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:39:37+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "hk"
}
-->
# 開始這門課程

我們非常期待您開始這門課程，看看您會被生成式人工智能激發出什麼樣的創作！

為了確保您的成功，本頁面概述了設置步驟、技術要求以及需要時的求助方式。

## 設置步驟

要開始這門課程，您需要完成以下步驟。

### 1. Fork 此 Repo

[Fork 整個 repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) 到您自己的 GitHub 帳戶，以便能夠更改任何代碼並完成挑戰。您還可以 [star (🌟) 此 repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) 以便更輕鬆找到它和相關的 repo。

### 2. 創建一個 codespace

為了避免在運行代碼時出現任何依賴問題，我們建議在 [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) 中運行這門課程。

您可以在這個 repo 的 forked 版本中選擇 `Code` 選項，然後選擇 **Codespaces** 選項來創建。

![顯示創建 codespace 按鈕的對話框](../../../00-course-setup/images/who-will-pay.webp)

### 3. 存儲您的 API 密鑰

在構建任何類型的應用程式時，保持您的 API 密鑰的安全性非常重要。我們建議不要直接在代碼中存儲任何 API 密鑰。將這些詳細信息提交到公共存儲庫可能會導致安全問題，甚至在被不良行為者使用時產生不必要的成本。
以下是一個如何為 Python 創建 `.env` 文件並添加 `GITHUB_TOKEN` 的逐步指南：

1. **導航到您的項目目錄**：打開您的終端或命令提示符，導航到您要創建 `.env` 文件的項目的根目錄。

   ```bash
   cd path/to/your/project
   ```

2. **創建 `.env` 文件**：使用您喜歡的文本編輯器創建一個名為 `.env` 的新文件。如果您使用命令行，您可以使用 `touch` (on Unix-based systems) or `echo`（在 Windows 上）：

   Unix 系統：
   ```bash
   touch .env
   ```

   Windows：
   ```cmd
   echo . > .env
   ```

3. **編輯 `.env` 文件**：在文本編輯器中打開 `.env` 文件（例如，VS Code、Notepad++ 或其他編輯器）。在文件中添加以下行，將 `your_github_token_here` 替換為您的實際 GitHub token：

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **保存文件**：保存更改並關閉文本編輯器。

5. **安裝 `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` 包以從 `.env` 文件中加載環境變量到您的 Python 應用程式。您可以使用 `pip` 來安裝它：

   ```bash
   pip install python-dotenv
   ```

6. **在您的 Python 腳本中加載環境變量**：在您的 Python 腳本中，使用 `python-dotenv` 包來從 `.env` 文件中加載環境變量：

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

就是這樣！您已成功創建 `.env` 文件，添加了您的 GitHub token，並將其加載到您的 Python 應用程式中。

## 如何在您的電腦上本地運行

要在您的電腦上本地運行代碼，您需要安裝某個版本的 [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)。

然後使用存儲庫，您需要克隆它：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

一旦您檢出所有內容，您就可以開始了！

## 可選步驟

### 安裝 Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是一個輕量級安裝程序，用於安裝 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python 以及一些包。
Conda 本身是一個包管理器，可以輕鬆設置和切換不同的 Python [**虛擬環境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)和包。它在安裝不通過 `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml` 提供的包時也很方便。

繼續用以下代碼片段填充您的環境文件：

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

如果您發現使用 conda 時出現錯誤，可以手動使用以下命令在終端中安裝 Microsoft AI Libraries。

```
conda install -c microsoft azure-ai-ml
```

環境文件指定了我們需要的依賴項。`<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` 是 Python 的最新主要版本。

完成後，您可以繼續在命令行/終端中運行以下命令來創建您的 Conda 環境

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

如果遇到任何問題，請參考 [Conda 環境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

### 使用 Visual Studio Code 和 Python 支援擴展

我們建議使用 [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) 編輯器並安裝 [Python 支援擴展](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 來進行這門課程。然而，這更多的是一個建議，而不是必須的要求。

> **注意**：通過在 VS Code 中打開課程存儲庫，您可以選擇在容器中設置項目。這是因為課程存儲庫中有一個 [特殊的 `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 目錄。稍後會有更多介紹。

> **注意**：一旦您在 VS Code 中克隆並打開目錄，它會自動建議您安裝 Python 支援擴展。

> **注意**：如果 VS Code 建議您在容器中重新打開存儲庫，請拒絕此請求以使用本地安裝的 Python 版本。

### 在瀏覽器中使用 Jupyter

您也可以在瀏覽器中使用 [Jupyter 環境](https://jupyter.org?WT.mc_id=academic-105485-koreyst) 來進行項目開發。無論是經典的 Jupyter 還是 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) 都提供了相當不錯的開發環境，具有自動完成、代碼高亮等功能。

要在本地啟動 Jupyter，請前往終端/命令行，導航到課程目錄，並執行：

```bash
jupyter notebook
```

或

```bash
jupyterhub
```

這將啟動一個 Jupyter 實例，並在命令行窗口中顯示訪問的 URL。

一旦您訪問該 URL，您應該能看到課程大綱並能導航到任何 `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` 文件，查看代碼和輸出。

## 第一次使用 Azure OpenAI 服務

如果這是您第一次使用 Azure OpenAI 服務，請按照指南了解如何 [創建和部署 Azure OpenAI 服務資源。](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## 第一次使用 OpenAI API

如果這是您第一次使用 OpenAI API，請按照指南了解如何 [創建和使用界面。](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## 與其他學員見面

我們在官方 [AI 社群 Discord 伺服器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) 中創建了頻道，供學員交流。這是與其他志同道合的企業家、開發者、學生以及任何希望在生成式人工智能領域提升的人交流的好方式。

[![加入 discord 頻道](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

項目團隊也將在這個 Discord 伺服器上為學員提供幫助。

## 貢獻

這門課程是一個開源計劃。如果您看到改進或問題的地方，請創建 [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) 或記錄 [GitHub 問題](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

項目團隊將跟踪所有貢獻。貢獻開源是一個在生成式人工智能領域建立職業生涯的絕佳方式。

大多數貢獻要求您同意一份貢獻者許可協議 (CLA)，聲明您有權並實際授予我們使用您貢獻的權利。詳細信息請訪問 [CLA，貢獻者許可協議網站](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)。

重要提示：在翻譯此 repo 中的文本時，請確保您不使用機器翻譯。我們將通過社群驗證翻譯，因此請僅在您精通的語言中志願進行翻譯。

當您提交 pull request 時，CLA 機器人將自動確定您是否需要提供 CLA 並適當地裝飾 PR（例如，標籤、評論）。只需按照機器人提供的指示操作。您只需在使用我們的 CLA 的所有存儲庫中進行一次。

此項目已採用 [Microsoft 開源行為準則](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)。欲了解更多信息，請閱讀行為準則常見問題或通過 [Email opencode](opencode@microsoft.com) 聯繫我們以獲取任何其他問題或評論。

## 讓我們開始吧

現在您已完成完成這門課程所需的步驟，讓我們通過獲取 [生成式人工智能和 LLMs 的介紹](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) 開始吧。

**免責聲明**:  
本文件已使用AI翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)進行翻譯。儘管我們努力確保準確性，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤譯不承擔責任。