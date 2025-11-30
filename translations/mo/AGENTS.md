<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T10:53:54+00:00",
  "source_file": "AGENTS.md",
  "language_code": "mo"
}
-->
# AGENTS.md

## 專案概述

此存儲庫包含一套完整的21課課程，教授生成式人工智慧的基礎知識及應用開發。課程專為初學者設計，涵蓋從基本概念到建立生產級應用的所有內容。

**主要技術：**
- Python 3.9+，使用以下庫：`openai`、`python-dotenv`、`tiktoken`、`azure-ai-inference`、`pandas`、`numpy`、`matplotlib`
- TypeScript/JavaScript，使用 Node.js 和以下庫：`@azure/openai`、`@azure-rest/ai-inference`、`openai`
- Azure OpenAI Service、OpenAI API 和 GitHub Models
- Jupyter Notebooks 用於互動式學習
- Dev Containers 提供一致的開發環境

**存儲庫結構：**
- 21個編號的課程目錄（00-21），包含README文件、程式碼範例和作業
- 多種實現方式：Python、TypeScript，有時還包括 .NET 範例
- 翻譯目錄，支持40多種語言版本
- 通過 `.env` 文件集中配置（使用 `.env.copy` 作為模板）

## 設置指令

### 初始存儲庫設置

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Python 環境設置

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Node.js/TypeScript 設置

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container 設置（推薦）

存儲庫包含 `.devcontainer` 配置文件，可用於 GitHub Codespaces 或 VS Code Dev Containers：

1. 在 GitHub Codespaces 或 VS Code 中打開存儲庫，並使用 Dev Containers 擴展
2. Dev Container 將自動執行以下操作：
   - 從 `requirements.txt` 安裝 Python 依賴項
   - 執行 post-create 腳本（`.devcontainer/post-create.sh`）
   - 設置 Jupyter kernel

## 開發工作流程

### 環境變數

所有需要 API 訪問的課程都使用 `.env` 中定義的環境變數：

- `OPENAI_API_KEY` - 用於 OpenAI API
- `AZURE_OPENAI_API_KEY` - 用於 Azure OpenAI Service
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI 端點 URL
- `AZURE_OPENAI_DEPLOYMENT` - 聊天完成模型的部署名稱
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - 嵌入模型的部署名稱
- `AZURE_OPENAI_API_VERSION` - API 版本（默認：`2024-02-01`）
- `HUGGING_FACE_API_KEY` - 用於 Hugging Face 模型
- `GITHUB_TOKEN` - 用於 GitHub Models

### 執行 Python 範例

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### 執行 TypeScript 範例

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### 執行 Jupyter Notebooks

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### 處理不同類型的課程

- **「學習」課程**：專注於 README.md 文件中的文檔和概念
- **「構建」課程**：包含 Python 和 TypeScript 的工作程式碼範例
- 每個課程都有 README.md 文件，提供理論、程式碼講解和視頻內容的鏈接

## 程式碼風格指南

### Python

- 使用 `python-dotenv` 管理環境變數
- 導入 `openai` 庫進行 API 交互
- 使用 `pylint` 進行程式碼檢查（某些範例包含 `# pylint: disable=all` 以簡化）
- 遵循 PEP 8 命名規範
- 將 API 憑證存儲在 `.env` 文件中，切勿直接寫入程式碼

### TypeScript

- 使用 `dotenv` 套件管理環境變數
- 每個應用的 TypeScript 配置存儲在 `tsconfig.json` 中
- 使用 `@azure/openai` 或 `@azure-rest/ai-inference` 進行 Azure 服務交互
- 使用 `nodemon` 進行開發，支持自動重載
- 執行前需先編譯：`npm run build` 然後 `npm start`

### 通用規範

- 保持程式碼範例簡單且具有教育性
- 包含解釋關鍵概念的註解
- 每個課程的程式碼應該是自包含且可執行的
- 使用一致的命名方式：`aoai-` 前綴表示 Azure OpenAI，`oai-` 表示 OpenAI API，`githubmodels-` 表示 GitHub Models

## 文檔指南

### Markdown 風格

- 所有 URL 必須使用 `[文字](../../url)` 格式包裹，且無多餘空格
- 相對鏈接必須以 `./` 或 `../` 開頭
- 所有指向 Microsoft 域的鏈接必須包含追蹤 ID：`?WT.mc_id=academic-105485-koreyst`
- URL 中不得包含國家/地區特定的語言代碼（避免 `/en-us/`）
- 圖片存儲在 `./images` 文件夾中，文件名需具描述性
- 文件名使用英文字母、數字和連字符

### 翻譯支持

- 存儲庫通過 GitHub Actions 支持40多種語言
- 翻譯存儲在 `translations/` 目錄中
- 不接受部分翻譯
- 不接受機器翻譯
- 翻譯後的圖片存儲在 `translated_images/` 目錄中

## 測試與驗證

### 提交前檢查

此存儲庫使用 GitHub Actions 進行驗證。在提交 PR 之前：

1. **檢查 Markdown 鏈接**：
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **手動測試**：
   - 測試 Python 範例：啟動虛擬環境並運行腳本
   - 測試 TypeScript 範例：`npm install`，`npm run build`，`npm start`
   - 確保環境變數配置正確
   - 檢查 API 密鑰是否與程式碼範例匹配

3. **程式碼範例**：
   - 確保所有程式碼無錯誤運行
   - 在適用時測試 Azure OpenAI 和 OpenAI API
   - 驗證範例是否支持 GitHub Models

### 無自動化測試

這是一個以教程和範例為重點的教育存儲庫，沒有單元測試或集成測試。驗證主要包括：
- 手動測試程式碼範例
- GitHub Actions 用於 Markdown 驗證
- 社群審核教育內容

## Pull Request 指南

### 提交前

1. 在適用時測試 Python 和 TypeScript 的程式碼更改
2. 運行 Markdown 驗證（PR 提交時自動觸發）
3. 確保所有 Microsoft URL 包含追蹤 ID
4. 檢查相對鏈接是否有效
5. 確保圖片引用正確

### PR 標題格式

- 使用描述性標題：`[Lesson 06] 修正 Python 範例錯誤` 或 `更新第08課的 README`
- 在適用時引用問題編號：`Fixes #123`

### PR 描述

- 解釋更改內容及原因
- 鏈接相關問題
- 對於程式碼更改，說明測試了哪些範例
- 對於翻譯 PR，包含所有文件以完成翻譯

### 貢獻要求

- 簽署 Microsoft CLA（首次提交 PR 時自動完成）
- 在進行更改之前，將存儲庫分叉到您的帳戶
- 每個邏輯更改提交一個 PR（不要合併不相關的修復）
- 儘量保持 PR 集中且小型化

## 常見工作流程

### 添加新程式碼範例

1. 導航到相應的課程目錄
2. 在 `python/` 或 `typescript/` 子目錄中創建範例
3. 遵循命名規範：`{provider}-{example-name}.{py|ts|js}`
4. 使用實際 API 憑證進行測試
5. 在課程 README 中記錄任何新環境變數

### 更新文檔

1. 編輯課程目錄中的 README.md
2. 遵循 Markdown 指南（追蹤 ID、相對鏈接）
3. 翻譯由 GitHub Actions 處理（不要手動編輯）
4. 測試所有鏈接是否有效

### 使用 Dev Containers

1. 存儲庫包含 `.devcontainer/devcontainer.json`
2. Post-create 腳本自動安裝 Python 依賴項
3. 預先配置 Python 和 Jupyter 擴展
4. 環境基於 `mcr.microsoft.com/devcontainers/universal:2.11.2`

## 部署與發布

這是一個學習存儲庫，沒有部署流程。課程內容的使用方式包括：

1. **GitHub 存儲庫**：直接訪問程式碼和文檔
2. **GitHub Codespaces**：即時開發環境，預先配置設置
3. **Microsoft Learn**：內容可能會同步到官方學習平台
4. **docsify**：基於 Markdown 的文檔網站（參見 `docsifytopdf.js` 和 `package.json`）

### 建立文檔網站

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## 疑難排解

### 常見問題

**Python 導入錯誤**：
- 確保虛擬環境已啟動
- 運行 `pip install -r requirements.txt`
- 檢查 Python 版本是否為 3.9+

**TypeScript 編譯錯誤**：
- 在特定應用目錄中運行 `npm install`
- 檢查 Node.js 版本是否兼容
- 清除 `node_modules` 並重新安裝

**API 身份驗證錯誤**：
- 確認 `.env` 文件存在且值正確
- 檢查 API 密鑰是否有效且未過期
- 確保端點 URL 與您的地區匹配

**缺少環境變數**：
- 將 `.env.copy` 複製為 `.env`
- 填寫您正在處理的課程所需的所有值
- 更新 `.env` 後重新啟動應用

## 其他資源

- [課程設置指南](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [貢獻指南](./CONTRIBUTING.md)
- [行為準則](./CODE_OF_CONDUCT.md)
- [安全政策](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [高級程式碼範例集合](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## 專案特定注意事項

- 這是一個**教育存儲庫**，重點在於學習，而非生產程式碼
- 範例故意簡化，專注於教授概念
- 程式碼品質在教育清晰度和實用性之間取得平衡
- 每個課程都是自包含的，可獨立完成
- 存儲庫支持多個 API 提供者：Azure OpenAI、OpenAI 和 GitHub Models
- 內容支持多語言，並具有自動翻譯工作流程
- Discord 社群活躍，可用於提問和支持

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解釋不承擔責任。