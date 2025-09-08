<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T16:00:58+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "pa"
}
-->
# ਕਲਾਉਡ ਸੈਟਅੱਪ ☁️ – GitHub Codespaces

**ਇਹ ਗਾਈਡ ਉਨ੍ਹਾਂ ਲਈ ਹੈ ਜੋ ਆਪਣੇ ਕੰਪਿਊਟਰ 'ਤੇ ਕੁਝ ਵੀ ਇੰਸਟਾਲ ਨਹੀਂ ਕਰਨਾ ਚਾਹੁੰਦੇ।**  
Codespaces ਤੁਹਾਨੂੰ ਇੱਕ ਮੁਫ਼ਤ, ਬਰਾਊਜ਼ਰ-ਅਧਾਰਤ VS Code ਇੰਸਟੈਂਸ ਦਿੰਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਸਾਰੀਆਂ ਲੋੜੀਂਦੀਆਂ dependencies ਪਹਿਲਾਂ ਹੀ ਇੰਸਟਾਲ ਹਨ।

---

## 1.  Codespaces ਕਿਉਂ?

| ਫਾਇਦਾ | ਤੁਹਾਡੇ ਲਈ ਇਸਦਾ ਕੀ ਮਤਲਬ |
|---------|----------------------|
| ✅ ਕੋਈ ਇੰਸਟਾਲ ਨਹੀਂ | Chromebook, iPad, ਸਕੂਲ ਲੈਬ PCs 'ਤੇ ਵੀ ਚੱਲਦਾ |
| ✅ Pre-built dev container | Python 3, Node.js, .NET, Java ਪਹਿਲਾਂ ਹੀ ਮੌਜੂਦ |
| ✅ ਮੁਫ਼ਤ quota | Personal accounts ਨੂੰ **120 core-hours / 60 GB-hours ਪ੍ਰਤੀ ਮਹੀਨਾ** ਮਿਲਦੇ ਹਨ |

> 💡 **ਟਿਪ**  
> ਆਪਣਾ quota ਵਧੀਆ ਰੱਖਣ ਲਈ **idle codespaces ਨੂੰ ਰੋਕੋ ਜਾਂ ਹਟਾਓ**  
> (View ▸ Command Palette ▸ *Codespaces: Stop Codespace*)।

---

## 2.  Codespace ਬਣਾਓ (ਇੱਕ ਕਲਿੱਕ 'ਚ)

1. **Fork** ਕਰੋ ਇਹ repo (ਉੱਤੇ-ਸੱਜੇ **Fork** ਬਟਨ 'ਤੇ ਕਲਿੱਕ ਕਰੋ)।  
2. ਆਪਣੇ fork ਵਿੱਚ, **Code ▸ Codespaces ▸ Create codespace on main** 'ਤੇ ਕਲਿੱਕ ਕਰੋ।  
   ![ਡਾਇਲਾਗ ਜਿਸ ਵਿੱਚ codespace ਬਣਾਉਣ ਲਈ ਬਟਨ ਦਿਖਾਏ ਗਏ ਹਨ](../../../00-course-setup/images/who-will-pay.webp)

✅ ਇੱਕ ਬਰਾਊਜ਼ਰ VS Code ਵਿੰਡੋ ਖੁਲਦੀ ਹੈ ਅਤੇ dev container ਬਣਨਾ ਸ਼ੁਰੂ ਹੋ ਜਾਂਦਾ ਹੈ।
ਇਹ ਪਹਿਲੀ ਵਾਰ **ਲਗਭਗ 2 ਮਿੰਟ** ਲੈਂਦਾ ਹੈ।

## 3. ਆਪਣੀ API key ਸ਼ਾਮਲ ਕਰੋ (ਸੁਰੱਖਿਅਤ ਤਰੀਕੇ ਨਾਲ)

### Option A Codespaces Secrets — ਸਿਫ਼ਾਰਸ਼ੀ

1. ⚙️ Gear icon -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Name: OPENAI_API_KEY
3. Value: ਆਪਣੀ key ਪੇਸਟ ਕਰੋ → Add secret

ਇਹੀ ਹੈ—ਸਾਡਾ ਕੋਡ ਇਸਨੂੰ ਆਪਣੇ ਆਪ ਲੈ ਲਵੇਗਾ।

### Option B .env ਫਾਈਲ (ਜੇ ਤੁਹਾਨੂੰ ਵਾਕਈ ਲੋੜ ਹੈ)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**ਅਸਵੀਕਰਨ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਅਸੀਂ ਯਥਾਸੰਭਵ ਸਹੀ ਅਨੁਵਾਦ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਪਰ ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਣਪਛਾਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼, ਜਿਸ ਭਾਸ਼ਾ ਵਿੱਚ ਉਹ ਲਿਖਿਆ ਗਿਆ ਹੈ, ਨੂੰ ਹੀ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਅਰਥ ਲਗਾਉਣ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।