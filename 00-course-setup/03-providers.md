# Choosing & Configuring an LLM Provider 🔑

Assignments **may** also be setup to work against one or more Large Language Model (LLM) deployments through a supported service provider like OpenAI, Azure or Hugging Face. These provide a _hosted endpoint_ (API) that we can access programmatically with the right credentials (API key or token). In this course, we discuss these providers:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) with diverse models including the core GPT series.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) for OpenAI models with enterprise readiness in focus
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) for open-source models and inference server

**You will need to use your own accounts for these exercises**. Assignments are optional so you can choose to setup one, all - or none - of the providers based on your interests. Some guidance for signup:

| Signup | Cost | API Key | Playground | Comments |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Pricing](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Project-based](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Multiple Models Available |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Must Apply Ahead For Access](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Pricing](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat has limited models](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Follow the directions below to _configure_ this repository for use with different providers. Assignments that require a specific provider will contain one of these tags in their filename:

- `aoai` - requires Azure OpenAI endpoint, key
- `oai` - requires OpenAI endpoint, key
- `hf` - requires Hugging Face token

You can configure one, none, or all providers. Related assignments will simply error out on missing credentials.

## Create `.env` file

We assume that you have already read the guidance above and signed up with the relevant provider, and obtained the required authentication credentials (API_KEY or token). In the case of Azure OpenAI, we assume you also have a valid deployment of an Azure OpenAI Service (endpoint) with at least one GPT model deployed for chat completion.

The next step is to configure your **local environment variables** as follows:

1. Look in the root folder for a `.env.copy` file that should have contents like this:

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
| | |

Note: The last two Azure OpenAI variables reflect a default model for chat completion (text generation) and vector search (embeddings) respectively. Instructions for setting them will be defined in relevant assignments.

## Configure Azure: From Portal

The Azure OpenAI endpoint and key values will be found in the [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) so let's start there.

1. Go to the [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Click the **Keys and Endpoint** option in the sidebar (menu at left).
1. Click **Show Keys** - you should see the following: KEY 1, KEY 2 and Endpoint.
1. Use the KEY 1 value for AZURE_OPENAI_API_KEY
1. Use the Endpoint value for AZURE_OPENAI_ENDPOINT

Next, we need the endpoints for the specific models we've deployed.

1. Click the **Model deployments** option in the sidebar (left menu) for Azure OpenAI resource.
1. In the destination page, click **Manage Deployments**

This will take you to the Azure OpenAI Studio website, where we'll find the other values as described below.

## Configure Azure: From Studio

1. Navigate to [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **from your resource** as described above.
1. Click the **Deployments** tab (sidebar, left) to view currently deployed models.
1. If your desired model is not deployed, use **Create new deployment** to deploy it.
1. You will need a _text-generation_ model - we recommend: **gpt-35-turbo**
1. You will need a _text-embedding_ model - we recommend **text-embedding-ada-002**

Now update the environment variables to reflect the _Deployment name_ used. This will typically be the same as the model name unless you changed it explcitly. So, as an example, you might have:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Don't forget to save the .env file when done**. You can now exit the file and return to the instructions for running the notebook.

## Configure OpenAI: From Profile

Your OpenAI API key can be found in your [OpenAI account](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). If you don't have one, you can sign up for an account and create an API key. Once you have the key, you can use it to populate the `OPENAI_API_KEY` variable in the `.env` file.

## Configure Hugging Face: From Profile

Your Hugging Face token can be found in your profile under [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Don't post or share these publicly. Instead, create a new token for this project usage and copy that into the `.env` file under the `HUGGING_FACE_API_KEY` variable. _Note:_ This is technically not an API key but is used for authentication so we are keeping that naming convention for consistency.
