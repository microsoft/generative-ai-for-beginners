# 选择和配置大型语言模型提供商 🔑

作业 <strong>也可以</strong> 设置为通过支持的服务提供商（如 OpenAI、Azure 或 Hugging Face）访问一个或多个大型语言模型（LLM）部署。这些提供了一个我们可以通过正确凭证（API 密钥或令牌）以编程方式访问的 _托管端点_（API）。本课程讨论以下提供商：

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) ，包含多样的模型，包括核心 GPT 系列。
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) ，注重企业级准备的 OpenAI 模型
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ，一个单一端点和 API 密钥访问来自 OpenAI、Meta、Mistral、Cohere、微软等数百种模型（替代将于 2026 年 7 月底退休的 GitHub Models）
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) ，用于开源模型和推理服务器
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) 或 [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) ，如果您更愿意完全离线在自己的设备上运行模型，无需云订阅

<strong>您需要使用自己的账户进行这些练习</strong>。作业是可选的，您可以根据兴趣选择设置一个、全部或不设置任何提供商。注册的部分指导如下：

| 注册 | 费用 | API 密钥 | 玩乐场 | 备注 |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [定价](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [基于项目](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [无代码，网页](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | 多模型可用 |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [定价](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK 快速入门](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio 快速入门](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [需预先申请访问](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [定价](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [项目概览页](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry 玩乐场](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | 有免费层；一个端点和密钥可访问多家模型提供商 |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [定价](https://huggingface.co/pricing) | [访问令牌](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat 支持的模型有限](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | 免费（在您的设备上运行） | 不需要 | [本地 CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | 完全离线，兼容 OpenAI 端点 |
| | | | | |

按照以下说明配置本仓库以用于不同的提供商。需要特定提供商的作业文件名中会包含以下标签之一：

- `aoai` - 需要 Azure OpenAI 端点和密钥
- `oai` - 需要 OpenAI 端点和密钥
- `hf` - 需要 Hugging Face 令牌
- `githubmodels` - 需要 Microsoft Foundry Models 端点和密钥（GitHub Models 将于 2026 年 7 月底退休）

您可以配置一个、没有或全部提供商。未填写凭证的相关作业将在运行时出错。

## 创建 `.env` 文件

我们假设您已经阅读上述指导，并在相关提供商注册，获得了所需的认证凭据（API_KEY 或令牌）。对于 Azure OpenAI，我们假设您也有一个有效的 Azure OpenAI 服务（端点）部署，并已经部署了至少一个用于聊天完成的 GPT 模型。

下一步是按如下方式配置您的 <strong>本地环境变量</strong>：

1. 在根文件夹找到一个 `.env.copy` 文件，应该包含如下内容：

   ```bash
   # OpenAI 提供者
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Microsoft Foundry 中的 Azure OpenAI
   ## （Azure OpenAI 服务现为 Microsoft Foundry 的一部分：https://ai.azure.com）
   AZURE_OPENAI_API_VERSION='2024-10-21' # 默认已设置！（当前稳定 GA API 版本）
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry 模型（多提供者模型目录，取代 GitHub 模型，后者将于2026年7月底退役）
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. 使用下面命令复制该文件为 `.env`。此文件列入 `.gitignore`，以保证密钥安全。

   ```bash
   cp .env.copy .env
   ```

3. 按下一节说明，填写等号右侧的值（替换占位符）。

4. （可选）如果您使用 GitHub Codespaces，可以选择将环境变量保存为与此仓库相关联的 _Codespaces 秘钥_。这样您就无需设置本地 `.env` 文件。**但是请注意，此选项仅在使用 GitHub Codespaces 情境下有效。** 如果您使用 Docker Desktop，仍需设置 `.env` 文件。

## 填写 `.env` 文件

我们简要查看一下变量名，以了解它们分别代表什么：

| 变量名  | 描述  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | 这是您在个人资料中设置的用户访问令牌 |
| OPENAI_API_KEY | 用于非 Azure OpenAI 端点的授权密钥 |
| AZURE_OPENAI_API_KEY | 用于该服务的授权密钥 |
| AZURE_OPENAI_ENDPOINT | Azure OpenAI 资源的已部署端点 |
| AZURE_OPENAI_DEPLOYMENT | _文本生成_ 模型的部署端点 |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | _文本嵌入_ 模型的部署端点 |
| AZURE_INFERENCE_ENDPOINT | 您的 Microsoft Foundry 项目的端点，用于 Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | 您的 Microsoft Foundry 项目的 API 密钥 |
| | |

注意：最后两个 Azure OpenAI 变量分别对应默认的聊天完成（文本生成）模型和向量搜索（嵌入）模型。设置方法将在相关作业中说明。

## 配置 Azure OpenAI：通过门户

> **注意：** Azure OpenAI 服务现在已整合到 [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)。资源和部署仍在 Azure 门户显示，但日常模型管理（部署、玩乐场、监控）现改在 Foundry 门户，而不再使用旧的独立“Azure OpenAI Studio”。

Azure OpenAI 的端点和密钥值可以在 [Azure 门户](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) 找到，因此我们从那里开始。

1. 访问 [Azure 门户](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. 点击侧边栏（左侧菜单）中的 <strong>密钥和端点</strong> 选项。
1. 点击 <strong>显示密钥</strong> — 您应能看到以下内容：密钥 1、密钥 2 和端点。
1. 使用密钥 1 的内容作为 AZURE_OPENAI_API_KEY
1. 使用端点内容作为 AZURE_OPENAI_ENDPOINT

接下来，我们需要针对已部署的具体模型获取端点。

1. 点击 Azure OpenAI 资源侧边栏（左菜单）中的 <strong>模型部署</strong> 选项。
1. 在目标页面中，点击 **前往 Microsoft Foundry 门户**（或 <strong>管理部署</strong>，视资源类型而定）

此操作将带您进入 Microsoft Foundry 门户，下面会描述如何找到其它值。

## 配置 Azure OpenAI：通过 Microsoft Foundry 门户

1. 按上述说明从您的资源进入 [Microsoft Foundry 门户](https://ai.azure.com?WT.mc_id=academic-105485-koreyst)。
1. 点击 <strong>部署</strong> 选项卡（侧栏，左侧）查看当前已部署模型。
1. 如果还未部署所需模型，可通过 <strong>部署模型</strong> 从 [模型目录](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 中部署它。
1. 您需要一个 _文本生成_ 模型 — 推荐：**gpt-5-mini**
1. 您需要一个 _文本嵌入_ 模型 — 推荐：**text-embedding-3-small**

现在更新环境变量以反映所用的 _部署名称_。通常该名称与模型名称相同，除非您显式修改过。举例如下：

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**编辑完毕后别忘了保存 .env 文件**。现在您可以关闭文件，返回执行笔记本的说明。

## 配置 OpenAI：通过个人资料

您的 OpenAI API 密钥可以在您的 [OpenAI 账号](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) 中找到。如果没有账号，可以注册后创建 API 密钥。获取密钥后，将其填入 `.env` 文件中的 `OPENAI_API_KEY` 变量。

## 配置 Hugging Face：通过个人资料

您的 Hugging Face 令牌可在个人资料中的 [访问令牌](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) 处找到。请勿公开分享或发布。建议为此项目创建新的令牌，并将其复制到 `.env` 文件的 `HUGGING_FACE_API_KEY` 变量中。_注：_ 这实际上不是 API 密钥，但用于身份验证，因此我们保持该命名方便统一。

## 配置 Microsoft Foundry Models：通过门户

> **注意：** GitHub Models 将于 2026 年 7 月底退休。Microsoft Foundry Models 是其直接替代方案，提供相同的免费试用模型目录和 Azure AI 推理 SDK / OpenAI SDK 体验。

1. 访问 [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) 并创建（或打开）一个 Foundry 项目。
1. 浏览 [模型目录](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 并部署一个模型，例如 `gpt-5-mini`。
1. 在项目的 <strong>概览</strong> 页面，复制 <strong>端点</strong> 和 **API 密钥**。
1. 在 `.env` 文件中，分别将端点填入 `AZURE_INFERENCE_ENDPOINT`，将密钥填入 `AZURE_INFERENCE_CREDENTIAL`。

## 离线 / 本地提供商

如果您完全不想使用云订阅，可以直接在自己的设备上运行兼容的开源模型：

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - 微软的设备端运行时。它自动选择最佳执行提供商（NPU、GPU 或 CPU），并暴露一个兼容 OpenAI 的端点，因此您可以用本课程的大部分示例代码，并做最小改动即可。详情请参见 [Foundry Local 文档](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst)，或使用命令 `winget install Microsoft.FoundryLocal`（Windows） / `brew install microsoft/foundrylocal/foundrylocal`（macOS）安装。
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - 一款流行的本地运行开源模型的替代方案，支持 Llama、Phi、Mistral 和 Gemma 等模型。


有关使用这两种选项的实操示例，请参见[第19课：使用SLM构建](../19-slm/README.md?WT.mc_id=academic-105485-koreyst)。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->