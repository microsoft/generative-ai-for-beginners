<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d46aad0917a1a342d613e2c13d457da5",
  "translation_date": "2025-07-09T12:52:41+00:00",
  "source_file": "08-building-search-applications/README.md",
  "language_code": "pa"
}
-->
# ਖੋਜ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣਾ

[![ਜਨਰੇਟਿਵ AI ਅਤੇ ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲਾਂ ਦਾ ਪਰਿਚਯ](../../../translated_images/08-lesson-banner.8fff48c566dad08a1cbb9f4b4a2c16adfdd288a7bbfffdd30770b466fe08c25c.pa.png)](https://aka.ms/gen-ai-lesson8-gh?WT.mc_id=academic-105485-koreyst)

> > _ਇਸ ਪਾਠ ਦਾ ਵੀਡੀਓ ਦੇਖਣ ਲਈ ਉਪਰ ਦਿੱਤੀ ਤਸਵੀਰ 'ਤੇ ਕਲਿੱਕ ਕਰੋ_

LLM ਸਿਰਫ ਚੈਟਬੋਟ ਅਤੇ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਤੱਕ ਸੀਮਿਤ ਨਹੀਂ ਹਨ। Embeddings ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਖੋਜ ਐਪਲੀਕੇਸ਼ਨ ਵੀ ਬਣਾਈਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ। Embeddings ਡੇਟਾ ਦੇ ਗਿਣਤੀਕ ਪ੍ਰਤੀਨਿਧਿਤਵ ਹਨ, ਜਿਨ੍ਹਾਂ ਨੂੰ ਵੈਕਟਰ ਵੀ ਕਹਿੰਦੇ ਹਨ, ਅਤੇ ਇਹ ਡੇਟਾ ਲਈ ਸੈਮਾਂਟਿਕ ਖੋਜ ਵਿੱਚ ਵਰਤੇ ਜਾਂਦੇ ਹਨ।

ਇਸ ਪਾਠ ਵਿੱਚ, ਤੁਸੀਂ ਸਾਡੇ ਸਿੱਖਿਆ ਸਟਾਰਟਅਪ ਲਈ ਇੱਕ ਖੋਜ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ ਜਾ ਰਹੇ ਹੋ। ਸਾਡਾ ਸਟਾਰਟਅਪ ਇੱਕ ਗੈਰ-ਮੁਨਾਫਾ ਸੰਸਥਾ ਹੈ ਜੋ ਵਿਕਾਸਸ਼ੀਲ ਦੇਸ਼ਾਂ ਦੇ ਵਿਦਿਆਰਥੀਆਂ ਨੂੰ ਮੁਫ਼ਤ ਸਿੱਖਿਆ ਪ੍ਰਦਾਨ ਕਰਦੀ ਹੈ। ਸਾਡੇ ਕੋਲ ਬਹੁਤ ਸਾਰੇ YouTube ਵੀਡੀਓ ਹਨ ਜਿਨ੍ਹਾਂ ਦੀ ਮਦਦ ਨਾਲ ਵਿਦਿਆਰਥੀ AI ਬਾਰੇ ਸਿੱਖ ਸਕਦੇ ਹਨ। ਸਾਡਾ ਸਟਾਰਟਅਪ ਇੱਕ ਐਸਾ ਖੋਜ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣਾ ਚਾਹੁੰਦਾ ਹੈ ਜੋ ਵਿਦਿਆਰਥੀਆਂ ਨੂੰ ਸਵਾਲ ਲਿਖ ਕੇ YouTube ਵੀਡੀਓ ਖੋਜਣ ਦੀ ਆਗਿਆ ਦੇਵੇ।

ਉਦਾਹਰਨ ਵਜੋਂ, ਕੋਈ ਵਿਦਿਆਰਥੀ 'What are Jupyter Notebooks?' ਜਾਂ 'What is Azure ML' ਲਿਖ ਸਕਦਾ ਹੈ ਅਤੇ ਖੋਜ ਐਪਲੀਕੇਸ਼ਨ ਸਵਾਲ ਨਾਲ ਸੰਬੰਧਿਤ YouTube ਵੀਡੀਓਜ਼ ਦੀ ਸੂਚੀ ਵਾਪਸ ਕਰੇਗਾ, ਅਤੇ ਵਧੀਆ ਗੱਲ ਇਹ ਹੈ ਕਿ ਖੋਜ ਐਪਲੀਕੇਸ਼ਨ ਵੀਡੀਓ ਵਿੱਚ ਉਸ ਥਾਂ ਦਾ ਲਿੰਕ ਵੀ ਦੇਵੇਗਾ ਜਿੱਥੇ ਸਵਾਲ ਦਾ ਜਵਾਬ ਮਿਲਦਾ ਹੈ।

## ਪਰਿਚਯ

ਇਸ ਪਾਠ ਵਿੱਚ ਅਸੀਂ ਕਵਰ ਕਰਾਂਗੇ:

- ਸੈਮਾਂਟਿਕ ਅਤੇ ਕੀਵਰਡ ਖੋਜ ਵਿੱਚ ਫਰਕ।
- Text Embeddings ਕੀ ਹਨ।
- Text Embeddings ਇੰਡੈਕਸ ਬਣਾਉਣਾ।
- Text Embeddings ਇੰਡੈਕਸ ਵਿੱਚ ਖੋਜ ਕਰਨਾ।

## ਸਿੱਖਣ ਦੇ ਲਕੜ

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- ਸੈਮਾਂਟਿਕ ਅਤੇ ਕੀਵਰਡ ਖੋਜ ਵਿੱਚ ਫਰਕ ਦੱਸਣ ਲਈ।
- Text Embeddings ਕੀ ਹਨ ਸਮਝਾਉਣ ਲਈ।
- Embeddings ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਡੇਟਾ ਖੋਜਣ ਲਈ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ ਲਈ।

## ਖੋਜ ਐਪਲੀਕੇਸ਼ਨ ਕਿਉਂ ਬਣਾਈਏ?

ਖੋਜ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ ਨਾਲ ਤੁਹਾਨੂੰ ਸਮਝ ਆਵੇਗੀ ਕਿ Embeddings ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਡੇਟਾ ਕਿਵੇਂ ਖੋਜਿਆ ਜਾਂਦਾ ਹੈ। ਤੁਸੀਂ ਇਹ ਵੀ ਸਿੱਖੋਗੇ ਕਿ ਵਿਦਿਆਰਥੀਆਂ ਲਈ ਇੱਕ ਐਸਾ ਖੋਜ ਐਪਲੀਕੇਸ਼ਨ ਕਿਵੇਂ ਬਣਾਇਆ ਜਾਵੇ ਜੋ ਉਹਨਾਂ ਨੂੰ ਜਾਣਕਾਰੀ ਤੇਜ਼ੀ ਨਾਲ ਲੱਭਣ ਵਿੱਚ ਮਦਦ ਕਰੇ।

ਇਸ ਪਾਠ ਵਿੱਚ Microsoft [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) YouTube ਚੈਨਲ ਦੇ ਟ੍ਰਾਂਸਕ੍ਰਿਪਟਸ ਦਾ Embedding ਇੰਡੈਕਸ ਸ਼ਾਮਲ ਹੈ। AI Show ਇੱਕ YouTube ਚੈਨਲ ਹੈ ਜੋ ਤੁਹਾਨੂੰ AI ਅਤੇ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਬਾਰੇ ਸਿਖਾਉਂਦਾ ਹੈ। Embedding ਇੰਡੈਕਸ ਵਿੱਚ ਹਰ YouTube ਟ੍ਰਾਂਸਕ੍ਰਿਪਟ ਲਈ Embeddings ਹਨ ਜੋ ਅਕਤੂਬਰ 2023 ਤੱਕ ਦੇ ਹਨ। ਤੁਸੀਂ ਇਸ Embedding ਇੰਡੈਕਸ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸਾਡੇ ਸਟਾਰਟਅਪ ਲਈ ਖੋਜ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਗੇ। ਖੋਜ ਐਪਲੀਕੇਸ਼ਨ ਵੀਡੀਓ ਵਿੱਚ ਉਸ ਥਾਂ ਦਾ ਲਿੰਕ ਵਾਪਸ ਕਰੇਗਾ ਜਿੱਥੇ ਸਵਾਲ ਦਾ ਜਵਾਬ ਹੈ। ਇਹ ਵਿਦਿਆਰਥੀਆਂ ਲਈ ਜਾਣਕਾਰੀ ਤੇਜ਼ੀ ਨਾਲ ਲੱਭਣ ਦਾ ਵਧੀਆ ਤਰੀਕਾ ਹੈ।

ਹੇਠਾਂ ਦਿੱਤਾ ਗਿਆ ਉਦਾਹਰਨ ਸਵਾਲ 'can you use rstudio with azure ml?' ਲਈ ਸੈਮਾਂਟਿਕ ਕਵੈਰੀ ਹੈ। YouTube URL ਵਿੱਚ ਟਾਈਮਸਟੈਂਪ ਹੁੰਦਾ ਹੈ ਜੋ ਤੁਹਾਨੂੰ ਵੀਡੀਓ ਵਿੱਚ ਉਸ ਥਾਂ ਲੈ ਜਾਂਦਾ ਹੈ ਜਿੱਥੇ ਸਵਾਲ ਦਾ ਜਵਾਬ ਹੈ।

![ਸਵਾਲ "can you use rstudio with Azure ML" ਲਈ ਸੈਮਾਂਟਿਕ ਕਵੈਰੀ](../../../translated_images/query-results.bb0480ebf025fac69c5179ad4d53b6627d643046838c857dc9e2b1281f1cdeb7.pa.png)

## ਸੈਮਾਂਟਿਕ ਖੋਜ ਕੀ ਹੈ?

ਹੁਣ ਤੁਸੀਂ ਸੋਚ ਰਹੇ ਹੋਵੋਗੇ ਕਿ ਸੈਮਾਂਟਿਕ ਖੋਜ ਕੀ ਹੈ? ਸੈਮਾਂਟਿਕ ਖੋਜ ਇੱਕ ਖੋਜ ਤਕਨੀਕ ਹੈ ਜੋ ਕਵੈਰੀ ਵਿੱਚ ਸ਼ਬਦਾਂ ਦੇ ਅਰਥ ਜਾਂ ਮਤਲਬ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸੰਬੰਧਿਤ ਨਤੀਜੇ ਵਾਪਸ ਕਰਦੀ ਹੈ।

ਇੱਥੇ ਇੱਕ ਸੈਮਾਂਟਿਕ ਖੋਜ ਦਾ ਉਦਾਹਰਨ ਹੈ। ਮੰਨ ਲਓ ਤੁਸੀਂ ਕਾਰ ਖਰੀਦਣੀ ਹੈ, ਤਾਂ ਤੁਸੀਂ 'my dream car' ਖੋਜ ਸਕਦੇ ਹੋ। ਸੈਮਾਂਟਿਕ ਖੋਜ ਸਮਝਦਾ ਹੈ ਕਿ ਤੁਸੀਂ ਕਾਰ ਦਾ ਸੁਪਨਾ ਨਹੀਂ ਦੇਖ ਰਹੇ, ਬਲਕਿ ਆਪਣੀ 'ਆਦਰਸ਼' ਕਾਰ ਖਰੀਦਣੀ ਹੈ। ਸੈਮਾਂਟਿਕ ਖੋਜ ਤੁਹਾਡੇ ਇਰਾਦੇ ਨੂੰ ਸਮਝਦਾ ਹੈ ਅਤੇ ਸੰਬੰਧਿਤ ਨਤੀਜੇ ਦਿੰਦਾ ਹੈ। ਇਸਦੇ ਬਦਲੇ, ਕੀਵਰਡ ਖੋਜ ਸਿਰਫ਼ ਸ਼ਬਦਾਂ ਨੂੰ ਲਿਟਰਲ ਤੌਰ 'ਤੇ ਖੋਜਦਾ ਹੈ ਅਤੇ ਅਕਸਰ ਗਲਤ ਨਤੀਜੇ ਦਿੰਦਾ ਹੈ।

## Text Embeddings ਕੀ ਹਨ?

[Text embeddings](https://en.wikipedia.org/wiki/Word_embedding?WT.mc_id=academic-105485-koreyst) ਇੱਕ ਟੈਕਸਟ ਪ੍ਰਤੀਨਿਧਿਤਵ ਤਕਨੀਕ ਹੈ ਜੋ [ਨੈਚਰਲ ਲੈਂਗਵੇਜ ਪ੍ਰੋਸੈਸਿੰਗ](https://en.wikipedia.org/wiki/Natural_language_processing?WT.mc_id=academic-105485-koreyst) ਵਿੱਚ ਵਰਤੀ ਜਾਂਦੀ ਹੈ। Text embeddings ਟੈਕਸਟ ਦੇ ਸੈਮਾਂਟਿਕ ਗਿਣਤੀਕ ਪ੍ਰਤੀਨਿਧਿਤਵ ਹਨ। Embeddings ਡੇਟਾ ਨੂੰ ਇਸ ਤਰੀਕੇ ਨਾਲ ਦਰਸਾਉਂਦੇ ਹਨ ਜੋ ਮਸ਼ੀਨ ਲਈ ਸਮਝਣਾ ਆਸਾਨ ਹੁੰਦਾ ਹੈ। Text embeddings ਬਣਾਉਣ ਲਈ ਕਈ ਮਾਡਲ ਹਨ, ਇਸ ਪਾਠ ਵਿੱਚ ਅਸੀਂ OpenAI Embedding Model ਦੀ ਵਰਤੋਂ ਕਰਕੇ embeddings ਬਣਾਉਣ 'ਤੇ ਧਿਆਨ ਦੇਵਾਂਗੇ।

ਇੱਕ ਉਦਾਹਰਨ ਦੇ ਤੌਰ 'ਤੇ, ਸੋਚੋ ਹੇਠਾਂ ਦਿੱਤਾ ਟੈਕਸਟ AI Show YouTube ਚੈਨਲ ਦੇ ਕਿਸੇ ਐਪੀਸੋਡ ਦੇ ਟ੍ਰਾਂਸਕ੍ਰਿਪਟ ਵਿੱਚ ਹੈ:

```text
Today we are going to learn about Azure Machine Learning.
```

ਅਸੀਂ ਇਸ ਟੈਕਸਟ ਨੂੰ OpenAI Embedding API ਨੂੰ ਭੇਜਾਂਗੇ ਅਤੇ ਇਹ 1536 ਨੰਬਰਾਂ ਵਾਲਾ ਇੱਕ ਵੈਕਟਰ ਵਾਪਸ ਕਰੇਗਾ। ਵੈਕਟਰ ਵਿੱਚ ਹਰ ਨੰਬਰ ਟੈਕਸਟ ਦੇ ਕਿਸੇ ਖਾਸ ਪੱਖ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ। ਸਹੂਲਤ ਲਈ, ਇੱਥੇ ਵੈਕਟਰ ਦੇ ਪਹਿਲੇ 10 ਨੰਬਰ ਦਿੱਤੇ ਗਏ ਹਨ।

```python
[-0.006655829958617687, 0.0026128944009542465, 0.008792596869170666, -0.02446001023054123, -0.008540431968867779, 0.022071078419685364, -0.010703742504119873, 0.003311325330287218, -0.011632772162556648, -0.02187200076878071, ...]
```

## Embedding ਇੰਡੈਕਸ ਕਿਵੇਂ ਬਣਾਇਆ ਜਾਂਦਾ ਹੈ?

ਇਸ ਪਾਠ ਲਈ Embedding ਇੰਡੈਕਸ Python ਸਕ੍ਰਿਪਟਾਂ ਦੀ ਇੱਕ ਲੜੀ ਨਾਲ ਬਣਾਇਆ ਗਿਆ ਸੀ। ਤੁਸੀਂ ਇਹ ਸਕ੍ਰਿਪਟਾਂ ਅਤੇ ਹਦਾਇਤਾਂ [README](./scripts/README.md?WT.mc_id=academic-105485-koreyst) ਵਿੱਚ 'scripts' ਫੋਲਡਰ ਵਿੱਚ ਲੱਭ ਸਕਦੇ ਹੋ। ਤੁਹਾਨੂੰ ਇਹ ਸਕ੍ਰਿਪਟਾਂ ਚਲਾਉਣ ਦੀ ਲੋੜ ਨਹੀਂ ਹੈ ਕਿਉਂਕਿ Embedding ਇੰਡੈਕਸ ਤੁਹਾਡੇ ਲਈ ਪਹਿਲਾਂ ਹੀ ਦਿੱਤਾ ਗਿਆ ਹੈ।

ਸਕ੍ਰਿਪਟਾਂ ਹੇਠਾਂ ਦਿੱਤੇ ਕੰਮ ਕਰਦੀਆਂ ਹਨ:

1. [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1) ਪਲੇਲਿਸਟ ਵਿੱਚ ਹਰ YouTube ਵੀਡੀਓ ਦਾ ਟ੍ਰਾਂਸਕ੍ਰਿਪਟ ਡਾਊਨਲੋਡ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।
2. [OpenAI Functions](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling?WT.mc_id=academic-105485-koreyst) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪਹਿਲੇ 3 ਮਿੰਟਾਂ ਦੇ ਟ੍ਰਾਂਸਕ੍ਰਿਪਟ ਤੋਂ ਸਪੀਕਰ ਦਾ ਨਾਮ ਕੱਢਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਹਰ ਵੀਡੀਓ ਲਈ ਸਪੀਕਰ ਦਾ ਨਾਮ Embedding ਇੰਡੈਕਸ `embedding_index_3m.json` ਵਿੱਚ ਸਟੋਰ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।
3. ਟ੍ਰਾਂਸਕ੍ਰਿਪਟ ਟੈਕਸਟ ਨੂੰ **3 ਮਿੰਟਾਂ ਦੇ ਟੈਕਸਟ ਸੈਗਮੈਂਟਾਂ** ਵਿੱਚ ਵੰਡਿਆ ਜਾਂਦਾ ਹੈ। ਹਰ ਸੈਗਮੈਂਟ ਵਿੱਚ ਅਗਲੇ ਸੈਗਮੈਂਟ ਤੋਂ ਲਗਭਗ 20 ਸ਼ਬਦ ਓਵਰਲੈਪ ਹੁੰਦੇ ਹਨ ਤਾਂ ਜੋ ਸੈਗਮੈਂਟ ਦਾ Embedding ਕੱਟਿਆ ਨਾ ਜਾਵੇ ਅਤੇ ਖੋਜ ਲਈ ਵਧੀਆ ਸੰਦਰਭ ਮਿਲੇ।
4. ਹਰ ਟੈਕਸਟ ਸੈਗਮੈਂਟ ਨੂੰ OpenAI Chat API ਨੂੰ ਭੇਜ ਕੇ 60 ਸ਼ਬਦਾਂ ਵਿੱਚ ਸੰਖੇਪ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। ਇਹ ਸੰਖੇਪ ਵੀ Embedding ਇੰਡੈਕਸ `embedding_index_3m.json` ਵਿੱਚ ਸਟੋਰ ਕੀਤਾ ਜਾਂਦਾ ਹੈ।
5. ਆਖ਼ਿਰ ਵਿੱਚ, ਸੈਗਮੈਂਟ ਟੈਕਸਟ ਨੂੰ OpenAI Embedding API ਨੂੰ ਭੇਜਿਆ ਜਾਂਦਾ ਹੈ। Embedding API 1536 ਨੰਬਰਾਂ ਵਾਲਾ ਵੈਕਟਰ ਵਾਪਸ ਕਰਦਾ ਹੈ ਜੋ ਸੈਗਮੈਂਟ ਦੇ ਸੈਮਾਂਟਿਕ ਮਤਲਬ ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ। ਸੈਗਮੈਂਟ ਅਤੇ OpenAI Embedding ਵੈਕਟਰ Embedding ਇੰਡੈਕਸ `embedding_index_3m.json` ਵਿੱਚ ਸਟੋਰ ਕੀਤੇ ਜਾਂਦੇ ਹਨ।

### ਵੈਕਟਰ ਡੇਟਾਬੇਸ

ਸਿੱਖਣ ਦੀ ਸੌਖਿਆ ਲਈ, Embedding ਇੰਡੈਕਸ ਇੱਕ JSON ਫਾਇਲ `embedding_index_3m.json` ਵਿੱਚ ਸਟੋਰ ਕੀਤਾ ਗਿਆ ਹੈ ਅਤੇ Pandas DataFrame ਵਿੱਚ ਲੋਡ ਕੀਤਾ ਜਾਂਦਾ ਹੈ। ਪਰ ਪ੍ਰੋਡਕਸ਼ਨ ਵਿੱਚ, Embedding ਇੰਡੈਕਸ ਨੂੰ ਵੈਕਟਰ ਡੇਟਾਬੇਸ ਵਿੱਚ ਸਟੋਰ ਕੀਤਾ ਜਾਵੇਗਾ ਜਿਵੇਂ ਕਿ [Azure Cognitive Search](https://learn.microsoft.com/training/modules/improve-search-results-vector-search?WT.mc_id=academic-105485-koreyst), [Redis](https://cookbook.openai.com/examples/vector_databases/redis/readme?WT.mc_id=academic-105485-koreyst), [Pinecone](https://cookbook.openai.com/examples/vector_databases/pinecone/readme?WT.mc_id=academic-105485-koreyst), [Weaviate](https://cookbook.openai.com/examples/vector_databases/weaviate/readme?WT.mc_id=academic-105485-koreyst) ਆਦਿ।

## ਕੋਸਾਈਨ ਸਮਾਨਤਾ ਨੂੰ ਸਮਝਣਾ

ਅਸੀਂ Text embeddings ਬਾਰੇ ਸਿੱਖਿਆ, ਹੁਣ ਅਗਲਾ ਕਦਮ ਹੈ ਕਿ Text embeddings ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਡੇਟਾ ਖੋਜਣਾ ਅਤੇ ਖਾਸ ਕਰਕੇ ਦਿੱਤੇ ਗਏ ਕਵੈਰੀ ਲਈ ਸਭ ਤੋਂ ਮਿਲਦੇ ਜੁਲਦੇ embeddings ਨੂੰ ਕੋਸਾਈਨ ਸਮਾਨਤਾ ਦੀ ਵਰਤੋਂ ਨਾਲ ਲੱਭਣਾ।

### ਕੋਸਾਈਨ ਸਮਾਨਤਾ ਕੀ ਹੈ?

ਕੋਸਾਈਨ ਸਮਾਨਤਾ ਦੋ ਵੈਕਟਰਾਂ ਵਿਚਕਾਰ ਸਮਾਨਤਾ ਦੀ ਮਾਪ ਹੈ, ਇਸਨੂੰ `nearest neighbor search` ਵੀ ਕਿਹਾ ਜਾਂਦਾ ਹੈ। ਕੋਸਾਈਨ ਸਮਾਨਤਾ ਖੋਜ ਕਰਨ ਲਈ ਤੁਹਾਨੂੰ OpenAI Embedding API ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕਵੈਰੀ ਟੈਕਸਟ ਦਾ ਵੈਕਟਰ ਬਣਾਉਣਾ ਪੈਂਦਾ ਹੈ। ਫਿਰ ਕਵੈਰੀ ਵੈਕਟਰ ਅਤੇ Embedding ਇੰਡੈਕਸ ਵਿੱਚ ਹਰ ਵੈਕਟਰ ਵਿਚਕਾਰ ਕੋਸਾਈਨ ਸਮਾਨਤਾ ਦੀ ਗਣਨਾ ਕਰੋ। ਯਾਦ ਰੱਖੋ, Embedding ਇੰਡੈਕਸ ਵਿੱਚ ਹਰ YouTube ਟ੍ਰਾਂਸਕ੍ਰਿਪਟ ਟੈਕਸਟ ਸੈਗਮੈਂਟ ਲਈ ਇੱਕ ਵੈਕਟਰ ਹੁੰਦਾ ਹੈ। ਆਖ਼ਿਰ ਵਿੱਚ, ਨਤੀਜਿਆਂ ਨੂੰ ਕੋਸਾਈਨ ਸਮਾਨਤਾ ਦੇ ਅਧਾਰ 'ਤੇ ਛਾਂਟੋ ਅਤੇ ਸਭ ਤੋਂ ਵੱਧ ਕੋਸਾਈਨ ਸਮਾਨਤਾ ਵਾਲੇ ਟੈਕਸਟ ਸੈਗਮੈਂਟ ਕਵੈਰੀ ਨਾਲ ਸਭ ਤੋਂ ਜ਼ਿਆਦਾ ਮਿਲਦੇ ਹਨ।

ਗਣਿਤੀ ਦ੍ਰਿਸ਼ਟੀਕੋਣ ਤੋਂ, ਕੋਸਾਈਨ ਸਮਾਨਤਾ ਦੋ ਵੈਕਟਰਾਂ ਦੇ ਵਿਚਕਾਰ ਬਹੁ-ਆਯਾਮੀ ਸਪੇਸ ਵਿੱਚ ਕੋਣ ਦਾ ਕੋਸਾਈਨ ਮਾਪਦਾ ਹੈ। ਇਹ ਮਾਪ ਲਾਭਦਾਇਕ ਹੈ ਕਿਉਂਕਿ ਜੇ ਦੋ ਦਸਤਾਵੇਜ਼ Euclidean ਦੂਰੀ ਨਾਲ ਦੂਰ ਹਨ ਪਰ ਉਹਨਾਂ ਦੇ ਵਿਚਕਾਰ ਕੋਣ ਛੋਟਾ ਹੈ ਤਾਂ ਉਹਨਾਂ ਦੀ ਕੋਸਾਈਨ ਸਮਾਨਤਾ ਵੱਧ ਹੋ ਸਕਦੀ ਹੈ। ਕੋਸਾਈਨ ਸਮਾਨਤਾ ਦੇ ਸਮੀਕਰਨਾਂ ਬਾਰੇ ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ ਵੇਖੋ [Cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity?WT.mc_id=academic-105485-koreyst)।

## ਆਪਣੀ ਪਹਿਲੀ ਖੋਜ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣਾ

ਹੁਣ ਅਸੀਂ ਸਿੱਖਾਂਗੇ ਕਿ Embeddings ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਖੋਜ ਐਪਲੀਕੇਸ਼ਨ ਕਿਵੇਂ ਬਣਾਈਏ। ਇਹ ਖੋਜ ਐਪਲੀਕੇਸ਼ਨ ਵਿਦਿਆਰਥੀਆਂ ਨੂੰ ਸਵਾਲ ਲਿਖ ਕੇ ਵੀਡੀਓ ਖੋਜਣ ਦੀ ਆਗਿਆ ਦੇਵੇਗਾ। ਖੋਜ ਐਪਲੀਕੇਸ਼ਨ ਸਵਾਲ ਨਾਲ ਸੰਬੰਧਿਤ ਵੀਡੀਓਜ਼ ਦੀ ਸੂਚੀ ਵਾਪਸ ਕਰੇਗਾ। ਇਹ ਵੀਡੀਓ ਵਿੱਚ ਉਸ ਥਾਂ ਦਾ ਲਿੰਕ ਵੀ ਦੇਵੇਗਾ ਜਿੱਥੇ ਸਵਾਲ ਦਾ ਜਵਾਬ ਹੈ।

ਇਹ ਹੱਲ Windows 11, macOS, ਅਤੇ Ubuntu 22.04 'ਤੇ Python 3.10 ਜਾਂ ਉਸ ਤੋਂ ਬਾਅਦ ਦੇ ਵਰਜਨ ਨਾਲ ਬਣਾਇਆ ਅਤੇ ਟੈਸਟ ਕੀਤਾ ਗਿਆ ਹੈ। ਤੁਸੀਂ Python [python.org](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ਤੋਂ ਡਾਊਨਲੋਡ ਕਰ ਸਕਦੇ ਹੋ।

## ਅਸਾਈਨਮੈਂਟ - ਵਿਦਿਆਰਥੀਆਂ ਲਈ ਖੋਜ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣਾ

ਅਸੀਂ ਇਸ ਪਾਠ ਦੀ ਸ਼ੁਰੂਆਤ ਵਿੱਚ ਆਪਣੇ ਸਟਾਰਟਅਪ ਦਾ ਪਰਿਚਯ ਦਿੱਤਾ ਸੀ। ਹੁਣ ਸਮਾਂ ਹੈ ਕਿ ਵਿਦਿਆਰਥੀਆਂ ਨੂੰ ਆਪਣੀਆਂ ਅਸਾਈਨਮੈਂਟਾਂ ਲਈ ਖੋਜ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ ਲਈ ਸਮਰੱਥ ਬਣਾਇਆ ਜਾਵੇ।

ਇਸ ਅਸਾਈਨਮੈਂਟ ਵਿੱਚ, ਤੁਸੀਂ ਉਹ Azure OpenAI Services ਬਣਾਉਗੇ ਜੋ ਖੋਜ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ ਲਈ ਵਰਤੀ ਜਾਣਗੀਆਂ। ਤੁਸੀਂ ਹੇਠਾਂ ਦਿੱਤੇ Azure OpenAI Services ਬਣਾਉਣਗੇ। ਇਸ ਅਸਾਈਨਮੈਂਟ ਨੂੰ ਪੂਰਾ ਕਰਨ ਲਈ ਤੁਹਾਡੇ ਕੋਲ Azure ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਹੋਣਾ ਜਰੂਰੀ ਹੈ।

### Azure Cloud Shell ਸ਼ੁਰੂ ਕਰੋ

1. [Azure portal](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) ਵਿੱਚ ਸਾਈਨ ਇਨ ਕਰੋ।
2. Azure ਪੋਰਟਲ ਦੇ ਉੱਪਰ-ਸੱਜੇ ਕੋਨੇ ਵਿੱਚ Cloud Shell ਆਈਕਨ ਚੁਣੋ।
3. Environment type ਲਈ **Bash** ਚੁਣੋ।

#### ਰਿਸੋਰਸ ਗਰੁੱਪ ਬਣਾਓ

> ਇਨ੍ਹਾਂ ਹਦਾਇਤਾਂ ਲਈ, ਅਸੀਂ East US ਵਿੱਚ "semantic-video-search" ਨਾਮਕ ਰਿਸੋਰਸ ਗਰੁੱਪ ਦੀ ਵਰਤੋਂ ਕਰ ਰਹੇ ਹਾਂ।
> ਤੁਸੀਂ ਰਿਸੋਰਸ ਗਰੁੱਪ ਦਾ ਨਾਮ ਬਦਲ ਸਕਦੇ ਹੋ, ਪਰ ਜਦੋਂ ਰਿਸੋਰਸਾਂ ਲਈ ਸਥਾਨ ਬਦਲੋ,
> ਤਾਂ [model availability table](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst) ਦੀ ਜਾਂਚ ਕਰੋ।

```shell
az group create --name semantic-video-search --location eastus
```

#### Azure OpenAI Service ਰਿਸੋਰਸ ਬਣਾਓ

Azure Cloud Shell ਤੋਂ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਚਲਾਕੇ Azure OpenAI Service ਰਿਸੋਰਸ ਬਣਾਓ।

```shell
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

#### ਇਸ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਵਰਤੋਂ ਲਈ endpoint ਅਤੇ keys ਪ੍ਰਾਪਤ ਕਰੋ

Azure Cloud Shell ਤੋਂ ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡ ਚਲਾਕੇ Azure OpenAI Service ਰਿਸੋਰਸ ਲਈ endpoint ਅਤੇ keys ਪ੍ਰਾਪਤ ਕਰੋ।

```shell
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

#### OpenAI Embedding ਮਾਡਲ ਡਿਪਲੋਇ ਕਰੋ

Azure Cloud Shell ਤੋਂ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਚਲਾਕੇ OpenAI Embedding ਮਾਡਲ ਡਿਪਲੋਇ ਕਰੋ।

```shell
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name text-embedding-ada-002 \
    --model-name text-embedding-ada-002 \
    --model-version "2"  \
    --model-format OpenAI \
    --sku-capacity 100 --sku-name "Standard"
```

## ਹੱਲ

GitHub Codespaces ਵਿੱਚ [solution notebook

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।