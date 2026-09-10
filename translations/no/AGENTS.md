# AGENTS.md

## Prosjektoversikt

Dette depotet inneholder en omfattende læreplan med 21 leksjoner som lærer grunnleggende om Generativ AI og applikasjonsutvikling. Kurset er designet for nybegynnere og dekker alt fra grunnleggende konsepter til bygging av produksjonsklare applikasjoner.

**Nøkkelteknologier:**
- Python 3.9+ med biblioteker: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript med Node.js og biblioteker: `openai` (Azure OpenAI via v1-endepunktet + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry-modeller)
- Azure OpenAI Service, OpenAI API og Microsoft Foundry-modeller (GitHub Models trekkes tilbake i slutten av juli 2026)
- Jupyter Notebooks for interaktiv læring
- Dev Containers for konsistent utviklingsmiljø

**Depotstruktur:**
- 21 nummererte leksjonsmapper (00-21) som inneholder README-filer, kodeeksempler og oppgaver
- Flere implementasjoner: Python, TypeScript og av og til .NET-eksempler
- Oversettelsesmappe med 40+ språkoppsett
- Sentralisert konfigurasjon via `.env`-fil (bruk `.env.copy` som mal)

## Oppsettkommandoer

### Første oppsett av depot

```bash
# Klon depotet
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Kopier miljømal
cp .env.copy .env
# Rediger .env med dine API-nøkler og endepunkter
```

### Python-miljøoppsett

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

### Node.js/TypeScript-oppsett

```bash
# Installer avhengigheter på rot-nivå (for dokumentasjonsverktøy)
npm install

# For individuelle leksjonseksempler i TypeScript, naviger til den spesifikke leksjonen:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container-oppsett (anbefalt)

Depotet inkluderer en `.devcontainer`-konfigurasjon for GitHub Codespaces eller VS Code Dev Containers:

1. Åpne depotet i GitHub Codespaces eller VS Code med Dev Containers-utvidelsen
2. Dev Container vil automatisk:
   - Installere Python-avhengigheter fra `requirements.txt`
   - Kjøre post-create script (`.devcontainer/post-create.sh`)
   - Sette opp Jupyter-kjerne

## Utviklingsflyt

### Miljøvariabler

Alle leksjoner som krever API-tilgang bruker miljøvariabler definert i `.env`:

- `OPENAI_API_KEY` - For OpenAI API
- `AZURE_OPENAI_API_KEY` - For Azure OpenAI i Microsoft Foundry (Azure OpenAI Service er nå del av Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI-endepunkt-URL (Foundry-ressursendepunkt)
- `AZURE_OPENAI_DEPLOYMENT` - Navn på distribusjon av chat-kompletteringsmodell (kursstandard: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Navn på distribusjon av embeddings-modell (kursstandard: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - API-versjon (standard: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - For Hugging Face-modeller
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry Models-endepunkt (flere leverandører modellkatalog)
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry Models API-nøkkel (erstatter den nedtrukkede `GITHUB_TOKEN`)
- `AZURE_INFERENCE_CHAT_MODEL` - En modell uten resonnering (f.eks. `Llama-3.3-70B-Instruct`) brukt av `temperature`-eksemplene, siden resonneringsmodeller ikke støtter sampling-kontroller

### Modellkonvensjoner (viktig)

- **Standard chat-modell er `gpt-5-mini`** - en nåværende, ikke-utdatert **resonnerings**modell. Fra 2026 blir de eldre temperatur-aktiverte "mini"-modellene (`gpt-4o-mini`, `gpt-4.1-mini`) *utrangert*, så læreplanen standardiserer på GPT-5-familien.
- **Resonneringsmodeller avviser `temperature` og `top_p`**, og bruker `max_output_tokens` (Responses API) / `max_completion_tokens` (chat-kompletteringer) i stedet for `max_tokens`. Ikke legg til `temperature`/`top_p`/`max_tokens` i eksempler som kaller `gpt-5-mini`.
- **For å demonstrere `temperature`**, bruker eksemplene en **Llama**-modell (`Llama-3.3-70B-Instruct`) via Microsoft Foundry Models-endepunktet (`AZURE_INFERENCE_CHAT_MODEL`). Styr resonneringsmodeller med prompt-engineering + resonneringskontroller i stedet for utvalgsinnstillinger.
- **Finjustering (leksjon 18)** beholder `gpt-4.1-mini`: GPT-5 støtter kun forsterkningsbasert finjustering (RFT), ikke den overstyrte finjusteringen (SFT) vist der.
- Leksjon 20 (Mistral) og 21 (Meta) beholder `temperature`/`max_tokens` fordi de retter seg mot Mistral/Llama-modeller som støtter disse.

### Kjøre Python-eksempler

```bash
# Naviger til leksjonskatalogen
cd 06-text-generation-apps/python

# Kjør et Python-skript
python aoai-app.py
```

### Kjøre TypeScript-eksempler

```bash
# Naviger til TypeScript-appkatalogen
cd 06-text-generation-apps/typescript/recipe-app

# Bygg TypeScript-koden
npm run build

# Kjør applikasjonen
npm start
```

### Kjøre Jupyter Notebooks

```bash
# Start Jupyter i rotmappen til prosjektet
jupyter notebook

# Eller bruk VS Code med Jupyter-utvidelsen
```

### Arbeide med ulike leksjonstyper

- **"Lær" leksjoner**: Fokus på README.md dokumentasjon og konsepter
- **"Bygg" leksjoner**: Inkluderer fungerende kodeeksempler i Python og TypeScript
- Hver leksjon har en README.md med teori, kodegjennomganger og lenker til videoinnhold

## Retningslinjer for kodestil

### Python

- Bruk `python-dotenv` for håndtering av miljøvariabler
- Importer `openai`-biblioteket for API-interaksjoner
- Bruk `pylint` for linting (noen eksempler inneholder `# pylint: disable=all` for enkelhet)
- Følg PEP 8 navnekonvensjoner
- Lagre API-legitimasjon i `.env`-fil, aldri i koden

### TypeScript

- Bruk `dotenv`-pakken for miljøvariabler
- TypeScript-konfigurasjon i `tsconfig.json` for hver app
- Bruk `openai`-pakken for Azure OpenAI (pek klienten til `/openai/v1/` endepunkt og kall `client.responses.create`); bruk `@azure-rest/ai-inference` for Microsoft Foundry Models
- Bruk `nodemon` for utvikling med auto-reload
- Bygg før kjøring: `npm run build` deretter `npm start`

### Generelle konvensjoner

- Hold kodeeksempler enkle og pedagogiske
- Inkluder kommentarer som forklarer nøkkelkonsepter
- Koden til hver leksjon bør være selvstendig og kjøreklar
- Bruk konsekvente navnekonvensjoner: `aoai-` prefiks for Azure OpenAI, `oai-` for OpenAI API, `githubmodels-` for Microsoft Foundry Models (arvet prefiks fra GitHub Models-epoken)

## Dokumentasjonsretningslinjer

### Markdown-stil

- Alle URL-er må være omsluttet i `[tekst](../../url)` format uten ekstra mellomrom
- Relative lenker må starte med `./` eller `../`
- Alle lenker til Microsoft-domener må inkludere sporings-ID: `?WT.mc_id=academic-105485-koreyst`
- Ingen lands-spesifikke lokaliteter i URL-er (unngå `/en-us/`)
- Bilder lagres i `./images`-mappen med beskrivende navn
- Bruk engelske tegn, tall og bindestreker i filnavn

### Støtte for oversettelse

- Depotet støtter 40+ språk via automatiserte GitHub Actions
- Oversettelser lagres i `translations/`-katalogen
- Ikke send inn delvise oversettelser
- Maskinoversettelser aksepteres ikke
- Oversatte bilder lagres i `translated_images/`-katalogen

## Testing og validering

### Sjekker før innsending

Dette depotet bruker GitHub Actions for validering. Før innsending av PR-er:

1. **Sjekk markdown-lenker**:
   ```bash
   # validate-markdown.yml-arbeidsflyten sjekker:
   # - Ødelagte relative baner
   # - Manglende sporings-IDer på baner
   # - Manglende sporings-IDer på URL-er
   # - URL-er med landsspesifikk lokalisering
   # - Ødelagte eksterne URL-er
   ```

2. **Manuell testing**:
   - Test Python-eksempler: Aktiver venv og kjør skripter
   - Test TypeScript-eksempler: `npm install`, `npm run build`, `npm start`
   - Bekreft at miljøvariabler er korrekt konfigurert
   - Sjekk at API-nøkler fungerer med kodeeksemplene

3. **Kodeeksempler**:
   - Sørg for at all kode kjører uten feil
   - Test med både Azure OpenAI og OpenAI API når aktuelt
   - Bekreft at eksempler fungerer med Microsoft Foundry Models der det støttes

### Ingen automatiserte tester

Dette er et utdanningsdepot fokusert på opplæring og eksempler. Det finnes ingen enhetstester eller integrasjonstester. Validering er primært:
- Manuell testing av kodeeksempler
- GitHub Actions for Markdown-validering
- Fellesskapsgjennomgang av pedagogisk innhold

## Retningslinjer for pull requests

### Før innsending

1. Test kodeendringer i både Python og TypeScript der aktuelt
2. Kjør Markdown-validering (utløst automatisk på PR)
3. Sørg for at sporings-ID-er er tilstede på alle Microsoft-URL-er
4. Sjekk at relative lenker er gyldige
5. Bekreft at bilder er riktig referert

### PR-tittelformat

- Bruk beskrivende titler: `[Lesson 06] Fix Python example typo` eller `Update README for lesson 08`
- Referer til issues når aktuelt: `Fixes #123`

### PR-beskrivelse

- Forklar hva som ble endret og hvorfor
- Lenke til relaterte issues
- For kodeendringer, spesifiser hvilke eksempler som ble testet
- For oversettelses-PR-er, inkluder alle filer for fullstendig oversettelse

### Krav til bidrag

- Signer Microsoft CLA (automatisk ved første PR)
- Fork depotet til din konto før du gjør endringer
- Én PR per logisk endring (ikke kombiner urelaterte fikser)
- Hold PR-er fokuserte og små når mulig

## Vanlige arbeidsflyter

### Legge til et nytt kodeeksempel

1. Gå til riktig leksjonskatalog
2. Opprett eksempel i `python/` eller `typescript/` undermappe
3. Følg navnekonvensjon: `{provider}-{example-name}.{py|ts|js}`
4. Test med faktiske API-legitimasjoner
5. Dokumenter eventuelle nye miljøvariabler i leksjonens README

### Oppdatere dokumentasjon

1. Rediger README.md i leksjonskatalogen
2. Følg Markdown-retningslinjer (sporings-ID-er, relative lenker)
3. Oppdateringer til oversettelser håndteres av GitHub Actions (ikke rediger manuelt)
4. Test at alle lenker er gyldige

### Arbeide med Dev Containers

1. Depotet inkluderer `.devcontainer/devcontainer.json`
2. Post-create script installerer Python-avhengigheter automatisk
3. Utvidelser for Python og Jupyter er forhåndskonfigurert
4. Miljøet er basert på `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Distribusjon og publisering

Dette er et læringsdepot - det finnes ingen distribusjonsprosess. Læreplanen konsumeres gjennom:

1. **GitHub Repository**: Direkte tilgang til kode og dokumentasjon
2. **GitHub Codespaces**: Øyeblikkelig utviklingsmiljø med ferdigoppsett
3. **Microsoft Learn**: Innhold kan distribueres til den offisielle læringsplattformen
4. **docsify**: Dokumentasjonsnettsted bygget fra Markdown (se `docsifytopdf.js` og `package.json`)

### Bygge dokumentasjonsnettsted

```bash
# Generer PDF fra dokumentasjon (hvis nødvendig)
npm run convert
```

## Feilsøking

### Vanlige problemer

**Python Import-feil**:
- Sørg for at virtuelt miljø er aktivert
- Kjør `pip install -r requirements.txt`
- Sjekk at Python-versjonen er 3.9+

**TypeScript-buildfeil**:
- Kjør `npm install` i den spesifikke app-katalogen
- Sjekk at Node.js-versjonen er kompatibel
- Rydd `node_modules` og installer på nytt om nødvendig

**API-autentiseringsfeil**:
- Verifiser at `.env`-filen eksisterer og har riktige verdier
- Sjekk at API-nøkler er gyldige og ikke utløpt
- Sørg for at endepunkt-URL-er er riktige for din region

**Manglende miljøvariabler**:
- Kopier `.env.copy` til `.env`
- Fyll inn alle nødvendige verdier for leksjonen du jobber med
- Start applikasjonen på nytt etter oppdatering av `.env`

## Tilleggsressurser

- [Kursoppsettveiledning](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Retningslinjer for bidrag](./CONTRIBUTING.md)
- [Adferdskodeks](./CODE_OF_CONDUCT.md)
- [Sikkerhetspolicy](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Samling av avanserte kodeeksempler](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Prosjektspesifikke merknader

- Dette er et **utdanningsdepot** fokusert på læring, ikke produksjonskode
- Eksemplene er med vilje enkle og fokusert på å lære konsepter
- Kvaliteten på koden balanseres med pedagogisk klarhet
- Hver leksjon er selvstendig og kan fullføres uavhengig
- Depotet støtter flere API-leverandører: Azure OpenAI, OpenAI, Microsoft Foundry Models, og offline-leverandører som Foundry Local og Ollama
- Innholdet er flerspråklig med automatiserte oversettelsesarbeidsflyter
- Aktivt fellesskap på Discord for spørsmål og støtte

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->