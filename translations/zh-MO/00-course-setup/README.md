# 開始修讀本課程

我們非常興奮您開始這個課程，看您如何受到啟發使用生成式人工智能創造！

為確保您的成功，這頁概述了設置步驟、技術需求及如有需要時可獲得協助的位置。

## 設置步驟

開始修讀本課程前，您需要完成以下步驟。

### 1. 分叉此存儲庫

[分叉整個存儲庫](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) 到您的 GitHub 帳戶，以便您能更改任何程式碼及完成挑戰。您也可以 [為此存儲庫加星號 (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)，方便您尋找它及相關的存儲庫。

### 2. 創建一個 codespace

為避免運行代碼時出現依賴問題，我們建議您使用 [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) 運行本課程。

在您的分叉版本中：**代碼 -> Codespaces -> 主分支上新建**

![顯示創建 codespace 按鈕的對話框](../../../translated_images/zh-MO/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 新增一個秘密

1. ⚙️ 齒輪圖示 -> 命令面板-> Codespaces：管理用戶秘密 -> 新增秘密。
2. 命名為 OPENAI_API_KEY，貼上您的金鑰，保存。

### 3. 接下來怎麼做？

| 我想要…                | 前往…                                                                |
|-------------------------|----------------------------------------------------------------------|
| 開始第一課               | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)  |
| 離線工作                | [`setup-local.md`](02-setup-local.md)                                |
| 設置大型語言模型提供者    | [`providers.md`](03-providers.md)                                     |
| 認識其他學員            | [加入我們的 Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 疑難排解


| 症狀                                   | 解決方法                                                      |
|---------------------------------------|------------------------------------------------------------|
| 容器構建卡住超過 10 分鐘                 | **Codespaces ➜ “重新構建容器”**                           |
| 顯示 `python: command not found`       | 終端機未附加；點擊 **+** ➜ *bash*                        |
| 由 OpenAI 回傳 `401 Unauthorized`     | `OPENAI_API_KEY` 錯誤或已過期                              |
| VS Code 顯示 “開發容器裝載中…”            | 重新整理瀏覽器分頁 — Codespaces 有時會斷線                |
| 筆記本內核缺失                        | 筆記本菜單 ➜ **核心 ▸ 選擇核心 ▸ Python 3**               |

   基於 Unix 的系統：

   ```bash
   touch .env
   ```

   Windows 系統：

   ```cmd
   echo . > .env
   ```

3. **編輯 `.env` 文件**：用文字編輯器 (例如 VS Code、Notepad++ 或其他編輯器) 打開 `.env` 文件。加入以下幾行，將佔位符替換成您實際的 Microsoft Foundry Models 端點和金鑰（請參閱 [`providers.md`](03-providers.md) 瞭解如何取得）：

   > **注意：** GitHub 模型（及其 `GITHUB_TOKEN` 變數）將於 2026 年 7 月底退休。請改用 [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)。

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. <strong>保存文件</strong>：保存更改並關閉文字編輯器。

5. **安裝 `python-dotenv`**：如果尚未安裝，您需要安裝 `python-dotenv` 套件以從 `.env` 文件載入環境變數到您的 Python 應用。可用 `pip` 來安裝：

   ```bash
   pip install python-dotenv
   ```

6. **在您的 Python 腳本中載入環境變數**：用 `python-dotenv` 套件從 `.env` 文件載入環境變數：

   ```python
   from dotenv import load_dotenv
   import os

   # 從 .env 文件載入環境變數
   load_dotenv()

   # 存取 Microsoft Foundry Models 變數
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

就這樣！您已成功建立 `.env` 文件，加入Microsoft Foundry Models 憑證，並載入到您的 Python 應用中。

## 如何在您的電腦本地運行

若要在本地運行代碼，您需要安裝某版本的 [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)。

接著，您需要複製此存儲庫：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

一旦您已克隆完成，就可以開始使用！

## 可選步驟

### 安裝 Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是一個輕量級安裝器，可以用來安裝 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python，以及部分套件。
Conda 本身是一套套件管理器，非常方便建立和切換不同 Python [<strong>虛擬環境</strong>](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) 及套件。Condais 還很有用於安裝 `pip` 無法取得的套件。

您可以依循 [Miniconda 安裝指南](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) 來完成安裝。

安裝 Miniconda 後，若您尚未克隆 [存儲庫](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)，請先克隆。

接著，您需建立虛擬環境。對 Conda 而言，建議建立新環境文件(_environment.yml_)。若您使用 Codespaces，請於 `.devcontainer` 目錄下建立此文件，即 `.devcontainer/environment.yml`。

請在環境文件中填入下方內容：

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

若使用 conda 遇到錯誤，可以在終端機手動執行以下命令安裝 Microsoft AI 函式庫。

```
conda install -c microsoft azure-ai-ml
```

環境文件指定了所需依賴。`<environment-name>` 請填入您欲使用的 Conda 環境名稱，`<python-version>` 是您想用的 Python 版本，例如，`3` 是最新主版本。

完成後，請於命令行／終端執行以下命令來建立您的 Conda 環境：

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer 子路徑只適用於 Codespace 設定
conda activate ai4beg
```

如遇問題，請參考 [Conda 環境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

### 使用帶 Python 支援擴充功能的 Visual Studio Code

我們建議本課程使用 [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) 編輯器，並安裝 [Python 支援擴充功能](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)。不過這是推薦選項，非硬性要求。

> <strong>注意</strong>：打開課程存儲庫於 VS Code 可選擇將專案設在容器中，因為存儲庫裡包含特殊的 [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 文件夾。稍後會詳細說明。

> <strong>注意</strong>：您克隆並開啟目錄於 VS Code 時，會自動建議安裝 Python 支援擴充功能。

> <strong>注意</strong>：如果 VS Code 建議您在容器中重新打開存儲庫，請拒絕此要求以使用本機安裝的 Python 版本。

### 在瀏覽器中使用 Jupyter

您也可以在瀏覽器中使用 [Jupyter 環境](https://jupyter.org?WT.mc_id=academic-105485-koreyst) 進行專案開發。經典版 Jupyter 和 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) 都具自動補完、程式碼高亮等便利功能，提供良好的開發體驗。

在本地啟動 Jupyter，請開啟終端機／命令行，切換至課程目錄，執行：

```bash
jupyter notebook
```

或

```bash
jupyterhub
```

執行後，Jupyter 實例會啟動，並於命令行視窗顯示訪問 URL。

打開 URL 後，您會看到課程目錄，可導航至任一 `.ipynb` 檔案，如 `08-building-search-applications/python/oai-solution.ipynb`。

### 在容器中運行

除了在電腦或 Codespace 設定外，您也可用 [容器](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)。課程存儲庫中有特殊 `.devcontainer` 文件夾，使 VS Code 能在容器中設置專案。在 Codespaces 以外，這需要安裝 Docker，而且頗為複雜，我們建議僅經驗豐富的用家使用。

使用 GitHub Codespaces 保持 API 金鑰安全的最佳方式之一是利用 Codespace Secrets。請參考 [Codespaces 秘密管理](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) 指南了解詳情。


## 課程及技術需求

本課程包括「學習」課程解釋生成式人工智能概念，及「構建」課程展示以 **Python** 和 **TypeScript** 實作的實戰程式碼（視情況而定）。

程式編碼課程使用 Microsoft Foundry 上的 Azure OpenAI。您需要 Azure 訂閱和 API 金鑰。存取開放無申請限制，您可 [創建 Microsoft Foundry 資源並部署模型](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) 以取得端點及金鑰。

每堂程式課程亦包含 `README.md` 文件，讓您可查看程式碼與輸出，無需執行任何程式。

## 首次使用 Azure OpenAI 服務

如您首次使用 Azure OpenAI 服務，請參考此指南：[如何創建與部署 Azure OpenAI 服務資源](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## 首次使用 OpenAI API

如您首次使用 OpenAI API，請依循此說明使用介面：[快速入門指南](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## 認識其他學員

我們於官方 [AI Community Discord 伺服器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) 建立了頻道，供學員交流。這是與志同道合的創業者、開發者、學生及任何希望在生成式 AI 領域提升的人士建立人脈的好方式。

[![加入 Discord 頻道](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

專案團隊也會在此 Discord 伺服器上協助學員。

## 貢獻

本課程為開源項目。若您發現改進空間或問題，請提出 [拉取請求](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) 或回報 [GitHub 問題](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

專案團隊會追蹤所有貢獻。參與開源是拓展生成式 AI 事業的絕佳途徑。

大部分貢獻需簽署貢獻者許可協議 (CLA)，聲明您擁有並確實授權我們使用您的貢獻。詳情請參閱 [CLA，貢獻者許可協議網站](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)。

重要提醒：本存儲庫翻譯請勿使用機器翻譯。我們將透過社群確認譯文，請只參與您熟練語言的翻譯工作。


當您提交拉取請求時，CLA-bot 會自動判定您是否需要提供 CLA 並適當標記該拉取請求（例如，標籤、評論）。只需按照機器人提供的指示操作。所有使用我們 CLA 的存儲庫中您只需執行一次此操作。

此專案已採用 [Microsoft 開源行為守則](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)。欲了解更多資訊，請閱讀行為守則常見問題或透過 [Email opencode](opencode@microsoft.com) 聯絡我們，有任何其他問題或意見也歡迎提出。

## 開始吧

現在您已完成完成此課程所需的步驟，讓我們先從獲得 [生成式 AI 與大型語言模型 (LLMs) 介紹](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) 開始吧。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->