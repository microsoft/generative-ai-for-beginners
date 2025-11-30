<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T10:48:58+00:00",
  "source_file": "AGENTS.md",
  "language_code": "en"
}
-->
# AGENTS.md

## Project Overview

This repository offers a comprehensive 21-lesson curriculum on Generative AI fundamentals and application development. The course is tailored for beginners, covering everything from foundational concepts to creating production-ready applications.

**Key Technologies:**
- Python 3.9+ with libraries: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript with Node.js and libraries: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API, and GitHub Models
- Jupyter Notebooks for interactive learning
- Dev Containers for a consistent development environment

**Repository Structure:**
- 21 numbered lesson directories (00-21) containing READMEs, code examples, and assignments
- Multiple implementations: Python, TypeScript, and occasionally .NET examples
- Translations directory with over 40 language versions
- Centralized configuration via `.env` file (use `.env.copy` as a template)

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

The repository includes a `.devcontainer` configuration for GitHub Codespaces or VS Code Dev Containers:

1. Open the repository in GitHub Codespaces or VS Code with the Dev Containers extension.
2. The Dev Container will automatically:
   - Install Python dependencies from `requirements.txt`
   - Run the post-create script (`.devcontainer/post-create.sh`)
   - Set up the Jupyter kernel

## Development Workflow

### Environment Variables

Lessons requiring API access use environment variables defined in `.env`:

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
- **"Build" lessons**: Include working code examples in Python and TypeScript
- Each lesson has a README.md with theory, code walkthroughs, and links to video content

## Code Style Guidelines

### Python

- Use `python-dotenv` for managing environment variables
- Import the `openai` library for API interactions
- Use `pylint` for linting (some examples include `# pylint: disable=all` for simplicity)
- Follow PEP 8 naming conventions
- Store API credentials in `.env` file, never in code

### TypeScript

- Use the `dotenv` package for environment variables
- TypeScript configuration is defined in `tsconfig.json` for each app
- Use `@azure/openai` or `@azure-rest/ai-inference` for Azure services
- Use `nodemon` for development with auto-reload
- Build before running: `npm run build` then `npm start`

### General Conventions

- Keep code examples simple and educational
- Include comments explaining key concepts
- Each lesson's code should be self-contained and runnable
- Use consistent naming: `aoai-` prefix for Azure OpenAI, `oai-` for OpenAI API, `githubmodels-` for GitHub Models

## Documentation Guidelines

### Markdown Style

- All URLs must be wrapped in `[text](../../url)` format with no extra spaces
- Relative links must start with `./` or `../`
- All links to Microsoft domains must include tracking ID: `?WT.mc_id=academic-105485-koreyst`
- Avoid country-specific locales in URLs (e.g., `/en-us/`)
- Images should be stored in the `./images` folder with descriptive names
- Use English characters, numbers, and dashes in file names

### Translation Support

- The repository supports over 40 languages via automated GitHub Actions
- Translations are stored in the `translations/` directory
- Do not submit partial translations
- Machine translations are not accepted
- Translated images are stored in the `translated_images/` directory

## Testing and Validation

### Pre-submission Checks

This repository uses GitHub Actions for validation. Before submitting PRs:

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
   - Test Python examples: Activate the virtual environment and run scripts
   - Test TypeScript examples: `npm install`, `npm run build`, `npm start`
   - Verify environment variables are configured correctly
   - Check that API keys work with the code examples

3. **Code Examples**:
   - Ensure all code runs without errors
   - Test with both Azure OpenAI and OpenAI API when applicable
   - Verify examples work with GitHub Models where supported

### No Automated Tests

This is an educational repository focused on tutorials and examples. There are no unit tests or integration tests to run. Validation is primarily:
- Manual testing of code examples
- GitHub Actions for Markdown validation
- Community review of educational content

## Pull Request Guidelines

### Before Submitting

1. Test code changes in both Python and TypeScript when applicable
2. Run Markdown validation (triggered automatically on PR)
3. Ensure tracking IDs are present on all Microsoft URLs
4. Check that relative links are valid
5. Verify images are properly referenced

### PR Title Format

- Use descriptive titles: `[Lesson 06] Fix Python example typo` or `Update README for lesson 08`
- Reference issue numbers when applicable: `Fixes #123`

### PR Description

- Explain what was changed and why
- Link to related issues
- For code changes, specify which examples were tested
- For translation PRs, include all files for a complete translation

### Contribution Requirements

- Sign the Microsoft CLA (automatic on first PR)
- Fork the repository to your account before making changes
- Submit one PR per logical change (don't combine unrelated fixes)
- Keep PRs focused and small when possible

## Common Workflows

### Adding a New Code Example

1. Navigate to the appropriate lesson directory
2. Create the example in the `python/` or `typescript/` subdirectory
3. Follow naming conventions: `{provider}-{example-name}.{py|ts|js}`
4. Test with actual API credentials
5. Document any new environment variables in the lesson README

### Updating Documentation

1. Edit the README.md in the lesson directory
2. Follow Markdown guidelines (tracking IDs, relative links)
3. Translation updates are handled by GitHub Actions (don't edit manually)
4. Test all links to ensure they are valid

### Working with Dev Containers

1. The repository includes `.devcontainer/devcontainer.json`
2. The post-create script installs Python dependencies automatically
3. Extensions for Python and Jupyter are pre-configured
4. The environment is based on `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Deployment and Publishing

This is a learning repository - there is no deployment process. The curriculum is consumed through:

1. **GitHub Repository**: Direct access to code and documentation
2. **GitHub Codespaces**: Instant development environment with pre-configured setup
3. **Microsoft Learn**: Content may be syndicated to the official learning platform
4. **docsify**: Documentation site built from Markdown (see `docsifytopdf.js` and `package.json`)

### Building Documentation Site

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Troubleshooting

### Common Issues

**Python Import Errors**:
- Ensure the virtual environment is activated
- Run `pip install -r requirements.txt`
- Check that the Python version is 3.9+

**TypeScript Build Errors**:
- Run `npm install` in the specific app directory
- Check that the Node.js version is compatible
- Clear `node_modules` and reinstall if needed

**API Authentication Errors**:
- Verify the `.env` file exists and has correct values
- Check that API keys are valid and not expired
- Ensure endpoint URLs are correct for your region

**Missing Environment Variables**:
- Copy `.env.copy` to `.env`
- Fill in all required values for the lesson you're working on
- Restart your application after updating `.env`

## Additional Resources

- [Course Setup Guide](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Contributing Guidelines](./CONTRIBUTING.md)
- [Code of Conduct](./CODE_OF_CONDUCT.md)
- [Security Policy](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Collection of Advanced Code Samples](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Project-Specific Notes

- This is an **educational repository** focused on learning, not production code
- Examples are intentionally simple and focused on teaching concepts
- Code quality is balanced with educational clarity
- Each lesson is self-contained and can be completed independently
- The repository supports multiple API providers: Azure OpenAI, OpenAI, and GitHub Models
- Content is multilingual with automated translation workflows
- Active community on Discord for questions and support

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.