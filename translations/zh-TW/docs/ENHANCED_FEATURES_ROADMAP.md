# 增強功能與改進路線圖

本文件概述了根據全面的程式碼審查與產業最佳實踐分析，對《生成式 AI 初學者》課程建議的增強和改進措施。

## 執行摘要

程式碼庫已針對安全性、程式碼品質及教育成效進行分析。本文檔提供立即修復、近期改進及未來增強的建議。

---

## 1. 安全性強化（優先級：關鍵）

### 1.1 立即修復（已完成）

| 問題 | 影響檔案 | 狀態 |
|-------|----------------|--------|
| 硬編碼的 SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | 已修復 |
| 缺少環境變數驗證 | 多個 JS/TS 文件 | 已修復 |
| 不安全函式呼叫 | `11-integrating-with-function-calling/js-githubmodels/app.js` | 已修復 |
| 檔案控制器洩漏 | `08-building-search-applications/scripts/` | 已修復 |
| 缺少請求超時 | `09-building-image-applications/python/` | 已修復 |

### 1.2 推薦的額外安全功能

1. <strong>速率限制範例</strong>
   - 增加範例程式碼示範如何對 API 呼叫實施速率限制
   - 展示指數退避模式

2. **API 金鑰輪替**
   - 新增有關 API 金鑰輪替的最佳實踐文件
   - 包含使用 Azure Key Vault 或類似服務的範例

3. <strong>內容安全整合</strong>
   - 加入使用 Azure Content Safety API 的範例
   - 展示輸入/輸出內容審查模式

---

## 2. 程式碼品質改進

### 2.1 新增設定檔

| 檔案 | 目的 |
|------|---------|
| `.eslintrc.json` | JavaScript/TypeScript 程式碼檢查規則 |
| `.prettierrc` | 程式碼格式標準 |
| `pyproject.toml` | Python 工具配置（Black、Ruff、mypy） |

### 2.2 創建共享工具

新增 `shared/python/` 模組，包含：
- `env_utils.py` - 環境變數處理
- `input_validation.py` - 輸入驗證與淨化
- `api_utils.py` - 安全的 API 請求封裝

### 2.3 推薦的程式碼改進

1. <strong>類型註解覆蓋率</strong>
   - 為所有 Python 文件添加類型註解
   - 在所有 TS 專案中啟用嚴格 TypeScript 模式

2. <strong>文件標準</strong>
   - 為所有 Python 函數增加 docstring
   - 為所有 JavaScript/TypeScript 函數添加 JSDoc 註解

3. <strong>測試框架</strong>
   - 新增 pytest 配置與示例測試 _(完成：`pyproject.toml` 中的 pytest 配置；在 CI 中運行的共享工具示例測試位於 [`tests/`](../../../tests)_) 
   - 新增 JavaScript/TypeScript 的 Jest 配置

---

## 3. 教育增強

### 3.1 新增課程主題

1. **AI 應用中的安全性**（擬定課程 22）
   - Prompt 注入攻擊及防禦
   - API 金鑰管理
   - 內容審查
   - 速率限制與防濫用

2. <strong>生產環境部署</strong>（擬定課程 23）
   - 使用 Docker 容器化
   - CI/CD 管線
   - 監控與日誌記錄
   - 成本管理

3. **進階 RAG 技術**（擬定課程 24）
   - 混合搜尋（關鍵字 + 語義）
   - 重新排序策略
   - 多模態 RAG
   - 評估指標

### 3.2 現有課程改進

| 課程 | 推薦改進 |
|--------|------------------------|
| 06 - 文字生成 | 新增串流回應範例 |
| 07 - 聊天應用 | 新增對話記憶模式 |
| 08 - 搜尋應用 | 新增向量資料庫比較 |
| 09 - 圖像生成 | 新增圖像編輯/變異範例 |
| 11 - 函數呼叫 | 新增平行函數呼叫 |
| 15 - RAG | 新增分塊策略比較 |
| 17 - AI 代理 | 新增多代理協調 |

---

## 4. API 現代化

### 4.1 棄用 API 模式（遷移完成）

所有 Python 和 TypeScript <strong>聊天</strong>範例已從 Chat Completions API 遷移至 **Responses API**（`client.responses.create(...)` → `response.output_text`）。

| 舊模式 | 新模式 | 狀態 |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()`（聊天） | `OpenAI(base_url="<endpoint>/openai/v1/")`（Responses API） | 已完成 |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | 已完成 |
| `@azure/openai` `OpenAIClient.getChatCompletions()`（TypeScript） | `openai` 套件 `client.responses.create()` → `response.output_text` | 已完成 |
| `df.append()`（pandas） | `pd.concat()` | 已完成 |

> **注意：** 使用 `azure-ai-inference` / `@azure-rest/ai-inference` SDK（`client.complete()`）的 Microsoft Foundry Models 範例仍使用模型推理 API，該 API 不支援 Responses API。`AzureOpenAI()` 僅在仍有效的情況下保留（embeddings 和影像生成）。

### 4.2 需展示的新 API 功能

1. <strong>結構化輸出</strong>（OpenAI）
   - JSON 模式
   - 嚴格 schema 的函數呼叫

2. <strong>視覺能力</strong>
   - 使用 GPT-4o（視覺版）進行圖像分析
   - 多模態提示詞

3. **Responses API 內建工具**（取代舊 Assistants API）
   - 程式碼解譯器
   - 檔案搜尋
   - 網頁搜尋與自訂工具

---

## 5. 基礎架構改進

### 5.1 CI/CD 改善

已於 [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml) 實施：在維護中的 `shared/` 公用功能模組上<strong>強制</strong>執行 Python lint/格式化（Ruff + Black），課程其他部分則執行<strong>建議性</strong>檢查，加上 JavaScript/TypeScript 的建議性 ESLint 通過。示例基線為：

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

已於 [`.github/workflows/security.yml`](../../../.github/workflows/security.yml) 實施：Python 與 JavaScript/TypeScript 的 CodeQL 分析（在推送、拉取請求及週期任務觸發），並在拉取請求中執行相依性審查。示例基線為：

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

## 6. 開發者體驗改進

### 6.1 DevContainer 強化

已於 [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) 和 [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh) 實施：容器現在內置 Pylance、Black 格式化工具、Ruff、ESLint、Prettier 和 Copilot 擴充套件，啟用保存時格式化並使用 repo 的 Black/Prettier 配置，安裝開發工具（`ruff`、`black`、`mypy`、`pytest`），使得 [code-quality 工作流程](../../../.github/workflows/code-quality.yml) 能在本地再現。`mcr.microsoft.com/devcontainers/universal` 基底映像已經包含 Python 和 Node，無需額外功能。示例基線為：

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
- 預填 API 金鑰（透過環境變數）的 Jupyter 筆記本
- 適合視覺學習者的 Gradio/Streamlit 示範
- 用於知識評估的互動測驗

---

## 7. 多語言支援

### 7.1 目前語言涵蓋

| 技術 | 涉及課程 | 狀態 |
|------------|-----------------|--------|
| Python | 全部 | 已完成 |
| TypeScript | 06-09, 11 | 部分 |
| JavaScript | 06-08, 11 | 部分 |
| .NET/C# | 部分 | 部分 |

### 7.2 推薦新增

1. **Go** - AI/ML 工具生態持續成長
2. **Rust** - 針對效能關鍵應用
3. **Java/Kotlin** - 企業應用

---

## 8. 性能優化

### 8.1 程式碼層級優化

1. **Async/Await 範式**
   - 增加批次處理的非同步範例
   - 示範並行 API 呼叫

2. <strong>快取策略</strong>
   - 新增 embedding 快取範例
   - 示範回應快取模式

3. **Token 使用最佳化**
   - 新增 tiktoken 使用範例
   - 示範提示詞壓縮技巧

### 8.2 成本優化範例

新增展示範例：
- 根據任務複雜度選擇模型
- 以提示詞工程提升 token 效率
- 批次處理大量作業

---

## 9. 可及性與國際化

### 9.1 目前翻譯狀況

所有翻譯皆<strong>完成</strong>，並由 [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) 自動產生，維持 50 多種語言版本與英文源文件同步。翻譯內容儲存在 `translations/`，本地化圖片存於 `translated_images/`；完整可用語言列表刊載於倉庫 README 頁首。

| 項目 | 狀態 |
|--------|--------|
| 翻譯涵蓋範圍 | 完整 — 50 多種語言，涵蓋所有課程 |
| 翻譯方式 | 透過 [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) 自動 |
| 與英文源保持同步 | 是 — 自動重新生成 |

### 9.2 無障礙改善

1. 為所有圖片加入替代文字
2. 確保程式碼範例有適當語法高亮
3. 為所有影片內容提供字幕稿
4. 確保色彩對比符合 WCAG 指南

---

## 10. 實施優先順序

### 第一階段：立即（第 1-2 週）
- [x] 修復關鍵安全問題
- [x] 新增程式碼品質設定檔
- [x] 創建共享工具
- [x] 文件化安全指導方針

### 第二階段：短期（第 3-4 週）
- [x] 更新棄用 API 模式（聊天補全 → Responses API，Python 與 TypeScript）
- [ ] 為所有 Python 檔案加入類型註解（已完成維護的 `shared/` 模組；課程範例以簡潔為主）
- [x] 新增用於程式碼品質的 CI/CD 工作流程
- [x] 創建安全掃描工作流程

### 第三階段：中期（第 2-3 個月）
- [ ] 新增安全性課程
- [ ] 新增生產環境部署課程
- [x] 改善 DevContainer 設定
- [ ] 新增互動式示範

### 第四階段：長期（第 4 個月以上）
- [ ] 新增進階 RAG 課程
- [ ] 擴充語言支援
- [ ] 新增完整測試套件
- [ ] 創建認證計畫

---

## 結論

本路線圖為《生成式 AI 初學者》課程的改進提供結構化方案。透過解決安全問題、現代化 API 並新增教育內容，課程將更好地準備學生面對實務 AI 應用開發。

如有疑問或貢獻，歡迎於 GitHub 倉庫開啟 issue。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->