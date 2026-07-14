# AGENTS.md

## Project Overview

Dis repository get full 21-lesson curriculum wey dey teach Generative AI basics and how to develop app dem. Di course na for beginners and e cover everything from basic tins go reach how to build app wey ready for production.

**Key Technologies:**
- Python 3.9+ with libraries: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript with Node.js and libraries: `openai` (Azure OpenAI via the v1 endpoint + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI Service, OpenAI API, and Microsoft Foundry Models (GitHub Models dey retire end of July 2026)
- Jupyter Notebooks for interactive learning
- Dev Containers for consistent development environment

**Repository Structure:**
- 21 numbered lesson directories (00-21) wey get READMEs, code examples, and assignments
- Multiple implementations: Python, TypeScript, and sometimes .NET examples
- Translations directory with 40+ language versions
- Centralized configuration via `.env` file (use `.env.copy` as template)

## Setup Commands

### Initial Repository Setup

```bash
# Make copy di repo
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env wit your API keys and endpoints
```

### Python Environment Setup

```bash
# Make virtual environment
python3 -m venv venv

# Turn on virtual environment
# For macOS/Linux:
source venv/bin/activate
# For Windows:
venv\Scripts\activate

# Install wetin e need
pip install -r requirements.txt
```

### Node.js/TypeScript Setup

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, go waka go di specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container Setup (Recommended)

Di repository get `.devcontainer` configuration for GitHub Codespaces or VS Code Dev Containers:

1. Open repository for GitHub Codespaces or VS Code with Dev Containers extension
2. Dev Container go automatically:
   - Install Python dependencies from `requirements.txt`
   - Run post-create script (`.devcontainer/post-create.sh`)
   - Set up Jupyter kernel

## Development Workflow

### Environment Variables

All lessons wey need API access dey use environment variables wey define for `.env`:

- `OPENAI_API_KEY` - For OpenAI API
- `AZURE_OPENAI_API_KEY` - For Azure OpenAI for Microsoft Foundry (Azure OpenAI Service na part of Microsoft Foundry now: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI endpoint URL (Foundry resource endpoint)
- `AZURE_OPENAI_DEPLOYMENT` - Chat completion model deployment name
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Embeddings model deployment name
- `AZURE_OPENAI_API_VERSION` - API version (default: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - For Hugging Face models
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry Models endpoint (multi-provider model catalog)
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry Models API key (replace the retiring `GITHUB_TOKEN`)

### Running Python Examples

```bash
# waka go lesson directory
cd 06-text-generation-apps/python

# run Python script
python aoai-app.py
```

### Running TypeScript Examples

```bash
# waka go TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# build di TypeScript code
npm run build

# run di application
npm start
```

### Running Jupyter Notebooks

```bash
# Start Jupyter for di repo root
jupyter notebook

# Or use VS Code wit Jupyter extension
```

### Working with Different Lesson Types

- **"Learn" lessons**: Focus on README.md documentation and concepts
- **"Build" lessons**: Get working code examples for Python and TypeScript
- Every lesson get README.md with theory, code walkthroughs, and links to video content

## Code Style Guidelines

### Python

- Use `python-dotenv` to manage environment variables
- Import `openai` library to interact with API
- Use `pylint` for linting (some examples get `# pylint: disable=all` for simplicity)
- Follow PEP 8 naming conventions
- Store API credentials for `.env` file, no put am for code

### TypeScript

- Use `dotenv` package for environment variables
- TypeScript configuration dey for `tsconfig.json` for every app
- Use `openai` package for Azure OpenAI (point the client for `/openai/v1/` endpoint and call `client.responses.create`); use `@azure-rest/ai-inference` for Microsoft Foundry Models
- Use `nodemon` for development with auto-reload
- Build before running: `npm run build` then `npm start`

### General Conventions

- Keep code examples easy and educational
- Put comments wey explain key concepts
- Each lesson code suppose be self-contained and e fit run
- Use consistent naming: `aoai-` prefix for Azure OpenAI, `oai-` for OpenAI API, `githubmodels-` for Microsoft Foundry Models (old prefix from GitHub Models time still dey)

## Documentation Guidelines

### Markdown Style

- All URLs suppose dey wrap inside `[text](../../url)` style no extra spaces
- Relative links suppose start with `./` or `../`
- All Microsoft domains links suppose get tracking ID: `?WT.mc_id=academic-105485-koreyst`
- No country local versions for URLs (no use `/en-us/`)
- Images dey inside `./images` folder with descriptive names
- Use English characters, numbers, and dashes for file names

### Translation Support

- Repository dey support over 40 languages through automated GitHub Actions
- Translations dey for `translations/` directory
- No send partial translations
- Machine translations no dey accepted
- Translated images dey inside `translated_images/` directory

## Testing and Validation

### Pre-submission Checks

Dis repository dey use GitHub Actions for validation. Before you submit PRs:

1. **Check Markdown Links**:
   ```bash
   # Di validate-markdown.yml workflow dey check:
   # - Brokens relative paths
   # - Paths wey no get tracking IDs
   # - URLs wey no get tracking IDs
   # - URLs wey get country locale
   # - Brokens external URLs
   ```

2. **Manual Testing**:
   - Test Python examples: Activate venv and run scripts
   - Test TypeScript examples: `npm install`, `npm run build`, `npm start`
   - Verify environment variables don set well
   - Check say API keys dey work with code examples

3. **Code Examples**:
   - Make sure all code dey run without wahala
   - Test with both Azure OpenAI and OpenAI API if e concern
   - Verify examples dey work with Microsoft Foundry Models where e need am

### No Automated Tests

Dis na educational repository wey focus on tutorials and examples. No get unit tests or integration tests to run. Validation na mainly:
- Manual test of code examples
- GitHub Actions to validate Markdown
- Community review for educational content

## Pull Request Guidelines

### Before Submitting

1. Test code changes for both Python and TypeScript if e concern
2. Run Markdown validation (e dey trigger automatically on PR)
3. Make sure tracking IDs dey for all Microsoft URLs
4. Check say relative links valid
5. Verify say images get correct reference

### PR Title Format

- Use descriptive titles: `[Lesson 06] Fix Python example typo` or `Update README for lesson 08`
- Reference issue numbers if e concern: `Fixes #123`

### PR Description

- Explain wetin you change and why
- Link the related issues
- For code changes, talk which examples you don test
- For translation PRs, include all files for complete translation

### Contribution Requirements

- Sign Microsoft CLA (e automatic on first PR)
- Fork repository to your account before you make changes
- One PR per logical change (no join unrelated fixes)
- Make PRs focus and small if fit

## Common Workflows

### Adding a New Code Example

1. Go to correct lesson directory
2. Create example for `python/` or `typescript/` subdirectory
3. Follow naming convention: `{provider}-{example-name}.{py|ts|js}`
4. Test with correct API credentials
5. Write any new environment variables down for lesson README

### Updating Documentation

1. Edit README.md inside lesson directory
2. Follow Markdown guidelines (tracking IDs, relative links)
3. Translation updates dey handled by GitHub Actions (no edit manually)
4. Test all links make dem valid

### Working with Dev Containers

1. Repository get `.devcontainer/devcontainer.json`
2. Post-create script install Python dependencies automatically
3. Extensions for Python and Jupyter dey pre-configured
4. Environment base on `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Deployment and Publishing

Dis na learning repository - no get deployment process. Curriculum dey consumed by:

1. **GitHub Repository**: Direct access to code and documentation
2. **GitHub Codespaces**: Instant dev environment with pre-configured setup
3. **Microsoft Learn**: Content fit dey syndicated to official learning platform
4. **docsify**: Documentation site wey build from Markdown (see `docsifytopdf.js` and `package.json`)

### Building Documentation Site

```bash
# Make PDF from di documentation (if e dey necessary)
npm run convert
```

## Troubleshooting

### Common Issues

**Python Import Errors**:
- Make sure say virtual environment don activate
- Run `pip install -r requirements.txt`
- Check Python version na 3.9+ 

**TypeScript Build Errors**:
- Run `npm install` inside the correct app directory
- Check Node.js version dey compatible
- Clear `node_modules` and reinstall if e need

**API Authentication Errors**:
- Make sure `.env` file dey and get correct values
- Check API keys valid and no expire
- Ensure endpoint URLs correct for your region

**Missing Environment Variables**:
- Copy `.env.copy` go `.env`
- Fill all needed values for the lesson wey you dey work on
- Restart your application after you update `.env`

## Additional Resources

- [Course Setup Guide](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Contributing Guidelines](./CONTRIBUTING.md)
- [Code of Conduct](./CODE_OF_CONDUCT.md)
- [Security Policy](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Collection of Advanced Code Samples](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Project-Specific Notes

- Dis na **educational repository** wey focus on learning, no be production code
- Examples na simple ones to help teach concepts
- Code quality balance with educational clarity
- Every lesson self-contained and you fit do am on your own
- Repository dey support multiple API providers: Azure OpenAI, OpenAI, Microsoft Foundry Models, and offline providers like Foundry Local and Ollama
- Content dey multilingual with automated translation workflows
- Active community for Discord for questions and support

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->