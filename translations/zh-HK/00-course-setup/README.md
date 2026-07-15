# 課程入門指南

我們很高興您開始這門課程，並期待看到您使用生成式 AI 所激發出的創作靈感！

為確保您的學習順利，本文頁將概述設定步驟、技術需求以及需要時可尋求協助的管道。

## 設定步驟

要開始本課程，您需要完成以下步驟。

### 1. 分叉本程式碼庫

[將本程式碼庫全部分叉 (Fork this entire repo)](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) 到您自己的 GitHub 帳號，以便修改程式碼並完成挑戰。您也可以[加星標 (🌟) 本儲存庫](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)，讓您更容易找到它及相關儲存庫。

### 2. 建立 Codespace

為避免執行程式碼時遇到任何相依性問題，我們建議您使用 [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) 來運行本課程。

在您的分叉庫中：**Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/zh-HK/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 新增密鑰 (Secret)

1. ⚙️ 齒輪圖示 -> 指令面板 (Command Palette) -> Codespaces : Manage user secret -> 新增密鑰。
2. 名稱填寫 OPENAI_API_KEY，貼上您的密鑰，然後儲存。

### 3. 下一步是？

| 我想要…             | 前往…                                                             |
|---------------------|------------------------------------------------------------------|
| 開始第一課           | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md) |
| 離線作業             | [`setup-local.md`](02-setup-local.md)                              |
| 設定大型語言模型供應商 | [`providers.md`](03-providers.md)                                  |
| 認識其他學員         | [加入我們的 Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 故障排除


| 症狀                                     | 解決方法                                                       |
|-----------------------------------------|--------------------------------------------------------------|
| 容器建置卡住超過 10 分鐘                   | **Codespaces ➜ “Rebuild Container”**                         |
| 顯示 `python: command not found`           | 終端機未連接，點擊 **+** ➜ *bash*                             |
| 從 OpenAI 取得 `401 Unauthorized`         | 錯誤或過期的 `OPENAI_API_KEY`                                  |
| VS Code 顯示「Dev container mounting…」   | 重新整理瀏覽器分頁——Codespaces 有時會失去連線                 |
| 筆記本內核 (kernel) 遺失                    | 筆記本選單 ➜ **Kernel ▸ Select Kernel ▸ Python 3**             |

   Unix 系統：

   ```bash
   touch .env
   ```

   Windows 系統：

   ```cmd
   echo . > .env
   ```

3. **編輯 `.env` 檔案**：使用文字編輯器（例如 VS Code、Notepad++ 或其他編輯器）開啟 `.env` 檔案，加入以下內容，並以您實際的 Microsoft Foundry Models 端點和金鑰替換占位符（取得方式請參考 [`providers.md`](03-providers.md)）：

   > **注意：** GitHub Models（及其 `GITHUB_TOKEN` 變數）將於 2026 年 7 月底退役，請改用 [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)。

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. <strong>儲存檔案</strong>：儲存變更並關閉文字編輯器。

5. **安裝 `python-dotenv`**：若尚未安裝，您需要安裝 `python-dotenv` 套件，用以從 `.env` 檔案加載環境變數到 Python 應用程式。使用 `pip` 安裝指令如下：

   ```bash
   pip install python-dotenv
   ```

6. **在您的 Python 腳本中載入環境變數**：於 Python 腳本中，使用 `python-dotenv` 套件載入 `.env` 中的環境變數：

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

就這樣！您已成功建立 `.env` 檔案，新增 Microsoft Foundry Models 認證，並在 Python 程式中載入它們。

## 如何在本機電腦上執行

若要在本機電腦上執行程式碼，您需先安裝某個版本的 [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)。

之後，您需要將此儲存庫克隆 (clone) 下來：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

準備就緒後，即可開始動手！

## 可選步驟

### 安裝 Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是 Conda、Python 及部分套件的輕量安裝器。
Conda 本身是一套套件管理器，可輕鬆建置並切換不同 Python [<strong>虛擬環境</strong>](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) 及套件。且在安裝無法使用 `pip` 的套件時十分有用。

您可以參考 [MiniConda 安裝指南](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) 進行設定。

安裝完 Miniconda 後，若尚未克隆儲存庫，請先克隆 [本儲存庫](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)

接著，您需要建立一個虛擬環境。使用 Conda 可以建立一個新環境設定檔（_environment.yml_）。若您使用 Codespaces，請在 `.devcontainer` 資料夾下建立，即 `.devcontainer/environment.yml`。

請將底下片段貼入您的環境設定檔：

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

若使用 conda 遇到錯誤，可手動利用以下命令安裝 Microsoft AI 套件。

```
conda install -c microsoft azure-ai-ml
```

環境設定檔定義我們所需要的相依套件。`<environment-name>` 是您要用於 Conda 環境的名稱，`<python-version>` 則是您想使用的 Python 版本，例如 `3` 代表使用最新的大版本。

完成後，您可以在命令列/終端機使用以下指令建立 Conda 環境：

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer 子路徑只適用於 Codespace 設定
conda activate ai4beg
```

如有問題，請參考 [Conda 環境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

### 使用 Visual Studio Code 與 Python 支援擴充套件

我們建議本課程使用 [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) 編輯器，並安裝 [Python 支援擴充套件](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)。不過這只是建議，非絕對必要。

> <strong>注意</strong>：將課程儲存庫用 VS Code 開啟時，您可選擇在容器中設定專案，因為課程儲存庫內有[特殊 `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)資料夾。後續會詳細說明。

> <strong>注意</strong>：一旦您克隆並用 VS Code 開啟資料夾，它會自動建議您安裝 Python 支援擴充套件。

> <strong>注意</strong>：若 VS Code 建議您重新在容器中開啟儲存庫，請拒絕此請求，以便使用本機安裝的 Python 版本。

### 使用瀏覽器中的 Jupyter

您也可以直接在瀏覽器中使用 [Jupyter 環境](https://jupyter.org?WT.mc_id=academic-105485-koreyst) 開發專案。無論是經典的 Jupyter，或是 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst)，均提供了完善的開發環境，具自動完成、程式碼高亮等功能。

要在本機啟動 Jupyter，請打開終端機或命令列，切換至課程資料夾，然後執行：

```bash
jupyter notebook
```

或者

```bash
jupyterhub
```

執行後，命令列視窗將顯示可訪問的 Jupyter 網址。

進入該網址後，您將看到課程大綱，並能瀏覽任何 `*.ipynb` 檔案。例如 `08-building-search-applications/python/oai-solution.ipynb`。

### 容器中執行

除了在電腦或 Codespace 內設定外，另一選擇是使用 [容器 (container)](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)。課程儲存庫中特殊的 `.devcontainer` 資料夾可協助 VS Code 在容器中建立此專案。若非 Codespaces 環境，您需要安裝 Docker。坦白說，這比較複雜，我們只建議具有容器經驗者使用。

在 GitHub Codespaces 使用時，保護 API 密鑰最安全的方法之一是用 Codespace Secrets。請參閱 [Codespaces 秘密管理指南](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) 以了解詳情。


## 課程與技術需求

課程包含 6 個概念課程及 6 個程式設計課程。

程式設計課程使用 Azure OpenAI 服務。執行程式碼前，您須取得 Azure OpenAI 服務之存取權和 API 金鑰。您可透過[填寫此申請表](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)申請。

在等候申請審核期間，每堂程式設計課程也附有 `README.md` 檔，供您瀏覽程式碼和輸出結果。

## 初次使用 Azure OpenAI 服務

若您是首次使用 Azure OpenAI 服務，請參考此指南了解如何[建立並部署 Azure OpenAI 資源](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)。

## 初次使用 OpenAI API

若您是首次使用 OpenAI API，請參考此指南學習如何[建立及使用介面](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)。

## 認識其他學員

我們在官方的 [AI Community Discord 伺服器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) 建立了頻道以供學員交流。這是與其他志同道合的創業者、開發者、學生及任何希望提升生成式 AI 技能者交友的絕佳管道。

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

專案團隊也會在此 Discord 伺服器協助學習者。

## 貢獻

此課程為開源專案，若您發現可改進之處或問題，歡迎提出 [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) 或回報 [GitHub 問題](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

專案團隊會追蹤所有貢獻。參與開源是一種學習生成式 AI 的極佳方式。

多數貢獻需要您同意貢獻者授權協議 (CLA)，聲明您有權利並確實授權我們使用您的貢獻。詳情請參閱[CLA, 貢獻者授權協議網站](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)。

重要提示：翻譯本儲存庫內文字時，請勿使用機器翻譯。我們會透過社群驗證翻譯內容，請只在您精通的語言義務參與翻譯。

當您提交拉取請求 (pull request) 時，CLA 機器人會自動判定您是否需要提供 CLA，並標示 PR（例如標籤、評論）。只須按照機器人指示操作即可，且一般只需執行一次，適用於所有採用我們 CLA 的儲存庫。


本項目已採用 [Microsoft 開源行為守則](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)。欲了解更多資訊，請閱讀行為守則常見問題或聯絡 [電子郵件 opencode](opencode@microsoft.com) 提出任何額外問題或意見。

## 讓我們開始吧

現在您已完成了本課程所需的步驟，讓我們先從瞭解 [生成式 AI 與大型語言模型介紹](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) 開始。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->