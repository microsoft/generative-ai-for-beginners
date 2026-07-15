# Pinahusay na Mga Tampok at Roadmap ng Mga Pagpapabuti

Ang dokumentong ito ay naglalahad ng mga inirerekomendang pag-enhance at pagpapabuti para sa kurikulum na Generative AI para sa Mga Baguhan, batay sa komprehensibong pagsusuri ng code at analisis ng mga pinakamahuhusay na gawain sa industriya.

## Buod ng Tagapamahala

Nasuri ang codebase para sa seguridad, kalidad ng code, at bisa sa edukasyon. Nagbibigay ang dokumentong ito ng mga rekomendasyon para sa agarang pag-aayos, mga pagpapabuti sa malapit na panahon, at mga hinaharap na enhancement.

---

## 1. Mga Pagpapahusay sa Seguridad (Prayoridad: Kritikal)

### 1.1 Agarang Pag-aayos (Natapos Na)

| Isyu | Mga Apektadong File | Katayuan |
|-------|----------------|--------|
| Hardcoded SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | Naayos |
| Nawawalang validasyon ng env | Maraming JS/TS files | Naayos |
| Hindi ligtas na tawag sa function | `11-integrating-with-function-calling/js-githubmodels/app.js` | Naayos |
| Tagas ng file handle | `08-building-search-applications/scripts/` | Naayos |
| Nawawalang request timeouts | `09-building-image-applications/python/` | Naayos |

### 1.2 Inirerekomendang Karagdagang Mga Tampok sa Seguridad

1. **Mga Halimbawa ng Rate Limiting**
   - Magdagdag ng sample code na nagpapakita kung paano mag-implement ng rate limiting para sa mga API call
   - Ipakita ang mga pattern ng exponential backoff

2. **Pag-ikot ng API Key**
   - Magdagdag ng dokumentasyon tungkol sa mga pinakamahusay na kasanayan sa pag-ikot ng mga API key
   - Isama ang mga halimbawa ng paggamit ng Azure Key Vault o katulad na serbisyo

3. **Integrasyon ng Content Safety**
   - Magdagdag ng mga halimbawa gamit ang Azure Content Safety API
   - Ipakita ang mga pattern ng input/output moderation

---

## 2. Mga Pagpapabuti sa Kalidad ng Code

### 2.1 Mga Idinagdag na Configuration Files

| File | Layunin |
|------|---------|
| `.eslintrc.json` | Mga patakaran sa linting ng JavaScript/TypeScript |
| `.prettierrc` | Mga pamantayan sa pag-format ng code |
| `pyproject.toml` | Konfigurasyon ng tooling para sa Python (Black, Ruff, mypy) |

### 2.2 Mga Nai-set Up na Shared Utilities

Bagong `shared/python/` module na may:
- `env_utils.py` - Paghawak ng mga environment variable
- `input_validation.py` - Validation at sanitization ng input
- `api_utils.py` - Safe wrappers para sa mga API request

### 2.3 Inirerekomendang Mga Pagpapabuti sa Code

1. **Saklaw ng Type Hints**
   - Magdagdag ng type hints sa lahat ng Python files
   - I-enable ang mahigpit na TypeScript mode sa lahat ng proyekto ng TS

2. **Mga Pamantayan sa Dokumentasyon**
   - Magdagdag ng docstrings sa lahat ng Python functions
   - Magdagdag ng JSDoc comments sa lahat ng JavaScript/TypeScript functions

3. **Testing Framework**
   - Magdagdag ng pytest configuration at mga halimbawa ng tests _(natapos: pytest config sa `pyproject.toml`; halimbawa ng tests para sa shared utilities sa [`tests/`](../../../tests) na tumatakbo sa CI)_
   - Magdagdag ng Jest configuration para sa JavaScript/TypeScript

---

## 3. Mga Pagpapahusay sa Edukasyon

### 3.1 Mga Bagong Paksa sa Aralin

1. **Seguridad sa AI Applications** (Inirerekomendang Aralin 22)
   - Mga pag-atake sa prompt injection at mga depensa
   - Pamamahala ng API key
   - Moderasyon ng nilalaman
   - Rate limiting at pag-iwas sa pang-aabuso

2. **Production Deployment** (Inirerekomendang Aralin 23)
   - Containerization gamit ang Docker
   - CI/CD pipelines
   - Monitoring at logging
   - Pamamahala ng gastos

3. **Advanced RAG Techniques** (Inirerekomendang Aralin 24)
   - Hybrid search (keyword + semantic)
   - Mga estratehiya sa re-ranking
   - Multi-modal RAG
   - Mga sukatan sa ebalwasyon

### 3.2 Mga Pinagandang Umiiral na Aralin

| Aralin | Inirerekomendang Pagpapabuti |
|--------|------------------------|
| 06 - Text Generation | Magdagdag ng mga halimbawa ng streaming response |
| 07 - Chat Applications | Magdagdag ng mga pattern sa memorya ng pag-uusap |
| 08 - Search Applications | Magdagdag ng paghahambing ng vector database |
| 09 - Image Generation | Magdagdag ng mga halimbawa ng pag-edit/pag-iba ng imahe |
| 11 - Function Calling | Magdagdag ng parallel function calling |
| 15 - RAG | Magdagdag ng paghahambing ng chunking strategy |
| 17 - AI Agents | Magdagdag ng multi-agent orchestration |

---

## 4. Modernisasyon ng API

### 4.1 Mga Deprecated na Pattern ng API (Natapos na ang Migrasyon)

Lahat ng Python at TypeScript **chat** samples ay na-migrate mula sa Chat Completions API patungo sa **Responses API** (`client.responses.create(...)` → `response.output_text`).

| Lumang Pattern | Bagong Pattern | Katayuan |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (chat) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | Natapos |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | Natapos |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | `openai` package `client.responses.create()` → `response.output_text` | Natapos |
| `df.append()` (pandas) | `pd.concat()` | Natapos |

> **Tandaan:** Ang mga Microsoft Foundry Models samples na gumagamit ng `azure-ai-inference` / `@azure-rest/ai-inference` SDK (`client.complete()`) ay nananatili sa Model Inference API, na hindi sumusuporta sa Responses API. Ang `AzureOpenAI()` ay sinadyang pinanatili kung saan ito pa rin valid (embeddings at pagbuo ng imahe).

### 4.2 Mga Bagong Tampok ng API na Ipapakita

1. **Structured Outputs** (OpenAI)
   - JSON mode
   - Function calling na may mahigpit na mga schema

2. **Kakayahan sa Vision**
   - Pagsusuri ng imahe gamit ang GPT-4o (vision)
   - Multi-modal prompts

3. **Built-in Tools ng Responses API** (pumapalit sa legacy Assistants API)
   - Code interpreter
   - Paghahanap ng file
   - Web search at custom na mga tool

---

## 5. Mga Pagpapahusay sa Imprastruktura

### 5.1 Mga Pagpapahusay sa CI/CD

Ipinasok sa [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml): Ang Python linting/formatting (Ruff + Black) ay **pinilit** sa pinapanatili na `shared/` utilities module at tumatakbo bilang **advisory** sa buong kurikulum, kasama ang advisory ESLint pass para sa JavaScript/TypeScript. Ang ilustratibong baseline ay:

```yaml
# .github/workflows/code-quality.yml
name: Code Quality

on: [push, pull_request]

jobs:
  python-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - run: pip install ruff black mypy
      - run: ruff check .
      - run: black --check .

  js-lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npx eslint .
```

### 5.2 Security Scanning

Ipinasok sa [`.github/workflows/security.yml`](../../../.github/workflows/security.yml): CodeQL analysis para sa Python at JavaScript/TypeScript (sa push, pull request, at lingguhang iskedyul) pati na rin ang dependency review sa mga pull request. Ang ilustratibong baseline ay:

```yaml
# .github/workflows/security.yml
name: Security Scan

on: [push, pull_request]

jobs:
  codeql:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v3
        with:
          languages: javascript, python
      - uses: github/codeql-action/analyze@v3

  dependency-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/dependency-review-action@v4
```

---

## 6. Mga Pagpapahusay sa Karanasan ng Developer

### 6.1 Mga Pagpapahusay sa DevContainer

Ipinasok sa [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) at [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh): Ang container ay naglalaman na ng Pylance, Black formatter, Ruff, ESLint, Prettier, at Copilot extensions, nag-enable ng format-on-save na nakakabit sa Black/Prettier config ng repo, at nag-iinstala ng mga developer tooling (`ruff`, `black`, `mypy`, `pytest`) upang maparami ang [code-quality workflow](../../../.github/workflows/code-quality.yml) nang lokal. Ang `mcr.microsoft.com/devcontainers/universal` base image ay bundling na ng Python at Node, kaya walang kailangang dagdag na features. Ang ilustratibong baseline ay:

```json
{
  "name": "Generative AI for Beginners",
  "image": "mcr.microsoft.com/devcontainers/universal:2",
  "features": {
    "ghcr.io/devcontainers/features/python:1": {
      "version": "3.11"
    },
    "ghcr.io/devcontainers/features/node:1": {
      "version": "20"
    }
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-toolsai.jupyter",
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode",
        "github.copilot"
      ],
      "settings": {
        "python.formatting.provider": "black",
        "editor.formatOnSave": true
      }
    }
  },
  "postCreateCommand": "pip install -e .[dev] && npm install"
}
```

### 6.2 Interactive Playground

Isaalang-alang ang pagdaragdag ng:
- Jupyter notebooks na may pre-filled na API keys (sa pamamagitan ng environment)
- Gradio/Streamlit demos para sa visual learners
- Interactive quizzes para sa pagsusuri ng kaalaman

---

## 7. Suporta para sa Maramihang Wika

### 7.1 Kasalukuyang Saklaw ng Wika

| Teknolohiya | Mga Natutunang Saklaw | Katayuan |
|------------|-----------------|--------|
| Python | Lahat | Kumpleto |
| TypeScript | 06-09, 11 | Bahagya |
| JavaScript | 06-08, 11 | Bahagya |
| .NET/C# | Ilan | Bahagya |

### 7.2 Inirerekomendang Mga Karagdagan

1. **Go** - Lumalawak sa AI/ML tooling
2. **Rust** - Para sa mga aplikasyong kritikal sa performance
3. **Java/Kotlin** - Para sa mga enterprise applications

---

## 8. Mga Pag-optimize sa Performance

### 8.1 Mga Pag-optimize sa Antas ng Code

1. **Mga Pattern ng Async/Await**
   - Magdagdag ng async na mga halimbawa para sa batch processing
   - Ipakita ang concurrent na mga tawag sa API

2. **Mga Estratehiya sa Caching**
   - Magdagdag ng mga halimbawa ng embedding caching
   - Ipakita ang mga pattern ng response caching

3. **Pag-optimize ng Token**
   - Magdagdag ng mga halimbawa ng paggamit ng tiktoken
   - Ipakita ang mga teknik sa prompt compression

### 8.2 Mga Halimbawa ng Pag-optimize sa Gastos

Magdagdag ng mga halimbawa na nagpapakita ng:
- Pagpili ng modelo batay sa komplikasyon ng gawain
- Prompt engineering para sa token efficiency
- Batch processing para sa maramihang operasyon

---

## 9. Accessibility at Internationalization

### 9.1 Kasalukuyang Kalagayan ng Pagsasalin

Lahat ng mga pagsasalin ay **kumpleto** at awtomatikong nilikha ng [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst), na gumagawa at nagpapanatili ng higit sa 50 na mga bersyon ng wika ng kurikulum na naka-sync sa orihinal na Ingles. Ang mga isinaling nilalaman ay matatagpuan sa ilalim ng `translations/` at ang mga nilokalisa na larawan sa `translated_images/`; ang buong listahan ng mga magagamit na wika ay inilathala sa itaas ng README ng repository.

| Aspeto | Katayuan |
|--------|--------|
| Saklaw ng pagsasalin | Kumpleto — 50+ na wika, lahat ng aralin |
| Paraan ng pagsasalin | Awtomatikong gamit ang [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) |
| Pinananatiling naka-sync sa English source | Oo — awtomatikong nire-regenerate |

### 9.2 Mga Pagpapahusay sa Accessibility

1. Magdagdag ng alt text sa lahat ng mga larawan
2. Siguraduhing may tamang syntax highlighting ang mga halimbawa ng code
3. Magdagdag ng transcripts ng video para sa lahat ng nilalaman ng video
4. Siguraduhing ang color contrast ay sumusunod sa mga patnubay ng WCAG

---

## 10. Prayoridad ng Pagpapatupad

### Phase 1: Agarang Gawain (Linggo 1-2)
- [x] Ayusin ang mga kritikal na isyu sa seguridad
- [x] Magdagdag ng configuration sa kalidad ng code
- [x] Gumawa ng shared utilities
- [x] I-dokumento ang mga patnubay sa seguridad

### Phase 2: Pang-maikling Panahon (Linggo 3-4)
- [x] I-update ang mga deprecated na pattern sa API (Chat Completions → Responses API, Python + TypeScript)
- [ ] Magdagdag ng type hints sa lahat ng Python files (natapos para sa pinapanatiling `shared/` module; ang mga lesson samples ay pinanatiling simple)
- [x] Magdagdag ng CI/CD workflows para sa kalidad ng code
- [x] Gumawa ng security scanning workflow

### Phase 3: Pang-medium Panahon (Buwan 2-3)
- [ ] Magdagdag ng bagong security na aralin
- [ ] Magdagdag ng aralin sa production deployment
- [x] Pagandahin ang DevContainer setup
- [ ] Magdagdag ng interactive na demos

### Phase 4: Pang-matagalang Panahon (Buwan 4+)
- [ ] Magdagdag ng advanced RAG na aralin
- [ ] Palawakin ang saklaw ng wika
- [ ] Magdagdag ng komprehensibong test suite
- [ ] Gumawa ng programang sertipikasyon

---

## Konklusyon

Nagbibigay ang roadmap na ito ng istrakturadong pamamaraan upang mapabuti ang kurikulum ng Generative AI para sa Mga Baguhan. Sa pamamagitan ng pagtugon sa mga isyu sa seguridad, modernisasyon ng mga API, at pagdaragdag ng nilalaman na pang-edukasyon, mas mahusay na mapaghahandaan ng kurso ang mga estudyante para sa pagbuo ng mga totoong aplikasyon ng AI.

Para sa mga katanungan o kontribusyon, mangyaring magbukas ng isyu sa GitHub repository.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->