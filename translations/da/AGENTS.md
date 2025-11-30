<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T11:04:06+00:00",
  "source_file": "AGENTS.md",
  "language_code": "da"
}
-->
# AGENTS.md

## Projektoversigt

Dette repository indeholder et omfattende 21-lektions pensum, der underviser i grundlæggende Generativ AI og applikationsudvikling. Kurset er designet til begyndere og dækker alt fra basale koncepter til opbygning af produktionsklare applikationer.

**Nøgleteknologier:**
- Python 3.9+ med biblioteker: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript med Node.js og biblioteker: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API og GitHub Models
- Jupyter Notebooks til interaktiv læring
- Dev Containers for et konsistent udviklingsmiljø

**Repository-struktur:**
- 21 nummererede lektionsmapper (00-21) med READMEs, kodeeksempler og opgaver
- Flere implementeringer: Python, TypeScript og nogle gange .NET-eksempler
- Oversættelsesmappe med versioner på 40+ sprog
- Centraliseret konfiguration via `.env`-fil (brug `.env.copy` som skabelon)

## Opsætningskommandoer

### Initial Repository Opsætning

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Opsætning af Python-miljø

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

### Opsætning af Node.js/TypeScript

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Opsætning af Dev Container (Anbefalet)

Repositoryet inkluderer en `.devcontainer`-konfiguration til GitHub Codespaces eller VS Code Dev Containers:

1. Åbn repositoryet i GitHub Codespaces eller VS Code med Dev Containers-udvidelsen
2. Dev Container vil automatisk:
   - Installere Python-afhængigheder fra `requirements.txt`
   - Køre post-create script (`.devcontainer/post-create.sh`)
   - Opsætte Jupyter-kernel

## Udviklingsworkflow

### Miljøvariabler

Alle lektioner, der kræver API-adgang, bruger miljøvariabler defineret i `.env`:

- `OPENAI_API_KEY` - Til OpenAI API
- `AZURE_OPENAI_API_KEY` - Til Azure OpenAI Service
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI endpoint-URL
- `AZURE_OPENAI_DEPLOYMENT` - Chat completion model deployment-navn
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Embeddings model deployment-navn
- `AZURE_OPENAI_API_VERSION` - API-version (standard: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Til Hugging Face-modeller
- `GITHUB_TOKEN` - Til GitHub Models

### Kørsel af Python-eksempler

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### Kørsel af TypeScript-eksempler

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Kørsel af Jupyter Notebooks

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### Arbejde med forskellige lektionstyper

- **"Learn"-lektioner**: Fokus på README.md-dokumentation og koncepter
- **"Build"-lektioner**: Indeholder fungerende kodeeksempler i Python og TypeScript
- Hver lektion har en README.md med teori, kodegennemgange og links til videomateriale

## Kodestilretningslinjer

### Python

- Brug `python-dotenv` til håndtering af miljøvariabler
- Importér `openai`-biblioteket til API-interaktioner
- Brug `pylint` til linting (nogle eksempler inkluderer `# pylint: disable=all` for enkelhed)
- Følg PEP 8-navngivningskonventioner
- Gem API-legitimationsoplysninger i `.env`-filen, aldrig i koden

### TypeScript

- Brug `dotenv`-pakken til miljøvariabler
- TypeScript-konfiguration i `tsconfig.json` for hver app
- Brug `@azure/openai` eller `@azure-rest/ai-inference` til Azure-tjenester
- Brug `nodemon` til udvikling med automatisk genindlæsning
- Byg før kørsel: `npm run build` og derefter `npm start`

### Generelle konventioner

- Hold kodeeksempler enkle og pædagogiske
- Inkluder kommentarer, der forklarer nøglekoncepter
- Hver lektions kode skal være selvstændig og kørbar
- Brug konsekvente navne: `aoai-` præfiks for Azure OpenAI, `oai-` for OpenAI API, `githubmodels-` for GitHub Models

## Dokumentationsretningslinjer

### Markdown-stil

- Alle URL'er skal være indpakket i `[tekst](../../url)`-format uden ekstra mellemrum
- Relative links skal starte med `./` eller `../`
- Alle links til Microsoft-domæner skal inkludere tracking-ID: `?WT.mc_id=academic-105485-koreyst`
- Ingen landespecifikke lokaliteter i URL'er (undgå `/en-us/`)
- Billeder gemmes i `./images`-mappen med beskrivende navne
- Brug engelske tegn, tal og bindestreger i filnavne

### Oversættelsesstøtte

- Repositoryet understøtter 40+ sprog via automatiserede GitHub Actions
- Oversættelser gemmes i `translations/`-mappen
- Indsend ikke delvise oversættelser
- Maskinoversættelser accepteres ikke
- Oversatte billeder gemmes i `translated_images/`-mappen

## Test og validering

### Kontroller før indsendelse

Dette repository bruger GitHub Actions til validering. Før du indsender PR'er:

1. **Kontroller Markdown-links**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Manuel testning**:
   - Test Python-eksempler: Aktivér venv og kør scripts
   - Test TypeScript-eksempler: `npm install`, `npm run build`, `npm start`
   - Verificér, at miljøvariabler er korrekt konfigureret
   - Kontroller, at API-nøgler fungerer med kodeeksemplerne

3. **Kodeeksempler**:
   - Sørg for, at al kode kører uden fejl
   - Test med både Azure OpenAI og OpenAI API, hvor det er relevant
   - Verificér, at eksempler fungerer med GitHub Models, hvor det understøttes

### Ingen automatiserede tests

Dette er et pædagogisk repository med fokus på tutorials og eksempler. Der er ingen enhedstests eller integrationstests at køre. Validering er primært:
- Manuel testning af kodeeksempler
- GitHub Actions til Markdown-validering
- Fællesskabets gennemgang af undervisningsindhold

## Retningslinjer for Pull Requests

### Før indsendelse

1. Test kodeændringer i både Python og TypeScript, hvor det er relevant
2. Kør Markdown-validering (udløses automatisk ved PR)
3. Sørg for, at tracking-ID'er er til stede på alle Microsoft-URL'er
4. Kontroller, at relative links er gyldige
5. Verificér, at billeder er korrekt refereret

### PR-titelformat

- Brug beskrivende titler: `[Lesson 06] Fix Python example typo` eller `Update README for lesson 08`
- Referér til issue-numre, hvor det er relevant: `Fixes #123`

### PR-beskrivelse

- Forklar, hvad der blev ændret, og hvorfor
- Link til relaterede issues
- For kodeændringer, specificér hvilke eksempler der blev testet
- For oversættelses-PR'er, inkluder alle filer for en komplet oversættelse

### Bidragskrav

- Underskriv Microsoft CLA (automatisk ved første PR)
- Fork repositoryet til din konto, før du foretager ændringer
- Én PR pr. logisk ændring (kombinér ikke urelaterede rettelser)
- Hold PR'er fokuserede og små, når det er muligt

## Almindelige arbejdsprocesser

### Tilføjelse af et nyt kodeeksempel

1. Navigér til den relevante lektionsmappe
2. Opret eksempel i `python/` eller `typescript/` undermappen
3. Følg navngivningskonventionen: `{provider}-{example-name}.{py|ts|js}`
4. Test med faktiske API-legitimationsoplysninger
5. Dokumentér eventuelle nye miljøvariabler i lektions-README

### Opdatering af dokumentation

1. Redigér README.md i lektionsmappen
2. Følg Markdown-retningslinjerne (tracking-ID'er, relative links)
3. Opdaterede oversættelser håndteres af GitHub Actions (redigér ikke manuelt)
4. Test, at alle links er gyldige

### Arbejde med Dev Containers

1. Repositoryet inkluderer `.devcontainer/devcontainer.json`
2. Post-create script installerer automatisk Python-afhængigheder
3. Udvidelser til Python og Jupyter er forudkonfigurerede
4. Miljøet er baseret på `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Udgivelse og publicering

Dette er et læringsrepository - der er ingen udrulningsproces. Pensum bruges af:

1. **GitHub Repository**: Direkte adgang til kode og dokumentation
2. **GitHub Codespaces**: Øjeblikkeligt udviklingsmiljø med forudkonfigureret opsætning
3. **Microsoft Learn**: Indhold kan syndikeres til den officielle læringsplatform
4. **docsify**: Dokumentationsside bygget fra Markdown (se `docsifytopdf.js` og `package.json`)

### Bygning af dokumentationsside

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Fejlfinding

### Almindelige problemer

**Python-importfejl**:
- Sørg for, at det virtuelle miljø er aktiveret
- Kør `pip install -r requirements.txt`
- Kontroller, at Python-versionen er 3.9+

**TypeScript-byggefejl**:
- Kør `npm install` i den specifikke app-mappe
- Kontroller, at Node.js-versionen er kompatibel
- Ryd `node_modules` og geninstaller, hvis nødvendigt

**API-autentificeringsfejl**:
- Verificér, at `.env`-filen eksisterer og har korrekte værdier
- Kontroller, at API-nøgler er gyldige og ikke udløbet
- Sørg for, at endpoint-URL'er er korrekte for din region

**Manglende miljøvariabler**:
- Kopiér `.env.copy` til `.env`
- Udfyld alle nødvendige værdier for den lektion, du arbejder på
- Genstart din applikation efter opdatering af `.env`

## Yderligere ressourcer

- [Kursusopsætningsguide](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Retningslinjer for bidrag](./CONTRIBUTING.md)
- [Adfærdskodeks](./CODE_OF_CONDUCT.md)
- [Sikkerhedspolitik](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Samling af avancerede kodeeksempler](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Projektspecifikke noter

- Dette er et **pædagogisk repository** med fokus på læring, ikke produktionskode
- Eksempler er bevidst enkle og fokuseret på undervisning i koncepter
- Kvaliteten af koden balanceres med pædagogisk klarhed
- Hver lektion er selvstændig og kan gennemføres uafhængigt
- Repositoryet understøtter flere API-udbydere: Azure OpenAI, OpenAI og GitHub Models
- Indholdet er flersproget med automatiserede oversættelsesarbejdsgange
- Aktivt fællesskab på Discord til spørgsmål og support

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.