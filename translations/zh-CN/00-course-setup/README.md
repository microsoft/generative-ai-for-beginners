# 开始本课程

我们非常高兴您开始这门课程，期待您用生成式 AI 构建出令人振奋的作品！

为了确保您的成功，本页将说明设置步骤、技术要求以及在需要时获取帮助的渠道。

## 设置步骤

开始本课程之前，您需要完成以下步骤。

### 1. Fork 本仓库

将[整个仓库 Fork](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)到您自己的 GitHub 账号，以便您修改代码并完成挑战。您也可以[为本仓库加星标 (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)，方便后续查找本仓库及相关仓库。

### 2. 创建 Codespace

为了避免运行代码时出现依赖问题，我们推荐您在[GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)中运行本课程。

在您的 fork 仓库里：**代码 -> Codespaces -> 在 main 分支新建**

![Dialog showing buttons to create a codespace](../../../translated_images/zh-CN/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 添加密钥

1. ⚙️ 齿轮图标 -> 命令面板 -> Codespaces : 管理用户密钥 -> 添加新密钥。
2. 名称写 OPENAI_API_KEY，粘贴您的密钥，保存。

### 3. 下一步？

| 我想……                | 跳转到……                                                              |
|------------------------|------------------------------------------------------------------------|
| 开始第1课              | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| 离线工作              | [`setup-local.md`](02-setup-local.md)                                   |
| 设置大型语言模型提供商  | [`providers.md`](03-providers.md)                                        |
| 认识其他学习者          | [加入我们的 Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 故障排查

| 症状                                      | 解决方法                                                              |
|------------------------------------------|----------------------------------------------------------------------|
| 容器构建卡住超过 10 分钟                  | **Codespaces ➜ “重新构建容器”**                                     |
| 终端显示 `python: command not found`      | 终端未连接；点击 **+** ➜ *bash*                                      |
| OpenAI 返回 `401 Unauthorized`             | `OPENAI_API_KEY` 错误或已过期                                        |
| VS Code 显示“开发容器挂载中…”            | 刷新浏览器标签页——Codespaces 有时会断开连接                         |
| 笔记本内核丢失                          | 笔记本菜单 ➜ **内核 ▸ 选择内核 ▸ Python 3**                          |

   基于 Unix 的系统：

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **编辑 `.env` 文件**：用文本编辑器（如 VS Code、Notepad++ 或任何其他编辑器）打开 `.env` 文件。在文件中添加以下行，将 `your_github_token_here` 替换为您的实际 GitHub 令牌：

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **保存文件**：保存更改并关闭编辑器。

5. **安装 `python-dotenv`**：如果尚未安装，您需要安装 `python-dotenv` 包，以便将 `.env` 文件中的环境变量加载到 Python 应用中。您可使用 `pip` 安装：

   ```bash
   pip install python-dotenv
   ```

6. **在 Python 脚本中加载环境变量**：在您的 Python 脚本中，使用 `python-dotenv` 包加载 `.env` 文件中的环境变量：

   ```python
   from dotenv import load_dotenv
   import os

   # 从 .env 文件加载环境变量
   load_dotenv()

   # 访问 GITHUB_TOKEN 变量
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

完成以上操作后，您就成功创建了 `.env` 文件，添加了 GitHub 令牌，并将其加载到了您的 Python 应用中。

## 如何在本地电脑运行

要在本地电脑运行代码，您需要安装某个版本的[Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)。

然后您需要克隆仓库：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

确认所有内容就绪后，您就可以开始了！

## 可选步骤

### 安装 Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是用于安装 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python 及少量包的轻量级安装器。  
Conda 本身是一个包管理器，可以方便地设置和切换不同的 Python [**虚拟环境**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)及依赖包。安装一些 `pip` 无法获得的包时也很有用。

您可参考[Miniconda 安装指南](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst)完成安装。

安装 Miniconda 后，您需要克隆[仓库](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)（如果还未克隆）。

接着，您需要创建一个虚拟环境。使用 Conda，先创建环境文件（_environment.yml_）。如果您使用 Codespaces，请在 `.devcontainer` 目录下创建此文件，即 `.devcontainer/environment.yml`。

将以下内容填入您的环境文件：

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

如果在使用 conda 时遇到错误，可以在终端手动运行以下命令安装 Microsoft AI 库。

```
conda install -c microsoft azure-ai-ml
```

环境文件中指定了所需依赖。`<environment-name>` 是您想用作 Conda 环境名称的名字，`<python-version>` 是您希望使用的 Python 版本，例如 `3` 是最新的主版本。

完成后，您可在命令行/终端运行以下命令创建 Conda 环境：

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer 子路径仅适用于 Codespace 设置
conda activate ai4beg
```

如遇问题请参考[Conda 环境管理指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

### 使用带 Python 支持扩展的 Visual Studio Code

我们推荐本课程使用安装了[Python 支持扩展](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)的[Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst)编辑器。不过这只是建议，不是硬性要求。

> **注意**：打开课程仓库时，您可以选择在容器内设置项目，因为课程仓库中带有[特殊的 `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)目录，稍后会详细说明。

> **注意**：克隆并在 VS Code 打开目录后，它会自动提示您安装 Python 支持扩展。

> **注意**：如果 VS Code 提示您重新在容器中打开仓库，请拒绝此请求以使用本地安装的 Python 版本。

### 在浏览器中使用 Jupyter

您也可以直接在浏览器中使用[Jupyter 环境](https://jupyter.org?WT.mc_id=academic-105485-koreyst)开发。经典 Jupyter 和[Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst)均提供了相当舒适的开发体验，包括自动补全、代码高亮等功能。

启动本地 Jupyter，打开终端/命令行，定位到课程目录后执行：

```bash
jupyter notebook
```

或者

```bash
jupyterhub
```

该命令会启动 Jupyter 实例，命令行窗口会显示访问的 URL。

访问该 URL 后，您将看到课程大纲，并可以打开任何 `*.ipynb` 文件，例如 `08-building-search-applications/python/oai-solution.ipynb`。

### 容器中运行

除了在电脑或 Codespace 装环境，还可以用[容器](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)运行。课程仓库中的特殊 `.devcontainer` 文件夹支持 VS Code 在容器内设置项目。Codespaces 之外使用这功能需要安装 Docker，操作稍复杂，建议只有有容器经验的人使用。

使用 GitHub Codespaces 时，为了保证 API 密钥安全，最推荐用 Codespaces Secrets。请参考[Codespaces 密钥管理](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst)指南了解详情。

## 课程与技术要求

课程包含 6 节理念课和 6 节编程课。

编程课使用 Azure OpenAI 服务。运行时您需要一个 Azure OpenAI 服务的访问权限与 API 密钥。可通过[提交申请](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)获取访问。

等待申请批准期间，每节编程课的 `README.md` 文件都包含查看代码和输出的内容。

## 首次使用 Azure OpenAI 服务

如果您是第一次使用 Azure OpenAI 服务，请参照此指南了解如何[创建和部署 Azure OpenAI 资源](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)。

## 首次使用 OpenAI API

如果您是第一次使用 OpenAI API，请按照指南了解如何[创建和使用接口](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)。

## 认识其他学习者

我们已在官方[AI 社区 Discord 服务器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)开设频道，方便您结识其他学习者。这是与志同道合的创业者、开发者、学生及想在生成式 AI 领域提升自我的人的交流好地方。

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

项目团队也会在该 Discord 服务器提供帮助。

## 贡献

本课程是开源项目。如果您发现改进点或问题，请提交[Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)或创建[GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

项目团队会跟踪所有贡献。参与开源是构建生成式 AI 职业生涯的绝佳途径。

大多数贡献需要您同意贡献者许可协议（CLA），声明您有权且确实授予我们使用您贡献内容的权限。详情请访问[CLA，贡献者许可协议网站](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)。

重要提示：翻译本仓库内容时，请确保不要使用机器翻译。我们将通过社区审查翻译质量，因此请仅对自己熟练掌握的语言志愿参与翻译。

提交 PR 时，CLA-bot 会自动判断您是否需要提交 CLA，并在 PR 上做相应标注（如标签、评论）。按照机器人指示操作即可。您在所有签署 CLA 的仓库中只需执行一次此步骤。

本项目采用了[微软开源行为准则](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)。详情请参阅行为准则常见问题，或通过[Email opencode](opencode@microsoft.com)联系提供更多问题或反馈。

## 让我们开始吧
既然您已经完成了完成本课程所需的步骤，让我们开始，通过了解[生成式人工智能和大型语言模型的介绍](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能存在错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议采用专业人工翻译。因使用本翻译而产生的任何误解或错误解读，本公司概不负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->