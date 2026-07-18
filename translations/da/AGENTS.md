# AGENTS.md

## Projektoversigt

Dette repository indeholder et omfattende kursus med 21 lektioner, der underviser i grundlæggende generativ AI og applikationsudvikling. Kurset er designet til begyndere og dækker alt fra grundlæggende koncepter til opbygning af produktionsklare applikationer.

**Nøgle-teknologier:**
- Python 3.9+ med biblioteker: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript med Node.js og biblioteker: `openai` (Azure OpenAI via v1-endpoint + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI Service, OpenAI API og Microsoft Foundry Models (GitHub Models udfases ved udgangen af juli 2026)
- Jupyter Notebooks til interaktiv læring
- Dev Containers til ensartet udviklingsmiljø

**Repository struktur:**
- 21 nummererede lektionsmapper (00-21) indeholdende README-filer, kodeeksempler og opgaver
- Flere implementeringer: Python, TypeScript og nogle gange .NET eksempler
- Oversættelsesmappe med over 40 sprogversioner
- Centraliseret konfiguration via `.env` fil (brug `.env.copy` som skabelon)

## Opsætningskommandoer

### Initial opsætning af repository

```bash
# Klon depotet
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Kopier miljøskabelon
cp .env.copy .env
# Rediger .env med dine API-nøgler og slutpunkter
```

### Python miljøopsætning

```bash
# Opret virtuel miljø
python3 -m venv venv

# Aktivér virtuel miljø
# På macOS/Linux:
source venv/bin/activate
# På Windows:
venv\Scripts\activate

# Installer afhængigheder
pip install -r requirements.txt
```

### Node.js/TypeScript opsætning

```bash
# Installer afhængigheder på rodbaseniveau (til dokumentationsværktøjer)
npm install

# For individuelle lektioners TypeScript-eksempler, naviger til den specifikke lektion:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container opsætning (anbefalet)

Repository indeholder en `.devcontainer` konfiguration til GitHub Codespaces eller VS Code Dev Containers:

1. Åbn repository i GitHub Codespaces eller VS Code med Dev Containers-udvidelsen
2. Dev Container vil automatisk:
   - Installere Python-afhængigheder fra `requirements.txt`
   - Køre efter-oprettelses script (`.devcontainer/post-create.sh`)
   - Sætte Jupyter kernel op

## Udviklingsworkflow

### Miljøvariabler

Alle lektioner der kræver API-adgang bruger miljøvariabler defineret i `.env`:

- `OPENAI_API_KEY` - Til OpenAI API
- `AZURE_OPENAI_API_KEY` - Til Azure OpenAI i Microsoft Foundry (Azure OpenAI Service er nu en del af Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI endpoint-URL (Foundry resource endpoint)
- `AZURE_OPENAI_DEPLOYMENT` - Navn på Chat completion model-udrulning (kursusstandard: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Navn på embeddings model-udrulning (kursusstandard: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - API-version (standard: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Til Hugging Face-modeller
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry Models endpoint (multi-udbyder modelkatalog)
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry Models API nøgle (erstatter den udfasede `GITHUB_TOKEN`)
- `AZURE_INFERENCE_CHAT_MODEL` - En ikke-begrundende model (f.eks. `Llama-3.3-70B-Instruct`) brugt i `temperature` eksempler, da begrundende modeller ikke understøtter sampling-kontroller

### Modelkonventioner (vigtige)

- **Standard chatmodel er `gpt-5-mini`** - en aktuel, ikke-udgået **begrundende** model. Fra 2026 udfases de ældre temperatur-kompatible "mini" modeller (`gpt-4o-mini`, `gpt-4.1-mini`), så pensum standardiserer på GPT-5 familien.
- **Begrundende modeller afviser `temperature` og `top_p`**, og bruger `max_output_tokens` (Responses API) / `max_completion_tokens` (chat completions) i stedet for `max_tokens`. Tilføj **ikke** `temperature`/`top_p`/`max_tokens` i eksempler der kalder `gpt-5-mini`.
- **For at demonstrere `temperature`**, bruger eksempler en **Llama** model (`Llama-3.3-70B-Instruct`) via Microsoft Foundry Models endpoint (`AZURE_INFERENCE_CHAT_MODEL`). Styr begrundende modeller med prompt-udformning + begrundelseskontroller i stedet for sampling-indstillinger.
- **Finjustering (lektion 18)** beholder `gpt-4.1-mini`: GPT-5 understøtter kun reinforcement finjustering (RFT), ikke superviseret finjustering (SFT) som vist der.
- Lektion 20 (Mistral) og 21 (Meta) beholder `temperature`/`max_tokens`, da de retter sig mod Mistral/Llama modeller, som understøtter det.

### Kørsel af Python-eksempler

```bash
# Naviger til lektionsmappen
cd 06-text-generation-apps/python

# Kør et Python-script
python aoai-app.py
```

### Kørsel af TypeScript-eksempler

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

### Arbejde med forskellige lektionstyper

- **"Lær" lektioner**: Fokus på README.md dokumentation og koncepter
- **"Byg" lektioner**: Indeholder fungerende kodeeksempler i Python og TypeScript
- Hver lektion har en README.md med teori, kodegennemgange og links til videoindhold

## Kode stil retningslinjer

### Python

- Brug `python-dotenv` til håndtering af miljøvariabler
- Importer `openai` bibliotek til API-interaktioner
- Brug `pylint` til kodeanalyse (nogle eksempler inkluderer `# pylint: disable=all` for enkelhed)
- Følg PEP 8 navngivningskonventioner
- Opbevar API legitimationsoplysninger i `.env` fil, aldrig i koden

### TypeScript

- Brug `dotenv` pakken til miljøvariabler
- TypeScript konfiguration i `tsconfig.json` for hver app
- Brug `openai` pakken til Azure OpenAI (peg klienten mod `/openai/v1/` endpoint og kald `client.responses.create`); brug `@azure-rest/ai-inference` til Microsoft Foundry Models
- Brug `nodemon` til udvikling med automatisk genstart
- Byg før kørsel: `npm run build` derefter `npm start`

### Generelle konventioner

- Hold kodeeksempler simple og pædagogiske
- Inkluder kommentarer der forklarer nøglekoncepter
- Hver lektions kode bør være selvstændig og kørbar
- Brug konsistent navngivning: `aoai-` præfiks for Azure OpenAI, `oai-` for OpenAI API, `githubmodels-` for Microsoft Foundry Models (arvet præfiks fra GitHub Models æraen)

## Dokumentationsretningslinjer

### Markdown stil

- Alle URL'er skal være pakket ind i `[text](../../url)` format uden ekstra mellemrum
- Relative links skal starte med `./` eller `../`
- Alle links til Microsoft-domæner skal inkludere tracking ID: `?WT.mc_id=academic-105485-koreyst`
- Ingen landespecifikke lokaliteter i URL'er (undgå `/en-us/`)
- Billeder gemmes i `./images` mappen med beskrivende navne
- Brug engelske tegn, tal og bindestreger i filnavne

### Oversættelsesstøtte

- Repository understøtter 40+ sprog via automatiserede GitHub Actions
- Oversættelser gemmes i `translations/` mappen
- Indsend ikke delvise oversættelser
- Maskinoversættelser accepteres ikke
- Oversatte billeder gemmes i `translated_images/` mappen

## Testning og validering

### Tjek før indsendelse

Dette repository bruger GitHub Actions til validering. Før PR'er indsendes:

1. **Tjek Markdown links**:
   ```bash
   # Validate-markdown.yml-arbejdsgangen kontrollerer:
   # - Ødelagte relative stier
   # - Manglende sporings-ID'er på stier
   # - Manglende sporings-ID'er på URL'er
   # - URL'er med landelokalisering
   # - Ødelagte eksterne URL'er
   ```

2. **Manuel test**:
   - Test Python-eksempler: Aktivér venv og kør scripts
   - Test TypeScript-eksempler: `npm install`, `npm run build`, `npm start`
   - Bekræft at miljøvariabler er korrekt konfigureret
   - Tjek at API nøgler fungerer med kodeeksempler

3. **Kodeeksempler**:
   - Sørg for at al kode kører uden fejl
   - Test med både Azure OpenAI og OpenAI API hvor relevant
   - Bekræft at eksempler fungerer med Microsoft Foundry Models hvor understøttet

### Ingen automatiserede tests

Dette er et undervisnings-repository fokuseret på tutorials og eksempler. Der findes ingen unit-tests eller integrationstests at køre. Validering foregår primært via:
- Manuel test af kodeeksempler
- GitHub Actions til Markdown validering
- Fællesskabsgennemgang af undervisningsindhold

## Retningslinjer for Pull Requests

### Før indsendelse

1. Test kodeændringer i både Python og TypeScript hvor relevant
2. Kør Markdown validering (udløses automatisk ved PR)
3. Sikr at tracking IDs er til stede på alle Microsoft URLs
4. Tjek at relative links er gyldige
5. Bekræft at billeder er korrekt refererede

### PR titelformat

- Brug beskrivende titler: `[Lesson 06] Fix Python example typo` eller `Update README for lesson 08`
- Referer til issues hvor relevant: `Fixes #123`

### PR beskrivelse

- Forklar hvad der er ændret og hvorfor
- Link til relaterede issues
- For kodeændringer, angiv hvilke eksempler der er testet
- For oversættelses PR'er, inkluder alle filer for en komplet oversættelse

### Bidragskrav

- Underskriv Microsoft CLA (automatisk ved første PR)
- Fork repository til din konto før ændringer foretages
- Én PR per logisk ændring (kombinér ikke upassende rettelser)
- Hold PR'er fokuserede og små når muligt

## Almindelige workflows

### Tilføjelse af nyt kodeeksempel

1. Naviger til den relevante lektionsmappe
2. Opret eksempel i `python/` eller `typescript/` undermappe
3. Følg navngivningskonvention: `{provider}-{example-name}.{py|ts|js}`
4. Test med faktiske API legitimationsoplysninger
5. Dokumenter nye miljøvariabler i lektions README

### Opdatering af dokumentation

1. Rediger README.md i lektionsmappen
2. Følg Markdown retningslinjer (tracking IDs, relative links)
3. Opdateringer til oversættelser håndteres af GitHub Actions (rediger ikke manuelt)
4. Test at alle links er gyldige

### Arbejde med Dev Containers

1. Repository inkluderer `.devcontainer/devcontainer.json`
2. Post-create script installerer Python-afhængigheder automatisk
3. Udvidelser til Python og Jupyter er forudkonfigurerede
4. Miljøet er baseret på `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Udrulning og publicering

Dette er et læringsrepository - der findes ingen udrulningsproces. Pensum forbruges via:

1. **GitHub Repository**: Direkte adgang til kode og dokumentation
2. **GitHub Codespaces**: Øjeblikkeligt dev-miljø med forudkonfigureret setup
3. **Microsoft Learn**: Indhold kan blive syndikeret til officiel læringsplatform
4. **docsify**: Dokumentationsside bygget fra Markdown (se `docsifytopdf.js` og `package.json`)

### Bygning af dokumentationsside

```bash
# Generer PDF fra dokumentation (hvis nødvendigt)
npm run convert
```

## Fejlfinding

### Almindelige problemer

**Python importfejl**:
- Sørg for at virtuelt miljø er aktiveret
- Kør `pip install -r requirements.txt`
- Tjek at Python version er 3.9+

**TypeScript byggefejl**:
- Kør `npm install` i den specifikke app-mappe
- Tjek at Node.js version er kompatibel
- Ryd `node_modules` og geninstaller om nødvendigt

**API autentificeringsfejl**:
- Bekræft `.env` fil findes og har korrekte værdier
- Tjek at API nøgler er gyldige og ikke udløbet
- Sørg for at endpoint URLs er korrekte for din region

**Manglende miljøvariabler**:
- Kopiér `.env.copy` til `.env`
- Udfyld alle nødvendige værdier for lektionen du arbejder på
- Genstart din applikation efter opdatering af `.env`

## Yderligere ressourcer

- [Kursusopsætningsguide](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Retningslinjer for bidrag](./CONTRIBUTING.md)
- [Adfærdskodeks](./CODE_OF_CONDUCT.md)
- [Sikkerhedspolitik](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Samling af avancerede kodeeksempler](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Projektspecifikke noter

- Dette er et **undervisningsrepository** fokuseret på læring, ikke produktionskode
- Eksempler er bevidst simple og fokuserer på at lære koncepter
- Kodekvaliteten balanceres med pædagogisk klarhed
- Hver lektion er selvstændig og kan gennemføres uafhængigt
- Repository understøtter flere API-udbydere: Azure OpenAI, OpenAI, Microsoft Foundry Models og offline-udbydere som Foundry Local og Ollama
- Indhold er flersproget med automatiserede oversættelses-workflows
- Aktivt fællesskab på Discord til spørgsmål og support

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->