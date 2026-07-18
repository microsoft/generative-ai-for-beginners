# Chọs & Setup LLM Provider 🔑

Assignments fit also setup make dem work wit one or plus Large Language Model (LLM) deployments through supported service provider like OpenAI, Azure or Hugging Face. Dem dey provide _hosted endpoint_ (API) we fit access programmatically if we get correct credentials (API key or token). For dis course, we go talk about dis providers:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) get different models including the core GPT series.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) for OpenAI models wey focus on enterprise readiness
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) get one endpoint and API key wey fit access hundreds models from OpenAI, Meta, Mistral, Cohere, Microsoft and more (e dey replace GitHub Models, wey go retire for end July 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) get open-source models and inference server
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) or [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) if you dey prefer run models fully offline for your own device, no cloud subscription required

**You go need to use your own accounts for these exercises**. Assignments na optional so you fit choose setup one, all - or none - of the providers based on wetin you like. Some advice for signup:

| Signup | Cost | API Key | Playground | Comments |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Pricing](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Project-based](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Plenty Models Available |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [You Must Apply Ahead To Access](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Pricing](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Project Overview page](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Free tier dey; one endpoint + key for many model providers |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Pricing](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat get limited models](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Free (e dey run for your device) | No need | [Local CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Fully offline, OpenAI-compatible endpoint |
| | | | | |

Follow di way wey dem talk below to _configure_ dis repository to work with different providers. Assignments wey need specific provider go get one of these tags for their filename:

- `aoai` - need Azure OpenAI endpoint, key
- `oai` - need OpenAI endpoint, key
- `hf` - need Hugging Face token
- `githubmodels` - need Microsoft Foundry Models endpoint, key (GitHub Models go retire for end July 2026)

You fit configure one, none, or all providers. Related assignments go just show error if credentials no dey.

## Create `.env` file

We assume say you don already read di advice above and you don sign up with the correct provider, and you don get the necessary authentication credentials (API_KEY or token). For Azure OpenAI, we assume say you also get valid deployment of Azure OpenAI Service (endpoint) with at least one GPT model deployed for chat completion.

Next step na to configure your **local environment variables** as e follow:

1. Look for `.env.copy` file inside root folder wey go get content like dis:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI for Microsoft Foundry
   ## (Azure OpenAI Service don join Microsoft Foundry now: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Default don set! (current stable GA API version)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry Models (multi-provider model catalog, e replace GitHub Models, wey go retire end of July 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Copy that file to `.env` using di command wey dey below. This file na _gitignore-d_, to keep secrets safe.

   ```bash
   cp .env.copy .env
   ```

3. Fill di values (replace di placeholders for the right side of `=`) as e go follow for next section.

4. (Option) If you dey use GitHub Codespaces, you fit save environment variables as _Codespaces secrets_ wey dey associated with dis repository. If na so, you no go need setup local .env file. **But, you supposed sabi say dis option only work if you dey use GitHub Codespaces.** You go still need setup .env file if you dey use Docker Desktop.

## Populate `.env` file

Make we quickly check di variable names so you go sabi wetin dem mean:

| Variable  | Description  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Na dis user access token wey you setup for your profile |
| OPENAI_API_KEY | Na di authorization key for use service for non-Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Na di authorization key for use dat service |
| AZURE_OPENAI_ENDPOINT | Na di deployed endpoint for Azure OpenAI resource |
| AZURE_OPENAI_DEPLOYMENT | Na di _text generation_ model deployment endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Na di _text embeddings_ model deployment endpoint |
| AZURE_INFERENCE_ENDPOINT | Na di endpoint for your Microsoft Foundry project, wey dem use for Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Na di API key for your Microsoft Foundry project |
| | |

Note: The last two Azure OpenAI variables dey represent default model for chat completion (text generation) and vector search (embeddings) respectively. Instructions to set dem go dey for relevant assignments.

## Configure Azure OpenAI: From Portal

> **Note:** Azure OpenAI Service don become part of [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) now. Resources and deployments still dey show wit for Azure Portal, but the daily model management (deployments, playground, monitoring) dey happen for Foundry portal instead of the old standalone "Azure OpenAI Studio".

You go fit find Azure OpenAI endpoint and key values for [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), so make we start there.

1. Go to the [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Click **Keys and Endpoint** option for sidebar (menu for left).
1. Click **Show Keys** - you go see dis thing: KEY 1, KEY 2 and Endpoint.
1. Use the KEY 1 value for AZURE_OPENAI_API_KEY
1. Use the Endpoint value for AZURE_OPENAI_ENDPOINT

Next, we need di endpoints for the specific models wey you deploy.

1. Click **Model deployments** option for sidebar (left menu) for Azure OpenAI resource.
1. For di page wea open, click **Go to Microsoft Foundry portal** (or **Manage Deployments**, depend on your resource type)

Dis one go carry you go Microsoft Foundry portal, wey we go find the other values as e follow below.

## Configure Azure OpenAI: From Microsoft Foundry portal

1. Navigate to [Microsoft Foundry portal](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **from your resource** as dem talk before.
1. Click **Deployments** tab (sidebar, left) to see models wey dey already deployed.
1. If the model wey you want no still dey deployed, use **Deploy model** to deploy from the [model catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. You go need one _text-generation_ model - we recommend: **gpt-5-mini**
1. You go need one _text-embedding_ model - we recommend **text-embedding-3-small**

Now update the environment variables make dem reflect di _Deployment name_ wey you use. Normally e go be di same as di model name unless you change am well well. So, example, you fit get:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**No forget to save the .env file when you finish**. You fit comot for the file and continue with instructions to run notebook.

## Configure OpenAI: From Profile

Your OpenAI API key fit dey your [OpenAI account](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). If you never get one, you fit sign up and create API key. When you get am, use am put for the `OPENAI_API_KEY` variable inside the `.env` file.

## Configure Hugging Face: From Profile

Your Hugging Face token fit dey your profile under [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). No make you post am or share am public. Instead, create new token for dis project use and copy am enter the `.env` file under `HUGGING_FACE_API_KEY` variable. _Note:_ Dis one no be API key strictly but na im dem dey use for authentication, so we dey keep di name for consistency.

## Configure Microsoft Foundry Models: From Portal

> **Note:** GitHub Models go retire for end July 2026. Microsoft Foundry Models na direct replacement, e dey offer same free-to-try model catalog and Azure AI Inference SDK / OpenAI SDK experience.

1. Go to [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) and create or open Foundry project.
1. Browse [model catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) and deploy model, example `gpt-5-mini`.
1. For project **Overview** page, copy **endpoint** and **API key**.
1. Use endpoint value for `AZURE_INFERENCE_ENDPOINT` and key value for `AZURE_INFERENCE_CREDENTIAL` inside your `.env` file.

## Offline / Local Providers

If you no wan use cloud subscription at all, you fit run open models wey compatible directly for your own device:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoft on-device runtime. E dey automatically select best execution provider (NPU, GPU, or CPU) and e expose OpenAI-compatible endpoint, so you fit use most sample code for dis course wit small change. Check [Foundry Local documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) to start, or install wit `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - popular choice to run open models like Llama, Phi, Mistral, and Gemma locally.


See [Lesson 19: Building with SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) for hands-on examples wey dey use both options.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->