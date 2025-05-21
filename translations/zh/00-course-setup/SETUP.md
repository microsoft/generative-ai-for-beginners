<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T09:04:40+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "zh"
}
-->
# 设置您的开发环境

我们为这个仓库和课程设置了一个[开发容器](https://containers.dev?WT.mc_id=academic-105485-koreyst)，它具有支持 Python3、.NET、Node.js 和 Java 开发的通用运行时。相关配置在这个仓库根目录的 `.devcontainer/` 文件夹中的 `devcontainer.json` 文件中定义。

要激活开发容器，可以在 [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst)（用于云托管运行时）或 [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst)（用于本地设备托管运行时）中启动它。阅读[这篇文档](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst)以了解开发容器如何在 VS Code 中工作。

> [!TIP]  
> 我们推荐使用 GitHub Codespaces 以便快速启动并减少操作步骤。它为个人账户提供了慷慨的[免费使用额度](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst)。配置[超时设置](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst)以停止或删除不活跃的代码空间，以最大化您的额度使用。

## 1. 执行作业

每节课都会有_可选_作业，这些作业可能以一种或多种编程语言提供，包括：Python、.NET/C#、Java 和 JavaScript/TypeScript。本节提供有关执行这些作业的一般指导。

### 1.1 Python 作业

Python 作业可以以应用程序形式提供（`.py` 文件）或 Jupyter 笔记本形式提供（`.ipynb` 文件）。
- 要运行笔记本，在 Visual Studio Code 中打开它，然后点击_选择内核_（在右上角），选择显示的默认 Python 3 选项。您现在可以_全部运行_以执行笔记本。
- 要从命令行运行 Python 应用程序，请按照作业特定的说明确保您选择正确的文件并提供所需的参数。

## 2. 配置提供商

作业**可能**还可以设置为通过支持的服务提供商（如 OpenAI、Azure 或 Hugging Face）与一个或多个大型语言模型（LLM）部署一起工作。这些提供一个_托管端点_（API），我们可以使用正确的凭证（API 密钥或令牌）以编程方式访问。在本课程中，我们讨论这些提供商：

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst)，提供多种模型，包括核心 GPT 系列。
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)，专注于企业级准备的 OpenAI 模型。
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst)，提供开源模型和推理服务器。

**您将需要使用自己的账户进行这些练习**。作业是可选的，因此您可以根据自己的兴趣选择设置一个、全部或不设置任何提供商。以下是注册的一些指导：

| 注册 | 成本 | API 密钥 | 操作台 | 评论 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [定价](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [基于项目](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [无代码，网页](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 提供多种模型 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [定价](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK 快速入门](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio 快速入门](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [必须提前申请访问](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [定价](https://huggingface.co/pricing) | [访问令牌](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat 模型有限](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

按照以下指示为使用不同的提供商_配置_此仓库。需要特定提供商的作业将在其文件名中包含以下标签之一：
- `aoai` - 需要 Azure OpenAI 端点，密钥
- `oai` - 需要 OpenAI 端点，密钥
- `hf` - 需要 Hugging Face 令牌

您可以配置一个、没有或所有提供商。相关作业将因缺少凭证而出错。

### 2.1. 创建 `.env` 文件

我们假设您已经阅读了上述指导，并注册了相关提供商，并获得了所需的认证凭证（API_KEY 或令牌）。对于 Azure OpenAI，我们假设您也有一个有效的 Azure OpenAI 服务部署（端点），并至少部署了一个用于聊天完成的 GPT 模型。

下一步是配置您的**本地环境变量**如下：

1. 在根文件夹中查找一个 `.env.copy` 文件，其内容应如下所示：

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
   ```

2. 使用下面的命令将该文件复制到 `.env`。该文件已被_gitignore_，以确保机密安全。

   ```bash
   cp .env.copy .env
   ```

3. 按照下一节中描述的方法填写值（替换 `=` 右侧的占位符）。

4. （可选）如果您使用 GitHub Codespaces，您可以选择将环境变量保存为与此仓库关联的_Codespaces 机密_。在这种情况下，您不需要设置本地 .env 文件。**然而，请注意，这个选项仅在您使用 GitHub Codespaces 时有效。**如果您使用 Docker Desktop，仍需要设置 .env 文件。

### 2.2. 填充 `.env` 文件

我们快速浏览一下变量名称，以了解它们代表什么：

| 变量 | 描述 |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 这是您在个人资料中设置的用户访问令牌 |
| OPENAI_API_KEY | 这是用于非 Azure OpenAI 端点服务的授权密钥 |
| AZURE_OPENAI_API_KEY | 这是用于该服务的授权密钥 |
| AZURE_OPENAI_ENDPOINT | 这是 Azure OpenAI 资源的部署端点 |
| AZURE_OPENAI_DEPLOYMENT | 这是_文本生成_模型的部署端点 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | 这是_文本嵌入_模型的部署端点 |
| | |

注意：最后两个 Azure OpenAI 变量分别反映了用于聊天完成（文本生成）和向量搜索（嵌入）的默认模型。设置它们的说明将在相关作业中定义。

### 2.3 配置 Azure：从门户

Azure OpenAI 端点和密钥值将在[Azure 门户](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)中找到，所以我们从那里开始。

1. 访问 [Azure 门户](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
2. 点击侧边栏（左侧菜单）中的**密钥和端点**选项。
3. 点击**显示密钥** - 您应该看到以下内容：KEY 1、KEY 2 和端点。
4. 使用 KEY 1 值作为 AZURE_OPENAI_API_KEY
5. 使用端点值作为 AZURE_OPENAI_ENDPOINT

接下来，我们需要具体模型部署的端点。

1. 点击 Azure OpenAI 资源的侧边栏（左侧菜单）中的**模型部署**选项。
2. 在目标页面中，点击**管理部署**

这将带您到 Azure OpenAI Studio 网站，我们将在下面找到其他值。

### 2.4 配置 Azure：从 Studio

1. 从上面描述的资源导航到 [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst)。
2. 点击侧边栏（左侧）中的**部署**标签以查看当前已部署的模型。
3. 如果您想要的模型未部署，请使用**创建新部署**来部署它。
4. 您将需要一个_文本生成_模型 - 我们推荐：**gpt-35-turbo**
5. 您将需要一个_文本嵌入_模型 - 我们推荐 **text-embedding-ada-002**

现在更新环境变量以反映使用的_部署名称_。这通常与模型名称相同，除非您明确更改了它。因此，作为示例，您可能有：

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**完成后不要忘记保存 .env 文件**。您现在可以退出文件并返回运行笔记本的说明。

### 2.5 配置 OpenAI：从个人资料

您的 OpenAI API 密钥可以在您的 [OpenAI 账户](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst)中找到。如果您没有，可以注册一个账户并创建一个 API 密钥。一旦您有了密钥，可以用它来填充 `.env` 文件中的 `OPENAI_API_KEY` 变量。

### 2.6 配置 Hugging Face：从个人资料

您的 Hugging Face 令牌可以在个人资料中的 [访问令牌](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst)下找到。不要公开发布或分享这些。相反，为此项目使用创建一个新令牌，并将其复制到 `.env` 文件中的 `HUGGING_FACE_API_KEY` 变量下。_注意：_这技术上不是一个 API 密钥，但用于认证，因此我们保持这种命名惯例以保持一致性。

**免责声明**：
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行了翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原始语言的文档视为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用此翻译而产生的任何误解或误读，我们不承担责任。