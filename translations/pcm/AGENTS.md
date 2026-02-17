# AGENTS.md

## Project Overview

Dis repo get 21 lessons wey dey teach di basics of Generative AI and how to develop apps wey fit work well. Di course na for people wey dey start and e cover everything from di basic ideas to how to build apps wey fit work for production.

**Key Technologies:**
- Python 3.9+ wit libraries: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript wit Node.js and libraries: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API, and GitHub Models
- Jupyter Notebooks for interactive learning
- Dev Containers for consistent development environment

**Repository Structure:**
- 21 lesson folders wey get numbers (00-21) wey get READMEs, code examples, and assignments
- Different implementations: Python, TypeScript, and sometimes .NET examples
- Translations folder wey get 40+ language versions
- `.env` file for centralized configuration (use `.env.copy` as template)

## Setup Commands

### Initial Repository Setup

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Python Environment Setup

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

### Node.js/TypeScript Setup

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container Setup (Recommended)

Dis repo get `.devcontainer` configuration for GitHub Codespaces or VS Code Dev Containers:

1. Open di repo for GitHub Codespaces or VS Code wit Dev Containers extension
2. Di Dev Container go automatically:
   - Install Python dependencies from `requirements.txt`
   - Run post-create script (`.devcontainer/post-create.sh`)
   - Set up Jupyter kernel

## Development Workflow

### Environment Variables

All di lessons wey need API access dey use environment variables wey dey `.env`:

- `OPENAI_API_KEY` - For OpenAI API
- `AZURE_OPENAI_API_KEY` - For Azure OpenAI Service
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI endpoint URL
- `AZURE_OPENAI_DEPLOYMENT` - Chat completion model deployment name
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Embeddings model deployment name
- `AZURE_OPENAI_API_VERSION` - API version (default: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - For Hugging Face models
- `GITHUB_TOKEN` - For GitHub Models

### Running Python Examples

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### Running TypeScript Examples

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Running Jupyter Notebooks

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### Working with Different Lesson Types

- **"Learn" lessons**: Focus on README.md documentation and concepts
- **"Build" lessons**: Get working code examples for Python and TypeScript
- Each lesson get README.md wey explain di theory, code walkthroughs, and links to video content

## Code Style Guidelines

### Python

- Use `python-dotenv` to manage environment variables
- Import `openai` library for API interactions
- Use `pylint` for linting (some examples get `# pylint: disable=all` for simplicity)
- Follow PEP 8 naming conventions
- Store API credentials for `.env` file, no put am for code

### TypeScript

- Use `dotenv` package for environment variables
- TypeScript configuration dey `tsconfig.json` for each app
- Use `@azure/openai` or `@azure-rest/ai-inference` for Azure services
- Use `nodemon` for development wit auto-reload
- Build before you run: `npm run build` then `npm start`

### General Conventions

- Make code examples simple and easy to understand
- Add comments wey explain di main ideas
- Each lesson code suppose dey complete and fit run
- Use consistent naming: `aoai-` prefix for Azure OpenAI, `oai-` for OpenAI API, `githubmodels-` for GitHub Models

## Documentation Guidelines

### Markdown Style

- All URLs suppose dey inside `[text](../../url)` format wit no extra space
- Relative links suppose start wit `./` or `../`
- All links to Microsoft domains suppose get tracking ID: `?WT.mc_id=academic-105485-koreyst`
- No country-specific locales for URLs (no use `/en-us/`)
- Images dey store for `./images` folder wit good names
- Use English characters, numbers, and dashes for file names

### Translation Support

- Dis repo dey support 40+ languages wit automated GitHub Actions
- Translations dey store for `translations/` folder
- No submit half translations
- Machine translations no dey accepted
- Translated images dey store for `translated_images/` folder

## Testing and Validation

### Pre-submission Checks

Dis repo dey use GitHub Actions for validation. Before you submit PRs:

1. **Check Markdown Links**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Manual Testing**:
   - Test Python examples: Activate venv and run scripts
   - Test TypeScript examples: `npm install`, `npm run build`, `npm start`
   - Make sure environment variables dey set well
   - Check say API keys dey work wit di code examples

3. **Code Examples**:
   - Make sure all code dey run well without errors
   - Test wit both Azure OpenAI and OpenAI API if e dey possible
   - Make sure examples dey work wit GitHub Models if e dey supported

### No Automated Tests

Dis repo na for learning tutorials and examples. E no get unit tests or integration tests to run. Validation na mainly:
- Manual testing of code examples
- GitHub Actions for Markdown validation
- Community review of di educational content

## Pull Request Guidelines

### Before Submitting

1. Test code changes for both Python and TypeScript if e dey possible
2. Run Markdown validation (e go run automatically for PR)
3. Make sure tracking IDs dey for all Microsoft URLs
4. Check say relative links dey valid
5. Confirm say images dey referenced well

### PR Title Format

- Use descriptive titles: `[Lesson 06] Fix Python example typo` or `Update README for lesson 08`
- Reference issue numbers if e dey possible: `Fixes #123`

### PR Description

- Explain wetin you change and why
- Link to di related issues
- For code changes, talk which examples you test
- For translation PRs, include all files for complete translation

### Contribution Requirements

- Sign Microsoft CLA (e dey automatic for first PR)
- Fork di repo to your account before you make changes
- One PR for one change (no join different fixes together)
- Make PRs simple and focused if e dey possible

## Common Workflows

### Adding a New Code Example

1. Go di correct lesson folder
2. Create example for `python/` or `typescript/` subfolder
3. Follow naming convention: `{provider}-{example-name}.{py|ts|js}`
4. Test wit di real API credentials
5. Write down any new environment variables for di lesson README

### Updating Documentation

1. Edit README.md for di lesson folder
2. Follow Markdown guidelines (tracking IDs, relative links)
3. Update translations dey handled by GitHub Actions (no edit manually)
4. Test say all links dey valid

### Working with Dev Containers

1. Di repo get `.devcontainer/devcontainer.json`
2. Post-create script dey automatically install Python dependencies
3. Extensions for Python and Jupyter don already dey set up
4. Environment dey based on `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Deployment and Publishing

Dis na learning repo - e no get deployment process. Di curriculum dey used by:

1. **GitHub Repository**: Direct access to code and documentation
2. **GitHub Codespaces**: Instant dev environment wit pre-configured setup
3. **Microsoft Learn**: Content fit dey syndicated to official learning platform
4. **docsify**: Documentation site wey dem build from Markdown (check `docsifytopdf.js` and `package.json`)

### Building Documentation Site

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Troubleshooting

### Common Issues

**Python Import Errors**:
- Make sure virtual environment dey activated
- Run `pip install -r requirements.txt`
- Check say Python version na 3.9+

**TypeScript Build Errors**:
- Run `npm install` for di specific app folder
- Check say Node.js version dey compatible
- Clear `node_modules` and reinstall if e dey needed

**API Authentication Errors**:
- Confirm say `.env` file dey and e get correct values
- Check say API keys dey valid and never expire
- Make sure endpoint URLs dey correct for your region

**Missing Environment Variables**:
- Copy `.env.copy` to `.env`
- Put all di required values for di lesson wey you dey work on
- Restart your app after you update `.env`

## Additional Resources

- [Course Setup Guide](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Contributing Guidelines](./CONTRIBUTING.md)
- [Code of Conduct](./CODE_OF_CONDUCT.md)
- [Security Policy](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Collection of Advanced Code Samples](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Project-Specific Notes

- Dis na **educational repo** wey dey focus on learning, no be production code
- Examples dey simple and dey focus on teaching ideas
- Code quality dey balanced wit educational clarity
- Each lesson dey complete and you fit finish am one by one
- Di repo dey support different API providers: Azure OpenAI, OpenAI, and GitHub Models
- Content dey multilingual wit automated translation workflows
- Active community dey for Discord for questions and support

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transle-shon service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transle-shon. Even as we dey try make am correct, abeg make you sabi say AI transle-shon fit get mistake or no dey accurate well. Di original dokyument wey dey for im native language na di one wey you go take as di correct source. For important mata, e good make you use professional human transle-shon. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transle-shon.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->