# 课程入门指南

我们非常高兴您能开始这门课程，期待看到您用生成式人工智能创作的精彩作品！

为了确保您的学习成功，本页将介绍设置步骤、技术要求以及需要帮助时的获取方式。

## 设置步骤

要开始学习本课程，您需要完成以下步骤。

### 1. Fork 代码仓库

[Fork 整个仓库](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) 到您自己的 GitHub 账户，以便能够修改代码并完成挑战。您也可以[给仓库点星 (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)，方便查找此仓库及相关项目。

### 2. 创建 Codespace

为避免在运行代码时遇到依赖问题，我们推荐使用 [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) 来执行本课程。

在您 Fork 的仓库中：**Code -> Codespaces -> New on main**

![用于创建 codespace 的对话框按钮](../../../translated_images/zh-CN/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 添加密钥

1. ⚙️ 齿轮图标 -> 命令面板 -> Codespaces : 管理用户密钥 -> 添加新密钥。
2. 名称填写 OPENAI_API_KEY，粘贴您的密钥，保存。

### 3. 下一步？

| 我要做…             | 进入…                                                                   |
|---------------------|-------------------------------------------------------------------------|
| 开始第 1 课         | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| 离线使用            | [`setup-local.md`](02-setup-local.md)                                    |
| 配置大型语言模型供应商 | [`providers.md`](03-providers.md)                                         |
| 认识其他学习者       | [加入我们的 Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)         |

## 故障排除


| 现象                                   | 解决方案                                                        |
|---------------------------------------|----------------------------------------------------------------|
| 容器构建卡住超过 10 分钟               | **Codespaces ➜ “重新构建容器”**                                  |
| 终端显示 `python: command not found` | 终端未连接；点击 **+** ➜ *bash*                                 |
| OpenAI 返回 `401 Unauthorized`         | `OPENAI_API_KEY` 错误或过期                                     |
| VS Code 显示 “Dev container mounting…” | 刷新浏览器标签页——Codespaces 有时会断开连接                    |
| Notebook 内核丢失                      | Notebook 菜单 ➜ **Kernel ▸ 选择内核 ▸ Python 3**                  |

   Unix 系统：

   ```bash
   touch .env
   ```

   Windows 系统：

   ```cmd
   echo . > .env
   ```

3. **编辑 `.env` 文件**：用文本编辑器（例如 VS Code、Notepad++ 或其他）打开 `.env` 文件，将以下内容添加到文件中，并替换为您的 Microsoft Foundry Models 端点和密钥（详情见 [`providers.md`](03-providers.md)）：

   > **注意：** GitHub Models 及其 `GITHUB_TOKEN` 变量将在 2026 年 7 月底退役，请改用 [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)。

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. <strong>保存文件</strong>：保存更改后关闭文本编辑器。

5. **安装 `python-dotenv`**：如果尚未安装，需要安装 `python-dotenv` 包以从 `.env` 文件加载环境变量到 Python 应用。可通过 `pip` 安装：

   ```bash
   pip install python-dotenv
   ```

6. **在 Python 脚本中加载环境变量**：在您的 Python 脚本中，使用 `python-dotenv` 包加载 `.env` 文件中的环境变量：

   ```python
   from dotenv import load_dotenv
   import os

   # 从 .env 文件加载环境变量
   load_dotenv()

   # 访问 Microsoft Foundry 模型变量
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

完成！您已成功创建 `.env` 文件，添加 Microsoft Foundry Models 凭据，并加载到 Python 应用中。

## 如何在本地电脑运行

要在本地电脑运行代码，您需要安装某个版本的 [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)。

然后，需要克隆仓库：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

克隆完成后，即可开始学习！

## 可选步骤

### 安装 Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是一个轻量级安装器，用于安装 [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst)、Python 及部分包。
Conda 是一款包管理器，方便您设置和切换不同的 Python [<strong>虚拟环境</strong>](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)及包。安装一些 `pip` 无法提供的包时也非常实用。

您可以参照 [Miniconda 安装指南](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) 进行安装。

安装 Miniconda 后，需要克隆 [仓库](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)（如果尚未操作）。

接下来，您需要创建虚拟环境。使用 Conda 来做这个操作，创建一个环境文件 (_environment.yml_)。如果您在使用 Codespaces，请放置于 `.devcontainer` 目录下，即 `.devcontainer/environment.yml`。

填入下面的示例内容：

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

遇到 conda 错误时，可以在终端手动执行以下命令安装微软 AI 库。

```
conda install -c microsoft azure-ai-ml
```

环境文件中指定了依赖项。`<environment-name>` 替换为您希望为 Conda 环境起的名字，`<python-version>` 是您使用的 Python 版本，比如 `3` 是 Python 最新主版本。

文件准备好后，可通过下面命令创建 Conda 环境：

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer 子路径仅适用于 Codespace 设置
conda activate ai4beg
```

遇到问题请查阅 [Conda 环境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

### 使用带 Python 支持扩展的 Visual Studio Code

推荐使用 [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) 编辑器，安装 [Python 支持扩展](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 来进行本课程开发。这只是推荐而非强制。

> **注意：** 打开课程仓库后，VS Code 提供在容器内设置项目的选项，这得益于课程仓库内的专用 [.devcontainer](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) 目录，稍后会详细介绍。

> **注意：** 克隆并打开目录后，VS Code 会自动提示安装 Python 支持扩展。

> **注意：** 当 VS Code 提议在容器中重新打开仓库时，请选择拒绝，以使用本地安装的 Python 版本。

### 浏览器中使用 Jupyter

您也可以在浏览器内使用 [Jupyter 环境](https://jupyter.org?WT.mc_id=academic-105485-koreyst) 进行开发。经典 Jupyter 和 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) 都提供了自动补全、代码高亮等便捷功能。

本地启动 Jupyter，请在终端或命令行中进入课程目录，执行：

```bash
jupyter notebook
```

或者

```bash
jupyterhub
```

启动后，终端会显示访问的 URL。

访问该 URL 后，您会看到课程目录，可以打开任意 `*.ipynb` 文件，比如 `08-building-search-applications/python/oai-solution.ipynb`。

### 使用容器运行

除了在电脑或 Codespace 安装配置，您还可以选择使用 [容器](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)。课程仓库中的专用 `.devcontainer` 文件夹使 VS Code 能在容器内搭建项目。除 Codespaces 外，该方案要求安装 Docker；操作较复杂，建议有容器经验的用户使用。

使用 GitHub Codespaces 时，确保 API 密钥安全的最好方式是利用 Codespace Secrets。请参见 [Codespaces 密钥管理指南](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) 了解详情。


## 课程内容及技术需求

课程包含讲解生成式 AI 概念的“学习”课程，以及尽可能用 **Python** 和 **TypeScript** 提供实操代码示例的“实战”课程。

编码课程使用 Microsoft Foundry 中的 Azure OpenAI，您需要 Azure 订阅和 API 密钥。访问开放，无需申请，可 [创建 Microsoft Foundry 资源并部署模型](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)，获取端点和密钥。

每节编码课程还包含 `README.md` 文件，可查看代码和输出，无需运行。

## 首次使用 Azure OpenAI 服务

如果您首次使用 Azure OpenAI 服务，请参照本指南了解如何 [创建和部署 Azure OpenAI 服务资源。](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## 首次使用 OpenAI API

如果您首次使用 OpenAI API，请参照指南了解如何 [创建和使用接口。](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## 认识其他学习者

我们在官方 [AI Community Discord 服务器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)创建了频道，供学习者互相交流。这里是结识志同道合的创业者、开发者、学生及希望提升生成式 AI 技能人士的好去处。

[![加入 discord 频道](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

项目团队也会在该 Discord 服务器上帮助学习者。

## 贡献

本课程是开源项目。如发现改进点或问题，请创建 [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) 或提交 [GitHub 问题](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

项目团队将跟踪所有贡献。为开源项目做贡献是构建生成式 AI 职业生涯的绝佳途径。

大多数贡献都要求您同意贡献者许可协议（CLA），声明您有权且确实授权我们使用您的贡献。详情见 [CLA，贡献者许可协议网站](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)。

重要提示：翻译本仓库内容时，请确保不要使用机器翻译。我们会通过社区核实翻译，因此请仅在您熟悉的语言中自愿参与翻译工作。


当您提交拉取请求时，CLA-bot 会自动确定您是否需要提供 CLA，并相应地装饰 PR（例如，标签、评论）。只需遵循机器人提供的说明即可。您只需在使用我们 CLA 的所有存储库中执行此操作一次。

本项目已采纳[微软开源行为准则](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)。欲了解更多信息，请阅读行为准则常见问题解答，或通过[电子邮件 opencode](opencode@microsoft.com)联系我们，提出任何其他问题或意见。

## 让我们开始吧

既然您已经完成了完成此课程所需的步骤，让我们从获取[生成式 AI 和大语言模型简介](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)开始。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->