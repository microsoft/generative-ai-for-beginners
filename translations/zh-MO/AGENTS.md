# AGENTS.md

## 專案概述

此儲存庫包含完整的 21 課課程，教授生成式 AI 的基礎與應用開發。該課程專為初學者設計，覆蓋從基本概念到建置可投入生產的應用程式。

**主要技術：**
- Python 3.9+ 並使用函式庫：`openai`、`python-dotenv`、`tiktoken`、`azure-ai-inference`、`pandas`、`numpy`、`matplotlib`
- TypeScript/JavaScript 使用 Node.js 及函式庫：`openai`（透過 v1 端點 + 回應 API 使用 Azure OpenAI）、`@azure-rest/ai-inference`（Microsoft Foundry 模型）
- Azure OpenAI 服務、OpenAI API 及 Microsoft Foundry 模型（GitHub Models 將於 2026 年 7 月底退休）
- 使用 Jupyter Notebooks 進行互動式學習
- Dev Containers 提供一致的開發環境

**儲存庫結構：**
- 21 個編號課程目錄（00-21），內含 README、程式碼範例及作業
- 多種實作：Python、TypeScript，有時包含 .NET 範例
- 翻譯目錄涵蓋 40 多種語言版本
- 統一配置透過 `.env` 檔案（可使用 `.env.copy` 作為範本）

## 安裝指令

### 儲存庫初次設定

```bash
# 複製儲存庫
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# 複製環境範本
cp .env.copy .env
# 用你的 API 金鑰和端點編輯 .env
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

### Node.js/TypeScript 環境設定

```bash
# 安裝根目錄層級的依賴（用於文件工具）
npm install

# 若針對單一課程的 TypeScript 範例，請導航至該特定課程：
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container 設定（推薦）

儲存庫包含 `.devcontainer` 設定檔，適用於 GitHub Codespaces 或 VS Code Dev Containers：

1. 於 GitHub Codespaces 或 VS Code（有 Dev Containers 擴充功能）中開啟儲存庫
2. Dev Container 將自動執行：
   - 從 `requirements.txt` 安裝 Python 依賴
   - 執行 post-create 腳本（`.devcontainer/post-create.sh`）
   - 設定 Jupyter kernel

## 開發流程

### 環境變數

所有需使用 API 的課程皆透過 `.env` 中定義的環境變數：

- `OPENAI_API_KEY` - 用於 OpenAI API
- `AZURE_OPENAI_API_KEY` - 用於 Microsoft Foundry 中的 Azure OpenAI（Azure OpenAI 服務現為 Microsoft Foundry 一部分：https://ai.azure.com）
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI 端點 URL（Foundry 資源端點）
- `AZURE_OPENAI_DEPLOYMENT` - 聊天完成模型部署名稱
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - 向量嵌入模型部署名稱
- `AZURE_OPENAI_API_VERSION` - API 版本（預設：`2024-10-21`）
- `HUGGING_FACE_API_KEY` - 用於 Hugging Face 模型
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry 模型端點（多供應商模型目錄）
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry 模型 API 金鑰（取代即將退役的 `GITHUB_TOKEN`）

### 執行 Python 範例

```bash
# 導航到課程目錄
cd 06-text-generation-apps/python

# 執行 Python 腳本
python aoai-app.py
```

### 執行 TypeScript 範例

```bash
# 導航到 TypeScript 應用程式目錄
cd 06-text-generation-apps/typescript/recipe-app

# 編譯 TypeScript 程式碼
npm run build

# 執行應用程式
npm start
```

### 執行 Jupyter Notebooks

```bash
# 喺儲存庫根目錄啟動 Jupyter
jupyter notebook

# 或者用帶 Jupyter 擴展嘅 VS Code
```

### 處理不同類型的課程

- **「學習」課程**：專注於 README.md 文檔及概念
- **「建構」課程**：包含 Python 及 TypeScript 的運行範例
- 每個課程都有 README.md，涵蓋理論、代碼導覽與影片連結

## 代碼風格準則

### Python

- 使用 `python-dotenv` 管理環境變數
- 引入 `openai` 函式庫以呼叫 API
- 使用 `pylint` 偵錯（部分範例為簡化，包含 `# pylint: disable=all`）
- 遵循 PEP 8 命名慣例
- API 憑證儲存在 `.env` 檔案，絕不放入程式碼中

### TypeScript

- 使用 `dotenv` 套件管理環境變數
- 各應用的 TypeScript 設定在 `tsconfig.json`
- 使用 `openai` 套件調用 Azure OpenAI（客戶端指向 `/openai/v1/` 端點，呼叫 `client.responses.create`）；使用 `@azure-rest/ai-inference` 呼叫 Microsoft Foundry 模型
- 開發時使用 `nodemon` 自動重載
- 執行前先編譯：`npm run build`，接著 `npm start`

### 通用慣例

- 保持範例程式簡潔且具教學性
- 含註解說明重點概念
- 每課程的程式碼應自包含且能執行
- 命名一致：Azure OpenAI 須以 `aoai-` 為前綴，OpenAI API 以 `oai-`，Microsoft Foundry 模型（從 GitHub Models 時代延續）以 `githubmodels-`

## 文件撰寫指引

### Markdown 格式

- 所有網址必須以 `[text](../../url)` 格式包裹，且中間不留空格
- 相對連結必須以 `./` 或 `../` 開頭
- 所有指向 Microsoft 領域的連結必須包含追蹤 ID：`?WT.mc_id=academic-105485-koreyst`
- 網址中不使用國家特定語系路徑（避免 `/en-us/`）
- 圖片存放於 `./images` 資料夾，名稱需描述性
- 檔案名稱使用英文字母、數字和短橫線

### 翻譯支援

- 儲存庫支援透過自動化 GitHub Actions 產生 40 多種語言版本
- 翻譯檔存放於 `translations/` 目錄
- 不接受部分翻譯提交
- 不接受機器翻譯
- 翻譯後的圖片存放於 `translated_images/` 目錄

## 測試與驗證

### 提交前檢查

此儲存庫使用 GitHub Actions 進行驗證。提交 PR 前：

1. **檢查 Markdown 連結**：
   ```bash
   # validate-markdown.yml 工作流程檢查：
   # - 斷裂的相對路徑
   # - 路徑上缺少追蹤 ID
   # - URL 上缺少追蹤 ID
   # - 包含國家地區代碼的 URL
   # - 斷裂的外部 URL
   ```

2. <strong>手動測試</strong>：
   - 測試 Python 範例：啟動 venv 並執行腳本
   - 測試 TypeScript 範例：`npm install`、`npm run build`、`npm start`
   - 確認環境變數配置正確
   - 確認 API 金鑰能運作於程式碼範例

3. <strong>程式碼範例</strong>：
   - 確保所有程式碼能無錯誤執行
   - 支援時同時測試 Azure OpenAI 及 OpenAI API
   - 確認範例支援 Microsoft Foundry 模型時正常運作

### 無自動化測試

此為教學儲存庫，重點在教學與範例，無單元測試或整合測試。驗證主要依賴：
- 手動測試程式碼範例
- GitHub Actions 驗證 Markdown 格式
- 社群審核教學內容

## 取回請求指引

### 提交前注意事項

1. 針對 Python 和 TypeScript 進行程式碼變更測試（如適用）
2. 執行 Markdown 驗證（PR 自動觸發）
3. 確認所有 Microsoft 網址含追蹤 ID
4. 檢查相對連結有效
5. 確認圖片引用正確

### PR 標題格式

- 使用具描述性的標題，例如 `[Lesson 06] 修正 Python 範例錯字` 或 `更新第08課 README`
- 有關議題請標明修正關聯號碼，例如 `Fixes #123`

### PR 說明

- 說明更動內容及原因
- 提供相關議題連結
- 針對程式碼更動，說明測試範例
- 針對翻譯 PR，需包含完整翻譯檔案

### 貢獻條件

- 簽署 Microsoft CLA（首次 PR 自動完成）
- 複製儲存庫至個人帳號後進行更改
- 一個 PR 一項邏輯變更（避免合併無關修正）
- 盡量保持 PR 專注且簡潔

## 常見工作流程

### 新增程式碼範例

1. 前往相應課程目錄
2. 於 `python/` 或 `typescript/` 子目錄新建範例
3. 遵守命名規則：`{provider}-{example-name}.{py|ts|js}`
4. 使用真實 API 憑證測試
5. 於課程 README 中記錄任何新增的環境變數

### 更新文件

1. 編輯課程目錄中的 README.md
2. 遵循 Markdown 規範（追蹤 ID、相對連結）
3. 翻譯由 GitHub Actions 自動處理（請勿手動修改）
4. 確認所有連結有效

### 使用 Dev Containers

1. 儲存庫包含 `.devcontainer/devcontainer.json`
2. post-create 腳本會自動安裝 Python 依賴
3. 已預配置 Python 與 Jupyter 擴充功能
4. 環境基於 `mcr.microsoft.com/devcontainers/universal:2.11.2`

## 部署與發布

這是學習用的儲存庫，無部署流程。課程內容透過以下方式使用：

1. **GitHub 儲存庫**：直接存取程式碼與文件
2. **GitHub Codespaces**：立即開啟預配置的開發環境
3. **Microsoft Learn**：課程可能同步至官方學習平台
4. **docsify**：從 Markdown 建立的文件站點（參見 `docsifytopdf.js` 與 `package.json`）

### 建置文件站點

```bash
# 從文件生成 PDF（如有需要）
npm run convert
```

## 疑難排解

### 常見問題

**Python 匯入錯誤**：
- 確認虛擬環境已啟動
- 執行 `pip install -r requirements.txt`
- 檢查 Python 版本需為 3.9 以上

**TypeScript 編譯錯誤**：
- 在該應用目錄執行 `npm install`
- 確認 Node.js 版本相容
- 如有需要，清除 `node_modules` 後重新安裝

**API 認證錯誤**：
- 確認 `.env` 檔案存在且值正確
- 檢查 API 金鑰有效且未過期
- 確認端點 URL 符合所屬地區

<strong>缺少環境變數</strong>：
- 複製 `.env.copy` 為 `.env`
- 填寫該課需要的所有欄位
- 更新 `.env` 後重新啟動應用程式

## 附加資源

- [課程設定指南](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [貢獻指引](./CONTRIBUTING.md)
- [行為守則](./CODE_OF_CONDUCT.md)
- [安全政策](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [進階程式碼範例集](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## 專案專屬說明

- 這是一個<strong>教育用途儲存庫</strong>，側重學習，非生產程式碼
- 範例有意簡化，專注於教學概念
- 代碼品質與教學清晰度兼顧
- 每課獨立且可獨立完成
- 支援多個 API 供應商：Azure OpenAI、OpenAI、Microsoft Foundry 模型，以及離線供應商如 Foundry Local、Ollama
- 內容多語言，並有自動翻譯工作流程
- Discord 社群活躍，提供問題與支援服務

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->