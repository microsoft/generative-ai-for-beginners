# Vägkarta för Förbättrade Funktioner och Förbättringar

Detta dokument beskriver rekommenderade förbättringar och utvecklingar för kursplanen Generativ AI för Nybörjare, baserat på en omfattande kodgranskning och analys av branschens bästa praxis.

## Sammanfattning

Kodbasen har analyserats för säkerhet, kodkvalitet och utbildningseffektivitet. Detta dokument ger rekommendationer för omedelbara åtgärder, kortsiktiga förbättringar och framtida utvecklingar.

---

## 1. Säkerhetsförbättringar (Prioritet: Kritisk)

### 1.1 Omedelbara åtgärder (Slutförda)

| Problem | Påverkade filer | Status |
|---------|-----------------|--------|
| Inbäddad SECRET_KEY | `05-advanced-prompts/python/aoai-solution.py` | Åtgärdad |
| Saknad validering av miljövariabler | Flera JS/TS filer | Åtgärdad |
| Osäkra funktionsanrop | `11-integrating-with-function-calling/js-githubmodels/app.js` | Åtgärdad |
| Läckage av filhanterare | `08-building-search-applications/scripts/` | Åtgärdad |
| Saknade timeout för förfrågningar | `09-building-image-applications/python/` | Åtgärdad |

### 1.2 Rekommenderade ytterligare säkerhetsfunktioner

1. **Exempel på Rate Limiting**
   - Lägg till exempel som visar hur man implementerar rate limiting för API-anrop
   - Visa mönster för exponentiell backoff

2. **Rotation av API-nycklar**
   - Lägg till dokumentation om bästa praxis för rotation av API-nycklar
   - Inkludera exempel med Azure Key Vault eller liknande tjänster

3. **Integrering av innehållssäkerhet**
   - Lägg till exempel med Azure Content Safety API
   - Visa mönster för in- och utgångsmoderering

---

## 2. Förbättringar av kodkvalitet

### 2.1 Tillagda konfigurationsfiler

| Fil | Syfte |
|------|--------|
| `.eslintrc.json` | Lintningsregler för JavaScript/TypeScript |
| `.prettierrc` | Kodformateringsstandarder |
| `pyproject.toml` | Pythonverktygskonfiguration (Black, Ruff, mypy) |

### 2.2 Skapade gemensamma verktyg

Ny modul `shared/python/` med:
- `env_utils.py` - Hantering av miljövariabler
- `input_validation.py` - Validering och sanering av indata
- `api_utils.py` - Säker omslag för API-förfrågningar

### 2.3 Rekommenderade kodförbättringar

1. **Täcka typanteckningar**
   - Lägg till typanteckningar i alla Python-filer
   - Aktivera strikt TypeScript-läge i alla TS-projekt

2. **Dokumentationsstandarder**
   - Lägg till docstrings i alla Python-funktioner
   - Lägg till JSDoc-kommentarer i alla JavaScript/TypeScript-funktioner

3. **Testningsramverk**
   - Lägg till pytest-konfiguration och exempeltester
   - Lägg till Jest-konfiguration för JavaScript/TypeScript

---

## 3. Pedagogiska förbättringar

### 3.1 Nya ämnen för lektioner

1. **Säkerhet i AI-applikationer** (Föreslagen lektion 22)
   - Promptinjektionsattacker och skydd
   - Hantering av API-nycklar
   - Innehållsmoderering
   - Rate limiting och missbruksprevention

2. **Produktionssättning** (Föreslagen lektion 23)
   - Containerisering med Docker
   - CI/CD-pipelines
   - Övervakning och loggning
   - Kostnadshantering

3. **Avancerade RAG-tekniker** (Föreslagen lektion 24)
   - Hybrid-sökning (nyckelord + semantik)
   - Omrankningsstrategier
   - Multimodal RAG
   - Utvärderingsmått

### 3.2 Befintliga lektionsförbättringar

| Lektion | Rekommenderad förbättring |
|---------|-------------------------|
| 06 - Textgenerering | Lägg till exempel på streamingrespons |
| 07 - Chatt-applikationer | Lägg till mönster för konversationsminne |
| 08 - Sökapplikationer | Lägg till jämförelse av vektordatabaser |
| 09 - Bildgenerering | Lägg till exempel på bildredigering/variation |
| 11 - Funktionsanrop | Lägg till parallella funktionsanrop |
| 15 - RAG | Lägg till jämförelse av chunkningsstrategier |
| 17 - AI-agenter | Lägg till samordning av flera agenter |

---

## 4. API-modernisering

### 4.1 Föråldrade API-mönster att uppdatera

| Gammalt mönster | Nytt mönster | Påverkade filer |
|-----------------|--------------|-----------------|
| `openai.api_type = "azure"` | `AzureOpenAI()` klient | Flera skript i `08-building-search-applications/` |
| `openai.ChatCompletion.create()` | `client.chat.completions.create()` | Flera notebooks |
| `df.append()` (pandas) | `pd.concat()` | RAG-notebook |

### 4.2 Nya API-funktioner att demonstrera

1. **Strukturerade svar** (OpenAI)
   - JSON-läge
   - Funktionsanrop med strikta scheman

2. **Visionfunktioner**
   - Bildanalys med GPT-4V
   - Multimodala prompts

3. **Assistants API**
   - Kodtolk
   - Filsökning
   - Anpassade verktyg

---

## 5. Infrastrukturförbättringar

### 5.1 CI/CD-förbättringar

Nuvarande arbetsflöden hanterar markdownvalidering. Rekommenderade tillägg:

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

## 6. Förbättringar av utvecklarupplevelsen

### 6.1 Förbättringar av DevContainer

Uppdatera `.devcontainer/devcontainer.json`:

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

### 6.2 Interaktiv lekyta

Överväg att lägga till:
- Jupyter-notebooks med förifyllda API-nycklar (via miljövariabler)
- Gradio/Streamlit-demonstrationer för visuella elever
- Interaktiva quiz för kunskapsbedömning

---

## 7. Stöd för flera språk

### 7.1 Nuvarande språktäckning

| Teknik | Behandlade lektioner | Status |
|---------|--------------------|--------|
| Python | Alla | Komplett |
| TypeScript | 06-09, 11 | Partiell |
| JavaScript | 06-08, 11 | Partiell |
| .NET/C# | Vissa | Partiell |

### 7.2 Rekommenderade tillägg

1. **Go** - Växande inom AI/ML-verktyg
2. **Rust** - Prestandakritiska applikationer
3. **Java/Kotlin** - Företagsapplikationer

---

## 8. Prestandaoptimeringar

### 8.1 Optimeringar på kodnivå

1. **Async/Await-mönster**
   - Lägg till asynkrona exempel för batchbearbetning
   - Visa samtidiga API-anrop

2. **Cachingstrategier**
   - Lägg till exempel på caching av inbäddningar
   - Visa mönster för cache av svar

3. **Tokenoptimering**
   - Lägg till exempel på användning av tiktoken
   - Visa tekniker för promptkomprimering

### 8.2 Exempel på kostnadsoptimering

Lägg till exempel som visar:
- Modellval baserat på uppgiftskomplexitet
- Prompt-engineering för token-effektivitet
- Batchbearbetning för volymhantering

---

## 9. Tillgänglighet och Internationalisering

### 9.1 Nuvarande översättningsstatus

| Språk | Status |
|--------|--------|
| Engelska | Komplett |
| Kinesiska (förenklad) | Komplett |
| Japanska | Komplett |
| Koreanska | Komplett |
| Spanska | Partiell |
| Portugisiska | Partiell |
| Turkiska | Partiell |
| Polska | Partiell |

### 9.2 Förbättringar av tillgänglighet

1. Lägg till alt-text för alla bilder
2. Säkerställ korrekt syntaxmarkering i kodexempel
3. Lägg till videotranskriptioner för allt videoinnehåll
4. Säkerställ att färgkontraster uppfyller WCAG-riktlinjer

---

## 10. Prioritering av implementering

### Fas 1: Omedelbart (Vecka 1-2)
- [x] Åtgärda kritiska säkerhetsproblem
- [x] Lägg till konfiguration för kodkvalitet
- [x] Skapa gemensamma verktyg
- [x] Dokumentera säkerhetsriktlinjer

### Fas 2: Kort sikt (Vecka 3-4)
- [ ] Uppdatera föråldrade API-mönster
- [ ] Lägg till typanteckningar i alla Python-filer
- [ ] Lägg till CI/CD-arbetsflöden för kodkvalitet
- [ ] Skapa arbetsflöde för säkerhetsskanning

### Fas 3: Medellång sikt (Månad 2-3)
- [ ] Lägg till ny säkerhetslektion
- [ ] Lägg till lektionsmodul för produktionssättning
- [ ] Förbättra DevContainer-installation
- [ ] Lägg till interaktiva demonstrationer

### Fas 4: Lång sikt (Månad 4+)
- [ ] Lägg till avancerad RAG-lektion
- [ ] Utöka språktäckningen
- [ ] Lägg till komplett testsuite
- [ ] Skapa certifieringsprogram

---

## Slutsats

Denna vägkarta ger en strukturerad metod för att förbättra kursplanen Generativ AI för Nybörjare. Genom att adressera säkerhetsaspekter, modernisera API:er och lägga till pedagogiskt innehåll kommer kursen bättre förbereda studenter för verklig utveckling av AI-applikationer.

För frågor eller bidrag, vänligen öppna en issue i GitHub-repositoriet.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår på grund av användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->