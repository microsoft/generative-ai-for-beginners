# AGENTS.md

## Projektoversigt

Dette repository indeholder en omfattende 21-lektioners undervisningsplan, der lærer Generativ AI grundlæggende og applikationsudvikling. Kurset er designet til begyndere og dækker alt fra grundlæggende begreber til opbygning af produktionsklare applikationer.

**Nøgle teknologier:**
- Python 3.9+ med biblioteker: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript med Node.js og biblioteker: `openai` (Azure OpenAI via v1 endpoint + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI Service, OpenAI API, og Microsoft Foundry Models (GitHub Models udfases ved udgangen af juli 2026)
- Jupyter Notebooks til interaktiv læring
- Dev Containers for konsistent udviklingsmiljø

**Repository Struktur:**
- 21 nummererede lektionsmapper (00-21) med READMEs, kodeeksempler, og opgaver
- Flere implementeringer: Python, TypeScript, og nogle gange .NET eksempler
- Oversættelsesmappe med 40+ sprogversioner
- Central konfiguration via `.env` fil (brug `.env.copy` som skabelon)

## Opsætningskommandoer

### Indledende Repository Opsætning

```bash
# Klon arkivet
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Kopier miljøskabelonen
cp .env.copy .env
# Rediger .env med dine API-nøgler og slutpunkter
```

### Python Miljøopsætning

```bash
# Opret virtuelt miljø
python3 -m venv venv

# Aktiver virtuelt miljø
# På macOS/Linux:
source venv/bin/activate
# På Windows:
venv\Scripts\activate

# Installer afhængigheder
pip install -r requirements.txt
```

### Node.js/TypeScript Opsætning

```bash
# Installer root-level afhængigheder (til dokumentationsværktøj)
npm install

# For individuelle lektion TypeScript-eksempler, naviger til den specifikke lektion:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container Opsætning (Anbefalet)

Repositoryet inkluderer en `.devcontainer` konfiguration til GitHub Codespaces eller VS Code Dev Containers:

1. Åbn repository i GitHub Codespaces eller VS Code med Dev Containers-udvidelsen
2. Dev Container vil automatisk:
   - Installere Python-afhængigheder fra `requirements.txt`
   - Køre post-create script (`.devcontainer/post-create.sh`)
   - Opsætte Jupyter kernel

## Udviklingsarbejdsgang

### Miljøvariable

Alle lektioner, der kræver API-adgang, bruger miljøvariable defineret i `.env`:

- `OPENAI_API_KEY` - Til OpenAI API
- `AZURE_OPENAI_API_KEY` - Til Azure OpenAI i Microsoft Foundry (Azure OpenAI Service er nu en del af Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI endpoint URL (Foundry ressource endpoint)
- `AZURE_OPENAI_DEPLOYMENT` - Chat completion model deployment navn
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Embeddings model deployment navn
- `AZURE_OPENAI_API_VERSION` - API version (standard: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Til Hugging Face modeller
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry Models endpoint (multi-udbyder model katalog)
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry Models API nøgle (erstatter det udfasede `GITHUB_TOKEN`)

### Kørsel af Python Eksempler

```bash
# Naviger til lektionsmappen
cd 06-text-generation-apps/python

# Kør et Python-script
python aoai-app.py
```

### Kørsel af TypeScript Eksempler

```bash
# Naviger til TypeScript-appmappen
cd 06-text-generation-apps/typescript/recipe-app

# Byg TypeScript-koden
npm run build

# Kør applikationen
npm start
```

### Kørsel af Jupyter Notebooks

```bash
# Start Jupyter i rodmappen for depotet
jupyter notebook

# Eller brug VS Code med Jupyter-udvidelsen
```

### Arbejde med Forskellige Lektionstyper

- **"Learn" lektioner**: Fokus på README.md dokumentation og koncepter
- **"Build" lektioner**: Indeholder fungerende kodeeksempler i Python og TypeScript
- Hver lektion har en README.md med teori, kodegennemgange, og links til videoindhold

## Kodestil Retningslinjer

### Python

- Brug `python-dotenv` til håndtering af miljøvariable
- Importer `openai` bibliotek til API-interaktioner
- Brug `pylint` til linting (nogle eksempler inkluderer `# pylint: disable=all` for enkelhed)
- Følg PEP 8 navnekonventioner
- Opbevar API legitimationsoplysninger i `.env` fil, aldrig i kode

### TypeScript

- Brug `dotenv` pakken til miljøvariable
- TypeScript konfiguration i `tsconfig.json` for hver app
- Brug `openai` pakken til Azure OpenAI (peg klienten mod `/openai/v1/` endpoint og kald `client.responses.create`); brug `@azure-rest/ai-inference` til Microsoft Foundry Models
- Brug `nodemon` til udvikling med auto-genindlæsning
- Byg før kørsel: `npm run build` derefter `npm start`

### Generelle Konventioner

- Hold kodeeksempler enkle og didaktiske
- Inkluder kommentarer, der forklarer nøglebegreber
- Hver lektions kode skal være selvstændig og kørbar
- Brug konsekvent navngivning: `aoai-` præfiks for Azure OpenAI, `oai-` for OpenAI API, `githubmodels-` for Microsoft Foundry Models (legacy præfiks bevaret fra GitHub Models perioden)

## Dokumentationsretningslinjer

### Markdown Stil

- Alle URL'er skal være indpakket i `[text](../../url)` format uden ekstra mellemrum
- Relative links skal starte med `./` eller `../`
- Alle links til Microsoft domæner skal indeholde tracking ID: `?WT.mc_id=academic-105485-koreyst`
- Ingen landespecifikke lokaliteter i URL'er (undgå `/en-us/`)
- Billeder gemmes i `./images` mappe med beskrivende navne
- Brug engelske tegn, tal og bindestreger i filnavne

### Oversættelsesstøtte

- Repository understøtter 40+ sprog via automatiserede GitHub Actions
- Oversættelser gemmes i `translations/` mappen
- Indsend ikke delvise oversættelser
- Maskinoversættelser accepteres ikke
- Oversatte billeder gemmes i `translated_images/` mappen

## Test og Validering

### Pre-indsendelseskontroller

Dette repository bruger GitHub Actions til validering. Før du indsender PR'er:

1. **Tjek Markdown Links**:
   ```bash
   # validate-markdown.yml-arbejdsgangen kontrollerer:
   # - Ødelagte relative stier
   # - Manglende sporings-id'er på stier
   # - Manglende sporings-id'er på URL'er
   # - URL'er med landelokale
   # - Ødelagte eksterne URL'er
   ```

2. **Manuel Test**:
   - Test Python eksempler: Aktivér venv og kør scripts
   - Test TypeScript eksempler: `npm install`, `npm run build`, `npm start`
   - Verificer at miljøvariable er konfigureret korrekt
   - Tjek at API-nøgler virker med kodeeksemplerne

3. **Kodeeksempler**:
   - Sikr at al kode kører uden fejl
   - Test med både Azure OpenAI og OpenAI API hvor relevant
   - Verificer at eksempler virker med Microsoft Foundry Models, hvor understøttet

### Ingen Automatiske Tests

Dette er et undervisningsrepository fokuseret på tutorials og eksempler. Der er ingen unit tests eller integrationstests at køre. Validering sker primært ved:
- Manuel test af kodeeksempler
- GitHub Actions til Markdown validering
- Community review af undervisningsindhold

## Retningslinjer for Pull Requests

### Før Indsendelse

1. Test kodeændringer i både Python og TypeScript hvor relevant
2. Kør Markdown validering (udløses automatisk ved PR)
3. Sikr at tracking IDs er til stede på alle Microsoft URL'er
4. Tjek at relative links er gyldige
5. Verificer at billeder er korrekt refererede

### PR Titel Format

- Brug beskrivende titler: `[Lesson 06] Fix Python eksempel fejl` eller `Opdater README for lektion 08`
- Referer til issue numre når relevant: `Fixes #123`

### PR Beskrivelse

- Forklar hvad der er ændret og hvorfor
- Link til relaterede issues
- For kodeændringer, specificer hvilke eksempler der er testet
- For oversættelses-PR'er, inkluder alle filer for en komplet oversættelse

### Bidragskrav

- Underskriv Microsoft CLA (automatisk ved første PR)
- Fork repository til din konto før ændringer
- Én PR per logisk ændring (kombiner ikke urelaterede rettelser)
- Hold PR'er fokuserede og små, når muligt

## Almindelige Arbejdsgange

### Tilføjelse af Nyt Kodeeksempel

1. Naviger til den relevante lektionsmappe
2. Opret eksempel i `python/` eller `typescript/` undermappe
3. Følg navngivningskonvention: `{provider}-{example-name}.{py|ts|js}`
4. Test med faktiske API legitimationsoplysninger
5. Dokumenter nye miljøvariable i lektions README

### Opdatering af Dokumentation

1. Rediger README.md i lektionsmappen
2. Følg Markdown retningslinjer (tracking IDs, relative links)
3. Opdateringer af oversættelser håndteres af GitHub Actions (rediger ikke manuelt)
4. Test at alle links er gyldige

### Arbejde med Dev Containers

1. Repository inkluderer `.devcontainer/devcontainer.json`
2. Post-create script installerer Python afhængigheder automatisk
3. Udvidelser til Python og Jupyter er forudkonfigurerede
4. Miljøet er baseret på `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Udrulning og Publicering

Dette er et læringsrepository - der er ingen udrulningsproces. Undervisningsplanen benyttes via:

1. **GitHub Repository**: Direkte adgang til kode og dokumentation
2. **GitHub Codespaces**: Øjeblikkeligt udviklingsmiljø med forudkonfigureret opsætning
3. **Microsoft Learn**: Indhold kan blive syndikeret til den officielle læringsplatform
4. **docsify**: Dokumentationsside bygget fra Markdown (se `docsifytopdf.js` og `package.json`)

### Bygning af Dokumentationsside

```bash
# Generer PDF fra dokumentationen (hvis nødvendigt)
npm run convert
```

## Fejlfinding

### Almindelige Problemer

**Python Importfejl**:
- Sikr at det virtuelle miljø er aktiveret
- Kør `pip install -r requirements.txt`
- Tjek at Python versionen er 3.9+

**TypeScript Bygningsfejl**:
- Kør `npm install` i den specifikke appmappe
- Tjek at Node.js version er kompatibel
- Ryd `node_modules` og geninstaller om nødvendigt

**API Autentificeringsfejl**:
- Verificer at `.env` filen findes og har korrekte værdier
- Tjek at API-nøgler er gyldige og ikke udløbet
- Sikr at endpoint URLs er korrekte for din region

**Manglende Miljøvariable**:
- Kopier `.env.copy` til `.env`
- Udfyld alle påkrævede værdier for den lektion, du arbejder på
- Genstart din applikation efter opdatering af `.env`

## Yderligere Ressourcer

- [Course Setup Guide](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Contributing Guidelines](./CONTRIBUTING.md)
- [Code of Conduct](./CODE_OF_CONDUCT.md)
- [Security Policy](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Collection of Advanced Code Samples](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Projektspecifikke Noter

- Dette er et **undervisningsrepository** fokus på læring, ikke produktionskode
- Eksempler er bevidst simple og fokuseret på at undervise koncepter
- Kodekvaliteten afbalanceres med undervisningsklarhed
- Hver lektion er selvstændig og kan gennemføres uafhængigt
- Repositoryet understøtter flere API-udbydere: Azure OpenAI, OpenAI, Microsoft Foundry Models og offline udbydere såsom Foundry Local og Ollama
- Indholdet er flersproget med automatiserede oversættelses-workflows
- Aktivt fællesskab på Discord til spørgsmål og support

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->