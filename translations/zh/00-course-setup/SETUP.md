<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:08:45+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "zh"
}
-->
# 设置开发环境

我们为这个代码库和课程设置了一个[开发容器](https://containers.dev?WT.mc_id=academic-105485-koreyst)，它具有支持Python3、.NET、Node.js和Java开发的通用运行时。相关配置在这个代码库根目录的`.devcontainer/`文件夹中的`devcontainer.json`文件中定义。

要激活开发容器，可以在[GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst)（用于云托管运行时）或[Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst)（用于本地设备托管运行时）中启动它。阅读[此文档](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst)以获取有关开发容器在VS Code中工作方式的更多详细信息。

> [!TIP]  
> 我们建议使用GitHub Codespaces以最少的努力快速启动。它为个人账户提供了慷慨的[免费使用额度](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst)。配置[超时](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst)以停止或删除不活动的代码空间，以最大化您的配额使用。

## 1. 执行任务

每节课将有_可选_任务，可以用一种或多种编程语言提供，包括：Python、.NET/C#、Java和JavaScript/TypeScript。本节提供与执行这些任务相关的一般指导。

### 1.1 Python任务

Python任务以应用程序（`.py`文件）或Jupyter笔记本（`.ipynb`文件）的形式提供。
- 要运行笔记本，请在Visual Studio Code中打开它，然后点击_选择内核_（右上角），选择显示的默认Python 3选项。现在可以_运行全部_来执行笔记本。
- 要从命令行运行Python应用程序，请遵循任务特定说明以确保选择正确的文件并提供所需参数。

## 2. 配置提供者

任务**可能**还设置为通过支持的服务提供商（如OpenAI、Azure或Hugging Face）对一个或多个大型语言模型（LLM）部署进行工作。这些提供了一个_托管端点_（API），我们可以通过正确的凭据（API密钥或令牌）进行编程访问。在本课程中，我们讨论这些提供者：

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst)，提供多样化的模型，包括核心GPT系列。
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)，专注于企业准备的OpenAI模型。
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst)，提供开源模型和推理服务器。

**您需要使用自己的账户进行这些练习**。任务是可选的，因此您可以根据自己的兴趣选择设置一个、全部或不设置任何提供者。以下是注册的一些指导：

| 注册 | 费用 | API密钥 | 操作台 | 评论 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [定价](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [基于项目](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [无代码，网页](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 可用多种模型 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [定价](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK快速入门](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio快速入门](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [必须提前申请访问](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [定价](https://huggingface.co/pricing) | [访问令牌](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat有有限的模型](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

按照以下指示_配置_此代码库以与不同提供者一起使用。需要特定提供者的任务将在其文件名中包含以下标签之一：
 - `aoai` - 需要Azure OpenAI端点，密钥
 - `oai` - 需要OpenAI端点，密钥
 - `hf` - 需要Hugging Face令牌

您可以配置一个、没有或所有提供者。相关任务在缺少凭据时将简单地报错。

### 2.1 创建`.env`文件

我们假设您已经阅读了上述指导，并注册了相关提供者，并获得了所需的身份验证凭据（API_KEY或令牌）。在Azure OpenAI的情况下，我们假设您还有一个有效的Azure OpenAI服务部署（端点），至少部署了一个GPT模型用于聊天完成。

下一步是配置您的**本地环境变量**如下：

1. 在根文件夹中查找一个`.env.copy`文件，其内容应如下所示：

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

2. 使用下面的命令将该文件复制到`.env`。该文件已_gitignore-d_，以保证秘密安全。

   ```bash
   cp .env.copy .env
   ```

3. 根据下一节中的描述填写值（替换`=`右侧的占位符）。

3.（可选）如果您使用GitHub Codespaces，您可以选择将环境变量保存为与此代码库关联的_Codespaces secrets_。在这种情况下，您不需要设置本地.env文件。**但请注意，这个选项仅在您使用GitHub Codespaces时有效。**如果您使用Docker Desktop，仍然需要设置.env文件。

### 2.2 填写`.env`文件

我们快速看一下变量名称，以了解它们代表什么：

| 变量 | 描述 |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 这是您在个人资料中设置的用户访问令牌 |
| OPENAI_API_KEY | 这是用于非Azure OpenAI端点服务的授权密钥 |
| AZURE_OPENAI_API_KEY | 这是使用该服务的授权密钥 |
| AZURE_OPENAI_ENDPOINT | 这是Azure OpenAI资源的已部署端点 |
| AZURE_OPENAI_DEPLOYMENT | 这是_文本生成_模型部署端点 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | 这是_文本嵌入_模型部署端点 |
| | |

注意：最后两个Azure OpenAI变量分别反映了聊天完成（文本生成）和向量搜索（嵌入）的默认模型。设置它们的说明将在相关任务中定义。

### 2.3 从门户配置Azure

Azure OpenAI端点和密钥值将在[Azure门户](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)中找到，所以我们从那里开始。

1. 进入[Azure门户](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. 点击侧栏中的**密钥和端点**选项（左侧菜单）。
1. 点击**显示密钥** - 您应该看到以下内容：密钥1、密钥2和端点。
1. 使用密钥1值作为AZURE_OPENAI_API_KEY
1. 使用端点值作为AZURE_OPENAI_ENDPOINT

接下来，我们需要获取我们已部署的特定模型的端点。

1. 点击侧栏中的**模型部署**选项（左侧菜单）以获取Azure OpenAI资源。
1. 在目标页面中，点击**管理部署**

这将带您到Azure OpenAI Studio网站，我们将在下面找到其他值。

### 2.4 从Studio配置Azure

1. 按照上述说明，从您的资源导航到[Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst)。
1. 点击**部署**选项卡（侧栏，左侧）以查看当前部署的模型。
1. 如果您的目标模型未部署，请使用**创建新部署**来部署它。
1. 您将需要一个_文本生成_模型 - 我们推荐：**gpt-35-turbo**
1. 您将需要一个_文本嵌入_模型 - 我们推荐**text-embedding-ada-002**

现在更新环境变量以反映使用的_部署名称_。这通常与模型名称相同，除非您显式更改它。因此，例如，您可能有：

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**完成后不要忘记保存.env文件**。您现在可以退出文件并返回运行笔记本的说明。

### 2.5 从个人资料配置OpenAI

您的OpenAI API密钥可以在您的[OpenAI账户](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst)中找到。如果您没有，可以注册一个账户并创建一个API密钥。一旦您有了密钥，可以用它来填充`.env`文件中的`OPENAI_API_KEY`变量。

### 2.6 从个人资料配置Hugging Face

您的Hugging Face令牌可以在您的个人资料中找到，位于[访问令牌](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst)下。不要公开发布或分享这些。相反，为这个项目使用创建一个新的令牌，并将其复制到`.env`文件中的`HUGGING_FACE_API_KEY`变量下。_注意：_这实际上不是一个API密钥，但用于身份验证，所以我们保持这种命名约定以保持一致性。

**免责声明**：
本文档已使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。虽然我们努力确保准确性，但请注意自动翻译可能包含错误或不准确之处。应将原始语言的文档视为权威来源。对于关键信息，建议进行专业人工翻译。对于因使用此翻译而产生的任何误解或误读，我们不承担责任。