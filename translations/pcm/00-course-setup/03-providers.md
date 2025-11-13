<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-11-12T09:03:15+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "pcm"
}
-->
# How to Choose & Set Up LLM Provider 🔑

You fit set up assignments make dem work with one or more Large Language Model (LLM) deployments wey dey through service providers like OpenAI, Azure or Hugging Face. Dis providers dey give hosted endpoint (API) wey we fit use programmatically if we get correct credentials (API key or token). For dis course, we go talk about dis providers:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) wey get plenty models including di main GPT series.
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) wey dey focus on enterprise readiness for OpenAI models.
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) wey dey offer open-source models and inference server.

**You go need use your own accounts for dis exercises**. Assignments na optional, so you fit choose to set up one, all, or even none of di providers based on wetin you like. Some tips for signup:

| Signup | Cost | API Key | Playground | Comments |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Pricing](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Project-based](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Plenty Models dey available |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [You go need apply first for access](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Pricing](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat get limited models](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Follow di instructions below to configure dis repository make e work with di different providers. Assignments wey need specific provider go get one of dis tags for dia filename:

- `aoai` - need Azure OpenAI endpoint, key
- `oai` - need OpenAI endpoint, key
- `hf` - need Hugging Face token

You fit configure one, none, or all di providers. Assignments wey need di provider go just show error if credentials no dey.

## Create `.env` file

We dey assume say you don already read di tips wey dey above, signup with di provider wey you need, and collect di authentication credentials (API_KEY or token). For Azure OpenAI, we dey assume say you don also deploy valid Azure OpenAI Service (endpoint) wey get at least one GPT model wey dey for chat completion.

Di next step na to configure your **local environment variables** like dis:

1. Check di root folder for `.env.copy` file wey suppose get content like dis:

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

2. Copy di file go `.env` using di command wey dey below. Dis file dey _gitignore-d_, so e go keep secrets safe.

   ```bash
   cp .env.copy .env
   ```

3. Put di values (replace placeholders wey dey di right side of `=`) as we go explain for di next section.

4. (Optional) If you dey use GitHub Codespaces, you fit save environment variables as _Codespaces secrets_ wey dey linked to dis repository. If you do dis, you no go need setup local .env file. **But note say dis option na only for GitHub Codespaces.** You go still need setup di .env file if you dey use Docker Desktop.

## Populate `.env` file

Make we look di variable names small make we understand wetin dem mean:

| Variable  | Description  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Dis na di user access token wey you setup for your profile |
| OPENAI_API_KEY | Dis na di authorization key wey you go use for di service wey no be Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Dis na di authorization key wey you go use for dat service |
| AZURE_OPENAI_ENDPOINT | Dis na di deployed endpoint for Azure OpenAI resource |
| AZURE_OPENAI_DEPLOYMENT | Dis na di _text generation_ model deployment endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Dis na di _text embeddings_ model deployment endpoint |
| | |

Note: Di last two Azure OpenAI variables dey represent default model for chat completion (text generation) and vector search (embeddings). Instructions for how to set dem go dey inside di assignments wey need dem.

## Configure Azure: From Portal

Di Azure OpenAI endpoint and key values dey for [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), so make we start from dia.

1. Go [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Click **Keys and Endpoint** option wey dey di sidebar (menu for left).
1. Click **Show Keys** - you go see KEY 1, KEY 2 and Endpoint.
1. Use di KEY 1 value for AZURE_OPENAI_API_KEY
1. Use di Endpoint value for AZURE_OPENAI_ENDPOINT

Next, we go find di endpoints for di specific models wey we don deploy.

1. Click **Model deployments** option wey dey di sidebar (left menu) for Azure OpenAI resource.
1. For di page wey you go land, click **Manage Deployments**

Dis go carry you go Azure OpenAI Studio website, where we go find di other values as we go explain below.

## Configure Azure: From Studio

1. Go [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **from your resource** as we don talk above.
1. Click **Deployments** tab (sidebar, left) to see di models wey don deploy.
1. If di model wey you want no dey deploy, use **Create new deployment** to deploy am.
1. You go need _text-generation_ model - we dey recommend: **gpt-35-turbo**
1. You go need _text-embedding_ model - we dey recommend **text-embedding-ada-002**

Now update di environment variables to show di _Deployment name_ wey you use. Normally, dis go be di same as di model name unless you change am. Example:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**No forget to save di .env file when you finish**. You fit now close di file and go back to di instructions for how to run di notebook.

## Configure OpenAI: From Profile

Your OpenAI API key dey for your [OpenAI account](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). If you no get one, you fit signup for account and create API key. Once you get di key, use am to fill di `OPENAI_API_KEY` variable for di `.env` file.

## Configure Hugging Face: From Profile

Your Hugging Face token dey for your profile under [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). No post or share dis publicly. Instead, create new token for dis project use and copy am enter di `.env` file under di `HUGGING_FACE_API_KEY` variable. _Note:_ Dis no really be API key but e dey used for authentication, so we dey keep di naming style for consistency.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am correct, abeg sabi say machine translation fit get mistake or no dey accurate well. Di original dokyument for im native language na di main source wey you go trust. For important information, e better make professional human translator check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->