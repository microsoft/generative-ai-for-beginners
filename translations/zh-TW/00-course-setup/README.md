# 這門課程的入門指南

我們非常期待你開始這門課程，看看你會受到什麼啟發，使用生成式 AI 打造什麼作品！

為確保你的成功，本頁面將說明設定步驟、技術需求，以及如有需要可獲得協助的地方。

## 設定步驟

想開始進行這門課程，請完成以下步驟。

### 1. 分支這個程式庫（Fork this Repo）

[將整個程式庫 fork 到你的 GitHub 帳號](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)，以能更改程式碼並完成挑戰。你也可以[為此程式庫加星號 (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)，方便未來尋找本程式庫及相關程式庫。

### 2. 建立 codespace

為避免執行程式碼時遇到相依性問題，我們建議你使用 [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) 執行這門課程。

在你的 fork 中：**Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/zh-TW/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 新增秘密金鑰

1. ⚙️ 齒輪圖示 -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret。
2. 名稱輸入 OPENAI_API_KEY，貼上你的 API 金鑰，點擊儲存。

### 3. 下一步？

| 我想要…           | 前往…                                                                          |
|---------------------|-------------------------------------------------------------------------------|
| 開始第一堂課      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)            |
| 離線使用            | [`setup-local.md`](02-setup-local.md)                                          |
| 設定大型語言模型提供者 | [`providers.md`](03-providers.md)                                               |
| 認識其他學員       | [加入我們的 Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)  |

## 疑難排解


| 症狀                                         | 解決方法                                                      |
|-----------------------------------------------|------------------------------------------------------------|
| 容器建立停滯超過 10 分鐘                      | **Codespaces ➜ “Rebuild Container”**                        |
| `python: command not found`                   | 終端機未附加；點擊 **+** ➜ *bash*                            |
| OpenAI 回傳 `401 Unauthorized`               | `OPENAI_API_KEY` 輸入錯誤或過期                              |
| VS Code 顯示「Dev container mounting…」訊息 | 重新整理瀏覽器分頁—Codespaces 有時會連線中斷                |
| 筆記本內核缺失                               | 筆記本選單 ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix 系統：

   ```bash
   touch .env
   ```

   Windows 系統：

   ```cmd
   echo . > .env
   ```

3. **編輯 `.env` 檔案**：使用文字編輯器（例如 VS Code、Notepad++ 或任一編輯器）開啟 `.env` 檔案，加入以下幾行，並以你自己的 Microsoft Foundry Models 端點與金鑰替換佔位符（詳見[`providers.md`](03-providers.md) 取得方法）：

   > **注意：** GitHub Models（及其 `GITHUB_TOKEN` 變數）將於 2026 年 7 月底下架，請改用 [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)。

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. <strong>儲存檔案</strong>：儲存修改後關閉文字編輯器。

5. **安裝 `python-dotenv` 套件**：若尚未安裝，請使用 `pip` 安裝 `python-dotenv`，以便從 `.env` 檔案載入環境變數到你的 Python 應用程式：

   ```bash
   pip install python-dotenv
   ```

6. **在 Python 腳本中載入環境變數**：使用 `python-dotenv` 套件從 `.env` 檔案載入環境變數：

   ```python
   from dotenv import load_dotenv
   import os

   # 從 .env 檔案載入環境變數
   load_dotenv()

   # 存取 Microsoft Foundry Models 的變數
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

就是這樣！你已成功建立 `.env` 檔案，新增 Microsoft Foundry Models 的認證資訊，並將它們載入你的 Python 應用程式。

## 如何在本機電腦上執行

若你想在本機電腦上執行程式碼，需先安裝某版本的 [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)。

之後，你必須將本程式庫克隆（clone）下來：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

當你完成檢出一切後，就可以開始進行囉！

## 選擇性步驟

### 安裝 Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是一款輕量型安裝程式，能安裝 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python 及部分套件。
Conda 是套件管理器，能方便設定及切換不同的 Python [<strong>虛擬環境</strong>](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)及套件。它也非常適合安裝無法透過 `pip` 取得的套件。

你可以參考 [MiniConda 安裝指南](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst)。

安裝 Miniconda 後，如果你還沒做，可先克隆此[程式庫](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)

接著需建立虛擬環境。使用 Conda 的話，請建立新環境檔案（_environment.yml_）。若你在 Codespaces 中同步操作，請在 `.devcontainer` 目錄下建立，路徑即為 `.devcontainer/environment.yml`。

將以下程式碼填入你的環境檔案：

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

若你使用 conda 出錯，可以在終端機手動執行下列指令安裝 Microsoft AI 套件。

```
conda install -c microsoft azure-ai-ml
```

環境檔案指定我們的依賴。`<environment-name>` 代表你想使用的 Conda 環境名稱，`<python-version>` 為想使用的 Python 版本，例如 `3` 代表 Python 最新大版本。

完成後，在命令列/終端機執行以下指令，建立你的 Conda 環境。

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer 子路徑僅適用於 Codespace 設定
conda activate ai4beg
```

若有問題，可參考 [Conda 環境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

### 使用 Visual Studio Code 配合 Python 支援擴充功能

我們建議使用 [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) 編輯器，並安裝 [Python 支援延伸](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)，來完成這門課程，但這只算是推薦，非必要條件。

> <strong>注意</strong>：在 VS Code 中開啟課程程式庫時，你可以選擇將專案設置在容器內執行。這是因為本課程程式庫中有一個[特殊的 `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)目錄。稍後會介紹更多相關內容。

> <strong>注意</strong>：當你克隆並在 VS Code 開啟程式目錄時，會自動建議你安裝 Python 支援擴充功能。

> <strong>注意</strong>：若 VS Code 建議你重新在容器中開啟程式庫，請拒絕此請求，以使用在本地安裝的 Python 版本。

### 在瀏覽器中使用 Jupyter

你也可以直接在瀏覽器使用 [Jupyter 環境](https://jupyter.org?WT.mc_id=academic-105485-koreyst) 來進行專案。無論是傳統 Jupyter 還是 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) 都能提供相當愉快的開發體驗，如自動完成、程式碼高亮等功能。

若要在本機啟動 Jupyter，請開啟終端機/命令列，切換至課程目錄，並輸入：

```bash
jupyter notebook
```

或者

```bash
jupyterhub
```

這會啟動 Jupyter 實例，命令列上會顯示存取的 URL。

使用該 URL 後，你將看到課程大綱並能瀏覽任何 `*.ipynb` 筆記本檔。例如 `08-building-search-applications/python/oai-solution.ipynb`。

### 在容器中執行

若不想在電腦或 Codespace 上直接設定，也可使用[容器](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)。此課程程式庫中特殊的 `.devcontainer` 資料夾讓 VS Code 能在容器中設定專案。非 Codespaces 使用時，你需安裝 Docker，但說實話，這過程頗為繁瑣，因此建議有容器經驗者使用。

在 GitHub Codespaces 中，保障 API 金鑰安全的最佳方式是使用 Codespace Secrets。詳情請參考[Codespaces 秘密管理指南](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst)。


## 課程內容與技術需求

本課程包含「學習」課程，說明生成式 AI 概念，以及「實作」課程，提供可能的 **Python** 與 **TypeScript** 程式碼範例。

在實作課程中，我們使用 Microsoft Foundry 的 Azure OpenAI。你將需要 Azure 訂閱與 API 金鑰。此項目開放使用，無需申請，可 [建立 Microsoft Foundry 資源並部署模型](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)，取得你的端點與金鑰。

每堂實作課程還包含 `README.md` 檔案，你可在裡面查看程式碼與輸出結果，而不必執行任何程式。

## 首次使用 Azure OpenAI 服務

若你是初次使用 Azure OpenAI 服務，請參考本指引說明如何[建立及部署 Azure OpenAI 服務資源。](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## 首次使用 OpenAI API

若你是初次使用 OpenAI API，請依本指引了解如何[建立並使用介面。](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## 認識其他學員

我們在官方 [AI Community Discord 伺服器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)中創建了頻道，方便學員們相互認識。這是與其他志同道合的創業家、開發者、學生，以及任何想在生成式 AI 領域提升自己的人建立聯繫的好方法。

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

專案團隊也會在此 Discord 伺服器上協助學員。

## 貢獻

這門課程是開源計畫，若你發現可改進處或問題，請提出 [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) 或回報 [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

專案團隊會追蹤所有貢獻。參與開源是發展生成式 AI 職涯的絕佳途徑。

大多數貢獻須同意貢獻者授權協議（CLA），聲明你有權限且確實授權我們使用你的貢獻。詳情請見 [CLA 貢獻者授權協議網站](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)。

重要事項：翻譯本程式庫文件時，請勿使用機器翻譯。我們會透過社群驗證翻譯品質，請只在你精通該語言時，參與翻譯。


當您提交拉取請求時，CLA-bot 將自動判斷您是否需要提供 CLA 並相應地標註 PR（例如標籤、評論）。只需按照機器人提供的指示操作即可。您只需在所有使用我們 CLA 的倉庫中執行一次此操作。

本專案已採用 [Microsoft 開源行為準則](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)。如需更多資訊，請閱讀行為準則常見問題或使用 [Email opencode](opencode@microsoft.com) 聯絡我們，提出任何其他問題或意見。

## 讓我們開始吧

現在您已完成本課程需要的步驟，讓我們從[生成式 AI 和大型語言模型的介紹](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)開始吧。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->