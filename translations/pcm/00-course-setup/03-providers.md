<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b5b016b0eb8a1cef2e3097620d8aa23",
  "translation_date": "2025-12-19T18:14:39+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "pcm"
}
-->
# Choosing & Configuring an LLM Provider 🔑

Assignments **fit** also dey setup to work against one or more Large Language Model (LLM) deployments through one supported service provider like OpenAI, Azure or Hugging Face. Dem dey provide _hosted endpoint_ (API) wey we fit access programmatically with the correct credentials (API key or token). For this course, we go talk about these providers:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) wey get different models including the main GPT series.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) for OpenAI models wey focus on enterprise readiness
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) for open-source models and inference server

**You go need use your own accounts for these exercises**. Assignments no mandatory so you fit choose to setup one, all - or none - of the providers based on wetin you like. Some guidance for signup:

| Signup | Cost | API Key | Playground | Comments |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Pricing](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Project-based](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Plenty Models Dey Available |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [You Must Apply Before To Get Access](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Pricing](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat get limited models](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Follow the directions below to _configure_ this repository to work with different providers. Assignments wey need one specific provider go get one of these tags for their filename:

- `aoai` - need Azure OpenAI endpoint, key
- `oai` - need OpenAI endpoint, key
- `hf` - need Hugging Face token

You fit configure one, none, or all providers. Related assignments go just error if credentials no dey.

## Create `.env` file

We assume say you don already read the guidance above and sign up with the correct provider, and you don get the required authentication credentials (API_KEY or token). For Azure OpenAI case, we assume say you get valid deployment of Azure OpenAI Service (endpoint) with at least one GPT model deployed for chat completion.

The next step na to configure your **local environment variables** like this:

1. Look for `.env.copy` file for the root folder wey get contents like this:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default don set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Copy that file to `.env` with the command below. This file dey _gitignore-d_, to keep secrets safe.

   ```bash
   cp .env.copy .env
   ```

3. Fill the values (change placeholders for right side of `=`) as we go explain for the next section.

4. (Option) If you dey use GitHub Codespaces, you fit save environment variables as _Codespaces secrets_ wey relate to this repository. If na so, you no go need setup local .env file. **But, note say this option only work if you dey use GitHub Codespaces.** You still go need setup the .env file if you dey use Docker Desktop.

## Populate `.env` file

Make we quickly check the variable names to sabi wetin dem mean:

| Variable  | Description  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Na the user access token wey you setup for your profile |
| OPENAI_API_KEY | Na the authorization key to use the service for non-Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Na the authorization key to use that service |
| AZURE_OPENAI_ENDPOINT | Na the deployed endpoint for Azure OpenAI resource |
| AZURE_OPENAI_DEPLOYMENT | Na the _text generation_ model deployment endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Na the _text embeddings_ model deployment endpoint |
| | |

Note: The last two Azure OpenAI variables dey represent default model for chat completion (text generation) and vector search (embeddings) respectively. Instructions to set dem go dey for relevant assignments.

## Configure Azure: From Portal

The Azure OpenAI endpoint and key values go dey for the [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) so make we start there.

1. Go to the [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Click the **Keys and Endpoint** option for the sidebar (menu for left).
1. Click **Show Keys** - you go see: KEY 1, KEY 2 and Endpoint.
1. Use the KEY 1 value for AZURE_OPENAI_API_KEY
1. Use the Endpoint value for AZURE_OPENAI_ENDPOINT

Next, we need the endpoints for the specific models we don deploy.

1. Click the **Model deployments** option for the sidebar (left menu) for Azure OpenAI resource.
1. For the destination page, click **Manage Deployments**

This one go carry you go Azure OpenAI Studio website, where we go find the other values as we talk below.

## Configure Azure: From Studio

1. Go [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **from your resource** as we talk before.
1. Click the **Deployments** tab (sidebar, left) to see models wey dey deployed now.
1. If your model no dey deployed, use **Create new deployment** to deploy am.
1. You go need _text-generation_ model - we recommend: **gpt-35-turbo**
1. You go need _text-embedding_ model - we recommend **text-embedding-ada-002**

Now update the environment variables to show the _Deployment name_ wey you use. Normally e go be the same as the model name unless you change am yourself. So, example, you fit get:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**No forget to save the .env file when you finish**. You fit now close the file and continue with the instructions to run the notebook.

## Configure OpenAI: From Profile

Your OpenAI API key fit dey your [OpenAI account](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). If you never get, you fit sign up for account and create API key. Once you get the key, you fit use am to fill the `OPENAI_API_KEY` variable for the `.env` file.

## Configure Hugging Face: From Profile

Your Hugging Face token fit dey your profile under [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). No post or share am publicly. Instead, create new token for this project use and copy am enter the `.env` file under the `HUGGING_FACE_API_KEY` variable. _Note:_ This one no be API key technically but na authentication token so we dey use that naming for consistency.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg sabi say automated translation fit get some mistakes or no too correct. Di original document wey e dey for im own language na di correct one. If na serious matter, e better make human professional translate am. We no go responsible for any misunderstanding or wrong meaning wey fit come from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->