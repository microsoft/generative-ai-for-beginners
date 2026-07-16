# 加強功能與改進路線圖

本文件概述了根據全面的代碼審查和行業最佳實踐分析，對《初學者生成式 AI》課程推薦的增強與改進建議。

## 執行摘要

本代碼庫已針對安全性、代碼質量及教學效能進行分析。本文檔提供立即修復、近期改進及未來增強的建議。

---

## 1. 安全性增強（優先級：關鍵）

### 1.1 立即修復（已完成）

| 問題 | 影響檔案 | 狀態 |
|-------|----------------|--------|
| 硬編碼 SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | 已修復 |
| 缺少環境變數驗證 | 多個 JS/TS 檔案 | 已修復 |
| 不安全的函式調用 | `11-integrating-with-function-calling/js-githubmodels/app.js` | 已修復 |
| 檔案句柄洩漏 | `08-building-search-applications/scripts/` | 已修復 |
| 缺少請求超時 | `09-building-image-applications/python/` | 已修復 |

### 1.2 推薦的額外安全功能

1. <strong>速率限制範例</strong>
   - 新增範例代碼展示如何為 API 調用實作速率限制
   - 演示指數退避模式

2. **API 金鑰輪換**
   - 增加有關 API 金鑰輪換最佳實踐的文件
   - 包含使用 Azure Key Vault 或類似服務的範例

3. <strong>內容安全整合</strong>
   - 新增使用 Azure 內容安全 API 的範例
   - 演示輸入/輸出審查模式

---

## 2. 代碼質量改進

### 2.1 新增配置檔

| 檔案 | 目的 |
|------|---------|
| `.eslintrc.json` | JavaScript/TypeScript 的 lint 規則 |
| `.prettierrc` | 代碼格式標準 |
| `pyproject.toml` | Python 工具配置（Black、Ruff、mypy） |

### 2.2 新建共用工具

新增 `shared/python/` 模組，包含：
- `env_utils.py` - 環境變數處理
- `input_validation.py` - 輸入驗證與淨化
- `api_utils.py` - 安全的 API 請求包裝器

### 2.3 推薦代碼改進

1. <strong>類型標註覆蓋</strong>
   - 為所有 Python 檔案新增類型標註
   - 在所有 TS 專案中啟用嚴格的 TypeScript 模式

2. <strong>文件標準</strong>
   - 為所有 Python 函式添加 docstring
   - 為所有 JavaScript/TypeScript 函式添加 JSDoc 註解

3. <strong>測試框架</strong>
   - 增加 pytest 配置和範例測試 _（已完成：pytest 配置在 `pyproject.toml`；共用工具範例測試於 [`tests/`](../../../tests)，並在 CI 中執行）_
   - 新增 JavaScript/TypeScript 的 Jest 配置

---

## 3. 教育增強

### 3.1 新課題主題

1. **AI 應用的安全性**（提案課程 22）
   - 提示注入攻擊與防禦
   - API 金鑰管理
   - 內容審查
   - 速率限制與濫用防止

2. <strong>生產部署</strong>（提案課程 23）
   - 使用 Docker 容器化
   - CI/CD 管線
   - 監控與日誌記錄
   - 成本管理

3. **進階 RAG 技術**（提案課程 24）
   - 混合搜尋（關鍵詞 + 語意）
   - 重排序策略
   - 多模態 RAG
   - 評估指標

### 3.2 現有課程改進

| 課程 | 推薦改進 |
|--------|------------------------|
| 06 - 文字生成 | 新增串流回應範例 |
| 07 - 聊天應用 | 新增對話記憶模式 |
| 08 - 搜尋應用 | 新增向量資料庫比較 |
| 09 - 影像生成 | 新增影像編輯/變化範例 |
| 11 - 函式呼叫 | 新增平行函式呼叫 |
| 15 - RAG | 新增分塊策略比較 |
| 17 - AI 代理 | 新增多代理協調 |

---

## 4. API 現代化

### 4.1 棄用的 API 模式（遷移已完成）

所有 Python 和 TypeScript <strong>聊天</strong> 範例已從 Chat Completions API 遷移到 **Responses API**（`client.responses.create(...)` → `response.output_text`）。

| 舊模式 | 新模式 | 狀態 |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()`（聊天） | `OpenAI(base_url="<endpoint>/openai/v1/")`（Responses API） | 已完成 |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | 已完成 |
| `@azure/openai` `OpenAIClient.getChatCompletions()`（TypeScript） | `openai` 套件 `client.responses.create()` → `response.output_text` | 已完成 |
| `df.append()`（pandas） | `pd.concat()` | 已完成 |

> **注意：** 使用 `azure-ai-inference` / `@azure-rest/ai-inference` SDK (`client.complete()`) 的 Microsoft Foundry Models 範例仍維持在模型推論 API，該 API 不支援 Responses API。`AzureOpenAI()` 在仍有效的情況下（嵌入向量及影像生成）被保留。

### 4.2 新 API 功能展示

1. <strong>結構化輸出</strong>（OpenAI）
   - JSON 模式
   - 帶有嚴格模式的函式呼叫

2. <strong>視覺能力</strong>
   - 使用 GPT-4o（vision）的影像分析
   - 多模態提示

3. **Responses API 內建工具**（取代舊 Assistants API）
   - 程式碼解譯器
   - 檔案搜尋
   - 網頁搜尋與自訂工具

---

## 5. 基礎架構改進

### 5.1 CI/CD 增強

已實作於 [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml)：Python lint/格式化工具 (Ruff + Black) <strong>強制</strong>在維護的 `shared/` 工具模組上執行，課程其他部分則執行<strong>建議</strong>檢查，並對 JS/TS 新增 ESLint 建議檢查。參考基準為：

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

已實作於 [`.github/workflows/security.yml`](../../../.github/workflows/security.yml)：針對 Python 與 JavaScript/TypeScript 執行 CodeQL 分析（在 push、pull request 及每週定時），以及 pull request 的相依性檢查。參考基準為：

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

### 6.1 DevContainer 增強

已實作於 [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) 和 [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh)：容器現已附帶 Pylance、Black 格式化工具、Ruff、ESLint、Prettier 與 Copilot 擴充功能，啟用格式儲存即時套用並對應至 repo 的 Black/Prettier 配置，同時安裝開發工具（`ruff`、`black`、`mypy`、`pytest`），讓 [code-quality workflow](../../../.github/workflows/code-quality.yml) 可於本地重現。`mcr.microsoft.com/devcontainers/universal` 基底映像已包含 Python 和 Node，故不需其他額外元件。參考基準為：

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

建議增加：
- 含預填 API 金鑰（經由環境變數）的 Jupyter 筆記本
- 為視覺學習者設計的 Gradio / Streamlit 展示
- 互動式測驗用以知識評估

---

## 7. 多語言支援

### 7.1 目前語言覆蓋

| 技術 | 覆蓋課程 | 狀態 |
|------------|-----------------|--------|
| Python | 全部 | 完成 |
| TypeScript | 06-09, 11 | 部分 |
| JavaScript | 06-08, 11 | 部分 |
| .NET/C# | 部分課程 | 部分 |

### 7.2 推薦新增

1. **Go** - 在 AI/ML 工具領域日漸增長
2. **Rust** - 用於效能關鍵型應用
3. **Java/Kotlin** - 企業級應用

---

## 8. 性能優化

### 8.1 代碼層面優化

1. **Async/Await 模式**
   - 新增批次處理的非同步範例
   - 演示並發 API 呼叫

2. <strong>快取策略</strong>
   - 新增向量快取範例
   - 演示回應快取模式

3. **Token 優化**
   - 新增 tiktoken 使用範例
   - 演示提示詞壓縮技巧

### 8.2 成本優化範例

新增示範：
- 依任務複雜度選擇模型
- 透過提示工程提高 tokens 使用效率
- 批次處理大量操作

---

## 9. 無障礙與國際化

### 9.1 目前翻譯狀態

所有翻譯均已<strong>完成</strong>，由 [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) 自動生成維護，該工具將超過 50 種語言版本的課程內容與英文原文保持同步。翻譯內容存於 `translations/`，本地化圖片存於 `translated_images/`；完整可用語言列表刊載於倉庫 README 頂部。

| 項目 | 狀態 |
|--------|--------|
| 翻譯覆蓋 | 完整 — 50+ 種語言，包含全部課程 |
| 翻譯方式 | 透過 [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) 自動化完成 |
| 與英文來源同步 | 是 — 自動重新生成 |

### 9.2 無障礙改進

1. 為所有圖片新增替代文字
2. 確保代碼範例有適當語法高亮
3. 為所有視訊內容提供字幕稿
4. 確保色彩對比符合 WCAG 指南

---

## 10. 實施優先順序

### 第一階段：立即（第 1-2 週）
- [x] 修復關鍵安全問題
- [x] 增加代碼質量配置
- [x] 建立共用工具
- [x] 撰寫安全指導文件

### 第二階段：短期（第 3-4 週）
- [x] 更新棄用 API 模式（從 Chat Completions → Responses API，Python 與 TypeScript）
- [ ] 為所有 Python 檔案添加類型標註（已針對維護中的 `shared/` 模組完成；課堂範例保持簡潔）
- [x] 新增 CI/CD 工作流程以保障代碼質量
- [x] 建立安全掃描工作流程

### 第三階段：中期（第 2-3 個月）
- [ ] 新增安全性課程
- [ ] 新增生產部署課程
- [x] 改善 DevContainer 配置
- [ ] 新增互動示範

### 第四階段：長期（第 4 個月起）
- [ ] 新增進階 RAG 課程
- [ ] 擴充語言支援範圍
- [ ] 新增完整測試套件
- [ ] 建立認證課程

---

## 結語

本路線圖提供了結構化方法來改進《初學者生成式 AI》課程。透過解決安全問題、現代化 API 及增加教學內容，該課程將使學生更好地準備面對真實世界中的 AI 應用開發。

如有疑問或想作出貢獻，請在 GitHub 倉庫中開啟 Issue。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->