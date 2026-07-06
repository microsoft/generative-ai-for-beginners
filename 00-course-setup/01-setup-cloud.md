# Cloud Setup ☁️ – GitHub Codespaces

**Use this guide if you don’t want to install anything locally.**  
Codespaces gives you a free, browser-based VS Code instance with all dependencies pre-installed.

---

## 1.  Why Codespaces?

| Benefit | What it means for you |
|---------|----------------------|
| ✅ Zero installs | Works on Chromebook, iPad, school lab PCs… |
| ✅ Pre-built dev container | Python 3, Node.js, .NET, Java already inside |
| ✅ Free quota | Personal accounts get **120 core-hours / 60 GB-hours per month** |

> 💡 **Tip**  
> Keep your quota healthy by **stopping** or **deleting** idle codespaces  
> (View ▸ Command Palette ▸ *Codespaces: Stop Codespace*).

---

## 2.  Create a Codespace (one click)

1. **Fork** this repo (top-right **Fork** button).  
2. In your fork, click **Code ▸ Codespaces ▸ Create codespace on main**.  
   ![Dialog showing buttons to create a codespace](./images/who-will-pay.webp?WT.mc_id=academic-105485-koreyst)

✅ A browser VS Code window opens and the dev container starts building.
This takes **~2 minutes** the first time.

## 3. Add your API key (the safe way)

### Option A Codespaces Secrets — Recommended

1. ⚙️ Gear icon -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Name: OPENAI_API_KEY
3. Value: paste your key → Add secret

That’s it—our code will pick it up automatically.

### Option B .env file (if you really need one)

```bash
cp .env.copy .env
code .env         # fill in OPENAI_API_KEY=your_key_here
```

