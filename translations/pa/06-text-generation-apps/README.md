# ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪਲੀਕੇਸ਼ਨਾਂ ਬਣਾਉਣਾ

[![ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪਲੀਕੇਸ਼ਨਾਂ ਬਣਾਉਣਾ](../../../translated_images/pa/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(ਇਸ ਪਾਠ ਦੇ ਵੀਡੀਓ ਨੂੰ ਦੇਖਣ ਲਈ ਉਪਰ ਦਿੱਤੀ ਚਿੱਤਰ 'ਤੇ ਕਲਿੱਕ ਕਰੋ)_

ਤੁਸੀਂ ਇਸ ਕ੍ਰਿਕੁਲਮ ਦੁਆਰਾ ਹੁਣ ਤੱਕ ਵੇਖਿਆ ਹੈ ਕਿ ਪ੍ਰਾਂਪਟਾਂ ਵਰਗੇ ਮੂਲਭੂਤ ਸੰਕਲਪ ਹਨ ਅਤੇ ਇੱਕ ਪੂਰਾ ਵਿਭਾਗ "prompt engineering" ਨਾਲ ਵੀ ਸਬੰਧਿਤ ਹੈ। ਕਈ ਸੰਦ ਜਿਵੇਂ ChatGPT, Office 365, Microsoft Power Platform ਅਤੇ ਹੋਰ, ਤੁਹਾਨੂੰ ਕਿਸੇ ਕੰਮ ਨੂੰ ਪੂਰਾ ਕਰਨ ਲਈ ਪ੍ਰਾਂਪਟਾਂ ਦੇ ਉਪਯੋਗ ਨਾਲ ਸਹਾਇਤਾ ਕਰਦੇ ਹਨ।

ਤੁਹਾਡੇ ਲਈ ਐਪ ਵਿੱਚ ਐਸਾ ਅਨੁਭਵ ਜੋੜਨ ਲਈ, ਤੁਹਾਨੂੰ ਪ੍ਰਾਂਪਟ, ਪੂਰਨਾਂ ਅਤੇ ਕੰਮ ਕਰਨ ਲਈ ਇੱਕ ਲਾਇਬ੍ਰੇਰੀ ਚੁਣਨ ਵਰਗੇ ਸੰਕਲਪਾਂ ਨੂੰ ਸਮਝਣਾ ਜਰੂਰੀ ਹੈ। ਇਹੀ ਤੁਸੀਂ ਇਸ ਅਧਿਆਇ ਵਿੱਚ ਸਿੱਖੋਗੇ।

## ਪਰਿਚਯ

ਇਸ ਅਧਿਆਇ ਵਿੱਚ, ਤੁਸੀਂ:

- openai ਲਾਇਬ੍ਰੇਰੀ ਅਤੇ ਇਸਦੇ ਮੁੱਖ ਸੰਕਲਪਾਂ ਬਾਰੇ ਸਿੱਖੋਗੇ।
- openai ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ ਇੱਕ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਬਣਾਵੋਗੇ।
- ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਬਣਾਉਣ ਲਈ ਪ੍ਰਾਂਪਟ, ਤਾਪਮਾਨ ਅਤੇ ਟੋਕਨਾਂ ਵਰਗੇ ਸੰਕਲਪਾਂ ਦੀ ਵਰਤੋਂ ਕਿਵੇਂ ਕਰਨੀ ਹੈ, ਇਹ ਸਮਝੋਗੇ।

## ਸਿੱਖਣ ਦੇ ਲਕੜੀ

ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਵਿੱਚ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- ਟੈਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਕੀ ਹੈ, ਸਮਝਾ ਸਕੋਗੇ।
- openai ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਬਣਾ ਸਕੋਗੇ।
- ਆਪਣੀ ਐਪ ਨੂੰ ਵੱਧ ਜਾਂ ਘੱਟ ਟੋਕਨਾਂ ਦੀ ਵਰਤੋਂ ਕਰਨ ਲਈ ਸੰਰਚਿਤ ਕਰ ਸਕੋਗੇ ਅਤੇ ਵੱਖ ਵੱਖ ਨਤੀਜਿਆਂ ਲਈ ਤਾਪਮਾਨ ਨੂੰ ਵੀ ਬਦਲ ਸਕੋਗੇ।

## ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਕੀ ਹੁੰਦੀ ਹੈ?

ਆਮ ਤੌਰ ਤੇ ਕਦੋਂ ਤੁਸੀਂ ਕੋਈ ਐਪ ਬਣਾਉਂਦੇ ਹੋ ਤਾਂ ਇਸ ਦਾ ਕੋਈ ਇੰਟਰਫੇਸ ਹੁੰਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ:

- ਕਮਾਂਡ ਅਧਾਰਿਤ। ਕਨਸੋਲ ਐਪ ਉਹ ਹੁੰਦੀ ਹੈ ਜਿੱਥੇ ਤੁਸੀਂ ਕਮਾਂਡ ਟਾਈਪ ਕਰਦੇ ਹੋ ਅਤੇ ਇਹ ਕੰਮ ਕਰਦਾ ਹੈ। ਉਦਾਹਰਣ ਵਜੋਂ, `git` ਇੱਕ ਕਮਾਂਡ ਅਧਾਰਿਤ ਐਪ ਹੈ।
- ਉਪਭੁੋਗਤਾ ਇੰਟਰਫੇਸ (UI)। ਕੁਝ ਐਪ ਗ੍ਰਾਫ਼ਿਕਲ ਉਪਭੋਗਤਾ ਇੰਟਰਫੇਸ (GUIs) ਵਾਲੀਆਂ ਹੁੰਦੀਆਂ ਹਨ ਜਿੱਥੇ ਤੁਸੀਂ ਬਟਨਾਂ ਨੂੰ ਕਲਿੱਕ ਕਰਦੇ ਹੋ, ਲਿਖਾਈ ਕਰਦੇ ਹੋ, ਵਿਕਲਪ ਚੁਣਦੇ ਹੋ ਅਤੇ ਹੋਰ।

### ਕਨਸੋਲ ਅਤੇ UI ਐਪਾਂ ਸੀਮਤ ਹੁੰਦੀਆਂ ਹਨ

ਇਸ ਨੂੰ ਉਸ ਕਮਾਂਡ ਅਧਾਰਿਤ ਐਪ ਨਾਲ ਤੁਲਨਾ ਕਰੋ ਜਿੱਥੇ ਤੁਸੀਂ ਖਾਸ ਕਮਾਂਡ ਟਾਈਪ ਕਰਦੇ ਹੋ:

- **ਇਹ ਸੀਮਤ ਹੈ**। ਤੁਸੀਂ ਕੋਈ ਵੀ ਕਮਾਂਡ ਨਹੀਂ ਟਾਈਪ ਕਰ ਸਕਦੇ, ਸਿਰਫ ਉਹ ਕਮਾਂਡ ਜੋ ਐਪ ਸਮਰਥਨ ਕਰਦੀ ਹੈ।
- **ਭਾਸ਼ਾ ਨਿਰਧਾਰਿਤ**। ਬਹੁਤ ਸਾਰੀਆਂ ਐਪਾਂ ਕਈ ਭਾਸ਼ਾਵਾਂ ਲਈ ਸਮਰਥਨ ਕਰਦੀਆਂ ਹਨ, ਪਰ ਡਿਫਾਲਟ ਰੂਪ ਵਿੱਚ ਇਹ ਖਾਸ ਭਾਸ਼ਾ ਲਈ ਬਣਾਈਆਂ ਗਈਆਂ ਹੁੰਦੀਆਂ ਹਨ, ਯਦਿਪਿ ਤੁਸੀਂ ਹੋਰ ਭਾਸ਼ਾ ਸਮਰਥਨ ਵੀ ਜੋੜ ਸਕਦੇ ਹੋ।

### ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪਾਂ ਦੇ ਫਾਇਦੇ

ਤਾਂ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਵਿੱਚ ਕੀ ਅੰਤਰ ਹੈ?

ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਵਿੱਚ, ਤੁਹਾਡੇ ਕੋਲ ਹੋਰ ਲਚੀਲਾਪਣ ਹੁੰਦਾ ਹੈ, ਤੁਸੀਂ ਕਮਾਂਡਾਂ ਜਾਂ ਖ਼ਾਸ ਸ਼ੁਰੂਆਤੀ ਭਾਸ਼ਾ ਤੱਕ ਸੀਮਤ ਨਹੀਂ ਹੋ। ਇਸ ਦੀ ਥਾਂ, ਤੁਸੀਂ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਦੀ ਵਰਤੋਂ ਨਾਲ ਐਪ ਨਾਲ ਗੱਲਬਾਤ ਕਰ ਸਕਦੇ ਹੋ। ਇੱਕ ਹੋਰ ਫਾਇਦਾ ਇਹ ਹੈ ਕਿ ਤੁਸੀਂ ਇੱਕ ਡਾਟਾ ਸਰੋਤ ਨਾਲ ਸੰਚਾਰ ਕਰ ਰਹੇ ਹੋ ਜੋ ਵੱਡੇ ਪਾਠਕਾਂਡ ਜਾਂ ਜਾਣਕਾਰੀ ਸ਼੍ਰੋਤ ਉੱਤੇ ਤਿਆਰ ਕੀਤਾ ਗਿਆ ਹੈ, ਜਦੋਂ ਕਿ ਪਾਰੰਪਰਿਕ ਐਪ ਡਾਟਾਬੇਸ ਵਿੱਚ ਸੀਮਤ ਹੋ ਸਕਦੀ ਹੈ।

### ਮੈਂ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਨਾਲ ਕੀ ਕੁਝ ਬਣਾ ਸਕਦਾ ਹਾਂ?

ਤੁਸੀਂ ਬਹੁਤ ਕੁਝ ਬਣਾ ਸਕਦੇ ਹੋ। ਉਦਾਹਰਣ ਲਈ:

- **ਇੱਕ ਚੈਟਬੋਟ**। ਇੱਕ ਚੈਟਬੋਟ ਜੋ ਤੁਹਾਡੇ ਕੰਪਨੀ ਅਤੇ ਇਸਦੇ ਉਤਪਾਦਾਂ ਬਾਰੇ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਦਿੰਦਾ ਹੈ, ਇਹ ਇਕ ਚੰਗਾ ਵਿਕਲਪ ਹੋ ਸਕਦਾ ਹੈ।
- **ਮਦਦਗਾਰ**। LLMs ਟੈਕਸਟ ਦਾ ਸਾਰ ਇੱਕੱਠਾ ਕਰਨ, ਜਾਣਕਾਰੀਆਂ ਪ੍ਰਾਪਤ ਕਰਨ, ਰੋਜ਼ਗਾਰਜੀਵੀ ਲਿਖਣ ਵਰਗੀਆਂ ਚੀਜ਼ਾਂ ਵਿੱਚ ਬਹੁਤ ਵਧੀਆ ਹਨ।
- **ਕੋਡ ਸਹਾਇਕ**। ਜਿਸ ਭਾਸ਼ਾ ਮਾਡਲ ਦੀ ਤੁਸੀਂ ਵਰਤੋਂ ਕਰਦੇ ਹੋ ਉਸ ਦੇ ਅਨੁਸਾਰ, ਤੁਸੀਂ ਇੱਕ ਕੋਡ ਸਹਾਇਕ ਬਣਾ ਸਕਦੇ ਹੋ ਜੋ ਤੁਹਾਨੂੰ ਕੋਡ ਲਿਖਣ ਵਿੱਚ ਸਹਾਇਤਾ ਕਰਦਾ ਹੈ। ਉਦਾਹਰਣ ਲਈ, ਤੁਸੀਂ GitHub Copilot ਜਾਂ ChatGPT ਵਰਗੇ ਉਤਪਾਦ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ।

## ਮੈਂ ਕਿਵੇਂ ਸ਼ੁਰੂ ਕਰ ਸਕਦਾ ਹਾਂ?

ਸੋ, ਤੁਹਾਨੂੰ LLM ਨਾਲ ਇਕੱਠਾ ਕਰਨ ਦਾ ਤਰੀਕਾ ਲੱਭਣਾ ਪੈਂਦਾ ਹੈ ਜੋ ਅਮੂਮਨ ਦੋ ਤਰੀਕਿਆਂ ਵਿੱਚੋਂ ਕੋਈ ਹੁੰਦਾ ਹੈ:

- API ਦੀ ਵਰਤੋਂ ਕਰੋ। ਇੱਥੇ ਤੁਸੀਂ ਆਪਣੇ ਪ੍ਰਾਂਪਟ ਨਾਲ ਵੈੱਬ ਬੇਨਤੀਆਂ ਬਣਾਉਂਦੇ ਹੋ ਅਤੇ ਜਨਰੇਟ ਕੀਤਾ ਟੈਕਸਟ ਪ੍ਰਾਪਤ ਕਰਦੇ ਹੋ।
- ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਵਰਤੋਂ ਕਰੋ। ਲਾਇਬ੍ਰੇਰੀਆਂ API ਕਾਲਜ਼ ਨੂੰ ਇੰਕੈਪਸੂਲੇਟ ਕਰਦੀਆਂ ਹਨ ਅਤੇ ਇਸ ਨੂੰ ਵਰਤਣ ਬਹੁਤ ਸੌਖਾ ਬਣਾਉਂਦੀਆਂ ਹਨ।

## ਲਾਇਬ੍ਰੇਰੀਆਂ/SDKs

LLMs ਨਾਲ ਕੰਮ ਕਰਨ ਲਈ ਕੁਝ ਪ੍ਰਸਿੱਧ ਲਾਇਬ੍ਰੇਰੀਆਂ ਹਨ ਜਿਵੇਂ ਕਿ:

- **openai**, ਇਹ ਲਾਇਬ੍ਰੇਰੀ ਤੁਹਾਡੇ ਮਾਡਲ ਨਾਲ ਜੁੜਨ ਅਤੇ ਪ੍ਰਾਂਪਟ ਭੇਜਣ ਵਿੱਚ ਆਸਾਨੀ ਕਰਦੀ ਹੈ।

ਫਿਰ ਕੁਝ ਲਾਇਬ੍ਰੇਰੀਆਂ ਹਨ ਜੋ ਉਦ੍ਧਾਤ ਸਤਰ 'ਤੇ ਕੰਮ ਕਰਦੀਆਂ ਹਨ ਜਿਵੇਂ ਕਿ:

- **Langchain**। Langchain ਮਸ਼ਹੂਰ ਹੈ ਅਤੇ ਪਾਇਥਨ ਨੂੰ ਸਮਰਥਨ ਕਰਦਾ ਹੈ।
- **Semantic Kernel**। Semantic Kernel ਮਾਇਕ੍ਰੋਸਾਫਟ ਦੀ ਲਾਇਬ੍ਰੇਰੀ ਹੈ ਜੋ C#, ਪਾਇਥਨ ਅਤੇ ਜਾਵਾ ਭਾਸ਼ਾਵਾਂ ਦਾ ਸਮਰਥਨ ਕਰਦੀ ਹੈ।

## openai ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪਹਿਲੀ ਐਪ

ਆਓ ਵੇਖੀਏ ਕਿ ਆਪਣੀ ਪਹਿਲੀ ਐਪ ਕਿਵੇਂ ਬਣਾਉਣੀ ਹੈ, ਸਾਨੂੰ ਕਿਹੜੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਦੀ ਲੋੜ ਹੈ, ਇਹ ਕਿੰਨੀ ਲੋੜੀਂਦੀ ਹੈ ਆਦਿ।

### openai ਇੰਸਟਾਲ ਕਰੋ

OpenAI ਜਾਂ Azure OpenAI ਨਾਲ ਇੰਟਰੈਕਟ ਕਰਨ ਲਈ ਬਹੁਤ ਸਾਰੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਹਨ। ਕਈ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ ਵੀ ਵਰਤੀ ਜਾ ਸਕਦੀਆਂ ਹਨ ਜਿਵੇਂ C#, ਪਾਇਥਨ, ਜਾਵਾਸਕ੍ਰਿਪਟ, ਜਾਵਾ ਅਤੇ ਹੋਰ। ਅਸੀਂ `openai` ਪਾਇਥਨ ਲਾਇਬ੍ਰੇਰੀ ਨੂੰ ਬਰਤਣ ਲਈ ਚੁਣਿਆ ਹੈ, ਇਸ ਲਈ ਅਸੀਂ `pip` ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਸ ਨੂੰ ਇੰਸਟਾਲ ਕਰਾਂਗੇ।

```bash
pip install openai
```

### ਇੱਕ ਰੀਸੋਰਸ ਬਣਾਓ

ਤੁਹਾਨੂੰ ਹੇਠ ਲਿਖੇ ਕਦਮ ਕਰਨੇ ਹੁੰਦੇ ਹਨ:

- Azure 'ਤੇ ਇੱਕ ਖਾਤਾ ਬਣਾਓ [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)।
- Azure OpenAI ਦੀ ਪਹੁੰਚ ਪ੍ਰਾਪਤ ਕਰੋ। ਜਾਓ [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) ਅਤੇ ਪਹੁੰਚ ਦੀ ਅਰਜ਼ੀ ਦਿਓ।

  > [!NOTE]
  > ਲਿਖਣ ਸਮੇਂ, ਤੁਹਾਨੂੰ Azure OpenAI ਲਈ ਪਹੁੰਚ ਲਈ ਅਰਜ਼ੀ ਦੇਣੀ ਪੈਂਦੀ ਹੈ।

- Python ਇੰਸਟਾਲ ਕਰੋ <https://www.python.org/>
- Azure OpenAI ਸੇਵਾ ਦਾ ਇੱਕ ਰੀਸੋਰਸ ਬਣਾਇਆ ਹੋਇਆ ਹੋਵੇ। ਇਸ ਗਾਈਡ ਦੇਖੋ ਕਿਵੇਂ [ਰੀਸੋਰਸ ਬਣਾਉਣਾ](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)।

### API ਕੁੰਜੀ ਅਤੇ ਐਂਡਪੋਇੰਟ ਲੱਭੋ

ਇਸ ਸਮੇਂ, ਤੁਹਾਨੂੰ ਆਪਣੇ `openai` ਲਾਇਬ੍ਰੇਰੀ ਨੂੰ ਦੱਸਣਾ ਪੈਂਦਾ ਹੈ ਕਿ ਕਿਹੜੀ API ਕੁੰਜੀ ਵਰਤਣੀ ਹੈ। ਆਪਣੀ API ਕੁੰਜੀ ਲੱਭਣ ਲਈ, ਆਪਣੇ Azure OpenAI ਰੀਸੋਰਸ ਦੇ "Keys and Endpoint" ਸੈਕਸ਼ਨ ਵਿੱਚ ਜਾਓ ਅਤੇ "Key 1" ਦੀ ਕਾਪੀ ਬਣਾਓ।

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

ਹੁਣ ਜਦੋਂ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਇਹ ਜਾਣਕਾਰੀ ਕਾਪੀ ਹੋ ਗਈ ਹੈ, ਆਓ ਲਾਇਬ੍ਰੇਰੀਆਂ ਨੂੰ ਇਸਦੀ ਵਰਤੋਂ ਕਰਨ ਲਈ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼ ਦਈਏ।

> [!NOTE]
> ਆਪਣੇ API ਕੁੰਜੀ ਨੂੰ ਆਪਣੇ ਕੋਡ ਤੋਂ ਵੱਖਰਾ ਰੱਖਣਾ ਵਧੀਆ ਹੁੰਦਾ ਹੈ। ਤੁਸੀਂ ਇਹ ਵਾਤਾਵਰਣ ਚਰ ਹਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕਰ ਸਕਦੇ ਹੋ।
>
> - ਵਾਤਾਵਰਣ ਚਰ `OPENAI_API_KEY` ਨੂੰ ਆਪਣੀ API ਕੁੰਜੀ 'ਤੇ ਸੈੱਟ ਕਰੋ।
>   `export OPENAI_API_KEY='sk-...'`

### Azure ਕੰਫਿਗਰੇਸ਼ਨ ਸੈਟਅਪ ਕਰੋ

ਜੇ ਤੁਸੀਂ Azure OpenAI (ਹੁਣ Microsoft Foundry ਦਾ ਹਿੱਸਾ) ਵਰਤ ਰਹੇ ਹੋ, ਇਹ ਹੈ ਕੰਫਿਗਰੇਸ਼ਨ ਸੈਟਅਪ ਕਰਨ ਦਾ ਤਰੀਕਾ। ਅਸੀਂ ਪਾਰੰਪਰਿਕ `OpenAI` ਕਲਾਇੰਟ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਾਂ ਜੋ Azure OpenAI `/openai/v1/` ਐਂਡਪੋਇੰਟ ਵਲ ਇਸ਼ਾਰਾ ਕਰਦਾ ਹੈ, ਜੋ Responses API ਨਾਲ ਕੰਮ ਕਰਦਾ ਹੈ ਅਤੇ `api_version` ਦੀ ਲੋੜ ਨਹੀਂ ਹੁੰਦੀ:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

ਉਪਰੋਕਤ ਵਿੱਚ ਅਸੀਂ ਹੇਠ ਲਿਖੀਆਂ ਚੀਜ਼ਾਂ ਸੈੱਟ ਕਰ ਰਹੇ ਹਾਂ:

- `api_key`, ਇਹ ਤੁਹਾਡੀ API ਕੁੰਜੀ ਹੈ ਜੋ Azure Portal ਜਾਂ Microsoft Foundry ਪੋਰਟਲ ਵਿੱਚ ਮਿਲਦੀ ਹੈ।
- `base_url`, ਇਹ ਤੁਹਾਡੇ Foundry ਰੀਸੋਰਸ ਐਂਡਪੋਇੰਟ ਨਾਲ `/openai/v1/` ਜੋੜਕੇ ਬਣਾਈ ਜਾਂਦੀ ਹੈ। ਸਥਾਈ v1 ਐਂਡਪੋਇੰਟ OpenAI ਅਤੇ Azure OpenAI ਫੈਲਾਵ 'ਤੇ ਕੰਮ ਕਰਦਾ ਹੈ ਬਿਨਾਂ `api_version` ਦੀ ਦੇਖਭਾਲ।

> [!NOTE] > `os.environ` ਵਾਤਾਵਰਣ ਚਰ ਨੂੰ ਪੜ੍ਹਦਾ ਹੈ। ਤੁਸੀਂ ਇਸਨੂੰ `AZURE_OPENAI_API_KEY` ਅਤੇ `AZURE_OPENAI_ENDPOINT` ਵਰਗੇ ਵਾਤਾਵਰਣ ਚਰਾਂ ਨੂੰ ਪੜ੍ਹਨ ਲਈ ਵਰਤ ਸਕਦੇ ਹੋ। ਆਪਣੀ ਟਰਮਿਨਲ ਵਿੱਚ ਇਹਨਾਂ ਵਾਤਾਵਰਣ ਚਰਾਂ ਨੂੰ ਸੈੱਟ ਕਰੋ ਜਾਂ `dotenv` ਵਰਗੇ ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਵਰਤੋਂ ਕਰੋ।

## ਟੈਕਸਟ ਬਣਾਓ

ਟੈਕਸਟ ਬਣਾਉਣ ਦਾ ਤਰੀਕਾ Responses API ਦੀ `responses.create` ਵਿਧੀ ਦੀ ਵਰਤੋਂ ਕਰਨਾ ਹੈ। ਇਹ ਰਹੀ ਇੱਕ ਉਦਾਹਰਣ:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # ਇਹ ਤੁਹਾਡਾ ਮਾਡਲ ਤੈਨਾਤ ਕਰਨ ਦਾ ਨਾਮ ਹੈ
    input=prompt,
    store=False,
)
print(response.output_text)
```

ਉਪਰੋਕਤ ਕੋਡ ਵਿੱਚ, ਅਸੀਂ ਇੱਕ ਜਵਾਬ ਬਣਾਉਂਦੇ ਹਾਂ ਅਤੇ ਮਾਡਲ ਤੇ ਪ੍ਰਾਂਪਟ ਦਿੰਦੇ ਹਾਂ। ਫਿਰ ਅਸੀਂ `response.output_text` ਰਾਹੀਂ ਬਣਾਇਆ ਹੋਇਆ ਟੈਕਸਟ ਪ੍ਰਿੰਟ ਕਰਦੇ ਹਾਂ।

### ਬਹੁ-ਮੁੜ ਗੱਲਬਾਤਾਂ

Responses API ਨਿਰਦੇਸ਼ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਅਤੇ ਬਹੁ-ਮੁੜ ਚੈਟਬੋਟ ਦੋਵਾਂ ਲਈ ਚੰਗੀ ਤਰ੍ਹਾਂ ਉਪਯੋਗੀ ਹੈ - ਤੁਸੀਂ `input` ਵਿੱਚ ਸੁਨੇਹਿਆਂ ਦੀ ਸੂਚੀ ਪੈਅਦੇ ਹੋ ਜੋ ਗੱਲਬਾਤ ਬਣਾਉਂਦਾ ਹੈ:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

ਇਸ ਵਿਸ਼ੇਸ਼ਤਾ ਬਾਰੇ ਹੋਰ ਇਕ ਅਧਿਆਇ ਵਿੱਚ ਵਧੇਰੇ ਜਾਣਕਾਰੀ ਮਿਲੇਗੀ।

## ਅਭਿਆਸ - ਤੁਹਾਡੀ ਪਹਿਲੀ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ

ਹੁਣ ਜਦੋਂ ਅਸੀਂ openai ਸੈਟਅਪ ਅਤੇ ਸੰਰਚਨਾ ਸਿੱਖ ਲਈ ਹੈ, ਸਮਾਂ ਹੈ ਆਪਣੀ ਪਹਿਲੀ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਬਨਾਉਣ ਦਾ। ਆਪਣੀ ਐਪ ਬਣਾਉਣ ਲਈ ਇਹ ਕਦਮ ਲਵੋ:

1. ਇੱਕ ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਓ ਅਤੇ openai ਇੰਸਟਾਲ ਕਰੋ:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > ਜੇ ਤੁਸੀਂ Windows ਵਰਤ ਰਹੇ ਹੋ ਤਾਂ `source venv/bin/activate` ਦੀ ਥਾਂ `venv\Scripts\activate` ਟਾਈપ ਕਰੋ।

   > [!NOTE]
   > ਆਪਣੀ Azure OpenAI ਕੁੰਜੀ ਇਹਨਾਂ ਸਥਾਨਾਂ 'ਤੇ ਲੱਭੋ: [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), ਫਿਰ ਸ਼ੋਧ ਕਰੋ `Open AI`, `Open AI resource` ਚੁਣੋ, ਫਿਰ `Keys and Endpoint` ਤੇ ਜਾ ਕੇ `Key 1` ਦੀ ਕਾਪੀ ਤਿਆਰ ਕਰੋ।

1. ਇੱਕ ਫਾਇਲ _app.py_ ਬਣਾਓ ਅਤੇ ਹੇਠ ਲਿਖਿਆ ਕੋਡ ਪਾਓ:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # ਆਪਣਾ ਪੂਰਾ ਕਰਨ ਦਾ ਕੋਡ ਸ਼ਾਮਲ ਕਰੋ
   prompt = "Complete the following: Once upon a time there was a"

   # Responses API ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਕ ਬੇਨਤੀ ਕਰੋ
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # ਜਵਾਬ ਛਪਾਓ
   print(response.output_text)
   ```

   > [!NOTE]
   > ਜੇ ਤੁਸੀਂ ਸਾਫ OpenAI ਵਰਤ ਰਹੇ ਹੋ (Azure نہیں), ਤਾਂ ਵਰਤੋਂ ਕਰੋ `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (ਕੋਈ `base_url` ਨਹੀਂ) ਅਤੇ ਮਾਡਲ ਦਾ ਨਾਂ ਜਿਵੇਂ `gpt-4o-mini` ਦਿਓ deployment ਦੇ ਨਾਂ ਦੀ ਥਾਂ।

   ਤੁਸੀਂ ਹੇਠ ਲਿਖੇ ਵਾਂਗ ਨਤੀਜਾ ਵੇਖੋਗੇ:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## ਵੱਖ-ਵੱਖ ਕਿਸਮਾਂ ਦੇ ਪ੍ਰਾਂਪਟ, ਵੱਖ-ਵੱਖ ਕੰਮਾਂ ਲਈ

ਹੁਣ ਤੁਸੀਂ ਦੇਖਿਆ ਕਿ ਕਿਸ ਤਰ੍ਹਾਂ ਪ੍ਰਾਂਪਟ ਵਰਤ ਕੇ ਟੈਕਸਟ ਬਣਾਇਆ ਜਾਂਦਾ ਹੈ। ਤੁਹਾਡੇ ਕੋਲ ਇੱਕ ਪ੍ਰੋਗਰਾਮ ਵੀ ਚੱਲ ਰਿਹਾ ਹੈ ਜਿਸਨੂੰ ਤੁਸੀਂ ਬਦਲ ਕੇ ਵੱਖ-ਵੱਖ ਕਿਸਮਾਂ ਦੇ ਟੈਕਸਟ ਉਤਪੰਨ ਕਰ ਸਕਦੇ ਹੋ।

ਪ੍ਰਾਂਪਟ ਹਰ ਤਰ੍ਹਾਂ ਦੇ ਕੰਮਾਂ ਲਈ ਵਰਤੇ ਜਾ ਸਕਦੇ ਹਨ। ਉਦਾਹਰਣ ਲਈ:

- **ਟੈਕਸਟ ਦੀ ਕਿਸਮ ਉਤਪੰਨ ਕਰੋ**। ਉਦਾਹਰਣ ਵਜੋਂ, ਤੁਸੀਂ ਕੁਵਿਤਾ, ਪ੍ਰਸ਼ਨਾਂ ਦੀ ਸੂਚੀ ਜੋੜ ਸਕਦੇ ਹੋ ਆਦਿ।
- **ਜਾਣਕਾਰੀ ਲੱਭੋ**। ਤੁਸੀਂ ਪ੍ਰਾਂਪਟ ਵਰਤ ਕੇ ਜਾਣਕਾਰੀ ਲੱਭ ਸਕਦੇ ਹੋ, ਜਿਵੇਂ ਕਿ 'ਵੈੱਬ ਡਿਵੈਲਪਮੈਂਟ ਵਿੱਚ CORS ਦਾ ਕੀ ਮਤਲਬ ਹੈ?'।
- **ਕੋਡ ਬਣਾਓ**। ਪ੍ਰਾਂਪਟ ਵਰਤੀ ਜਾ ਸਕਦੀ ਹੈ ਕੋਡ ਬਣਾਉਣ ਲਈ, ਜਿਵੇਂ ਕਿ ਇਮੇਲ ਵੈਧਤਾ ਲਈ ਰੈਗੁਲਰ ਐਕਸਪ੍ਰੈਸ਼ਨ ਲਿਖਣਾ ਜਾਂ ਪੂਰੇ ਪ੍ਰੋਗਰਾਮ ਜਿਵੇਂ ਵੈੱਬ ਐਪ ਤਿਆਰ ਕਰਨਾ।

## ਇੱਕ ਵੱਧ ਕਾਰਗਰ ਵਰਤੋਂ ਦਾ ਮਾਮਲਾ: ਰੇਸਪੀ ਜਨਰੇਟਰ

ਕਲਪਨਾ ਕਰੋ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਘਰ ਵਿੱਚ ਸਮੱਗਰੀ ਹੈ ਅਤੇ ਤੁਸੀਂ ਕੁਝ ਬਣਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ। ਇਸ ਲਈ, ਤੁਹਾਨੂੰ ਇੱਕ ਰੇਸਪੀ ਦੀ ਲੋੜ ਹੈ। ਰੇਸਪੀ ਲੱਭਣ ਲਈ ਤੁਸੀਂ ਸਰਚ ਇੰਜਣ ਵਰਤ ਸਕਦੇ ਹੋ ਜਾਂ LLM ਦੀ ਮਦਦ ਲੈ ਸਕਦੇ ਹੋ।

ਤੁਸੀਂ ਕੁਝ ਇਸ ਤਰ੍ਹਾਂ ਦਾ ਪ੍ਰਾਂਪਟ ਲਿਖ ਸਕਦੇ ਹੋ:

> "ਨਿਮਨਲਿਖਿਤ ਸਮੱਗਰੀਆਂ ਵਾਲੇ ਵਿਅੰਜਨ ਲਈ 5 ਰੇਸਪੀਆਂ ਦਿਖਾਓ: ਚਿਕਨ, ਆਲੂ, ਤੇ ਗਾਜਰ। ਹਰ ਰੇਸਪੀ ਲਈ, ਸਾਰੀ ਵਰਤੀ ਗਈ ਸਮੱਗਰੀ ਦੀ ਸੁਚੀ ਦਿਓ।"

ਇਸ ਪ੍ਰਾਂਪਟ ਦੇ ਨਾਲ ਤੁਹਾਨੂੰ ਸਬੰਧਤ ਨਤੀਜਾ ਮਿਲ ਸਕਦਾ ਹੈ:

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

ਇਹ ਨਤੀਜਾ ਵਧੀਆ ਹੈ, ਮੈਨੂੰ ਪਤਾ ਲੱਗ ਗਿਆ ਕਿ ਕੀ ਬਣਾਉਣਾ ਹੈ। ਇਸ ਸਮੇਂ, ਕੁਝ ਸੁਤਰੰਸ਼ ਇਹ ਹੋ ਸਕਦੇ ਹਨ:

- ਉਹ ਸਮੱਗਰੀ ਫਿਲਟਰ ਕਰੋ ਜੋ ਮੈਨੂੰ ਪਸੰਦ ਨਹੀਂ ਜਾਂ ਜਿਸ ਨਾਲ ਮੈਨੂੰ ਐਲਰਜੀ ਹੈ।
- ਜੇ ਇੱਕ ਜਿੰਨਾ ਵੀ ਸਮੱਗਰੀ ਘਰ ਵਿੱਚ ਨਹੀਂ ਹੈ, ਤਾਂ ਇਸ ਲਈ ਖਰੀਦਦਾਰੀ ਦੀ ਸੂਚੀ ਬਣਾਓ।

ਉਪਰੋਕਤ ਮਾਮਲਿਆਂ ਲਈ, ਆਓ ਇੱਕ ਹੋਰ ਪ੍ਰਾਂਪਟ ਜੋੜੀਏ:

> "ਕਿਰਪਾ ਕਰਕੇ ਪ੍ਰੈਸਲੀ ਰੇਸਪੀਆਂ ਜੋ ਮੇਰੇ ਲਈ ਨੁਕਸਾਨਦਾਇਕ ਹਨ ਅਤੇ ਮੈਂਦੇ ਐਲਰਜਿਕ ਹਾਂ ਉਹ ਹਟਾਓ ਅਤੇ ਓਥੇ ਕੁਝ ਹੋਰ ਨਾਲ ਬਦਲੋ। ਨਾਲ ਹੀ, ਮੌਜੂਦਾ ਚਿਕਨ, ਆਲੂ ਅਤੇ ਗਾਜਰ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖ ਕੇ ਖਰੀਦਦਾਰੀ ਦੀ ਸੂਚੀ ਤਿਆਰ ਕਰੋ।"

ਹੁਣ ਤੁਹਾਨੂੰ ਨਵਾਂ ਨਤੀਜਾ ਮਿਲੇਗਾ, ਜਿਵੇਂ:

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

ਇਹ ਤੁਹਾਡੇ ਪੰਜ ਰੇਸਪੀਆਂ ਹਨ, ਜਿਨ੍ਹਾਂ ਵਿੱਚ ਲਸਣ ਨਹੀਂ ਹੈ ਅਤੇ ਤੁਹਾਡੇ ਘਰ ਵਾਲੀ ਸਮੱਗਰੀ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖ ਕੇ ਖਰੀਦਦਾਰੀ ਸੂਚੀ ਵੀ ਹੈ।

## ਅਭਿਆਸ - ਇੱਕ ਰੇਸਪੀ ਜਨਰੇਟਰ ਬਣਾਓ

ਹੁਣ ਜਦੋਂ ਅਸੀਂ ਇੱਕ ਸਨੀਹਾ ਕਥਾ ਵਜੋਂ ਅਭਿਆਸ ਕੀਤਾ ਹੈ, ਆਓ ਉਸਦੇ ਲਈ ਕੋਡ ਲਿਖੀਏ। ਇਸ ਲਈ ਇਹ ਕਦਮ ਲਵੋ:

1. ਮੌਜੂਦਾ _app.py_ ਫਾਇਲ ਨੂੰ ਸ਼ੁਰੂਆਤ ਲਈ ਵਰਤੋਂ
1. `prompt` ਵੈਰੀਅਬਲ ਲੱਭੋ ਅਤੇ ਇਸ ਦਾ ਕੋਡ ਹੇਠ ਲਿਖੇ ਤਰੀਕੇ ਨਾਲ ਬਦਲੋ:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   ਹੁਣ ਜੇ ਤੁਸੀਂ ਕੋਡ ਚਲਾਓ ਤਾਂ ਤੁਹਾਨੂੰ ਇਸ ਦੇ ਸਮਾਨ ਨਤੀਜਾ ਮਿਲੇਗਾ:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > ਨੋਟ ਕਰੋ, ਤੁਹਾਡਾ LLM ਨਾਨ ਡੀਟੇਰਮਿਨਿਸਟਿਕ ਹੈ, ਇਸ ਕਰਕੇ ਹਰ ਵਾਰੀ ਇਹ ਵੱਖ-ਵੱਖ ਨਤੀਜੇ ਦੇ ਸਕਦਾ ਹੈ।

   ਵਧੀਆ, ਆਓ ਵੇਖੀਏ ਇਸ ਨੂੰ ਕਿਵੇਂ ਸੁਧਾਰਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਸੁਧਾਰ ਲਈ, ਅਸੀਂ ਚਾਹੁੰਦੇ ਹਾਂ ਕਿ ਕੋਡ ਲਚੀਲਾ ਹੋਵੇ, ਤਾਂ ਜੋ ਸਮੱਗਰੀ ਅਤੇ ਰੇਸਪੀ ਦੀ ਗਿਣਤੀ ਬਦਲੀ ਜਾ ਸਕੇ।

1. ਆਓ ਕੋਡ ਇਸ ਤਰੀਕੇ ਨਾਲ ਬਦਲੋ:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # ਪ੍ਰੋੰਪਟ ਅਤੇ ਸਮੱਗਰੀ ਵਿੱਚ ਵਿਧੀਆਂ ਦੀ ਗਿਣਤੀ ਦੀ ਵਿਚੋਲੀ ਕਰਨਾ
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   ਟੈਸਟ ਚਲਾਉਣ ਲਈ ਇਹ ਕੋਡ ਇਸ ਤਰ੍ਹਾਂ ਲੱਗ ਸਕਦਾ ਹੈ:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### ਫਿਲਟਰ ਅਤੇ ਖਰੀਦਦਾਰੀ ਸੂਚੀ ਜੁੜਕੇ ਸੁਧਾਰ ਕਰੋ

ਸਾਡੇ ਕੋਲ ਹੁਣ ਇੱਕ ਕੰਮ ਕਰਨ ਵਾਲੀ ਐਪ ਹੈ ਜੋ ਰੇਸਪੀ ਬਣਾਉਂਦੀ ਹੈ ਅਤੇ ਜੋ ਉਪਭੋਗਤਾ ਦੇ ਇਨਪੁੱਟਾਂ ਤੇ ਵਧੀਕ ਨਮ੍ਰਤਾ ਨਾਲ ਨਿਰਭਰ ਕਰਦੀ ਹੈ, ਜਿਵੇਂ ਕਿ ਰੇਸਪੀ ਦੀ ਗਿਣਤੀ ਅਤੇ ਸਮੱਗਰੀ।

ਇਸਨੂੰ ਹੋਰ ਸੁਧਾਰਨ ਲਈ, ਅਸੀਂ ਇਹ ਚਾਹੁੰਦੇ ਹਾਂ:

- **ਸਮੱਗਰੀਆਂ ਨੂੰ ਫਿਲਟਰ ਕਰੋ**। ਅਸੀਂ ਉਹ ਸਮੱਗਰੀ ਹਟਾਉਂਣ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹਾਂ ਜੋ ਸਾਨੂੰ ਪਸੰਦ ਨਹੀਂ ਜਾਂ ਜਿਸ ਨਾਲ ਐਲਰਜੀ ਹੈ। ਇਹ ਕਰਨ ਲਈ, ਅਸੀਂ ਆਪਣੀ ਮੌਜੂਦਾ ਪ੍ਰਾਂਪਟ ਨੂੰ ਸੋਧ ਕੇ ਇਸ ਦੇ ਅੰਤੀਮ ਵਿੱਚ ਇੱਕ ਫਿਲਟਰ ਸ਼ਰਤ ਜੋੜ ਸਕਦੇ ਹਾਂ:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  ਉਪਰ, ਅਸੀਂ ਪ੍ਰਾਂਪਟ ਦੇ ਅੰਤ ਵਿੱਚ `{filter}` ਜੋੜਿਆ ਹੈ ਅਤੇ ਫਿਲਟਰ ਮੁੱਲ ਉਪਭੋਗਤਾ ਤੋਂ ਲਿਆ ਗਿਆ ਹੈ।

  ਪ੍ਰੋਗਰਾਮ ਚਲਾਉਣ ਲਈ ਇੱਕ ਉਦਾਹਰਣ ਇਨਪੁੱਟ ਹੁਣ ਇਸ ਤਰ੍ਹਾਂ ਦਿੱਸ ਸਕਦਾ ਹੈ:

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

  ਦੇਖੋ ਜੇ ਕਿਸੇ ਰੇਸਪੀ ਵਿੱਚ ਦੂਧ ਹੈ ਤਾਂ ਉਹ ਫਿਲਟਰ ਕੀਤਾ ਗਿਆ ਹੈ। ਪਰ ਜੇ ਤੁਸੀਂ ਲੈਕਟੋਜ਼ ਇੰਟੋਲਰੈਂਟ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਚੀਜ਼ ਵਾਲੀਆਂ ਰੇਸਪੀਆਂ ਵੀ ਫਿਲਟਰ ਕਰਨਾ ਚਾਹੋਗੇ, ਇਸ ਲਈ ਇਹ ਸਾਫ ਹੋਣਾ ਜਰੂਰੀ ਹੈ।


- **ਖਰੀਦਦਾਰੀ ਦੀ ਸੂਚੀ ਬਣਾਓ**। ਅਸੀਂ ਘਰ ਵਿੱਚ ਪਹਿਲਾਂ ਹੀ ਜੋ ਕੁਝ ਹੈ, ਉਸਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖਦੇ ਹੋਏ ਖਰੀਦਦਾਰੀ ਦੀ ਸੂਚੀ ਬਣਾਉਣੀ ਚਾਹੁੰਦੇ ਹਾਂ।

  ਇਸ ਫੰਕਸ਼ਨਲਟੀ ਲਈ, ਅਸੀਂ ਸਾਰੀ ਗੱਲ ਇੱਕ ਪ੍ਰਾਂਪਟ ਵਿੱਚ ਹੱਲ ਕਰ ਸਕਦੇ ਹਾਂ ਜਾਂ ਇਸਨੂੰ ਦੋ ਪ੍ਰਾਂਪਟਾਂ ਵਿੱਚ ਵੰਡ ਸਕਦੇ ਹਾਂ। ਚਲੋ ਦੂਜੇ ਤਰੀਕੇ ਨੂੰ ਅਜ਼ਮਾਈਏ। ਇੱਥੇ ਅਸੀਂ ਇੱਕ ਵਾਧੂ ਪ੍ਰਾਂਪਟ ਸ਼ਾਮਲ ਕਰਨ ਦੀ ਸਿਫਾਰਿਸ਼ ਕਰ ਰਹੇ ਹਾਂ, ਪਰ ਇਹ ਕੰਮ ਕਰਨ ਲਈ, ਸਾਨੂੰ ਪਹਿਲੇ ਪ੍ਰਾਂਪਟ ਦੇ ਨਤੀਜੇ ਨੂੰ ਦੂਜੇ ਪ੍ਰਾਂਪਟ ਦੇ ਸੰਦਰਭ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰਨਾ ਪਵੇਗਾ।

  ਉਸ ਕੋਡ ਦਾ ਹਿੱਸਾ ਲੱਭੋ ਜੋ ਪਹਿਲੇ ਪ੍ਰਾਂਪਟ ਦੇ ਨਤੀਜੇ ਨੂੰ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ ਅਤੇ ਹੇਠ ਲਿਖਿਆ ਕੋਡ ਉਸਦੇ ਨਾਲ ਹੇਠਾਂ ਜੋੜੋ:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # ਪ੍ਰਤੀਕਿਰਿਆ ਪ੍ਰਿੰਟ ਕਰੋ
  print("Shopping list:")
  print(response.output_text)
  ```

  ਹੇਠ ਲਿਖੇ ਗੱਲਾਂ ਨੂੰ ਧਿਆਨ ਦਿਓ:

  1. ਅਸੀਂ ਇੱਕ ਨਵਾਂ ਪ੍ਰਾਂਪਟ ਤਿਆਰ ਕਰ ਰਹੇ ਹਾਂ ਜੋ ਪਹਿਲੇ ਪ੍ਰਾਂਪਟ ਦੇ ਨਤੀਜੇ ਨੂੰ ਨਵੇਂ ਪ੍ਰਾਂਪਟ ਨਾਲ ਜੋੜਦਾ ਹੈ:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. ਅਸੀਂ ਇੱਕ ਨਵੀਂ ਬੇਨਤੀ ਕਰਦੇ ਹਾਂ, ਪਰ ਪਹਿਲੇ ਪ੍ਰਾਂਪਟ ਵਿੱਚ ਪੁੱਛੇ ਟੋਕਨ ਦੀ ਗਿਣਤੀ ਨੁੰ ਵੀ ਧਿਆਨ ਵਿੱਚ ਰੱਖਦੇ ਹਾਂ, ਇਸ ਵਾਰੀ ਅਸੀਂ ਕਹਿੰਦੇ ਹਾਂ `max_output_tokens` 1200 ਹੈ।

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     ਇਸ ਕੋਡ ਨੂੰ ਚਲਾਉਂਦੇ ਹੋਏ, ਅਸੀਂ ਹੁਣ ਹੇਠ ਲਿਖੇ ਆਉਟਪੁੱਟ 'ਤੇ ਪਹੁੰਚਦੇ ਹਾਂ:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## ਤੁਹਾਡੇ ਸੈਟਅੱਪ ਨੂੰ ਸੁਧਾਰੋ

ਇਸ ਸਮੇਂ ਸਾਡੇ ਕੋਲ ਇੱਕ ਐਸਾ ਕੋਡ ਹੈ ਜੋ ਕੰਮ ਕਰਦਾ ਹੈ, ਪਰ ਕੁਝ ਸੋਧਾਂ ਹਨ ਜੋ ਅਸੀਂ ਚੀਜ਼ਾਂ ਨੂੰ ਹੋਰ ਬਿਹਤਰ ਬਣਾਉਣ ਲਈ ਕਰ ਸਕਦੇ ਹਾਂ। ਕੁਝ ਗੱਲਾਂ ਜੋ ਅਸੀਂ ਕਰ ਸਕਦੇ ਹਾਂ, ਉਹ ਹਨ:

- **ਰਹਸਿਆਂ ਨੂੰ ਕੋਡ ਤੋਂ ਅਲੱਗ ਕਰੋ**, ਜਿਵੇਂ ਕਿ API ਕੁੰਜੀ। ਰਹਸੇ ਕੋਡ ਵਿੱਚ ਨਹੀਂ ਹੋਣੇ ਚਾਹੀਦੇ ਅਤੇ ਉਹਨਾਂ ਨੂੰ ਸੁਰੱਖਿਅਤ ਥਾਂ 'ਤੇ ਸਟੋਰ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਰਹਸਿਆਂ ਨੂੰ ਕੋਡ ਤੋਂ ਅਲੱਗ ਕਰਨ ਲਈ ਅਸੀਂ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਅਤੇ `python-dotenv` ਵਰਗੀਆਂ ਲਾਈਬ੍ਰੇਰੀਆਂ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹਾਂ ਜੋ ਉਹਨਾਂ ਨੂੰ ਫਾਈਲ ਤੋਂ ਲੋਡ ਕਰਦੀਆਂ ਹਨ। ਕੋਡ ਵਿੱਚ ਇਹ ਇੰਝ ਦਿਖਾਈ ਦੇਵੇਗਾ:

  1. ਇੱਕ `.env` ਫਾਈਲ ਬਣਾਓ ਜਿਸ ਵਿੱਚ ਹੇਠ ਲਿਖਿਆ ਸਮੱਗਰੀ ਹੋਵੇ:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > ਧਿਆਨ ਦਿਓ, Microsoft Foundry ਵਿੱਚ Azure OpenAI ਲਈ, ਤੁਹਾਨੂੰ ਬਦਲ ਕੇ ਹੇਠ ਲਿਖੇ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਸੈੱਟ ਕਰਨੇ ਪੈਣਗੇ:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     ਕੋਡ ਵਿੱਚ ਤੁਸੀਂ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਇਸ ਤਰ੍ਹਾਂ ਲੋਡ ਕਰੋਗੇ:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **ਟੋਕਨ ਦੀ ਲੰਬਾਈ 'ਤੇ ਇੱਕ ਸ਼ਬਦ**। ਸਾਨੂੰ ਇਹ ਧਿਆਨ ਵਿੱਚ ਰੱਖਣਾ ਚਾਹੀਦਾ ਹੈ ਕਿ ਅਸੀਂ ਕਿੰਨੇ ਟੋਕਨ ਵਰਤਕੇ ਲਿਖਤ ਤਿਆਰ ਕਰ ਰਹੇ ਹਾਂ। ਟੋਕਨਾਂ ਦੀ ਲਾਗਤ ਹੁੰਦੀ ਹੈ, ਇਸ ਲਈ ਜਿੱਥੇ ਸੰਭਵ ਹੋਵੇ, ਸਾਨੂੰ ਵਰਤੇ ਗਏ ਟੋਕਨ ਦੀ ਗਿਣਤੀ ਨੂੰ ਸਾਬਤਕਾਰਿਤ ਅਤੇ ਕਿਫਾਇਤੀ ਬਣਾਉਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਨੀ ਚਾਹੀਦੀ ਹੈ। ਉਦਾਹਰਣ ਲਈ, ਕੀ ਅਸੀਂ ਪ੍ਰਾਂਪਟ ਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਲਿਖ ਸਕਦੇ ਹਾਂ ਕਿ ਘੱਟ ਟੋਕਨ ਦੀ ਲੋੜ ਹੋਵੇ?

  ਟੋਕਨ ਦੀ ਗਿਣਤੀ ਬਦਲਣ ਲਈ, ਤੁਸੀਂ `max_output_tokens` ਪੈਰਾਮੀਟਰ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ। ਉਦਾਹਰਣ ਲਈ, ਜੇ ਤੁਸੀਂ 100 ਟੋਕਨ ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਇਹ ਕਰ ਸਕਦੇ ਹੋ:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **ਤਾਪਮਾਨ (ਤੇਮਪਰੇਚਰ) ਨਾਲ ਪ੍ਰਯੋਗ**। ਤਾਪਮਾਨ ਇੱਕ ਗੱਲ ਹੈ ਜਿਸ ਬਾਰੇ ਅਸੀਂ ਇਸ ਤੱਕ ਗੱਲ ਨਹੀਂ ਕੀਤੀ, ਪਰ ਇਹ ਸਾਡੇ ਪ੍ਰੋਗ੍ਰਾਮ ਦੀ ਕਾਰਗੁਜ਼ਾਰੀ ਲਈ ਇੱਕ ਜਰੂਰੀ ਸੰਦਰਭ ਹੈ। ਜਿੰਨਾ ਵੱਧ ਤਾਪਮਾਨ ਮੁੱਲ ਹੋਵੇਗਾ, ਆਉਟਪੁੱਟ ਉਤਨੀ ਹੀ ਜਿਆਦਾ ਬੇਤਰਤੀਬ ਹੋਵੇਗਾ। ਵਿਰੋਧ ਵਿੱਚ, ਜਿੰਨਾ ਘੱਟ ਤਾਪਮਾਨ ਮੁੱਲ ਹੋਵੇਗਾ, ਆਉਟਪੁੱਟ ਉਤਨਾ ਹੀ ਜਿਆਦਾ ਅਨੁਮਾਨਯੋਗ ਹੋਵੇਗਾ। ਸੋਚੋ ਕਿ ਤੁਸੀਂ ਆਪਣੇ ਆਉਟਪੁੱਟ ਵਿੱਚ ਫ਼ਰਕ ਚਾਹੁੰਦੇ ਹੋ ਜਾਂ ਨਹੀਂ।

  ਤਾਪਮਾਨ ਬਦਲਣ ਲਈ, ਤੁਸੀਂ `temperature` ਪੈਰਾਮੀਟਰ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ। ਉਦਾਹਰਣ ਲਈ, ਜੇ ਤੁਸੀਂ 0.5 ਦਾ ਤਾਪਮਾਨ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਇਹ ਕਰਨਾ:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > ਧਿਆਨ ਦਿਓ, 1.0 ਦੇ ਨੇੜੇ ਹੋਣ 'ਤੇ ਆਉਟਪੁੱਟ ਜਿਆਦਾ ਬਦਲਦਾ ਰਹੇਗਾ।

## ਅਸਾਈਨਮੈਂਟ

ਇਸ ਅਸਾਈਨਮੈਂਟ ਲਈ, ਤੁਸੀਂ ਚੁਣ ਸਕਦੇ ਹੋ ਕਿ ਕੀ ਬਣਾਉਣਾ ਹੈ।

ਇੱਥੇ ਕੁਝ ਸਿਫਾਰਸ਼ਾਂ ਹਨ:

- ਰੈਸੀਪੀ ਜੈਨਰੇਟਰ ਐਪ ਨੂੰ ਹੋਰ ਬਿਹਤਰ ਬਣਾਉਣ ਲਈ ਸੋਧੋ। ਤਾਪਮਾਨ ਮੁੱਲਾਂ ਅਤੇ ਪ੍ਰਾਂਪਟਾਂ ਨਾਲ ਖੇਡੋ ਅਤੇ ਵੇਖੋ ਕਿ ਤੁਸੀਂ ਕਿਸ ਤਰ੍ਹਾਂ ਦੇ ਨਤੀਜੇ ਲਿਆ ਸਕਦੇ ਹੋ।
- "ਅਧਿਐਨ ਸਾਥੀ" ਬਣਾਓ। ਇਹ ਐਪ ਕਿਸੇ ਵਿਸ਼ੇ ਬਾਰੇ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਦੇ ਸਕਦੀ ਹੈ, ਉਦਾਹਰਣ ਲਈ Python। ਤੁਹਾਡੇ ਕੋਲ ਐਸੇ ਪ੍ਰਾਂਪਟ ਹੋ ਸਕਦੇ ਹਨ "Python ਵਿੱਚ ਕਿਸੇ ਵਿਸ਼ੇ ਦਾ ਕੀ ਮਤਲਬ ਹੈ?", ਜਾਂ ਕੋਈ ਪ੍ਰਾਂਪਟ ਕਿ ਮੈਂ ਕਿਸੇ ਵਿਸ਼ੇ ਲਈ ਕੋਡ ਦਿਖਾਓ ਆਦਿ।
- ਇਤਿਹਾਸ ਬਾਟ, ਇਤਿਹਾਸ ਨੂੰ ਜਿਊਂਦਾ ਕਰੋ, ਬਾਟ ਨੂੰ ਇੱਕ ਵਿਸ਼ੇਸ਼ ਇਤਿਹਾਸਕ ਪਾਤਰ ਵਜੋਂ ਕਿਰਦਾਰ ਨਿਭਾਉਣ ਲਈ ਕਹੋ ਅਤੇ ਉਸਦੇ ਜੀਵਨ ਅਤੇ ਸਮੇਂ ਬਾਰੇ ਸਵਾਲਾਂ ਪੁੱਛੋ।

## ਹੱਲ

### ਅਧਿਐਨ ਸਾਥੀ

ਹੇਠਾਂ ਇੱਕ ਸ਼ੁਰੂਆਤੀ ਪ੍ਰਾਂਪਟ ਦਿੱਤਾ ਗਿਆ ਹੈ, ਦੇਖੋ ਕਿ ਤੁਸੀਂ ਇਸ ਨੂੰ ਕਿਵੇਂ ਵਰਤ ਸਕਦੇ ਹੋ ਅਤੇ ਇਸ ਨੂੰ ਆਪਣੀ ਪਸੰਦ ਅਨੁਸਾਰ ਸੋਧ ਸਕਦੇ ਹੋ।

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### ਇਤਿਹਾਸ ਬਾਟ

ਇੱਥੇ ਕੁਝ ਪ੍ਰਾਂਪਟ ਹਨ ਜੋ ਤੁਸੀਂ ਵਰਤ ਸਕਦੇ ਹੋ:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## ਗਿਆਨ ਜਾਂਚ

ਤਾਪਮਾਨ (temperature) ਦਾ ਕੀ ਮਤਲਬ ਹੈ?

1. ਇਹ ਨਿਰਧਾਰਤ ਕਰਦਾ ਹੈ ਕਿ ਆਉਟਪੁੱਟ ਕਿੰਨਾ ਬੇਤਰਤੀਬ ਹੋਵੇਗਾ।
1. ਇਹ ਨਿਰਧਾਰਤ ਕਰਦਾ ਹੈ ਕਿ ਜਵਾਬ ਕਿੰਨਾ ਵੱਡਾ ਹੋਵੇਗਾ।
1. ਇਹ ਨਿਰਧਾਰਤ ਕਰਦਾ ਹੈ ਕਿ ਕਿੰਨੇ ਟੋਕਨ ਵਰਤੇ ਜਾਣਗੇ।

## 🚀 ਚੈਲੇਂਜ

ਜਦੋਂ ਅਸਾਈਨਮੈਂਟ 'ਤੇ ਕੰਮ ਕਰ ਰਹੇ ਹੋ, ਤਾਪਮਾਨ ਨੂੰ ਵੱਖਰੇ-ਵੱਖਰੇ ਮੁੱਲਾਂ ਤੇ ਸੈੱਟ ਕਰਕੇ ਦੇਖੋ, ਜਿਵੇਂ 0, 0.5, ਅਤੇ 1। ਯਾਦ ਰੱਖੋ ਕਿ 0 ਸਭ ਤੋਂ ਘੱਟ ਬਦਲਾਅ ਹੈ ਅਤੇ 1 ਸਭ ਤੋਂ ਜ਼ਿਆਦਾ। ਤੁਹਾਡੇ ਐਪ ਲਈ ਸਭ ਤੋਂ ਵਧੀਆ ਮੁੱਲ ਕਿਹੜਾ ਹੈ?

## ਸ਼ਾਬਾਸ਼! ਆਪਣਾ ਅਧਿਐਨ ਜਾਰੀ ਰੱਖੋ

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਸਾਡੇ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ਨੂੰ ਦੇਖੋ ਤਾਂ ਜੋ ਤੁਸੀਂ ਆਪਣੀ Generative AI ਦੀ ਜਾਣਕਾਰੀ ਵਿੱਚ ਵਾਧਾ ਕਰ ਸਕੋ!

ਲੈਸਨ 7 ਤੇ ਜਾਓ ਜਿੱਥੇ ਅਸੀਂ ਵੇਖਾਂਗੇ ਕਿ [ਚੈਟ ਐਪਲੀਕੇਸ਼ਨ ਕਿਵੇਂ ਬਣਾਏ ਜਾਣ](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)ਗੀਆਂ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->