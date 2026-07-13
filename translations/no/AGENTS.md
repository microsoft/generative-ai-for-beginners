# AGENTS.md

## Prosjektoversikt

Dette depotet inneholder en omfattende pensum med 21 leksjoner som lærer grunnleggende Generativ AI og applikasjonsutvikling. Kurset er designet for nybegynnere og dekker alt fra grunnleggende konsepter til bygging av produksjonsklare applikasjoner.

**Nøkkel Teknologier:**
- Python 3.9+ med biblioteker: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript med Node.js og biblioteker: `openai` (Azure OpenAI via v1-endepunkt + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI Service, OpenAI API og Microsoft Foundry Models (GitHub Models faset ut slutten av juli 2026)
- Jupyter Notebooks for interaktiv læring
- Dev Containers for konsistent utviklingsmiljø

**Depotstruktur:**
- 21 nummererte leksjonsmapper (00-21) som inneholder README-filer, kodeeksempler og oppgaver
- Flere implementasjoner: Python, TypeScript, og noen ganger .NET eksempler
- Oversettelsesmappen med 40+ språkversjoner
- Sentralisert konfigurasjon via `.env` fil (bruk `.env.copy` som mal)

## Oppsettskommandoer

### Første Oppsett av Depot

```bash
# Klon depotet
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Kopier miljømalen
cp .env.copy .env
# Rediger .env med dine API-nøkler og endepunkter
```

### Python Miljøoppsett

```bash
# Opprett virtuelt miljø
python3 -m venv venv

# Aktiver virtuelt miljø
# På macOS/Linux:
source venv/bin/activate
# På Windows:
venv\Scripts\activate

# Installer avhengigheter
pip install -r requirements.txt
```

### Node.js/TypeScript Oppsett

```bash
# Installer avhengigheter på rot-nivå (for dokumentasjonsverktøy)
npm install

# For individuelle leksjons-Typescript-eksempler, naviger til den spesifikke leksjonen:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container Oppsett (Anbefalt)

Depotet inkluderer en `.devcontainer` konfigurasjon for GitHub Codespaces eller VS Code Dev Containers:

1. Åpne depotet i GitHub Codespaces eller VS Code med Dev Containers-utvidelsen
2. Dev Container vil automatisk:
   - Installere Python-avhengigheter fra `requirements.txt`
   - Kjøre post-create skript (`.devcontainer/post-create.sh`)
   - Sette opp Jupyter-kjernen

## Utviklingsarbeidsflyt

### Miljøvariabler

Alle leksjoner som krever API-tilgang bruker miljøvariabler definert i `.env`:

- `OPENAI_API_KEY` - For OpenAI API
- `AZURE_OPENAI_API_KEY` - For Azure OpenAI i Microsoft Foundry (Azure OpenAI Service er nå en del av Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI endepunkt-URL (Foundry ressursendepunkt)
- `AZURE_OPENAI_DEPLOYMENT` - Chat completion modellutplassering navn
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Embeddings modellutplassering navn
- `AZURE_OPENAI_API_VERSION` - API-versjon (standard: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - For Hugging Face modeller
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry Models endepunkt (flere leverandører modellkatalog)
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry Models API-nøkkel (erstatter den nedtrappede `GITHUB_TOKEN`)

### Kjøre Python Eksempler

```bash
# Naviger til leksjonskatalogen
cd 06-text-generation-apps/python

# Kjør et Python-skript
python aoai-app.py
```

### Kjøre TypeScript Eksempler

```bash
# Naviger til TypeScript app-katalogen
cd 06-text-generation-apps/typescript/recipe-app

# Bygg TypeScript-koden
npm run build

# Kjør applikasjonen
npm start
```

### Kjøre Jupyter Notebooks

```bash
# Start Jupyter i rotmappen til repositoriet
jupyter notebook

# Eller bruk VS Code med Jupyter-utvidelsen
```

### Arbeide med Ulike Leksjonstyper

- **"Lær" leksjoner**: Fokuser på README.md dokumentasjon og konsepter
- **"Bygg" leksjoner**: Inkluderer fungerende kodeeksempler i Python og TypeScript
- Hver leksjon har en README.md med teori, kodegjennomganger, og lenker til videoinnhold

## Kode stilig retningslinjer

### Python

- Bruk `python-dotenv` for håndtering av miljøvariabler
- Importer `openai` biblioteket for API-interaksjoner
- Bruk `pylint` for linting (noen eksempler inkluderer `# pylint: disable=all` for enkelhet)
- Følg PEP 8 navnekonvensjoner
- Lagre API-legitimasjon i `.env` fil, aldri i kode

### TypeScript

- Bruk `dotenv` pakken for miljøvariabler
- TypeScript-konfigurasjon i `tsconfig.json` for hver app
- Bruk `openai` pakken for Azure OpenAI (pek klienten til `/openai/v1/` endepunkt og kall `client.responses.create`); bruk `@azure-rest/ai-inference` for Microsoft Foundry Models
- Bruk `nodemon` for utvikling med auto-reload
- Bygg før kjøring: `npm run build` deretter `npm start`

### Generelle Konvensjoner

- Hold kodeeksempler enkle og pedagogiske
- Inkluder kommentarer som forklarer nøkkelkonsepter
- Hver leksjons kode skal være selvstendig og kjørbar
- Bruk konsistent navngivning: `aoai-` prefiks for Azure OpenAI, `oai-` for OpenAI API, `githubmodels-` for Microsoft Foundry Models (arvet prefiks fra GitHub Models epoken)

## Dokumentasjonsretningslinjer

### Markdown Stil

- Alle URLer må være pakket inn i `[text](../../url)` format uten ekstra mellomrom
- Relative lenker må starte med `./` eller `../`
- Alle lenker til Microsoft-domener må inkludere sporings-ID: `?WT.mc_id=academic-105485-koreyst`
- Ingen lands-spesifikke lokaliteter i URLer (unngå `/en-us/`)
- Bilder lagres i `./images` mappe med beskrivende navn
- Bruk engelske bokstaver, tall og bindestreker i filnavn

### Støtte for Oversettelse

- Depotet støtter 40+ språk via automatiserte GitHub Actions
- Oversettelser lagres i `translations/` mappen
- Ikke send inn delvise oversettelser
- Maskinoversettelser godtas ikke
- Oversatte bilder lagres i `translated_images/` mappen

## Testing og Validering

### Sjekker før innsending

Dette depotet bruker GitHub Actions for validering. Før innsending av PRs:

1. **Sjekk Markdown-lenker**:
   ```bash
   # validate-markdown.yml-arbeidsflyten sjekker:
   # - Ødelagte relative stier
   # - Manglende sporings-IDer på stier
   # - Manglende sporings-IDer på URL-er
   # - URL-er med landslocale
   # - Ødelagte eksterne URL-er
   ```

2. **Manuell Testing**:
   - Test Python-eksempler: Aktiver venv og kjør skriptene
   - Test TypeScript-eksempler: `npm install`, `npm run build`, `npm start`
   - Verifiser miljøvariabler er riktig konfigurert
   - Kontroller at API-nøkler fungerer med kodeeksemplene

3. **Kodeeksempler**:
   - Sikre at all kode kjører uten feil
   - Test med både Azure OpenAI og OpenAI API når det er relevant
   - Verifiser at eksempler fungerer med Microsoft Foundry Models der støttet

### Ingen Automatiserte Tester

Dette er et pedagogisk depot fokusert på opplæring og eksempler. Det finnes ingen enhetstester eller integrasjonstester å kjøre. Validering er hovedsakelig:
- Manuell testing av kodeeksempler
- GitHub Actions for Markdown-validering
- Fellesskapsgjennomgang av opplæringsinnhold

## Retningslinjer for Pull Requests

### Før innsending

1. Test kodeendringer i både Python og TypeScript når relevant
2. Kjør Markdown-validering (utløses automatisk på PR)
3. Sørg for at sporings-IDer er til stede på alle Microsoft-URLer
4. Sjekk at relative lenker er gyldige
5. Verifiser at bilder er riktig referert

### PR Tittel Format

- Bruk beskrivende titler: `[Lesson 06] Fix Python example typo` eller `Oppdater README for leksjon 08`
- Referer til saknummer når mulig: `Fixes #123`

### PR Beskrivelse

- Forklar hva som ble endret og hvorfor
- Lenke til relaterte saker
- For kodeendringer, spesifiser hvilke eksempler som ble testet
- For oversettelses-PRer, inkluder alle filer for en fullstendig oversettelse

### Bidragskrav

- Signer Microsoft CLA (automatisk ved første PR)
- Fork depotet til din konto før du gjør endringer
- En PR per logisk endring (ikke kombiner urelaterte fikser)
- Hold PRer fokuserte og små når mulig

## Vanlige Arbeidsflyter

### Legge til et Nytt Kodeeksempel

1. Naviger til riktig leksjonsmappe
2. Opprett eksempel i `python/` eller `typescript/` undermappe
3. Følg navngivningskonvensjon: `{provider}-{example-name}.{py|ts|js}`
4. Test med faktiske API-legitimasjoner
5. Dokumenter eventuelle nye miljøvariabler i leksjonens README

### Oppdatere Dokumentasjon

1. Rediger README.md i leksjonsmappen
2. Følg Markdown-retningslinjer (sporings-IDer, relative lenker)
3. Oppdateringer av oversettelser håndteres av GitHub Actions (ikke rediger manuelt)
4. Test at alle lenker er gyldige

### Arbeide med Dev Containers

1. Depotet inkluderer `.devcontainer/devcontainer.json`
2. Post-create skript installerer Python-avhengigheter automatisk
3. Utvidelser for Python og Jupyter er forhåndskonfigurert
4. Miljøet baseres på `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Distribusjon og Publisering

Dette er et læringsdepot – det finnes ingen distribusjonsprosess. Pensumet konsumeres gjennom:

1. **GitHub Repository**: Direkte tilgang til kode og dokumentasjon
2. **GitHub Codespaces**: Umiddelbart utviklingsmiljø med forhåndskonfigurert oppsett
3. **Microsoft Learn**: Innhold kan distribueres til offisiell læringsplattform
4. **docsify**: Dokumentasjonsnettsted bygget fra Markdown (se `docsifytopdf.js` og `package.json`)

### Bygge Dokumentasjonsnettsted

```bash
# Generer PDF fra dokumentasjon (om nødvendig)
npm run convert
```

## Feilsøking

### Vanlige Problemer

**Python Import Feil**:
- Sørg for at virtuell miljø er aktivert
- Kjør `pip install -r requirements.txt`
- Sjekk at Python-versjonen er 3.9+

**TypeScript Byggefeil**:
- Kjør `npm install` i den spesifikke app-mappen
- Sjekk at Node.js-versjonen er kompatibel
- Rydd `node_modules` og installer på nytt hvis nødvendig

**API Autentiseringsfeil**:
- Verifiser at `.env`-filen finnes og har riktige verdier
- Sjekk at API-nøkler er gyldige og ikke utløpt
- Sørg for at endepunkts-URLer er riktige for din region

**Manglende Miljøvariabler**:
- Kopier `.env.copy` til `.env`
- Fyll inn alle nødvendige verdier for leksjonen du jobber med
- Start applikasjonen på nytt etter oppdatering av `.env`

## Ekstra Ressurser

- [Kursoppsett Veiledning](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Retningslinjer for Bidrag](./CONTRIBUTING.md)
- [Adferdskodeks](./CODE_OF_CONDUCT.md)
- [Sikkerhetspolicy](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Samling av Avanserte Kodeeksempler](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Prosjektspesifikke Notater

- Dette er et **pedagogisk depot** fokusert på læring, ikke produksjonskode
- Eksemplene er bevisst enkle og fokuserte på å lære konsepter
- Kodekvalitet balanseres med pedagogisk klarhet
- Hver leksjon er selvstendig og kan fullføres uavhengig
- Depotet støtter flere API-leverandører: Azure OpenAI, OpenAI, Microsoft Foundry Models, og offline leverandører som Foundry Local og Ollama
- Innhold er flerspråklig med automatiserte oversettelsesarbeidsflyter
- Aktivt fellesskap på Discord for spørsmål og støtte

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->