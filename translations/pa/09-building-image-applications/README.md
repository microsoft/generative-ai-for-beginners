<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "063a2ac57d6b71bea0eaa880c68770d2",
  "translation_date": "2025-09-29T21:39:21+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "pa"
}
-->
# ਚਿੱਤਰ ਜਨਰੇਸ਼ਨ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣਾ

[![ਚਿੱਤਰ ਜਨਰੇਸ਼ਨ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣਾ](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.pa.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLMs ਸਿਰਫ਼ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਤੱਕ ਹੀ ਸੀਮਿਤ ਨਹੀਂ ਹਨ। ਇਹ ਟੈਕਸਟ ਵਰਣਨ ਤੋਂ ਚਿੱਤਰ ਬਣਾਉਣ ਦੇ ਯੋਗ ਵੀ ਹਨ। ਚਿੱਤਰਾਂ ਨੂੰ ਇੱਕ ਮੋਡੈਲਿਟੀ ਵਜੋਂ ਵਰਤਣਾ ਕਈ ਖੇਤਰਾਂ ਵਿੱਚ ਬਹੁਤ ਹੀ ਲਾਭਦਾਇਕ ਹੋ ਸਕਦਾ ਹੈ ਜਿਵੇਂ ਕਿ ਮੈਡਟੈਕ, ਆਰਕੀਟੈਕਚਰ, ਟੂਰਿਜ਼ਮ, ਗੇਮ ਡਿਵੈਲਪਮੈਂਟ ਅਤੇ ਹੋਰ। ਇਸ ਅਧਿਆਇ ਵਿੱਚ, ਅਸੀਂ ਦੋ ਸਭ ਤੋਂ ਪ੍ਰਸਿੱਧ ਚਿੱਤਰ ਜਨਰੇਸ਼ਨ ਮਾਡਲਾਂ, DALL-E ਅਤੇ Midjourney, ਬਾਰੇ ਜਾਣਕਾਰੀ ਲਵਾਂਗੇ।

## ਪਰਿਚਯ

ਇਸ ਪਾਠ ਵਿੱਚ, ਅਸੀਂ ਕਵਰ ਕਰਾਂਗੇ:

- ਚਿੱਤਰ ਜਨਰੇਸ਼ਨ ਅਤੇ ਇਹ ਕਿਉਂ ਲਾਭਦਾਇਕ ਹੈ।
- DALL-E ਅਤੇ Midjourney, ਇਹ ਕੀ ਹਨ ਅਤੇ ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦੇ ਹਨ।
- ਤੁਸੀਂ ਚਿੱਤਰ ਜਨਰੇਸ਼ਨ ਐਪਲੀਕੇਸ਼ਨ ਕਿਵੇਂ ਬਣਾਉਂਦੇ ਹੋ।

## ਸਿੱਖਣ ਦੇ ਲਕਸ਼

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਇਹ ਕਰਨ ਦੇ ਯੋਗ ਹੋਵੋਗੇ:

- ਚਿੱਤਰ ਜਨਰੇਸ਼ਨ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣਾ।
- ਆਪਣੇ ਐਪਲੀਕੇਸ਼ਨ ਲਈ ਮੈਟਾ ਪ੍ਰੌੰਪਟਸ ਨਾਲ ਸੀਮਾਵਾਂ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨਾ।
- DALL-E ਅਤੇ Midjourney ਨਾਲ ਕੰਮ ਕਰਨਾ।

## ਚਿੱਤਰ ਜਨਰੇਸ਼ਨ ਐਪਲੀਕੇਸ਼ਨ ਕਿਉਂ ਬਣਾਈਏ?

ਚਿੱਤਰ ਜਨਰੇਸ਼ਨ ਐਪਲੀਕੇਸ਼ਨ ਜਨਰੇਟਿਵ AI ਦੀਆਂ ਸਮਰੱਥਾਵਾਂ ਦੀ ਪੜਚੋਲ ਕਰਨ ਦਾ ਇੱਕ ਸ਼ਾਨਦਾਰ ਤਰੀਕਾ ਹੈ। ਇਹ ਕਈ ਉਦਾਹਰਣਾਂ ਲਈ ਵਰਤੀਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ:

- **ਚਿੱਤਰ ਸੰਪਾਦਨ ਅਤੇ ਸਿੰਥੇਸਿਸ**। ਤੁਸੀਂ ਚਿੱਤਰ ਸੰਪਾਦਨ ਅਤੇ ਚਿੱਤਰ ਸਿੰਥੇਸਿਸ ਵਰਗੇ ਕਈ ਉਪਯੋਗਾਂ ਲਈ ਚਿੱਤਰ ਬਣਾਉਣ ਲਈ ਵਰਤ ਸਕਦੇ ਹੋ।

- **ਕਈ ਉਦਯੋਗਾਂ ਵਿੱਚ ਲਾਗੂ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ**। ਇਹ ਮੈਡਟੈਕ, ਟੂਰਿਜ਼ਮ, ਗੇਮ ਡਿਵੈਲਪਮੈਂਟ ਅਤੇ ਹੋਰ ਵਰਗੇ ਕਈ ਉਦਯੋਗਾਂ ਲਈ ਚਿੱਤਰ ਬਣਾਉਣ ਲਈ ਵੀ ਵਰਤੇ ਜਾ ਸਕਦੇ ਹਨ।

## ਸਥਿਤੀ: Edu4All

ਇਸ ਪਾਠ ਦੇ ਹਿੱਸੇ ਵਜੋਂ, ਅਸੀਂ ਆਪਣੇ ਸਟਾਰਟਅਪ, Edu4All, ਨਾਲ ਕੰਮ ਜਾਰੀ ਰੱਖਾਂਗੇ। ਵਿਦਿਆਰਥੀ ਆਪਣੇ ਅਸੈਸਮੈਂਟ ਲਈ ਚਿੱਤਰ ਬਣਾਉਣਗੇ, ਕਿਹੜੇ ਚਿੱਤਰ ਬਣਾਉਣੇ ਹਨ ਇਹ ਵਿਦਿਆਰਥੀਆਂ ਉੱਤੇ ਹੈ, ਪਰ ਉਹ ਆਪਣੇ ਪਰੀਆਂ ਦੀ ਕਹਾਣੀ ਲਈ ਚਿੱਤਰ ਬਣਾਉਣ ਜਾਂ ਆਪਣੇ ਵਿਚਾਰਾਂ ਅਤੇ ਧਾਰਨਾਵਾਂ ਨੂੰ ਦ੍ਰਿਸ਼ਮਾਨ ਕਰਨ ਲਈ ਨਵੇਂ ਪਾਤਰ ਬਣਾਉਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰ ਸਕਦੇ ਹਨ।

ਇਹ ਹੈ ਜੋ Edu4All ਦੇ ਵਿਦਿਆਰਥੀ ਜਨਰੇਟ ਕਰ ਸਕਦੇ ਹਨ ਜੇ ਉਹ ਕਲਾਸ ਵਿੱਚ ਸਮਾਰਕਾਂ 'ਤੇ ਕੰਮ ਕਰ ਰਹੇ ਹਨ:

![Edu4All ਸਟਾਰਟਅਪ, ਕਲਾਸ ਸਮਾਰਕਾਂ 'ਤੇ, Eiffel Tower](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.pa.png)

ਇੱਕ ਪ੍ਰੌੰਪਟ ਵਰਤ ਕੇ

> "ਸਵੇਰੇ ਦੀ ਧੁੱਪ ਵਿੱਚ Eiffel Tower ਦੇ ਕੋਲ ਕੁੱਤਾ"

## DALL-E ਅਤੇ Midjourney ਕੀ ਹਨ?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) ਅਤੇ [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) ਦੋ ਸਭ ਤੋਂ ਪ੍ਰਸਿੱਧ ਚਿੱਤਰ ਜਨਰੇਸ਼ਨ ਮਾਡਲ ਹਨ, ਇਹ ਤੁਹਾਨੂੰ ਪ੍ਰੌੰਪਟਸ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਚਿੱਤਰ ਬਣਾਉਣ ਦੀ ਆਗਿਆ ਦਿੰਦੇ ਹਨ।

### DALL-E

ਚਲੋ DALL-E ਨਾਲ ਸ਼ੁਰੂ ਕਰੀਏ, ਜੋ ਕਿ ਇੱਕ ਜਨਰੇਟਿਵ AI ਮਾਡਲ ਹੈ ਜੋ ਟੈਕਸਟ ਵਰਣਨ ਤੋਂ ਚਿੱਤਰ ਬਣਾਉਂਦਾ ਹੈ।

> [DALL-E ਦੋ ਮਾਡਲਾਂ, CLIP ਅਤੇ diffused attention, ਦਾ ਸੰਯੋਗ ਹੈ](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)।

- **CLIP**, ਇੱਕ ਮਾਡਲ ਹੈ ਜੋ ਚਿੱਤਰਾਂ ਅਤੇ ਟੈਕਸਟ ਤੋਂ ਐਮਬੈਡਿੰਗਜ਼ ਬਣਾਉਂਦਾ ਹੈ, ਜੋ ਡਾਟਾ ਦੇ ਸੰਖਿਆਤਮਕ ਪ੍ਰਤੀਨਿਧਾਨ ਹਨ।

- **Diffused attention**, ਇੱਕ ਮਾਡਲ ਹੈ ਜੋ ਐਮਬੈਡਿੰਗਜ਼ ਤੋਂ ਚਿੱਤਰ ਬਣਾਉਂਦਾ ਹੈ। DALL-E ਨੂੰ ਚਿੱਤਰਾਂ ਅਤੇ ਟੈਕਸਟ ਦੇ ਡਾਟਾਸੈਟ 'ਤੇ ਟ੍ਰੇਨ ਕੀਤਾ ਗਿਆ ਹੈ ਅਤੇ ਇਸਨੂੰ ਟੈਕਸਟ ਵਰਣਨ ਤੋਂ ਚਿੱਤਰ ਬਣਾਉਣ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਉਦਾਹਰਣ ਲਈ, DALL-E ਨੂੰ ਇੱਕ ਟੋਪੀ ਵਿੱਚ ਬਿੱਲੀ ਜਾਂ ਮੋਹਾਕ ਵਾਲੇ ਕੁੱਤੇ ਦੇ ਚਿੱਤਰ ਬਣਾਉਣ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ।

### Midjourney

Midjourney DALL-E ਦੇ ਸਮਾਨ ਹੀ ਕੰਮ ਕਰਦਾ ਹੈ, ਇਹ ਟੈਕਸਟ ਪ੍ਰੌੰਪਟਸ ਤੋਂ ਚਿੱਤਰ ਬਣਾਉਂਦਾ ਹੈ। Midjourney ਨੂੰ "ਟੋਪੀ ਵਿੱਚ ਬਿੱਲੀ" ਜਾਂ "ਮੋਹਾਕ ਵਾਲੇ ਕੁੱਤੇ" ਵਰਗੇ ਪ੍ਰੌੰਪਟਸ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਚਿੱਤਰ ਬਣਾਉਣ ਲਈ ਵੀ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ।

![Midjourney ਦੁਆਰਾ ਜਨਰੇਟ ਕੀਤਾ ਚਿੱਤਰ, ਮਕੈਨਿਕਲ ਕਬੂਤਰ](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_ਚਿੱਤਰ ਕ੍ਰੈਡਿਟ: ਵਿਕੀਪੀਡੀਆ, Midjourney ਦੁਆਰਾ ਜਨਰੇਟ ਕੀਤਾ ਚਿੱਤਰ_

## DALL-E ਅਤੇ Midjourney ਕਿਵੇਂ ਕੰਮ ਕਰਦੇ ਹਨ

ਸਭ ਤੋਂ ਪਹਿਲਾਂ, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)। DALL-E ਇੱਕ ਜਨਰੇਟਿਵ AI ਮਾਡਲ ਹੈ ਜੋ ਟ੍ਰਾਂਸਫਾਰਮਰ ਆਰਕੀਟੈਕਚਰ 'ਤੇ ਅਧਾਰਿਤ ਹੈ ਜਿਸ ਵਿੱਚ ਇੱਕ _autoregressive transformer_ ਹੈ।

ਇੱਕ _autoregressive transformer_ ਇਹ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ ਕਿ ਮਾਡਲ ਟੈਕਸਟ ਵਰਣਨ ਤੋਂ ਚਿੱਤਰ ਕਿਵੇਂ ਬਣਾਉਂਦਾ ਹੈ। ਇਹ ਇੱਕ ਸਮੇਂ ਵਿੱਚ ਇੱਕ ਪਿਕਸਲ ਜਨਰੇਟ ਕਰਦਾ ਹੈ ਅਤੇ ਫਿਰ ਜਨਰੇਟ ਕੀਤੇ ਪਿਕਸਲਾਂ ਨੂੰ ਅਗਲੇ ਪਿਕਸਲ ਨੂੰ ਜਨਰੇਟ ਕਰਨ ਲਈ ਵਰਤਦਾ ਹੈ। ਨਿਊਰਲ ਨੈਟਵਰਕ ਵਿੱਚ ਕਈ ਲੇਅਰਾਂ ਤੋਂ ਗੁਜ਼ਰਦੇ ਹੋਏ, ਜਦੋਂ ਤੱਕ ਚਿੱਤਰ ਪੂਰਾ ਨਹੀਂ ਹੋ ਜਾਂਦਾ।

ਇਸ ਪ੍ਰਕਿਰਿਆ ਨਾਲ, DALL-E, ਚਿੱਤਰ ਵਿੱਚ ਜਨਰੇਟ ਕੀਤੇ ਗੁਣਾਂ, ਵਸਤੂਆਂ, ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਅਤੇ ਹੋਰ ਨੂੰ ਨਿਯੰਤਰਿਤ ਕਰਦਾ ਹੈ। ਹਾਲਾਂਕਿ, DALL-E 2 ਅਤੇ 3 ਜਨਰੇਟ ਕੀਤੇ ਚਿੱਤਰ 'ਤੇ ਹੋਰ ਵੱਧ ਨਿਯੰਤਰਣ ਰੱਖਦੇ ਹਨ।

## ਆਪਣੀ ਪਹਿਲੀ ਚਿੱਤਰ ਜਨਰੇਸ਼ਨ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣਾ

ਤਾਂ ਚਿੱਤਰ ਜਨਰੇਸ਼ਨ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ ਲਈ ਤੁਹਾਨੂੰ ਕੀ ਚਾਹੀਦਾ ਹੈ? ਤੁਹਾਨੂੰ ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਦੀ ਲੋੜ ਹੈ:

- **python-dotenv**, ਇਹ ਲਾਇਬ੍ਰੇਰੀ ਤੁਹਾਡੇ ਰਾਜ਼ਾਂ ਨੂੰ _.env_ ਫਾਈਲ ਵਿੱਚ ਕੋਡ ਤੋਂ ਦੂਰ ਰੱਖਣ ਲਈ ਬਹੁਤ ਹੀ ਸਿਫਾਰਸ਼ੀ ਹੈ।
- **openai**, ਇਹ ਲਾਇਬ੍ਰੇਰੀ OpenAI API ਨਾਲ ਸੰਚਾਰ ਕਰਨ ਲਈ ਵਰਤੀ ਜਾਂਦੀ ਹੈ।
- **pillow**, ਪਾਈਥਨ ਵਿੱਚ ਚਿੱਤਰਾਂ ਨਾਲ ਕੰਮ ਕਰਨ ਲਈ।
- **requests**, HTTP ਰਿਕਵੈਸਟ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਨ ਲਈ।

## Azure OpenAI ਮਾਡਲ ਬਣਾਓ ਅਤੇ ਡਿਪਲੌਇ ਕਰੋ

ਜੇਕਰ ਪਹਿਲਾਂ ਨਹੀਂ ਕੀਤਾ, ਤਾਂ [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) ਪੇਜ 'ਤੇ ਦਿੱਤੀਆਂ ਹਦਾਇਤਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ
Azure OpenAI ਸਰੋਤ ਅਤੇ ਮਾਡਲ ਬਣਾਉਣ ਲਈ। ਮਾਡਲ ਵਜੋਂ DALL-E 3 ਚੁਣੋ।  

## ਐਪ ਬਣਾਓ

1. _.env_ ਫਾਈਲ ਬਣਾਓ ਜਿਸ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਸਮੱਗਰੀ ਹੋਵੇ:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   ਇਹ ਜਾਣਕਾਰੀ Azure OpenAI Foundry Portal ਵਿੱਚ ਆਪਣੇ ਸਰੋਤ ਦੇ "Deployments" ਸੈਕਸ਼ਨ ਵਿੱਚ ਲੱਭੋ।

1. ਉਪਰੋਕਤ ਲਾਇਬ੍ਰੇਰੀਆਂ ਨੂੰ _requirements.txt_ ਫਾਈਲ ਵਿੱਚ ਇਕੱਠਾ ਕਰੋ ਇਸ ਤਰ੍ਹਾਂ:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. ਅਗਲੇ ਕਦਮ ਵਿੱਚ, ਵਰਚੁਅਲ ਐਨਵਾਇਰਨਮੈਂਟ ਬਣਾਓ ਅਤੇ ਲਾਇਬ੍ਰੇਰੀਆਂ ਇੰਸਟਾਲ ਕਰੋ:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows ਲਈ, ਵਰਚੁਅਲ ਐਨਵਾਇਰਨਮੈਂਟ ਬਣਾਉਣ ਅਤੇ ਐਕਟੀਵੇਟ ਕਰਨ ਲਈ ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡ ਵਰਤੋ:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ ਨਾਮਕ ਫਾਈਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤਾ ਕੋਡ ਸ਼ਾਮਲ ਕਰੋ:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # import dotenv
    dotenv.load_dotenv()
    
    # configure Azure OpenAI service client 
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
    try:
        # Create an image by using the image generation API
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # Set the directory for the stored image
        image_dir = os.path.join(os.curdir, 'images')

        # If the directory doesn't exist, create it
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Initialize the image path (note the filetype should be png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Retrieve the generated image
        image_url = generation_response.data[0].url  # extract image URL from response
        generated_image = requests.get(image_url).content  # download the image
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # Display the image in the default image viewer
        image = Image.open(image_path)
        image.show()

    # catch exceptions
    except openai.InvalidRequestError as err:
        print(err)
   ```

ਇਸ ਕੋਡ ਨੂੰ ਸਮਝਦੇ ਹਾਂ:

- ਸਭ ਤੋਂ ਪਹਿਲਾਂ, ਅਸੀਂ ਲੋੜੀਂਦੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਨੂੰ ਇੰਪੋਰਟ ਕਰਦੇ ਹਾਂ, ਜਿਵੇਂ ਕਿ OpenAI ਲਾਇਬ੍ਰੇਰੀ, dotenv ਲਾਇਬ੍ਰੇਰੀ, requests ਲਾਇਬ੍ਰੇਰੀ, ਅਤੇ Pillow ਲਾਇਬ੍ਰੇਰੀ।

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- ਅਗਲੇ ਕਦਮ ਵਿੱਚ, ਅਸੀਂ _.env_ ਫਾਈਲ ਤੋਂ ਵਾਤਾਵਰਣ ਚਰਾਂ ਨੂੰ ਲੋਡ ਕਰਦੇ ਹਾਂ।

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- ਇਸ ਤੋਂ ਬਾਅਦ, ਅਸੀਂ Azure OpenAI ਸੇਵਾ ਕਲਾਇੰਟ ਨੂੰ ਸੰਰਚਿਤ ਕਰਦੇ ਹਾਂ।

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- ਅਗਲੇ ਕਦਮ ਵਿੱਚ, ਅਸੀਂ ਚਿੱਤਰ ਜਨਰੇਟ ਕਰਦੇ ਹਾਂ:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  ਉਪਰੋਕਤ ਕੋਡ JSON ਆਬਜੈਕਟ ਨਾਲ ਜਵਾਬ ਦਿੰਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਜਨਰੇਟ ਕੀਤੇ ਚਿੱਤਰ ਦਾ URL ਹੁੰਦਾ ਹੈ। ਅਸੀਂ URL ਨੂੰ ਵਰਤ ਕੇ ਚਿੱਤਰ ਡਾਊਨਲੋਡ ਕਰ ਸਕਦੇ ਹਾਂ ਅਤੇ ਇਸਨੂੰ ਫਾਈਲ ਵਿੱਚ ਸੇਵ ਕਰ ਸਕਦੇ ਹਾਂ।

- ਆਖਰੀ ਵਿੱਚ, ਅਸੀਂ ਚਿੱਤਰ ਨੂੰ ਖੋਲ੍ਹਦੇ ਹਾਂ ਅਤੇ ਮਿਆਰੀ ਚਿੱਤਰ ਦਰਸ਼ਕ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਸਨੂੰ ਦਿਖਾਉਂਦੇ ਹਾਂ:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### ਚਿੱਤਰ ਜਨਰੇਸ਼ਨ 'ਤੇ ਹੋਰ ਵੇਰਵੇ

ਆਓ ਉਸ ਕੋਡ ਨੂੰ ਵੇਖੀਏ ਜੋ ਚਿੱਤਰ ਜਨਰੇਟ ਕਰਦਾ ਹੈ:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, ਉਹ ਟੈਕਸਟ ਪ੍ਰੌੰਪਟ ਹੈ ਜੋ ਚਿੱਤਰ ਜਨਰੇਟ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ। ਇਸ ਮਾਮਲੇ ਵਿੱਚ, ਅਸੀਂ "ਘੋੜੇ 'ਤੇ ਖਰਗੋਸ਼, ਲੌਲੀਪੌਪ ਫੜ੍ਹਦਾ ਹੋਇਆ, ਧੁੰਦਲੇ ਮੈਦਾਨ 'ਤੇ ਜਿੱਥੇ ਡੈਫੋਡਿਲਸ ਉੱਗਦੇ ਹਨ" ਵਰਤ ਰਹੇ ਹਾਂ।
- **size**, ਜਨਰੇਟ ਕੀਤੇ ਚਿੱਤਰ ਦਾ ਆਕਾਰ ਹੈ। ਇਸ ਮਾਮਲੇ ਵਿੱਚ, ਅਸੀਂ 1024x1024 ਪਿਕਸਲ ਦਾ ਚਿੱਤਰ ਜਨਰੇਟ ਕਰ ਰਹੇ ਹਾਂ।
- **n**, ਜਨਰੇਟ ਕੀਤੇ ਚਿੱਤਰਾਂ ਦੀ ਗਿਣਤੀ ਹੈ। ਇਸ ਮਾਮਲੇ ਵਿੱਚ, ਅਸੀਂ ਦੋ ਚਿੱਤਰ ਜਨਰੇਟ ਕਰ ਰਹੇ ਹਾਂ।
- **temperature**, ਇੱਕ ਪੈਰਾਮੀਟਰ ਹੈ ਜੋ ਜਨਰੇਟਿਵ AI ਮਾਡਲ ਦੇ ਆਉਟਪੁੱਟ ਦੀ ਰੈਂਡਮਨੈਸ ਨੂੰ ਨਿਯੰਤਰਿਤ ਕਰਦਾ ਹੈ। ਤਾਪਮਾਨ 0 ਅਤੇ 1 ਦੇ ਵਿਚਕਾਰ ਇੱਕ ਮੁੱਲ ਹੈ ਜਿੱਥੇ 0 ਦਾ ਮਤਲਬ ਹੈ ਕਿ ਆਉਟਪੁੱਟ ਨਿਰਧਾਰਤ ਹੈ ਅਤੇ 1 ਦਾ ਮਤਲਬ ਹੈ ਕਿ ਆਉਟਪੁੱਟ ਰੈਂਡਮ ਹੈ। ਡਿਫਾਲਟ ਮੁੱਲ 0.7 ਹੈ।

ਚਿੱਤਰਾਂ ਨਾਲ ਹੋਰ ਵੀ ਕਈ ਕੰਮ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ ਜੋ ਅਸੀਂ ਅਗਲੇ ਸੈਕਸ਼ਨ ਵਿੱਚ ਕਵਰ ਕਰਾਂਗੇ।

## ਚਿੱਤਰ ਜਨਰੇਸ਼ਨ ਦੀਆਂ ਵਾਧੂ ਸਮਰੱਥਾਵਾਂ

ਤੁਸੀਂ ਹੁਣ ਤੱਕ ਦੇਖਿਆ ਕਿ ਅਸੀਂ ਪਾਈਥਨ ਵਿੱਚ ਕੁਝ ਲਾਈਨਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਚਿੱਤਰ ਜਨਰੇਟ ਕਰਨ ਦੇ ਯੋਗ ਹੋਏ। ਹਾਲਾਂਕਿ, ਚਿੱਤਰਾਂ ਨਾਲ ਹੋਰ ਵੀ ਕਈ ਕੰਮ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ।

ਤੁਸੀਂ ਇਹ ਵੀ ਕਰ ਸਕਦੇ ਹੋ:

- **ਸੰਪਾਦਨ ਕਰੋ**। ਮੌਜੂਦਾ ਚਿੱਤਰ, ਇੱਕ ਮਾਸਕ ਅਤੇ ਇੱਕ ਪ੍ਰੌੰਪਟ ਪ੍ਰਦਾਨ ਕਰਕੇ, ਤੁਸੀਂ ਚਿੱਤਰ ਨੂੰ ਬਦਲ ਸਕਦੇ ਹੋ। ਉਦਾਹਰਣ ਲਈ, ਤੁਸੀਂ ਚਿੱਤਰ ਦੇ ਕਿਸੇ ਹਿੱਸੇ ਵਿੱਚ ਕੁਝ ਸ਼ਾਮਲ ਕਰ ਸਕਦੇ ਹੋ। ਕਲਪਨਾ ਕਰੋ ਸਾਡੇ ਖਰਗੋਸ਼ ਦੇ ਚਿੱਤਰ ਨੂੰ, ਤੁਸੀਂ ਖਰਗੋਸ਼ ਨੂੰ ਇੱਕ ਟੋਪੀ ਸ਼ਾਮਲ ਕਰ ਸਕਦੇ ਹੋ। ਤੁਸੀਂ ਇਹ ਕਿਵੇਂ ਕਰਦੇ ਹੋ ਇਹ ਚਿੱਤਰ, ਇੱਕ ਮਾਸਕ (ਬਦਲਾਅ ਲਈ ਖੇਤਰ ਦੀ ਪਛਾਣ ਕਰਦੇ ਹੋਏ) ਅਤੇ ਇੱਕ ਟੈਕਸਟ ਪ੍ਰੌੰਪਟ ਪ੍ਰਦਾਨ ਕਰਕੇ ਹੈ। 
> ਨੋਟ: ਇਹ DALL-E 3 ਵਿੱਚ ਸਮਰਥਿਤ ਨਹੀਂ ਹੈ। 
 
ਇਹ GPT ਚਿੱਤਰ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ ਇੱਕ ਉਦਾਹਰਣ ਹੈ:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  ਬੇਸ ਚਿੱਤਰ ਵਿੱਚ ਸਿਰਫ਼ ਪੂਲ ਵਾਲਾ ਲਾਊਂਜ ਹੋਵੇਗਾ ਪਰ ਅੰਤਿਮ ਚਿੱਤਰ ਵਿੱਚ ਇੱਕ ਫਲਮਿੰਗੋ ਹੋਵੇਗਾ:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.pa.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.pa.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.pa.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **ਵੈਰੀਏਸ਼ਨ ਬਣਾਓ**। ਵਿਚਾਰ ਇਹ ਹੈ ਕਿ ਤੁਸੀਂ ਮੌਜੂਦਾ ਚਿੱਤਰ ਲੈਂਦੇ ਹੋ ਅਤੇ ਮੰਗਦੇ ਹੋ ਕਿ ਵੈਰੀਏਸ਼ਨ ਬਣਾਈਆਂ ਜਾਣ। ਵੈਰੀਏਸ਼ਨ ਬਣਾਉਣ ਲਈ, ਤੁਸੀਂ ਇੱਕ ਚਿੱਤਰ ਅਤੇ ਇੱਕ ਟੈਕਸਟ ਪ੍ਰੌੰਪਟ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹੋ ਅਤੇ ਇਸ ਤਰ੍ਹਾਂ ਕੋਡ ਕਰਦੇ ਹੋ:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > ਨੋਟ, ਇਹ ਸਿਰਫ਼ OpenAI 'ਤੇ ਸਮਰਥਿਤ ਹੈ।

## ਤਾਪਮਾਨ

ਤਾਪਮਾਨ ਇੱਕ ਪੈਰਾਮੀਟਰ ਹੈ ਜੋ ਜਨਰੇਟਿਵ AI ਮਾਡਲ ਦੇ ਆਉਟਪੁੱਟ ਦੀ ਰੈਂਡਮਨੈਸ ਨੂੰ ਨਿਯੰਤਰਿਤ ਕਰਦਾ ਹੈ। ਤਾਪਮਾਨ 0 ਅਤੇ 1 ਦੇ ਵਿਚਕਾਰ ਇੱਕ ਮੁੱਲ ਹੈ ਜਿੱਥੇ 0 ਦਾ ਮਤਲਬ ਹੈ ਕਿ ਆਉਟਪੁੱਟ ਨਿਰਧਾਰਤ ਹੈ ਅਤੇ 1 ਦਾ ਮਤਲਬ ਹੈ ਕਿ ਆਉਟਪੁੱਟ ਰੈਂਡਮ ਹੈ। ਡਿਫਾਲਟ ਮੁੱਲ 0.7 ਹੈ।

ਆਓ ਇੱਕ ਉਦਾਹਰਣ ਦੇਖੀਏ ਕਿ ਤਾਪਮਾਨ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ, ਇਸ ਪ੍ਰੌੰਪਟ ਨੂੰ ਦੋ ਵਾਰ ਚਲਾਉਣ ਦੁਆਰਾ:

> ਪ੍ਰੌੰਪਟ : "ਘੋੜੇ 'ਤੇ ਖਰਗੋਸ਼, ਲੌਲੀਪੌਪ ਫੜ੍ਹਦਾ ਹੋਇਆ, ਧੁੰਦਲੇ ਮੈਦਾਨ 'ਤੇ ਜਿੱਥੇ ਡੈਫੋਡਿਲਸ ਉੱਗਦੇ ਹਨ"

![ਘੋੜੇ 'ਤੇ ਖਰਗੋਸ਼, ਲੌਲੀਪੌਪ ਫੜ੍ਹਦਾ ਹੋਇਆ, ਵਰਜਨ 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.pa.png)

ਹੁਣ ਆਓ ਉਸੇ ਪ੍ਰੌੰਪਟ ਨੂੰ ਫਿਰ ਚ
```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# import dotenv
dotenv.load_dotenv()

# Get endpoint and key from environment variables
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
  api_key=os.environ['AZURE_OPENAI_API_KEY'],
  api_version = "2024-02-01"
  )


disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"""{meta_prompt}
Generate monument of the Arc of Triumph in Paris, France, in the evening light with a small child holding a Teddy looks on.
""""

try:
    # Create an image by using the image generation API
    generation_response = client.images.generate(
        prompt=prompt,    # Enter your prompt text here
        size='1024x1024',
        n=1,
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    image_url = generation_response.data[0].url  # extract image URL from response
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
except openai.BadRequestError as err:
    print(err)
```

## ਸ਼ਾਨਦਾਰ ਕੰਮ! ਆਪਣੀ ਸਿੱਖਿਆ ਜਾਰੀ ਰੱਖੋ

ਇਹ ਪਾਠ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਸਾਡੇ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) 'ਤੇ ਜਾਓ ਅਤੇ ਆਪਣਾ Generative AI ਗਿਆਨ ਵਧਾਉਣ ਜਾਰੀ ਰੱਖੋ!

ਪਾਠ 10 ਵੱਲ ਜਾਓ ਜਿੱਥੇ ਅਸੀਂ [low-code ਨਾਲ AI ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) ਦੇ ਤਰੀਕੇ ਦੇਖਾਂਗੇ।

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚੱਜੇਪਣ ਹੋ ਸਕਦੇ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਅਸਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।