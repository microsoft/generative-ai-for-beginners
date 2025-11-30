<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "be9cef0460b3696ed5d8f6f8d2f64d45",
  "translation_date": "2025-08-26T13:16:35+00:00",
  "source_file": "00-course-setup/01-setup-cloud.md",
  "language_code": "en"
}
-->
# Cloud Setup ☁️ – GitHub Codespaces

**Use this guide if you don’t want to install anything on your computer.**  
Codespaces gives you a free, browser-based VS Code environment with all the tools you need already set up.

---

## 1.  Why use Codespaces?

| Benefit | What it means for you |
|---------|----------------------|
| ✅ No installations needed | Works on Chromebook, iPad, school lab computers… |
| ✅ Ready-to-use dev container | Python 3, Node.js, .NET, Java are all included |
| ✅ Free usage | Personal accounts get **120 core-hours / 60 GB-hours per month** |

> 💡 **Tip**  
> Save your quota by **stopping** or **deleting** codespaces you’re not using  
> (View ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2.  Create a Codespace (just one click)

1. **Fork** this repository (top-right **Fork** button).  
2. In your fork, click **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![ialog showing buttons to create a codespace](../../../00-course-setup/images/who-will-pay.webp)

✅ A VS Code window will open in your browser and the dev container will start setting up.
This usually takes **about 2 minutes** the first time.

## 3. Add your API key (the safe way)

### Option A Codespaces Secrets — Recommended

1. ⚙️ Click the gear icon -> Command Palette -> Codespaces: Manage user secret -> Add a new secret.
2. Name: OPENAI_API_KEY
3. Value: paste your key → Add secret

That’s it—our code will automatically use your key.

### Option B .env file (if you really need one)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

**Disclaimer**:
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.