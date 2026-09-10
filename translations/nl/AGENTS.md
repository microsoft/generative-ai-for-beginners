# AGENTS.md

## Project Overzicht

Deze repository bevat een uitgebreide 21-lessen curriculum die de basisprincipes van Generatieve AI en applicatieontwikkeling onderwijst. De cursus is ontworpen voor beginners en behandelt alles van basisconcepten tot het bouwen van productieklare applicaties.

**Belangrijke Technologieën:**
- Python 3.9+ met libraries: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript met Node.js en libraries: `openai` (Azure OpenAI via de v1 endpoint + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI Service, OpenAI API, en Microsoft Foundry Models (GitHub Models wordt beëindigd eind juli 2026)
- Jupyter Notebooks voor interactieve leermomenten
- Dev Containers voor een consistente ontwikkelomgeving

**Repository Structuur:**
- 21 genummerde lesmappen (00-21) met README's, codevoorbeelden en opdrachten
- Meerdere implementaties: Python, TypeScript en soms .NET voorbeelden
- Vertalingen map met 40+ taalversies
- Gecentraliseerde configuratie via `.env` bestand (gebruik `.env.copy` als sjabloon)

## Setup Commando's

### Initiële Repository Setup

```bash
# Clone de repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Kopieer het omgevingssjabloon
cp .env.copy .env
# Bewerk .env met je API-sleutels en eindpunten
```

### Python Omgevingsinstelling

```bash
# Maak virtuele omgeving aan
python3 -m venv venv

# Activeer virtuele omgeving
# Op macOS/Linux:
source venv/bin/activate
# Op Windows:
venv\Scripts\activate

# Installeer afhankelijkheden
pip install -r requirements.txt
```

### Node.js/TypeScript Setup

```bash
# Installeer afhankelijkheden op rootniveau (voor documentatietools)
npm install

# Voor afzonderlijke TypeScript-voorbeelden van lessen, navigeer naar de specifieke les:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container Setup (Aanbevolen)

De repository bevat een `.devcontainer` configuratie voor GitHub Codespaces of VS Code Dev Containers:

1. Open de repository in GitHub Codespaces of VS Code met de Dev Containers extensie
2. Dev Container zal automatisch:
   - Python dependencies installeren vanuit `requirements.txt`
   - Post-create script uitvoeren (`.devcontainer/post-create.sh`)
   - Jupyter kernel instellen

## Ontwikkel Workflow

### Omgevingsvariabelen

Alle lessen die API-toegang vereisen gebruiken omgevingsvariabelen gedefinieerd in `.env`:

- `OPENAI_API_KEY` - Voor OpenAI API
- `AZURE_OPENAI_API_KEY` - Voor Azure OpenAI in Microsoft Foundry (Azure OpenAI Service is nu onderdeel van Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI endpoint URL (Foundry resource endpoint)
- `AZURE_OPENAI_DEPLOYMENT` - Chat completion model deployment naam (cursus standaard: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Embeddings model deployment naam (cursus standaard: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - API versie (standaard: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Voor Hugging Face modellen
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry Models endpoint (multi-provider modelcatalogus)
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry Models API sleutel (vervangt de uit te faseren `GITHUB_TOKEN`)
- `AZURE_INFERENCE_CHAT_MODEL` - Een niet-redenerend model (bijv. `Llama-3.3-70B-Instruct`) gebruikt door de `temperature` voorbeelden, aangezien redeneringsmodellen sampling controls niet ondersteunen

### Modelconventies (belangrijk)

- **Standaard chatmodel is `gpt-5-mini`** - een actueel, niet-verouderd **redenerings** model. Vanaf 2026 worden de oudere temperature-capable "mini" modellen (`gpt-4o-mini`, `gpt-4.1-mini`) *uitgefaseerd*, dus het curriculum standaardiseert op de GPT-5 familie.
- **Redeneringsmodellen verwerpen `temperature` en `top_p`**, en gebruiken `max_output_tokens` (Responses API) / `max_completion_tokens` (chat completions) in plaats van `max_tokens`. Voeg **niet** `temperature`/`top_p`/`max_tokens` toe aan voorbeelden die `gpt-5-mini` aanroepen.
- **Om `temperature` te demonstreren**, gebruiken voorbeelden een **Llama** model (`Llama-3.3-70B-Instruct`) via het Microsoft Foundry Models endpoint (`AZURE_INFERENCE_CHAT_MODEL`). Stuur redeneringsmodellen aan met prompt engineering + reasoning controls in plaats van sampling knoppen.
- **Fine-tuning (les 18)** houdt vast aan `gpt-4.1-mini`: GPT-5 ondersteunt alleen reinforcement fine-tuning (RFT), niet de getoonde supervised fine-tuning (SFT).
- Lessen 20 (Mistral) en 21 (Meta) behouden `temperature`/`max_tokens` omdat ze gericht zijn op Mistral/Llama modellen, die deze ondersteunen.

### Python Voorbeelden Uitvoeren

```bash
# Navigeer naar de lesmap
cd 06-text-generation-apps/python

# Voer een Python-script uit
python aoai-app.py
```

### TypeScript Voorbeelden Uitvoeren

```bash
# Navigeer naar de TypeScript-app directory
cd 06-text-generation-apps/typescript/recipe-app

# Bouw de TypeScript-code
npm run build

# Voer de applicatie uit
npm start
```

### Jupyter Notebooks Uitvoeren

```bash
# Start Jupyter in de hoofdmap van de repository
jupyter notebook

# Of gebruik VS Code met de Jupyter-extensie
```

### Werken met Verschillende Les Types

- **"Leer" lessen**: Focus op README.md documentatie en concepten
- **"Bouw" lessen**: Bevatten werkende codevoorbeelden in Python en TypeScript
- Elke les heeft een README.md met theorie, code walkthroughs en links naar videocontent

## Codestijl Richtlijnen

### Python

- Gebruik `python-dotenv` voor beheer van omgevingsvariabelen
- Importeer `openai` bibliotheek voor API-interacties
- Gebruik `pylint` voor linting (sommige voorbeelden hebben `# pylint: disable=all` voor eenvoud)
- Volg PEP 8 naamgevingsconventies
- Sla API-gegevens op in `.env` bestand, nooit in code

### TypeScript

- Gebruik `dotenv` pakket voor omgevingsvariabelen
- TypeScript configuratie in `tsconfig.json` voor elke app
- Gebruik het `openai` pakket voor Azure OpenAI (wijs client toe aan `/openai/v1/` endpoint en roep `client.responses.create` aan); gebruik `@azure-rest/ai-inference` voor Microsoft Foundry Models
- Gebruik `nodemon` voor ontwikkeling met automatische herlaad
- Bouw vóór het uitvoeren: `npm run build` dan `npm start`

### Algemene Conventies

- Houd codevoorbeelden eenvoudig en educatief
- Voeg commentaar toe om kernconcepten uit te leggen
- De code van elke les moet zelfstandig en uitvoerbaar zijn
- Gebruik consistente naamgeving: `aoai-` prefix voor Azure OpenAI, `oai-` voor OpenAI API, `githubmodels-` voor Microsoft Foundry Models (oud prefix behouden van GitHub Models tijdperk)

## Documentatie Richtlijnen

### Markdown Stijl

- Alle URL's moeten in `[text](../../url)` formaat zijn zonder extra spaties
- Relatieve links moeten beginnen met `./` of `../`
- Alle links naar Microsoft domeinen moeten een tracking ID bevatten: `?WT.mc_id=academic-105485-koreyst`
- Geen land-specifieke locales in URL's (vermijd `/en-us/`)
- Afbeeldingen opgeslagen in `./images` map met beschrijvende namen
- Gebruik Engelse karakters, cijfers en streepjes in bestandsnamen

### Vertalingsondersteuning

- Repository ondersteunt 40+ talen via geautomatiseerde GitHub Actions
- Vertalingen opgeslagen in `translations/` directory
- Dien geen gedeeltelijke vertalingen in
- Machinale vertalingen worden niet geaccepteerd
- Vertaalde afbeeldingen opgeslagen in `translated_images/` directory

## Testen en Validatie

### Pre-submissie Checks

Deze repository gebruikt GitHub Actions voor validatie. Voordat PRs ingediend worden:

1. **Controleer Markdown Links**:
   ```bash
   # De validate-markdown.yml workflow controleert:
   # - Kapotte relatieve paden
   # - Ontbrekende tracking-ID's op paden
   # - Ontbrekende tracking-ID's op URL's
   # - URL's met landinstelling
   # - Kapotte externe URL's
   ```

2. **Handmatig testen**:
   - Test Python voorbeelden: activeer venv en voer scripts uit
   - Test TypeScript voorbeelden: `npm install`, `npm run build`, `npm start`
   - Controleer of omgevingsvariabelen correct zijn ingesteld
   - Controleer of API-sleutels werken met de codevoorbeelden

3. **Code Voorbeelden**:
   - Zorg dat alle code zonder fouten draait
   - Test met zowel Azure OpenAI als OpenAI API waar van toepassing
   - Verifieer dat voorbeelden werken met Microsoft Foundry Models waar ondersteund

### Geen Geautomatiseerde Tests

Dit is een educatieve repository gericht op tutorials en voorbeelden. Er zijn geen unit tests of integratietests om uit te voeren. Validatie is voornamelijk:
- Handmatig testen van codevoorbeelden
- GitHub Actions voor Markdown validatie
- Gemeenschapsbeoordeling van educatieve inhoud

## Richtlijnen Voor Pull Requests

### Voor Indienen

1. Test codewijzigingen in zowel Python als TypeScript waar van toepassing
2. Voer Markdown-validatie uit (wordt automatisch getriggerd bij PR)
3. Zorg dat tracking ID's aanwezig zijn op alle Microsoft URL's
4. Controleer dat relatieve links geldig zijn
5. Verifieer dat afbeeldingen correct worden verwezen

### PR Titel Formaat

- Gebruik beschrijvende titels: `[Lesson 06] Fix Python example typo` of `Update README for lesson 08`
- Verwijs naar issuetickets indien van toepassing: `Fixes #123`

### PR Beschrijving

- Leg uit wat veranderd is en waarom
- Verwijs naar gerelateerde issues
- Geef bij codewijzigingen aan welke voorbeelden getest zijn
- Voor vertalingen: voeg alle bestanden bij voor een volledige vertaling

### Bijdragevereisten

- Onderteken Microsoft CLA (automatisch bij eerste PR)
- Fork de repository naar je account vóór wijzigingen
- Eén PR per logische wijziging (combineer geen niet-gerelateerde fixes)
- Houd PR's gefocust en klein indien mogelijk

## Algemene Workflows

### Een Nieuw Code Voorbeeld Toevoegen

1. Navigeer naar de juiste lesmap
2. Maak voorbeeld in `python/` of `typescript/` submap
3. Volg naamgevingsconventie: `{provider}-{voorbeeld-naam}.{py|ts|js}`
4. Test met daadwerkelijke API-gegevens
5. Documenteer nieuwe omgevingsvariabelen in les README

### Documentatie Bijwerken

1. Bewerk README.md in de lesmap
2. Volg Markdown richtlijnen (tracking ID’s, relatieve links)
3. Vertalingen worden verwerkt door GitHub Actions (niet handmatig bewerken)
4. Test dat alle links geldig zijn

### Werken met Dev Containers

1. Repository bevat `.devcontainer/devcontainer.json`
2. Post-create script installeert automatisch Python afhankelijkheden
3. Extensies voor Python en Jupyter zijn vooraf geconfigureerd
4. Omgeving is gebaseerd op `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Deployment en Publicatie

Dit is een leer-repository - er is geen deploymentproces. Het curriculum wordt gebruikt via:

1. **GitHub Repository**: Directe toegang tot code en documentatie
2. **GitHub Codespaces**: Instant ontwikkelomgeving met vooraf geconfigureerde setup
3. **Microsoft Learn**: Inhoud kan gesyndiceerd worden naar het officiële leerplatform
4. **docsify**: Documentatiesite gebouwd vanuit Markdown (zie `docsifytopdf.js` en `package.json`)

### Documentatie Site Bouwen

```bash
# Genereer PDF van documentatie (indien nodig)
npm run convert
```

## Problemen Oplossen

### Veelvoorkomende Problemen

**Python Importfouten**:
- Zorg dat de virtuele omgeving is geactiveerd
- Voer `pip install -r requirements.txt` uit
- Controleer dat Python versie 3.9+ is

**TypeScript Build Fouten**:
- Voer `npm install` uit in de specifieke app-map
- Controleer of Node.js versie compatibel is
- Verwijder `node_modules` en installeer opnieuw indien nodig

**API Authenticatiefouten**:
- Verifieer dat `.env` bestand bestaat en correcte waarden heeft
- Controleer of API-sleutels geldig en niet verlopen zijn
- Zorg dat endpoint URLs correct zijn voor jouw regio

**Ontbrekende Omgevingsvariabelen**:
- Kopieer `.env.copy` naar `.env`
- Vul alle vereiste waarden in voor de les waaraan je werkt
- Herstart je applicatie na het bijwerken van `.env`

## Aanvullende Bronnen

- [Handleiding Cursus Setup](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Bijdrager Richtlijnen](./CONTRIBUTING.md)
- [Gedragscode](./CODE_OF_CONDUCT.md)
- [Beveiligingsbeleid](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Verzameling Geavanceerde Codevoorbeelden](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Projectspecifieke Notities

- Dit is een **educatieve repository** gericht op leren, niet op productiecode
- Voorbeelden zijn bewust eenvoudig en gericht op het onderwijzen van concepten
- Codekwaliteit wordt in balans gehouden met educatieve duidelijkheid
- Elke les is zelfstandig en kan onafhankelijk voltooid worden
- De repository ondersteunt meerdere API-providers: Azure OpenAI, OpenAI, Microsoft Foundry Models en offline providers zoals Foundry Local en Ollama
- Inhoud is meertalig met geautomatiseerde vertaalworkflows
- Actieve community op Discord voor vragen en ondersteuning

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->