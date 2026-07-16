# AGENTS.md

## Projektöversikt

Detta arkiv innehåller en omfattande kursplan med 21 lektioner som lär ut grunderna i Generativ AI och applikationsutveckling. Kursen är utformad för nybörjare och täcker allt från grundläggande koncept till att bygga produktionsklara applikationer.

**Nyckelteknologier:**
- Python 3.9+ med bibliotek: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript med Node.js och bibliotek: `openai` (Azure OpenAI via v1-endpoint + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI Service, OpenAI API och Microsoft Foundry Models (GitHub Models fasas ut i slutet av juli 2026)
- Jupyter Notebooks för interaktivt lärande
- Dev Containers för enhetlig utvecklingsmiljö

**Arkivstruktur:**
- 21 numrerade lektionskataloger (00-21) med README-filer, kodexempel och uppgifter
- Flera implementationer: Python, TypeScript och ibland .NET-exempel
- Katalog för översättningar med 40+ språkversioner
- Centraliserad konfiguration via `.env`-fil (använd `.env.copy` som mall)

## Installationskommandon

### Initial uppsättning av arkivet

```bash
# Klona repositoriet
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Kopiera miljömall
cp .env.copy .env
# Redigera .env med dina API-nycklar och slutpunkter
```

### Python-miljösetup

```bash
# Skapa virtuell miljö
python3 -m venv venv

# Aktivera virtuell miljö
# På macOS/Linux:
source venv/bin/activate
# På Windows:
venv\Scripts\activate

# Installera beroenden
pip install -r requirements.txt
```

### Node.js/TypeScript-setup

```bash
# Installera beroenden på rot-nivå (för dokumentationsverktyg)
npm install

# För individuella TypeScript-exempel för lektioner, navigera till den specifika lektionen:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container-setup (rekommenderat)

Arkivet inkluderar en `.devcontainer`-konfiguration för GitHub Codespaces eller VS Code Dev Containers:

1. Öppna arkivet i GitHub Codespaces eller i VS Code med Dev Containers-tillägget
2. Dev Container kommer automatiskt att:
   - Installera Python-beroenden från `requirements.txt`
   - Köra post-create-script (`.devcontainer/post-create.sh`)
   - Ställa in Jupyter-kärnan

## Utvecklingsarbetsflöde

### Miljövariabler

Alla lektioner som kräver API-åtkomst använder miljövariabler definierade i `.env`:

- `OPENAI_API_KEY` - För OpenAI API
- `AZURE_OPENAI_API_KEY` - För Azure OpenAI i Microsoft Foundry (Azure OpenAI Service är nu del av Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI-endpoint URL (Foundry-resurs endpoint)
- `AZURE_OPENAI_DEPLOYMENT` - Namn på Chat completion-modellens distribution
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Namn på embeddingsmodellens distribution
- `AZURE_OPENAI_API_VERSION` - API-version (standard: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - För Hugging Face-modeller
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry Models endpoint (flerproviders modellkatalog)
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry Models API-nyckel (ersätter den utgående `GITHUB_TOKEN`)

### Köra Python-exempel

```bash
# Navigera till lektionsmappen
cd 06-text-generation-apps/python

# Kör ett Python-skript
python aoai-app.py
```

### Köra TypeScript-exempel

```bash
# Navigera till TypeScript-appmappen
cd 06-text-generation-apps/typescript/recipe-app

# Bygg TypeScript-koden
npm run build

# Kör applikationen
npm start
```

### Köra Jupyter Notebooks

```bash
# Starta Jupyter i rotmappen för förvaret
jupyter notebook

# Eller använd VS Code med Jupyter-tillägg
```

### Arbeta med olika lektionstyper

- **"Learn"-lektioner**: Fokuserar på README.md-dokumentation och koncept
- **"Build"-lektioner**: Inkluderar fungerande kodexempel i Python och TypeScript
- Varje lektion har en README.md med teori, kodgenomgångar och länkar till videoinnehåll

## Kodstilriktlinjer

### Python

- Använd `python-dotenv` för hantering av miljövariabler
- Importera `openai`-bibliotek för API-interaktioner
- Använd `pylint` för linting (vissa exempel inkluderar `# pylint: disable=all` för enkelhet)
- Följ PEP 8:s namngivningskonventioner
- Spara API-uppgifter i `.env`-fil, aldrig i koden

### TypeScript

- Använd `dotenv`-paketet för miljövariabler
- TypeScript-konfiguration i `tsconfig.json` för varje app
- Använd `openai`-paketet för Azure OpenAI (rikta klienten mot `/openai/v1/`-endpointen och kalla `client.responses.create`); använd `@azure-rest/ai-inference` för Microsoft Foundry Models
- Använd `nodemon` för utveckling med automatisk omladdning
- Bygg innan körning: `npm run build` följt av `npm start`

### Allmänna konventioner

- Håll kodexempel enkla och pedagogiska
- Inkludera kommentarer som förklarar nyckelkoncept
- Varje lektions kod ska vara självständig och körbar
- Använd konsekvent namngivning: `aoai-` prefix för Azure OpenAI, `oai-` för OpenAI API, `githubmodels-` för Microsoft Foundry Models (gammalt prefix från GitHub Models-tiden bevaras)

## Dokumentationsriktlinjer

### Markdown-stil

- Alla URL:er måste vara omslutna med `[text](../../url)`-format utan extra mellanslag
- Relativa länkar måste börja med `./` eller `../`
- Alla länkar till Microsoft-domäner ska inkludera spårnings-ID: `?WT.mc_id=academic-105485-koreyst`
- Inga landspecifika lokaliseringsvägar i URL:er (undvik `/en-us/`)
- Bilder lagras i mappen `./images` med beskrivande namn
- Använd engelska tecken, siffror och bindestreck i filnamn

### Support för översättning

- Arkivet stöder 40+ språk via automatiserade GitHub Actions
- Översättningar lagras i katalogen `translations/`
- Skicka inte in partiella översättningar
- Maskinöversättningar accepteras inte
- Översatta bilder lagras i katalogen `translated_images/`

## Testning och validering

### Kontroller före inskickning

Detta arkiv använder GitHub Actions för validering. Innan du skickar PR:

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
   - Verifiera att miljövariabler är korrekt konfigurerade
   - Kontrollera att API-nycklar fungerar med kodexemplen

3. **Kodexempel**:
   - Säkerställ att all kod körs utan fel
   - Testa med både Azure OpenAI och OpenAI API när tillämpligt
   - Verifiera att exemplen fungerar med Microsoft Foundry Models där det stöds

### Inga automatiserade tester

Detta arkiv är utbildningsfokuserat och inriktat på handledningar och exempel. Det finns inga enhetstester eller integrationstester att köra. Validering sker främst genom:
- Manuell testning av kodexempel
- GitHub Actions för Markdown-validering
- Gemenskapsgranskning av utbildningsinnehåll

## Riktlinjer för Pull Requests

### Innan inskickning

1. Testa kodändringar i både Python och TypeScript när tillämpligt
2. Kör Markdown-validering (triggas automatiskt vid PR)
3. Se till att spårnings-ID finns på alla Microsoft-URL:er
4. Kontrollera att relativa länkar är giltiga
5. Verifiera att bilder är korrekt refererade

### PR-titelformat

- Använd beskrivande titlar: `[Lesson 06] Fix Python example typo` eller `Update README for lesson 08`
- Referera till ärendenummer när det är relevant: `Fixes #123`

### PR-beskrivning

- Förklara vad som ändrats och varför
- Länka till relaterade ärenden
- För kodändringar, specificera vilka exempel som testades
- För översättnings-PR, inkludera alla filer för en komplett översättning

### Krav för bidrag

- Skriv under Microsoft CLA (automatiskt vid första PR)
- Forka arkivet till ditt konto innan du gör ändringar
- En PR per logisk ändring (kombinera ej orelaterade fixar)
- Håll PR:er fokuserade och små när det är möjligt

## Vanliga arbetsflöden

### Lägga till ett nytt kodexempel

1. Navigera till lämplig lektionskatalog
2. Skapa exempel i `python/` eller `typescript/` undermapp
3. Följ namngivningskonvention: `{provider}-{example-name}.{py|ts|js}`
4. Testa med faktiska API-uppgifter
5. Dokumentera eventuella nya miljövariabler i lektions-README

### Uppdatera dokumentation

1. Redigera README.md i lektionskatalogen
2. Följ Markdown-riktlinjer (spårnings-ID, relativa länkar)
3. Uppdateringar av översättningar hanteras av GitHub Actions (redigera inte manuellt)
4. Testa att alla länkar är giltiga

### Arbeta med Dev Containers

1. Arkivet innehåller `.devcontainer/devcontainer.json`
2. Post-create-script installerar Python-beroenden automatiskt
3. Tillägg för Python och Jupyter är förkonfigurerade
4. Miljön baseras på `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Distribution och publicering

Detta är ett utbildningsarkiv - det finns inget distributionsflöde. Kursplanen tas emot via:

1. **GitHub Repository**: Direktåtkomst till kod och dokumentation
2. **GitHub Codespaces**: Omedelbar utvecklingsmiljö med förkonfigurerad setup
3. **Microsoft Learn**: Innehåll kan distribueras till officiell lärplattform
4. **docsify**: Dokumentationssajt byggd från Markdown (se `docsifytopdf.js` och `package.json`)

### Bygga dokumentationssajten

```bash
# Generera PDF från dokumentation (om nödvändigt)
npm run convert
```

## Felsökning

### Vanliga problem

**Python-importfel**:
- Säkerställ att virtuella miljön är aktiverad
- Kör `pip install -r requirements.txt`
- Kontrollera Python-version 3.9+

**TypeScript-byggfel**:
- Kör `npm install` i aktuell app-mapp
- Kontrollera att Node.js-version är kompatibel
- Rensa `node_modules` och installera om vid behov

**API-autentiseringsfel**:
- Verifiera att `.env`-fil finns och har korrekta värden
- Kontrollera att API-nycklar är giltiga och inte utgångna
- Säkerställ att endpoint-URL:er är korrekta för din region

**Saknade miljövariabler**:
- Kopiera `.env.copy` till `.env`
- Fyll i alla nödvändiga värden för aktuell lektion
- Starta om applikationen efter att ha uppdaterat `.env`

## Ytterligare resurser

- [Kursuppsättningsguide](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Riktlinjer för bidrag](./CONTRIBUTING.md)
- [Uppförandekod](./CODE_OF_CONDUCT.md)
- [Säkerhetspolicy](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Samling av avancerade kodexempel](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Projektspecifika anteckningar

- Detta är ett **utbildningsarkiv** fokuserat på lärande, inte produktionskod
- Exempel är medvetet enkla och fokuserade på att lära ut koncept
- Kodkvalitet balanseras med pedagogisk tydlighet
- Varje lektion är självständig och kan genomföras oberoende
- Arkivet stödjer flera API-leverantörer: Azure OpenAI, OpenAI, Microsoft Foundry Models och offline-leverantörer som Foundry Local och Ollama
- Innehåll är flerspråkigt med automatiserade översättningsarbetsflöden
- Aktiv gemenskap på Discord för frågor och support

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->