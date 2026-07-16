# AGENTS.md

## 项目概览

本仓库包含一个涵盖生成式人工智能基础知识及应用开发的完整21课课程。课程面向初学者，涵盖从基本概念到构建生产就绪应用的全部内容。

**关键技术：**
- Python 3.9+，使用库：`openai`、`python-dotenv`、`tiktoken`、`azure-ai-inference`、`pandas`、`numpy`、`matplotlib`
- TypeScript/JavaScript，基于 Node.js，使用库：`openai`（通过v1端点和Responses API访问Azure OpenAI）、`@azure-rest/ai-inference`（Microsoft Foundry 模型）
- Azure OpenAI 服务、OpenAI API 和 Microsoft Foundry 模型（GitHub Models 将于2026年7月底退休）
- 使用 Jupyter 笔记本进行交互式学习
- 使用开发容器保持一致的开发环境

**仓库结构：**
- 包含 21 章节的编号目录（00-21），包括 README 文档、代码示例和作业
- 多种实现方式：Python、TypeScript，有时包含 .NET 示例
- translations 目录下提供40多种语言版本
- 通过 `.env` 文件实现集中配置（使用 `.env.copy` 作为模板）

## 安装命令

### 初始仓库设置

```bash
# 克隆仓库
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# 复制环境模板
cp .env.copy .env
# 用您的API密钥和端点编辑.env
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
# 安装根级依赖项（用于文档工具）
npm install

# 对于单个课程的 TypeScript 示例，导航到特定课程：
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### 开发容器设置（推荐）

仓库包含 `.devcontainer` 配置，支持 GitHub Codespaces 或 VS Code 开发容器：

1. 在 GitHub Codespaces 或已安装开发容器扩展的 VS Code 中打开仓库
2. 开发容器将自动：
   - 从 `requirements.txt` 安装 Python 依赖
   - 运行后置创建脚本（`.devcontainer/post-create.sh`）
   - 设置 Jupyter 内核

## 开发工作流程

### 环境变量

需要调用 API 的所有课程使用定义在 `.env` 文件中的环境变量：

- `OPENAI_API_KEY` - 用于 OpenAI API
- `AZURE_OPENAI_API_KEY` - 用于 Microsoft Foundry 中的 Azure OpenAI（Azure OpenAI 服务现已成为 Microsoft Foundry 的一部分：https://ai.azure.com）
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI 端点 URL（Foundry 资源端点）
- `AZURE_OPENAI_DEPLOYMENT` - 聊天完成模型部署名称
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - 嵌入模型部署名称
- `AZURE_OPENAI_API_VERSION` - API 版本（默认：`2024-10-21`）
- `HUGGING_FACE_API_KEY` - 用于 Hugging Face 模型
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry 模型端点（多厂商模型目录）
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry 模型 API 密钥（替代即将退休的 `GITHUB_TOKEN`）

### 运行 Python 示例

```bash
# 导航到课程目录
cd 06-text-generation-apps/python

# 运行一个Python脚本
python aoai-app.py
```

### 运行 TypeScript 示例

```bash
# 导航到 TypeScript 应用程序目录
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

# 或者使用带有 Jupyter 扩展的 VS Code
```

### 处理不同类型的课程

- **“学习”课程**：专注于 README.md 文档和概念
- **“构建”课程**：包括 Python 和 TypeScript 的工作代码示例
- 每个课程都有 README.md，包含理论、代码讲解和视频链接

## 代码风格指南

### Python

- 使用 `python-dotenv` 管理环境变量
- 导入 `openai` 库用于 API 交互
- 使用 `pylint` 进行代码检查（部分示例为了简单包含了 `# pylint: disable=all`）
- 遵循 PEP 8 命名规范
- 将 API 凭据存储在 `.env` 文件中，绝不硬编码于代码

### TypeScript

- 使用 `dotenv` 包管理环境变量
- 每个应用在 `tsconfig.json` 中进行 TypeScript 配置
- 使用 `openai` 包访问 Azure OpenAI（客户端指向 `/openai/v1/` 端点并调用 `client.responses.create`）；使用 `@azure-rest/ai-inference` 访问 Microsoft Foundry 模型
- 使用 `nodemon` 开发时自动重载
- 运行前需先构建：`npm run build`，然后 `npm start`

### 通用约定

- 保持代码示例简洁且具有教学意义
- 添加注释解释关键概念
- 每个课程的代码应自包含且可运行
- 使用统一命名：`aoai-` 前缀表示 Azure OpenAI，`oai-` 表示 OpenAI API，`githubmodels-` 表示 Microsoft Foundry 模型（遗留自 GitHub Models 时代）

## 文档指南

### Markdown 风格

- 所有 URL 必须使用 `[text](../../url)` 格式包裹，无额外空格
- 相对链接必须以 `./` 或 `../` 开头
- 所有指向 Microsoft 域名的链接必须包含跟踪 ID：`?WT.mc_id=academic-105485-koreyst`
- URL 中不允许包含国家/地区特定的本地化路径（避免 `/en-us/`）
- 图片存储在 `./images` 文件夹，文件名具有描述性
- 文件名使用英文字母、数字和连字符

### 翻译支持

- 仓库通过自动化 GitHub Actions 支持40多种语言版本
- 翻译存储在 `translations/` 目录
- 不接受部分翻译提交
- 不接受机器翻译稿
- 翻译后的图片存储在 `translated_images/` 目录

## 测试与验证

### 提交前检查

本仓库使用 GitHub Actions 进行验证。提交 PR 前请：

1. **检查 Markdown 链接**：
   ```bash
   # validate-markdown.yml 工作流检查：
   # - 损坏的相对路径
   # - 路径上缺少跟踪 ID
   # - URL 上缺少跟踪 ID
   # - 含有国家/地区语言环境的 URL
   # - 损坏的外部 URL
   ```

2. <strong>手动测试</strong>：
   - 测试 Python 示例：激活虚拟环境并运行脚本
   - 测试 TypeScript 示例：`npm install`、`npm run build`、`npm start`
   - 确认环境变量配置正确
   - 确认 API 密钥能用于代码示例

3. <strong>代码示例</strong>：
   - 确保所有代码运行无误
   - 在适用情况下同时测试 Azure OpenAI 和 OpenAI API
   - 在支持处测试 Microsoft Foundry 模型

### 无自动化测试

这是一个以教程和示例为主的教育仓库，无单元测试或集成测试。验证主要依赖于：
- 代码示例的手动测试
- GitHub Actions 进行 Markdown 验证
- 社区对教学内容的审查

## 拉取请求指南

### 提交前

1. 在适用情况下测试 Python 和 TypeScript 代码更改
2. 运行 Markdown 验证（PR 自动触发）
3. 确保所有 Microsoft URL 均包含跟踪 ID
4. 检查相对链接有效性
5. 确认图片引用正确

### PR 标题格式

- 使用描述性标题：`[Lesson 06] Fix Python example typo` 或 `Update README for lesson 08`
- 如适用，引用相关问题编号：`Fixes #123`

### PR 描述

- 说明更改内容及原因
- 链接相关问题
- 针对代码更改，说明测试了哪些示例
- 针对翻译 PR，确保包含所有文件以保证完整翻译

### 贡献要求

- 签署 Microsoft CLA（首次 PR 自动完成）
- 在修改前先将仓库 fork 到个人帐户
- 一次 PR 只做一个逻辑更改（不要合并无关修复）
- 尽量保持 PR 精简并聚焦

## 常用工作流程

### 添加新代码示例

1. 进入相应课程目录
2. 在 `python/` 或 `typescript/` 子目录创建示例
3. 遵循命名规范：`{provider}-{example-name}.{py|ts|js}`
4. 使用真实 API 凭据测试
5. 在课程 README 中记录新增的环境变量

### 更新文档

1. 编辑课程目录下的 README.md
2. 遵守 Markdown 规范（跟踪 ID，相对链接）
3. 翻译由 GitHub Actions 处理（勿手动编辑）
4. 确认所有链接有效

### 使用开发容器

1. 仓库包含 `.devcontainer/devcontainer.json`
2. 后置创建脚本自动安装 Python 依赖
3. 预配置 Python 和 Jupyter 扩展
4. 基于 `mcr.microsoft.com/devcontainers/universal:2.11.2` 镜像

## 部署与发布

这是一个学习型仓库，没有部署流程。课程内容通过以下方式访问：

1. **GitHub 仓库**：直接访问代码和文档
2. **GitHub Codespaces**：预配置环境的即时开发空间
3. **Microsoft Learn**：内容可能会同步到官方学习平台
4. **docsify**：基于 Markdown 构建的文档网站（参见 `docsifytopdf.js` 和 `package.json`）

### 构建文档网站

```bash
# 从文档生成 PDF（如果需要）
npm run convert
```

## 故障排除

### 常见问题

**Python 导入错误**：
- 确认虚拟环境已激活
- 运行 `pip install -r requirements.txt`
- 检查 Python 版本是否为 3.9 以上

**TypeScript 编译错误**：
- 在对应应用目录运行 `npm install`
- 检查 Node.js 版本是否兼容
- 如有需要，删除 `node_modules` 并重新安装依赖

**API 认证错误**：
- 确认存在 `.env` 文件且值正确
- 检查 API 密钥有效且未过期
- 确认端点 URL 符合所在地区

<strong>缺少环境变量</strong>：
- 将 `.env.copy` 复制为 `.env`
- 填写当前课程所需的所有值
- 更新 `.env` 后重启应用

## 额外资源

- [课程安装指南](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [贡献指南](./CONTRIBUTING.md)
- [行为准则](./CODE_OF_CONDUCT.md)
- [安全政策](./SECURITY.md)
- [Azure AI Discord 群组](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [高级代码示例合集](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## 项目特别说明

- 本仓库为<strong>教育性质</strong>，专注于学习，不是生产环境代码
- 示例代码刻意简洁，重点教学概念
- 代码质量与教学清晰度平衡
- 每课独立完结，可单独完成
- 支持多种 API 提供商：Azure OpenAI、OpenAI、Microsoft Foundry 模型及离线提供商如 Foundry Local 和 Ollama
- 内容多语言支持，并有自动化翻译流程
- Discord 社区活跃，提供问题解答与支持

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->