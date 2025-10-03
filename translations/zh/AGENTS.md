<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T10:53:25+00:00",
  "source_file": "AGENTS.md",
  "language_code": "zh"
}
-->
# AGENTS.md

## 项目概述

此代码库包含一个全面的21课课程，教授生成式人工智能的基础知识和应用开发。课程专为初学者设计，涵盖从基本概念到构建生产级应用的所有内容。

**关键技术：**
- Python 3.9+及以下库：`openai`、`python-dotenv`、`tiktoken`、`azure-ai-inference`、`pandas`、`numpy`、`matplotlib`
- TypeScript/JavaScript及Node.js库：`@azure/openai`、`@azure-rest/ai-inference`、`openai`
- Azure OpenAI服务、OpenAI API和GitHub模型
- Jupyter Notebooks用于交互式学习
- Dev Containers提供一致的开发环境

**代码库结构：**
- 21个编号的课程目录（00-21），包含README文件、代码示例和作业
- 多种实现方式：Python、TypeScript，有时还有.NET示例
- 翻译目录，支持40多种语言版本
- 通过`.env`文件集中配置（使用`.env.copy`作为模板）

## 设置命令

### 初始代码库设置

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Python环境设置

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Node.js/TypeScript设置

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container设置（推荐）

代码库包含一个`.devcontainer`配置文件，可用于GitHub Codespaces或VS Code Dev Containers：

1. 在GitHub Codespaces或VS Code中打开代码库，安装Dev Containers扩展
2. Dev Container将自动：
   - 从`requirements.txt`安装Python依赖项
   - 运行创建后脚本（`.devcontainer/post-create.sh`）
   - 设置Jupyter内核

## 开发工作流程

### 环境变量

所有需要API访问的课程都使用`.env`中定义的环境变量：

- `OPENAI_API_KEY` - 用于OpenAI API
- `AZURE_OPENAI_API_KEY` - 用于Azure OpenAI服务
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI端点URL
- `AZURE_OPENAI_DEPLOYMENT` - 聊天完成模型的部署名称
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - 嵌入模型的部署名称
- `AZURE_OPENAI_API_VERSION` - API版本（默认：`2024-02-01`）
- `HUGGING_FACE_API_KEY` - 用于Hugging Face模型
- `GITHUB_TOKEN` - 用于GitHub模型

### 运行Python示例

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### 运行TypeScript示例

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### 运行Jupyter Notebooks

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### 处理不同类型的课程

- **“学习”课程**：专注于README.md文档和概念
- **“构建”课程**：包含Python和TypeScript的工作代码示例
- 每节课程都有一个README.md文件，包含理论、代码讲解和视频内容链接

## 代码风格指南

### Python

- 使用`python-dotenv`管理环境变量
- 导入`openai`库进行API交互
- 使用`pylint`进行代码检查（某些示例包含`# pylint: disable=all`以简化）
- 遵循PEP 8命名规范
- 将API凭据存储在`.env`文件中，切勿直接写入代码

### TypeScript

- 使用`dotenv`包管理环境变量
- 每个应用的TypeScript配置存储在`tsconfig.json`中
- 使用`@azure/openai`或`@azure-rest/ai-inference`与Azure服务交互
- 使用`nodemon`进行开发，支持自动重载
- 运行前需构建：`npm run build`然后`npm start`

### 通用约定

- 保持代码示例简单且具有教育意义
- 包含解释关键概念的注释
- 每节课程的代码应独立且可运行
- 使用一致的命名：`aoai-`前缀用于Azure OpenAI，`oai-`用于OpenAI API，`githubmodels-`用于GitHub模型

## 文档指南

### Markdown风格

- 所有URL必须使用`[文本](../../url)`格式包裹，且无额外空格
- 相对链接必须以`./`或`../`开头
- 所有指向Microsoft域的链接必须包含跟踪ID：`?WT.mc_id=academic-105485-koreyst`
- URL中不得包含国家/地区特定的语言代码（避免`/en-us/`）
- 图片存储在`./images`文件夹中，文件名需具有描述性
- 文件名使用英文字符、数字和短横线

### 翻译支持

- 代码库通过自动化GitHub Actions支持40多种语言
- 翻译存储在`translations/`目录中
- 不接受部分翻译
- 不接受机器翻译
- 翻译后的图片存储在`translated_images/`目录中

## 测试与验证

### 提交前检查

此代码库使用GitHub Actions进行验证。在提交PR之前：

1. **检查Markdown链接**：
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **手动测试**：
   - 测试Python示例：激活虚拟环境并运行脚本
   - 测试TypeScript示例：`npm install`，`npm run build`，`npm start`
   - 确保环境变量配置正确
   - 检查API密钥是否与代码示例匹配

3. **代码示例**：
   - 确保所有代码运行无错误
   - 在适用时测试Azure OpenAI和OpenAI API
   - 验证示例是否支持GitHub模型

### 无自动化测试

这是一个以教程和示例为重点的教育代码库，没有单元测试或集成测试。验证主要包括：
- 手动测试代码示例
- GitHub Actions进行Markdown验证
- 社区对教育内容的审查

## Pull Request指南

### 提交前

1. 在适用时测试Python和TypeScript代码更改
2. 运行Markdown验证（PR自动触发）
3. 确保所有Microsoft URL包含跟踪ID
4. 检查相对链接是否有效
5. 验证图片引用是否正确

### PR标题格式

- 使用描述性标题：`[Lesson 06] 修复Python示例中的拼写错误`或`更新第08课的README`
- 在适用时引用问题编号：`Fixes #123`

### PR描述

- 说明更改内容及原因
- 链接相关问题
- 对于代码更改，说明测试了哪些示例
- 对于翻译PR，包含所有文件以完成翻译

### 贡献要求

- 签署Microsoft CLA（首次PR时自动完成）
- 在修改前将代码库Fork到您的账户
- 每个逻辑更改提交一个PR（不要合并不相关的修复）
- 尽量保持PR专注且小型化

## 常见工作流程

### 添加新的代码示例

1. 转到相应的课程目录
2. 在`python/`或`typescript/`子目录中创建示例
3. 遵循命名规范：`{provider}-{example-name}.{py|ts|js}`
4. 使用实际API凭据进行测试
5. 在课程README中记录任何新的环境变量

### 更新文档

1. 编辑课程目录中的README.md
2. 遵循Markdown指南（跟踪ID、相对链接）
3. 翻译由GitHub Actions处理（不要手动编辑）
4. 测试所有链接是否有效

### 使用Dev Containers

1. 代码库包含`.devcontainer/devcontainer.json`
2. 创建后脚本自动安装Python依赖项
3. 预配置Python和Jupyter扩展
4. 环境基于`mcr.microsoft.com/devcontainers/universal:2.11.2`

## 部署与发布

这是一个学习代码库，没有部署流程。课程内容通过以下方式使用：

1. **GitHub代码库**：直接访问代码和文档
2. **GitHub Codespaces**：预配置的即时开发环境
3. **Microsoft Learn**：内容可能会同步到官方学习平台
4. **docsify**：从Markdown构建的文档网站（参见`docsifytopdf.js`和`package.json`）

### 构建文档网站

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## 故障排除

### 常见问题

**Python导入错误**：
- 确保虚拟环境已激活
- 运行`pip install -r requirements.txt`
- 检查Python版本是否为3.9+

**TypeScript构建错误**：
- 在特定应用目录中运行`npm install`
- 检查Node.js版本是否兼容
- 清除`node_modules`并重新安装

**API认证错误**：
- 验证`.env`文件是否存在且值正确
- 检查API密钥是否有效且未过期
- 确保端点URL与您的区域匹配

**缺少环境变量**：
- 将`.env.copy`复制为`.env`
- 填写您正在处理的课程所需的所有值
- 更新`.env`后重启应用

## 其他资源

- [课程设置指南](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [贡献指南](./CONTRIBUTING.md)
- [行为准则](./CODE_OF_CONDUCT.md)
- [安全政策](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [高级代码示例集合](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## 项目特定说明

- 这是一个**教育代码库**，专注于学习而非生产代码
- 示例有意保持简单，专注于教学概念
- 代码质量与教育清晰度之间保持平衡
- 每节课程都是独立的，可单独完成
- 代码库支持多个API提供商：Azure OpenAI、OpenAI和GitHub模型
- 内容支持多语言，具有自动化翻译工作流
- Discord社区活跃，可用于提问和支持

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。