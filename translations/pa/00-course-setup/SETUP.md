<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:27:43+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "pa"
}
-->
# ਆਪਣਾ ਡਿਵੈਲਪਮੈਂਟ ਵਾਤਾਵਰਣ ਸੈੱਟਅਪ ਕਰੋ

ਅਸੀਂ ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਅਤੇ ਕੋਰਸ ਨੂੰ ਇੱਕ [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) ਨਾਲ ਸੈੱਟਅਪ ਕੀਤਾ ਹੈ ਜਿਸ ਵਿੱਚ ਇੱਕ ਯੂਨੀਵਰਸਲ ਰਨਟਾਈਮ ਹੈ ਜੋ Python3, .NET, Node.js ਅਤੇ Java ਡਿਵੈਲਪਮੈਂਟ ਨੂੰ ਸਹਾਰਾ ਦੇ ਸਕਦਾ ਹੈ। ਸੰਬੰਧਿਤ ਕਨਫਿਗਰੇਸ਼ਨ `devcontainer.json` ਫਾਇਲ ਵਿੱਚ ਪਰਿਭਾਸ਼ਿਤ ਹੈ ਜੋ ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਦੀ ਰੂਟ `.devcontainer/` ਫੋਲਡਰ ਵਿੱਚ ਮੌਜੂਦ ਹੈ।

ਡਿਵ ਕੰਟੇਨਰ ਨੂੰ ਐਕਟੀਵੇਟ ਕਰਨ ਲਈ, ਇਸਨੂੰ [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (ਕਲਾਉਡ-ਹੋਸਟਡ ਰਨਟਾਈਮ ਲਈ) ਜਾਂ [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (ਲੋਕਲ ਡਿਵਾਈਸ-ਹੋਸਟਡ ਰਨਟਾਈਮ ਲਈ) ਵਿੱਚ ਲਾਂਚ ਕਰੋ। ਡਿਵ ਕੰਟੇਨਰ VS Code ਵਿੱਚ ਕਿਵੇਂ ਕੰਮ ਕਰਦੇ ਹਨ, ਇਸ ਬਾਰੇ ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ [ਇਸ ਦਸਤਾਵੇਜ਼](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) ਨੂੰ ਪੜ੍ਹੋ।  

> [!TIP]  
> ਅਸੀਂ GitHub Codespaces ਦੀ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ ਤਾਂ ਜੋ ਤੁਸੀਂ ਘੱਟ ਮਿਹਨਤ ਨਾਲ ਤੇਜ਼ੀ ਨਾਲ ਸ਼ੁਰੂਆਤ ਕਰ ਸਕੋ। ਇਹ ਨਿੱਜੀ ਖਾਤਿਆਂ ਲਈ ਇੱਕ ਵੱਡਾ [ਮੁਫ਼ਤ ਵਰਤੋਂ ਕੋਟਾ](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ। ਆਪਣੀ ਕੋਟਾ ਵਰਤੋਂ ਨੂੰ ਵੱਧ ਤੋਂ ਵੱਧ ਕਰਨ ਲਈ ਗੈਰ-ਸਰਗਰਮ codespaces ਨੂੰ ਬੰਦ ਜਾਂ ਮਿਟਾਉਣ ਲਈ [timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) ਸੈੱਟ ਕਰੋ।


## 1. ਅਸਾਈਨਮੈਂਟ ਚਲਾਉਣਾ

ਹਰ ਪਾਠ ਵਿੱਚ _ਵਿਕਲਪਿਕ_ ਅਸਾਈਨਮੈਂਟ ਹੋ ਸਕਦੇ ਹਨ ਜੋ ਇੱਕ ਜਾਂ ਵੱਧ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਦਿੱਤੇ ਜਾ ਸਕਦੇ ਹਨ, ਜਿਵੇਂ ਕਿ: Python, .NET/C#, Java ਅਤੇ JavaScript/TypeScript। ਇਹ ਭਾਗ ਉਹਨਾਂ ਅਸਾਈਨਮੈਂਟਾਂ ਨੂੰ ਚਲਾਉਣ ਲਈ ਆਮ ਮਾਰਗਦਰਸ਼ਨ ਦਿੰਦਾ ਹੈ।

### 1.1 Python ਅਸਾਈਨਮੈਂਟ

Python ਅਸਾਈਨਮੈਂਟ ਜਾਂ ਤਾਂ ਐਪਲੀਕੇਸ਼ਨ (`.py` ਫਾਇਲਾਂ) ਜਾਂ Jupyter ਨੋਟਬੁੱਕ (`.ipynb` ਫਾਇਲਾਂ) ਦੇ ਰੂਪ ਵਿੱਚ ਦਿੱਤੇ ਜਾਂਦੇ ਹਨ।  
- ਨੋਟਬੁੱਕ ਚਲਾਉਣ ਲਈ, ਇਸਨੂੰ Visual Studio Code ਵਿੱਚ ਖੋਲ੍ਹੋ, ਫਿਰ ਉੱਪਰ ਸੱਜੇ ਕੋਨੇ 'ਤੇ _Select Kernel_ 'ਤੇ ਕਲਿੱਕ ਕਰੋ ਅਤੇ ਦਿਖਾਏ ਗਏ ਡਿਫਾਲਟ Python 3 ਵਿਕਲਪ ਨੂੰ ਚੁਣੋ। ਹੁਣ ਤੁਸੀਂ _Run All_ ਕਰਕੇ ਨੋਟਬੁੱਕ ਚਲਾ ਸਕਦੇ ਹੋ।  
- ਕਮਾਂਡ-ਲਾਈਨ ਤੋਂ Python ਐਪਲੀਕੇਸ਼ਨ ਚਲਾਉਣ ਲਈ, ਅਸਾਈਨਮੈਂਟ-ਵਿਸ਼ੇਸ਼ ਹਦਾਇਤਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ ਤਾਂ ਜੋ ਸਹੀ ਫਾਇਲਾਂ ਚੁਣੀਆਂ ਜਾਣ ਅਤੇ ਲੋੜੀਂਦੇ ਆਰਗੁਮੈਂਟ ਦਿੱਤੇ ਜਾਣ।  

## 2. ਪ੍ਰੋਵਾਈਡਰਾਂ ਦੀ ਸੰਰਚਨਾ

ਅਸਾਈਨਮੈਂਟਾਂ ਨੂੰ ਇੱਕ ਜਾਂ ਵੱਧ Large Language Model (LLM) ਡਿਪਲੋਇਮੈਂਟਾਂ ਨਾਲ ਕੰਮ ਕਰਨ ਲਈ ਸੈੱਟਅਪ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ, ਜੋ OpenAI, Azure ਜਾਂ Hugging Face ਵਰਗੇ ਸਹਾਇਕ ਸਰਵਿਸ ਪ੍ਰੋਵਾਈਡਰਾਂ ਰਾਹੀਂ ਹੁੰਦੇ ਹਨ। ਇਹ ਇੱਕ _hosted endpoint_ (API) ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ ਜਿਸਨੂੰ ਅਸੀਂ ਸਹੀ ਪ੍ਰਮਾਣਿਕਤਾ (API key ਜਾਂ ਟੋਕਨ) ਨਾਲ ਪ੍ਰੋਗਰਾਮਿੰਗ ਰੂਪ ਵਿੱਚ ਐਕਸੈਸ ਕਰ ਸਕਦੇ ਹਾਂ। ਇਸ ਕੋਰਸ ਵਿੱਚ ਅਸੀਂ ਇਹ ਪ੍ਰੋਵਾਈਡਰਾਂ ਬਾਰੇ ਗੱਲ ਕਰਦੇ ਹਾਂ:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) ਵੱਖ-ਵੱਖ ਮਾਡਲਾਂ ਸਮੇਤ ਕੋਰ GPT ਸੀਰੀਜ਼ ਨਾਲ।  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) OpenAI ਮਾਡਲਾਂ ਲਈ ਜਿਹੜੇ ਉਦਯੋਗਿਕ ਤਿਆਰੀ 'ਤੇ ਧਿਆਨ ਕੇਂਦ੍ਰਿਤ ਕਰਦੇ ਹਨ।  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) ਖੁੱਲ੍ਹੇ ਸਰੋਤ ਮਾਡਲਾਂ ਅਤੇ ਇਨਫਰੈਂਸ ਸਰਵਰ ਲਈ।  

**ਤੁਹਾਨੂੰ ਇਹਨਾਂ ਅਭਿਆਸਾਂ ਲਈ ਆਪਣੇ ਖਾਤੇ ਦੀ ਲੋੜ ਪਵੇਗੀ**। ਅਸਾਈਨਮੈਂਟ ਵਿਕਲਪਿਕ ਹਨ, ਇਸ ਲਈ ਤੁਸੀਂ ਆਪਣੀ ਰੁਚੀ ਅਨੁਸਾਰ ਇੱਕ, ਸਾਰੇ ਜਾਂ ਕੋਈ ਵੀ ਪ੍ਰੋਵਾਈਡਰ ਸੈੱਟਅਪ ਕਰ ਸਕਦੇ ਹੋ। ਸਾਈਨਅਪ ਲਈ ਕੁਝ ਮਾਰਗਦਰਸ਼ਨ:

| Signup | ਲਾਗਤ | API Key | Playground | ਟਿੱਪਣੀਆਂ |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Pricing](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Project-based](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | ਕਈ ਮਾਡਲ ਉਪਲਬਧ |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [ਪਹੁੰਚ ਲਈ ਪਹਿਲਾਂ ਅਰਜ਼ੀ ਦੇਣੀ ਲਾਜ਼ਮੀ](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Pricing](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat ਵਿੱਚ ਸੀਮਿਤ ਮਾਡਲ ਹਨ](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ ਵੱਖ-ਵੱਖ ਪ੍ਰੋਵਾਈਡਰਾਂ ਨਾਲ ਵਰਤੋਂ ਲਈ _ਕਨਫਿਗਰ_ ਕਰਨ ਲਈ ਹੇਠਾਂ ਦਿੱਤੇ ਨਿਰਦੇਸ਼ਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ। ਜਿਹੜੇ ਅਸਾਈਨਮੈਂਟ ਕਿਸੇ ਖਾਸ ਪ੍ਰੋਵਾਈਡਰ ਦੀ ਲੋੜ ਰੱਖਦੇ ਹਨ, ਉਹਨਾਂ ਦੀ ਫਾਇਲ ਨਾਂ ਵਿੱਚ ਇਹਨਾਂ ਵਿੱਚੋਂ ਇੱਕ ਟੈਗ ਹੋਵੇਗਾ:  
 - `aoai` - Azure OpenAI endpoint, key ਦੀ ਲੋੜ  
 - `oai` - OpenAI endpoint, key ਦੀ ਲੋੜ  
 - `hf` - Hugging Face token ਦੀ ਲੋੜ  

ਤੁਸੀਂ ਇੱਕ, ਕੋਈ ਵੀ ਜਾਂ ਸਾਰੇ ਪ੍ਰੋਵਾਈਡਰ ਕਨਫਿਗਰ ਕਰ ਸਕਦੇ ਹੋ। ਸੰਬੰਧਿਤ ਅਸਾਈਨਮੈਂਟਾਂ ਵਿੱਚ ਜੇ ਪ੍ਰਮਾਣਿਕਤਾ ਨਾ ਹੋਵੇ ਤਾਂ ਸਿਰਫ਼ ਐਰਰ ਆਵੇਗਾ।  

###  2.1. `.env` ਫਾਇਲ ਬਣਾਓ

ਅਸੀਂ ਮੰਨਦੇ ਹਾਂ ਕਿ ਤੁਸੀਂ ਉਪਰ ਦਿੱਤੀ ਮਾਰਗਦਰਸ਼ਨ ਪੜ੍ਹ ਲਈ ਹੈ ਅਤੇ ਸੰਬੰਧਿਤ ਪ੍ਰੋਵਾਈਡਰ ਨਾਲ ਸਾਈਨਅਪ ਕਰਕੇ ਲੋੜੀਂਦੇ ਪ੍ਰਮਾਣਿਕਤਾ (API_KEY ਜਾਂ ਟੋਕਨ) ਪ੍ਰਾਪਤ ਕਰ ਲਈ ਹੈ। Azure OpenAI ਦੇ ਮਾਮਲੇ ਵਿੱਚ, ਅਸੀਂ ਇਹ ਵੀ ਮੰਨਦੇ ਹਾਂ ਕਿ ਤੁਹਾਡੇ ਕੋਲ Azure OpenAI ਸਰਵਿਸ (endpoint) ਦਾ ਇੱਕ ਵੈਧ ਡਿਪਲੋਇਮੈਂਟ ਹੈ ਜਿਸ ਵਿੱਚ ਘੱਟੋ-ਘੱਟ ਇੱਕ GPT ਮਾਡਲ ਚੈਟ ਕੰਪਲੀਸ਼ਨ ਲਈ ਤਿਆਰ ਹੈ।  

ਅਗਲਾ ਕਦਮ ਤੁਹਾਡੇ **ਲੋਕਲ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲਜ਼** ਨੂੰ ਹੇਠਾਂ ਦਿੱਤੇ ਅਨੁਸਾਰ ਕਨਫਿਗਰ ਕਰਨਾ ਹੈ:  

1. ਰੂਟ ਫੋਲਡਰ ਵਿੱਚ `.env.copy` ਫਾਇਲ ਲੱਭੋ ਜਿਸ ਵਿੱਚ ਕੁਝ ਇਸ ਤਰ੍ਹਾਂ ਦਾ ਸਮੱਗਰੀ ਹੋਵੇਗਾ:  

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

2. ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡ ਨਾਲ ਉਸ ਫਾਇਲ ਨੂੰ `.env` ਵਿੱਚ ਕਾਪੀ ਕਰੋ। ਇਹ ਫਾਇਲ _gitignore-d_ ਹੈ, ਜੋ ਸਿਰਲੇਖਾਂ ਨੂੰ ਸੁਰੱਖਿਅਤ ਰੱਖਦੀ ਹੈ।  

   ```bash
   cp .env.copy .env
   ```

3. ਮੁੱਲ ਭਰੋ (ਸੱਜੇ ਪਾਸੇ `=` ਦੇ ਬਾਅਦ ਵਾਲੇ ਪਲੇਸਹੋਲਡਰਾਂ ਨੂੰ ਬਦਲੋ) ਜਿਵੇਂ ਅਗਲੇ ਭਾਗ ਵਿੱਚ ਦਿੱਤਾ ਗਿਆ ਹੈ।  

3. (ਵਿਕਲਪ) ਜੇ ਤੁਸੀਂ GitHub Codespaces ਵਰਤਦੇ ਹੋ, ਤਾਂ ਤੁਹਾਡੇ ਕੋਲ ਇਹ ਵਿਕਲਪ ਹੈ ਕਿ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲਜ਼ ਨੂੰ ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਨਾਲ ਜੁੜੇ _Codespaces secrets_ ਵਜੋਂ ਸੁਰੱਖਿਅਤ ਕੀਤਾ ਜਾਵੇ। ਇਸ ਸਥਿਤੀ ਵਿੱਚ, ਤੁਹਾਨੂੰ ਲੋਕਲ `.env` ਫਾਇਲ ਸੈੱਟਅਪ ਕਰਨ ਦੀ ਲੋੜ ਨਹੀਂ ਪਵੇਗੀ। **ਪਰ ਧਿਆਨ ਰੱਖੋ ਕਿ ਇਹ ਵਿਕਲਪ ਸਿਰਫ਼ GitHub Codespaces ਲਈ ਹੀ ਕੰਮ ਕਰਦਾ ਹੈ।** ਜੇ ਤੁਸੀਂ Docker Desktop ਵਰਤਦੇ ਹੋ ਤਾਂ `.env` ਫਾਇਲ ਸੈੱਟਅਪ ਕਰਨੀ ਪਵੇਗੀ।  

### 2.2. `.env` ਫਾਇਲ ਭਰੋ

ਆਓ ਵੈਰੀਏਬਲ ਨਾਂਵਾਂ ਤੇ ਇੱਕ ਨਜ਼ਰ ਮਾਰੀਏ ਤਾਂ ਜੋ ਸਮਝ ਆ ਸਕੇ ਕਿ ਇਹ ਕੀ ਦਰਸਾਉਂਦੇ ਹਨ:  

| ਵੈਰੀਏਬਲ  | ਵੇਰਵਾ  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | ਇਹ ਉਹ ਯੂਜ਼ਰ ਐਕਸੈਸ ਟੋਕਨ ਹੈ ਜੋ ਤੁਸੀਂ ਆਪਣੇ ਪ੍ਰੋਫਾਈਲ ਵਿੱਚ ਸੈੱਟ ਕੀਤਾ ਹੈ |  
| OPENAI_API_KEY | ਇਹ ਸੇਵਾ ਨੂੰ ਵਰਤਣ ਲਈ ਅਧਿਕਾਰਿਤ ਕੁੰਜੀ ਹੈ ਜੋ ਨਾਨ-Azure OpenAI endpoints ਲਈ ਹੈ |  
| AZURE_OPENAI_API_KEY | ਇਹ ਉਸ ਸੇਵਾ ਲਈ ਅਧਿਕਾਰਿਤ ਕੁੰਜੀ ਹੈ |  
| AZURE_OPENAI_ENDPOINT | ਇਹ Azure OpenAI ਸਰੋਤ ਲਈ ਡਿਪਲੋਇਡ ਐਂਡਪੌਇੰਟ ਹੈ |  
| AZURE_OPENAI_DEPLOYMENT | ਇਹ _ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ_ ਮਾਡਲ ਡਿਪਲੋਇਮੈਂਟ ਐਂਡਪੌਇੰਟ ਹੈ |  
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | ਇਹ _ਟੈਕਸਟ ਐਮਬੈਡਿੰਗ_ ਮਾਡਲ ਡਿਪਲੋਇਮੈਂਟ ਐਂਡਪੌਇੰਟ ਹੈ |  
| | |  

ਨੋਟ: ਆਖਰੀ ਦੋ Azure OpenAI ਵੈਰੀਏਬਲਜ਼ ਡਿਫਾਲਟ ਮਾਡਲ ਨੂੰ ਦਰਸਾਉਂਦੇ ਹਨ ਜੋ ਚੈਟ ਕੰਪਲੀਸ਼ਨ (ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ) ਅਤੇ ਵੈਕਟਰ ਖੋਜ (ਐਮਬੈਡਿੰਗ) ਲਈ ਵਰਤੇ ਜਾਂਦੇ ਹਨ। ਇਹਨਾਂ ਨੂੰ ਸੈੱਟ ਕਰਨ ਲਈ ਹਦਾਇਤਾਂ ਸੰਬੰਧਿਤ ਅਸਾਈਨਮੈਂਟਾਂ ਵਿੱਚ ਦਿੱਤੀਆਂ ਜਾਣਗੀਆਂ।  

### 2.3 Azure ਕਨਫਿਗਰ ਕਰੋ: ਪੋਰਟਲ ਤੋਂ

Azure OpenAI ਐਂਡਪੌਇੰਟ ਅਤੇ ਕੁੰਜੀ ਦੀਆਂ ਕੀਮਤਾਂ [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) ਵਿੱਚ ਮਿਲਣਗੀਆਂ, ਤਾਂ ਆਓ ਉੱਥੋਂ ਸ਼ੁਰੂ ਕਰੀਏ।  

1. [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) 'ਤੇ ਜਾਓ  
1. ਸਾਈਡਬਾਰ (ਖੱਬੇ ਮੀਨੂ) ਵਿੱਚ **Keys and Endpoint** ਵਿਕਲਪ 'ਤੇ ਕਲਿੱਕ ਕਰੋ।  
1. **Show Keys** 'ਤੇ ਕਲਿੱਕ ਕਰੋ - ਤੁਹਾਨੂੰ KEY 1, KEY 2 ਅਤੇ Endpoint ਵੇਖਣ ਨੂੰ ਮਿਲੇਗਾ।  
1. AZURE_OPENAI_API_KEY ਲਈ KEY 1 ਦੀ ਕੀਮਤ ਵਰਤੋਂ।  
1. AZURE_OPENAI_ENDPOINT ਲਈ Endpoint ਦੀ ਕੀਮਤ ਵਰਤੋਂ।  

ਹੁਣ ਸਾਨੂੰ ਉਹ ਐਂਡਪੌਇੰਟ ਚਾਹੀਦੇ ਹਨ ਜੋ ਅਸੀਂ ਖਾਸ ਮਾਡਲਾਂ ਲਈ ਡਿਪਲੋਇ ਕੀਤੇ ਹਨ।  

1. Azure OpenAI ਸਰੋਤ ਲਈ ਸਾਈਡਬਾਰ ਵਿੱਚ **Model deployments** ਵਿਕਲਪ 'ਤੇ ਕਲਿੱਕ ਕਰੋ।  
1. ਮੰਜ਼ਿਲ ਪੰਨਾ 'ਤੇ **Manage Deployments** 'ਤੇ ਕਲਿੱਕ ਕਰੋ।  

ਇਹ ਤੁਹਾਨੂੰ Azure OpenAI Studio ਵੈੱਬਸਾਈਟ 'ਤੇ ਲੈ ਜਾਵੇਗਾ, ਜਿੱਥੇ ਅਸੀਂ ਹੋਰ ਕੀਮਤਾਂ ਲੱਭਾਂਗੇ।  

### 2.4 Azure ਕਨਫਿਗਰ ਕਰੋ: ਸਟੂਡੀਓ ਤੋਂ

1. ਉਪਰ ਦਿੱਤੇ ਤਰੀਕੇ ਨਾਲ ਆਪਣੇ ਸਰੋਤ ਤੋਂ [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) 'ਤੇ ਜਾਓ।  
1. ਮੌਜੂਦਾ ਡਿਪਲੋਇ ਕੀਤੇ ਮਾਡਲਾਂ ਨੂੰ ਵੇਖਣ ਲਈ ਸਾਈਡਬਾਰ (ਖੱਬਾ) ਵਿੱਚ **Deployments** ਟੈਬ 'ਤੇ ਕਲਿੱਕ ਕਰੋ।  
1. ਜੇ ਤੁਹਾਡਾ ਚਾਹੀਦਾ ਮਾਡਲ ਡਿਪਲੋਇ ਨਹੀਂ ਹੈ, ਤਾਂ **Create new deployment** ਨਾਲ ਨਵਾਂ ਡਿਪਲੋਇ ਕਰੋ।  
1. ਤੁਹਾਨੂੰ ਇੱਕ _text-generation_ ਮਾਡਲ ਦੀ ਲੋੜ ਹੋਵੇਗੀ - ਅਸੀਂ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ: **gpt-35-turbo**  
1. ਤੁਹਾਨੂੰ ਇੱਕ _text-embedding_ ਮਾਡਲ ਦੀ ਲੋੜ ਹੋਵੇਗੀ - ਅਸੀਂ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ: **text-embedding-ada-002**  

ਹੁਣ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲਜ਼ ਨੂੰ ਅਪਡੇਟ ਕਰੋ ਤਾਂ ਜੋ ਉਹ _Deployment name_ ਨੂੰ ਦਰਸਾਉਣ, ਜੋ ਆਮ ਤੌਰ 'ਤੇ ਮਾਡਲ ਦੇ ਨਾਮ ਦੇ ਬਰਾਬਰ ਹੁੰਦਾ ਹੈ ਜੇਕਰ ਤੁਸੀਂ ਇਸਨੂੰ ਖਾਸ ਤੌਰ 'ਤੇ ਬਦਲਿਆ ਨਾ ਹੋਵੇ। ਉਦਾਹਰਨ ਵਜੋਂ, ਤੁਸੀਂ ਇਹ ਹੋ ਸਕਦਾ ਹੈ:  

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**ਜਦੋਂ ਕੰਮ ਮੁਕੰਮਲ ਹੋ ਜਾਵੇ ਤਾਂ .env ਫਾਇਲ ਸੇਵ ਕਰਨਾ ਨਾ ਭੁੱਲੋ**। ਹੁਣ ਤੁਸੀਂ ਫਾਇਲ ਬੰਦ ਕਰਕੇ ਨੋਟਬੁੱਕ ਚਲਾਉਣ ਲਈ ਹਦਾਇਤਾਂ ਵੱਲ ਵਾਪਸ ਜਾ ਸਕਦੇ ਹੋ।  

### 2.5 OpenAI ਕਨਫਿਗਰ ਕਰੋ: ਪ੍ਰੋਫਾਈਲ ਤੋਂ

ਤੁਹਾਡੀ OpenAI API ਕੁੰਜੀ ਤੁਹਾਡੇ [OpenAI ਖਾਤੇ](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) ਵਿੱਚ ਮਿਲੇਗੀ। ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਨਹੀਂ ਹੈ, ਤਾਂ ਤੁਸੀਂ ਖਾਤਾ ਬਣਾਕੇ API ਕੁੰਜੀ ਤਿਆਰ ਕਰ ਸਕਦੇ ਹੋ। ਕੁੰਜੀ ਮਿਲਣ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਇਸਨੂੰ `.env` ਫਾਇਲ ਵਿੱਚ `OPENAI_API_KEY` ਵੈਰੀਏਬਲ ਵਿੱਚ ਭਰ ਸਕਦੇ ਹੋ।  

### 2.6 Hugging Face ਕਨਫਿਗਰ ਕਰੋ: ਪ੍ਰੋਫਾਈਲ ਤੋਂ

ਤੁਹਾਡਾ Hugging Face ਟੋਕਨ ਤੁਹਾਡੇ ਪ੍ਰੋਫਾਈਲ ਵਿੱਚ [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) ਹਿੱਸੇ ਵਿੱਚ ਮਿਲੇਗਾ। ਇਹਨਾਂ ਨੂੰ ਜਨਤਕ ਤੌਰ 'ਤੇ ਨਾ ਪੋਸਟ ਕਰੋ ਜਾਂ ਸਾਂਝਾ ਨਾ ਕਰੋ। ਇਸ ਪ੍ਰੋਜੈਕਟ ਲਈ ਇੱਕ ਨਵਾਂ ਟੋਕਨ ਬਣਾਓ ਅਤੇ ਉਸਨੂੰ `.env` ਫਾਇਲ ਵਿੱਚ `HUGGING_FACE_API_KEY` ਵੈਰੀਏਬਲ ਵਿੱਚ ਕਾਪੀ ਕਰੋ। _ਨੋਟ:_ ਇਹ ਤਕਨੀਕੀ ਤੌਰ 'ਤੇ API ਕੁੰਜੀ

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।