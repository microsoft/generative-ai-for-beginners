# Choosing & Configuring an LLM Provider 🔑

Assignments **may** also be setup to work against one or more Large Language Model (LLM) deployments through a supported service provider like OpenAI, Azure or Hugging Face. These provide a _hosted endpoint_ (API) that we can access programmatically with the right credentials (API key or token). In this course, we discuss these providers:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) with diverse models including the core GPT series.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) for OpenAI models with enterprise readiness in focus
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) for a single endpoint and API key to access hundreds of models from OpenAI, Meta, Mistral, Cohere, Microsoft and more (replaces GitHub Models, which is retiring at the end of July 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) for open-source models and inference server
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) or [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) if you'd rather run models fully offline on your own device, with no cloud subscription required

**You will need to use your own accounts for these exercises**. Assignments are optional so you can choose to setup one, all - or none - of the providers based on your interests. Some guidance for signup:

| Signup | Cost | API Key | Playground | Comments |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Pricing](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Project-based](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Multiple Models Available |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Must Apply Ahead For Access](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Pricing](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Project Overview page](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Free tier available; one endpoint + key for many model providers |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Pricing](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat has limited models](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Free (runs on your device) | Not required | [Local CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Fully offline, OpenAI-compatible endpoint |
| | | | | |

Follow the directions below to _configure_ this repository for use with different providers. Assignments that require a specific provider will contain one of these tags in their filename:

- `aoai` - requires Azure OpenAI endpoint, key
- `oai` - requires OpenAI endpoint, key
- `hf` - requires Hugging Face token
- `githubmodels` - requires Microsoft Foundry Models endpoint, key (GitHub Models is retiring at the end of July 2026)

You can configure one, none, or all providers. Related assignments will simply error out on missing credentials.

## Create `.env` file

We assume that you have already read the guidance above and signed up with the relevant provider, and obtained the required authentication credentials (API_KEY or token). In the case of Azure OpenAI, we assume you also have a valid deployment of an Azure OpenAI Service (endpoint) with at least one GPT model deployed for chat completion.

The next step is to configure your **local environment variables** as follows:

1. Look in the root folder for a `.env.copy` file that should have contents like this:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI in Microsoft Foundry
   ## (Azure OpenAI Service is now part of Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Default is set! (current stable GA API version)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry Models (multi-provider model catalog, replaces GitHub Models, which retires end of July 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Copy that file to `.env` using the command below. This file is _gitignore-d_, keeping secrets safe.

   ```bash
   cp .env.copy .env
   ```

3. Fill in the values (replace placeholders on right side of `=`) as described in the next section.

4. (Option) If you use GitHub Codespaces, you have the option to save environment variables as _Codespaces secrets_ associated with this repository. In that case, you won't need to setup a local .env file. **However, note that this option works only if you use GitHub Codespaces.** You will still need to setup the .env file if you use Docker Desktop instead.

## Populate `.env` file

Let's take a quick look at the variable names to understand what they represent:

| Variable  | Description  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | This is the user access token you setup in your profile |
| OPENAI_API_KEY | This is the authorization key for using the service for non-Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | This is the authorization key for using that service |
| AZURE_OPENAI_ENDPOINT | This is the deployed endpoint for an Azure OpenAI resource |
| AZURE_OPENAI_DEPLOYMENT | This is the _text generation_ model deployment endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | This is the _text embeddings_ model deployment endpoint |
| AZURE_INFERENCE_ENDPOINT | This is the endpoint for your Microsoft Foundry project, used for Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | This is the API key for your Microsoft Foundry project |
| | |

Note: The last two Azure OpenAI variables reflect a default model for chat completion (text generation) and vector search (embeddings) respectively. Instructions for setting them will be defined in relevant assignments.

## Configure Azure OpenAI: From Portal

> **Note:** Azure OpenAI Service is now part of [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Resources and deployments still show up in the Azure Portal, but day-to-day model management (deployments, playground, monitoring) now happens in the Foundry portal instead of the old standalone "Azure OpenAI Studio".

The Azure OpenAI endpoint and key values will be found in the [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) so let's start there.

1. Go to the [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Click the **Keys and Endpoint** option in the sidebar (menu at left).
1. Click **Show Keys** - you should see the following: KEY 1, KEY 2 and Endpoint.
1. Use the KEY 1 value for AZURE_OPENAI_API_KEY
1. Use the Endpoint value for AZURE_OPENAI_ENDPOINT

Next, we need the endpoints for the specific models we've deployed.

1. Click the **Model deployments** option in the sidebar (left menu) for Azure OpenAI resource.
1. In the destination page, click **Go to Microsoft Foundry portal** (or **Manage Deployments**, depending on your resource type)

This will take you to the Microsoft Foundry portal, where we'll find the other values as described below.

## Configure Azure OpenAI: From Microsoft Foundry portal

1. Navigate to the [Microsoft Foundry portal](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **from your resource** as described above.
1. Click the **Deployments** tab (sidebar, left) to view currently deployed models.
1. If your desired model is not deployed, use **Deploy model** to deploy it from the [model catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. You will need a _text-generation_ model - we recommend: **gpt-5-mini**
1. You will need a _text-embedding_ model - we recommend **text-embedding-3-small**

Now update the environment variables to reflect the _Deployment name_ used. This will typically be the same as the model name unless you changed it explicitly. So, as an example, you might have:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Don't forget to save the .env file when done**. You can now exit the file and return to the instructions for running the notebook.

## Configure OpenAI: From Profile

Your OpenAI API key can be found in your [OpenAI account](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). If you don't have one, you can sign up for an account and create an API key. Once you have the key, you can use it to populate the `OPENAI_API_KEY` variable in the `.env` file.

## Configure Hugging Face: From Profile

Your Hugging Face token can be found in your profile under [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Don't post or share these publicly. Instead, create a new token for this project usage and copy that into the `.env` file under the `HUGGING_FACE_API_KEY` variable. _Note:_ This is technically not an API key but is used for authentication so we are keeping that naming convention for consistency.

## Configure Microsoft Foundry Models: From Portal

> **Note:** GitHub Models is retiring at the end of July 2026. Microsoft Foundry Models is the direct replacement, offering the same free-to-try model catalog and Azure AI Inference SDK / OpenAI SDK experience.

1. Go to [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) and create (or open) a Foundry project.
1. Browse the [model catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) and deploy a model, for example `gpt-5-mini`.
1. On the project's **Overview** page, copy the **endpoint** and **API key**.
1. Use the endpoint value for `AZURE_INFERENCE_ENDPOINT` and the key value for `AZURE_INFERENCE_CREDENTIAL` in your `.env` file.

## Offline / Local Providers

If you'd rather not use a cloud subscription at all, you can run compatible open models directly on your own device:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoft's on-device runtime. It automatically selects the best execution provider (NPU, GPU, or CPU) and exposes an OpenAI-compatible endpoint, so you can reuse most of the sample code in this course with minimal changes. See the [Foundry Local documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) to get started, or install with `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - a popular alternative for running open models like Llama, Phi, Mistral, and Gemma locally.

See [Lesson 19: Building with SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) for hands-on examples using both options.
