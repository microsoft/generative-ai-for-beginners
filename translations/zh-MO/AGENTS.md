# AGENTS.md

## 專案概覽

這個儲存庫包含一個全面的 21 課程綱要，教授生成式 AI 的基礎知識及應用開發。課程設計適合初學者，涵蓋從基本概念到建立可投入生產的應用程式。

**關鍵技術：**
- Python 3.9+ 與函式庫：`openai`、`python-dotenv`、`tiktoken`、`azure-ai-inference`、`pandas`、`numpy`、`matplotlib`
- TypeScript/JavaScript 搭配 Node.js 及函式庫：`openai`（透過 v1 端點及 Responses API 使用 Azure OpenAI）、`@azure-rest/ai-inference`（微軟 Foundry 模型）
- Azure OpenAI 服務、OpenAI API 與微軟 Foundry 模型（GitHub Models 將於 2026 年 7 月底退休）
- 用於互動學習的 Jupyter 筆記本
- 用於一致性開發環境的 Dev Containers

**儲存庫結構：**
- 21 個編號課程目錄（00-21），包含 README、代碼範例及作業
- 多種實作：Python、TypeScript，有時也包含 .NET 範例
- 翻譯目錄包含 40 多種語言版本
- 透過 `.env` 檔案集中管理設定（使用 `.env.copy` 作為範本）

## 設定指令

### 初始儲存庫設定

```bash
# 複製倉庫
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# 複製環境範本
cp .env.copy .env
# 編輯 .env，輸入你的 API 金鑰及端點
```

### Python 環境設定

```bash
# 建立虛擬環境
python3 -m venv venv

# 啟動虛擬環境
# 在 macOS/Linux：
source venv/bin/activate
# 在 Windows：
venv\Scripts\activate

# 安裝依賴項
pip install -r requirements.txt
```

### Node.js/TypeScript 設定

```bash
# 安裝根目錄層級的依賴項（用於文件工具）
npm install

# 對於個別課程的 TypeScript 範例，請導航至特定課程：
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container 設定（建議）

本儲存庫包含 `.devcontainer` 設定檔，可用於 GitHub Codespaces 或 VS Code Dev Containers：

1. 在 GitHub Codespaces 或安裝了 Dev Containers 擴充功能的 VS Code 中開啟儲存庫
2. Dev Container 會自動：
   - 安裝 `requirements.txt` 中的 Python 相依套件
   - 執行建立後腳本（`.devcontainer/post-create.sh`）
   - 設定 Jupyter 核心

## 開發工作流程

### 環境變數

所有需存取 API 的課程皆使用 `.env` 中定義的環境變數：

- `OPENAI_API_KEY` - 用於 OpenAI API
- `AZURE_OPENAI_API_KEY` - 用於微軟 Foundry 的 Azure OpenAI（Azure OpenAI 服務現屬於微軟 Foundry：https://ai.azure.com）
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI 端點 URL（Foundry 資源端點）
- `AZURE_OPENAI_DEPLOYMENT` - 聊天完成模型部署名稱（課程預設：`gpt-5-mini`）
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - 嵌入模型部署名稱（課程預設：`text-embedding-3-small`）
- `AZURE_OPENAI_API_VERSION` - API 版本（預設：`2024-10-21`）
- `HUGGING_FACE_API_KEY` - 用於 Hugging Face 模型
- `AZURE_INFERENCE_ENDPOINT` - 微軟 Foundry 模型端點（多供應商模型目錄）
- `AZURE_INFERENCE_CREDENTIAL` - 微軟 Foundry 模型 API 金鑰（取代即將退休的 `GITHUB_TOKEN`）
- `AZURE_INFERENCE_CHAT_MODEL` - 用於 `temperature` 範例的非推理模型（例如 `Llama-3.3-70B-Instruct`），因推理模型不支援抽樣控制

### 模型規範（重要）

- **預設聊天模型為 `gpt-5-mini`<strong> — 一款目前非棄用的 </strong>推理** 模型。2026 年起，較舊且支持 temperature 的 “mini” 模型（`gpt-4o-mini`、`gpt-4.1-mini`）將逐步淘汰，因此課程統一採用 GPT-5 系列。
- **推理模型不接受 `temperature` 與 `top_p`**，取而代之使用 `max_output_tokens`（Responses API）/ `max_completion_tokens`（聊天完成）替代 `max_tokens`。請 <strong>勿</strong> 對呼叫 `gpt-5-mini` 的範例加入 `temperature`/`top_p`/`max_tokens`。
- **為展示 `temperature`，範例使用 Llama 模型**（`Llama-3.3-70B-Instruct`），透過微軟 Foundry 模型的端點（`AZURE_INFERENCE_CHAT_MODEL`）呼叫。採用提示工程與推理控管方法引導推理模型，而非抽樣參數。
- **微調（第 18 課）維持使用 `gpt-4.1-mini`**：GPT-5 目前僅支援強化學習微調（RFT），不支援此處的監督式微調（SFT）。
- 第 20（Mistral）及第 21（Meta）課仍使用 `temperature`/`max_tokens`，因目標模型為支援該參數的 Mistral/Llama。

### 執行 Python 範例

```bash
# 導航到課程目錄
cd 06-text-generation-apps/python

# 執行一個 Python 腳本
python aoai-app.py
```

### 執行 TypeScript 範例

```bash
# 導覽至 TypeScript 應用程式目錄
cd 06-text-generation-apps/typescript/recipe-app

# 編譯 TypeScript 程式碼
npm run build

# 執行應用程式
npm start
```

### 執行 Jupyter 筆記本

```bash
# 由儲存庫根目錄啟動 Jupyter
jupyter notebook

# 或使用帶有 Jupyter 擴充功能的 VS Code
```

### 處理不同類型的課程

- **「學習」課程**：著重於 README.md 說明文件與概念
- **「建置」課程**：包含 Python 與 TypeScript 的可運作代碼範例
- 每個課程均有 README.md，包括理論、代碼導覽及影片連結

## 程式碼風格準則

### Python

- 使用 `python-dotenv` 管理環境變數
- 匯入 `openai` 函式庫進行 API 互動
- 使用 `pylint` 進行程式碼檢查（部分範例為簡潔性加上 `# pylint: disable=all`）
- 遵循 PEP 8 命名慣例
- API 憑證存於 `.env` 檔案，切勿硬編碼於程式中

### TypeScript

- 使用 `dotenv` 套件管理環境變數
- 各應用的 TypeScript 設定於 `tsconfig.json`
- 使用 `openai` 套件以呼叫 Azure OpenAI（指向 `/openai/v1/` 端點並呼叫 `client.responses.create`）；使用 `@azure-rest/ai-inference` 以調用微軟 Foundry 模型
- 使用 `nodemon` 進行開發，具自動重載功能
- 執行前先編譯：`npm run build`，接著啟動：`npm start`

### 一般慣例

- 保持範例代碼簡單，聚焦教學
- 加入註解解釋關鍵概念
- 每個單元的程式碼皆應獨立完整且可執行
- 命名保持一致：Azure OpenAI 使用 `aoai-` 為前綴，OpenAI API 使用 `oai-`，微軟 Foundry 模型使用 `githubmodels-`（沿用 GitHub Models 時代的舊前綴）

## 文件準則

### Markdown 風格

- 所有網址需以 `[文字](../../網址)` 格式包裹，且不得有多餘空格
- 相對連結必須以 `./` 或 `../` 開頭
- 所有指向 Microsoft 領域的連結必須包括追蹤 ID：`?WT.mc_id=academic-105485-koreyst`
- 避免網址中出現特定國家語系（避免 `/en-us/`）
- 圖片儲存在 `./images` 資料夾，檔名需具描述性
- 檔名使用英文字母、數字與連字號

### 翻譯支援

- 儲存庫透過自動化 GitHub Actions 支援 40 多種語言
- 翻譯內容存於 `translations/` 目錄
- 不接受部分翻譯提交
- 不接受機器翻譯
- 翻譯後的圖片存於 `translated_images/` 目錄

## 測試與驗證

### 提交前檢查

此儲存庫利用 GitHub Actions 進行驗證。提交 PR 前：

1. **檢查 Markdown 連結**：
   ```bash
   # validate-markdown.yml 工作流程檢查：
   # - 損壞的相對路徑
   # - 路徑中缺失的追蹤 ID
   # - URL 中缺失的追蹤 ID
   # - 含有國家地區代碼的 URL
   # - 損壞的外部 URL
   ```

2. <strong>手動測試</strong>：
   - 測試 Python 範例：啟動 venv 並執行腳本
   - 測試 TypeScript 範例：執行 `npm install`、`npm run build`、`npm start`
   - 確認環境變數設定正確
   - 測試 API 金鑰能於範例中正常使用

3. <strong>程式碼範例</strong>：
   - 確保所有代碼皆能無錯執行
   - 具支援時，同時測試 Azure OpenAI 與 OpenAI API
   - 確認與支持的 Microsoft Foundry 模型範例能正常運作

### 無自動化測試

這是一個教育性質的儲存庫，專注於教程與範例。無單元測試或整合測試執行。驗證主要依靠：
- 手動測試程式碼範例
- GitHub Actions 進行 Markdown 驗證
- 社區對教育內容的審查

## Pull Request 指南

### 提交前

1. 於有關 Python 與 TypeScript 的修改均進行測試
2. 執行 Markdown 驗證（PR 自動觸發）
3. 確保所有微軟網址包含追蹤 ID
4. 檢查相對連結有效性
5. 確認圖片引用正確

### PR 標題格式

- 使用具描述性的標題：`[Lesson 06] 修正 Python 範例錯字` 或 `更新第 08 課 README`
- 適用時參考議題號碼：`Fixes #123`

### PR 說明

- 說明變更內容與原因
- 連結相關議題
- 就程式碼變更指定已測試的範例
- 翻譯 PR 請附上完整檔案以完成翻譯

### 貢獻需求

- 需簽署微軟 CLA（首次 PR 自動完成）
- 在進行修改前，先將儲存庫分支到個人帳戶
- 每次 PR 聚焦於一項邏輯變更（避免混合不相關修改）
- 儘量保持 PR 精簡集中

## 常見工作流程

### 新增程式碼範例

1. 前往相應課程目錄
2. 在 `python/` 或 `typescript/` 子目錄中建立範例
3. 遵循命名規則：`{provider}-{example-name}.{py|ts|js}`
4. 使用真實 API 憑證測試
5. 在課程 README 文件中記錄新增的環境變數

### 更新文件

1. 編輯課程目錄內的 README.md
2. 遵循 Markdown 指南（追蹤 ID、相對連結）
3. 翻譯由 GitHub Actions 自動處理（勿手動編輯）
4. 測試所有連結有效

### 使用 Dev Containers

1. 儲存庫含 `.devcontainer/devcontainer.json`
2. 建立後腳本自動安裝 Python 依賴
3. 預先設定 Python 與 Jupyter 擴充功能
4. 環境基於 `mcr.microsoft.com/devcontainers/universal:2.11.2`

## 部署與發佈

本儲存庫為學習用，無部署流程。課程使用方式包含：

1. **GitHub 儲存庫**：直接存取程式碼與文件
2. **GitHub Codespaces**：即時開發環境與預設定置
3. **Microsoft Learn**：內容可能經由官方學習平台發佈
4. **docsify**：利用 Markdown 編譯成文件網站（參見 `docsifytopdf.js` 與 `package.json`）

### 編譯文件網站

```bash
# 從文件生成 PDF（如有需要）
npm run convert
```

## 疑難排解

### 常見問題

**Python 匯入錯誤**：
- 確認已啟用虛擬環境
- 執行 `pip install -r requirements.txt`
- 檢查 Python 版本是否為 3.9 以上

**TypeScript 編譯錯誤**：
- 在特定應用目錄執行 `npm install`
- 確認 Node.js 版本相容
- 若需要，刪除 `node_modules` 並重新安裝

**API 認證錯誤**：
- 確認 `.env` 檔案存在且數值正確
- 檢查 API 金鑰有效且未過期
- 確認端點 URL 符合您所在區域

<strong>缺少環境變數</strong>：
- 將 `.env.copy` 複製為 `.env`
- 填寫您工作課程需要的所有值
- 更新 `.env` 後重新啟動應用程式

## 額外資源

- [課程設定指南](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [貢獻指南](./CONTRIBUTING.md)
- [行為準則](./CODE_OF_CONDUCT.md)
- [安全政策](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [進階代碼範例彙整](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## 專案特定說明

- 本儲存庫為<strong>教育性質</strong>，專注學習，不是生產代碼
- 範例特意保持簡單，聚焦在教學概念
- 代碼品質與教學清晰度保持平衡
- 各課程獨立完整，可獨立完成
- 儲存庫支援多種 API 供應商：Azure OpenAI、OpenAI、微軟 Foundry 模型，以及離線供應商如 Foundry Local 和 Ollama
- 內容多語言支持，自動化翻譯工作流
- 活躍社區於 Discord，提供問題與支援

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->