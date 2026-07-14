# ਇੱਕ LLM ਪ੍ਰਦਾਤਾ ਚੁਣਨਾ ਅਤੇ ਕਨਫਿਗਰ ਕਰਨਾ 🔑

ਅਸਾਈਨਮੈਂਟ ਕੁਝ ਵਾਰ ਇੱਕ ਜਾਂ ਵੱਧ ਲਾਰਜ ਲਾਂਗਵੇਜ ਮਾਡਲ (LLM) ਡਿਪਲੌਇਮੈਂਟਾਂ ਖਿਲਾਫ ਕੰਮ ਕਰਨ ਲਈ ਸੈਟਅੱਪ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ, ਜੋ ਸਹਾਇਕ ਸੇਵਾ ਪ੍ਰਦਾਤਾ ਜਿਵੇਂ OpenAI, Azure ਜਾਂ Hugging Face ਦੇ ਜ਼ਰੀਏ ਹੁੰਦੇ ਹਨ। ਇਹ ਇੱਕ _ਹੋਸਟਡ ਏਂਡਪੌਇੰਟ_ (API) ਮੁਹੱਈਆ ਕਰਵਾਉਂਦੇ ਹਨ ਜਿਸ ਤੱਕ ਅਸੀਂ ਸਹੀ ਪ੍ਰਮਾਣ ਪੱਤਰਾਂ (API ਕੀ ਜਾਂ ਟੋਕਨ) ਨਾਲ ਪ੍ਰੋਗਰਾਮਾਟਿਕ ਤਰੀਕੇ ਨਾਲ ਪਹੁੰਚ ਕਰ ਸਕਦੇ ਹਾਂ। ਇਸ ਕੋਰਸ ਵਿੱਚ, ਅਸੀਂ ਇਨ੍ਹਾਂ ਪ੍ਰਦਾਤਿਆਂ ਬਾਰੇ ਚਰਚਾ ਕਰਦੇ ਹਾਂ:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) ਵੱਖ ਵੱਖ ਮਾਡਲਾਂ ਸਮੇਤ ਕੋਰ GPT ਸੀਰੀਜ਼।
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) ਜਿਹੜਾ ਉਦਯੋਗਿਕ ਤੈਯਾਰੀ 'ਤੇ ਕੇਂਦਰਿਤ OpenAI ਮਾਡਲਾਂ ਲਈ ਹੈ
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ਇੱਕੋ ਏਂਡਪੌਇੰਟ ਅਤੇ API ਕੀ ਨਾਲ ਸੈਂਕੜਿਆਂ ਮਾਡਲਾਂ ਤੱਕ ਪਹੁੰਚ ਵਾਸਤੇ OpenAI, Meta, Mistral, Cohere, Microsoft ਅਤੇ ਹੋਰ ਤੋਂ (GitHub Models ਨੂੰ ਬਦਲਦਾ ਹੈ, ਜੋ ਜੁਲਾਈ 2026 ਦੇ ਅੰਤ ਵਿੱਖੇ ਰਿਟਾਇਰ ਹੋ ਰਹਾ ਹੈ)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) ਖੁੱਲ੍ਹੇ ਸੋਰਸ ਮਾਡਲਾਂ ਅਤੇ ਇਨਫਰੈਂਸ ਸਰਵਰ ਲਈ
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ਜਾਂ [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) ਜੇ ਤੁਸੀਂ ਆਪਣੀ ਡਿਵਾਈਸ 'ਤੇ ਪੂਰੀ ਤਰ੍ਹਾਂ ਬਿਨਾਂ ਕਲਾਊਡ ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਦੇ ਮਾਡਲ ਚਲਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ

**ਇਨ੍ਹਾਂ ਅਭਿਆਸਾਂ ਲਈ ਤੁਹਾਨੂੰ ਆਪਣੇ ਹੀ ਖਾਤੇ ਵਰਤਣੇ ਪੈਣਗੇ**। ਅਸਾਈਨਮੈਂਟ ਵਿਕਲਪਿਕ ਹਨ ਤਾਂ ਤੁਸੀਂ ਆਪਣੀ ਰੁਚੀ ਅਨੁਸਾਰ ਇੱਕ, ਸਭ ਜਾਂ ਕੋਈ ਵੀ ਪ੍ਰਦਾਤਾ ਚੁਣ ਸਕਦੇ ਹੋ। ਸਾਇਨਅੱਪ ਲਈ ਕੁਝ ਮਦਦ:

| ਸਾਇਨਅੱਪ | ਲਾਗਤ | API ਕੀ | ਪਲੇਗ੍ਰਾਊਂਡ | ਟਿੱਪਣੀਆਂ |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [ਕੀਮਤ](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [ਪਰੋਜੈਕਟ-ਆਧਾਰਿਤ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [ਨੋ-ਕੋਡ, ਵੈੱਬ](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | ਕਈ ਮਾਡਲ ਉਪਲਬਧ |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [ਕੀਮਤ](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK ਤੁਰੰਤ ਸ਼ੁਰੂਆਤ](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [ਸਟੂਡੀਓ ਤੁਰੰਤ ਸ਼ੁਰੂਆਤ](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [ਪਹੁੰਚ ਲਈ ਪਹਿਲਾਂ ਅਪਲਾਈ ਕਰਨਾ ਲਾਜ਼ਮੀ](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [ਕੀਮਤ](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [ਪਰੋਜੈਕਟ ਓਵਰਵਿਊ ਪੇਜ਼](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry ਪਲੇਗ੍ਰਾਊਂਡ](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | ਮੁਫ਼ਤ ਪਰਤ ਉਪਲਬਧ; ਕਈ ਮਾਡਲ ਪ੍ਰਦਾਤਿਆਂ ਲਈ ਇੱਕ ਐਂਡਪੌਇੰਟ + ਕੀ |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [ਕੀਮਤ](https://huggingface.co/pricing) | [ਪਹੁੰਚ ਟੋਕਨ](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ਵਿੱਚ ਸੀਮਤ ਮਾਡਲ ਹਨ](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | ਮੁਫ਼ਤ (ਤੁਹਾਡੇ ਡਿਵਾਈਸ 'ਤੇ ਚੱਲਦਾ ਹੈ) | ਜ਼ਰੂਰੀ ਨਹੀਂ | [ਲੋਕਲ CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | ਪੂਰੀ ਤਰ੍ਹਾਂ ਆਫਲਾਈਨ, OpenAI-ਅਨੁਕੂਲ ਏਂਡਪੌਇੰਟ |
| | | | | |

ਵੱਖ-ਵੱਖ ਪ੍ਰਦਾਤਿਆਂ ਨਾਲ ਇਸ ਰਿਪੋਜਿਟਰੀ ਨੂੰ ਵਰਤੋਂ ਲਈ _ਕਨਫਿਗਰ_ ਕਰਨ ਲਈ ਹੇਠਾਂ ਦਿੱਤੇ ਨਿਰਦੇਸ਼ਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ। ਜਿਹੜੇ ਅਸਾਈਨਮੈਂਟ ਕਿਸੇ ਖਾਸ ਪ੍ਰਦਾਤਾ ਦੀ ਲੋੜ ਰੱਖਦੇ ਹਨ ਉਹਨਾਂ ਦੀ ਫਾਈਲਨਾਮ ਵਿੱਚ ਇਨ੍ਹਾਂ ਟੈਗਾਂ ਵਿੱਚੋਂ ਇੱਕ ਹੋਵੇਗਾ:

- `aoai` - Azure OpenAI ਏਂਡਪੌਇੰਟ, ਕੀ ਦੀ ਲੋੜ ਹੈ
- `oai` - OpenAI ਏਂਡਪੌਇੰਟ, ਕੀ ਦੀ ਲੋੜ ਹੈ
- `hf` - Hugging Face ਟੋਕਨ ਦੀ ਲੋੜ ਹੈ
- `githubmodels` - Microsoft Foundry Models ਏਂਡਪੌਇੰਟ, ਕੀ ਦੀ ਲੋੜ ਹੈ (GitHub Models ਜੁਲਾਈ 2026 ਦੇ ਅੰਤ 'ਤੇ ਰਿਟਾਇਰ ਹੋ ਰਿਹਾ ਹੈ)

ਤੁਸੀਂ ਇੱਕ, ਕੋਈ ਵੀ ਜਾਂ ਸਾਰੇ ਪ੍ਰਦਾਤਾ ਕਨਫਿਗਰ ਕਰ ਸਕਦੇ ਹੋ। ਸਬੰਧਿਤ ਅਸਾਈਨਮੈਂਟਾਂ ਵਿੱਚ ਜੇ ਪ੍ਰਮਾਣ ਪੱਤਰ ਮੌਜੂਦ ਨਹੀਂ ਹੋਣਗੇ ਤਾਂ ਸਿੱਧਾ ਐਰਰ ਆ ਜਾਵੇਗਾ।

## `.env` ਫਾਇਲ ਬਣਾਓ

ਅਸੀਂ ਮੰਨਦੇ ਹਾਂ ਕਿ ਤੁਸੀਂ ਪਹਿਲਾਂ ਹੀ ਉਪਰੋਕਤ ਗਾਈਡਲਾਈਨ ਪੜ੍ਹ ਲਈ ਹੈ ਅਤੇ ਸੰਬੰਧਿਤ ਪ੍ਰਦਾਤਾ ਨਾਲ ਸਾਇਨਅੱਪ ਕਰ ਲਿਆ ਹੈ, ਅਤੇ ਲੋੜੀਂਦੇ ਪ੍ਰਮਾਣਿਕਤਾ ਪੈਰਾਮੀਟਰ (API_KEY ਜਾਂ ਟੋਕਨ) ਪ੍ਰਾਪਤ ਕਰ ਲਿਆ ਹੈ। Azure OpenAI ਦੇ ਮਾਮਲੇ ਵਿੱਚ, ਅਸੀਂ ਇਹ ਵੀ ਮੰਨਦੇ ਹਾਂ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਇੱਕ Azure OpenAI ਸਰਵਿਸ (ਏਂਡਪੌਇੰਟ) ਦਾ ਮਾਨਿਆ ਹੋਇਆ ਡਿਪਲੌਯਮੈਂਟ ਹੈ ਜਿਸ 'ਤੇ ਘੱਟੋ-ਘੱਟ ਇੱਕ GPT ਮਾਡਲ ਚੈੱਟ ਪੂਰਤੀ ਲਈ ਡਿਪਲੌਇਡ ਹੈ।

ਅਗਲਾ ਕਦਮ ਤੁਹਾਡੇ **ਲੋਕਲ ਐਨਵਾਇਰਨਮੇਟ ਵੈਰੀਏਬਲਸ** ਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਕਨਫਿਗਰ ਕਰਨਾ ਹੈ:

1. ਰੂਟ ਫੋਲਡਰ ਵਿੱਚ `.env.copy` ਫਾਇਲ ਲੱਭੋ ਜਿਥੇ ਕੁਝ ਇਸ ਤਰ੍ਹਾਂ ਦੀ ਸਮੱਗਰੀ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ:

   ```bash
   # ਓਪਨ ਏਆਈ ਪ੍ਰਦਾਤਾ
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## ਮਾਇਕ੍ਰੋਸਾਫਟ ਫਾਉਂਡਰੀ ਵਿੱਚ ਏਜ਼ੁਰ ਓਪਨ ਏਆਈ
   ## (ਏਜ਼ੁਰ ਓਪਨ ਏਆਈ ਸਰਵਿਸ ਹੁਣ ਮਾਇਕ੍ਰੋਸਾਫਟ ਫਾਉਂਡਰੀ ਦਾ ਹਿੱਸਾ ਹੈ: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # ਮੂਲ ਸੈੱਟ ਹੈ! (ਵਰਤਮਾਨ ਸਥਿਰ ਜੀਏ ਏਪੀਐਈ ਵਰਜਨ)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## ਮਾਇਕ੍ਰੋਸਾਫਟ ਫਾਉਂਡਰੀ ਮਾਡਲ (ਬਹੁ-ਪ੍ਰਦਾਤਾ ਮਾਡਲ ਕੈਟਾਲੌਗ, ਜੋ ਗਿਟਹਬ ਮਾਡਲਾਂ ਦੀ ਥਾਂ ਲੈਂਦਾ ਹੈ, ਜਿਹੜੇ ਜੁਲਾਈ 2026 ਦੇ ਅੰਤ 'ਚ ਸੰਤੋਖਾਪੂਰਕ ਤੌਰ 'ਤੇ ਖਤਮ ਹੋ ਜਾਣਗੇ)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## ਹੱਗਿੰਗ ਫੇਸ
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. ਉਹ ਫਾਇਲ `.env` ਵਿੱਚ ਕਾਪੀ ਕਰੋ ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡ ਨਾਲ। ਇਹ ਫਾਇਲ _gitignore ਕੀਤੀ ਜਾਂਦੀ ਹੈ_, ਜੋ ਰਹੱਸ ਭਰੇ ਡੈਟਾ ਨੂੰ ਸੁਰੱਖਿਅਤ ਰੱਖਦੀ ਹੈ।

   ```bash
   cp .env.copy .env
   ```

3. ਮੁੱਲ (ਸੱਜਾ ਪਾਸਾ `=` ਵਾਲੀ ਜਗ੍ਹਾ) ਭਰੋ ਜਿਵੇਂ ਅਗਲੇ ਭਾਗ ਵਿੱਚ ਦਿੱਤਾ ਹੈ।

4. (ਵਿਕਲਪ) ਜੇ ਤੁਸੀਂ GitHub Codespaces ਵਰਤਦੇ ਹੋ, ਤਾਂ ਤੁਹਾਡੇ ਕੋਲ ਇਹ ਵਿਕਲਪ ਹੈ ਕਿ ਅਸੀਂ ਐਨਵਾਇਰਨਮੇਟ ਵੈਰੀਏਬਲਸ ਨੂੰ ਇਸ ਰਿਪੋਜਿਟਰੀ ਨਾਲ ਜੁੜੇ _Codespaces secrets_ ਵੱਜੋਂ ਸੰਭਾਲ ਸਕਦੇ ਹਾਂ। ਇਸ ਸਥਿਤੀ ਵਿੱਚ, ਤੁਹਾਨੂੰ ਲੋਕਲ .env ਫਾਇਲ ਸੈਟਅੱਪ ਕਰਨ ਦੀ ਲੋੜ ਨਹੀਂ ਪਵੇਗੀ। **ਪਰ ਇਹ ਵਿਕਲਪ ਸਿਰਫ GitHub Codespaces ਵਰਤੋਂ ਕਰਨ 'ਤੇ ਹੀ ਕੰਮ ਕਰਦਾ ਹੈ।** ਜੇ ਤੁਸੀਂ Docker Desktop ਵਰਤਦੇ ਹੋ ਤਾਂ ਫਿਰ ਵੀ .env ਫਾਇਲ ਸੈਟਅੱਪ ਕਰਨ ਦੀ ਲੋੜ ਹੋਵੇਗੀ।

## `.env` ਫਾਇਲ ਭਰੋ

ਆਓ ਦੇਖੀਏ ਇਹ ਵੈਰੀਏਬਲ ਨਾਮ ਕਿਸ ਬਾਰੇ ਹਨ:

| ਵੈਰੀਏਬਲ | ਵਰਨਨ |
| :--- | :--- |
| HUGGING_FACE_API_KEY | ਇਹ ਉਪਭੋਗਤਾ ਪਹੁੰਚ ਟੋਕਨ ਹੈ ਜੋ ਤੁਸੀਂ ਆਪਣੀ ਪ੍ਰੋਫਾਈਲ ਵਿੱਚ ਸੈਟ ਕੀਤਾ ਹੈ |
| OPENAI_API_KEY | ਇਹ ਉਹ ਪ੍ਰਮਾਣਕੰਨ ਕੁੰਜੀ ਹੈ ਜੋ ਨੌਂ-ਐਜ਼ੂਰ OpenAI ਏਂਡਪੌਇੰਟ ਦੀ ਸੇਵਾ ਲਈ ਵਰਤੀ ਜਾਂਦੀ ਹੈ |
| AZURE_OPENAI_API_KEY | ਇਹ ਸੇਵਾ ਵਰਤਣ ਲਈ ਪ੍ਰਮਾਣਕੰਨ ਕੁੰਜੀ ਹੈ |
| AZURE_OPENAI_ENDPOINT | ਇਹ ਏਂਡਪੌਇੰਟ ਹੈ ਜੋ Azure OpenAI ਰਿਸੋਰਸ ਲਈ ਡਿਪਲੌਇਡ ਕੀਤਾ ਗਿਆ ਹੈ |
| AZURE_OPENAI_DEPLOYMENT | ਇਹ _ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ_ ਮਾਡਲ ਡਿਪਲੌਇਮੈਂਟ ਏਂਡਪੌਇੰਟ ਹੈ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | ਇਹ _ਟੈਕਸਟ ਐਂਬੈੱਡਿੰਗ_ ਮਾਡਲ ਡਿਪਲੌਇਮੈਂਟ ਏਂਡਪੌਇੰਟ ਹੈ |
| AZURE_INFERENCE_ENDPOINT | ਇਹ ਤੁਹਾਡੇ Microsoft Foundry ਪ੍ਰੋਜੈਕਟ ਦਾ ਏਂਡਪੌਇੰਟ ਹੈ, ਜੋ Microsoft Foundry Models ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ |
| AZURE_INFERENCE_CREDENTIAL | ਇਹ ਤੁਹਾਡੇ Microsoft Foundry ਪ੍ਰੋਜੈਕਟ ਲਈ API ਕੁੰਜੀ ਹੈ |
| | |

ਨੋਟ: ਆਖਰੀ ਦੋ Azure OpenAI ਵੈਰੀਏਬਲਾਂ ਚੈਟ ਪੂਰਤੀ (ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ) ਅਤੇ ਵਿਕਟਰ ਖੋਜ (ਐਂਬੈੱਡਿੰਗ) ਲਈ ਡਿਫਾਲਟ ਮਾਡਲ ਨੂੰ ਦਰਸਾਉਂਦੇ ਹਨ। ਇਹਨਾਂ ਦਾ ਸੈਟਅੱਪ ਸੰਬੰਧਿਤ ਅਸਾਈਨਮੈਂਟਾਂ ਵਿੱਚ ਦੱਸਿਆ ਜਾਵੇਗਾ।

## Azure OpenAI ਮੁਹਿਆ ਕਰਵਾਓ: ਪੋਰਟਲ ਤੋਂ

> **ਨੋਟ:** Azure OpenAI ਸਰਵਿਸ ਹੁਣ [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) ਦਾ ਹਿੱਸਾ ਹੈ। ਸਰੋਤ ਅਤੇ ਡਿਪਲੌਇਮੈਂਟ Azure ਪੋਰਟਲ ਵਿੱਚ ਵੇਖੇ ਜਾ ਸਕਦੇ ਹਨ, ਪਰ ਰੋਜ਼ਾਨਾ ਮਾਡਲ ਪ੍ਰਬੰਧਨ (ਡਿਪਲੌਇਮੈਂਟ, ਪਲੇਗ੍ਰਾਊਂਡ, ਨਿਗਰਾਨੀ) ਹੁਣ Foundry ਪੋਰਟਲ ਵਿੱਚ ਹੁੰਦਾ ਹੈ, ਨਾ ਕਿ ਪੁਰਾਣੇ ਅਲੱਗ "Azure OpenAI Studio" ਵਿੱਚ।

Azure OpenAI ਏਂਡਪੌਇੰਟ ਅਤੇ ਕੀ ਦੀਆਂ ਮੁੱਲਾਂ [Azure ਪੋਰਟਲ](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) 'ਚ ਮਿਲਣਗੀਆਂ, ਤਾਂ ਆਓ ਉਹਥੋਂ ਸ਼ੁਰੂ ਕਰੀਏ।

1. [Azure ਪੋਰਟਲ](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) 'ਤੇ ਜਾਓ
1. ਸਾਈਡਬਾਰ (ਖੱਬੇ ਪਾਸੇ ਮੈਨੂ) ਵਿੱਚ **ਕੀ ਅਤੇ ਏਂਡਪੌਇੰਟ** ਚੁਣੋ।
1. **ਕੀ ਦਿਖਾਓ** 'ਤੇ ਕਲਿੱਕ ਕਰੋ - ਤੁਹਾਨੂੰ ਇਹ ਜਾਣਕਾਰੀ ਮਿਲੇਗੀ: KEY 1, KEY 2 ਅਤੇ Endpoint।
1. AZURE_OPENAI_API_KEY ਲਈ KEY 1 ਮੁੱਲ ਵਰਤੋ
1. AZURE_OPENAI_ENDPOINT ਲਈ Endpoint ਵੈਲਯੂ ਵਰਤੋ

ਅਗਲੇ ਕਦਮ ਵਿੱਚ ਸਾਨੂੰ ਉਹ ਏਂਡਪੌਇੰਟ ਚਾਹੀਦੇ ਹਨ ਜੋ ਸਾਡੇ ਨਿਰਧਾਰਤ ਮਾਡਲਾਂ ਲਈ ਡਿਪਲੌਇਡ ਕੀਤੇ ਗਏ ਹਨ।

1. Azure OpenAI ਸਰੋਤ ਲਈ ਸਾਈਡਬਾਰ (ਖੱਬਾ ਮੈਨੂ) ਵਿੱਚ **ਮਾਡਲ ਡਿਪਲੌਇਮੈਂਟਸ** ਚੁਣੋ।
1. ਮੰਜ਼ਿਲੇ ਪੰਨੇ ਤੇ, **Microsoft Foundry ਪੋਰਟਲ 'ਤੇ ਜਾਓ** (ਜਾਂ **ਡਿਪਲੌਇਮੈਂਟ ਪ੍ਰਬੰਧਨ**, ਤੁਹਾਡੇ ਸਰੋਤ ਦੇ ਕਿਸਮ ਅਨੁਸਾਰ)

ਇਹ ਤੁਹਾਨੂੰ Microsoft Foundry ਪੋਰਟਲ 'ਤੇ ਲੈ ਜਾਵੇਗਾ, ਜਿੱਥੇ ਅਸੀਂ ਹੋਰ ਮੁੱਲ ਹੇਠਾਂ ਦਿੱਤੇ ਬਿਆਨ ਅਨੁਸਾਰ ਲੱਭਾਂਗੇ।

## Azure OpenAI ਮੁਹਿਆ ਕਰਵਾਓ: Microsoft Foundry ਪੋਰਟਲ ਤੋਂ

1. [Microsoft Foundry ਪੋਰਟਲ](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) 'ਤੇ ਆਪਣੇ ਸਰੋਤ ਤੋਂ ਜਾਓ ਜਿਵੇਂ ਉਪਰ ਦਿੱਤਾ ਹੈ।
1. ਮੌਜੂਦਾ ਡਿਪਲੌਇਡ ਮਾਡਲਾਂ ਨੂੰ ਵੇਖਣ ਲਈ ਸਾਈਡਬਾਰ (ਖੱਬੇ) ਵਿੱਚ **ਡਿਪਲੌਇਮੈਂਟਸ** ਟੈਬ ਤੇ ਕਲਿੱਕ ਕਰੋ।
1. ਜੇ ਤੁਹਾਡਾ ਚਾਹਿਦਾ ਮਾਡਲ ਡਿਪਲੌਇਡ ਨਹੀਂ ਹੈ, ਤਾਂ [ਮਾਡਲ ਕੈਟਾਲੌਗ](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ਤੋਂ ਇਸਨੂੰ ਡਿਪਲੌਇ ਕਰੋ।
1. ਤੁਹਾਨੂੰ ਇੱਕ _ਟੈਕਸਟ-ਜਨਰੇਸ਼ਨ_ ਮਾਡਲ ਦੀ ਲੋੜ ਪਵੇਗੀ - ਅਸੀਂ ਸਿਫ਼ਾਰਸ਼ ਕਰਦੇ ਹਾਂ: **gpt-4o-mini**
1. ਤੁਹਾਨੂੰ ਇੱਕ _ਟੈਕਸਟ-ਐਂਬੈੱਡਿੰਗ_ ਮਾਡਲ ਦੀ ਲੋੜ ਪਵੇਗੀ - ਅਸੀਂ ਸਿਫ਼ਾਰਸ਼ ਕਰਦੇ ਹਾਂ **text-embedding-3-small**

ਹੁਣ ਐਨਵਾਇਰਨਮੇਟ ਵੈਰੀਏਬਲਾਂ ਨੂੰ ਅਪਡੇਟ ਕਰੋ ਤਾ ਕਿ _ਡਿਪਲੌਇਮੈਂਟ ਨਾਂ_ ਦਰਸਾਇਆ ਜਾ ਸਕੇ। ਆਮ ਤੌਰ 'ਤੇ ਇਹ ਮਾਡਲ ਨਾਮ ਦੇ ਬਰਾਬਰ ਹੁੰਦਾ ਹੈ ਜਦ ਤੱਕ ਤੁਸੀਂ ਇਸਨੂੰ ਖਾਸ ਤੌਰ ਤੇ ਨਹੀਂ ਬਦਲਦੇ। ਉਦਾਹਰਨ ਵੱਜੋਂ:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**ਜਦੋਂ ਕੰਮ ਮੁਕੰਮਲ ਹੋ ਜਾਵੇ ਤਾਂ .env ਫਾਇਲ ਸੇਵ ਕਰਨਾ ਨਾ ਭੁੱਲੋ।** ਹੁਣ ਤੁਸੀਂ ਫਾਇਲ ਨੂੰ ਬੰਦ ਕਰ ਸਕਦੇ ਹੋ ਅਤੇ ਨੋਟਬੁੱਕ ਚਲਾਉਣ ਲਈ ਨਿਰਦੇਸ਼ਾਂ ਵੱਲ ਵਾਪਸ ਜਾ ਸਕਦੇ ਹੋ।

## OpenAI ਮੁਹਿਆ ਕਰਵਾਓ: ਪ੍ਰੋਫਾਈਲ ਤੋਂ

ਤੁਹਾਡੀ OpenAI API ਕੀ ਤੁਹਾਡੇ [OpenAI ਖਾਤੇ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) ਵਿੱਚ ਮਿਲ ਸਕਦੀ ਹੈ। ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਨਹੀਂ ਹੈ, ਤਾਂ ਤੁਸੀਂ ਖਾਤਾ ਬਣਾਕੇ API ਕੀ ਤਿਆਰ ਕਰ ਸਕਦੇ ਹੋ। ਇੱਕ ਵਾਰੀ ਕੀ ਮਿਲ ਜਾਣ 'ਤੇ `.env` ਫਾਇਲ ਵਿੱਚ `OPENAI_API_KEY` ਵੈਰੀਏਬਲ ਭਰੋ।

## Hugging Face ਮੁਹਿਆ ਕਰਵਾਓ: ਪ੍ਰੋਫਾਈਲ ਤੋਂ

ਤੁਹਾਡਾ Hugging Face ਟੋਕਨ ਤੁਹਾਡੇ ਪ੍ਰੋਫਾਈਲ ਵਿੱਚ [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) ਹੇਠਾਂ ਮਿਲੇਗਾ। ਇਹਨਾਂ ਨੂੰ ਜਨਤਕ ਸਾਂਝਾ ਨਾ ਕਰੋ। ਇਸ ਪ੍ਰੋਜੈਕਟ ਲਈ ਇੱਕ ਨਵਾਂ ਟੋਕਨ ਬਣਾਓ ਅਤੇ ਉਸਨੂੰ `.env` ਫਾਇਲ ਵਿੱਚ `HUGGING_FACE_API_KEY` ਵੈਰੀਏਬਲ ਹੇਠਾਂ ਪੇਸਟ ਕਰੋ। _ਨੋਟ:_ ਇਹ ਤਕਨੀਕੀ ਤੌਰ 'ਤੇ API ਕੁੰਜੀ ਨਹੀਂ ਹੈ ਪਰ ਪ੍ਰਮਾਣਿਕਤਾ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ, ਇਸ ਲਈ ਅਸੀਂ ਸਮਰੱਥਾ ਲਈ ਇਹ ਨਾਮ ਵਰਤ ਰਹੇ ਹਾਂ।

## Microsoft Foundry Models ਮੁਹਿਆ ਕਰਵਾਓ: ਪੋਰਟਲ ਤੋਂ

> **ਨੋਟ:** GitHub Models ਜੁਲਾਈ 2026 ਦੇ ਆਖ਼ਰੀ ਹਫ਼ਤੇ ਰਿਟਾਇਰ ਹੋ ਰਹੇ ਹਨ। Microsoft Foundry Models ਸਿੱਧਾ ਬਦਲੀ ਹੈ, ਮੁਫ਼ਤ ਮਾਡਲ ਕੈਟਾਲੌਗ ਅਤੇ Azure AI ਇਨਫਰੈਂਸ SDK / OpenAI SDK ਦੇ ਤਜਰਬੇ ਨਾਲ।

1. [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) 'ਤੇ ਜਾਓ ਅਤੇ ਇੱਕ Foundry ਪ੍ਰੋਜੈਕਟ ਬਣਾਓ (ਜਾਂ ਖੋਲ੍ਹੋ)।
1. [ਮਾਡਲ ਕੈਟਾਲੌਗ](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ਵਿਚੋਂ ਕੋਈ ਮਾਡਲ ਚੁਣਕੇ ਡਿਪਲੌਇ ਕਰੋ, ਜਿਵੇਂ `gpt-4o-mini`।
1. ਪ੍ਰੋਜੈਕਟ ਦੀ **ਓਵਰਵਿਊ** ਪੇਜ਼ 'ਤੇ ਜਾ ਕੇ **ਏਂਡਪੌਇੰਟ** ਅਤੇ **API ਕੀ** ਨਕਲ ਕਰੋ।
1. `.env` ਫਾਇਲ ਵਿੱਚ `AZURE_INFERENCE_ENDPOINT` ਲਈ ਏਂਡਪੌਇੰਟ ਅਤੇ `AZURE_INFERENCE_CREDENTIAL` ਲਈ ਕੀ ਦੀ ਮੁੱਲ ਦਿਓ।

## ਆਫਲਾਈਨ / ਲੋਕਲ ਪ੍ਰਦਾਤਾ

ਜੇ ਤੁਸੀਂ ਬਿਲਕुल ਕਲਾਊਡ ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਵਰਤਣਾ ਨਹੀਂ ਚਾਹੁੰਦੇ, ਤਾਂ ਤੁਸੀਂ ਖੁੱਲ੍ਹੇ ਮਾਡਲ ਸਿੱਧਾ ਆਪਣੀ ਡਿਵਾਈਸ 'ਤੇ ਚਲਾ ਸਕਦੇ ਹੋ:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - ਮਾਈਕ੍ਰੋਸੌਫਟ ਦਾ ਡਿਵਾਈਸ ਉੱਤੇ ਰਨਟਾਈਮ। ਇਹ ਆਪਣੇ ਆਪ ਸਭ ਤੋਂ ਵਧੀਆ ਐਗਜ਼ੀਕਿੁਸ਼ਨ ਪ੍ਰਦਾਤਾ (NPU, GPU, ਜਾਂ CPU) ਚੁਣਦਾ ਹੈ ਅਤੇ OpenAI-ਅਨੁਕੂਲ ਏਂਡਪੌਇੰਟ ਦਿੰਦਾ ਹੈ, ਤਾਂ ਜੋ ਤੁਸੀਂ ਇਸ ਕੋਰਸ ਵਿੱਚ ਦਿੱਤੇ ਉਦਾਹਰਨ ਕੋਡ ਨੂੰ ਘੱਟ ਤੋਂ ਘੱਟ ਬਦਲ ਕੇ ਵਰਤ ਸਕੋ। ਸ਼ੁਰੂਆਤ ਲਈ [Foundry Local ਦਸਤਾਵੇਜ਼](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) ਵੇਖੋ, ਜਾਂ ਇਹ ਕمانਡ ਚਲਾ ਕੇ ਇਨਸਟਾਲ ਕਰੋ: `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS)।
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - ਖੁੱਲ੍ਹੇ ਮਾਡਲਾਂ ਜਿਵੇਂ Llama, Phi, Mistral, ਤੇ Gemma ਨੂੰ ਲੋਕਲ ਚਲਾਉਣ ਲਈ ਇੱਕ ਲੋਕਪ੍ਰਿਯ ਵਿਕਲਪ।


ਦੋਹਾਂ ਵਿਕਲਪਾਂ ਦੇ ਭੌਤਿਕ ਉਦਾਹਰਨਾਂ ਲਈ [Lesson 19: Building with SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) ਨੂੰ ਦੇਖੋ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->