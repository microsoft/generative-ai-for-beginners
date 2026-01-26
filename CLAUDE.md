# CLAUDE.md - AI Assistant Guidelines for Generative AI for Beginners

This document provides comprehensive guidance for AI assistants working with this repository.

## Repository Overview

**Generative AI for Beginners** is a Microsoft-sponsored, 21-lesson open-source curriculum teaching the fundamentals of building Generative AI applications. The course includes both conceptual lessons ("Learn") and hands-on coding lessons ("Build") with examples in Python and TypeScript.

**Repository URL:** https://github.com/microsoft/generative-ai-for-beginners

## Directory Structure

```
/
├── 00-course-setup/             # Course setup and prerequisites
├── 01-introduction-to-genai/    # Introduction to Generative AI and LLMs
├── 02-exploring-and-comparing-different-llms/
├── 03-using-generative-ai-responsibly/
├── 04-prompt-engineering-fundamentals/
├── 05-advanced-prompts/
├── 06-text-generation-apps/     # Building text generation applications
├── 07-building-chat-applications/
├── 08-building-search-applications/
├── 09-building-image-applications/
├── 10-building-low-code-ai-applications/
├── 11-integrating-with-function-calling/
├── 12-designing-ux-for-ai-applications/
├── 13-securing-ai-applications/
├── 14-the-generative-ai-application-lifecycle/
├── 15-rag-and-vector-databases/
├── 16-open-source-models/       # Hugging Face models
├── 17-ai-agents/
├── 18-fine-tuning/
├── 19-slm/                      # Small Language Models (Phi-3)
├── 20-mistral/                  # Mistral models
├── 21-meta/                     # Meta/Llama models
├── .devcontainer/               # GitHub Codespaces configuration
├── .github/workflows/           # CI/CD workflows for markdown validation
├── docs/                        # Additional documentation
├── images/                      # Repository-level images
├── presentations/               # Presentation materials
└── translations/                # Root-level translations (cn, es-mx, ja-jp, ko, pt-br, tw)
```

### Lesson Structure

Each lesson folder follows this pattern:
```
XX-lesson-name/
├── README.md                    # Main lesson content
├── images/                      # Lesson-specific images
├── translations/                # Translated versions (cn, es-mx, ja-jp, ko, pt-br, tw)
│   └── {locale}/README.md
├── python/                      # Python code samples
│   ├── aoai-assignment.ipynb    # Azure OpenAI notebook
│   ├── oai-assignment.ipynb     # OpenAI API notebook
│   ├── githubmodels-assignment.ipynb  # GitHub Models notebook
│   └── *.py                     # Python scripts
├── typescript/                  # TypeScript code samples
└── dotnet/                      # .NET code samples (some lessons)
```

## Tech Stack

### Languages & Frameworks
- **Python 3.x** - Primary language for code samples
- **TypeScript** - Alternative implementations
- **.NET/C#** - Some lesson implementations
- **Jupyter Notebooks** (.ipynb) - Interactive code samples

### Key Dependencies

**Python (requirements.txt):**
```
openai>=0.28.0
python-dotenv==1.0.0
azure-ai-inference
tiktoken
numpy==1.24.2
pandas==1.5.3
matplotlib==3.7.0
ipywidgets==7.7.1
tqdm==4.66.3
```

**Node.js (package.json):**
```json
{
  "@azure-rest/ai-inference": "^1.0.0-beta.2",
  "@azure/core-auth": "^1.8.0",
  "openai": "^4.10.0"
}
```

### AI Providers Supported
1. **Azure OpenAI Service** - Primary provider (files: `aoai-*.py`, `aoai-*.ipynb`)
2. **OpenAI API** - Direct OpenAI access (files: `oai-*.py`, `oai-*.ipynb`)
3. **GitHub Models** - GitHub Marketplace models (files: `githubmodels-*.py`, `githubmodels-*.ipynb`)
4. **Hugging Face** - Open-source models (Lesson 16)

## Development Environment Setup

### GitHub Codespaces (Recommended)
The repository includes `.devcontainer/devcontainer.json` for zero-configuration setup:
- Image: `mcr.microsoft.com/devcontainers/universal:2`
- Auto-installs Python dependencies from `requirements.txt`
- Pre-configured VS Code extensions: Python, Jupyter

### Local Setup
```bash
# Clone repository
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners

# Install Python dependencies
pip install -r requirements.txt

# Install Node.js dependencies (for TypeScript samples)
npm install
```

### Environment Variables
Copy `.env.copy` to `.env` and configure:
```bash
# OpenAI Provider
OPENAI_API_KEY='<your-key>'

# Azure OpenAI
AZURE_OPENAI_API_VERSION='2024-02-01'
AZURE_OPENAI_API_KEY='<your-key>'
AZURE_OPENAI_ENDPOINT='<your-endpoint>'
AZURE_OPENAI_DEPLOYMENT='<deployment-name>'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<embeddings-deployment>'

# Hugging Face
HUGGING_FACE_API_KEY='<your-token>'
```

## Code Patterns

### Python - Azure OpenAI
```python
from openai import AzureOpenAI
import os
import dotenv

dotenv.load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ['AZURE_OPENAI_API_KEY'],
    api_version="2024-02-01"
)

deployment = os.environ['AZURE_OPENAI_DEPLOYMENT']
messages = [{"role": "user", "content": "Your prompt here"}]
completion = client.chat.completions.create(model=deployment, messages=messages)
print(completion.choices[0].message.content)
```

### TypeScript - Azure OpenAI
```typescript
import { OpenAIClient, AzureKeyCredential } from "@azure/openai";
import * as dotenv from "dotenv";

dotenv.config();

const client = new OpenAIClient(
    process.env.AZURE_OPENAI_ENDPOINT || '',
    new AzureKeyCredential(process.env.AZURE_OPENAI_API_KEY || '')
);
```

## Important Conventions

### Markdown & Link Requirements

**CRITICAL:** All markdown files must follow these rules (enforced by CI):

1. **Tracking IDs Required:** All URLs and relative paths must include `?WT.mc_id=academic-105485-koreyst` or `&WT.mc_id=academic-105485-koreyst`
   ```markdown
   <!-- Correct -->
   [Link](./path/to/file.md?WT.mc_id=academic-105485-koreyst)
   [External](https://example.com?WT.mc_id=academic-105485-koreyst)

   <!-- Incorrect -->
   [Link](./path/to/file.md)
   ```

2. **Relative Paths:** Must start with `./` or `../`
   ```markdown
   <!-- Correct -->
   [Next Lesson](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst)

   <!-- Incorrect -->
   [Next Lesson](01-introduction-to-genai/README.md)
   ```

3. **No Locale in URLs:** Remove country-specific locale prefixes
   ```markdown
   <!-- Correct -->
   https://learn.microsoft.com/azure/...

   <!-- Incorrect -->
   https://learn.microsoft.com/en-us/azure/...
   ```

4. **Image Storage:** All images must be in the `./images/` folder of the relevant lesson
5. **Image Naming:** Use English characters, numbers, and dashes only

### Translation Guidelines
- Human translations only - no machine translation
- Submit complete lesson translations (all files) in a single PR
- Supported locales: `cn`, `es-mx`, `ja-jp`, `ko`, `pt-br`, `tw`

## GitHub Workflows

### Validate Markdown (`validate-markdown.yml`)
Triggered on PRs modifying `.md` or `.ipynb` files:
- **check-broken-paths** - Validates relative links work
- **check-paths-tracking** - Ensures relative paths have tracking IDs
- **check-urls-tracking** - Ensures URLs have tracking IDs
- **check-urls-locale** - Ensures URLs don't have country locale
- **check-broken-urls** - Validates external URLs are accessible

### Other Workflows
- `lock.yml` - Locks stale issues
- `stale.yml` - Marks inactive issues/PRs as stale
- `welcome-pr.yml` - Welcomes new contributors
- `welcome-issue.yml` - Welcomes new issue reporters

## Contributing Guidelines

1. **Fork First:** Always fork the repository before making changes
2. **Separate PRs:** Submit separate PRs for different types of changes (bug fixes vs. docs)
3. **Sync Before PR:** Ensure your local main matches the upstream main
4. **CLA Required:** Contributors must agree to the Microsoft CLA

### PR Checklist
- [ ] All links include tracking ID (`?WT.mc_id=academic-105485-koreyst`)
- [ ] Relative paths start with `./` or `../`
- [ ] No country locale in URLs
- [ ] Images stored in `./images/` folder
- [ ] Images have descriptive English names with dashes

## Common Tasks

### Running Jupyter Notebooks
```bash
# Start Jupyter locally
jupyter notebook

# Or use JupyterHub
jupyterhub
```

### Running Python Scripts
```bash
cd 06-text-generation-apps/python
python aoai-app.py
```

### Running TypeScript Examples
```bash
cd 06-text-generation-apps/typescript/recipe-app
npm install
npx ts-node src/main.ts
```

### Converting to PDF
```bash
npm run convert  # Uses docsify-to-pdf
```

## File Naming Conventions

| Pattern | Description | Example |
|---------|-------------|---------|
| `aoai-*.py/ipynb` | Azure OpenAI implementation | `aoai-assignment.ipynb` |
| `oai-*.py/ipynb` | OpenAI API implementation | `oai-assignment.ipynb` |
| `githubmodels-*.py/ipynb` | GitHub Models implementation | `githubmodels-assignment.ipynb` |
| `*-solution.*` | Solution/answer files | `aoai-solution.py` |
| `*-assignment.*` | Exercise files | `aoai-assignment.ipynb` |

## Key Files Reference

| File | Purpose |
|------|---------|
| `README.md` | Main course overview and lesson index |
| `CONTRIBUTING.md` | Contribution guidelines and PR workflow |
| `CODE_OF_CONDUCT.md` | Microsoft Open Source Code of Conduct |
| `SECURITY.md` | Security policy and vulnerability reporting |
| `.env.copy` | Template for environment variables |
| `requirements.txt` | Python dependencies |
| `package.json` | Node.js dependencies and scripts |

## Notes for AI Assistants

1. **Always add tracking IDs** when creating or modifying links
2. **Check workflow requirements** before suggesting markdown changes
3. **Respect the lesson structure** - keep code in appropriate subfolders
4. **Test relative links** - ensure they work from the file's location
5. **Preserve multilingual content** - translations are maintained separately
6. **Use appropriate API client** based on file naming convention
7. **Environment variables** - never hardcode API keys; always use dotenv pattern
