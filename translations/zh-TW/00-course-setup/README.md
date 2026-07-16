# 開始本課程

我們很高興您開始這門課程，並期待看到您利用生成式 AI 所激發的創作靈感！

為確保您的成功，這頁面將說明設定步驟、技術需求，並告知您需要幫助時該去哪裡。

## 設定步驟

想開始學習本課程，您需要完成以下步驟。

### 1. 分岔這個資料庫

[將整個資料庫分岔到您的 GitHub 帳戶](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)，以便您可以更改任何程式碼並完成挑戰。您也可以為本資料庫 [加星標 (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)，方便日後尋找此資料庫及相關資料庫。

### 2. 建立 codespace

為避免執行程式碼時有依賴性問題，我們建議您在 [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) 中運行本課程。

在您的分岔庫中：**Code -> Codespaces -> New on main**

![對話框顯示建立 codespace 的按鈕](../../../translated_images/zh-TW/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 新增密鑰

1. ⚙️ 齒輪圖標 -> 命令面板 -> Codespaces : Manage user secret -> Add a new secret。
2. 名稱輸入 OPENAI_API_KEY，貼上您的密鑰，然後儲存。

### 3. 接下來怎麼做？

| 我想要…           | 前往…                                                                   |
|--------------------|------------------------------------------------------------------------|
| 開始第一課        | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| 離線作業          | [`setup-local.md`](02-setup-local.md)                                   |
| 設定一個 LLM 供應商 | [`providers.md`](03-providers.md)                                        |
| 認識其他學習者    | [加入我們的 Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 疑難排解


| 症狀                                    | 解決方案                                                        |
|----------------------------------------|----------------------------------------------------------------|
| 容器建置卡住超過 10 分鐘                   | **Codespaces ➜ “Rebuild Container”**                           |
| `python: command not found`              | 終端機未連接；點擊 **+** ➜ *bash*                               |
| OpenAI 回傳 `401 Unauthorized`          | `OPENAI_API_KEY` 誤植或已過期                                  |
| VS Code 顯示 “Dev container mounting…”  | 重新整理瀏覽器標籤頁——Codespaces 有時會失去連線                 |
| 筆記本內核缺失                          | 筆記本選單 ➜ **Kernel ▸ Select Kernel ▸ Python 3**              |

   Unix 系統：

   ```bash
   touch .env
   ```

   Windows：

   ```cmd
   echo . > .env
   ```

3. **編輯 `.env` 文件**：使用文字編輯器（例如 VS Code、Notepad++ 或其他編輯器）打開 `.env` 文件。新增以下內容，將佔位符替換為您實際的 Microsoft Foundry Models 端點與金鑰（詳見 [`providers.md`](03-providers.md) 如何取得）：

   > **注意：**GitHub Models（及其 `GITHUB_TOKEN` 變數）將於 2026 年 7 月底退役。請改用 [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)。

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. <strong>儲存檔案</strong>：儲存修改後關閉編輯器。

5. **安裝 `python-dotenv`**：若還沒安裝，您需要裝 `python-dotenv` 套件，讓 Python 應用可從 `.env` 文件讀取環境變數。可透過 `pip` 安裝：

   ```bash
   pip install python-dotenv
   ```

6. **在 Python 腳本中載入環境變數**：在 Python 程式中，使用 `python-dotenv` 讀取 `.env` 文件的環境變數：

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

就這樣！您已成功建立 `.env` 文件，新增 Microsoft Foundry Models 認證，並將它們載入 Python 應用程式。

## 如何在本地電腦運行

要在本地電腦上運行程式碼，需要先安裝某個版本的 [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)。

接著，您需要將此資料庫複製到本地：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

複製完畢後，您就可以開始了！

## 可選步驟

### 安裝 Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是一個輕量級的安裝器，用於安裝 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python，以及少數套件。
Conda 本身是套件管理器，使得設置及切換不同 Python [<strong>虛擬環境</strong>](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) 和套件變得簡單，也方便安裝無法透過 `pip` 取得的套件。

您可以參考 [MiniConda 安裝指南](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) 來設定。

安裝 Miniconda 後，若還沒複製 [本資料庫](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)，請完成此步驟。

接著，需要建立一個虛擬環境。使用 Conda 的話，您可以創建一個新環境設定檔（_environment.yml_）。若您採用 Codespaces，請將此檔建立於 `.devcontainer` 目錄，即 `.devcontainer/environment.yml`。

請將以下內容填入您的環境檔案：

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

如若您使用 conda 時遇到錯誤，您可以在終端機中手動安裝 Microsoft AI 函式庫，使用以下命令：

```
conda install -c microsoft azure-ai-ml
```

此環境檔指定我們需要的相依性。`<environment-name>` 是您欲命名的 Conda 環境名稱，`<python-version>` 是您想用的 Python 版本，例如 `3` 表示最新主版本。

完成後，您可以在命令行/終端機運行以下指令來建立 Conda 環境：

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer 子路徑僅適用於 Codespace 設置
conda activate ai4beg
```

若有任何問題，請參考 [Conda 環境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

### 使用 Visual Studio Code 的 Python 支援擴充

我們推薦使用 [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) 編輯器，並安裝 [Python 支援擴充](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 來進行本課程。不過這只是建議，非絕對必要。

> <strong>注意</strong>：在 VS Code 中開啟課程資料庫時，您可以選擇在容器中設置專案。因為本課程資料庫含有一個特殊的 [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 目錄，稍後將介紹更多相關內容。

> <strong>注意</strong>：一旦您複製並在 VS Code 開啟目錄，它會自動建議安裝 Python 支援擴充。

> <strong>注意</strong>：如 VS Code 建議您在容器中重開資料庫，請拒絕此請求，以便使用本機安裝的 Python 版本。

### 在瀏覽器中使用 Jupyter

您也可以使用瀏覽器內的 [Jupyter 環境](https://jupyter.org?WT.mc_id=academic-105485-koreyst) 來進行專案作業。經典 Jupyter 以及 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) 都提供相當舒適的開發環境，如自動補全、程式碼高亮等功能。

若要在本地啟動 Jupyter，請開啟終端機或命令行，切換到課程目錄，並執行：

```bash
jupyter notebook
```

或者

```bash
jupyterhub
```

這將啟動一個 Jupyter 實例，並在命令行視窗中顯示其訪問 URL。

進入該 URL 後，您會看到課程大綱，並能瀏覽任何 `*.ipynb` 檔案。例如，`08-building-search-applications/python/oai-solution.ipynb`。

### 容器中執行

除了在您的電腦或 Codespace 安裝設定外，您也可使用 [容器](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)。課程資料庫的特殊 `.devcontainer` 資料夾使 VS Code 可在容器中設置專案。非 Codespaces 環境下，需安裝 Docker，並且作業比較繁複，因此我們只建議有容器使用經驗的使用者嘗試。

在使用 GitHub Codespaces 時，確保 API 金鑰安全的最佳方式是利用 Codespace Secrets。請參考 [Codespaces 秘密管理](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) 指南了解更多。


## 課程內容與技術需求

本課程包含 6 節概念課程及 6 節程式實作課程。

實作課將使用 Azure OpenAI 服務。您需要取得 Azure OpenAI 服務的存取權與 API 金鑰才能執行程式碼。您可以透過 [完整此申請](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) 獲得存取權。

申請期間，每節程式實作課也附有 `README.md` 檔案，供您查看程式碼和輸出內容。

## 首次使用 Azure OpenAI 服務

若您是首次使用 Azure OpenAI 服務，請參考本指南演練如何[建立與部署 Azure OpenAI 服務資源。](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## 首次使用 OpenAI API

若您是首次使用 OpenAI API，請參閱該指南了解如何[建立與使用介面。](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## 認識其他學員

我們在官方 [AI 社群 Discord 伺服器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) 中建立了頻道，促進學員交流。這是與志同道合的創業者、開發者、學生及想提升生成式 AI 技能者建立人脈的絕佳途徑。

[![加入 Discord 頻道](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

專案團隊也會在此 Discord 伺服器上為學員提供協助。

## 參與貢獻

本課程為開源專案。如果您發現可改進或有問題，請提交 [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) 或登記 [GitHub 問題單](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

專案團隊會追蹤所有貢獻。參與開源是建立生成式 AI 職涯的絕佳方式。

大多數貢獻需您同意一份貢獻者授權協議 (CLA)，聲明您有權利且願意授權我們使用您的貢獻。詳細資訊請參閱 [CLA，貢獻者授權協議官網](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)。

注意：在本資料庫翻譯文字時，請勿使用機器翻譯。我們將由社群驗證翻譯品質，請僅在您熟悉的語言中提供翻譯協助。

當您提交 PR 時，CLA-bot 會自動判斷是否需要您提供 CLA，並於 PR 中加註標籤或留言。請依照機器人指示操作。您只需在所有使用本 CLA 的程式庫中完成一次。


本專案已採用 [Microsoft 開源行為準則](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)。欲了解更多資訊，請參閱行為準則常見問題，或透過 [Email opencode](opencode@microsoft.com) 聯絡我們，提出任何其他問題或意見。

## 開始吧

現在您已完成完成此課程所需的步驟，讓我們從 [生成式 AI 及大型語言模型介紹](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) 開始吧。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->