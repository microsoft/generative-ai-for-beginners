# 開始這個課程

我們非常期待你開始這個課程，並看看你會用生成式人工智能激發出什麼創意！

為確保你的成功，此頁面列出了設定步驟、技術要求，以及需要幫助時可以取得支援的地方。

## 設定步驟

要開始這個課程，你需要完成以下步驟。

### 1. 分叉這個儲存庫

將[整個儲存庫分叉 (fork)](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)到你自己的 GitHub 帳號，這樣你才能更改任何程式碼及完成挑戰。你也可以[收藏 (star)🌟 這個儲存庫](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)，方便日後找到它和相關的儲存庫。

### 2. 建立 codespace

為避免執行程式碼時遇到相依性問題，我們建議在[GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)中運行此課程。

進入你的分叉儲存庫：**Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/zh-MO/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 新增祕密

1. ⚙️ 齒輪圖示 -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret。  
2. 名稱填 OPENAI_API_KEY，貼上你的金鑰，並儲存。

### 3. 下一步是什麼？

| 我想要…            | 前往…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| 開始第一課          | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| 離線工作            | [`setup-local.md`](02-setup-local.md)                                   |
| 設置 LLM 供應商     | [`providers.md`](03-providers.md)                                        |
| 認識其他學員        | [加入我們的 Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 疑難排解

| 症狀                                   | 解決方法                                                         |
|--------------------------------------|-----------------------------------------------------------------|
| 容器建構卡住超過 10 分鐘              | **Codespaces ➜ “Rebuild Container”**                            |
| 顯示 `python: command not found`      | 終端機未連接；點擊 **+** ➜ *bash*                                |
| OpenAI 回傳 `401 Unauthorized`        | `OPENAI_API_KEY` 鍵錯誤或已過期                                   |
| VS Code 顯示「Dev container mounting…」| 重新整理瀏覽器分頁 — Codespaces 有時會失去連線                   |
| 筆記本內核缺失                        | 筆記本選單 ➜ **Kernel ▸ Select Kernel ▸ Python 3**              |

   Unix 系統：

   ```bash
   touch .env
   ```

   Windows：

   ```cmd
   echo . > .env
   ```

3. **編輯 `.env` 檔案**：使用文字編輯器（例如 VS Code、Notepad++ 或任何其他編輯器）打開 `.env` 檔案。加入以下行，將 `your_github_token_here` 換成你的 GitHub 令牌：

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **儲存檔案**：儲存變更並關閉文字編輯器。

5. **安裝 `python-dotenv`**：如果尚未安裝，你需要安裝 `python-dotenv` 套件，讓你的 Python 應用程式可以從 `.env` 檔案讀取環境變數。你可以使用 `pip` 安裝：

   ```bash
   pip install python-dotenv
   ```

6. **在 Python 程式中載入環境變數**：在你的 Python 程式中，使用 `python-dotenv` 套件載入 `.env` 檔案中的環境變數：

   ```python
   from dotenv import load_dotenv
   import os

   # 從 .env 檔案載入環境變數
   load_dotenv()

   # 訪問 GITHUB_TOKEN 變數
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

完成了！你已成功建立 `.env` 檔案、加入 GitHub 令牌，並將其載入你的 Python 應用程式。

## 在你的電腦本地端執行

要在本地電腦執行程式碼，你必須先安裝某個版本的[Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)。

接著，你需要將此儲存庫複製 (clone)：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

完成檢出後，你就可以開始學習了！

## 可選步驟

### 安裝 Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是一個輕量級的安裝程式，用於安裝 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python 及部分套件。  
Conda 本身是套件管理器，使你能輕鬆設定並切換不同的 Python [虛擬環境](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)及套件。它也適合安裝不支援使用 `pip` 安裝的套件。

你可以依照[MiniConda 安裝指南](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst)來安裝。

安裝 Miniconda 後，如果還沒做，你需要先[複製儲存庫](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)。

接著，你需要建立虛擬環境。使用 Conda 的話，請先建立一個環境設定檔 (_environment.yml_)。如果你使用 Codespaces，請在 `.devcontainer` 目錄中建立，也就是 `.devcontainer/environment.yml`。

在該環境檔案填入以下內容：

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

如果你使用 conda 時遇到錯誤，可以在終端機中手動安裝 Microsoft AI 函式庫，請使用下方指令：

```
conda install -c microsoft azure-ai-ml
```

環境檔指定了我們需要的相依套件。`<environment-name>` 是你想為 Conda 環境命名的名稱，`<python-version>` 是你要使用的 Python 版本，例如，`3` 代表 Python 最新主版本。

完成後，你可以在指令行／終端機執行以下指令來建立 Conda 環境：

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer 子路徑只適用於 Codespace 設定
conda activate ai4beg
```

如果遇到問題，請參考[Conda 環境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

### 使用帶有 Python 支援擴充功能的 Visual Studio Code

我們建議此課程使用 [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) 編輯器，並安裝 [Python 支援擴充功能](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)。不過這只是建議，非硬性要求。

> **注意**：開啟課程儲存庫於 VS Code 時，可以選擇在容器內設定此專案，因為儲存庫中有[特別的 `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)目錄。稍後會進一步說明。

> **注意**：一旦你克隆且開啟目錄，VS Code 會自動提議你安裝 Python 支援擴充功能。

> **注意**：若 VS Code 建議你重新在容器中開啟儲存庫，請拒絕，這樣你才能使用本機安裝的 Python 版本。

### 在瀏覽器中使用 Jupyter

你也可以直接用瀏覽器內的 [Jupyter 環境](https://jupyter.org?WT.mc_id=academic-105485-koreyst)工作。經典 Jupyter 和 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) 提供愉快的開發環境，有自動補全、語法高亮等功能。

要在本地啟動 Jupyter，請開啟終端機／命令列，切換到課程目錄，執行：

```bash
jupyter notebook
```

或是

```bash
jupyterhub
```

執行後會啟動 Jupyter 服務，權限的 URL 會顯示在命令列視窗。

你開啟 URL 後應該能看到課程大綱，並能導覽任何 `*.ipynb` 筆記本檔案，例如 `08-building-search-applications/python/oai-solution.ipynb`。

### 在容器中執行

除了在電腦或 Codespace 設定環境外，你也可以使用[容器](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)。課程儲存庫中的特殊 `.devcontainer` 資料夾可讓 VS Code 在容器中設定專案。  
在 Codespaces 以外的情況，這需要安裝 Docker，而且確實比較複雜，所以我們建議只有有容器經驗的人選用。

使用 GitHub Codespaces 時保護 API 金鑰安全的最佳方法之一是使用 Codespace Secrets。請參考[Codespaces 秘密管理指南](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst)了解詳情。

## 課程與技術要求

本課程包含 6 個概念課和 6 個程式課。

程式課使用 Azure OpenAI 服務，你需要擁有 Azure OpenAI 的使用權和 API 金鑰方能執行程式碼。你可以透過[提交申請](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)來獲取使用權。

在申請審核期間，每堂程式課也會附有 `README.md` 檔案供你查看程式碼與輸出結果。

## 第一次使用 Azure OpenAI 服務

若你是第一次使用 Azure OpenAI 服務，請遵循此指南，了解如何[建立並部署 Azure OpenAI 服務資源。](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## 第一次使用 OpenAI API

若你是第一次使用 OpenAI API，請依指南學習如何[建立和使用這個介面。](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## 認識其他學員

我們在官方的 [AI 社群 Discord 伺服器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)創建了與其他學員互動的頻道。這是認識其他志同道合創業家、開發者、學生，以及想在生成式 AI 領域進修所有人的好管道。

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

專案團隊也會在此 Discord 伺服器中協助學員。

## 貢獻

這門課程是開源計畫。如果你發現改進的空間或問題，請建立[拉取請求 (Pull Request)](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)或提出[GitHub 問題追蹤 (issue)](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

專案團隊會追蹤所有貢獻。在生成式 AI 領域，貢獻開源是一條極佳的職涯發展途徑。

多數貢獻需要你同意一份貢獻者授權協議 (Contributor License Agreement, CLA)，聲明你有權並確實授權我們使用你的貢獻。詳細內容請參閱[CLA，貢獻者授權協議網站](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)。

重要：翻譯此儲存庫內容時，請勿使用機器翻譯。我們會透過社群驗證翻譯品質，故請只協助翻譯你熟悉的語言。

提交拉取請求後，CLA-bot 會自動判定你是否須提供 CLA，並為 PR 添加適當標籤或留言。請遵照機器人的指示操作。全生態系中只需操作一次即可。

本專案已採納[微軟開源行為準則](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)。想了解更多，請閱讀行為準則常見問答或電郵聯絡[Email opencode](opencode@microsoft.com)。

## 讓我們開始吧
現在您已完成完成此課程所需的步驟，讓我們通過獲得一個[生成式人工智能和大型語言模型的介紹](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)開始吧。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件是使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。儘管我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原文文件之母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->