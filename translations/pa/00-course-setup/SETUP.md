<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:15:19+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "pa"
}
-->
# ਆਪਣਾ ਡਿਵੈਲਪਮੈਂਟ ਵਾਤਾਵਰਣ ਸੈਟਅਪ ਕਰੋ

ਅਸੀਂ ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਅਤੇ ਕੋਰਸ ਨੂੰ ਇੱਕ [ਡਿਵੈਲਪਮੈਂਟ ਕੰਟੇਨਰ](https://containers.dev?WT.mc_id=academic-105485-koreyst) ਨਾਲ ਸੈਟਅਪ ਕੀਤਾ ਹੈ ਜਿਸ ਵਿੱਚ ਇੱਕ ਯੂਨੀਵਰਸਲ ਰਨਟਾਈਮ ਹੈ ਜੋ Python3, .NET, Node.js ਅਤੇ Java ਵਿਕਾਸ ਨੂੰ ਸਹਾਇਤਾ ਦੇ ਸਕਦਾ ਹੈ। ਸਬੰਧਤ ਕਨਫਿਗਰੇਸ਼ਨ ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਦੇ ਰੂਟ 'ਤੇ `.devcontainer/` ਫੋਲਡਰ ਵਿੱਚ ਸਥਿਤ `devcontainer.json` ਫਾਈਲ ਵਿੱਚ ਪਰਿਭਾਸ਼ਿਤ ਹੈ।

ਡਿਵੈਲਪਮੈਂਟ ਕੰਟੇਨਰ ਨੂੰ ਸਰਗਰਮ ਕਰਨ ਲਈ, ਇਸਨੂੰ [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) ਵਿੱਚ ਲਾਂਚ ਕਰੋ (ਕਲਾਉਡ-ਹੋਸਟ ਕੀਤੇ ਰਨਟਾਈਮ ਲਈ) ਜਾਂ [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) ਵਿੱਚ (ਲੋਕਲ ਡਿਵਾਈਸ-ਹੋਸਟ ਕੀਤੇ ਰਨਟਾਈਮ ਲਈ)। ਡਿਵੈਲਪਮੈਂਟ ਕੰਟੇਨਰਾਂ ਦੇ VS Code ਵਿੱਚ ਕਿਵੇਂ ਕੰਮ ਕਰਦੇ ਹਨ, ਇਸ ਬਾਰੇ ਹੋਰ ਵਿਸਥਾਰ ਲਈ [ਇਹ ਦਸਤਾਵੇਜ਼](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) ਪੜ੍ਹੋ।

> [!TIP]  
> ਘੱਟ ਕੋਸ਼ਿਸ਼ ਨਾਲ ਤੇਜ਼ ਸ਼ੁਰੂਆਤ ਲਈ ਅਸੀਂ GitHub Codespaces ਦੀ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ। ਇਹ ਨਿੱਜੀ ਖਾਤਿਆਂ ਲਈ ਇੱਕ ਬਹੁਤ ਹੀ [ਮੁਫ਼ਤ ਵਰਤੋਂ ਕੋਟਾ](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ। ਆਪਣੇ ਕੋਟੇ ਦੀ ਵਰਤੋਂ ਨੂੰ ਵਧਾਓਣ ਲਈ ਨਿਸ਼ਕ੍ਰਿਯ ਕੋਡਸਪੇਸ ਨੂੰ ਰੋਕਣ ਜਾਂ ਹਟਾਉਣ ਲਈ [ਟਾਈਮਆਊਟ](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) ਕਨਫਿਗਰ ਕਰੋ।

## 1. ਅਸਾਈਨਮੈਂਟ ਚਲਾਉਣਾ

ਹਰ ਪਾਠ ਵਿੱਚ _ਵਿਕਲਪਿਕ_ ਅਸਾਈਨਮੈਂਟ ਹੋ ਸਕਦੇ ਹਨ ਜੋ ਇੱਕ ਜਾਂ ਇੱਕ ਤੋਂ ਵੱਧ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਦਿੱਤੇ ਜਾ ਸਕਦੇ ਹਨ ਜਿਵੇਂ ਕਿ: Python, .NET/C#, Java ਅਤੇ JavaScript/TypeScript। ਇਹ ਭਾਗ ਉਹ ਅਸਾਈਨਮੈਂਟ ਚਲਾਉਣ ਦੇ ਸੰਬੰਧ ਵਿੱਚ ਆਮ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

### 1.1 ਪਾਈਥਨ ਅਸਾਈਨਮੈਂਟ

ਪਾਈਥਨ ਅਸਾਈਨਮੈਂਟ ਜਾਂ ਤਾਂ ਐਪਲੀਕੇਸ਼ਨ (`.py` ਫਾਈਲਾਂ) ਜਾਂ Jupyter ਨੋਟਬੁੱਕ (`.ipynb` ਫਾਈਲਾਂ) ਦੇ ਰੂਪ ਵਿੱਚ ਪ੍ਰਦਾਨ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।
- ਨੋਟਬੁੱਕ ਚਲਾਉਣ ਲਈ, ਇਸਨੂੰ Visual Studio Code ਵਿੱਚ ਖੋਲ੍ਹੋ ਫਿਰ _Select Kernel_ (ਉਪਰਲੇ ਸੱਜੇ ਕੋਨੇ ਵਿੱਚ) 'ਤੇ ਕਲਿਕ ਕਰੋ ਅਤੇ ਦਿਖਾਈ ਦੇ ਰਹੇ ਡਿਫਾਲਟ Python 3 ਵਿਕਲਪ ਨੂੰ ਚੁਣੋ। ਹੁਣ ਤੁਸੀਂ ਨੋਟਬੁੱਕ ਚਲਾਉਣ ਲਈ _Run All_ ਕਰ ਸਕਦੇ ਹੋ।
- ਕਮਾਂਡ-ਲਾਈਨ ਤੋਂ ਪਾਈਥਨ ਐਪਲੀਕੇਸ਼ਨ ਚਲਾਉਣ ਲਈ, ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਅਸਾਈਨਮੈਂਟ-ਵਿਸ਼ੇਸ਼ ਨਿਰਦੇਸ਼ਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ ਕਿ ਤੁਸੀਂ ਸਹੀ ਫਾਈਲਾਂ ਚੁਣਦੇ ਹੋ ਅਤੇ ਲੋੜੀਂਦੇ ਤਰਕ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹੋ।

## 2. ਪ੍ਰੋਵਾਈਡਰ ਸੈਟਅਪ ਕਰਨਾ

ਅਸਾਈਨਮੈਂਟ ਇੱਕ ਜਾਂ ਇੱਕ ਤੋਂ ਵੱਧ ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲ (LLM) ਡਿਪਲੋਇਮੈਂਟ ਦੇ ਖਿਲਾਫ ਕੰਮ ਕਰਨ ਲਈ ਸਹਾਇਕ ਸੇਵਾ ਪ੍ਰਦਾਤਾ ਜਿਵੇਂ ਕਿ OpenAI, Azure ਜਾਂ Hugging Face ਰਾਹੀਂ ਸੈਟਅਪ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ। ਇਹ ਇੱਕ _ਹੋਸਟ ਕੀਤੇ ਐਂਡਪੌਇੰਟ_ (API) ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ ਜਿਸ ਨੂੰ ਅਸੀਂ ਸਹੀ ਪ੍ਰਮਾਣ ਪੱਤਰਾਂ (API ਕੁੰਜੀ ਜਾਂ ਟੋਕਨ) ਨਾਲ ਪ੍ਰੋਗਰਾਮੈਟਿਕ ਤੌਰ 'ਤੇ ਐਕਸੈਸ ਕਰ ਸਕਦੇ ਹਾਂ। ਇਸ ਕੋਰਸ ਵਿੱਚ, ਅਸੀਂ ਇਹ ਪ੍ਰਦਾਤਾ ਚਰਚਾ ਕਰਦੇ ਹਾਂ:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) ਵੱਖ-ਵੱਖ ਮਾਡਲਾਂ ਨਾਲ, ਜਿਸ ਵਿੱਚ ਮੁੱਖ GPT ਸੀਰੀਜ਼ ਸ਼ਾਮਲ ਹੈ।
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI ਮਾਡਲਾਂ ਲਈ, ਜਿਸ ਵਿੱਚ ਉਦਯੋਗ ਤਿਆਰੀ 'ਤੇ ਧਿਆਨ ਦਿੱਤਾ ਗਿਆ ਹੈ।
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) ਖੁੱਲ੍ਹੇ-ਸਰੋਤ ਮਾਡਲਾਂ ਅਤੇ ਅਨੁਮਾਨ ਸਰਵਰ ਲਈ।

**ਤੁਹਾਨੂੰ ਇਨ੍ਹਾਂ ਅਭਿਆਸਾਂ ਲਈ ਆਪਣੇ ਖਾਤਿਆਂ ਦੀ ਵਰਤੋਂ ਕਰਨ ਦੀ ਲੋੜ ਹੋਵੇਗੀ**। ਅਸਾਈਨਮੈਂਟ ਵਿਕਲਪਿਕ ਹਨ ਇਸ ਲਈ ਤੁਸੀਂ ਆਪਣੀਆਂ ਰੁਚੀਆਂ ਦੇ ਅਧਾਰ 'ਤੇ ਇੱਕ, ਸਾਰੇ - ਜਾਂ ਕੋਈ ਵੀ ਪ੍ਰਦਾਤਾ ਸੈਟਅਪ ਕਰ ਸਕਦੇ ਹੋ। ਸਾਈਨਅਪ ਲਈ ਕੁਝ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼:

| ਸਾਈਨਅਪ | ਲਾਗਤ | API ਕੁੰਜੀ | ਖੇਡ ਦਾ ਮੈਦਾਨ | ਟਿੱਪਣੀਆਂ |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [ਕੀਮਤ](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [ਪ੍ਰੋਜੈਕਟ-ਅਧਾਰਿਤ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [ਕੋਡ-ਰਹਿਤ, ਵੈੱਬ](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | ਕਈ ਮਾਡਲ ਉਪਲਬਧ ਹਨ |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [ਕੀਮਤ](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK ਕਵਿਕਸਟਾਰਟ](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [ਸਟੂਡੀਓ ਕਵਿਕਸਟਾਰਟ](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [ਪਹੁੰਚ ਲਈ ਅੱਗੇ ਤੋਂ ਅਰਜ਼ੀ ਦੇਣੀ ਪਵੇਗੀ](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [ਕੀਮਤ](https://huggingface.co/pricing) | [ਐਕਸੈਸ ਟੋਕਨ](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ਵਿੱਚ ਸੀਮਤ ਮਾਡਲ ਹਨ](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼ਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ ਤਾਂ ਜੋ ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ ਵੱਖ-ਵੱਖ ਪ੍ਰਦਾਤਾਵਾਂ ਨਾਲ ਵਰਤੋਂ ਲਈ _ਸੈਟਅਪ_ ਕੀਤਾ ਜਾ ਸਕੇ। ਅਸਾਈਨਮੈਂਟ ਜੋ ਕਿਸੇ ਵਿਸ਼ੇਸ਼ ਪ੍ਰਦਾਤਾ ਦੀ ਲੋੜ ਹੋਵੇਗੀ ਉਹਨਾਂ ਦੇ ਫਾਈਲਨਾਮ ਵਿੱਚ ਇਨ੍ਹਾਂ ਟੈਗਾਂ ਵਿੱਚੋਂ ਇੱਕ ਸ਼ਾਮਲ ਹੋਵੇਗਾ:
 - `aoai` - Azure OpenAI ਐਂਡਪੌਇੰਟ, ਕੁੰਜੀ ਦੀ ਲੋੜ ਹੈ
 - `oai` - OpenAI ਐਂਡਪੌਇੰਟ, ਕੁੰਜੀ ਦੀ ਲੋੜ ਹੈ
 - `hf` - Hugging Face ਟੋਕਨ ਦੀ ਲੋੜ ਹੈ

ਤੁਸੀਂ ਇੱਕ, ਕੋਈ ਵੀ, ਜਾਂ ਸਾਰੇ ਪ੍ਰਦਾਤਾ ਕਨਫਿਗਰ ਕਰ ਸਕਦੇ ਹੋ। ਸਬੰਧਤ ਅਸਾਈਨਮੈਂਟ ਸਿਰਫ ਗੁੰਝਲਦਾਰ ਪ੍ਰਮਾਣ ਪੱਤਰਾਂ 'ਤੇ ਗਲਤੀ ਕਰ ਜਾਣਗੇ।

### 2.1. `.env` ਫਾਈਲ ਬਣਾਓ

ਅਸੀਂ ਧਾਰਨਾ ਕਰਦੇ ਹਾਂ ਕਿ ਤੁਸੀਂ ਪਹਿਲਾਂ ਹੀ ਉਪਰ ਦਿੱਤੇ ਨਿਰਦੇਸ਼ਾਂ ਨੂੰ ਪੜ੍ਹ ਲਿਆ ਹੈ ਅਤੇ ਸੰਬੰਧਤ ਪ੍ਰਦਾਤਾ ਨਾਲ ਸਾਈਨਅਪ ਕਰ ਲਿਆ ਹੈ, ਅਤੇ ਲੋੜੀਂਦੇ ਪ੍ਰਮਾਣ ਪੱਤਰ (API_KEY ਜਾਂ ਟੋਕਨ) ਪ੍ਰਾਪਤ ਕਰ ਲਿਆ ਹੈ। Azure OpenAI ਦੇ ਮਾਮਲੇ ਵਿੱਚ, ਅਸੀਂ ਇਹ ਵੀ ਧਾਰਨਾ ਕਰਦੇ ਹਾਂ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਚੈਟ ਪੂਰਨਤਾ ਲਈ ਘੱਟੋ-ਘੱਟ ਇੱਕ GPT ਮਾਡਲ ਨਾਲ ਇੱਕ ਵੈਧ ਡਿਪਲੋਇਮੈਂਟ ਹੈ।

ਅਗਲਾ ਕਦਮ ਤੁਹਾਡੇ **ਲੋਕਲ ਵਾਤਾਵਰਣ ਵਰੀਏਬਲਾਂ** ਨੂੰ ਹੇਠ ਲਿਖੇ ਤਰੀਕੇ ਨਾਲ ਕਨਫਿਗਰ ਕਰਨਾ ਹੈ:

1. ਰੂਟ ਫੋਲਡਰ ਵਿੱਚ ਇੱਕ `.env.copy` ਫਾਈਲ ਦੇਖੋ ਜਿਸ ਵਿੱਚ ਇਸ ਤਰ੍ਹਾਂ ਦੀ ਸਮੱਗਰੀ ਹੋਵੇਗੀ:

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

2. ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਸ ਫਾਈਲ ਨੂੰ `.env` ਵਿੱਚ ਕਾਪੀ ਕਰੋ। ਇਹ ਫਾਈਲ _gitignore-d_ ਹੈ, ਜੋ ਰਾਜ਼ਾਂ ਨੂੰ ਸੁਰੱਖਿਅਤ ਰੱਖਦੀ ਹੈ।

   ```bash
   cp .env.copy .env
   ```

3. ਅਗਲੇ ਭਾਗ ਵਿੱਚ ਵਰਣਨ ਕੀਤੇ ਤੌਰ 'ਤੇ ਮੁੱਲ ਭਰੋ (ਸੱਜੇ ਪਾਸੇ `=` 'ਤੇ ਪਲੇਸਹੋਲਡਰਾਂ ਨੂੰ ਬਦਲੋ)।

3. (ਵਿਕਲਪ) ਜੇ ਤੁਸੀਂ GitHub Codespaces ਵਰਤਦੇ ਹੋ, ਤਾਂ ਤੁਹਾਡੇ ਕੋਲ ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਨਾਲ ਸੰਬੰਧਿਤ ਵਾਤਾਵਰਣ ਵਰੀਏਬਲਾਂ ਨੂੰ _Codespaces ਰਾਜ਼_ ਦੇ ਤੌਰ ਤੇ ਸੇਵ ਕਰਨ ਦਾ ਵਿਕਲਪ ਹੈ। ਇਸ ਮਾਮਲੇ ਵਿੱਚ, ਤੁਹਾਨੂੰ ਇੱਕ ਸਥਾਨਕ .env ਫਾਈਲ ਸੈਟਅਪ ਕਰਨ ਦੀ ਲੋੜ ਨਹੀਂ ਹੋਵੇਗੀ। **ਹਾਲਾਂਕਿ, ਧਿਆਨ ਰੱਖੋ ਕਿ ਇਹ ਵਿਕਲਪ ਸਿਰਫ ਉਸੇ ਸਮੇਂ ਕੰਮ ਕਰਦਾ ਹੈ ਜਦੋਂ ਤੁਸੀਂ GitHub Codespaces ਵਰਤਦੇ ਹੋ।** ਜੇ ਤੁਸੀਂ Docker Desktop ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋ ਤਾਂ ਵੀ ਤੁਹਾਨੂੰ .env ਫਾਈਲ ਸੈਟਅਪ ਕਰਨ ਦੀ ਲੋੜ ਹੋਵੇਗੀ।

### 2.2. `.env` ਫਾਈਲ ਭਰੋ

ਆਓ ਅਸੀਂ ਵਰੀਏਬਲ ਨਾਵਾਂ ਨੂੰ ਸਮਝਣ ਲਈ ਇੱਕ ਝਲਕ ਮਾਰਦੇ ਹਾਂ ਕਿ ਉਹ ਕੀ ਦਰਸਾਉਂਦੇ ਹਨ:

| ਵਰੀਏਬਲ | ਵਰਣਨ |
| :--- | :--- |
| HUGGING_FACE_API_KEY | ਇਹ ਉਹ ਯੂਜ਼ਰ ਐਕਸੈਸ ਟੋਕਨ ਹੈ ਜੋ ਤੁਸੀਂ ਆਪਣੇ ਪ੍ਰੋਫਾਈਲ ਵਿੱਚ ਸੈਟਅਪ ਕੀਤਾ ਹੈ |
| OPENAI_API_KEY | ਇਹ ਸੇਵਾ ਦੀ ਵਰਤੋਂ ਲਈ ਅਧਿਕਾਰ ਕੁੰਜੀ ਹੈ ਜੋ ਕਿ ਨਾਨ-Azure OpenAI ਐਂਡਪੌਇੰਟ ਲਈ ਹੈ |
| AZURE_OPENAI_API_KEY | ਇਹ ਸੇਵਾ ਦੀ ਵਰਤੋਂ ਲਈ ਅਧਿਕਾਰ ਕੁੰਜੀ ਹੈ |
| AZURE_OPENAI_ENDPOINT | ਇਹ ਇੱਕ Azure OpenAI ਸਰੋਤ ਲਈ ਡਿਪਲੋਇਡ ਐਂਡਪੌਇੰਟ ਹੈ |
| AZURE_OPENAI_DEPLOYMENT | ਇਹ _ਪਾਠ ਉਤਪਾਦਨ_ ਮਾਡਲ ਡਿਪਲੋਇਮੈਂਟ ਐਂਡਪੌਇੰਟ ਹੈ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | ਇਹ _ਪਾਠ ਇੰਬੈਡਿੰਗ_ ਮਾਡਲ ਡਿਪਲੋਇਮੈਂਟ ਐਂਡਪੌਇੰਟ ਹੈ |
| | |

ਨੋਟ: ਆਖਰੀ ਦੋ Azure OpenAI ਵਰੀਏਬਲ ਚੈਟ ਪੂਰਨਤਾ (ਪਾਠ ਉਤਪਾਦਨ) ਅਤੇ ਵੇਕਟਰ ਖੋਜ (ਇੰਬੈਡਿੰਗ) ਲਈ ਇੱਕ ਡਿਫਾਲਟ ਮਾਡਲ ਦਰਸਾਉਂਦੇ ਹਨ। ਉਨ੍ਹਾਂ ਨੂੰ ਸੈਟ ਕਰਨ ਲਈ ਨਿਰਦੇਸ਼ ਸਬੰਧਤ ਅਸਾਈਨਮੈਂਟ ਵਿੱਚ ਪਰਿਭਾਸ਼ਿਤ ਕੀਤੇ ਜਾਣਗੇ।

### 2.3 ਅਜ਼ੂਰ ਕਨਫਿਗਰ ਕਰੋ: ਪੋਰਟਲ ਤੋਂ

Azure OpenAI ਐਂਡਪੌਇੰਟ ਅਤੇ ਕੁੰਜੀ ਮੁੱਲ [Azure ਪੋਰਟਲ](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) ਵਿੱਚ ਮਿਲਣਗੇ, ਇਸ ਲਈ ਆਓ ਉੱਥੇ ਸ਼ੁਰੂ ਕਰੀਏ।

1. [Azure ਪੋਰਟਲ](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) 'ਤੇ ਜਾਓ
1. ਸਾਈਡਬਾਰ (ਖੱਬੇ ਮੀਨੂ) ਵਿੱਚ **ਕੁੰਜੀਆਂ ਅਤੇ ਐਂਡਪੌਇੰਟ** ਵਿਕਲਪ 'ਤੇ ਕਲਿਕ ਕਰੋ।
1. **ਕੁੰਜੀਆਂ ਦਿਖਾਓ** 'ਤੇ ਕਲਿਕ ਕਰੋ - ਤੁਹਾਨੂੰ ਇਹਨਾਂ ਨੂੰ ਵੇਖਣਾ ਚਾਹੀਦਾ ਹੈ: KEY 1, KEY 2 ਅਤੇ ਐਂਡਪੌਇੰਟ।
1. AZURE_OPENAI_API_KEY ਲਈ KEY 1 ਮੁੱਲ ਦੀ ਵਰਤੋਂ ਕਰੋ
1. AZURE_OPENAI_ENDPOINT ਲਈ ਐਂਡਪੌਇੰਟ ਮੁੱਲ ਦੀ ਵਰਤੋਂ ਕਰੋ

ਅਗਲਾ, ਸਾਨੂੰ ਉਹ ਐਂਡਪੌਇੰਟ ਲੋੜੀਂਦੇ ਹਨ ਜੋ ਅਸੀਂ ਤਹਿ ਕੀਤੇ ਮਾਡਲਾਂ ਲਈ ਹਨ।

1. Azure OpenAI ਸਰੋਤ ਲਈ ਸਾਈਡਬਾਰ (ਖੱਬੇ ਮੀਨੂ) ਵਿੱਚ **ਮਾਡਲ ਡਿਪਲੋਇਮੈਂਟਸ** ਵਿਕਲਪ 'ਤੇ ਕਲਿਕ ਕਰੋ।
1. ਗੰਤੀ ਦੇ ਪੰਨੇ 'ਤੇ, **ਡਿਪਲੋਇਮੈਂਟਸ ਪ੍ਰਬੰਧਿਤ ਕਰੋ** 'ਤੇ ਕਲਿਕ ਕਰੋ

ਇਹ ਤੁਹਾਨੂੰ Azure OpenAI Studio ਵੈਬਸਾਈਟ 'ਤੇ ਲੈ ਜਾਵੇਗਾ, ਜਿੱਥੇ ਅਸੀਂ ਹੇਠਾਂ ਦਿੱਤੇ ਮੁੱਲਾਂ ਨੂੰ ਲੱਭਾਂਗੇ।

### 2.4 ਅਜ਼ੂਰ ਕਨਫਿਗਰ ਕਰੋ: ਸਟੂਡੀਓ ਤੋਂ

1. [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) 'ਤੇ ਜਾਓ **ਆਪਣੇ ਸਰੋਤ ਤੋਂ** ਜਿਵੇਂ ਉਪਰ ਦਿੱਤਾ ਗਿਆ ਹੈ।
1. ਵਰਤਮਾਨ ਡਿਪਲੋਇਡ ਮਾਡਲਾਂ ਨੂੰ ਵੇਖਣ ਲਈ **ਡਿਪਲੋਇਮੈਂਟਸ** ਟੈਬ (ਸਾਈਡਬਾਰ, ਖੱਬੇ) 'ਤੇ ਕਲਿਕ ਕਰੋ।
1. ਜੇਕਰ ਤੁਹਾਡਾ ਲੋੜੀਂਦਾ ਮਾਡਲ ਡਿਪਲੋਇਡ ਨਹੀਂ ਹੈ, ਤਾਂ ਇਸਨੂੰ ਡਿਪਲੋਇ ਕਰਨ ਲਈ **ਨਵਾਂ ਡਿਪਲੋਇਮੈਂਟ ਬਣਾਓ** ਦੀ ਵਰਤੋਂ ਕਰੋ।
1. ਤੁਹਾਨੂੰ ਇੱਕ _ਪਾਠ-ਉਤਪਾਦਨ_ ਮਾਡਲ ਦੀ ਲੋੜ ਹੋਵੇਗੀ - ਅਸੀਂ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ: **gpt-35-turbo**
1. ਤੁਹਾਨੂੰ ਇੱਕ _ਪਾਠ-ਇੰਬੈਡਿੰਗ_ ਮਾਡਲ ਦੀ ਲੋੜ ਹੋਵੇਗੀ - ਅਸੀਂ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ **text-embedding-ada-002**

ਹੁਣ ਵਾਤਾਵਰਣ ਵਰੀਏਬਲਾਂ ਨੂੰ _ਡਿਪਲੋਇਮੈਂਟ ਨਾਮ_ ਨੂੰ ਦਰਸਾਉਣ ਲਈ ਅਪਡੇਟ ਕਰੋ। ਇਹ ਆਮ ਤੌਰ 'ਤੇ ਮਾਡਲ ਦੇ ਨਾਮ ਦੇ ਬਰਾਬਰ ਹੋਵੇਗਾ ਜਦੋਂ ਤੱਕ ਤੁਸੀਂ ਇਸਨੂੰ ਸਪਸ਼ਟ ਤੌਰ 'ਤੇ ਨਹੀਂ ਬਦਲਿਆ। ਇਸ ਲਈ, ਉਦਾਹਰਣ ਵਜੋਂ, ਤੁਹਾਡੇ ਕੋਲ ਹੋ ਸਕਦਾ ਹੈ:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**ਜਦੋਂ ਹੋ ਜਾਵੇ ਤਾਂ .env ਫਾਈਲ ਨੂੰ ਸੇਵ ਕਰਨਾ ਨਾ ਭੁੱਲੋ**। ਹੁਣ ਤੁਸੀਂ ਫਾਈਲ ਨੂੰ ਬੰਦ ਕਰ ਸਕਦੇ ਹੋ ਅਤੇ ਨੋਟਬੁੱਕ ਚਲਾਉਣ ਦੇ ਨਿਰਦੇਸ਼ਾਂ 'ਤੇ ਵਾਪਸ ਜਾ ਸਕਦੇ ਹੋ।

### 2.5 OpenAI ਕਨਫਿਗਰ ਕਰੋ: ਪ੍ਰੋਫਾਈਲ ਤੋਂ

ਤੁਹਾਡੀ OpenAI API ਕੁੰਜੀ

**ਅਸਵੀਕਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਪਜਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤ ਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।