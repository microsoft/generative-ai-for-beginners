<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:23:30+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "zh"
}
-->
# 设置开发环境

我们为此仓库和课程配置了一个[开发容器](https://containers.dev?WT.mc_id=academic-105485-koreyst)，它包含一个通用运行时，支持 Python3、.NET、Node.js 和 Java 开发。相关配置定义在仓库根目录下 `.devcontainer/` 文件夹中的 `devcontainer.json` 文件里。

要激活开发容器，可以在[GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst)（云端运行时）或[Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst)（本地设备运行时）中启动。有关开发容器在 VS Code 中工作原理的更多细节，请参阅[此文档](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst)。

> [!TIP]  
> 我们推荐使用 GitHub Codespaces 以快速开始且操作简便。它为个人账户提供了慷慨的[免费使用额度](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst)。你可以配置[超时设置](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst)，自动停止或删除不活跃的 codespaces，以最大化额度利用。

## 1. 执行作业

每节课都会提供 _可选_ 的作业，可能包含一种或多种编程语言版本，包括 Python、.NET/C#、Java 和 JavaScript/TypeScript。本节提供执行这些作业的一般指导。

### 1.1 Python 作业

Python 作业以应用程序（`.py` 文件）或 Jupyter 笔记本（`.ipynb` 文件）形式提供。  
- 运行笔记本时，在 Visual Studio Code 中打开它，点击右上角的 _选择内核_，选择默认的 Python 3 选项。然后你可以点击 _全部运行_ 来执行笔记本。  
- 从命令行运行 Python 应用程序时，请按照作业的具体说明，确保选择正确的文件并提供所需参数。

## 2. 配置服务提供商

作业**可能**需要通过支持的服务提供商（如 OpenAI、Azure 或 Hugging Face）连接一个或多个大型语言模型（LLM）部署。这些服务提供一个 _托管端点_（API），我们可以通过正确的凭据（API 密钥或令牌）以编程方式访问。在本课程中，我们讨论以下提供商：

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst)，提供多种模型，包括核心的 GPT 系列。  
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)，专注于企业级的 OpenAI 模型。  
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst)，提供开源模型和推理服务器。

**你需要使用自己的账户完成这些练习**。作业是可选的，你可以根据兴趣选择配置其中一个、全部或不配置任何提供商。以下是注册的一些指导：

| 注册 | 费用 | API 密钥 | Playground | 备注 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [价格](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [基于项目](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [无代码，网页](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 多种模型可用 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [价格](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [SDK 快速入门](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Studio 快速入门](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [需提前申请访问](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [价格](https://huggingface.co/pricing) | [访问令牌](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Hugging Chat 模型有限](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

请按照以下说明为不同提供商 _配置_ 本仓库。需要特定提供商的作业文件名中会包含以下标签之一：  
- `aoai` - 需要 Azure OpenAI 端点和密钥  
- `oai` - 需要 OpenAI 端点和密钥  
- `hf` - 需要 Hugging Face 令牌  

你可以配置一个、多个或不配置任何提供商。缺少凭据时，相关作业会报错。

### 2.1 创建 `.env` 文件

假设你已经阅读了上述指导，注册了相关提供商，并获得了所需的认证凭据（API_KEY 或令牌）。对于 Azure OpenAI，我们假设你还拥有一个有效的 Azure OpenAI 服务部署（端点），并至少部署了一个用于聊天完成的 GPT 模型。

下一步是配置你的**本地环境变量**，步骤如下：

1. 在根目录查找 `.env.copy` 文件，内容类似于：

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

2. 使用以下命令将该文件复制为 `.env`。此文件已被 _gitignore_，可确保密钥安全。

   ```bash
   cp .env.copy .env
   ```

3. 按下一节说明填写变量值（替换 `=` 右侧的占位符）。

3.（可选）如果你使用 GitHub Codespaces，可以选择将环境变量保存为与本仓库关联的 _Codespaces secrets_。这样就不需要本地设置 `.env` 文件。**但请注意，此选项仅适用于 GitHub Codespaces。**如果使用 Docker Desktop，仍需设置 `.env` 文件。

### 2.2 填写 `.env` 文件

快速了解变量名及其含义：

| 变量名 | 说明 |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 你在个人资料中设置的用户访问令牌 |
| OPENAI_API_KEY | 用于非 Azure OpenAI 端点的服务授权密钥 |
| AZURE_OPENAI_API_KEY | Azure OpenAI 服务的授权密钥 |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI 资源的部署端点 |
| AZURE_OPENAI_DEPLOYMENT | _文本生成_ 模型的部署端点 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _文本嵌入_ 模型的部署端点 |
| | |

注意：最后两个 Azure OpenAI 变量分别对应聊天完成（文本生成）和向量搜索（嵌入）的默认模型。相关作业中会说明如何设置。

### 2.3 通过门户配置 Azure

Azure OpenAI 的端点和密钥可在[Azure 门户](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)中找到，步骤如下：

1. 访问[Azure 门户](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
2. 点击侧边栏（左侧菜单）中的 **Keys and Endpoint** 选项  
3. 点击 **显示密钥**，你会看到 KEY 1、KEY 2 和 Endpoint  
4. 使用 KEY 1 的值填入 AZURE_OPENAI_API_KEY  
5. 使用 Endpoint 的值填入 AZURE_OPENAI_ENDPOINT  

接下来需要获取已部署模型的端点：

1. 在 Azure OpenAI 资源的侧边栏点击 **Model deployments**  
2. 在目标页面点击 **管理部署**  

这会跳转到 Azure OpenAI Studio 网站，接下来我们将在那里找到其他所需值。

### 2.4 通过 Studio 配置 Azure

1. 按上述方法从你的资源访问 [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst)  
2. 点击左侧栏的 **Deployments** 标签，查看当前已部署的模型  
3. 如果没有你需要的模型，点击 **创建新部署** 进行部署  
4. 你需要一个 _文本生成_ 模型，推荐使用：**gpt-35-turbo**  
5. 你需要一个 _文本嵌入_ 模型，推荐使用：**text-embedding-ada-002**  

然后更新环境变量，填写所用的 _部署名称_。通常部署名称与模型名称相同，除非你显式更改过。例如，你可能会有：

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**完成后别忘了保存 .env 文件**。保存后即可关闭文件，继续执行笔记本的相关说明。

### 2.5 通过个人资料配置 OpenAI

你的 OpenAI API 密钥可在你的[OpenAI 账户](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst)中找到。如果没有账户，可以注册并创建 API 密钥。获得密钥后，将其填入 `.env` 文件中的 `OPENAI_API_KEY` 变量。

### 2.6 通过个人资料配置 Hugging Face

你的 Hugging Face 令牌可在个人资料的[访问令牌](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst)页面找到。请勿公开或分享这些令牌。建议为本项目创建新的令牌，并将其复制到 `.env` 文件中的 `HUGGING_FACE_API_KEY` 变量。  
_注意：_ 这技术上不是 API 密钥，但用于身份验证，因此我们保持此命名以保持一致性。

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议采用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。