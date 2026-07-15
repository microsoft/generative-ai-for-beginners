# AGENTS.md

## 專案概覽

此儲存庫包含一套完整的 21 課課程，教授生成式 AI 的基礎知識與應用開發。課程專為初學者設計，涵蓋從基本概念到建置可投入生產的應用程式。

**主要技術：**
- Python 3.9+，使用函式庫：`openai`、`python-dotenv`、`tiktoken`、`azure-ai-inference`、`pandas`、`numpy`、`matplotlib`
- TypeScript/JavaScript，搭配 Node.js 與函式庫：`openai`（Azure OpenAI 透過 v1 endpoint + Responses API）、`@azure-rest/ai-inference`（Microsoft Foundry Models）
- Azure OpenAI 服務、OpenAI API 與 Microsoft Foundry Models（GitHub Models 將於 2026 年 7 月底退役）
- 互動式 Jupyter 筆記本
- 開發容器（Dev Containers）確保開發環境一致

**儲存庫結構：**
- 21 個編號課程目錄（00-21），包含 README、程式碼範例與作業
- 多種實作：Python、TypeScript，部分包含 .NET 範例
- 翻譯資料夾，提供 40 多種語言版本
- 中央化設定透過 `.env` 檔案管理（使用 `.env.copy` 作為範本）

## 設定指令

### 初始儲存庫設定

```bash
# 複製儲存庫
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# 複製環境範本
cp .env.copy .env
# 使用你的 API 金鑰和端點編輯 .env
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

# 對於單個課程的 TypeScript 範例，請導覽至特定課程：
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### 開發容器設定（推薦）

本儲存庫提供 `.devcontainer` 設定，適用於 GitHub Codespaces 或 VS Code Dev Containers：

1. 於 GitHub Codespaces 或已安裝 Dev Containers 擴充功能的 VS Code 開啟儲存庫
2. 開發容器將自動：
   - 從 `requirements.txt` 安裝 Python 依賴
   - 執行建立後腳本（`.devcontainer/post-create.sh`）
   - 設定 Jupyter 核心

## 開發工作流程

### 環境變數

需要 API 存取的所有課程均使用 `.env` 定義的環境變數：

- `OPENAI_API_KEY` - 用於 OpenAI API
- `AZURE_OPENAI_API_KEY` - Microsoft Foundry 中的 Azure OpenAI 金鑰（Azure OpenAI 服務現為 Microsoft Foundry 一部分：https://ai.azure.com）
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI 端點 URL（Foundry 資源端點）
- `AZURE_OPENAI_DEPLOYMENT` - 聊天完成模型部署名稱
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - 嵌入模型部署名稱
- `AZURE_OPENAI_API_VERSION` - API 版本（預設：`2024-10-21`）
- `HUGGING_FACE_API_KEY` - 用於 Hugging Face 模型
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry Models 端點（多供應者模型目錄）
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry Models API 金鑰（取代即將退役的 `GITHUB_TOKEN`）

### 執行 Python 範例

```bash
# 前往課程目錄
cd 06-text-generation-apps/python

# 執行 Python 腳本
python aoai-app.py
```

### 執行 TypeScript 範例

```bash
# 導航至 TypeScript 應用程式目錄
cd 06-text-generation-apps/typescript/recipe-app

# 編譯 TypeScript 代碼
npm run build

# 運行應用程式
npm start
```

### 執行 Jupyter 筆記本

```bash
# 在倉庫根目錄啟動 Jupyter
jupyter notebook

# 或使用帶有 Jupyter 擴展的 VS Code
```

### 處理不同課程類型

- **「學習」課程**：聚焦於 README.md 文件與概念說明
- **「建置」課程**：包含 Python 與 TypeScript 的實作程式碼範例
- 每堂課均有 README.md，涵蓋理論、程式碼解析及影片連結

## 程式碼風格指南

### Python

- 使用 `python-dotenv` 管理環境變數
- 匯入 `openai` 函式庫以呼叫 API
- 使用 `pylint` 進行程式碼檢查（部分範例包含 `# pylint: disable=all` 以簡化）
- 遵循 PEP 8 命名慣例
- 將 API 憑證存放於 `.env`，切勿硬編碼於程式碼中

### TypeScript

- 使用 `dotenv` 套件管理環境變數
- 各應用在 `tsconfig.json` 中設定 TypeScript 編譯選項
- 使用 `openai` 套件調用 Azure OpenAI（指向 `/openai/v1/` 端點並呼叫 `client.responses.create`）；Microsoft Foundry Models 使用 `@azure-rest/ai-inference`
- 開發時使用 `nodemon` 自動重載
- 執行前先建置：`npm run build`，再執行 `npm start`

### 一般慣例

- 保持程式碼範例簡潔且具教學性
- 加入註解說明重要概念
- 每個課程的程式碼應獨立且可執行
- 命名保持一致：`aoai-` 前綴表示 Azure OpenAI，`oai-` 表示 OpenAI API，`githubmodels-` 表示 Microsoft Foundry Models（保留 GitHub Models 時代的舊前綴）

## 文件指南

### Markdown 樣式

- 所有 URL 必須採用 `[text](../../url)` 格式，且無多餘空白
- 相對連結必須以 `./` 或 `../` 起頭
- 所有 Microsoft 網域連結必須包含追蹤 ID：`?WT.mc_id=academic-105485-koreyst`
- 避免 URL 中包含特定國家地區語系（勿出現 `/en-us/`）
- 圖像存放於 `./images` 資料夾並使用描述性名稱
- 檔名使用英文字符、數字與連字號

### 翻譯支援

- 儲存庫透過自動化 GitHub Actions 支援超過 40 種語言
- 翻譯版本存放於 `translations/` 資料夾
- 不接受部分翻譯提交
- 不接受機器翻譯
- 翻譯後的圖像存放於 `translated_images/` 資料夾

## 測試與驗證

### 提交前檢查

本儲存庫使用 GitHub Actions 進行驗證。提交 PR 前請：

1. **檢查 Markdown 連結**：
   ```bash
   # validate-markdown.yml 工作流程檢查：
   # - 斷開的相對路徑
   # - 路徑缺少追蹤 ID
   # - URL 缺少追蹤 ID
   # - 含有國家地區碼的 URL
   # - 斷開的外部 URL
   ```

2. <strong>手動測試</strong>：
   - 測試 Python 範例：啟動 venv 並執行腳本
   - 測試 TypeScript 範例：執行 `npm install`，`npm run build`，再 `npm start`
   - 確認環境變數設定正確
   - 確認 API 金鑰可與範例程式碼正常運作

3. <strong>程式碼範例</strong>：
   - 確認所有程式碼皆可無誤執行
   - 必要時，同時測試 Azure OpenAI 與 OpenAI API
   - 確認支援時，範例可搭配 Microsoft Foundry Models 運作

### 無自動化測試

本為教學用儲存庫，專注於教程與範例，無單元測試或整合測試。驗證主要依賴：
- 程式碼範例的人工測試
- 使用 GitHub Actions 驗證 Markdown
- 社群對教學內容的審核

## Pull Request 指南

### 提交前準備

1. 針對 Python 與 TypeScript 皆測試程式碼變更（如適用）
2. 執行 Markdown 驗證（PR 自動觸發）
3. 確認所有 Microsoft 網址包含追蹤 ID
4. 確認相對連結有效
5. 確認圖像標示正確

### PR 標題格式

- 使用描述性標題：`[Lesson 06] 修正 Python 範例錯字` 或 `更新第 08 課 README`
- 如適用，標示相關 issue 編號：`修正 #123`

### PR 說明

- 說明變更內容及原因
- 連結相關 issue
- 針對程式碼變更，指定測試過的範例
- 翻譯 PR 需包含所有檔案，確保完整翻譯

### 貢獻要求

- 簽署 Microsoft CLA（首個 PR 自動完成）
- 先 Fork 儲存庫至自身帳號再進行修改
- 一個 PR 僅包含一項邏輯變更（勿合併不相關修正）
- PR 儘量聚焦且精簡

## 常見工作流程

### 新增程式碼範例

1. 進入對應課程目錄
2. 於 `python/` 或 `typescript/` 子目錄中新增範例
3. 依命名慣例命名：`{provider}-{example-name}.{py|ts|js}`
4. 以真實 API 憑證測試
5. 在課程 README 記錄任何新增環境變數

### 文件更新

1. 編輯對應課程目錄的 README.md
2. 遵循 Markdown 指南（追蹤 ID、相對連結）
3. 翻譯由 GitHub Actions 自動處理（勿手動編輯）
4. 確認所有連結均有效

### 使用開發容器

1. 儲存庫包含 `.devcontainer/devcontainer.json`
2. 建立後腳本自動安裝 Python 依賴
3. 預先設定 Python 與 Jupyter 擴充功能
4. 環境基於 `mcr.microsoft.com/devcontainers/universal:2.11.2`

## 部署與發佈

此為學習性質的儲存庫，無部署流程。課程資源透過：

1. **GitHub 儲存庫**：直接存取程式碼與文件
2. **GitHub Codespaces**：即時且預先設定好的開發環境
3. **Microsoft Learn**：課程內容可能會同步發布至官方學習平台
4. **docsify**：由 Markdown 建立的文件網站（請參閱 `docsifytopdf.js` 及 `package.json`）

### 建置文件網站

```bash
# 從文件產生 PDF（如有需要）
npm run convert
```

## 疑難排解

### 常見問題

**Python 匯入錯誤**：
- 確認虛擬環境已啟動
- 執行 `pip install -r requirements.txt`
- 確認 Python 版本為 3.9+

**TypeScript 建置錯誤**：
- 於對應應用目錄執行 `npm install`
- 確認 Node.js 版本相容
- 如有需要，清除 `node_modules` 後重新安裝

**API 認證錯誤**：
- 確認 `.env` 檔案存在且內容正確
- 確認 API 金鑰有效且未過期
- 確認端點 URL 適用於你的區域

<strong>缺少環境變數</strong>：
- 將 `.env.copy` 複製為 `.env`
- 填寫你所作業課程所需的全部數值
- 更新 `.env` 後請重啟應用程式

## 額外資源

- [課程設定指南](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [貢獻指南](./CONTRIBUTING.md)
- [行為守則](./CODE_OF_CONDUCT.md)
- [資安政策](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [進階程式碼範例彙整](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## 專案特定說明

- 這是個<strong>教學性質的儲存庫</strong>，專注於學習，不是用於生產
- 範例故意簡單，重點是教導概念
- 程式碼品質與教學清晰度取得平衡
- 每堂課獨立，能獨立完成
- 儲存庫支援多個 API 提供者：Azure OpenAI、OpenAI、Microsoft Foundry Models，以及離線提供者如 Foundry Local 和 Ollama
- 內容多語系，搭配自動化翻譯工作流程
- Discord 上有活躍社群，提供問題解答與支援

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->