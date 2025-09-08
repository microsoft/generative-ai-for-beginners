<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T14:48:09+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "hk"
}
-->
# 開始這個課程

我哋好開心你開始呢個課程，期待睇下你會用生成式 AI 創造啲咩有趣嘅項目！

為咗確保你順利學習，呢頁會講解設定步驟、技術要求，同埋如果有需要可以去邊度搵幫手。

## 設定步驟

要開始呢個課程，你需要完成以下步驟。

### 1. Fork 呢個 Repo

[將成個 repo fork](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) 去你自己嘅 GitHub 帳戶，咁你就可以改 code 同完成挑戰。你都可以 [star (🌟) 呢個 repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)，方便之後搵返佢同相關 repo。

### 2. 建立一個 codespace

為咗避免運行 code 時出現依賴問題，我哋建議你用 [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) 來上呢個課程。

喺你 fork 咗嘅 repo 入面：**Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 加入 secret

1. ⚙️ 齒輪 icon -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. 名稱填 OPENAI_API_KEY，貼上你嘅 key，然後 Save。

### 3.  下一步做咩？

| 我想…                | 去邊度…                                                                 |
|---------------------|-------------------------------------------------------------------------|
| 開始第一課           | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| 離線學習             | [`setup-local.md`](02-setup-local.md)                                   |
| 設定 LLM 供應商      | [`providers.md`](providers.md)                                          |
| 同其他學員交流       | [加入我哋嘅 Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 常見問題排解

| 症狀                                       | 解決方法                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| Container build 超過 10 分鐘都未完成      | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal 未連接；撳 **+** ➜ *bash*                              |
| OpenAI 回傳 `401 Unauthorized`            | `OPENAI_API_KEY` 錯咗／過期                                     |
| VS Code 顯示 “Dev container mounting…”    | 重新整理瀏覽器分頁—Codespaces 有時會斷線                        |
| Notebook kernel 唔見咗                    | Notebook menu ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix-based 系統：

   ```bash
   touch .env
   ```

   Windows：

   ```cmd
   echo . > .env
   ```

3. **編輯 `.env` 檔案**：用文字編輯器（例如 VS Code、Notepad++ 或其他）打開 `.env` 檔案。加以下一行，將 `your_github_token_here` 換成你真正嘅 GitHub token：

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **儲存檔案**：儲存更改並關閉編輯器。

5. **安裝 `python-dotenv`**：如果你未安裝過，請用 `pip` 安裝 `python-dotenv`，咁先可以喺 Python 應用程式讀取 `.env` 檔案入面嘅環境變數。

   ```bash
   pip install python-dotenv
   ```

6. **喺 Python 程式載入環境變數**：喺你嘅 Python 程式入面，用 `python-dotenv` 載入 `.env` 檔案嘅環境變數：

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

就係咁簡單！你已經成功建立 `.env` 檔案，加入咗 GitHub token，並且載入咗去你嘅 Python 應用程式。

## 點樣喺你部電腦本地運行

如果你想喺自己部電腦本地運行 code，你需要安裝 [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) 嘅某個版本。

之後要用呢個 repo，你要 clone 佢：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

clone 完之後，你就可以開始啦！

## 可選步驟

### 安裝 Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 係一個輕量級嘅安裝程式，可以幫你安裝 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python 同埋一啲常用套件。
Conda 本身係一個套件管理器，可以方便你設定同切換唔同嘅 Python [**虛擬環境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) 同套件。對於安裝一啲 `pip` 無嘅套件都好有用。

你可以跟住 [MiniConda 安裝教學](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) 去安裝。

安裝好 Miniconda 之後，你要 clone [呢個 repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)（如果你未 clone 過）。

跟住你要建立一個虛擬環境。用 Conda 嘅話，可以建立一個新嘅環境檔案（_environment.yml_）。如果你用緊 Codespaces，請喺 `.devcontainer` 目錄入面建立，即 `.devcontainer/environment.yml`。

將以下內容加落你嘅環境檔案：

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

如果你用 conda 有咩問題，可以手動用以下指令安裝 Microsoft AI Libraries。

```
conda install -c microsoft azure-ai-ml
```

環境檔案會列出我哋需要嘅依賴。`<environment-name>` 係你想用嘅 Conda 環境名，`<python-version>` 係你想用嘅 Python 版本，例如 `3` 係最新主版本。

搞掂之後，可以喺命令列／終端機執行以下指令建立 Conda 環境：

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

如果有問題，可以參考 [Conda 環境教學](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

### 用 Visual Studio Code 同 Python 擴充功能

我哋建議你用 [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) 編輯器，並安裝 [Python 擴充功能](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 來上呢個課程。不過呢個只係建議，唔係必須。

> **Note**: 打開課程 repo 喺 VS Code，可以選擇用 container 方式設定項目。因為 repo 入面有個 [特別嘅 `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 目錄。之後會再詳細講。

> **Note**: 你 clone 完並打開目錄喺 VS Code，佢會自動建議你安裝 Python 擴充功能。

> **Note**: 如果 VS Code 建議你用 container 打開 repo，請拒絕，咁你就可以用本地安裝嘅 Python。

### 用瀏覽器開 Jupyter

你都可以用 [Jupyter 環境](https://jupyter.org?WT.mc_id=academic-105485-koreyst) 喺瀏覽器直接做項目。無論係 classic Jupyter 定 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) 都有自動補全、語法高亮等功能，開發體驗唔錯。

要本地開 Jupyter，可以去終端機／命令列，去到課程目錄，然後執行：

```bash
jupyter notebook
```

或者

```bash
jupyterhub
```

咁就會開一個 Jupyter 實例，命令列會顯示登入網址。

登入之後，你會見到課程大綱，可以打開任何 `*.ipynb` 檔案。例如 `08-building-search-applications/python/oai-solution.ipynb`。

### 用 container 運行

除咗喺你部電腦或者 Codespace 設定環境，你都可以用 [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)。課程 repo 入面有個特別嘅 `.devcontainer` 資料夾，VS Code 可以用嚟喺 container 入面設定項目。如果唔係用 Codespaces，就要安裝 Docker，過程會複雜啲，所以只建議有 container 經驗嘅人用。

用 GitHub Codespaces 嘅時候，最安全嘅方法係用 Codespace Secrets 儲存 API key。可以參考 [Codespaces secrets 管理教學](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) 了解更多。

## 課程內容同技術要求

課程有 6 個概念課堂同 6 個編程課堂。

編程課堂會用到 Azure OpenAI Service。你需要有 Azure OpenAI service 嘅存取權同 API key 先可以運行 code。你可以[填表申請](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)。

等申請批核期間，每個編程課堂都有 `README.md`，你可以睇 code 同埋執行結果。

## 第一次用 Azure OpenAI Service

如果你第一次用 Azure OpenAI service，請跟住呢個教學 [建立同部署 Azure OpenAI Service 資源](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)。

## 第一次用 OpenAI API

如果你第一次用 OpenAI API，請參考教學 [建立同使用介面](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)。

## 同其他學員交流

我哋喺官方 [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) 開咗頻道，方便大家交流。呢個係一個好好嘅機會，可以同其他有志創業、開發、學生或者想學生成式 AI 嘅朋友建立人脈。

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

項目團隊都會喺 Discord 幫大家解答問題。

## 參與貢獻

呢個課程係開源項目。如果你發現有改善空間或者有問題，歡迎 [開 Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) 或者 [報 GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

項目團隊會記錄所有貢獻。參與開源係建立你生成式 AI 事業嘅好方法。

大部分貢獻都需要你同意 Contributor License Agreement (CLA)，即係你有權利同願意授權我哋使用你嘅貢獻。詳情可以睇 [CLA, Contributor License Agreement 網站](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)。

重要提示：翻譯本 repo 內容時，請確保唔好用機器翻譯。我哋會由社群驗證翻譯，所以只接受你熟悉語言嘅翻譯。

你提交 pull request 時，CLA-bot 會自動判斷你需唔需要簽 CLA，並加上標籤或留言。只要跟住 bot 指示做就得。你只需要喺所有用我哋 CLA 嘅 repo 做一次。

本項目採用 [Microsoft 開源行為守則](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)。想了解多啲可以睇 FAQ 或電郵 [Email opencode](opencode@microsoft.com) 查詢。

## 一齊開始啦
而家你已經完成咗呢個課程所需嘅步驟，咁我哋就開始啦，首先嚟睇下[生成式人工智能同大型語言模型嘅簡介](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)。

---

**免責聲明**：
本文件經由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能會有錯誤或不準確之處。原始語言的文件應被視為具權威性的來源。對於重要資訊，建議使用專業人工翻譯。我們不會對因使用本翻譯而產生的任何誤解或誤釋承擔責任。