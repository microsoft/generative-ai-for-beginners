# Forbedrede Funktioner og Forbedringsplan

Dette dokument skitserer anbefalede forbedringer og opgraderinger til Generative AI for Beginners pensum, baseret på en omfattende kodegennemgang og analyse af branchens bedste praksisser.

## Resumé

Kodebasen er blevet analyseret for sikkerhed, kodekvalitet og pædagogisk effektivitet. Dette dokument giver anbefalinger til øjeblikkelige rettelser, forbedringer på kort sigt og fremtidige opgraderinger.

---

## 1. Sikkerhedsforbedringer (Prioritet: Kritisk)

### 1.1 Øjeblikkelige Rettelser (Udført)

| Problem | Berørte Filer | Status |
|-------|----------------|--------|
| Hardcoded SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | Rettet |
| Manglende miljøvalidering | Flere JS/TS filer | Rettet |
| Usikre funktionskald | `11-integrating-with-function-calling/js-githubmodels/app.js` | Rettet |
| File handle leaks | `08-building-search-applications/scripts/` | Rettet |
| Manglende request timeouts | `09-building-image-applications/python/` | Rettet |

### 1.2 Anbefalede Yderligere Sikkerhedsfunktioner

1. **Eksempler på Rate Limiting**
   - Tilføj eksempel kode der viser, hvordan man implementerer rate limiting for API-kald
   - Demonstrer mønstre med eksponentiel backoff

2. **Rotation af API-nøgler**
   - Tilføj dokumentation om bedste praksis for rotation af API-nøgler
   - Inkluder eksempler på brug af Azure Key Vault eller lignende tjenester

3. **Integration af Content Safety**
   - Tilføj eksempler med Azure Content Safety API
   - Demonstrer input/output moderation mønstre

---

## 2. Forbedringer af Kodekvalitet

### 2.1 Tilføjede Konfigurationsfiler

| Fil | Formål |
|------|---------|
| `.eslintrc.json` | JavaScript/TypeScript linting regler |
| `.prettierrc` | Standarder for kodeformatering |
| `pyproject.toml` | Python tooling konfiguration (Black, Ruff, mypy) |

### 2.2 Delte Hjælpefunktioner Oprettet

Ny `shared/python/` modul med:
- `env_utils.py` - Miljøvariabel håndtering
- `input_validation.py` - Input validering og sanitering
- `api_utils.py` - Sikker API forespørgsels wrappers

### 2.3 Anbefalede Kodeforbedringer

1. **Dækning af Type Hints**
   - Tilføj type hints i alle Python-filer
   - Aktiver strict TypeScript mode i alle TS projekter

2. **Dokumentationsstandarder**
   - Tilføj docstrings til alle Python funktioner
   - Tilføj JSDoc kommentarer til alle JavaScript/TypeScript funktioner

3. **Test Framework**
   - Tilføj pytest konfiguration og eksempeltests _(udført: pytest konfiguration i `pyproject.toml`; eksempeltests for de delte hjælpefunktioner i [`tests/`](../../../tests) køres i CI)_
   - Tilføj Jest konfiguration for JavaScript/TypeScript

---

## 3. Pædagogiske Forbedringer

### 3.1 Nye Lektionsemner

1. **Sikkerhed i AI Applikationer** (Foreslået Lektion 22)
   - Prompt injection angreb og forsvar
   - API nøglehåndtering
   - Content moderation
   - Rate limiting og forebyggelse af misbrug

2. **Produktion Udrulning** (Foreslået Lektion 23)
   - Containerisering med Docker
   - CI/CD pipelines
   - Overvågning og logning
   - Omkostningsstyring

3. **Avancerede RAG Teknikker** (Foreslået Lektion 24)
   - Hybrid søgning (keyword + semantisk)
   - Re-ranking strategier
   - Multi-modal RAG
   - Evalueringsmetrikker

### 3.2 Forbedringer af Eksisterende Lektioner

| Lektion | Anbefalet Forbedring |
|--------|------------------------|
| 06 - Tekstgenerering | Tilføj eksempler på streaming svar |
| 07 - Chat Applikationer | Tilføj samtalememory mønstre |
| 08 - Søgeapplikationer | Tilføj sammenligning af vektordatabaser |
| 09 - Billedgenerering | Tilføj eksempler på billedredigering/variation |
| 11 - Funktionskald | Tilføj parallelle funktionskald |
| 15 - RAG | Tilføj sammenligning af chunking strategier |
| 17 - AI Agenter | Tilføj multi-agent orkestrering |

---

## 4. API Modernisering

### 4.1 Udfasede API Mønstre (Migrering Fuldført)

Alle Python og TypeScript **chat** eksempler er blevet migreret fra Chat Completions API til **Responses API** (`client.responses.create(...)` → `response.output_text`).

| Gammelt Mønster | Nyt Mønster | Status |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (chat) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | Fuldført |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | Fuldført |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | `openai` pakke `client.responses.create()` → `response.output_text` | Fuldført |
| `df.append()` (pandas) | `pd.concat()` | Fuldført |

> **Note:** Microsoft Foundry Models eksempler, som bruger `azure-ai-inference` / `@azure-rest/ai-inference` SDK (`client.complete()`), forbliver på Model Inference API, som ikke understøtter Responses API. `AzureOpenAI()` bevares bevidst hvor stadig gyldigt (embeddings og billedgenerering).

### 4.2 Nye API Funktioner at Demonstrere

1. **Strukturerede Output** (OpenAI)
   - JSON-tilstand
   - Funktionskald med strenge skemaer

2. **Vision Funktionaliteter**
   - Billedanalyse med GPT-4o (vision)
   - Multi-modale prompts

3. **Built-in Værktøjer i Responses API** (afløser den gamle Assistants API)
   - Kodefortolker
   - Filsøgning
   - Websøgning og brugerdefinerede værktøjer

---

## 5. Infrastrukturforbedringer

### 5.1 CI/CD Forbedringer

Implementeret i [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml): Python linting/formatering (Ruff + Black) er **håndhævet** på det vedligeholdte `shared/` hjælpefunktionsmodul og kører **vejledende** på resten af pensum, plus et vejledende ESLint run for JavaScript/TypeScript. Den illustrerede baseline var:

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

### 5.2 Sikkerhedsscanning

Implementeret i [`.github/workflows/security.yml`](../../../.github/workflows/security.yml): CodeQL analyse for Python og JavaScript/TypeScript (ved push, pull request og ugentlig kørsel) plus afhængighedsgennemgang ved pull requests. Den illustrerede baseline var:

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

## 6. Forbedringer af Udvikleroplevelsen

### 6.1 DevContainer Forbedringer

Implementeret i [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) og [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh): containeren leverer nu Pylance, Black formatter, Ruff, ESLint, Prettier og Copilot udvidelser, aktiverer format-on-save koblet til repoets Black/Prettier konfiguration, og installerer udviklerværktøjerne (`ruff`, `black`, `mypy`, `pytest`), så [code-quality workflow](../../../.github/workflows/code-quality.yml) kan gentages lokalt. Baseline-billedet `mcr.microsoft.com/devcontainers/universal` indeholder allerede Python og Node, så ingen ekstra funktioner er nødvendige. Den illustrerede baseline var:

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

### 6.2 Interaktiv Legeplads

Overvej at tilføje:
- Jupyter notebooks med forudfyldte API nøgler (via miljø)
- Gradio/Streamlit demos for visuelle elever
- Interaktive quizzer til vidensvurdering

---

## 7. Multisproget Support

### 7.1 Nuværende Sprogdækning

| Teknologi | Dækkede Lektioner | Status |
|------------|-----------------|--------|
| Python | Alle | Fuldstændig |
| TypeScript | 06-09, 11 | Delvis |
| JavaScript | 06-08, 11 | Delvis |
| .NET/C# | Nogle | Delvis |

### 7.2 Anbefalede Tilføjelser

1. **Go** - Voksende inden for AI/ML tooling
2. **Rust** - Ydelses-kritiske applikationer
3. **Java/Kotlin** - Enterprise applikationer

---

## 8. Performanceoptimeringer

### 8.1 Kode-niveau Optimeringer

1. **Async/Await Mønstre**
   - Tilføj asynkrone eksempler for batch-behandling
   - Demonstrer samtidige API-kald

2. **Caching Strategier**
   - Tilføj eksempler på embedding caching
   - Demonstrer mønstre for respons caching

3. **Tokenoptimering**
   - Tilføj eksempler på brug af tiktoken
   - Demonstrer prompt komprimeringsteknikker

### 8.2 Eksempler på Omkostningsoptimering

Tilføj eksempler, der demonstrerer:
- Modelvalg baseret på opgavens kompleksitet
- Prompt engineering for token effektivitet
- Batch-behandling for volumensoperationer

---

## 9. Tilgængelighed og Internationalisering

### 9.1 Nuværende Oversættelsesstatus

Alle oversættelser er **færdige** og genereret automatisk af [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst), som producerer og holder 50+ sprogversioner af pensum synkroniseret med den engelske kilde. Oversat indhold findes under `translations/` og lokaliserede billeder under `translated_images/`; den komplette liste over tilgængelige sprog er offentliggjort øverst i repository README.

| Aspekt | Status |
|--------|--------|
| Oversættelsesdækning | Fuldstændig — 50+ sprog, alle lektioner |
| Oversættelsesmetode | Automatiseret via [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) |
| Holdt synkroniseret med engelsk kilde | Ja — regenereres automatisk |

### 9.2 Tilgængelighedsforbedringer

1. Tilføj alt-tekst til alle billeder
2. Sikr at kodeeksempler har korrekt syntaksfremhævning
3. Tilføj video transskriptioner for alt videomateriale
4. Sikr farvekontrast opfylder WCAG retningslinjer

---

## 10. Implementeringsprioritet

### Fase 1: Øjeblikkelig (Uge 1-2)
- [x] Løs kritiske sikkerhedsproblemer
- [x] Tilføj konfiguration for kodekvalitet
- [x] Opret delte hjælpefunktioner
- [x] Dokumenter sikkerhedsretningslinjer

### Fase 2: Kort sigt (Uge 3-4)
- [x] Opdater forældede API-mønstre (Chat Completions → Responses API, Python + TypeScript)
- [ ] Tilføj type hints til alle Python-filer (udført for det vedligeholdte `shared/` modul; lektionseksempler holdes simple)
- [x] Tilføj CI/CD workflows for kodekvalitet
- [x] Opret sikkerhedsscanning workflow

### Fase 3: Mellemlang sigt (Måned 2-3)
- [ ] Tilføj ny sikkerhedslektie
- [ ] Tilføj produktion udrulningslektie
- [x] Forbedr DevContainer opsætning
- [ ] Tilføj interaktive demos

### Fase 4: Lang sigt (Måned 4+)
- [ ] Tilføj avanceret RAG lektion
- [ ] Udvid sprogdækning
- [ ] Tilføj omfattende testsuite
- [ ] Opret certificeringsprogram

---

## Konklusion

Denne køreplan giver en struktureret tilgang til at forbedre Generative AI for Beginners pensum. Ved at adressere sikkerhedsproblemer, modernisere API'er og tilføje pædagogisk indhold, vil kurset bedre forberede studerende til udvikling af AI-applikationer i den virkelige verden.

For spørgsmål eller bidrag, venligst opret en issue på GitHub repositoryet.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->