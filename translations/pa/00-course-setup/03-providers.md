<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T16:01:33+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "pa"
}
-->
# LLM ਪ੍ਰਦਾਤਾ ਚੁਣਨਾ ਅਤੇ ਸੰਰਚਨਾ ਕਰਨਾ 🔑

ਅਸਾਈਨਮੈਂਟਾਂ **ਸ਼ਾਇਦ** ਇੱਕ ਜਾਂ ਵੱਧ ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲ (LLM) ਡਿਪਲੋਇਮੈਂਟਾਂ ਉੱਤੇ ਕੰਮ ਕਰਨ ਲਈ ਸਹਾਇਕ ਸਰਵਿਸ ਪ੍ਰਦਾਤਾ ਜਿਵੇਂ ਕਿ OpenAI, Azure ਜਾਂ Hugging Face ਰਾਹੀਂ ਸੈੱਟਅੱਪ ਕੀਤੀਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ। ਇਹ ਸਾਨੂੰ ਇੱਕ _ਹੋਸਟ ਕੀਤਾ ਐਂਡਪੌਇੰਟ_ (API) ਦਿੰਦੇ ਹਨ, ਜਿਸਨੂੰ ਅਸੀਂ ਠੀਕ ਪਛਾਣ ਪੱਤਰ (API ਕੁੰਜੀ ਜਾਂ ਟੋਕਨ) ਨਾਲ ਪ੍ਰੋਗਰਾਮਿੰਗ ਰਾਹੀਂ ਐਕਸੈੱਸ ਕਰ ਸਕਦੇ ਹਾਂ। ਇਸ ਕੋਰਸ ਵਿੱਚ, ਅਸੀਂ ਇਹ ਪ੍ਰਦਾਤਾ ਚਰਚਾ ਕਰਦੇ ਹਾਂ:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) ਜਿਸ ਵਿੱਚ ਮੁੱਖ GPT ਸੀਰੀਜ਼ ਸਮੇਤ ਕਈ ਮਾਡਲ ਹਨ।
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) ਜੋ OpenAI ਮਾਡਲਾਂ ਨੂੰ ਇੰਟਰਪ੍ਰਾਈਜ਼ ਲਈ ਤਿਆਰ ਕਰਦਾ ਹੈ
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) ਜੋ ਖੁੱਲ੍ਹੇ ਸਰੋਤ ਮਾਡਲਾਂ ਅਤੇ ਇੰਫਰੈਂਸ ਸਰਵਰ ਲਈ ਹੈ

**ਤੁਹਾਨੂੰ ਇਹ ਅਭਿਆਸ ਕਰਨ ਲਈ ਆਪਣੇ ਖਾਤਿਆਂ ਦੀ ਲੋੜ ਹੋਵੇਗੀ**। ਅਸਾਈਨਮੈਂਟਾਂ ਚੋਣਵਾਂ ਹਨ, ਇਸ ਲਈ ਤੁਸੀਂ ਆਪਣੇ ਰੁਚੀ ਅਨੁਸਾਰ ਇੱਕ, ਸਾਰੇ ਜਾਂ ਕੋਈ ਵੀ ਪ੍ਰਦਾਤਾ ਸੈੱਟਅੱਪ ਕਰ ਸਕਦੇ ਹੋ। ਸਾਈਨਅੱਪ ਲਈ ਕੁਝ ਹਦਾਇਤਾਂ:

| ਸਾਈਨਅੱਪ | ਲਾਗਤ | API ਕੁੰਜੀ | ਪਲੇਅਗਰਾਊਂਡ | ਟਿੱਪਣੀਆਂ |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [ਕੀਮਤ](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [ਪਰੋਜੈਕਟ ਅਧਾਰਤ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [ਬਿਨਾ ਕੋਡ, ਵੈੱਬ](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | ਕਈ ਮਾਡਲ ਉਪਲਬਧ ਹਨ |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [ਕੀਮਤ](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK ਕਵਿਕਸਟਾਰਟ](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [ਸਟੂਡੀਓ ਕਵਿਕਸਟਾਰਟ](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [ਐਕਸੈੱਸ ਲਈ ਪਹਿਲਾਂ ਅਰਜ਼ੀ ਦੇਣੀ ਪੈਂਦੀ ਹੈ](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [ਕੀਮਤ](https://huggingface.co/pricing) | [ਐਕਸੈੱਸ ਟੋਕਨ](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ਵਿੱਚ ਮਾਡਲ ਸੀਮਤ ਹਨ](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਹਦਾਇਤਾਂ ਦੀ ਪਾਲਣਾ ਕਰਕੇ ਇਹ ਰਿਪੋਜ਼ਟਰੀ ਵੱਖ-ਵੱਖ ਪ੍ਰਦਾਤਾਵਾਂ ਨਾਲ ਵਰਤਣ ਲਈ _ਸੰਰਚਿਤ_ ਕਰੋ। ਜਿਹੜੀਆਂ ਅਸਾਈਨਮੈਂਟਾਂ ਨੂੰ ਕਿਸੇ ਖਾਸ ਪ੍ਰਦਾਤਾ ਦੀ ਲੋੜ ਹੋਵੇਗੀ, ਉਹਨਾਂ ਦੇ ਫਾਈਲ ਨਾਂ ਵਿੱਚ ਇਹ ਟੈਗ ਹੋਵੇਗਾ:

- `aoai` - Azure OpenAI ਐਂਡਪੌਇੰਟ, ਕੁੰਜੀ ਦੀ ਲੋੜ
- `oai` - OpenAI ਐਂਡਪੌਇੰਟ, ਕੁੰਜੀ ਦੀ ਲੋੜ
- `hf` - Hugging Face ਟੋਕਨ ਦੀ ਲੋੜ

ਤੁਸੀਂ ਇੱਕ, ਕੋਈ ਵੀ ਨਹੀਂ ਜਾਂ ਸਾਰੇ ਪ੍ਰਦਾਤਾ ਸੰਰਚਿਤ ਕਰ ਸਕਦੇ ਹੋ। ਸੰਬੰਧਤ ਅਸਾਈਨਮੈਂਟਾਂ ਵਿੱਚ ਜੇ ਪਛਾਣ ਪੱਤਰ ਨਾ ਹੋਣ ਤਾਂ ਗਲਤੀ ਆ ਜਾਵੇਗੀ।

## `.env` ਫਾਈਲ ਬਣਾਓ

ਅਸੀਂ ਮੰਨਦੇ ਹਾਂ ਕਿ ਤੁਸੀਂ ਉਪਰੋਕਤ ਹਦਾਇਤਾਂ ਪੜ੍ਹ ਲੀਆਂ ਹਨ, ਸੰਬੰਧਤ ਪ੍ਰਦਾਤਾ ਨਾਲ ਸਾਈਨਅੱਪ ਕਰ ਲਿਆ ਹੈ, ਅਤੇ ਲੋੜੀਂਦੇ ਪਛਾਣ ਪੱਤਰ (API_KEY ਜਾਂ ਟੋਕਨ) ਪ੍ਰਾਪਤ ਕਰ ਲਏ ਹਨ। Azure OpenAI ਦੇ ਮਾਮਲੇ ਵਿੱਚ, ਅਸੀਂ ਮੰਨਦੇ ਹਾਂ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਘੱਟੋ-ਘੱਟ ਇੱਕ GPT ਮਾਡਲ ਨਾਲ ਡਿਪਲੋਇਡ Azure OpenAI ਸਰਵਿਸ (ਐਂਡਪੌਇੰਟ) ਵੀ ਹੈ।

ਅਗਲਾ ਕਦਮ ਤੁਹਾਡੇ **ਲੋਕਲ ਇਨਵਾਇਰਨਮੈਂਟ ਵੈਰੀਏਬਲ** ਹੇਠਾਂ ਦਿੱਤੇ ਤਰੀਕੇ ਨਾਲ ਸੰਰਚਿਤ ਕਰਨਾ ਹੈ:

1. ਰੂਟ ਫੋਲਡਰ ਵਿੱਚ `.env.copy` ਫਾਈਲ ਵੇਖੋ, ਜਿਸ ਵਿੱਚ ਕੁਝ ਇਸ ਤਰ੍ਹਾਂ ਦਾ ਸਮੱਗਰੀ ਹੋਵੇਗਾ:

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

2. ਇਸ ਫਾਈਲ ਨੂੰ ਹੇਠਾਂ ਦਿੱਤੇ ਹੁਕਮ ਨਾਲ `.env` ਵਿੱਚ ਕਾਪੀ ਕਰੋ। ਇਹ ਫਾਈਲ _gitignore_ ਕੀਤੀ ਹੋਈ ਹੈ, ਜਿਸ ਨਾਲ ਰਾਜ਼ ਸੁਰੱਖਿਅਤ ਰਹਿੰਦੇ ਹਨ।

   ```bash
   cp .env.copy .env
   ```

3. ਅਗਲੇ ਭਾਗ ਵਿੱਚ ਦਿੱਤੇ ਵੇਰਵੇ ਅਨੁਸਾਰ ਮੁੱਲ ਭਰੋ (ਸੱਜੇ ਪਾਸੇ ਦੇ ਪਲੇਸਹੋਲਡਰ ਨੂੰ ਬਦਲੋ)।

4. (ਚੋਣਵਾਂ) ਜੇ ਤੁਸੀਂ GitHub Codespaces ਵਰਤਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਇਨਵਾਇਰਨਮੈਂਟ ਵੈਰੀਏਬਲਾਂ ਨੂੰ _Codespaces secrets_ ਵਜੋਂ ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਨਾਲ ਸੰਭਾਲ ਸਕਦੇ ਹੋ। ਇਸ ਮਾਮਲੇ ਵਿੱਚ, ਤੁਹਾਨੂੰ ਲੋਕਲ .env ਫਾਈਲ ਬਣਾਉਣ ਦੀ ਲੋੜ ਨਹੀਂ। **ਪਰ, ਧਿਆਨ ਦਿਓ ਕਿ ਇਹ ਵਿਕਲਪ ਸਿਰਫ GitHub Codespaces ਲਈ ਹੀ ਕੰਮ ਕਰਦਾ ਹੈ।** ਜੇ ਤੁਸੀਂ Docker Desktop ਵਰਤਦੇ ਹੋ ਤਾਂ ਵੀ .env ਫਾਈਲ ਬਣਾਉਣੀ ਪਵੇਗੀ।

## `.env` ਫਾਈਲ ਭਰੋ

ਆਓ ਵੈਰੀਏਬਲ ਨਾਂ ਵੇਖੀਏ ਕਿ ਉਹ ਕੀ ਦਰਸਾਉਂਦੇ ਹਨ:

| ਵੈਰੀਏਬਲ  | ਵੇਰਵਾ  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | ਇਹ ਤੁਹਾਡੀ ਪ੍ਰੋਫਾਈਲ ਵਿੱਚ ਸੈੱਟ ਕੀਤਾ ਯੂਜ਼ਰ ਐਕਸੈੱਸ ਟੋਕਨ ਹੈ |
| OPENAI_API_KEY | ਇਹ ਨਾਨ-ਐਜ਼ੂਰ OpenAI ਐਂਡਪੌਇੰਟ ਲਈ ਸਰਵਿਸ ਵਰਤਣ ਦੀ ਪਰਵਾਨਗੀ ਕੁੰਜੀ ਹੈ |
| AZURE_OPENAI_API_KEY | ਇਹ ਉਸ ਸਰਵਿਸ ਲਈ ਪਰਵਾਨਗੀ ਕੁੰਜੀ ਹੈ |
| AZURE_OPENAI_ENDPOINT | ਇਹ Azure OpenAI ਰਿਸੋਰਸ ਲਈ ਡਿਪਲੋਇਡ ਐਂਡਪੌਇੰਟ ਹੈ |
| AZURE_OPENAI_DEPLOYMENT | ਇਹ _ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ_ ਮਾਡਲ ਡਿਪਲੋਇਮੈਂਟ ਐਂਡਪੌਇੰਟ ਹੈ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | ਇਹ _ਟੈਕਸਟ ਐਮਬੈਡਿੰਗ_ ਮਾਡਲ ਡਿਪਲੋਇਮੈਂਟ ਐਂਡਪੌਇੰਟ ਹੈ |
| | |

ਨੋਟ: ਆਖਰੀ ਦੋ Azure OpenAI ਵੈਰੀਏਬਲ ਚੈਟ ਕੰਪਲੀਸ਼ਨ (ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ) ਅਤੇ ਵੈਕਟਰ ਸਰਚ (ਐਮਬੈਡਿੰਗ) ਲਈ ਡਿਫੌਲਟ ਮਾਡਲ ਦਰਸਾਉਂਦੇ ਹਨ। ਇਹ ਸੈੱਟ ਕਰਨ ਦੀ ਹਦਾਇਤ ਸੰਬੰਧਤ ਅਸਾਈਨਮੈਂਟਾਂ ਵਿੱਚ ਦਿੱਤੀ ਜਾਵੇਗੀ।

## Azure ਸੰਰਚਿਤ ਕਰੋ: ਪੋਰਟਲ ਤੋਂ

Azure OpenAI ਐਂਡਪੌਇੰਟ ਅਤੇ ਕੁੰਜੀ ਦੀ ਜਾਣਕਾਰੀ ਤੁਹਾਨੂੰ [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) ਵਿੱਚ ਮਿਲੇਗੀ, ਤਾਂ ਆਓ ਉੱਥੋਂ ਸ਼ੁਰੂ ਕਰੀਏ।

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) ਤੇ ਜਾਓ
1. ਸਾਈਡਬਾਰ (ਖੱਬੇ ਮੀਨੂ) ਵਿੱਚ **Keys and Endpoint** ਚੁਣੋ।
1. **Show Keys** ਤੇ ਕਲਿੱਕ ਕਰੋ - ਤੁਹਾਨੂੰ KEY 1, KEY 2 ਅਤੇ Endpoint ਵੇਖਾਈ ਦੇਣਗੇ।
1. AZURE_OPENAI_API_KEY ਲਈ KEY 1 ਦੀ ਵੈਲਯੂ ਵਰਤੋ
1. AZURE_OPENAI_ENDPOINT ਲਈ Endpoint ਦੀ ਵੈਲਯੂ ਵਰਤੋ

ਹੁਣ, ਅਸੀਂ ਆਪਣੇ ਡਿਪਲੋਇਡ ਮਾਡਲਾਂ ਲਈ ਐਂਡਪੌਇੰਟ ਲੈਣੇ ਹਨ।

1. Azure OpenAI ਰਿਸੋਰਸ ਲਈ ਸਾਈਡਬਾਰ (ਖੱਬੇ ਮੀਨੂ) ਵਿੱਚ **Model deployments** ਚੁਣੋ।
1. ਟੀਚਾ ਪੰਨੇ ਤੇ **Manage Deployments** ਤੇ ਕਲਿੱਕ ਕਰੋ

ਇਸ ਨਾਲ ਤੁਸੀਂ Azure OpenAI Studio ਵੈੱਬਸਾਈਟ ਤੇ ਪਹੁੰਚ ਜਾਵੋਗੇ, ਜਿੱਥੇ ਹੇਠਾਂ ਦਿੱਤੇ ਤਰੀਕੇ ਨਾਲ ਹੋਰ ਮੁੱਲ ਮਿਲਣਗੇ।

## Azure ਸੰਰਚਿਤ ਕਰੋ: Studio ਤੋਂ

1. [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **ਆਪਣੇ ਰਿਸੋਰਸ ਤੋਂ** ਉੱਤੇ ਜਾਓ, ਜਿਵੇਂ ਉਪਰ ਦਿੱਤਾ ਗਿਆ।
1. ਮੌਜੂਦਾ ਡਿਪਲੋਇਡ ਮਾਡਲ ਵੇਖਣ ਲਈ **Deployments** ਟੈਬ (ਸਾਈਡਬਾਰ, ਖੱਬੇ) ਤੇ ਕਲਿੱਕ ਕਰੋ।
1. ਜੇ ਤੁਹਾਡਾ ਚਾਹੀਦਾ ਮਾਡਲ ਡਿਪਲੋਇਡ ਨਹੀਂ, ਤਾਂ **Create new deployment** ਵਰਤ ਕੇ ਡਿਪਲੋਇ ਕਰੋ।
1. ਤੁਹਾਨੂੰ _ਟੈਕਸਟ-ਜਨਰੇਸ਼ਨ_ ਮਾਡਲ ਦੀ ਲੋੜ ਹੋਵੇਗੀ - ਅਸੀਂ ਸੁਝਾਅ ਦਿੰਦੇ ਹਾਂ: **gpt-35-turbo**
1. ਤੁਹਾਨੂੰ _ਟੈਕਸਟ-ਐਮਬੈਡਿੰਗ_ ਮਾਡਲ ਦੀ ਲੋੜ ਹੋਵੇਗੀ - ਅਸੀਂ ਸੁਝਾਅ ਦਿੰਦੇ ਹਾਂ **text-embedding-ada-002**

ਹੁਣ ਇਨਵਾਇਰਨਮੈਂਟ ਵੈਰੀਏਬਲਾਂ ਨੂੰ _Deployment name_ ਅਨੁਸਾਰ ਅਪਡੇਟ ਕਰੋ। ਆਮ ਤੌਰ ਤੇ ਇਹ ਮਾਡਲ ਨਾਂ ਹੀ ਹੋਵੇਗਾ ਜਦ ਤੱਕ ਤੁਸੀਂ ਖੁਦ ਨਾ ਬਦਲਿਆ ਹੋਵੇ। ਉਦਾਹਰਨ ਵਜੋਂ, ਤੁਹਾਡੇ ਕੋਲ ਇਹ ਹੋ ਸਕਦਾ ਹੈ:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**ਜਦੋਂ ਹੋ ਜਾਵੇ ਤਾਂ .env ਫਾਈਲ ਸੰਭਾਲਣੀ ਨਾ ਭੁੱਲੋ**। ਹੁਣ ਤੁਸੀਂ ਫਾਈਲ ਬੰਦ ਕਰਕੇ ਨੋਟਬੁੱਕ ਚਲਾਉਣ ਦੀ ਹਦਾਇਤਾਂ ਉੱਤੇ ਵਾਪਸ ਜਾ ਸਕਦੇ ਹੋ।

## OpenAI ਸੰਰਚਿਤ ਕਰੋ: ਪ੍ਰੋਫਾਈਲ ਤੋਂ

ਤੁਹਾਡੀ OpenAI API ਕੁੰਜੀ ਤੁਹਾਡੇ [OpenAI ਖਾਤੇ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) ਵਿੱਚ ਮਿਲੇਗੀ। ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਨਹੀਂ, ਤਾਂ ਖਾਤਾ ਬਣਾਓ ਅਤੇ API ਕੁੰਜੀ ਬਣਾਓ। ਜਦ ਤੁਹਾਡੇ ਕੋਲ ਕੁੰਜੀ ਆ ਜਾਵੇ, ਤਾਂ `.env` ਫਾਈਲ ਵਿੱਚ `OPENAI_API_KEY` ਵੈਰੀਏਬਲ ਵਿੱਚ ਭਰੋ।

## Hugging Face ਸੰਰਚਿਤ ਕਰੋ: ਪ੍ਰੋਫਾਈਲ ਤੋਂ

ਤੁਹਾਡਾ Hugging Face ਟੋਕਨ ਤੁਹਾਡੀ ਪ੍ਰੋਫਾਈਲ ਵਿੱਚ [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) ਹੇਠਾਂ ਮਿਲੇਗਾ। ਇਹਨਾਂ ਨੂੰ ਕਦੇ ਵੀ ਜਨਤਕ ਤੌਰ ਤੇ ਪੋਸਟ ਜਾਂ ਸਾਂਝਾ ਨਾ ਕਰੋ। ਇਸ ਪ੍ਰੋਜੈਕਟ ਲਈ ਨਵਾਂ ਟੋਕਨ ਬਣਾਓ ਅਤੇ `.env` ਫਾਈਲ ਵਿੱਚ `HUGGING_FACE_API_KEY` ਵੈਰੀਏਬਲ ਹੇਠਾਂ ਪਾਓ। _ਨੋਟ:_ ਇਹ ਤਕਨੀਕੀ ਤੌਰ ਤੇ API ਕੁੰਜੀ ਨਹੀਂ, ਪਰ ਪਰਮਾਣਕਿਤਾ ਲਈ ਵਰਤੀ ਜਾਂਦੀ ਹੈ, ਇਸ ਲਈ ਨਾਂਕਰਨ ਇੱਕੋ ਜਿਹਾ ਰੱਖਿਆ ਗਿਆ ਹੈ।

---

**ਅਸਵੀਕਰਨ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਅਸੀਂ ਯਥਾਸੰਭਵ ਸਹੀ ਅਨੁਵਾਦ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਪਰ ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਣਪਛਾਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼, ਜਿਸ ਭਾਸ਼ਾ ਵਿੱਚ ਉਹ ਲਿਖਿਆ ਗਿਆ ਹੈ, ਨੂੰ ਹੀ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਅਰਥ ਲਗਾਉਣ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।