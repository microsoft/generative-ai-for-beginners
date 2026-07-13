# Forbedret funksjonalitet og forbedringsplan

Dette dokumentet skisserer anbefalte forbedringer og oppgraderinger for Generative AI for Beginners-kurset, basert på en omfattende kodegjennomgang og analyse av beste praksis i bransjen.

## Sammendrag

Kodebasen er analysert for sikkerhet, kodekvalitet og pedagogisk effektivitet. Dette dokumentet gir anbefalinger for umiddelbare rettelser, kortsiktige forbedringer og fremtidige oppgraderinger.

---

## 1. Sikkerhetsforbedringer (Prioritet: Kritisk)

### 1.1 Umiddelbare rettelser (Fullført)

| Problem | Berørte filer | Status |
|-------|----------------|--------|
| Hardkodet SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | Løst |
| Manglende miljøvalidering | Flere JS/TS-filer | Løst |
| Usikre funksjonskall | `11-integrating-with-function-calling/js-githubmodels/app.js` | Løst |
| Filhåndteringslekkasjer | `08-building-search-applications/scripts/` | Løst |
| Manglende tidsavbrudd på forespørsler | `09-building-image-applications/python/` | Løst |

### 1.2 Anbefalte ekstra sikkerhetsfunksjoner

1. **Eksempler på ratebegrensing**
   - Legg til eksempel på hvordan implementere ratebegrensing for API-kall
   - Demonstrer eksponentielle tilbakebetalingsmønstre

2. **Rotasjon av API-nøkler**
   - Legg til dokumentasjon om beste praksis for rotasjon av API-nøkler
   - Inkluder eksempler på bruk av Azure Key Vault eller lignende tjenester

3. **Integrering av innholdssikkerhet**
   - Legg til eksempler som bruker Azure Content Safety API
   - Demonstrer mønstre for input/output-moderering

---

## 2. Forbedringer i kodekvalitet

### 2.1 Konfigurasjonsfiler lagt til

| Fil | Formål |
|------|---------|
| `.eslintrc.json` | Regler for JavaScript/TypeScript-linting |
| `.prettierrc` | Standard for kodeformatering |
| `pyproject.toml` | Konfigurasjon av Python-verktøy (Black, Ruff, mypy) |

### 2.2 Delte verktøy laget

Ny `shared/python/` modul med:
- `env_utils.py` - Håndtering av miljøvariabler
- `input_validation.py` - Validering og rensing av inndata
- `api_utils.py` - Sikker innpakning av API-forespørsler

### 2.3 Anbefalte kodeforbedringer

1. **Dekning av typehint**
   - Legg til typehint i alle Python-filer
   - Aktiver streng TypeScript-modus i alle TS-prosjekter

2. **Dokumentasjonsstandarder**
   - Legg til docstrings i alle Python-funksjoner
   - Legg til JSDoc-kommentarer i alle JavaScript/TypeScript-funksjoner

3. **Test-rammeverk**
   - Legg til pytest-konfigurasjon og eksempeltester _(ferdig: pytest-konfigurasjon i `pyproject.toml`; eksempeltester for de delte verktøyene i [`tests/`](../../../tests) kjøres i CI)_
   - Legg til Jest-konfigurasjon for JavaScript/TypeScript

---

## 3. Pedagogiske forbedringer

### 3.1 Nye leksjonsemner

1. **Sikkerhet i AI-applikasjoner** (Foreslått leksjon 22)
   - Prompt injection-angrep og forsvar
   - Håndtering av API-nøkler
   - Innholdsmoderering
   - Ratebegrensing og misbruksforebygging

2. **Produksjonsutplassering** (Foreslått leksjon 23)
   - Containerisering med Docker
   - CI/CD-pipelines
   - Overvåkning og logging
   - Kostnadsstyring

3. **Avanserte RAG-teknikker** (Foreslått leksjon 24)
   - Hybrid søk (nøkkelord + semantisk)
   - Omklassifiseringsstrategier
   - Multi-modal RAG
   - Evalueringsmetrikker

### 3.2 Forbedringer av eksisterende leksjoner

| Leksjon | Anbefalt forbedring |
|--------|------------------------|
| 06 - Tekstgenerering | Legg til eksempler på streaming-respons |
| 07 - Chat-applikasjoner | Legg til mønstre for samtaleminne |
| 08 - Søkeapplikasjoner | Legg til sammenligning av vektor-databaser |
| 09 - Bildegenerering | Legg til eksempler på bilde-redigering/variasjon |
| 11 - Funksjonskall | Legg til parallell funksjonskall |
| 15 - RAG | Legg til sammenligning av chunking-strategier |
| 17 - AI-Agenter | Legg til orkestrering med flere agenter |

---

## 4. API-modernisering

### 4.1 Utdaterte API-mønstre (Migrering fullført)

Alle Python- og TypeScript-eksempler for **chat** har blitt migrert fra Chat Completions API til **Responses API** (`client.responses.create(...)` → `response.output_text`).

| Gammelt mønster | Nytt mønster | Status |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (chat) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | Fullført |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | Fullført |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | `openai`-pakken `client.responses.create()` → `response.output_text` | Fullført |
| `df.append()` (pandas) | `pd.concat()` | Fullført |

> **Merk:** Microsoft Foundry Models-eksempler som bruker `azure-ai-inference` / `@azure-rest/ai-inference` SDK (`client.complete()`) forblir på Model Inference API, som ikke støtter Responses API. `AzureOpenAI()` beholdes bevisst der det fortsatt er gyldig (embeddings og bilde-generering).

### 4.2 Nye API-funksjoner å demonstrere

1. **Strukturerte utdata** (OpenAI)
   - JSON-modus
   - Funksjonskall med strenge skjemaer

2. **Visjonsmuligheter**
   - Bildeanalyse med GPT-4o (visjon)
   - Multi-modale prompts

3. **Innebygde verktøy i Responses API** (erstatter det eldre Assistants API)
   - Kode-tolk
   - Fil-søk
   - Web-søk og egendefinerte verktøy

---

## 5. Infrastrukturforbedringer

### 5.1 Forbedringer i CI/CD

Implementert i [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml): Python-linting/formatering (Ruff + Black) er **pålagt** for det vedlikeholdte `shared/`-verktøymodul og kjøres som **veiledning** i resten av kurset, pluss en veiledende ESLint-gjennomgang for JavaScript/TypeScript. Det illustrerende utgangspunktet var:

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

### 5.2 Sikkerhetsskanning

Implementert i [`.github/workflows/security.yml`](../../../.github/workflows/security.yml): CodeQL-analyse for Python og JavaScript/TypeScript (ved push, pull request og ukentlig plan) i tillegg til avhengighetsgjennomgang i pull requests. Det illustrerende utgangspunktet var:

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

## 6. Forbedringer i utvikleropplevelse

### 6.1 Forbedringer i DevContainer

Implementert i [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) og [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh): containeren leveres nå med Pylance, Black-formatteren, Ruff, ESLint, Prettier og Copilot-utvidelser, aktiverer format-on-save koblet til repoets Black/Prettier-konfigurasjon, og installerer utviklerverktøyene (`ruff`, `black`, `mypy`, `pytest`) slik at [code-quality workflow](../../../.github/workflows/code-quality.yml) kan reproduceres lokalt. Basebildet `mcr.microsoft.com/devcontainers/universal` inkluderer allerede Python og Node, så ingen ekstra funksjoner er nødvendig. Det illustrerende utgangspunktet var:

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

### 6.2 Interaktiv lekeplass

Vurder å legge til:
- Jupyter-notatbøker med forhåndsutfylte API-nøkler (via miljøvariabler)
- Gradio/Streamlit-demoer for visuelle lærende
- Interaktive quizzer for kunnskapstesting

---

## 7. Støtte for flere språk

### 7.1 Nåværende språkomfang

| Teknologi | Dekket i leksjoner | Status |
|------------|-----------------|--------|
| Python | Alle | Fullført |
| TypeScript | 06-09, 11 | Delvis |
| JavaScript | 06-08, 11 | Delvis |
| .NET/C# | Noen | Delvis |

### 7.2 Anbefalte tillegg

1. **Go** - Voksende innen AI/ML-verktøy
2. **Rust** - Applikasjoner med høye ytelsesbehov
3. **Java/Kotlin** - Enterprise-applikasjoner

---

## 8. Ytelsesoptimaliseringer

### 8.1 Optimaliseringer i koden

1. **Asynkrone mønstre (async/await)**
   - Legg til asynkrone eksempler for batch-behandling
   - Demonstrer samtidige API-kall

2. **Caching-strategier**
   - Legg til eksempler på caching av embeddings
   - Demonstrer mønstre for caching av responser

3. **Tokenoptimalisering**
   - Legg til eksempel på bruk av tiktoken
   - Demonstrer teknikker for prompt-komprimering

### 8.2 Eksempler på kostnadsoptimalisering

Legg til eksempler som viser:
- Modellvalg basert på oppgavekompleksitet
- Prompt-engineering for token-effektivitet
- Batch-behandling for store operasjoner

---

## 9. Tilgjengelighet og internasjonalisering

### 9.1 Nåværende oversettelsesstatus

Alle oversettelser er **fullført** og genereres automatisk av [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst), som produserer og holder 50+ språkversjoner av kurset synkronisert med den engelske kilden. Oversatt innhold finnes under `translations/` og lokaliserte bilder under `translated_images/`; full liste over tilgjengelige språk publiseres øverst i repository README.

| Aspekt | Status |
|--------|--------|
| Oversettelsesdekning | Fullført — 50+ språk, alle leksjoner |
| Oversettelsesmetode | Automatisert via [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) |
| Holdt synkronisert med engelsk kilde | Ja — automatisk regenerert |

### 9.2 Forbedringer i tilgjengelighet

1. Legg til alternativ tekst på alle bilder
2. Sørg for at kodeeksempler har riktig syntaksutheving
3. Legg til video-transkripsjoner for alt videoinnhold
4. Sørg for at fargekontrast oppfyller WCAG-retningslinjer

---

## 10. Implementeringsprioritet

### Fase 1: Umiddelbart (Uke 1-2)
- [x] Fiks kritiske sikkerhetsproblemer
- [x] Legg til konfigurasjon for kodekvalitet
- [x] Opprett delte verktøy
- [x] Dokumenter sikkerhetsretningslinjer

### Fase 2: Kort sikt (Uke 3-4)
- [x] Oppdater utdaterte API-mønstre (Chat Completions → Responses API, Python + TypeScript)
- [ ] Legg til typehint i alle Python-filer (ferdig for den vedlikeholdte `shared/`-modulen; leksjonseksempler holdes enkle)
- [x] Legg til CI/CD-arbeidsflyter for kodekvalitet
- [x] Opprett arbeidsflyt for sikkerhetsskanning

### Fase 3: Middels sikt (Måned 2-3)
- [ ] Legg til ny sikkerhetsleksjon
- [ ] Legg til leksjon om produksjonsutplassering
- [x] Forbedre DevContainer-oppsett
- [ ] Legg til interaktive demoer

### Fase 4: Lang sikt (Måned 4+)
- [ ] Legg til avansert RAG-leksjon
- [ ] Utvid språkomfang
- [ ] Legg til omfattende testpakke
- [ ] Opprett sertifiseringsprogram

---

## Konklusjon

Denne veikartet gir en strukturert tilnærming til å forbedre Generative AI for Beginners-kurset. Ved å adressere sikkerhetsproblemer, modernisere APIer og legge til pedagogisk innhold, vil kurset bedre forberede studentene på utvikling av AI-applikasjoner i praksis.

For spørsmål eller bidrag, vennligst åpne en sak i GitHub-repositoriet.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->