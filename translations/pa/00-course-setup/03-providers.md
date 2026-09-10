# ਇੱਕ LLM ਪ੍ਰਦਾਤਾ ਚੁਣਨਾ ਅਤੇ ਸੰਰਚਨਾ ਕਰਨ 🔑

ਨਿਯੁਕਤੀ **ਸ਼ਾਇਦ** ਇੱਕ ਜਾਂ ਵੱਧ ਲਾਰਜ ਲੈੰਗਵੇਜ਼ ਮਾਡਲ (LLM) ਤੈਅਾਰੀਆਂ ਵਿਰੁੱਧ ਕੰਮ ਕਰਨ ਲਈ ਸੈੱਟਅਪ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹਨ ਇੱਕ ਸਮਰਥਿਤ ਸੇਵਾ ਪ੍ਰਦਾਤਾ ਜਿਵੇਂ ਕਿ OpenAI, Azure ਜਾਂ Hugging Face ਰਾਹੀਂ। ਇਹ ਇਕ _ਹੋਸਟ ਕੀਤਾ ਹੋਇਆ ਐਂਡਪੌਇੰਟ_ (API) ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ ਜਿਸ ਨੂੰ ਅਸੀਂ ਸਹੀ ਪ੍ਰਮਾਣ ਪੱਤਰਾਂ (API ਕੀ ਜਾਂ ਟੋਕਨ) ਨਾਲ ਪਰੋਗਰਾਮੈਟਿਕ ਤਰੀਕੇ ਨਾਲ ਦਿੱਤਲ੍ਹ ਕਰ ਸਕਦੇ ਹਾਂ। ਇਸ ਕੋਰਸ ਵਿੱਚ, ਅਸੀਂ ਇਹਨਾਂ ਪ੍ਰਦਾਤਾਵਾਂ ਬਾਰੇ ਚਰਚਾ ਕਰਦੇ ਹਾਂ:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) ਵਿੱਚ ਵੱਖ-ਵੱਖ ਮਾਡਲਾਂ ਸਮੇਤ ਕੋਰ GPT ਸੀਰੀਜ਼ ਸ਼ਾਮਲ ਹੈ।
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) OpenAI ਮਾਡਲਾਂ ਲਈ ਜਿੱਥੇ ਉਦਯੋਗਿਕ ਤਿਆਰੀ ਉੱਤੇ ਧਿਆਨ ਹੈ।
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ਇੱਕ ਏਂਡਪੌਇੰਟ ਅਤੇ API ਕੀ ਨਾਲ਼ ਸੈਂਕੜੇ ਮਾਡਲਾਂ ਨੂੰ ਪਰਾਪਤ ਕਰਨ ਲਈ OpenAI, Meta, Mistral, Cohere, Microsoft ਅਤੇ ਹੋਰ ਤੋਂ (GitHub Models ਦੀ ਥਾਂ ਜਿਹੜਾ ਜੁਲਾਈ 2026 ਦੇ ਅੰਤ ਵਿੱਚ ਰਿਟਾਇਰ ਹੋ ਰਿਹਾ ਹੈ)।
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) ਖੁੱਲ੍ਹੇ ਸਰੋਤ ਮਾਡਲਾਂ ਅਤੇ ਇਨਫਰੈਂਸ ਸਰਵਰ ਲਈ
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ਜਾਂ [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) ਜੇ ਤੁਸੀਂ ਆਪਣੇ ਜੰਤਰ 'ਤੇ ਪੂਰੀ ਤਰ੍ਹਾਂ ਅਫਲਾਈਨ ਮਾਡਲ ਚਲਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਬਿਨਾਂ ਕਿਸੇ ਕਲਾਉਡ ਸਰਵਿਸ ਵਾਲੇ ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਦੀ ਲੋੜ ਦੇ

**ਤੁਹਾਨੂੰ ਇਨ੍ਹਾਂ ਅਭਿਆਸਾਂ ਲਈ ਆਪਣੀਆਂ ਖਾਤਿਆਂ ਦੀ ਵਰਤੋਂ ਕਰਨ ਦੀ ਲੋੜ ਪਵੇਗੀ**। ਨਿਯੁਕਤੀਆਂ ਵਿਕਲਪੀ ਹਨ ਇਸ ਲਈ ਤੁਸੀਂ ਆਪਣੀ ਰੁਚੀ ਦੇ ਅਨੁਸਾਰ ਇੱਕ, ਸਾਰੇ ਜਾਂ ਕੋਈ ਨਹੀਂ ਪ੍ਰਦਾਤਾ ਸੈੱਟਅਪ ਕਰ ਸਕਦੇ ਹੋ। ਸਾਈਨਅਪ ਲਈ ਕੁਝ ਮਦਦ:

| ਸਾਈਨਅਪ | ਲਾਗਤ | API ਕੀ | ਪਲੇਗ੍ਰਾਊਂਡ | ਟਿੱਪਣੀਆਂ |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [ਕੀਮਤਾਂ](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [ਪ੍ਰੋਜੈਕਟ-ਅਧਾਰਿਤ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, ਵੈੱਬ](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | ਕਈ ਮਾਡਲ ਉਪਲਬਧ |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [ਕੀਮਤ](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK ਕੁਵਿਕਸਟਾਰਟ](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [ਸਟੂਡੀਓ ਕੁਵਿਕਸਟਾਰਟ](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [ਪਹੁੰਚ ਲਈ ਪਹਿਲਾਂ ਅਰਜ਼ੀ ਦੇਣੀ ਲਾਜ਼ਮੀ](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [ਕੀਮਤ](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [ਪ੍ਰੋਜੈਕਟ ਓਵਰਵਿਉ ਪੰਨਾ](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry ਪਲੇਗ੍ਰਾਊਂਡ](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | ਮੁਫ਼ਤ ਤਹਿਰੀ ਉਪਲਬਧ; ਇਕ ਏਂਡਪੌਇੰਟ + ਕੀ ਕਈ ਮਾਡਲ ਪ੍ਰਦਾਤਾਵਾਂ ਲਈ |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [ਕੀਮਤ](https://huggingface.co/pricing) | [ਐਕਸੈਸ ਟੋਕਨ](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging ਚੈਟ](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging ਚੈਟ ਵਿੱਚ ਸੀਮਿਤ ਮਾਡਲ ਹਨ](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | ਮੁਫਤ (ਤੁਹਾਡੇ ਜੰਤਰ 'ਤੇ ਚੱਲਦਾ ਹੈ) | ਲੋੜ ਨਹੀਂ | [ਲੋਕਲ CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | ਪੂਰੀ ਤਰ੍ਹਾਂ ਅਫਲਾਈਨ, OpenAI-ਅਨੁਕੂਲ ਏਂਡਪੌਇੰਟ |
| | | | | |

ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਹਦਾਇਤਾਂ ਦੀ ਪਾਲਣਾ ਕਰਕੇ ਇਸ ਰਿਪਾਜ਼ਟਰੀ ਨੂੰ ਵੱਖ-ਵੱਖ ਪ੍ਰਦਾਤਿਆਂ ਨਾਲ ਵਰਤੋਂ ਲਈ _ਕੰਫਿਗਰ_ ਕਰੋ। ਨਿਯੁਕਤੀਆਂ ਜੋ ਕਿਸੇ ਖਾਸ ਪ੍ਰਦਾਤਾ ਦੀ ਲੋੜ ਰੱਖਦੀਆਂ ਹਨ ਉਹਨਾਂ ਦੇ ਫਾਈਲਾਂ ਦੇ ਨਾਮ ਵਿੱਚ ਇਹਨਾਂ ਟੈਗਾਂ ਵਿੱਚੋਂ ਕੋਈ ਇੱਕ ਹੋਵੇਗਾ:

- `aoai` - ਇਹ Azure OpenAI ਐਂਡਪੌਇੰਟ ਅਤੇ ਕੀ ਦੀ ਲੋੜ ਹੈ
- `oai` - ਇਹ OpenAI ਐਂਡਪੌਇੰਟ ਅਤੇ ਕੀ ਦੀ ਲੋੜ ਹੈ
- `hf` - ਇਹ Hugging Face ਟੋਕਨ ਦੀ ਲੋੜ ਹੈ
- `githubmodels` - ਇਹ Microsoft Foundry ਮਾਡਲਾਂ ਦੇ ਐਂਡਪੌਇੰਟ ਅਤੇ ਕੀ ਦੀ ਲੋੜ ਹੈ (GitHub Models ਜੁਲਾਈ 2026 ਦੇ ਅੰਤ ਵਿੱਚ ਰਿਟਾਇਰ ਹੋ ਰਹੀ ਹੈ)

ਤੁਸੀਂ ਇੱਕ, ਕੋਈ ਨਹੀਂ, ਜਾਂ ਸਾਰੇ ਪ੍ਰਦਾਤਾ ਸੰਰਚਿਤ ਕਰ ਸਕਦੇ ਹੋ। ਸੰਬੰਧਿਤ ਨਿਯੁਕਤੀਆਂ ਅਣਉਪਲੱਬਧ ਪ੍ਰਮਾਣਪੱਤਰਾਂ 'ਤੇ ਸਿਰਫ਼ ਗਲਤੀ ਕਰ ਕੇ ਰੁਕ ਜਾਣਗੀਆਂ।

## `.env` ਫਾਇਲ ਬਣਾਓ

ਅਸੀਂ ਧਾਰਨਾ ਕਰਦੇ ਹਾਂ ਕਿ ਤੁਸੀਂ ਉਪਰੋਕਤ ਮਾਰਗਦਰਸ਼ਨ ਪੜ੍ਹ ਲਿਆ ਹੈ ਅਤੇ ਸੰਬੰਧਿਤ ਪ੍ਰਦਾਤਾ ਨਾਲ ਸਾਈਨਅਪ ਕਰ ਚੁੱਕੇ ਹੋ ਅਤੇ ਜ਼ਰੂਰੀ ਪ੍ਰਮਾਣਿਕਤਾ ਦੇ ਪ੍ਰਮਾਣ ਪੱਤਰ (API_KEY ਜਾਂ ਟੋਕਨ) ਪ੍ਰਾਪਤ ਕੀਤੇ ਹਨ। Azure OpenAI ਦੇ ਕੇਸ ਵਿੱਚ, ਅਸੀਂ ਧਾਰਨਾ ਕਰਦੇ ਹਾਂ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਇੱਕ Azure OpenAI ਸੇਵਾ ਦੀ ਵੈਧ ਤੈਅਾਰੀ (ਐਂਡਪੌਇੰਟ) ਹੈ ਜਿਸ 'ਤੇ ਘੱਟੋ-ਘੱਟ ਇੱਕ GPT ਮਾਡਲ ਚੈਟ ਪੂਰਨ ਕਰਨ ਲਈ ਤੈਅਾਰ ਹੈ।

ਅਗਲਾ ਕਦਮ ਇਹ ਹੈ ਕਿ ਤੁਸੀਂ ਆਪਣੇ **ਲੋਕਲ ਵਾਤਾਵਰਣ ਚਲਨਯੋਗਾਂ** ਨੂੰ ਹੇਠਾਂ ਦਿੱਤੇ ਤਰੀਕੇ ਨਾਲ ਸੰਰਚਿਤ ਕਰੋ:

1. ਰੂਟ ਫੋਲਡਰ ਵਿੱਚ `.env.copy` ਫਾਇਲ ਲੱਭੋ ਜਿਸ ਵਿੱਚ ਇਸ ਤਰ੍ਹਾਂ ਸਮੱਗਰੀ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ:

   ```bash
   # OpenAI ਪ੍ਰਦਾਤਾ
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## ਮਾਇਕ੍ਰੋਸੋਫਟ ਫੌਂਡਰੀ ਵਿੱਚ Azure OpenAI
   ## (Azure OpenAI ਸੇਵਾ ਹੁਣ ਮਾਇਕ੍ਰੋਸੋਫਟ ਫੌਂਡਰੀ ਦਾ ਹਿੱਸਾ ਹੈ: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # ਡਿਫੌਲਟ ਸੈਟ ਕੀਤਾ ਗਿਆ ਹੈ! (ਮੌਜੂਦਾ ਸਥਿਰ GA API ਵਰਜ਼ਨ)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## ਮਾਇਕ੍ਰੋਸੋਫਟ ਫੌਂਡਰੀ ਮਾਡਲ (ਮਲਟੀ-ਪ੍ਰਦਾਤਾ ਮਾਡਲ ਕੈਟਾਲਾਗ, GitHub ਮਾਡਲਾਂ ਨੂੰ ਬਦਲਦਾ ਹੈ, ਜੋ 2026 ਦੇ ਜੁਲਾਈ ਅੰਤ ਵਿੱਚ ਰਿਟਾਇਰ ਹੋ ਜਾਂਦੇ ਹਨ)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## ਹੱਗਿੰਗ ਫੇਸ
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. ਹੇਠਾਂ ਦਿੱਤੇ ਆਦੇਸ਼ ਨਾਲ ਉਸ ਫਾਇਲ ਨੂੰ `.env` ਵਿੱਚ ਕਾਪੀ ਕਰੋ। ਇਹ ਫਾਇਲ _gitignore ਕੀਤੀ ਗਈ_ ਹੈ, ਜੋ ਸੁਰੱਖਿਅਤ ਰੱਖਦੀ ਹੈ ਸੀਕ੍ਰੇਟਾਂ ਨੂੰ।

   ```bash
   cp .env.copy .env
   ```

3. ਮੁੱਲ ਭਰੋ (ਸਮਾਨ ਦੇ ਖੱਬੇ ਪਾਸੇ ਦਿੱਤੇ ਪਲੇਸਹੋਲਡਰਾਂ ਨੂੰ ਬਦਲੋ) ਜਿਵੇਂ ਅਗਲੇ ਭਾਗ ਵਿੱਚ ਦਿੱਤਾ ਹੈ।

4. (ਵਿਕਲਪ) ਜੇ ਤੁਸੀਂ GitHub Codespaces ਵਰਤਦੇ ਹੋ, ਤਦ ਤੁਹਾਡੇ ਕੋਲ ਵਿਕਲਪ ਹੈ ਕਿ ਵਾਤਾਵਰਣ ਚਲਨਯੋਗਾਂ ਨੂੰ ਇਸ ਰਿਪਾਜ਼ਟਰੀ ਨਾਲ ਜੁੜੇ _Codespaces secrets_ ਵਜੋਂ ਸੁਰੱਖਿਅਤ ਕਰੋ। ਇਸ ਸਥਿਤੀ ਵਿੱਚ, ਤੁਹਾਨੂੰ ਲੋਕਲ `.env` ਫਾਇਲ ਸੈੱਟਅਪ ਕਰਨ ਦੀ ਲੋੜ ਨਹੀਂ ਪਵੇਗੀ। **ਪਰ, ਇਹ ਵਿਕਲਪ ਸਿਰਫ਼ ਤਦ ਹੀ ਕੰਮ ਕਰਦਾ ਹੈ ਜੇ ਤੁਸੀਂ GitHub Codespaces ਵਰਤ ਰਹੇ ਹੋ।** ਜੇ ਤੁਸੀਂ Docker Desktop ਵਰਤਦੇ ਹੋ ਤਾਂ ਤੁਹਾਨੂੰ ਫਿਰ ਵੀ `.env` ਫਾਇਲ ਸੈੱਟਅਪ ਕਰਨੀ ਪਏਗੀ।

## `.env` ਫਾਇਲ ਭਰੋ

ਆਓ ਚੀਜ਼ਾਂ ਨੂੰ ਸਮਝਣ ਲਈ ਵੈਰੀਏਬਲ ਨਾਮਾਂ ਤੇ ਇੱਕ ਨਜ਼ਰ ਮਾਰੀਏ:

| ਵੈਰੀਏਬਲ  | ਵੇਰਵਾ  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | ਇਹ ਉਹ ਯੂਜ਼ਰ ਐਕਸੈਸ ਟੋਕਨ ਹੈ ਜੋ ਤੁਸੀਂ ਆਪਣੇ ਪ੍ਰੋਫਾਈਲ ਵਿੱਚ ਸੈੱਟ ਕੀਤਾ ਹੈ |
| OPENAI_API_KEY | ਇਹ ਉਹ ਪ੍ਰਮਾਣਿਕਤਾ ਕੁੰਜੀ ਹੈ ਜੋ ਗੈਰ-Azure OpenAI ਐਂਡਪੌਇੰਟਾਂ ਲਈ ਵਰਤੀ ਜਾਂਦੀ ਹੈ |
| AZURE_OPENAI_API_KEY | ਇਹ ਉਸ ਸੇਵਾ ਲਈ ਪ੍ਰਮਾਣਿਕਤਾ ਕੁੰਜੀ ਹੈ |
| AZURE_OPENAI_ENDPOINT | ਇਹ ਇੱਕ Azure OpenAI ਸਰੋਤ (resource) ਲਈ ਤੈਅਾਰ ਕੀਤਾ ਹੋਇਆ ਐਂਡਪੌਇੰਟ ਹੈ |
| AZURE_OPENAI_DEPLOYMENT | ਇਹ _ਟੈਕਸਟ ਜੈਨਰੇਸ਼ਨ_ ਮਾਡਲ ਦੇ ਤੈਅਾਰੀ ਦਾ ਐਂਡਪੌਇੰਟ ਹੈ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | ਇਹ _ਟੈਕਸਟ ਐਮਬੈੱਡਿੰਗ_ ਮਾਡਲ ਦੇ ਤੈਅਾਰੀ ਦਾ ਐਂਡਪੌਇੰਟ ਹੈ |
| AZURE_INFERENCE_ENDPOINT | ਇਹ ਤੁਹਾਡੇ Microsoft Foundry ਪ੍ਰੋਜੈਕਟ ਲਈ ਐਂਡਪੌਇੰਟ ਹੈ, ਜੋ Microsoft Foundry ਮਾਡਲਾਂ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ |
| AZURE_INFERENCE_CREDENTIAL | ਇਹ ਤੁਹਾਡੇ Microsoft Foundry ਪ੍ਰੋਜੈਕਟ ਲਈ API ਕੁੰਜੀ ਹੈ |
| | |

ਟਿੱਪਣੀ: ਆਖਰੀ ਦੋ Azure OpenAI ਵੈਰੀਏਬਲਾਂ ਚੈਟ ਪੂਰਨ ਕਰਨ (ਟੈਕਸਟ ਜੈਨਰੇਸ਼ਨ) ਅਤੇ ਵੇਕਟਰ ਸਰਚ (ਐਮਬੈੱਡਿੰਗ) ਲਈ ਇਕ ਡੀਫੋਲਟ ਮਾਡਲ ਨੂੰ ਦਰਸਾਉਂਦੀਆਂ ਹਨ। ਇਹਨਾਂ ਨੂੰ ਸੈੱਟ ਕਰਨ ਲਈ ਹਦਾਇਤਾਂ ਸੰਬੰਧਿਤ ਨਿਯੁਕਤੀਆਂ ਵਿੱਚ ਦਿੱਤੀਆਂ ਜਾਣਗੀਆਂ।

## Azure OpenAI ਸੰਰਚਨਾ: ਪੋਰਟਲ ਤੋਂ

> **ਟਿੱਪਣੀ:** Azure OpenAI ਸੇਵਾ ਹੁਣ [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) ਦਾ ਹਿਸ्सा ਹੈ। ਸਰੋਤ ਅਤੇ ਤੈਅਾਰੀਆਂ ਅਜੇ ਵੀ Azure Portal ਵਿੱਚ ਦਿੱਖਦੀਆਂ ਹਨ, ਪਰ ਰੋਜ਼ਾਨਾ ਮਾਡਲ ਮੈਨੇਜਮੈਂਟ (ਤੈਅਾਰੀਆਂ, ਪਲੇਗ੍ਰਾਊਂਡ, ਨਿਗਰਾਨੀ) ਹੁਣ Foundry ਪੋਰਟਲ ਵਿੱਚ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਪੁਰਾਣੇ ਵੱਖਰੇ "Azure OpenAI Studio" ਦੀ ਥਾਂ।

Azure OpenAI ਐਂਡਪੌਇੰਟ ਅਤੇ ਕੀ ਮੁੱਲ [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) ਵਿੱਚ ਮਿਲਣਗੇ, ਇਸ ਲਈ ਅਸੀਂ ਉਥੋਂ ਸ਼ੁਰੂ ਕਰਦੇ ਹਾਂ।

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) 'ਤੇ ਜਾਓ
1. ਸਾਈਡਬਾਰ (ਖੱਬੇ ਮੀਨੂ) ਵਿੱਚ **Keys and Endpoint** ਵਿਕਲਪ 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
1. **Show Keys** 'ਤੇ ਕਲਿੱਕ ਕਰੋ - ਤੁਹਾਨੂੰ KEY 1, KEY 2 ਅਤੇ Endpoint ਵੇਖਣ ਨੂੰ ਮਿਲੇਗਾ।
1. AZURE_OPENAI_API_KEY ਲਈ KEY 1 ਦੀ ਕੀਮਤ ਵਰਤੋ
1. AZURE_OPENAI_ENDPOINT ਲਈ Endpoint ਦੀ ਕੀਮਤ ਵਰਤੋ

ਹੁਣ, ਸਾਨੂੰ ਤੈਅ ਕੀਤੇ ਮਾਡਲਾਂ ਦੇ ਖਾਸ ਐਂਡਪੌਇੰਟਾਂ ਦੀ ਲੋੜ ਹੈ।

1. Azure OpenAI ਸਰੋਤ ਲਈ ਝਾੜੀ ਵਾਲੇ ਮੀਨੂ ਵਿੱਚ **Model deployments** ਵਿਕਲਪ 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
1. ਗੰਤੀ ਸਫਾ 'ਤੇ, **Go to Microsoft Foundry portal** (ਜਾਂ **Manage Deployments**, ਤੁਹਾਡੇ ਸਰੋਤ ਦੇ ਕਿਸਮ ਅਨੁਸਾਰ) 'ਤੇ ਕਲਿੱਕ ਕਰੋ

ਇਹ ਤੁਹਾਨੂੰ Microsoft Foundry ਪੋਰਟਲ 'ਤੇ ਲੈ ਜਾਵੇਗਾ, ਜਿੱਥੇ ਅਸੀਂ ਹੋਰ ਕੀਮਤਾਂ ਹੇਠਾਂ ਦਿੱਤੇ ਤਰੀਕੇ ਨਾਲ ਲੱਭਾਂਗੇ।

## Azure OpenAI ਸੰਰਚਨਾ: Microsoft Foundry ਪੋਰਟਲ ਤੋਂ

1. [Microsoft Foundry ਪੋਰਟਲ](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) 'ਤੇ ਜਾਓ **ਤੁਹਾਡੇ ਸਰੋਤ ਤੋਂ** ਜਿਵੇਂ ਉਪਰ ਦੱਸਿਆ ਗਿਆ ਹੈ।
1. ਚਾਲੂ ਤੈਅਾਰ ਕੀਤੇ ਮਾਡਲਾਂ ਦੇਖਣ ਲਈ ਸਾਈਡਬਾਰ ਵਿਚੋਂ **Deployments** ਟੈਬ 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
1. ਜੇ ਤੁਹਾਡਾ ਮਨਪਸੰਦ ਮਾਡਲ ਤੈਅਾਰ ਨਹੀਂ ਹੈ, ਤਾਂ [ਮਾਡਲ ਕੈਟਾਲੌਗ](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ਤੋਂ **Deploy model** ਵਰਤ ਕੇ ਤੈਅਾਰ ਕਰੋ।
1. ਤੁਹਾਨੂੰ ਇੱਕ _ਟੈਕਸਟ-ਜੈਨਰੇਸ਼ਨ_ ਮਾਡਲ ਦੀ ਲੋੜ ਪਵੇਗੀ - ਅਸੀਂ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ: **gpt-5-mini**
1. ਤੁਹਾਨੂੰ ਇੱਕ _ਟੈਕਸਟ-ਐਮਬੈੱਡਿੰਗ_ ਮਾਡਲ ਦੀ ਲੋੜ ਪਵੇਗੀ - ਅਸੀਂ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ **text-embedding-3-small**

ਹੁਣ ਵਾਤਾਵਰਣ ਚਲਨਯੋਗਾਂ ਨੂੰ ਅਪਡੇਟ ਕਰੋ ਤਾਂ ਜੋ ਉਹ ਉਪਯੋਗ ਕੀਤਾ ਗਿਆ _Deployment ਨਾਮ_ ਦਰਸਾਉਂਦਾ ਹੋਵੇ। ਆਮ ਤੌਰ ਤੇ ਇਹ ਮਾਡਲ ਦੇ ਨਾਮ ਵਰਗਾ ਹੀ ਹੁੰਦਾ ਹੈ ਜਦੋਂ ਤੱਕ ਤੁਸੀਂ ਇਸ ਨੂੰ ਖਾਸ ਤੌਰ 'ਤੇ ਨਹੀਂ ਬਦਲਦੇ। ਉਦਾਹਰਨ ਵਜੋਂ:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**ਕੰਮ ਮੁਕੰਮਲ ਹੋਣ 'ਤੇ .env ਫਾਇਲ ਨੂੰ ਸੰਭਾਲਣਾ ਨਾ ਭੁੱਲੋ**। ਹੁਣ ਤੁਸੀਂ ਫਾਇਲ ਬੰਦ ਕਰ ਸਕਦੇ ਹੋ ਅਤੇ ਨੋਟਬੁੱਕ ਚਲਾਉਣ ਦੀਆਂ ਹਦਾਇਤਾਂ ਵੱਲ ਮੁੜ ਜਾ ਸਕਦੇ ਹੋ।

## OpenAI ਸੰਰਚਨਾ: ਪ੍ਰੋਫਾਈਲ ਤੋਂ

ਤੁਹਾਡੀ OpenAI API ਕੁੰਜੀ ਤੁਹਾਡੇ [OpenAI ਖਾਤੇ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) ਵਿੱਚ ਮਿਲ ਸਕਦੀ ਹੈ। ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਕੋਈ ਨਹੀਂ, ਤਾਂ ਤੁਸੀਂ ਖਾਤਾ ਬਣਾਕੇ API ਕੁੰਜੀ ਤਿਆਰ ਕਰ ਸਕਦੇ ਹੋ। ਇੱਕ ਵਾਰ ਤੁਹਾਡੇ ਕੋਲ ਕੁੰਜੀ ਹੋਵੇ, ਤਾਂ ਤੁਸੀਂ ਇਸ ਨੂੰ `.env` ਫਾਇਲ ਵਿੱਚ `OPENAI_API_KEY` ਵੈਰੀਏਬਲ ਵਿੱਚ ਭਰ ਸਕਦੇ ਹੋ।

## Hugging Face ਸੰਰਚਨਾ: ਪ੍ਰੋਫਾਈਲ ਤੋਂ

ਤੁਹਾਡਾ Hugging Face ਟੋਕਨ ਤੁਹਾਡੇ ਪ੍ਰੋਫਾਈਲ ਵਿੱਚ [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) ਹਿੱਸੇ ਵਿੱਚ ਮਿਲਦਾ ਹੈ। ਇਹਨਾਂ ਨੂੰ ਜਨਤਕ ਤੌਰ 'ਤੇ ਸ਼ੇਅਰ ਜਾਂ ਪੋਸਟ ਨਾ ਕਰੋ। ਇਸ ਪ੍ਰੋਜੈਕਟ ਦੇ ਲਈ ਇੱਕ ਨਵਾਂ ਟੋਕਨ ਬਣਾਓ ਅਤੇ ਉਸ ਨੂੰ `.env` ਫਾਇਲ ਵਿੱਚ `HUGGING_FACE_API_KEY` ਵੈਰੀਏਬਲ ਹੇਠਾਂ ਭਰੋ। _ਨੋਟ:_ ਇਹ ਤਕਨੀਕੀ ਤੌਰ 'ਤੇ API ਕੁੰਜੀ ਨਹੀਂ ਹੈ ਪਰ ਪ੍ਰਮਾਣਿਕਤਾ ਲਈ ਵਰਤੀ ਜਾਂਦੀ ਹੈ ਇਸ ਲਈ ਅਸੀਂ ਨਾਮ ਰਿਵਾਜ ਨੂੰ ਬਣਾਈ ਰੱਖਿਆ ਹੈ।

## Microsoft Foundry Models ਸੰਰਚਨਾ: ਪੋਰਟਲ ਤੋਂ

> **ਟਿੱਪਣੀ:** GitHub Models ਜੁਲਾਈ 2026 ਦੇ ਅੰਤ ਵਿੱਚ ਰਿਟਾਇਰ ਹੋ ਰਹੇ ਹਨ। Microsoft Foundry Models ਇਸਦਾ ਸਿੱਧਾ ਬਦਲ ਹਨ, ਜੋ ਉਹੀ ਮੁਫ਼ਤ-ਟ੍ਰਾਈ ਮਾਡਲ ਕੈਟਾਲੌਗ ਅਤੇ Azure AI ਇਨਫਰੈਂਸ SDK / OpenAI SDK ਅਨੁਭਵ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

1. [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) 'ਤੇ ਜਾਓ ਅਤੇ ਇੱਕ Foundry ਪ੍ਰੋਜੈਕਟ ਬਣਾਓ ਜਾਂ ਖੋਲ੍ਹੋ।
1. [ਮਾਡਲ ਕੈਟਾਲੌਗ](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ਵਿੱਚੋਂ ਇੱਕ ਮਾਡਲ ਤੈਅਾਰ ਕਰੋ, ਉਦਾਹਰਨ ਵਜੋਂ `gpt-5-mini`।
1. ਪ੍ਰੋਜੈਕਟ ਦੇ **ਓਵਰਵਿਊ** ਪੰਨੇ 'ਤੇ, **ਐਂਡਪੌਇੰਟ** ਅਤੇ **API ਕੁੰਜੀ** ਦੀ ਕਾਪੀ ਲੋ।
1. ਤੁਹਾਡੇ `.env` ਫਾਇਲ ਵਿੱਚ `AZURE_INFERENCE_ENDPOINT` ਲਈ ਐਂਡਪੌਇੰਟ ਦੀ ਕੀਮਤ ਅਤੇ `AZURE_INFERENCE_CREDENTIAL` ਲਈ ਕੁੰਜੀ ਦੀ ਕੀਮਤ ਭਰੋ।

## ਅਫਲਾਈਨ / ਲੋਕਲ ਪ੍ਰਦਾਤਾ

ਜੇ ਤੁਸੀਂ ਬਿਲਕੁਲ ਕਲਾਉਡ ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਇਸਤੇਮਾਲ ਨਾ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਆਪਣੇ ਜੰਤਰ 'ਤੇ ਖੁੱਲ੍ਹੇ ਮਾਡਲਾਂ ਨੂੰ ਚਲਾ ਸਕਦੇ ਹੋ:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - ਮਾਇਕ੍ਰੋਸਾਫਟ ਦਾ ਡਿਵਾਈਸ 'ਤੇ ਚਲਣ ਵਾਲਾ ਰuntime। ਇਹ ਆਪਣੇ ਆਪ ਵਿੱਚ ਸਭ ਤੋਂ ਵਧੀਆ ਪ੍ਰਦਾਨ ਕਰਤਾ (NPU, GPU ਜਾਂ CPU) ਚੁਣਦਾ ਹੈ ਅਤੇ OpenAI-ਅਨੁਕੂਲ ਏਂਡਪੌਇੰਟ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਤਾਂ ਜੋ ਤੁਸੀਂ ਇਸ ਕੋਰਸ ਵਿੱਚ ਸੈਮੀਪਲ ਕੋਡ ਨੂੰ ਗੂੰਜਲਦਾਰ ਤਬਦੀਲੀਆਂ ਨਾਲ ਵਰਤ ਸਕੋ। ਸ਼ੁਰੂ ਕਰਨ ਲਈ [Foundry Local ਡੋਕਯੂਮੈਂਟੇਸ਼ਨ](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) ਵੇਖੋ, ਜਾਂ `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS) ਨਾਲ ਇੰਸਟਾਲ ਕਰੋ।
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - ਖੁੱਲ੍ਹੇ ਮਾਡਲਾਂ ਨੂੰ ਜਿਵੇਂ Llama, Phi, Mistral, ਅਤੇ Gemma ਨੂੰ ਲੋਕਲ ਤੌਰ 'ਤੇ ਚਲਾਉਣ ਲਈ ਪ੍ਰਸਿੱਧ ਵਿਕਲਪ।


ਦੋਹਾਂ ਵਿਕਲਪਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ ਹਥਿਆਰਬੰਦ ਉਦਾਹਰਣਾਂ ਲਈ [ਪਾਠ 19: SLMs ਨਾਲ ਨirmaਾਣ](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) ਵੇਖੋ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->