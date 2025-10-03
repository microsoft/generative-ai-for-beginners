<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T11:03:47+00:00",
  "source_file": "AGENTS.md",
  "language_code": "sv"
}
-->
# AGENTS.md

## Projektöversikt

Det här arkivet innehåller en omfattande kurs med 21 lektioner som lär ut grunderna i Generativ AI och applikationsutveckling. Kursen är utformad för nybörjare och täcker allt från grundläggande koncept till att bygga produktionsklara applikationer.

**Nyckelteknologier:**
- Python 3.9+ med bibliotek: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript med Node.js och bibliotek: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API och GitHub Models
- Jupyter Notebooks för interaktivt lärande
- Dev Containers för en konsekvent utvecklingsmiljö

**Arkivstruktur:**
- 21 numrerade lektionskataloger (00-21) som innehåller README-filer, kodexempel och uppgifter
- Flera implementationer: Python, TypeScript och ibland .NET-exempel
- Översättningskatalog med versioner på över 40 språk
- Centraliserad konfiguration via `.env`-fil (använd `.env.copy` som mall)

## Installationskommandon

### Initial inställning av arkivet

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Inställning av Python-miljö

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

### Inställning av Node.js/TypeScript

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Inställning av Dev Container (rekommenderas)

Arkivet innehåller en `.devcontainer`-konfiguration för GitHub Codespaces eller VS Code Dev Containers:

1. Öppna arkivet i GitHub Codespaces eller VS Code med Dev Containers-tillägget
2. Dev Container kommer automatiskt att:
   - Installera Python-beroenden från `requirements.txt`
   - Köra post-create-skriptet (`.devcontainer/post-create.sh`)
   - Ställa in Jupyter-kärnan

## Utvecklingsarbetsflöde

### Miljövariabler

Alla lektioner som kräver API-åtkomst använder miljövariabler definierade i `.env`:

- `OPENAI_API_KEY` - För OpenAI API
- `AZURE_OPENAI_API_KEY` - För Azure OpenAI Service
- `AZURE_OPENAI_ENDPOINT` - URL för Azure OpenAI endpoint
- `AZURE_OPENAI_DEPLOYMENT` - Namn på chat completion-modellens distribution
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Namn på embeddings-modellens distribution
- `AZURE_OPENAI_API_VERSION` - API-version (standard: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - För Hugging Face-modeller
- `GITHUB_TOKEN` - För GitHub Models

### Köra Python-exempel

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### Köra TypeScript-exempel

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Köra Jupyter Notebooks

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### Arbeta med olika lektionsformat

- **"Learn"-lektioner**: Fokus på README.md-dokumentation och koncept
- **"Build"-lektioner**: Innehåller fungerande kodexempel i Python och TypeScript
- Varje lektion har en README.md med teori, kodgenomgångar och länkar till videoinnehåll

## Kodstilsguider

### Python

- Använd `python-dotenv` för hantering av miljövariabler
- Importera `openai`-biblioteket för API-interaktioner
- Använd `pylint` för linting (vissa exempel inkluderar `# pylint: disable=all` för enkelhetens skull)
- Följ PEP 8-namngivningskonventioner
- Spara API-uppgifter i `.env`-filen, aldrig i koden

### TypeScript

- Använd `dotenv`-paketet för miljövariabler
- TypeScript-konfiguration i `tsconfig.json` för varje app
- Använd `@azure/openai` eller `@azure-rest/ai-inference` för Azure-tjänster
- Använd `nodemon` för utveckling med automatisk omladdning
- Bygg innan körning: `npm run build` följt av `npm start`

### Allmänna konventioner

- Håll kodexempel enkla och pedagogiska
- Inkludera kommentarer som förklarar nyckelkoncept
- Varje lektions kod ska vara självständig och körbar
- Använd konsekvent namngivning: `aoai-` prefix för Azure OpenAI, `oai-` för OpenAI API, `githubmodels-` för GitHub Models

## Dokumentationsguider

### Markdown-stil

- Alla URL:er måste vara inslagna i `[text](../../url)`-format utan extra mellanslag
- Relativa länkar måste börja med `./` eller `../`
- Alla länkar till Microsoft-domäner måste inkludera spårnings-ID: `?WT.mc_id=academic-105485-koreyst`
- Inga landsspecifika lokaler i URL:er (undvik `/en-us/`)
- Bilder lagras i `./images`-mappen med beskrivande namn
- Använd engelska tecken, siffror och bindestreck i filnamn

### Översättningsstöd

- Arkivet stödjer över 40 språk via automatiserade GitHub Actions
- Översättningar lagras i `translations/`-katalogen
- Skicka inte in ofullständiga översättningar
- Maskinöversättningar accepteras inte
- Översatta bilder lagras i `translated_images/`-katalogen

## Testning och validering

### Kontroll före inlämning

Det här arkivet använder GitHub Actions för validering. Innan du skickar in PRs:

1. **Kontrollera Markdown-länkar**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Manuell testning**:
   - Testa Python-exempel: Aktivera venv och kör skript
   - Testa TypeScript-exempel: `npm install`, `npm run build`, `npm start`
   - Kontrollera att miljövariabler är korrekt konfigurerade
   - Kontrollera att API-nycklar fungerar med kodexemplen

3. **Kodexempel**:
   - Säkerställ att all kod körs utan fel
   - Testa med både Azure OpenAI och OpenAI API när det är tillämpligt
   - Kontrollera att exemplen fungerar med GitHub Models där det stöds

### Inga automatiserade tester

Det här är ett utbildningsarkiv som fokuserar på handledningar och exempel. Det finns inga enhetstester eller integrationstester att köra. Validering sker främst genom:
- Manuell testning av kodexempel
- GitHub Actions för Markdown-validering
- Gemenskapsgranskning av utbildningsinnehåll

## Riktlinjer för pull requests

### Innan inlämning

1. Testa kodändringar i både Python och TypeScript när det är tillämpligt
2. Kör Markdown-validering (utlöses automatiskt vid PR)
3. Säkerställ att spårnings-ID finns på alla Microsoft-URL:er
4. Kontrollera att relativa länkar är giltiga
5. Kontrollera att bilder är korrekt refererade

### Format för PR-titlar

- Använd beskrivande titlar: `[Lesson 06] Fix Python example typo` eller `Update README for lesson 08`
- Referera till ärendenummer när det är tillämpligt: `Fixes #123`

### PR-beskrivning

- Förklara vad som ändrades och varför
- Länka till relaterade ärenden
- För kodändringar, specificera vilka exempel som testades
- För översättnings-PRs, inkludera alla filer för en komplett översättning

### Krav för bidrag

- Signera Microsoft CLA (automatiskt vid första PR)
- Forka arkivet till ditt konto innan du gör ändringar
- En PR per logisk ändring (kombinera inte orelaterade fixar)
- Håll PRs fokuserade och små när det är möjligt

## Vanliga arbetsflöden

### Lägga till ett nytt kodexempel

1. Navigera till rätt lektionskatalog
2. Skapa exempel i `python/` eller `typescript/` underkatalogen
3. Följ namngivningskonventionen: `{provider}-{example-name}.{py|ts|js}`
4. Testa med faktiska API-uppgifter
5. Dokumentera eventuella nya miljövariabler i lektions-README

### Uppdatera dokumentation

1. Redigera README.md i lektionskatalogen
2. Följ Markdown-riktlinjer (spårnings-ID, relativa länkar)
3. Uppdateringar av översättningar hanteras av GitHub Actions (redigera inte manuellt)
4. Testa att alla länkar är giltiga

### Arbeta med Dev Containers

1. Arkivet inkluderar `.devcontainer/devcontainer.json`
2. Post-create-skriptet installerar Python-beroenden automatiskt
3. Tillägg för Python och Jupyter är förkonfigurerade
4. Miljön baseras på `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Distribution och publicering

Det här är ett utbildningsarkiv - det finns ingen distributionsprocess. Kursen används av:

1. **GitHub-arkiv**: Direkt åtkomst till kod och dokumentation
2. **GitHub Codespaces**: Omedelbar utvecklingsmiljö med förkonfigurerad inställning
3. **Microsoft Learn**: Innehåll kan syndikeras till den officiella lärplattformen
4. **docsify**: Dokumentationssida byggd från Markdown (se `docsifytopdf.js` och `package.json`)

### Bygga dokumentationssida

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Felsökning

### Vanliga problem

**Importfel i Python**:
- Kontrollera att den virtuella miljön är aktiverad
- Kör `pip install -r requirements.txt`
- Kontrollera att Python-versionen är 3.9+

**Byggfel i TypeScript**:
- Kör `npm install` i den specifika appkatalogen
- Kontrollera att Node.js-versionen är kompatibel
- Rensa `node_modules` och installera om vid behov

**Autentiseringsfel för API**:
- Kontrollera att `.env`-filen finns och har korrekta värden
- Kontrollera att API-nycklar är giltiga och inte har gått ut
- Säkerställ att endpoint-URL:er är korrekta för din region

**Saknade miljövariabler**:
- Kopiera `.env.copy` till `.env`
- Fyll i alla nödvändiga värden för lektionen du arbetar med
- Starta om din applikation efter att ha uppdaterat `.env`

## Ytterligare resurser

- [Kursens installationsguide](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Riktlinjer för bidrag](./CONTRIBUTING.md)
- [Uppförandekod](./CODE_OF_CONDUCT.md)
- [Säkerhetspolicy](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Samling av avancerade kodexempel](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Projekt-specifika anteckningar

- Detta är ett **utbildningsarkiv** som fokuserar på lärande, inte produktionskod
- Exemplen är avsiktligt enkla och fokuserade på att lära ut koncept
- Kodkvaliteten balanseras med pedagogisk tydlighet
- Varje lektion är självständig och kan genomföras oberoende
- Arkivet stödjer flera API-leverantörer: Azure OpenAI, OpenAI och GitHub Models
- Innehållet är flerspråkigt med automatiserade översättningsarbetsflöden
- Aktiv gemenskap på Discord för frågor och support

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.