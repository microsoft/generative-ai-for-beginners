# AGENTS.md

## 專案概覽

此儲存庫包含一個完整的 21 課程綱要，教授生成式 AI 的基礎與應用開發。該課程針對初學者設計，涵蓋從基本概念到建立可投入生產的應用程式。

**主要技術：**
- Python 3.9+ 和相關函式庫：`openai`、`python-dotenv`、`tiktoken`、`azure-ai-inference`、`pandas`、`numpy`、`matplotlib`
- TypeScript/JavaScript 搭配 Node.js 及函式庫：`openai`（透過 v1 endpoint 呼叫 Azure OpenAI + Responses API）、`@azure-rest/ai-inference`（Microsoft Foundry Models）
- Azure OpenAI 服務、OpenAI API 及 Microsoft Foundry Models（GitHub Models 將於 2026 年 7 月底退役）
- Jupyter 筆記本用於互動學習
- Dev Containers 用於一致的開發環境

**儲存庫結構：**
- 21 個編號課程目錄（00–21），包含 README、程式碼範例及作業
- 多種實現：Python、TypeScript，有時候也有 .NET 範例
- 翻譯目錄含超過 40 種語言版本
- 透過 `.env` 檔案集中配置（使用 `.env.copy` 作為範本）

## 設定指令

### 初次儲存庫設定

```bash
# 複製儲存庫
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# 複製環境範本
cp .env.copy .env
# 使用你的 API 金鑰及端點編輯 .env
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
# 安裝 root 級別的依賴（用於文件工具）
npm install

# 對於個別課程的 TypeScript 範例，請導航到特定課程：
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container 設定（建議）

此儲存庫包含 `.devcontainer` 設定，可於 GitHub Codespaces 或 VS Code Dev Containers 使用：

1. 在 GitHub Codespaces 或安裝 Dev Containers 擴充功能的 VS Code 開啟儲存庫
2. Dev Container 將自動：
   - 從 `requirements.txt` 安裝 Python 相依套件
   - 執行 post-create 腳本（`.devcontainer/post-create.sh`）
   - 設定 Jupyter kernel

## 開發流程

### 環境變數

所有需 API 存取的課程都使用 `.env` 定義的環境變數：

- `OPENAI_API_KEY` - OpenAI API 金鑰
- `AZURE_OPENAI_API_KEY` - Microsoft Foundry 中 Azure OpenAI 的金鑰（Azure OpenAI 服務現為 Microsoft Foundry 的一部分：https://ai.azure.com）
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI 服務端點 URL（Foundry 資源端點）
- `AZURE_OPENAI_DEPLOYMENT` - 聊天完成模型部署名稱（課程預設：`gpt-5-mini`）
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Embeddings 模型部署名稱（課程預設：`text-embedding-3-small`）
- `AZURE_OPENAI_API_VERSION` - API 版本（預設：`2024-10-21`）
- `HUGGING_FACE_API_KEY` - Hugging Face 模型的金鑰
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry Models 端點（多供應者模型目錄）
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry Models API 金鑰（取代即將退役的 `GITHUB_TOKEN`）
- `AZURE_INFERENCE_CHAT_MODEL` - 非推理模型（例如 `Llama-3.3-70B-Instruct`），用於 `temperature` 範例，因推理模型不支援采樣控制

### 模型慣例（重要）

- **預設聊天模型為 `gpt-5-mini`<strong> — 一款目前非棄用的</strong>推理**模型。2026年起，舊的支持 temperature 的 "mini" 模型（`gpt-4o-mini`、`gpt-4.1-mini`）逐步棄用，課程統一採用 GPT-5 系列。
- **推理模型不接受 `temperature` 和 `top_p`**，並使用 `max_output_tokens`（Responses API）/ `max_completion_tokens`（聊天完成）取代 `max_tokens`。呼叫 `gpt-5-mini` 時，不要添加 `temperature`/`top_p`/`max_tokens`。
- **示範 `temperature` 時<strong>，範例使用 Microsoft Foundry Models 端點的 </strong>Llama** 模型（`Llama-3.3-70B-Instruct`，透過 `AZURE_INFERENCE_CHAT_MODEL`）。推理模型則以提示工程和推理控制代替采樣旋鈕。
- **微調（第 18 課）** 仍保留`gpt-4.1-mini`：GPT-5 僅支援強化微調（RFT），不支援該課程中的監督微調（SFT）。
- 第 20 課（Mistral）和第 21 課（Meta）保留 `temperature`/`max_tokens`，因以 Mistral/Llama 模型為目標，支援這些參數。

### 執行 Python 範例

```bash
# 導航到課程目錄
cd 06-text-generation-apps/python

# 執行一個 Python 腳本
python aoai-app.py
```

### 執行 TypeScript 範例

```bash
# 進入 TypeScript 應用目錄
cd 06-text-generation-apps/typescript/recipe-app

# 編譯 TypeScript 程式碼
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

### 不同課程類型的作業方式

- **「學習」課程**：專注於 README.md 文件與概念
- **「建置」課程**：包含 Python 和 TypeScript 的運作中程式碼範例
- 每個課程都有 README.md，內含理論、程式碼解說及影片連結

## 程式碼風格指引

### Python

- 使用 `python-dotenv` 管理環境變數
- 匯入 `openai` 函式庫進行 API 互動
- 使用 `pylint` 做程式碼檢查（部分範例使用 `# pylint: disable=all` 簡化）
- 遵守 PEP 8 命名慣例
- 將 API 認證資訊存放 `.env` 檔案，絕不硬寫於程式碼中

### TypeScript

- 使用 `dotenv` 套件管理環境變數
- 在每個應用程式中使用 `tsconfig.json` 配置 TypeScript
- 使用 `openai` 套件呼叫 Azure OpenAI（指向 `/openai/v1/` endpoint，並呼叫 `client.responses.create`）；使用 `@azure-rest/ai-inference` 呼叫 Microsoft Foundry Models
- 使用 `nodemon` 進行開發時自動重新載入
- 執行前先編譯：`npm run build`，然後 `npm start`

### 一般慣例

- 使程式碼範例保持簡單且具教育性
- 加入關鍵概念的註解說明
- 每課程的程式碼應自包含且可執行
- 命名要統一：Azure OpenAI 使用 `aoai-` 前綴，OpenAI API 使用 `oai-`，Microsoft Foundry Models 使用 `githubmodels-`（保留 GitHub Models 時代的舊前綴）

## 文件撰寫準則

### Markdown 風格

- 所有 URL 必須採用 `[text](../../url)` 格式且無多餘空格
- 相對連結必須以 `./` 或 `../` 開頭
- 所有指向 Microsoft 領域的連結必須包含追蹤 ID：`?WT.mc_id=academic-105485-koreyst`
- URL 中不可包含特定國家語系（避免 `/en-us/`）
- 圖片存放於 `./images` 資料夾，名稱需具描述性
- 使用英文字母、數字和連字號做檔名

### 翻譯支援

- 儲存庫支援超過 40 種語言，由 GitHub Actions 自動化處理
- 翻譯檔放置於 `translations/` 目錄
- 不接受部分翻譯提交
- 不接受機器翻譯稿
- 翻譯的圖片存放於 `translated_images/` 目錄

## 測試與驗證

### 提交前檢查

此儲存庫使用 GitHub Actions 進行驗證。提交 PR 前請：

1. **檢查 Markdown 連結**：
   ```bash
   # validate-markdown.yml 工作流程會檢查：
   # - 損壞的相對路徑
   # - 路徑缺少追蹤 ID
   # - URL 缺少追蹤 ID
   # - 帶有國家地區設定的 URL
   # - 損壞的外部 URL
   ```

2. <strong>手動測試</strong>：
   - 測試 Python 範例：啟動 venv 並執行腳本
   - 測試 TypeScript 範例：`npm install`、`npm run build`、`npm start`
   - 確認環境變數設定正確
   - 檢查 API 金鑰與範例程式碼可正常搭配

3. <strong>程式碼範例</strong>：
   - 確保程式碼可無錯誤執行
   - 適用時測試 Azure OpenAI 與 OpenAI API
   - 支援時測試 Microsoft Foundry Models 範例

### 無自動測試

這是一個教育用儲存庫，專注於教學與範例。沒有單元測試或整合測試。驗證主要方式為：
- 手動測試程式碼範例
- GitHub Actions 做 Markdown 驗證
- 社群審核教學內容

## 拉取請求準則

### 提交前

1. 測試有改動的 Python 與 TypeScript 程式碼（適用時）
2. 執行 Markdown 驗證（PR 自動觸發）
3. 確保所有 Microsoft URL 含追蹤 ID
4. 確認相對連結有效
5. 確認圖像引用正確

### PR 標題格式

- 使用描述性標題：[Lesson 06] 修正 Python 範例錯字 或 更新第 08 課 README
- 適用時引用相關 Issue 號碼：Fixes #123

### PR 描述

- 說明修改內容與原因
- 連結相關 Issue
- 程式碼修改須註明測試過的範例
- 翻譯 PR 請包含完整翻譯檔案

### 貢獻須知

- 簽署 Microsoft CLA（首個 PR 自動）
- 先 fork 儲存庫至個人帳號後再更改
- 一次 PR 僅限一項邏輯修改（勿混合無關修正）
- PR 儘量聚焦且小規模

## 常見流程

### 新增程式碼範例

1. 前往對應課程資料夾
2. 在 `python/` 或 `typescript/` 子目錄新增範例
3. 遵循命名規則：`{provider}-{example-name}.{py|ts|js}`
4. 以實際 API 金鑰測試
5. 在課程 README 中記錄新增環境變數

### 更新文件

1. 編輯課程資料夾中的 README.md
2. 遵守 Markdown 指南（含追蹤 ID 和相對連結）
3. 翻譯由 GitHub Actions 處理（勿手動編輯）
4. 測試確保所有連結有效

### 使用 Dev Containers

1. 儲存庫包含 `.devcontainer/devcontainer.json`
2. post-create 腳本自動安裝 Python 相依套件
3. 預設安裝 Python 和 Jupyter 擴充功能
4. 環境基於 `mcr.microsoft.com/devcontainers/universal:2.11.2`

## 部署與發佈

這是學習用儲存庫，無部署流程。課程透過以下方式使用：

1. **GitHub 儲存庫**：直接存取程式碼與文件
2. **GitHub Codespaces**：即時開發環境，預設配置
3. **Microsoft Learn**：內容可能會同步發佈於官方學習平台
4. **docsify**：以 Markdown 建構的文件網站（參見 `docsifytopdf.js` 和 `package.json`）

### 建置文件網站

```bash
# 從文件生成 PDF（如有需要）
npm run convert
```

## 疑難排解

### 常見問題

**Python 匯入錯誤**：
- 確認已啟動虛擬環境
- 執行 `pip install -r requirements.txt`
- 確認 Python 版本為 3.9+

**TypeScript 編譯錯誤**：
- 在特定應用程式目錄執行 `npm install`
- 確認 Node.js 版本相容
- 如有需要清除 `node_modules` 並重新安裝

**API 認證錯誤**：
- 確認 `.env` 檔存在且值正確
- 檢查 API 金鑰有效且未過期
- 確認端點 URL 適合你的區域

<strong>缺少環境變數</strong>：
- 複製 `.env.copy` 為 `.env`
- 填寫你正在作業課程所需的所有值
- 更新 `.env` 後重新啟動應用程式

## 其他資源

- [課程設定指南](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [貢獻指南](./CONTRIBUTING.md)
- [行為守則](./CODE_OF_CONDUCT.md)
- [安全政策](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [進階程式碼範例集](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## 專案專屬說明

- 這是<strong>教育用儲存庫</strong>，專注於學習而非生產程式碼
- 範例刻意設計簡潔，聚焦教學概念
- 程式碼品質在教學清晰度中取得平衡
- 每課程自包含，能獨立完成
- 儲存庫支援多種 API 供應商：Azure OpenAI、OpenAI、Microsoft Foundry Models 及離線供應商如 Foundry Local 和 Ollama
- 內容多語言化並有自動翻譯工作流程
- Discord 社群活躍，提供問答與支援

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->