<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T12:46:10+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "pa"
}
-->
# ਆਪਣੇ ਡੈਵ ਮਾਹੌਲ ਸੈੱਟ ਕਰੋ

ਅਸੀਂ ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਅਤੇ ਕੋਰਸ ਨੂੰ ਇੱਕ [ਵਿਕਾਸ ਕੰਟੇਨਰ](https://containers.dev?WT.mc_id=academic-105485-koreyst) ਨਾਲ ਸੈੱਟ ਕੀਤਾ ਹੈ ਜਿਸ ਵਿੱਚ ਯੂਨੀਵਰਸਲ ਰਨਟਾਈਮ ਹੈ ਜੋ Python3, .NET, Node.js ਅਤੇ Java ਵਿਕਾਸ ਨੂੰ ਸਹਾਇਤਾ ਕਰ ਸਕਦਾ ਹੈ। ਸੰਬੰਧਤ ਸੰਰਚਨਾ `devcontainer.json` ਫਾਇਲ ਵਿੱਚ ਪਰਿਭਾਸ਼ਿਤ ਕੀਤੀ ਗਈ ਹੈ ਜੋ ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਦੇ ਮੂਲ ਵਿੱਚ `.devcontainer/` ਫੋਲਡਰ ਵਿੱਚ ਸਥਿਤ ਹੈ।

ਡੈਵ ਕੰਟੇਨਰ ਨੂੰ ਚਾਲੂ ਕਰਨ ਲਈ, ਇਸਨੂੰ [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (ਕਲਾਉਡ-ਹੋਸਟਿਡ ਰਨਟਾਈਮ ਲਈ) ਜਾਂ [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (ਸਥਾਨਕ ਡਿਵਾਈਸ-ਹੋਸਟਿਡ ਰਨਟਾਈਮ ਲਈ) ਵਿੱਚ ਸ਼ੁਰੂ ਕਰੋ। VS Code ਵਿੱਚ ਡੈਵ ਕੰਟੇਨਰ ਕਿਵੇਂ ਕੰਮ ਕਰਦੇ ਹਨ, ਇਸ ਬਾਰੇ ਹੋਰ ਵਿਸਤਾਰ ਲਈ [ਇਹ ਦਸਤਾਵੇਜ਼](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) ਪੜ੍ਹੋ।

> [!TIP]  
> ਘੱਟ ਕੋਸ਼ਿਸ਼ ਨਾਲ ਤੇਜ਼ ਸ਼ੁਰੂਆਤ ਲਈ GitHub Codespaces ਦੀ ਵਰਤੋਂ ਕਰਨ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਹ ਨਿੱਜੀ ਖਾਤਿਆਂ ਲਈ ਦਿਲਕਸ਼ [ਮੁਫਤ ਵਰਤੋਂ ਕੋਟਾ](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ। ਆਪਣੇ ਕੋਟਾ ਦੀ ਵਰਤੋਂ ਨੂੰ ਵਧਾਉਣ ਲਈ ਗੈਰ-ਸਕ੍ਰਿਆ ਕੋਡਸਪੇਸ ਨੂੰ ਰੋਕਣ ਜਾਂ ਮਿਟਾਉਣ ਲਈ [ਟਾਈਮਆਉਟ](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) ਸੰਰਚਿਤ ਕਰੋ।

## 1. ਅਸਾਈਨਮੈਂਟ ਚਲਾਉਣਾ

ਹਰ ਪਾਠ ਵਿੱਚ _ਵਿਕਲਪਿਕ_ ਅਸਾਈਨਮੈਂਟ ਹੋ ਸਕਦੇ ਹਨ ਜੋ ਇੱਕ ਜਾਂ ਵੱਧ ਪ੍ਰੋਗਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਦਿੱਤੇ ਜਾ ਸਕਦੇ ਹਨ ਜਿਵੇਂ: Python, .NET/C#, Java ਅਤੇ JavaScript/TypeScript। ਇਹ ਭਾਗ ਉਹਨਾਂ ਅਸਾਈਨਮੈਂਟਾਂ ਨੂੰ ਚਲਾਉਣ ਨਾਲ ਸੰਬੰਧਤ ਕੁਝ ਆਮ ਰਾਹਨੁਮਾਈ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

### 1.1 Python ਅਸਾਈਨਮੈਂਟ

Python ਅਸਾਈਨਮੈਂਟ ਜਾਂ ਤਾਂ ਐਪਲੀਕੇਸ਼ਨ (`.py` ਫਾਇਲਾਂ) ਜਾਂ Jupyter ਨੋਟਬੁੱਕ (`.ipynb` ਫਾਇਲਾਂ) ਵਜੋਂ ਪ੍ਰਦਾਨ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।
- ਨੋਟਬੁੱਕ ਚਲਾਉਣ ਲਈ, ਇਸਨੂੰ Visual Studio Code ਵਿੱਚ ਖੋਲ੍ਹੋ ਫਿਰ _Select Kernel_ (ਸਿਖਰ ਉੱਤੇ ਸੱਜੇ) 'ਤੇ ਕਲਿੱਕ ਕਰੋ ਅਤੇ ਦਿਖਾਈ ਗਈ ਮੂਲ Python 3 ਵਿਕਲਪ ਚੁਣੋ। ਹੁਣ ਤੁਸੀਂ ਨੋਟਬੁੱਕ ਚਲਾਉਣ ਲਈ _Run All_ ਕਰ ਸਕਦੇ ਹੋ।
- ਕਮਾਂਡ-ਲਾਈਨ ਤੋਂ Python ਐਪਲੀਕੇਸ਼ਨ ਚਲਾਉਣ ਲਈ, ਸਹੀ ਫਾਇਲਾਂ ਚੁਣਨ ਅਤੇ ਜ਼ਰੂਰੀ ਦਲੀਲਾਂ ਪ੍ਰਦਾਨ ਕਰਨ ਲਈ ਅਸਾਈਨਮੈਂਟ-ਵਿਸ਼ੇਸ਼ ਹਦਾਇਤਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ

## 2. ਪ੍ਰਦਾਤਾ ਸੰਰਚਿਤ ਕਰਨਾ

ਅਸਾਈਨਮੈਂਟ **ਇੱਕ ਜਾਂ ਵੱਧ ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲ (LLM) ਨਿਯੁਕਤੀ** ਵਿਰੁੱਧ ਕੰਮ ਕਰਨ ਲਈ ਸੈੱਟ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ ਜਿਵੇਂ ਕਿ OpenAI, Azure ਜਾਂ Hugging Face ਵਰਗੇ ਸਹਾਇਕ ਸੇਵਾ ਪ੍ਰਦਾਤਾ। ਇਹ ਇੱਕ _ਹੋਸਟਿਡ ਐਂਡਪਾਇੰਟ_ (API) ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ ਜਿਸ ਨੂੰ ਅਸੀਂ ਸਹੀ ਪ੍ਰਮਾਣ ਪੱਤਰ (API ਕੁੰਜੀ ਜਾਂ ਟੋਕਨ) ਨਾਲ ਪ੍ਰੋਗਰਾਮਿੰਗ ਦੁਆਰਾ ਪਹੁੰਚ ਸਕਦੇ ਹਾਂ। ਇਸ ਕੋਰਸ ਵਿੱਚ, ਅਸੀਂ ਇਹਨਾਂ ਪ੍ਰਦਾਤਾਵਾਂ ਬਾਰੇ ਚਰਚਾ ਕਰਦੇ ਹਾਂ:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) ਵਿਸ਼ਾਲ ਮਾਡਲਾਂ ਦੇ ਨਾਲ ਜਿਵੇਂ ਕਿ ਕੋਰ GPT ਸੀਰੀਜ਼।
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) ਕਾਰਪੋਰੇਟ ਤਿਆਰੀ 'ਤੇ ਧਿਆਨ ਨਾਲ OpenAI ਮਾਡਲਾਂ ਲਈ
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) ਖੁੱਲੇ-ਸਰੋਤ ਮਾਡਲਾਂ ਅਤੇ ਇਨਫਰੈਂਸ ਸਰਵਰ ਲਈ

**ਤੁਹਾਨੂੰ ਇਹਨਾਂ ਅਭਿਆਸਾਂ ਲਈ ਆਪਣੇ ਖਾਤਿਆਂ ਦੀ ਵਰਤੋਂ ਕਰਨ ਦੀ ਲੋੜ ਹੋਵੇਗੀ**। ਅਸਾਈਨਮੈਂਟ ਵਿਕਲਪਿਕ ਹਨ ਇਸ ਲਈ ਤੁਸੀਂ ਆਪਣੇ ਰੁਚੀਆਂ ਦੇ ਅਧਾਰ 'ਤੇ ਇੱਕ, ਸਾਰੇ - ਜਾਂ ਕੋਈ - ਪ੍ਰਦਾਤਾ ਸੈੱਟ ਕਰਨ ਦੀ ਚੋਣ ਕਰ ਸਕਦੇ ਹੋ। ਸਾਈਨਅਪ ਲਈ ਕੁਝ ਰਾਹਨੁਮਾਈ:

| ਸਾਈਨਅਪ | ਲਾਗਤ | API ਕੁੰਜੀ | ਖੇਡਦਾਰ | ਟਿੱਪਣੀਆਂ |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [ਮੁੱਲ](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [ਪ੍ਰੋਜੈਕਟ-ਅਧਾਰਿਤ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [ਬਿਨਾ ਕੋਡ, ਵੈੱਬ](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | ਕਈ ਮਾਡਲ ਉਪਲਬਧ ਹਨ |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [ਮੁੱਲ](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [ਪਹੁੰਚ ਲਈ ਪਹਿਲਾਂ ਅਰਜ਼ੀ ਦੇਣੀ ਪੈਂਦੀ ਹੈ](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [ਮੁੱਲ](https://huggingface.co/pricing) | [ਪਹੁੰਚ ਟੋਕਨ](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ਵਿੱਚ ਸੀਮਿਤ ਮਾਡਲ ਹਨ](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

ਹੇਠ ਦਿੱਤੀਆਂ ਹਦਾਇਤਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ ਤਾਂ ਜੋ ਵੱਖ-ਵੱਖ ਪ੍ਰਦਾਤਾਵਾਂ ਦੇ ਨਾਲ ਵਰਤੋਂ ਲਈ ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ _ਸੰਰਚਿਤ_ ਕੀਤਾ ਜਾ ਸਕੇ। ਅਸਾਈਨਮੈਂਟਾਂ ਜੋ ਇੱਕ ਵਿਸ਼ੇਸ਼ ਪ੍ਰਦਾਤਾ ਦੀ ਲੋੜ ਹੈ ਉਹਨਾਂ ਦੇ ਫਾਇਲਨਾਮ ਵਿੱਚ ਇਹਨਾਂ ਟੈਗਾਂ ਵਿੱਚੋਂ ਇੱਕ ਹੋਵੇਗਾ:
- `aoai` - Azure OpenAI ਐਂਡਪਾਇੰਟ, ਕੁੰਜੀ ਦੀ ਲੋੜ ਹੈ
- `oai` - OpenAI ਐਂਡਪਾਇੰਟ, ਕੁੰਜੀ ਦੀ ਲੋੜ ਹੈ
- `hf` - Hugging Face ਟੋਕਨ ਦੀ ਲੋੜ ਹੈ

ਤੁਸੀਂ ਇੱਕ, ਕੋਈ, ਜਾਂ ਸਾਰੇ ਪ੍ਰਦਾਤਾਵਾਂ ਨੂੰ ਸੰਰਚਿਤ ਕਰ ਸਕਦੇ ਹੋ। ਸੰਬੰਧਤ ਅਸਾਈਨਮੈਂਟ ਸਿਰਫ ਗੁੰਮ ਪ੍ਰਮਾਣ ਪੱਤਰਾਂ 'ਤੇ ਗਲਤੀ ਕਰਦੇ ਹਨ।

### 2.1. `.env` ਫਾਇਲ ਬਣਾਓ

ਅਸੀਂ ਮੰਨਦੇ ਹਾਂ ਕਿ ਤੁਸੀਂ ਪਹਿਲਾਂ ਹੀ ਉਪਰੋਕਤ ਰਾਹਨੁਮਾਈ ਪੜ੍ਹੀ ਹੈ ਅਤੇ ਸੰਬੰਧਤ ਪ੍ਰਦਾਤਾ ਨਾਲ ਸਾਈਨਅਪ ਕੀਤਾ ਹੈ, ਅਤੇ ਜ਼ਰੂਰੀ ਪ੍ਰਮਾਣ ਪੱਤਰ (API_KEY ਜਾਂ ਟੋਕਨ) ਪ੍ਰਾਪਤ ਕੀਤੇ ਹਨ। Azure OpenAI ਦੇ ਮਾਮਲੇ ਵਿੱਚ, ਅਸੀਂ ਮੰਨਦੇ ਹਾਂ ਕਿ ਤੁਸੀਂ ਇੱਕ GPT ਮਾਡਲ ਚੈਟ ਪੂਰਨਤਾ ਲਈ ਤੈਨਾਤ ਕਰਕੇ ਇੱਕ Azure OpenAI ਸੇਵਾ (ਐਂਡਪਾਇੰਟ) ਦੀ ਵੈਧ ਨਿਯੁਕਤੀ ਵੀ ਕੀਤੀ ਹੈ।

ਅਗਲਾ ਕਦਮ ਤੁਹਾਡੇ **ਸਥਾਨਕ ਮਾਹੌਲ ਵੈਰੀਏਬਲ** ਨੂੰ ਹੇਠਾਂ ਦਿੱਤੇ ਤਰੀਕੇ ਨਾਲ ਸੰਰਚਿਤ ਕਰਨਾ ਹੈ:

1. ਮੂਲ ਫੋਲਡਰ ਵਿੱਚ ਇੱਕ `.env.copy` ਫਾਇਲ ਲੱਭੋ ਜਿਸਦਾ ਸਮੱਗਰੀ ਇਸ ਤਰ੍ਹਾਂ ਹੋਵੇ:

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

2. ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਸ ਫਾਇਲ ਨੂੰ `.env` ਵਿੱਚ ਕਾਪੀ ਕਰੋ। ਇਹ ਫਾਇਲ _gitignore-d_ ਹੈ, ਰਾਜ਼ਾਂ ਨੂੰ ਸੁਰੱਖਿਅਤ ਰੱਖਦੀ ਹੈ।

   ```bash
   cp .env.copy .env
   ```

3. ਹੇਠਲੇ ਭਾਗ ਵਿੱਚ ਵਰਣਨ ਕੀਤੇ ਗਏ ਤਰੀਕੇ ਨਾਲ ਮੂਲਾਂ ਨੂੰ (ਸੱਜੇ ਪਾਸੇ ਦੇ `=`) ਬਦਲੋ।

3. (ਵਿਕਲਪ) ਜੇ ਤੁਸੀਂ GitHub Codespaces ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋ, ਤਾਂ ਤੁਹਾਡੇ ਕੋਲ ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਨਾਲ ਸੰਬੰਧਿਤ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲਾਂ ਨੂੰ _Codespaces ਰਾਜ਼_ ਵਜੋਂ ਸੁਰੱਖਿਅਤ ਕਰਨ ਦਾ ਵਿਕਲਪ ਹੈ। ਇਸ ਮਾਮਲੇ ਵਿੱਚ, ਤੁਹਾਨੂੰ ਸਥਾਨਕ .env ਫਾਇਲ ਸੈੱਟ ਕਰਨ ਦੀ ਲੋੜ ਨਹੀਂ ਹੋਵੇਗੀ। **ਹਾਲਾਂਕਿ, ਨੋਟ ਕਰੋ ਕਿ ਇਹ ਵਿਕਲਪ ਸਿਰਫ ਜਦੋਂ ਕੰਮ ਕਰਦਾ ਹੈ ਜਦੋਂ ਤੁਸੀਂ GitHub Codespaces ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋ।** ਜੇ ਤੁਸੀਂ Docker Desktop ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋ ਤਾਂ ਤੁਹਾਨੂੰ .env ਫਾਇਲ ਸੈੱਟ ਕਰਨੀ ਪਵੇਗੀ।

### 2.2. `.env` ਫਾਇਲ ਨੂੰ ਭਰੋ

ਚਲੋ ਵੈਰੀਏਬਲਾਂ ਦੇ ਨਾਮਾਂ 'ਤੇ ਇੱਕ ਛੋਟਾ ਜਿਹਾ ਨਜ਼ਰ ਮਾਰਦੇ ਹਾਂ ਤਾਂ ਜੋ ਇਹ ਸਮਝ ਸਕੀਏ ਕਿ ਇਹ ਕੀ ਪ੍ਰਸਤੁਤ ਕਰਦੇ ਹਨ:

| ਵੈਰੀਏਬਲ | ਵਰਣਨ |
| :--- | :--- |
| HUGGING_FACE_API_KEY | ਇਹ ਉਹ ਯੂਜ਼ਰ ਪਹੁੰਚ ਟੋਕਨ ਹੈ ਜੋ ਤੁਸੀਂ ਆਪਣੇ ਪ੍ਰੋਫਾਈਲ ਵਿੱਚ ਸੈੱਟ ਕੀਤਾ ਹੈ |
| OPENAI_API_KEY | ਇਹ ਗੈਰ-Azure OpenAI ਐਂਡਪਾਇੰਟ ਲਈ ਸੇਵਾ ਦੀ ਵਰਤੋਂ ਲਈ ਅਧਿਕਾਰ ਕੁੰਜੀ ਹੈ |
| AZURE_OPENAI_API_KEY | ਇਹ ਸੇਵਾ ਦੀ ਵਰਤੋਂ ਲਈ ਅਧਿਕਾਰ ਕੁੰਜੀ ਹੈ |
| AZURE_OPENAI_ENDPOINT | ਇਹ Azure OpenAI ਸਰੋਤ ਲਈ ਤੈਨਾਤ ਐਂਡਪਾਇੰਟ ਹੈ |
| AZURE_OPENAI_DEPLOYMENT | ਇਹ _ਪਾਠ ਉਤਪਾਦਨ_ ਮਾਡਲ ਤੈਨਾਤ ਐਂਡਪਾਇੰਟ ਹੈ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | ਇਹ _ਪਾਠ ਐਮਬੈਡਿੰਗ_ ਮਾਡਲ ਤੈਨਾਤ ਐਂਡਪਾਇੰਟ ਹੈ |
| | |

ਨੋਟ: ਆਖਰੀ ਦੋ Azure OpenAI ਵੈਰੀਏਬਲ ਚੈਟ ਪੂਰਨਤਾ (ਪਾਠ ਉਤਪਾਦਨ) ਅਤੇ ਵੈਕਟਰ ਖੋਜ (ਐਮਬੈਡਿੰਗ) ਲਈ ਇੱਕ ਮੂਲ ਮਾਡਲ ਨੂੰ ਦਰਸਾਉਂਦੇ ਹਨ। ਉਹਨਾਂ ਨੂੰ ਸੈੱਟ ਕਰਨ ਲਈ ਹਦਾਇਤਾਂ ਸੰਬੰਧਤ ਅਸਾਈਨਮੈਂਟਾਂ ਵਿੱਚ ਪਰਿਭਾਸ਼ਿਤ ਕੀਤੀਆਂ ਜਾਣਗੀਆਂ।

### 2.3 Azure ਸੰਰਚਿਤ ਕਰੋ: ਪੋਰਟਲ ਤੋਂ

Azure OpenAI ਐਂਡਪਾਇੰਟ ਅਤੇ ਕੁੰਜੀ ਮੁੱਲਾਂ [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) ਵਿੱਚ ਲੱਭੇ ਜਾਣਗੇ ਤਾਂ ਆਓ ਸੇਰ ਕਰੀਏ।

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) 'ਤੇ ਜਾਓ
1. ਸਾਈਡਬਾਰ (ਖੱਬੇ ਮੀਨੂ) ਵਿੱਚ **Keys and Endpoint** ਵਿਕਲਪ 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
1. **Show Keys** 'ਤੇ ਕਲਿੱਕ ਕਰੋ - ਤੁਸੀਂ ਇਹ ਦੇਖਣਾ ਚਾਹੀਦਾ ਹੈ: KEY 1, KEY 2 ਅਤੇ Endpoint।
1. AZURE_OPENAI_API_KEY ਲਈ KEY 1 ਮੁੱਲ ਦੀ ਵਰਤੋਂ ਕਰੋ
1. AZURE_OPENAI_ENDPOINT ਲਈ Endpoint ਮੁੱਲ ਦੀ ਵਰਤੋਂ ਕਰੋ

ਅਗਲੇ, ਸਾਨੂੰ ਉਹ ਐਂਡਪਾਇੰਟਾਂ ਦੀ ਲੋੜ ਹੈ ਜੋ ਅਸੀਂ ਤੈਨਾਤ ਕੀਤੇ ਮਾਡਲਾਂ ਲਈ ਹਨ।

1. Azure OpenAI ਸਰੋਤ ਲਈ ਸਾਈਡਬਾਰ (ਖੱਬੇ ਮੀਨੂ) ਵਿੱਚ **Model deployments** ਵਿਕਲਪ 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
1. ਗੰਤਵ ਪੰਨਾ ਵਿੱਚ, **Manage Deployments** 'ਤੇ ਕਲਿੱਕ ਕਰੋ

ਇਹ ਤੁਹਾਨੂੰ Azure OpenAI Studio ਵੈਬਸਾਈਟ 'ਤੇ ਲੈ ਜਾਵੇਗਾ, ਜਿੱਥੇ ਅਸੀਂ ਹੇਠਾਂ ਦਿੱਤੇ ਤਰੀਕੇ ਨਾਲ ਹੋਰ ਮੁੱਲਾਂ ਲੱਭਾਂਗੇ।

### 2.4 Azure ਸੰਰਚਿਤ ਕਰੋ: ਸਟੂਡੀਓ ਤੋਂ

1. [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) 'ਤੇ **ਤੁਹਾਡੇ ਸਰੋਤ** ਤੋਂ ਜਿਵੇਂ ਉਪਰੋਕਤ ਵਰਣਨ ਕੀਤਾ ਗਿਆ ਹੈ, ਜਾਓ।
1. ਇਸ ਸਮੇਂ ਤੈਨਾਤ ਕੀਤੇ ਮਾਡਲਾਂ ਨੂੰ ਦੇਖਣ ਲਈ **Deployments** ਟੈਬ (ਸਾਈਡਬਾਰ, ਖੱਬੇ) 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
1. ਜੇ ਤੁਹਾਡਾ ਚਾਹਵਾਂ ਮਾਡਲ ਤੈਨਾਤ ਨਹੀਂ ਹੈ, **Create new deployment** ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਸਨੂੰ ਤੈਨਾਤ ਕਰੋ।
1. ਤੁਹਾਨੂੰ _ਪਾਠ-ਉਤਪਾਦਨ_ ਮਾਡਲ ਦੀ ਲੋੜ ਹੋਵੇਗੀ - ਅਸੀਂ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ: **gpt-35-turbo**
1. ਤੁਹਾਨੂੰ _ਪਾਠ-ਐਮਬੈਡਿੰਗ_ ਮਾਡਲ ਦੀ ਲੋੜ ਹੋਵੇਗੀ - ਅਸੀਂ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ **text-embedding-ada-002**

ਹੁਣ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲਾਂ ਨੂੰ _ਤੈਨਾਤ ਨਾਮ_ ਵਰਤਿਆ ਗਿਆ ਪ੍ਰਤੀਬਿੰਬਿਤ ਕਰਨ ਲਈ ਅਪਡੇਟ ਕਰੋ। ਇਹ ਆਮ ਤੌਰ 'ਤੇ ਮਾਡਲ ਨਾਮ ਦੇ ਸਮਾਨ ਹੋਵੇਗਾ ਜਦੋਂ ਤੱਕ ਤੁਸੀਂ ਇਸਨੂੰ ਸਪਸ਼ਟ ਤੌਰ 'ਤੇ ਬਦਲਿਆ ਨਹੀਂ ਹੈ। ਇਸ ਲਈ, ਉਦਾਹਰਣ ਵਜੋਂ, ਤੁਹਾਡੇ ਕੋਲ ਹੋ ਸਕਦਾ ਹੈ:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**ਕਿਰਪਾ ਕਰਕੇ .env ਫਾਇਲ ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰਨਾ ਨਾ ਭੁੱਲੋ**। ਤੁਸੀਂ ਹੁਣ ਫਾਇਲ ਨੂੰ ਬੰਦ ਕਰ ਸਕਦੇ ਹੋ ਅਤੇ ਨੋਟਬੁੱਕ ਚਲਾਉਣ ਲਈ ਹਦਾਇਤਾਂ 'ਤੇ ਵਾਪਸ ਜਾ ਸਕਦੇ ਹੋ।

### 2.5 OpenAI ਸੰਰਚਿਤ ਕਰੋ: ਪ੍ਰੋਫਾਈਲ ਤੋਂ

ਤੁਹਾਡੀ OpenAI API ਕੁੰਜੀ ਤੁਹਾਡੇ [OpenAI ਖਾਤੇ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) ਵਿੱਚ ਲੱਭੀ ਜਾ ਸਕਦੀ ਹੈ। ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਨਹੀਂ ਹੈ, ਤੁਸੀਂ ਖਾਤਾ ਸਾਈਨਅਪ ਕਰ ਸਕਦੇ ਹੋ ਅਤੇ API ਕੁੰਜੀ ਤਿਆਰ ਕਰ ਸਕਦੇ ਹੋ। ਜਦੋਂ ਤੁਹਾਡੇ ਕੋਲ ਕੁੰਜੀ ਹੋਵੇ, ਤਾਂ ਤੁਸੀਂ ਇਸਨੂੰ `.env` ਫਾਇਲ ਵਿੱਚ `OPENAI_API_KEY` ਵੈਰੀਏਬਲ ਨੂੰ ਭਰਣ ਲਈ ਵਰਤ ਸਕਦੇ ਹੋ।

### 2.6 Hugging Face ਸੰਰਚਿਤ ਕਰੋ: ਪ੍ਰੋਫਾਈਲ ਤੋਂ

ਤੁਹਾਡਾ Hugging Face ਟੋਕਨ ਤੁਹਾਡੇ ਪ੍ਰੋਫਾਈਲ ਵਿੱਚ [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) ਹੇਠਾਂ ਲੱਭਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਇਹਨਾਂ ਨੂੰ ਜਨਤਕ ਤੌਰ 'ਤੇ ਪੋਸਟ ਜਾਂ

**ਅਸਵੀਕਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚੀਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।