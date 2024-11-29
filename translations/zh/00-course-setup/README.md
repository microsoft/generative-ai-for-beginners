# 开始本课程

我们非常期待您开始这门课程，并看看生成式AI能激发您构建出什么样的作品！

为了确保您的成功，这一页概述了设置步骤、技术要求以及在需要时如何获取帮助。

## 设置步骤

要开始学习这门课程，您需要完成以下步骤。

### 1. Fork 此仓库

[Fork 整个仓库](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)到您自己的GitHub账户，以便能够更改任何代码并完成挑战。您还可以[给此仓库加星标 (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)以便更容易找到它和相关的仓库。

### 2. 创建一个代码空间

为了避免在运行代码时出现任何依赖问题，我们建议在[GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)中运行这门课程。

这可以通过在您Fork的版本中选择`Code`选项并选择**Codespaces**选项来创建。

![显示创建代码空间按钮的对话框](../../../00-course-setup/images/who-will-pay.webp)

### 3. 存储您的API密钥

在构建任何类型的应用程序时，保持API密钥的安全和保密是很重要的。我们建议不要直接在代码中存储任何API密钥。将这些细节提交到公共仓库可能会导致安全问题，甚至在被不法分子使用时产生不必要的费用。

## 如何在本地计算机上运行

要在本地计算机上运行代码，您需要安装某个版本的[Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)。

然后要使用该仓库，您需要克隆它：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

一旦您完成所有操作，就可以开始了！

### 安装 Miniconda（可选步骤）

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst)是一个轻量级安装程序，用于安装[Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python以及一些包。
Conda本身是一个包管理器，它使得设置和切换不同的Python[**虚拟环境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)和包变得容易。它也非常适合安装那些无法通过`pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`获得的包。

继续用以下代码片段填充您的环境文件：

```yml
name: <environment-name>
channels:
 - defaults
dependencies:
- python=<python-version>
- openai
- python-dotenv
- azure-ai-inference

```

环境文件指定了我们需要的依赖项。`<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3`是Python的最新主要版本。

完成后，您可以通过在命令行/终端中运行以下命令来创建您的Conda环境

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

如果遇到任何问题，请参考[Conda环境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

### 使用带有Python支持扩展的Visual Studio Code

我们推荐使用[Visual Studio Code (VS Code)](http://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst)编辑器，并安装[Python支持扩展](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)来学习这门课程。不过，这只是一个建议，并不是绝对要求。

> **注意**：通过在VS Code中打开课程仓库，您可以选择在容器中设置项目。这是因为在课程仓库中有一个[特殊的`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)目录。稍后会详细介绍。

> **注意**：一旦您克隆并在VS Code中打开目录，它会自动建议您安装Python支持扩展。

> **注意**：如果VS Code建议您在容器中重新打开仓库，请拒绝此请求以便使用本地安装的Python版本。

### 在浏览器中使用Jupyter

您还可以在浏览器中使用[Jupyter环境](https://jupyter.org?WT.mc_id=academic-105485-koreyst)进行项目开发。经典的Jupyter和[Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst)都提供了相当愉快的开发环境，具备自动完成、代码高亮等功能。

要在本地启动Jupyter，请前往终端/命令行，导航到课程目录，并执行：

```bash
jupyter notebook
```

或

```bash
jupyterhub
```

这将启动一个Jupyter实例，并在命令行窗口中显示访问它的URL。

一旦您访问该URL，您应该能看到课程大纲，并能够导航到任何`*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md`文件，在那里您可以查看代码和输出。

## 第一次使用Azure OpenAI服务

如果这是您第一次使用Azure OpenAI服务，请按照本指南了解如何[创建和部署Azure OpenAI服务资源](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)。

## 第一次使用OpenAI API

如果这是您第一次使用OpenAI API，请按照指南了解如何[创建和使用接口](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)。

## 结识其他学习者

我们在官方[AI社区Discord服务器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)中创建了频道，供学习者互相认识。这是与其他志同道合的企业家、构建者、学生以及任何希望在生成式AI领域提升自我的人的绝佳网络。

[![加入Discord频道](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

项目团队也会在这个Discord服务器上帮助任何学习者。

## 贡献

这门课程是一个开源项目。如果您发现可以改进的地方或问题，请创建一个[Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)或记录一个[GitHub问题](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

项目团队将跟踪所有贡献。为开源做贡献是构建您在生成式AI领域职业生涯的绝佳方式。

大多数贡献要求您同意贡献者许可协议（CLA），声明您有权并实际上授予我们使用您贡献的权利。详情请访问[CLA, 贡献者许可协议网站](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)。

重要提示：在翻译此仓库中的文本时，请确保不使用机器翻译。我们将通过社区验证翻译，因此请仅在您熟练的语言中志愿翻译。

当您提交拉取请求时，CLA-bot会自动确定您是否需要提供CLA，并适当地装饰PR（例如，标签、评论）。只需按照bot提供的说明操作。您只需在所有使用我们CLA的仓库中执行一次。

此项目采用了[Microsoft开源行为准则](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)。欲了解更多信息，请阅读行为准则常见问题解答或通过[电子邮件opencode](opencode@microsoft.com)联系我们，提出任何额外的问题或意见。

## 开始吧

现在您已经完成了完成这门课程所需的步骤，让我们通过获取[生成式AI和LLM的介绍](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)开始吧。

**免责声明**：  
本文档使用机器翻译服务进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原始文档视为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用此翻译而引起的任何误解或误读，我们概不负责。