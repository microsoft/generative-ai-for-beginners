<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T14:31:08+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "zh"
}
-->
# 开始学习本课程

我们非常期待你开始这门课程，看看你会受到什么启发，利用生成式 AI 构建出怎样的项目！

为了帮助你顺利学习，本页将介绍环境配置步骤、技术要求，以及遇到问题时的求助方式。

## 配置步骤

要开始学习本课程，你需要完成以下步骤。

### 1. Fork 本仓库

[将整个仓库 Fork 到你的 GitHub 账号](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)，这样你就可以修改代码并完成挑战。你也可以[为本仓库加星 (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)，方便以后查找本仓库及相关项目。

### 2. 创建 codespace

为避免运行代码时出现依赖问题，我们推荐你在 [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) 中学习本课程。

在你的 fork 仓库中：**Code -> Codespaces -> New on main**

![显示创建 codespace 按钮的对话框](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 添加密钥

1. ⚙️ 齿轮图标 -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret。
2. 名称填写 OPENAI_API_KEY，粘贴你的密钥，保存。

### 3. 接下来做什么？

| 我想要…              | 前往…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| 开始第一课           | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| 离线学习             | [`setup-local.md`](02-setup-local.md)                                   |
| 配置 LLM 服务商      | [`providers.md`](providers.md)                                          |
| 结识其他学习者       | [加入我们的 Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 故障排查

| 症状                                       | 解决方法                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| 容器构建卡住超过 10 分钟                   | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | 终端未连接；点击 **+** ➜ *bash*                                  |
| OpenAI 返回 `401 Unauthorized`            | `OPENAI_API_KEY` 错误或已过期                                   |
| VS Code 显示 “Dev container mounting…”    | 刷新浏览器标签页——Codespaces 有时会断开连接                     |
| Notebook 内核缺失                         | Notebook 菜单 ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix 系统：

   ```bash
   touch .env
   ```

   Windows：

   ```cmd
   echo . > .env
   ```

3. **编辑 `.env` 文件**：用文本编辑器（如 VS Code、Notepad++ 或其他编辑器）打开 `.env` 文件。添加如下内容，将 `your_github_token_here` 替换为你的 GitHub token：

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **保存文件**：保存更改并关闭编辑器。

5. **安装 `python-dotenv`**：如果还没安装，需要用 `pip` 安装 `python-dotenv` 包，以便从 `.env` 文件加载环境变量：

   ```bash
   pip install python-dotenv
   ```

6. **在 Python 脚本中加载环境变量**：在你的 Python 脚本中，使用 `python-dotenv` 包加载 `.env` 文件中的环境变量：

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

就这样！你已经成功创建了 `.env` 文件，添加了 GitHub token，并将其加载到 Python 应用中。

## 如何在本地运行

如果你想在本地电脑上运行代码，需要先[安装 Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)。

然后克隆仓库：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

一切准备好后，就可以开始啦！

## 可选步骤

### 安装 Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是一个轻量级的 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst) 和 Python 安装器，还包含一些常用包。
Conda 是一个包管理器，可以方便地创建和切换不同的 Python [**虚拟环境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) 及包。对于那些 `pip` 无法安装的包，Conda 也很有用。

你可以参考 [MiniConda 安装指南](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) 进行安装。

安装好 Miniconda 后，需要克隆[本仓库](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)（如果还没克隆的话）。

接下来需要创建一个虚拟环境。用 Conda 创建新环境文件（_environment.yml_）。如果你在 Codespaces 中操作，请在 `.devcontainer` 目录下创建，即 `.devcontainer/environment.yml`。

将下面的内容填入你的环境文件：

```yml
name: <environment-name>
channels:
  - defaults
  - microsoft
dependencies:
  - python=<python-version>
  - openai
  - python-dotenv
  - pip
  - pip:
      - azure-ai-ml
```

如果你在使用 conda 时遇到错误，可以在终端手动安装 Microsoft AI 库，命令如下：

```
conda install -c microsoft azure-ai-ml
```

环境文件中指定了所需依赖。`<environment-name>` 是你想为 Conda 环境起的名字，`<python-version>` 是你想用的 Python 版本，比如 `3` 代表最新主版本。

完成后，在命令行/终端运行以下命令创建 Conda 环境：

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

如果遇到问题，可以参考 [Conda 环境管理指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

### 在 Visual Studio Code 中使用 Python 扩展

我们推荐你在本课程中使用 [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) 编辑器，并安装 [Python 扩展](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)。当然，这只是推荐，并非强制要求。

> **Note**: 打开课程仓库时，VS Code 会提示你可以在容器中配置项目。这是因为仓库中有一个特殊的 [.devcontainer](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 目录。后面会详细介绍。

> **Note**: 克隆并打开目录后，VS Code 会自动建议你安装 Python 扩展。

> **Note**: 如果 VS Code 建议你在容器中重新打开仓库，请拒绝，以便使用本地安装的 Python。

### 在浏览器中使用 Jupyter

你也可以直接在浏览器中使用 [Jupyter 环境](https://jupyter.org?WT.mc_id=academic-105485-koreyst)进行项目开发。无论是经典 Jupyter 还是 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) 都提供了很好的开发体验，比如自动补全、代码高亮等。

要在本地启动 Jupyter，请在终端/命令行进入课程目录，执行：

```bash
jupyter notebook
```

或

```bash
jupyterhub
```

这样会启动一个 Jupyter 实例，命令行窗口会显示访问的 URL。

访问该 URL 后，你会看到课程大纲，并可以浏览任意 `*.ipynb` 文件。例如，`08-building-search-applications/python/oai-solution.ipynb`。

### 在容器中运行

除了在本地或 Codespace 配置环境外，你还可以使用 [容器](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)。课程仓库中的 `.devcontainer` 文件夹让 VS Code 可以在容器中配置项目。如果不是在 Codespaces 中，这需要你安装 Docker，操作相对复杂，建议有容器经验的同学使用。

在 GitHub Codespaces 中保护 API 密钥的最佳方式之一是使用 Codespace Secrets。请参考 [Codespaces 密钥管理指南](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) 了解更多信息。

## 课程内容与技术要求

本课程包含 6 节概念课和 6 节编程课。

在编程课中，我们使用 Azure OpenAI 服务。你需要有 Azure OpenAI 服务的访问权限和 API 密钥才能运行代码。你可以[填写申请表](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)获取访问权限。

在等待申请审核期间，每节编程课的 `README.md` 文件中都可以查看代码和输出结果。

## 第一次使用 Azure OpenAI 服务

如果你是第一次使用 Azure OpenAI 服务，请参考此指南，了解如何[创建并部署 Azure OpenAI 服务资源](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)。

## 第一次使用 OpenAI API

如果你是第一次使用 OpenAI API，请参考[创建和使用接口的指南](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)。

## 结识其他学习者

我们在官方 [AI Community Discord 服务器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) 上为大家创建了交流频道。这里是结识志同道合的创业者、开发者、学生，以及所有想在生成式 AI 领域提升自我的人的好地方。

[![加入 discord 频道](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

项目团队成员也会在 Discord 上为大家提供帮助。

## 贡献

本课程是一个开源项目。如果你发现有改进空间或问题，请提交 [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) 或记录 [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

项目团队会跟踪所有贡献。参与开源是提升你在生成式 AI 领域职业发展的绝佳方式。

大多数贡献需要你同意贡献者许可协议（CLA），声明你有权并同意授予我们使用你贡献内容的权利。详情请访问 [CLA, 贡献者许可协议网站](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)。

重要提示：在翻译本仓库内容时，请确保不要使用机器翻译。我们会通过社区审核翻译内容，因此请只在你精通的语言下自愿参与翻译。

当你提交 pull request 时，CLA-bot 会自动判断你是否需要签署 CLA，并在 PR 上做出相应标记（如标签、评论）。只需按照 bot 的指示操作即可。你只需在所有使用我们 CLA 的仓库中做一次此操作。

本项目采用了 [Microsoft 开源行为准则](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)。更多信息请阅读行为准则 FAQ，或通过 [Email opencode](opencode@microsoft.com) 联系我们提出问题或建议。

## 让我们开始吧
现在你已经完成了本课程所需的步骤，让我们开始吧，首先来了解一下[生成式人工智能和大语言模型的简介](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)。

---

**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文件应被视为权威来源。对于关键信息，建议采用专业人工翻译。因使用本翻译而产生的任何误解或误读，我们概不负责。