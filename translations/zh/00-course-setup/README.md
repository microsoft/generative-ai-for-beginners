<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:38:39+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "zh"
}
-->
# 开始这门课程

我们非常高兴您能开始这门课程，并期待看到您使用生成式 AI 创造的成果！

为确保您的成功，本页面概述了设置步骤、技术要求以及在需要时获取帮助的途径。

## 设置步骤

要开始这门课程，您需要完成以下步骤。

### 1. Fork 此仓库

[Fork 整个仓库](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)到您自己的 GitHub 账户，以便更改任何代码并完成挑战。您还可以[星标 (🌟) 此仓库](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)，以便更容易找到它和相关的仓库。

### 2. 创建一个 codespace

为了避免在运行代码时遇到任何依赖问题，我们建议在 [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)中运行这门课程。

您可以通过在 fork 版本的仓库中选择 `Code` 选项，然后选择 **Codespaces** 选项来创建。

![显示创建 codespace 按钮的对话框](../../../00-course-setup/images/who-will-pay.webp)

### 3. 存储您的 API 密钥

在构建任何类型的应用程序时，保持 API 密钥的安全和保密是很重要的。我们建议不要将任何 API 密钥直接存储在您的代码中。将这些详细信息提交到公共仓库可能会导致安全问题，甚至在被恶意行为者使用时产生不必要的费用。
以下是如何为 Python 创建 `.env` 文件并添加 `GITHUB_TOKEN` 的分步指南：

1. **导航到您的项目目录**：打开终端或命令提示符，并导航到您希望创建 `.env` 文件的项目根目录。

   ```bash
   cd path/to/your/project
   ```

2. **创建 `.env` 文件**：使用您喜欢的文本编辑器创建一个名为 `.env` 的新文件。如果您使用命令行，可以使用 `touch` (on Unix-based systems) or `echo`（在 Windows 上）：

   基于 Unix 的系统：
   ```bash
   touch .env
   ```

   Windows：
   ```cmd
   echo . > .env
   ```

3. **编辑 `.env` 文件**：在文本编辑器中打开 `.env` 文件（例如，VS Code、Notepad++ 或其他任何编辑器）。将以下行添加到文件中，将 `your_github_token_here` 替换为您的实际 GitHub 令牌：

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **保存文件**：保存更改并关闭文本编辑器。

5. **安装 `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` 包以从 `.env` 文件中加载环境变量到您的 Python 应用程序。您可以使用 `pip` 安装它：

   ```bash
   pip install python-dotenv
   ```

6. **在您的 Python 脚本中加载环境变量**：在您的 Python 脚本中，使用 `python-dotenv` 包从 `.env` 文件中加载环境变量：

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

完成了！您已成功创建了一个 `.env` 文件，添加了您的 GitHub 令牌，并将其加载到您的 Python 应用程序中。

## 如何在本地计算机上运行

要在本地计算机上运行代码，您需要安装某个版本的 [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)。

然后要使用该仓库，您需要克隆它：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

一旦您完成了所有检查，您就可以开始了！

## 可选步骤

### 安装 Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是一个轻量级安装程序，用于安装 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python 以及一些包。
Conda 本身是一个包管理器，它使得设置和切换不同的 Python [**虚拟环境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)和包变得容易。它也非常适合安装那些不能通过 `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml` 获得的包。

继续并使用以下代码片段填充您的环境文件：

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

如果您发现使用 conda 时出现错误，您可以手动安装 Microsoft AI Libraries，使用以下命令在终端中执行。

```
conda install -c microsoft azure-ai-ml
```

环境文件指定了我们需要的依赖项。`<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` 是最新的 Python 主版本。

完成这些后，您可以继续并通过在命令行/终端中运行以下命令来创建您的 Conda 环境

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

如果遇到任何问题，请参考 [Conda 环境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

### 使用 Visual Studio Code 和 Python 支持扩展

我们建议在这门课程中使用安装了 [Python 支持扩展](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)的 [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) 编辑器。不过，这只是一个建议，而不是绝对要求。

> **注意**：通过在 VS Code 中打开课程仓库，您可以选择在容器中设置项目。这是因为在课程仓库中找到了 [特殊的 `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 目录。稍后会详细介绍。

> **注意**：一旦您在 VS Code 中克隆并打开目录，它将自动建议您安装 Python 支持扩展。

> **注意**：如果 VS Code 建议您在容器中重新打开仓库，请拒绝此请求以使用本地安装的 Python 版本。

### 在浏览器中使用 Jupyter

您还可以在浏览器中使用 [Jupyter 环境](https://jupyter.org?WT.mc_id=academic-105485-koreyst)进行项目开发。经典 Jupyter 和 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) 都提供了一个相当不错的开发环境，具有自动补全、代码高亮等功能。

要在本地启动 Jupyter，请前往终端/命令行，导航到课程目录，并执行：

```bash
jupyter notebook
```

或

```bash
jupyterhub
```

这将启动一个 Jupyter 实例，访问它的 URL 将显示在命令行窗口中。

一旦您访问了 URL，您应该能看到课程大纲，并能够导航到任何 `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` 文件，您可以在其中查看代码和输出。

## 第一次使用 Azure OpenAI 服务

如果这是您第一次使用 Azure OpenAI 服务，请按照本指南了解如何[创建和部署 Azure OpenAI 服务资源。](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## 第一次使用 OpenAI API

如果这是您第一次使用 OpenAI API，请按照本指南了解如何[创建和使用接口。](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## 结识其他学习者

我们在官方 [AI 社区 Discord 服务器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)中创建了频道，以便与其他学习者见面。这是一个与其他志同道合的企业家、开发者、学生以及任何想在生成式 AI 领域提升自我的人的绝佳方式。

[![加入 discord 频道](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

项目团队也将在此 Discord 服务器上帮助任何学习者。

## 贡献

这门课程是一个开源项目。如果您发现需要改进的地方或问题，请创建一个 [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) 或记录一个 [GitHub 问题](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

项目团队将跟踪所有贡献。为开源项目做贡献是构建您在生成式 AI 领域职业生涯的绝佳方式。

大多数贡献需要您同意一个贡献者许可协议 (CLA)，声明您有权并实际授予我们使用您贡献的权利。详情请访问 [CLA，贡献者许可协议网站](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)。

重要提示：在翻译此仓库中的文本时，请确保不使用机器翻译。我们将通过社区验证翻译，因此请仅在您熟练的语言中志愿翻译。

当您提交一个 pull request 时，CLA-bot 将自动确定您是否需要提供 CLA 并适当地装饰 PR（例如，标签、评论）。只需按照机器人提供的说明进行操作即可。在使用我们 CLA 的所有仓库中，您只需执行一次。

此项目采用了 [Microsoft 开源行为准则](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)。有关更多信息，请阅读行为准则常见问题或联系 [Email opencode](opencode@microsoft.com) 以获取任何其他问题或意见。

## 让我们开始吧

现在您已经完成了完成这门课程所需的步骤，让我们通过了解 [生成式 AI 和 LLMs 的介绍](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)来开始吧。

**免责声明**：
本文档已使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保准确性，请注意自动翻译可能包含错误或不准确之处。应将原始语言的文档视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误释负责。