# ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪਲੀਕੇਸ਼ਨਾਂ ਦਾ ਨਿਰਮਾਣ

[![ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪਲੀਕੇਸ਼ਨਾਂ ਦਾ ਨਿਰਮਾਣ](../../../translated_images/pa/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(ਇਸ ਪਾਠ ਦਾ ਵੀਡੀਓ ਦੇਖਣ ਲਈ ਉਪਰ ਦਿੱਤੀ ਤਸਵੀਰ 'ਤੇ ਕਲਿੱਕ ਕਰੋ)_

ਤੁਸੀਂ ਇਸ ਕੋਰਸ ਦੇ ਦੌਰਾਨ ਦੇਖਿਆ ਹੈ ਕਿ ਕੁਝ ਮੁੱਖ ਧਾਰਣਾਵਾਂ ਹਨ ਜਿਵੇਂ ਕਿ ਪ੍ਰੰਪਟ ਅਤੇ ਇਥੇ ਤੱਕ ਕਿ ਪੂਰੀ ਵਿਧਾ "prompt engineering" ਵੀ ਹੈ। ਬਹੁਤ ਸਾਰੇ ਸਾਧਨ ਜਿਨ੍ਹਾਂ ਨਾਲ ਤੁਸੀਂ ਇੰਟਰੈਕਟ ਕਰ ਸਕਦੇ ਹੋ ਜਿਵੇਂ ਕਿ ChatGPT, Office 365, Microsoft Power Platform ਅਤੇ ਹੋਰ, ਤੁਹਾਨੂੰ ਕੁਝ ਹਾਸਲ ਕਰਨ ਲਈ ਪ੍ਰੰਪਟਾਂ ਦੀ ਵਰਤੋਂ ਕਰਨ ਵਿੱਚ ਸਹਾਇਤਾ ਕਰਦੇ ਹਨ।

ਐਪ ਵਿੱਚ ਅਜਿਹਾ ਤਜਰਬਾ ਸ਼ਾਮਲ ਕਰਨ ਲਈ, ਤੁਹਾਨੂੰ ਪ੍ਰੰਪਟ, ਪੂਰਨਾਵਾਂ ਵਰਗੀਆਂ ਧਾਰਣਾਵਾਂ ਨੂੰ ਸਮਝਣ ਦੀ ਲੋੜ ਹੈ ਅਤੇ ਕੰਮ ਕਰਨ ਲਈ ਇੱਕ ਲਾਇਬ੍ਰੇਰੀ ਚੁਣਨੀ ਪੈਂਦੀ ਹੈ। ਇਹੀ ਤੁਸੀਂ ਇਸ ਅਧਿਆਇ ਵਿੱਚ ਸਿੱਖੋਗੇ।

## ਜਾਣੂ ਕਰਵਾਈ

ਇਸ ਅਧਿਆਇ ਵਿੱਚ, ਤੁਸੀਂ:

- openai ਲਾਇਬ੍ਰੇਰੀ ਅਤੇ ਇਸ ਦੀਆਂ ਮੁੱਖ ਧਾਰਣਾਵਾਂ ਬਾਰੇ ਸਿੱਖੋਗੇ।
- openai ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਬਣਾਉਗੇ।
- ਡਿੱਚ ਉਹੋ ਪ੍ਰੰਪਟ, ਤਾਪਮਾਨ ਅਤੇ ਟੋਕਨ ਵਰਗੀਆਂ ਧਾਰਣਾਵਾਂ ਦੀ ਵਰਤੋਂ ਕਿਵੇਂ ਕਰੀਦਾ ਹੈ ਸਮਝੋਗੇ ਜੋ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਬਣਾਉਣ ਲਈ ਜਰੂਰੀ ਹਨ।

## ਸਿੱਖਣ ਦੇ ਲਕੜ

ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਵਿੱਚ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- ਇਹ ਸਮਝਾਉ ਕਿ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਕੀ ਹੈ।
- openai ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਬਣਾਉਣਾ।
- ਆਪਣੇ ਐਪ ਨੂੰ ਹੋਰ ਜਿਆਦਾ ਜਾਂ ਘੱਟ ਟੋਕਨ ਵਰਤਣ ਲਈ ਤੇ ਤਾਪਮਾਨ ਬਦਲ ਕੇ ਵੱਖ-ਵੱਖ ਰਿਜ਼ਲਟ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਸੰਰੱਚਿਤ ਕਰਨਾ।

## ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਕੀ ਹੈ?

ਆਮ ਤੌਰ 'ਤੇ ਜਦੋਂ ਤੁਸੀਂ ਕੋਈ ਐਪ ਬਣਾਉਂਦੇ ਹੋ ਤਾਂ ਉਹ ਕਿਸੇ ਕਿਸਮ ਦਾ ਇੰਟਰਫੇਸ ਹੁੰਦਾ ਹੈ ਜਿਵੇਂ:

- ਕਮਾਂਡ-ਆਧਾਰਿਤ। ਕਨਸੋਲ ਐਪ ਆਮ ਐਪ ਹੁੰਦੇ ਹਨ ਜਿੱਥੇ ਤੁਸੀਂ ਕਮਾਂਡ ਟਾਈਪ ਕਰਦੇ ਹੋ ਅਤੇ ਉਹ ਕੰਮ ਕਰਦਾ ਹੈ। ਉਦਾਹਰਨ ਵਜੋਂ, `git` ਇੱਕ ਕਮਾਂਡ-ਆਧਾਰਿਤ ਐਪ ਹੈ।
- ਯੂਜ਼ਰ ਇੰਟਰਫੇਸ (UI)। ਕਈ ਐਪਾਂ ਵਿੱਚ ਗ੍ਰਾਫਿਕਲ ਯੂਜ਼ਰ ਇੰਟਰਫੇਸ (GUIs) ਹੁੰਦਾ ਹੈ ਜਿੱਥੇ ਤੁਸੀਂ ਬਟਨਾਂ ਤੇ ਕਲਿੱਕ ਕਰਦੇ ਹੋ, ਟੈਕਸਟ ਦਾਖਲ ਕਰਦੇ ਹੋ, ਚੋਣ ਕਰਦੇ ਹੋ ਅਤੇ ਹੋਰ।

### ਕਨਸੋਲ ਅਤੇ UI ਐਪ ਸੀਮਿਤ ਹਨ

ਇਸਨੂੰ ਉਸ ਕਮਾਂਡ-ਆਧਾਰਿਤ ਐਪ ਨਾਲ ਤੁਲਨਾ ਕਰੋ ਜਿੱਥੇ ਤੁਸੀਂ ਕਮਾਂਡ ਟਾਈਪ ਕਰਦੇ ਹੋ:

- **ਇਹ ਸੀਮਿਤ ਹੈ**। ਤੁਸੀਂ ਕੋਈ ਵੀ ਕਮਾਂਡ ਨਹੀਂ ਟਾਈਪ ਕਰ ਸਕਦੇ, ਸਿਰਫ ਉਹੀ ਜੋ ਐਪ ਸਹਿਯੋਗ ਕਰਦਾ ਹੈ।
- **ਭਾਸ਼ਾ ਵਿਸ਼ੇਸ਼**। ਕੁਝ ਐਪਨ ਹੋਰ-ਭਾਸ਼ਾਵਾਂ ਦਾ ਸਹਿਯੋਗ ਕਰਦੇ ਹਨ, ਪਰ ਡਿਫਾਲਟ ਤੌਰ ਤੇ ਐਪ ਇੱਕ ਵਿਸ਼ੇਸ਼ ਭਾਸ਼ਾ ਲਈ ਬਣਾਇਆ ਜਾਂਦਾ ਹੈ, ਜੇਕਰ ਤੁਸੀਂ ਹੋਰ ਭਾਸ਼ਾਵਾਂ ਸਹਿਯੋਗ ਸ਼ਾਮਲ ਵੀ ਕਰੋ।

### ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਦੇ ਫਾਇਦੇ

ਤਾਂ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਕਿਵੇਂ ਵੱਖਰਾ ਹੈ?

ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਵਿੱਚ ਤੁਹਾਨੂੰ ਹੋਰ ਲਚੀਲਾਪਣ ਮਿਲਦਾ ਹੈ, ਤੁਸੀਂ ਕਮਾਂਡ ਜਾਂ ਖਾਸ ਇੰਪੁੱਟ ਭਾਸ਼ਾ ਤੱਕ ਸੀਮਿਤ ਨਹੀਂ ਹੁੰਦੇ। ਬਦਲੇ ਵਿੱਚ, ਤੁਸੀਂ ਸਾਮਾਨ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਭਾਸ਼ਾ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਐਪ ਨਾਲ ਗੱਲਬਾਤ ਕਰ ਸਕਦੇ ਹੋ। ਇਕ ਹੋਰ ਫਾਇਦਾ ਇਹ ਹੈ ਕਿ ਤੁਸੀਂ ਪਹਿਲਾਂ ਹੀ ਇੱਕ ਡੇਟਾ ਸਰੋਤ ਨਾਲ ਗੱਲਬਾਤ ਕਰ ਰਹੇ ਹੋ ਜੋ ਜਾਣਕਾਰੀ ਦੇ ਵੱਡੇ ਸੰਘਟਨ 'ਤੇ ਟਰੇਂਡ ਕੀਤਾ ਗਿਆ ਹੈ, ਜਦ ਕਿ ਪਰੰਪਰਾਗਤ ਐਪ ਡੇਟਾਬੇਸ ਵਿੱਚ ਮੌਜੂਦ ਜਾਣਕਾਰੀ ਉੱਤੇ ਸੀਮਿਤ ਹੋ ਸਕਦਾ ਹੈ।

### ਮੈਂ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ ਨਾਲ ਕੀ ਬਣਾਉਂਦਾ ਹਾਂ?

ਤੁਸੀਂ ਬਹੁਤ ਕੁਝ ਬਣਾਉ ਸਕਦੇ ਹੋ। ਉਦਾਹਰਨ ਵਜੋਂ:

- **ਇੱਕ ਚੈਟਬੋਟ**। ਚੈਟਬੋਟ ਜੋ ਤੁਸੀਂ ਆਪਣੀ ਕੰਪਨੀ ਅਤੇ ਇਸਦਾ ਉਤਪਾਦਾਂ ਬਾਰੇ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਦਿਵਾਉਂਦਾ ਹੈ, ਵਰਗਾ ਚੰਗਾ ਮਿਲਾਪ ਹੋ ਸਕਦਾ ਹੈ।
- **ਮਦਦਗਾਰ**। LLMs ਟੈਕਸਟ ਨੂੰ ਸੰਖੇਪਿਤ ਕਰਨ, ਸੂਚਨਾਵਾਂ ਪ੍ਰਾਪਤ ਕਰਨ, ਰੇਜ਼ਿਊਮੇ ਜਿਹੇ ਟੈਕਸਟ ਬਣਾਉਣ ਵਿੱਚ ਮਹਾਨ ਹਨ।
- **ਕੋਡ ਸਹਾਇਕ**। ਤੁਸੀਂ ਵਰਤੇ ਹੋਏ ਭਾਸ਼ਾ ਮਾਡਲ 'ਤੇ ਨਿਰਭਰ ਕਰਦੇ ਹੋਏ, ਐਸਾ ਕੋਡ ਸਹਾਇਕ ਬਣਾਉ ਸਕਦੇ ਹੋ ਜੋ ਕੋਡ ਲਿਖਣ ਵਿੱਚ ਸਹਾਇਤਾ ਕਰਦਾ ਹੈ। ਉਦਾਹਰਨ ਵਜੋਂ, ਤੁਸੀਂ GitHub Copilot ਅਤੇ ChatGPT ਵਰਗਾ ਉਤਪਾਦ ਵਰਤ ਸਕਦੇ ਹੋ ਜੋ ਕੋਡ ਲਿਖਣ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ।

## ਮੈਂ ਕਿਵੇਂ ਸ਼ੁਰੂ ਕਰਾਂ?

ਖੈਰ, ਤੁਹਾਨੂੰ ਇੱਕ LLM ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਕਰਨ ਦਾ ਤਰੀਕਾ ਲੱਭਣਾ ਪਵੇਗਾ ਜਿਸ ਵਿੱਚ ਆਮ ਤੌਰ ਤੇ ਇਹ ਦੋ ਤਰੀਕੇ ਹੁੰਦੇ ਹਨ:

- API ਦੀ ਵਰਤੋਂ ਕਰੋ। ਇੱਥੇ ਤੁਸੀਂ ਆਪਣੇ ਪ੍ਰੰਪਟ ਨਾਲ ਵੈਬ ਰਿਕਵੇਸਟ ਤਿਆਰ ਕਰਦੇ ਹੋ ਅਤੇ ਬਣੇ ਹੋਏ ਟੈਕਸਟ ਨੂੰ ਪ੍ਰਾਪਤ ਕਰਦੇ ਹੋ।
- ਇੱਕ ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਵਰਤੋਂ ਕਰੋ। ਲਾਇਬ੍ਰੇਰੀਆਂ API ਕਾਲਾਂ ਨੂੰ ਸੰਚਿਤ ਕਰਨ ਵਿੱਚ ਸਹਾਇਤਾ ਕਰਦੀਆਂ ਹਨ ਅਤੇ ਵਰਤਣ ਵਿੱਚ ਆਸਾਨ ਬਣਾਉਂਦੀਆਂ ਹਨ।

## ਲਾਇਬ੍ਰੇਰੀਆਂ/SDKs

LLMs ਨਾਲ ਕੰਮ ਕਰਨ ਲਈ ਕੁਝ ਮਸ਼ਹੂਰ ਲਾਇਬ੍ਰੇਰੀਆਂ ਹਨ ਜਿਵੇਂ:

- **openai**, ਇਹ ਲਾਇਬ੍ਰੇਰੀ ਤੁਹਾਡੇ ਮਾਡਲ ਨਾਲ ਜੁੜਨ ਅਤੇ ਪ੍ਰੰਪਟ ਭੇਜਣ ਨੂੰ ਸੌਖਾ ਬਣਾਉਂਦੀ ਹੈ।

ਫਿਰ ਕੁਝ ਉੱਚ-ਸਤਹੀ ਲਾਇਬ੍ਰੇਰੀਆਂ ਹਨ ਜਿਵੇਂ:

- **Langchain**। Langchain ਮਸ਼ਹੂਰ ਹੈ ਅਤੇ Python ਦਾ ਸਹਿਯੋਗ ਕਰਦਾ ਹੈ।
- **Semantic Kernel**। Semantic Kernel ਇੱਕ ਮਾਈਕ੍ਰੋਸਾਫਟ ਦੁਆਰਾ ਬਣਾਈ ਗਈ ਲਾਇਬ੍ਰੇਰੀ ਹੈ ਜੋ C#, Python, ਅਤੇ Java ਭਾਸ਼ਾਵਾਂ ਦਾ ਸਮਰਥਨ ਕਰਦੀ ਹੈ।

## openai ਨਾਲ ਪਹਿਲਾ ਐਪ

ਦੇਖੀਏ ਕਿ ਅਸੀਂ ਆਪਣਾ ਪਹਿਲਾ ਐਪ ਕਿਵੇਂ ਬਣਾਈਏ, ਸਾਨੂੰ ਕਿਹੜੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਲੋੜੀਂਦੀਆਂ ਹਨ, ਕਿੰਨਾ ਸਮੱਗਰੀ ਚਾਹੀਦੀ ਹੈ ਆਦਿ।

### openai ਨੂੰ ਇੰਸਟਾਲ ਕਰੋ

ਮੁਹੱਈਆ ਹਨ ਬਹੁਤ ਸਾਰੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਜੋ OpenAI ਜਾਂ Azure OpenAI ਨਾਲ ਸੰਚਾਰ ਕਰਨ ਲਈ ਹਨ। ਕਈ ਪ੍ਰੋਗਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ ਵਰਗੀ C#, Python, JavaScript, Java ਆਦਿ ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ। ਅਸੀਂ Python ਦੀ `openai` ਲਾਇਬ੍ਰੇਰੀ ਚੁਣੀ ਹੈ, ਇਸ ਲਈ ਅਸੀਂ ਇੰਜ `pip` ਦੁਆਰਾ ਇਸ ਨੂੰ ਇੰਸਟਾਲ ਕਰਾਂਗੇ।

```bash
pip install openai
```

### ਇੱਕ ਸਰੋਤ ਬਣਾਓ

ਤੁਸੀਂ ਹੇਠਾਂ ਦਿੱਤੇ ਕੰਮ ਕਰਨੇ ਹਨ:

- Azure 'ਤੇ ਇੱਕ ਖਾਤਾ ਬਣਾਓ [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)].
- Azure OpenAI ਲਈ ਪਹੁੰਚ ਪ੍ਰਾਪਤ ਕਰੋ। ਜਾਓ [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) ਅਤੇ ਪਹੁੰਚ ਲਈ ਅਰਜ਼ੀ ਦਿਓ।

  > [!NOTE]
  > ਲਿਖਾਈ ਦੇ ਵੇਲੇ, ਤੁਹਾਨੂੰ Azure OpenAI ਲਈ ਪਹੁੰਚ ਲਈ ਅਰਜ਼ੀ ਦੇਣੀ ਪੈਂਦੀ ਹੈ।

- Python <https://www.python.org/> ਇੰਸਟਾਲ ਕਰੋ।
- ਇੱਕ Azure OpenAI Service ਸਰੋਤ ਬਣਾਇਆ ਹੋਇਆ ਹੋਵੇ। ਇਸ ਮਦਦ ਨਾਲ ਦੇਖੋ ਕਿ ਕਿਵੇਂ [ਸਰੋਤ ਬਣਾਇਆ ਜਾਂਦਾ ਹੈ](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)।

### API ਕੁੰਜੀ ਅਤੇ ਐਨਡਪੌਇਂਟ ਲੱਭੋ

ਇਸ ਸਮੇਂ, ਤੁਹਾਨੂੰ ਆਪਣੇ `openai` ਲਾਇਬ੍ਰੇਰੀ ਨੂੰ ਦੱਸਣਾ ਪਵੇਗਾ ਕਿ ਕਿਹੜੀ API ਕੁੰਜੀ ਵਰਤਣੀ ਹੈ। ਆਪਣੀ API ਕੁੰਜੀ ਲਭਣ ਲਈ, ਆਪਣੀ Azure OpenAI ਸਰੋਤ ਦੇ "Keys and Endpoint" ਭਾਗ ਵਿੱਚ ਜਾਓ ਅਤੇ "Key 1" ਦੀ ਕੀਮਤ ਨਕਲ ਕਰੋ।

![Azure Portal ਵਿੱਚ Keys ਅਤੇ Endpoint ਸਰੋਤ ਬਲੇਡ](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

ਹੁਣ ਜਦ ਤੁਹਾਨੂੰ ਇਹ ਜਾਣਕਾਰੀ ਮਿਲ ਗਈ ਹੈ, ਆਓ ਲਾਇਬ੍ਰੇਰੀਆਂ ਨੂੰ ਇਹ ਵਰਤਣ ਲਈ ਕਹੀਏ।

> [!NOTE]
> ਆਪਣੀ API ਕੁੰਜੀ ਨੂੰ ਆਪਣੇ ਕੋਡ ਤੋਂ ਵੱਖਰਾ ਰੱਖਣਾ ਵਧੀਆ ਹੁੰਦਾ ਹੈ। ਤੁਸੀਂ ਇਸਨੂੰ environment variables ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕਰ ਸਕਦੇ ਹੋ।
>
> - environment variable `OPENAI_API_KEY` ਨੂੰ ਆਪਣੀ API ਕੁੰਜੀ ਸੈੱਟ ਕਰੋ।
>   `export OPENAI_API_KEY='sk-...'`

### Azure ਸੰਰਚਨਾ ਸੈੱਟ ਕਰੋ

ਜੇਕਰ ਤੁਸੀਂ Azure OpenAI ਵਰਤ ਰਹੇ ਹੋ (ਜੋ ਹੁਣ Microsoft Foundry ਦਾ ਹਿੱਸਾ ਹੈ), ਤਾਂ ਇਸ ਤਰ੍ਹਾਂ ਸੈੱਟ ਕਰੋ। ਅਸੀਂ ਸਧਾਰਣ `OpenAI` ਕਲਾਇੰਟ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਾਂ ਜੋ Azure OpenAI `/openai/v1/` ਐਨਡਪੌਇੰਟ 'ਤੇ ਹੈ, ਜੋ Responses API ਨਾਲ ਕੰਮ ਕਰਦਾ ਹੈ ਅਤੇ ਕਿਸੇ ਵੀ `api_version` ਦੀ ਲੋੜ ਨਹੀਂ:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

ਉੱਪਰ ਅਸੀਂ ਇਹ ਸੈੱਟ ਕਰ ਰਹੇ ਹਾਂ:

- `api_key`, ਇਹ ਤੁਹਾਡੀ API ਕੁੰਜੀ ਹੈ ਜੋ Azure Portal ਜਾਂ Microsoft Foundry ਪੋਰਟਲ ਤੋਂ ਮਿਲੇਗੀ।
- `base_url`, ਇਹ ਤੁਹਾਡਾ Foundry ਸਰੋਤ ਐਨਡਪੌਇੰਟ ਹੈ ਜਿਸ ਵਿੱਚ `/openai/v1/` ਜੋੜਿਆ ਗਿਆ ਹੈ। stable v1 ਐਨਡਪੌਇੰਟ OpenAI ਅਤੇ Azure OpenAI ਦੋਹਾਂ ਲਈ ਕੰਮ ਕਰਦਾ ਹੈ ਬਿਨਾਂ ਕਿਸੇ `api_version` ਦੇ ਪ੍ਰਬੰਧ ਦੇ।

> [!NOTE] > `os.environ` environment variables ਨੂੰ ਪੜ੍ਹਦਾ ਹੈ। ਤੁਸੀਂ ਇਸਦੀ ਵਰਤੋਂ environment variables ਜਿਵੇਂ ਕਿ `AZURE_OPENAI_API_KEY` ਅਤੇ `AZURE_OPENAI_ENDPOINT` ਨੂੰ ਪੜ੍ਹਨ ਲਈ ਕਰ ਸਕਦੇ ਹੋ। ਇਹ environment variables ਆਪਣੇ ਟਰਮੀਨਲ ਵਿੱਚ ਸੈੱਟ ਕਰੋ ਜਾਂ ਕੋਈ ਲਾਇਬ੍ਰੇਰੀ ਜਿਵੇਂ ਕਿ `dotenv` ਦੀ ਵਰਤੋਂ ਕਰੋ।

## ਟੈਕਸਟ ਬਣਾਓ

ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਕਰਨ ਦਾ ਤਰੀਕਾ Responses API ਦੀ `responses.create` ਮੈਥਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਹੈ। ਇਹ ਇੱਕ ਉਦਾਹਰਨ ਹੈ:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

ਉਪਰ ਦਿੱਤੇ ਕੋਡ ਵਿੱਚ, ਅਸੀਂ ਇੱਕ response ਬਣਾਉਂਦੇ ਹਾਂ ਅਤੇ ਮਾਡਲ ਅਤੇ ਪ੍ਰੰਪਟ ਪਾਸ ਕਰਦੇ ਹਾਂ। ਫਿਰ ਅਸੀਂ ਬਣੀ ਟੈਕਸਟ ਨੂੰ `response.output_text` ਰਾਹੀਂ ਪ੍ਰਿੰਟ ਕਰਦੇ ਹਾਂ।

### ਬਹੁ-ਵਾਰਤੀ ਗੱਲਬਾਤਾਂ

Responses API ਇਕੱਲੇ ਵਾਰ ਦੀ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਅਤੇ ਬਹੁ-ਵਾਰਤੀ ਚੈਟਬੋਟਾਂ ਦੋਹਾਂ ਲਈ ਵਧੀਆ ਹੈ - ਤੁਸੀਂ ਗੱਲਬਾਤ ਤਿਆਰ ਕਰਨ ਲਈ ਸੁਨੇਹਿਆਂ ਦੀ ਸੁਚੀ `input` ਵਿੱਚ ਦਿੰਦੇ ਹੋ:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

ਇਸ ਫੰਕਸ਼ਨਲਿਟੀ ਬਾਰੇ ਹੋਰ ਵਧੇਰੇ ਅਧਿਆਇ ਵਿੱਚ।

## ਅਭਿਆਸ - ਆਪਣਾ ਪਹਿਲਾ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਐਪ

ਹੁਣ ਜਦ ਅਸੀਂ openai ਸੈੱਟਅਪ ਅਤੇ ਸੰਰਚਿਤ ਕਰਨਾ ਸਿੱਖ ਲਿਆ, ਤਾਂ ਆਓ ਇਹ ਐਪ ਬਣਾਈਏ। ਐਪ ਬਣਾਉਣ ਲਈ, ਇਹ ਕਦਮ ਅਪਣਾਓ:

1. ਇੱਕ ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਓ ਅਤੇ openai ਇੰਸਟਾਲ ਕਰੋ:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > ਜੇਕਰ ਤੁਸੀਂ Windows ਵਰਤ ਰਹੇ ਹੋ ਤਾਂ `venv\Scripts\activate` ਦੀ ਬਜਾਏ `source venv/bin/activate` ਦਿਓ।

   > [!NOTE]
   > ਆਪਣੀ Azure OpenAI ਕੁੰਜੀ ਲੱਭਣ ਲਈ ਜਾਓ [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) ਅਤੇ `Open AI` ਖੋਜੋ, `Open AI resource` ਚੁਣੋ, ਫਿਰ `Keys and Endpoint` ਚੁਣੋ ਅਤੇ `Key 1` ਦੀ ਕੀਮਤ ਨਕਲ ਕਰੋ।

1. ਇੱਕ _app.py_ ਫਾਇਲ ਬਣਾਓ ਅਤੇ ਇਹ ਕੋਡ ਦੇਵੋ:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"

   # make a request using the Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # print response
   print(response.output_text)
   ```

   > [!NOTE]
   > ਜੇਕਰ ਤੁਸੀਂ ਸਿਧੀ OpenAI (Azure ਨਹੀਂ) ਵਰਤ ਰਹੇ ਹੋ, ਤਾਂ `client = OpenAI(api_key="<replace this value with your OpenAI key>")` ਵਰਤੋਂ (ਬਿਨਾਂ `base_url`) ਅਤੇ ਡੀਪਲੋਇਮੈਂਟ ਨਾਮ ਦੀ ਬਜਾਏ ਮਾਡਲ ਦਾ ਨਾਮ ਜਿਵੇਂ `gpt-5-mini` ਦਿਓ।

   ਤੁਹਾਡੇ ਕੋਲ ਕੁਝ ਇਸ ਤਰ੍ਹਾਂ ਨਤੀਜਾ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## ਵੱਖ-ਵੱਖ ਕਿਸਮਾਂ ਦੇ ਪ੍ਰੰਪਟ, ਵੱਖ-ਵੱਖ ਕੰਮਾਂ ਲਈ

ਹੁਣ ਤੁਸੀਂ ਦੇਖ ਲਿਆ ਕਿ ਪ੍ਰੰਪਟ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਟੈਕਸਟ ਕਿਵੇਂ ਜਨਰੇਟ ਕਰਨਾ ਹੈ। ਤੁਹਾਡੇ ਕੋਲ ਅਜੇ ਇਕ ਕਾਰਜਤਮਕ ਪ੍ਰੋਗ੍ਰਾਮ ਹੈ ਜਿਸਨੂੰ ਤੁਸੀਂ ਬਦਲ ਸਕਦੇ ਹੋ ਅਤੇ ਵੱਖ-ਵੱਖ ਕਿਸਮਾਂ ਦੇ ਟੈਕਸਟ ਜਨਰੇਟ ਕਰ ਸਕਦੇ ਹੋ।

ਪ੍ਰੰਪਟ ਹਰ ਕਿਸਮ ਦੇ ਕੰਮਾਂ ਲਈ ਵਰਤੇ ਜਾ ਸਕਦੇ ਹਨ। ਉਦਾਹਰਨ ਵਜੋਂ:

- **ਕਿਸੇ ਕਿਸਮ ਦਾ ਟੈਕਸਟ ਬਣਾਓ**। ਉਦਾਹਰਨ ਵਜੋਂ, ਤੁਸੀਂ ਕਵਿਤਾ, ਕਵਿਜ਼ ਲਈ ਸਵਾਲ ਆਦਿ ਜਨਰੇਟ ਕਰ ਸਕਦੇ ਹੋ।
- **ਸੂਚਨਾ ਲੱਭੋ**। ਤੁਸੀਂ ਪ੍ਰੰਪਟ ਦਾ ਵਰਤ ਕੇ ਸੂਚਨਾ ਲੱਭ ਸਕਦੇ ਹੋ ਜਿਵੇਂ '"ਵੈੱਬ ਡਿਵੈਲਪਮੈਂਟ ਵਿੱਚ CORS ਦਾ ਕੀ ਮਤਲਬ ਹੈ?"'।
- **ਕੋਡ ਬਣਾਓ**। ਤੁਸੀਂ ਕੋਡ ਬਣਾਉਣ ਲਈ ਪ੍ਰੰਪਟ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ, ਉਦਾਹਰਨ ਵਜੋਂ ਇਮੇਲ ਸੱਚਾਈ ਲਈ ਰੈਗੁਲਰ ਐਕਸਪ੍ਰੈਸ਼ਨ ਬਣਾਉਣਾ ਜਾਂ ਪੂਰਾ ਪ੍ਰੋਗ੍ਰਾਮ, ਜਿਵੇਂ ਵੈੱਬ ਐਪ, ਬਣਾਉਣਾ।

## ਇਕ ਹੋਰ ਪ੍ਰੈਟਿਕਲ ਉਦਾਹਰਨ: ਰੈਸਿਪੀ ਜਨਰੇਟਰ

ਸੋਚੋ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਘਰ ਵਿੱਚ ਕੁਝ ਸਮੱਗਰੀ ਹੈ ਅਤੇ ਤੁਸੀਂ ਕੁਝ ਬਣਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ। ਇਸ ਲਈ ਤੁਹਾਨੂੰ ਕੋਈ ਰੈਸਿਪੀ ਚਾਹੀਦੀ ਹੈ। ਰੈਸਿਪੀ ਲੱਭਣ ਦਾ ਇੱਕ ਤਰੀਕਾ ਹੈ ਸਰਚ ਇੰਜਣ ਦੀ ਵਰਤੋਂ ਕਰਨਾ ਜਾਂ ਤੁਸੀਂ ਇੱਕ LLM ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ।

ਤੁਸੀਂ ਐਡਾ ਪ੍ਰੰਪਟ ਲਿਖ ਸਕਦੇ ਹੋ:

> "ਮੇਰੇ ਲਈ 5 ਰੈਸਿਪੀਆਂ ਦਿਖਾਓ ਜਿਨ੍ਹਾਂ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਸਮੱਗਰੀ ਹਨ: ਚਿਕਨ, ਆਲੂ ਅਤੇ ਗਾਜਰ। ਹਰ ਰੈਸਿਪੀ ਲਈ ਸਾਰੀ ਵਰਤੀ ਸਮੱਗਰੀ ਲਿਸਟ ਕਰੋ।"

ਇਸ ਪ੍ਰੰਪਟ ਦੇ ਅਧਾਰ ਤੇ, ਤੁਹਾਨੂੰ ਮਿਲ ਸਕਦਾ ਹੈ ਕੁਝ ਗੱਲਬਾਤ ਜਿਹੜਾ ਵਿੱਚ ਲੱਗਦਾ ਹੈ:

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

ਇਹ ਨਤੀਜਾ ਚੰਗਾ ਹੈ, ਹੁਣ ਮੈਨੂੰ ਪਤਾ ਹੈ ਕਿ ਕੀ ਬਣਾਉਣਾ ਹੈ। ਇਸ ਪੜਾਅ ਤੇ ਕੂਝ ਸੁਧਾਰ ਲੋੜੀਂਦੇ ਹਨ:

- ਅਜਿਹੀ ਸਮੱਗਰੀ ਹਟਾਓ ਜੋ ਮੈਨੂੰ ਪਸੰਦ ਨਹੀਂ ਜਾਂ ਜਿਸ ਨਾਲ ਮੈਂ ਅਲਰਜੀਕ ਹਾਂ।
- ਖਰੀਦਾਰੀ ਦੀ ਸੂਚੀ ਤਿਆਰ ਕਰੋ, ਜੇ ਘਰ ਵਿੱਚ ਸਾਰੀਆਂ ਸਮਗਰੀਆਂ ਨਹੀਂ ਹਨ।

ਇਨ੍ਹਾਂ ਮਾਮਲਿਆਂ ਲਈ ਹੇਠਾਂ ਦਿੱਤਾ ਹੋਰ ਪ੍ਰੰਪਟ ਸ਼ਾਮਲ ਕਰੋ:

> "ਕ੍ਰਿਪਾ ਕਰਕੇ ਉਹ ਰੈਸਿਪੀ ਹਟਾਓ ਜਿਨ੍ਹਾਂ ਵਿੱਚ ਲਸਣ ਹੈ ਕਿਉਂਕਿ ਮੈਨੂੰ ਇਸ ਨਾਲ ਅਲਰਜੀ ਹੈ ਅਤੇ ਇਸਦੀ ਥਾਂ ਕੁਝ ਹੋਰ ਦਿਓ। ਨਾਲ ਹੀ, ਮੈਂ ਚਿਕਨ, ਆਲੂ ਅਤੇ ਗਾਜਰ ਪਹਿਲਾਂ ਹੀ ਘਰ ਵਿੱਚ ਰੱਖਦਾ ਹਾਂ, ਇਸ ਲਈ ਰੈਸਿਪੀ ਲਈ ਖਰੀਦਾਰੀ ਸੂਚੀ ਤਿਆਰ ਕਰੋ।"

ਹੁਣ ਤੁਹਾਡੇ ਕੋਲ ਇਹ ਨਵਾਂ ਨਤੀਜਾ ਹੈ:

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

ਇਹ ਤੁਹਾਡੇ 5 ਰੈਸਿਪੀਆਂ ਹਨ, ਜਿਨ੍ਹਾਂ ਵਿੱਚ ਲਸਣ ਨਹੀਂ ਹੈ ਅਤੇ ਤੁਹਾਡੇ ਕੋਲ ਇੱਕ ਖਰੀਦਾਰੀ ਸੂਚੀ ਵੀ ਹੈ ਜੋ ਉਹਨਾਂ ਸਮੱਗਰੀਆਂ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖਦੀ ਹੈ ਜੋ ਤੁਹਾਡੇ ਘਰ ਵਿੱਚ ਪਹਿਲਾਂ ਹੀ ਹਨ।

## ਅਭਿਆਸ - ਰੈਸਿਪੀ ਜਨਰੇਟਰ ਬਣਾਓ

ਹੁਣ ਜਦੋਂ ਅਸੀਂ ਇਕ ਪ੍ਰਸੰਗ ਖੇਡ ਲਿਆ ਹੈ, ਆਓ ਇਸ ਪ੍ਰਸੰਗ ਅਨੁਸਾਰ ਕੋਡ ਲਿਖੀਏ। ਇਹ ਕਰਨ ਲਈ ਇਹ ਕਦਮ ਅਪਣਾਓ:

1. ਮੌਜੂਦਾ _app.py_ ਫਾਇਲ ਨੂੰ ਸ਼ੁਰੂਆਤੀ ਬਿੰਦੂ ਵਜੋਂ ਵਰਤੋਂ ਕਰੋ
1. `prompt` ਵੈਰੀਏਬਲ ਲੱਭੋ ਅਤੇ ਇਸਦਾ ਕੋਡ ਹੇਠਾਂ ਦਿੱਤੇ ਤਰ੍ਹਾਂ ਬਦਲ ਦਿਓ:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   ਹੁਣ ਜੇ ਤੁਸੀਂ ਕੋਡ ਚਲਾਉਂਦੇ ਹੋ, ਤਾਂ ਤੁਹਾਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਨਤੀਜਾ ਮਿਲੇਗਾ:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > ਧਿਆਨ ਦਿਓ, ਤੁਹਾਡਾ LLM ਨੌਂ-ਡਿਸਟੀਨੇਸਟਿਕ ਹੈ, ਇਸਲਈ ਹਰ ਵਾਰੀ ਪ੍ਰੋਗ੍ਰਾਮ ਚਲਾਉਣ ਤੇ ਵੱਖ-ਵੱਖ ਨਤੀਜੇ ਮਿਲ ਸਕਦੇ ਹਨ।

   ਚਲੋ ਹੁਣ ਵੇਖੀਏ ਕਿ ਅਸੀਂ ਕਿਵੇਂ ਚੀਜ਼ਾਂ ਸੁਧਾਰ ਸਕਦੇ ਹਾਂ। ਸੁਧਾਰ ਕਰਨ ਲਈ, ਅਸੀਂ ਚਾਹੁੰਦੇ ਹਾਂ ਕਿ ਕੋਡ ਲਚੀਲਾ ਹੋਵੇ ਤਾਂ ਜੋ ਸਮੱਗਰੀਆਂ ਅਤੇ ਰੈਸਿਪੀਆਂ ਦੀ ਗਿਣਤੀ ਆਸਾਨੀ ਨਾਲ ਬਦਲੀ ਜਾ ਸਕੇ।

1. ਅਸੀਂ ਕੋਡ ਵਿੱਚ ਇਹ ਤਬਦੀਲੀ ਕਰੀਏ:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   ਇਸ ਕੋਡ ਨੂੰ ਟੈਸਟ ਰਨ ਲਈ ਇਸ ਤਰ੍ਹਾਂ ਲੈ ਸਕਦੇ ਹੋ:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### ਫਿਲਟਰ ਅਤੇ ਖਰੀਦਾਰੀ ਸੂਚੀ ਸ਼ਾਮਲ ਕਰਕੇ ਸੁਧਾਰ

ਹੁਣ ਸਾਡੇ ਕੋਲ ਇੱਕ ਅਜਿਹਾ ਐਪ ਹੈ ਜੋ ਰੈਸਿਪੀਆਂ ਬਣਾਉਂਦਾ ਹੈ ਅਤੇ ਇਹ ਲਚੀਲਾ ਹੈ ਕਿਉਂਕਿ ਇਹ ਯੂਜ਼ਰ ਦੀ ਡਾਟਾ 'ਤੇ ਨਿਰਭਰ ਕਰਦਾ ਹੈ, ਦੋਹਾਂ ਹੀ ਰੈਸਿਪੀਆਂ ਦੀ ਗਿਣਤੀ ਅਤੇ ਵਰਤੀ ਸਮੱਗਰੀ ਉੱਤੇ।

ਇਸਨੂੰ ਹੋਰ ਸੁਧਾਰਣ ਲਈ, ਅਸੀਂ ਹੇਠਾਂ ਦਿੱਤੇ ਕੰਮ ਜੋੜਨਾ ਚਾਹੁੰਦੇ ਹਾਂ:

- **ਸਮੱਗਰੀਆਂ ਨੂੰ ਫਿਲਟਰ ਕਰੋ**। ਅਸੀਂ ਉਹ ਸਮੱਗਰੀਆਂ ਹਟਾਉਣੀ ਚਾਹੁੰਦੇ ਹਾਂ ਜੋ ਸਾਨੂੰ ਪਸੰਦ ਨਹੀਂ ਜਾਂ ਜਿਨ੍ਹਾਂ ਨਾਲ ਅਸੀਂ ਅਲਰਜਿਕ ਹਾਂ। ਇਸ ਲਈ, ਅਸੀਂ ਆਪਣੇ ਮੌਜੂਦਾ ਪ੍ਰੰਪਟ ਨੂੰ ਸੋਧ ਕਰ ਦੇ ਸਕਦੇ ਹਾਂ ਅਤੇ ਇਸਦੇ ਅੰਤ ਵਿੱਚ ਇੱਕ ਫਿਲਟਰ ਸ਼ਰਤ ਸ਼ਾਮਲ ਕਰਦੇ ਹਾਂ ਜਿਵੇਂ:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  ਉੱਪਰ, ਅਸੀਂ ਪ੍ਰੰਪਟ ਦੇ ਆਖ਼ਰ ਵਿੱਚ `{filter}` ਸ਼ਾਮਲ ਕਰਦੇ ਹਾਂ ਅਤੇ ਵਰਤੋਂਕਾਰ ਤੋਂ ਫਿਲਟਰ ਮੁੱਲ ਵੀ ਲੈਂਦੇ ਹਾਂ।

  ਪ੍ਰੋਗ੍ਰਾਮ ਚਲਾਉਣ ਦਾ ਉਦਾਹਰਨ ਇੰਝ ਹੋ ਸਕਦਾ ਹੈ:

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

  ਜਿਵੇਂ ਤੁਸੀਂ ਵੇਖ ਸਕਦੇ ਹੋ, ਦੁੱਧ ਵਾਲੀਆਂ ਰੈਸਿਪੀਆਂ ਹਟਾ ਦਿੱਤੀਆਂ ਗਈਆਂ ਹਨ। ਪਰ ਜੇ ਤੁਸੀਂ ਲੈਕਟੋਜ਼ ਇੰਟੋਲਰੈਂਟ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਪਨੀਰ ਵਾਲੀਆਂ ਰੈਸਿਪੀਆਂ ਵੀ ਹਟਾਉਣਾ ਚਾਹੁਂਦੇ ਹੋ, ਇਸ ਲਈ ਸਪਸ਼ਟ ਹੋਣਾ ਜਰੂਰੀ ਹੈ।

- **ਖਰੀਦਾਰੀ ਸੂਚੀ ਤਿਆਰ ਕਰੋ**। ਅਸੀਂ ਖਰੀਦਾਰੀ ਸੂਚੀ ਬਣਾਉਣੀ ਚਾਹੁੰਦੇ ਹਾਂ ਜਿਸ ਵਿੱਚ ਧਿਆਨ ਹੋਵੇ ਕਿ ਸਾਡੇ ਕੋਲ ਘਰ ਵਿੱਚ ਕੀ ਹੈ।

  ਇਸ ਫੰਕਸ਼ਨਲਿਟੀ ਲਈ, ਅਸੀਂ ਇੱਕੋ ਪ੍ਰੰਪਟ ਵਿੱਚ ਸਭ ਕੁਝ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰ ਸਕਦੇ ਹਾਂ ਜਾਂ ਇਸਨੂੰ ਦੋ ਪ੍ਰੰਪਟਾਂ ਵਿੱਚ ਵੰਡ ਸਕਦੇ ਹਾਂ। ਅਸੀਂ ਦੂਜਾ ਤਰੀਕਾ ਅਪਣਾਉਣਾ ਚਾਹੁੰਦੇ ਹਾਂ। ਇਸ ਕਰਕੇ ਸਾਨੂੰ ਪਹਿਲੇ ਪ੍ਰੰਪਟ ਦੀ ਨਤੀਜੇ ਨੂੰ ਦੂਜੇ ਪ੍ਰੰਪਟ ਦਾ ਸੰਦਰਭ ਬਣਾਉਣਾ ਪਵੇਗਾ।

  ਕੋਡ ਵਿੱਚ ਉਸ ਹਿੱਸੇ ਨੂੰ ਲੱਭੋ ਜੋ ਪਹਿਲੇ ਪ੍ਰੰਪਟ ਤੋਂ ਨਤੀਜਾ ਛਾਪਦਾ ਹੈ ਅਤੇ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਸ਼ਾਮਲ ਕਰੋ:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  ਨੋਟ ਕਰੋ:

  1. ਅਸੀਂ ਨਵਾਂ ਪ੍ਰੰਪਟ ਬਣਾਉਂਦੇ ਹਾੰ ਜੋ ਪਹਿਲੇ ਪ੍ਰੰਪਟ ਦੇ ਨਤੀਜੇ ਨੂੰ ਨਵਾਂ ਪ੍ਰੰਪਟ ਵਿੱਚ ਸ਼ਾਮਲ ਕਰਦਾ ਹੈ:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. ਅਸੀਂ ਨਵੀਂ ਬੇਨਤੀ ਭੇਜਦੇ ਹਾਂ ਅਤੇ ਪਹਿਲੇ ਪ੍ਰੰਪਟ ਲਈ ਮੰਗੇ ਗਏ ਟੋਕਨ ਦੀ ਗਿਣਤੀ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖਦੇ ਹਾਂ, ਇਸ ਵਾਰੀ ਅਸੀਂ ਕਹਿੰਦੇ ਹਾਂ ਕਿ `max_output_tokens` 1200 ਹੈ।

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     ਇਸ ਕੋਡ ਨੂੰ ਚਲਾ ਕੇ ਅਸੀਂ ਹੇਠਾਂ ਦਿੱਤਾ ਨਤੀਜਾ ਪ੍ਰਾਪਤ ਕਰਦੇ ਹਾਂ:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## ਆਪਣਾ ਸੈੱਟਅਪ ਸੁਧਾਰੋ

ਜੋ ਕੁਝ ਅਸੀਂ ਹੁਣ ਤੱਕ ਕੀਤਾ ਹੈ ਉਹ ਕੰਮ ਕਰਨ ਵਾਲਾ ਕੋਡ ਹੈ, ਪਰ ਕੁਝ ਤਰਮੀਮਾਂ ਹੋਣੀਆਂ ਚਾਹੀਦੀਆਂ ਹਨ ਤਾਂ ਜੋ ਚੀਜ਼ਾਂ ਹੋਰ ਵਧੀਆ ਹੋ ਸਕਣ। ਕੁਝ ਗੱਲਾਂ ਜੋ ਸਾਨੂੰ ਕਰਣੀਆਂ ਚਾਹੀਦੀਆਂ ਹਨ ਇਹ ਹਨ:

- **ਕੋਡ ਤੋਂ ਸਿੱਕੜੇ ਅਲੱਗ ਕਰੋ**, ਜਿਵੇਂ ਕਿ API ਕੀ। ਸਿੱਕੜੇ ਕੋਡ ਵਿੱਚ ਨਹੀਂ ਹੋਣੇ ਚਾਹੀਦੇ ਅਤੇ ਉਹਨਾਂ ਨੂੰ ਸੁਰੱਖਿਅਤ ਜਗ੍ਹਾ ਤੇ ਸੰਭਾਲਣ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ। ਸਿੱਕੜਿਆਂ ਨੂੰ ਕੋਡ ਤੋਂ ਅਲੱਗ ਕਰਨ ਲਈ, ਅਸੀਂ ਵਾਤਾਵਰਣ ਵਾਲੀਆਂ ਚਰ (environment variables) ਅਤੇ `python-dotenv` ਵਰਗੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹਾਂ ਜੋ ਉਹਨਾਂ ਨੂੰ ਫਾਈਲ ਤੋਂ ਲੋਡ ਕਰਦੀਆਂ ਹਨ। ਇਹ ਇਸ ਤਰ੍ਹਾਂ ਕੋਡ ਵਿੱਚ ਦਿਖਾਈ ਦੇਵੇਗਾ:

  1. ਇੱਕ `.env` ਫਾਈਲ ਬਣਾਓ ਜਿਸਦਾ ਸਮੱਗਰੀ ਹੇਠਾਂ ਦਿੱਤਾ ਗਿਆ ਹੈ:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > ਨੋਟ ਕਰੋ, Microsoft Foundry ਵਿੱਚ Azure OpenAI ਲਈ, ਤੁਹਾਨੂੰ ਬਦਲੇ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਵਾਤਾਵਰਣ ਵਾਲੀਆਂ ਚਰ ਸੈੱਟ ਕਰਣੀਆਂ ਪੈਣਗੀਆਂ:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     ਕੋਡ ਵਿੱਚ, ਤੁਸੀਂ ਇਸ ਤਰ੍ਹਾਂ ਵਾਤਾਵਰਣ ਵਾਲੀਆਂ ਚਰਾਂ ਲੋਡ ਕਰੋਂਗੇ:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **ਟੋਕਨ ਲੰਬਾਈ ਬਾਰੇ ਇੱਕ ਗੱਲ**। ਸਾਨੂੰ ਇਹ ਸੋਚਣਾ ਚਾਹੀਦਾ ਹੈ ਕਿ ਅਸੀਂ ਲਿਖਤ ਬਣਾਉਣ ਲਈ ਕਿੰਨੇ ਟੋਕਨ ਚਾਹੀਦੇ ਹਨ। ਟੋਕਨ ਲਈ ਪੈਸਾ ਲੱਗਦਾ ਹੈ, ਇਸ ਲਈ ਜਿੱਥੇ ਸਮਭਵ ਹੋਵੇ, ਸਾਨੂੰ ਟੋਕਨਾਂ ਦੀ ਗਿਣਤੀ ਵਿੱਚ ਬਚਤ ਕਰਨੀ ਚਾਹੀਦੀ ਹੈ। ਉਦਾਹਰਨ ਵਜੋਂ, ਕੀ ਅਸੀਂ ਪ੍ਰਾਪਟ ਨੂੰ ਇੰਝ ਬਣਾਉਣ ਦੇਖ ਸਕਦੇ ਹਾਂ ਕਿ ਅਸੀਂ ਘੱਟ ਟੋਕਨ ਵਰਤ ਸਕੀਏ?

  ਟੋਕਨ ਦੀ ਗਿਣਤੀ ਬਦਲਣ ਲਈ, ਤੁਸੀਂ `max_output_tokens` ਪੈਰਾਮੀਟਰ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ। ਉਦਾਹਰਨ ਵਜੋਂ, ਜੇ ਤੁਸੀਂ 100 ਟੋਕਨ ਵਰਤੇ ਜਾਣੇ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਇਹ ਕਰੋਂਗੇ:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **ਤਾਪਮਾਨ ਦੇ ਨਾਲ ਅਨੁਭਵ**। ਤਾਪਮਾਨ ਇੱਕ ਅਜਿਹਾ ਪਰਿਮਾਣ ਹੈ ਜਿਸਦਾ ਅਸੀ ਹੁਣ ਤੱਕ ਜ਼ਿਕਰ ਨਹੀਂ ਕੀਤਾ ਹੈ ਪਰ ਇਹ ਸਾਡੇ ਪ੍ਰੋਗਰਾਮ ਦੀ ਕਾਰਗੁਜ਼ਾਰੀ ਲਈ ਮਹੱਤਵਪੂਰਨ ਸੰਦਰਭ ਹੈ। ਜਿਵੇਂ ਜਿਵੇਂ ਤਾਪਮਾਨ ਦਾ ਮੂਲ ਵੱਧਦਾ ਹੈ, ਨਿਕਾਸ ਹੋਰ ਬੇਤਰਤੀਬ ਹੋਵੇਗਾ। ਉਲਟ, ਜਿਵੇਂ ਜਿਵੇਂ ਤਾਪਮਾਨ ਘੱਟ ਹੁੰਦਾ ਹੈ, ਨਿਕਾਸ ਹੋਰ ਅਨੁਮਾਨਿਆ ਜਾਂਦਾ ਹੈ। ਸੋਚੋ ਕਿ ਤੁਸੀਂ ਆਪਣੇ ਨਿਕਾਸ ਵਿੱਚ ਬਦਲਾਵ ਚਾਹੁੰਦੇ ਹੋ ਜਾਂ ਨਹੀਂ।

  ਤਾਪਮਾਨ ਬਦਲਣ ਲਈ, ਤੁਸੀਂ `temperature` ਪੈਰਾਮੀਟਰ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ। ਉਦਾਹਰਨ ਵਜੋਂ, ਜੇ ਤੁਸੀਂ 0.5 ਦਾ ਤਾਪਮਾਨ ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ ਇਹ ਕਰੋਂਗੇ:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > ਨੋਟ ਕਰੋ, 1.0 ਦੇ ਨੇੜੇ ਹੋਣ ਤੇ ਨਿਕਾਸ ਹੋਰ ਵੱਖਰੇ ਹੋ ਜਾਣਗੇ।

- **ਤਰਕਸ਼ੀਲ ਮਾਡਲ `temperature` ਦੀ ਵਰਤੋਂ ਨਹੀਂ ਕਰਦੇ**। ਇਹ 2026 ਦੀ ਇੱਕ ਮਹੱਤਵਪੂਰਨ ਤਬਦੀਲੀ ਹੈ। Microsoft Foundry ਵਿੱਚ ਮੌਜੂਦਾ, ਅਵਿਕਸਤ ਮਾਡਲ ਹਨ **ਤਰਕਸ਼ੀਲ ਮਾਡਲ** (GPT-5 ਪਰਿਵਾਰ, o-ਸਿਰੀਜ਼) - ਅਤੇ ਉਹ **`temperature` ਜਾਂ `top_p`** (ਅਤੇ ਨਾ ਹੀ `max_tokens`; ਇਸ ਦੀ ਥਾਂ `max_output_tokens` ਵਰਤੋ) ਦਾ ਸਮਰਥਨ ਨਹੀਂ ਕਰਦੇ। ਜੇ ਤੁਸੀਂ `temperature` ਨੂੰ `gpt-5-mini` ਨੂੰ ਭੇਜੋ ਤਾਂ ਤੁਹਾਨੂੰ "parameter not supported" ਗਲਤੀ ਮਿਲੇਗੀ। ਇਸ ਲਈ, ਉੱਪਰ ਦਿੱਤੇ ਗਏ ਤਾਪਮਾਨ ਉਦਾਹਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਨ ਲਈ, ਉਹ ਮਾਡਲ ਚੁਣੋ ਜੋ ਅਜੇ ਵੀ ਸੈਂਪਲਿੰਗ ਕੰਟਰੋਲ ਸਮਰਥਨ ਕਰਦਾ ਹੈ - ਉਦਾਹਰਨ ਲਈ ਖੁੱਲ੍ਹਾ **ਲਾਮਾ** ਮਾਡਲ ਜਿਵੇਂ ਕਿ `Llama-3.3-70B-Instruct`, ਜੋ [Microsoft Foundry ਮਾਡਲ ਕੈਟਾਲਾਗ](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ਵਿੱਚ ਹੈ, ਅਤੇ Foundry Models / Azure AI ਇੰਫਰੰਸ ਐਂਡਪੌਇੰਟ ਤੋਂ ਕਾਲ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ (ਉਹੀ ਤਰ੍ਹਾਂ ਜਿਵੇਂ `githubmodels-*` ਨਮੂਨੇ)। GPT-5 ਵਰਗੇ ਤਰਕਸ਼ੀਲ ਮਾਡਲਾਂ ਲਈ, ਤੁਸੀਂ ਨਿਕਾਸ ਨੂੰ ਵੱਖਰੇ ਢੰਗ ਨਾਲ ਨਿਯੰਤ੍ਰਿਤ ਕਰਦੇ ਹੋ:
  - **ਪ੍ਰਾਂਪਟ ਇੰਜੀਨੀਅਰਿੰਗ** - ਸਾਫ ਹੁਕਮ, ਉਦਾਹਰਨ ਅਤੇ ਸੰਰਚਿਤ ਨਿਕਾਸ (ਦੇਖੋ ਪਾਠ [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) ਉਹ ਕੰਮ ਕਰਦੇ ਹਨ ਜੋ ਸੈਂਪਲਿੰਗ ਕਨਟਰੋਲ ਕਰਦੇ ਸਨ।
  - **ਤਰਕਸ਼ੀਲ ਨਿਯੰਤਰਣ** - ਪਰਮੀਟਰ ਜਿਵੇਂ ਤਰਕਸ਼ੀਲ ਲਗਨ/ਵਿਸਤਾਰ, ਤਰਕਸ਼ੀਲ ਦੀ ਗਹਿਰਾਈ ਨੂੰ ਦਿਰਘਕਾਲ ਅਤੇ ਲਾਗਤ ਦੇ ਖਿਲਾਫ਼ ਤੋਲਦੇ ਹਨ।

  ਸੰਖੇਪ ਵਿੱਚ: `temperature`/`top_p` ਬਹੁਤ ਮਾਡਲਾਂ (Llama, Mistral, Phi, ਅਤੇ GPT-4.x ਪਰਿਵਾਰ - ਹਾਲਾਂਕਿ GPT-4.x ਖਤਮ ਹੋ ਰਿਹਾ ਹੈ) ਤੇ ਅਜੇ ਵੀ ਵੈਧ ਹਨ, ਪਰ ਮਾਰਗ ਵਿੱਚ ਤਰਕਸ਼ੀਲ ਮਾਡਲਾਂ ਜਿਵੇਂ GPT-5 ਲਈ ਯਾਤਰਾ ਪ੍ਰਾਂਪਟ ਇੰਜੀਨੀਅਰਿੰਗ + ਤਰਕਸ਼ੀਲ ਨਿਯੰਤਰਣ ਵੱਲ ਹੈ।

## ਅਸਾਈਨਮੈਂਟ

ਇਸ ਅਸਾਈਨਮੈਂਟ ਲਈ, ਤੁਸੀਂ ਬਣਾ ਸਕਦੇ ਹੋ ਜੋ ਚਾਹੁੰਦੇ ਹੋ।

ਇੱਥੇ ਕੁਝ ਸੁਝਾਅ ਹਨ:

- ਰੇਸਪੀ ਜਨਰੇਟਰ ਐਪ ਨੂੰ ਹੋਰ ਵਧੀਆ ਬਣਾਉਣ ਲਈ ਤਰਮੀਮ ਕਰੋ। ਤਾਪਮਾਨ ਮੁੱਲਾਂ ਦੇ ਨਾਲ ਖੇਡੋ ਅਤੇ ਪ੍ਰਾਂਪਟਸ ਦੇ ਨਾਲ ਦੇਖੋ ਕਿ ਤੁਸੀਂ ਕੀ ਕੁਝ ਬਣਾ ਸਕਦੇ ਹੋ।
- ਇੱਕ "ਸਟੱਡੀ ਬਡੀ" ਬਣਾਓ। ਇਹ ਐਪ ਕਿਸੇ ਵਿਸ਼ੇ ਦੀਆਂ ਸਵਾਲਾਂ ਦੇ ਜਵਾਬ ਦੇ ਸਕਣੀ ਚਾਹੀਦੀ ਹੈ, ਉਦਾਹਰਨ ਵਜੋਂ Python; ਤੁਸੀਂ ਪ੍ਰਾਂਪਟਸ ਜਿਵੇਂ "Python ਵਿੱਚ ਕੁਝ ਵਿਸ਼ਾ ਕੀ ਹੈ?", ਜਾਂ ਤਾਂ ਤੁਸੀਂ ਪ੍ਰਾਂਪਟ ਦੇ ਸਕਦੇ ਹੋ ਕਿ ਕਿਸੇ ਵਿਸ਼ੇ ਲਈ ਕੋਡ ਦਿਖਾਓ ਆਦਿ।
- ਇਤਿਹਾਸ ਬੋਟ, ਇਤਿਹਾਸ ਨੂੰ ਜੀਵੰਤ ਬਣਾਓ, ਬੋਟ ਨੂੰ ਕੋਈ ਵਿਸ਼ੇਸ਼ ਇਤਿਹਾਸਕ ਪਾਤਰ ਖੇਡਣ ਲਈ ਕਹੋ ਅਤੇ ਉਸਦੀ ਜ਼ਿੰਦਗੀ ਅਤੇ ਸਮਿਆਂ ਬਾਰੇ ਸਵਾਲ ਪੁੱਛੋ।

## ਹੱਲ

### ਸਟੱਡੀ ਬਡੀ

ਹੇਠਾਂ ਇੱਕ ਸ਼ੁਰੂਆਤੀ ਪ੍ਰਾਂਪਟ ਹੈ, ਦੇਖੋ ਤੁਸੀਂ ਇਸ ਨੂੰ ਕਿਵੇਂ ਵਰਤ ਸਕਦੇ ਹੋ ਅਤੇ ਆਪਣੇ ਮਨਮੁਤਾਬਕ ਤਬਦੀਲ ਕਰ ਸਕਦੇ ਹੋ।

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

## ਗਿਆਨ ਪਰਖ

ਤਾਪਮਾਨ ਦੀ ਸੰਕਲਪਨਾ ਕੀ ਕੰਮ ਕਰਦੀ ਹੈ?

1. ਇਹ ਨਿਕਾਸ ਕਿੰਨਾ ਬੇਤਰਤੀਬ ਹੈ ਇਸ ਨੂੰ ਨਿਯੰਤ੍ਰਿਤ ਕਰਦਾ ਹੈ।
1. ਇਹ ਜਵਾਬ कितना ਵੱਡਾ ਹੈ ਇਸ ਨੂੰ ਨਿਯੰਤ੍ਰਿਤ ਕਰਦਾ ਹੈ।
1. ਇਹ ਕਿੰਨੇ ਟੋਕਨ ਵਰਤੇ ਜਾਂਦੇ ਹਨ ਇਸ ਨੂੰ ਨਿਯੰਤ੍ਰਿਤ ਕਰਦਾ ਹੈ।

## 🚀 ਚੈਲੰਜ

ਅਸਾਈਨਮੈਂਟ 'ਤੇ ਕੰਮ ਕਰਦਿਆਂ, ਤਾਪਮਾਨ ਨੂੰ ਵੱਖ-ਵੱਖ ਮੁੱਲਾਂ ਅਤੇ ਦੀਆਂਕ 0, 0.5, ਅਤੇ 1 ਕਰਕੇ ਦੇਖੋ। ਯਾਦ ਰੱਖੋ ਕਿ 0 ਸਭ ਤੋਂ ਘੱਟ ਵੱਖਰੇ ਨਿਕਾਸ ਅਤੇ 1 ਸਭ ਤੋਂ ਵੱਧ ਵੱਖਰਾ ਨਿਕਾਸ ਦੇਂਦਾ ਹੈ। ਤੁਹਾਡੇ ਐਪ ਲਈ ਸਭ ਤੋਂ ਵਧੀਆ ਮੁੱਲ ਕਿਹੜਾ ਹੈ?

## ਵਧੀਆ ਕੰਮ! ਆਪਣੀ ਸਿੱਖਿਆ ਜਾਰੀ ਰੱਖੋ

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਸਾਡੇ [Generative AI ਸਿੱਖਣ ਦੀ ਸੰਗ੍ਰਹਿ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ਨੂੰ ਵੇਖੋ ਤਾਂ ਜੋ ਤੁਸੀਂ ਆਪਣਾ Generative AI ਗਿਆਨ ਹੋਰ ਵਧਾ ਸਕੋ!

ਪਾਠ 7 'ਤੇ ਜਾਓ ਜਿੱਥੇ ਅਸੀਂ ਦੇਖਾਂਗੇ ਕਿ ਕਿਵੇਂ [ਚੈਟ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਏ](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->