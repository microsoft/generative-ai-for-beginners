<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T14:30:43+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "zh"
}
-->
# 选择与配置 LLM 提供商 🔑

作业**也可以**通过支持的服务商（如 OpenAI、Azure 或 Hugging Face）连接到一个或多个大型语言模型（LLM）部署。这些服务商会提供一个_托管的接口_（API），只要有正确的凭证（API 密钥或令牌），我们就能以编程方式访问。在本课程中，我们会讨论以下服务商：

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst)：拥有多种模型，包括核心的 GPT 系列。
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)：专注于企业级的 OpenAI 模型
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst)：提供开源模型和推理服务器

**这些练习需要你使用自己的账号。** 作业是可选的，你可以根据兴趣选择配置一个、全部或都不配置。注册建议如下：

| 注册 | 费用 | API 密钥 | Playground | 备注 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [价格](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [按项目分配](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [免代码，网页版](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 可用多种模型 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [价格](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK 快速入门](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio 快速入门](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [需提前申请访问权限](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [价格](https://huggingface.co/pricing) | [访问令牌](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat 支持的模型有限](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

按照下面的说明，_配置_本仓库以支持不同的服务商。需要特定服务商的作业文件名会包含以下标签之一：

- `aoai` - 需要 Azure OpenAI 的 endpoint 和密钥
- `oai` - 需要 OpenAI 的 endpoint 和密钥
- `hf` - 需要 Hugging Face 的令牌

你可以配置一个、全部或都不配置。相关作业如果缺少凭证会直接报错。

## 创建 `.env` 文件

我们假设你已经阅读了上面的说明，注册了相关服务商，并获得了所需的认证凭证（API_KEY 或令牌）。如果是 Azure OpenAI，还需要你已经部署了一个有效的 Azure OpenAI 服务（endpoint），并至少部署了一个 GPT 模型用于聊天补全。

下一步是按如下方式配置你的**本地环境变量**：

1. 在根目录下找到一个名为 `.env.copy` 的文件，内容大致如下：

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

2. 用下面的命令将该文件复制为 `.env`。此文件已被 _gitignore_，可以安全存放密钥。

   ```bash
   cp .env.copy .env
   ```

3. 按下一节说明填写具体的值（将 `=` 右侧的占位符替换为你的信息）。

4. （可选）如果你使用 GitHub Codespaces，可以选择将环境变量保存为与本仓库关联的 _Codespaces secrets_。这样就不需要本地设置 .env 文件。**但请注意，这个选项仅适用于 GitHub Codespaces。** 如果你用的是 Docker Desktop，还是需要配置 .env 文件。

## 填写 `.env` 文件

我们来快速了解一下变量名及其含义：

| 变量  | 说明  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 你在个人资料中设置的用户访问令牌 |
| OPENAI_API_KEY | 用于非 Azure OpenAI endpoint 的服务授权密钥 |
| AZURE_OPENAI_API_KEY | 用于该服务的授权密钥 |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI 资源的已部署 endpoint |
| AZURE_OPENAI_DEPLOYMENT | _文本生成_模型的部署名称 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _文本嵌入_模型的部署名称 |
| | |

注意：最后两个 Azure OpenAI 变量分别对应默认的聊天补全（文本生成）和向量搜索（嵌入）模型。具体设置方法会在相关作业中说明。

## 配置 Azure：通过 Portal

Azure OpenAI 的 endpoint 和密钥可以在 [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) 找到，步骤如下：

1. 进入 [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. 点击左侧菜单中的 **Keys and Endpoint** 选项。
1. 点击 **Show Keys**，你会看到：KEY 1、KEY 2 和 Endpoint。
1. 用 KEY 1 的值填写 AZURE_OPENAI_API_KEY
1. 用 Endpoint 的值填写 AZURE_OPENAI_ENDPOINT

接下来，需要获取你已部署模型的 endpoint。

1. 在 Azure OpenAI 资源的左侧菜单点击 **Model deployments** 选项。
1. 在目标页面点击 **Manage Deployments**

这会跳转到 Azure OpenAI Studio 网站，下面会说明如何获取其他变量。

## 配置 Azure：通过 Studio

1. 按上面说明，从你的资源进入 [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst)。
1. 点击左侧边栏的 **Deployments** 标签，查看当前已部署的模型。
1. 如果你想用的模型还没部署，可以用 **Create new deployment** 新建部署。
1. 你需要一个 _文本生成_ 模型，推荐使用：**gpt-35-turbo**
1. 你需要一个 _文本嵌入_ 模型，推荐使用 **text-embedding-ada-002**

现在，更新环境变量，填写你用的 _Deployment name_。通常和模型名一致，除非你自己改过。比如：

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**记得保存 .env 文件。** 完成后可以关闭文件，继续按照 notebook 的运行说明操作。

## 配置 OpenAI：通过个人资料

你的 OpenAI API 密钥可以在 [OpenAI 账号](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) 找到。如果还没有，可以注册账号并创建 API 密钥。拿到密钥后，把它填到 `.env` 文件里的 `OPENAI_API_KEY` 变量。

## 配置 Hugging Face：通过个人资料

你的 Hugging Face 令牌可以在个人资料的 [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) 下找到。不要公开或分享这些令牌。建议为本项目新建一个令牌，然后复制到 `.env` 文件的 `HUGGING_FACE_API_KEY` 变量下。_注意：_ 这其实不是 API 密钥，但用于认证，所以我们沿用这个命名以保持一致。

---

**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译。我们尽力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文件应被视为权威来源。对于关键信息，建议使用专业人工翻译。因使用本翻译而产生的任何误解或误读，我们概不负责。