# 強化功能與改進路線圖

本文檔概述了針對初學者生成式 AI 課程基於全面的代碼審查和行業最佳實踐分析所推薦的增強與改進方案。

## 執行摘要

已對代碼庫進行了安全性、代碼質量及教學效果的分析。本文件提供了立即修復、近期改進及未來增強的建議。

---

## 1. 安全增強（優先級：緊急）

### 1.1 立即修復（已完成）

| 問題 | 影響檔案 | 狀態 |
|-------|----------------|--------|
| 硬編碼 SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | 已修復 |
| 缺少環境變數驗證 | 多個 JS/TS 檔案 | 已修復 |
| 不安全的函式呼叫 | `11-integrating-with-function-calling/js-githubmodels/app.js` | 已修復 |
| 檔案處理器洩漏 | `08-building-search-applications/scripts/` | 已修復 |
| 缺少請求超時 | `09-building-image-applications/python/` | 已修復 |

### 1.2 推薦的額外安全功能

1. **限流示範**
   - 新增示範代碼展示如何為 API 呼叫實作限流
   - 展示指數退避（exponential backoff）模式

2. **API 金鑰輪替**
   - 新增 API 金鑰輪替的最佳實務文件
   - 包含使用 Azure Key Vault 或類似服務的範例

3. **內容安全整合**
   - 新增使用 Azure Content Safety API 的示例
   - 展示輸入/輸出審核模式

---

## 2. 代碼質量改進

### 2.1 新增配置檔案

| 檔案 | 作用 |
|------|---------|
| `.eslintrc.json` | JavaScript/TypeScript 程式碼檢查規則 |
| `.prettierrc` | 程式碼格式化標準 |
| `pyproject.toml` | Python 工具配置（Black、Ruff、mypy） |

### 2.2 新建共享工具模組

新增 `shared/python/` 模組，包含：
- `env_utils.py` - 環境變數處理
- `input_validation.py` - 輸入驗證與淨化
- `api_utils.py` - 安全的 API 請求封裝

### 2.3 推薦代碼改進

1. **型別提示覆蓋**
   - 為所有 Python 檔案新增型別提示
   - 在所有 TS 專案中開啟嚴格模式

2. **文件註解標準**
   - 為所有 Python 函數新增 docstrings
   - 為所有 JavaScript/TypeScript 函數新增 JSDoc 註解

3. **測試框架**
   - 新增 pytest 配置與範例測試
   - 新增 JavaScript/TypeScript 的 Jest 配置

---

## 3. 教學增強

### 3.1 新增課程主題

1. **AI 應用安全**（建議課程 22）
   - 提示注入攻擊與防禦
   - API 金鑰管理
   - 內容審核
   - 限流與濫用防止

2. **生產環境部署**（建議課程 23）
   - 使用 Docker 容器化
   - CI/CD 管線
   - 監控與日誌
   - 成本管理

3. **進階 RAG 技術**（建議課程 24）
   - 混合檢索（關鍵字 + 語義）
   - 再排序策略
   - 多模態 RAG
   - 評估指標

### 3.2 現有課程改進

| 課程 | 推薦改進 |
|--------|------------------------|
| 06 - 文字生成 | 新增串流回應示例 |
| 07 - 聊天應用 | 新增對話記憶模式 |
| 08 - 搜尋應用 | 新增向量資料庫比較 |
| 09 - 影像生成 | 新增影像編輯/變異示例 |
| 11 - 函式呼叫 | 新增平行函式呼叫 |
| 15 - RAG | 新增切塊策略比較 |
| 17 - AI 代理 | 新增多代理編排 |

---

## 4. API 現代化

### 4.1 需更新的已廢棄 API 模式

| 舊模式 | 新模式 | 影響檔案 |
|-------------|-------------|----------------|
| `openai.api_type = "azure"` | `AzureOpenAI()` 客戶端 | `08-building-search-applications/`多個腳本 |
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
   - 程式碼解譯器
   - 檔案搜尋
   - 自訂工具

---

## 5. 基礎建設改進

### 5.1 CI/CD 增強

目前工作流程處理 markdown 驗證。推薦新增：

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
- 具備預設 API 金鑰（透過環境變數）的 Jupyter 筆記本
- 適合視覺學習者的 Gradio/Streamlit 示範
- 知識評測的互動式小測驗

---

## 7. 多語言支援

### 7.1 目前語言覆蓋狀況

| 技術 | 適用課程 | 狀態 |
|------------|-----------------|--------|
| Python | 全部 | 完成 |
| TypeScript | 06-09、11 | 部分 |
| JavaScript | 06-08、11 | 部分 |
| .NET/C# | 部分 | 部分 |

### 7.2 推薦新增語言

1. **Go** - 於 AI/ML 工具中持續成長
2. **Rust** - 性能關鍵應用
3. **Java/Kotlin** - 企業應用

---

## 8. 性能優化

### 8.1 代碼層級優化

1. **Async/Await 模式**
   - 新增批次處理的非同步示例
   - 展示並行 API 呼叫

2. **快取策略**
   - 新增嵌入向量快取示例
   - 展示回應快取模式

3. **令牌優化**
   - 新增 tiktoken 使用示例
   - 展示提示壓縮技巧

### 8.2 成本優化示例

新增示例示範：
- 根據任務複雜度選擇模型
- 提示工程以提升令牌效率
- 批次處理以提升大量操作效能

---

## 9. 無障礙與國際化

### 9.1 目前翻譯狀況

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

1. 為所有圖片添加替代文字
2. 確保程式碼範例具備適當語法高亮
3. 為所有影片內容提供文字稿
4. 確保色彩對比符合 WCAG 指南

---

## 10. 實施優先順序

### 第一階段：立即（第 1-2 週）
- [x] 修復關鍵安全問題
- [x] 新增代碼質量配置
- [x] 建立共享工具
- [x] 文件基礎安全指引

### 第二階段：短期（第 3-4 週）
- [ ] 更新已廢棄的 API 模式
- [ ] 為所有 Python 檔案新增型別提示
- [ ] 為代碼質量新增 CI/CD 工作流程
- [ ] 建立安全掃描工作流程

### 第三階段：中期（第 2-3 個月）
- [ ] 新增安全相關課程
- [ ] 新增生產部署課程
- [ ] 改進 DevContainer 設定
- [ ] 新增互動式示範

### 第四階段：長期（第 4 個月以上）
- [ ] 新增進階 RAG 課程
- [ ] 擴展語言支援範圍
- [ ] 新增完整測試套件
- [ ] 建立認證計畫

---

## 結論

本路線圖提供了一個結構化的方向，以提升初學者生成式 AI 課程。透過解決安全問題、現代化 API 及擴展教學內容，課程將更能幫助學生為實務 AI 應用開發做好準備。

如有疑問或貢獻，請於 GitHub 倉庫開啟議題。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意自動化翻譯可能包含錯誤或不正確之處。原始文件的母語版本應視為具權威性的資料來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->