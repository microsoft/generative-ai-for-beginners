<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:40:09+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "tw"
}
-->
# 開始這門課程

我們非常期待您開始這門課程，並看到您受到生成式 AI 的啟發，構建出什麼樣的作品！

為了確保您的成功，這一頁概述了設置步驟、技術要求，以及在需要時如何獲得幫助。

## 設置步驟

要開始這門課程，您需要完成以下步驟。

### 1. Fork 這個 Repo

[Fork 整個 repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) 到您自己的 GitHub 帳戶，以便能夠更改任何代碼並完成挑戰。您也可以[star (🌟) 這個 repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) 以更輕鬆找到它和相關的 repo。

### 2. 創建一個 codespace

為了避免運行代碼時的任何依賴問題，我們建議在 [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) 中運行這門課程。

這可以通過在您 fork 的這個 repo 版本中選擇 `Code` 選項，然後選擇 **Codespaces** 選項來創建。

![顯示如何創建 codespace 的對話框](../../../00-course-setup/images/who-will-pay.webp)

### 3. 儲存您的 API 金鑰

在構建任何類型的應用程式時，保持您的 API 金鑰安全是很重要的。我們建議不要將任何 API 金鑰直接存儲在您的代碼中。將這些詳細信息提交到公共倉庫可能會導致安全問題，甚至在被不良行為者使用時產生不必要的費用。
以下是如何為 Python 創建 `.env` 文件並添加 `GITHUB_TOKEN` 的分步指南：

1. **導航到您的專案目錄**：打開您的終端或命令提示符，導航到您想創建 `.env` 文件的專案根目錄。

   ```bash
   cd path/to/your/project
   ```

2. **創建 `.env` 文件**：使用您喜歡的文本編輯器創建一個名為 `.env` 的新文件。如果您使用的是命令行，您可以使用 `touch` (on Unix-based systems) or `echo`（在 Windows 上）：

   基於 Unix 的系統：
   ```bash
   touch .env
   ```

   Windows：
   ```cmd
   echo . > .env
   ```

3. **編輯 `.env` 文件**：在文本編輯器中打開 `.env` 文件（例如 VS Code、Notepad++ 或任何其他編輯器）。將以下行添加到文件中，將 `your_github_token_here` 替換為您的實際 GitHub token：

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **保存文件**：保存更改並關閉文本編輯器。

5. **安裝 `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` 套件以從 `.env` 文件中加載環境變量到您的 Python 應用程式中。您可以使用 `pip` 安裝它：

   ```bash
   pip install python-dotenv
   ```

6. **在您的 Python 腳本中加載環境變量**：在您的 Python 腳本中，使用 `python-dotenv` 套件從 `.env` 文件中加載環境變量：

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

然後要使用這個倉庫，您需要克隆它：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

一旦您檢出所有內容，您就可以開始了！

## 可選步驟

### 安裝 Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是一個輕量級的安裝程序，用於安裝 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python 以及一些套件。
Conda 本身是一個包管理器，可以輕鬆設置和切換不同的 Python [**虛擬環境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) 和套件。它也非常適合安裝不通過 `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml` 提供的套件。

繼續並使用下面的代碼片段填充您的環境文件：

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

如果您發現使用 conda 出現錯誤，可以手動在終端中使用以下命令安裝 Microsoft AI Libraries。

```
conda install -c microsoft azure-ai-ml
```

環境文件指定了我們需要的依賴項。`<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` 是 Python 的最新主要版本。

完成後，您可以在命令行/終端中運行以下命令來創建您的 Conda 環境：

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

如果您遇到任何問題，請參考 [Conda 環境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

### 使用帶有 Python 支持擴展的 Visual Studio Code

我們建議使用 [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) 編輯器，並安裝 [Python 支持擴展](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 來完成這門課程。然而，這更多是一個建議而不是必然的要求。

> **注意**：通過在 VS Code 中打開課程倉庫，您可以選擇在容器中設置項目。這是因為課程倉庫中有 [特殊的 `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 目錄。稍後會介紹更多內容。

> **注意**：一旦您克隆並在 VS Code 中打開目錄，它會自動建議您安裝 Python 支持擴展。

> **注意**：如果 VS Code 建議您在容器中重新打開倉庫，請拒絕此請求以便使用本地安裝的 Python 版本。

### 在瀏覽器中使用 Jupyter

您也可以在瀏覽器中使用 [Jupyter 環境](https://jupyter.org?WT.mc_id=academic-105485-koreyst) 來完成項目。經典的 Jupyter 和 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) 都提供了非常愉快的開發環境，具有自動完成、代碼高亮等功能。

要在本地啟動 Jupyter，請打開終端/命令行，導航到課程目錄，並執行：

```bash
jupyter notebook
```

或

```bash
jupyterhub
```

這將啟動一個 Jupyter 實例，訪問的 URL 將顯示在命令行窗口中。

一旦您訪問該 URL，您應該能看到課程大綱並能導航到任何 `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` 文件，您可以在那裡查看代碼和輸出。

## 第一次使用 Azure OpenAI 服務

如果這是您第一次使用 Azure OpenAI 服務，請按照此指南了解如何 [創建和部署 Azure OpenAI 服務資源。](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## 第一次使用 OpenAI API

如果這是您第一次使用 OpenAI API，請按照指南了解如何 [創建和使用接口。](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## 與其他學習者會面

我們在官方的 [AI 社區 Discord 服務器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) 中創建了頻道，以便與其他學習者會面。這是一個與其他志同道合的企業家、創建者、學生以及任何希望在生成式 AI 中提升的人進行網絡交流的好方法。

[![加入 discord 頻道](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

項目團隊也會在這個 Discord 服務器上幫助任何學習者。

## 貢獻

這門課程是一個開源的倡議。如果您看到改進的地方或問題，請創建一個 [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) 或記錄一個 [GitHub 問題](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

項目團隊將跟踪所有貢獻。對開源的貢獻是構建您在生成式 AI 領域職業生涯的絕佳方式。

大多數貢獻需要您同意一份貢獻者許可協議 (CLA)，聲明您有權並實際授予我們使用您貢獻的權利。詳情請訪問 [CLA，貢獻者許可協議網站](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)。

重要提示：在翻譯此 repo 中的文本時，請確保您不使用機器翻譯。我們將通過社區驗證翻譯，因此請僅在您精通的語言中志願進行翻譯。

當您提交 pull request 時，CLA 機器人將自動確定您是否需要提供 CLA 並適當地裝飾 PR（例如，標籤、評論）。只需按照機器人提供的指示進行操作。您只需要在使用我們的 CLA 的所有倉庫中這樣做一次。

此項目已採用 [Microsoft 開源行為準則](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)。欲了解更多信息，請閱讀行為準則 FAQ 或聯繫 [Email opencode](opencode@microsoft.com) 提出任何其他問題或評論。

## 開始吧

現在您已經完成了完成這門課程所需的步驟，讓我們通過獲得 [生成式 AI 和 LLMs 的介紹](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) 來開始吧。

**免責聲明**：
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保準確性，請注意自動翻譯可能包含錯誤或不準確之處。應將原始語言的文件視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用此翻譯而產生的任何誤解或誤釋承擔責任。