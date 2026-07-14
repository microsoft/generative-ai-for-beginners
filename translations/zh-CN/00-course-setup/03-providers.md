# 选择和配置 LLM 提供商 🔑

作业 <strong>可能</strong> 也会设置为通过支持的服务提供商（如 OpenAI、Azure 或 Hugging Face）访问一个或多个大型语言模型（LLM）部署。这些提供了一个我们可以通过合适的凭据（API 密钥或令牌）以编程方式访问的 _托管端点_（API）。在本课程中，我们讨论以下提供商：

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) 拥有包括核心 GPT 系列的多样模型。
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) 以企业级准备为重点的 OpenAI 模型
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 通过单一端点和 API 密钥访问 OpenAI、Meta、Mistral、Cohere、Microsoft 等数百种模型（替代将于2026年7月底退役的 GitHub Models）
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) 开源模型和推理服务器
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) 或 [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) ，如果你希望完全在自己的设备离线运行模型，无需云订阅

<strong>这些练习需要你使用自己的账户</strong>。作业是可选的，因此你可以根据自己的兴趣选择设置其中一个、全部或不设置任何提供商。下面是一些注册指导：

| 注册 | 费用 | API 密钥 | 游乐场 | 备注 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [价格](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [基于项目](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [无代码，网页](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 多种模型可用 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [价格](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK 快速开始](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio 快速开始](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [须提前申请访问](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [价格](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [项目概览页面](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry 游乐场](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | 提供免费层；单个端点+密钥访问多模型提供商 |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [价格](https://huggingface.co/pricing) | [访问令牌](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging 聊天](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging 聊天支持有限模型](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | 免费（在你的设备上运行） | 不需要 | [本地 CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | 完全离线，兼容 OpenAI 端点 |
| | | | | |

按以下说明 _配置_ 此仓库以供不同提供商使用。需要特定提供商的作业文件名中将包含以下标签之一：

- `aoai` - 需要 Azure OpenAI 端点和密钥
- `oai` - 需要 OpenAI 端点和密钥
- `hf` - 需要 Hugging Face 令牌
- `githubmodels` - 需要 Microsoft Foundry Models 端点和密钥（GitHub Models 将于2026年7月底退役）

你可以配置其中一个、全部或者都不配置。关联的作业在未提供凭据时会出错。

## 创建 `.env` 文件

我们假定你已经阅读上述指南，注册了相关提供商，并获得了所需的认证凭据（API_KEY 或令牌）。对于 Azure OpenAI，我们假设你还部署了至少一个用于聊天完成的 GPT 模型的 Azure OpenAI 服务（端点）。

下一步是按以下方式配置你的 <strong>本地环境变量</strong>：

1. 在根文件夹中查找 `.env.copy` 文件，内容应类似如下：

   ```bash
   # OpenAI 提供者
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Microsoft Foundry 中的 Azure OpenAI
   ##（Azure OpenAI 服务现已成为 Microsoft Foundry 的一部分：https://ai.azure.com）
   AZURE_OPENAI_API_VERSION='2024-10-21' # 默认已设置！（当前稳定的正式版 API 版本）
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry 模型（多提供商模型目录，替代 GitHub 模型，后者将于 2026 年 7 月底退役）
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. 使用以下命令复制该文件为 `.env`。此文件已被 _gitignore_，以保护密钥安全。

   ```bash
   cp .env.copy .env
   ```

3. 按下一节所述填入各值（替换 `=` 右侧的占位符）。

4. （可选）如果你使用 GitHub Codespaces，可以选择将环境变量保存为与此仓库关联的 _Codespaces 秘密_。这样你就无需在本地设置 .env 文件。**但注意此选项仅适用于 GitHub Codespaces。** 如果使用 Docker Desktop，则仍需设置 .env 文件。

## 填写 `.env` 文件

我们快速看一下变量名及其含义：

| 变量名  | 说明  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 这是你在个人资料中设置的用户访问令牌 |
| OPENAI_API_KEY | 这是用于非 Azure OpenAI 端点的授权密钥 |
| AZURE_OPENAI_API_KEY | 这是 Azure OpenAI 服务的授权密钥 |
| AZURE_OPENAI_ENDPOINT | 这是 Azure OpenAI 资源的部署端点 |
| AZURE_OPENAI_DEPLOYMENT | 这是 _文本生成_ 模型的部署端点名 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | 这是 _文本嵌入_ 模型的部署端点名 |
| AZURE_INFERENCE_ENDPOINT | 这是你的 Microsoft Foundry 项目的端点，用于 Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | 这是你的 Microsoft Foundry 项目的 API 密钥 |
| | |

注意：最后两个 Azure OpenAI 变量分别对应聊天完成（文本生成）和向量搜索（嵌入）的默认模型。相关配置将在对应作业中说明。

## 配置 Azure OpenAI：通过门户

> **注意：** Azure OpenAI 服务现已整合到 [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) 中。资源及部署仍显示在 Azure 门户，但日常的模型管理（部署、游乐场、监控）现在在 Foundry 门户而非旧的独立“Azure OpenAI Studio”进行。

Azure OpenAI 的端点和密钥可在 [Azure 门户](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) 找到，我们从这里开始。

1. 访问 [Azure 门户](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. 点击侧边栏（左侧菜单）的 **Keys and Endpoint** 选项。
1. 点击 <strong>显示密钥</strong> - 你将看到 KEY 1、KEY 2 和端点信息。
1. 使用 KEY 1 作为 AZURE_OPENAI_API_KEY
1. 使用 Endpoint 作为 AZURE_OPENAI_ENDPOINT

接下来，我们需要获取具体部署模型的端点。

1. 点击 Azure OpenAI 资源侧边栏（左菜单）的 **Model deployments** 选项。
1. 在目标页面中，点击 **前往 Microsoft Foundry 门户**（或 <strong>管理部署</strong>，取决于资源类型）

这会把你带到 Microsoft Foundry 门户，我们将在这里找到其它必要值，如下所述。

## 配置 Azure OpenAI：通过 Microsoft Foundry 门户

1. 按上述说明，从你的资源访问 [Microsoft Foundry 门户](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)。
1. 点击左侧栏的 **Deployments** 标签，查看当前已部署的模型。
1. 如果所需模型未部署，可通过 <strong>部署模型</strong> 从 [模型目录](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 进行部署。
1. 你需要一个 _文本生成_ 模型 - 推荐：**gpt-4o-mini**
1. 你需要一个 _文本嵌入_ 模型 - 推荐 **text-embedding-3-small**

现在更新环境变量中的 _部署名称_ 。该名称通常和模型名称相同，除非你显式修改。举例来说，你可能会：

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**完成后别忘了保存 .env 文件**。保存后即可关闭该文件并返回后续笔记本运行说明。

## 配置 OpenAI：通过个人资料

你的 OpenAI API 密钥可以在你的 [OpenAI 账户](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) 中找到。如果尚无账户，可注册并创建 API 密钥。获取后，将该密钥填入 `.env` 文件中的 `OPENAI_API_KEY` 变量。

## 配置 Hugging Face：通过个人资料

你的 Hugging Face 令牌可在个人资料中的 [访问令牌](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) 页面找到。请勿公开分享这些令牌。建议为本项目专门创建一个新令牌，并将其复制到 `.env` 文件中的 `HUGGING_FACE_API_KEY` 变量中。_注意：_ 技术上这不是 API 密钥，但用于身份验证，因此为了统一起见，我们仍采用此命名。

## 配置 Microsoft Foundry Models：通过门户

> **注意：** GitHub Models 将于2026年7月底退役。Microsoft Foundry Models 是直接替代，提供相同的免费试用模型目录及 Azure AI 推理 SDK / OpenAI SDK 体验。

1. 访问 [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)，创建或打开一个 Foundry 项目。
1. 浏览 [模型目录](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 并部署一个模型，例如 `gpt-4o-mini`。
1. 在项目的 <strong>概览</strong> 页面，复制 <strong>端点</strong> 和 **API 密钥**。
1. 将端点值填入 `.env` 文件的 `AZURE_INFERENCE_ENDPOINT`，将密钥值填入 `AZURE_INFERENCE_CREDENTIAL`。

## 离线 / 本地提供商

如果你不想使用云订阅，可以直接在自己的设备上运行兼容的开源模型：

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - 微软的设备端运行时。它自动选择最佳执行提供者（NPU、GPU 或 CPU）并暴露兼容 OpenAI 的端点，因此你可以用本课程的大部分示例代码，几乎不做修改。参见 [Foundry Local 文档](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) 快速上手，或通过 `winget install Microsoft.FoundryLocal`（Windows）/ `brew install microsoft/foundrylocal/foundrylocal`（macOS）安装。
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - 一款流行的本地运行开源模型（如 Llama、Phi、Mistral 和 Gemma）的替代方案。


请参阅[第19课：使用SLM构建](../19-slm/README.md?WT.mc_id=academic-105485-koreyst)，了解使用这两种选项的实践示例。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->