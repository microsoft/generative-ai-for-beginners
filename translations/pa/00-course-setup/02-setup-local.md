<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T16:01:08+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "pa"
}
-->
# ਲੋਕਲ ਸੈਟਅੱਪ 🖥️

**ਇਹ ਗਾਈਡ ਉਨ੍ਹਾਂ ਲਈ ਹੈ ਜੋ ਸਭ ਕੁਝ ਆਪਣੇ ਲੈਪਟਾਪ 'ਤੇ ਚਲਾਉਣਾ ਚਾਹੁੰਦੇ ਹਨ।**  
ਤੁਹਾਡੇ ਕੋਲ ਦੋ ਚੋਣਾਂ ਹਨ: **(A) ਨੈਟਿਵ ਪਾਈਥਨ + ਵਰਚੁਅਲ-ਇਨਵ** ਜਾਂ **(B) VS Code Dev Container Docker ਨਾਲ**।  
ਜੋ ਵੀ ਆਸਾਨ ਲੱਗੇ, ਚੁਣੋ—ਦੋਵੇਂ ਰਾਹ ਇੱਕੋ ਹੀ ਪਾਠਾਂ ਵੱਲ ਲੈ ਜਾਂਦੇ ਹਨ।

## 1.  ਲੋੜੀਂਦੇ ਟੂਲ

| ਟੂਲ                | ਵਰਜਨ / ਨੋਟਸ                                                                       |
|--------------------|-----------------------------------------------------------------------------------|
| **Python**         | 3.10 + (<https://python.org> ਤੋਂ ਲਵੋ)                                              |
| **Git**            | ਨਵਾਂ (Xcode / Git for Windows / Linux package manager ਨਾਲ ਆਉਂਦਾ)                  |
| **VS Code**        | ਚੋਣਵੀਂ, ਪਰ ਸਿਫਾਰਸ਼ੀ <https://code.visualstudio.com>                              |
| **Docker Desktop** | *ਸਿਰਫ* Option B ਲਈ। ਮੁਫ਼ਤ ਇੰਸਟਾਲ: <https://docs.docker.com/desktop/>           |

> 💡 **ਟਿੱਪ** – ਟੂਲ ਟਰਮੀਨਲ 'ਚ ਚੈੱਕ ਕਰੋ:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Option A – ਨੈਟਿਵ ਪਾਈਥਨ (ਸਭ ਤੋਂ ਤੇਜ਼)

### Step 1  ਇਹ ਰਿਪੋ ਕਲੋਨ ਕਰੋ

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Step 2 ਵਰਚੁਅਲ ਇਨਵਾਇਰਨਮੈਂਟ ਬਣਾਓ ਤੇ ਐਕਟੀਵੇਟ ਕਰੋ

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ ਹੁਣ ਪ੍ਰੌਂਪਟ (.venv) ਨਾਲ ਸ਼ੁਰੂ ਹੋਣਾ ਚਾਹੀਦਾ—ਇਹਦਾ ਮਤਲਬ ਤੁਸੀਂ ਇਨਵਾਇਰਨਮੈਂਟ 'ਚ ਹੋ।

### Step 3 Dependencies ਇੰਸਟਾਲ ਕਰੋ

```bash
pip install -r requirements.txt
```

[API keys](../../../00-course-setup) ਵਾਲੇ Section 3 'ਤੇ ਜਾਓ

## 2. Option B – VS Code Dev Container (Docker)

ਅਸੀਂ ਇਹ ਰਿਪੋ ਤੇ ਕੋਰਸ [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) ਨਾਲ ਸੈੱਟਅੱਪ ਕੀਤਾ ਹੈ, ਜਿਸ ਵਿੱਚ Universal runtime ਹੈ ਜੋ Python3, .NET, Node.js ਅਤੇ Java development ਲਈ ਸਹਾਇਕ ਹੈ। ਇਸ ਦੀ configuration `devcontainer.json` ਫਾਇਲ ਵਿੱਚ `.devcontainer/` ਫੋਲਡਰ 'ਚ ਰਿਪੋ ਦੇ ਰੂਟ 'ਤੇ ਹੈ।

>**ਇਹ ਕਿਉਂ ਚੁਣੋ?**
>Codespaces ਵਰਗਾ ਹੀ environment; dependency drift ਨਹੀਂ ਹੁੰਦੀ।

### Step 0 Extra ਚੀਜ਼ਾਂ ਇੰਸਟਾਲ ਕਰੋ

Docker Desktop – ```docker --version``` ਚਲਾਉਣ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ।
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers) ਲੋੜੀਂਦੀ ਹੈ।

### Step 1 VS Code 'ਚ ਰਿਪੋ ਖੋਲ੍ਹੋ

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code `.devcontainer/` ਨੂੰ ਡਿਟੈਕਟ ਕਰ ਲੈਂਦਾ ਤੇ ਪ੍ਰੌਂਪਟ ਆ ਜਾਂਦੀ।

### Step 2 Container 'ਚ Reopen ਕਰੋ

"Reopen in Container" 'ਤੇ ਕਲਿੱਕ ਕਰੋ। Docker image ਬਣਾਉਂਦਾ (ਪਹਿਲੀ ਵਾਰ ≈ 3 ਮਿੰਟ ਲੱਗਦੇ)।
ਜਦੋਂ ਟਰਮੀਨਲ ਪ੍ਰੌਂਪਟ ਆਵੇ, ਤੁਸੀਂ container 'ਚ ਹੋ।

## 2.  Option C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ਇੱਕ ਹਲਕਾ installer ਹੈ [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, ਅਤੇ ਕੁਝ packages ਇੰਸਟਾਲ ਕਰਨ ਲਈ।
Conda ਇੱਕ package manager ਹੈ, ਜੋ ਵੱਖ-ਵੱਖ Python [**virtual environments**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) ਤੇ packages ਸੈੱਟਅੱਪ ਤੇ ਸਵਿੱਚ ਕਰਨਾ ਆਸਾਨ ਬਣਾਉਂਦਾ। ਇਹ ਉਹ packages ਇੰਸਟਾਲ ਕਰਨ ਲਈ ਵੀ ਵਧੀਆ ਹੈ ਜੋ `pip` ਰਾਹੀਂ ਨਹੀਂ ਮਿਲਦੇ।

### Step 0  Miniconda ਇੰਸਟਾਲ ਕਰੋ

[MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) ਦੇਖੋ ਤੇ ਸੈੱਟਅੱਪ ਕਰੋ।

```bash
conda --version
```

### Step 1 ਵਰਚੁਅਲ ਇਨਵਾਇਰਨਮੈਂਟ ਬਣਾਓ

ਨਵਾਂ environment file (*environment.yml*) ਬਣਾਓ। ਜੇ Codespaces ਵਰਤ ਰਹੇ ਹੋ, `.devcontainer` ਡਾਇਰੈਕਟਰੀ 'ਚ ਬਣਾਓ, ਜਿਵੇਂ `.devcontainer/environment.yml`।

### Step 2  Environment file 'ਚ ਡਾਟਾ ਪਾਓ

`environment.yml` 'ਚ ਹੇਠਾਂ ਦਿੱਤਾ snippet ਪਾਓ

```yml
name: <environment-name>
channels:
 - defaults
 - microsoft
dependencies:
- python=<python-version>
- openai
- python-dotenv
- pip
- pip:
    - azure-ai-ml

```

### Step 3 ਆਪਣਾ Conda environment ਬਣਾਓ

ਹੇਠਾਂ ਦਿੱਤੇ commands command line/terminal 'ਚ ਚਲਾਓ

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

[Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) ਵੇਖੋ ਜੇ ਕੋਈ ਸਮੱਸਿਆ ਆਵੇ।

## 2  Option D – Classic Jupyter / Jupyter Lab (browser 'ਚ)

> **ਇਹ ਕਿਸ ਲਈ?**  
> ਜਿਹੜੇ classic Jupyter interface ਪਸੰਦ ਕਰਦੇ ਜਾਂ VS Code ਤੋਂ ਬਿਨਾਂ notebooks ਚਲਾਉਣਾ ਚਾਹੁੰਦੇ।  

### Step 1  ਯਕੀਨੀ ਬਣਾਓ Jupyter ਇੰਸਟਾਲ ਹੈ

Jupyter ਲੋਕਲ ਚਲਾਉਣ ਲਈ, ਟਰਮੀਨਲ/ਕਮਾਂਡ ਲਾਈਨ 'ਚ ਜਾਓ, ਕੋਰਸ ਡਾਇਰੈਕਟਰੀ 'ਚ ਜਾਓ, ਤੇ ਚਲਾਓ:

```bash
jupyter notebook
```

ਜਾਂ

```bash
jupyterhub
```

ਇਸ ਨਾਲ Jupyter instance ਚਲ ਜਾਵੇਗੀ ਤੇ URL ਕਮਾਂਡ ਲਾਈਨ 'ਚ ਦਿਖਾਈ ਦੇਵੇਗੀ।

URL 'ਤੇ ਜਾ ਕੇ, ਤੁਹਾਨੂੰ ਕੋਰਸ outline ਦਿਖਾਈ ਦੇਵੇਗੀ ਤੇ ਤੁਸੀਂ ਕਿਸੇ ਵੀ `*.ipynb` ਫਾਇਲ 'ਚ ਜਾ ਸਕਦੇ ਹੋ। ਉਦਾਹਰਨ ਲਈ, `08-building-search-applications/python/oai-solution.ipynb`।

## 3. ਆਪਣੀਆਂ API Keys ਪਾਓ

API keys ਨੂੰ ਸੁਰੱਖਿਅਤ ਰੱਖਣਾ ਕਿਸੇ ਵੀ ਐਪ ਬਣਾਉਣ ਸਮੇਂ ਜ਼ਰੂਰੀ ਹੈ। ਅਸੀਂ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ ਕਿ API keys ਕਦੇ ਵੀ code 'ਚ ਸਿੱਧਾ ਨਾ ਪਾਓ। ਜੇ ਇਹ detailz public repository 'ਚ commit ਹੋ ਗਈ ਤਾਂ security risk ਤੇ extra ਖਰਚਾ ਹੋ ਸਕਦਾ।
ਇੱਥੇ `.env` ਫਾਇਲ Python ਲਈ ਬਣਾਉਣ ਤੇ `GITHUB_TOKEN` ਪਾਉਣ ਦੀ ਪੂਰੀ ਪ੍ਰਕਿਰਿਆ ਦਿੱਤੀ ਹੈ:

1. **Project ਡਾਇਰੈਕਟਰੀ 'ਚ ਜਾਓ**: ਆਪਣਾ ਟਰਮੀਨਲ ਜਾਂ command prompt ਖੋਲ੍ਹੋ ਤੇ project ਦੀ root ਡਾਇਰੈਕਟਰੀ 'ਚ ਜਾਓ, ਜਿੱਥੇ `.env` ਫਾਇਲ ਬਣਾਉਣੀ ਹੈ।

   ```bash
   cd path/to/your/project
   ```

2. **`.env` ਫਾਇਲ ਬਣਾਓ**: ਆਪਣਾ ਮਨਪਸੰਦ text editor ਵਰਤੋ, ਨਵੀਂ `.env` ਫਾਇਲ ਬਣਾਓ। ਜੇ command line ਵਰਤ ਰਹੇ ਹੋ, `touch` (Unix-based) ਜਾਂ `echo` (Windows) ਵਰਤੋ:

   Unix-based systems:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **`.env` ਫਾਇਲ edit ਕਰੋ**: `.env` ਫਾਇਲ text editor (VS Code, Notepad++ ਜਾਂ ਹੋਰ) 'ਚ ਖੋਲ੍ਹੋ। ਹੇਠਾਂ ਦਿੱਤੀ ਲਾਈਨ ਪਾਓ, `your_github_token_here` ਨੂੰ ਆਪਣੇ GitHub token ਨਾਲ ਬਦਲੋ:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **ਫਾਇਲ save ਕਰੋ**: Save ਕਰੋ ਤੇ editor ਬੰਦ ਕਰੋ।

5. **`python-dotenv` ਇੰਸਟਾਲ ਕਰੋ**: ਜੇ ਪਹਿਲਾਂ ਨਹੀਂ ਕੀਤਾ, `python-dotenv` package ਇੰਸਟਾਲ ਕਰੋ, ਤਾਂ ਜੋ `.env` ਫਾਇਲ ਤੋਂ environment variables Python 'ਚ ਲੋਡ ਹੋ ਸਕਣ। `pip` ਨਾਲ ਇੰਸਟਾਲ ਕਰੋ:

   ```bash
   pip install python-dotenv
   ```

6. **Python script 'ਚ Environment Variables ਲੋਡ ਕਰੋ**: Python script 'ਚ `python-dotenv` package ਵਰਤੋ, ਤਾਂ ਜੋ `.env` ਫਾਇਲ ਤੋਂ variables ਲੋਡ ਹੋਣ:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

ਬਸ! ਤੁਸੀਂ `.env` ਫਾਇਲ ਬਣਾਈ, GitHub token ਪਾਇਆ, ਤੇ Python ਐਪ 'ਚ ਲੋਡ ਕੀਤਾ।

🔐 .env ਕਦੇ ਵੀ commit ਨਾ ਕਰੋ—ਇਹ ਪਹਿਲਾਂ ਹੀ .gitignore 'ਚ ਹੈ।
ਪੂਰੀ provider instructions [`providers.md`](03-providers.md) 'ਚ ਹਨ।

## 4. ਅੱਗੇ ਕੀ?

| ਮੈਂ ਚਾਹੁੰਦਾ/ਦੀ…         | ਜਾਓ…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| Lesson 1 ਸ਼ੁਰੂ ਕਰੋ      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| LLM Provider ਸੈੱਟਅੱਪ ਕਰੋ | [`providers.md`](03-providers.md)                                       |
| ਹੋਰ learners ਨੂੰ ਮਿਲੋ | [Join our Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Troubleshooting

| ਲੱਛਣ                                    | ਹੱਲ                                                              |
|-------------------------------------------|------------------------------------------------------------------|
| `python not found`                        | Python ਨੂੰ PATH 'ਚ ਪਾਓ ਜਾਂ install ਤੋਂ ਬਾਅਦ ਟਰਮੀਨਲ ਮੁੜ ਖੋਲ੍ਹੋ     |
| `pip` cannot build wheels (Windows)       | `pip install --upgrade pip setuptools wheel` ਫਿਰ retry ਕਰੋ।      |
| `ModuleNotFoundError: dotenv`             | `pip install -r requirements.txt` ਚਲਾਓ (env install ਨਹੀਂ ਹੋਇਆ)। |
| Docker build fails *No space left*        | Docker Desktop ▸ *Settings* ▸ *Resources* → disk size ਵਧਾਓ।     |
| VS Code keeps prompting to reopen         | ਦੋਵੇਂ Options active ਹੋ ਸਕਦੀਆਂ; ਇੱਕ ਚੁਣੋ (venv **ਜਾਂ** container)|
| OpenAI 401 / 429 errors                   | `OPENAI_API_KEY` value ਜਾਂ request rate limits ਚੈੱਕ ਕਰੋ।          |
| Errors using Conda                        | Microsft AI libraries `conda install -c microsoft azure-ai-ml` ਨਾਲ install ਕਰੋ|

---

**ਅਸਵੀਕਰਨ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਅਸੀਂ ਯਥਾਸੰਭਵ ਸਹੀ ਅਨੁਵਾਦ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਪਰ ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਣਪਛਾਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼, ਜਿਸ ਭਾਸ਼ਾ ਵਿੱਚ ਉਹ ਲਿਖਿਆ ਗਿਆ ਹੈ, ਨੂੰ ਹੀ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਅਰਥ ਲਗਾਉਣ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।