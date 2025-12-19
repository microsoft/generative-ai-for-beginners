<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b5b016b0eb8a1cef2e3097620d8aa23",
  "translation_date": "2025-12-19T13:19:09+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "zh"
}
-->
# 选择和配置 LLM 提供商 🔑

作业**可能**也会设置为通过支持的服务提供商（如 OpenAI、Azure 或 Hugging Face）对一个或多个大型语言模型（LLM）部署进行操作。这些提供了一个我们可以通过正确凭据（API 密钥或令牌）以编程方式访问的_托管端点_（API）。在本课程中，我们讨论以下提供商：

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst)，提供包括核心 GPT 系列在内的多样化模型。
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)，专注于企业级准备的 OpenAI 模型。
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst)，提供开源模型和推理服务器。

**您需要使用自己的账户完成这些练习**。作业是可选的，因此您可以根据兴趣选择设置一个、全部或不设置任何提供商。以下是一些注册指导：

| 注册 | 费用 | API 密钥 | Playground | 备注 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [价格](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [基于项目](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [无代码，网页](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 多种模型可用 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [价格](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK 快速入门](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio 快速入门](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [必须提前申请访问](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [价格](https://huggingface.co/pricing) | [访问令牌](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat 模型有限](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

请按照以下说明为不同提供商_配置_此仓库。需要特定提供商的作业文件名中会包含以下标签之一：

- `aoai` - 需要 Azure OpenAI 端点和密钥
- `oai` - 需要 OpenAI 端点和密钥
- `hf` - 需要 Hugging Face 令牌

您可以配置一个、多个或全部提供商。相关作业在缺少凭据时会报错。

## 创建 `.env` 文件

我们假设您已经阅读了上述指导，注册了相关提供商，并获得了所需的认证凭据（API_KEY 或令牌）。对于 Azure OpenAI，我们假设您还拥有一个有效的 Azure OpenAI 服务部署（端点），并且至少部署了一个用于聊天完成的 GPT 模型。

下一步是按如下方式配置您的**本地环境变量**：

1. 在根目录查找 `.env.copy` 文件，内容应类似如下：

   ```bash
   # OpenAI 提供者
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # 默认已设置！
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. 使用以下命令将该文件复制为 `.env`。此文件已被 _gitignore_，可确保秘密安全。

   ```bash
   cp .env.copy .env
   ```

3. 按下一节描述填写值（替换 `=` 右侧的占位符）。

4. （可选）如果您使用 GitHub Codespaces，可以选择将环境变量保存为与此仓库关联的 _Codespaces secrets_。这样就不需要设置本地 .env 文件。**但请注意，此选项仅适用于 GitHub Codespaces。** 如果使用 Docker Desktop，仍需设置 .env 文件。

## 填充 `.env` 文件

快速了解变量名及其含义：

| 变量名  | 描述  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 您在个人资料中设置的用户访问令牌 |
| OPENAI_API_KEY | 用于非 Azure OpenAI 端点的服务授权密钥 |
| AZURE_OPENAI_API_KEY | 用于 Azure OpenAI 服务的授权密钥 |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI 资源的部署端点 |
| AZURE_OPENAI_DEPLOYMENT | _文本生成_ 模型部署端点 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _文本嵌入_ 模型部署端点 |
| | |

注意：最后两个 Azure OpenAI 变量分别对应聊天完成（文本生成）和向量搜索（嵌入）的默认模型。相关作业中会定义设置说明。

## 配置 Azure：从门户

Azure OpenAI 端点和密钥值可在 [Azure 门户](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) 中找到，我们从这里开始。

1. 访问 [Azure 门户](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. 点击侧边栏（左侧菜单）中的 **密钥和端点** 选项。
1. 点击 **显示密钥** - 您应看到 KEY 1、KEY 2 和端点。
1. 使用 KEY 1 的值作为 AZURE_OPENAI_API_KEY
1. 使用端点值作为 AZURE_OPENAI_ENDPOINT

接下来，我们需要获取已部署的具体模型端点。

1. 点击 Azure OpenAI 资源侧边栏（左菜单）中的 **模型部署** 选项。
1. 在目标页面点击 **管理部署**

这将带您进入 Azure OpenAI Studio 网站，我们将在那里找到其他值，如下所述。

## 配置 Azure：从 Studio

1. 按上述说明从您的资源访问 [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst)。
1. 点击左侧边栏的 **部署** 标签，查看当前已部署的模型。
1. 如果所需模型未部署，使用 **创建新部署** 进行部署。
1. 您需要一个 _文本生成_ 模型 - 推荐：**gpt-35-turbo**
1. 您需要一个 _文本嵌入_ 模型 - 推荐：**text-embedding-ada-002**

现在更新环境变量以反映所用的_部署名称_。通常这与模型名称相同，除非您显式更改。例如，您可能有：

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**完成后别忘了保存 .env 文件**。然后可以退出文件，继续执行笔记本的说明。

## 配置 OpenAI：从个人资料

您的 OpenAI API 密钥可在您的 [OpenAI 账户](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) 中找到。如果没有，可以注册账户并创建 API 密钥。获得密钥后，将其填入 `.env` 文件中的 `OPENAI_API_KEY` 变量。

## 配置 Hugging Face：从个人资料

您的 Hugging Face 令牌可在个人资料的 [访问令牌](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) 中找到。请勿公开发布或分享。建议为本项目创建新的令牌，并将其复制到 `.env` 文件中的 `HUGGING_FACE_API_KEY` 变量。_注意：_ 这技术上不是 API 密钥，但用于认证，因此我们保持此命名惯例以保持一致。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件由人工智能翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译。虽然我们力求准确，但请注意自动翻译可能存在错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。因使用本翻译而产生的任何误解或误释，我们概不负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->