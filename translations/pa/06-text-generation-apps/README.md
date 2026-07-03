# ਟੈਕਸਟ ਜਿਨਰੇਸ਼ਨ ਐਪਲੀਕੇਸ਼ਨਾਂ ਦਾ ਬਨਾਣਾ

[![Building Text Generation Applications](../../../translated_images/pa/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(ਇਸ ਪਾਠ ਦਾ ਵੀਡੀਓ ਵੇਖਣ ਲਈ ਉੱਪਰ ਦਿੱਤੀ ਚਿੱਤਰ 'ਤੇ ਕਲਿੱਕ ਕਰੋ)_

ਤੁਸੀਂ ਇਸ ਕਰਿਕੁਲਮ ਵਿੱਚ ਹੁਣ ਤੱਕ ਵੇਖਿਆ ਹੈ ਕਿ ਕੁਝ ਮੁੱਖ ਧਾਰਨਾਵਾਂ ਹਨ ਜਿਵੇਂ ਪ੍ਰੌਂਪਟ ਅਤੇ ਇੱਥੇ ਤਕ ਕਿ ਇੱਕ ਪੂਰੀ ਵਿਸ਼ੇਸ਼ਤਾ ਹੈ ਜਿਸਨੂੰ "ਪ੍ਰੌਂਪਟ ਇੰਜੀਨੀਅਰਿੰਗ" ਕਿਹਾ ਜਾਂਦਾ ਹੈ। ਕਈ ਔਜ਼ਾਰ ਜਿਵੇਂ ChatGPT, Office 365, Microsoft Power Platform ਅਤੇ ਹੋਰ, ਤੁਹਾਡੇ ਨਾਲ ਸਹਿਯੋਗ ਲਈ ਪ੍ਰੌਂਪਟ ਦੇ ਕੇ ਕੰਮ ਕਰਦੇ ਹਨ।

ਤੁਹਾਨੂੰ ਐਪ ਵਿੱਚ ਵਿਸ਼ੇਸ਼ ਅਨੁਭਵ ਜੋੜਨ ਲਈ, ਤੁਹਾਨੂੰ ਪ੍ਰੌਂਪਟ, ਕਮਪਲੀਸ਼ਨਾਂ ਵਰਗੀਆਂ ਧਾਰਨਾਵਾਂ ਨੂੰ ਸਮਝਣਾ ਤੇ ਕੰਮ ਕਰਨ ਲਈ ਕੋਈ ਲਾਇਬ੍ਰੇਰੀ ਚੁਣਨੀ ਪਵੇਗੀ। ਇਹੀ ਕੁਝ ਤੁਸੀਂ ਇਸ ਅਧਿਆਇ ਵਿੱਚ ਸਿੱਖੋਗੇ।

## ਪਰਿਚય

ਇਸ ਅਧਿਆਇ ਵਿੱਚ, ਤੁਸੀਂ:

- openai ਲਾਇਬ੍ਰੇਰੀ ਅਤੇ ਇਸਦੇ ਮੁੱਖ ਧਾਰਨਾਵਾਂ ਬਾਰੇ ਸਿੱਖੋਗੇ।
- openai ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਟੈਕਸਟ ਜਿਨਰੇਸ਼ਨ ਐਪ ਬਣਾਵੋਗੇ।
- ਪ੍ਰੌਂਪਟ, ਤਾਪਮਾਨ ਅਤੇ ਟੋਕਨਾਂ ਵਰਗੀਆਂ ਧਾਰਨਾਵਾਂ ਦੀ ਵਰਤੋਂ ਸਿੱਖੋਗੇ ਜਿਸਨਾਲ ਟੈਕਸਟ ਜਿਨਰੇਸ਼ਨ ਐਪ ਬਣਾਈ ਜਾ ਸਕਦੀ ਹੈ।

## ਸਿੱਖਣ ਦੇ ਲਕੜ

ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਤੇ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- ਸਮਝਾਉਣ ਲਈ ਕਿ ਟੈਕਸਟ ਜਿਨਰੇਸ਼ਨ ਐਪ ਕੀ ਹੈ।
- openai ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਟੈਕਸਟ ਜਿਨਰੇਸ਼ਨ ਐਪ ਬਣਾਉਣਾ।
- ਆਪਣੇ ਐਪ ਨੂੰ ਅਧਿਕ ਜਾਂ ਘੱਟ ਟੋਕਨ ਵਰਤਣ ਲਈ ਸੰਰਚਿਤ ਕਰਨਾ ਅਤੇ ਤਾਪਮਾਨ ਨੂੰ ਵੀ ਬਦਲਣਾ, ਵੱਖਰੇ ਨਤੀਜੇ ਲਈ।

## ਟੈਕਸਟ ਜਿਨਰੇਸ਼ਨ ਐਪ ਕੀ ਹੈ?

ਆਮ ਤੌਰ ‘ਤੇ ਜਦੋਂ ਤੁਸੀਂ ਕੋਈ ਐਪ ਬਣਾਉਂਦੇ ਹੋ ਤਾਂ ਉਹ ਕਿਸੇ ਤਰ੍ਹਾਂ ਦੀ ਇੰਟਰਫੇਸ ਹੁੰਦੀ ਹੈ, ਜਿਵੇਂ:

- ਕਮਾਂਡ ਆਧਾਰਤ। ਕੰਸੋਲ ਐਪ ਉਹ ਐਪ ਹੁੰਦੀਆਂ ਹਨ ਜਿੱਥੇ ਤੁਸੀਂ ਕਮਾਂਡ ਲਿਖਦੇ ਹੋ ਅਤੇ ਉਹ ਕੰਮ ਕਰਦੀ ਹੈ। ਉਦਾਹਰਨ ਲਈ, `git` ਇੱਕ ਕਮਾਂਡ ਆਧਾਰਤ ਐਪ ਹੈ।
- ਯੂਜ਼ਰ ਇੰਟਰਫੇਸ (UI). ਕੁਝ ਐਪ ਨੇ ਗ੍ਰਾਫਿਕਲ ਯੂਜ਼ਰ ਇੰਟਰਫੇਸ (GUIs) ਹੁੰਦੇ ਹਨ ਜਿੱਥੇ ਤੁਸੀਂ ਬਟਨਾਂ ਤੇ ਕਲਿੱਕ ਕਰਦੇ ਹੋ, ਟੈਕਸਟ ਸੁਮਿਲਦਿਆਂ ਅਤੇ ਵਿਕਲਪ ਚੁਣਦੇ ਹੋ।

### ਕੰਸੋਲ ਅਤੇ UI ਐਪ ਸੀਮਿਤ ਹਨ

ਇੱਕ ਕਮਾਂਡ ਆਧਾਰਤ ਐਪ ਨਾਲ ਤੁਲਨਾ ਕਰੋ ਜਿੱਥੇ ਤੁਸੀਂ ਕਮਾਂਡ ਲਿਖਦੇ ਹੋ:

- **ਇਹ ਸੀਮਿਤ ਹੈ**। ਤੁਸੀਂ ਕੋਈ ਵੀ ਕਮਾਂਡ ਨਹੀਂ ਲਿਖ ਸਕਦੇ, ਸਿਰਫ ਉਹੀ ਜੋ ਐਪ ਸਹਿਯੋਗ ਕਰਦੀ ਹੈ।
- **ਭਾਸ਼ਾ ਵਿਸ਼ੇਸ਼**। ਕੁਝ ਐਪ ਕਈਆਂ ਭਾਸ਼ਾਵਾਂ ਦਾ ਸਹਿਯੋਗ ਕਰਦੇ ਹਨ, ਪਰ ਆਮ ਤੌਰ ‘ਤੇ ਐਪ ਕਿਸੇ ਵਿਸ਼ੇਸ਼ ਭਾਸ਼ਾ ਲਈ ਬਣਾਈ ਗਈ ਹੁੰਦੀ ਹੈ, ਹਾਲਾਂਕਿ ਤੁਸੀਂ ਹੋਰ ਭਾਸ਼ਾਵਾਂ ਜੋੜ ਸਕਦੇ ਹੋ।

### ਟੈਕਸਟ ਜਿਨਰੇਸ਼ਨ ਐਪ ਦੇ ਫਾਇਦੇ

ਤਾਂ ਫਿਰ ਟੈਕਸਟ ਜਿਨਰੇਸ਼ਨ ਐਪ ਕਿਵੇਂ ਵੱਖਰਾ ਹੈ?

ਇੱਕ ਟੈਕਸਟ ਜਿਨਰੇਸ਼ਨ ਐਪ ਵਿੱਚ, ਤੁਹਾਡੇ ਕੋਲ ਵਧੇਰੇ ਲਚੀਲਾਪਨ ਹੁੰਦਾ ਹੈ, ਤੁਸੀਂ ਕਮਾਂਡਾਂ ਜਾਂ ਕਿਸੇ ਵਿਸ਼ੇਸ਼ ਇਨਪੁਟ ਭਾਸ਼ਾ ਤੱਕ ਸੀਮਿਤ ਨਹੀਂ ਹੋ। ਤੁਸੀਂ ਕਿਰਤੀ ਭਾਸ਼ਾ ਵਰਤ ਕੇ ਐਪ ਨਾਲ ਸੰਪਰਕ ਕਰ ਸਕਦੇ ਹੋ। ਇਕ ਹੋਰ ਫਾਇਦਾ ਇਹ ਹੈ ਕਿ ਤੁਸੀਂ ਪਹਿਲਾਂ ਹੀ ਇਕ ਡੇਟਾ ਸਰੋਤ ਨਾਲ ਸੰਪਰਕ ਕਰ ਰਹੇ ਹੋ ਜੋ ਵੱਡੇ ਦਸਤਾਵੇਜ਼ਾਂ ਤੇ ਟ੍ਰੇਨ ਕੀਤਾ ਗਿਆ ਹੈ, ਜਦਕਿ ਆਮ ਐਪ ਸਿਰਫ ਡੇਟਾਬੇਸ ਵਿੱਚ ਮੌਜੂਦ ਕੀਤੇ ਚੀਜ਼ਾਂ ਤੱਕ ਸੀਮਿਤ ਰਹਿੰਦਾ ਹੈ।

### ਟੈਕਸਟ ਜਿਨਰੇਸ਼ਨ ਐਪ ਨਾਲ ਕੀ ਬਣਾਇਆ ਜਾ ਸਕਦਾ ਹੈ?

ਤੁਹਾਡੇ ਕੋਲ ਕਈ ਚੀਜ਼ਾਂ ਹਨ ਜੋ ਤੁਸੀਂ ਬਣਾ ਸਕਦੇ ਹੋ। ਉਦਾਹਰਨ ਲਈ:

- **ਇੱਕ ਚੈਟਬੌਟ**। ਜਿਹੜਾ ਤੁਹਾਡੇ ਕੰਪਨੀ ਅਤੇ ਵਸਤੂਆਂ ਦੇ ਬਾਰੇ ਸਵਾਲਾਂ ਦਾ ਜਵਾਬ ਦੇ ਸਕਦਾ ਹੈ।
- **ਸਹਾਇਕ**। LLM ਵਧੀਆ ਹਨ ਜਿਵੇਂ ਕਿ ਟੈਕਸਟ ਦਾ ਸੰਖੇਪ ਬਨਾਉਣਾ, ਟੈਕਸਟ ਤੋਂ ਜਾਣਕਾਰੀ ਲੈਣਾ, ਰੇਜ਼ਿਊਮੇ ਵਰਗਾ ਟੈਕਸਟ ਤਿਆਰ ਕਰਨਾ ਆਦਿ।
- **ਕੋਡ ਸਹਾਇਕ**। ਤੁਸੀਂ ਆਪਣੀ ਭਾਸ਼ਾ ਮਾਡਲ ਦੇ ਅਨੁਸਾਰ ਇੱਕ ਕੋਡ ਸਹਾਇਕ ਤਿਆਰ ਕਰ ਸਕਦੇ ਹੋ ਜੋ ਤੁਹਾਡੇ ਕੋਡ ਲਿਖਣ ਵਿੱਚ ਮਦਦ ਕਰੇ। ਉਦਾਹਰਨ ਲਈ, GitHub Copilot ਜਾਂ ChatGPT ਵਰਗੇ ਉਤਪਾਦ ਵਰਤ ਕੇ।

## ਕਿਵੇਂ ਸ਼ੁਰੂ ਕਰਾਂ?

ਤੁਹਾਨੂੰ ਆਮ ਤੌਰ 'ਤੇ LLM (ਲਾਰਜ ਭਾਸ਼ਾ ਮਾਡਲ) ਨਾਲ ਇੰਟੇਗਰੇਟ ਕਰਨ ਲਈ ਦੋ ਤਰੀਕੇ ਲਭਣੇ ਪੈਂਦੇ ਹਨ:

- ਏਪੀਅਈ ਦੀ ਵਰਤੋਂ ਕਰੋ। ਇੱਥੇ ਤੁਸੀਂ ਆਪਣਾ ਪ੍ਰੌਂਪਟ ਲੈ ਕੇ ਵੈੱਬ ਰਿਕਵੈਸਟ ਬਣਾਉਂਦੇ ਹੋ ਅਤੇ ਜਿਨਰੇਟ ਕੀਤਾ ਟੈਕਸਟ ਮਿੱਲਦਾ ਹੈ।
- ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਵਰਤੋਂ ਕਰੋ। ਲਾਇਬ੍ਰੇਰੀ API ਕਾਲਾਂ ਨੂੰ ਸਮੇਟ ਕੇ ਉਨ੍ਹਾਂ ਨੂੰ ਵਰਤਣਾ آسان ਬਣਾਉਂਦੀਆਂ ਹਨ।

## ਲਾਇਬ੍ਰੇਰੀਆਂ/SDKs

LLM ਨਾਲ ਕੰਮ ਕਰਨ ਲਈ ਕੁਝ ਜਾਣੀਆਂ ਮਸ਼ਹੂਰ ਲਾਇਬ੍ਰੇਰੀਆਂ ਹਨ:

- **openai**: ਇਹ ਲਾਇਬ੍ਰੇਰੀ ਤੁਹਾਡੇ ਮਾਡਲ ਨਾਲ ਜੁੜਨ ਅਤੇ ਪ੍ਰੌਂਪਟ ਭੇਜਣ ਨੂੰ ਆਸਾਨ ਬਣਾਉਂਦੀ ਹੈ।

ਫਿਰ ਉੱਪਰਲੇ ਦਰਜੇ ਦੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਹਨ ਜਿਵੇਂ:

- **Langchain**: Langchain ਚੰਗੀ ਤਰ੍ਹਾਂ ਜਾਣੀ ਜਾਂਦੀ ਹੈ ਅਤੇ Python ਲਈ ਸਹਿਯੋਗ ਹੈ।
- **Semantic Kernel**: Semantic Kernel Microsoft ਵਲੋਂ ਹੈ ਜੋ C#, Python ਅਤੇ Java ਭਾਸ਼ਾਵਾਂ ਨੂੰ ਸਹਿਯੋਗ ਦਿੰਦਾ ਹੈ।

## openai ਨਾਲ ਪਹਿਲੀ ਐਪ

ਆਓ ਵੇਖੀਏ ਕਿ ਅਸੀਂ ਆਪਣੀ ਪਹਿਲੀ ਐਪ ਕਿਵੇਂ ਬਣਾਈਏ, ਕੀ ਲਾਇਬ੍ਰੇਰੀਆਂ ਚਾਹੀਦੀਆਂ ਹਨ, ਕਿੰਨਾ ਲੋੜੀਂਦਾ ਹੈ ਆਦਿ।

### openai ਇੰਸਟਾਲ ਕਰੋ

OpenAI ਜਾਂ Azure OpenAI ਨਾਲ ਕੰਮ ਕਰਨ ਲਈ ਬਹੁਤ ਸਾਰੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਹਨ। ਤੁਸੀਂ ਕਈ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ ਵਰਗੇ C#, Python, JavaScript, Java, ਆਦਿ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ। ਸਾਨੂੰ `openai` Python ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਵਰਤੋਂ ਕਰਨੀ ਹੈ, ਇਸ ਲਈ ਇਹ ਇੰਸਟਾਲ ਕਰਨ ਲਈ `pip` ਦੀ ਵਰਤੋਂ ਕਰਾਂਗੇ।

```bash
pip install openai
```

### ਇਕ ਸਰੋਤ ਬਣਾਓ

ਤੁਹਾਨੂੰ ਹੇਠਾਂ ਦਿੱਤੇ ਕਦਮ ਕਰਨੇ ਪੈਣਗੇ:

- Azure ਉੱਤੇ ਖਾਤਾ ਬਣਾਓ [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Azure OpenAI ਲਈ ਇਜਾਜ਼ਤ ਪ੍ਰਾਪਤ ਕਰੋ। [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) ਤੇ ਜਾਓ ਅਤੇ ਇਜਾਜ਼ਤ ਮੰਗੋ।

  > [!NOTE]
  > ਲਿਖਣ ਵੇਲੇ, Azure OpenAI ਲਈ ਇਜਾਜ਼ਤ ਲਈ ਅਰਜ਼ੀ ਦੇਣੀ ਪੈਂਦੀ ਹੈ।

- Python ਇੰਸਟਾਲ ਕਰੋ <https://www.python.org/>
- Azure OpenAI Service ਸਰੋਤ ਬਣਾਇਆ ਹੋਇਆ ਹੋਵੇ। ਇਸ ਗਾਈਡ ਨੂੰ ਵੇਖੋ ਕਿ ਕਿਵੇਂ [ਸਰੋਤ ਬਣਾਇਆ ਜਾਵੇ](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)।

### API ਕੁੰਜੀ ਅਤੇ ਐਂਡਪੋਇੰਟ ਲੱਭੋ

ਹੁਣ ਤੁਹਾਨੂੰ ਆਪਣੀ `openai` ਲਾਇਬ੍ਰੇਰੀ ਨੂੰ ਦੱਸਣਾ ਹੋਵੇਗਾ ਕਿ ਕਿਹੜੀ API ਕੁੰਜੀ ਵਰਤਣੀ ਹੈ। ਆਪਣੀ API ਕੁੰਜੀ ਲੱਭਣ ਲਈ, Azure OpenAI ਸਰੋਤ ਵਿੱਚ "Keys and Endpoint" ਹਿੱਸਾ ਜਾਓ ਅਤੇ "Key 1" ਕਾਪੀ ਕਰੋ।

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

ਹੁਣ ਜਦ ਇਹ ਜਾਣਕਾਰੀ ਤੁਹਾਡੇ ਕੋਲ ਹੈ, ਆਓ ਲਾਇਬ੍ਰੇਰੀਆਂ ਨੂੰ ਇਸ ਦੀ ਵਰਤੋਂ ਕਾਰਨ ਲਿਖੀਏ।

> [!NOTE]
> ਆਪਣੇ ਕੋਡ ਤੋਂ API ਕੁੰਜੀ ਨੂੰ ਵੱਖਰਾ ਰੱਖਣਾ ਚਾਹੀਦਾ ਹੈ। ਤੁਸੀਂ ਇਹ ਮਾਹੌਲ ਦੇ ਵੈਰੀਏਬਲ ਵਰਤ ਕੇ ਕਰ ਸਕਦੇ ਹੋ।
>
> - ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ `OPENAI_API_KEY` ਨੂੰ ਆਪਣੀ API ਕੁੰਜੀ ਤੇ ਸੈੱਟ ਕਰੋ।
>   `export OPENAI_API_KEY='sk-...'`

### Azure ਲਈ ਸੰਰਚਨਾ ਸੈੱਟ ਅੱਪ ਕਰੋ

ਜੇ ਤੁਸੀਂ Azure OpenAI ਵਰਤ ਰਹੇ ਹੋ ਤਾਂ ਇਹ ਹੈ ਕਿ ਤੁਸੀਂ ਕਿਵੇਂ ਸੰਰਚਨਾ ਸੈੱਟ ਕਰਦੇ ਹੋ:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

ਉੱਪਰ ਅਸੀਂ ਇਹ ਸੈੱਟ ਕਰ ਰਹੇ ਹਾਂ:

- `api_type` ਨੂੰ `azure` ਤੇ ਸੈੱਟ ਕਰਨਾ। ਇਹ ਲਾਇਬ੍ਰੇਰੀ ਨੂੰ ਦੱਸਦਾ ਹੈ ਕਿ Azure OpenAI ਵਰਤੋਂ ਅਤੇ OpenAI ਨਹੀਂ।
- `api_key`, ਇਹ ਤੁਹਾਡੀ API ਕੁੰਜੀ ਹੈ ਜੋ Azure ਪੋਰਟਲ ਵਿੱਚ ਮਿਲੀ ਹੈ।
- `api_version`, ਇਹ API ਦਾ ਵਰਜਨ ਹੈ ਜੋ ਤੁਸੀਂ ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹੋ। ਲਿਖਣ ਦੇ ਸਮੇਂ ਅਖੀਰੀ ਵਰਜਨ `2023-05-15` ਹੈ।
- `api_base`, ਇਹ API ਦਾ ਐਂਡਪੋਇੰਟ ਹੈ ਜੋ Azure ਪੋਰਟਲ ਵਿੱਚ ਤੁਹਾਡੀ API ਕੁੰਜੀ ਦੇ ਕੋਲ ਹੈ।

> [!NOTE]
> `os.getenv` ਮਾਹੌਲ ਵੈਰੀਏਬਲਾਂ ਨੂੰ ਪੜ੍ਹਨ ਵਾਲਾ ਫੰਕਸ਼ਨ ਹੈ। ਤੁਸੀਂ ਇਸਦਾ ਉਪਯੋਗ ਕਰਕੇ `OPENAI_API_KEY` ਅਤੇ `API_BASE` ਵਰਗੇ ਵੈਰੀਏਬਲਾਂ ਨੂੰ ਪੜ੍ਹ ਸਕਦੇ ਹੋ। ਇਨ੍ਹਾਂ ਵੈਰੀਏਬਲਾਂ ਨੂੰ ਟਰਮੀਨਲ ਵਿੱਚ ਜਾਂ `dotenv` ਜਿਹੀ ਲਾਇਬ੍ਰੇਰੀ ਵਰਤ ਕੇ ਸੈੱਟ ਕਰੋ।

## ਟੈਕਸਟ ਜਿਨਰੇਸ਼ਨ ਕਰਨਾ

ਟੈਕਸਟ ਜਿਨਰੇਟ ਕਰਨ ਲਈ `Completion` ਕਲਾਸ ਦੀ ਵਰਤੋਂ ਹੁੰਦੀ ਹੈ। ਇਹ ਦਿਖਾਵਾ ਹੇਠਾਂ ਹੈ:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ, ਅਸੀਂ ਇੱਕ Completion ਓਬਜੈਕਟ ਬਣਾਉਂਦੇ ਹਾਂ ਅਤੇ ਮਾਡਲ ਅਤੇ ਪ੍ਰੌਂਪਟ ਦਿੱਤਾ ਜਾਂਦਾ ਹੈ। ਫਿਰ ਜਿਨਰੇਟ ਕੀਤਾ ਟੈਕਸਟ ਪ੍ਰਿੰਟ ਕਰਦੇ ਹਾਂ।

### ਚੈਟ ਕਮਪਲੀਸ਼ਨ

ਹੁਣ ਤੱਕ, ਤੁਸੀਂ ਦੇਖਿਆ ਕਿ ਅਸੀਂ `Completion` ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਟੈਕਸਟ ਜਿਨਰੇਸ਼ਨ ਕਰ ਰਹੇ ਹਾਂ। ਪਰ ਇੱਕ ਹੋਰ ਕਲਾਸ `ChatCompletion` ਵੀ ਹੈ ਜੋ ਚੈਟਬੌਟ ਲਈ ਹੋਰ ਠੀਕ ਬੈਠਦੀ ਹੈ। ਇਹ ਉਦਾਹਰਨ ਹੈ:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

ਇਸ ਕਾਰਜਸ਼ੀਲਤਾ ਬਾਰੇ ਛੇਤੀ ਆਉਣ ਵਾਲੇ ਅਧਿਆਇ ਵਿੱਚ ਹੋਰ ਜਾਣਕਾਰੀ ਮਿਲੇਗੀ।

## ਅਭਿਆਸ - ਆਪਣੀ ਪਹਿਲੀ ਟੈਕਸਟ ਜਿਨਰੇਸ਼ਨ ਐਪ

ਹੁਣ ਜਦੋਂ ਅਸੀਂ openai ਨੂੰ ਸੈੱਟ ਅੱਪ ਕਰਨਾ ਸਿੱਖ ਲਿਆ ਹੈ, ਆਪਣੀ ਪਹਿਲੀ ਟੈਕਸਟ ਜਿਨਰੇਸ਼ਨ ਐਪ ਬਣਾਉਣ ਦਾ ਸਮਾਂ ਹੈ। ਆਪਣੀ ਐਪ ਬਣਾਉਣ ਲਈ, ਇਹ ਕਦਮ ਪਾਲਣ ਕਰੋ:

1. ਇੱਕ ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਉ ਅਤੇ openai ਇੰਸਟਾਲ ਕਰੋ:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > ਜੇ ਤੁਸੀਂ Windows ਵਰਤ ਰਹੇ ਹੋ ਤਾਂ `source venv/bin/activate` ਦੀ ਥਾਂ `venv\Scripts\activate` ਲਿਖੋ।

   > [!NOTE]
   > ਆਪਣਾ Azure OpenAI ਕੁੰਜੀ ਲੱਭਣ ਲਈ [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) ਜਾਓ, `Open AI` ਖੋਜੋ, `Open AI resource` ਚੁਣੋ ਅਤੇ `Keys and Endpoint` ਤੋਂ `Key 1` ਕਾਪੀ ਕਰੋ।

1. ਇੱਕ _app.py_ ਫਾਇਲ ਬਣਾਓ ਅਤੇ ਇਸ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਲਿਖੋ:

   ```python
   import openai

   openai.api_key = "<replace this value with your open ai key or Azure OpenAI key>"

   openai.api_type = 'azure'
   openai.api_version = '2023-05-15'
   openai.api_base = "<endpoint found in Azure Portal where your API key is>"
   deployment_name = "<deployment name>"

   # ਆਪਣਾ مکمل کوڈ شامل کریں
   prompt = "Complete the following: Once upon a time there was a"
   messages = [{"role": "user", "content": prompt}]

   # مکمل کریں
   completion = openai.chat.completions.create(model=deployment_name, messages=messages)

   # جواب پرنٹ کریں
   print(completion.choices[0].message.content)
   ```

   > [!NOTE]
   > ਜੇ ਤੁਸੀਂ Azure OpenAI ਵਰਤ ਰਹੇ ਹੋ ਤਾਂ `api_type` ਨੂੰ `azure` ਤੇ ਸੈੱਟ ਕਰੋ ਅਤੇ ਆਪਣੀ Azure OpenAI ਕੁੰਜੀ `api_key` ਵਿੱਚ ਭਰੋ।

   ਤੁਸੀਂ ਇਸ ਤਰ੍ਹਾਂ ਦਾ ਨਤੀਜਾ ਦੇਖੋਗੇ:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## ਵੱਖ-ਵੱਖ ਕਿਸਮ ਦੇ ਪ੍ਰੌਂਪਟ, ਵੱਖ-ਵੱਖ ਕੰਮਾਂ ਲਈ

ਹੁਣ ਤੁਹਾਡੇ ਕੋਲ ਟੈਕਸਟ ਜਿਨਰੇਟ ਕਰਨ ਲਈ ਕੋਡ ਹੈ। ਤੁਸੀਂ ਇੱਕ ਪ੍ਰੋਗਰਾਮ ਵੀ ਤਿਆਰ ਕਰ ਚੁੱਕੇ ਹੋ ਜੋ ਤਬਦੀਲ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

ਪ੍ਰੌਂਪਟ ਬਹੁਤ ਸਾਰੇ ਕੰਮਾਂ ਲਈ ਵਰਤੇ ਜਾ ਸਕਦੇ ਹਨ। ਉਦਾਹਰਨ:

- **ਇੱਕ ਕਿਸਮ ਦਾ ਟੈਕਸਟ ਜਿਨਰੇਟ ਕਰੋ**। ਉਦਾਹਰਨ ਲਈ, ਇੱਕ ਕਵਿਤਾ, ਪ੍ਰਸ਼ਨਾਂ ਦੀ ਇੱਕ ਕਵਿਜ਼ ਆਦਿ।
- **ਜਾਣਕਾਰੀ ਲੱਭਣਾ**। ਜਿਵੇਂ ਪ੍ਰੌਂਪਟ 'ਵੈੱਬ ਵਿਕਾਸ ਵਿੱਚ CORS ਦਾ ਕੀ ਮਤਲਬ ਹੈ?' ਵਰਗੀਆਂ ਜਾਣਕਾਰੀਆਂ ਲਈ।
- **ਕੋਡ ਜਿਨਰੇਟ ਕਰੋ**। ਇਹਨਾਂ ਪ੍ਰੌਂਪਟ ਨਾਲ ਤੁਸੀਂ ਕੋਡ ਬਣਾ ਸਕਦੇ ਹੋ, ਜਿਵੇਂ ਇਮੇਲ ਵੈਰੀਫਿਕੇਸ਼ਨ ਲਈ ਰੈਗੁਲਰ ਐਕਸਪ੍ਰੈਸ਼ਨ ਹੋਵੇ ਜਾਂ ਪੂਰੀ ਐਪ ਬਣਾਉਣ ਲਈ।

## ਇਕ ਹੋਰ ਵਿਆਵਹਾਰਿਕ ਉਦਾਹਰਨ: ਰੈਸੀਪੀ ਜਿਨਰੇਟਰ

ਸੋਚੋ ਤੁਹਾਡੇ ਕੋਲ ਘਰ ਵਿੱਚ ਕੁਝ ਸਾਮੱਗਰੀ ਹੈ ਤੇ ਤੁਸੀਂ ਕੁਝ ਬਣਾਉਣੇ ਹੋ। ਇਸ ਲਈ ਤੁਹਾਨੂੰ ਇੱਕ ਰੈਸੀਪੀ ਚਾਹੀਦੀ ਹੈ। ਰੈਸੀਪੀ ਖੋਜਣ ਲਈ ਤੁਸੀਂ ਖੋਜ ਇੰਜਨਾਂ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ ਜਾਂ LLM ਦੀ।

ਤੁਸੀਂ ਇਸ ਤਰ੍ਹਾਂ ਦਾ ਪ੍ਰੌਂਪਟ ਲਿਖ ਸਕਦੇ ਹੋ:

> "ਨਿਮਨਲਿਖਤ ਸਮਗਰੀ ਨਾਲ ਬਣਾਏ ਜਾ ਸਕਣ ਵਾਲੇ 5 ਪਕਵਾਨਾਂ ਦੀ ਲਿਸਟ ਦਿਖਾਓ: ਚਿਕਨ, ਆਲੂ ਅਤੇ ਗਾਜਰ। ਹਰ ਰੈਸੀਪੀ ਵਿੱਚ ਵਰਤੀ ਗਈ ਸਾਰੀਆਂ ਸਮਗਰੀ ਬਤਾਓ।"

ਇਸ ਪ੍ਰੌਂਪਟ ਤੇ ਇੱਕ ਉੱਤਰ ਇੰਝ ਹੋ ਸਕਦਾ ਹੈ:

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

ਇਹ ਨਤੀਜਾ ਚੰਗਾ ਹੈ, ਹੁਣ ਮੈਂ ਸਮਝ ਗਿਆ ਕਿ ਕੀ ਬਣਾਉਣਾ ਹੈ। ਇਸ ਵੇਲੇ ਕੁਝ ਸੁਧਾਰ ਹਨ:

- ਉਹ ਸਮੱਗਰੀ ਫਿਲਟਰ ਕਰਨਾ ਜੋ ਮੈਂ ਪਸੰਦ ਨਹੀਂ ਕਰਦਾ ਜਾਂ ਜਿਸ ਤੋਂ ਮੈਂ ਐਲਰਜੀਕ ਹਾਂ।
- ਖਰੀਦਦਾਰੀ ਦੀ ਸੂਚੀ ਬਣਾਉਣਾ, ਜੇ ਮੇਰੇ ਕੋਲ ਕੁਝ ਸਮੱਗਰੀ ਘਰ ਵਿੱਚ ਨਹੀਂ ਹੈ।

ਇਸ ਲਈ ਇੱਕ ਹੋਰ ਪ੍ਰੌਂਪਟ ਜੋੜੋ:

> "ਮੇਹਰਬਾਨੀ ਕਰਕੇ ਦਰਦਨੇਯੁਕਤ ਲਸਣ ਵਾਲੀਆਂ ਰੈਸੀਪੀਆਂ ਨੂੰ ਹਟਾਓ ਕਿਉਂਕਿ ਮੈਨੂੰ ਲਸਣ ਨਾਲ ਐਲਰਜੀ ਹੈ। ਇਸ ਦੇ ਨਾਲ ਖਰੀਦਦਾਰੀ ਦੀ ਸੂਚੀ ਵੀ ਬਣਾਓ, ਮਾਨ ਕੇ ਚਲ ਰਹੇ ਹੋ ਕਿ ਮੇਰੇ ਕੋਲ ਚਿਕਨ, ਆਲੂ ਅਤੇ ਗਾਜਰ ਹਨ।"

ਹੁਣ ਤੁਹਾਡੇ ਕੋਲ ਆਉਟਪੁੱਟ ਹੈ:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
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
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
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
- 1 teaspoon dried oregano

Shopping List:
- Olive oil
- Onion
- Thyme
- Oregano
- Salt
- Pepper
```

ਇਹ ਪੰਜ ਰੈਸੀਪੀ ਹਨ, ਜਿਸ ਵਿੱਚ ਲਸਣ ਨਹੀਂ ਹੈ ਅਤੇ ਤੁਹਾਡੇ ਕੋਲ ਖਰੀਦਦਾਰੀ ਦੀ ਸੂਚੀ ਵੀ ਹੈ ਜੋ ਤੁਹਾਡੇ ਮੌਜੂਦਾ ਸਮੱਗਰੀ ਦੇ ਨਾਲ ਹੈ।

## ਅਭਿਆਸ - ਇੱਕ ਰੈਸੀਪੀ ਜਿਨਰੇਟਰ ਬਣਾਓ

ਹੁਣ ਜਦ ਸਾਨੂੰ ਮਾਡਲ ਸਮਝ ਆ ਗਿਆ ਹੈ, ਕੋਡ ਲਿਖ ਕੇ ਇਸ ਦਰਸਾਏ ਪ੍ਰਣਾਲੀ ਨੂੰ ਬਣਾਈਏ।

ਕਦਮ:

1. ਮੌਜੂਦਾ _app.py_ ਫਾਇਲ ਦਾ ਉਪਯੋਗ ਸ਼ੁਰੂਆਤ ਵਜੋਂ ਕਰੋ।
1. `prompt` ਵੈਰੀਏਬਲ ਨੂੰ ਲੱਭੋ ਤੇ ਇਸ ਕੋਡ ਨੂੰ ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਨਾਲ ਬਦਲੋ:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   ਜੇ ਤੁਸੀਂ ਹੁਣ ਕੋਡ ਚਲਾਓਗੇ, ਤਾਂ ਤੁਸੀਂ ਇਸ ਤਰ੍ਹਾਂ ਦਾ ਨਤੀਜਾ ਵੇਖੋਗੇ:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > ਨੋਟ ਕਰੋ, ਤੁਹਾਡਾ LLM ਅਸਥਿਰ ਹੈ, ਇਸ ਲਈ ਹਰ ਵਾਰੀ ਵੱਖਰੇ ਨਤੀਜੇ ਮਿਲ ਸਕਦੇ ਹਨ।

ਸ਼ਾਬਾਸ਼, ਆਪਾਂ ਦੇਖੀਏ ਕਿ ਅਸੀਂ ਕਿਸ ਤਰ੍ਹਾਂ ਚੀਜ਼ਾਂ ਸੁਧਾਰ ਸਕਦੇ ਹਾਂ। ਸੁਧਾਰ ਲਈ ਕੁਝ ਅਜਿਹਾ ਬਣਾਓ ਕਿ ਸਮੱਗਰੀ ਅਤੇ ਰੈਸੀਪੀਆਂ ਦੀ ਗਿਣਤੀ ਅਡਜਸਟ ਕੀਤੀ ਜਾ ਸਕੇ।

1. ਕੋਡ ਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਬਦਲੋ:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # ਪ੍ਰੰਪਟ ਅਤੇ ਸਮੱਗਰੀ ਵਿੱਚ ਰੈਸੀਪੀ ਦੀ ਗਿਣਤੀ ਨੂੰ ਦਰਜ ਕਰੋ
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

ਤੈਸਤ ਰਨ ਲਈ ਕੋਡ ਕੁਝ ਇਸ ਤਰ੍ਹਾਂ ਹੋ ਸਕਦਾ ਹੈ:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### ਫਿਲਟਰ ਅਤੇ ਖਰੀਦਦਾਰੀ ਦੀ ਸੂਚੀ ਜੋੜਕੇ ਸੁਧਾਰ ਕਰੋ

ਹੁਣ ਸਾਡੀ ਇੱਕ ਐਪ ਕੰਮ ਕਰ ਰਹੀ ਹੈ ਜੋ ਰੈਸੀਪੀ ਬਣਾ ਸਕਦੀ ਹੈ ਅਤੇ ਯੂਜ਼ਰ ਤੋਂ ਸੂਚਨਾ ਲੈ ਕੇ ਫਲੈਕਸਿਬਲ ਵੀ ਹੈ।

ਹੁਣ ਅਸੀਂ ਇਹ ਚਾਹੁੰਦੇ ਹਾਂ:

- **ਸਮੱਗਰੀ ਫਿਲਟਰ ਕਰੋ**। ਅਸੀਂ ਉਹ ਸਮੱਗਰੀ ਹਟਾਉਣਾ ਚਾਹੁੰਦੇ ਹਾਂ ਜੋ ਪਸੰਦ ਨਹੀਂ ਜਾਂ ਐਲਰਜੀ ਵਾਲੀ ਹੋਵੇ। ਇੱਥੇ, ਅਸੀਂ ਪ੍ਰੌਂਪਟ ਦੇ ਅੰਤ `filter` ਸ਼ਬਦ ਜੋੜ ਰਹੇ ਹਾਂ ਅਤੇ ਯੂਜ਼ਰ ਤੋਂ ਇਹ ਮੁੱਲ ਲੈ ਰਹੇ ਹਾਂ।

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

ਉੱਪਰ `{filter}` ਨੂੰ ਪ੍ਰੌਂਪਟ ਦੇ ਅੰਤ ਵਿਚ ਜੋੜਿਆ ਹੈ ਅਤੇ ਯੂਜ਼ਰ ਤੋਂ ਫਿਲਟਰ ਮੁੱਲ ਲਿਆ ਗਿਆ ਹੈ।

ਪ੍ਰੋਗਰਾਮ ਚਲਾਉਂਦੇ ਸਮੇਂ ਇੱਕ ਉਦਾਹਰਨ ਇੰਪੁਟ ਇੰਝ ਹੋ ਸਕਦਾ ਹੈ:

  ```output
  No of recipes (for example, 5): 3
  List of ingredients (for example, chicken, potatoes, and carrots): onion,milk
  Filter (for example, vegetarian, vegan, or gluten-free): no milk

  1. French Onion Soup

  Ingredients:

  -1 large onion, sliced
  -3 cups beef broth
  -1 cup milk
  -6 slices french bread
  -1/4 cup shredded Parmesan cheese
  -1 tablespoon butter
  -1 teaspoon dried thyme
  -1/4 teaspoon salt
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add beef broth, milk, thyme, salt, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Place french bread slices on soup bowls.
  5. Ladle soup over bread.
  6. Sprinkle with Parmesan cheese.

  2. Onion and Potato Soup

  Ingredients:

  -1 large onion, chopped
  -2 cups potatoes, diced
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add potatoes, vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Serve hot.

  3. Creamy Onion Soup

  Ingredients:

  -1 large onion, chopped
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper
  -1/4 cup all-purpose flour
  -1/2 cup shredded Parmesan cheese

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. In a small bowl, whisk together flour and Parmesan cheese until smooth.
  5. Add to soup and simmer for an additional 5 minutes, or until soup has thickened.
  ```

ਤੁਸੀਂ ਵੇਖ ਰਹੇ ਹੋ ਕਿ ਦੁਧ ਵਾਲੀਆਂ ਰੈਸੀਪੀਆਂ ਹਟਾ ਦਿੱਤੀਆਂ ਗਈਆਂ ਹਨ। ਪਰ ਜੇ ਤੁਸੀਂ ਲੈਕਟੋਜ਼ ਇੰਟੋਲਰੈਂਟ ਹੋ ਤਾਂ ਤੁਸੀਂ ਪਨੀਰ ਵਾਲੀਆਂ ਰੈਸੀਪੀਆਂ ਵੀ ਫਿਲਟਰ ਕਰਨੀ ਚਾਹੁੰਦੇ ਹੋ, ਇਸ ਲਈ ਸਪਸ਼ਟਤਾ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ।

- **ਖਰੀਦਦਾਰੀ ਸੂਚੀ ਬਣਾਓ**। ਜੋ ਸਮੱਗਰੀ ਤੁਹਾਡੇ ਕੋਲ ਘਰ ਵਿੱਚ ਨਹੀਂ ਹੈ, ਉਸਦੇ ਲਈ ਖਰੀਦਦਾਰੀ ਸੂਚੀ ਤਿਆਰ ਕਰੋ।

ਇਸ ਕੰਮ ਲਈ, ਅਸੀਂ ਇੱਕ ਹੀ ਪ੍ਰੌਂਪਟ ਵਿੱਚ ਸਭ ਨਹੀਂ ਕਰਾਂਗੇ। ਅਸੀਂ ਦੋ ਵੱਖਰੇ ਪ੍ਰੌਂਪਟ ਉਤਪਨ ਕਰਾਂਗੇ। ਦੂਜੇ ਪ੍ਰੌਂਪਟ ਵਿੱਚ ਪਹਿਲੇ ਪ੍ਰੌਂਪਟ ਦੇ ਨਤੀਜੇ ਨੂੰ ਸੰਦਰਭ ਵਜੋਂ ਸ਼ਾਮਿਲ ਕਰਨਾ ਹੋਵੇਗਾ।

ਪਹਿਲੇ ਪ੍ਰੌਂਪਟ ਦਾ ਨਤੀਜਾ ਪ੍ਰਿੰਟ ਕਰਨ ਵਾਲੀ ਜਗ੍ਹਾ ਲੱਭੋ ਤੇ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਜੋੜੋ:

  ```python
  old_prompt_result = completion.choices[0].message.content
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  messages = [{"role": "user", "content": new_prompt}]
  completion = openai.Completion.create(engine=deployment_name, messages=messages, max_tokens=1200)

  # ਪ੍ਰਤਿਕਿਰਿਆ ਪ੍ਰਿੰਟ ਕਰੋ
  print("Shopping list:")
  print(completion.choices[0].message.content)
  ```

ਨੋਟ ਕਰੋ:
  1. ਅਸੀਂ ਪਹਿਲੇ ਪ੍ਰਾਂਪਟ ਦੇ ਨਤੀਜੇ ਨੂੰ ਨਵੇਂ ਪ੍ਰਾਂਪਟ ਵਿੱਚ ਜੋੜ ਕੇ ਇੱਕ ਨਵਾਂ ਪ੍ਰਾਂਪਟ ਬਣਾਇਆ ਜਾ ਰਿਹਾ ਹੈ:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. ਅਸੀਂ ਇੱਕ ਨਵੀਂ ਬੇਨਤੀ ਕਰਦੇ ਹਾਂ, ਪਰ ਪਹਿਲੇ ਪ੍ਰਾਂਪਟ ਵਿੱਚ ਪੁੱਛੇ ਗਏ ਟੋਕਨ ਦੀ ਗਿਣਤੀ ਨੂੰ ਵੀ ਧਿਆਨ ਵਿੱਚ ਰੱਖਦੇ ਹਾਂ, ਇਸ ਲਈ ਇਸ ਵਾਰੀ ਅਸੀਂ ਕਹਿੰਦੇ ਹਾਂ ਕਿ `max_tokens` 1200 ਹੈ।

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     ਇਸ ਕੋਡ ਨੂੰ ਚਲਾਉਂਦੇ ਹੋਏ, ਅਸੀਂ ਹੁਣ ਹੇਠ ਲਿਖੇ ਨਤੀਜੇ ਤੱਕ ਪਹੁੰਚਦੇ ਹਾਂ:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## ਆਪਣੀ ਸੈਟਅਪ ਨੂੰ ਸੁਧਾਰੋ

ਹੁਣ ਤੱਕ ਜੋ ਕੁਝ ਹੈ ਉਹ ਕੰਮ ਕਰਨ ਵਾਲਾ ਕੋਡ ਹੈ, ਪਰ ਕੁਝ ਸੋਧਾਂ ਹੋਣੀਆਂ ਚਾਹੀਦੀਆਂ ਹਨ ਤਾਂ ਜੋ ਚੀਜ਼ਾਂ ਹੋਰ ਬਿਹਤਰ ਬਣ ਸਕਣ। ਕੁਝ ਚੀਜ਼ਾਂ ਜੋ ਸਾਨੂੰ ਕਰਨੀ ਚਾਹੀਦੀਆਂ ਹਨ:

- **ਕੋਡ ਤੋਂ ਰਾਜ਼ਾਂ ਨੂੰ ਵੱਖਰਾ ਕਰੋ**, ਜਿਵੇਂ ਕਿ ਏਪੀਅਈ ਕੁੰਜੀ। ਰਾਜ਼ ਕੋਡ ਵਿੱਚ ਨਹੀਂ ਹੋਣੇ ਚਾਹੀਦੇ ਅਤੇ ਇੱਕ ਸੁਰੱਖਿਅਤ ਜਗ੍ਹਾ ਤੇ ਸਟੋਰ ਕਰਨੇ ਚਾਹੀਦੇ ਹਨ। ਰਾਜ਼ਾਂ ਨੂੰ ਕੋਡ ਤੋਂ ਵੱਖਰਾ ਕਰਨ ਲਈ ਅਸੀਂ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਅਤੇ `python-dotenv` ਵਰਗੀਆਂ ਲਾਇਬਰੇਰੀਜ਼ ਨੂੰ ਵਰਤ ਸਕਦੇ ਹਾਂ ਜੋ ਇਨ੍ਹਾਂ ਨੂੰ ਕਿਸੇ ਫਾਇਲ ਤੋਂ ਲੋਡ ਕਰ ਸਕਦੀਆਂ ਹਨ। ਕੋਡ ਵਿੱਚ ਇਹ ਧਰਾਂ ਇਸ ਤਰ੍ਹਾਂ ਦਿਖਾਈ ਦੇਵੇਗਾ:

  1. ਇੱਕ `.env` ਫਾਇਲ ਬਣਾਓ ਜਿਸ ਵਿੱਚ ਹੇਠ ਲਿਖਿਆ ਸਮੱਗਰੀ ਹੋਵੇ:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > ਧਿਆਨ ਦਿਉ, Azure ਲਈ, ਸਾਨੂੰ ਹੇਠ ਲਿਖੇ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਸੈੱਟ ਕਰਨੇ ਪੈਂਦੇ ਹਨ:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     ਕੋਡ ਵਿੱਚ, ਤੁਸੀਂ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਲੋਡ ਕਰੋਗੇ:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **ਟੋਕਨ ਲੰਬਾਈ ਬਾਰੇ ਇੱਕ ਗੱਲ**। ਸਾਨੂੰ ਸੋਚਣਾ ਚਾਹੀਦਾ ਹੈ ਕਿ ਸਾਨੂੰ ਜਿਨ੍ਹਾਂ ਟੋਕੇਨ ਦੀ ਲੋੜ ਹੈ ਉਹ ਟੈਕਸਟ ਬਨਾਉਣ ਲਈ ਕਿੰਨੇ ਹਨ। ਟੋਕਨ ਪੈਸੇ ਖਰਚ ਕਰਦੇ ਹਨ, ਇਸ ਲਈ ਜਿੱਥੇ ਸੰਭਵ ਹੋਵੇ, ਸਾਨੂੰ ਟੋਕਨਾਂ ਦੀ ਗਿਣਤੀ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖਣਾ ਚਾਹੀਦਾ ਹੈ। ਉਦਾਹਰਣ ਵਜੋਂ, ਕੀ ਅਸੀਂ ਪ੍ਰਾਂਪਟ ਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਬਣਾ ਸਕਦੇ ਹਾਂ ਤਾਂ ਜੋ ਘੱਟ ਟੋਕਨ ਵਰਤੇ ਜਾ ਸਕਣ?

  ਟੋਕਨਾਂ ਨੂੰ ਬਦਲਣ ਲਈ, ਤੁਸੀਂ `max_tokens` ਪੈਰਾਮੀਟਰ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ। ਜਿਵੇਂ ਕਿ ਜੇ ਤੁਸੀਂ 100 ਟੋਕਨ ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਇਸ ਤਰ੍ਹਾਂ ਕਰੋਗੇ:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **ਟੈਮਪਰੇਚਰ ਨਾਲ ਪ੍ਰਯੋਗ ਕਰਨਾ**। ਟੈਮਪਰੇਚਰ ਇੱਕ ਅਜਿਹੀ ਚੀਜ਼ ਹੈ ਜਿਸਦਾ ਅਸੀਂ ਅਜੇ ਤਕ ਜ਼ਿਕਰ ਨਹੀਂ ਕੀਤਾ ਪਰ ਇਹ ਸਾਡੇ ਪ੍ਰੋਗਰਾਮ ਦੇ ਕੰਮ ਕਰਨ ਦਾ ਮਹੱਤਵਪੂਰਨ ਸੰਦਰਭ ਹੈ। ਜਿੰਨੀ ਵੱਧ ਟੈਮਪਰੇਚਰ ਦੀ ਕੀਮਤ ਹੋਵੇਗੀ, ਆਉਟਪੁੱਟ ਉਤਨਾ ਜ਼ਿਆਦਾ ਬੇਤਰਤੀਬ ਹੋਵੇਗਾ। ਇਸਦੇ ਉਲਟ, ਜਿੰਨੀ ਘੱਟ ਟੈਮਪਰੇਚਰ ਦੀ ਕੀਮਤ ਹੋਏਗੀ, ਆਉਟਪੁੱਟ ਓਨਾ ਜ਼ਿਆਦਾ ਪੂਰਵਨੀਰਧਾਰਿਤ ਹੋਵੇਗਾ। ਸੋਚੋ ਕਿ ਤੁਸੀਂ ਆਪਣੀ ਆਉਟਪੁੱਟ ਵਿੱਚ ਵੈਰੀਏਸ਼ਨ ਚਾਹੁੰਦੇ ਹੋ ਜਾਂ ਨਹੀਂ।

  ਟੈਮਪਰੇਚਰ ਬਦਲਣ ਲਈ, ਤੁਸੀਂ `temperature` ਪੈਰਾਮੀਟਰ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ। ਉਦਾਹਰਣ ਵਜੋਂ, ਜੇ ਤੁਸੀਂ 0.5 ਦਾ ਟੈਮਪਰੇਚਰ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਇਹ ਕਰੋਗੇ:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > ਧਿਆਨ ਦਿਓ, ਜਿੰਨਾ ਨਜ਼ਦੀਕ 1.0 ਹੋਵੇਗਾ, ਆਉਟਪੁੱਟ ਉਤਨਾ ਹੀ ਵੱਖਰਾ/ਵਿਭਿੰਨ ਹੋਏਗਾ।

## ਅਸਾਈਨਮੈਂਟ

ਇਸ ਅਸਾਈਨਮੈਂਟ ਲਈ, ਤੁਸੀਂ ਚੁਣ ਸਕਦੇ ਹੋ ਕਿ ਕੀ ਬਣਾਉਣਾ ਹੈ।

ਕੁਝ ਸੁਝਾਵ ਹੇਠਾਂ ਦਿੱਤੇ ਗਏ ਹਨ:

- ਰੈਸਪੀ ਜੇਨੇਰੇਟਰ ਐਪ ਨੂੰ ਹੋਰ ਬਿਹਤਰ ਕਰਨ ਲਈ ਸੋਧ ਕਰੋ। ਟੈਮਪਰੇਚਰ ਦੀਆਂ ਵੈਲਯੂਜ਼ ਅਤੇ ਪ੍ਰਾਂਪਟਸ ਨਾਲ ਖੇਡੋ ਅਤੇ ਦੇਖੋ ਕਿ ਤੁਸੀਂ ਕੀ ਕੱਢ ਸਕਦੇ ਹੋ।
- ਇੱਕ "ਸਟਡੀ ਬੱਡੀ" ਬਣਾਓ। ਇਹ ਐਪ ਕਿਸੇ ਵਿਸ਼ੇ ਬਾਰੇ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਦੇ ਸਕਦੀ ਹੈ, ਉਦਾਹਰਣ ਵਜੋਂ Python। ਤੁਸੀਂ ਪ੍ਰਾਂਪਟਸ ਵਰਗੇ "Python ਵਿੱਚ ਕਿਸੇ ਵਿਸ਼ੇ ਦਾ ਕੀ ਹੈ?" ਜਾਂ "ਮੈਨੂੰ ਕਿਸੇ ਵਿਸ਼ੇ ਦਾ ਕੋਡ ਦਿਖਾਓ" ਰੱਖ ਸਕਦੇ ਹੋ।
- ਹਿਸਟਰੀ ਬੋਟ, ਇਤਿਹਾਸ ਨੂੰ ਜੀਉਂਦਾ ਬਣਾਓ, ਬੋਟ ਨੂੰ ਦੱਸੋ ਕਿ ਉਹ ਕਿਸੇ ਇਤਿਹਾਸੀ ਪਾਤਰ ਦੀ ਭੂਮਿਕਾ ਨਿਭਾਏ ਅਤੇ ਉਸਦੀ ਜ਼ਿੰਦਗੀ ਅਤੇ ਸਮੇਂ ਬਾਰੇ ਸਵਾਲ ਪੁੱਛੋ।

## ਹੱਲ

### ਸਟਡੀ ਬੱਡੀ

ਹੇਠਾਂ ਇੱਕ ਸ਼ੁਰੂਆਤੀ ਪ੍ਰਾਂਪਟ ਦਿੱਤੀ ਗਈ ਹੈ, ਦੇਖੋ ਕਿ ਤੁਸੀਂ ਇਸਦੀ ਵਰਤੋਂ ਕਿਵੇਂ ਕਰ ਸਕਦੇ ਹੋ ਅਤੇ ਆਪਣੇ ਮਨਪਸੰਦ ਤਰੀਕੇ ਨਾਲ ਸੋਧ ਕਰ ਸਕਦੇ ਹੋ।

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### ਹਿਸਟਰੀ ਬੋਟ

ਇਥੇ ਕੁਝ ਪ੍ਰਾਂਪਟਸ ਹਨ ਜਿਨ੍ਹਾਂ ਦੀ ਤੁਸੀਂ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## ਗਿਆਨ ਦੀ ਜਾਂਚ

ਟੈਮਪਰੇਚਰ ਸੰਕਲਪ ਕੀ ਕਰਦਾ ਹੈ?

1. ਇਹ ਨਿਰਧਾਰਿਤ ਕਰਦਾ ਹੈ ਕਿ ਆਉਟਪੁੱਟ ਕਿੰਨਾ ਬੇਤਰਤੀਬ ਹੈ।
1. ਇਹ ਨਿਰਧਾਰਿਤ ਕਰਦਾ ਹੈ ਕਿ ਜਵਾਬ ਕਿੰਨਾ ਬੱਡਾ ਹੈ।
1. ਇਹ ਨਿਰਧਾਰਿਤ ਕਰਦਾ ਹੈ ਕਿ ਕਿੰਨੇ ਟੋਕੇਨ ਵਰਤੇ ਜਾਂਦੇ ਹਨ।

## 🚀 ਚੈਲੀੰਜ

ਅਸਾਈਨਮੈਂਟ ‘ਤੇ ਕੰਮ ਕਰਦੇ ਸਮੇਂ, ਟੈਮਪਰੇਚਰ ਵੱਖਰੇ ਵੱਖਰੇ ਸੈਟਿੰਗ ਵਿੱਚ ਟ੍ਰਾਈ ਕਰੋ, ਜਿਵੇਂ 0, 0.5 ਅਤੇ 1। ਯਾਦ ਰੱਖੋ ਕਿ 0 ਸਭ ਤੋਂ ਘੱਟ ਵੱਖਰਾ ਹੈ ਅਤੇ 1 ਸਭ ਤੋਂ ਵੱਧ। ਤੁਹਾਡੇ ਐਪ ਲਈ ਕਿਹੜੀ ਕੀਮਤ ਸਭ ਤੋਂ ਵਧੀਆ ਕੰਮ ਕਰਦੀ ਹੈ?

## ਸ਼ਾਬਾਸ਼! ਆਪਣਾ ਸਿੱਖਿਆ ਜਾਰੀ ਰੱਖੋ

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਸਾਡੀ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ਵੇਖੋ, ਇਸ ਨਾਲ ਤੁਸੀਂ ਆਪਣਾ Generative AI ਗਿਆਨ ਵਧਾ ਸਕਦੇ ਹੋ!

ਲੈਸਨ 7 'ਤੇ ਚੱਲੋ ਜਿੱਥੇ ਅਸੀਂ ਦੇਖਾਂਗੇ ਕਿ ਕਿਵੇਂ [ਚੈਟ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਈਏ](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->