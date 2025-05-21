<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T19:05:59+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "pa"
}
-->
# ਇਮੇਜ ਜਨਰੇਸ਼ਨ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣਾ

LLMs ਵਿੱਚ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਤੋਂ ਵੱਧ ਕੁਝ ਹੈ। ਇਹ ਟੈਕਸਟ ਵੇਰਵਿਆਂ ਤੋਂ ਤਸਵੀਰਾਂ ਜਨਰੇਟ ਕਰਨਾ ਵੀ ਸੰਭਵ ਹੈ। ਮੋਡੈਲਿਟੀ ਵਜੋਂ ਤਸਵੀਰਾਂ ਹੋਣ ਨਾਲ ਕਈ ਖੇਤਰਾਂ ਵਿੱਚ ਬਹੁਤ ਲਾਭਦਾਇਕ ਹੋ ਸਕਦਾ ਹੈ ਜਿਵੇਂ ਕਿ ਮੈਡਟੈਕ, ਆਰਕੀਟੈਕਚਰ, ਟੂਰਿਜ਼ਮ, ਗੇਮ ਵਿਕਾਸ ਅਤੇ ਹੋਰ। ਇਸ ਅਧਿਆਇ ਵਿੱਚ, ਅਸੀਂ ਦੋ ਸਭ ਤੋਂ ਪ੍ਰਸਿੱਧ ਇਮੇਜ ਜਨਰੇਸ਼ਨ ਮਾਡਲਾਂ, DALL-E ਅਤੇ Midjourney ਦੇਖਾਂਗੇ।

## ਪਰੀਚਿਆ

ਇਸ ਪਾਠ ਵਿੱਚ, ਅਸੀਂ ਕਵਰ ਕਰਾਂਗੇ:

- ਤਸਵੀਰ ਜਨਰੇਸ਼ਨ ਅਤੇ ਇਹ ਕਿਉਂ ਲਾਭਦਾਇਕ ਹੈ।
- DALL-E ਅਤੇ Midjourney, ਇਹ ਕੀ ਹਨ, ਅਤੇ ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦੇ ਹਨ।
- ਤੁਸੀਂ ਕਿਵੇਂ ਇੱਕ ਇਮੇਜ ਜਨਰੇਸ਼ਨ ਐਪ ਬਣਾਉਗੇ।

## ਸਿੱਖਣ ਦੇ ਲਕਸ਼

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਸਮਰਥ ਹੋਵੋਗੇ:

- ਇੱਕ ਇਮੇਜ ਜਨਰੇਸ਼ਨ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣਾ।
- ਆਪਣੇ ਐਪਲੀਕੇਸ਼ਨ ਲਈ ਮੈਟਾ ਪ੍ਰੋੰਪਟਸ ਨਾਲ ਸੀਮਾਵਾਂ ਪਰਿਭਾਸ਼ਿਤ ਕਰੋ।
- DALL-E ਅਤੇ Midjourney ਨਾਲ ਕੰਮ ਕਰੋ।

## ਇੱਕ ਇਮੇਜ ਜਨਰੇਸ਼ਨ ਐਪਲੀਕੇਸ਼ਨ ਕਿਉਂ ਬਣਾਉਣਾ?

ਤਸਵੀਰ ਜਨਰੇਸ਼ਨ ਐਪਲੀਕੇਸ਼ਨ ਜਨਰੇਟਿਵ AI ਦੀ ਸਮਰਥਾ ਦੀ ਜਾਂਚ ਕਰਨ ਦਾ ਇੱਕ ਵਧੀਆ ਤਰੀਕਾ ਹਨ। ਇਹਨਾਂ ਨੂੰ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ, ਉਦਾਹਰਣ ਵਜੋਂ:

- **ਤਸਵੀਰ ਸੰਪਾਦਨ ਅਤੇ ਸਿੰਥੇਸਿਸ**। ਤੁਸੀਂ ਤਸਵੀਰਾਂ ਜਨਰੇਟ ਕਰ ਸਕਦੇ ਹੋ ਵੱਖ-ਵੱਖ ਵਰਤੋਂ ਦੇ ਕੇਸਾਂ ਲਈ, ਜਿਵੇਂ ਕਿ ਤਸਵੀਰ ਸੰਪਾਦਨ ਅਤੇ ਤਸਵੀਰ ਸਿੰਥੇਸਿਸ।

- **ਵੱਖ-ਵੱਖ ਉਦਯੋਗਾਂ ਵਿੱਚ ਲਾਗੂ ਕੀਤਾ ਗਿਆ**। ਇਹਨਾਂ ਨੂੰ ਮੈਡਟੈਕ, ਟੂਰਿਜ਼ਮ, ਗੇਮ ਵਿਕਾਸ ਅਤੇ ਹੋਰ ਜਿਵੇਂ ਵੱਖ-ਵੱਖ ਉਦਯੋਗਾਂ ਲਈ ਤਸਵੀਰਾਂ ਜਨਰੇਟ ਕਰਨ ਲਈ ਵੀ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ।

## ਪ੍ਰਸੰਗ: Edu4All

ਇਸ ਪਾਠ ਦੇ ਹਿੱਸੇ ਵਜੋਂ, ਅਸੀਂ ਇਸ ਪਾਠ ਵਿੱਚ ਆਪਣੇ ਸਟਾਰਟਅਪ, Edu4All ਨਾਲ ਕੰਮ ਕਰਨਾ ਜਾਰੀ ਰੱਖਾਂਗੇ। ਵਿਦਿਆਰਥੀ ਆਪਣੀਆਂ ਮੁਲਾਂਕਣਾਂ ਲਈ ਤਸਵੀਰਾਂ ਬਣਾਉਣਗੇ, ਅਸਲ ਵਿੱਚ ਕਿਹੜੀਆਂ ਤਸਵੀਰਾਂ ਹਨ ਇਹ ਵਿਦਿਆਰਥੀਆਂ 'ਤੇ ਨਿਰਭਰ ਕਰਦਾ ਹੈ, ਪਰ ਉਹ ਆਪਣੇ ਆਪਣੇ ਪ੍ਰਿੰਸ ਦੀ ਕਹਾਣੀ ਲਈ ਚਿੱਤਰਾਂ ਹੋ ਸਕਦੇ ਹਨ ਜਾਂ ਆਪਣੀ ਕਹਾਣੀ ਲਈ ਨਵਾਂ ਪਾਤਰ ਬਣਾਉਣ ਜਾਂ ਆਪਣੇ ਵਿਚਾਰਾਂ ਅਤੇ ਧਾਰਨਾਵਾਂ ਨੂੰ ਦਰਸਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰ ਸਕਦੇ ਹਨ।

ਇਹ ਹੈ ਕਿ ਜੇਕਰ ਉਹ ਕਲਾਸ ਵਿੱਚ ਸਮਾਰਕਾਂ 'ਤੇ ਕੰਮ ਕਰ ਰਹੇ ਹਨ ਤਾਂ Edu4All ਦੇ ਵਿਦਿਆਰਥੀ ਉਦਾਹਰਣ ਲਈ ਕੀ ਜਨਰੇਟ ਕਰ ਸਕਦੇ ਹਨ:

"ਸਵੇਰੇ ਦੀ ਰੌਸ਼ਨੀ ਵਿੱਚ ਐਫਲ ਟਾਵਰ ਦੇ ਕੋਲ ਕੁੱਤਾ" ਵਰਗੇ ਪ੍ਰੋੰਪਟ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ

## DALL-E ਅਤੇ Midjourney ਕੀ ਹਨ?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) ਅਤੇ [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) ਦੋ ਸਭ ਤੋਂ ਪ੍ਰਸਿੱਧ ਇਮੇਜ ਜਨਰੇਸ਼ਨ ਮਾਡਲ ਹਨ, ਇਹ ਤੁਹਾਨੂੰ ਪ੍ਰੋੰਪਟਸ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਤਸਵੀਰਾਂ ਜਨਰੇਟ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦੇ ਹਨ।

### DALL-E

ਆਓ DALL-E ਨਾਲ ਸ਼ੁਰੂ ਕਰੀਏ, ਜੋ ਕਿ ਇੱਕ ਜਨਰੇਟਿਵ AI ਮਾਡਲ ਹੈ ਜੋ ਟੈਕਸਟ ਵੇਰਵਿਆਂ ਤੋਂ ਤਸਵੀਰਾਂ ਜਨਰੇਟ ਕਰਦਾ ਹੈ।

- **CLIP**, ਇੱਕ ਮਾਡਲ ਹੈ ਜੋ ਇਮੇਜ ਅਤੇ ਟੈਕਸਟ ਤੋਂ ਅੰਕੀ ਪ੍ਰਸਤੁਤੀਆਂ, ਜੋ ਕਿ ਅੰਕੜੇ ਦੀਆਂ ਗਿਣਤੀ ਪ੍ਰਸਤੁਤੀਆਂ ਹੁੰਦੀਆਂ ਹਨ, ਬਣਾਉਂਦਾ ਹੈ।

- **ਡਿਫਿਊਜ਼ਡ ਅਟੈਂਸ਼ਨ**, ਇੱਕ ਮਾਡਲ ਹੈ ਜੋ ਅੰਕੜੇ ਤੋਂ ਤਸਵੀਰਾਂ ਜਨਰੇਟ ਕਰਦਾ ਹੈ। DALL-E ਨੂੰ ਤਸਵੀਰਾਂ ਅਤੇ ਟੈਕਸਟ ਦੇ ਡਾਟਾਸੇਟ 'ਤੇ ਸਿਖਲਾਈ ਦਿੱਤੀ ਜਾਂਦੀ ਹੈ ਅਤੇ ਇਸ ਨੂੰ ਟੈਕਸਟ ਵੇਰਵਿਆਂ ਤੋਂ ਤਸਵੀਰਾਂ ਜਨਰੇਟ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਉਦਾਹਰਣ ਲਈ, DALL-E ਨੂੰ ਇੱਕ ਟੋਪੀ ਵਿੱਚ ਬਿੱਲੀ ਜਾਂ ਮੋਹਾਕ ਨਾਲ ਕੁੱਤੇ ਦੀ ਤਸਵੀਰ ਬਣਾਉਣ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ।

### Midjourney

Midjourney DALL-E ਦੀ ਤਰ੍ਹਾਂ ਹੀ ਕੰਮ ਕਰਦਾ ਹੈ, ਇਹ ਟੈਕਸਟ ਪ੍ਰੋੰਪਟਸ ਤੋਂ ਤਸਵੀਰਾਂ ਜਨਰੇਟ ਕਰਦਾ ਹੈ। Midjourney ਨੂੰ "ਟੋਪੀ ਵਿੱਚ ਬਿੱਲੀ" ਜਾਂ "ਮੋਹਾਕ ਨਾਲ ਕੁੱਤਾ" ਵਰਗੇ ਪ੍ਰੋੰਪਟਸ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਤਸਵੀਰਾਂ ਜਨਰੇਟ ਕਰਨ ਲਈ ਵੀ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ।

## DALL-E ਅਤੇ Midjourney ਕਿਵੇਂ ਕੰਮ ਕਰਦੇ ਹਨ

ਪਹਿਲਾਂ, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)। DALL-E ਇੱਕ ਜਨਰੇਟਿਵ AI ਮਾਡਲ ਹੈ ਜੋ ਟ੍ਰਾਂਸਫਾਰਮਰ ਆਰਕੀਟੈਕਚਰ 'ਤੇ ਅਧਾਰਿਤ ਹੈ ਜਿਸ ਵਿੱਚ ਇੱਕ _ਆਟੋਰੇਗਰੈਸੀਵ ਟ੍ਰਾਂਸਫਾਰਮਰ_ ਹੈ।

ਇੱਕ _ਆਟੋਰੇਗਰੈਸੀਵ ਟ੍ਰਾਂਸਫਾਰਮਰ_ ਇਹ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ ਕਿ ਇੱਕ ਮਾਡਲ ਕਿਵੇਂ ਟੈਕਸਟ ਵੇਰਵਿਆਂ ਤੋਂ ਤਸਵੀਰਾਂ ਜਨਰੇਟ ਕਰਦਾ ਹੈ, ਇਹ ਇੱਕ ਸਮੇਂ ਵਿੱਚ ਇੱਕ ਪਿਕਸਲ ਜਨਰੇਟ ਕਰਦਾ ਹੈ, ਅਤੇ ਫਿਰ ਅਗਲਾ ਪਿਕਸਲ ਜਨਰੇਟ ਕਰਨ ਲਈ ਜਨਰੇਟ ਕੀਤੇ ਪਿਕਸਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ। ਇੱਕ ਨਿਊਰਲ ਨੈਟਵਰਕ ਵਿੱਚ ਕਈ ਪਰਤਾਂ ਵਿੱਚੋਂ ਲੰਘਦਾ ਹੈ, ਜਦੋਂ ਤੱਕ ਕਿ ਤਸਵੀਰ ਪੂਰੀ ਨਹੀਂ ਹੋ ਜਾਂਦੀ।

ਇਸ ਪ੍ਰਕਿਰਿਆ ਨਾਲ, DALL-E, ਤਸਵੀਰ ਵਿੱਚ ਲੱਛਣ, ਵਸਤੂਆਂ, ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ, ਅਤੇ ਹੋਰ ਨੂੰ ਨਿਯੰਤਰਿਤ ਕਰਦਾ ਹੈ ਜੋ ਇਹ ਜਨਰੇਟ ਕਰਦਾ ਹੈ। ਹਾਲਾਂਕਿ, DALL-E 2 ਅਤੇ 3 ਜਨਰੇਟ ਕੀਤੀ ਗਈ ਤਸਵੀਰ 'ਤੇ ਵੱਧ ਨਿਯੰਤਰਣ ਕਰਦੇ ਹਨ।

## ਆਪਣੀ ਪਹਿਲੀ ਇਮੇਜ ਜਨਰੇਸ਼ਨ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣਾ

ਇੱਕ ਇਮੇਜ ਜਨਰੇਸ਼ਨ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ ਲਈ ਤੁਹਾਨੂੰ ਕੀ ਚਾਹੀਦਾ ਹੈ? ਤੁਹਾਨੂੰ ਹੇਠ ਲਿਖੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਦੀ ਲੋੜ ਹੈ:

- **python-dotenv**, ਤੁਹਾਨੂੰ ਆਪਣੀਆਂ ਸਿਕਰਟਸ ਨੂੰ ਕੋਡ ਤੋਂ ਦੂਰ _.env_ ਫਾਈਲ ਵਿੱਚ ਰੱਖਣ ਲਈ ਇਸ ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਵਰਤੋਂ ਕਰਨ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ।
- **openai**, ਇਹ ਲਾਇਬ੍ਰੇਰੀ ਹੈ ਜੋ ਤੁਸੀਂ OpenAI API ਨਾਲ ਗੱਲਬਾਤ ਕਰਨ ਲਈ ਵਰਤੋਂ ਕਰੋਂਗੇ।
- **pillow**, ਪਾਇਥਨ ਵਿੱਚ ਤਸਵੀਰਾਂ ਨਾਲ ਕੰਮ ਕਰਨ ਲਈ।
- **requests**, HTTP ਬੇਨਤੀਆਂ ਕਰਨ ਵਿੱਚ ਤੁਹਾਡੀ ਮਦਦ ਕਰਨ ਲਈ।

1. ਹੇਠ ਲਿਖੀ ਸਮੱਗਰੀ ਨਾਲ _.env_ ਫਾਈਲ ਬਣਾਓ:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   ਆਪਣੇ ਸਰੋਤ ਲਈ "ਕੁੰਜੀਆਂ ਅਤੇ ਐਂਡਪੋਇੰਟ" ਭਾਗ ਵਿੱਚ ਅਜ਼ੂਰ ਪੋਰਟਲ ਵਿੱਚ ਇਸ ਜਾਣਕਾਰੀ ਨੂੰ ਲੱਭੋ।

1. ਉੱਪਰ ਦਿੱਤੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਨੂੰ ਇੱਕ ਫਾਈਲ _requirements.txt_ ਵਿੱਚ ਇਕੱਠਾ ਕਰੋ ਇਸ ਤਰ੍ਹਾਂ:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. ਅਗਲੇ, ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਓ ਅਤੇ ਲਾਇਬ੍ਰੇਰੀਆਂ ਨੂੰ ਸਥਾਪਿਤ ਕਰੋ:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   ਵਿਂਡੋਜ਼ ਲਈ, ਆਪਣੇ ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਨੂੰ ਬਣਾਉਣ ਅਤੇ ਸਰਗਰਮ ਕਰਨ ਲਈ ਹੇਠ ਲਿਖੀਆਂ ਕਮਾਂਡਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ ਨਾਮਕ ਫਾਈਲ ਵਿੱਚ ਹੇਠ ਲਿਖਿਆ ਕੋਡ ਸ਼ਾਮਲ ਕਰੋ:

   ```python
   import openai
   import os
   import requests
   from PIL import Image
   import dotenv

   # import dotenv
   dotenv.load_dotenv()

   # Get endpoint and key from environment variables
   openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
   openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

   # Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
   openai.api_version = '2023-06-01-preview'
   openai.api_type = 'azure'


   try:
       # Create an image by using the image generation API
       generation_response = openai.Image.create(
           prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
           size='1024x1024',
           n=2,
           temperature=0,
       )
       # Set the directory for the stored image
       image_dir = os.path.join(os.curdir, 'images')

       # If the directory doesn't exist, create it
       if not os.path.isdir(image_dir):
           os.mkdir(image_dir)

       # Initialize the image path (note the filetype should be png)
       image_path = os.path.join(image_dir, 'generated-image.png')

       # Retrieve the generated image
       image_url = generation_response["data"][0]["url"]  # extract image URL from response
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

ਆਓ ਇਸ ਕੋਡ ਨੂੰ ਸਮਝਾਈਏ:

- ਪਹਿਲਾਂ, ਅਸੀਂ ਲੋੜੀਂਦੇ ਲਾਇਬ੍ਰੇਰੀਆਂ ਨੂੰ ਇੰਪੋਰਟ ਕਰਦੇ ਹਾਂ, ਜਿਸ ਵਿੱਚ OpenAI ਲਾਇਬ੍ਰੇਰੀ, dotenv ਲਾਇਬ੍ਰੇਰੀ, requests ਲਾਇਬ੍ਰੇਰੀ, ਅਤੇ Pillow ਲਾਇਬ੍ਰੇਰੀ ਸ਼ਾਮਲ ਹਨ।

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- ਅਗਲੇ, ਅਸੀਂ _.env_ ਫਾਈਲ ਤੋਂ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲਾਂ ਨੂੰ ਲੋਡ ਕਰਦੇ ਹਾਂ।

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- ਉਸ ਤੋਂ ਬਾਅਦ, ਅਸੀਂ OpenAI API ਲਈ ਐਂਡਪੋਇੰਟ, ਕੁੰਜੀ, ਵਰਜਨ ਅਤੇ ਕਿਸਮ ਸੈੱਟ ਕਰਦੇ ਹਾਂ।

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- ਅਗਲੇ, ਅਸੀਂ ਤਸਵੀਰ ਜਨਰੇਟ ਕਰਦੇ ਹਾਂ:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  ਉੱਪਰ ਦਿੱਤਾ ਕੋਡ ਇੱਕ JSON ਵਸਤੂ ਨਾਲ ਜਵਾਬ ਦਿੰਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਜਨਰੇਟ ਕੀਤੀ ਗਈ ਤਸਵੀਰ ਦਾ URL ਹੁੰਦਾ ਹੈ। ਅਸੀਂ ਤਸਵੀਰ ਡਾਊਨਲੋਡ ਕਰਨ ਅਤੇ ਇਸਨੂੰ ਫਾਈਲ ਵਿੱਚ ਸੇਵ ਕਰਨ ਲਈ URL ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹਾਂ।

- ਆਖ਼ਰਕਾਰ, ਅਸੀਂ ਤਸਵੀਰ ਖੋਲ੍ਹਦੇ ਹਾਂ ਅਤੇ ਇਸਨੂੰ ਪ੍ਰਮਾਣਿਤ ਤਸਵੀਰ ਦਰਸ਼ਕ ਨਾਲ ਪ੍ਰਦਰਸ਼ਿਤ ਕਰਦੇ ਹਾਂ:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### ਤਸਵੀਰ ਜਨਰੇਟ ਕਰਨ ਬਾਰੇ ਹੋਰ ਵਿਸਥਾਰ

ਆਓ ਇਸ ਕੋਡ ਨੂੰ ਵੇਖੀਏ ਜੋ ਤਸਵੀਰ ਜਨਰੇਟ ਕਰਦਾ ਹੈ:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, ਉਹ ਟੈਕਸਟ ਪ੍ਰੋੰਪਟ ਹੈ ਜੋ ਤਸਵੀਰ ਜਨਰੇਟ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ। ਇਸ ਮਾਮਲੇ ਵਿੱਚ, ਅਸੀਂ ਪ੍ਰੋੰਪਟ "ਘੋੜੇ 'ਤੇ ਖਰਗੋਸ਼, ਚੂਪਾ ਚੂਪਸ ਫੜਿਆ ਹੋਇਆ, ਧੁੰਦਲੇ ਘਾਸ ਦੇ ਮੈਦਾਨ ਵਿੱਚ ਜਿੱਥੇ ਡੈਫੋਡਿਲਸ ਉੱਗਦੇ ਹਨ" ਦੀ ਵਰਤੋਂ ਕਰ ਰਹੇ ਹਾਂ।
- **size**, ਜਨਰੇਟ ਕੀਤੀ ਗਈ ਤਸਵੀਰ ਦਾ ਆਕਾਰ ਹੈ। ਇਸ ਮਾਮਲੇ ਵਿੱਚ, ਅਸੀਂ ਇੱਕ ਤਸਵੀਰ ਜਨਰੇਟ ਕਰ ਰਹੇ ਹਾਂ ਜੋ 1024x1024 ਪਿਕਸਲ ਹੈ।
- **n**, ਜਨਰੇਟ ਕੀਤੀਆਂ ਤਸਵੀਰਾਂ ਦੀ ਗਿਣਤੀ ਹੈ। ਇਸ ਮਾਮਲੇ ਵਿੱਚ, ਅਸੀਂ ਦੋ ਤਸਵੀਰਾਂ ਜਨਰੇਟ ਕਰ ਰਹੇ ਹਾਂ।
- **temperature**, ਇੱਕ ਪੈਰਾਮੀਟਰ ਹੈ ਜੋ ਜਨਰੇਟਿਵ AI ਮਾਡਲ ਦੇ ਨਤੀਜੇ ਦੀ ਬੇਤਰਤੀਬੀ ਨੂੰ ਨਿਯੰਤਰਿਤ ਕਰਦਾ ਹੈ। ਤਾਪਮਾਨ 0 ਅਤੇ 1 ਦੇ ਵਿਚਕਾਰ ਇੱਕ ਮੁੱਲ ਹੈ ਜਿੱਥੇ 0 ਦਾ ਮਤਲਬ ਹੈ ਕਿ ਨਤੀਜਾ ਨਿਰਧਾਰਤ ਹੈ ਅਤੇ 1 ਦਾ ਮਤਲਬ ਹੈ ਕਿ ਨਤੀਜਾ ਬੇਤਰਤੀਬ ਹੈ। ਡਿਫੌਲਟ ਮੁੱਲ 0.7 ਹੈ।

ਤਸਵੀਰਾਂ ਨਾਲ ਹੋਰ ਵੀ ਚੀਜ਼ਾਂ ਹਨ ਜੋ ਅਸੀਂ ਅਗਲੇ ਭਾਗ ਵਿੱਚ ਕਵਰ ਕਰਾਂਗੇ।

## ਤਸਵੀਰ ਜਨਰੇਸ਼ਨ ਦੀ ਵਾਧੂ ਸਮਰਥਾ

ਤੁਸੀਂ ਹੁਣ ਤੱਕ ਦੇਖਿਆ ਹੈ ਕਿ ਅਸੀਂ ਪਾਇਥਨ ਵਿੱਚ ਕੁਝ ਲਾਈਨਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਤਸਵੀਰ ਕਿਵੇਂ ਜਨਰੇਟ ਕਰਨ ਵਿੱਚ ਸਮਰਥ ਹੋਏ। ਹਾਲਾਂਕਿ, ਤਸਵੀਰਾਂ ਨਾਲ ਹੋਰ ਵੀ ਚੀਜ਼ਾਂ ਹਨ ਜੋ ਤੁਸੀਂ ਕਰ ਸਕਦੇ ਹੋ।

ਤੁਸੀਂ ਹੇਠ ਲਿਖੀਆਂ ਚੀਜ਼ਾਂ ਵੀ ਕਰ ਸਕਦੇ ਹੋ:

- **ਸੰਪਾਦਨ ਕਰੋ**। ਮੌਜੂਦਾ ਤਸਵੀਰ, ਇੱਕ ਮਾਸਕ ਅਤੇ ਇੱਕ ਪ੍ਰੋੰਪਟ ਪ੍ਰਦਾਨ ਕਰਕੇ, ਤੁਸੀਂ ਇੱਕ ਤਸਵੀਰ ਨੂੰ ਬਦਲ ਸਕਦੇ ਹੋ। ਉਦਾਹਰਣ ਲਈ, ਤੁਸੀਂ ਤਸਵੀਰ ਦੇ ਇੱਕ ਹਿੱਸੇ ਵਿੱਚ ਕੁਝ ਸ਼ਾਮਲ ਕਰ ਸਕਦੇ ਹੋ। ਕਲਪਨਾ ਕਰੋ ਸਾਡੀ ਖਰਗੋਸ਼ ਦੀ ਤਸਵੀਰ, ਤੁਸੀਂ ਖਰਗੋਸ਼ ਨੂੰ ਇੱਕ ਟੋਪੀ ਸ਼ਾਮਲ ਕਰ ਸਕਦੇ ਹੋ। ਤੁਸੀਂ ਇਹ ਕਿਵੇਂ ਕਰੋਗੇ ਇਹ ਤਸਵੀਰ, ਇੱਕ ਮਾਸਕ (ਬਦਲਾਅ ਲਈ ਖੇਤਰ ਦੇ ਹਿੱਸੇ ਦੀ ਪਛਾਣ ਕਰਨਾ) ਅਤੇ ਇੱਕ ਟੈਕਸਟ ਪ੍ਰੋੰਪਟ ਪ੍ਰਦਾਨ ਕਰਕੇ ਹੈ ਕਿ ਕੀ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ।

  ```python
  response = openai.Image.create_edit(
    image=open("base_image.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="An image of a rabbit with a hat on its head.",
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  ਬੇਸ ਤਸਵੀਰ ਵਿੱਚ ਸਿਰਫ਼ ਖਰਗੋਸ਼ ਹੀ ਸ਼ਾਮਲ ਹੋਵੇਗਾ ਪਰ ਆਖਰੀ ਤਸਵੀਰ ਵਿੱਚ ਖਰਗੋਸ਼ 'ਤੇ ਟੋਪੀ ਹੋਵੇਗੀ।

- **ਵੈਰੀਏਸ਼ਨ ਬਣਾਓ**। ਵਿਚਾਰ ਇਹ ਹੈ ਕਿ ਤੁਸੀਂ ਇੱਕ ਮੌਜੂਦਾ ਤਸਵੀਰ ਲੈਂਦੇ ਹੋ ਅਤੇ ਮੰਗਦੇ ਹੋ ਕਿ ਵੈਰੀਏਸ਼ਨ ਬਣਾਏ ਜਾਣ। ਇੱਕ ਵੈਰੀਏਸ਼ਨ ਬਣਾਉਣ ਲਈ, ਤੁਸੀਂ ਇੱਕ ਤਸਵੀਰ ਅਤੇ ਇੱਕ ਟੈਕਸਟ ਪ੍ਰੋੰਪਟ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹੋ ਅਤੇ ਕੋਡ ਇਸ ਤਰ੍ਹਾਂ:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > ਨੋਟ ਕਰੋ, ਇਹ ਸਿਰਫ਼ OpenAI 'ਤੇ ਸਮਰਥਿਤ ਹੈ

## ਤਾਪਮਾਨ

ਤਾਪਮਾਨ ਇੱਕ ਪੈਰਾਮੀਟਰ ਹੈ ਜੋ ਜਨਰੇਟਿਵ AI ਮਾਡਲ ਦੇ ਨਤੀਜੇ ਦੀ ਬੇਤਰਤੀਬੀ ਨੂੰ ਨਿਯੰਤਰਿਤ ਕਰਦਾ ਹੈ। ਤਾਪਮਾਨ 0 ਅਤੇ 1 ਦੇ ਵਿਚਕਾਰ ਇੱਕ ਮੁੱਲ ਹੈ ਜਿੱਥੇ 0 ਦਾ ਮਤਲਬ ਹੈ ਕਿ ਨਤੀਜਾ ਨਿਰਧਾਰਤ ਹੈ ਅਤੇ 1 ਦਾ ਮਤਲਬ ਹੈ ਕਿ ਨਤੀਜਾ ਬੇਤਰਤੀਬ ਹੈ। ਡਿਫੌਲਟ ਮੁੱਲ 0.7 ਹੈ।

ਆਓ ਦੇਖੀਏ ਕਿ ਤਾਪਮਾਨ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ, ਇਸ ਪ੍ਰੋੰਪਟ ਨੂੰ ਦੋ ਵਾਰ ਚਲਾਕੇ:

> ਪ੍ਰੋੰਪਟ: "ਘੋੜੇ 'ਤੇ ਖਰਗੋਸ਼, ਚੂਪਾ ਚੂਪਸ ਫੜਿਆ ਹੋਇਆ, ਧੁੰਦਲੇ ਘਾਸ ਦੇ ਮੈਦਾਨ ਵਿੱਚ ਜਿੱਥੇ ਡੈਫੋਡਿਲਸ ਉੱਗਦੇ ਹਨ"

ਹੁਣ ਆਓ ਉਸੇ ਪ੍ਰੋੰਪਟ ਨੂੰ ਚਲਾਈਏ ਸਿਰਫ਼ ਇਹ ਵੇਖਣ ਲਈ ਕਿ ਸਾਨੂੰ ਦੋ ਵਾਰ ਇੱਕੋ ਤਸਵੀਰ ਨਹੀਂ ਮਿਲੇਗੀ:

ਜਿਵੇਂ ਤੁਸੀਂ ਦੇਖ ਸਕਦੇ ਹੋ, ਤਸਵੀਰਾਂ ਇੱਕੋ ਜਿਹੀਆਂ ਹਨ, ਪਰ ਇਕੋ ਨਹੀਂ। ਆਓ ਤਾਪਮਾਨ ਮੁੱਲ ਨੂੰ 0.1 'ਤੇ ਬਦਲਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੀਏ ਅਤੇ ਵੇਖੀਏ ਕਿ ਕੀ ਹੁੰਦਾ ਹੈ:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### ਤਾਪਮਾਨ ਬਦਲਣਾ

ਤਾਂ ਆਓ ਜਵਾਬ ਨੂੰ ਵੱਧ ਨਿਰਧਾਰਤ ਬਣਾਉਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੀਏ। ਅਸੀਂ ਜਨਰੇਟ ਕੀਤੀਆਂ ਦੋ ਤਸਵੀਰਾਂ ਤੋਂ ਅਨੁਮਾਨ ਲਗਾ ਸਕਦੇ ਹਾਂ ਕਿ ਪਹਿਲੀ ਤਸਵੀਰ ਵਿੱਚ ਇੱਕ ਖਰਗੋਸ਼ ਹੈ ਅਤੇ ਦੂਜੀ ਤਸਵੀਰ ਵਿੱਚ ਇੱਕ ਘੋੜਾ ਹੈ, ਇਸ ਲਈ ਤਸਵੀਰਾਂ ਬਹੁਤ ਵੱਧ ਬਦਲ ਰਹੀਆਂ ਹਨ।

ਇਸ ਲਈ ਆਓ ਆਪਣਾ ਕੋਡ ਬਦਲੋ ਅਤੇ ਤਾਪਮਾਨ ਨੂੰ 0 'ਤੇ ਸੈੱਟ ਕਰੋ, ਇਸ ਤਰ੍ਹਾਂ:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

ਹੁਣ ਜਦੋਂ ਤੁਸੀਂ ਇਹ ਕੋਡ ਚਲਾਉਂਦੇ ਹੋ, ਤੁਹਾਨੂੰ ਇਹ ਦੋ ਤਸਵੀਰਾਂ ਮਿਲਦੀਆਂ ਹਨ:

ਇੱਥੇ ਤੁਸੀਂ ਸਪੱਸ਼ਟ ਤੌਰ 'ਤੇ ਦੇਖ ਸਕਦੇ ਹੋ ਕਿ ਤਸਵੀਰਾਂ ਇੱਕ ਦੂਜੇ ਨਾਲ ਵੱਧ ਮਿਲਦੀਆਂ ਹਨ।

## ਮੈਟਾਪ੍ਰੋੰਪਟਸ ਨਾਲ ਆਪਣੇ ਐਪਲੀਕੇਸ਼ਨ ਲਈ ਸੀਮਾਵਾਂ ਕਿਵੇਂ ਪਰਿਭਾਸ਼ਿਤ ਕਰਨੀ ਹੈ

ਸਾਡੇ ਡੈਮੋ ਨਾਲ, ਅਸੀਂ ਪਹਿਲਾਂ ਹੀ ਆਪਣੇ ਗਾਹਕਾਂ ਲਈ ਤਸਵੀਰਾਂ ਜਨਰੇਟ ਕਰ ਸਕਦੇ ਹਾਂ। ਹਾਲਾਂਕਿ, ਸਾਨੂੰ ਆਪਣੇ ਐਪਲੀਕੇਸ਼ਨ ਲਈ ਕੁਝ ਸੀਮਾਵਾਂ ਬਣਾਉਣ ਦੀ ਲੋੜ ਹੈ।

ਉਦਾਹਰਣ ਲਈ, ਅਸੀਂ ਨਹੀਂ ਚਾਹੁੰਦੇ ਕਿ ਅਜ

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਪਰ ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁੱਤੀਜਨਕਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਈ ਕਿਸੇ ਵੀ ਗਲਤ ਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।