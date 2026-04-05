# Cloud Setup ☁️ – GitHub Codespaces

**Use dis guide if you no wan install anytin for ya computer.**  
Codespaces go give you free VS Code wey dey work for browser, wit all di tins wey you need don already dey inside.

---

## 1.  Why Codespaces?

| Benefit | Wetin e mean for you |
|---------|----------------------|
| ✅ No need to install anytin | E go work for Chromebook, iPad, school lab PCs… |
| ✅ Dev container don already dey set | Python 3, Node.js, .NET, Java don dey inside am |
| ✅ Free quota | Personal accounts dey get **120 core-hours / 60 GB-hours per month** |

> 💡 **Tip**  
> Make sure say you no dey waste ya quota by **stopping** or **deleting** codespaces wey you no dey use again  
> (View ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2.  Create Codespace (just one click)

1. **Fork** dis repo (top-right **Fork** button).  
2. For ya fork, click **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![ialog showing buttons to create a codespace](../../../00-course-setup/images/who-will-pay.webp)

✅ Browser VS Code window go open and di dev container go start to build.  
E go take **~2 minutes** di first time.

## 3. Add ya API key (di safe way)

### Option A Codespaces Secrets — We recommend dis one

1. ⚙️ Gear icon -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Name: OPENAI_API_KEY
3. Value: paste ya key → Add secret

Na all be dat—our code go use am automatically.

### Option B .env file (if you really need am)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transle-shon service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transle-shon. Even as we dey try make am accurate, abeg make you sabi say transle-shon wey machine do fit get mistake or no dey correct well. Di original dokyument for im native language na di one wey you go take as di correct source. For important mata, e good make professional human transle-shon dey do am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transle-shon.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->