<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T10:59:02+00:00",
  "source_file": "AGENTS.md",
  "language_code": "pa"
}
-->
# AGENTS.md

## ਪ੍ਰੋਜੈਕਟ ਝਲਕ

ਇਹ ਰਿਪੋਜ਼ਟਰੀ ਵਿੱਚ 21 ਪਾਠਾਂ ਦੀ ਵਿਸਤ੍ਰਿਤ ਪਾਠਕ੍ਰਮ ਸ਼ਾਮਲ ਹੈ ਜੋ ਜਨਰੇਟਿਵ AI ਦੇ ਮੂਲ ਸਿਧਾਂਤਾਂ ਅਤੇ ਐਪਲੀਕੇਸ਼ਨ ਵਿਕਾਸ ਸਿਖਾਉਂਦਾ ਹੈ। ਇਹ ਕੋਰਸ ਸ਼ੁਰੂਆਤੀ ਸਿਖਿਆਰਥੀਆਂ ਲਈ ਤਿਆਰ ਕੀਤਾ ਗਿਆ ਹੈ ਅਤੇ ਬੁਨਿਆਦੀ ਧਾਰਨਾਵਾਂ ਤੋਂ ਲੈ ਕੇ ਉਤਪਾਦਨ-ਤਿਆਰ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਉਣ ਤੱਕ ਸਭ ਕੁਝ ਕਵਰ ਕਰਦਾ ਹੈ।

**ਮੁੱਖ ਤਕਨਾਲੋਜੀਆਂ:**
- Python 3.9+ ਨਾਲ ਲਾਇਬ੍ਰੇਰੀਆਂ: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript ਨਾਲ Node.js ਅਤੇ ਲਾਇਬ੍ਰੇਰੀਆਂ: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API, ਅਤੇ GitHub Models
- ਇੰਟਰਐਕਟਿਵ ਸਿਖਲਾਈ ਲਈ Jupyter Notebooks
- ਸਥਿਰ ਵਿਕਾਸ ਵਾਤਾਵਰਣ ਲਈ Dev Containers

**ਰਿਪੋਜ਼ਟਰੀ ਸਟ੍ਰਕਚਰ:**
- 21 ਗਿਣਤੀ ਵਾਲੇ ਪਾਠ ਡਾਇਰੈਕਟਰੀਆਂ (00-21) ਜਿਨ੍ਹਾਂ ਵਿੱਚ README, ਕੋਡ ਉਦਾਹਰਨਾਂ, ਅਤੇ ਅਸਾਈਨਮੈਂਟ ਸ਼ਾਮਲ ਹਨ
- ਕਈ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ: Python, TypeScript, ਅਤੇ ਕਦੇ-ਕਦੇ .NET ਉਦਾਹਰਨਾਂ
- 40+ ਭਾਸ਼ਾਵਾਂ ਦੇ ਅਨੁਵਾਦਾਂ ਵਾਲੀ ਡਾਇਰੈਕਟਰੀ
- `.env` ਫਾਈਲ ਰਾਹੀਂ ਕੇਂਦਰੀਕ੍ਰਿਤ ਸੰਰਚਨਾ (`.env.copy` ਨੂੰ ਟੈਂਪਲੇਟ ਵਜੋਂ ਵਰਤੋ)

## ਸੈਟਅੱਪ ਕਮਾਂਡ

### ਸ਼ੁਰੂਆਤੀ ਰਿਪੋਜ਼ਟਰੀ ਸੈਟਅੱਪ

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Python ਵਾਤਾਵਰਣ ਸੈਟਅੱਪ

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Node.js/TypeScript ਸੈਟਅੱਪ

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container ਸੈਟਅੱਪ (ਸਿਫਾਰਸ਼ ਕੀਤੀ)

ਰਿਪੋਜ਼ਟਰੀ ਵਿੱਚ GitHub Codespaces ਜਾਂ VS Code Dev Containers ਲਈ `.devcontainer` ਸੰਰਚਨਾ ਸ਼ਾਮਲ ਹੈ:

1. ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ GitHub Codespaces ਜਾਂ VS Code ਵਿੱਚ Dev Containers ਐਕਸਟੈਂਸ਼ਨ ਨਾਲ ਖੋਲ੍ਹੋ
2. Dev Container ਆਪਣੇ ਆਪ:
   - `requirements.txt` ਤੋਂ Python dependencies ਇੰਸਟਾਲ ਕਰੇਗਾ
   - ਪੋਸਟ-ਕ੍ਰੀਏਟ ਸਕ੍ਰਿਪਟ (`.devcontainer/post-create.sh`) ਚਲਾਏਗਾ
   - Jupyter kernel ਸੈਟਅੱਪ ਕਰੇਗਾ

## ਵਿਕਾਸ ਵਰਕਫਲੋ

### ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ

ਸਭ ਪਾਠ ਜਿਨ੍ਹਾਂ ਨੂੰ API ਪਹੁੰਚ ਦੀ ਲੋੜ ਹੈ `.env` ਵਿੱਚ ਪਰਿਭਾਸ਼ਿਤ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ:

- `OPENAI_API_KEY` - OpenAI API ਲਈ
- `AZURE_OPENAI_API_KEY` - Azure OpenAI Service ਲਈ
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI endpoint URL
- `AZURE_OPENAI_DEPLOYMENT` - Chat completion ਮਾਡਲ ਡਿਪਲੋਇਮੈਂਟ ਨਾਮ
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Embeddings ਮਾਡਲ ਡਿਪਲੋਇਮੈਂਟ ਨਾਮ
- `AZURE_OPENAI_API_VERSION` - API ਵਰਜਨ (ਡਿਫਾਲਟ: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Hugging Face ਮਾਡਲਾਂ ਲਈ
- `GITHUB_TOKEN` - GitHub Models ਲਈ

### Python ਉਦਾਹਰਨ ਚਲਾਉਣਾ

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### TypeScript ਉਦਾਹਰਨ ਚਲਾਉਣਾ

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Jupyter Notebooks ਨਾਲ ਕੰਮ ਕਰਨਾ

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### ਵੱਖ-ਵੱਖ ਪਾਠਾਂ ਦੇ ਕਿਸਮਾਂ ਨਾਲ ਕੰਮ ਕਰਨਾ

- **"Learn" ਪਾਠ**: README.md ਦਸਤਾਵੇਜ਼ ਅਤੇ ਧਾਰਨਾਵਾਂ 'ਤੇ ਧਿਆਨ ਕੇਂਦਰਿਤ
- **"Build" ਪਾਠ**: Python ਅਤੇ TypeScript ਵਿੱਚ ਕੰਮ ਕਰਨ ਵਾਲੇ ਕੋਡ ਉਦਾਹਰਨਾਂ ਸ਼ਾਮਲ ਹਨ
- ਹਰ ਪਾਠ ਵਿੱਚ README.md ਹੁੰਦੀ ਹੈ ਜਿਸ ਵਿੱਚ ਸਿਧਾਂਤ, ਕੋਡ ਵਾਕਥਰੂ, ਅਤੇ ਵੀਡੀਓ ਸਮੱਗਰੀ ਲਈ ਲਿੰਕ ਸ਼ਾਮਲ ਹੁੰਦੇ ਹਨ

## ਕੋਡ ਸਟਾਈਲ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼

### Python

- ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਪ੍ਰਬੰਧਨ ਲਈ `python-dotenv` ਦੀ ਵਰਤੋਂ ਕਰੋ
- API ਇੰਟਰਐਕਸ਼ਨ ਲਈ `openai` ਲਾਇਬ੍ਰੇਰੀ ਇੰਪੋਰਟ ਕਰੋ
- ਲਿੰਟਿੰਗ ਲਈ `pylint` ਦੀ ਵਰਤੋਂ ਕਰੋ (ਕੁਝ ਉਦਾਹਰਨਾਂ ਵਿੱਚ ਸਾਦਗੀ ਲਈ `# pylint: disable=all` ਸ਼ਾਮਲ ਹੈ)
- PEP 8 ਨਾਮਕਰਨ ਰੀਤੀਆਂ ਦੀ ਪਾਲਣਾ ਕਰੋ
- API credentials ਨੂੰ `.env` ਫਾਈਲ ਵਿੱਚ ਸਟੋਰ ਕਰੋ, ਕਦੇ ਵੀ ਕੋਡ ਵਿੱਚ ਨਹੀਂ

### TypeScript

- ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲਾਂ ਲਈ `dotenv` ਪੈਕੇਜ ਦੀ ਵਰਤੋਂ ਕਰੋ
- ਹਰ ਐਪ ਲਈ `tsconfig.json` ਵਿੱਚ TypeScript ਸੰਰਚਨਾ
- Azure ਸੇਵਾਵਾਂ ਲਈ `@azure/openai` ਜਾਂ `@azure-rest/ai-inference` ਦੀ ਵਰਤੋਂ ਕਰੋ
- ਆਟੋ-ਰੀਲੋਡ ਨਾਲ ਵਿਕਾਸ ਲਈ `nodemon` ਦੀ ਵਰਤੋਂ ਕਰੋ
- ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਬਣਾਓ: `npm run build` ਫਿਰ `npm start`

### ਆਮ ਰੀਤੀਆਂ

- ਕੋਡ ਉਦਾਹਰਨਾਂ ਸਾਦੇ ਅਤੇ ਸਿੱਖਣ ਯੋਗ ਰੱਖੋ
- ਮੁੱਖ ਧਾਰਨਾਵਾਂ ਨੂੰ ਸਮਝਾਉਣ ਵਾਲੇ ਟਿੱਪਣੀਆਂ ਸ਼ਾਮਲ ਕਰੋ
- ਹਰ ਪਾਠ ਦਾ ਕੋਡ ਸਵੈ-ਨਿਰਭਰ ਅਤੇ ਚਲਾਉਣ ਯੋਗ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ
- ਸਥਿਰ ਨਾਮਕਰਨ ਦੀ ਵਰਤੋਂ ਕਰੋ: Azure OpenAI ਲਈ `aoai-` ਪ੍ਰੀਫਿਕਸ, OpenAI API ਲਈ `oai-`, GitHub Models ਲਈ `githubmodels-`

## ਦਸਤਾਵੇਜ਼ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼

### Markdown ਸਟਾਈਲ

- ਸਾਰੇ URLs ਨੂੰ `[text](../../url)` ਫਾਰਮੈਟ ਵਿੱਚ ਲਪੇਟਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ ਬਿਨਾਂ ਕਿਸੇ ਵਾਧੂ ਖਾਲੀ ਜਗ੍ਹਾ ਦੇ
- ਰਿਸ਼ਤੇਦਾਰ ਲਿੰਕ `./` ਜਾਂ `../` ਨਾਲ ਸ਼ੁਰੂ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ
- Microsoft ਡੋਮੇਨ ਦੇ ਸਾਰੇ ਲਿੰਕਾਂ ਵਿੱਚ ਟ੍ਰੈਕਿੰਗ ID ਸ਼ਾਮਲ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ: `?WT.mc_id=academic-105485-koreyst`
- URLs ਵਿੱਚ ਕੋਈ ਦੇਸ਼-ਵਿਸ਼ੇਸ਼ ਸਥਾਨ ਨਹੀਂ (ਜਿਵੇਂ `/en-us/` ਤੋਂ ਬਚੋ)
- ਚਿੱਤਰਾਂ `./images` ਫੋਲਡਰ ਵਿੱਚ ਵਰਣਨਾਤਮਕ ਨਾਮਾਂ ਨਾਲ ਸਟੋਰ ਕੀਤੇ ਜਾਣੇ ਚਾਹੀਦੇ ਹਨ
- ਫਾਈਲ ਨਾਮਾਂ ਵਿੱਚ ਅੰਗਰੇਜ਼ੀ ਅੱਖਰ, ਗਿਣਤੀ, ਅਤੇ ਡੈਸ਼ ਦੀ ਵਰਤੋਂ ਕਰੋ

### ਅਨੁਵਾਦ ਸਹਾਇਤਾ

- ਰਿਪੋਜ਼ਟਰੀ GitHub Actions ਰਾਹੀਂ 40+ ਭਾਸ਼ਾਵਾਂ ਦਾ ਸਮਰਥਨ ਕਰਦੀ ਹੈ
- ਅਨੁਵਾਦ `translations/` ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਸਟੋਰ ਕੀਤੇ ਜਾਂਦੇ ਹਨ
- ਅਧੂਰੇ ਅਨੁਵਾਦ ਜਮ੍ਹਾਂ ਨਾ ਕਰੋ
- ਮਸ਼ੀਨ ਅਨੁਵਾਦ ਸਵੀਕਾਰ ਨਹੀਂ ਕੀਤੇ ਜਾਂਦੇ
- ਅਨੁਵਾਦਿਤ ਚਿੱਤਰ `translated_images/` ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਸਟੋਰ ਕੀਤੇ ਜਾਂਦੇ ਹਨ

## ਟੈਸਟਿੰਗ ਅਤੇ ਵੈਰੀਫਿਕੇਸ਼ਨ

### ਪੇਸ਼ਕਸ਼ ਤੋਂ ਪਹਿਲਾਂ ਚੈੱਕ

ਇਹ ਰਿਪੋਜ਼ਟਰੀ GitHub Actions ਦੀ ਵਰਤੋਂ ਕਰਦੀ ਹੈ। PR ਜਮ੍ਹਾਂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ:

1. **Markdown ਲਿੰਕ ਚੈੱਕ ਕਰੋ**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **ਮੈਨੂਅਲ ਟੈਸਟਿੰਗ**:
   - Python ਉਦਾਹਰਨਾਂ ਟੈਸਟ ਕਰੋ: venv ਐਕਟੀਵੇਟ ਕਰੋ ਅਤੇ ਸਕ੍ਰਿਪਟ ਚਲਾਓ
   - TypeScript ਉਦਾਹਰਨਾਂ ਟੈਸਟ ਕਰੋ: `npm install`, `npm run build`, `npm start`
   - ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਸੰਰਚਿਤ ਹਨ
   - API ਕੁੰਜੀਆਂ ਕੋਡ ਉਦਾਹਰਨਾਂ ਨਾਲ ਕੰਮ ਕਰ ਰਹੀਆਂ ਹਨ ਜਾਂ ਨਹੀਂ

3. **ਕੋਡ ਉਦਾਹਰਨਾਂ**:
   - ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਸਾਰੇ ਕੋਡ ਬਿਨਾਂ ਗਲਤੀਆਂ ਦੇ ਚਲਦੇ ਹਨ
   - ਜਿੱਥੇ ਲਾਗੂ ਹੋਵੇ, Azure OpenAI ਅਤੇ OpenAI API ਨਾਲ ਟੈਸਟ ਕਰੋ
   - ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਉਦਾਹਰਨ GitHub Models ਨਾਲ ਕੰਮ ਕਰਦੇ ਹਨ

### ਕੋਈ ਆਟੋਮੈਟਿਕ ਟੈਸਟ ਨਹੀਂ

ਇਹ ਇੱਕ ਸਿੱਖਣ ਵਾਲੀ ਰਿਪੋਜ਼ਟਰੀ ਹੈ ਜੋ ਟਿਊਟੋਰਿਅਲ ਅਤੇ ਉਦਾਹਰਨਾਂ 'ਤੇ ਕੇਂਦਰਿਤ ਹੈ। ਕੋਈ ਯੂਨਿਟ ਟੈਸਟ ਜਾਂ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਟੈਸਟ ਨਹੀਂ ਚਲਾਏ ਜਾਂਦੇ। ਵੈਰੀਫਿਕੇਸ਼ਨ ਮੁੱਖ ਤੌਰ 'ਤੇ:
- ਕੋਡ ਉਦਾਹਰਨਾਂ ਦੀ ਮੈਨੂਅਲ ਟੈਸਟਿੰਗ
- Markdown ਵੈਰੀਡੇਸ਼ਨ ਲਈ GitHub Actions
- ਸਿੱਖਣ ਸਮੱਗਰੀ ਦੀ ਕਮਿਊਨਿਟੀ ਸਮੀਖਾ

## ਪੂਲ ਰਿਕਵੇਸਟ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼

### ਜਮ੍ਹਾਂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ

1. Python ਅਤੇ TypeScript ਵਿੱਚ ਕੋਡ ਬਦਲਾਅ ਟੈਸਟ ਕਰੋ ਜਿੱਥੇ ਲਾਗੂ ਹੋਵੇ
2. Markdown ਵੈਰੀਡੇਸ਼ਨ ਚਲਾਓ (PR 'ਤੇ ਆਟੋਮੈਟਿਕ ਤਰੀਕੇ ਨਾਲ ਚਾਲੂ ਹੁੰਦੀ ਹੈ)
3. ਯਕੀਨੀ ਬਣਾਓ ਕਿ Microsoft URLs 'ਤੇ ਟ੍ਰੈਕਿੰਗ IDs ਮੌਜੂਦ ਹਨ
4. ਚੈੱਕ ਕਰੋ ਕਿ ਰਿਸ਼ਤੇਦਾਰ ਲਿੰਕ ਸਹੀ ਹਨ
5. ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਚਿੱਤਰ ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਦਰਸਾਏ ਗਏ ਹਨ

### PR ਸਿਰਲੇਖ ਫਾਰਮੈਟ

- ਵਰਣਨਾਤਮਕ ਸਿਰਲੇਖ ਦੀ ਵਰਤੋਂ ਕਰੋ: `[Lesson 06] Fix Python example typo` ਜਾਂ `Update README for lesson 08`
- ਜਿੱਥੇ ਲਾਗੂ ਹੋਵੇ, ਮਾਮਲੇ ਦੇ ਨੰਬਰ ਦਰਸਾਓ: `Fixes #123`

### PR ਵਰਣਨ

- ਕੀ ਬਦਲਿਆ ਅਤੇ ਕਿਉਂ, ਇਹ ਸਮਝਾਓ
- ਸੰਬੰਧਿਤ ਮਾਮਲਿਆਂ ਦੇ ਲਿੰਕ ਸ਼ਾਮਲ ਕਰੋ
- ਕੋਡ ਬਦਲਾਅ ਲਈ, ਦਰਸਾਓ ਕਿ ਕਿਹੜੇ ਉਦਾਹਰਨ ਟੈਸਟ ਕੀਤੇ ਗਏ
- ਅਨੁਵਾਦ PR ਲਈ, ਸਾਰੇ ਫਾਈਲਾਂ ਨੂੰ ਪੂਰੇ ਅਨੁਵਾਦ ਲਈ ਸ਼ਾਮਲ ਕਰੋ

### ਯੋਗਦਾਨ ਦੀਆਂ ਲੋੜਾਂ

- Microsoft CLA 'ਤੇ ਹਸਤਾਖਰ ਕਰੋ (ਪਹਿਲੇ PR 'ਤੇ ਆਟੋਮੈਟਿਕ)
- ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ ਆਪਣੇ ਖਾਤੇ ਵਿੱਚ ਫੋਰਕ ਕਰੋ ਬਦਲਾਅ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ
- ਇੱਕ PR ਪ੍ਰਤੀ ਤਰਕਸੰਗਤ ਬਦਲਾਅ (ਅਸੰਬੰਧਤ ਸੁਧਾਰਾਂ ਨੂੰ ਨਾ ਜੋੜੋ)
- PR ਨੂੰ ਸੰਕੇਂਦ੍ਰਿਤ ਅਤੇ ਛੋਟਾ ਰੱਖੋ ਜਿੱਥੇ ਸੰਭਵ ਹੋਵੇ

## ਆਮ ਵਰਕਫਲੋ

### ਨਵਾਂ ਕੋਡ ਉਦਾਹਰਨ ਸ਼ਾਮਲ ਕਰਨਾ

1. ਸਹੀ ਪਾਠ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਜਾਓ
2. `python/` ਜਾਂ `typescript/` ਸਬਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਉਦਾਹਰਨ ਬਣਾਓ
3. ਨਾਮਕਰਨ ਰੀਤੀ ਦੀ ਪਾਲਣਾ ਕਰੋ: `{provider}-{example-name}.{py|ts|js}`
4. ਅਸਲ API credentials ਨਾਲ ਟੈਸਟ ਕਰੋ
5. ਪਾਠ README ਵਿੱਚ ਕੋਈ ਨਵਾਂ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਦਸਤਾਵੇਜ਼ ਕਰੋ

### ਦਸਤਾਵੇਜ਼ ਅਪਡੇਟ ਕਰਨਾ

1. ਪਾਠ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ README.md ਨੂੰ ਸੰਪਾਦਿਤ ਕਰੋ
2. Markdown ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼ਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ (ਟ੍ਰੈਕਿੰਗ IDs, ਰਿਸ਼ਤੇਦਾਰ ਲਿੰਕ)
3. ਅਨੁਵਾਦ GitHub Actions ਦੁਆਰਾ ਸੰਭਾਲੇ ਜਾਂਦੇ ਹਨ (ਮੈਨੂਅਲ ਤਰੀਕੇ ਨਾਲ ਸੰਪਾਦਿਤ ਨਾ ਕਰੋ)
4. ਸਾਰੇ ਲਿੰਕ ਸਹੀ ਹਨ ਜਾਂ ਨਹੀਂ, ਟੈਸਟ ਕਰੋ

### Dev Containers ਨਾਲ ਕੰਮ ਕਰਨਾ

1. ਰਿਪੋਜ਼ਟਰੀ ਵਿੱਚ `.devcontainer/devcontainer.json` ਸ਼ਾਮਲ ਹੈ
2. ਪੋਸਟ-ਕ੍ਰੀਏਟ ਸਕ੍ਰਿਪਟ ਆਪਣੇ ਆਪ Python dependencies ਇੰਸਟਾਲ ਕਰਦਾ ਹੈ
3. Python ਅਤੇ Jupyter ਲਈ ਐਕਸਟੈਂਸ਼ਨ ਪਹਿਲਾਂ ਹੀ ਸੰਰਚਿਤ ਹਨ
4. ਵਾਤਾਵਰਣ `mcr.microsoft.com/devcontainers/universal:2.11.2` 'ਤੇ ਅਧਾਰਿਤ ਹੈ

## ਡਿਪਲੋਇਮੈਂਟ ਅਤੇ ਪ੍ਰਕਾਸ਼ਨ

ਇਹ ਇੱਕ ਸਿੱਖਣ ਵਾਲੀ ਰਿਪੋਜ਼ਟਰੀ ਹੈ - ਕੋਈ ਡਿਪਲੋਇਮੈਂਟ ਪ੍ਰਕਿਰਿਆ ਨਹੀਂ ਹੈ। ਪਾਠਕ੍ਰਮ ਨੂੰ ਹੇਠਾਂ ਦਿੱਤੇ ਤਰੀਕਿਆਂ ਨਾਲ ਵਰਤਿਆ ਜਾਂਦਾ ਹੈ:

1. **GitHub ਰਿਪੋਜ਼ਟਰੀ**: ਕੋਡ ਅਤੇ ਦਸਤਾਵੇਜ਼ਾਂ ਤੱਕ ਸਿੱਧੀ ਪਹੁੰਚ
2. **GitHub Codespaces**: ਪਹਿਲਾਂ ਤੋਂ ਸੰਰਚਿਤ ਸੈਟਅੱਪ ਨਾਲ ਤੁਰੰਤ ਵਿਕਾਸ ਵਾਤਾਵਰਣ
3. **Microsoft Learn**: ਸਮੱਗਰੀ ਨੂੰ ਅਧਿਕਾਰਤ ਸਿੱਖਣ ਪਲੇਟਫਾਰਮ 'ਤੇ ਸਿੰਡਿਕੇਟ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ
4. **docsify**: Markdown ਤੋਂ ਬਣਾਈ ਗਈ ਦਸਤਾਵੇਜ਼ ਸਾਈਟ (`docsifytopdf.js` ਅਤੇ `package.json` ਵੇਖੋ)

### ਦਸਤਾਵੇਜ਼ ਸਾਈਟ ਬਣਾਉਣਾ

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## ਸਮੱਸਿਆ ਹੱਲ

### ਆਮ ਸਮੱਸਿਆਵਾਂ

**Python Import Errors**:
- ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਐਕਟੀਵੇਟ ਹੈ
- `pip install -r requirements.txt` ਚਲਾਓ
- Python ਵਰਜਨ 3.9+ ਹੈ ਜਾਂ ਨਹੀਂ, ਚੈੱਕ ਕਰੋ

**TypeScript Build Errors**:
- ਖਾਸ ਐਪ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ `npm install` ਚਲਾਓ
- Node.js ਵਰਜਨ ਅਨੁਕੂਲ ਹੈ ਜਾਂ ਨਹੀਂ, ਚੈੱਕ ਕਰੋ
- `node_modules` ਨੂੰ ਸਾਫ ਕਰੋ ਅਤੇ ਦੁਬਾਰਾ ਇੰਸਟਾਲ ਕਰੋ ਜੇ ਲੋੜ ਹੋਵੇ

**API Authentication Errors**:
- `.env` ਫਾਈਲ ਮੌਜੂਦ ਹੈ ਅਤੇ ਸਹੀ ਮੁੱਲਾਂ ਨਾਲ ਭਰੀ ਹੋਈ ਹੈ ਜਾਂ ਨਹੀਂ, ਚੈੱਕ ਕਰੋ
- API ਕੁੰਜੀਆਂ ਵੈਧ ਹਨ ਅਤੇ ਮਿਆਦ ਖਤਮ ਨਹੀਂ ਹੋਈ
- ਯਕੀਨੀ ਬਣਾਓ ਕਿ endpoint URLs ਤੁਹਾਡੇ ਖੇਤਰ ਲਈ ਸਹੀ ਹਨ

**Missing Environment Variables**:
- `.env.copy` ਨੂੰ `.env` ਵਿੱਚ ਕਾਪੀ ਕਰੋ
- ਜਿਹੜੇ ਪਾਠ 'ਤੇ ਤੁਸੀਂ ਕੰਮ ਕਰ ਰਹੇ ਹੋ, ਉਸ ਲਈ ਸਾਰੇ ਲੋੜੀਂਦੇ ਮੁੱਲ ਭਰੋ
- `.env` ਅਪਡੇਟ ਕਰਨ ਤੋਂ ਬਾਅਦ ਆਪਣੀ ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਦੁਬਾਰਾ ਸ਼ੁਰੂ ਕਰੋ

## ਵਾਧੂ ਸਰੋਤ

- [ਕੋਰਸ ਸੈਟਅੱਪ ਗਾਈਡ](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [ਯੋਗਦਾਨ ਦਿਸ਼ਾ-ਨਿਰਦੇਸ਼](./CONTRIBUTING.md)
- [ਚਾਲ-ਚਲਣ ਕੋਡ](./CODE_OF_CONDUCT.md)
- [ਸੁਰੱਖਿਆ ਨੀਤੀ](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [ਉੱਚ-ਸਤਰੀ ਕੋਡ ਉਦਾਹਰਨਾਂ ਦਾ ਸੰਗ੍ਰਹਿ](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## ਪ੍ਰੋਜੈਕਟ-ਵਿਸ਼ੇਸ਼ ਟਿੱਪਣੀਆਂ

- ਇਹ ਇੱਕ **ਸਿੱਖਣ ਵਾਲੀ ਰਿਪੋਜ਼ਟਰੀ** ਹੈ ਜੋ ਸਿੱਖਣ 'ਤੇ ਕੇਂਦਰਿਤ ਹੈ, ਉਤਪਾਦਨ ਕੋਡ 'ਤੇ ਨਹੀਂ
- ਉਦਾਹਰਨਾਂ ਜਾਨਬੂਝ ਕੇ ਸਾਦੇ ਅਤੇ ਸਿੱਖਣ 'ਤੇ ਕੇਂਦਰਿਤ ਹਨ
- ਕੋਡ ਗੁਣਵੱਤਾ ਸਿੱਖਣ ਦੀ ਸਪਸ਼ਟਤਾ ਨਾਲ ਸੰਤੁਲਿਤ ਹੈ
- ਹਰ ਪਾਠ ਸਵੈ-ਨਿਰਭਰ ਹੈ ਅਤੇ ਅਲੱਗ-ਅਲੱਗ ਪੂਰਾ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ
- ਰਿਪੋਜ਼ਟਰੀ ਕਈ API ਪ੍ਰਦਾਤਾਵਾਂ ਦਾ ਸਮਰਥਨ ਕਰਦੀ ਹੈ: Azure Open

---

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਣਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।