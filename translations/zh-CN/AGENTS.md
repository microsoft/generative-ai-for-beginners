# AGENTS.md

## 项目概览

本仓库包含一个全面的21课课程，教授生成式人工智能基础知识及应用开发。该课程为初学者设计，涵盖从基础概念到构建生产就绪应用的所有内容。

**关键技术：**
- Python 3.9+和库：`openai`、`python-dotenv`、`tiktoken`、`azure-ai-inference`、`pandas`、`numpy`、`matplotlib`
- TypeScript/JavaScript 搭配 Node.js 和库：`openai`（通过v1端点+Responses API使用 Azure OpenAI），`@azure-rest/ai-inference`（微软 Foundry 模型）
- Azure OpenAI 服务、OpenAI API 和微软 Foundry 模型（GitHub Models 将于2026年7月底退役）
- 用于交互式学习的 Jupyter 笔记本
- 用于一致开发环境的开发容器

**仓库结构：**
- 21个编号课程目录（00-21），包含 README、代码示例和作业
- 多种实现：Python、TypeScript，有时还包括.NET示例
- 翻译目录，包含40多种语言版本
- 通过 `.env` 文件集中配置（使用 `.env.copy` 作为模板）

## 设置命令

### 初始仓库设置

```bash
# 克隆仓库
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# 复制环境模板
cp .env.copy .env
# 使用你的API密钥和端点编辑.env
```

### Python 环境设置

```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
# 在 macOS/Linux 上：
source venv/bin/activate
# 在 Windows 上：
venv\Scripts\activate

# 安装依赖项
pip install -r requirements.txt
```

### Node.js/TypeScript 设置

```bash
# 安装根级依赖（用于文档工具）
npm install

# 对于单个课程的 TypeScript 示例，导航到特定课程：
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### 开发容器设置（推荐）

仓库包含 `.devcontainer` 配置，可用于 GitHub Codespaces 或 VS Code 开发容器：

1. 在 GitHub Codespaces 或安装了开发容器扩展的 VS Code 中打开仓库
2. 开发容器将自动：
   - 从 `requirements.txt` 安装 Python 依赖
   - 运行创建后脚本（`.devcontainer/post-create.sh`）
   - 设置 Jupyter 内核

## 开发工作流程

### 环境变量

所有需要 API 访问的课程都使用在 `.env` 中定义的环境变量：

- `OPENAI_API_KEY` - OpenAI API 密钥
- `AZURE_OPENAI_API_KEY` - Microsoft Foundry 中 Azure OpenAI 的密钥（Azure OpenAI 服务现为 Microsoft Foundry 的一部分：https://ai.azure.com）
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI 端点 URL（Foundry 资源端点）
- `AZURE_OPENAI_DEPLOYMENT` - 聊天补全模型部署名称（课程默认：`gpt-5-mini`）
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - 嵌入模型部署名称（课程默认：`text-embedding-3-small`）
- `AZURE_OPENAI_API_VERSION` - API 版本（默认：`2024-10-21`）
- `HUGGING_FACE_API_KEY` - Hugging Face 模型密钥
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry 模型端点（多提供者模型目录）
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry 模型 API 密钥（替代即将退役的 `GITHUB_TOKEN`）
- `AZURE_INFERENCE_CHAT_MODEL` - 一个非推理模型（例如 `Llama-3.3-70B-Instruct`），用于 `temperature` 示例，因为推理模型不支持采样控制

### 模型约定（重要）

- **默认聊天模型为 `gpt-5-mini`<strong> - 当前非弃用的 </strong>推理** 模型。自2026年起，旧的支持 temperature 的“迷你”模型（`gpt-4o-mini`、`gpt-4.1-mini`）将<em>弃用</em>，课程统一采用 GPT-5 家族。
- **推理模型拒绝 `temperature` 和 `top_p`**，使用 `max_output_tokens`（Responses API） / `max_completion_tokens`（聊天补全）替代 `max_tokens`。调用 `gpt-5-mini` 的示例中切勿添加 `temperature`/`top_p`/`max_tokens`。
- **为演示 `temperature`**，示例使用 Microsoft Foundry 模型端点的 **Llama** 模型（`Llama-3.3-70B-Instruct`，通过 `AZURE_INFERENCE_CHAT_MODEL`）。推理模型请通过提示工程和推理控制代替采样调节。
- **微调（第18课）** 保留 `gpt-4.1-mini`：GPT-5 仅支持强化学习微调（RFT），不支持该处展示的监督式微调（SFT）。
- 第20（Mistral）和21课（Meta）保留 `temperature`/`max_tokens`，因为它们面向支持这些参数的 Mistral/Llama 模型。

### 运行 Python 示例

```bash
# 导航到课程目录
cd 06-text-generation-apps/python

# 运行一个Python脚本
python aoai-app.py
```

### 运行 TypeScript 示例

```bash
# 导航到 TypeScript 应用目录
cd 06-text-generation-apps/typescript/recipe-app

# 构建 TypeScript 代码
npm run build

# 运行应用程序
npm start
```

### 运行 Jupyter 笔记本

```bash
# 在仓库根目录启动 Jupyter
jupyter notebook

# 或使用带有 Jupyter 扩展的 VS Code
```

### 各类课程作业方式

- **“学习”课程**：专注于 README.md 文档和概念讲解
- **“构建”课程**：包含 Python 和 TypeScript 工作代码示例
- 每节课均含有包含理论、代码讲解及视频内容链接的 README.md

## 代码风格指南

### Python

- 使用 `python-dotenv` 管理环境变量
- 导入 `openai` 库进行 API 交互
- 使用 `pylint` 进行代码检查（部分示例为了简单使用了 `# pylint: disable=all`）
- 遵循 PEP 8 命名规范
- 将 API 凭证存储在 `.env` 文件，代码中绝不硬编码

### TypeScript

- 使用 `dotenv` 包管理环境变量
- 每个应用在 `tsconfig.json` 中配置 TypeScript
- 使用 `openai` 包调用 Azure OpenAI（客户端指向 `/openai/v1/` 端点并调用 `client.responses.create`）；使用 `@azure-rest/ai-inference` 调用微软 Foundry 模型
- 使用 `nodemon` 进行开发，支持自动重载
- 运行前先构建：`npm run build` 然后 `npm start`

### 通用约定

- 保持示例代码简单且具教育性
- 添加注释解释关键概念
- 每节课的代码应相互独立且可直接运行
- 命名风格统一：`aoai-` 前缀表示 Azure OpenAI，`oai-` 表示 OpenAI API，`githubmodels-` 表示微软 Foundry 模型（保留 GitHub Models 时代的遗留前缀）

## 文档指南

### Markdown 风格

- 所有 URL 必须使用 `[文本](../../链接)` 格式，不得有额外空格
- 相对链接必须以 `./` 或 `../` 开头
- 所有指向 Microsoft 域名的链接必须包含跟踪 ID：`?WT.mc_id=academic-105485-koreyst`
- 不使用针对特定国家的 URL 语言路径（避免 `/en-us/`）
- 图片存于 `./images` 文件夹，文件名具描述性
- 文件名使用英文字母、数字和短横线

### 翻译支持

- 仓库通过自动化 GitHub Actions 支持40多种语言
- 翻译文件位于 `translations/` 目录
- 不接受部分翻译提交
- 不接受机器翻译
- 翻译后的图片存放于 `translated_images/` 目录

## 测试与验证

### 提交前检查

本仓库使用 GitHub Actions 进行验证。提交 PR 前：

1. **检查 Markdown 链接：**
   ```bash
   # validate-markdown.yml 工作流检查：
   # - 断开的相对路径
   # - 路径上缺失的跟踪ID
   # - URL上缺失的跟踪ID
   # - 带有国家/地区语言代码的URL
   # - 断开的外部URL
   ```

2. **人工测试：**
   - 测试 Python 示例：激活虚拟环境并运行脚本
   - 测试 TypeScript 示例：`npm install`，`npm run build`，`npm start`
   - 检查环境变量是否正确配置
   - 确认 API 密钥对代码示例有效

3. **代码示例：**
   - 确保所有代码无错误运行
   - 涉及时同时测试 Azure OpenAI 和 OpenAI API
   - 验证受支持时的微软 Foundry 模型示例有效

### 无自动化测试

这是一个专注于教程和示例的教育仓库，无单元测试或集成测试。验证主要通过：
- 代码示例的人工测试
- GitHub Actions 的 Markdown 验证
- 教育内容的社区审核

## 拉取请求指南

### 提交前

1. 在 Python 和 TypeScript 中测试代码更改（适用时）
2. 运行 Markdown 验证（PR 提交自动触发）
3. 确保所有 Microsoft URL 带有跟踪 ID
4. 检查相对链接有效
5. 确认图片引用正确

### PR 标题格式

- 使用描述性标题：`[Lesson 06] 修正 Python 示例拼写错误` 或 `更新第08课 README`
- 相关时引用 Issue 号码：`Fixes #123`

### PR 描述

- 说明更改内容及原因
- 链接相关 Issue
- 对代码更改说明测试覆盖示例
- 语言翻译 PR 包含所有相关文件以完成翻译

### 贡献要求

- 签署 Microsoft CLA（第一次 PR 自动）
- 更改前先 Fork 仓库至个人账户
- 每个逻辑变更一个 PR（避免合并不相关修复）
- 尽量保持 PR 简洁聚焦

## 常用工作流程

### 添加新代码示例

1. 进入相应的课程目录
2. 在 `python/` 或 `typescript/` 子目录创建示例
3. 遵循命名规则：`{provider}-{example-name}.{py|ts|js}`
4. 使用真实 API 凭证测试
5. 在课程 README 中记录任何新增环境变量

### 更新文档

1. 编辑课程目录下的 README.md
2. 遵循 Markdown 指南（跟踪 ID、相对链接）
3. 翻译由 GitHub Actions 处理（请勿手动编辑）
4. 测试所有链接有效

### 使用开发容器

1. 仓库包含 `.devcontainer/devcontainer.json`
2. 创建后脚本自动安装 Python 依赖
3. 预配置了 Python 和 Jupyter 扩展
4. 环境基于 `mcr.microsoft.com/devcontainers/universal:2.11.2`

## 部署与发布

这是一个学习型仓库 - 无部署流程。课程使用方式：

1. **GitHub 仓库**：直接访问代码和文档
2. **GitHub Codespaces**：即时预配置的开发环境
3. **Microsoft Learn**：内容可能被联合发布到官方学习平台
4. **docsify**：基于 Markdown 构建的文档网站（见 `docsifytopdf.js` 和 `package.json`）

### 构建文档网站

```bash
# 从文档生成 PDF（如果需要）
npm run convert
```

## 故障排查

### 常见问题

**Python 导入错误**：
- 确保虚拟环境已激活
- 运行 `pip install -r requirements.txt`
- 检查 Python 版本是否为 3.9+

**TypeScript 构建错误**：
- 在具体应用目录运行 `npm install`
- 检查 Node.js 版本兼容性
- 如有需要清空 `node_modules` 并重新安装

**API 认证错误**：
- 确认 `.env` 文件存在且配置正确
- 确认 API 密钥有效且未过期
- 确认端点 URL 适合所在区域

<strong>缺少环境变量</strong>：
- 复制 `.env.copy` 为 `.env`
- 填写当前课程所需的所有值
- 更新 `.env` 后重启应用

## 其他资源

- [课程设置指南](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [贡献指南](./CONTRIBUTING.md)
- [行为准则](./CODE_OF_CONDUCT.md)
- [安全政策](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [高级代码示例合集](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## 项目特定说明

- 本仓库为<strong>教育用途</strong>，侧重学习，不是生产代码
- 示例代码设计简单，专注于教学概念
- 代码质量与教学清晰性保持平衡
- 每节课代码自成体系，能独立完成
- 支持多种 API 提供者：Azure OpenAI、OpenAI、微软 Foundry 模型，以及离线提供者如 Foundry Local 和 Ollama
- 内容多语言化，支持自动翻译工作流
- Discord 社区活跃，提供问答与支持

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->