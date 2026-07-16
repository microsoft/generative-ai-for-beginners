# AGENTS.md

## Pangkalahatang-ideya ng Proyekto

Ang repositoryong ito ay naglalaman ng isang komprehensibong kurikulum na may 21 na aralin na nagtuturo ng mga pundasyon ng Generative AI at pagbuo ng aplikasyon. Ang kurso ay dinisenyo para sa mga baguhan at sumasaklaw mula sa mga pangunahing konsepto hanggang sa paggawa ng mga aplikasyon na handa na para sa produksyon.

**Pangunahing Teknolohiya:**
- Python 3.9+ na may mga library: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript gamit ang Node.js at mga library: `openai` (Azure OpenAI sa pamamagitan ng v1 endpoint + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI Service, OpenAI API, at Microsoft Foundry Models (Magreretiro ang GitHub Models sa katapusan ng Hulyo 2026)
- Jupyter Notebooks para sa interaktibong pagkatuto
- Dev Containers para sa pare-parehong kapaligiran sa pag-unlad

**Istraktura ng Repositoryo:**
- 21 na mga direktoryo na may bilang ng aralin (00-21) na naglalaman ng mga README, halimbawa ng code, at mga takdang-aralin
- Maraming implementasyon: Python, TypeScript, at minsan ay mga halimbawa ng .NET
- Direktoryo ng mga pagsasalin na may higit sa 40 na bersyon ng wika
- Sentralisadong konfigurasyon sa pamamagitan ng `.env` na file (gumamit ng `.env.copy` bilang template)

## Mga Utos sa Setup

### Paunang Setup ng Repositoryo

```bash
# Kopyahin ang repositoryo
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Kopyahin ang template ng kapaligiran
cp .env.copy .env
# I-edit ang .env gamit ang iyong mga API key at mga endpoint
```

### Setup ng Python Environment

```bash
# Gumawa ng virtual na kapaligiran
python3 -m venv venv

# I-activate ang virtual na kapaligiran
# Sa macOS/Linux:
source venv/bin/activate
# Sa Windows:
venv\Scripts\activate

# Mag-install ng mga dependencies
pip install -r requirements.txt
```

### Setup ng Node.js/TypeScript

```bash
# I-install ang mga dependencies sa antas ng ugat (para sa mga kasangkapang pantulong sa dokumentasyon)
npm install

# Para sa mga indibidwal na halimbawa ng lesson sa TypeScript, pumunta sa partikular na lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Setup ng Dev Container (Inirerekomenda)

Kasama sa repositoryo ang `.devcontainer` na konfigurasyon para sa GitHub Codespaces o VS Code Dev Containers:

1. Buksan ang repositoryo sa GitHub Codespaces o VS Code gamit ang Dev Containers extension
2. Ang Dev Container ay awtomatikong:
   - I-install ang mga kinakailangang dependencies ng Python mula sa `requirements.txt`
   - Patakbuhin ang post-create script (`.devcontainer/post-create.sh`)
   - Isaayos ang Jupyter kernel

## Daloy ng Pag-unlad

### Mga Environment Variable

Lahat ng aralin na nangangailangan ng API access ay gumagamit ng mga environment variable na tinukoy sa `.env`:

- `OPENAI_API_KEY` - Para sa OpenAI API
- `AZURE_OPENAI_API_KEY` - Para sa Azure OpenAI sa Microsoft Foundry (Ang Azure OpenAI Service ay bahagi na ngayon ng Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL ng Azure OpenAI endpoint (Foundry resource endpoint)
- `AZURE_OPENAI_DEPLOYMENT` - Pangalan ng deployment ng chat completion model
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Pangalan ng deployment ng embeddings model
- `AZURE_OPENAI_API_VERSION` - Bersyon ng API (default: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Para sa Hugging Face models
- `AZURE_INFERENCE_ENDPOINT` - Endpoint ng Microsoft Foundry Models (multi-provider model catalog)
- `AZURE_INFERENCE_CREDENTIAL` - API key ng Microsoft Foundry Models (pumapalit sa nagreretirong `GITHUB_TOKEN`)

### Pagpatakbo ng Mga Halimbawa sa Python

```bash
# Mag-navigate sa direktoryo ng aralin
cd 06-text-generation-apps/python

# Patakbuhin ang isang Python script
python aoai-app.py
```

### Pagpatakbo ng Mga Halimbawa sa TypeScript

```bash
# Mag-navigate sa direktoryo ng TypeScript app
cd 06-text-generation-apps/typescript/recipe-app

# I-build ang TypeScript na code
npm run build

# Patakbuhin ang aplikasyon
npm start
```

### Pagpatakbo ng Jupyter Notebooks

```bash
# Simulan ang Jupyter sa ugat ng repositoryo
jupyter notebook

# O gamitin ang VS Code na may Jupyter extension
```

### Paggamit ng Iba't Ibang Uri ng Aralin

- **Mga "Learn" na aralin**: Nakatuon sa dokumentasyon ng README.md at mga konsepto
- **Mga "Build" na aralin**: May kasamang gumaganang mga halimbawa ng code sa Python at TypeScript
- Bawat aralin ay may README.md na may teorya, walkthrough ng code, at mga link sa video content

## Mga Gabay sa Estilo ng Code

### Python

- Gumamit ng `python-dotenv` para sa pamamahala ng environment variable
- I-import ang `openai` na library para sa pakikipag-ugnayan sa API
- Gumamit ng `pylint` para sa linting (ang ilang halimbawa ay may `# pylint: disable=all` para sa pagiging simple)
- Sundin ang PEP 8 naming conventions
- Itago ang mga kredensyal ng API sa `.env` file, huwag kailanman sa code

### TypeScript

- Gumamit ng `dotenv` package para sa mga environment variable
- TypeScript configuration sa `tsconfig.json` para sa bawat app
- Gumamit ng `openai` package para sa Azure OpenAI (ituro ang client sa `/openai/v1/` endpoint at tawagin ang `client.responses.create`); gumamit ng `@azure-rest/ai-inference` para sa Microsoft Foundry Models
- Gumamit ng `nodemon` para sa pag-unlad na may auto-reload
- I-build bago patakbuhin: `npm run build` pagkatapos `npm start`

### Pangkalahatang Mga Konbensyon

- Panatilihing simple at pang-edukasyon ang mga halimbawa ng code
- Isama ang mga komento na nagpapaliwanag ng mga pangunahing konsepto
- Ang code ng bawat aralin ay dapat na nakahiwalay at maaaring patakbuhin
- Gumamit ng pare-parehong paggalang sa pangalan: `aoai-` prefix para sa Azure OpenAI, `oai-` para sa OpenAI API, `githubmodels-` para sa Microsoft Foundry Models (napanatili ang legacy prefix mula sa GitHub Models era)

## Mga Gabay sa Dokumentasyon

### Estilo ng Markdown

- Lahat ng URL ay dapat balutin sa format na `[text](../../url)` nang walang dagdag na spaces
- Ang mga relative link ay dapat magsimula sa `./` o `../`
- Lahat ng mga link sa mga domain ng Microsoft ay kailangang may tracking ID: `?WT.mc_id=academic-105485-koreyst`
- Walang country-specific na mga locale sa mga URL (iwasan ang `/en-us/`)
- Ang mga larawan ay nakaimbak sa `./images` na folder na may mga naglalarawang pangalan
- Gumamit ng mga English na karakter, numero, at gitling sa mga pangalan ng file

### Suporta sa Pagsasalin

- Sinusuportahan ng repositoryo ang higit sa 40 na wika gamit ang automated GitHub Actions
- Ang mga pagsasalin ay nakaimbak sa `translations/` na direktoryo
- Huwag magsumite ng mga bahagyang pagsasalin
- Hindi tinatanggap ang mga machine translation
- Ang mga isinaling larawan ay nakaimbak sa `translated_images/` na direktoryo

## Pagsubok at Pagpapatunay

### Pre-submission Checks

Ang repositoryo na ito ay gumagamit ng GitHub Actions para sa pagpapatunay. Bago magsumite ng PR:

1. **Suriin ang mga Link sa Markdown**:
   ```bash
   # Tine-tsek ng validate-markdown.yml na workflow:
   # - Sira o mali ang relative paths
   # - Nawawalang tracking IDs sa mga path
   # - Nawawalang tracking IDs sa mga URL
   # - URL na may country locale
   # - Sira o mali ang mga external URL
   ```

2. **Manwal na Pagsusuri**:
   - Subukan ang mga halimbawang Python: I-activate ang venv at patakbuhin ang mga script
   - Subukan ang mga halimbawang TypeScript: `npm install`, `npm run build`, `npm start`
   - Siguraduhing tama ang pagkaka-configure ng mga environment variable
   - Suriin na gumagana ang mga API key kasama ang mga halimbawa ng code

3. **Mga Halimbawa ng Code**:
   - Siguraduhing walang error sa pagpapatakbo ng lahat ng code
   - Subukan gamit ang parehong Azure OpenAI at OpenAI API kung naaangkop
   - Suriing gumagana ang mga halimbawa sa Microsoft Foundry Models kung suportado

### Walang Automated Tests

Ito ay isang pang-edukasyon na repositoryo na nakatuon sa mga tutorial at halimbawa. Walang unit tests o integration tests na kailangang patakbuhin. Ang pagpapatunay ay pangunahing:
- Manwal na pagsusuri ng mga halimbawa ng code
- GitHub Actions para sa validasyon ng Markdown
- Pagsusuri ng komunidad sa nilalaman ng edukasyon

## Mga Panuntunan sa Pull Request

### Bago Magsumite

1. Subukan ang mga pagbabago sa code sa parehong Python at TypeScript kung naaangkop
2. Patakbuhin ang validasyon ng Markdown (awtomatikong pinapagana sa PR)
3. Siguraduhing naroroon ang mga tracking ID sa lahat ng Microsoft URL
4. Suriin na balido ang mga relative link
5. Siguraduhing tama ang pag-reference ng mga larawan

### Format ng Pamagat ng PR

- Gumamit ng mga deskriptibong pamagat: `[Lesson 06] Ayusin ang typo sa halimbawang Python` o `Update README para sa aralin 08`
- Banggitin ang mga numero ng isyu kung naaangkop: `Fixes #123`

### Deskripsyon ng PR

- Ipaliwanag kung ano ang binago at bakit
- Mag-link sa mga kaugnay na isyu
- Para sa mga pagbabago sa code, tukuyin kung alin sa mga halimbawa ang nasubukan
- Para sa mga PR ng pagsasalin, isama ang lahat ng file para sa kumpletong pagsasalin

### Mga Kinakailangan sa Kontribusyon

- Lagdaan ang Microsoft CLA (awtomatiko sa unang PR)
- I-fork ang repositoryo sa iyong account bago gumawa ng mga pagbabago
- Isang PR kada lohikal na pagbabago (huwag pagsamahin ang mga hindi magkaugnay na fix)
- Panatilihing naka-focus at maliit ang mga PR kung maaari

## Karaniwang Daloy ng Trabaho

### Pagdaragdag ng Bagong Halimbawa ng Code

1. Pumunta sa naaangkop na direktoryo ng aralin
2. Gumawa ng halimbawa sa subdirectory na `python/` o `typescript/`
3. Sundin ang naming convention: `{provider}-{example-name}.{py|ts|js}`
4. Subukan gamit ang aktwal na API credentials
5. I-dokumento ang anumang bagong environment variable sa README ng aralin

### Pag-update ng Dokumentasyon

1. I-edit ang README.md sa direktoryo ng aralin
2. Sundin ang mga gabay sa Markdown (tracking ID, relative links)
3. Ang mga update sa pagsasalin ay hinahawakan ng GitHub Actions (huwag i-edit nang mano-mano)
4. Subukang tiyakin na lahat ng link ay balido

### Paggamit sa Dev Containers

1. Kasama sa repositoryo ang `.devcontainer/devcontainer.json`
2. Ang post-create script ay awtomatikong nag-i-install ng mga dependencies ng Python
3. Nakapre-configure ang mga extension para sa Python at Jupyter
4. Ang kapaligiran ay nakabase sa `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Deployment at Pag-publish

Ito ay isang repositoryo para sa pagkatuto - walang proseso ng deployment. Ang kurikulum ay ginagamit sa pamamagitan ng:

1. **GitHub Repository**: Direktang access sa code at dokumentasyon
2. **GitHub Codespaces**: Instant na dev environment na may paunang nakaayos na setup
3. **Microsoft Learn**: Maaaring isyndicate ang nilalaman sa opisyal na learning platform
4. **docsify**: Site ng dokumentasyon na ginawa mula sa Markdown (tingnan ang `docsifytopdf.js` at `package.json`)

### Pagbuo ng Documentation Site

```bash
# Lumikha ng PDF mula sa dokumentasyon (kung kinakailangan)
npm run convert
```

## Pag-troubleshoot

### Mga Karaniwang Isyu

**Mga Error sa Pag-import ng Python**:
- Siguraduhing naka-activate ang virtual environment
- Patakbuhin ang `pip install -r requirements.txt`
- Tiyaking ang bersyon ng Python ay 3.9+

**Mga Error sa Pagbuo ng TypeScript**:
- Patakbuhin ang `npm install` sa partikular na direktoryo ng app
- Tiyaking compatible ang bersyon ng Node.js
- Linisin ang `node_modules` at muling i-install kung kinakailangan

**Mga Error sa Pagpapatotoo ng API**:
- Siguraduhing umiiral ang `.env` file at may tamang mga halaga
- Suriing valid at hindi expired ang API key
- Siguraduhing tama ang mga URL ng endpoint para sa iyong rehiyon

**Kulang na Mga Environment Variable**:
- Kopyahin ang `.env.copy` sa `.env`
- Punan ang lahat ng kinakailangang halaga para sa araling iyong ginagawa
- I-restart ang iyong aplikasyon pagkatapos i-update ang `.env`

## Karagdagang Mga Mapagkukunan

- [Course Setup Guide](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Contributing Guidelines](./CONTRIBUTING.md)
- [Code of Conduct](./CODE_OF_CONDUCT.md)
- [Security Policy](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Collection of Advanced Code Samples](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Mga Tandaang-Specipikong Tala

- Ito ay isang **pang-edukasyon na repositoryo** na nakatuon sa pagkatuto, hindi sa produksyon na code
- Ang mga halimbawa ay sinadya na maging simple at nakatuon sa pagtuturo ng mga konsepto
- Ang kalidad ng code ay binabalanse sa kalinawan ng edukasyon
- Ang bawat aralin ay nakahiwalay at maaaring tapusin nang mag-isa
- Sinusuportahan ng repositoryo ang maraming API provider: Azure OpenAI, OpenAI, Microsoft Foundry Models, at offline providers tulad ng Foundry Local at Ollama
- Ang nilalaman ay multilingual na may awtomatikong daloy sa pagsasalin
- May aktibong komunidad sa Discord para sa mga tanong at suporta

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->