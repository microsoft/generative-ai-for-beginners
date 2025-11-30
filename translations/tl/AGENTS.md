<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T11:08:15+00:00",
  "source_file": "AGENTS.md",
  "language_code": "tl"
}
-->
# AGENTS.md

## Pangkalahatang-ideya ng Proyekto

Ang repository na ito ay naglalaman ng isang komprehensibong kurikulum na binubuo ng 21 aralin na nagtuturo ng mga pangunahing kaalaman sa Generative AI at pagbuo ng mga aplikasyon. Ang kurso ay idinisenyo para sa mga baguhan at sumasaklaw mula sa mga pangunahing konsepto hanggang sa paggawa ng mga aplikasyon na handa para sa produksyon.

**Pangunahing Teknolohiya:**
- Python 3.9+ na may mga library: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript gamit ang Node.js at mga library: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API, at GitHub Models
- Jupyter Notebooks para sa interaktibong pag-aaral
- Dev Containers para sa pare-parehong kapaligiran sa pag-develop

**Struktura ng Repository:**
- 21 na may numerong direktoryo ng aralin (00-21) na naglalaman ng mga README, halimbawa ng code, at mga takdang-aralin
- Maramihang implementasyon: Python, TypeScript, at paminsan-minsan .NET na mga halimbawa
- Direktoryo ng mga pagsasalin na may higit sa 40 bersyon ng wika
- Sentralisadong konfigurasyon gamit ang `.env` file (gamitin ang `.env.copy` bilang template)

## Mga Utos sa Setup

### Paunang Setup ng Repository

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Setup ng Python Environment

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

### Setup ng Node.js/TypeScript

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Setup ng Dev Container (Inirerekomenda)

Ang repository ay may kasamang `.devcontainer` na konfigurasyon para sa GitHub Codespaces o VS Code Dev Containers:

1. Buksan ang repository sa GitHub Codespaces o VS Code gamit ang Dev Containers extension
2. Ang Dev Container ay awtomatikong:
   - Mag-i-install ng mga dependency ng Python mula sa `requirements.txt`
   - Magpapatakbo ng post-create script (`.devcontainer/post-create.sh`)
   - Magse-set up ng Jupyter kernel

## Workflow ng Pag-develop

### Mga Environment Variable

Ang lahat ng aralin na nangangailangan ng API access ay gumagamit ng mga environment variable na tinukoy sa `.env`:

- `OPENAI_API_KEY` - Para sa OpenAI API
- `AZURE_OPENAI_API_KEY` - Para sa Azure OpenAI Service
- `AZURE_OPENAI_ENDPOINT` - URL ng endpoint ng Azure OpenAI
- `AZURE_OPENAI_DEPLOYMENT` - Pangalan ng deployment ng chat completion model
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Pangalan ng deployment ng embeddings model
- `AZURE_OPENAI_API_VERSION` - Bersyon ng API (default: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Para sa Hugging Face models
- `GITHUB_TOKEN` - Para sa GitHub Models

### Pagpapatakbo ng Python Examples

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### Pagpapatakbo ng TypeScript Examples

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Pagpapatakbo ng Jupyter Notebooks

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### Paggawa sa Iba't Ibang Uri ng Aralin

- **"Learn" lessons**: Nakatuon sa README.md na dokumentasyon at mga konsepto
- **"Build" lessons**: May kasamang gumaganang halimbawa ng code sa Python at TypeScript
- Ang bawat aralin ay may README.md na naglalaman ng teorya, walkthrough ng code, at mga link sa video content

## Mga Alituntunin sa Estilo ng Code

### Python

- Gumamit ng `python-dotenv` para sa pamamahala ng environment variable
- I-import ang `openai` library para sa API interactions
- Gumamit ng `pylint` para sa linting (ang ilang mga halimbawa ay may kasamang `# pylint: disable=all` para sa pagiging simple)
- Sundin ang PEP 8 naming conventions
- Itago ang mga kredensyal ng API sa `.env` file, huwag sa code

### TypeScript

- Gumamit ng `dotenv` package para sa environment variables
- TypeScript configuration sa `tsconfig.json` para sa bawat app
- Gumamit ng `@azure/openai` o `@azure-rest/ai-inference` para sa Azure services
- Gumamit ng `nodemon` para sa pag-develop na may auto-reload
- I-build bago patakbuhin: `npm run build` pagkatapos `npm start`

### Pangkalahatang Konbensyon

- Panatilihing simple at pang-edukasyon ang mga halimbawa ng code
- Isama ang mga komento na nagpapaliwanag ng mga pangunahing konsepto
- Ang code ng bawat aralin ay dapat na self-contained at runnable
- Gumamit ng pare-parehong naming: `aoai-` prefix para sa Azure OpenAI, `oai-` para sa OpenAI API, `githubmodels-` para sa GitHub Models

## Mga Alituntunin sa Dokumentasyon

### Estilo ng Markdown

- Ang lahat ng URL ay dapat nakabalot sa `[text](../../url)` format na walang sobrang espasyo
- Ang mga relative link ay dapat magsimula sa `./` o `../`
- Ang lahat ng link sa Microsoft domains ay dapat may kasamang tracking ID: `?WT.mc_id=academic-105485-koreyst`
- Walang country-specific locales sa mga URL (iwasan ang `/en-us/`)
- Ang mga imahe ay nakaimbak sa `./images` folder na may mga deskriptibong pangalan
- Gumamit ng English characters, numbers, at dashes sa mga pangalan ng file

### Suporta sa Pagsasalin

- Ang repository ay sumusuporta sa higit sa 40 wika sa pamamagitan ng automated GitHub Actions
- Ang mga pagsasalin ay nakaimbak sa `translations/` directory
- Huwag magsumite ng partial translations
- Hindi tinatanggap ang machine translations
- Ang mga isinaling imahe ay nakaimbak sa `translated_images/` directory

## Pagsusuri at Pagpapatunay

### Mga Pre-submission Checks

Ang repository na ito ay gumagamit ng GitHub Actions para sa validation. Bago magsumite ng PRs:

1. **Suriin ang Markdown Links**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Manwal na Pagsusuri**:
   - Subukan ang mga halimbawa ng Python: I-activate ang venv at patakbuhin ang mga script
   - Subukan ang mga halimbawa ng TypeScript: `npm install`, `npm run build`, `npm start`
   - Siguraduhing tama ang pagkaka-configure ng mga environment variable
   - Suriin na gumagana ang mga API keys sa mga halimbawa ng code

3. **Mga Halimbawa ng Code**:
   - Siguraduhing gumagana ang lahat ng code nang walang error
   - Subukan gamit ang parehong Azure OpenAI at OpenAI API kung naaangkop
   - Suriin na gumagana ang mga halimbawa gamit ang GitHub Models kung suportado

### Walang Automated Tests

Ito ay isang educational repository na nakatuon sa tutorials at mga halimbawa. Walang unit tests o integration tests na kailangang patakbuhin. Ang validation ay pangunahing:
- Manwal na pagsusuri ng mga halimbawa ng code
- GitHub Actions para sa Markdown validation
- Pagsusuri ng komunidad sa educational content

## Mga Alituntunin sa Pull Request

### Bago Magsumite

1. Subukan ang mga pagbabago sa code sa parehong Python at TypeScript kung naaangkop
2. Patakbuhin ang Markdown validation (awtomatikong na-trigger sa PR)
3. Siguraduhing may tracking IDs ang lahat ng Microsoft URLs
4. Suriin na valid ang mga relative links
5. Siguraduhing tama ang pag-refer sa mga imahe

### Format ng PR Title

- Gumamit ng mga deskriptibong pamagat: `[Lesson 06] Fix Python example typo` o `Update README for lesson 08`
- I-refer ang mga numero ng isyu kung naaangkop: `Fixes #123`

### Deskripsyon ng PR

- Ipaliwanag kung ano ang binago at bakit
- Mag-link sa mga kaugnay na isyu
- Para sa mga pagbabago sa code, tukuyin kung aling mga halimbawa ang nasubukan
- Para sa mga PR ng pagsasalin, isama ang lahat ng file para sa kumpletong pagsasalin

### Mga Kinakailangan sa Kontribusyon

- Pirmahan ang Microsoft CLA (awtomatiko sa unang PR)
- I-fork ang repository sa iyong account bago gumawa ng mga pagbabago
- Isang PR bawat lohikal na pagbabago (huwag pagsamahin ang hindi kaugnay na mga pag-aayos)
- Panatilihing nakatuon at maliit ang mga PR kung maaari

## Karaniwang Workflow

### Pagdaragdag ng Bagong Halimbawa ng Code

1. Pumunta sa naaangkop na direktoryo ng aralin
2. Gumawa ng halimbawa sa `python/` o `typescript/` subdirectory
3. Sundin ang naming convention: `{provider}-{example-name}.{py|ts|js}`
4. Subukan gamit ang aktwal na mga kredensyal ng API
5. Idokumento ang anumang bagong environment variable sa README ng aralin

### Pag-update ng Dokumentasyon

1. I-edit ang README.md sa direktoryo ng aralin
2. Sundin ang mga alituntunin sa Markdown (tracking IDs, relative links)
3. Ang mga update sa pagsasalin ay pinangangasiwaan ng GitHub Actions (huwag i-edit nang manu-mano)
4. Subukan na valid ang lahat ng link

### Paggawa gamit ang Dev Containers

1. Ang repository ay may kasamang `.devcontainer/devcontainer.json`
2. Ang post-create script ay awtomatikong nag-i-install ng mga dependency ng Python
3. Ang mga extension para sa Python at Jupyter ay naka-pre-configure
4. Ang environment ay nakabase sa `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Deployment at Pag-publish

Ito ay isang learning repository - walang proseso ng deployment. Ang kurikulum ay ginagamit sa pamamagitan ng:

1. **GitHub Repository**: Direktang access sa code at dokumentasyon
2. **GitHub Codespaces**: Instant dev environment na may pre-configured setup
3. **Microsoft Learn**: Ang content ay maaaring i-syndicate sa opisyal na learning platform
4. **docsify**: Documentation site na binuo mula sa Markdown (tingnan ang `docsifytopdf.js` at `package.json`)

### Pagbuo ng Documentation Site

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Pag-troubleshoot

### Karaniwang Isyu

**Python Import Errors**:
- Siguraduhing naka-activate ang virtual environment
- Patakbuhin ang `pip install -r requirements.txt`
- Suriin na ang bersyon ng Python ay 3.9+

**TypeScript Build Errors**:
- Patakbuhin ang `npm install` sa partikular na direktoryo ng app
- Suriin na ang bersyon ng Node.js ay compatible
- I-clear ang `node_modules` at i-reinstall kung kinakailangan

**API Authentication Errors**:
- Siguraduhing may `.env` file at may tamang mga halaga
- Suriin na valid at hindi expired ang mga API keys
- Siguraduhing tama ang endpoint URLs para sa iyong rehiyon

**Missing Environment Variables**:
- Kopyahin ang `.env.copy` sa `.env`
- Punan ang lahat ng kinakailangang halaga para sa aralin na iyong ginagawa
- I-restart ang iyong aplikasyon pagkatapos i-update ang `.env`

## Karagdagang Resources

- [Course Setup Guide](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Contributing Guidelines](./CONTRIBUTING.md)
- [Code of Conduct](./CODE_OF_CONDUCT.md)
- [Security Policy](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Collection of Advanced Code Samples](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Mga Tala Tungkol sa Proyekto

- Ito ay isang **educational repository** na nakatuon sa pag-aaral, hindi production code
- Ang mga halimbawa ay sadyang simple at nakatuon sa pagtuturo ng mga konsepto
- Ang kalidad ng code ay balanse sa edukasyonal na kalinawan
- Ang bawat aralin ay self-contained at maaaring kumpletuhin nang mag-isa
- Ang repository ay sumusuporta sa maramihang API providers: Azure OpenAI, OpenAI, at GitHub Models
- Ang content ay multilingual na may automated translation workflows
- Aktibong komunidad sa Discord para sa mga tanong at suporta

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.