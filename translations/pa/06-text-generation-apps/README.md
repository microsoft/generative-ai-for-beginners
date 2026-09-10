# ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣਾ

[![ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣਾ](../../../translated_images/pa/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(ਇਸ ਪਾਠ ਦੀ ਵੀਡੀਓ ਦੇਖਣ ਲਈ ਉਪਰ ਦਿੱਤੀ ਬੀਮ ਨੂੰ ਕਲਿੱਕ ਕਰੋ)_

ਇਸ ਕਰਿਕੁਲਮ ਵਿਚ ਤੁਸੀਂ ਹੁਣ ਤੱਕ ਵੇਖਿਆ ਹੈ ਕਿ ਮੁੱਖ ਸੰਕਲਪ ਜਿਵੇਂ ਪ੍ਰੰਪਟਸ ਹਨ ਅਤੇ ਇੱਕ ਪੂਰਾ ਵਿਭਾਗ ਹੈ ਜਿਸ ਨੂੰ "prompt engineering" ਕਹਿੰਦੇ ਹਨ। ਬਹੁਤ ਸਾਰੇ ٹੂਲਸ ਜਿਵੇਂ ChatGPT, Office 365, Microsoft Power Platform ਅਤੇ ਹੋਰ ਤੁਹਾਨੂੰ ਪ੍ਰੰਪਟਸ ਵਰਤ ਕੇ ਕਿਸੇ ਕੰਮ ਨੂੰ ਪੂਰਾ ਕਰਨ ਵਿੱਚ ਸਹਾਇਤਾ ਕਰਦੇ ਹਨ।

ਤਾਂ ਤੁਹਾਨੂੰ ਐਪ ਵਿੱਚ ਐਸਾ ਅਨੁਭਵ ਸ਼ਾਮਲ ਕਰਨ ਲਈ, ਤੁਹਾਨੂੰ ਪ੍ਰੰਪਟਸ, ਕੰਪਲੀਸ਼ਨਸ ਵਰਗੇ ਸੰਕਲਪ ਸਮਝਣੇ ਪੈਣਗੇ ਅਤੇ ਕੰਮ ਕਰਨ ਲਈ ਕੋਈ ਲਾਇਬ੍ਰੇਰੀ ਚੁਣਨੀ ਪਵੇਗੀ। ਇਹੀ ਤੁਹਾਨੂੰ ਇਸ ਅਧਿਆਇ ਵਿੱਚ ਸਿੱਖਾਇਆ ਜਾਵੇਗਾ।

## ਪਰਿਚਯ

ਇਸ ਅਧਿਆਇ ਵਿੱਚ, ਤੁਸੀਂ:

- openai ਲਾਇਬ੍ਰੇਰੀ ਅਤੇ ਇਸ ਦੇ ਮੁੱਖ ਸੰਕਲਪਾਂ ਬਾਰੇ ਜਾਣੋਗੇ।
- openai ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਕ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਬਣਾਵੋਗੇ।
- ਪ੍ਰੰਪਟ, ਤਾਪਮਾਨ, ਅਤੇ ਟੋਕਨ ਵਰਗੇ ਸੰਕਲਪਾਂ ਨੂੰ ਸਮਝ ਕੇ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਬਨਾਉਣਾ ਸਿੱਖੋਗੇ।

## ਸਿੱਖਣ ਦੇ 목표

ਇਸ ਪਾਠ ਦੇ ਅੰਤ 'ਤੇ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ ਕਿ:

- ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਕੀ ਹੁੰਦੀ ਹੈ, ਇਸ ਦੀ ਵਿਆਖਿਆ ਕਰ ਸਕੋ।
- openai ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਬਣਾ ਸਕੋ।
- ਆਪਣੇ ਐਪ ਲਈ ਵੱਧ ਜਾਂ ਘੱਟ ਟੋਕਨ ਵਰਤੋਂ ਅਤੇ ਤਾਪਮਾਨ ਬਦਲ ਕੇ ਵੱਖ-ਵੱਖ ਨਤੀਜੇ ਬਣਾਉਣ ਲਈ ਸੰਰਚਨਾ ਕਰ ਸਕੋ।

## ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਕੀ ਹੈ?

ਆਮ ਤੌਰ 'ਤੇ ਜਦੋਂ ਤੁਸੀਂ ਕੋਈ ਐਪ ਬਣਾਉਂਦੇ ਹੋ ਤਾਂ ਇਸ ਦਾ ਕੁਝ ਤਰ੍ਹਾਂ ਦਾ ਇੰਟਰਫੇਸ ਹੁੰਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ ਹੇਠਾਂ ਦਿੱਤਾ ਗਿਆ:

- ਕਮਾਂਡ-ਅਧਾਰਤ। ਕੰਸੋਲ ਐਪ ਆਮ ਤੌਰ 'ਤੇ ਉਹ ਐਪ ਹੁੰਦੇ ਹਨ ਜਿੱਥੇ ਤੁਸੀਂ ਕੋਈ ਕਮਾਂਡ ਲਿਖਦੇ ਹੋ ਅਤੇ ਇਹ ਓਹ ਕੰਮ ਕਰਦਾ ਹੈ। ਉਦਾਹਰਨ ਵਜੋਂ, `git` ਇੱਕ ਕਮਾਂਡ-ਅਧਾਰਤ ਐਪ ਹੈ।
- ਯੂਜ਼ਰ ਇੰਟਰਫੇਸ(UI)। ਕੁਝ ਐਪ ਵਿੱਚ ਗ੍ਰਾਫ਼ਿਕਲ ਯੂਜ਼ਰ ਇੰਟਰਫੇਸ (GUI) ਹੁੰਦਾ ਹੈ ਜਿੱਥੇ ਤੁਸੀਂ ਬਟਨ ਕਲਿੱਕ ਕਰਦੇ ਹੋ, ਟੈਕਸਟ ਦਰਜ ਕਰਦੇ ਹੋ, ਵਿਕਲਪ ਚੁਣਦੇ ਹੋ ਆਦਿ।

### ਕੰਸੋਲ ਅਤੇ UI ਐਪ ਸੀਮਿਤ ਹਨ

ਇਸਦਾ ਤੁਲਨਾ ਇੱਕ ਕਮਾਂਡ-ਅਧਾਰਤ ਐਪ ਨਾਲ ਕਰੋ ਜਿੱਥੇ ਤੁਸੀਂ ਕਮਾਂਡ ਲਿਖਦੇ ਹੋ:

- **ਇਹ ਸੀਮਿਤ ਹੈ**। ਤੁਸੀਂ ਕੋਈ ਭੀ ਕਮਾਂਡ ਨਹੀਂ ਲਿਖ ਸਕਦੇ, ਸਿਰਫ ਉਹੀ ਜੋ ਐਪ ਸਮਰਥਨ ਕਰਦਾ ਹੈ।
- **ਭਾਸ਼ਾ ਵਿਸ਼ੇਸ਼**। ਕੁਝ ਐਪ ਬਹੁਤ ਸਾਰੀਆਂ ਭਾਸ਼ਾਵਾਂ ਦਾ ਸਮਰਥਨ ਕਰਦੇ ਹਨ, ਪਰ ਆਮ ਤੌਰ 'ਤੇ ਇਹ ਕਿਸੇ ਇੱਕ ਭਾਸ਼ਾ ਲਈ ਬਣਾਏ ਜਾਂਦੇ ਹਨ, ਹਾਲਾਂਕਿ ਤੁਸੀਂ ਹੋਰ ਭਾਸ਼ਾਵਾਂ ਦਾ ਸਹਿਯੋਗ ਜੋੜ ਸਕਦੇ ਹੋ।

### ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਦੇ ਫਾਇਦੇ

ਤਾਂ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਕਿਸ ਤਰ੍ਹਾਂ ਵੱਖਰਾ ਹੁੰਦਾ ਹੈ?

ਇੱਕ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਵਿੱਚ ਤੁਹਾਡੇ ਕੋਲ ਵੱਧ ਲਚੀਲਾਪਨ ਹੁੰਦਾ ਹੈ, ਤੁਸੀਂ ਕਿਸੇ ਕਰਮਾਂ ਜਾਂ ਕਿਸੇ ਨਿਰਧਾਰਤ ਭਾਸ਼ਾ ਨਾਲ ਸੀਮਤ ਨਹੀਂ ਹੁੰਦੇ। ਇਸ ਦੀ ਬਜਾਏ, ਤੁਸੀਂ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਐਪ ਨਾਲ ਬਾਤਚੀਤ ਕਰ ਸਕਦੇ ਹੋ। ਹੋਰ ਫਾਇਦਾ ਇਹ ਹੈ ਕਿ ਤੁਸੀਂ ਆਪਣੀ ਜਾਣਕਾਰੀ ਦੇ ਵੱਡੇ ਸਟੋਰ ਤੇ ਟ੍ਰੇਨ ਕੀਤੇ ਗਏ ਡੇਟਾ ਸਰੋਤ ਨਾਲ ਬਾਤ ਕਰ ਰਹੇ ਹੋ, ਜਦਕਿ ਪਰੰਪਰਾ ਐਪ ਡੇਟਾਬੇਸ ਵਿਚਕਾਰ ਸੀਮਿਤ ਰਹਿ ਸਕਦਾ ਹੈ।

### ਮੈਂ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਨਾਲ ਕੀ ਬਣਾਉਂ ਸਕਦਾ ਹਾਂ?

ਤੁਸੀਂ ਕਈ ਚੀਜ਼ਾਂ ਬਣਾ ਸਕਦੇ ਹੋ। ਉਦਾਹਰਨ ਵਜੋਂ:

- **ਚੈਟਬੋਟ**। ਆਪਣੀ ਕੰਪਨੀ ਅਤੇ ਇਸ ਦੇ ਉਤਪਾਦਾਂ ਬਾਰੇ ਸਵਾਲਾਂ ਦਾ ਜਵਾਬ ਦੇਣ ਵਾਲਾ ਚੈਟਬੋਟ ਇੱਕ ਵਧੀਆ ਚੋਣ ਹੋ ਸਕਦਾ ਹੈ।
- **ਸਹਾਇਕ**। LLM ਟੈਕਸਟ ਦੇ ਸੰਖੇਪ, ਜਾਣਕਾਰੀ ਲੈਣਾ, ਬਾਇਓਡੇਟਾ ਆਦਿ ਵਰਗੀਆਂ ਚੀਜ਼ਾਂ ਕਰਨ ਵਿੱਚ ਮਹਾਨ ਹਨ।
- **ਕੋਡ ਸਹਾਇਕ**। ਤੁਸੀਂ ਜਿਸ ਭਾਸ਼ਾ ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋ ਉਸਤੋਂ ਅਨੁਸਾਰ ਤੁਸੀਂ ਇੱਕ ਕੋਡ ਮਦਦਗਾਰ ਬਣਾ ਸਕਦੇ ਹੋ ਜੋ ਤੂੰਹਾਨੂੰ ਕੋਡ ਲਿਖਣ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ। ਉਦਾਹਰਨ ਵਜੋਂ, ਤੁਸੀਂ GitHub Copilot ਜਿਹਾ ਉਤਪਾਦ ਅਤੇ ChatGPT ਵਰਤ ਕੇ ਕੋਡ ਲਿਖਣ ਵਿੱਚ ਮਦਦ ਲੈ ਸਕਦੇ ਹੋ।

## ਮੈਂ ਕਿਵੇਂ ਸ਼ੁਰੂ ਕਰਾਂ?

ਖੈਰ, ਤੁਹਾਨੂੰ ਕਿਸੇ LLM ਨਾਲ ਇੰਟਿਗ੍ਰੇਟ ਕਰਨ ਦਾ ਤਰੀਕਾ ਲੱਭਣਾ ਹੈ ਜੋ ਆਮ ਤੌਰ 'ਤੇ ਦੋ ਤਰੀਕਿਆਂ 'ਤੇ ਆਧਾਰਿਤ ਹੁੰਦਾ ਹੈ:

- API ਦੀ ਵਰਤੋਂ ਕਰੋ। ਇੱਥੇ ਤੁਸੀਂ ਆਪਣੇ ਪ੍ਰੰਪਟ ਨਾਲ ਵੈੱਬ ਰੀਕਵੇਸਟ ਤਿਆਰ ਕਰਦੇ ਹੋ ਅਤੇ ਜਨਰੇਟ ਕੀਤਾ ਗਿਆ ਟੈਕਸਟ ਵਾਪਸ ਲੈਂਦੇ ਹੋ।
- ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਵਰਤੋਂ ਕਰੋ। ਲਾਇਬ੍ਰੇਰੀਜ਼ API ਕਾਲਾਂ ਨੂੰ ਸਮੇਤ ਕੇ ਉਨ੍ਹਾਂ ਦੀ ਵਰਤੋਂ ਨੂੰ ਆਸਾਨ ਬਣਾਉਂਦੀ ਹੈ।

## ਲਾਇਬ੍ਰੇਰੀਆਂ/SDKs

LLMs ਨਾਲ ਕੰਮ ਕਰਨ ਲਈ ਕੁਝ ਜ਼ਿਆਦਾ ਮਸ਼ਹੂਰ ਲਾਇਬ੍ਰੇਰੀਆਂ ਹਨ ਜਿਵੇਂ:

- **openai**, ਇਹ ਲਾਇਬ੍ਰੇਰੀ ਤੁਹਾਡੇ ਮਾਡਲ ਨਾਲ ਜੁੜਨ ਅਤੇ ਪ੍ਰੰਪਟ ਭੇਜਣ ਨੂੰ ਆਸਾਨ ਬਣਾ ਦਿੰਦੀ ਹੈ।

ਫਿਰ ਕੁਝ ਉੱਚ ਪੱਧਰੀ ਲਾਇਬ੍ਰੇਰੀਆਂ ਹਨ ਜਿਵੇਂ:

- **Langchain**। Langchain ਮਸ਼ਹੂਰ ਹੈ ਅਤੇ Python ਦਾ ਸਮਰਥਨ ਕਰਦਾ ਹੈ।
- **Semantic Kernel**। Semantic Kernel ਮਾਇਕਰੋਸਾਫਟ ਦੀ ਲਾਇਬ੍ਰੇਰੀ ਹੈ ਜੋ C#, Python ਅਤੇ Java ਭਾਸ਼ਾਵਾਂ ਨੂੰ ਸਮਰਥਨ ਦਿੰਦੀ ਹੈ।

## openai ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪਹਿਲੀ ਐਪ

ਆਓ ਵੇਖੀਏ ਕਿ ਅਸੀਂ apni ਪਹਿਲੀ ਐਪ ਕਿਵੇਂ ਬਣਾ ਸਕਦੇ ਹਾਂ, ਕਿਹੜੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਦੀ ਜਰੂਰਤ ਹੈ ਅਤੇ ਕਿੰਨੀ ਖ਼ੁਰਾਕ ਚਾਹੀਦੀ ਹੈ।

### openai ਇੰਸਟਾਲ ਕਰੋ

ਬਾਜ਼ਾਰ ਵਿੱਚ ਕਈ ਲਾਇਬ੍ਰੇਰੀਆਂ ਹਨ ਜੋ OpenAI ਜਾਂ Azure OpenAI ਨਾਲ ਇੰਟਰੈਕਟ ਕਰਨ ਲਈ ਹਨ। ਤੁਸੀਂ ਕਈ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ ਵਰਤ ਸਕਦੇ ਹੋ ਜਿਵੇਂ C#, Python, JavaScript, Java ਆਦਿ। ਅਸੀਂ `openai` Python ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਚੋਣ ਕੀਤੀ ਹੈ, ਇਸ ਲਈ ਅਸੀਂ `pip` ਵਰਤ ਕੇ ਇਸਨੂੰ ਇੰਸਟਾਲ ਕਰਵਾਏਂਗੇ।

```bash
pip install openai
```

### ਇੱਕ ਸਰੋਤ ਬਣਾਓ

ਤੁਹਾਨੂੰ ਨਿਮਨਲਿਖਤ ਕਦਮ ਕਰਨੇ ਹੋਣਗੇ:

- Azure 'ਤੇ ਇੱਕ ਖਾਤਾ ਬਣਾਓ [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)।
- Azure OpenAI ਤੱਕ ਪਹੁੰਚ ਪ੍ਰਾਪਤ ਕਰੋ। ਜਾਓ [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) ਅਤੇ ਐਕਸੇਸ ਦੀ ਬੇਨਤੀ ਕਰੋ।

  > [!NOTE]
  > ਲਿਖਤ ਦੇ ਸਮੇਂ ਤੇ, ਤੁਹਾਨੂੰ Azure OpenAI ਲਈ ਐਕਸੇਸ ਲਈ ਅਰਜ਼ੀ ਦੇਣੀ ਪੈਂਦੀ ਹੈ।

- Python ਨੂੰ ਇੰਸਟਾਲ ਕਰੋ <https://www.python.org/>
- ਇੱਕ Azure OpenAI ਸੇਵਾ ਸਰੋਤ ਬਣਾਇਆ ਹੋਇਆ ਹੋਵੇ। ਇਸ ਗਾਈਡ ਦੇਖੋ ਕਿ ਕਿਵੇਂ [ਇੱਕ ਸਰੋਤ ਬਣਾਇਆ ਜਾਂਦਾ ਹੈ](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)।

### API ਕੁੰਜੀ ਅਤੇ ਐਂਡਪੌਇੰਟ ਲੱਭੋ

ਹੁਣ ਤੁਹਾਨੂੰ ਆਪਣੀ `openai` ਲਾਇਬ੍ਰੇਰੀ ਨੂੰ ਦੱਸਣਾ ਪੈਂਦਾ ਹੈ ਕਿ ਕਿਹੜੀ API ਕੁੰਜੀ ਵਰਤਣੀ ਹੈ। ਆਪਣੀ API ਕੁੰਜੀ ਲੱਭਣ ਲਈ, ਆਪਣੇ Azure OpenAI ਸਰੋਤ ਦੇ "Keys and Endpoint" ਭਾਗ ਵਿੱਚ ਜਾਓ ਅਤੇ "Key 1" ਦੀ ਕਾਪੀ ਕਰੋ।

![Azure ਪੋਰਟਲ ਵਿੱਚ Keys and Endpoint ਸਰੋਤ ਬਲੇਡ](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

ਹੁਣ ਤੁਸੀਂ ਇਹ ਜਾਣਕਾਰੀ ਕਾਪੀ ਕਰ ਲੀ ਹੈ, ਆਓ ਲਾਇਬ੍ਰੇਰੀਜ਼ ਨੂੰ ਇਸਦੀ ਵਰਤੋਂ ਕਰਨ ਲਈ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼ ਦੇਈਏ।

> [!NOTE]
> ਆਪਣੀ API ਕੁੰਜੀ ਨੂੰ ਕੋਡ ਤੋਂ ਅਲੱਗ ਰੱਖਣਾ ਵਧੀਆ ਹੈ। ਤੁਸੀਂ ਇਹ ਮਾਹੌਲ ਵੈਰੀਏਬਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕਰ ਸਕਦੇ ਹੋ।
>
> - ਮਾਹੌਲ ਵੈਰੀਏਬਲ `OPENAI_API_KEY` ਨੂੰ ਆਪਣੀ API ਕੁੰਜੀ ਸੈੱਟ ਕਰੋ।
>   `export OPENAI_API_KEY='sk-...'`

### Azure ਕਾਨਫਿਗਰੇਸ਼ਨ ਸੈੱਟ ਕਰੋ

ਜੇ ਤੁਸੀਂ Azure OpenAI (ਹੁਣ Microsoft Foundry ਦਾ ਹਿੱਸਾ) ਵਰਤ ਰਹੇ ਹੋ, ਤਾਂ ਇਸ ਤਰ੍ਹਾਂ ਕਾਨਫਿਗਰੇਸ਼ਨ ਸੈੱਟ ਕਰੋ। ਅਸੀਂ ਮਿਆਰੀ `OpenAI` ਕਸਟਮਰ ਨੂੰ Azure OpenAI `/openai/v1/` ਐਂਡਪੌਇੰਟ 'ਤੇ ਦਿੱਖਾ ਰਹੇ ਹਾਂ, ਜੋ Responses API ਨਾਲ ਕੰਮ ਕਰਦਾ ਹੈ ਅਤੇ ਕਿਸੇ `api_version` ਦੀ ਲੋੜ ਨਹੀਂ।

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

ਉਪਰ ਦਿੱਤੇ ਗਏ ਵਿੱਚ ਅਸੀਂ ਹੇਠਾਂ ਦਿੱਤੀ ਗੱਲਾਂ ਸੈੱਟ ਕਰ ਰਹੇ ਹਾਂ:

- `api_key`, ਇਹ ਤੁਹਾਡੀ API ਕੁੰਜੀ ਹੈ ਜੋ Azure ਪੋਰਟਲ ਜਾਂ Microsoft Foundry ਪੋਰਟਲ ਤੋਂ ਮਿਲੀ ਹੈ।
- `base_url`, ਇਹ ਤੁਹਾਡਾ Foundry ਸਰੋਤ ਐਂਡਪੌਇੰਟ ਹੈ ਜਿਸ ਨਾਲ `/openai/v1/` ਜੋੜਿਆ ਹੋਇਆ ਹੈ। ਸਥਿਰ v1 ਐਂਡਪੌਇੰਟ OpenAI ਅਤੇ Azure OpenAI ਦੋਹਾਂ 'ਤੇ ਕੰਮ ਕਰਦਾ ਹੈ ਅਤੇ ਕਿਸੇ `api_version` ਪ੍ਰਬੰਧਨ ਦੀ ਲੋੜ ਨਹੀਂ।

> [!NOTE] > `os.environ` ਮਾਹੌਲ ਦੀਆਂ ਵੈਰੀਏਬਲਾਂ ਨੂੰ ਪੜ੍ਹਦਾ ਹੈ। ਤੁਸੀਂ ਇਸ ਦੀ ਵਰਤੋਂ `AZURE_OPENAI_API_KEY` ਅਤੇ `AZURE_OPENAI_ENDPOINT` ਵਰਗੀਆਂ ਵੈਰੀਏਬਲਾਂ ਪੜ੍ਹਨ ਲਈ ਕਰ ਸਕਦੇ ਹੋ। ਇਨ੍ਹਾਂ ਵੈਰੀਏਬਲਾਂ ਨੂੰ ਆਪਣੀ ਟਰਮੀਨਲ ਵਿੱਚ ਜਾਂ `dotenv` ਜਿਹੀ ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸੈੱਟ ਕਰੋ।

## ਟੈਕਸਟ ਜਨਰੇਟ ਕਰੋ

ਟੈਕਸਟ ਜਨਰੇਟ ਕਰਨ ਦਾ ਤਰੀਕਾ Responses API ਦੀ `responses.create` ਮੈਥਡ ਦੀ ਵਰਤੋਂ ਕਰਨਾ ਹੈ। ਹੇਠਾਂ ਇੱਕ ਉਦਾਹਰਨ ਹੈ:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # ਇਹ ਤੁਹਾਡੇ ਮਾਡਲ ਡਿਪਲੋਇਮੈਂਟ ਦਾ ਨਾਮ ਹੈ
    input=prompt,
    store=False,
)
print(response.output_text)
```

ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ, ਅਸੀਂ ਇੱਕ ਰਿਸਪਾਂਸ ਬਣਾਉਂਦੇ ਹਾਂ ਅਤੇ ਮਾਡਲ ਅਤੇ ਪ੍ਰੰਪਟ ਭੇਜਦੇ ਹਾਂ। ਫਿਰ ਅਸੀਂ ਜਨਰੇਟ ਕੀਤਾ ਗਿਆ ਟੈਕਸਟ `response.output_text` ਰਾਹੀਂ ਪ੍ਰਿੰਟ ਕਰਦੇ ਹਾਂ।

### ਬਹੁ-ਚਰਣ ਚਰਚਾ

Responses API ਦੋਹਾਂ ਇੱਕਲ-ਚਰਣ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਅਤੇ ਬਹੁ-ਚਰਣ ਚੈਟਬੋਟ ਲਈ ਬਹੁਤ موزੂ ਹੈ – ਤੁਸੀਂ `input` ਵਿੱਚ ਸੁਨੇਹਿਆਂ ਦੀ ਸੂਚੀ ਦਿੰਦਿਆਂ ਗੱਲਬਾਤ ਬਣਾਉਂਦੇ ਹੋ:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

ਇਸ ਫੰਕਸ਼ਨਲਿਟੀ 'ਤੇ ਅਗਲੇ ਅਧਿਆਇ ਵਿੱਚ ਹੋਰ ਜਾਣਕਾਰੀ ਦਿੱਤੀ ਜਾਵੇਗੀ।

## ਅਭਿਆਸ - ਤੁਹਾਡੀ ਪਹਿਲੀ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ

ਹੁਣ ਜਦੋਂ ਅਸੀਂ openai ਸੈੱਟਅੱਪ ਅਤੇ ਸੰਰਚਨਾ ਕਰਨਾ ਸਿੱਖ ਲਿਆ ਹੈ, ਤਾਂ ਵਿਕਾਸ ਕਰਨ ਦਾ ਸਮਾਂ ਹੈ। ਆਪਣੇ ਐਪ ਦਾ ਵਿਕਾਸ ਕਰਨ ਲਈ ਹੇਠ ਲਿਖੇ ਕਦਮਾਂ ਦਾ ਪਾਲਣ ਕਰੋ:

1. ਇੱਕ ਵਰਚੁਅਲ ਵਾਤਾਵਰਨ ਬਣਾਓ ਅਤੇ openai ਇੰਸਟਾਲ ਕਰੋ:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > ਜੇ ਤੁਸੀਂ Windows ਵਰਤ ਰਹੇ ਹੋ ਤਾਂ `source venv/bin/activate` ਦੀ ਜਗ੍ਹਾ `venv\Scripts\activate` ਟਾਈਪ ਕਰੋ।

   > [!NOTE]
   > ਆਪਣੀ Azure OpenAI ਕੁੰਜੀ ਲੱਭਣ ਲਈ ਜਾਓ [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) ਅਤੇ `Open AI` ਖੋਜੋ, ਫਿਰ `Open AI resource` ਚੁਣੋ ਅਤੇ ਫੇਰ `Keys and Endpoint` ਵਿੱਚ ਜਾ ਕੇ `Key 1` ਦੀ ਕਾਪੀ ਕਰੋ।

1. ਇੱਕ _app.py_ ਫਾਈਲ ਬਣਾਓ ਅਤੇ ਇਸ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਪਾਓ:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # ਆਪਣਾ ਪੂਰਾ ਕਰਨ ਵਾਲਾ ਕੋਡ ਸ਼ਾਮਿਲ ਕਰੋ
   prompt = "Complete the following: Once upon a time there was a"

   # Responses API ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਬੇਨਤੀ ਬਣਾਓ
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # ਪ੍ਰਤੀਉਤਰ ਪ੍ਰਿੰਟ ਕਰੋ
   print(response.output_text)
   ```

   > [!NOTE]
   > ਜੇ ਤੁਸੀਂ ਸਿੱਧਾ OpenAI (Azure ਨਹੀਂ) ਵਰਤ ਰਹੇ ਹੋ ਤਾਂ `client = OpenAI(api_key="<replace this value with your OpenAI key>")` ਵਰਤੋ (ਕੋਈ `base_url` ਨਹੀਂ) ਅਤੇ ਮਾਡਲ ਨਾਮ ਦੇਵੋ ਜਿਵੇਂ `gpt-5-mini` ਬਜਾਏ ਡਿਪਲੋਇਮੈਂਟ ਨਾਮ ਦੇ।

   ਤੁਹਾਨੂੰ ਹੇਠਾਂ ਵਰਗਾ ਨਤੀਜਾ ਵੇਖਣ ਨੂੰ ਮਿਲੇਗਾ:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## ਵੱਖ-ਵੱਖ ਤਰ੍ਹਾਂ ਦੇ ਪ੍ਰੰਪਟ, ਵੱਖ-ਵੱਖ ਕੰਮਾਂ ਲਈ

ਹੁਣ ਤੁਸੀਂ ਦੇਖ ਚੁੱਕੇ ਹੋ ਕਿ ਇੱਕ ਪ੍ਰੰਪਟ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਟੈਕਸਟ ਕਿਵੇਂ ਜਨਰੇਟ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। ਤੁਹਾਡੇ ਕੋਲ ਇੱਕ ਪ੍ਰੋਗ੍ਰਾਮ ਵੀ ਹੈ ਜੋ ਚੱਲ ਰਿਹਾ ਹੈ ਅਤੇ ਤੁਸੀਂ ਇਸ ਨੂੰ ਸੋਧ ਕੇ ਵੱਖ-ਵੱਖ ਕਿਸਮਾਂ ਦਾ ਟੈਕਸਟ ਜਨਰੇਟ ਕਰ ਸਕਦੇ ਹੋ।

ਪ੍ਰੰਪਟ ਹਰ ਤਰ੍ਹਾਂ ਦੇ ਕੰਮਾਂ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਉਦਾਹਰਨ ਵਜੋਂ:

- **ਇੱਕ ਕਿਸਮ ਦਾ ਟੈਕਸਟ ਜਨਰੇਟ ਕਰੋ**। ਉਦਾਹਰਨ ਵਜੋਂ, ਤੁਸੀਂ ਕਵਿਤਾ, ਕਵਿਜ਼ ਲਈ ਸਵਾਲ ਆਦਿ ਜਨਰੇਟ ਕਰ ਸਕਦੇ ਹੋ।
- **ਜਾਣਕਾਰੀ ਲੱਭੋ**। ਤੁਸੀਂ ਪ੍ਰੰਪਟਸ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਜਾਣਕਾਰੀ ਲੱਭ ਸਕਦੇ ਹੋ ਜਿਵੇਂ 'ਵੈੱਬ ਵਿਕਾਸ ਵਿੱਚ CORS ਦਾ ਕੀ ਮਤਲਬ ਹੈ?'।
- **ਕੋਡ ਜਨਰੇਟ ਕਰੋ**। ਤੁਸੀਂ ਕੋਡ ਜਨਰੇਟ ਕਰਨ ਲਈ ਪ੍ਰੰਪਟਸ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ, ਉਦਾਹਰਨ ਵਜੋਂ ਈਮੇਲਾਂ ਦੀ ਪੁਸ਼ਟੀ ਕਰਨ ਲਈ ਰੈਗੂਲਰ ਐਕਸਪ੍ਰੈਸ਼ਨ ਵਿਕਸਿਤ ਕਰਨਾ ਜਾਂ ਪੂਰਾ ਪ੍ਰੋਗ੍ਰਾਮ ਬਣਾਉਣਾ, ਜਿਵੇਂ ਵੈੱਬ ਐਪ।

## ਇਕ ਹੋਰ ਪ੍ਰਯੋਗਿਕ ਉਦਾਹਰਨ: ਰੈਸੀਪੀ ਜਨਰੇਟਰ

ਕਲਪਨਾ ਕਰੋ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਘਰ ਵਿੱਚ ਸਮੱਗਰੀ ਹੈ ਅਤੇ ਤੁਸੀਂ ਕੁਝ ਬਣਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ। ਇਸ ਲਈ, ਤੁਹਾਨੂੰ ਇੱਕ ਰੈਸੀਪੀ ਦੀ ਲੋੜ ਹੈ। ਰੈਸੀਪੀ ਲੱਭਣ ਦਾ ਤਰੀਕਾ ਖੋਜ ਇੰਜਣ ਵਰਤਣਾ ਹੋ ਸਕਦਾ ਹੈ ਜਾਂ ਤੁਸੀਂ LLM ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ।

ਤੁਸੀਂ ਇਸ ਤਰ੍ਹਾਂ ਦਾ ਪ੍ਰੰਪਟ ਲਿਖ ਸਕਦੇ ਹੋ:

> "ਮੇਰੇ ਲਈ ਇਹ ਸਮੱਗਰੀ ਨਾਲ ਬਣਾਈ ਜਾਣ ਵਾਲੇ ਪੰਜ ਪਕਵਾਨਾਂ ਦੀ ਰੈਸੀਪੀ ਦਿਖਾਉ: ਚਿਕਨ, ਆਲੂ, ਅਤੇ ਗਾਜਰ। ਹਰ ਰੈਸੀਪੀ ਲਈ ਵਰਤੀ ਸਮੱਗਰੀ ਦੀ ਸੂਚੀ ਦਿਓ"

ਦਿਤੇ ਗਏ ਪ੍ਰੰਪਟ 'ਤੇ ਤੁਸੀਂ ਇਸ ਤਰ੍ਹਾਂ ਦਾ ਜਵਾਬ ਲੈ ਸਕਦੇ ਹੋ:

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

ਇਹ ਨਤੀਜਾ ਵਧੀਆ ਹੈ, ਮੈਨੂੰ ਪਤਾ ਚਲ ਗਿਆ ਕਿ ਕੀ ਬਣਾਉਣਾ ਹੈ। ਹੁਣ ਜੋ ਵਿਕਾਸੀ ਸੁਧਾਰ ਲਾਭਦਾਇਕ ਹੋ ਸਕਦੇ ਹਨ ਉਹ ਹਨ:

- ਉਹ ਸਮੱਗਰੀ ਹਟਾ ਦਿਓ ਜੋ ਮੈਨੂੰ ਪਸੰਦ ਨਹੀਂ ਜਾਂ ਜਿਸ ਨੂੰ ਮੈਂ ਸਹਿਣ ਨਹੀਂ ਸਕਦਾ।
- ਇੱਕ ਖਰੀਦ ਸੂਚੀ ਤਿਆਰ ਕਰੋ, ਜੇ ਘਰ ਵਿੱਚ ਸਾਰੀਆਂ ਸਮੱਗਰੀ ਨਹੀਂ ਹੈ ਤਾਂ।

ਉਪਰ ਦਿੱਤੇ ਹਾਲਤਾਂ ਲਈ, ਇੱਕ ਵਾਧੂ ਪ੍ਰੰਪਟ ਜੋੜੀਏ:

> "ਕਿਰਪਾ ਕਰਕੇ ਉਸ ਰੈਸੀਪੀਆਂ ਨੂੰ ਹਟਾਓ ਜਿੰਨ੍ਹਾਂ ਵਿੱਚ ਲਸਣ ਹੈ ਕਿਉਂਕਿ ਮੈਂ ਇਸ ਨਾਲ ਐਲਰਜਿਕ ਹਾਂ ਅਤੇ ਇਸਦੀ ਥਾਂ ਕੁਝ ਹੋਰ ਪ੍ਰਸਤਾਵਿਤ ਕਰੋ। ਨਾਲ ਹੀ, ਇੱਕ ਖਰੀਦ ਸੂਚੀ ਤਿਆਰ ਕਰੋ, ਮੰਨ ਕੇ ਕਿ ਘਰ ਵਿੱਚ ਚਿਕਨ, ਆਲੂ ਅਤੇ ਗਾਜਰ ਪਹਿਲਾਂ ਹੀ ਮੌਜੂਦ ਹਨ।"

ਹੁਣ ਤੁਹਾਡੇ ਕੋਲ ਨਵਾਂ ਨਤੀਜਾ ਹੈ:

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

ਇਹ ਤੁਹਾਡੀਆਂ ਪੰਜ ਰੈਸੀਪੀਆਂ ਹਨ ਜਿਨ੍ਹਾਂ ਵਿੱਚ ਲਸਣ ਦੀ ਗੱਲ ਨਹੀਂ ਹੈ ਅਤੇ ਤੁਹਾਡੇ ਘਰ ਵਿੱਚ ਮੌਜੂਦ ਸਮੱਗਰੀ ਮੁਤਾਬਕ ਖਰੀਦ ਸੂਚੀ ਵੀ ਹੈ।

## ਅਭਿਆਸ - ਇੱਕ ਰੈਸੀਪੀ ਜਨਰੇਟਰ ਬਣਾਓ

ਹੁਣ ਜਦੋਂ ਅਸੀਂ ਇੱਕ ਪੜਦਾ ਨਜ਼ਾਰਾ ਖੇਡਿਆ, ਆਓ ਕੋਡ ਲਿਖੀਏ ਜੋ ਇਸ ਵਿਖਾਏ ਗਏ ਨਜ਼ਾਰੇ ਨਾਲ ਮੇਲ ਖਾਂਦਾ ਹੋਵੇ। ਇਸ ਲਈ, ਹੇਠ ਲਿਖੇ ਕਦਮ ਚਲਾਓ:

1. ਮੌਜੂਦਾ _app.py_ ਫਾਈਲ ਨੂੰ ਸ਼ੁਰੂਆਤੀ ਬਿੰਦੂ ਵਜੋਂ ਵਰਤੋ
1. `prompt` ਵੈਰੀਏਬਲ ਦਾ ਕੋਡ ਇਸ ਪ੍ਰਕਾਰ ਬਦਲੋ:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   ਹੁਣ ਜੇ ਤੁਸੀਂ ਕੋਡ ਚਲਾਵੋਗੇ, ਤਾਂ ਇਸ ਤਰ੍ਹਾਂ ਦਾ ਨਤੀਜਾ ਵੇਖੋਗੇ:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > ਨੋਟ, ਤੁਹਾਡਾ LLM ਗੈਰ-ਨਿਸ਼ਚਿਤ ਹੋ ਸਕਦਾ ਹੈ, ਇਸ ਲਈ ਹਰ ਵਾਰੀ ਕੋਡ ਦੌੜਾਉਂਦੇ ਸਮੇਂ ਵੱਖਰੇ ਨਤੀਜੇ ਮਿਲ ਸਕਦੇ ਹਨ।

   ਵਧੀਆ, ਆਓ ਦੇਖੀਏ ਕਿ ਅਸੀਂ ਕਿਵੇਂ ਗੱਲਾਂ ਨੂੰ ਸੁਧਾਰ ਸਕਦੇ ਹਾਂ। ਸੁਧਾਰ ਲਈ ਅਸੀਂ ਚਾਹੁੰਦੇ ਹਾਂ ਕਿ ਕੋਡ ਲਚੀਲਾ ਹੋਵੇ ਤਾਂ ਜੋ ਸਮੱਗਰੀ ਅਤੇ ਰੈਸੀਪੀਆਂ ਦੀ ਗਿਣਤੀ ਬਦਲੀ ਜਾ ਸਕੇ।

1. ਆਓ ਕੋਡ ਇਹ ਤਰ੍ਹਾਂ ਬਦਲਈਏ:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # ਨੁਸਖਿਆਂ ਦੀ ਗਿਣਤੀ ਨੂੰ ਪ੍ਰੋੰਪਟ ਅਤੇ ਸਮੱਗਰੀਆਂ ਵਿੱਚ ਦਾਖਲ ਕਰੋ
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   ਟੈਸਟ ਦੌੜ ਲਈ ਕੋਡ ਇਸ ਤਰ੍ਹਾਂ ਹੋ ਸਕਦਾ ਹੈ:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### ਫਿਲਟਰ ਅਤੇ ਖਰੀਦ ਸੂਚੀ ਜੋੜ ਕੇ ਸੁਧਾਰ ਕਰੋ

ਅਸੀਂ ਹੁਣ ਇੱਕ ਕਾਰਗਰ ਐਪ ਹੈ ਜੋ ਰੈਸੀਪੀਆਂ ਤਿਆਰ ਕਰ ਸਕਦਾ ਹੈ ਅਤੇ ਇਹ ਲਚੀਲਾ ਹੈ ਕਿਉਂਕਿ ਇਸ ਦਾ ਨਿਰਭਰਤਾ ਉਪਭੋਗਤਾ ਦੇ ਇਨਪੁਟ 'ਤੇ ਹੈ, ਨਾ ਕੇਵਲ ਰੈਸੀਪੀਆਂ ਦੀ ਗਿਣਤੀ 'ਤੇ ਬਲਕਿ ਉਪਯੋਗ ਕੀਤੀ ਸਮੱਗਰੀ 'ਤੇ ਵੀ।

ਇਸਨੂੰ ਹੋਰ ਸੁਧਾਰਨ ਲਈ, ਅਸੀਂ ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਗੱਲਾਂ ਸ਼ਾਮਲ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹਾਂ:

- **ਸਮੱਗਰੀ ਫਿਲਟਰ ਕਰੋ**। ਅਸੀਂ ਉਹ ਸਮੱਗਰੀ ਹਟਾਉਣੀ ਚਾਹੁੰਦੇ ਹਾਂ ਜੋ ਸਾਨੂੰ ਪਸੰਦ ਨਹੀਂ ਜਾਂ ਜਿਸ ਨਾਲ ਅਸੀਂ ਸਹਿਣਸ਼ੀਲ ਨਹੀਂ ਹਾਂ। ਇਸ ਬਦਲਾਅ ਲਈ, ਅਸੀਂ ਆਪਣੀ ਮੌਜੂਦਾ ਪ੍ਰੰਪਟ ਸੋਧ ਕੇ ਇਸ ਦੇ ਅੰਤ ਵਿੱਚ ਇੱਕ ਫਿਲਟਰ ਸਥਿਤੀ ਜੋੜ ਸਕਦੇ ਹਾਂ, ਜਿਵੇਂ:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  ਉਪਰ, ਅਸੀਂ `{filter}` ਪ੍ਰੰਪਟ ਦੇ ਅੰਤ 'ਚ ਜੋੜਿਆ ਹੈ ਅਤੇ ਫਿਲਟਰ ਮੁੱਲ ਨੂੰ ਉਪਭੋਗਤਾ ਤੋਂ ਲੈਂਦੇ ਹਾਂ।

  ਪ੍ਰੋਗਰਾਮ ਚਲਾਉਣ ਦਾ ਇੱਕ ਉਦਾਹਰਨ ਇਨਪੁਟ ਹੁਣ ਇਸ ਤਰ੍ਹਾਂ ਹੋ ਸਕਦਾ ਹੈ:

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

  ਜਿਵੇਂ ਤੁਸੀਂ ਦੇਖ ਰਹੇ ਹੋ, ਜਿਹੜੀਆਂ ਰੈਸੀਪੀਆਂ ਵਿੱਚ ਦੁੱਧ ਹੈ ਉਹ ਹਟਾਈਆਂ ਗਈਆਂ ਹਨ। ਪਰ ਜੇ ਤੁਸੀਂ ਲੈਕਟੋਜ਼ ਇੰਟੌਲੇਰੈਂਟ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਜਿਹੜੀਆਂ ਰੈਸੀਪੀਆਂ ਵਿੱਚ ਪਨੀਰ ਹੈ ਉਹ ਵੀ ਫਿਲਟਰ ਕਰਨੀ ਚਾਹੁੰਦੇ ਹੋ, ਇਸ ਲਈ ਇਹ ਗੱਲ ਸਾਫ਼ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ।


- **ਖਰੀਦਦਾਰੀ ਦੀ ਸੂਚੀ ਬਣਾਓ**। ਅਸੀਂ ਖਰੀਦਦਾਰੀ ਦੀ ਸੂਚੀ ਬਣਾਉਣੀ ਚਾਹੁੰਦੇ ਹਾਂ, ਇਸ ਗੱਲ ਨੂੰ ਧਿਆਨ ਵਿਚ ਰੱਖਦੇ ਹੋਏ ਕਿ ਸਾਡੇ ਕੋਲ ਘਰ ਵਿੱਚ ਕੀ ਹੈ।

  ਇਸ ਫੰਕਸ਼ਨਲਟੀ ਲਈ, ਅਸੀਂ ਸਾਰੇ ਕੰਮ ਇੱਕ ਪ੍ਰਾਂਪਟ ਵਿੱਚ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰ ਸਕਦੇ ਹਾਂ ਜਾਂ ਇਸਨੂੰ ਦੋ ਪ੍ਰਾਂਪਟਾਂ ਵਿੱਚ ਵੰਡ ਸਕਦੇ ਹਾਂ। ਆਓ ਚਲੋ ਦੂਜਾ ਤਰੀਕਾ ਅਜਮਾਈਏ। ਇੱਥੇ ਅਸੀਂ ਇੱਕ ਵਾਧੂ ਪ੍ਰਾਂਪਟ ਸ਼ਾਮਲ ਕਰਨ ਦਾ ਸੁਝਾਅ ਦੇ ਰਹੇ ਹਾਂ, ਪਰ ਇਸ ਦੇ ਕੰਮ ਕਰਨ ਲਈ, ਸਾਨੂੰ ਪਹਿਲਾ ਪ੍ਰਾਂਪਟ ਦੇ ਨਤੀਜੇ ਨੂੰ ਦੂਜੇ ਪ੍ਰਾਂਪਟ ਦੇ ਸੰਦਰਭ ਵਜੋਂ ਸ਼ਾਮਲ ਕਰਨਾ ਪਵੇਗਾ।

  ਉਸ ਸਥਾਨ ਨੂੰ ਕੋਡ ਵਿੱਚ ਲੱਭੋ ਜਿੱਥੇ ਪਹਿਲੇ ਪ੍ਰਾਂਪਟ ਤੋਂ ਨਤੀਜਾ ਪ੍ਰਿੰਟ ਕੀਤਾ ਜਾਂਦਾ ਹੈ ਅਤੇ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਸ਼ਾਮਲ ਕਰੋ:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # ਪ੍ਰਿੰਟ ਜਵਾਬ
  print("Shopping list:")
  print(response.output_text)
  ```

  ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਗੱਲਾਂ ਦਾ ਧਿਆਨ ਰੱਖੋ:

  1. ਅਸੀਂ ਇੱਕ ਨਵਾਂ ਪ੍ਰਾਂਪਟ ਤਿਆਰ ਕਰ ਰਹੇ ਹਾਂ ਜਿਸ ਵਿੱਚ ਪਹਿਲੇ ਪ੍ਰਾਂਪਟ ਤੋਂ ਨਤੀਜਾ ਜੋੜਿਆ ਜਾ ਰਿਹਾ ਹੈ:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. ਅਸੀਂ ਇੱਕ ਨਵੀਂ ਬੇਨਤੀ ਕਰਦੇ ਹਾਂ, ਪਰ ਪਹਿਲੇ ਪ੍ਰਾਂਪਟ ਵਿੱਚ ਮੰਗੇ ਗਏ ਟੋਕਨਾਂ ਦੀ ਗਿਣਤੀ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖਦੇ ਹੋਏ, ਇਸ ਵਾਰੀ ਅਸੀਂ `max_output_tokens` 1200 ਕਰਦੇ ਹਾਂ।

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     ਇਸ ਕੋਡ ਨੂੰ ਚਲਾਉਂਦੇ ਹੋਏ, ਸਾਨੂੰ ਹੁਣ ਹੇਠਾਂ ਦਿੱਤਾ ਨਤੀਜਾ ਮਿਲਦਾ ਹੈ:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## ਆਪਣੀ ਸੈਟਅਪ ਬਿਹਤਰ ਬਣਾਓ

ਅਜੇ ਤਕ ਸਾਡੇ ਕੋਲ ਕੋਡ ਹੈ ਜੋ ਕੰਮ ਕਰਦਾ ਹੈ, ਪਰ ਕੁਝ ਤਬਦੀਲੀਆਂ ਕਰਨੀਆਂ ਚਾਹੀਦੀਆਂ ਹਨ ਤਾਂ ਜੋ ਗੱਲਾਂ ਹੋਰ ਵੀ ਸੁਧਰ ਸਕਣ। ਕੁਝ ਗੱਲਾਂ ਜੋ ਸਾਨੂੰ ਕਰਨੀ ਚਾਹੀਦੀਆਂ ਹਨ:

- **ਰਹਸਿਆਂ ਨੂੰ ਕੋਡ ਤੋਂ ਵੱਖਰਾ ਕਰੋ**, ਜਿਵੇਂ ਕਿ API ਕੁੰਜੀ। ਰਹਿਸ਼ੇ ਕੋਡ ਵਿੱਚ ਨਹੀਂ ਹੋਣੇ ਚਾਹੀਦੇ ਅਤੇ ਉਹ ਇੱਕ ਸੁਰੱਖਿਅਤ ਸਥਾਨ 'ਤੇ ਸਟੋਰ ਕੀਤੇ ਜਾਣੇ ਚਾਹੀਦੇ ਹਨ। ਰਹਿਸ਼ਿਆਂ ਨੂੰ ਕੋਡ ਤੋਂ ਵੱਖਰਾ ਕਰਨ ਲਈ, ਅਸੀਂ ਵਾਤਾਵਰਣ ਵੇਰੀਏਬਲ ਅਤੇ `python-dotenv` ਵਰਗੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਵਰਤ ਸਕਦੇ ਹਾਂ ਜੋ ਉਨ੍ਹਾਂ ਨੂੰ ਫਾਇਲ ਵਿੱਚੋਂ ਲੋਡ ਕਰਦੀਆਂ ਹਨ। ਇਸ ਤਰ੍ਹਾਂ ਕੋਡ ਵਿੱਚ ਇਹ ਦਿੱਸਦਾ ਹੈ:

  1. ਇੱਕ `.env` ਫਾਇਲ ਬਣਾਓ ਜਿਸ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਸਮੱਗਰੀ ਹੋਵੇ:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > ਧਿਆਨ ਦਿਓ, Microsoft Foundry ਵਿੱਚ Azure OpenAI ਲਈ, ਤੁਹਾਨੂੰ ਹੇਠਾਂ ਦਿੱਤੇ ਵਾਤਾਵਰਣ ਵੇਰੀਏਬਲ ਸੈੱਟ ਕਰਨ ਦੀ ਲੋੜ ਹੈ:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     ਕੋਡ ਵਿੱਚ, ਤੁਸੀਂ ਵਾਤਾਵਰਣ ਵੇਰੀਏਬਲ ਇਸ ਤਰ੍ਹਾਂ ਲੋਡ ਕਰੋਂਗੇ:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **ਟੋਕਨ ਦੀ ਲੰਬਾਈ ਬਾਰੇ ਇੱਕ ਸ਼ਬਦ**। ਸਾਨੂੰ ਇਹ ਸੋਚਣਾ ਚਾਹੀਦਾ ਹੈ ਕਿ ਸਾਨੂੰ ਜੋ ਲਿਖਣਾ ਹੈ ਉਸ ਲਈ ਕਿੰਨੇ ਟੋਕਨ ਜਰੂਰੀ ਹਨ। ਟੋਕਨਾਂ ਦੀ ਕੀਮਤ ਹੁੰਦੀ ਹੈ, ਇਸ ਲਈ ਜਿੱਥੇ ਹੋ ਸਕੇ, ਸਾਨੂੰ ਟੋਕਨਾਂ ਦੀ ਗਿਣਤੀ ਨੂੰ ਕਮੀ ਕਰਨੀ ਚਾਹੀਦੀ ਹੈ। ਉਦਾਹਰਨ ਵਜੋਂ, ਕੀ ਅਸੀਂ ਪ੍ਰਾਂਪਟ ਐਸਾ ਤਿਆਰ ਕਰ ਸਕਦੇ ਹਾਂ ਕਿ ਘੱਟ ਟੋਕਨਾਂ ਦੀ ਵਰਤੋਂ ਹੋਵੇ?

  ਟੋਕਨ ਦੀ ਗਿਣਤੀ ਬਦਲਣ ਲਈ, ਤੁਸੀਂ `max_output_tokens` ਪੈਰਾਮੀਟਰ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ। ਉਦਾਹਰਨ ਵਜੋਂ, ਜੇ ਤੁਸੀਂ 100 ਟੋਕਨ ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਇਹ ਕਰੋਗੇ:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **ਤਾਪਮਾਨ ਨਾਲ ਪ੍ਰਯੋਗ ਕਰਨਾ**। ਤਾਪਮਾਨ ਇੱਕ ਐਸੀ ਗੱਲ ਹੈ ਜਿਸਦਾ ਅਸੀਂ ਹਜੇ ਤੱਕ ਜ਼ਿਕਰ ਨਹੀਂ ਕੀਤਾ ਪਰ ਇਹ ਸਾਡੇ ਪ੍ਰੋਗਰਾਮ ਦੇ ਪ੍ਰਦਰਸ਼ਨ ਲਈ ਮਹੱਤਵਪੂਰਨ ਸੰਦਰਭ ਹੈ। ਜਿੰਨਾ ਵੱਧ ਤਾਪਮਾਨ ਹੋਵੇਗਾ, ਨਤੀਜਾ ਓਨਾ ਹੀ ਬੇਤਰਤੀਬ ਹੋਵੇਗਾ। ਵਿਰੁੱਧ, ਜਿੰਨਾ ਘੱਟ ਤਾਪਮਾਨ ਹੋਵੇਗਾ, ਨਤੀਜਾ ਓਨਾ ਹੀ ਅੰਦਾਜ਼ਾ ਲੱਗਣਯੋਗ ਹੋਵੇਗਾ। ਸੋਚੋ ਕਿ ਤੁਸੀਂ ਆਪਣੇ ਨਤੀਜੇ ਵਿੱਚ ਵੱਖ-ਵੱਖਤਾ ਚਾਹੁੰਦੇ ਹੋ ਜਾਂ ਨਹੀਂ।

  ਤਾਪਮਾਨ ਨੂੰ ਬਦਲਣ ਲਈ, ਤੁਸੀਂ `temperature` ਪੈਰਾਮੀਟਰ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ। ਉਦਾਹਰਨ ਵਜੋਂ, ਜੇ ਤੁਸੀਂ 0.5 ਤਾਪਮਾਨ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਇਹ ਕਰੋਗੇ:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > ਧਿਆਨ ਦਿਓ, 1.0 ਦੇ ਨੇੜੇ, ਨਤੀਜਾ ਵੱਧ ਵੱਖਰਾ ਹੋਵੇਗਾ।

- **Reasoning ਮਾਡਲਾਂ `temperature` ਦੀ ਵਰਤੋਂ ਨਹੀਂ ਕਰਦੇ**। ਇਹ 2026 ਵਿੱਚ ਇੱਕ ਅਹੰਕਾਰਪੂਰਨ ਬਦਲਾਅ ਹੈ। ਮਾਇਕ੍ਰੋਸਾਫਟ ਫਾਉਂਡਰੀ ਉੱਤੇ ਮੌਜੂਦ ਮੌਜੂਦਾ, ਗੈਰ-ਪੁਰਾਣੇ ਮਾਡਲ ਹਨ **reasoning ਮਾਡਲ** (GPT-5 ਪਰਿਵਾਰ, o-series) - ਅਤੇ ਇਹ **`temperature` ਜਾਂ `top_p` ਦਾ ਸਮਰਥਨ ਨਹੀਂ ਕਰਦੇ** (ਨਾ `max_tokens`; ਇਸਦਾ ਬਦਲ `max_output_tokens` ਵਰਤੋ)। ਜੇ ਤੁਸੀਂ `temperature` ਨੂੰ `gpt-5-mini` ਨੂੰ ਭੇਜੋਗੇ ਤਾਂ ਤੁਹਾਨੂੰ "parameter not supported" ਦੀ ਗਲਤੀ ਮਿਲੇਗੀ। ਇਸ ਲਈ, ਉਪਰ ਦਿੱਤੇ ਤਾਪਮਾਨ ਦੇ ਉਦਾਹਰਨ ਨੂੰ ਅਜਮਾਉਣ ਲਈ, ਕਿਸੇ ਐਸੇ ਮਾਡਲ ਵੱਲ ਇਸ਼ਾਰਾ ਕਰੋ ਜੋ ਹਾਲੇ ਵੀ ਸੈਂਪਲਿੰਗ ਕੰਟਰੋਲ ਨੂੰ ਸਮਰਥਨ ਕਰਦਾ ਹੈ - ਉਦਾਹਰਨ ਵਜੋਂ ਇੱਕ ਖੁੱਲ੍ਹਾ **Llama** ਮਾਡਲ ਜਿਵੇਂ `Llama-3.3-70B-Instruct` ਜੋ [Microsoft Foundry ਮਾਡਲ ਕੈਟਾਲੌਗ](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ਤੋਂ ਮੰਗਿਆ ਜਾਂਦਾ ਹੈ, ਜੋ Foundry Models / Azure AI Inference ਪਾਇੰਟ ਦੁਆਰਾ ਕਾਲ ਕੀਤਾ ਜਾਂਦਾ ਹੈ (ਉਹੀ ਢੰਗ ਜਿਵੇਂ ਕਿ `githubmodels-*` ਨਮੂਨੇ)। ਗਿਣਨਵਾਂ ਮਾਡਲਾਂ ਜਿਵੇਂ GPT-5 ਲਈ, ਤੁਸੀਂ ਨਤੀਜੇ ਨੂੰ ਵੱਖਰੇ ਤਰੀਕੇ ਨਾਲ ਨਿਯੰਤਰਿਤ ਕਰਦੇ ਹੋ:
  - **Prompt engineering** - ਸਾਫ਼ ਹਦਾਇਤਾਂ, ਉਦਾਹਰਣਾਂ, ਅਤੇ ਬਨਾਮੁਨਾਅ ਕਿਰਿਆਵੀ ਨਿਕਾਸ (ਦੇਖੋ ਪਾਠ [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) ਉਹ ਕੰਮ ਕਰਦੇ ਹਨ ਜੋ ਸੈਂਪਲਿੰਗ ਕੰਟਰੋਲ ਪਹਿਲਾਂ ਕਰਦੇ ਸਨ।
  - **Reasoning controls** - ਪੈਰਾਮੀਟਰ ਜਿਵੇਂ reasoning effort/verbosity reasoning ਦੀ ਗਹਿਰਾਈ ਨੂੰ ਲੰਬਾਈ ਅਤੇ ਲਾਗਤ ਨਾਲ ਤੋਲਦੇ ਹਨ।

  ਸੰਖੇਪ ਵਿੱਚ: `temperature`/`top_p` ਕਈ ਮਾਡਲਾਂ (Llama, Mistral, Phi, ਅਤੇ GPT-4.x ਪਰਿਵਾਰ - ਹਾਲਾਂਕਿ GPT-4.x ਹਟਾਇਆ ਜਾ ਰਿਹਾ ਹੈ) ਵਿਚ ਅਜੇ ਵੀ ਮੰਨਿਆ ਜਾਂਦਾ ਹੈ, ਪਰ ਗਤੀ ਪ੍ਰਾਂਪਟ ਇੰਜੀਨੀਅਰਿੰਗ + reasoning controls ਦੀ ਵੱਲ ਜਾ ਰਹੀ ਹੈ reasoning ਮਾਡਲਾਂ ਜਿਵੇਂ GPT-5 ਲਈ।

## ਅਸਾਈਨਮੈਂਟ

ਇਸ ਅਸਾਈਨਮੈਂਟ ਲਈ, ਤੁਸੀਂ ਚੁਣ ਸਕਦੇ ਹੋ ਕਿ ਕੀ ਬਣਾਉਣਾ ਹੈ।

ਇੱਥੇ ਕੁਝ ਸੁਝਾਅ ਹਨ:

- ਰੈਸੀਪੀ ਜਨਰੇਟਰ ਐਪ ਨੂੰ ਹੋਰ ਸੁਧਾਰਨ ਲਈ ਸਵਾਲ-ਜਵਾਬ ਕਰੋ। ਤਾਪਮਾਨ ਦੇ ਮੁੱਲਾਂ ਨਾਲ ਖੇਡੋ, ਅਤੇ ਪ੍ਰਾਂਪਟਾਂ ਨੂੰ ਦੇਖ ਕੇ ਵੇਖੋ ਕਿ ਤੁਸੀਂ ਕੀ ਕੁਝ ਬਣਾ ਸਕਦੇ ਹੋ।
- ਇੱਕ "ਸਟੱਡੀ ਬੱਡੀ" ਬਣਾਓ। ਇਹ ਐਪ ਕਿਸੇ ਵਿਸ਼ੇ ਬਾਰੇ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਦੇ ਸਕਦਾ ਹੈ ਉਦਾਹਰਨ ਵਜੋਂ Python ਲਈ, ਤੁਹਾਡੇ ਕੋਲ ਪ੍ਰਾਂਪਟ ਹੋ ਸਕਦੇ ਹਨ "Python ਵਿੱਚ ਕਿਸੇ ਵਿਸ਼ੇ ਦੇ ਬਾਰੇ ਕੀ ਹੈ?", ਜਾਂ ਤੁਸੀਂ ਕੋਈ ਐਸਾ ਪ੍ਰਾਂਪਟ ਰੱਖ ਸਕਦੇ ਹੋ ਜੋ ਕੰਡਾ ਦਿਖਾਏ ਉਦਾਹਰਨ ਵਜੋਂ ਕਿਸੇ ਵਿਸ਼ੇ ਲਈ ਕੋਡ।
- ਇਤਿਹਾਸ ਬੌਟ, ਇਤਿਹਾਸ ਨੂੰ ਜਿੰਦਾਬਾਏ ਬਣਾਓ, ਬੌਟ ਨੂੰ ਕਿਹਾ ਜਾਵੇ ਕਿ ਉਹ ਕਿਸੇ ਵਿਸ਼ੇਸ਼ ਇਤਿਹਾਸਕ ਪਾਤਰ ਦਾ ਭੂਮਿਕਾ ਨਿਭਾਏ ਅਤੇ ਉਸ ਦੀ ਜਿੰਦਗੀ ਅਤੇ ਦੌਰ ਬਾਰੇ ਸਵਾਲ ਪੁੱਛੋ।

## ਹੱਲ

### ਸਟੱਡੀ ਬੱਡੀ

ਹੇਠਾਂ ਇੱਕ ਸ਼ੁਰੂਆਤੀ ਪ੍ਰਾਂਪਟ ਹੈ, ਵੇਖੋ ਤੁਸੀਂ ਇਸਨੂੰ ਕਿਵੇਂ ਵਰਤ ਸਕਦੇ ਹੋ ਅਤੇ ਆਪਣੇ ਮਨਪਸੰਦ ਤਰੀਕੇ ਨਾਲ ਬਦਲ ਸਕਦੇ ਹੋ।

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### ਇਤਿਹਾਸ ਬੌਟ

ਇੱਥੇ ਕੁਝ ਪ੍ਰਾਂਪਟ ਹਨ ਜੋ ਤੁਸੀਂ ਵਰਤ ਸਕਦੇ ਹੋ:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## ਗਿਆਨ ਜਾਂਚ

ਤਾਪਮਾਨ ਦਾ ਕੀ ਕੰਮ ਹੈ?

1. ਇਹ ਨਤੀਜੇ ਦੀ ਬੇਤਰਤੀਬਤਾ ਨੂੰ ਨਿਯੰਤਰਿਤ ਕਰਦਾ ਹੈ।
1. ਇਹ ਜਵਾਬ ਦੀ ਵੱਡਾਈ ਨੂੰ ਨਿਯੰਤਰਿਤ ਕਰਦਾ ਹੈ।
1. ਇਹ ਟੋਕਨਾਂ ਦੀ ਸੰਖਿਆ ਨੂੰ ਨਿਯੰਤਰਿਤ ਕਰਦਾ ਹੈ।

## 🚀 ਚੁਣੌਤੀ

ਅਸਾਈਨਮੈਂਟ 'ਤੇ ਕੰਮ ਕਰਦਿਆਂ, ਤਾਪਮਾਨ ਨੂੰ ਵੱਖ-ਵੱਖ ਕਰੋ, ਇਸਨੂੰ 0, 0.5, ਅਤੇ 1 'ਤੇ ਸੈਟ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ। ਯਾਦ ਰੱਖੋ ਕਿ 0 ਸਭ ਤੋਂ ਘੱਟ ਵੱਖਰਾ ਹੈ ਅਤੇ 1 ਸਭ ਤੋਂ ਵੱਧ। ਤੁਹਾਡੇ ਐਪ ਲਈ ਕਿਹੜਾ ਮੁੱਲ ਬਿਹਤਰ ਕੰਮ ਕਰਦਾ ਹੈ?

## ਸ਼ਾਬਾਸ਼! ਆਪਣੀ ਸਿੱਖਿਆ ਜਾਰੀ ਰੱਖੋ

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਸਾਡੇ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ਨੂੰ ਦੇਖੋ ਤਾਂ ਜੋ ਤੁਹਾਡਾ Generative AI ਗਿਆਨ ਹੋਰ ਵਧ ਸਕੇ!

ਹੇਠਾਂ ਜਾਓ ਪਾਠ 7 ਵੱਲ ਜਿੱਥੇ ਅਸੀਂ ਵੇਖਾਂਗੇ ਕਿ ਕਿਵੇਂ [ਚੈਟ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਵਣੀਆਂ ਹਨ](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->