# AGENTS.md

## 專案概覽

本儲存庫包含完整的 21 課程綱要，教授生成式 AI 基礎及應用開發。此課程為初學者設計，涵蓋從基礎概念到構建可用於生產的應用程式。

**主要技術：**
- Python 3.9+ 與以下函式庫：`openai`、`python-dotenv`、`tiktoken`、`azure-ai-inference`、`pandas`、`numpy`、`matplotlib`
- TypeScript/JavaScript 搭配 Node.js 及函式庫：`openai`（Azure OpenAI 透過 v1 端點 + Responses API）、`@azure-rest/ai-inference`（Microsoft Foundry 模型）
- Azure OpenAI 服務、OpenAI API 及 Microsoft Foundry 模型（GitHub 模型將於 2026 年 7 月底退休）
- 互動式 Jupyter 筆記本
- 開發容器以維持一致的開發環境

**儲存庫結構：**
- 21 個以編號分隔的課程目錄（00-21），包含 README、程式碼範例與作業
- 多種實作：Python、TypeScript 與有時候的 .NET 範例
- 翻譯目錄包含超過 40 種語言版本
- 透過 `.env` 檔案進行集中化設定（參考 `.env.copy` 範本）

## 設定指令

### 初始儲存庫設定

```bash
# 複製資料庫
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# 複製環境範本
cp .env.copy .env
# 使用您的 API 密鑰和端點編輯 .env
```

### Python 環境設定

```bash
# 建立虛擬環境
python3 -m venv venv

# 啟動虛擬環境
# 在 macOS/Linux 上：
source venv/bin/activate
# 在 Windows 上：
venv\Scripts\activate

# 安裝依賴項
pip install -r requirements.txt
```

### Node.js/TypeScript 設定

```bash
# 安裝根目錄層級的依賴（用於文件工具）
npm install

# 對於單獨課程的 TypeScript 範例，請進入特定課程目錄：
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### 開發容器設定（建議）

此儲存庫包含 `.devcontainer` 設定，可用於 GitHub Codespaces 或 VS Code 開發容器：

1. 在 GitHub Codespaces 或裝有開發容器擴充套件的 VS Code 中開啟儲存庫
2. 開發容器會自動執行：
   - 從 `requirements.txt` 安裝 Python 相依性
   - 執行 post-create 腳本（`.devcontainer/post-create.sh`）
   - 設定 Jupyter 核心

## 開發工作流程

### 環境變數

需要 API 存取的所有課程使用定義在 `.env` 中的環境變數：

- `OPENAI_API_KEY` - 用於 OpenAI API
- `AZURE_OPENAI_API_KEY` - 用於 Microsoft Foundry 中的 Azure OpenAI（Azure OpenAI 服務現為 Microsoft Foundry 一部分：https://ai.azure.com）
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI 端點網址（Foundry 資源端點）
- `AZURE_OPENAI_DEPLOYMENT` - 聊天完成模型部署名稱
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - 嵌入模型部署名稱
- `AZURE_OPENAI_API_VERSION` - API 版本（預設：`2024-10-21`）
- `HUGGING_FACE_API_KEY` - 用於 Hugging Face 模型
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry 模型端點（多供應商模型目錄）
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry 模型 API 金鑰（取代即將退休的 `GITHUB_TOKEN`）

### 執行 Python 範例

```bash
# 導航至課程目錄
cd 06-text-generation-apps/python

# 執行 Python 腳本
python aoai-app.py
```

### 執行 TypeScript 範例

```bash
# 導航到 TypeScript 應用程式目錄
cd 06-text-generation-apps/typescript/recipe-app

# 建置 TypeScript 程式碼
npm run build

# 執行應用程式
npm start
```

### 執行 Jupyter 筆記本

```bash
# 在儲存庫根目錄啟動 Jupyter
jupyter notebook

# 或使用帶有 Jupyter 擴充功能的 VS Code
```

### 處理不同課程類型

- **「學習」課程**：聚焦於 README.md 文檔與概念
- **「實作」課程**：包含 Python 與 TypeScript 的可執行程式範例
- 每個課程皆有包含理論、程式碼導覽及影片連結的 README.md

## 程式碼風格指引

### Python

- 使用 `python-dotenv` 管理環境變數
- 匯入 `openai` 函式庫與 API 互動
- 使用 `pylint` 做語法檢查（部分範例含 `# pylint: disable=all` 以簡化示範）
- 遵循 PEP 8 命名慣例
- API 憑證存放於 `.env` 檔案中，切勿寫死於程式碼

### TypeScript

- 使用 `dotenv` 套件管理環境變數
- 在每個應用程式中使用 `tsconfig.json` 進行 TypeScript 設定
- 對 Azure OpenAI 使用 `openai` 套件（將客戶端指向 `/openai/v1/` 端點並呼叫 `client.responses.create`）；使用 `@azure-rest/ai-inference` 來操作 Microsoft Foundry 模型
- 使用 `nodemon` 進行開發自動重載
- 執行前先 build：`npm run build`，再 `npm start`

### 一般慣例

- 程式範例保持簡潔並具教育意義
- 包含說明關鍵概念的註解
- 各課程程式碼內容應獨立且可直接執行
- 命名一貫性：Azure OpenAI 使用 `aoai-` 作為前綴，OpenAI API 使用 `oai-`，Microsoft Foundry 模型使用 `githubmodels-`（保留自 GitHub Models 時期的舊前綴）

## 文件指引

### Markdown 風格

- 所有 URL 必須使用 `[text](../../url)` 格式，且不得有多餘空白
- 相對連結必須以 `./` 或 `../` 起始
- 所有指向 Microsoft 領域的連結必須包含追蹤 ID：`?WT.mc_id=academic-105485-koreyst`
- URL 中不得出現國家地區特定的語系路徑（避免 `/en-us/`）
- 圖片存放於 `./images` 資料夾，檔名具描述性
- 檔名使用英文字母、數字及連字號

### 翻譯支援

- 儲存庫透過自動化的 GitHub Actions 支援 40 多種語言
- 翻譯內容存放於 `translations/` 目錄
- 不得提交不完整的翻譯
- 不接受機器翻譯
- 翻譯後的圖片存放於 `translated_images/` 目錄

## 測試與驗證

### 提交前檢查

此儲存庫使用 GitHub Actions 進行驗證。提交拉取請求（PR）前：

1. **檢查 Markdown 連結**：
   ```bash
   # validate-markdown.yml 工作流程檢查：
   # - 斷開的相對路徑
   # - 路徑缺少追蹤 ID
   # - URL 缺少追蹤 ID
   # - 含有國家地區設定的 URL
   # - 斷開的外部 URL
   ```

2. <strong>手動測試</strong>：
   - 測試 Python 範例：啟動虛擬環境並執行腳本
   - 測試 TypeScript 範例：`npm install`，`npm run build`，`npm start`
   - 確認環境變數設定正確
   - 驗證 API 金鑰是否可與範例程式正常配合

3. <strong>程式碼範例</strong>：
   - 確保所有程式碼無錯誤執行
   - 依適用情況，使用 Azure OpenAI 與 OpenAI API 進行測試
   - 支援的話，確認範例可與 Microsoft Foundry 模型正常運作

### 無自動化測試

本為教學型儲存庫，主軸在於教學及範例示範，無須執行單元測試或整合測試。驗證方式主要為：
- 程式碼範例的手動測試
- GitHub Actions 的 Markdown 驗證
- 社群對教育內容的審核

## 拉取請求指南

### 提交前事項

1. 針對 Python 與 TypeScript 皆進行程式碼變更測試（視情況）
2. 執行 Markdown 驗證（PR 時自動觸發）
3. 確保所有 Microsoft 網址含追蹤 ID
4. 檢查相對連結有效
5. 確認圖片引用正確

### PR 標題格式

- 使用描述性標題：`[Lesson 06] 修正 Python 範例錯字` 或 `更新第 08 課 README`
- 適用時引用 issue 編號：`Fixes #123`

### PR 描述

- 說明變更內容及原因
- 連結相關問題
- 對程式碼變更，指明測試過的範例
- 對翻譯 PR，包含所有檔案以完成整體翻譯

### 貢獻必要條件

- 簽署 Microsoft CLA（首次 PR 自動）
- 變更前先從原儲存庫 fork 至自己的帳號
- 一個 PR 僅包含一項邏輯變更（避免混合不相關修正）
- 盡量保持 PR 聚焦且小型

## 常用工作流程

### 新增程式碼範例

1. 前往對應課程目錄
2. 在 `python/` 或 `typescript/` 子目錄建立範例
3. 遵循命名慣例：`{provider}-{example-name}.{py|ts|js}`
4. 使用實際 API 憑證測試
5. 在課程 README 中說明任何新增的環境變數

### 更新文件

1. 編輯課程資料夾內的 README.md
2. 遵守 Markdown 指引（追蹤 ID、相對連結）
3. 翻譯更新由 GitHub Actions 處理（請勿手動編輯）
4. 測試所有連結有效

### 使用開發容器

1. 儲存庫包含 `.devcontainer/devcontainer.json`
2. post-create 腳本自動安裝 Python 相依性
3. 預先設定 Python 與 Jupyter 擴充套件
4. 環境基於 `mcr.microsoft.com/devcontainers/universal:2.11.2`

## 部署與發佈

此為學習型儲存庫，無部署流程。課程內容透過以下管道使用：

1. **GitHub 儲存庫**：直接存取程式碼與文件
2. **GitHub Codespaces**：預先設定好環境的即時開發環境
3. **Microsoft Learn**：內容可能會同步至官方學習平台
4. **docsify**：以 Markdown 生成的文件網站（參見 `docsifytopdf.js` 與 `package.json`）

### 建置文件網站

```bash
# 從文件產生 PDF（如果需要）
npm run convert
```

## 疑難排解

### 常見問題

**Python 匯入錯誤**：
- 確認虛擬環境已啟動
- 執行 `pip install -r requirements.txt`
- 確認 Python 版本 3.9 以上

**TypeScript 編譯錯誤**：
- 在特定應用程式目錄執行 `npm install`
- 確認 Node.js 版本相容
- 必要時刪除 `node_modules` 並重新安裝

**API 認證錯誤**：
- 確認 `.env` 檔案存在且值正確
- 確認 API 金鑰有效且未過期
- 確認端點 URL 與您的區域相符

<strong>缺少環境變數</strong>：
- 複製 `.env.copy` 為 `.env`
- 補齊所屬課程所需的所有值
- 更新 `.env` 後重啟應用程式

## 額外資源

- [課程設定指南](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [貢獻指南](./CONTRIBUTING.md)
- [行為守則](./CODE_OF_CONDUCT.md)
- [安全政策](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [進階程式碼範例彙整](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## 專案特定說明

- 本為以學習為主的 <strong>教育型儲存庫</strong>，非生產環境程式碼
- 範例刻意簡化，以聚焦教學概念
- 程式碼品質與教學清晰度兼顧
- 每課程獨立且可自行完成
- 支援多個 API 供應商：Azure OpenAI、OpenAI、Microsoft Foundry 模型，以及離線供應商如 Foundry Local 和 Ollama
- 內容為多語言，並有自動翻譯工作流程
- 於 Discord 社群活躍，提供問答與支援

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->