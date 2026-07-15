# 強化功能與改進路線圖

本文件列出基於全面代碼審查及行業最佳實踐分析，對新手生成式 AI 課程推薦的增強和改進方案。

## 執行摘要

代碼庫已就安全性、代碼質量及教育效果進行分析。本文提供立即修復、近期改進及未來增強建議。

---

## 1. 安全性增強（優先級：關鍵）

### 1.1 立即修復（已完成）

| 問題 | 影響檔案 | 狀態 |
|-------|----------------|--------|
| 硬編碼 SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | 已修正 |
| 缺少環境變數驗證 | 多個 JS/TS 檔案 | 已修正 |
| 不安全的函數調用 | `11-integrating-with-function-calling/js-githubmodels/app.js` | 已修正 |
| 檔案句柄洩露 | `08-building-search-applications/scripts/` | 已修正 |
| 缺少請求超時 | `09-building-image-applications/python/` | 已修正 |

### 1.2 推薦額外安全功能

1. <strong>速率限制範例</strong>
   - 新增示範如何對 API 調用實現速率限制的範例代碼
   - 展示指數退避模式

2. **API 密鑰輪替**
   - 新增有關 API 密鑰輪替最佳實踐的文件
   - 包含使用 Azure Key Vault 或類似服務的範例

3. <strong>內容安全整合</strong>
   - 新增使用 Azure Content Safety API 的範例
   - 示範輸入/輸出審查模式

---

## 2. 代碼質量提升

### 2.1 新增配置檔案

| 檔案 | 目的 |
|------|---------|
| `.eslintrc.json` | JavaScript/TypeScript 代碼檢查規則 |
| `.prettierrc` | 代碼格式化標準 |
| `pyproject.toml` | Python 工具設定（Black、Ruff、mypy） |

### 2.2 新增共用工具

新增 `shared/python/` 模組，包含：
- `env_utils.py` - 環境變數處理
- `input_validation.py` - 輸入驗證與消毒
- `api_utils.py` - 安全 API 請求包裝器

### 2.3 推薦代碼改進

1. <strong>型別提示覆蓋</strong>
   - 補充所有 Python 檔案的型別提示
   - 啟用所有 TS 項目中的嚴格型別模式

2. <strong>文件標準</strong>
   - 為所有 Python 函數添加文檔字符串
   - 為所有 JavaScript/TypeScript 函數添加 JSDoc 注釋

3. <strong>測試框架</strong>
   - 添加 pytest 配置及範例測試 _(已完成：`pyproject.toml` 中含 pytest 配置；CI 中執行 [`tests/`](../../../tests) 的共用工具範例測試)_
   - 添加 JavaScript/TypeScript 的 Jest 配置

---

## 3. 教育性增強

### 3.1 新課程主題

1. **AI 應用中的安全性**（建議第 22 課）
   - 提示注入攻擊與防禦
   - API 密鑰管理
   - 內容審查
   - 速率限制與濫用防範

2. <strong>生產部署</strong>（建議第 23 課）
   - 使用 Docker 容器化
   - CI/CD 管道
   - 監控與日誌
   - 成本管理

3. **進階 RAG 技術**（建議第 24 課）
   - 混合搜索（關鍵字 + 語義）
   - 重排策略
   - 多模態 RAG
   - 評估指標

### 3.2 現有課程改進

| 課程 | 推薦改進 |
|--------|------------------------|
| 06 - 文字生成 | 新增串流式響應範例 |
| 07 - 聊天應用 | 新增對話記憶模式 |
| 08 - 搜索應用 | 新增向量資料庫比較 |
| 09 - 影像生成 | 新增圖片編輯/變化範例 |
| 11 - 函數呼叫 | 新增平行函數呼叫 |
| 15 - RAG | 新增分塊策略比較 |
| 17 - AI 代理 | 新增多代理協調 |

---

## 4. API 現代化

### 4.1 棄用 API 模式（遷移完成）

所有 Python 與 TypeScript 的 <strong>聊天</strong> 範例已從 Chat Completions API 遷移到 **Responses API**（`client.responses.create(...)` → `response.output_text`）。

| 舊模式 | 新模式 | 狀態 |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()`（聊天） | `OpenAI(base_url="<endpoint>/openai/v1/")`（Responses API） | 已完成 |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | 已完成 |
| `@azure/openai` `OpenAIClient.getChatCompletions()`（TypeScript） | `openai` 套件 `client.responses.create()` → `response.output_text` | 已完成 |
| `df.append()` (pandas) | `pd.concat()` | 已完成 |

> **注意：** 使用 `azure-ai-inference` / `@azure-rest/ai-inference` SDK（`client.complete()`）的 Microsoft Foundry Models 範例仍使用模型推斷 API，該 API 不支持 Responses API。`AzureOpenAI()` 仍在可用的情況下保留（用於 embedding 及影像生成）。

### 4.2 新 API 功能示範

1. <strong>結構化輸出</strong>（OpenAI）
   - JSON 模式
   - 帶嚴格 schema 的函數調用

2. <strong>視覺功能</strong>
   - 使用 GPT-4o（視覺）的圖片分析
   - 多模態提示

3. **Responses API 內建工具**（取代舊 Assistants API）
   - 代碼解釋器
   - 文件搜索
   - 網頁搜索與自訂工具

---

## 5. 基礎設施改進

### 5.1 CI/CD 增強

已實作於 [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml)：Python 代碼檢查/格式化（Ruff + Black）於維護中的 `shared/` 工具模組採強制執行，課程其餘部分則為建議性，且針對 JavaScript/TypeScript 執行 ESLint 建議性檢查。示範基準為：

```yaml
# .github/workflows/code-quality.yml
name: Code Quality

on: [push, pull_request]

jobs:
  python-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - run: pip install ruff black mypy
      - run: ruff check .
      - run: black --check .

  js-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npx eslint .
```

### 5.2 安全掃描

已實作於 [`.github/workflows/security.yml`](../../../.github/workflows/security.yml)：Python 及 JavaScript/TypeScript 的 CodeQL 分析（觸發於 push、pull request 與每週排程），此外於 pull request 執行相依性審查。示範基準為：

```yaml
# .github/workflows/security.yml
name: Security Scan

on: [push, pull_request]

jobs:
  codeql:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v3
        with:
          languages: javascript, python
      - uses: github/codeql-action/analyze@v3

  dependency-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/dependency-review-action@v4
```

---

## 6. 開發體驗改進

### 6.1 DevContainer 增強

已實作於 [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) 與 [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh)：容器現在內置 Pylance、Black 格式化工具、Ruff、ESLint、Prettier 及 Copilot 擴充功能，啟用保存時格式化並連結到 repo 的 Black/Prettier 設定，且安裝開發工具（`ruff`、`black`、`mypy`、`pytest`），使 [code-quality workflow](../../../.github/workflows/code-quality.yml) 可於本地重現。基底映像使用 `mcr.microsoft.com/devcontainers/universal`，已內含 Python 和 Node，不需額外功能。示範基準為：

```json
{
  "name": "Generative AI for Beginners",
  "image": "mcr.microsoft.com/devcontainers/universal:2",
  "features": {
    "ghcr.io/devcontainers/features/python:1": {
      "version": "3.11"
    },
    "ghcr.io/devcontainers/features/node:1": {
      "version": "20"
    }
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-toolsai.jupyter",
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "github.copilot"
      ],
      "settings": {
        "python.formatting.provider": "black",
        "editor.formatOnSave": true
      }
    }
  },
  "postCreateCommand": "pip install -e .[dev] && npm install"
}
```

### 6.2 互動式遊樂場

考慮新增：
- 帶預置 API 密鑰（透過環境變數）的 Jupyter 筆記本
- 適合視覺學習者的 Gradio/Streamlit 示範
- 用於知識評估的互動式測驗

---

## 7. 多語言支援

### 7.1 目前語言涵蓋

| 技術 | 涵蓋課程 | 狀態 |
|------------|-----------------|--------|
| Python | 全部 | 完整 |
| TypeScript | 06-09, 11 | 部分 |
| JavaScript | 06-08, 11 | 部分 |
| .NET/C# | 部分 | 部分 |

### 7.2 推薦新增語言

1. **Go** - AI/ML 工具快速成長中
2. **Rust** - 性能區域關鍵應用
3. **Java/Kotlin** - 企業應用

---

## 8. 性能優化

### 8.1 代碼層級優化

1. **非同步/等待模式**
   - 新增批次處理的非同步範例
   - 展示併發 API 呼叫

2. <strong>快取策略</strong>
   - 新增 embedding 快取範例
   - 展示回應快取模式

3. **Token 優化**
   - 添加 tiktoken 使用範例
   - 展示提示壓縮技術

### 8.2 成本優化範例

新增示範：
- 根據任務複雜度選擇模型
- 提示工程以提升 token 效率
- 批量處理實現批量操作

---

## 9. 可及性與國際化

### 9.1 當前翻譯狀態

所有翻譯均【完整】由 [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) 自動生成，該工具保持 50 多種語言版本的課程與英語版同步。翻譯內容放置於 `translations/`，本地化圖片位於 `translated_images/`；完整可用語言列表發佈於資料庫 README 頂部。

| 方面 | 狀態 |
|--------|--------|
| 翻譯覆蓋率 | 完整 — 50 多種語言，所有課程 |
| 翻譯方式 | 透過 [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) 自動化 |
| 與英文原稿保持同步 | 是 — 自動重生成 |

### 9.2 可及性改進

1. 所有圖片添加替代文字
2. 確保程式碼範例具有適當語法高亮
3. 全部影片內容添加字幕稿
4. 確保色彩對比符合 WCAG 指引

---

## 10. 實施優先次序

### 第一階段：立即（第 1-2 週）
- [x] 修復關鍵安全問題
- [x] 新增代碼質量配置
- [x] 建立共用工具
- [x] 文件化安全指引

### 第二階段：短期（第 3-4 週）
- [x] 更新棄用 API 模式（聊天完成 → Responses API，Python + TypeScript）
- [ ] 為所有 Python 檔案添加型別提示（維護中的 `shared/` 模組已完成；課程範例保持簡單）
- [x] 新增 CI/CD 工作流程以保證代碼質量
- [x] 創建安全掃描工作流程

### 第三階段：中期（第 2-3 個月）
- [ ] 新增安全相關課程
- [ ] 新增生產部署課程
- [x] 優化 DevContainer 設置
- [ ] 新增互動示範

### 第四階段：長期（第 4 個月以上）
- [ ] 新增進階 RAG 課程
- [ ] 擴充語言涵蓋範圍
- [ ] 增建全面測試套件
- [ ] 建立認證計劃

---

## 結論

本路線圖提供系統化方案以優化新手生成式 AI 課程。透過解決安全問題、更新 API 並增補教學內容，課程將更好裝備學員應對實務 AI 應用開發。

如有問題或欲作出貢獻，請於 GitHub 資料庫開啟 Issue。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->