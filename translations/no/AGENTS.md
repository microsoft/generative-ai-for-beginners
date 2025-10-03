<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T11:04:49+00:00",
  "source_file": "AGENTS.md",
  "language_code": "no"
}
-->
# AGENTS.md

## Prosjektoversikt

Dette repositoriet inneholder et omfattende 21-leksjons pensum som lærer grunnleggende om Generativ AI og applikasjonsutvikling. Kurset er designet for nybegynnere og dekker alt fra grunnleggende konsepter til å bygge produksjonsklare applikasjoner.

**Nøkkelteknologier:**
- Python 3.9+ med biblioteker: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript med Node.js og biblioteker: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API og GitHub Models
- Jupyter Notebooks for interaktiv læring
- Dev Containers for konsistent utviklingsmiljø

**Struktur for repositoriet:**
- 21 nummererte leksjonsmapper (00-21) som inneholder README-filer, kodeeksempler og oppgaver
- Flere implementasjoner: Python, TypeScript og noen ganger .NET-eksempler
- Oversettelseskatalog med versjoner på 40+ språk
- Sentralisert konfigurasjon via `.env`-fil (bruk `.env.copy` som mal)

## Oppsettskommandoer

### Initialt oppsett av repositoriet

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Oppsett av Python-miljø

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

### Oppsett av Node.js/TypeScript

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Oppsett av Dev Container (anbefalt)

Repositoriet inkluderer en `.devcontainer`-konfigurasjon for GitHub Codespaces eller VS Code Dev Containers:

1. Åpne repositoriet i GitHub Codespaces eller VS Code med Dev Containers-utvidelsen
2. Dev Container vil automatisk:
   - Installere Python-avhengigheter fra `requirements.txt`
   - Kjøre post-create script (`.devcontainer/post-create.sh`)
   - Sette opp Jupyter-kjerne

## Utviklingsarbeidsflyt

### Miljøvariabler

Alle leksjoner som krever API-tilgang bruker miljøvariabler definert i `.env`:

- `OPENAI_API_KEY` - For OpenAI API
- `AZURE_OPENAI_API_KEY` - For Azure OpenAI Service
- `AZURE_OPENAI_ENDPOINT` - URL for Azure OpenAI-endepunkt
- `AZURE_OPENAI_DEPLOYMENT` - Navn på chat completion-modellens distribusjon
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Navn på embeddings-modellens distribusjon
- `AZURE_OPENAI_API_VERSION` - API-versjon (standard: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - For Hugging Face-modeller
- `GITHUB_TOKEN` - For GitHub Models

### Kjøre Python-eksempler

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### Kjøre TypeScript-eksempler

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Kjøre Jupyter Notebooks

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### Arbeide med ulike leksjonstyper

- **"Learn"-leksjoner**: Fokus på README.md-dokumentasjon og konsepter
- **"Build"-leksjoner**: Inkluderer fungerende kodeeksempler i Python og TypeScript
- Hver leksjon har en README.md med teori, gjennomgang av kode og lenker til videoinnhold

## Retningslinjer for kodestil

### Python

- Bruk `python-dotenv` for håndtering av miljøvariabler
- Importer `openai`-biblioteket for API-interaksjoner
- Bruk `pylint` for linting (noen eksempler inkluderer `# pylint: disable=all` for enkelhet)
- Følg PEP 8-navnekonvensjoner
- Lagre API-legitimasjon i `.env`-filen, aldri i kode

### TypeScript

- Bruk `dotenv`-pakken for miljøvariabler
- TypeScript-konfigurasjon i `tsconfig.json` for hver app
- Bruk `@azure/openai` eller `@azure-rest/ai-inference` for Azure-tjenester
- Bruk `nodemon` for utvikling med automatisk oppdatering
- Bygg før kjøring: `npm run build` deretter `npm start`

### Generelle konvensjoner

- Hold kodeeksempler enkle og pedagogiske
- Inkluder kommentarer som forklarer nøkkelkonsepter
- Hver leksjonskode skal være selvstendig og kjørbar
- Bruk konsistent navngivning: `aoai-`-prefiks for Azure OpenAI, `oai-` for OpenAI API, `githubmodels-` for GitHub Models

## Retningslinjer for dokumentasjon

### Markdown-stil

- Alle URL-er må være pakket inn i `[tekst](../../url)`-format uten ekstra mellomrom
- Relative lenker må starte med `./` eller `../`
- Alle lenker til Microsoft-domener må inkludere sporings-ID: `?WT.mc_id=academic-105485-koreyst`
- Ingen landspesifikke lokaliteter i URL-er (unngå `/en-us/`)
- Bilder lagres i `./images`-mappen med beskrivende navn
- Bruk engelske tegn, tall og bindestreker i filnavn

### Støtte for oversettelse

- Repositoriet støtter 40+ språk via automatiserte GitHub Actions
- Oversettelser lagres i `translations/`-katalogen
- Ikke send inn delvise oversettelser
- Maskinoversettelser aksepteres ikke
- Oversatte bilder lagres i `translated_images/`-katalogen

## Testing og validering

### Sjekker før innsending

Dette repositoriet bruker GitHub Actions for validering. Før innsending av PR-er:

1. **Sjekk Markdown-lenker**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Manuell testing**:
   - Test Python-eksempler: Aktiver venv og kjør skriptene
   - Test TypeScript-eksempler: `npm install`, `npm run build`, `npm start`
   - Verifiser at miljøvariabler er riktig konfigurert
   - Sjekk at API-nøkler fungerer med kodeeksemplene

3. **Kodeeksempler**:
   - Sørg for at all kode kjører uten feil
   - Test med både Azure OpenAI og OpenAI API der det er aktuelt
   - Verifiser at eksempler fungerer med GitHub Models der det er støttet

### Ingen automatiserte tester

Dette er et pedagogisk repositorium fokusert på opplæring og eksempler. Det finnes ingen enhetstester eller integrasjonstester å kjøre. Validering er primært:
- Manuell testing av kodeeksempler
- GitHub Actions for Markdown-validering
- Fellesskapsgjennomgang av pedagogisk innhold

## Retningslinjer for pull requests

### Før innsending

1. Test kodeendringer i både Python og TypeScript der det er aktuelt
2. Kjør Markdown-validering (utløses automatisk ved PR)
3. Sørg for at sporings-ID-er er til stede på alle Microsoft-URL-er
4. Sjekk at relative lenker er gyldige
5. Verifiser at bilder er riktig referert

### Format for PR-titler

- Bruk beskrivende titler: `[Leksjon 06] Fiks skrivefeil i Python-eksempel` eller `Oppdater README for leksjon 08`
- Referer til issuenummer der det er aktuelt: `Fixes #123`

### PR-beskrivelse

- Forklar hva som ble endret og hvorfor
- Lenke til relaterte issues
- For kodeendringer, spesifiser hvilke eksempler som ble testet
- For oversettelses-PR-er, inkluder alle filer for en komplett oversettelse

### Krav til bidrag

- Signer Microsoft CLA (automatisk ved første PR)
- Fork repositoriet til din konto før du gjør endringer
- Én PR per logisk endring (ikke kombiner urelaterte fikser)
- Hold PR-er fokuserte og små der det er mulig

## Vanlige arbeidsflyter

### Legge til et nytt kodeeksempel

1. Naviger til riktig leksjonsmappe
2. Opprett eksempel i `python/` eller `typescript/`-undermappe
3. Følg navnekonvensjon: `{provider}-{example-name}.{py|ts|js}`
4. Test med faktiske API-legitimasjoner
5. Dokumenter eventuelle nye miljøvariabler i leksjonens README

### Oppdatere dokumentasjon

1. Rediger README.md i leksjonsmappen
2. Følg Markdown-retningslinjer (sporings-ID-er, relative lenker)
3. Oppdater oversettelser håndteres av GitHub Actions (ikke rediger manuelt)
4. Test at alle lenker er gyldige

### Arbeide med Dev Containers

1. Repositoriet inkluderer `.devcontainer/devcontainer.json`
2. Post-create script installerer Python-avhengigheter automatisk
3. Utvidelser for Python og Jupyter er forhåndskonfigurert
4. Miljøet er basert på `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Distribusjon og publisering

Dette er et læringsrepositorium - det finnes ingen distribusjonsprosess. Pensumet konsumeres av:

1. **GitHub-repositorium**: Direkte tilgang til kode og dokumentasjon
2. **GitHub Codespaces**: Umiddelbart utviklingsmiljø med forhåndskonfigurert oppsett
3. **Microsoft Learn**: Innhold kan bli syndikert til den offisielle læringsplattformen
4. **docsify**: Dokumentasjonsnettsted bygget fra Markdown (se `docsifytopdf.js` og `package.json`)

### Bygge dokumentasjonsnettsted

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Feilsøking

### Vanlige problemer

**Python-importfeil**:
- Sørg for at virtuelt miljø er aktivert
- Kjør `pip install -r requirements.txt`
- Sjekk at Python-versjonen er 3.9+

**TypeScript-byggefeil**:
- Kjør `npm install` i den spesifikke app-mappen
- Sjekk at Node.js-versjonen er kompatibel
- Tøm `node_modules` og installer på nytt hvis nødvendig

**API-autentiseringsfeil**:
- Verifiser at `.env`-filen eksisterer og har riktige verdier
- Sjekk at API-nøkler er gyldige og ikke utløpt
- Sørg for at endepunkt-URL-er er riktige for din region

**Manglende miljøvariabler**:
- Kopier `.env.copy` til `.env`
- Fyll inn alle nødvendige verdier for leksjonen du jobber med
- Start applikasjonen på nytt etter oppdatering av `.env`

## Tilleggsressurser

- [Veiledning for kursoppsett](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Retningslinjer for bidrag](./CONTRIBUTING.md)
- [Regler for oppførsel](./CODE_OF_CONDUCT.md)
- [Sikkerhetspolicy](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Samling av avanserte kodeeksempler](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Prosjektspesifikke notater

- Dette er et **pedagogisk repositorium** fokusert på læring, ikke produksjonskode
- Eksempler er med vilje enkle og fokusert på å lære konsepter
- Kvaliteten på koden balanseres med pedagogisk klarhet
- Hver leksjon er selvstendig og kan fullføres uavhengig
- Repositoriet støtter flere API-leverandører: Azure OpenAI, OpenAI og GitHub Models
- Innholdet er flerspråklig med automatiserte oversettelsesarbeidsflyter
- Aktivt fellesskap på Discord for spørsmål og støtte

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.