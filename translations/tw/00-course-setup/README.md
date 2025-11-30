<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-17T23:42:48+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "tw"
}
-->
# 開始學習這門課程

我們非常期待您開始這門課程，並看看您能夠用生成式 AI 激發出什麼樣的創意！

為了確保您的成功，本頁面概述了設置步驟、技術需求，以及在需要時可以尋求幫助的地方。

## 設置步驟

要開始學習這門課程，您需要完成以下步驟。

### 1. Fork 此 Repo

[Fork 整個這個 repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) 到您的 GitHub 帳戶，以便能夠修改任何代碼並完成挑戰。您也可以[給此 repo 加星標 (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)，以便更容易找到它和相關的 repo。

### 2. 創建 Codespace

為了避免運行代碼時出現依賴問題，我們建議您在 [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) 中運行這門課程。

在您的 fork 中：**Code -> Codespaces -> New on main**

![顯示創建 Codespace 按鈕的對話框](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 添加密鑰

1. ⚙️ 齒輪圖標 -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret。
2. 命名為 OPENAI_API_KEY，粘貼您的密鑰，保存。

### 3. 接下來做什麼？

| 我想要…              | 前往…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| 開始第一課          | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| 離線工作            | [`setup-local.md`](02-setup-local.md)                                   |
| 設置 LLM 提供者     | [`providers.md`](03-providers.md)                                        |
| 與其他學員交流      | [加入我們的 Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 疑難排解

| 症狀                                   | 解決方法                                                         |
|---------------------------------------|-----------------------------------------------------------------|
| 容器構建超過 10 分鐘卡住              | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`           | 終端未連接；點擊 **+** ➜ *bash*                                 |
| OpenAI 返回 `401 Unauthorized`        | 錯誤或過期的 `OPENAI_API_KEY`                                   |
| VS Code 顯示 “Dev container mounting…”| 刷新瀏覽器標籤頁—Codespaces 有時會失去連接                     |
| Notebook 核心缺失                     | Notebook 菜單 ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix 系統：

   ```bash
   touch .env
   ```

   Windows：

   ```cmd
   echo . > .env
   ```

3. **編輯 `.env` 文件**：在文本編輯器（例如 VS Code、Notepad++ 或其他編輯器）中打開 `.env` 文件。添加以下行到文件中，將 `your_github_token_here` 替換為您的 GitHub token：

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **保存文件**：保存更改並關閉文本編輯器。

5. **安裝 `python-dotenv`**：如果您尚未安裝，您需要安裝 `python-dotenv` 套件，以便將 `.env` 文件中的環境變量加載到您的 Python 應用程序中。您可以使用 `pip` 安裝：

   ```bash
   pip install python-dotenv
   ```

6. **在 Python 腳本中加載環境變量**：在您的 Python 腳本中，使用 `python-dotenv` 套件從 `.env` 文件加載環境變量：

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

完成了！您已成功創建 `.env` 文件，添加了您的 GitHub token，並將其加載到您的 Python 應用程序中。

## 如何在本地運行

要在您的電腦上本地運行代碼，您需要安裝某個版本的 [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)。

然後使用倉庫，您需要克隆它：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

一旦您檢出所有內容，就可以開始了！

## 可選步驟

### 安裝 Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是一個輕量級的安裝程序，用於安裝 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python 以及一些套件。
Conda 本身是一個包管理器，可以輕鬆設置和切換不同的 Python [**虛擬環境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)和套件。它還非常適合安裝 `pip` 無法提供的套件。

您可以按照 [MiniConda 安裝指南](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) 進行設置。

安裝 Miniconda 後，您需要克隆 [倉庫](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)（如果您尚未克隆）。

接下來，您需要創建一個虛擬環境。使用 Conda 創建新環境文件 (_environment.yml_)。如果您使用 Codespaces，請在 `.devcontainer` 目錄中創建此文件，即 `.devcontainer/environment.yml`。

接下來，使用以下代碼片段填充您的環境文件：

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

如果您使用 Conda 時遇到錯誤，可以手動使用以下命令在終端中安裝 Microsoft AI Libraries。

```
conda install -c microsoft azure-ai-ml
```

環境文件指定了我們需要的依賴項。`<environment-name>` 是您希望使用的 Conda 環境名稱，`<python-version>` 是您希望使用的 Python 版本，例如，`3` 是最新的 Python 主版本。

完成後，您可以通過在命令行/終端中運行以下命令來創建您的 Conda 環境：

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

如果遇到任何問題，請參考 [Conda 環境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

### 使用 Visual Studio Code 和 Python 支援擴展

我們建議使用 [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) 編輯器，並安裝 [Python 支援擴展](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 來學習這門課程。不過，這只是建議，並非必須。

> **注意**：通過在 VS Code 中打開課程倉庫，您可以選擇在容器中設置項目。這是因為課程倉庫中有 [特殊的 `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 目錄。稍後會詳細介紹。

> **注意**：一旦您克隆並在 VS Code 中打開目錄，它會自動建議您安裝 Python 支援擴展。

> **注意**：如果 VS Code 建議您在容器中重新打開倉庫，請拒絕此請求以使用本地安裝的 Python 版本。

### 在瀏覽器中使用 Jupyter

您也可以使用 [Jupyter 環境](https://jupyter.org?WT.mc_id=academic-105485-koreyst) 在瀏覽器中進行項目開發。無論是經典 Jupyter 還是 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst)，都提供了非常愉快的開發環境，具有自動補全、代碼高亮等功能。

要在本地啟動 Jupyter，請打開終端/命令行，導航到課程目錄，並執行：

```bash
jupyter notebook
```

或

```bash
jupyterhub
```

這將啟動一個 Jupyter 實例，並在命令行窗口中顯示訪問的 URL。

訪問該 URL 後，您應該能看到課程大綱，並能導航到任何 `*.ipynb` 文件。例如，`08-building-search-applications/python/oai-solution.ipynb`。

### 在容器中運行

除了在您的電腦或 Codespace 上設置一切，您還可以使用 [容器](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)。課程倉庫中的特殊 `.devcontainer` 文件夾使得 VS Code 能夠在容器中設置項目。在 Codespaces 之外，這需要安裝 Docker，並且相當麻煩，因此我們建議僅對有容器使用經驗的人使用此方法。

在使用 GitHub Codespaces 時，保護您的 API 密鑰的最佳方法之一是使用 Codespace Secrets。請按照 [Codespaces 密鑰管理指南](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) 了解更多信息。

## 課程和技術需求

這門課程包含 6 個概念課程和 6 個編程課程。

在編程課程中，我們使用 Azure OpenAI Service。您需要訪問 Azure OpenAI Service 並獲得 API 密鑰才能運行此代碼。您可以通過[完成此申請](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)來申請訪問。

在等待您的申請處理期間，每個編程課程也包含一個 `README.md` 文件，您可以在其中查看代碼和輸出。

## 第一次使用 Azure OpenAI Service

如果這是您第一次使用 Azure OpenAI Service，請按照此指南了解如何[創建和部署 Azure OpenAI Service 資源。](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## 第一次使用 OpenAI API

如果這是您第一次使用 OpenAI API，請按照指南了解如何[創建和使用介面。](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## 與其他學員交流

我們在官方 [AI 社群 Discord 伺服器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) 中創建了頻道，供學員之間交流。這是一個與其他志同道合的創業者、開發者、學生以及任何希望在生成式 AI 領域提升的人建立聯繫的好方法。

[![加入 Discord 頻道](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

項目團隊也會在這個 Discord 伺服器上幫助學員。

## 貢獻

這門課程是一個開源項目。如果您看到需要改進的地方或問題，請創建 [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) 或記錄 [GitHub 問題](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

項目團隊將跟蹤所有貢獻。為開源項目做貢獻是一個在生成式 AI 領域建立職業生涯的絕佳方式。

大多數貢獻需要您同意一份貢獻者許可協議 (CLA)，聲明您有權並確實授予我們使用您的貢獻的權利。詳情請訪問 [CLA, 貢獻者許可協議網站](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)。

重要提示：在翻譯此 repo 中的文本時，請確保您不使用機器翻譯。我們將通過社群驗證翻譯，因此請僅在您精通某種語言時志願進行翻譯。

當您提交 Pull Request 時，CLA-bot 會自動確定您是否需要提供 CLA，並適當地標記 PR（例如，標籤、評論）。只需按照 bot 提供的指示操作即可。您只需在所有使用我們 CLA 的倉庫中執行一次。

此項目已採用 [Microsoft 開源行為準則](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)。欲了解更多信息，請閱讀行為準則 FAQ 或聯繫 [Email opencode](opencode@microsoft.com) 提出任何其他問題或意見。

## 開始吧！
現在您已完成完成此課程所需的步驟，讓我們開始了解[生成式人工智慧和大型語言模型的介紹](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)。

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。