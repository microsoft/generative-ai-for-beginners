# 增強功能與改進路線圖

本文件概述了《初學者生成式 AI》課程的建議增強與改進，基於全面的程式碼審查及行業最佳實踐分析。

## 執行摘要

程式碼庫已針對安全性、程式碼品質和教育效果進行分析。本文檔提供了即時修復、近期改進和未來增強的建議。

---

## 1. 安全性增強（優先級：重要）

### 1.1 即時修復（已完成）

| 問題 | 受影響檔案 | 狀態 |
|-------|----------------|--------|
| 硬編碼的 SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | 已修復 |
| 缺少環境變數驗證 | 多個 JS/TS 檔案 | 已修復 |
| 不安全的函式呼叫 | `11-integrating-with-function-calling/js-githubmodels/app.js` | 已修復 |
| 文件句柄泄漏 | `08-building-search-applications/scripts/` | 已修復 |
| 缺少請求超時 | `09-building-image-applications/python/` | 已修復 |

### 1.2 建議的額外安全功能

1. **速率限制範例**
   - 新增示範如何為 API 呼叫實作速率限制的範例程式碼
   - 展示指數退避模式

2. **API 金鑰輪替**
   - 新增關於輪替 API 金鑰的最佳實務文件
   - 包含使用 Azure Key Vault 或類似服務的範例

3. **內容安全整合**
   - 增加使用 Azure Content Safety API 的示例
   - 展示輸入/輸出審核模式

---

## 2. 程式碼品質改進

### 2.1 新增組態檔

| 檔案 | 用途 |
|------|---------|
| `.eslintrc.json` | JavaScript/TypeScript 的程式碼規則 |
| `.prettierrc` | 程式碼格式標準 |
| `pyproject.toml` | Python 工具配置（Black、Ruff、mypy） |

### 2.2 建立共用工具模組

新增 `shared/python/` 模組，包含：
- `env_utils.py` - 環境變數處理
- `input_validation.py` - 輸入驗證與消毒
- `api_utils.py` - 安全 API 請求封裝

### 2.3 建議的程式碼改進

1. **類型提示覆蓋**
   - 為所有 Python 檔案補充類型提示
   - 為所有 TS 專案啟用嚴格模式

2. **文件標準**
   - 為所有 Python 函式新增函式說明字串 (docstring)
   - 為所有 JavaScript/TypeScript 函式新增 JSDoc 註解

3. **測試框架**
   - 新增 pytest 組態與範例測試
   - 新增 Jest 組態用於 JavaScript/TypeScript

---

## 3. 教育增強

### 3.1 新課程主題

1. **AI 應用的安全性**（建議課程 22）
   - 提示注入攻擊與防禦
   - API 金鑰管理
   - 內容審核
   - 速率限制與濫用防範

2. **生產部署**（建議課程 23）
   - Docker 容器化
   - CI/CD 管線
   - 監控與日誌記錄
   - 成本管理

3. **進階 RAG 技術**（建議課程 24）
   - 混合搜尋（關鍵詞 + 語意）
   - 重排序策略
   - 多模態 RAG
   - 評估指標

### 3.2 現有課程改進

| 課程 | 建議改進 |
|--------|------------------------|
| 06 - 文字生成 | 新增串流回應範例 |
| 07 - 聊天應用 | 新增會話記憶模式 |
| 08 - 搜尋應用 | 新增向量資料庫比較 |
| 09 - 影像生成 | 新增影像編輯/變異範例 |
| 11 - 函式呼叫 | 新增平行函式呼叫 |
| 15 - RAG | 新增分塊策略比較 |
| 17 - AI 代理人 | 新增多代理人協作 |

---

## 4. API 現代化

### 4.1 待更新的過時 API 模式

| 舊模式 | 新模式 | 受影響檔案 |
|-------------|-------------|----------------|
| `openai.api_type = "azure"` | `AzureOpenAI()` 用戶端 | `08-building-search-applications/` 多腳本 |
| `openai.ChatCompletion.create()` | `client.chat.completions.create()` | 多個筆記本 |
| `df.append()`（pandas） | `pd.concat()` | RAG 筆記本 |

### 4.2 新 API 功能示範

1. **結構化輸出**（OpenAI）
   - JSON 模式
   - 嚴格 schema 的函式呼叫

2. **視覺能力**
   - GPT-4V 影像分析
   - 多模態提示

3. **助理 API**
   - 程式碼解釋器
   - 文件搜尋
   - 自訂工具

---

## 5. 基礎建設改進

### 5.1 CI/CD 增強

目前流程處理 markdown 驗證。建議新增：

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

更新 `.devcontainer/devcontainer.json`：

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

建議新增：
- 帶預置 API 金鑰（透過環境變數）的 Jupyter 筆記本
- Gradio/Streamlit 視覺化教學範例
- 互動式測驗以評估知識

---

## 7. 多語言支援

### 7.1 目前語言覆蓋範圍

| 技術 | 涵蓋課程 | 狀態 |
|------------|-----------------|--------|
| Python | 全部 | 完全 |
| TypeScript | 06-09, 11 | 部分 |
| JavaScript | 06-08, 11 | 部分 |
| .NET/C# | 部分 | 部分 |

### 7.2 建議新增

1. **Go** - AI/ML 工具日益成長
2. **Rust** - 性能關鍵應用
3. **Java/Kotlin** - 企業應用

---

## 8. 效能優化

### 8.1 程式碼層級優化

1. **Async/Await 範例**
   - 新增批次處理的非同步示範
   - 展示並發 API 呼叫

2. **快取策略**
   - 新增嵌入快取範例
   - 展示回應快取模式

3. **Token 優化**
   - 新增 tiktoken 使用範例
   - 展示提示壓縮技巧

### 8.2 成本優化範例

新增展示：
- 根據任務複雜度選擇模型
- 提示工程以提升 Token 效率
- 批次處理以提高效能

---

## 9. 無障礙與國際化

### 9.1 目前翻譯狀態

| 語言 | 狀態 |
|----------|--------|
| 英文 | 完成 |
| 中文（簡體） | 完成 |
| 日文 | 完成 |
| 韓文 | 完成 |
| 西班牙文 | 部分 |
| 葡萄牙文 | 部分 |
| 土耳其文 | 部分 |
| 波蘭文 | 部分 |

### 9.2 無障礙改進

1. 為所有影像新增替代文字
2. 確保程式碼範例有適當語法高亮
3. 為所有影片內容新增文字稿
4. 確保色彩對比符合 WCAG 指南

---

## 10. 實作優先順序

### 第一階段：即時（第1-2週）
- [x] 修復關鍵安全問題
- [x] 新增程式碼品質組態
- [x] 建立共用工具
- [x] 撰寫安全指導文件

### 第二階段：短期（第3-4週）
- [ ] 更新過時 API 模式
- [ ] 為所有 Python 檔案新增類型提示
- [ ] 新增程式碼品質 CI/CD 流程
- [ ] 建立安全掃描流程

### 第三階段：中期（第2-3個月）
- [ ] 新增安全性課程
- [ ] 新增生產部署課程
- [ ] 改善 DevContainer 設定
- [ ] 新增互動範例

### 第四階段：長期（第4個月起）
- [ ] 新增進階 RAG 課程
- [ ] 擴充語言覆蓋範圍
- [ ] 新增全面測試套件
- [ ] 建立認證課程

---

## 結論

本路線圖提供了結構化的方式，提升《初學者生成式 AI》課程。透過解決安全問題、現代化 API 與豐富教學內容，能更好地幫助學員應對真實世界的 AI 應用開發。

如有問題或貢獻，請於 GitHub 倉庫開啟 issue。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能會包含錯誤或不準確之處。原始語言版本的文件應被視為權威來源。對於重要資訊，建議使用專業人類翻譯。我們對因使用此翻譯所引起的任何誤解或錯誤詮釋概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->