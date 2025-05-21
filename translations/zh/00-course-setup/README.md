<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-05-19T08:58:18+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "zh"
}
-->
# 开始这门课程

我们非常高兴你开始这门课程，期待看到你在生成式AI的启发下能创造出什么！

为了确保你的成功，这个页面列出了设置步骤、技术要求，以及在需要时获取帮助的途径。

## 设置步骤

要开始这门课程，你需要完成以下步骤。

### 1. Fork 这个仓库

[Fork 这个完整的仓库](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)到你自己的 GitHub 账户，以便更改代码并完成挑战。你也可以[给这个仓库加星（🌟）](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)以更容易找到它和相关的仓库。

### 2. 创建一个 codespace

为了避免运行代码时出现依赖问题，我们建议在[GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)中运行这门课程。

可以通过在你 fork 的版本中选择 `Code` 选项并选择 **Codespaces** 选项来创建。

![显示如何创建 codespace 按钮的对话框](../../../00-course-setup/images/who-will-pay.webp)

### 3. 存储你的 API 密钥

在构建任何类型的应用程序时，保持你的 API 密钥安全非常重要。我们建议不要将任何 API 密钥直接存储在代码中。将这些细节提交到公共仓库可能会导致安全问题，甚至在被恶意使用时产生不必要的费用。
以下是如何为 Python 创建 `.env` 文件并添加 `GITHUB_TOKEN` 的分步指南：

1. **导航到你的项目目录**：打开你的终端或命令提示符，并导航到你想创建 `.env` 文件的项目根目录。

   ```bash
   cd path/to/your/project
   ```

2. **创建 `.env` 文件**：使用你喜欢的文本编辑器创建一个名为 `.env` 的新文件。如果你使用命令行，可以使用 `touch` (on Unix-based systems) or `echo`（在 Windows 上）：

   基于 Unix 的系统：
   ```bash
   touch .env
   ```

   Windows：
   ```cmd
   echo . > .env
   ```

3. **编辑 `.env` 文件**：在文本编辑器中打开 `.env` 文件（例如，VS Code、Notepad++ 或任何其他编辑器）。将以下行添加到文件中，用你的实际 GitHub 令牌替换 `your_github_token_here`：

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **保存文件**：保存更改并关闭文本编辑器。

5. **安装 `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` 包以从 `.env` 文件加载环境变量到你的 Python 应用程序中。你可以使用 `pip` 安装：

   ```bash
   pip install python-dotenv
   ```

6. **在你的 Python 脚本中加载环境变量**：在你的 Python 脚本中，使用 `python-dotenv` 包从 `.env` 文件加载环境变量：

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

完成了！你已经成功创建了一个 `.env` 文件，添加了你的 GitHub 令牌，并将其加载到你的 Python 应用程序中。

## 如何在本地计算机上运行

要在本地计算机上运行代码，你需要安装某个版本的 [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)。

然后要使用这个仓库，你需要克隆它：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

一旦你检查完所有内容，就可以开始了！

## 可选步骤

### 安装 Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是一个用于安装 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python 以及一些包的轻量级安装程序。
Conda 本身是一个包管理器，可以轻松设置和切换不同的 Python [**虚拟环境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)和包。它在安装无法通过 `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml` 获取的包时也很有用。

继续使用下面的代码片段填充你的环境文件：

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

如果你发现使用 conda 时出现错误，可以在终端中使用以下命令手动安装 Microsoft AI 库。

```
conda install -c microsoft azure-ai-ml
```

环境文件指定了我们需要的依赖项。`<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` 是 Python 的最新主版本。

完成后，你可以继续通过在命令行/终端中运行以下命令来创建你的 Conda 环境

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

如果你遇到任何问题，请参考 [Conda 环境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

### 使用带有 Python 支持扩展的 Visual Studio Code

我们推荐使用安装了 [Python 支持扩展](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)的 [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) 编辑器来学习这门课程。不过，这只是一个建议，并不是绝对要求。

> **注意**：通过在 VS Code 中打开课程仓库，你可以选择在容器内设置项目。这是因为课程仓库中有一个[特殊的 `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 目录。稍后会详细介绍。

> **注意**：一旦你克隆并在 VS Code 中打开目录，它会自动建议你安装 Python 支持扩展。

> **注意**：如果 VS Code 建议你在容器中重新打开仓库，请拒绝此请求以使用本地安装的 Python 版本。

### 在浏览器中使用 Jupyter

你也可以直接在浏览器中使用 [Jupyter 环境](https://jupyter.org?WT.mc_id=academic-105485-koreyst)进行项目开发。经典的 Jupyter 和 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) 都提供了相当不错的开发环境，具有自动补全、代码高亮等功能。

要在本地启动 Jupyter，请打开终端/命令行，导航到课程目录，然后执行：

```bash
jupyter notebook
```

或

```bash
jupyterhub
```

这将启动一个 Jupyter 实例，并在命令行窗口中显示访问它的 URL。

一旦你访问该 URL，你应该能看到课程大纲，并可以导航到任何 `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` 文件，查看代码和输出。

## 第一次使用 Azure OpenAI 服务

如果这是你第一次使用 Azure OpenAI 服务，请按照此指南[创建和部署 Azure OpenAI 服务资源](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)。

## 第一次使用 OpenAI API

如果这是你第一次使用 OpenAI API，请按照指南了解如何[创建和使用接口](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)。

## 认识其他学习者

我们在官方的 [AI 社区 Discord 服务器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)上创建了频道供学习者交流。这是一个与其他志同道合的创业者、开发者、学生以及任何想在生成式AI领域提升自我的人进行网络交流的好方法。

[![加入 discord 频道](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

项目团队也会在这个 Discord 服务器上帮助学习者。

## 贡献

这门课程是一个开源项目。如果你发现有改进空间或问题，请创建一个 [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) 或记录一个 [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

项目团队将跟踪所有贡献。为开源项目做贡献是建立生成式AI职业生涯的绝佳方式。

大多数贡献需要你同意一个贡献者许可协议 (CLA)，声明你有权并实际授予我们使用你贡献的权利。详情请访问 [CLA, Contributor License Agreement 网站](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)。

重要提示：在翻译这个仓库中的文本时，请确保不使用机器翻译。我们将通过社区验证翻译，因此请仅在你精通的语言中自愿翻译。

当你提交 pull request 时，CLA-bot 会自动判断你是否需要提供 CLA，并适当地装饰 PR（例如，标签、评论）。只需按照机器人提供的说明操作即可。在使用我们的 CLA 的所有仓库中，你只需做一次。

这个项目采用了 [Microsoft 开源行为准则](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)。欲了解更多信息，请阅读行为准则常见问题或通过 [Email opencode](opencode@microsoft.com) 联系我们，提出任何额外的问题或评论。

## 让我们开始吧

现在你已经完成了这门课程所需的步骤，让我们通过获取[生成式AI和LLM的介绍](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)来开始吧。

**免责声明**：
本文档是使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译的。虽然我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原始文档视为权威来源。对于重要信息，建议进行专业人工翻译。对于因使用此翻译而产生的任何误解或误读，我们不承担责任。