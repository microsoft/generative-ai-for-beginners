# 開始本課程

我們非常高興你開始這門課程，並期待看到你用生成式 AI 創作出什麼靈感作品！

為確保你的學習成功，本頁概述設定步驟、技術需求以及需要幫助時的資源。

## 設定步驟

要開始上課，你需要完成以下步驟。

### 1. 分叉此程式庫

[將整個程式庫分叉](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)到你自己的 GitHub 帳號，以便修改任何代碼並完成挑戰。你也可以[為此程式庫加星標 (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)，以便更容易找到它和相關程式庫。

### 2. 建立 codespace

為避免執行代碼時的相依性問題，我們建議在 [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) 執行本課程。

在你的分叉版本中：**Code -> Codespaces -> New on main**

![顯示建立 codespace 按鈕的對話框](../../../translated_images/zh-MO/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 新增密鑰

1. ⚙️ 齒輪圖示 -> 命令面板 -> Codespaces : 管理使用者密鑰 -> 新增密鑰。
2. 名稱為 OPENAI_API_KEY，貼上你的金鑰，儲存。

### 3. 下一步？

| 我想要…          | 前往…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| 開始第 1 課      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| 離線工作        | [`setup-local.md`](02-setup-local.md)                                   |
| 設定大型語言模型供應商 | [`providers.md`](03-providers.md)                                        |
| 認識其他學員     | [加入我們的 Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 疑難排解


| 症狀                                    | 解決方法                                                           |
|-----------------------------------------|-------------------------------------------------------------------|
| 容器建置卡住超過 10 分鐘                  | **Codespaces ➜ 「重建容器」**                                      |
| `python: command not found`               | 終端機沒啟動，點選 **+** ➜ *bash*                                 |
| 從 OpenAI 收到 `401 Unauthorized`      | `OPENAI_API_KEY` 錯誤或過期                                       |
| VS Code 顯示「Dev container 掛載中…」     | 重新整理瀏覽器分頁－Codespaces 有時候會失去連線                   |
| 筆記型本核心遺失                         | 筆記型本選單 ➜ **Kernel ▸ 選擇核心 ▸ Python 3**                   |

   Unix 類系統：

   ```bash
   touch .env
   ```

   Windows：

   ```cmd
   echo . > .env
   ```

3. **編輯 `.env` 檔案**：使用文字編輯器（例如 VS Code、Notepad++ 或任何其他編輯器）開啟 `.env` 檔案。加入以下內容，將佔位符替換為你實際的 Microsoft Foundry Models 端點和密鑰（參見 [`providers.md`](03-providers.md) 了解取得方式）：

   > **注意：** GitHub Models（及其 `GITHUB_TOKEN` 變數）將於 2026 年 7 月底退役。請改用 [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)。

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. <strong>儲存檔案</strong>：儲存變更並關閉文字編輯器。

5. **安裝 `python-dotenv`**：如果尚未安裝，需要透過 `pip` 安裝此套件，以便從 `.env` 檔案載入環境變數到你的 Python 應用程式：

   ```bash
   pip install python-dotenv
   ```

6. **在 Python 腳本中載入環境變數**：在你的 Python 腳本中使用 `python-dotenv` 套件載入 `.env` 檔案中環境變數：

   ```python
   from dotenv import load_dotenv
   import os

   # 從 .env 文件加載環境變量
   load_dotenv()

   # 訪問 Microsoft Foundry 模型變量
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

就是這樣！你已成功建立 `.env` 檔案，加入 Microsoft Foundry Models 認證，並將它們載入 Python 應用程式中。

## 如何在本機電腦執行

若要在本機電腦執行程式碼，你需要先安裝某個版本的 [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)。

接著，使用 git 將此儲存庫克隆：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

克隆完成後，即可開始上課！

## 選擇性步驟

### 安裝 Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是輕量級的 Conda、Python 及部分套件安裝器。
Conda 本身是套件管理工具，方便設定和切換不同的 Python [<strong>虛擬環境</strong>](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)及套件，也方便安裝無法用 `pip` 取得的套件。

你可以依照 [MiniConda 安裝指南](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) 安裝。

安裝 Miniconda 後，若尚未克隆 [程式庫](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)，請先克隆它。

接著建立虛擬環境。使用 Conda，可以建立一個環境描述檔案（_environment.yml_）。若你使用 Codespaces，請於 `.devcontainer` 目錄下建立，即 `.devcontainer/environment.yml`。

在環境檔案中填入以下片段：

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

若使用 conda 遇到錯誤，你也可在終端機手動安裝 Microsoft AI 函式庫：

```
conda install -c microsoft azure-ai-ml
```

環境檔案列出我們需要的相依套件。`<environment-name>` 是你想命名的 Conda 環境名稱，`<python-version>` 是你想用的 Python 版本，例如 `3` 是最新主要版。

完成後，可在命令提示字元/終端機執行以下命令，建立 Conda 環境：

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer 子路徑只適用於 Codespace 設定
conda activate ai4beg
```

如遇困難，可參考 [Conda 環境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

### 使用帶 Python 支援擴充的 Visual Studio Code

我們建議使用 [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) 編輯器並安裝 [Python 支援擴充](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 來學習本課程，不過這只是建議，非硬性要求。

> <strong>注意</strong>：在 VS Code 開啟課程程式庫時，可選擇在容器中設定專案，這是因為程式庫內有 [特別的 `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 目錄。稍後會有更多說明。

> <strong>注意</strong>：一旦你克隆並在 VS Code 打開該資料夾，系統會自動建議安裝 Python 支援擴充。

> <strong>注意</strong>：若 VS Code 建議你在容器中重新開啟程式庫，請拒絕此請求，以使用本機安裝的 Python 版本。

### 在瀏覽器中使用 Jupyter

你也可以在瀏覽器中直接使用 [Jupyter 環境](https://jupyter.org?WT.mc_id=academic-105485-koreyst) 開發。經典版 Jupyter 與 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) 都提供舒適的開發環境，有自動完成、程式碼高亮等功能。

若要在本機啟動 Jupyter，請到終端機/命令列，切換到課程目錄，並執行：

```bash
jupyter notebook
```

或

```bash
jupyterhub
```

執行後會啟動 Jupyter 實例，命令行視窗會顯示存取 URL。

瀏覽至該 URL 後，你會看到課程大綱並能瀏覽所有 `*.ipynb` 檔，如 `08-building-search-applications/python/oai-solution.ipynb`。

### 容器中執行

另一種不用在本機或 Codespace 建置環境的方式，是使用 [容器](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)。課程程式庫中特別的 `.devcontainer` 資料夾讓 VS Code 能在容器中建置專案。若非透過 Codespaces，要先安裝 Docker，老實說也需要一些操作經驗，因此建議有容器操作背景的人嘗試。

使用 GitHub Codespaces 時，保持 API 金鑰安全的最佳方法之一是使用 Codespace 秘密。請參考 [Codespaces 秘密管理指南](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) 瞭解詳情。


## 課程內容與技術需求

本課程包含 6 個概念課程與 6 個編程課程。

編程課程使用 Azure OpenAI 服務。你需取得 Azure OpenAI 服務的使用權及 API 金鑰，方可執行相關代碼。可透過 [填寫此申請表](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) 申請。

等待申請審核期間，每個編程課程附帶的 `README.md` 檔案內，均提供程式碼與輸出結果可供查看。

## 初次使用 Azure OpenAI 服務

若你是首次使用 Azure OpenAI 服務，請依照此指南了解如何[建立及部署 Azure OpenAI 服務資源。](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## 初次使用 OpenAI API

若你是首次使用 OpenAI API，請依此指南了解如何[建立與使用介面。](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## 認識其他學員

我們在官方 [AI 社群 Discord 伺服器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) 中建立了頻道供學員認識彼此。這是與志同道合的創業家、開發者、學生及任何希望在生成式 AI 領域進步的人交流的好機會。

[![加入 discord 頻道](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

專案團隊也會在 Discord 上協助任何學員。

## 貢獻

本課程為開源專案。若你發現改進空間或問題，歡迎建立 [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) 或回報 [GitHub Issues](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

專案團隊會追蹤所有貢獻。貢獻開源是發展生成式 AI 職涯的絕佳方式。

大部分貢獻須同意一份貢獻者授權協議 (CLA)，聲明你有權利且確實授權我們使用你的貢獻。詳情請見 [CLA，貢獻者授權協議網站](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)。

重要提示：翻譯本程式庫時，請勿使用機器翻譯。我們會透過社群核實翻譯品質，請僅自願翻譯你精通的語言版本。

提交 Pull Request 時，CLA 機器人會自動判斷你是否需簽署 CLA，並在 PR 加上標籤或留言提示。請按照機器人指示完成署名。此流程於所有使用 CLA 的程式庫中只須執行一次。


本項目已採納 [Microsoft 開源行為準則](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)。如需更多資訊，請閱讀行為準則常見問題或聯絡 [Email opencode](opencode@microsoft.com) 以提出任何額外問題或意見。

## 開始吧

現在您已完成本課程所需的步驟，讓我們透過獲取 [生成式 AI 及大型語言模型入門](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) 開始吧。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->