# 強化功能和改進路線圖

本文件概述了基於全面的代碼審查和行業最佳實踐分析，針對「生成式 AI 初學者」課程推薦的增強和改進建議。

## 執行摘要

代碼庫已對安全性、代碼質量和教育效果進行分析。本文件提供了即時修復、短期改進和未來增強的建議。

---

## 1. 安全性增強（優先級：關鍵）

### 1.1 即時修復（已完成）

| 問題 | 受影響文件 | 狀態 |
|-------|----------------|--------|
| 硬編碼的 SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | 已修復 |
| 缺少環境驗證 | 多個 JS/TS 文件 | 已修復 |
| 不安全的函數調用 | `11-integrating-with-function-calling/js-githubmodels/app.js` | 已修復 |
| 文件句柄洩漏 | `08-building-search-applications/scripts/` | 已修復 |
| 缺少請求超時 | `09-building-image-applications/python/` | 已修復 |

### 1.2 推薦的額外安全功能

1. **速率限制示例**
   - 新增示範代碼展示如何對 API 調用實施速率限制
   - 展示指數回退模式

2. **API 金鑰輪替**
   - 增加有關 API 金鑰輪替的最佳實踐文件
   - 包含使用 Azure Key Vault 或類似服務的示例

3. **內容安全整合**
   - 新增使用 Azure Content Safety API 的示例
   - 展示輸入/輸出審核模式

---

## 2. 代碼質量改進

### 2.1 新增配置文件

| 文件 | 目的 |
|------|---------|
| `.eslintrc.json` | JavaScript/TypeScript 的代碼檢查規則 |
| `.prettierrc` | 代碼格式化標準 |
| `pyproject.toml` | Python 工具配置（Black、Ruff、mypy） |

### 2.2 創建共用工具

新增 `shared/python/` 模組包含：
- `env_utils.py` - 環境變量處理
- `input_validation.py` - 輸入驗證與清理
- `api_utils.py` - 安全的 API 請求封裝

### 2.3 推薦的代碼改進

1. **類型提示覆蓋**
   - 為所有 Python 文件添加類型提示
   - 在所有 TS 項目中啟用嚴格的 TypeScript 模式

2. **文檔標準**
   - 為所有 Python 函數添加 Docstring
   - 為所有 JavaScript/TypeScript 函數添加 JSDoc 註釋

3. **測試框架**
   - 添加 pytest 配置及示例測試
   - 為 JavaScript/TypeScript 添加 Jest 配置

---

## 3. 教育增強

### 3.1 新課程主題

1. **AI 應用中的安全性**（建議課程 22）
   - 提示注入攻擊與防禦
   - API 金鑰管理
   - 內容審核
   - 速率限制與濫用防止

2. **生產環境部署**（建議課程 23）
   - 使用 Docker 容器化
   - CI/CD 管線
   - 監控與日誌
   - 成本管理

3. **進階 RAG 技術**（建議課程 24）
   - 混合搜索（關鍵字 + 語義）
   - 重排序策略
   - 多模態 RAG
   - 評估指標

### 3.2 現有課程改進

| 課程 | 推薦改進 |
|--------|------------------------|
| 06 - 文字生成 | 添加串流回應示例 |
| 07 - 聊天應用 | 添加對話記憶模式 |
| 08 - 搜索應用 | 添加向量資料庫比較 |
| 09 - 影像生成 | 添加影像編輯/變化示例 |
| 11 - 函數調用 | 添加平行函數調用 |
| 15 - RAG | 添加切塊策略比較 |
| 17 - AI 代理 | 添加多代理協調 |

---

## 4. API 現代化

### 4.1 待更新的已棄用 API 模式

| 舊模式 | 新模式 | 受影響文件 |
|-------------|-------------|----------------|
| `openai.api_type = "azure"` | `AzureOpenAI()` 客戶端 | `08-building-search-applications/` 多個腳本 |
| `openai.ChatCompletion.create()` | `client.chat.completions.create()` | 多個筆記本 |
| `df.append()` (pandas) | `pd.concat()` | RAG 筆記本 |

### 4.2 新 API 功能示範

1. **結構化輸出**（OpenAI）
   - JSON 模式
   - 函數調用與嚴格 schema

2. **視覺能力**
   - GPT-4V 影像分析
   - 多模態提示

3. **助理 API**
   - 代碼解釋器
   - 文件搜索
   - 自訂工具

---

## 5. 基礎設施改進

### 5.1 CI/CD 增強

目前工作流處理 Markdown 驗證。建議新增：

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

考慮新增：
- 含預先填充 API 金鑰的 Jupyter 筆記本（通過環境變量）
- Gradio/Streamlit 示範，適合視覺學習者
- 互動式小測驗以評估知識

---

## 7. 多語言支援

### 7.1 目前語言覆蓋

| 技術 | 覆蓋課程 | 狀態 |
|------------|-----------------|--------|
| Python | 全部 | 完成 |
| TypeScript | 06-09, 11 | 部分 |
| JavaScript | 06-08, 11 | 部分 |
| .NET/C# | 部分 | 部分 |

### 7.2 推薦新增語言

1. **Go** - AI/ML 工具日益增長
2. **Rust** - 性能關鍵應用
3. **Java/Kotlin** - 企業應用

---

## 8. 性能優化

### 8.1 代碼層級優化

1. **Async/Await 模式**
   - 新增批次處理的異步示例
   - 展示並行 API 調用

2. **緩存策略**
   - 添加嵌入緩存示例
   - 展示回應緩存模式

3. **Token 優化**
   - 添加 tiktoken 使用示例
   - 展示提示壓縮技術

### 8.2 成本優化示例

新增示例展示：
- 根據任務複雜度選擇模型
- 提示工程以提升 token 使用效率
- 批次處理以提高大宗操作效益

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

1. 為所有圖片添加替代文字
2. 確保程式碼範例有適當語法高亮
3. 為所有影片提供文字稿
4. 確保色彩對比符合 WCAG 指引

---

## 10. 實施優先順序

### 第 1 階段：即時（第 1-2 週）
- [x] 修復關鍵安全問題
- [x] 新增代碼質量配置
- [x] 建立共用工具
- [x] 文件化安全指引

### 第 2 階段：短期（第 3-4 週）
- [ ] 更新已棄用 API 模式
- [ ] 為所有 Python 文件添加類型提示
- [ ] 新增 CI/CD 工作流以保證代碼質量
- [ ] 建立安全掃描工作流

### 第 3 階段：中期（第 2-3 月）
- [ ] 新增安全性課程
- [ ] 新增生產部署課程
- [ ] 改善 DevContainer 設置
- [ ] 新增互動示範

### 第 4 階段：長期（第 4 月以上）
- [ ] 新增進階 RAG 課程
- [ ] 擴展語言覆蓋
- [ ] 添加全面測試套件
- [ ] 建立認證計劃

---

## 結論

本路線圖提供了改善「生成式 AI 初學者」課程的結構化方案。透過解決安全問題、現代化 API 並添加教學內容，該課程將更能幫助學生準備真實世界的 AI 應用開發。

如有疑問或貢獻，請在 GitHub 儲存庫中開啟 issue。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件乃使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件以其母語版本為準，應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->