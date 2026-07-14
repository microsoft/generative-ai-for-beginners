# 增强功能与改进路线图

本文档基于全面的代码审查和行业最佳实践分析，概述了面向初学者的生成式人工智能课程推荐的增强和改进方案。

## 执行摘要

代码库已针对安全性、代码质量和教学效果进行了分析。本文档提供了立即修复、近期改进和未来增强的建议。

---

## 1. 安全增强（优先级：关键）

### 1.1 立即修复（已完成）

| 问题 | 受影响文件 | 状态 |
|-------|----------------|--------|
| 硬编码的 SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | 已修复 |
| 缺失环境变量验证 | 多个 JS/TS 文件 | 已修复 |
| 不安全的函数调用 | `11-integrating-with-function-calling/js-githubmodels/app.js` | 已修复 |
| 文件句柄泄漏 | `08-building-search-applications/scripts/` | 已修复 |
| 缺失请求超时 | `09-building-image-applications/python/` | 已修复 |

### 1.2 推荐的额外安全特性

1. <strong>限流示例</strong>
   - 添加示例代码展示如何为 API 调用实现限流
   - 展示指数退避模式

2. **API 密钥轮换**
   - 添加关于 API 密钥轮换最佳实践的文档
   - 包含使用 Azure Key Vault 或类似服务的示例

3. <strong>内容安全集成</strong>
   - 添加使用 Azure 内容安全 API 的示例
   - 展示输入/输出内容审核模式

---

## 2. 代码质量改进

### 2.1 新增配置文件

| 文件 | 目的 |
|------|---------|
| `.eslintrc.json` | JavaScript/TypeScript 代码规范规则 |
| `.prettierrc` | 代码格式化标准 |
| `pyproject.toml` | Python 工具配置（Black、Ruff、mypy） |

### 2.2 创建共享工具库

新建 `shared/python/` 模块，包含：
- `env_utils.py` - 环境变量处理
- `input_validation.py` - 输入验证和清理
- `api_utils.py` - 安全的 API 请求封装

### 2.3 推荐代码改进

1. <strong>类型注解覆盖</strong>
   - 为所有 Python 文件添加类型注解
   - 在所有 TS 项目中启用严格的 TypeScript 模式

2. <strong>文档规范</strong>
   - 为所有 Python 函数添加 docstring
   - 为所有 JavaScript/TypeScript 函数添加 JSDoc 注释

3. <strong>测试框架</strong>
   - 添加 pytest 配置和示例测试_（已完成：`pyproject.toml` 中配置 pytest；共享工具的示例测试位于 [`tests/`](../../../tests)，并在 CI 中执行）_
   - 添加 JavaScript/TypeScript 的 Jest 配置

---

## 3. 教学改进

### 3.1 新增课程主题

1. **AI 应用中的安全**（拟定课程 22）
   - 提示注入攻击与防御
   - API 密钥管理
   - 内容审核
   - 限流与滥用防护

2. <strong>生产环境部署</strong>（拟定课程 23）
   - 使用 Docker 容器化
   - CI/CD 流水线
   - 监控与日志记录
   - 成本管理

3. **高级检索增强生成（RAG）技术**（拟定课程 24）
   - 混合搜索（关键词 + 语义）
   - 重新排序策略
   - 多模态 RAG
   - 评估指标

### 3.2 现有课程改进

| 课程 | 推荐改进 |
|--------|------------------------|
| 06 - 文本生成 | 增加流式响应示例 |
| 07 - 聊天应用 | 增加对话记忆模式 |
| 08 - 搜索应用 | 增加向量数据库对比 |
| 09 - 图像生成 | 增加图像编辑/变体示例 |
| 11 - 函数调用 | 增加并行函数调用 |
| 15 - RAG | 增加切片策略对比 |
| 17 - AI 代理 | 增加多代理编排 |

---

## 4. API 现代化

### 4.1 弃用的 API 模式（已迁移完成）

所有 Python 和 TypeScript <strong>聊天</strong>示例已经从 Chat Completions API 迁移到 **Responses API**（`client.responses.create(...)` → `response.output_text`）。

| 旧模式 | 新模式 | 状态 |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()`（聊天）| `OpenAI(base_url="<endpoint>/openai/v1/")`（Responses API）| 已完成 |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | 已完成 |
| `@azure/openai` `OpenAIClient.getChatCompletions()`（TypeScript）| `openai` 包的 `client.responses.create()` → `response.output_text` | 已完成 |
| `df.append()`（pandas）| `pd.concat()` | 已完成 |

> **注意：** 使用 `azure-ai-inference` / `@azure-rest/ai-inference` SDK (`client.complete()`) 的微软 Foundry 模型示例仍然使用模型推理 API，该 API 不支持 Responses API。`AzureOpenAI()` 在仍有效的场景（如嵌入和图像生成）中被有意保留。

### 4.2 演示的新 API 功能

1. <strong>结构化输出</strong>（OpenAI）
   - JSON 模式
   - 具有严格架构的函数调用

2. <strong>视觉能力</strong>
   - 通过 GPT-4o（视觉）进行图像分析
   - 多模态提示

3. **Responses API 内置工具**（替代传统助理 API）
   - 代码解释器
   - 文件搜索
   - 网络搜索和自定义工具

---

## 5. 基础设施改进

### 5.1 CI/CD 改进

已在 [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml) 实现：对维护的 `shared/` 工具模块强制执行 Python 静态检查和格式化（Ruff + Black），对其他课程采用建议性执行，并为 JavaScript/TypeScript 运行建议性 ESLint 检查。示例基线如下：

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

已在 [`.github/workflows/security.yml`](../../../.github/workflows/security.yml) 实现：Python 和 JavaScript/TypeScript 的 CodeQL 分析（推送、拉取请求及每周计划触发），以及拉取请求上的依赖项审查。示例基线如下：

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

### 6.1 DevContainer 改进

已在 [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) 和 [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh) 实现：容器现在包含 Pylance、Black 格式化工具、Ruff、ESLint、Prettier 及 Copilot 插件，启用基于仓库 Black/Prettier 配置的保存时自动格式化，并安装开发工具链（`ruff`、`black`、`mypy`、`pytest`），以支持本地重现 [代码质量工作流](../../../.github/workflows/code-quality.yml)。`mcr.microsoft.com/devcontainers/universal` 基础镜像已捆绑 Python 和 Node，无需添加额外功能。示例基线如下：

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

### 6.2 交互式演示环境

建议添加：
- 配置预置 API 密钥（通过环境变量）的 Jupyter 笔记本
- 适合视觉学习者的 Gradio/Streamlit 演示
- 用于知识评估的交互式测验

---

## 7. 多语言支持

### 7.1 现有语言覆盖

| 技术 | 涵盖课程 | 状态 |
|------------|-----------------|--------|
| Python | 全部 | 完整 |
| TypeScript | 06-09, 11 | 部分 |
| JavaScript | 06-08, 11 | 部分 |
| .NET/C# | 部分 | 部分 |

### 7.2 推荐新增

1. **Go** - AI/ML 工具有增长趋势
2. **Rust** - 性能关键应用
3. **Java/Kotlin** - 企业级应用

---

## 8. 性能优化

### 8.1 代码级优化

1. **异步/等待模式**
   - 添加批处理异步示例
   - 演示并发 API 调用

2. <strong>缓存策略</strong>
   - 添加嵌入缓存示例
   - 演示响应缓存模式

3. <strong>令牌优化</strong>
   - 添加 tiktoken 使用示例
   - 演示提示压缩技术

### 8.2 成本优化示例

添加示例演示：
- 根据任务复杂度选择模型
- 针对令牌效率进行提示工程
- 批量处理以支持大规模操作

---

## 9. 无障碍与国际化

### 9.1 当前翻译状态

所有翻译均已<strong>完成</strong>，并由 [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) 自动生成，该工具保持50多种语言版本课程与英文原版同步。翻译内容保存在 `translations/` 下，本地化图像保存在 `translated_images/`；完整语言列表发布在仓库 README 顶部。

| 方面 | 状态 |
|--------|--------|
| 翻译覆盖 | 完整 — 50+ 语言，涵盖全部课程 |
| 翻译方式 | 由 [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) 自动完成 |
| 与英文原版同步 | 是 — 自动再生成 |

### 9.2 无障碍改进

1. 为所有图像增加 alt 文本
2. 确保代码示例具有合适的语法高亮
3. 为所有视频内容添加文字记录
4. 确保色彩对比符合 WCAG 指南

---

## 10. 实施优先级

### 阶段 1：立即执行（第1-2周）
- [x] 修复关键安全问题
- [x] 添加代码质量配置
- [x] 创建共享工具库
- [x] 编写安全指南文档

### 阶段 2：短期（第3-4周）
- [x] 更新弃用的 API 模式（Chat Completions → Responses API，Python + TypeScript）
- [ ] 为所有 Python 文件添加类型注解（维护的 `shared/` 模块已完成；课程示例保持简洁）
- [x] 添加 CI/CD 工作流以保证代码质量
- [x] 创建安全扫描工作流

### 阶段 3：中期（第2-3个月）
- [ ] 添加新安全课程
- [ ] 添加生产环境部署课程
- [x] 改进 DevContainer 配置
- [ ] 添加交互式演示

### 阶段 4：长期（第4个月及以后）
- [ ] 添加高级 RAG 课程
- [ ] 扩展语言支持
- [ ] 添加全面测试套件
- [ ] 创建认证项目

---

## 结论

本路线图为改进“生成式人工智能初学者”课程提供了结构化的方法。通过解决安全问题、现代化 API 以及丰富教学内容，该课程将更好地帮助学生准备现实的 AI 应用开发。

如有问题或贡献建议，请在 GitHub 仓库提交 issue。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->