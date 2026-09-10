# 課程入門指南

我們非常期待你開始這個課程，看看你會如何受生成式 AI 啟發來創作！

為了確保你的成功，本頁面將說明設定步驟、技術需求，以及如有需要的求助途徑。

## 設定步驟

要開始上這門課，你需要完成以下步驟。

### 1. Fork 此倉庫

[Fork 整個倉庫](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) 到你的 GitHub 帳號，以便更改任何程式碼並完成挑戰。你也可以[為此倉庫加星 (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)，方便日後找到本倉庫及相關倉庫。

### 2. 建立 codespace

為避免執行程式碼時出現相依性問題，我們建議使用 [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) 來完成課程。

在你的 fork 中：**Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/zh-HK/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 新增 secret

1. ⚙️ 齒輪圖示 -> Command Palette -> Codespaces : Manage user secret -> Add a new secret。
2. 命名為 OPENAI_API_KEY，貼上你的金鑰，然後保存。

### 3. 接下來做什麼？

| 我想…            | 前往…                                                                |
|-------------------|----------------------------------------------------------------------|
| 開始第一課        | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)  |
| 離線作業          | [`setup-local.md`](02-setup-local.md)                                |
| 設定 LLM 供應商  | [`providers.md`](03-providers.md)                                   |
| 認識其他學員      | [加入我們的 Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 疑難排解


| 症狀                                     | 解決方法                                                       |
|-----------------------------------------|--------------------------------------------------------------|
| 容器建立卡住超過 10 分鐘                 | **Codespaces ➜ “Rebuild Container”**                         |
| 出現 `python: command not found`        | 終端機未附加；點擊 **+** ➜ *bash*                              |
| OpenAI 回傳 `401 Unauthorized`          | 錯誤或過期的 `OPENAI_API_KEY`                                 |
| VS Code 顯示 “Dev container mounting…” | 重新整理瀏覽器分頁—Codespaces 有時會失去連線                  |
| Notebook kernel 缺失                     | Notebook 選單 ➜ **Kernel ▸ Select Kernel ▸ Python 3**        |

   Unix 系統：

   ```bash
   touch .env
   ```

   Windows 系統：

   ```cmd
   echo . > .env
   ```

3. **編輯 `.env` 檔案**：在文字編輯器（例如 VS Code、Notepad++ 或任何其他編輯器）中開啟 `.env` 檔案，加入以下內容，並將佔位符替換為你的 Microsoft Foundry Models 端點和金鑰（請參考 [`providers.md`](03-providers.md) 了解如何取得）：

   > **注意：** GitHub Models（及其 `GITHUB_TOKEN` 變數）將於 2026 年 7 月底退役，請改用 [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)。

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. <strong>保存檔案</strong>：保存修改後關閉文字編輯器。

5. **安裝 `python-dotenv`**：如果尚未安裝，你需要安裝 `python-dotenv` 套件，讓 Python 應用程式能從 `.env` 檔案讀取環境變數。可使用 `pip` 安裝：

   ```bash
   pip install python-dotenv
   ```

6. **在 Python 程式中載入環境變數**：在你的 Python 程式中，使用 `python-dotenv` 套件載入 `.env` 檔案中的環境變數：

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

完成了！你已成功建立 `.env` 檔案，加入 Microsoft Foundry Models 的憑證，並在 Python 應用程式中載入。

## 如何在本機電腦上執行

想在本機電腦上執行程式碼，你需要先[安裝某個版本的 Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)。

接著，要使用此倉庫，需要先 clone 它：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

完成以上步驟後，即可開始！

## 選用步驟

### 安裝 Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是一個輕量級安裝程式，用來安裝 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python 及部分套件。
Conda 本身是套件管理器，方便你建立和切換不同的 Python [<strong>虛擬環境</strong>](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)及套件，對安裝無法透過 `pip` 安裝的套件特別有用。

你可以參考 [MiniConda 安裝指南](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) 來安裝。

安裝 Miniconda 後，如果你還沒 clone [倉庫](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)，請先 clone。

接著你需要建立虛擬環境。使用 Conda 時，可建立環境文件（_environment.yml_）。如果你是使用 Codespaces 同步學習，請在 `.devcontainer` 目錄中建立，即為 `.devcontainer/environment.yml`。

請把以下內容填入你的環境文件：

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

如果你用 conda 時遇到錯誤，可以手動在終端機執行以下命令安裝 Microsoft AI 函式庫。

```
conda install -c microsoft azure-ai-ml
```

環境文件指定了我們需要的相依性。`<environment-name>` 是你想給 Conda 環境取的名字，`<python-version>` 是你想使用的 Python 版本，例如 `3` 代表最新的主要版本。

完成後，在命令列/終端機執行以下命令建立 Conda 環境

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer 子路徑只適用於 Codespace 設定
conda activate ai4beg
```

如果遇到問題，請參考 [Conda 的環境管理指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

### 使用帶 Python 擴充套件的 Visual Studio Code

我們推薦使用 [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) 編輯器，並安裝[Python 擴充套件](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 來完成課程。這只是建議，非必要條件。

> <strong>注意</strong>：在 VS Code 開啟本課程倉庫時，你可以選擇在容器中設定專案。這是因為課程倉庫中內建了[特殊的 `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)資料夾，稍後會詳細介紹。

> <strong>注意</strong>：當你 clone 並在 VS Code 中打開目錄後，會自動建議你安裝 Python 支援擴充套件。

> <strong>注意</strong>：如果 VS Code 建議你重新在容器中開啟倉庫，請拒絕此請求，以便使用本機安裝的 Python 版本。

### 在瀏覽器中使用 Jupyter

你也可以直接在瀏覽器中使用 [Jupyter 環境](https://jupyter.org?WT.mc_id=academic-105485-koreyst) 開發。本地端 Classic Jupyter 與 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) 都提供不錯的開發體驗，並具備自動完成、程式碼高亮等功能。

要在本地啟動 Jupyter，請打開終端機／命令列，切換到課程目錄，執行：

```bash
jupyter notebook
```

或者

```bash
jupyterhub
```

執行後會啟動 Jupyter，命令列視窗中會顯示存取 URL。

打開該 URL 後，你會看到課程大綱，並能瀏覽任何 `*.ipynb` 檔案。例如：`08-building-search-applications/python/oai-solution.ipynb`。

### 在容器中執行

除了在電腦或 Codespace 上設定環境外，另一種方案是使用 [容器](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)。課程倉庫中的特殊 `.devcontainer` 資料夾讓 VS Code 可在容器中設定專案。非 Codespaces 環境下，需要安裝 Docker，說實話有點麻煩，我們建議有容器經驗的學員使用。

使用 GitHub Codespaces 時，保護 API 金鑰的最佳方式之一是使用 Codespace Secrets。請參考 [Codespaces 秘密管理](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) 指南了解詳情。


## 課程內容與技術需求

課程包含「學習」課程講解生成式 AI 概念，以及「實作」課程提供 Python 與 TypeScript 的示範程式碼（視情況而定）。

這些程式碼課程會使用微軟 Foundry 的 Azure OpenAI。你需要有 Azure 訂閱和 API 金鑰。存取權開放，無須申請，[可直接建立 Microsoft Foundry 資源並部署模型](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) 以取得端點與金鑰。

每個程式課程同時都附有 `README.md` 檔，可以不用執行，直接查看程式碼與輸出結果。

## 初次使用 Azure OpenAI 服務

如果你是第一次使用 Azure OpenAI 服務，請參考此指南了解如何[建立和部署 Azure OpenAI 服務資源](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)。

## 初次使用 OpenAI API

如果這是你第一次使用 OpenAI API，請參考此指南了解如何[建立與使用介面](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)。

## 認識其他學員

我們在官方的 [AI 社群 Discord 伺服器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) 建立了頻道，方便學員互相認識。這是個很棒的管道，可以與志同道合的創業者、開發者、學生及所有想在生成式 AI 領域成長的人互相交流。

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

專案團隊也會在此 Discord 伺服器幫助學員。

## 貢獻

本課程為開源計畫。如果你發現可以改進之處或問題，請建立 [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) 或提交 [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

專案團隊會追蹤所有貢獻。參與開源是進入生成式 AI 領域的絕佳途徑。

大多數貢獻需你同意簽署貢獻者授權協議 (CLA)，聲明你有權並確實授予我們使用你貢獻的權利。詳情請參閱 [CLA，貢獻者授權協議官網](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)。

重要提示：在此倉庫翻譯文字時，請確保勿使用機器翻譯。我們會透過社群驗證翻譯品質，故請只在你精通的語言中自願翻譯。


當你提交拉取請求時，CLA-bot 會自動判斷你是否需要提供 CLA，並適當地標記 PR（例如標籤、評論）。只需按照機器人提供的指示操作即可。你只需在所有使用我們 CLA 的倉庫中完成一次此操作。

此專案已採用 [Microsoft 開源行為守則](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)。欲了解更多資訊，請參閱行為守則常見問題，或聯絡 [電子郵件 opencode](opencode@microsoft.com) 提出任何其他問題或意見。

## 開始吧

現在你已完成完成本課程所需的步驟，讓我們從了解 [生成式 AI 及大型語言模型的介紹](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) 開始吧。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->