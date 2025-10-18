<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-17T23:22:24+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "zh"
}
-->
# 开始学习本课程

我们非常高兴您开始学习本课程，并期待您通过生成式人工智能构建出令人惊叹的作品！

为了确保您的学习顺利进行，本页面概述了设置步骤、技术要求以及需要帮助时的获取方式。

## 设置步骤

要开始学习本课程，您需要完成以下步骤。

### 1. Fork 此代码库

[Fork 整个代码库](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)到您自己的 GitHub 账户，以便修改代码并完成挑战。您还可以[为此代码库加星标 (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)，以便更轻松地找到它和相关代码库。

### 2. 创建 Codespace

为了避免运行代码时出现依赖问题，我们建议您在 [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) 中运行本课程。

在您的 Fork 中：**Code -> Codespaces -> New on main**

![显示创建 Codespace 按钮的对话框](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 添加一个密钥

1. ⚙️ 齿轮图标 -> 命令面板 -> Codespaces : 管理用户密钥 -> 添加新密钥。
2. 命名为 OPENAI_API_KEY，粘贴您的密钥，保存。

### 3. 接下来做什么？

| 我想要…             | 前往…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| 开始第1课           | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| 离线学习            | [`setup-local.md`](02-setup-local.md)                                   |
| 设置 LLM 提供商      | [`providers.md`](03-providers.md)                                        |
| 认识其他学习者       | [加入我们的 Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 故障排除

| 症状                                     | 解决方法                                                         |
|-----------------------------------------|-----------------------------------------------------------------|
| 容器构建卡住超过10分钟                  | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`             | 终端未连接；点击 **+** ➜ *bash*                                 |
| OpenAI 返回 `401 Unauthorized`          | 错误或过期的 `OPENAI_API_KEY`                                   |
| VS Code 显示“Dev container mounting…”   | 刷新浏览器标签页—Codespaces 有时会失去连接                      |
| Notebook 内核丢失                       | Notebook 菜单 ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix 系统：

   ```bash
   touch .env
   ```

   Windows 系统：

   ```cmd
   echo . > .env
   ```

3. **编辑 `.env` 文件**：在文本编辑器中打开 `.env` 文件（例如 VS Code、Notepad++ 或其他编辑器）。将以下行添加到文件中，并将 `your_github_token_here` 替换为您的实际 GitHub 令牌：

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **保存文件**：保存更改并关闭文本编辑器。

5. **安装 `python-dotenv`**：如果尚未安装，您需要安装 `python-dotenv` 包，以便从 `.env` 文件中加载环境变量到您的 Python 应用程序。您可以使用 `pip` 安装：

   ```bash
   pip install python-dotenv
   ```

6. **在 Python 脚本中加载环境变量**：在您的 Python 脚本中，使用 `python-dotenv` 包从 `.env` 文件加载环境变量：

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

完成了！您已经成功创建了 `.env` 文件，添加了您的 GitHub 令牌，并将其加载到您的 Python 应用程序中。

## 如何在本地运行代码

要在本地运行代码，您需要安装某个版本的 [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)。

然后使用代码库，您需要克隆它：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

一旦完成所有操作，您就可以开始了！

## 可选步骤

### 安装 Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是一个轻量级安装程序，用于安装 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python 以及一些包。
Conda 本身是一个包管理器，可以轻松设置和切换不同的 Python [**虚拟环境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)和包。它还非常适合安装无法通过 `pip` 获取的包。

您可以按照 [MiniConda 安装指南](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst)进行设置。

安装 Miniconda 后，您需要克隆 [代码库](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)（如果尚未完成）。

接下来，您需要创建一个虚拟环境。使用 Conda 创建新环境文件（_environment.yml_）。如果您使用 Codespaces，请在 `.devcontainer` 目录中创建此文件，即 `.devcontainer/environment.yml`。

将以下代码片段填入您的环境文件：

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

如果使用 Conda 时遇到错误，您可以手动安装 Microsoft AI Libraries，使用以下命令：

```
conda install -c microsoft azure-ai-ml
```

环境文件指定了我们需要的依赖项。`<environment-name>` 是您希望为 Conda 环境使用的名称，`<python-version>` 是您希望使用的 Python 版本，例如 `3` 是 Python 的最新主要版本。

完成后，您可以通过在命令行/终端中运行以下命令来创建 Conda 环境：

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

如果遇到问题，请参考 [Conda 环境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

### 使用 Visual Studio Code 和 Python 支持扩展

我们建议您使用 [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) 编辑器，并安装 [Python 支持扩展](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 来学习本课程。不过，这只是一个建议，并不是强制要求。

> **注意**：通过在 VS Code 中打开课程代码库，您可以选择在容器中设置项目。这是因为课程代码库中包含了 [特殊的 `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 目录。稍后会详细介绍。

> **注意**：一旦您在 VS Code 中克隆并打开目录，它会自动建议您安装 Python 支持扩展。

> **注意**：如果 VS Code 建议您在容器中重新打开代码库，请拒绝此请求以使用本地安装的 Python 版本。

### 在浏览器中使用 Jupyter

您还可以直接在浏览器中使用 [Jupyter 环境](https://jupyter.org?WT.mc_id=academic-105485-koreyst) 来完成项目。经典 Jupyter 和 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) 都提供了非常友好的开发环境，具有自动补全、代码高亮等功能。

要在本地启动 Jupyter，请打开终端/命令行，导航到课程目录并执行以下命令：

```bash
jupyter notebook
```

或

```bash
jupyterhub
```

这将启动一个 Jupyter 实例，并在命令行窗口中显示访问的 URL。

访问该 URL 后，您应该能看到课程大纲，并可以导航到任何 `*.ipynb` 文件。例如，`08-building-search-applications/python/oai-solution.ipynb`。

### 在容器中运行

除了在您的电脑或 Codespace 上设置一切，您还可以使用 [容器](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)。课程代码库中的特殊 `.devcontainer` 文件夹使得 VS Code 可以在容器中设置项目。在 Codespaces 之外，这需要安装 Docker，过程可能会比较复杂，因此我们建议仅对有容器使用经验的用户使用此方法。

在使用 GitHub Codespaces 时，保护您的 API 密钥的最佳方法之一是使用 Codespace Secrets。请参考 [Codespaces 密钥管理指南](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) 了解更多信息。

## 课程和技术要求

本课程包括6个概念课程和6个编码课程。

对于编码课程，我们使用 Azure OpenAI 服务。您需要访问 Azure OpenAI 服务并获取 API 密钥才能运行代码。您可以通过[填写此申请](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)来申请访问权限。

在等待申请处理期间，每个编码课程还包括一个 `README.md` 文件，您可以在其中查看代码和输出。

## 第一次使用 Azure OpenAI 服务

如果这是您第一次使用 Azure OpenAI 服务，请按照此指南了解如何[创建和部署 Azure OpenAI 服务资源。](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## 第一次使用 OpenAI API

如果这是您第一次使用 OpenAI API，请按照指南了解如何[创建和使用接口。](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## 认识其他学习者

我们在官方 [AI 社区 Discord 服务器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) 中创建了频道，供学习者互相交流。这是与其他志同道合的创业者、开发者、学生以及任何希望在生成式人工智能领域提升技能的人建立联系的绝佳方式。

[![加入 Discord 频道](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

项目团队也会在此 Discord 服务器上帮助学习者。

## 贡献

本课程是一个开源项目。如果您发现需要改进的地方或问题，请创建 [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) 或记录 [GitHub 问题](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

项目团队将跟踪所有贡献。为开源项目做贡献是建立生成式人工智能职业生涯的绝佳方式。

大多数贡献需要您同意贡献者许可协议 (CLA)，声明您有权并确实授予我们使用您的贡献的权利。详情请访问 [CLA, 贡献者许可协议网站](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)。

重要提示：在翻译此代码库中的文本时，请确保不使用机器翻译。我们将通过社区验证翻译，因此请仅在您精通相关语言时自愿进行翻译。

当您提交 Pull Request 时，CLA-bot 会自动确定您是否需要提供 CLA，并适当地标记 PR（例如，标签、评论）。只需按照机器人提供的说明操作即可。您只需在所有使用我们 CLA 的代码库中执行一次此操作。

本项目采用了 [Microsoft 开源行为准则](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)。有关更多信息，请阅读行为准则 FAQ 或通过 [Email opencode](opencode@microsoft.com) 联系我们，提出其他问题或意见。

## 开始学习吧！
现在您已经完成了完成本课程所需的步骤，让我们开始了解[生成式人工智能和大型语言模型的介绍](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)。

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。