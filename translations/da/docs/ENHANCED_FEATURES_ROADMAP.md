# Forbedrings- og Udviklingsplan for Udvidede Funktioner

Dette dokument skitserer anbefalede forbedringer og opgraderinger til Generative AI for Beginners læseplanen, baseret på en omfattende kodegennemgang og analyse af branchens bedste praksis.

## Resumé for Ledelsen

Kodebasen er blevet analyseret for sikkerhed, kodekvalitet og pædagogisk effektivitet. Dette dokument giver anbefalinger til øjeblikkelige rettelser, kortsigtede forbedringer og fremtidige opgraderinger.

---

## 1. Sikkerhedsforbedringer (Prioritet: Kritisk)

### 1.1 Øjeblikkelige Rettelser (Færdiggjort)

| Problem | Påvirkede Filer | Status |
|---------|-----------------|--------|
| Hardcoded SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | Rettet |
| Manglende miljøvalidering | Flere JS/TS filer | Rettet |
| Usikre funktionskald | `11-integrating-with-function-calling/js-githubmodels/app.js` | Rettet |
| Filhåndtag lækager | `08-building-search-applications/scripts/` | Rettet |
| Manglende request-timeouts | `09-building-image-applications/python/` | Rettet |

### 1.2 Anbefalede Yderligere Sikkerhedsfunktioner

1. **Rate Limiting Eksempler**
   - Tilføj eksempel på kode, der viser, hvordan man implementerer rate limiting for API-kald
   - Demonstrer eksponentielle backoff-mønstre

2. **API Nøgle Rotation**
   - Tilføj dokumentation om bedste praksis for rotering af API-nøgler
   - Inkluder eksempler på brug af Azure Key Vault eller lignende tjenester

3. **Integration af Content Safety**
   - Tilføj eksempler, der bruger Azure Content Safety API
   - Demonstrer input/output moderation mønstre

---

## 2. Forbedringer af Kodekvalitet

### 2.1 Tilføjede Konfigurationsfiler

| Fil | Formål |
|-----|--------|
| `.eslintrc.json` | JavaScript/TypeScript lint-regler |
| `.prettierrc` | Standarder for kodeformatering |
| `pyproject.toml` | Python tooling-konfiguration (Black, Ruff, mypy) |

### 2.2 Oprettede Delte Hjælpefunktioner

Nyt `shared/python/` modul med:
- `env_utils.py` - Håndtering af miljøvariabler
- `input_validation.py` - Validering og sanitering af input
- `api_utils.py` - Sikker API-request wrappers

### 2.3 Anbefalede Kodeforbedringer

1. **Type Hints Dækning**
   - Tilføj type hints til alle Python-filer
   - Aktivér strict TypeScript mode i alle TS-projekter

2. **Dokumentationsstandarder**
   - Tilføj docstrings til alle Python-funktioner
   - Tilføj JSDoc-kommentarer til alle JavaScript/TypeScript-funktioner

3. **Test Framework**
   - Tilføj pytest-konfiguration og eksempeltests
   - Tilføj Jest-konfiguration for JavaScript/TypeScript

---

## 3. Pædagogiske Forbedringer

### 3.1 Nye Lektionsemner

1. **Sikkerhed i AI-applikationer** (Foreslået Lektion 22)
   - Prompt injection angreb og forsvar
   - API nøgle management
   - Content moderation
   - Rate limiting og misbrugsforebyggelse

2. **Produktionsudrulning** (Foreslået Lektion 23)
   - Containerization med Docker
   - CI/CD pipelines
   - Overvågning og logging
   - Omkostningsstyring

3. **Avancerede RAG-teknikker** (Foreslået Lektion 24)
   - Hybrid søgning (keyword + semantisk)
   - Re-ranking strategier
   - Multi-modal RAG
   - Evalueringsmetrikker

### 3.2 Forbedringer af Eksisterende Lektioner

| Lektion | Anbefalet Forbedring |
|---------|---------------------|
| 06 - Tekstgenerering | Tilføj streaming respons eksempler |
| 07 - Chat-applikationer | Tilføj samtalememory mønstre |
| 08 - Søgeapplikationer | Tilføj sammenligning af vektordatabaser |
| 09 - Billedgenerering | Tilføj eksempler på billedredigering/variation |
| 11 - Funktionskald | Tilføj parallelle funktionskald |
| 15 - RAG | Tilføj sammenligning af chunking-strategier |
| 17 - AI Agenter | Tilføj multi-agent orkestrering |

---

## 4. API Modernisering

### 4.1 Forældede API-Mønstre der Skal Opdateres

| Gammelt Mønster | Nyt Mønster | Påvirkede Filer |
|-----------------|-------------|-----------------|
| `openai.api_type = "azure"` | `AzureOpenAI()` klient | Flere scripts i `08-building-search-applications/` |
| `openai.ChatCompletion.create()` | `client.chat.completions.create()` | Flere notebooks |
| `df.append()` (pandas) | `pd.concat()` | RAG notebook |

### 4.2 Nye API-Funktioner til Demonstration

1. **Strukturerede Outputs** (OpenAI)
   - JSON-tilstand
   - Funktionskald med strenge skemaer

2. **Vision Funktionaliteter**
   - Billedanalyse med GPT-4V
   - Multi-modal prompts

3. **Assistants API**
   - Kodefortolker
   - Filesøgning
   - Tilpassede værktøjer

---

## 5. Infrastrukturforbedringer

### 5.1 CI/CD Forbedringer

Nuværende workflows håndterer markdown-validering. Anbefalede tilføjelser:

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

### 6.1 Forbedringer til DevContainer

Opdater `.devcontainer/devcontainer.json`:

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

### 6.2 Interaktiv Playground

Overvej at tilføje:
- Jupyter notebooks med forudindlæste API nøgler (via miljø)
- Gradio/Streamlit demoer for visuelle lærende
- Interaktive quizzer til vidensevaluering

---

## 7. Multi-Sprog Støtte

### 7.1 Nuværende Sprogdækning

| Teknologi | Dækkede Lektioner | Status |
|-----------|-------------------|--------|
| Python | Alle | Fuldstændig |
| TypeScript | 06-09, 11 | Delvis |
| JavaScript | 06-08, 11 | Delvis |
| .NET/C# | Nogle | Delvis |

### 7.2 Anbefalede Tilføjelser

1. **Go** - Voksende inden for AI/ML tooling
2. **Rust** - Applikationer der kræver høj ydelse
3. **Java/Kotlin** - Enterprise applikationer

---

## 8. Performanceoptimeringer

### 8.1 Optimeringer på Kodeniveau

1. **Async/Await Mønstre**
   - Tilføj async eksempler til batchbehandling
   - Demonstrer samtidige API-kald

2. **Caching Strategier**
   - Tilføj eksempler på embedding caching
   - Demonstrer respons caching mønstre

3. **Tokenoptimering**
   - Tilføj eksempler på brug af tiktoken
   - Demonstrer promptkomprimeringsteknikker

### 8.2 Eksempler på Omkostningsoptimering

Tilføj eksempler der demonstrerer:
- Modelvalg baseret på opgavens kompleksitet
- Prompt engineering for token effektivitet
- Batchbehandling til masseoperationer

---

## 9. Tilgængelighed og Internationalisering

### 9.1 Nuværende Oversættelsesstatus

| Sprog | Status |
|-------|--------|
| Engelsk | Fuldstændig |
| Kinesisk (Forenklet) | Fuldstændig |
| Japansk | Fuldstændig |
| Koreansk | Fuldstændig |
| Spansk | Delvis |
| Portugisisk | Delvis |
| Tyrkisk | Delvis |
| Polsk | Delvis |

### 9.2 Forbedringer af Tilgængelighed

1. Tilføj alt-tekst til alle billeder  
2. Sørg for at kodeeksempler har korrekt syntaksfremhævning  
3. Tilføj videotranskriptioner for alt videoindhold  
4. Sørg for at farvekontrast opfylder WCAG-retningslinjer  

---

## 10. Implementeringsprioritet

### Fase 1: Øjeblikkelig (Uge 1-2)
- [x] Rett kritiske sikkerhedsproblemer
- [x] Tilføj konfiguration for kodekvalitet
- [x] Opret delte hjælpefunktioner
- [x] Dokumenter sikkerhedsguidelines

### Fase 2: Kortsigtet (Uge 3-4)
- [ ] Opdater forældede API-mønstre
- [ ] Tilføj type hints til alle Python-filer
- [ ] Tilføj CI/CD workflows for kodekvalitet
- [ ] Opret sikkerhedsscannings workflow

### Fase 3: Mellemlang sigt (Måned 2-3)
- [ ] Tilføj ny sikkerhedslektion
- [ ] Tilføj lektion om produktionsudrulning
- [ ] Forbedr DevContainer setup
- [ ] Tilføj interaktive demonstrationer

### Fase 4: Langsigtet (Måned 4+)
- [ ] Tilføj avanceret RAG lektion
- [ ] Udvid sprogdækningen
- [ ] Tilføj omfattende testsuite
- [ ] Opret certificeringsprogram

---

## Konklusion

Denne køreplan giver en struktureret tilgang til at forbedre Generative AI for Beginners læseplanen. Ved at adressere sikkerhedsaspekter, modernisere API’er og tilføje pædagogisk indhold vil kurset bedre forberede studerende på udvikling af AI-applikationer i den virkelige verden.

For spørgsmål eller bidrag, åbn venligst en issue i GitHub-repositoriet.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi stræber efter nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->