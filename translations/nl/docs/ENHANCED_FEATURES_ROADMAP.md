# Verbeterde functies en verbeteringen roadmap

Dit document beschrijft aanbevolen verbeteringen en uitbreidingen voor het Generative AI for Beginners-curriculum, gebaseerd op een uitgebreide code-review en analyse van best practices in de industrie.

## Samenvatting voor leidinggevenden

De codebase is geanalyseerd op beveiliging, codekwaliteit en educatieve effectiviteit. Dit document biedt aanbevelingen voor directe reparaties, kortetermijnverbeteringen en toekomstige uitbreidingen.

---

## 1. Beveiligingsverbeteringen (Prioriteit: Kritiek)

### 1.1 Directe Reparaties (Voltooid)

| Probleem | Betrokken Bestanden | Status |
|---------|--------------------|--------|
| Hardcoded SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | Gerepareerd |
| Ontbrekende omgeving-validatie | Meerdere JS/TS-bestanden | Gerepareerd |
| Onveilige functieaanroepen | `11-integrating-with-function-calling/js-githubmodels/app.js` | Gerepareerd |
| File handle leaks | `08-building-search-applications/scripts/` | Gerepareerd |
| Ontbrekende request-timeouts | `09-building-image-applications/python/` | Gerepareerd |

### 1.2 Aanbevolen Extra Beveiligingsfuncties

1. **Voorbeelden van Rate Limiting**
   - Voeg voorbeeldcode toe om rate limiting voor API-aanroepen te implementeren
   - Demonstreer exponentiële backoff-patronen

2. **API Sleutel Rotatie**
   - Voeg documentatie toe over best practices voor rotatie van API-sleutels
   - Inclusief voorbeelden voor het gebruik van Azure Key Vault of vergelijkbare services

3. **Content Safety Integratie**
   - Voeg voorbeelden toe van het gebruik van Azure Content Safety API
   - Demonstreer input/output moderatiepatronen

---

## 2. Verbeteringen codekwaliteit

### 2.1 Toegevoegde configuratiebestanden

| Bestand | Doel |
|--------|------|
| `.eslintrc.json` | JavaScript/TypeScript lintregels |
| `.prettierrc` | Code formatteringsstandaarden |
| `pyproject.toml` | Python tooling configuratie (Black, Ruff, mypy) |

### 2.2 Gedeelde hulpprogramma's aangemaakt

Nieuw `shared/python/`-module met:
- `env_utils.py` - Afhandeling van omgevingsvariabelen
- `input_validation.py` - Validatie en sanering van invoer
- `api_utils.py` - Veilige API-aanvraag wrappers

### 2.3 Aanbevolen codeverbeteringen

1. **Type Hints Dekking**
   - Voeg type hints toe aan alle Python-bestanden
   - Zet strikte TypeScript-modus aan in alle TS-projecten

2. **Documentatiestandaarden**
   - Voeg docstrings toe aan alle Python-functies
   - Voeg JSDoc-comments toe aan alle JavaScript/TypeScript functies

3. **Test Framework**
   - Voeg pytest-configuratie en voorbeeldtests toe _(gedaan: pytest config in `pyproject.toml`; voorbeeldtests voor de gedeelde hulpprogramma's in [`tests/`](../../../tests) worden uitgevoerd in CI)_
   - Voeg Jest-configuratie toe voor JavaScript/TypeScript

---

## 3. Educatieve uitbreidingen

### 3.1 Nieuwe lesonderwerpen

1. **Beveiliging in AI-toepassingen** (Voorgestelde les 22)
   - Prompt injection aanvallen en verdedigingsmethoden
   - API sleutelbeheer
   - Contentmoderatie
   - Rate limiting en misbruikpreventie

2. **Productie-implementatie** (Voorgestelde les 23)
   - Containerisatie met Docker
   - CI/CD-pijplijnen
   - Monitoring en logging
   - Kostenbeheer

3. **Geavanceerde RAG-technieken** (Voorgestelde les 24)
   - Hybride zoeken (zoekwoord + semantisch)
   - Herordening strategieën
   - Multi-modale RAG
   - Evaluatiemaatstaven

### 3.2 Verbeteringen bestaande lessen

| Les | Aanbevolen Verbetering |
|-----|----------------------|
| 06 - Tekstgeneratie | Voeg streaming response voorbeelden toe |
| 07 - Chatapplicaties | Voeg gespreksgeheugenpatronen toe |
| 08 - Zoekapplicaties | Voeg vergelijking van vector databases toe |
| 09 - Beeldgeneratie | Voeg voorbeelden voor beeldbewerking/variaties toe |
| 11 - Functieaanroepen | Voeg parallelle functieaanroepen toe |
| 15 - RAG | Voeg vergelijking van chunkingstrategieën toe |
| 17 - AI Agents | Voeg multi-agent orkestratie toe |

---

## 4. API Modernisering

### 4.1 Verouderde API-patronen (Migratie voltooid)

Alle Python- en TypeScript-**chat**-voorbeelden zijn gemigreerd van de Chat Completions API naar de **Responses API** (`client.responses.create(...)` → `response.output_text`).

| Oud Patroon | Nieuw Patroon | Status |
|------------|--------------|--------|
| `openai.api_type = "azure"` / `AzureOpenAI()` (chat) | `OpenAI(base_url="<endpoint>/openai/v1/")` (Responses API) | Voltooid |
| `openai.ChatCompletion.create()` / `client.chat.completions.create()` | `client.responses.create(input=...)` → `response.output_text` | Voltooid |
| `@azure/openai` `OpenAIClient.getChatCompletions()` (TypeScript) | `openai` package `client.responses.create()` → `response.output_text` | Voltooid |
| `df.append()` (pandas) | `pd.concat()` | Voltooid |

> **Opmerking:** Microsoft Foundry Models-voorbeelden die de `azure-ai-inference` / `@azure-rest/ai-inference` SDK gebruiken (`client.complete()`) blijven op de Model Inference API, die de Responses API niet ondersteunt. `AzureOpenAI()` wordt bewust behouden waar nog geldig (embeddings en beeldgeneratie).

### 4.2 Nieuwe API-functies om te demonstreren

1. **Gestructureerde Uitvoer** (OpenAI)
   - JSON-modus
   - Functieaanroepen met strikte schema's

2. **Visie-mogelijkheden**
   - Beeldanalyse met GPT-4o (vision)
   - Multi-modale prompts

3. **Responses API ingebouwde hulpmiddelen** (vervangt de legacy Assistants API)
   - Code interpreter
   - Bestand zoeken
   - Web zoeken en aangepaste tools

---

## 5. Infrastructuurverbeteringen

### 5.1 CI/CD verbeteringen

Geïmplementeerd in [`.github/workflows/code-quality.yml`](../../../.github/workflows/code-quality.yml): Python linting/formatting (Ruff + Black) is **afgedwongen** op de onderhouden `shared/` hulpprogrammamodule en draait **adviseur**-modus over de rest van het curriculum, plus een adviserende ESLint-run voor JavaScript/TypeScript. De illustratieve basislijn was:

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

### 5.2 Beveiligingsscanning

Geïmplementeerd in [`.github/workflows/security.yml`](../../../.github/workflows/security.yml): CodeQL-analyse voor Python en JavaScript/TypeScript (bij push, pull request en wekelijks schema) plus een afhankelijkheidcontrole bij pull requests. De illustratieve basislijn was:

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

## 6. Verbeteringen aan ontwikkelaarservaring

### 6.1 DevContainer verbeteringen

Geïmplementeerd in [`.devcontainer/devcontainer.json`](../../../.devcontainer/devcontainer.json) en [`.devcontainer/post-create.sh`](../../../.devcontainer/post-create.sh): de container levert nu Pylance, de Black formatter, Ruff, ESLint, Prettier en Copilot extensies, schakelt format-on-save in gekoppeld aan de Black/Prettier-config van de repo, en installeert de ontwikkeltools (`ruff`, `black`, `mypy`, `pytest`) zodat de [code-quality workflow](../../../.github/workflows/code-quality.yml) lokaal reproduceerbaar is. Het `mcr.microsoft.com/devcontainers/universal` basisimage bevat al Python en Node, dus extra functies zijn niet vereist. De illustratieve basislijn was:

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

### 6.2 Interactieve speelplaats

Overweeg toe te voegen:
- Jupyter notebooks met vooraf ingevulde API-sleutels (via omgeving)
- Gradio/Streamlit-demo's voor visuele leerlingen
- Interactieve quizzen voor kennisbeoordeling

---

## 7. Meertalige ondersteuning

### 7.1 Huidige taalondersteuning

| Technologie | Gedekte lessen | Status |
|------------|-----------------|--------|
| Python | Alle | Volledig |
| TypeScript | 06-09, 11 | Gedeeltelijk |
| JavaScript | 06-08, 11 | Gedeeltelijk |
| .NET/C# | Sommige | Gedeeltelijk |

### 7.2 Aanbevolen toevoegingen

1. **Go** - Groeiend in AI/ML-tooling
2. **Rust** - Prestatiekritieke toepassingen
3. **Java/Kotlin** - Enterprise-toepassingen

---

## 8. Prestatieoptimalisaties

### 8.1 Optimalisaties op code niveau

1. **Async/Await-patronen**
   - Voeg async-voorbeelden toe voor batchverwerking
   - Demonstreer gelijktijdige API-aanroepen

2. **Caching-strategieën**
   - Voeg voorbeelden toe van embedding caching
   - Demonstreer response caching patronen

3. **Tokenoptimalisatie**
   - Voeg voorbeelden toe van tiktoken-gebruik
   - Demonstreer promptcompressietechnieken

### 8.2 Kostenoptimalisatievoorbeelden

Voeg voorbeelden toe die laten zien:
- Modelselectie op basis van taakcomplexiteit
- Prompt engineering voor token-efficiëntie
- Batchverwerking voor bulkbewerkingen

---

## 9. Toegankelijkheid en internationalisatie

### 9.1 Huidige vertaalstatus

Alle vertalingen zijn **voltooid** en worden automatisch gegenereerd door de [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst), die meer dan 50 taalversies van het curriculum produceert en synchroniseert met de Engelse bron. Vertaalde inhoud bevindt zich onder `translations/` en gelokaliseerde afbeeldingen onder `translated_images/`; de volledige lijst beschikbare talen staat bovenaan de repository README.

| Aspect | Status |
|--------|--------|
| Vertaaldekkingsgraad | Volledig — 50+ talen, alle lessen |
| Vertaalmethode | Geautomatiseerd via [Azure Co-op Translator](https://github.com/Azure/co-op-translator?WT.mc_id=academic-105485-koreyst) |
| Gesynchroniseerd met Engelse bron | Ja — automatisch opnieuw gegenereerd |

### 9.2 Verbeteringen voor toegankelijkheid

1. Voeg alt-tekst toe aan alle afbeeldingen
2. Zorg dat codevoorbeelden correcte syntaxhighlighting hebben
3. Voeg videotranscripties toe voor alle videocontent
4. Zorg dat kleurcontrasten voldoen aan WCAG-richtlijnen

---

## 10. Implementatieprioriteit

### Fase 1: Direct (Week 1-2)
- [x] Los kritieke beveiligingsproblemen op
- [x] Voeg codekwaliteitsconfiguratie toe
- [x] Maak gedeelde hulpprogramma's aan
- [x] Documenteer beveiligingsrichtlijnen

### Fase 2: Kortetermijn (Week 3-4)
- [x] Update verouderde API-patronen (Chat Completions → Responses API, Python + TypeScript)
- [ ] Voeg type hints toe aan alle Python-bestanden (gedaan voor het onderhouden `shared/`-module; lesvoorbeelden blijven eenvoudig)
- [x] Voeg CI/CD workflows toe voor codekwaliteit
- [x] Maak beveiligingsscanning workflow aan

### Fase 3: Middellange termijn (Maand 2-3)
- [ ] Voeg nieuwe beveiligingsles toe
- [ ] Voeg les toe over productie-implementatie
- [x] Verbeter DevContainer-setup
- [ ] Voeg interactieve demo's toe

### Fase 4: Lange termijn (Maand 4+)
- [ ] Voeg geavanceerde RAG-les toe
- [ ] Breid taaldekking uit
- [ ] Voeg uitgebreide testset toe
- [ ] Creëer certificeringsprogramma

---

## Conclusie

Deze roadmap biedt een gestructureerde aanpak om het Generative AI for Beginners-curriculum te verbeteren. Door beveiligingsproblemen aan te pakken, API's te moderniseren en educatieve inhoud toe te voegen, zal de cursus studenten beter voorbereiden op de ontwikkeling van AI-toepassingen in de praktijk.

Voor vragen of bijdragen kunt u een issue openen in de GitHub-repository.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->