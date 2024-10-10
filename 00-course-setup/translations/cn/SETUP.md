# 设置 Your Dev Environment

我们设置了这个数据库和课程，并使用[开发容器](https://containers.dev?WT.mc_id=academic-105485-koreyst)，该容器具有通用执行环境，可以支持 Python3、.NET、Node.js 和 Java 开发。相关配置定义在此数据库根目录的 `.devcontainer/` 文件夹中的 `devcontainer.json` 文件中。

要启动开发容器，请在[GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst)（用于云端托管的执行环境）或[Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst)（用于本地设备托管的执行环境）中启动它。阅读[此文件](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst)以获取有关开发容器在 VS Code 中如何工作的更多详细信息。

> [!TIP]  
> 我们建议使用 GitHub Codespaces 来快速开始并减少努力。它为个人账户提供慷慨的[免费使用配额](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst)。配置[超时](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst)以停止或删除不活动的 codespaces 以最大化您的配额使用。

## 1. 执行指派任务

每节课将有_可选的_作业，可能会以一种或多种编程语言提供，包括: Python、.NET/C#、Java 和 JavaScript/TypeScript。本节提供与执行这些作业相关的一般指导。

### 1.1 Python 指派

Python 指派是以应用程序（`.py` 文件）或 Jupyter 笔记本（`.ipynb` 文件）提供。

- 要执行笔记本，请在 Visual Studio Code 中打开它，然后点击 _Select Kernel_ (在右上角)，并选择显示的默认 Python 3 选项。现在你可以 _Run All_ 来执行笔记本。
- 要从命令行执行 Python 应用程序，请遵循特定作业的指示，以确保选择正确的文件并提供所需的参数。

## 2. 设置提供者

作业**可能**也会被设置为通过像 OpenAI、Azure 或 Hugging Face 这样的支持服务提供者来对抗一个或多个大型语言模型（LLM）部署。这些提供一个_托管端点_（API），我们可以使用正确的凭证（API 密钥或令牌）以编程方式访问。在本课程中，我们讨论这些提供者:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) 包含多样化模型，包括核心的 GPT 系列。
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) 提供专注于企业准备的 OpenAI 模型
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) 提供开源模型和推理服务器

**你将需要使用你自己的账户来完成这些练习**。作业是可选的，所以你可以根据自己的兴趣选择设置一个、全部或不设置任何提供者。以下是一些注册的指导：

| 注册 | 费用 | API 密钥 | 操作平台 | 评论 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [价格](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [基于项目](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [无代码, 网页](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 多种模型可用 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [价格](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK 快速入门](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio 快速入门](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [必须提前申请访问](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [价格](https://huggingface.co/pricing) | [访问令牌](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat 有限的模型](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

按照以下指示来_配置_此存储库以供不同提供者使用。需要特定提供者的作业将在其文件名中包含以下标签之一:

- `aoai` - 需要 Azure OpenAI 端点, 密钥
- `oai` - 需要 OpenAI 端点, 密钥
- `hf` - 需要 Hugging Face token

您可以设置一个、没有或所有提供者。相关的分配将因缺少凭证而简单地出错。

###  2.1. 创建 `.env` 文件

我们假设您已经阅读了上述指南并注册了相关提供者，并获得了所需的身份验证凭证(API_KEY 或 token)。在 Azure OpenAI 的情况下，我们假设您还拥有一个有效的 Azure OpenAI 服务部署(endpoint)，并至少部署了一个 GPT 模型以完成聊天。

下一步是按如下方式配置你的**本地环境变量**:

1. 在根目录中查找 `.env.copy` 文件，内容应如下所示:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
