# 開始進行本課程

我們非常期待你開始這門課程，並看看你會受到什麼啟發去創造基於生成式 AI 的項目！

為了確保你成功，這頁說明了設定步驟、技術要求，以及如有需要可尋求幫助的地方。

## 設定步驟

要開始進行本課程，你需要完成以下步驟。

### 1. Fork 這個倉庫

[Fork 整個倉庫](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) 到你自己的 GitHub 帳戶，以便你能更改任何程式碼並完成挑戰。你也可以[🌟星標這個倉庫](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)，以便更容易找到它和相關的倉庫。

### 2. 建立 codespace

為避免執行程式碼時出現依賴問題，我們建議在[GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)中執行本課程。

在你的 fork 倉庫中：**Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/zh-HK/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 加入密鑰

1. ⚙️ 齒輪圖示 -> Command Palette -> Codespaces : Manage user secret -> Add a new secret。
2. 名稱為 OPENAI_API_KEY，貼上你的金鑰，然後保存。

### 3. 接下來做什麼？

| 我想要…            | 前往…                                                                |
|---------------------|----------------------------------------------------------------------|
| 開始第一課          | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)   |
| 離線操作            | [`setup-local.md`](02-setup-local.md)                                 |
| 設定 LLM 供應商     | [`providers.md`](03-providers.md)                                     |
| 認識其他學習者      | [加入我們的 Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 故障排除

| 症狀                                   | 解決方法                                                        |
|---------------------------------------|-----------------------------------------------------------------|
| 容器建構持續卡住超過 10 分鐘           | **Codespaces ➜ “Rebuild Container”**                            |
| 出現 `python: command not found`      | 終端機未附加，點擊 **+** ➜ *bash*                               |
| 從 OpenAI 返回 `401 Unauthorized`    | `OPENAI_API_KEY` 錯誤或過期                                    |
| VS Code 顯示 “Dev container mounting…” | 重新整理瀏覽器分頁——Codespaces 有時會斷線                     |
| Notebook kernel 缺失                   | Notebook 選單 ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

   Unix 系統：

   ```bash
   touch .env
   ```

   Windows 系統：

   ```cmd
   echo . > .env
   ```

3. **編輯 `.env` 檔案**：在文字編輯器（例如 VS Code、Notepad++ 或其他編輯器）中打開 `.env` 檔案。加入以下內容，將 `your_github_token_here` 替換成你實際的 GitHub Token：

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **儲存檔案**：儲存變更並關閉文字編輯器。

5. **安裝 `python-dotenv`**：如果你還沒有安裝，需要安裝 `python-dotenv` 套件以將環境變數從 `.env` 檔案載入 Python 應用程式。你可以使用 `pip` 安裝：

   ```bash
   pip install python-dotenv
   ```

6. **在 Python 腳本中載入環境變數**：在你的 Python 腳本中，使用 `python-dotenv` 套件載入 `.env` 檔案中的環境變數：

   ```python
   from dotenv import load_dotenv
   import os

   # 從 .env 檔案載入環境變量
   load_dotenv()

   # 存取 GITHUB_TOKEN 變量
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

完成了！你已成功建立 `.env` 檔案，加入 GitHub Token，並載入到 Python 應用程式中。

## 如何在本機電腦上運行

要在本機電腦上運行程式碼，你需先安裝某個版本的[Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)。

接著你需要複製這個倉庫：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

當你完成所有檢出後，就可以開始了！

## 選用步驟

### 安裝 Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是用來安裝 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python 以及一些套件的輕量安裝器。
Conda 本身是一個套件管理器，讓你方便設定與切換不同 Python [**虛擬環境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)和套件。它也非常適合用來安裝無法透過 `pip` 安裝的套件。

你可以參考[MiniConda 安裝指南](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst)來完成安裝。

安裝 Miniconda 後，你需要複製[倉庫](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)（如果還沒做的話）

接著，你需要建立虛擬環境。使用 Conda 的話，在 `.devcontainer` 目錄下（如果你使用 Codespaces）建立一個新的環境描述檔案（_environment.yml_），路徑即為 `.devcontainer/environment.yml`。

請將下列範例內容加入你的環境描述檔案：

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

如果你遇到 conda 使用錯誤，可以在終端機手動執行以下指令安裝 Microsoft AI 函式庫：

```
conda install -c microsoft azure-ai-ml
```

該環境檔案指定了我們需要的相依項。`<environment-name>` 代表你想用作 Conda 環境的名稱，`<python-version>` 是你想使用的 Python 版本，例如 `3` 代表最新的 Python 主版本。

完成後，你可以在終端機執行以下指令來建立 Conda 環境：

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer 子路徑只適用於 Codespace 設定
conda activate ai4beg
```

如有問題，請參考[Conda 環境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

### 使用 Visual Studio Code 搭配 Python 支援外掛

我們建議在本課程中使用[Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst)編輯器，並安裝[Python 支援外掛](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)。不過這只是建議，非硬性要求。

> **注意**：透過在 VS Code 中開啟課程倉庫，你可以選擇在容器內設定此專案。這是因為課程倉庫中有[特別的 `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)目錄。後面會詳細說明。

> **注意**：克隆並開啟目錄後，VS Code 會自動建議你安裝 Python 支援外掛。

> **注意**：如果 VS Code 建議你重新以容器模式開啟倉庫，請拒絕此請求，以便使用本地已安裝的 Python。

### 在瀏覽器中使用 Jupyter

你也可以使用瀏覽器中的[Jupyter 環境](https://jupyter.org?WT.mc_id=academic-105485-koreyst)來工作。傳統 Jupyter 以及 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) 提供相當好用的開發環境，具備自動補齊、程式碼高亮等功能。

要在本機啟動 Jupyter，請打開終端機或命令行，切換到課程目錄，執行：

```bash
jupyter notebook
```

或者

```bash
jupyterhub
```

這會啟動一個 Jupyter 服務，並在命令行視窗中顯示存取 URL。

開啟該 URL 後，你應該會看到課程大綱並能瀏覽任何 `*.ipynb` 檔案，例如 `08-building-search-applications/python/oai-solution.ipynb`。

### 在容器中執行

另一種選擇是使用[容器](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)，來避免在電腦或 codespace 設定一切。課程庫中的特殊 `.devcontainer` 資料夾，可讓 VS Code 在容器中設定該專案。除了 Codespaces 外，你需要安裝 Docker，坦白說也需要一點技術背景，我們建議有容器使用經驗者使用此方案。

安全管理 API 金鑰的最佳方式之一是使用 GitHub Codespaces 的 Codespace Secrets。請參考[Codespaces secrets 管理](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst)指南以了解詳情。

## 課程課節與技術需求

本課程包含 6 個概念課節和 6 個程式實作課節。

實作課節使用 Azure OpenAI 服務。你需要有 Azure OpenAI 服務的存取權和 API 金鑰才能運行程式碼。你可以透過[填寫此申請表](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)申請存取權。

申請審核期間，每個程式實作課節也附有 `README.md` 文件，可以觀看程式碼與輸出結果。

## 首次使用 Azure OpenAI 服務

若是第一次使用 Azure OpenAI 服務，請遵循本指南了解如何[建立與部署 Azure OpenAI 服務資源](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)。

## 首次使用 OpenAI API

若是第一次接觸 OpenAI API，請參考指南了解如何[建立及使用介面](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)。

## 認識其他學習者

我們在官方 [AI Community Discord 伺服器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)中建立了頻道讓你認識其他學習者。這是建立人脈的好機會，適合其他志同道合的創業者、開發者、學生，以及所有想提升生成式 AI 技能的人。

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

專案團隊也會在此 Discord 伺服器上協助學習者。

## 貢獻

本課程是開源計畫。如果你發現改進空間或問題，請建立 [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) 或提交 [GitHub issues](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

專案團隊會追蹤所有貢獻。投身開源是建立生成式 AI 事業的絕佳方式。

大部分貢獻需要你同意一份貢獻者授權協議（Contributor License Agreement，CLA），聲明你有權且確實授權我們使用你的貢獻。詳情請參閱[CLA，貢獻者授權協議網站](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)。

重要說明：當翻譯本倉庫的文字時，請確保不要使用機器翻譯。我們會透過社群驗證翻譯內容，因此請僅承擔你熟悉語言的翻譯工作。

當你提交 pull request 時，CLA 機器人會自動判斷你是否需要提供 CLA，並適當標記 PR（例如標籤、留言）。請遵循該機器人指示。你只需在所有採用此 CLA 的倉庫中完成一次。

本計畫已採用[Microsoft 開源行為守則](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)。欲瞭解詳情，請閱讀守則常見問題，或寄信至 [Email opencode](opencode@microsoft.com) 詢問。

## 開始吧！
既然你已完成完成此課程所需的步驟，讓我們開始學習 [生成式 AI 與大型語言模型簡介](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。應以文件的原文版本作為權威來源。對於重要資訊，建議採用專業人工翻譯。本公司不對因使用此翻譯所引起之任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->