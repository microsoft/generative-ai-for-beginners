# AGENTS.md

## Pangkalahatang-ideya ng Proyekto

Ang repositoryong ito ay naglalaman ng komprehensibong 21-lesson na kurikulum na nagtuturo ng mga pundasyon ng Generative AI at pagbuo ng aplikasyon. Ang kurso ay idinisenyo para sa mga baguhan at sumasaklaw mula sa mga batayang konsepto hanggang sa paggawa ng mga aplikasyon na handa na para sa produksyon.

**Pangunahing Teknolohiya:**
- Python 3.9+ na may mga library: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript na may Node.js at mga library: `openai` (Azure OpenAI sa pamamagitan ng v1 endpoint + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI Service, OpenAI API, at Microsoft Foundry Models (Ang GitHub Models ay magreretiro sa katapusan ng Hulyo 2026)
- Jupyter Notebooks para sa interaktibong pag-aaral
- Dev Containers para sa pare-parehong development environment

**Estruktura ng Repositoryo:**
- 21 naka-number na lesson directories (00-21) na naglalaman ng mga README, halimbawa ng code, at mga asignatura
- Maramihang implementasyon: Python, TypeScript, at kung minsan ay mga halimbawa sa .NET
- Translations directory na may 40+ bersyon ng wika
- Sentralisadong konfigurasyon gamit ang `.env` na file (gamitin ang `.env.copy` bilang template)

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

# I-install ang mga dependencies
pip install -r requirements.txt
```

### Setup ng Node.js/TypeScript

```bash
# I-install ang mga root-level na dependencies (para sa mga tool sa dokumentasyon)
npm install

# Para sa mga indibidwal na halimbawa ng TypeScript ng aralin, pumunta sa partikular na aralin:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Setup ng Dev Container (Inirerekomenda)

Kasama sa repositoryo ang `.devcontainer` na konfigurasyon para sa GitHub Codespaces o VS Code Dev Containers:

1. Buksan ang repositoryo sa GitHub Codespaces o VS Code gamit ang Dev Containers extension
2. Awtomatikong gagawin ng Dev Container ang mga sumusunod:
   - I-install ang mga dependensiya ng Python mula sa `requirements.txt`
   - Patakbuhin ang post-create script (`.devcontainer/post-create.sh`)
   - I-set up ang kernel ng Jupyter

## Daloy ng Pag-develop

### Mga Environment Variable

Ang lahat ng mga leksyon na nangangailangan ng access sa API ay gumagamit ng mga environment variable na nakasaad sa `.env`:

- `OPENAI_API_KEY` - Para sa OpenAI API
- `AZURE_OPENAI_API_KEY` - Para sa Azure OpenAI sa Microsoft Foundry (Ang Azure OpenAI Service ay bahagi na ng Microsoft Foundry ngayon: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - URL ng Azure OpenAI endpoint (Foundry resource endpoint)
- `AZURE_OPENAI_DEPLOYMENT` - Pangalan ng chat completion model deployment (default ng kurso: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Pangalan ng embeddings model deployment (default ng kurso: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - Bersyon ng API (default: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Para sa Hugging Face models
- `AZURE_INFERENCE_ENDPOINT` - Endpoint para sa Microsoft Foundry Models (catalog ng multi-provider models)
- `AZURE_INFERENCE_CREDENTIAL` - API key para sa Microsoft Foundry Models (pumapalit sa magreretirong `GITHUB_TOKEN`)
- `AZURE_INFERENCE_CHAT_MODEL` - Isang non-reasoning model (hal. `Llama-3.3-70B-Instruct`) na ginagamit sa mga halimbawa ng `temperature`, dahil ang mga reasoning model ay hindi sumusuporta sa sampling controls

### Mga Palatuntunan sa Modelo (mahalaga)

- **Default chat model ay `gpt-5-mini`** - isang kasalukuyan, hindi deprecated na **reasoning** model. Simula 2026, ang mga lumang temperature-capable na "mini" models (`gpt-4o-mini`, `gpt-4.1-mini`) ay *pinapawalang-saysay*, kaya ang kurikulum ay nagsasaayos sa pamilya ng GPT-5.
- **Ang mga reasoning models ay tinatanggihan ang `temperature` at `top_p`**, at gumagamit ng `max_output_tokens` (Responses API) / `max_completion_tokens` (chat completions) sa halip na `max_tokens`. Huwag magdagdag ng `temperature`/`top_p`/`max_tokens` sa mga sample na tumatawag sa `gpt-5-mini`.
- **Para ipakita ang `temperature`**, ang mga sample ay gumagamit ng isang **Llama** model (`Llama-3.3-70B-Instruct`) sa pamamagitan ng Microsoft Foundry Models endpoint (`AZURE_INFERENCE_CHAT_MODEL`). I-steer ang reasoning models gamit ang prompt engineering + reasoning controls sa halip na sampling knobs.
- **Fine-tuning (lesson 18)** ay nananatili sa `gpt-4.1-mini`: Ang GPT-5 ay sumusuporta lamang sa reinforcement fine-tuning (RFT), hindi sa supervised fine-tuning (SFT) na ipinapakita doon.
- Ang Lessons 20 (Mistral) at 21 (Meta) ay nananatili sa `temperature`/`max_tokens` dahil tinatarget nila ang Mistral/Llama models, na sumusuporta rito.

### Pagpapatakbo ng Mga Halimbawa ng Python

```bash
# Mag-navigate sa direktoryo ng aralin
cd 06-text-generation-apps/python

# Patakbuhin ang isang Python na script
python aoai-app.py
```

### Pagpapatakbo ng Mga Halimbawa ng TypeScript

```bash
# Mag-navigate sa direktoryo ng TypeScript app
cd 06-text-generation-apps/typescript/recipe-app

# I-build ang TypeScript code
npm run build

# Patakbuhin ang aplikasyon
npm start
```

### Pagpapatakbo ng Jupyter Notebooks

```bash
# Simulan ang Jupyter sa ugat ng repositoryo
jupyter notebook

# O gamitin ang VS Code na may Jupyter extension
```

### Paggawa sa Iba't ibang Uri ng mga Leksyon

- **"Learn" na mga leksyon**: Nakatuon sa dokumentasyon ng README.md at mga konsepto
- **"Build" na mga leksyon**: May kasamang gumaganang mga halimbawa ng code sa Python at TypeScript
- Bawat leksyon ay may README.md na may teorya, walkthroughs ng code, at mga link sa video content

## Mga Alituntunin sa Estilo ng Code

### Python

- Gamitin ang `python-dotenv` para sa pamamahala ng environment variable
- I-import ang `openai` library para sa API interactions
- Gamitin ang `pylint` para sa linting (ang ilang mga halimbawa ay may `# pylint: disable=all` para sa pagiging simple)
- Sundin ang PEP 8 na panuntunan sa pangalan
- Itago ang mga API kredensyal sa `.env` file, huwag ilagay sa code

### TypeScript

- Gamitin ang `dotenv` package para sa mga environment variable
- TypeScript konfigurasyon sa `tsconfig.json` para sa bawat app
- Gamitin ang `openai` package para sa Azure OpenAI (ita-target ang client sa `/openai/v1/` endpoint at tawagan ang `client.responses.create`); gamitin ang `@azure-rest/ai-inference` para sa Microsoft Foundry Models
- Gamitin ang `nodemon` para sa development na may auto-reload
- I-build bago patakbuhin: `npm run build` pagkatapos ay `npm start`

### Mga Pangkalahatang Palatuntunan

- Panatilihing simple at pang-edukasyon ang mga halimbawa ng code
- Isama ang mga komento na nagpapaliwanag ng mahahalagang konsepto
- Dapat ang code ng bawat leksyon ay self-contained at maaaring patakbuhin
- Gumamit ng pare-parehong pangalan: `aoai-` prefix para sa Azure OpenAI, `oai-` para sa OpenAI API, `githubmodels-` para sa Microsoft Foundry Models (legacy na prefix mula sa GitHub Models era)

## Mga Alituntunin sa Dokumentasyon

### Estilo ng Markdown

- Lahat ng URL ay dapat balutin sa format na `[text](../../url)` na walang sobrang espasyo
- Ang mga relative na link ay dapat magsimula sa `./` o `../`
- Lahat ng link patungo sa Microsoft domains ay dapat may tracking ID: `?WT.mc_id=academic-105485-koreyst`
- Iwasan ang mga country-specific na lokal sa URL (iwasan ang `/en-us/`)
- Ang mga larawan ay nakaimbak sa `./images` folder na may mga deskriptibong pangalan
- Gamitin ang mga English na karakter, numero, at gitling sa mga pangalan ng file

### Suporta sa Pagsasalin

- Sinusuportahan ng repositoryo ang 40+ na wika gamit ang automated GitHub Actions
- Ang mga pagsasalin ay nakaimbak sa `translations/` na direktoryo
- Huwag magsumite ng mga bahagyang pagsasalin
- Hindi tinatanggap ang mga machine translations
- Ang mga isinalin na larawan ay nakaimbak sa `translated_images/` na direktoryo

## Pagsusuri at Pagpapatunay

### Mga Pre-submission Check

Ang repositoryong ito ay gumagamit ng GitHub Actions para sa pagpapatunay. Bago magsumite ng PRs:

1. **Suriin ang Markdown Links**:
   ```bash
   # Sinusuri ng validate-markdown.yml na workflow:
   # - Mga sirang relative path
   # - Nawawalang mga tracking ID sa mga path
   # - Nawawalang mga tracking ID sa mga URL
   # - Mga URL na may country locale
   # - Mga sirang panlabas na URL
   ```

2. **Manwal na Pagsubok**:
   - Subukan ang mga Python halimbawa: I-activate ang venv at patakbuhin ang mga script
   - Subukan ang mga TypeScript halimbawa: `npm install`, `npm run build`, `npm start`
   - Siguraduhing tama ang pagkaka-konfigura ng mga environment variable
   - Suriin kung gumagana ang mga API key sa mga halimbawa ng code

3. **Mga Halimbawa ng Code**:
   - Siguraduhing ang lahat ng code ay tumatakbo nang walang error
   - Subukan gamit ang parehong Azure OpenAI at OpenAI API kung naaangkop
   - Siguraduhin na gumagana ang mga halimbawa sa Microsoft Foundry Models kapag suportado

### Walang Awtomatikong Pagsubok

Ito ay isang edukasyonal na repositoryo na nakatuon sa mga tutorial at halimbawa. Walang unit test o integration test na ipinatatakbo. Ang pagpapatunay ay pangunahing:
- Manwal na pagsusuri ng mga halimbawa ng code
- GitHub Actions para sa pagpapatunay ng Markdown
- Pagsusuri ng komunidad sa nilalaman ng edukasyon

## Mga Alituntunin sa Pull Request

### Bago Magsumite

1. Subukan ang mga pagbabago sa code sa parehong Python at TypeScript kung naaangkop
2. Patakbuhin ang pagpapatunay ng Markdown (awtomatikong pinapalakad sa PR)
3. Siguraduhing naroroon ang mga tracking ID sa lahat ng Microsoft URLs
4. Suriin na valid ang mga relative na link
5. Siguraduhin na tama ang pag-reference ng mga larawan

### Format ng Pamagat ng PR

- Gumamit ng mga deskriptibong pamagat: `[Lesson 06] Ayusin ang typo sa halimbawa ng Python` o `I-update ang README para sa lesson 08`
- Banggitin ang numero ng isyu kung naaangkop: `Ayusin ang #123`

### Deskripsyon ng PR

- Ipaliwanag kung ano ang binago at bakit
- Magbigay ng link sa mga kaugnay na isyu
- Para sa mga pagbabago sa code, tukuyin kung aling mga halimbawa ang sinubukan
- Para sa mga PR ng pagsasalin, isama ang lahat ng mga file para sa kumpletong pagsasalin

### Mga Kinakailangan sa Kontribusyon

- Pumirma sa Microsoft CLA (awtomatiko sa unang PR)
- I-fork ang repositoryo sa iyong account bago gumawa ng mga pagbabago
- Isang PR kada lohikal na pagbabago (huwag paghaluin ang mga hindi magkaugnay na pag-aayos)
- Panatilihing pokus at maliit ang mga PR kapag posible

## Karaniwang Daloy ng Trabaho

### Pagdaragdag ng Bagong Halimbawa ng Code

1. Pumunta sa angkop na lesson directory
2. Gumawa ng halimbawa sa `python/` o `typescript/` subdirectory
3. Sundin ang naming convention: `{provider}-{example-name}.{py|ts|js}`
4. Subukan gamit ang aktwal na API credentials
5. Idokumento ang anumang bagong environment variable sa lesson README

### Pag-update ng Dokumentasyon

1. I-edit ang README.md sa loob ng lesson directory
2. Sundin ang mga alituntuning Markdown (tracking IDs, relative links)
3. Ang mga pag-update sa pagsasalin ay hinahawakan ng GitHub Actions (huwag manual na i-edit)
4. Subukan na lahat ng link ay valid

### Paggawa sa Dev Containers

1. Kasama sa repositoryo ang `.devcontainer/devcontainer.json`
2. Awtomatikong ini-install ng post-create script ang mga dependensiya ng Python
3. Mga extension para sa Python at Jupyter ay naka-pre-configure
4. Ang environment ay nakabase sa `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Pag-deploy at Paglathala

Ito ay isang learning repository - walang proseso ng pag-deploy. Ang kurikulum ay maaaring gamitin sa pamamagitan ng:

1. **GitHub Repository**: Direktang access sa code at dokumentasyon
2. **GitHub Codespaces**: Instant na dev environment na may naka-pre-configure na setup
3. **Microsoft Learn**: Maaaring mai-syndicate ang nilalaman sa opisyal na learning platform
4. **docsify**: Site ng dokumentasyon na gawa mula sa Markdown (tingnan ang `docsifytopdf.js` at `package.json`)

### Pagbuo ng Dokumentasyon na Site

```bash
# Gumawa ng PDF mula sa dokumentasyon (kung kinakailangan)
npm run convert
```

## Pag-troubleshoot

### Mga Karaniwang Isyu

**Mga Error sa Pag-import ng Python**:
- Siguraduhin na naka-activate ang virtual environment
- Patakbuhin ang `pip install -r requirements.txt`
- Suriin na ang bersyon ng Python ay 3.9+

**Mga Error sa Build ng TypeScript**:
- Patakbuhin ang `npm install` sa partikular na app directory
- Suriin na compatible ang bersyon ng Node.js
- Linisin ang `node_modules` at i-reinstall kung kinakailangan

**Mga Error sa API Authentication**:
- Siguraduhing umiiral ang `.env` file at may tamang mga halaga
- Suriin na valid ang mga API key at hindi expired
- Siguraduhing tama ang mga endpoint URL para sa iyong rehiyon

**Nawawalang mga Environment Variable**:
- Kopyahin ang `.env.copy` bilang `.env`
- Punan ang lahat ng kinakailangang mga halaga para sa leksyon na iyong ginagawang
- I-restart ang iyong aplikasyon pagkatapos i-update ang `.env`

## Karagdagang Mga Mapagkukunan

- [Course Setup Guide](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Contributing Guidelines](./CONTRIBUTING.md)
- [Code of Conduct](./CODE_OF_CONDUCT.md)
- [Security Policy](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Collection of Advanced Code Samples](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Mga Tiyak na Tala sa Proyekto

- Ito ay isang **edukasyonal na repositoryo** na nakatuon sa pag-aaral, hindi sa code para sa produksyon
- Ang mga halimbawa ay sadyang simple at nakatuon sa pagtuturo ng mga konsepto
- Ang kalidad ng code ay balanseng may kalinawan para sa edukasyon
- Bawat leksyon ay self-contained at maaaring tapusin nang independente
- Sinusuportahan ng repositoryo ang maramihang API provider: Azure OpenAI, OpenAI, Microsoft Foundry Models, at offline providers tulad ng Foundry Local at Ollama
- Multilingual ang nilalaman na may automated na workflows sa pagsasalin
- Aktibo ang komunidad sa Discord para sa mga tanong at suporta

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->