<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-05-19T12:19:59+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "hk"
}
-->
# 開始學習這門課程

我們非常期待你開始這門課程，看看你能夠受到生成式 AI 的啟發，創造出什麼作品！

為了確保你的成功，這頁面概述了設置步驟、技術要求，以及需要時可以獲得幫助的地方。

## 設置步驟

要開始學習這門課程，你需要完成以下步驟。

### 1. Fork 此 Repo

[Fork 整個 repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)到你的 GitHub 帳戶，以便能夠修改任何代碼並完成挑戰。你也可以[星標 (🌟) 此 repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)，以便更容易找到它和相關的 repo。

### 2. 創建 codespace

為了避免運行代碼時出現任何依賴問題，我們建議在 [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) 中運行這門課程。

這可以通過在你 fork 的版本中選擇 `Code` 選項並選擇 **Codespaces** 選項來創建。

![創建 codespace 的按鈕對話框](../../../00-course-setup/images/who-will-pay.webp)

### 3. 存儲你的 API 密鑰

在構建任何類型的應用程序時，保持你的 API 密鑰的安全和保密是很重要的。我們建議不要直接將任何 API 密鑰存儲在你的代碼中。將這些詳細信息提交到公共存儲庫可能會導致安全問題，甚至可能被不良行為者使用而產生不必要的費用。
這裡是一個逐步指南，教你如何為 Python 創建 `.env` 文件並添加 `GITHUB_TOKEN`：

1. **導航到你的項目目錄**：打開你的終端或命令提示符，導航到你想創建 `.env` 文件的項目根目錄。

   ```bash
   cd path/to/your/project
   ```

2. **創建 `.env` 文件**：使用你喜愛的文本編輯器創建一個名為 `.env` 的新文件。如果你使用命令行，你可以使用 `touch` (on Unix-based systems) or `echo`（在 Windows 上）：

   Unix 系統：
   ```bash
   touch .env
   ```

   Windows：
   ```cmd
   echo . > .env
   ```

3. **編輯 `.env` 文件**：在文本編輯器（例如 VS Code、Notepad++ 或其他編輯器）中打開 `.env` 文件。將以下行添加到文件中，將 `your_github_token_here` 替換為你的實際 GitHub 令牌：

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **保存文件**：保存更改並關閉文本編輯器。

5. **安裝 `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` 包以從 `.env` 文件中加載環境變量到你的 Python 應用程序。你可以使用 `pip` 安裝：

   ```bash
   pip install python-dotenv
   ```

6. **在你的 Python 腳本中加載環境變量**：在你的 Python 腳本中，使用 `python-dotenv` 包從 `.env` 文件中加載環境變量：

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

就是這樣！你已成功創建 `.env` 文件，添加了你的 GitHub 令牌，並將其加載到你的 Python 應用程序中。

## 如何在本地運行

要在你的計算機上本地運行代碼，你需要安裝某個版本的 [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)。

然後使用存儲庫，你需要克隆它：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

一旦你檢出所有內容，就可以開始了！

## 可選步驟

### 安裝 Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是一個輕量級安裝程序，用於安裝 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python 以及一些包。
Conda 本身是一個包管理器，可以輕鬆設置和切換不同的 Python [**虛擬環境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)和包。它在安裝 `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml` 不提供的包時也很方便。

繼續用下面的代碼片段填充你的環境文件：

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

如果你在使用 conda 時遇到錯誤，你可以使用以下命令在終端中手動安裝 Microsoft AI 庫。

```
conda install -c microsoft azure-ai-ml
```

環境文件指定了我們需要的依賴項。`<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` 是 Python 的最新主要版本。

完成後，你可以通過在命令行/終端中運行以下命令來創建你的 Conda 環境

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

如果你遇到任何問題，請參考 [Conda 環境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

### 使用 Visual Studio Code 和 Python 支持擴展

我們建議使用 [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) 編輯器，並安裝 [Python 支持擴展](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 來學習這門課程。這只是建議，並不是絕對要求。

> **注意**：通過在 VS Code 中打開課程存儲庫，你可以選擇在容器中設置項目。這是因為課程存儲庫中存在 [特殊的 `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 目錄。稍後會有更多介紹。

> **注意**：一旦你克隆並在 VS Code 中打開目錄，它會自動建議你安裝 Python 支持擴展。

> **注意**：如果 VS Code 建議你在容器中重新打開存儲庫，請拒絕此請求以便使用本地安裝的 Python 版本。

### 在瀏覽器中使用 Jupyter

你也可以直接在瀏覽器中使用 [Jupyter 環境](https://jupyter.org?WT.mc_id=academic-105485-koreyst) 來進行項目開發。經典 Jupyter 和 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) 都提供了相當愉快的開發環境，具有自動補全、代碼高亮等功能。

要在本地啟動 Jupyter，請打開終端/命令行，導航到課程目錄，並執行：

```bash
jupyter notebook
```

或

```bash
jupyterhub
```

這將啟動一個 Jupyter 實例，並在命令行窗口中顯示訪問的 URL。

一旦你訪問了 URL，你應該能看到課程大綱，並能夠導航到任何 `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` 文件，在那裡你可以查看代碼和輸出。

## 第一次使用 Azure OpenAI 服務

如果這是你第一次使用 Azure OpenAI 服務，請按照這個指南來 [創建和部署 Azure OpenAI 服務資源。](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## 第一次使用 OpenAI API

如果這是你第一次使用 OpenAI API，請按照指南來 [創建和使用接口。](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## 與其他學員交流

我們已在官方 [AI 社區 Discord 服務器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) 中創建了頻道，供學員相互交流。這是一個與其他志同道合的創業者、開發者、學生，以及任何想在生成式 AI 領域提升自己的人建立網絡的好方法。

[![加入 discord 頻道](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

項目團隊也會在這個 Discord 服務器上幫助學員。

## 貢獻

這門課程是一個開源項目。如果你看到需要改進的地方或問題，請創建 [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) 或記錄 [GitHub 問題](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

項目團隊將跟踪所有貢獻。為開源做貢獻是建立你在生成式 AI 領域職業生涯的一個驚人方式。

大多數貢獻需要你同意一份貢獻者許可協議 (CLA)，聲明你有權並實際授予我們使用你貢獻的權利。詳情請訪問 [CLA，貢獻者許可協議網站](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)。

重要提示：在翻譯此 repo 中的文本時，請確保不使用機器翻譯。我們將通過社區驗證翻譯，因此請僅在你精通的語言中志願翻譯。

當你提交 pull request 時，CLA 機器人將自動確定你是否需要提供 CLA 並適當地裝飾 PR（例如，標籤、評論）。只需按照機器人提供的指示進行操作即可。你只需要在使用我們的 CLA 的所有存儲庫中執行一次。

此項目已採用 [Microsoft 開源行為準則](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)。如需更多信息，請閱讀行為準則常見問題或通過 [Email opencode](opencode@microsoft.com) 聯繫我們以獲取任何其他問題或意見。

## 開始吧

現在你已完成這門課程所需的步驟，讓我們開始 [生成式 AI 和 LLMs 的介紹](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)。

**免責聲明**：
本文檔是使用AI翻譯服務[Co-op Translator](https://github.com/Azure/co-op-translator)進行翻譯的。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議尋求專業人工翻譯。我們對於使用此翻譯所引起的任何誤解或誤釋不承擔責任。