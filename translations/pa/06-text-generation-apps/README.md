<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ce8224073b86b728ed52b19bed7932fd",
  "translation_date": "2025-07-09T11:53:59+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "pa"
}
-->
# ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣਾ

[![Building Text Generation Applications](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.pa.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(ਇਸ ਪਾਠ ਦਾ ਵੀਡੀਓ ਦੇਖਣ ਲਈ ਉਪਰ ਦਿੱਤੀ ਤਸਵੀਰ 'ਤੇ ਕਲਿੱਕ ਕਰੋ)_

ਤੁਸੀਂ ਇਸ ਕਰੀਕੁਲਮ ਵਿੱਚ ਹੁਣ ਤੱਕ ਦੇਖਿਆ ਹੈ ਕਿ ਕੁਝ ਮੁੱਖ ਧਾਰਣਾਵਾਂ ਹਨ ਜਿਵੇਂ ਕਿ prompts ਅਤੇ ਇੱਕ ਪੂਰਾ ਵਿਸ਼ਾ "prompt engineering" ਵੀ ਹੈ। ਬਹੁਤ ਸਾਰੇ ਟੂਲ ਜਿਵੇਂ ChatGPT, Office 365, Microsoft Power Platform ਆਦਿ ਤੁਹਾਨੂੰ prompts ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੁਝ ਹਾਸਲ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦੇ ਹਨ।

ਤੁਹਾਨੂੰ ਆਪਣੀ ਐਪ ਵਿੱਚ ਇਹ ਤਜਰਬਾ ਸ਼ਾਮਲ ਕਰਨ ਲਈ prompts, completions ਵਰਗੀਆਂ ਧਾਰਣਾਵਾਂ ਨੂੰ ਸਮਝਣਾ ਪੈਂਦਾ ਹੈ ਅਤੇ ਕੰਮ ਕਰਨ ਲਈ ਕੋਈ ਲਾਇਬ੍ਰੇਰੀ ਚੁਣਨੀ ਪੈਂਦੀ ਹੈ। ਇਹੀ ਤੁਸੀਂ ਇਸ ਅਧਿਆਇ ਵਿੱਚ ਸਿੱਖੋਗੇ।

## ਪਰਿਚਯ

ਇਸ ਅਧਿਆਇ ਵਿੱਚ, ਤੁਸੀਂ:

- openai ਲਾਇਬ੍ਰੇਰੀ ਅਤੇ ਇਸ ਦੀਆਂ ਮੁੱਖ ਧਾਰਣਾਵਾਂ ਬਾਰੇ ਜਾਣੋਗੇ।
- openai ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਬਣਾਉਗੇ।
- ਸਮਝੋਗੇ ਕਿ prompt, temperature, ਅਤੇ tokens ਵਰਗੀਆਂ ਧਾਰਣਾਵਾਂ ਨੂੰ ਕਿਵੇਂ ਵਰਤ ਕੇ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਬਣਾਈ ਜਾਂਦੀ ਹੈ।

## ਸਿੱਖਣ ਦੇ ਲਕੜੇ

ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਵਿੱਚ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- ਸਮਝਾਉਣ ਲਈ ਕਿ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਕੀ ਹੁੰਦੀ ਹੈ।
- openai ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਬਣਾਉਣ ਲਈ।
- ਆਪਣੀ ਐਪ ਨੂੰ ਵੱਧ ਜਾਂ ਘੱਟ tokens ਵਰਤਣ ਲਈ ਅਤੇ temperature ਬਦਲਣ ਲਈ ਕਨਫਿਗਰ ਕਰਨ ਲਈ, ਤਾਂ ਜੋ ਨਤੀਜਾ ਵੱਖਰਾ ਹੋਵੇ।

## ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਕੀ ਹੁੰਦੀ ਹੈ?

ਆਮ ਤੌਰ 'ਤੇ ਜਦੋਂ ਤੁਸੀਂ ਕੋਈ ਐਪ ਬਣਾਉਂਦੇ ਹੋ ਤਾਂ ਇਸਦਾ ਕੋਈ ਇੰਟਰਫੇਸ ਹੁੰਦਾ ਹੈ ਜਿਵੇਂ:

- ਕਮਾਂਡ-ਆਧਾਰਿਤ। ਕਨਸੋਲ ਐਪ ਉਹ ਹੁੰਦੇ ਹਨ ਜਿੱਥੇ ਤੁਸੀਂ ਕਮਾਂਡ ਲਿਖਦੇ ਹੋ ਅਤੇ ਇਹ ਕੰਮ ਕਰਦਾ ਹੈ। ਉਦਾਹਰਨ ਵਜੋਂ, `git` ਇੱਕ ਕਮਾਂਡ-ਆਧਾਰਿਤ ਐਪ ਹੈ।
- ਯੂਜ਼ਰ ਇੰਟਰਫੇਸ (UI)। ਕੁਝ ਐਪ ਗ੍ਰਾਫਿਕਲ ਯੂਜ਼ਰ ਇੰਟਰਫੇਸ (GUIs) ਵਾਲੇ ਹੁੰਦੇ ਹਨ ਜਿੱਥੇ ਤੁਸੀਂ ਬਟਨ ਕਲਿੱਕ ਕਰਦੇ ਹੋ, ਟੈਕਸਟ ਦਾਖਲ ਕਰਦੇ ਹੋ, ਵਿਕਲਪ ਚੁਣਦੇ ਹੋ ਆਦਿ।

### ਕਨਸੋਲ ਅਤੇ UI ਐਪ ਸੀਮਿਤ ਹੁੰਦੇ ਹਨ

ਇਸਨੂੰ ਇੱਕ ਕਮਾਂਡ-ਆਧਾਰਿਤ ਐਪ ਨਾਲ ਤੁਲਨਾ ਕਰੋ ਜਿੱਥੇ ਤੁਸੀਂ ਕਮਾਂਡ ਲਿਖਦੇ ਹੋ:

- **ਇਹ ਸੀਮਿਤ ਹੈ**। ਤੁਸੀਂ ਕੋਈ ਵੀ ਕਮਾਂਡ ਨਹੀਂ ਲਿਖ ਸਕਦੇ, ਸਿਰਫ ਉਹ ਜੋ ਐਪ ਸਹਾਇਤਾ ਕਰਦਾ ਹੈ।
- **ਭਾਸ਼ਾ-ਵਿਸ਼ੇਸ਼**। ਕੁਝ ਐਪ ਕਈ ਭਾਸ਼ਾਵਾਂ ਸਹਾਇਤਾ ਕਰਦੇ ਹਨ, ਪਰ ਡਿਫਾਲਟ ਤੌਰ 'ਤੇ ਇਹ ਕਿਸੇ ਖਾਸ ਭਾਸ਼ਾ ਲਈ ਬਣੇ ਹੁੰਦੇ ਹਨ, ਭਾਵੇਂ ਤੁਸੀਂ ਹੋਰ ਭਾਸ਼ਾਵਾਂ ਸ਼ਾਮਲ ਕਰ ਸਕਦੇ ਹੋ।

### ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਦੇ ਫਾਇਦੇ

ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਕਿਵੇਂ ਵੱਖਰਾ ਹੈ?

ਇਸ ਵਿੱਚ ਤੁਹਾਡੇ ਕੋਲ ਵੱਧ ਲਚਕੀਲਾਪਣ ਹੁੰਦਾ ਹੈ, ਤੁਸੀਂ ਕਿਸੇ ਨਿਰਧਾਰਿਤ ਕਮਾਂਡ ਜਾਂ ਖਾਸ ਇਨਪੁੱਟ ਭਾਸ਼ਾ ਤੱਕ ਸੀਮਿਤ ਨਹੀਂ ਹੋ। ਇਸਦੀ ਬਜਾਏ, ਤੁਸੀਂ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਐਪ ਨਾਲ ਗੱਲਬਾਤ ਕਰ ਸਕਦੇ ਹੋ। ਇੱਕ ਹੋਰ ਫਾਇਦਾ ਇਹ ਹੈ ਕਿ ਤੁਸੀਂ ਪਹਿਲਾਂ ਹੀ ਇੱਕ ਡਾਟਾ ਸਰੋਤ ਨਾਲ ਗੱਲਬਾਤ ਕਰ ਰਹੇ ਹੋ ਜੋ ਵੱਡੇ ਪੱਧਰ 'ਤੇ ਜਾਣਕਾਰੀ 'ਤੇ ਟ੍ਰੇਨ ਕੀਤਾ ਗਿਆ ਹੈ, ਜਦਕਿ ਰਵਾਇਤੀ ਐਪ ਡਾਟਾਬੇਸ ਵਿੱਚ ਮੌਜੂਦ ਜਾਣਕਾਰੀ ਤੱਕ ਸੀਮਿਤ ਹੋ ਸਕਦਾ ਹੈ।

### ਮੈਂ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਨਾਲ ਕੀ ਬਣਾਉਂ ਸਕਦਾ ਹਾਂ?

ਤੁਸੀਂ ਬਹੁਤ ਕੁਝ ਬਣਾਉਂ ਸਕਦੇ ਹੋ। ਉਦਾਹਰਨ ਵਜੋਂ:

- **ਚੈਟਬੋਟ**। ਇੱਕ ਚੈਟਬੋਟ ਜੋ ਤੁਹਾਡੇ ਕੰਪਨੀ ਅਤੇ ਇਸਦੇ ਉਤਪਾਦਾਂ ਬਾਰੇ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਦਿੰਦਾ ਹੋਵੇ, ਵਧੀਆ ਰਹੇਗਾ।
- **ਮਦਦਗਾਰ**। LLMs ਟੈਕਸਟ ਦਾ ਸਾਰ ਬਣਾਉਣ, ਟੈਕਸਟ ਤੋਂ ਜਾਣਕਾਰੀ ਲੈਣ, ਰੇਜ਼ਿਊਮੇ ਵਰਗਾ ਟੈਕਸਟ ਬਣਾਉਣ ਵਿੱਚ ਬਹੁਤ ਵਧੀਆ ਹਨ।
- **ਕੋਡ ਸਹਾਇਕ**। ਤੁਸੀਂ ਵਰਤ ਰਹੇ ਭਾਸ਼ਾ ਮਾਡਲ ਦੇ ਅਨੁਸਾਰ, ਇੱਕ ਕੋਡ ਸਹਾਇਕ ਬਣਾਉਂ ਸਕਦੇ ਹੋ ਜੋ ਤੁਹਾਡੀ ਕੋਡ ਲਿਖਣ ਵਿੱਚ ਮਦਦ ਕਰੇ। ਉਦਾਹਰਨ ਵਜੋਂ, ਤੁਸੀਂ GitHub Copilot ਜਾਂ ChatGPT ਵਰਗੇ ਉਤਪਾਦਾਂ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ।

## ਮੈਂ ਕਿਵੇਂ ਸ਼ੁਰੂ ਕਰ ਸਕਦਾ ਹਾਂ?

ਤੁਹਾਨੂੰ LLM ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕਰਨ ਦਾ ਤਰੀਕਾ ਲੱਭਣਾ ਪੈਂਦਾ ਹੈ ਜੋ ਆਮ ਤੌਰ 'ਤੇ ਦੋ ਤਰੀਕਿਆਂ ਵਿੱਚੋਂ ਇੱਕ ਹੁੰਦਾ ਹੈ:

- API ਦੀ ਵਰਤੋਂ ਕਰੋ। ਇੱਥੇ ਤੁਸੀਂ ਆਪਣੇ prompt ਨਾਲ ਵੈੱਬ ਰਿਕਵੇਸਟ ਬਣਾਉਂਦੇ ਹੋ ਅਤੇ ਜਨਰੇਟ ਕੀਤਾ ਟੈਕਸਟ ਪ੍ਰਾਪਤ ਕਰਦੇ ਹੋ।
- ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਵਰਤੋਂ ਕਰੋ। ਲਾਇਬ੍ਰੇਰੀਆਂ API ਕਾਲਾਂ ਨੂੰ ਕੈਪਸੂਲੇਟ ਕਰਦੀਆਂ ਹਨ ਅਤੇ ਵਰਤੋਂ ਨੂੰ ਆਸਾਨ ਬਣਾਉਂਦੀਆਂ ਹਨ।

## ਲਾਇਬ੍ਰੇਰੀਆਂ/SDKs

LLMs ਨਾਲ ਕੰਮ ਕਰਨ ਲਈ ਕੁਝ ਪ੍ਰਸਿੱਧ ਲਾਇਬ੍ਰੇਰੀਆਂ ਹਨ ਜਿਵੇਂ:

- **openai**, ਇਹ ਲਾਇਬ੍ਰੇਰੀ ਤੁਹਾਡੇ ਮਾਡਲ ਨਾਲ ਜੁੜਨ ਅਤੇ prompts ਭੇਜਣ ਨੂੰ ਆਸਾਨ ਬਣਾਉਂਦੀ ਹੈ।

ਫਿਰ ਕੁਝ ਉੱਚ ਸਤਰ ਦੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਹਨ ਜਿਵੇਂ:

- **Langchain**। Langchain ਪ੍ਰਸਿੱਧ ਹੈ ਅਤੇ Python ਨੂੰ ਸਹਾਇਤਾ ਦਿੰਦਾ ਹੈ।
- **Semantic Kernel**। Semantic Kernel ਮਾਈਕ੍ਰੋਸਾਫਟ ਦੀ ਲਾਇਬ੍ਰੇਰੀ ਹੈ ਜੋ C#, Python, ਅਤੇ Java ਭਾਸ਼ਾਵਾਂ ਨੂੰ ਸਹਾਇਤਾ ਦਿੰਦੀ ਹੈ।

## openai ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪਹਿਲੀ ਐਪ

ਆਓ ਵੇਖੀਏ ਕਿ ਅਸੀਂ ਆਪਣੀ ਪਹਿਲੀ ਐਪ ਕਿਵੇਂ ਬਣਾਈਏ, ਕਿਹੜੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਦੀ ਲੋੜ ਹੈ, ਕਿੰਨਾ ਕੁ ਲੋੜੀਂਦਾ ਹੈ ਆਦਿ।

### openai ਇੰਸਟਾਲ ਕਰੋ

OpenAI ਜਾਂ Azure OpenAI ਨਾਲ ਇੰਟਰੈਕਟ ਕਰਨ ਲਈ ਬਹੁਤ ਸਾਰੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਹਨ। ਤੁਸੀਂ ਕਈ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ ਵਰਤ ਸਕਦੇ ਹੋ ਜਿਵੇਂ C#, Python, JavaScript, Java ਆਦਿ। ਅਸੀਂ `openai` Python ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਚੋਣ ਕੀਤੀ ਹੈ, ਇਸ ਲਈ ਅਸੀਂ `pip` ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਸਨੂੰ ਇੰਸਟਾਲ ਕਰਾਂਗੇ।

```bash
pip install openai
```

### ਇੱਕ ਰਿਸੋਰਸ ਬਣਾਓ

ਤੁਹਾਨੂੰ ਹੇਠਾਂ ਦਿੱਤੇ ਕਦਮ ਕਰਨੇ ਪੈਣਗੇ:

- Azure 'ਤੇ ਇੱਕ ਖਾਤਾ ਬਣਾਓ [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)।
- Azure OpenAI ਤੱਕ ਪਹੁੰਚ ਪ੍ਰਾਪਤ ਕਰੋ। ਜਾਓ [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) ਅਤੇ ਪਹੁੰਚ ਲਈ ਅਰਜ਼ੀ ਦਿਓ।

  > [!NOTE]
  > ਲਿਖਣ ਦੇ ਸਮੇਂ, ਤੁਹਾਨੂੰ Azure OpenAI ਲਈ ਪਹੁੰਚ ਲਈ ਅਰਜ਼ੀ ਦੇਣੀ ਪੈਂਦੀ ਹੈ।

- Python ਇੰਸਟਾਲ ਕਰੋ <https://www.python.org/>
- ਇੱਕ Azure OpenAI Service ਰਿਸੋਰਸ ਬਣਾਇਆ ਹੋਇਆ ਹੋਵੇ। ਇਸ ਗਾਈਡ ਨੂੰ ਵੇਖੋ ਕਿ ਕਿਵੇਂ [ਰਿਸੋਰਸ ਬਣਾਇਆ ਜਾਂਦਾ ਹੈ](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)।

### API ਕੀ ਅਤੇ endpoint ਲੱਭੋ

ਹੁਣ ਤੁਹਾਨੂੰ ਆਪਣੀ `openai` ਲਾਇਬ੍ਰੇਰੀ ਨੂੰ ਦੱਸਣਾ ਹੈ ਕਿ ਕਿਹੜੀ API ਕੀ ਵਰਤਣੀ ਹੈ। ਆਪਣੀ API ਕੀ ਲੱਭਣ ਲਈ, ਆਪਣੇ Azure OpenAI ਰਿਸੋਰਸ ਦੇ "Keys and Endpoint" ਸੈਕਸ਼ਨ ਵਿੱਚ ਜਾਓ ਅਤੇ "Key 1" ਦੀ ਕਾਪੀ ਕਰੋ।

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

ਹੁਣ ਜਦੋਂ ਤੁਹਾਡੇ ਕੋਲ ਇਹ ਜਾਣਕਾਰੀ ਹੈ, ਆਓ ਲਾਇਬ੍ਰੇਰੀਆਂ ਨੂੰ ਇਸਦੀ ਵਰਤੋਂ ਕਰਨ ਲਈ ਦੱਸਦੇ ਹਾਂ।

> [!NOTE]
> ਆਪਣੀ API ਕੀ ਨੂੰ ਕੋਡ ਤੋਂ ਵੱਖਰਾ ਰੱਖਣਾ ਚੰਗਾ ਹੁੰਦਾ ਹੈ। ਤੁਸੀਂ ਇਹ environment variables ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕਰ ਸਕਦੇ ਹੋ।
>
> - environment variable `OPENAI_API_KEY` ਨੂੰ ਆਪਣੀ API ਕੀ 'ਤੇ ਸੈੱਟ ਕਰੋ।
>   `export OPENAI_API_KEY='sk-...'`

### Azure ਲਈ ਕਨਫਿਗਰੇਸ਼ਨ ਸੈੱਟ ਕਰੋ

ਜੇ ਤੁਸੀਂ Azure OpenAI ਵਰਤ ਰਹੇ ਹੋ, ਤਾਂ ਕਨਫਿਗਰੇਸ਼ਨ ਸੈੱਟ ਕਰਨ ਦਾ ਤਰੀਕਾ ਇਹ ਹੈ:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

ਉਪਰ ਅਸੀਂ ਇਹ ਸੈੱਟ ਕਰ ਰਹੇ ਹਾਂ:

- `api_type` ਨੂੰ `azure`। ਇਹ ਲਾਇਬ੍ਰੇਰੀ ਨੂੰ ਦੱਸਦਾ ਹੈ ਕਿ Azure OpenAI ਵਰਤੋ, ਨਾ ਕਿ OpenAI।
- `api_key`, ਇਹ ਤੁਹਾਡੀ Azure Portal ਵਿੱਚ ਮਿਲੀ API ਕੀ ਹੈ।
- `api_version`, ਇਹ API ਦਾ ਵਰਜਨ ਹੈ ਜੋ ਤੁਸੀਂ ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹੋ। ਲਿਖਣ ਦੇ ਸਮੇਂ, ਸਭ ਤੋਂ ਨਵਾਂ ਵਰਜਨ `2023-05-15` ਹੈ।
- `api_base`, ਇਹ API ਦਾ endpoint ਹੈ। ਤੁਸੀਂ ਇਸਨੂੰ Azure Portal ਵਿੱਚ ਆਪਣੀ API ਕੀ ਦੇ ਨਾਲ ਲੱਭ ਸਕਦੇ ਹੋ।

> [!NOTE]
> `os.getenv` ਇੱਕ ਫੰਕਸ਼ਨ ਹੈ ਜੋ environment variables ਨੂੰ ਪੜ੍ਹਦਾ ਹੈ। ਤੁਸੀਂ ਇਸਨੂੰ ਵਰਤ ਕੇ environment variables ਜਿਵੇਂ `OPENAI_API_KEY` ਅਤੇ `API_BASE` ਪੜ੍ਹ ਸਕਦੇ ਹੋ। ਇਹ environment variables ਆਪਣੇ ਟਰਮੀਨਲ ਵਿੱਚ ਜਾਂ `dotenv` ਵਰਗੀ ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸੈੱਟ ਕਰੋ।

## ਟੈਕਸਟ ਜਨਰੇਟ ਕਰੋ

ਟੈਕਸਟ ਜਨਰੇਟ ਕਰਨ ਦਾ ਤਰੀਕਾ `Completion` ਕਲਾਸ ਦੀ ਵਰਤੋਂ ਕਰਨਾ ਹੈ। ਇੱਥੇ ਇੱਕ ਉਦਾਹਰਨ ਹੈ:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ, ਅਸੀਂ ਇੱਕ completion ਆਬਜੈਕਟ ਬਣਾਇਆ ਅਤੇ ਮਾਡਲ ਅਤੇ prompt ਦਿੱਤਾ। ਫਿਰ ਅਸੀਂ ਜਨਰੇਟ ਕੀਤਾ ਟੈਕਸਟ ਪ੍ਰਿੰਟ ਕੀਤਾ।

### ਚੈਟ ਕਮਪਲੀਸ਼ਨ

ਹੁਣ ਤੱਕ, ਤੁਸੀਂ ਦੇਖਿਆ ਕਿ ਅਸੀਂ `Completion` ਵਰਤ ਕੇ ਟੈਕਸਟ ਜਨਰੇਟ ਕਰ ਰਹੇ ਹਾਂ। ਪਰ ਇੱਕ ਹੋਰ ਕਲਾਸ ਹੈ `ChatCompletion` ਜੋ ਚੈਟਬੋਟ ਲਈ ਵਧੀਆ ਹੈ। ਇੱਥੇ ਇਸਦੀ ਵਰਤੋਂ ਦੀ ਉਦਾਹਰਨ ਹੈ:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

ਇਸ ਫੰਕਸ਼ਨਲਿਟੀ ਬਾਰੇ ਹੋਰ ਅਗਲੇ ਅਧਿਆਇ ਵਿੱਚ ਜਾਣਕਾਰੀ ਮਿਲੇਗੀ।

## ਅਭਿਆਸ - ਆਪਣੀ ਪਹਿਲੀ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ

ਹੁਣ ਜਦੋਂ ਅਸੀਂ openai ਸੈੱਟਅਪ ਅਤੇ ਕਨਫਿਗਰ ਕਰਨਾ ਸਿੱਖ ਲਿਆ ਹੈ, ਆਪਣੀ ਪਹਿਲੀ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਬਣਾਉਣ ਦਾ ਸਮਾਂ ਹੈ। ਆਪਣੀ ਐਪ ਬਣਾਉਣ ਲਈ, ਇਹ ਕਦਮ ਫੋਲੋ ਕਰੋ:

1. ਇੱਕ ਵਰਚੁਅਲ ਇਨਵਾਇਰਨਮੈਂਟ ਬਣਾਓ ਅਤੇ openai ਇੰਸਟਾਲ ਕਰੋ:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > ਜੇ ਤੁਸੀਂ Windows ਵਰਤ ਰਹੇ ਹੋ ਤਾਂ `source venv/bin/activate` ਦੀ ਥਾਂ `venv\Scripts\activate` ਲਿਖੋ।

   > [!NOTE]
   > ਆਪਣੀ Azure OpenAI ਕੀ ਲੱਭਣ ਲਈ [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) 'ਤੇ ਜਾਓ, `Open AI` ਖੋਜੋ, `Open AI resource` ਚੁਣੋ, ਫਿਰ `Keys and Endpoint` 'ਤੇ ਜਾ ਕੇ `Key 1` ਦੀ ਕਾਪੀ ਕਰੋ।

1. ਇੱਕ _app.py_ ਫਾਇਲ ਬਣਾਓ ਅਤੇ ਇਸ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਲਿਖੋ:

   ```python
   import openai

   openai.api_key = "<replace this value with your open ai key or Azure OpenAI key>"

   openai.api_type = 'azure'
   openai.api_version = '2023-05-15'
   openai.api_base = "<endpoint found in Azure Portal where your API key is>"
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"
   messages = [{"role": "user", "content": prompt}]

   # make completion
   completion = openai.chat.completions.create(model=deployment_name, messages=messages)

   # print response
   print(completion.choices[0].message.content)
   ```

   > [!NOTE]
   > ਜੇ ਤੁਸੀਂ Azure OpenAI ਵਰਤ ਰਹੇ ਹੋ, ਤਾਂ `api_type` ਨੂੰ `azure` ਤੇ `api_key` ਨੂੰ ਆਪਣੀ Azure OpenAI ਕੀ 'ਤੇ ਸੈੱਟ ਕਰੋ।

   ਤੁਹਾਨੂੰ ਹੇਠਾਂ ਦਿੱਤਾ ਨਤੀਜਾ ਮਿਲੇਗਾ:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## ਵੱਖ-ਵੱਖ ਕਿਸਮਾਂ ਦੇ prompts, ਵੱਖ-ਵੱਖ ਕੰਮਾਂ ਲਈ

ਹੁਣ ਤੁਸੀਂ ਦੇਖ ਚੁੱਕੇ ਹੋ ਕਿ prompt ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਟੈਕਸਟ ਕਿਵੇਂ ਜਨਰੇਟ ਕਰਨਾ ਹੈ। ਤੁਹਾਡੇ ਕੋਲ ਇੱਕ ਪ੍ਰੋਗਰਾਮ ਵੀ ਹੈ ਜੋ ਚੱਲ ਰਿਹਾ ਹੈ ਅਤੇ ਜਿਸਨੂੰ ਤੁਸੀਂ ਬਦਲ ਕੇ ਵੱਖ-ਵੱਖ ਕਿਸਮਾਂ ਦਾ ਟੈਕਸਟ ਜਨਰੇਟ ਕਰ ਸਕਦੇ ਹੋ।

Prompts ਹਰ ਤਰ੍ਹਾਂ ਦੇ ਕੰਮਾਂ ਲਈ ਵਰਤੇ ਜਾ ਸਕਦੇ ਹਨ। ਉਦਾਹਰਨ ਵਜੋਂ:

- **ਕਿਸੇ ਕਿਸਮ ਦਾ ਟੈਕਸਟ ਜਨਰੇਟ ਕਰੋ**। ਉਦਾਹਰਨ ਵਜੋਂ, ਤੁਸੀਂ ਕਵਿਤਾ, ਕਵਿਜ਼ ਲਈ ਸਵਾਲ ਆਦਿ ਜਨਰੇਟ ਕਰ ਸਕਦੇ ਹੋ।
- **ਜਾਣਕਾਰੀ ਲੱਭੋ**। ਤੁਸੀਂ prompts ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਜਾਣਕਾਰੀ ਲੱਭ ਸਕਦੇ ਹੋ, ਜਿਵੇਂ 'ਵੈੱਬ ਡਿਵੈਲਪਮੈਂਟ ਵਿੱਚ CORS ਦਾ ਕੀ ਮਤਲਬ ਹੈ?'।
- **ਕੋਡ ਜਨਰੇਟ ਕਰੋ**। ਤੁਸੀਂ prompts ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੋਡ ਜਨਰੇਟ ਕਰ ਸਕਦੇ ਹੋ, ਉਦਾਹਰਨ ਵਜੋਂ ਇਮੇਲ ਵੈਰੀਫਿਕੇਸ਼ਨ ਲਈ regular expression ਬਣਾਉਣਾ ਜਾਂ ਪੂਰਾ ਪ੍ਰੋਗਰਾਮ ਜਿਵੇਂ ਵੈੱਬ ਐਪ ਬਣਾਉਣਾ।

## ਇੱਕ ਹੋਰ ਪ੍ਰਯੋਗਿਕ ਮਾਮਲਾ: ਰੈਸੀਪੀ ਜਨਰੇਟਰ

ਕਲਪਨਾ ਕਰੋ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਘਰ ਵਿੱਚ ਕੁਝ ਸਮੱਗਰੀ ਹੈ ਅਤੇ ਤੁਸੀਂ ਕੁਝ ਬਣਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ। ਇਸ ਲਈ ਤੁਹਾਨੂੰ ਇੱਕ ਰੈਸੀਪੀ ਦੀ ਲੋੜ ਹੈ। ਰੈਸੀਪੀ ਲੱਭਣ ਲਈ ਤੁਸੀਂ ਖੋਜ ਇੰਜਣ ਵਰਤ ਸਕਦੇ ਹੋ ਜਾਂ LLM ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ।

ਤੁਸੀਂ ਇਸ ਤਰ੍ਹਾਂ ਦਾ prompt ਲਿਖ ਸਕਦੇ ਹੋ:

> "ਮੈਨੂੰ ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਸਮੱਗਰੀਆਂ ਨਾਲ ਬਣੇ ਖਾਣੇ ਲਈ 5 ਰੈਸੀਪੀ ਦਿਖਾਓ: ਚਿਕਨ, ਆਲੂ, ਅਤੇ ਗਾਜਰ। ਹਰ ਰੈਸੀਪੀ ਲਈ ਸਾਰੀਆਂ ਵਰਤੀ ਗਈਆਂ ਸਮੱਗਰੀਆਂ ਦੀ ਸੂਚੀ ਦਿਓ।"

ਉਪਰੋਕਤ prompt ਦੇ ਜਵਾਬ ਵਜੋਂ ਤੁਹਾਨੂੰ ਕੁਝ ਇਸ ਤਰ੍ਹਾਂ ਮਿਲ ਸਕਦਾ ਹੈ:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 2 cloves garlic, minced
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
```

ਇਹ ਨਤੀਜਾ ਵਧੀਆ ਹੈ, ਮੈਨੂੰ ਪਤਾ ਹੈ ਕਿ ਕੀ ਬਣਾਉਣਾ ਹੈ। ਇਸ ਸਮੇਂ, ਕੁਝ ਸੁਧਾਰ ਜੋ ਲਾਭਦਾਇਕ ਹੋ ਸਕਦੇ ਹਨ:

- ਉਹ ਸਮੱਗਰੀਆਂ ਫਿਲਟਰ ਕਰਨਾ ਜੋ ਮੈਨੂੰ ਪਸੰਦ ਨਹੀਂ ਜਾਂ ਜਿਨ੍ਹਾਂ ਨਾਲ ਮੈਂ ਐਲਰਜਿਕ ਹਾਂ।
- ਖਰੀਦਦਾਰੀ ਦੀ ਸੂਚੀ ਤਿਆਰ ਕਰਨਾ, ਜੇ ਘਰ ਵਿੱਚ ਸਾਰੀਆਂ ਸਮੱਗਰੀਆਂ ਨਹੀਂ ਹਨ।

ਉਪਰੋਕਤ ਮਾਮਲਿਆਂ ਲਈ, ਇੱਕ ਹੋਰ prompt ਸ਼ਾਮਲ ਕਰੀਏ:

> "ਕਿਰਪਾ ਕਰਕੇ ਉਹ ਰੈਸੀਪੀ ਹਟਾਓ ਜਿਨ੍ਹਾਂ ਵਿੱਚ ਲਸਣ ਹੈ ਕਿਉਂਕਿ ਮੈਨੂੰ ਲਸਣ ਨਾਲ ਐਲਰਜੀ ਹੈ ਅਤੇ ਇਸਦੀ ਥਾਂ ਕੁਝ ਹੋਰ ਦਿਓ। ਨਾਲ ਹੀ, ਰੈਸੀਪੀ ਲਈ ਖਰੀਦਦਾਰੀ ਦੀ ਸੂਚੀ ਬਣਾਓ, ਧਿਆਨ ਵਿੱਚ ਰੱਖਦੇ ਹੋਏ ਕਿ ਮੇਰੇ ਕੋਲ ਪਹਿਲਾਂ ਹੀ ਚਿਕਨ, ਆਲੂ ਅਤੇ ਗਾਜਰ ਹਨ।"

ਹੁਣ ਤੁਹਾਡੇ ਕੋਲ ਨਵਾਂ ਨਤੀਜ
1. ਅਸੀਂ ਇੱਕ ਨਵੀਂ ਬੇਨਤੀ ਕਰਦੇ ਹਾਂ, ਪਰ ਪਹਿਲੀ ਪ੍ਰਾਂਪਟ ਵਿੱਚ ਮੰਗੇ ਗਏ ਟੋਕਨ ਦੀ ਗਿਣਤੀ ਨੂੰ ਵੀ ਧਿਆਨ ਵਿੱਚ ਰੱਖਦੇ ਹਾਂ, ਇਸ ਵਾਰੀ ਅਸੀਂ ਕਹਿੰਦੇ ਹਾਂ ਕਿ `max_tokens` 1200 ਹੈ।

   ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

   ਇਸ ਕੋਡ ਨੂੰ ਚਲਾਉਂਦੇ ਹੋਏ, ਅਸੀਂ ਹੁਣ ਹੇਠਾਂ ਦਿੱਤਾ ਨਤੀਜਾ ਪ੍ਰਾਪਤ ਕਰਦੇ ਹਾਂ:

   ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## ਆਪਣਾ ਸੈਟਅਪ ਸੁਧਾਰੋ

ਹੁਣ ਤੱਕ ਸਾਡੇ ਕੋਲ ਕੰਮ ਕਰਨ ਵਾਲਾ ਕੋਡ ਹੈ, ਪਰ ਕੁਝ ਬਦਲਾਵ ਕਰਨੇ ਚਾਹੀਦੇ ਹਨ ਤਾਂ ਜੋ ਗੱਲਾਂ ਹੋਰ ਵਧੀਆ ਹੋ ਸਕਣ। ਕੁਝ ਗੱਲਾਂ ਜੋ ਸਾਨੂੰ ਕਰਨੀ ਚਾਹੀਦੀਆਂ ਹਨ:

- **ਰਹੱਸ ਨੂੰ ਕੋਡ ਤੋਂ ਵੱਖਰਾ ਕਰੋ**, ਜਿਵੇਂ ਕਿ API ਕੁੰਜੀ। ਰਹੱਸ ਕੋਡ ਵਿੱਚ ਨਹੀਂ ਹੋਣੇ ਚਾਹੀਦੇ ਅਤੇ ਉਹਨਾਂ ਨੂੰ ਸੁਰੱਖਿਅਤ ਥਾਂ ਤੇ ਰੱਖਣਾ ਚਾਹੀਦਾ ਹੈ। ਰਹੱਸ ਨੂੰ ਕੋਡ ਤੋਂ ਵੱਖਰਾ ਕਰਨ ਲਈ, ਅਸੀਂ environment variables ਅਤੇ `python-dotenv` ਵਰਗੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹਾਂ ਜੋ ਉਹਨਾਂ ਨੂੰ ਫਾਇਲ ਤੋਂ ਲੋਡ ਕਰਦੀਆਂ ਹਨ। ਕੋਡ ਵਿੱਚ ਇਹ ਇਸ ਤਰ੍ਹਾਂ ਦਿਖੇਗਾ:

  1. ਇੱਕ `.env` ਫਾਇਲ ਬਣਾਓ ਜਿਸ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਸਮੱਗਰੀ ਹੋਵੇ:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     
> [!NOTE] Azure ਲਈ, ਤੁਹਾਨੂੰ ਹੇਠਾਂ ਦਿੱਤੇ environment variables ਸੈੱਟ ਕਰਨੇ ਪੈਣਗੇ:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     ਕੋਡ ਵਿੱਚ, ਤੁਸੀਂ environment variables ਇਸ ਤਰ੍ਹਾਂ ਲੋਡ ਕਰੋਗੇ:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **ਟੋਕਨ ਦੀ ਲੰਬਾਈ ਬਾਰੇ ਇੱਕ ਗੱਲ**। ਸਾਨੂੰ ਸੋਚਣਾ ਚਾਹੀਦਾ ਹੈ ਕਿ ਸਾਨੂੰ ਲਿਖਤ ਬਣਾਉਣ ਲਈ ਕਿੰਨੇ ਟੋਕਨ ਚਾਹੀਦੇ ਹਨ। ਟੋਕਨ ਦੀ ਕੀਮਤ ਹੁੰਦੀ ਹੈ, ਇਸ ਲਈ ਜਿੱਥੇ ਸੰਭਵ ਹੋਵੇ, ਸਾਨੂੰ ਟੋਕਨਾਂ ਦੀ ਗਿਣਤੀ ਵਿੱਚ ਬਚਤ ਕਰਨੀ ਚਾਹੀਦੀ ਹੈ। ਉਦਾਹਰਨ ਵਜੋਂ, ਕੀ ਅਸੀਂ ਪ੍ਰਾਂਪਟ ਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਬਣਾ ਸਕਦੇ ਹਾਂ ਕਿ ਘੱਟ ਟੋਕਨ ਵਰਤੇ ਜਾਣ?

  ਟੋਕਨਾਂ ਦੀ ਗਿਣਤੀ ਬਦਲਣ ਲਈ, ਤੁਸੀਂ `max_tokens` ਪੈਰਾਮੀਟਰ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ। ਉਦਾਹਰਨ ਵਜੋਂ, ਜੇ ਤੁਸੀਂ 100 ਟੋਕਨ ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਇਹ ਕਰੋਗੇ:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **ਤਾਪਮਾਨ ਨਾਲ ਪ੍ਰਯੋਗ ਕਰਨਾ**। ਤਾਪਮਾਨ ਇੱਕ ਐਸਾ ਪੈਰਾਮੀਟਰ ਹੈ ਜਿਸ ਬਾਰੇ ਅਸੀਂ ਹੁਣ ਤੱਕ ਨਹੀਂ ਗੱਲ ਕੀਤੀ, ਪਰ ਇਹ ਸਾਡੇ ਪ੍ਰੋਗਰਾਮ ਦੀ ਕਾਰਗੁਜ਼ਾਰੀ ਲਈ ਮਹੱਤਵਪੂਰਨ ਹੈ। ਜਿੰਨਾ ਵੱਧ ਤਾਪਮਾਨ ਦਾ ਮੁੱਲ ਹੋਵੇਗਾ, ਨਤੀਜਾ ਉਤਨਾ ਹੀ ਜ਼ਿਆਦਾ ਬੇਤਰਤੀਬ ਹੋਵੇਗਾ। ਇਸਦੇ ਉਲਟ, ਜਿੰਨਾ ਘੱਟ ਤਾਪਮਾਨ ਹੋਵੇਗਾ, ਨਤੀਜਾ ਉਤਨਾ ਹੀ ਅਨੁਮਾਨਯੋਗ ਹੋਵੇਗਾ। ਸੋਚੋ ਕਿ ਤੁਸੀਂ ਆਪਣੇ ਨਤੀਜੇ ਵਿੱਚ ਵੱਖ-ਵੱਖਤਾ ਚਾਹੁੰਦੇ ਹੋ ਜਾਂ ਨਹੀਂ।

  ਤਾਪਮਾਨ ਬਦਲਣ ਲਈ, ਤੁਸੀਂ `temperature` ਪੈਰਾਮੀਟਰ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ। ਉਦਾਹਰਨ ਵਜੋਂ, ਜੇ ਤੁਸੀਂ 0.5 ਦਾ ਤਾਪਮਾਨ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਇਹ ਕਰੋਗੇ:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > [!NOTE] 1.0 ਦੇ ਨੇੜੇ ਹੋਣ ਤੇ ਨਤੀਜਾ ਹੋਰ ਵੱਖਰਾ ਹੋਵੇਗਾ।

## ਅਸਾਈਨਮੈਂਟ

ਇਸ ਅਸਾਈਨਮੈਂਟ ਲਈ, ਤੁਸੀਂ ਜੋ ਬਣਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ ਚੁਣ ਸਕਦੇ ਹੋ।

ਇੱਥੇ ਕੁਝ ਸੁਝਾਅ ਹਨ:

- ਰੈਸੀਪੀ ਜਨਰੇਟਰ ਐਪ ਨੂੰ ਹੋਰ ਸੁਧਾਰੋ। ਤਾਪਮਾਨ ਦੇ ਮੁੱਲਾਂ ਅਤੇ ਪ੍ਰਾਂਪਟਾਂ ਨਾਲ ਖੇਡੋ ਅਤੇ ਦੇਖੋ ਕਿ ਤੁਸੀਂ ਕੀ ਨਵਾਂ ਕਰ ਸਕਦੇ ਹੋ।
- ਇੱਕ "ਸਟਡੀ ਬੱਡੀ" ਬਣਾਓ। ਇਹ ਐਪ ਕਿਸੇ ਵਿਸ਼ੇ ਬਾਰੇ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਦੇ ਸਕਦੀ ਹੈ, ਉਦਾਹਰਨ ਵਜੋਂ Python, ਜਿੱਥੇ ਤੁਸੀਂ ਪ੍ਰਾਂਪਟਾਂ ਵਰਗੇ "Python ਵਿੱਚ ਕਿਸੇ ਵਿਸ਼ੇ ਦਾ ਕੀ ਮਤਲਬ ਹੈ?" ਜਾਂ "ਕਿਸੇ ਵਿਸ਼ੇ ਲਈ ਕੋਡ ਦਿਖਾਓ" ਵਰਗੇ ਪ੍ਰਾਂਪਟ ਰੱਖ ਸਕਦੇ ਹੋ।
- ਇਤਿਹਾਸ ਬੋਟ, ਇਤਿਹਾਸ ਨੂੰ ਜਿਊਂਦਾ ਕਰੋ, ਬੋਟ ਨੂੰ ਕਿਸੇ ਇਤਿਹਾਸਕ ਪਾਤਰ ਵਜੋਂ ਨਿਰਦੇਸ਼ ਦਿਓ ਅਤੇ ਉਸਦੇ ਜੀਵਨ ਅਤੇ ਸਮੇਂ ਬਾਰੇ ਸਵਾਲ ਪੁੱਛੋ।

## ਹੱਲ

### ਸਟਡੀ ਬੱਡੀ

ਹੇਠਾਂ ਇੱਕ ਸ਼ੁਰੂਆਤੀ ਪ੍ਰਾਂਪਟ ਦਿੱਤਾ ਗਿਆ ਹੈ, ਦੇਖੋ ਕਿ ਤੁਸੀਂ ਇਸਨੂੰ ਕਿਵੇਂ ਵਰਤ ਸਕਦੇ ਹੋ ਅਤੇ ਆਪਣੀ ਪਸੰਦ ਅਨੁਸਾਰ ਬਦਲ ਸਕਦੇ ਹੋ।

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### ਇਤਿਹਾਸ ਬੋਟ

ਇੱਥੇ ਕੁਝ ਪ੍ਰਾਂਪਟ ਹਨ ਜੋ ਤੁਸੀਂ ਵਰਤ ਸਕਦੇ ਹੋ:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## ਗਿਆਨ ਦੀ ਜਾਂਚ

ਤਾਪਮਾਨ ਦਾ ਕਾਂਸੈਪਟ ਕੀ ਕਰਦਾ ਹੈ?

1. ਇਹ ਨਤੀਜੇ ਦੀ ਬੇਤਰਤੀਬੀ ਨੂੰ ਨਿਯੰਤਰਿਤ ਕਰਦਾ ਹੈ।  
1. ਇਹ ਜਵਾਬ ਦੀ ਲੰਬਾਈ ਨੂੰ ਨਿਯੰਤਰਿਤ ਕਰਦਾ ਹੈ।  
1. ਇਹ ਵਰਤੇ ਗਏ ਟੋਕਨਾਂ ਦੀ ਗਿਣਤੀ ਨੂੰ ਨਿਯੰਤਰਿਤ ਕਰਦਾ ਹੈ।  

## 🚀 ਚੈਲੈਂਜ

ਅਸਾਈਨਮੈਂਟ 'ਤੇ ਕੰਮ ਕਰਦੇ ਸਮੇਂ, ਤਾਪਮਾਨ ਨੂੰ ਵੱਖ-ਵੱਖ ਕਰਕੇ ਦੇਖੋ, ਜਿਵੇਂ 0, 0.5, ਅਤੇ 1 ਸੈੱਟ ਕਰੋ। ਯਾਦ ਰੱਖੋ ਕਿ 0 ਸਭ ਤੋਂ ਘੱਟ ਵੱਖਰਾ ਹੁੰਦਾ ਹੈ ਅਤੇ 1 ਸਭ ਤੋਂ ਵੱਧ। ਤੁਹਾਡੇ ਐਪ ਲਈ ਕਿਹੜਾ ਮੁੱਲ ਸਭ ਤੋਂ ਵਧੀਆ ਕੰਮ ਕਰਦਾ ਹੈ?

## ਸ਼ਾਬਾਸ਼! ਆਪਣੀ ਸਿੱਖਿਆ ਜਾਰੀ ਰੱਖੋ

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਸਾਡੇ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ਨੂੰ ਵੇਖੋ ਤਾਂ ਜੋ ਤੁਸੀਂ ਆਪਣਾ Generative AI ਗਿਆਨ ਹੋਰ ਵਧਾ ਸਕੋ!

ਹੁਣ ਲੈਸਨ 7 ਵੱਲ ਜਾਓ ਜਿੱਥੇ ਅਸੀਂ ਦੇਖਾਂਗੇ ਕਿ ਕਿਵੇਂ [ਚੈਟ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਈਆਂ ਜਾਂਦੀਆਂ ਹਨ](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।