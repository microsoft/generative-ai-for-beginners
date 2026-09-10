# AGENTS.md

## Projet Overview

Dis repository get one complete 21-lesson curriculum wey teach Generative AI basics and how to build application. Di course dey for beginners and e cover everytin from basic ideas go reach how to build app wey ready for production.

**Key Technologies:**
- Python 3.9+ wit libraries: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript wit Node.js and libraries: `openai` (Azure OpenAI via di v1 endpoint + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI Service, OpenAI API, and Microsoft Foundry Models (GitHub Models dey retire end of July 2026)
- Jupyter Notebooks for interactive learning
- Dev Containers for consistent development environment

**Repository Structure:**
- 21 numbered lesson folders (00-21) wey get READMEs, code examples, and assignments
- Many implementations: Python, TypeScript, and sometimes .NET examples
- Translations folder wit 40+ language versions
- Central config via `.env` file (use `.env.copy` as template)

## Setup Commands

### Initial Repository Setup

```bash
# Make copy of di repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Change .env wit your API keys and endpoints
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

# Put dependencies inside
pip install -r requirements.txt
```

### Node.js/TypeScript Setup

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, make you waka go di specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container Setup (Recommended)

Di repository get `.devcontainer` config for GitHub Codespaces or VS Code Dev Containers:

1. Open repository for GitHub Codespaces or VS Code wit Dev Containers extension
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
- `AZURE_OPENAI_DEPLOYMENT` - Chat completion model deployment name (course default: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Embeddings model deployment name (course default: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - API version (default: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - For Hugging Face models
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry Models endpoint (multi-provider model catalog)
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry Models API key (dis replace di retiring `GITHUB_TOKEN`)
- `AZURE_INFERENCE_CHAT_MODEL` - One non-reasoning model (e.g. `Llama-3.3-70B-Instruct`) wey use for `temperature` examples, because reasoning models no dey support sampling controls

### Model conventions (important)

- **Default chat model na `gpt-5-mini`** - one current, no old **reasoning** model. As of 2026 old temperature-capable "mini" models (`gpt-4o-mini`, `gpt-4.1-mini`) dey *deprecate*, so di course make GPT-5 family standard.
- **Reasoning models no dey allow `temperature` and `top_p`**, dem dey use `max_output_tokens` (Responses API) / `max_completion_tokens` (chat completions) instead of `max_tokens`. No add `temperature`/`top_p`/`max_tokens` to samples wey call `gpt-5-mini`.
- **To show `temperature`**, samples dey use **Llama** model (`Llama-3.3-70B-Instruct`) via Microsoft Foundry Models endpoint (`AZURE_INFERENCE_CHAT_MODEL`). Make you control reasoning models wit prompt engineering + reasoning controls, no use sampling controls.
- **Fine-tuning (lesson 18)** still dey use `gpt-4.1-mini`: GPT-5 only support reinforcement fine-tuning (RFT), e no get supervised fine-tuning (SFT) wey dem show for there.
- Lessons 20 (Mistral) and 21 (Meta) still dey use `temperature`/`max_tokens` because dem dey target Mistral/Llama models, wey dem still support dem.

### Running Python Examples

```bash
# Go waka go di lesson folder
cd 06-text-generation-apps/python

# Run one Python script
python aoai-app.py
```

### Running TypeScript Examples

```bash
# waka go di TypeScript app folder
cd 06-text-generation-apps/typescript/recipe-app

# build di TypeScript code
npm run build

# run di app
npm start
```

### Running Jupyter Notebooks

```bash
# Start Jupyter for di root folder weh di repo de
jupyter notebook

# Or use VS Code wid Jupyter extension
```

### Working with Different Lesson Types

- **"Learn" lessons**: Focus on README.md documentation and concepts
- **"Build" lessons**: Get working code examples for Python and TypeScript
- Every lesson get README.md wit theory, code walkthroughs, and links to video content

## Code Style Guidelines

### Python

- Use `python-dotenv` for environment variable management
- Import `openai` library for API interactions
- Use `pylint` for linting (some examples get `# pylint: disable=all` for simple)
- Follow PEP 8 naming conventions
- Store API credentials for `.env` file, no put am for code

### TypeScript

- Use `dotenv` package for environment variables
- TypeScript config dey for `tsconfig.json` for every app
- Use `openai` package for Azure OpenAI (point di client to `/openai/v1/` endpoint and call `client.responses.create`); use `@azure-rest/ai-inference` for Microsoft Foundry Models
- Use `nodemon` for development with auto-reload
- Build before run: `npm run build` then `npm start`

### General Conventions

- Keep code examples simple and educational
- Put comments wey explain key concepts
- Every lesson's code suppose dey self-contained and fit run
- Use consistent naming: `aoai-` prefix for Azure OpenAI, `oai-` for OpenAI API, `githubmodels-` for Microsoft Foundry Models (legacy prefix from GitHub Models time)

## Documentation Guidelines

### Markdown Style

- All URLs suppose dey wrapped for `[text](../../url)` format wit no extra spaces
- Relative links suppose start wit `./` or `../`
- All links to Microsoft domains suppose get tracking ID: `?WT.mc_id=academic-105485-koreyst`
- No country-specific locales for URLs (no use `/en-us/`)
- Images store for `./images` folder wit descriptive names
- Use English characters, numbers, and dashes for file names

### Translation Support

- Repository support 40+ languages via automated GitHub Actions
- Translations store for `translations/` directory
- No submit partial translations
- Machine translations no dey accepted
- Translated images store for `translated_images/` directory

## Testing and Validation

### Pre-submission Checks

Dis repository dey use GitHub Actions for validation. Before you submit PRs:

1. **Check Markdown Links**:
   ```bash
   # Di validate-markdown.yml workflow dey check:
   # - Broken relative paths
   # - Where dem no get tracking IDs for paths
   # - Where dem no get tracking IDs for URLs
   # - URLs weh get country locale
   # - Broken external URLs
   ```

2. **Manual Testing**:
   - Test Python examples: Activate venv and run scripts
   - Test TypeScript examples: `npm install`, `npm run build`, `npm start`
   - Verify environment variables dey correct
   - Check API keys work wit di code examples

3. **Code Examples**:
   - Make sure all code run without error
   - Test wit both Azure OpenAI and OpenAI API if e fit
   - Verify examples work wit Microsoft Foundry Models where e support

### No Automated Tests

Dis na educational repository wey focus on tutorials and examples. No get unit tests or integration tests to run. Validation mainly:
- Manual testing of code examples
- GitHub Actions for Markdown validation
- Community review of educational content

## Pull Request Guidelines

### Before Submitting

1. Test code changes for both Python and TypeScript if e fit
2. Run Markdown validation (dis one dey trigger automatically for PR)
3. Make sure tracking IDs dey for all Microsoft URLs
4. Check say relative links valid
5. Verify images dey properly referenced

### PR Title Format

- Use descriptive titles: `[Lesson 06] Fix Python example typo` or `Update README for lesson 08`
- Reference issue numbers if e fit: `Fixes #123`

### PR Description

- Explain wetin you change and why
- Link to related issues
- For code changes, talk which examples you test
- For translation PRs, include all files for full translation

### Contribution Requirements

- Sign Microsoft CLA (automatic for first PR)
- Fork repository to your account before you change anything
- One PR per logical change (no combine unrelated fixes)
- Keep PRs focused and small if possible

## Common Workflows

### Adding a New Code Example

1. Go the correct lesson folder
2. Create example for `python/` or `typescript/` subfolder
3. Follow naming convention: `{provider}-{example-name}.{py|ts|js}`
4. Test wit real API credentials
5. Document any new environment variables for lesson README

### Updating Documentation

1. Edit README.md for the lesson folder
2. Follow Markdown guidelines (tracking IDs, relative links)
3. Update translations dey handled by GitHub Actions (no edit manually)
4. Test say all links valid

### Working with Dev Containers

1. Repository get `.devcontainer/devcontainer.json`
2. Post-create script dey install Python dependencies automatically
3. Extensions for Python and Jupyter dey pre-configured
4. Environment dey based on `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Deployment and Publishing

Dis na learning repository - no get deployment process. Di course dey used by:

1. **GitHub Repository**: Direct access to code and documentation
2. **GitHub Codespaces**: Instant dev environment wit pre-configured setup
3. **Microsoft Learn**: Content fit dey syndicated to official learning platform
4. **docsify**: Documentation site build from Markdown (see `docsifytopdf.js` and `package.json`)

### Building Documentation Site

```bash
# Make PDF from di documentation (if e dey needed)
npm run convert
```

## Troubleshooting

### Common Issues

**Python Import Errors**:
- Make sure virtual environment dey activated
- Run `pip install -r requirements.txt`
- Check say Python version be 3.9+

**TypeScript Build Errors**:
- Run `npm install` inside the specific app folder
- Check Node.js version dey compatible
- Clear `node_modules` and reinstall if e need

**API Authentication Errors**:
- Check `.env` file dey and get correct values
- Check API keys valid and no expire
- Make sure endpoint URLs dey correct for your region

**Missing Environment Variables**:
- Copy `.env.copy` enter `.env`
- Fill all the required values for di lesson wey you dey work on
- Restart your app after you update `.env`

## Additional Resources

- [Course Setup Guide](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Contributing Guidelines](./CONTRIBUTING.md)
- [Code of Conduct](./CODE_OF_CONDUCT.md)
- [Security Policy](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Collection of Advanced Code Samples](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Project-Specific Notes

- Dis na **educational repository** wey focus on learning, no be production code
- Examples dem simple wit purpose to teach concepts
- Code quality balance wit educational clarity
- Every lesson self-contained and fit finish am alone
- Di repository support multiple API providers: Azure OpenAI, OpenAI, Microsoft Foundry Models, and offline providers like Foundry Local and Ollama
- Content dey multilingual wit automated translation workflows
- Active community for Discord for questions and support

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->