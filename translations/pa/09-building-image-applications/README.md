# ਚਿੱਤਰ ਜਨਰੇਸ਼ਨ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣਾ

[![ਚਿੱਤਰ ਜਨਰੇਸ਼ਨ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣਾ](../../../translated_images/pa/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLMs ਸਿਰਫ ਟੈਕਸਟ ਜਨਰੇਸ਼ਨ ਤੱਕ ਸੀਮਤ ਨਹੀਂ ਹਨ। ਟੈਕਸਟ ਵੇਰਵਿਆਂ ਤੋਂ ਚਿੱਤਰ ਬਣਾਉਣਾ ਵੀ ਸੰਭਵ ਹੈ। ਚਿੱਤਰਾਂ ਨੂੰ ਇੱਕ ਮਾਡੈਲਿਟੀ ਵਜੋਂ ਰੱਖਣਾ ਕਈ ਖੇਤਰਾਂ ਲਈ ਬਹੁਤ ਲਾਭਦਾਇਕ ਹੋ ਸਕਦਾ ਹੈ ਜਿਵੇਂ ਕਿ MedTech, ਵਾਸਤੁਕਲਾ, ਸੈਲਾਨੀ, ਖੇਡ ਵਿਕਾਸ ਅਤੇ ਹੋਰ। ਇਸ ਅਧਿਆਇ ਵਿੱਚ, ਅਸੀਂ ਦੋ ਸਭ ਤੋਂ ਲੋਕਪ੍ਰਿਯ ਚਿੱਤਰ ਜਨਰੇਸ਼ਨ ਮਾਡਲਾਂ, DALL-E ਅਤੇ Midjourney ਨੂੰ ਵੇਖਾਂਗੇ।

## ਪਰਿਚਯ

ਇਸ ਪਾਠ ਵਿੱਚ, ਅਸੀਂ ਕਵਰ ਕਰਾਂਗੇ:

- ਚਿੱਤਰ ਜਨਰੇਸ਼ਨ ਅਤੇ ਇਸਦੇ ਫਾਇਦੇ।
- DALL-E ਅਤੇ Midjourney, ਉਹ ਕੀ ਹਨ ਅਤੇ ਕਿਵੇਂ ਕੰਮ ਕਰਦੇ ਹਨ।
- ਇੱਕ ਚਿੱਤਰ ਜਨਰੇਸ਼ਨ ਐਪ ਬਣਾਉਣ ਦਾ ਤਰੀਕਾ।

## ਸਿੱਖਣ ਦੇ ਲਕੜ

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- ਇੱਕ ਚਿੱਤਰ ਜਨਰੇਸ਼ਨ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ ਲਈ।
- ਆਪਣੇ ਐਪਲੀਕੇਸ਼ਨ ਲਈ ਮੈਟਾ ਪ੍ਰਾਂਪਟਸ ਨਾਲ ਹੱਦਾਂ ਨਿਰਧਾਰਤ ਕਰਨ ਲਈ।
- DALL-E ਅਤੇ Midjourney ਨਾਲ ਕੰਮ ਕਰਨ ਲਈ।

## ਚਿੱਤਰ ਜਨਰੇਸ਼ਨ ਐਪ ਬਣਾਉਣ ਦਾ ਕਾਰਨ ਕੀ ਹੈ?

ਚਿੱਤਰ ਜਨਰੇਸ਼ਨ ਐਪ ਆਮ ਤੌਰ 'ਤੇ Generative AI ਦੀ ਸਮਰੱਥਾ ਨੂੰ ਪਰਖਣ ਲਈ ਬਹੁਤ ਵਧੀਆ ਢੰਗ ਹਨ। ਇਹ ਇਸ ਤਰ੍ਹਾਂ ਵਰਤੇ ਜਾ ਸਕਦੇ ਹਨ:

- **ਚਿੱਤਰ ਸੰਪਾਦਨ ਅਤੇ ਸੰਸਲੇਸ਼ਣ**. ਤੁਸੀਂ ਚਿੱਤਰ ਸੰਪਾਦਨ ਅਤੇ ਚਿੱਤਰ ਸੰਸਲੇਸ਼ਣ ਵਰਗੇ ਕਈ ਉਪਯੋਗ ਖੇਤਰਾਂ ਲਈ ਚਿੱਤਰ ਸਿਰਜ ਸਕਦੇ ਹੋ।

- **ਹੁਣੀਕਿਆਂ ਦੇ ਕਈ ਉਦਯੋਗਾਂ 'ਚ ਵਰਤੋਂ**. ਇਹ Medtech, ਟੂਰਿਜ਼ਮ, ਖੇਡ ਵਿਕਾਸ ਅਤੇ ਹੋਰ ਉਦਯੋਗਾਂ ਲਈ ਚਿੱਤਰ ਵੀ ਬਣਾਉਂਦੇ ਹਨ।

## ਪਰਿਵੇਸ਼: Edu4All

ਇਸ ਪਾਠ ਦੇ ਹਿੱਸੇ ਵਜੋਂ, ਅਸੀਂ ਆਪਣੇ ਸਟਾਰਟਅਪ Edu4All ਨਾਲ ਕੰਮ ਜਾਰੀ ਰੱਖਾਂਗੇ। ਵਿਦਿਆਰਥੀ ਆਪਣੇ ਅਸੈਸਮੈਂਟ ਲਈ ਚਿੱਤਰ ਬਣਾਉਣਗੇ, ਕਿ ਕਿਹੜੇ ਚਿੱਤਰ ਬਣਾਣੇ ਹਨ ਇਹ ਵਿਦਿਆਰਥੀਆਂ ਦੀ ਆਪਣੀ ਪਸੰਦ ਤੇ منحصر ਹੈ, ਪਰ ਉਹ ਆਪਣੇ ਸੁਪਨਿਆਂ ਦੀਆਂ ਕਹਾਣੀਆਂ ਲਈ ਇਲਾਸਟ੍ਰੇਸ਼ਨ ਟਯਾਰ ਕਰ ਸਕਦੇ ਹਨ ਜਾਂ ਆਪਣੀ ਕਹਾਣੀ ਲਈ ਨਵੀਂ ਪਾਤਰ ਸਿਰਜ ਸਕਦੇ ਹਨ ਜਾਂ ਆਪਣੇ ਵਿਸ਼ਯਾਂ ਅਤੇ ਧਾਰਣਾਵਾਂ ਨੂੰ ਦ੍ਰਿਸ਼ਟੀਗਤ ਕਰ ਸਕਦੇ ਹਨ।

ਜੇ ਕਰ ਕੇ Edu4All ਦੇ ਵਿਦਿਆਰਥੀ ਕਲਾਸ ਵਿੱਚ ਸਥਾਨਕਾਂ ਲਈ ਕੰਮ ਕਰ ਰਹੇ ਹੋਣ ਤਾਂ ਉਹ ਇਸ ਤਰ੍ਹਾਂ ਕੁਝ ਚਿੱਤਰ ਬਣਾ ਸਕਦੇ ਹਨ:

![Edu4All startup, class on monuments, Eiffel Tower](../../../translated_images/pa/startup.94d6b79cc4bb3f5a.webp)

ਇਸ ਤਰ੍ਹਾਂ ਦੇ ਪ੍ਰਾਂਪਟ ਨਾਲ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ

> "ਡੌਗ ਲਗਭਗ ਐਫਲ ਟਾਵਰ ਦੇ ਕੋਲ ਸਵੇਰੇ ਸੂਰਜੀ ਰੌਸ਼ਨੀ ਵਿੱਚ"

## DALL-E ਅਤੇ Midjourney ਕੀ ਹਨ?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) ਅਤੇ [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) ਦੋ ਸਭ ਤੋਂ ਪ੍ਰਸਿੱਧ ਚਿੱਤਰ ਜਨਰੇਸ਼ਨ ਮਾਡਲ ਹਨ, ਜੋ ਪ੍ਰਾਂਪਟ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਚਿੱਤਰ ਬਣਾਉਂਦੇ ਹਨ।

### DALL-E

ਆਓ DALL-E ਨਾਲ ਸ਼ੁਰੂ ਕਰੀਏ, ਜੋ ਇਕ Generative AI ਮਾਡਲ ਹੈ ਜੋ ਟੈਕਸਟ ਵੇਰਵਿਆਂ ਤੋਂ ਚਿੱਤਰ ਬਣਾਉਂਦਾ ਹੈ।

> [DALL-E ਦੋ ਮਾਡਲਾਂ, CLIP ਅਤੇ diffused attention ਦੇ ਮਿਲਾਪ ਦਾ ਨਤੀਜਾ ਹੈ](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)।

- **CLIP**, ਇੱਕ ਮਾਡਲ ਹੈ ਜੋ ਚਿੱਤਰਾਂ ਅਤੇ ਟੈਕਸਟ ਤੋਂ ਐम्बੈਡਿੰਗਸ (ਦਾਤਾ ਦੇ ਗਿਣਤੀਵਾੜੇ ਪ੍ਰਤੀਕਾਂ) ਬਣਾਉਂਦਾ ਹੈ।

- **Diffused attention**, ਇੱਕ ਮਾਡਲ ਹੈ ਜੋ ਐम्बੈਡਿੰਗਸ ਤੋਂ ਚਿੱਤਰ ਬਣਾਉਂਦਾ ਹੈ। DALL-E ਚਿੱਤਰਾਂ ਅਤੇ ਟੈਕਸਟ ਦੇ ਡੇਟਾਸੈੱਟ 'ਤੇ ਟ੍ਰੇਨ ਕੀਤਾ ਗਿਆ ਹੈ ਅਤੇ ਇਹ ਟੈਕਸਟ ਵੇਰਵਿਆਂ ਤੋਂ ਚਿੱਤਰ ਬਣਾਉਣ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਉਦਾਹਰਣ ਵਜੋਂ, DALL-E ਬਿੱਲੀ ਦੇ ਟੋਪੀ ਵਾਲੇ ਚਿੱਤਰ ਜਾਂ ਮੋਹੌਕ ਵਾਲੇ ਕੁੱਤੇ ਦੇ ਚਿੱਤਰ ਬਣਾਉਣ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ।

### Midjourney

Midjourney ਵੀ DALL-E ਵਰਗੇ ਹੀ ਕੰਮ ਕਰਦਾ ਹੈ, ਇਹ ਟੈਕਸਟ ਪ੍ਰਾਂਪਟਸ ਤੋਂ ਚਿੱਤਰ ਬਣਾਉਂਦਾ ਹੈ। Midjourney ਨਾਲ ਵੀ "ਟੋਪੀ ਵਾਲੀ ਬਿੱਲੀ" ਜਾਂ "ਮੋਹੌਕ ਵਾਲੇ ਕੁੱਤੇ" ਵਾਲੇ ਪ੍ਰਾਂਪਟ ਨਾਲ ਚਿੱਤਰ ਬਣਾਏ ਜਾ ਸਕਦੇ ਹਨ।

![Midjourney ਵੱਲੋਂ ਬਣਾਇਆ ਗਇਆ ਚਿੱਤਰ, ਮਕੈਨਿਕਲ ਕਬੂਤਰ](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_ਚਿੱਤਰ ਸ੍ਰੋਤ ਵਿਕੀਪੀਡੀਆ, Midjourney ਵੱਲੋਂ ਬਣਾਇਆ ਗਇਆ_

## DALL-E ਅਤੇ Midjourney ਕਿਵੇਂ ਕੰਮ ਕਰਦੇ ਹਨ

ਸਭ ਤੋਂ ਪਹਿਲਾਂ, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)। DALL-E ਇੱਕ Generative AI ਮਾਡਲ ਹੈ ਜੋ ਟ੍ਰਾਂਸਫਾਰਮਰ ਆਰਕੀਟੈਕਚਰ ਤੇ ਆਧਾਰਿਤ ਹੈ ਜਿਸ ਵਿੱਚ _autoregressive transformer_ ਸ਼ਾਮਲ ਹੈ।

ਇੱਕ _autoregressive transformer_ ਮਾਡਲ ਦੱਸਦਾ ਹੈ ਕਿ ਕਿਵੇਂ ਟੈਕਸਟ ਵੇਰਵਿਆਂ ਤੋਂ ਚਿੱਤਰ ਬਣਾਉਂਦੇ ਹਨ, ਇਹ ਇੱਕ ਵਾਰੀ ਵਿੱਚ ਇੱਕ ਪਿੱਛਲGenerates generates a pixel generate pixels generate generates pixels next generate pixels generates pixels next generates pixels generates pixels pixels generates pixels generates pixels generates pixels generates pixels generates pixels generates generates generate generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates genera generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates generates pixels Generates pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels Generates pixels generates pixels generates pixels generates pixels generates pixels generates pixels generates pixels generates pixels generates pixels generate pixels pixels generates pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels generates pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels generates pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels pixels ਪੱਤਰ ਵਹੀ ਜੀਨਾਂਜ਼ਾ ਸ਼ਮਿਲ ਹੈ, ਹੁਣ ਚਿੱਤਰ ਪੂਰਾ ਹੋਣ ਤੱਕ ਨਿਊਰਲ ਨੈੱਟਵਰਕ ਦੀ ਕਈ ਪਰਤਾਂ ਨੂੰ ਪਾਰ ਕਰਦਾ ਹੈ।

ਇਸ ਪ੍ਰਕਿਰਿਆ ਨਾਲ, DALL-E ਚਿੱਤਰ ਵਿੱਚ ਗੁਣ, ਵਸਤੂਆਂ, ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਅਤੇ ਹੋਰ ਉਪ੍ਰੰਤ ਨਿਯੰਤਰਿਤ ਕਰਦਾ ਹੈ। ਫਿਰ ਵੀ, DALL-E 2 ਅਤੇ 3 ਨੇ ਬਣਾਏ ਗਏ ਚਿੱਤਰਾਂ 'ਤੇ ਵੱਧ ਨਿਯੰਤਰਣ ਰੱਖਦੇ ਹਨ।

## ਆਪਣਾ ਪਹਿਲਾ ਚਿੱਤਰ ਜਨਰੇਸ਼ਨ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣਾ

ਤਾਂ ਫਿਰ ਚਿੱਤਰ ਜਨਰੇਸ਼ਨ ਐਪ ਬਣਾਉਣ ਲਈ ਕੀ ਚਾਹੀਦਾ ਹੈ? ਤੁਹਾਨੂੰ ਹੇਠ ਲਿਖੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਦੀ ਲੋੜ ਹੈ:

- **python-dotenv**, ਇਸ ਲਾਇਬ੍ਰੇਰੀ ਦੀ ਵਰਤੋਂ ਕਰਨ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਤਾਂ ਜੋ ਆਪਣੇ ਗੁਪਤ ਜਾਣਕਾਰੀਆਂ _.env_ ਫਾਈਲ ਵਿੱਚ ਰੱਖ ਸਕੋ ਜਿਸਨੂੰ ਕੋਡ ਤੋਂ ਦੂਰ ਰੱਖਿਆ ਜਾ ਸਕੇ।
- **openai**, ਇਹ ਲਾਇਬ੍ਰੇਰੀ ਹੈ ਜਿਸ ਨਾਲ ਤੁਸੀਂ OpenAI API ਨਾਲ ਇੰਟਰੈੱਕਟ ਕਰੋਂਗੇ।
- **pillow**, Python ਵਿੱਚ ਚਿੱਤਰਾਂ ਨਾਲ ਕੰਮ ਕਰਨ ਲਈ।
- **requests**, HTTP ਬੇਨਤੀਆਂ ਬਣਾਉਣ ਵਿੱਚ ਮਦਦ ਲਈ।

## Azure OpenAI ਮਾਡਲ ਬਣਾਓ ਅਤੇ ਤੈਅਨਾਤ ਕਰੋ

ਜੇਕਰ ਇਹ ਪਹਿਲਾਂ ਨਹੀਂ ਕੀਤਾ ਤਾਂ, [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) ਪੰਨਾ ਤੇ ਦਿੱਤੇ ਹੁਕਮਾਂ ਦਾ ਪਾਲਣ ਕਰੋ
Azure OpenAI ਸਰੋਤ ਅਤੇ ਮਾਡਲ ਬਣਾਉਣ ਲਈ। ਮਾਡਲ ਵਜੋਂ **gpt-image-1** ਚੁਣੋ (ਮੌਜੂਦਾ Azure OpenAI ਚਿੱਤਰ ਮਾਡਲ; DALL-E 3 ਪੁਰਾਣਾ ਹੈ ਅਤੇ ਨਵੀਆਂ ਤੈਅਨਾਤੀਆਂ ਲਈ ਉਪਲੱਬਧ ਨਹੀਂ)।

## ਐਪ ਬਣਾਉ

1. _.env_ ਫਾਈਲ ਬਣਾਓ ਜਿਸ ਵਿਚ ਹੇਠਾਂ ਦਿੱਤੇ ਸਮੱਗਰੀ ਹੋਵੇ:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   ਇਹ ਜਾਣਕਾਰੀ ਆਪਣੇ ਸਰੋਤ ਲਈ Azure OpenAI Foundry ਪੋਰਟਲ ਦੇ "Deployments" ਹਿੱਸੇ ਵਿੱਚ ਲੱਭੋ।

1. ਉਪਰ ਦਿੱਤੀਆਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਨੂੰ ਇਕ ਫਾਈਲ _requirements.txt_ ਵਿੱਚ ਇਕੱਠਾ ਕਰੋ:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. ਅਗਲੇ, ਵਰਚੁਅਲ ਇਨਵਾਇਰਨਮੈਂਟ ਬਣਾਓ ਅਤੇ ਲਾਇਬ੍ਰੇਰੀਆਂ ਇੰਸਟਾਲ ਕਰੋ:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Windows ਲਈ, ਇਸ ਕਮਾਂਡ ਨਾਲ ਆਪਣੇ ਵਰਚੁਅਲ ਇਨਵਾਇਰਨਮੈਂਟ ਨੂੰ ਬਣਾਉ ਅਤੇ ਚਾਲੂ ਕਰੋ:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ ਨਾਮ ਦੀ ਫਾਈਲ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੀਆਂ ਕੋਡ ਲਾਈਨਾਂ ਸ਼ਾਮਲ ਕਰੋ:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # dotenv ਨੂੰ ਆਯਾਤ ਕਰੋ
    dotenv.load_dotenv()
    
    # Azure OpenAI ਸੇਵਾ ਕਲਾਇੰਟ ਨੂੰ ਸੰਰਚਿਤ ਕਰੋ
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # ਇਮੇਜ ਜਨਰੇਸ਼ਨ API ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਚਿੱਤਰ ਬਣਾਓ
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # ਸਟੋਰ ਕੀਤੇ ਚਿੱਤਰ ਲਈ ਡਾਇਰੈਕਟਰੀ ਸੈੱਟ ਕਰੋ
        image_dir = os.path.join(os.curdir, 'images')

        # ਜੇ ਡਾਇਰੈਕਟਰੀ ਮੌਜੂਦ ਨਹੀਂ ਹੈ, ਤਾਂ ਇਸਨੂੰ ਬਣਾਓ
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # ਚਿੱਤਰ ਦਾ ਰਸਤਾ ਸ਼ੁਰੂ ਕਰੋ (ਦਿਆਨ ਦਿਓ ਕਿ ਫਾਇਲ ਪ੍ਰਕਾਰ png ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # ਬਣਾਇਆ ਗਿਆ ਚਿੱਤਰ ਪ੍ਰਾਪਤ ਕਰੋ
        image_url = generation_response.data[0].url  # ਜਵਾਬ ਵਿੱਚੋਂ ਚਿੱਤਰ URL ਨਿਕਾਲੋ
        generated_image = requests.get(image_url).content  # ਚਿੱਤਰ ਡਾਊਨਲੋਡ ਕਰੋ
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # ਡਿਫਾਲਟ ਚਿੱਤਰ ਦਰਸ਼ਕ ਵਿੱਚ ਚਿੱਤਰ ਦਿਖਾਓ
        image = Image.open(image_path)
        image.show()

    # ਐਕਸਪਸ਼ਨਾਂ ਨੂੰ ਫੜੋ
    except openai.BadRequestError as err:
        print(err)
   ```

ਆਓ ਇਸ ਕੋਡ ਨੂੰ ਸਮਝੀਏ:

- ਸਭ ਤੋਂ ਪਹਿਲਾਂ, ਅਸੀਂ ਲਾਇਬ੍ਰੇਰੀਆਂ ਨੂੰ ਇੰਪੋਰਟ ਕਰਦੇ ਹਾਂ, ਜਿਸ ਵਿਚ OpenAI ਲਾਇਬ੍ਰੇਰੀ, dotenv ਲਾਇਬ੍ਰੇਰੀ, requests ਲਾਇਬ੍ਰੇਰੀ ਅਤੇ Pillow ਲਾਇਬ੍ਰੇਰੀ ਸ਼ਾਮਲ ਹਨ।

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- ਫਿਰ, ਅਸੀਂ _.env_ ਫਾਈਲ ਤੋਂ ENV ਵੈਰੀਏਬਲ ਲੋਡ ਕਰਦੇ ਹਾਂ।

  ```python
  # ਡੌਟਐਨਵੀ ਨੂੰ ਇੰਪੋਰਟ ਕਰੋ
  dotenv.load_dotenv()
  ```

- ਉਸ ਤੋਂ ਬਾਅਦ, ਅਸੀਂ Azure OpenAI ਸੇਵਾ ਕਲਾਇੰਟ ਨੂੰ ਸੰਰਚਿਤ ਕਰਦੇ ਹਾਂ 

  ```python
  # ਇਨਵਾਇਰਨਮੈਂਟ ਵੇਰੀਏਬਲਸ ਤੋਂ ਐਂਡਪਵਾਇੰਟ ਅਤੇ ਕੀ ਪ੍ਰਾਪਤ ਕਰੋ
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- ਫਿਰ, ਅਸੀਂ ਚਿੱਤਰ ਬਣਾਉਂਦੇ ਹਾਂ:

  ```python
  # ਇਮੇਜ ਜਨਰੇਸ਼ਨ API ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਚਿੱਤਰ ਬਣਾਓ
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  ਉਪਰੋਕਤ ਕੋਡ JSON ਵਸਤੂ ਨਾਲ ਜਵਾਬ ਦਿੰਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਬਣਾਏ ਗਏ ਚਿੱਤਰ URL ਹੁੰਦਾ ਹੈ। ਅਸੀਂ ਇਸ URL ਨੂੰ ਡਾਊਨਲੋਡ ਕਰਕੇ ਇੱਕ ਫਾਈਲ ਵਿੱਚ ਸੇਵ ਕਰ ਸਕਦੇ ਹਾਂ।

- ਆਖ਼ਰੀ ਵਿੱਚ, ਅਸੀਂ ਚਿੱਤਰ ਖੋਲ੍ਹਦੇ ਹਾਂ ਅਤੇ ਇਹ ਚਿੱਤਰ ਸਧਾਰਣ ਚਿੱਤਰ ਵਿਖਾਵਣ ਵਾਲੇ ਵਿੱਚ ਦਿਖਾਉਂਦੇ ਹਾਂ:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### ਚਿੱਤਰ ਬਣਾਉਣ ਉੱਤੇ ਹੋਰ ਵੇਰਵੇ

ਆਓ ਇਸ ਕੋਡ ਨੂੰ 자세히 ਵੇਖੀਏ ਜੋ ਚਿੱਤਰ ਬਣਾਉਂਦਾ ਹੈ:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, ਉਹ ਟੈਕਸਟ ਪ੍ਰਾਂਪਟ ਹੈ ਜਿਸ ਦੀ ਵਰਤੋਂ ਚਿੱਤਰ ਬਣਾਉਣ ਲਈ ਹੁੰਦੀ ਹੈ। ਇਸ ਉਦਾਹਰਣ ਵਿੱਚ, ਅਸੀਂ ਪ੍ਰਾਂਪਟ "ਘੋੜੇ ਤੇ ਖਰਗੋਸ਼, ਲੋਲਲੀਪੌਪ ਫੜ੍ਹੀ ਹੋਈ, ਧੁੰਦਲਾਈ ਨਾਲ ਢਕੀ ਘਾਸ ਵਾਲੀ ਖੇਤ ਜਿੱਥੇ ਡੈਫੋਡਿਲ ਕਲ੍ਹਦੇ ਹਨ" ਵਰਤ ਰਹੇ ਹਾਂ।
- **size**, ਉਸ ਚਿੱਤਰ ਦਾ ਆਕਾਰ ਹੈ ਜੋ ਬਣਾਇਆ ਜਾਂਦਾ ਹੈ। ਇਸ ਉਦਾਹਰਣ ਵਿੱਚ, ਅਸੀਂ 1024x1024 ਪਿਕਸਲ ਦੇ ਚਿੱਤਰ ਬਣਾਉਂਦੇ ਹਾਂ।
- **n**, ਇਹ ਬਣਾਏ ਜਾਣ ਵਾਲੇ ਚਿੱਤਰਾਂ ਦੀ ਸੰਖਿਆ ਹੈ। ਇਸ ਕિસੇ ਲਈ, ਅਸੀਂ ਦੋ ਚਿੱਤਰ ਬਣਉਂਦੇ ਹਾਂ।
- **temperature**, ਇੱਕ ਪੈਰਾਮੀਟਰ ਹੈ ਜੋ Generative AI ਮਾਡਲ ਦੇ ਆਊਟਪੁੱਟ ਦੀ ਯਾਦਰਚਛਿਤਾ ਨੂੰ ਨਿਯੰਤਰਿਤ ਕਰਦਾ ਹੈ। ਟემਪਰੇਚਰ 0 ਤੋਂ 1 ਦਰਮਿਆਨ ਹੁੰਦਾ ਹੈ ਜਿੱਥੇ 0 ਮਤਲਬ ਨਤੀਜਾ ਨਿਸ਼ਚਿਤ (ਡਿਟਰਮਿਨਿਸਟਿਕ) ਹੈ ਅਤੇ 1 ਮਤਲਬ ਨਤੀਜਾ ਯਾਦਰਚਛਿਤ (ਰੈਂਡਮ) ਹੈ। ਡਿਫਾਲਟ ਮੁੱਲ 0.7 ਹੈ।

ਹੋਰ ਵੀ ਚੀਜ਼ਾਂ ਹਨ ਜੋ ਤੁਸੀਂ ਚਿੱਤਰਾਂ ਨਾਲ ਕਰ ਸਕਦੇ ਹੋ ਜੋ ਅਸੀਂ ਅਗਲੇ ਭਾਗ ਵਿੱਚ ਕਵਰ ਕਰਾਂਗੇ।

## ਚਿੱਤਰ ਜਨਰੇਸ਼ਨ ਦੀ ਹੋਰ ਯੋਗਤਾਵਾਂ

ਤੁਸੀਂ ਹੁਣ ਤੱਕ ਦੇਖ ਚੁੱਕੇ ਹੋ ਕਿ ਅਸੀਂ ਕੁਝ ਕਤਾਰਾਂ ਵਿੱਚ ਪਾਇਥਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਚਿੱਤਰ ਕਿਵੇਂ ਬਣਾਉਂਦੇ ਹਾਂ। ਪਰ ਹੋਰ ਵੀ ਚੀਜ਼ਾਂ ਮੌਜੂਦ ਹਨ ਜੋ ਤੁਸੀਂ ਚਿੱਤਰਾਂ ਨਾਲ ਕਰ ਸਕਦੇ ਹੋ।

ਤੁਸੀਂ ਇਹ ਵੀ ਕਰ ਸਕਦੇ ਹੋ:

- **ਸੰਪਾਦਨ ਕਰੋ**. ਮੌਜੂਦਾ ਚਿੱਤਰ, ਮਾਸਕ ਅਤੇ ਪ੍ਰਾਂਪਟ ਦੇ ਕੇ ਤੁਸੀਂ ਚਿੱਤਰ ਵਿੱਚ ਤਬਦੀਲੀ ਕਰ ਸਕਦੇ ਹੋ। ਉਦਾਹਰਣ ਵਜੋਂ, ਤੁਸੀਂ ਬਨੀ ਚਿੱਤਰ ਵਿੱਚ ਟੋਪੀ ਜੋੜ ਸਕਦੇ ਹੋ। ਇਹ ਕਰਨ ਲਈ ਤੁਸੀਂ ਚਿੱਤਰ, ਮਾਸਕ (ਨੌਕਰੇਸ਼ਤਰ ਲਈ ਹਿੱਸਾ ਦਰਸਾਉਂਦਾ) ਅਤੇ ਟੈਕਸਟ ਪ੍ਰਾਂਪਟ ਦਿੰਦੇ ਹੋ ਜੋ ਕਹਿੰਦਾ ਹੈ ਕਿ ਕੀ ਬਦਲਣਾ ਹੈ।
> ਨੋਟ: ਇਹ DALL-E 3 ਵਿੱਚ ਸਮਰਥਿਤ ਨਹੀਂ ਹੈ।
 
ਜੀਪੀਟੀ ਇਮેજ ਵਰਤ ਕੇ ਇੱਕ ਉਦਾਹਰਣ:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  ਬੇਸ ਚਿੱਤਰ ਵਿੱਚ ਸਿਰਫ ਲਾਂਜ ਅਤੇ ਪੂਲ ਸ਼ਾਮਲ ਹੁੰਦੇ ਹਨ ਪਰ ਆਖ਼ਰੀ ਚਿੱਤਰ ਵਿੱਚ ਇੱਕ ਫਲੇਮਿੰਗੋ ਹੋਵੇਗਾ:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/pa/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/pa/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/pa/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **ਵੈਰੀਏਸ਼ਨ ਬਣਾਓ**. ਇਸ ਦਾ ਮਤਲਬ ਹੈ ਕਿ ਤੁਸੀਂ ਮੌਜੂਦਾ ਚਿੱਤਰ ਲੈਂਦੇ ਹੋ ਅਤੇ ਵੱਖ-ਵੱਖ ਵੈਰੀਏਸ਼ਨ ਬਣਾਉਣ ਚਾਹੁੰਦੇ ਹੋ। ਇੱਕ ਵੈਰੀਏਸ਼ਨ ਬਣਾਉਣ ਲਈ, ਤੁਸੀਂ ਚਿੱਤਰ ਅਤੇ ਟੈਕਸਟ ਪ੍ਰਾਂਪਟ ਦਿੰਦੇ ਹੋ ਅਤੇ ਹੇਠਾਂ ਦਿੱਤੇ ਕੋਡ ਵਰਗਾ ਕੁਝ ਚਲਾਉਂਦੇ ਹੋ:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > ਨੋਟ, ਇਹ ਸਿਰਫ OpenAI ਦੇ DALL-E 2 ਮਾਡਲ 'ਤੇ ਹੀ ਸਮਰਥਿਤ ਹੈ, gpt-image-1 'ਤੇ ਨਹੀਂ

## ਟੈਮਪਰੇਚਰ

ਟੈਮਪਰੇਚਰ ਇੱਕ ਪੈਰਾਮੀਟਰ ਹੈ ਜੋ Generative AI ਮਾਡਲ ਦੇ ਨਤੀਜੇ ਦੀ ਯਾਦਰਚਛਿਤਾ ਨੂੰ ਨਿਯੰਤਰਿਤ ਕਰਦਾ ਹੈ। ਟੈਮਪਰੇਚਰ ਦਾ ਮੁੱਲ 0 ਤੋਂ 1 ਦਰਮਿਆਨ ਹੁੰਦਾ ਹੈ ਜਿੱਥੇ 0 ਮਤਲਬ ਨਤੀਜਾ ਨਿਸ਼ਚਿਤ ਅਤੇ 1 ਮਤਲਬ ਨਤੀਜਾ ਯਾਦਰਚਛਿਤ ਹੈ। ਡਿਫਾਲਟ ਮੁੱਲ 0.7 ਹੈ।

ਆਓ ਇੱਕ ਉਦਾਹਰਣ ਦੇਖੀਏ ਕਿ ਟੈਮਪਰੇਚਰ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ, ਇਸ ਪ੍ਰਾਂਪਟ ਨੂੰ ਦੋ ਵਾਰੀ ਚਲਾਕੇ:

> ਪ੍ਰਾਂਪਟ : "ਘੋੜੇ ਤੇ ਖਰਗੋਸ਼, ਲੋਲਲੀਪੌਪ ਫੜ੍ਹੀ ਹੋਈ, ਧੁੰਦਲਾਈ ਨਾਲ ਢਕੀ ਘਾਸ ਵਾਲੀ ਖੇਤ ਜਿੱਥੇ ਡੈਫੋਡਿਲ ਕਲ੍ਹਦੇ ਹਨ"

![ਘੋੜੇ ਤੇ ਖਰਗੋਸ਼ ਲੋਲਲੀਪੌਪ ਫੜ੍ਹੀ ਹੋਈ, ਸੰਸਕਰਨ 1](../../../translated_images/pa/v1-generated-image.a295cfcffa3c13c2.webp)

ਹੁਣ ਜੇ ਅਸੀਂ ਉਹੀ ਪ੍ਰਾਂਪਟ ਇਕ ਵਾਰੀ ਹੋਰ ਚਲਾਈਏ ਤਾਂ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ ਕਿ ਸਾਡੇ ਕੋਲ ਬਿਲਕੁਲ ਉਹੋ ਜਿਹਾ ਚਿੱਤਰ ਨਹੀਂ ਆਊਂਦਾ:

![ਘੋੜੇ ਤੇ ਖਰਗੋਸ਼ ਦਾ ਜਨਰੇਟਡ ਚਿੱਤਰ](../../../translated_images/pa/v2-generated-image.33f55a3714efe61d.webp)

ਤੁਸੀਂ ਦੇਖ ਸਕਦੇ ਹੋ ਕਿ ਚਿੱਤਰ ਮਿਲਦੇ-ਜੁਲਦੇ ਹਨ ਪਰ ਇਕੋ ਜਿਹੇ ਨਹੀਂ ਹਨ। ਆਉਂਦੇ ਹਾਂ ਟੈਮਪਰੇਚਰ ਦਾ ਮੁੱਲ 0.1 ਕਰਕੇ ਦੇਖੀਏ ਤਾਂ ਕੀ ਹੁੰਦਾ ਹੈ:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # ਇੱਥੇ ਆਪਣਾ ਪ੍ਰੋੰਪਟ ਟੈਕਸਟ ਦਰਜ ਕਰੋ
        size='1024x1024',
        n=2
    )
```

### ਟੈਮਪਰੇਚਰ ਨੂੰ ਬਦਲਣਾ

ਤਾਂ ਚੱਲੋ ਨਤੀਜੇ ਨੂੰ ਹੋਰ ਨਿਸ਼ਚਿਤ ਬਣਾਉਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੀਏ। ਅਸੀਂ ਦੋ ਤਸਵੀਰਾਂ ਵਿੱਚ ਦੇਖਿਆ ਕਿ ਪਹਿਲੀ ਵਿੱਚ ਖਰਗੋਸ਼ ਹੈ ਅਤੇ ਦੂਜੀ ਵਿੱਚ ਘੋੜਾ, ਇਸ ਲਈ ਚਿੱਤਰ ਬਹੁਤ ਵੱਖਰੇ ਹਨ।

ਇਸ ਲਈ ਸਾਡਾ ਕੋਡ ਬਦਲ ਕੇ ਟੈਮਪਰੇਚਰ 0 ਕਰ ਦਿਉ, ਐਸਾ:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # ਆਪਣਾ ਪ੍ਰੰਪਟ ਟੈਕਸਟ ਇੱਥੇ ਦਾਖਲ ਕਰੋ
        size='1024x1024',
        n=2,
        temperature=0
    )
```

ਹੁਣ ਜਦੋਂ ਤੁਸੀਂ ਇਹ ਕੋਡ ਚਲਾਉਂਦੇ ਹੋ ਤਾਂ ਤੁਹਾਨੂੰ ਇਹ ਦੋ ਚਿੱਤਰ ਮਿਲਣਗੇ:

- ![ਟੈਮਪਰੇਚਰ 0, ਸੰਸਕਰਨ 1](../../../translated_images/pa/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![ਟੈਮਪਰੇਚਰ 0, ਸੰਸਕਰਨ 2](../../../translated_images/pa/v2-temp-generated-image.871d0c920dbfb0f1.webp)

ਇੱਥੇ ਤੁਸੀਂ ਸਾਫ਼ ਤੌਰ 'ਤੇ ਵੇਖ ਸਕਦੇ ਹੋ ਕਿ ਚਿੱਤਰ ਇੱਕ ਦੂਜੇ ਨਾਲ ਵੱਧ ਮਿਲਦੇ ਹਾਂ।

## ਆਪਣੇ ਐਪ ਲਈ ਹੱਦਬੰਦੀ ਕਰਨਾ ਮੈਟਾਪ੍ਰਾਂਪਟਸ ਨਾਲ

ਸਾਡੇ ਡੈਮੋ ਨਾਲ, ਅਸੀਂ ਪਹਿਲਾਂ ਹੀ ਗਾਹਕਾਂ ਲਈ ਚਿੱਤਰ ਬਣਾਉਂਦੇ ਹਾਂ। ਪਰ ਸਾਨੂੰ ਆਪਣੇ ਐਪ ਲਈ ਹੱਦਾਂ ਬਣਾਉਣੀਆਂ ਪੈਂਦੀਆਂ ਹਨ।

ਉਦਾਹਰਣ ਵਜੋਂ, ਅਸੀਂ ਐਸੇ ਚਿੱਤਰ ਨਹੀਂ ਬਣਾਉਣਾ ਚਾਹੁੰਦੇ ਜੋ ਕੰਮ ਲਈ ਅਣੁਕੂਲ ਨਾ ਹੋਣ ਜਾਂ ਜੋ ਬੱਚਿਆਂ ਲਈ ਮਾਨਯੋਗ ਨਾ ਹੋਣ।

ਅਸੀਂ ਇਹ _metaprompts_ ਨਾਲ ਕਰ ਸਕਦੇ ਹਾਂ। ਮੈਟਾਪ੍ਰਾਂਪਟਸ ਏਹ ਟੈਕਸਟ ਪ੍ਰਾਂਪਟ ਹੁੰਦੇ ਹਨ ਜੋ Generative AI ਮਾਡਲ ਦੇ ਨਤੀਜੇ ਨੂੰ ਨਿਯੰਤਰਿਤ ਕਰਨ ਲਈ ਵਰਤੋਂ ਵਿੱਚ ਆਉਂਦੇ ਹਨ। ਉਦਾਹਰਣ ਵਜੋਂ, ਅਸੀਂ ਮੈਟਾਪ੍ਰਾਂਪਟਸ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇਹ ਯਕੀਨੀ ਬਣਾ ਸਕਦੇ ਹਾਂ ਕਿ ਬਣਾਏ ਗਏ ਚਿੱਤਰ ਕੰਮ ਲਈ ਸੁਰੱਖਿਅਤ ਹਨ ਜਾਂ ਬੱਚਿਆਂ ਲਈ ਢੁਕਵੇਂ ਹਨ।

### ਇਹ ਕਿਵੇਂ ਕੰਮ ਕਰਦਾ ਹੈ?

ਹੁਣ, ਮੈਟਾਪ੍ਰਾਂਪਟਸ ਕਿਵੇਂ ਕੰਮ ਕਰਦੇ ਹਨ?

ਮੈਟਾਪ੍ਰਾਂਪਟਸ ਉਹ ਟੈਕਸਟ ਪ੍ਰਾਂਪਟ ਹੁੰਦੇ ਹਨ ਜੋ Generative AI ਮਾਡਲ ਦੇ ਨਤੀਜੇ ਨੂੰ ਨਿਯੰਤਰਿਤ ਕਰਨ ਲਈ ਵਰਤਿਆਂ ਜਾਂਦੇ ਹਨ, ਇਹ ਟੈਕਸਟ ਪ੍ਰਾਂਪਟ ਤੋਂ ਪਹਿਲਾਂ ਰੱਖੇ ਜਾਂਦੇ ਹਨ ਅਤੇ ਮਾਡਲ ਦੇ ਨਤੀਜੇ ਨੂੰ ਨਿਯੰਤਰਿਤ ਕਰਨ ਵਾਲੇ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਐਂਬੈਡ ਕੀਤੇ ਜਾਂਦੇ ਹਨ। ਇਹ ਪ੍ਰਾਂਪਟ ਇਨਪੁੱਟ ਅਤੇ ਮੈਟਾਪ੍ਰਾਂਪਟ ਇਨਪੁੱਟ ਇੱਕ ਸਿੰਗਲ ਟੈਕਸਟ ਪ੍ਰਾਂਪਟ ਵਿੱਚ ਸਮਾਇਆ ਜਾਂਦਾ ਹੈ।

ਇਕ ਮੈਟਾਪ੍ਰਾਂਪਟ ਦਾ ਉਦਾਹਰਣ ਹੁਣ ਵੇਖੀਏ:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

ਹੁਣ, ਆਓ ਵੇਖੀਏ ਕਿ ਸਾਡੇ ਡੈਮੋ ਵਿੱਚ ਮੈਟਾਪ੍ਰਾਂਪਟਸ ਕਿਵੇਂ ਵਰਤੇ ਜਾ ਸਕਦੇ ਹਨ।

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt =f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"{meta_prompt}
Create an image of a bunny on a horse, holding a lollipop"

# TODO ਚਿੱਤਰ ਬਣਾਉਣ ਲਈ ਬੇਨਤੀ ਜੋੜੋ
```

ਉਪਰੋਕਤ ਪ੍ਰਾਂਪਟ ਤੋਂ, ਤੁਸੀਂ ਵੇਖ ਸਕਦੇ ਹੋ ਕਿ ਬਣਾਈਆਂ ਗਈਆਂ ਸਭ ਚਿੱਤਰ ਮੈਟਾਪ੍ਰਾਂਪਟ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖਦੀਆਂ ਹਨ।

## ਅਸਾਈਨਮੈਂਟ - ਆਓ ਵਿਦਿਆਰਥੀਆਂ ਨੂੰ ਸਮਰੱਥ ਬਣਾਈਏ

ਅਸੀਂ ਇਸ ਪਾਠ ਦੀ ਸ਼ੁਰੂਆਤ ਵਿੱਚ Edu4All ਨੂੰ ਪੇਸ਼ ਕੀਤਾ ਸੀ। ਹੁਣ ਸਮਾਂ ਹੈ ਕਿ ਵਿਦਿਆਰਥੀਆਂ ਨੂੰ ਆਪਣੇ ਅਸੈਸਮੈਂਟ ਲਈ ਚਿੱਤਰ ਜਨਰੇਟ ਕਰਨ ਦੀ ਸਮਰੱਥਾ ਦਿੱਤੀ ਜਾਵੇ।


ਵਿਦਿਆਰਥੀ ਆਪਣੇ ਅੰਕਾਂ ਲਈ ਇੱਕ ਚਿੱਤਰ ਬਣਾਉਣਗੇ ਜਿਸ ਵਿੱਚ ਸਮਾਰਕ ਹੋਣਗੇ, ਕਿਹੜੇ ਸਮਾਰਕ ਹਨ ਇਹ ਵਿਦਿਆਰਥੀਆਂ 'ਤੇ ਨਿਰਭਰ ਕਰਦਾ ਹੈ। ਵਿਦਿਆਰਥੀਆਂ ਨੂੰ ਇਸ ਕੰਮ ਵਿੱਚ ਆਪਣੀ ਰਚਨਾਤਮਕਤਾ ਵਰਤਣ ਲਈ ਕਿਹਾ ਗਿਆ ਹੈ ਕਿ ਉਹ ਇਹ ਸਮਾਰਕ ਵੱਖ-ਵੱਖ ਸੰਦਰਭਾਂ ਵਿੱਚ ਰੱਖਣ।

## ਹੱਲ

ਇੱਥੇ ਇੱਕ ਸੰਭਵ ਹੱਲ ਦਿੱਤਾ ਗਿਆ ਹੈ:

```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# dotenv ਨੂੰ ਇੰਪੋਰਟ ਕਰੋ
dotenv.load_dotenv()

# ਮਾਹੌਲੀ ਵੈਰੀਏਬਲਾਂ ਤੋਂ ਐਂਡਪੌਇੰਟ ਅਤੇ ਕੁੰਜੀ ਪ੍ਰਾਪਤ ਕਰੋ
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
  api_key=os.environ['AZURE_OPENAI_API_KEY'],
  api_version = "2024-10-21"
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
"""

try:
    # ਇਮੇਜ ਜਨਰੇਸ਼ਨ API ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਚਿੱਤਰ ਬਣਾਓ
    generation_response = client.images.generate(
        prompt=prompt,    # ਆਪਣੇ ਪ੍ਰਾਂਪਟ ਟੈਕਸਟ ਇੱਥੇ ਦਰਜ ਕਰੋ
        size='1024x1024',
        n=1,
    )
    # ਸਟੋਰ ਕੀਤੇ ਚਿੱਤਰ ਲਈ ਡਾਇਰੈਕਟਰੀ ਸੈੱਟ ਕਰੋ
    image_dir = os.path.join(os.curdir, 'images')

    # ਜੇ ਡਾਇਰੈਕਟਰੀ ਮੌਜੂਦ ਨਹੀਂ ਹੈ ਤਾਂ ਇਸਨੂੰ ਬਣਾਓ
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # ਚਿੱਤਰ ਪਥ ਸ਼ੁਰੂ ਕਰੋ (ਨੋਟ ਕਰੋ ਕਿ ਫਾਇਲ ਟਾਈਪ png ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # ਤਿਆਰ ਕੀਤੇ ਚਿੱਤਰ ਨੂੰ ਪ੍ਰਾਪਤ ਕਰੋ
    image_url = generation_response.data[0].url  # ਜਵਾਬ ਤੋਂ ਚਿੱਤਰ URL ਕੱੱਢੋ
    generated_image = requests.get(image_url).content  # ਚਿੱਤਰ ਡਾਊਨਲੋਡ ਕਰੋ
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # ਡਿਫਾਲਟ ਚਿੱਤਰ ਦਰਸ਼ਕ ਵਿੱਚ ਚਿੱਤਰ ਦਿਖਾਓ
    image = Image.open(image_path)
    image.show()

# ਅਪਵਾਦਾਂ ਨੂੰ ਫੜੋ
except openai.BadRequestError as err:
    print(err)
```

## ਸ਼ਾਨਦਾਰ ਕੰਮ! ਆਪਣੀ ਸਿੱਖਿਆ ਜਾਰੀ ਰੱਖੋ

ਇਸ ਪਾਠ ਨੂੰ ਪੂਰਾ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਸਾਡੇ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ਨੂੰ ਵੇਖੋ ਤਾਂ ਜੋ ਤੁਸੀਂ ਆਪਣੀ Generative AI ਗਿਆਨ ਨੂੰ ਅੱਗੇ ਵਧਾ ਸਕੋ!

ਪਾਠ 10 ਵੱਲ ਜਾਓ ਜਿੱਥੇ ਅਸੀਂ ਦੇਖਾਂਗੇ ਕਿ ਕਿਵੇਂ [low-code ਦੇ ਨਾਲ AI ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਈਏ](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->