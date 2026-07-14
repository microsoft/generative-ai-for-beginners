# AGENTS.md

## Project Overzicht

Deze repository bevat een uitgebreid curriculum van 21 lessen die de basisprincipes en applicatieontwikkeling van Generative AI onderwijzen. De cursus is ontworpen voor beginners en behandelt alles van basisconcepten tot het bouwen van productieklare applicaties.

**Belangrijke Technologieën:**
- Python 3.9+ met bibliotheken: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript met Node.js en bibliotheken: `openai` (Azure OpenAI via de v1-endpoint + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Models)
- Azure OpenAI Service, OpenAI API, en Microsoft Foundry Models (GitHub Models wordt uitgefaseerd eind juli 2026)
- Jupyter Notebooks voor interactieve leerervaring
- Dev Containers voor een consistente ontwikkelomgeving

**Repository Structuur:**
- 21 genummerde lesmappen (00-21) met READMEs, codevoorbeelden en opdrachten
- Meerdere implementaties: Python, TypeScript, en soms .NET voorbeelden
- Vertalingen map met 40+ taalversies
- Gecentraliseerde configuratie via `.env` bestand (gebruik `.env.copy` als sjabloon)

## Setup Commando's

### Eerste Repository Setup

```bash
# Kloneer de repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Kopieer het omgevingssjabloon
cp .env.copy .env
# Bewerk .env met je API-sleutels en eindpunten
```

### Python Omgeving Setup

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
# Installeer root-level afhankelijkheden (voor documentatietools)
npm install

# Voor individuele les TypeScript-voorbeelden, navigeer naar de specifieke les:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container Setup (Aanbevolen)

De repository bevat een `.devcontainer` configuratie voor GitHub Codespaces of VS Code Dev Containers:

1. Open de repository in GitHub Codespaces of VS Code met de Dev Containers extensie
2. Dev Container zal automatisch:
   - Python afhankelijkheden installeren vanuit `requirements.txt`
   - Post-create script uitvoeren (`.devcontainer/post-create.sh`)
   - Jupyter kernel instellen

## Ontwikkelworkflow

### Omgevingsvariabelen

Alle lessen die API-toegang vereisen gebruiken omgevingsvariabelen gedefinieerd in `.env`:

- `OPENAI_API_KEY` - Voor OpenAI API
- `AZURE_OPENAI_API_KEY` - Voor Azure OpenAI in Microsoft Foundry (Azure OpenAI Service maakt nu deel uit van Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI endpoint URL (Foundry resource endpoint)
- `AZURE_OPENAI_DEPLOYMENT` - Chat completion model deployment naam
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Embeddings model deployment naam
- `AZURE_OPENAI_API_VERSION` - API versie (standaard: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Voor Hugging Face modellen
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry Models endpoint (multi-provider modelcatalogus)
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry Models API sleutel (vervangt de uitgefaseerde `GITHUB_TOKEN`)

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

# Of gebruik VS Code met de Jupyter extensie
```

### Werken met Verschillende Types Lessen

- **"Learn" lessen**: Richt zich op README.md documentatie en concepten
- **"Build" lessen**: Bevatten werkende codevoorbeelden in Python en TypeScript
- Elke les heeft een README.md met theorie, code-uitleg en links naar videomateriaal

## Code Stijl Richtlijnen

### Python

- Gebruik `python-dotenv` voor beheer van omgevingsvariabelen
- Importeer `openai` bibliotheek voor API interacties
- Gebruik `pylint` voor linting (sommige voorbeelden bevatten `# pylint: disable=all` voor eenvoud)
- Volg PEP 8 naamgevingsconventies
- Sla API-gegevens op in `.env` bestand, nooit in de code

### TypeScript

- Gebruik het `dotenv` pakket voor omgevingsvariabelen
- TypeScript configuratie in `tsconfig.json` voor elke app
- Gebruik het `openai` pakket voor Azure OpenAI (wijs de client naar de `/openai/v1/` endpoint en roep `client.responses.create` aan); gebruik `@azure-rest/ai-inference` voor Microsoft Foundry Models
- Gebruik `nodemon` voor ontwikkeling met auto-herladen
- Bouw eerst: `npm run build` dan `npm start`

### Algemene Conventies

- Houd codevoorbeelden simpel en educatief
- Voeg commentaar toe die belangrijke concepten uitlegt
- Elke lescode moet zelfstandig en uitvoerbaar zijn
- Gebruik consistente naamgeving: `aoai-` prefix voor Azure OpenAI, `oai-` voor OpenAI API, `githubmodels-` voor Microsoft Foundry Models (legacy prefix behouden van de GitHub Models tijdperk)

## Documentatie Richtlijnen

### Markdown Stijl

- Alle URL's moeten in `[text](../../url)` formaat worden gezet zonder extra spaties
- Relatieve links moeten beginnen met `./` of `../`
- Alle links naar Microsoft domeinen moeten tracking ID bevatten: `?WT.mc_id=academic-105485-koreyst`
- Geen land-specifieke locale in URL's (vermijd `/en-us/`)
- Afbeeldingen opgeslagen in `./images` map met beschrijvende namen
- Gebruik Engelse karakters, cijfers en streepjes in bestandsnamen

### Ondersteuning Vertalingen

- Repository ondersteunt 40+ talen via geautomatiseerde GitHub Actions
- Vertalingen opgeslagen in `translations/` directory
- Dien geen gedeeltelijke vertalingen in
- Machinevertalingen worden niet geaccepteerd
- Vertaalde afbeeldingen opgeslagen in `translated_images/` directory

## Testen en Validatie

### Checks Voor Indienen

Deze repository gebruikt GitHub Actions voor validatie. Voor het indienen van PRs:

1. **Controleer Markdown Links**:
   ```bash
   # De validate-markdown.yml workflow controleert:
   # - Kapotte relatieve paden
   # - Ontbrekende tracking-ID's op paden
   # - Ontbrekende tracking-ID's op URL's
   # - URL's met landinstelling
   # - Kapotte externe URL's
   ```

2. **Handmatig Testen**:
   - Test Python voorbeelden: activeer venv en voer scripts uit
   - Test TypeScript voorbeelden: `npm install`, `npm run build`, `npm start`
   - Controleer of omgevingsvariabelen correct zijn ingesteld
   - Controleer of API-sleutels werken met de codevoorbeelden

3. **Code Voorbeelden**:
   - Zorg dat alle code foutloos draait
   - Test met zowel Azure OpenAI als OpenAI API waar van toepassing
   - Verifieer dat voorbeelden werken met Microsoft Foundry Models waar ondersteund

### Geen Geautomatiseerde Tests

Dit is een educatieve repository gericht op tutorials en voorbeelden. Er zijn geen unit- of integratietests om uit te voeren. Validatie is primair:
- Handmatig testen van codevoorbeelden
- GitHub Actions voor Markdown validatie
- Community review van educatieve inhoud

## Richtlijnen Pull Requests

### Voor Indienen

1. Test codewijzigingen in zowel Python als TypeScript waar van toepassing
2. Voer Markdown validatie uit (wordt automatisch gestart bij PR)
3. Zorg dat tracking ID's aanwezig zijn op alle Microsoft URL's
4. Controleer dat relatieve links geldig zijn
5. Controleer dat afbeeldingen correct zijn opgenomen

### PR Titel Formaat

- Gebruik beschrijvende titels: `[Lesson 06] Fix Python example typo` of `Update README for lesson 08`
- Verwijs naar issuetickets indien van toepassing: `Fixes #123`

### PR Beschrijving

- Leg uit wat er is veranderd en waarom
- Link naar gerelateerde issues
- Voor codewijzigingen: geef aan welke voorbeelden getest zijn
- Voor vertaal PRs: includeer alle bestanden voor een volledige vertaling

### Vereisten voor Bijdragen

- Onderteken Microsoft CLA (automatisch bij eerste PR)
- Fork de repository naar je eigen account voor het maken van wijzigingen
- Eén PR per logische wijziging (combineer geen ongerelateerde fixes)
- Houd PR's gefocust en klein waar mogelijk

## Veelvoorkomende Workflows

### Een Nieuw Codevoorbeeld Toevoegen

1. Navigeer naar de juiste lesmap
2. Maak voorbeeld in `python/` of `typescript/` subdirectory
3. Volg naamgevingsconventie: `{provider}-{example-name}.{py|ts|js}`
4. Test met daadwerkelijke API-sleutels
5. Documenteer nieuwe omgevingsvariabelen in de les README

### Documentatie Bijwerken

1. Bewerk README.md in de lesmap
2. Volg Markdown richtlijnen (tracking ID's, relatieve links)
3. Vertalingen worden beheerd door GitHub Actions (niet handmatig aanpassen)
4. Test of alle links geldig zijn

### Werken met Dev Containers

1. Repository bevat `.devcontainer/devcontainer.json`
2. Post-create script installeert automatisch Python afhankelijkheden
3. Extensies voor Python en Jupyter zijn vooraf geconfigureerd
4. De omgeving is gebaseerd op `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Deployen en Publiceren

Dit is een leerrepository - er is geen deploymentproces. Het curriculum wordt gebruikt via:

1. **GitHub Repository**: Directe toegang tot code en documentatie
2. **GitHub Codespaces**: Directe ontwikkelomgeving met vooraf geconfigureerde setup
3. **Microsoft Learn**: Inhoud kan worden gesyndiceerd naar het officiële leerplatform
4. **docsify**: Documentatiesite gebouwd van Markdown (zie `docsifytopdf.js` en `package.json`)

### Documentatiesite Bouwen

```bash
# Genereer PDF van documentatie (indien nodig)
npm run convert
```

## Problemen Oplossen

### Veelvoorkomende Problemen

**Python Import Fouten**:
- Zorg dat de virtuele omgeving geactiveerd is
- Voer `pip install -r requirements.txt` uit
- Controleer dat Python versie 3.9+ is

**TypeScript Build Fouten**:
- Voer `npm install` uit in de specifieke appmap
- Controleer dat Node.js versie compatibel is
- Verwijder `node_modules` en installeer opnieuw indien nodig

**API Authenticatie Fouten**:
- Controleer dat `.env` bestand bestaat en juiste waarden heeft
- Controleer dat API-sleutels geldig en niet verlopen zijn
- Zorg dat endpoint URLs correct zijn voor jouw regio

**Ontbrekende Omgevingsvariabelen**:
- Kopieer `.env.copy` naar `.env`
- Vul alle vereiste waarden in voor de les waar je aan werkt
- Herstart je applicatie na het bijwerken van `.env`

## Extra Bronnen

- [Course Setup Guide](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Contributing Guidelines](./CONTRIBUTING.md)
- [Code of Conduct](./CODE_OF_CONDUCT.md)
- [Security Policy](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Collection of Advanced Code Samples](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Projectspecifieke Notities

- Dit is een **educatieve repository** gericht op leren, geen productiecode
- Voorbeelden zijn bewust eenvoudig en gericht op het onderwijzen van concepten
- Codekwaliteit wordt gebalanceerd met educatieve duidelijkheid
- Elke les is zelfstandig en kan onafhankelijk worden voltooid
- De repository ondersteunt meerdere API-providers: Azure OpenAI, OpenAI, Microsoft Foundry Models, en offline providers zoals Foundry Local en Ollama
- Inhoud is meertalig met geautomatiseerde vertaalworkflows
- Actieve community op Discord voor vragen en ondersteuning

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->