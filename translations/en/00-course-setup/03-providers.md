<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T13:17:01+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "en"
}
-->
# Choosing & Configuring an LLM Provider 🔑

Assignments **may** also be set up to work with one or more Large Language Model (LLM) deployments through a supported service provider like OpenAI, Azure, or Hugging Face. These providers offer a _hosted endpoint_ (API) that you can access programmatically with the right credentials (API key or token). In this course, we’ll cover these providers:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) offers a variety of models, including the core GPT series.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) provides OpenAI models with a focus on enterprise features.
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) offers open-source models and an inference server.

**You’ll need to use your own accounts for these exercises.** Assignments are optional, so you can choose to set up one, all, or none of the providers depending on your interests. Here’s some guidance for signing up:

| Signup | Cost | API Key | Playground | Comments |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Pricing](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Project-based](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Multiple Models Available |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Must Apply Ahead For Access](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Pricing](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat has limited models](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Follow the steps below to _configure_ this repository for use with different providers. Assignments that need a specific provider will have one of these tags in their filename:

- `aoai` - needs Azure OpenAI endpoint and key
- `oai` - needs OpenAI endpoint and key
- `hf` - needs Hugging Face token

You can set up one, none, or all providers. Assignments that depend on a provider will simply show an error if credentials are missing.

## Create `.env` file

We’re assuming you’ve already read the instructions above, signed up with the relevant provider, and obtained the required authentication credentials (API_KEY or token). For Azure OpenAI, you should also have a valid deployment of an Azure OpenAI Service (endpoint) with at least one GPT model deployed for chat completion.

The next step is to set up your **local environment variables** as follows:

1. In the root folder, look for a `.env.copy` file. It should look something like this:

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

2. Copy that file to `.env` using the command below. This file is _gitignore-d_, so your secrets are safe.

   ```bash
   cp .env.copy .env
   ```

3. Fill in the values (replace the placeholders on the right side of `=`) as described in the next section.

4. (Optional) If you use GitHub Codespaces, you can save environment variables as _Codespaces secrets_ for this repository. In that case, you won’t need to set up a local .env file. **However, this only works if you’re using GitHub Codespaces.** If you’re using Docker Desktop, you’ll still need to set up the .env file.

## Populate `.env` file

Let’s quickly review the variable names and what they mean:

| Variable  | Description  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | This is the user access token you set up in your profile |
| OPENAI_API_KEY | This is the authorization key for using the service with non-Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | This is the authorization key for using that service |
| AZURE_OPENAI_ENDPOINT | This is the deployed endpoint for an Azure OpenAI resource |
| AZURE_OPENAI_DEPLOYMENT | This is the _text generation_ model deployment endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | This is the _text embeddings_ model deployment endpoint |
| | |

Note: The last two Azure OpenAI variables refer to the default model for chat completion (text generation) and vector search (embeddings), respectively. Instructions for setting these will be provided in the relevant assignments.

## Configure Azure: From Portal

You’ll find the Azure OpenAI endpoint and key values in the [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), so let’s start there.

1. Go to the [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Click the **Keys and Endpoint** option in the sidebar (menu on the left).
1. Click **Show Keys** – you should see: KEY 1, KEY 2, and Endpoint.
1. Use the KEY 1 value for AZURE_OPENAI_API_KEY
1. Use the Endpoint value for AZURE_OPENAI_ENDPOINT

Next, you’ll need the endpoints for the specific models you’ve deployed.

1. Click the **Model deployments** option in the sidebar (left menu) for your Azure OpenAI resource.
1. On the destination page, click **Manage Deployments**

This will take you to the Azure OpenAI Studio website, where you’ll find the other values as described below.

## Configure Azure: From Studio

1. Go to [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **from your resource** as described above.
1. Click the **Deployments** tab (sidebar, left) to see the models you’ve deployed.
1. If your desired model isn’t deployed, use **Create new deployment** to deploy it.
1. You’ll need a _text-generation_ model – we recommend: **gpt-35-turbo**
1. You’ll need a _text-embedding_ model – we recommend **text-embedding-ada-002**

Now update the environment variables to match the _Deployment name_ you used. This is usually the same as the model name unless you changed it. For example, you might have:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Don’t forget to save the .env file when you’re done.** You can now close the file and return to the instructions for running the notebook.

## Configure OpenAI: From Profile

Your OpenAI API key is available in your [OpenAI account](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). If you don’t have one, sign up for an account and create an API key. Once you have the key, use it to fill in the `OPENAI_API_KEY` variable in the `.env` file.

## Configure Hugging Face: From Profile

Your Hugging Face token is in your profile under [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Don’t post or share these publicly. Instead, create a new token for this project and copy it into the `.env` file under the `HUGGING_FACE_API_KEY` variable. _Note:_ This isn’t technically an API key, but it’s used for authentication, so we’re keeping the naming consistent.

---

**Disclaimer**:
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.