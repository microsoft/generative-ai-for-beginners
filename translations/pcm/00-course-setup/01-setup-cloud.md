# Cloud Setup ☁️ – GitHub Codespaces

**Use dis guide if you no wan install anything for your local machine.**  
Codespaces dey give you free VS Code wey you fit run for browser with all dependencies wey don install before.

---

## 1. Why Codespaces?

| Benefit | Wetin e mean for you |
|---------|----------------------|
| ✅ Zero installs | E dey work for Chromebook, iPad, school lab PCs… |
| ✅ Pre-built dev container | Python 3, Node.js, .NET, Java don already dey inside |
| ✅ Free quota | Personal accounts go get **120 core-hours / 60 GB-hours every month** |

> 💡 **Tip**  
> Make your quota dey okay by **stopping** or **deleting** codespaces wey no dey use  
> (View ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2. Create Codespace (just one click)

1. **Fork** dis repo (top-right **Fork** button).  
2. For your fork, click **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dialog showing buttons to create a codespace](../../../translated_images/pcm/who-will-pay.4c0609b1c7780f44.webp)

✅ Browser VS Code window go open and dev container go start to build.
E go still take **~2 minutes** di first time.

## 3. Add your API key (di safe way)

### Option A Codespaces Secrets — Na di recommended way

1. ⚙️ Gear icon -> Command Pallete-> Codespaces : Manage user secret -> Add new secret.
2. Name: OPENAI_API_KEY
3. Value: paste your key → Add secret

Na so e be—our code go identify am automatically.

### Option B .env file (if na really you need am)

```bash
cp .env.copy .env
code .env         # put for OPENAI_API_KEY=your_key_here
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->