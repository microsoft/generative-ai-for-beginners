# AGENTER.md

## Projektöversikt

Denna repo innehåller en omfattande kursplan med 21 lektioner som lär ut grunderna i Generativ AI och applikationsutveckling. Kursen är utformad för nybörjare och täcker allt från grundläggande koncept till att bygga produktionsklara applikationer.

**Nyckelteknologier:**
- Python 3.9+ med bibliotek: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript med Node.js och bibliotek: `openai` (Azure OpenAI via v1-endpoint + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI Service, OpenAI API och Microsoft Foundry Models (GitHub Models upphör i slutet av juli 2026)
- Jupyter Notebooks för interaktivt lärande
- Dev Containers för konsekvent utvecklingsmiljö

**Reposstruktur:**
- 21 numrerade lektionskataloger (00-21) med README-filer, kodexempel och uppgifter
- Flera implementationer: Python, TypeScript, och ibland .NET-exempel
- Översättningskatalog med 40+ språkversioner
- Centraliserad konfiguration via `.env`-fil (använd `.env.copy` som mall)

## Setup-kommandon

### Initial reposetup

```bash
# Klona förvaret
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Kopiera miljömall
cp .env.copy .env
# Redigera .env med dina API-nycklar och slutpunkter
```

### Python miljösetup

```bash
# Skapa virtuellt miljö
python3 -m venv venv

# Aktivera virtuellt miljö
# På macOS/Linux:
source venv/bin/activate
# På Windows:
venv\Scripts\activate

# Installera beroenden
pip install -r requirements.txt
```

### Node.js/TypeScript setup

```bash
# Installera beroenden på root-nivå (för dokumentationsverktyg)
npm install

# För individuella TypeScript-exempel för lektioner, navigera till den specifika lektionen:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container setup (Rekommenderat)

Repositoriet innehåller en `.devcontainer`-konfiguration för GitHub Codespaces eller VS Code Dev Containers:

1. Öppna repot i GitHub Codespaces eller VS Code med Dev Containers extension
2. Dev Container gör automatiskt:
   - Installerar Python beroenden från `requirements.txt`
   - Kör post-create script (`.devcontainer/post-create.sh`)
   - Sätter upp Jupyter-kärnan

## Utvecklingsarbetsflöde

### Miljövariabler

Alla lektioner som kräver API-åtkomst använder miljövariabler definierade i `.env`:

- `OPENAI_API_KEY` - För OpenAI API
- `AZURE_OPENAI_API_KEY` - För Azure OpenAI i Microsoft Foundry (Azure OpenAI Service är nu del av Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI endpoint URL (Foundry-resursens endpoint)
- `AZURE_OPENAI_DEPLOYMENT` - Namn på chat completion-modellutplacering (kursens standard: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Namn på embeddings-modellutplacering (kursens standard: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - API-version (standard: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - För Hugging Face-modeller
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry Models endpoint (multi-provider modellkatalog)
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry Models API-nyckel (ersätter den utgående `GITHUB_TOKEN`)
- `AZURE_INFERENCE_CHAT_MODEL` - En icke-resonerande modell (t.ex. `Llama-3.3-70B-Instruct`) som används av `temperature`-exempel, eftersom resonerande modeller inte stöder sampling-kontroller

### Modellkonventioner (viktigt)

- **Standard chatmodell är `gpt-5-mini`** - en aktuell, icke-deprekerad **resonerande** modell. Från och med 2026 är de äldre temperaturkapabla "mini"-modellerna (`gpt-4o-mini`, `gpt-4.1-mini`) *på väg att fasas ut*, så kursplanen standardiserar på GPT-5-familjen.
- **Resonerande modeller avvisar `temperature` och `top_p`**, och använder istället `max_output_tokens` (Responses API) / `max_completion_tokens` (chat completion) istället för `max_tokens`. Lägg **inte** till `temperature`/`top_p`/`max_tokens` till exempel som anropar `gpt-5-mini`.
- **För att demonstrera `temperature`**, använder exempel en **Llama**-modell (`Llama-3.3-70B-Instruct`) via Microsoft Foundry Models endpoint (`AZURE_INFERENCE_CHAT_MODEL`). Styr resonerande modeller med prompt-engineering + resonerkontroller istället för sampling-reglage.
- **Fine-tuning (lektion 18)** behåller `gpt-4.1-mini`: GPT-5 stödjer bara förstärkningsfinjustering (RFT), inte övervakad finjustering (SFT) som visas där.
- Lektionerna 20 (Mistral) och 21 (Meta) behåller `temperature`/`max_tokens` eftersom de riktar sig mot Mistral/Llama-modeller som stöder detta.

### Köra Python-exempel

```bash
# Navigera till lektionsmappen
cd 06-text-generation-apps/python

# Kör ett Python-skript
python aoai-app.py
```

### Köra TypeScript-exempel

```bash
# Navigera till TypeScript-appkatalogen
cd 06-text-generation-apps/typescript/recipe-app

# Bygg TypeScript-koden
npm run build

# Kör applikationen
npm start
```

### Köra Jupyter Notebooks

```bash
# Starta Jupyter i repository-roten
jupyter notebook

# Eller använd VS Code med Jupyter-tillägget
```

### Arbeta med olika lektionstyper

- **"Learn"-lektioner**: Fokus på README.md dokumentation och koncept
- **"Build"-lektioner**: Innehåller fungerande kodexempel i Python och TypeScript
- Varje lektion har en README.md med teori, kodgenomgångar och länkar till videoinnehåll

## Kodstilriktlinjer

### Python

- Använd `python-dotenv` för hantering av miljövariabler
- Importera `openai`-biblioteket för API-interaktioner
- Använd `pylint` för linting (vissa exempel inkluderar `# pylint: disable=all` för enkelhetens skull)
- Följ PEP 8:s namngivningskonventioner
- Spara API-referenser i `.env`-fil, aldrig i koden

### TypeScript

- Använd `dotenv`-paketet för miljövariabler
- TypeScript-konfiguration i `tsconfig.json` för varje app
- Använd `openai`-paketet för Azure OpenAI (peka klienten på `/openai/v1/` endpoint och anropa `client.responses.create`); använd `@azure-rest/ai-inference` för Microsoft Foundry Models
- Använd `nodemon` för utveckling med automatisk omladdning
- Bygg innan körning: `npm run build` sedan `npm start`

### Generella konventioner

- Håll kodexemplen enkla och pedagogiska
- Inkludera kommentarer som förklarar nyckelkoncept
- Varje lektions kod ska vara självständig och körbar
- Använd konsekvent namngivning: `aoai-` prefix för Azure OpenAI, `oai-` för OpenAI API, `githubmodels-` för Microsoft Foundry Models (före detta prefix från GitHub Models-epoken behålls)

## Dokumentationsriktlinjer

### Markdownstil

- Alla URL:er måste omslutas i `[text](../../url)` format utan extra mellanslag
- Relativa länkar måste börja med `./` eller `../`
- Alla länkar till Microsoft-domäner måste innehålla spårnings-ID: `?WT.mc_id=academic-105485-koreyst`
- Inga landspecifika lokaliseringsdelar i URL:er (undvik `/en-us/`)
- Bilder lagras i `./images`-mappen med beskrivande namn
- Använd engelska tecken, siffror och bindestreck i filnamn

### Översättningsstöd

- Repositoriet stödjer 40+ språk via automatiserade GitHub Actions
- Översättningar lagras i `translations/`-katalogen
- Skicka inte in partiella översättningar
- Maskinöversättningar accepteras inte
- Översatta bilder lagras i `translated_images/`-katalogen

## Testning och validering

### Kontroll före inskickning

Detta repo använder GitHub Actions för validering. Innan PR skickas in:

1. **Kontrollera Markdown-länkar**:
   ```bash
   # Arbetsflödet validate-markdown.yml kontrollerar:
   # - Trasiga relativa sökvägar
   # - Saknade spårnings-ID:n på sökvägar
   # - Saknade spårnings-ID:n på URL:er
   # - URL:er med landslokal
   # - Trasiga externa URL:er
   ```

2. **Manuell testning**:
   - Testa Python-exempel: Aktivera venv och kör skript
   - Testa TypeScript-exempel: `npm install`, `npm run build`, `npm start`
   - Kontrollera att miljövariabler är korrekt konfigurerade
   - Kontrollera att API-nycklar fungerar med kodexemplen

3. **Kodexempel**:
   - Säkerställ att all kod körs utan fel
   - Testa med både Azure OpenAI och OpenAI API när det är tillämpligt
   - Verifiera att exempel fungerar med Microsoft Foundry Models där det stöds

### Inga automatiska tester

Detta är ett utbildningsrepo fokuserat på handledningar och exempel. Det finns inga enhetstester eller integrationstester att köra. Validering sker främst genom:
- Manuell testning av kodexempel
- GitHub Actions för Markdown-validering
- Gemenskapsgranskning av utbildningsinnehåll

## Riktlinjer för Pull Requests

### Före inskickning

1. Testa kodändringar i både Python och TypeScript när det är tillämpligt
2. Kör Markdown-validering (triggas automatiskt på PR)
3. Säkerställ att spårnings-ID finns på alla Microsoft-URL:er
4. Kontrollera att relativa länkar är giltiga
5. Verifiera att bilder refereras korrekt

### Format på PR-titel

- Använd beskrivande titlar: `[Lesson 06] Fix Python example typo` eller `Update README for lesson 08`
- Referera till ärendenummer när det är relevant: `Fixes #123`

### PR-beskrivning

- Förklara vad som ändrats och varför
- Länka till relaterade ärenden
- För kodändringar, ange vilka exempel som testades
- För översättnings-PR, inkludera alla filer för en komplett översättning

### Bidragskrav

- Signera Microsoft CLA (automatiskt vid första PR)
- Forka repot till ditt konto innan du gör ändringar
- En PR per logisk ändring (kombinera inte orelaterade fixar)
- Håll PR:erna fokuserade och små när det är möjligt

## Vanliga arbetsflöden

### Lägga till ett nytt kodexempel

1. Navigera till rätt lektionskatalog
2. Skapa exempel i `python/` eller `typescript/` undermapp
3. Följ namngivningskonvention: `{provider}-{exempel-namn}.{py|ts|js}`
4. Testa med riktiga API-uppgifter
5. Dokumentera eventuella nya miljövariabler i lektionens README

### Uppdatera dokumentation

1. Redigera README.md i lektionskatalogen
2. Följ Markdown-riktlinjer (spårnings-ID, relativa länkar)
3. Uppdatering av översättningar hanteras av GitHub Actions (redigera inte manuellt)
4. Testa att alla länkar är giltiga

### Arbeta med Dev Containers

1. Repositoriet innehåller `.devcontainer/devcontainer.json`
2. Post-create script installerar Python beroenden automatiskt
3. Extensioner för Python och Jupyter är förkonfigurerade
4. Miljön baseras på `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Distribution och publicering

Detta är ett läranderepository - det finns ingen distributionsprocess. Kursinnehållet konsumeras via:

1. **GitHub Repository**: Direktåtkomst till kod och dokumentation
2. **GitHub Codespaces**: Omedelbar utvecklingsmiljö med förkonfigurerad setup
3. **Microsoft Learn**: Innehåll kan spridas till officiell lärplattform
4. **docsify**: Dokumentationssida byggd från Markdown (se `docsifytopdf.js` och `package.json`)

### Bygga dokumentationssida

```bash
# Generera PDF från dokumentation (om nödvändigt)
npm run convert
```

## Felsökning

### Vanliga problem

**Python-importfel**:
- Säkerställ att virtuell miljö är aktiverad
- Kör `pip install -r requirements.txt`
- Kontrollera att Python-versionen är 3.9+

**TypeScript build-fel**:
- Kör `npm install` i specifik app-katalog
- Kontrollera att Node.js-versionen är kompatibel
- Rensa `node_modules` och installera om vid behov

**API-autentiseringsfel**:
- Verifiera att `.env`-fil finns och har rätt värden
- Kontrollera att API-nycklar är giltiga och inte har gått ut
- Säkerställ att endpoint-URL:er är korrekta för din region

**Saknade miljövariabler**:
- Kopiera `.env.copy` till `.env`
- Fyll i alla nödvändiga värden för lektionen du arbetar med
- Starta om din applikation efter att `.env` uppdaterats

## Ytterligare resurser

- [Kurs-setup-guide](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Bidragsriktlinjer](./CONTRIBUTING.md)
- [Uppförandekod](./CODE_OF_CONDUCT.md)
- [Säkerhetspolicy](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Samling av avancerade kodexempel](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Projektspecifika noteringar

- Detta är ett **utbildningsrepo** med fokus på lärande, inte produktionskod
- Exempel är medvetet enkla och inriktade på att lära ut koncept
- Kodkvaliteten balanseras med pedagogisk tydlighet
- Varje lektion är självständig och kan genomföras oberoende
- Repo stöder flera API-leverantörer: Azure OpenAI, OpenAI, Microsoft Foundry Models och offline-leverantörer som Foundry Local och Ollama
- Innehållet är flerspråkigt med automatiserade översättningsarbetsflöden
- Aktiv community på Discord för frågor och support

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->