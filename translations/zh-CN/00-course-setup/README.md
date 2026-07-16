# 课程入门

我们非常高兴您开始这门课程，并期待看到您用生成式 AI 构建的作品！

为了确保您的成功，本页概述了设置步骤、技术要求以及如有需要时的求助途径。

## 设置步骤

开始学习本课程，您需要完成以下步骤。

### 1. Fork 本仓库

[将整个仓库 Fork](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) 到您自己的 GitHub 账户，以便修改代码并完成挑战。您还可以[给本仓库加星（🌟）](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst)，方便以后找到它及相关仓库。

### 2. 创建 Codespace

为避免运行代码时的依赖问题，我们建议使用[GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst)进行本课程学习。

在您的 Fork 仓库中：**Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/zh-CN/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 添加密钥

1. ⚙️ 设置图标 -> 命令面板 -> Codespaces : 管理用户密钥 -> 添加新密钥。
2. 名称填写 OPENAI_API_KEY，粘贴您的密钥，保存。

### 3. 下一步？

| 我想…               | 前往…                                                                   |
|---------------------|-------------------------------------------------------------------------|
| 开始第 1 课           | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| 离线工作             | [`setup-local.md`](02-setup-local.md)                                   |
| 设置 LLM 提供商       | [`providers.md`](03-providers.md)                                        |
| 认识其他学习者       | [加入我们的 Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 故障排除


| 现象                                   | 解决方案                                                       |
|-------------------------------------------|---------------------------------------------------------------|
| 容器构建停滞超过 10 分钟                | **Codespaces ➜ “Rebuild Container”**                        |
| `python: command not found`            | 终端未附着；点击 **+** ➜ *bash*                              |
| OpenAI 返回 `401 Unauthorized`        | `OPENAI_API_KEY` 错误或过期                                   |
| VS Code 显示“Dev container mounting…”  | 刷新浏览器标签页——Codespaces 有时会失去连接                 |
| Notebook 内核丢失                      | Notebook 菜单 ➜ **Kernel ▸ Select Kernel ▸ Python 3**         |

   Unix 系统：

   ```bash
   touch .env
   ```

   Windows：

   ```cmd
   echo . > .env
   ```

3. **编辑 `.env` 文件**：用文本编辑器打开 `.env` 文件（如 VS Code、Notepad++ 或其他编辑器）。添加以下行，替换为您的 Microsoft Foundry Models 终端地址和密钥（具体获取方式见 [`providers.md`](03-providers.md)）：

   > **注意：** GitHub Models（及其 `GITHUB_TOKEN` 变量）将于 2026 年 7 月底退役。请使用[Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)替代。

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. <strong>保存文件</strong>：保存修改并关闭编辑器。

5. **安装 `python-dotenv`**：如果尚未安装，需安装 `python-dotenv` 包以从 `.env` 文件加载环境变量到 Python 应用。使用 `pip` 安装：

   ```bash
   pip install python-dotenv
   ```

6. **在 Python 脚本中加载环境变量**：在 Python 脚本中使用 `python-dotenv` 包加载 `.env` 文件的环境变量：

   ```python
   from dotenv import load_dotenv
   import os

   # 从 .env 文件加载环境变量
   load_dotenv()

   # 访问 Microsoft Foundry Models 变量
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

就这样！您已成功创建 `.env` 文件，添加 Microsoft Foundry Models 凭证，并在 Python 应用中加载它们。

## 在本地计算机上运行

要在本地运行代码，您需要安装某个版本的 [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst)。

然后您需要克隆仓库：

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

克隆完成后，就可以开始学习啦！

## 可选步骤

### 安装 Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) 是 Conda、Python 及一些软件包的轻量级安装器。
Conda 是包管理工具，可以方便地设置和切换不同的 Python [<strong>虚拟环境</strong>](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst)和软件包，也便于安装 `pip` 无法安装的软件包。

您可以按照[Miniconda 安装指南](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst)进行安装。

安装好 Miniconda 后，您需要克隆[仓库](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst)（若尚未克隆）

接着，您需要创建虚拟环境。使用 Conda，您可以创建一个环境文件（_environment.yml_）。如果您使用的是 Codespaces，请在 `.devcontainer` 目录内创建该文件，即 `.devcontainer/environment.yml`。

把以下内容填入环境文件：

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

如果您使用 conda 遇到错误，也可以在终端手动运行以下命令安装 Microsoft AI 库。

```
conda install -c microsoft azure-ai-ml
```

环境文件指定了所需依赖。`<environment-name>` 是您想用的 Conda 环境名，`<python-version>` 是 Python 版本，比如 `3` 代表最新版大版本。

完成后，您可以运行以下命令创建 Conda 环境：

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer 子路径仅适用于 Codespace 设置
conda activate ai4beg
```

如遇问题，请参阅[Conda 环境指南](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst)。

### 使用带 Python 支持扩展的 Visual Studio Code

我们推荐本课程使用安装了[Python 支持扩展](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)的[Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst)编辑器。但这只是建议，并非必须。

> <strong>注意</strong>：打开课程仓库时，您可以选择在容器内设置项目。这得益于课程仓库中特殊的[`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)目录，后面会详细介绍。

> <strong>注意</strong>：克隆并打开目录后，VS Code 会自动建议您安装 Python 支持扩展。

> <strong>注意</strong>：如果 VS Code 建议您重新在容器中打开仓库，请拒绝此请求，以使用本地已安装的 Python 版本。

### 在浏览器中使用 Jupyter

您也可以直接在浏览器中通过 [Jupyter 环境](https://jupyter.org?WT.mc_id=academic-105485-koreyst)进行项目开发。Jupyter 经典版和 [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) 都提供了诸如自动补全、代码高亮等优质开发体验。

若要在本地启动 Jupyter，请打开终端，进入课程目录，执行：

```bash
jupyter notebook
```

或者

```bash
jupyterhub
```

这将启动 Jupyter 实例，命令行窗口会显示访问它的 URL。

访问 URL 后，您会看到课程大纲，可以导航至任意 `*.ipynb` 文件，比如 `08-building-search-applications/python/oai-solution.ipynb`。

### 容器中运行

除了在本地或 Codespace 设置之外，还可使用[容器](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>)运行。本课程仓库中的特殊 `.devcontainer` 文件夹可让 VS Code 在容器中搭建项目。若不使用 Codespaces，则需先安装 Docker。说实话，这步骤较复杂，建议有容器使用经验的同学采用。

在 GitHub Codespaces 中，保护 API 密钥的最佳方法之一是使用 Codespace Secrets。详情请参阅[Codespaces 秘钥管理](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst)指南。


## 课程章节和技术要求

本课程包含 6 个概念课和 6 个编程课。

编程课使用 Azure OpenAI 服务，您需要获得 Azure OpenAI 服务访问权限和 API 密钥才能运行代码。可通过[提交申请](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst)获得访问权限。

申请审核期间，每个编程课也包含一个 `README.md` 文件，您可查看代码和输出结果。

## 首次使用 Azure OpenAI 服务

如果您是首次使用 Azure OpenAI 服务，请参阅此指南了解如何[创建和部署 Azure OpenAI 服务资源](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)。

## 首次使用 OpenAI API

如果您首次使用 OpenAI API，请参考指南了解如何[创建和使用接口](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)。

## 结识其他学习者

我们在官方 [AI 社区 Discord 服务器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)中创建了频道供学习者交流。这里是与志同道合的创业者、构建者、学生及希望提升生成式 AI 技能的朋友们建立联系的绝佳场所。

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

项目团队也将在此 Discord 服务器中帮助学习者。

## 贡献

本课程是一个开源项目。如果您发现改进空间或问题，请提交[拉取请求](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst)或反馈[GitHub Issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst)。

项目团队将跟踪所有贡献。参与开源是构建生成式 AI 职业生涯的绝佳途径。

大多数贡献需您同意贡献者许可协议（CLA），声明您有权且确实授予我们使用该贡献的权利。详情请访问[CLA，贡献者许可协议网站](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst)。

重要提示：翻译本仓库文本时，请确保不使用机器翻译。我们将通过社区验证翻译，请仅在您精通的语言中自愿参与翻译。

提交拉取请求时，CLA 机器人将自动判断您是否需要提交 CLA，并适当标注 PR（如标签、评论）。请按照机器人的指导操作。您只需在所有使用此 CLA 的仓库中完成一次。


本项目已采用 [Microsoft 开源行为守则](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst)。欲了解更多信息，请阅读行为守则常见问题解答，或通过 [Email opencode](opencode@microsoft.com) 联系我们，提出任何额外的问题或意见。

## 让我们开始吧

既然您已经完成了完成本课程所需的步骤，让我们通过获取 [生成式人工智能和大型语言模型简介](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) 开始吧。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->