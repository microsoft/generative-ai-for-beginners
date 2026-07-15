# Förbättrade Funktioner och Förbättringsplan

Detta dokument beskriver rekommenderade förbättringar och uppgraderingar för Generative AI for Beginners-kursplanen, baserat på en omfattande kodgranskning och analys av branschens bästa praxis.

## Sammanfattning

Kodbasen har analyserats för säkerhet, kodkvalitet och pedagogisk effektivitet. Detta dokument ger rekommendationer för omedelbara lösningar, kortsiktiga förbättringar och framtida uppgraderingar.

---

## 1. Säkerhetsförbättringar (Prioritet: Kritisk)

### 1.1 Omedelbara Fixar (Slutförda)

| Problem | Påverkade filer | Status |
|-------|----------------|--------|
| Hårdkodad SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | Fixad |
| Saknad validering av miljövariabler | Flera JS/TS-filer | Fixad |
| Osäkra funktionsanrop | `11-integrating-with-function-calling/js-githubmodels/app.js` | Fixad |
| Filhandtagsläckor | `08-building-search-applications/scripts/` | Fixad |
| Saknade timeout för förfrågningar | `09-building-image-applications/python/` | Fixad |

### 1.2 Rekommenderade Ytterligare Säkerhetsfunktioner

1. **Exempel på Avgränsning av API-anrop**
   - Lägg till exempel på hur man implementerar rate limiting för API-anrop
   - Visa exponentiella backoff-mönster

2. **Rotation av API-nycklar**
   - Lägg till dokumentation om bästa praxis för rotation av API-nycklar
   - Inkludera exempel på användning av Azure Key Vault eller liknande tjänster

3. **Integrering av Content Safety**
   - Lägg till exempel med Azure Content Safety API
   - Visa mönster för in-/utdata-moderering

---

## 2. Kodkvalitetsförbättringar

### 2.1 Konfigurationsfiler tillagda

| Fil | Syfte |
|------|---------|
| `.eslintrc.json` | JavaScript/TypeScript lintningsregler |
| `.prettierrc` | Kodformateringsstandarder |
| `pyproject.toml` | Python verktygskonfiguration (Black, Ruff, mypy) |

### 2.2 Delade Verktyg Skapade

Ny `shared/python/` modul med:
- `env_utils.py` - Hantering av miljövariabler
- `input_validation.py` - Inmatningsvalidering och sanering
- `api_utils.py` - Säkra API-förfrågningar

### 2.3 Rekommenderade Kodingrepp

1. **Typanvisningar Täckning**
   - Lägg till typanvisningar i alla Python-filer
   - Aktivera strikt TypeScript-läge i alla TS-projekt

2. **Dokumentationsstandarder**
   - Lägg till docstrings till alla Python-funktioner
   - Lägg till JSDoc-kommentarer till alla JavaScript/TypeScript-funktioner

3. **Testningsramverk**
   - Lägg till pytest-konfiguration och exempeltester _(gjort: pytest-konfiguration i `pyproject.toml`; exempeltester för delade verktyg i [`tests/`](../../../tests) körs i CI)_
   - Lägg till Jest-konfiguration för JavaScript/TypeScript

---

## 3. Pedagogiska Förbättringar

### 3.1 Nya Lektionsteman

1. **Säkerhet i AI-applikationer** (Föreslagen Lektion 22)
   - Prompt injection-attacker och försvar
   - Hantering av API-nycklar
   - Innehållsmoderering
   - Rate limiting och missbruksprevention

2. **Produktiondistribution** (Föreslagen Lektion 23)
   - Containerisering med Docker
   - CI/CD-pipelines
   - Övervakning och loggning
   - Kostnadshantering

3. **Avancerade RAG-tekniker** (Föreslagen Lektion 24)
   - Hybrid sökning (nyckelord + semantisk)
   - Omrankningsstrategier
   - Multimodal RAG
   - Utvärderingsmetoder

### 3.2 Förbättringar av Befintliga Lektioner

| Lektion | Rekommenderad förbättring |
|--------|--------------------------|
| 06 - Textgenerering | Lägg till exempel på strömmade svar |
| 07 - Chattapplikationer | Lägg till mönster för konversationsminne |
| 08 - Sökapplikationer | Lägg till jämförelse av vektordatabaser |
| 09 - Bildgenerering | Lägg till exempel på bildredigering/variation |
| 11 - Funktionsanrop | Lägg till parallella funktionsanrop |
| 15 - RAG | Lägg till jämförelse av chunking-strategier |
| 17 - AI-agenter | Lägg till multi-agent orkestrering |

---

## 4. API-modernisering

### 4.1 Utfasade API-mönster (Migration slutförd)

Alla Python- och TypeScript-exempel för **chatt** har migrerats från Chat Completions API till **Responses API** (`client.responses.create(...)` → `response.output_text`).

| Gamla Mönstret | Nya Mönstret | Status |
|-------------|-------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (chatt) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | Slutförd |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | Slutförd |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | `openai`-paket `client.responses.create()` → `response.output_text` | Slutförd |
| `df.append()` (pandas) | `pd.concat()` | Slutförd |

> **Notera:** Microsoft Foundry Models-exempel som använder `azure-ai-inference` / `@azure-rest/ai-inference` SDK (`client.complete()`) kvarstår på Model Inference API, som inte stödjer Responses API. `AzureOpenAI()` behålls medvetet där det fortfarande är giltigt (inbäddningar och bildgenerering).

### 4.2 Nya API-funktioner att demonstrera

1. **Strukturerade svar** (OpenAI)
   - JSON-läge
   - Funktionsanrop med strikta schemas

2. **Visionfunktioner**
   - Bildanalys med GPT-4o (vision)
   - Multimodala promptar

3. **Responses API Inbyggda Verktyg** (ersätter det äldre Assistants API)
   - Kodtolk
   - Filsökning
   - Webb-sökning och anpassade verktyg

---

## 5. Infrastrukturförbättringar

### 5.1 CI/CD-förbättringar

Implementerat i [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml): Python linting/formatering (Ruff + Black) är **påbjuden** för den underhållna `shared/`-modulen och körs **rådgivande** för resten av kursmaterialet, plus en rådgivande ESLint-pass för JavaScript/TypeScript. Baslinjen var:

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

### 5.2 Säkerhetsskanning

Implementerat i [`.github/workflows/security.yml`](../../../.github/workflows/security.yml): CodeQL-analys för Python och JavaScript/TypeScript (vid push, pull request och veckoschema) plus beroenderevision på pull requests. Baslinjen var:

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

## 6. Utvecklarupplevelse-förbättringar

### 6.1 DevContainer-förbättringar

Implementerat i [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) och [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh): containern levereras nu med Pylance, Black formatter, Ruff, ESLint, Prettier och Copilot-tillägg, aktiverar format-on-save kopplat till repo:ts Black/Prettier-konfiguration och installerar utvecklarverktyg (`ruff`, `black`, `mypy`, `pytest`) så att [code-quality workflow](../../../.github/workflows/code-quality.yml) kan reproducera lokalt. Basbilden `mcr.microsoft.com/devcontainers/universal` innehåller redan Python och Node, så inga extra funktioner krävs. Baslinjen var:

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

### 6.2 Interaktiv Lekplats

Överväg att lägga till:
- Jupyter-notebooks med förifyllda API-nycklar (via miljövariabler)
- Gradio/Streamlit-demonstrationer för visuella elever
- Interaktiva quiz för kunskapsbedömning

---

## 7. Flerspråkigt Stöd

### 7.1 Nuvarande Språktäckning

| Teknologi | Täckt i Lektioner | Status |
|------------|-----------------|--------|
| Python | Alla | Komplett |
| TypeScript | 06-09, 11 | Delvis |
| JavaScript | 06-08, 11 | Delvis |
| .NET/C# | Vissa | Delvis |

### 7.2 Rekommenderade Tillägg

1. **Go** - Växer inom AI/ML-verktyg
2. **Rust** - Prestandakritiska applikationer
3. **Java/Kotlin** - Företagsapplikationer

---

## 8. Prestandaoptimeringar

### 8.1 Optimeringar på Kodnivå

1. **Async/Await-mönster**
   - Lägg till asynkrona exempel för batchbearbetning
   - Visa parallella API-anrop

2. **Cachingstrategier**
   - Lägg till exempel på cachning av embeddingar
   - Visa mönster för responscachning

3. **Tokenoptimering**
   - Lägg till exempel på tiktoken-användning
   - Visa tekniker för promptkomprimering

### 8.2 Exempel på Kostnadsoptimering

Lägg till exempel som visar:
- Modellval baserat på uppgiftskomplexitet
- Promptteknik för token-effektivitet
- Batchbearbetning för massoperationer

---

## 9. Tillgänglighet och Internationell Användning

### 9.1 Nuvarande Översättningsstatus

Alla översättningar är **kompletta** och genereras automatiskt av [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst), som producerar och håller 50+ språkversioner av kursplanen i synk med den engelska källan. Översatt innehåll finns under `translations/` och lokaliserade bilder under `translated_images/`; fullständig lista över tillgängliga språk publiceras i toppen av repo:ts README.

| Aspekt | Status |
|--------|--------|
| Översättningstäckning | Komplett — 50+ språk, alla lektioner |
| Översättningsmetod | Automatisk via [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) |
| Hålls synkad med engelsk källa | Ja — regenereras automatiskt |

### 9.2 Tillgänglighetsförbättringar

1. Lägg till alt-text till alla bilder
2. Säkerställ att kodexempel har korrekt syntaxmarkering
3. Lägg till videotranskriptioner för allt videoinnehåll
4. Säkerställ att färgkontrast möter WCAG-riktlinjer

---

## 10. Implementeringsprioritering

### Fas 1: Omedelbar (Vecka 1-2)
- [x] Fixa kritiska säkerhetsproblem
- [x] Lägg till konfiguration för kodkvalitet
- [x] Skapa delade verktyg
- [x] Dokumentera säkerhetsriktlinjer

### Fas 2: Kort sikt (Vecka 3-4)
- [x] Uppdatera föråldrade API-mönster (Chat Completions → Responses API, Python + TypeScript)
- [ ] Lägg till typanvisningar till alla Python-filer (gjort för den underhållna `shared/`-modulen; lektionsprover hålls enkla)
- [x] Lägg till CI/CD-workflows för kodkvalitet
- [x] Skapa säkerhetsskannings-workflow

### Fas 3: Medellång sikt (Månad 2-3)
- [ ] Lägg till ny säkerhetslektion
- [ ] Lägg till lektion om produktiondistribution
- [x] Förbättra DevContainer-setup
- [ ] Lägg till interaktiva demonstrationer

### Fas 4: Lång sikt (Månad 4+)
- [ ] Lägg till avancerad RAG-lektion
- [ ] Utöka språktäckningen
- [ ] Lägg till omfattande testsuite
- [ ] Skapa certifieringsprogram

---

## Slutsats

Denna plan ger en strukturerad metod för att förbättra Generative AI for Beginners-kursplanen. Genom att adressera säkerhetsfrågor, modernisera API:er och lägga till pedagogiskt innehåll kommer kursen bättre förbereda studenter för verklig AI-applikationsutveckling.

För frågor eller bidrag, vänligen öppna ett ärende i GitHub-repot.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->