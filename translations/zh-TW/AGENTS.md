# AGENTS.md

## 專案概覽

本儲存庫包含一個完整的21課程綱要，教導生成式 AI 的基礎和應用開發。此課程專為初學者設計，涵蓋從基礎概念到建立可投入生產的應用程式。

**核心技術：**
- Python 3.9+，搭配以下套件：`openai`、`python-dotenv`、`tiktoken`、`azure-ai-inference`、`pandas`、`numpy`、`matplotlib`
- TypeScript/JavaScript，搭配 Node.js 及套件：`openai`（Azure OpenAI 透過 v1 端點和 Responses API）、`@azure-rest/ai-inference`（Microsoft Foundry 模型）
- Azure OpenAI 服務、OpenAI API 與 Microsoft Foundry 模型（GitHub Models 將於2026年7月底停用）
- 使用 Jupyter 筆記本進行互動式學習
- 使用開發容器以保持一致的開發環境

**儲存庫結構：**
- 21 個按序號命名的課程目錄（00-21），包含 README、程式碼範例和作業
- 多種實作版本：Python、TypeScript，有時也有 .NET 範例
- translations 目錄中有 40 多種語言版本
- 統一使用 `.env` 檔案做設定管理（可使用 `.env.copy` 作為範本）

## 設定指令

### 儲存庫初次設定

```bash
# 複製倉庫
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# 複製環境範本
cp .env.copy .env
# 編輯 .env，加入您的 API 金鑰和端點
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

# 安裝相依套件
pip install -r requirements.txt
```

### Node.js/TypeScript 環境設定

```bash
# 安裝根目錄層級的相依套件（用於文件工具）
npm install

# 若要使用各課程的 TypeScript 範例，請切換到特定課程目錄：
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### 開發容器設定（推薦）

本儲存庫提供 `.devcontainer` 設定，適用於 GitHub Codespaces 或 VS Code 的開發容器：

1. 在 GitHub Codespaces 或安裝了 Dev Containers 擴充功能的 VS Code 中開啟儲存庫
2. 開發容器會自動：
   - 從 `requirements.txt` 安裝 Python 依賴套件
   - 執行 post-create 腳本（`.devcontainer/post-create.sh`）
   - 設定 Jupyter 核心

## 開發流程

### 環境變數

所有需要 API 訪問的課程均使用 `.env` 檔案定義的環境變數：

- `OPENAI_API_KEY` - OpenAI API 金鑰
- `AZURE_OPENAI_API_KEY` - 用於 Microsoft Foundry 的 Azure OpenAI（金鑰）（Azure OpenAI 服務現為 Microsoft Foundry 一部分：https://ai.azure.com）
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI 端點 URL（Foundry 資源端點）
- `AZURE_OPENAI_DEPLOYMENT` - 聊天完成模型部署名稱（課程預設：`gpt-5-mini`）
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - 向量嵌入模型部署名稱（課程預設：`text-embedding-3-small`）
- `AZURE_OPENAI_API_VERSION` - API 版本（預設：`2024-10-21`）
- `HUGGING_FACE_API_KEY` - Hugging Face 模型金鑰
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry 模型端點（多供應商模型目錄）
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry 模型 API 金鑰（取代即將停用的 `GITHUB_TOKEN`）
- `AZURE_INFERENCE_CHAT_MODEL` - 一個非推理模型（例如 `Llama-3.3-70B-Instruct`），用於 `temperature` 範例，因為推理模型不支援抽樣控制參數

### 模型慣例（重要）

- **預設聊天模型為 `gpt-5-mini`<strong> — 目前非棄用的</strong>推理**模型。自2026年起，舊有支援溫度參數的「mini」模型（`gpt-4o-mini`、`gpt-4.1-mini`）正在<em>退役中</em>，本課程標準化採用 GPT-5 系列。
- **推理模型會拒絕 `temperature` 和 `top_p`**，並改用 `max_output_tokens`（Responses API）/`max_completion_tokens`（聊天完成）來代替 `max_tokens`。請勿在呼叫 `gpt-5-mini` 的範例中加入 `temperature`/`top_p`/`max_tokens`。
- **為展示 `temperature`**，範例使用一個 **Llama** 模型（`Llama-3.3-70B-Instruct`），透過 Microsoft Foundry Models 端點（`AZURE_INFERENCE_CHAT_MODEL`）。推理模型請用提示工程和推理控制來引導，而非使用抽樣調節參數。
- **微調（第18課）** 仍使用 `gpt-4.1-mini`：GPT-5 僅支援強化微調（RFT），不支援此處示範的監督式微調（SFT）。
- 第20課（Mistral）和第21課（Meta）則保留 `temperature` 和 `max_tokens`，因為它們針對支援這些參數的 Mistral/Llama 模型。

### 執行 Python 範例

```bash
# 導覽到課程目錄
cd 06-text-generation-apps/python

# 執行 Python 腳本
python aoai-app.py
```

### 執行 TypeScript 範例

```bash
# 導覽至 TypeScript 應用程式目錄
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

### 處理不同類型課程

- **「學習」課程**：著重 README.md 文檔和概念
- **「實作」課程**：包含 Python 和 TypeScript 的工作範例程式碼
- 每課皆有 README.md，說明理論、程式碼導覽及影片連結

## 程式碼風格指南

### Python

- 使用 `python-dotenv` 管理環境變數
- 匯入 `openai` 套件以進行 API 互動
- 使用 `pylint` 進行程式碼檢查（部分範例為簡便起見使用 `# pylint: disable=all`）
- 遵守 PEP 8 命名慣例
- API 憑證存放於 `.env` 檔案，絕不於程式碼中硬編

### TypeScript

- 使用 `dotenv` 套件管理環境變數
- 各應用的 TypeScript 配置存於 `tsconfig.json`
- 使用 `openai` 套件調用 Azure OpenAI（客戶端指向 `/openai/v1/` 端點並呼叫 `client.responses.create`）；使用 `@azure-rest/ai-inference` 呼叫 Microsoft Foundry 模型
- 使用 `nodemon` 進行自動重載開發
- 執行前請先 build：`npm run build`，再 `npm start`

### 通用慣例

- 保持範例程式碼簡潔且具教育意圖
- 添加註解說明重要概念
- 各課程程式碼為獨立且可執行的單元
- 命名保持一致：Azure OpenAI 使用`aoai-`前綴，OpenAI API使用`oai-`，Microsoft Foundry 模型使用`githubmodels-`（此為 GitHub Models 時期遺留前綴）

## 文件撰寫指南

### Markdown 風格

- 所有網址必須使用 `[text](../../url)` 格式，且無多餘空白
- 相對連結必須以 `./` 或 `../` 開頭
- 所有微軟網域連結必須附帶追蹤 ID：`?WT.mc_id=academic-105485-koreyst`
- 避免使用帶有國家地區碼的網址（如 `/en-us/`）
- 圖片存放於 `./images` 資料夾，檔名需具描述性
- 請使用英文字符、數字與連字符命名檔案

### 翻譯支援

- 儲存庫透過自動化 GitHub Actions 支援 40 多種語言
- 翻譯結果存放於 `translations/` 目錄
- 不接受部分翻譯提交
- 不接受機器翻譯結果
- 翻譯後的圖片存於 `translated_images/` 目錄

## 測試與驗證

### 提交前檢查

本儲存庫使用 GitHub Actions 進行驗證。提交 PR 前請：

1. **檢查 Markdown 連結**：
   ```bash
   # validate-markdown.yml 工作流程檢查：
   # - 斷裂的相對路徑
   # - 路徑中遺失追蹤ID
   # - URL中遺失追蹤ID
   # - 含有國家區域設定的URL
   # - 斷裂的外部URL
   ```

2. <strong>手動測試</strong>：
   - 測試 Python 範例：啟用虛擬環境並執行腳本
   - 測試 TypeScript 範例：執行 `npm install`、`npm run build`、`npm start`
   - 確保環境變數設定正確
   - 確認 API 金鑰可正常運作範例程式

3. <strong>程式碼範例</strong>：
   - 確保所有程式碼運行無誤
   - 在適用情況下同時測試 Azure OpenAI 及 OpenAI API
   - 確認範例與支援的 Microsoft Foundry 模型兼容

### 無自動化測試

本儲存庫為教學導向，著重教程與範例，無單元測試或整合測試。驗證主要依賴：
- 範例程式的手動測試
- GitHub Actions 的 Markdown 驗證
- 社群的教育內容審查

## 拉取請求規範

### 提交前

1. 針對 Python 與 TypeScript 進行程式碼測試（如適用）
2. 執行 Markdown 驗證（PR 建立時自動觸發）
3. 確保所有微軟網址包含追蹤 ID
4. 檢查相對連結有效性
5. 確認圖片正確引用

### PR 標題格式

- 使用說明性標題：`[Lesson 06] 修正 Python 範例錯字` 或 `更新第08課 README`
- 適用時引用議題號碼：`Fixes #123`

### PR 說明

- 說明變更內容及原因
- 連結相關議題
- 程式碼變更時說明測試過哪些範例
- 翻譯 PR 必須包含整套文件

### 貢獻條件

- 簽署 Microsoft CLA（首次 PR 自動執行）
- Fork 儲存庫至個人帳號後再進行更改
- 每個 PR 只提交一項邏輯變更（勿合併不相關修正）
- PR 盡量保持聚焦且輕量

## 常見工作流程

### 新增程式碼範例

1. 前往對應的課程資料夾
2. 在 `python/` 或 `typescript/` 子目錄創建範例
3. 遵循命名規則：`{provider}-{example-name}.{py|ts|js}`
4. 使用實際 API 憑證測試
5. 在課程 README 記錄新增的環境變數

### 更新文件

1. 編輯課程目錄下的 README.md
2. 遵守 Markdown 指南（包含追蹤 ID、相對連結）
3. 翻譯更新由 GitHub Actions 自動處理（勿手動修改）
4. 測試所有連結有效性

### 使用開發容器

1. 儲存庫含 `.devcontainer/devcontainer.json`
2. post-create 腳本會自動安裝 Python 依賴
3. 預先設定 Python 和 Jupyter 擴充功能
4. 開發環境基於 `mcr.microsoft.com/devcontainers/universal:2.11.2`

## 部署與發佈

本儲存庫為教學用途，無部署流程。課程內容透過以下管道提供：

1. **GitHub 儲存庫**：直接存取程式碼與文件
2. **GitHub Codespaces**：即時開發環境，預先配置
3. **Microsoft Learn**：內容可能會同步至官方學習平台
4. **docsify**：從 Markdown 建置的文件網站（參見 `docsifytopdf.js` 和 `package.json`）

### 文件網站建置

```bash
# 從文件生成 PDF（如有需要）
npm run convert
```

## 疑難排解

### 常見問題

**Python 匯入錯誤**：
- 確認虛擬環境已啟用
- 執行 `pip install -r requirements.txt`
- 檢查 Python 版本為 3.9+

**TypeScript 建置錯誤**：
- 在特定應用目錄執行 `npm install`
- 確認 Node.js 版本相容
- 清除 `node_modules` 並重新安裝（如有需要）

**API 認證錯誤**：
- 確認 `.env` 檔案存在且內容正確
- 檢查 API 金鑰有效且未過期
- 確保端點網址對應您的區域

<strong>缺少環境變數</strong>：
- 將 `.env.copy` 複製為 `.env`
- 填寫您所進行的課程所需變數
- 更新 `.env` 後請重啟應用程式

## 其他資源

- [課程設定指南](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [貢獻指南](./CONTRIBUTING.md)
- [行為準則](./CODE_OF_CONDUCT.md)
- [安全政策](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [高階程式碼範例集](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## 專案特定說明

- 本專案為 <strong>教育儲存庫</strong>，專注於學習，非生產用程式碼
- 範例故意保持簡單，著重於教學概念
- 程式碼品質在教育清晰度與可讀性間取得平衡
- 各課程為自足單元，可獨立完成
- 本儲存庫支援多個 API 供應商：Azure OpenAI、OpenAI、Microsoft Foundry 模型，以及離線供應商如 Foundry Local 與 Ollama
- 內容多語言，搭配自動翻譯工作流程
- Discord 社群活躍，提供問題諮詢與支援

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->