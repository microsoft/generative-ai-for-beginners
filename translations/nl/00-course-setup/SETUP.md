<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:32:44+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "nl"
}
-->
# Stel je ontwikkelomgeving in

We hebben deze repository en cursus opgezet met een [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) die een universele runtime bevat die Python3, .NET, Node.js en Java-ontwikkeling ondersteunt. De bijbehorende configuratie is gedefinieerd in het `devcontainer.json` bestand in de `.devcontainer/` map in de root van deze repository.

Om de dev container te activeren, start je deze in [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (voor een cloud-gehoste runtime) of in [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (voor een lokaal gehoste runtime). Lees [deze documentatie](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) voor meer details over hoe dev containers werken binnen VS Code.

> [!TIP]  
> We raden aan GitHub Codespaces te gebruiken voor een snelle start met minimale inspanning. Het biedt een royale [gratis gebruikskorting](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) voor persoonlijke accounts. Stel [timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) in om inactieve codespaces te stoppen of te verwijderen om je quotum optimaal te benutten.

## 1. Uitvoeren van opdrachten

Elke les bevat _optionele_ opdrachten die in één of meerdere programmeertalen kunnen worden aangeboden, waaronder: Python, .NET/C#, Java en JavaScript/TypeScript. Deze sectie geeft algemene richtlijnen voor het uitvoeren van deze opdrachten.

### 1.1 Python-opdrachten

Python-opdrachten worden geleverd als applicaties (`.py` bestanden) of Jupyter notebooks (`.ipynb` bestanden).  
- Om het notebook uit te voeren, open je het in Visual Studio Code, klik je op _Select Kernel_ (rechtsboven) en kies je de standaard Python 3 optie. Je kunt nu _Run All_ gebruiken om het notebook uit te voeren.  
- Om Python-applicaties via de commandoregel uit te voeren, volg je de opdracht-specifieke instructies om ervoor te zorgen dat je de juiste bestanden selecteert en de vereiste argumenten meegeeft.

## 2. Providers configureren

Opdrachten **kunnen** ook zo worden ingesteld dat ze werken met één of meerdere Large Language Model (LLM) implementaties via een ondersteunde serviceprovider zoals OpenAI, Azure of Hugging Face. Deze bieden een _gehoste endpoint_ (API) die we programmatisch kunnen benaderen met de juiste inloggegevens (API-sleutel of token). In deze cursus bespreken we de volgende providers:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) met diverse modellen, waaronder de kern GPT-serie.  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) voor OpenAI-modellen met focus op enterprise gereedheid  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) voor open-source modellen en inference server

**Je moet je eigen accounts gebruiken voor deze oefeningen**. Opdrachten zijn optioneel, dus je kunt ervoor kiezen om één, alle of geen van de providers in te stellen, afhankelijk van je interesse. Enkele aanwijzingen voor aanmelding:

| Aanmelden | Kosten | API-sleutel | Playground | Opmerkingen |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [Prijzen](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [Project-gebaseerd](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Meerdere modellen beschikbaar |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [Prijzen](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Toegang vooraf aanvragen](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Prijzen](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Hugging Chat heeft beperkte modellen](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Volg de onderstaande instructies om deze repository te _configureren_ voor gebruik met verschillende providers. Opdrachten die een specifieke provider vereisen, bevatten een van deze tags in hun bestandsnaam:  
 - `aoai` - vereist Azure OpenAI endpoint en sleutel  
 - `oai` - vereist OpenAI endpoint en sleutel  
 - `hf` - vereist Hugging Face token

Je kunt één, geen of alle providers configureren. Opdrachten die een provider vereisen zullen een foutmelding geven als de inloggegevens ontbreken.

### 2.1. Maak een `.env` bestand aan

We gaan ervan uit dat je de bovenstaande richtlijnen hebt gelezen, je hebt aangemeld bij de relevante provider en de benodigde authenticatiegegevens (API_KEY of token) hebt verkregen. In het geval van Azure OpenAI gaan we ervan uit dat je ook een geldige implementatie hebt van een Azure OpenAI Service (endpoint) met ten minste één GPT-model ingezet voor chat completion.

De volgende stap is het configureren van je **lokale omgevingsvariabelen** als volgt:

1. Zoek in de rootmap naar een `.env.copy` bestand dat er ongeveer zo uitziet:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopieer dat bestand naar `.env` met het onderstaande commando. Dit bestand is _gitignore-d_, zodat geheimen veilig blijven.

   ```bash
   cp .env.copy .env
   ```

3. Vul de waarden in (vervang de placeholders rechts van `=`) zoals beschreven in de volgende sectie.

3. (Optioneel) Als je GitHub Codespaces gebruikt, kun je omgevingsvariabelen opslaan als _Codespaces secrets_ die aan deze repository zijn gekoppeld. In dat geval hoef je geen lokaal .env bestand in te stellen. **Let op: deze optie werkt alleen als je GitHub Codespaces gebruikt.** Je moet het .env bestand nog steeds instellen als je Docker Desktop gebruikt.

### 2.2. Vul het `.env` bestand in

Laten we snel kijken naar de variabelen om te begrijpen wat ze betekenen:

| Variabele  | Beschrijving  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Dit is het gebruikersaccesstoken dat je in je profiel hebt ingesteld |
| OPENAI_API_KEY | Dit is de autorisatiesleutel voor het gebruik van de service voor niet-Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Dit is de autorisatiesleutel voor het gebruik van die service |
| AZURE_OPENAI_ENDPOINT | Dit is het geïmplementeerde endpoint voor een Azure OpenAI resource |
| AZURE_OPENAI_DEPLOYMENT | Dit is het _text generation_ model deployment endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Dit is het _text embeddings_ model deployment endpoint |
| | |

Opmerking: De laatste twee Azure OpenAI variabelen verwijzen respectievelijk naar een standaardmodel voor chat completion (tekstgeneratie) en vector search (embeddings). Instructies voor het instellen hiervan worden gegeven in de relevante opdrachten.

### 2.3 Configureer Azure: via Portal

De Azure OpenAI endpoint- en sleutelwaarden vind je in de [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), dus laten we daar beginnen.

1. Ga naar de [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
1. Klik op de optie **Keys and Endpoint** in de zijbalk (menu links).  
1. Klik op **Show Keys** - je ziet dan: KEY 1, KEY 2 en Endpoint.  
1. Gebruik de waarde van KEY 1 voor AZURE_OPENAI_API_KEY  
1. Gebruik de waarde van Endpoint voor AZURE_OPENAI_ENDPOINT

Vervolgens hebben we de endpoints nodig voor de specifieke modellen die we hebben ingezet.

1. Klik op de optie **Model deployments** in de zijbalk (linkermenu) voor de Azure OpenAI resource.  
1. Klik op de bestemmingspagina op **Manage Deployments**

Dit brengt je naar de Azure OpenAI Studio website, waar we de andere waarden vinden zoals hieronder beschreven.

### 2.4 Configureer Azure: via Studio

1. Navigeer naar [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **vanaf je resource** zoals hierboven beschreven.  
1. Klik op het tabblad **Deployments** (zijbalk, links) om de momenteel geïmplementeerde modellen te bekijken.  
1. Als je gewenste model niet is geïmplementeerd, gebruik dan **Create new deployment** om het te implementeren.  
1. Je hebt een _text-generation_ model nodig - wij raden aan: **gpt-35-turbo**  
1. Je hebt een _text-embedding_ model nodig - wij raden aan: **text-embedding-ada-002**

Werk nu de omgevingsvariabelen bij om de gebruikte _Deployment name_ weer te geven. Dit is meestal dezelfde naam als het model, tenzij je deze expliciet hebt aangepast. Bijvoorbeeld:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Vergeet niet het .env bestand op te slaan als je klaar bent**. Je kunt het bestand nu sluiten en terugkeren naar de instructies voor het uitvoeren van het notebook.

### 2.5 Configureer OpenAI: via profiel

Je OpenAI API-sleutel vind je in je [OpenAI account](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Als je er nog geen hebt, kun je een account aanmaken en een API-sleutel genereren. Zodra je de sleutel hebt, kun je deze gebruiken om de variabele `OPENAI_API_KEY` in het `.env` bestand in te vullen.

### 2.6 Configureer Hugging Face: via profiel

Je Hugging Face token vind je in je profiel onder [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Deel deze niet openbaar. Maak in plaats daarvan een nieuw token aan voor dit project en kopieer dat in het `.env` bestand onder de variabele `HUGGING_FACE_API_KEY`. _Let op:_ Dit is technisch gezien geen API-sleutel, maar wordt gebruikt voor authenticatie, dus we houden deze naamgeving aan voor consistentie.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.