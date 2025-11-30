<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T11:05:47+00:00",
  "source_file": "AGENTS.md",
  "language_code": "nl"
}
-->
# AGENTS.md

## Projectoverzicht

Deze repository bevat een uitgebreide cursus van 21 lessen over de basisprincipes van Generatieve AI en applicatieontwikkeling. De cursus is ontworpen voor beginners en behandelt alles, van basisconcepten tot het bouwen van productieklare applicaties.

**Belangrijke technologieën:**
- Python 3.9+ met bibliotheken: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript met Node.js en bibliotheken: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API en GitHub Models
- Jupyter Notebooks voor interactieve leerervaring
- Dev Containers voor een consistente ontwikkelomgeving

**Structuur van de repository:**
- 21 genummerde lesmappen (00-21) met README's, codevoorbeelden en opdrachten
- Meerdere implementaties: Python, TypeScript en soms .NET-voorbeelden
- Vertalingenmap met versies in meer dan 40 talen
- Gecentraliseerde configuratie via `.env`-bestand (gebruik `.env.copy` als sjabloon)

## Setup Commando's

### Initiële setup van de repository

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Python-omgeving instellen

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

### Node.js/TypeScript instellen

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container Setup (Aanbevolen)

De repository bevat een `.devcontainer`-configuratie voor GitHub Codespaces of VS Code Dev Containers:

1. Open de repository in GitHub Codespaces of VS Code met de Dev Containers-extensie
2. Dev Container zal automatisch:
   - Python-afhankelijkheden installeren vanuit `requirements.txt`
   - Post-create script uitvoeren (`.devcontainer/post-create.sh`)
   - Jupyter-kernel instellen

## Ontwikkelworkflow

### Omgevingsvariabelen

Alle lessen die API-toegang vereisen, gebruiken omgevingsvariabelen die zijn gedefinieerd in `.env`:

- `OPENAI_API_KEY` - Voor OpenAI API
- `AZURE_OPENAI_API_KEY` - Voor Azure OpenAI Service
- `AZURE_OPENAI_ENDPOINT` - URL van Azure OpenAI endpoint
- `AZURE_OPENAI_DEPLOYMENT` - Naam van chat completion model deployment
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Naam van embeddings model deployment
- `AZURE_OPENAI_API_VERSION` - API-versie (standaard: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Voor Hugging Face modellen
- `GITHUB_TOKEN` - Voor GitHub Models

### Python-voorbeelden uitvoeren

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### TypeScript-voorbeelden uitvoeren

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Jupyter Notebooks uitvoeren

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### Werken met verschillende lesstijlen

- **"Learn"-lessen**: Focus op README.md-documentatie en concepten
- **"Build"-lessen**: Bevat werkende codevoorbeelden in Python en TypeScript
- Elke les heeft een README.md met theorie, code-uitleg en links naar videomateriaal

## Code Stijlrichtlijnen

### Python

- Gebruik `python-dotenv` voor het beheren van omgevingsvariabelen
- Importeer de `openai`-bibliotheek voor API-interacties
- Gebruik `pylint` voor linting (sommige voorbeelden bevatten `# pylint: disable=all` voor eenvoud)
- Volg PEP 8 naamgevingsconventies
- Sla API-credentials op in het `.env`-bestand, nooit in de code

### TypeScript

- Gebruik het `dotenv`-pakket voor omgevingsvariabelen
- TypeScript-configuratie in `tsconfig.json` voor elke app
- Gebruik `@azure/openai` of `@azure-rest/ai-inference` voor Azure-diensten
- Gebruik `nodemon` voor ontwikkeling met automatische herlaadfunctie
- Bouw voordat je uitvoert: `npm run build` en daarna `npm start`

### Algemene conventies

- Houd codevoorbeelden eenvoudig en educatief
- Voeg opmerkingen toe die belangrijke concepten uitleggen
- De code van elke les moet zelfstandig uitvoerbaar zijn
- Gebruik consistente naamgeving: `aoai-` prefix voor Azure OpenAI, `oai-` voor OpenAI API, `githubmodels-` voor GitHub Models

## Documentatierichtlijnen

### Markdown-stijl

- Alle URL's moeten worden ingepakt in `[tekst](../../url)`-formaat zonder extra spaties
- Relatieve links moeten beginnen met `./` of `../`
- Alle links naar Microsoft-domeinen moeten een tracking-ID bevatten: `?WT.mc_id=academic-105485-koreyst`
- Geen land-specifieke lokale instellingen in URL's (vermijd `/en-us/`)
- Afbeeldingen opgeslagen in de map `./images` met beschrijvende namen
- Gebruik Engelse karakters, cijfers en streepjes in bestandsnamen

### Ondersteuning voor vertalingen

- Repository ondersteunt meer dan 40 talen via geautomatiseerde GitHub Actions
- Vertalingen opgeslagen in de map `translations/`
- Dien geen gedeeltelijke vertalingen in
- Machinevertalingen worden niet geaccepteerd
- Vertaalde afbeeldingen opgeslagen in de map `translated_images/`

## Testen en Validatie

### Controles vóór indiening

Deze repository gebruikt GitHub Actions voor validatie. Voordat je PR's indient:

1. **Controleer Markdown-links**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Handmatig testen**:
   - Test Python-voorbeelden: Activeer venv en voer scripts uit
   - Test TypeScript-voorbeelden: `npm install`, `npm run build`, `npm start`
   - Controleer of omgevingsvariabelen correct zijn geconfigureerd
   - Controleer of API-sleutels werken met de codevoorbeelden

3. **Codevoorbeelden**:
   - Zorg ervoor dat alle code zonder fouten werkt
   - Test met zowel Azure OpenAI als OpenAI API waar van toepassing
   - Controleer of voorbeelden werken met GitHub Models waar ondersteund

### Geen geautomatiseerde tests

Dit is een educatieve repository gericht op tutorials en voorbeelden. Er zijn geen unit-tests of integratietests om uit te voeren. Validatie is voornamelijk:
- Handmatig testen van codevoorbeelden
- GitHub Actions voor Markdown-validatie
- Communityreview van educatieve inhoud

## Richtlijnen voor Pull Requests

### Voor indiening

1. Test codewijzigingen in zowel Python als TypeScript waar van toepassing
2. Voer Markdown-validatie uit (automatisch geactiveerd bij PR)
3. Zorg ervoor dat tracking-ID's aanwezig zijn op alle Microsoft-URL's
4. Controleer of relatieve links geldig zijn
5. Controleer of afbeeldingen correct worden verwezen

### Formaat van PR-titel

- Gebruik beschrijvende titels: `[Les 06] Typfout in Python-voorbeeld opgelost` of `Update README voor les 08`
- Verwijs naar probleemnummers indien van toepassing: `Fixes #123`

### PR-beschrijving

- Leg uit wat er is gewijzigd en waarom
- Link naar gerelateerde problemen
- Voor codewijzigingen, specificeer welke voorbeelden zijn getest
- Voor vertalings-PR's, voeg alle bestanden toe voor een volledige vertaling

### Bijdragevereisten

- Onderteken Microsoft CLA (automatisch bij eerste PR)
- Fork de repository naar je eigen account voordat je wijzigingen aanbrengt
- Eén PR per logische wijziging (combineer geen ongerelateerde fixes)
- Houd PR's gefocust en klein waar mogelijk

## Veelvoorkomende Workflows

### Een nieuw codevoorbeeld toevoegen

1. Navigeer naar de juiste lesmap
2. Maak een voorbeeld in de submap `python/` of `typescript/`
3. Volg de naamgevingsconventie: `{provider}-{example-name}.{py|ts|js}`
4. Test met echte API-credentials
5. Documenteer eventuele nieuwe omgevingsvariabelen in de README van de les

### Documentatie bijwerken

1. Bewerk README.md in de lesmap
2. Volg Markdown-richtlijnen (tracking-ID's, relatieve links)
3. Vertalingen worden afgehandeld door GitHub Actions (niet handmatig bewerken)
4. Test of alle links geldig zijn

### Werken met Dev Containers

1. Repository bevat `.devcontainer/devcontainer.json`
2. Post-create script installeert automatisch Python-afhankelijkheden
3. Extensies voor Python en Jupyter zijn vooraf geconfigureerd
4. Omgeving is gebaseerd op `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Implementatie en Publicatie

Dit is een leerrepository - er is geen implementatieproces. De cursus wordt gebruikt via:

1. **GitHub Repository**: Directe toegang tot code en documentatie
2. **GitHub Codespaces**: Directe ontwikkelomgeving met vooraf geconfigureerde setup
3. **Microsoft Learn**: Inhoud kan worden gesyndiceerd naar het officiële leerplatform
4. **docsify**: Documentatiesite gebouwd vanuit Markdown (zie `docsifytopdf.js` en `package.json`)

### Documentatiesite bouwen

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Problemen oplossen

### Veelvoorkomende problemen

**Importfouten in Python**:
- Zorg ervoor dat de virtuele omgeving is geactiveerd
- Voer `pip install -r requirements.txt` uit
- Controleer of de Python-versie 3.9+ is

**Buildfouten in TypeScript**:
- Voer `npm install` uit in de specifieke app-map
- Controleer of de Node.js-versie compatibel is
- Wis `node_modules` en installeer opnieuw indien nodig

**Authenticatiefouten bij API**:
- Controleer of het `.env`-bestand bestaat en de juiste waarden bevat
- Controleer of API-sleutels geldig en niet verlopen zijn
- Zorg ervoor dat endpoint-URL's correct zijn voor jouw regio

**Ontbrekende omgevingsvariabelen**:
- Kopieer `.env.copy` naar `.env`
- Vul alle vereiste waarden in voor de les waaraan je werkt
- Start je applicatie opnieuw na het bijwerken van `.env`

## Aanvullende bronnen

- [Cursus Setup Gids](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Richtlijnen voor bijdragen](./CONTRIBUTING.md)
- [Gedragscode](./CODE_OF_CONDUCT.md)
- [Beveiligingsbeleid](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Verzameling van geavanceerde codevoorbeelden](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Projectspecifieke opmerkingen

- Dit is een **educatieve repository** gericht op leren, geen productiecode
- Voorbeelden zijn opzettelijk eenvoudig en gericht op het onderwijzen van concepten
- Codekwaliteit is in balans met educatieve duidelijkheid
- Elke les is zelfstandig en kan onafhankelijk worden voltooid
- De repository ondersteunt meerdere API-providers: Azure OpenAI, OpenAI en GitHub Models
- Inhoud is meertalig met geautomatiseerde vertaalworkflows
- Actieve community op Discord voor vragen en ondersteuning

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.