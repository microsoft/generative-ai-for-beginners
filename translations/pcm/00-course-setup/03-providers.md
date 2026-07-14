# Chọs & Konfiga wan LLM Provider 🔑

Assignments fit sef set up to work wit one or more Large Language Model (LLM) deployments thru wan supported service provider like OpenAI, Azure or Hugging Face. Dem dey provide _hosted endpoint_ (API) wey we fit access prográmmatically wit di correct credentials (API key or token). For dis course, we go talk about these providers:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) wit different models including di core GPT series.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) for OpenAI models wit enterprise readiness for mind
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) for one endpoint and API key to access plenty models from OpenAI, Meta, Mistral, Cohere, Microsoft and more (dis one go replace GitHub Models, wey dem dey retire for end of July 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) for open-source models and inference server
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) or [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) if you prefer run models full offline for your own device, no need subscription for cloud

**You go need your own accounts for these exercises**. Assignments no mandatory so you fit choose to setup one provider, all of dem - or none - based on your interest dem. Small guidance for signup:

| Signup | Cost | API Key | Playground | Comments |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Pricing](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Project-based](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Plenty Models dey |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [You Must Apply Before To Access](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Pricing](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Project Overview page](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Free tier dey; one endpoint + key for many model providers |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Pricing](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat get limited models](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Free (e go run na your device) | No need | [Local CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Fully offline, OpenAI-compatible endpoint |
| | | | | |

Follow di instructions wey dey below to _configure_ dis repository for use with different providers. Assignments wey require specific provider go get one of these tags for dia filename:

- `aoai` - require Azure OpenAI endpoint, key
- `oai` - require OpenAI endpoint, key
- `hf` - require Hugging Face token
- `githubmodels` - require Microsoft Foundry Models endpoint, key (GitHub Models dey retire for end of July 2026)

You fit configure one, none, or all providers. Related assignments go just get error if credentials no dey.

## Create `.env` file

We assume sey you don already read di instructions for signup and you don sign up wit di provider wey concern you, and you don get di needed authentication credentials (API_KEY or token). For Azure OpenAI, we assume say you get one valid deployment of Azure OpenAI Service (endpoint) wit at least one GPT model deployed for chat completion.

Di next step na to configure your **local environment variables** like dis:

1. Find di root folder and look for `.env.copy` file wey get contents wey go look like dis:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI for Microsoft Foundry
   ## (Azure OpenAI Service don become part of Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Default don set! (current stable GA API version)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry Models (multi-provider model catalog, e dey replace GitHub Models, wey go stop for end of July 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Copy dat file to `.env` wit dis command below. Dis file na _gitignore-d_, e dey keep your secrets safe.

   ```bash
   cp .env.copy .env
   ```

3. Fill di correct values (replace di placeholders for right side after `=`) as e go talk for next section.

4. (Optional) If you dey use GitHub Codespaces, you fit save environment variables as _Codespaces secrets_ wey dem connect to dis repository. If so, you no go need set up local .env file. **But note say dis one only work if you dey use GitHub Codespaces.** If you dey run Docker Desktop, you still go need set .env file.

## Populate `.env` file

Make we quick run through di variable names to understand wetin dem mean:

| Variable  | Meaning  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Dis na user access token wey you set for your profile |
| OPENAI_API_KEY | Dis na di authorization key to use the service for non-Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Dis na di authorization key to use dat service |
| AZURE_OPENAI_ENDPOINT | Dis na di deployed endpoint for Azure OpenAI resource |
| AZURE_OPENAI_DEPLOYMENT | Dis na di _text generation_ model deployment endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Dis na di _text embeddings_ model deployment endpoint |
| AZURE_INFERENCE_ENDPOINT | Dis na di endpoint for your Microsoft Foundry project, to use Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Dis na di API key for your Microsoft Foundry project |
| | |

Note: Di last two Azure OpenAI variables dey represent default model for chat completion (text generation) and vector search (embeddings) respectively. Di instruction for how to set dem go dey inside relevant assignments.

## Configure Azure OpenAI: From Portal

> **Note:** Azure OpenAI Service now be part of [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Resources and deployments still dey for Azure Portal, but daily model management (deployments, playground, monitoring) go happen for Foundry portal instead of di old "Azure OpenAI Studio".

You go find Azure OpenAI endpoint and key values for the [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), so make we start there.

1. Go to [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Click **Keys and Endpoint** option for sidebar (menu for left).
1. Click **Show Keys** - you suppose see dis: KEY 1, KEY 2 and Endpoint.
1. Use KEY 1 value for AZURE_OPENAI_API_KEY
1. Use Endpoint value for AZURE_OPENAI_ENDPOINT

Next, we need di endpoints for specific models wey we don deploy.

1. Click **Model deployments** option for sidebar (left menu) for Azure OpenAI resource.
1. For di page wey open, click **Go to Microsoft Foundry portal** (or **Manage Deployments**, depend on your resource type)

Dis go carry you go Microsoft Foundry portal, where we go find di other necessary values as we explain below.

## Configure Azure OpenAI: From Microsoft Foundry portal

1. Navigate go [Microsoft Foundry portal](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **from your resource** as we explain before.
1. Click **Deployments** tab (sidebar, left) to see models wey deployed now.
1. If di model wey you want no dey, use **Deploy model** to deploy am from di [model catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. You go need _text-generation_ model - we recommend: **gpt-4o-mini**
1. You go need _text-embedding_ model - we recommend **text-embedding-3-small**

Now update your environment variables to show di _Deployment name_ wey you use. Usually, na di same name as di model unless you change am yourself. So for example, you fit get:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**No forget to save di .env file when you finish**. You fit now close di file and continue with instructions to run di notebook.

## Configure OpenAI: From Profile

Your OpenAI API key go dey your [OpenAI account](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). If you no get one, you fit sign up and create API key. After you get am, you fit put am for `OPENAI_API_KEY` variable for `.env` file.

## Configure Hugging Face: From Profile

Your Hugging Face token fit dey your profile under [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). No post or share am publicly. Instead, create new token for dis project and copy am to `.env` file under `HUGGING_FACE_API_KEY`. _Note:_ E no be real API key, but e dey used for authentication, so we dey keep di name for consistency.

## Configure Microsoft Foundry Models: From Portal

> **Note:** GitHub Models dey retire end of July 2026. Microsoft Foundry Models na wetin go replace am direct, e still get same free-to-try model catalog and Azure AI Inference SDK / OpenAI SDK experience.

1. Go [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) create or open Foundry project.
1. Browse di [model catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) and deploy model, e.g. `gpt-4o-mini`.
1. For di project's **Overview** page, copy di **endpoint** and di **API key**.
1. Use di endpoint value for `AZURE_INFERENCE_ENDPOINT` and key for `AZURE_INFERENCE_CREDENTIAL` for your `.env` file.

## Offline / Local Providers

If you no want use any cloud subscription at all, you fit run compatible open models for your own device:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoft on-device runtime. E go choose di best execution provider (NPU, GPU, or CPU) by itself and e dey expose OpenAI-compatible endpoint, so you fit use most of di sample code for dis course with small changes. Check [Foundry Local documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) to start, or install wit `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - popular alternative to run open models like Llama, Phi, Mistral, and Gemma locally.


See [Lesson 19: Building with SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) for hands-on examples using both options.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->