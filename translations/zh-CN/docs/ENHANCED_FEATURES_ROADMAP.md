# 增强功能和改进路线图

本文件概述了针对新手生成式 AI 课程的推荐增强和改进，基于全面的代码审查和行业最佳实践分析。

## 执行摘要

我们对代码库进行了安全性、代码质量和教育效果的分析。本文档提供了紧急修复、近期改进和未来增强的建议。

---

## 1. 安全增强（优先级：关键）

### 1.1 紧急修复（已完成）

| 问题 | 受影响文件 | 状态 |
|-------|----------------|--------|
| 硬编码的 SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | 已修复 |
| 缺少环境变量验证 | 多个 JS/TS 文件 | 已修复 |
| 不安全的函数调用 | `11-integrating-with-function-calling/js-githubmodels/app.js` | 已修复 |
| 文件句柄泄露 | `08-building-search-applications/scripts/` | 已修复 |
| 请求缺少超时设置 | `09-building-image-applications/python/` | 已修复 |

### 1.2 推荐的额外安全功能

1. **限流示例**
   - 添加示例代码，展示如何为 API 调用实现限流
   - 演示指数退避模式

2. **API 密钥轮换**
   - 添加关于 API 密钥轮换最佳实践的文档
   - 包含使用 Azure Key Vault 或类似服务的示例

3. **内容安全集成**
   - 添加使用 Azure 内容安全 API 的示例
   - 演示输入/输出审核模式

---

## 2. 代码质量改进

### 2.1 新增配置文件

| 文件 | 作用 |
|------|---------|
| `.eslintrc.json` | JavaScript/TypeScript 代码规范规则 |
| `.prettierrc` | 代码格式化标准 |
| `pyproject.toml` | Python 工具配置（Black、Ruff、mypy） |

### 2.2 新建共享工具

新增 `shared/python/` 模块，包含：
- `env_utils.py` - 环境变量处理
- `input_validation.py` - 输入验证和清理
- `api_utils.py` - 安全的 API 请求封装

### 2.3 推荐代码改进

1. **类型注解覆盖**
   - 为所有 Python 文件添加类型注解
   - 在所有 TS 项目中启用严格的 TypeScript 模式

2. **文档标准**
   - 为所有 Python 函数添加文档字符串
   - 为所有 JavaScript/TypeScript 函数添加 JSDoc 注释

3. **测试框架**
   - 添加 pytest 配置和示例测试
   - 添加 JavaScript/TypeScript 的 Jest 配置

---

## 3. 教育增强

### 3.1 新增课程主题

1. **AI 应用安全**（提议第 22 课）
   - 提示注入攻击与防御
   - API 密钥管理
   - 内容审核
   - 限流与滥用防范

2. **生产部署**（提议第 23 课）
   - Docker 容器化
   - CI/CD 流水线
   - 监控与日志
   - 成本管理

3. **高级 RAG 技术**（提议第 24 课）
   - 混合搜索（关键词 + 语义）
   - 重排序策略
   - 多模态 RAG
   - 评估指标

### 3.2 现有课程改进

| 课程 | 推荐改进 |
|--------|------------------------|
| 06 - 文本生成 | 添加流式响应示例 |
| 07 - 聊天应用 | 添加会话记忆模式 |
| 08 - 搜索应用 | 添加向量数据库对比 |
| 09 - 图像生成 | 添加图像编辑/变体示例 |
| 11 - 函数调用 | 添加并行函数调用 |
| 15 - RAG | 添加拆分策略对比 |
| 17 - AI 代理 | 添加多代理编排 |

---

## 4. API 现代化

### 4.1 需更新的废弃 API 模式

| 旧模式 | 新模式 | 受影响文件 |
|-------------|-------------|----------------|
| `openai.api_type = "azure"` | `AzureOpenAI()` 客户端 | `08-building-search-applications/` 多个脚本 |
| `openai.ChatCompletion.create()` | `client.chat.completions.create()` | 多个笔记本 |
| `df.append()`（pandas） | `pd.concat()` | RAG 笔记本 |

### 4.2 要演示的新 API 功能

1. **结构化输出**（OpenAI）
   - JSON 模式
   - 带严格 schema 的函数调用

2. **视觉能力**
   - 使用 GPT-4V 进行图像分析
   - 多模态提示

3. **助理 API**
   - 代码解释器
   - 文件搜索
   - 自定义工具

---

## 5. 基础设施改进

### 5.1 CI/CD 增强

当前工作流包含 markdown 验证。推荐新增：

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

### 5.2 安全扫描

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

## 6. 开发者体验改进

### 6.1 DevContainer 增强

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

### 6.2 交互式游乐场

考虑添加：
- 带预置 API 密钥（通过环境配置）的 Jupyter 笔记本
- 视觉学习者的 Gradio/Streamlit 演示
- 知识评估的交互式测验

---

## 7. 多语言支持

### 7.1 目前语言覆盖情况

| 技术 | 涵盖课程 | 状态 |
|------------|-----------------|--------|
| Python | 全部 | 完整 |
| TypeScript | 06-09, 11 | 部分 |
| JavaScript | 06-08, 11 | 部分 |
| .NET/C# | 部分 | 部分 |

### 7.2 推荐新增语言

1. **Go** - AI/ML 工具成长中
2. **Rust** - 性能关键应用
3. **Java/Kotlin** - 企业应用

---

## 8. 性能优化

### 8.1 代码层面优化

1. **Async/Await 模式**
   - 添加批处理异步示例
   - 演示并发 API 调用

2. **缓存策略**
   - 添加向量缓存示例
   - 演示响应缓存模式

3. **Token 优化**
   - 添加 tiktoken 使用示例
   - 演示提示压缩技巧

### 8.2 成本优化示例

添加展示：
- 基于任务复杂度选择模型
- 编写高效提示降低 token 消耗
- 批量处理实现成本节约

---

## 9. 可访问性与国际化

### 9.1 当前翻译状态

| 语言 | 状态 |
|----------|--------|
| 英语 | 完整 |
| 中文（简体） | 完整 |
| 日语 | 完整 |
| 韩语 | 完整 |
| 西班牙语 | 部分 |
| 葡萄牙语 | 部分 |
| 土耳其语 | 部分 |
| 波兰语 | 部分 |

### 9.2 可访问性改进

1. 为所有图片添加替代文本
2. 确保代码样例有恰当语法高亮
3. 为所有视频内容添加字幕文稿
4. 确保色彩对比符合 WCAG 指南

---

## 10. 实施优先级

### 阶段 1：紧急（第 1-2 周）
- [x] 修复关键安全问题
- [x] 添加代码质量配置
- [x] 创建共享工具
- [x] 编写安全指南文档

### 阶段 2：短期（第 3-4 周）
- [ ] 更新废弃 API 模式
- [ ] 为所有 Python 文件添加类型注解
- [ ] 添加代码质量 CI/CD 工作流
- [ ] 创建安全扫描工作流

### 阶段 3：中期（第 2-3 个月）
- [ ] 新增安全课程
- [ ] 新增生产部署课程
- [ ] 改进 DevContainer 设置
- [ ] 添加交互式演示

### 阶段 4：长期（第 4 个月及以后）
- [ ] 新增高级 RAG 课程
- [ ] 扩展语言覆盖
- [ ] 添加全面测试套件
- [ ] 创建认证项目

---

## 结论

本路线图为改进新手生成式 AI 课程提供了有结构的路径。通过解决安全问题、现代化 API 并增加教学内容，课程将更好地帮助学生适应真实世界的 AI 应用开发。

有疑问或贡献，请在 GitHub 仓库提交 issue。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件由人工智能翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。以原始语言的原文文件为权威版本。对于重要信息，建议采用专业人工翻译。本公司不对因使用本翻译版本而产生的任何误解或误释承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->