<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:20:16+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "en"
}
-->
# Setup Your Dev Environment

We set up this repository and course with a [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) that includes a universal runtime supporting Python3, .NET, Node.js, and Java development. The related configuration is defined in the `devcontainer.json` file located in the `.devcontainer/` folder at the root of this repository.

To activate the dev container, launch it in [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (for a cloud-hosted runtime) or in [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (for a local device-hosted runtime). Read [this documentation](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) for more details on how dev containers work within VS Code.

> [!TIP]  
> We recommend using GitHub Codespaces for a quick start with minimal effort. It offers a generous [free usage quota](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) for personal accounts. Configure [timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) to stop or delete inactive codespaces to make the most of your quota.

## 1. Executing Assignments

Each lesson may include _optional_ assignments available in one or more programming languages such as Python, .NET/C#, Java, and JavaScript/TypeScript. This section provides general guidance on how to run those assignments.

### 1.1 Python Assignments

Python assignments are provided either as applications (`.py` files) or Jupyter notebooks (`.ipynb` files).  
- To run a notebook, open it in Visual Studio Code, then click _Select Kernel_ (top right) and choose the default Python 3 option. You can then _Run All_ to execute the notebook.  
- To run Python applications from the command line, follow the assignment-specific instructions to select the correct files and provide any required arguments.

## 2. Configuring Providers

Assignments **may** also be set up to work with one or more Large Language Model (LLM) deployments through supported service providers like OpenAI, Azure, or Hugging Face. These offer a _hosted endpoint_ (API) that can be accessed programmatically with the appropriate credentials (API key or token). In this course, we cover these providers:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) with a variety of models including the core GPT series.  
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) for OpenAI models with enterprise-grade features.  
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) for open-source models and inference servers.

**You will need to use your own accounts for these exercises**. Assignments are optional, so you can choose to set up one, all, or none of the providers depending on your interests. Here is some signup guidance:

| Signup | Cost | API Key | Playground | Comments |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [Pricing](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [Project-based](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Multiple Models Available |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [Pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Must Apply Ahead For Access](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Pricing](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Hugging Chat has limited models](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Follow the instructions below to _configure_ this repository for use with different providers. Assignments that require a specific provider will include one of these tags in their filename:  
- `aoai` - requires Azure OpenAI endpoint and key  
- `oai` - requires OpenAI endpoint and key  
- `hf` - requires Hugging Face token  

You can configure one, none, or all providers. Assignments will simply fail if the required credentials are missing.

### 2.1. Create `.env` file

We assume you have already read the guidance above, signed up with the relevant provider, and obtained the necessary authentication credentials (API_KEY or token). For Azure OpenAI, we also assume you have a valid deployment of an Azure OpenAI Service (endpoint) with at least one GPT model deployed for chat completion.

The next step is to configure your **local environment variables** as follows:

1. Look in the root folder for a `.env.copy` file that should contain something like this:

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

2. Copy that file to `.env` using the command below. This file is _gitignored_, keeping your secrets safe.

   ```bash
   cp .env.copy .env
   ```

3. Fill in the values (replace placeholders on the right side of `=`) as described in the next section.

3. (Optional) If you use GitHub Codespaces, you can save environment variables as _Codespaces secrets_ linked to this repository. In that case, you won’t need to set up a local `.env` file. **However, note that this option only works if you use GitHub Codespaces.** You will still need to set up the `.env` file if you use Docker Desktop instead.

### 2.2. Populate `.env` file

Here’s a quick overview of the variable names and what they represent:

| Variable  | Description  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | This is the user access token you set up in your profile |
| OPENAI_API_KEY | This is the authorization key for using the service with non-Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | This is the authorization key for using the Azure OpenAI service |
| AZURE_OPENAI_ENDPOINT | This is the deployed endpoint for an Azure OpenAI resource |
| AZURE_OPENAI_DEPLOYMENT | This is the _text generation_ model deployment endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | This is the _text embeddings_ model deployment endpoint |
| | |

Note: The last two Azure OpenAI variables correspond to default models for chat completion (text generation) and vector search (embeddings), respectively. Instructions for setting these will be provided in relevant assignments.

### 2.3 Configure Azure: From Portal

You can find the Azure OpenAI endpoint and key values in the [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst). Let’s start there.

1. Go to the [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
2. Click the **Keys and Endpoint** option in the sidebar (left menu).  
3. Click **Show Keys** — you should see KEY 1, KEY 2, and Endpoint.  
4. Use the KEY 1 value for `AZURE_OPENAI_API_KEY`  
5. Use the Endpoint value for `AZURE_OPENAI_ENDPOINT`

Next, we need the endpoints for the specific models you’ve deployed.

1. Click the **Model deployments** option in the sidebar (left menu) for your Azure OpenAI resource.  
2. On the destination page, click **Manage Deployments**

This will take you to the Azure OpenAI Studio website, where you’ll find the other values as described below.

### 2.4 Configure Azure: From Studio

1. Navigate to [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **from your resource** as described above.  
2. Click the **Deployments** tab (sidebar, left) to view currently deployed models.  
3. If your desired model isn’t deployed, use **Create new deployment** to deploy it.  
4. You will need a _text-generation_ model — we recommend: **gpt-35-turbo**  
5. You will need a _text-embedding_ model — we recommend **text-embedding-ada-002**

Now update the environment variables to reflect the _Deployment name_ used. This will usually be the same as the model name unless you changed it explicitly. For example, you might have:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Don’t forget to save the `.env` file when you’re done**. You can then close the file and return to the instructions for running the notebook.

### 2.5 Configure OpenAI: From Profile

Your OpenAI API key can be found in your [OpenAI account](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). If you don’t have one, you can sign up and create an API key. Once you have the key, use it to populate the `OPENAI_API_KEY` variable in the `.env` file.

### 2.6 Configure Hugging Face: From Profile

Your Hugging Face token can be found in your profile under [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Don’t share these publicly. Instead, create a new token specifically for this project and copy it into the `.env` file under the `HUGGING_FACE_API_KEY` variable. _Note:_ This isn’t technically an API key but is used for authentication, so we keep the naming consistent.

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.