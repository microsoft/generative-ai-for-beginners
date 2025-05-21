<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T12:52:40+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "nl"
}
-->
# Stel Je Ontwikkelomgeving In

We hebben deze repository en cursus opgezet met een [ontwikkelcontainer](https://containers.dev?WT.mc_id=academic-105485-koreyst) die een Universele runtime heeft die Python3, .NET, Node.js en Java ontwikkeling ondersteunt. De bijbehorende configuratie is gedefinieerd in het `devcontainer.json` bestand in de `.devcontainer/` map aan de basis van deze repository.

Om de ontwikkelcontainer te activeren, start je deze in [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (voor een cloud-gehoste runtime) of in [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (voor een lokaal gehoste runtime). Lees [deze documentatie](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) voor meer details over hoe ontwikkelcontainers werken binnen VS Code.  

> [!TIP]  
> We raden aan om GitHub Codespaces te gebruiken voor een snelle start met minimale inspanning. Het biedt een royale [gratis gebruiksquotum](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) voor persoonlijke accounts. Stel [timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) in om inactieve codespaces te stoppen of te verwijderen om je quotum optimaal te benutten.

## 1. Uitvoeren van Opdrachten

Elke les heeft _optionele_ opdrachten die mogelijk worden aangeboden in een of meer programmeertalen, waaronder: Python, .NET/C#, Java en JavaScript/TypeScript. Dit gedeelte biedt algemene richtlijnen met betrekking tot het uitvoeren van die opdrachten.

### 1.1 Python Opdrachten

Python-opdrachten worden aangeboden als toepassingen (`.py` bestanden) of Jupyter notebooks (`.ipynb` bestanden). 
- Om het notebook te draaien, open je het in Visual Studio Code en klik je op _Select Kernel_ (rechtsboven) en selecteer je de standaard Python 3 optie die wordt weergegeven. Je kunt nu _Run All_ kiezen om het notebook uit te voeren.
- Om Python-toepassingen vanuit de command-line uit te voeren, volg je de opdracht-specifieke instructies om ervoor te zorgen dat je de juiste bestanden selecteert en de vereiste argumenten verstrekt.

## 2. Configureren van Providers

Opdrachten **kunnen** ook worden ingesteld om te werken tegen een of meer Large Language Model (LLM) implementaties via een ondersteunde serviceprovider zoals OpenAI, Azure of Hugging Face. Deze bieden een _gehoste eindpunt_ (API) die we programmatisch kunnen benaderen met de juiste inloggegevens (API-sleutel of token). In deze cursus bespreken we deze providers:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) met diverse modellen, waaronder de kern GPT-serie.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) voor OpenAI-modellen met focus op ondernemingsgereedheid
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) voor open-source modellen en inferentie server

**Je zult je eigen accounts moeten gebruiken voor deze oefeningen**. Opdrachten zijn optioneel, dus je kunt ervoor kiezen om één, alle - of geen - van de providers in te stellen op basis van je interesses. Enige richtlijnen voor aanmelden:

| Aanmelden | Kosten | API Sleutel | Playground | Opmerkingen |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Prijzen](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Project-gebaseerd](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Meerdere modellen beschikbaar |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Prijzen](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Moet vooraf aanvragen voor toegang](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Prijzen](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat heeft beperkte modellen](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Volg de onderstaande instructies om deze repository te _configureren_ voor gebruik met verschillende providers. Opdrachten die een specifieke provider vereisen, bevatten een van deze tags in hun bestandsnaam:
 - `aoai` - vereist Azure OpenAI eindpunt, sleutel
 - `oai` - vereist OpenAI eindpunt, sleutel
 - `hf` - vereist Hugging Face token

Je kunt één, geen of alle providers configureren. Gerelateerde opdrachten zullen simpelweg een foutmelding geven bij ontbrekende inloggegevens.

###  2.1. Maak `.env` bestand

We gaan ervan uit dat je de bovenstaande richtlijnen hebt gelezen en je hebt aangemeld bij de relevante provider, en de vereiste authenticatiegegevens (API_KEY of token) hebt verkregen. In het geval van Azure OpenAI gaan we ervan uit dat je ook een geldige implementatie van een Azure OpenAI Service (eindpunt) hebt met ten minste één GPT-model geïmplementeerd voor chat voltooiing.

De volgende stap is om je **lokale omgevingsvariabelen** als volgt te configureren:

1. Zoek in de hoofdmap naar een `.env.copy` bestand dat inhoud zou moeten hebben zoals dit:

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

2. Kopieer dat bestand naar `.env` met het onderstaande commando. Dit bestand is _gitignore-d_, waardoor geheimen veilig blijven.

   ```bash
   cp .env.copy .env
   ```

3. Vul de waarden in (vervang placeholders aan de rechterkant van `=`) zoals beschreven in het volgende gedeelte.

3. (Optie) Als je GitHub Codespaces gebruikt, heb je de optie om omgevingsvariabelen op te slaan als _Codespaces geheimen_ die aan deze repository zijn gekoppeld. In dat geval hoef je geen lokaal .env bestand in te stellen. **Let echter op dat deze optie alleen werkt als je GitHub Codespaces gebruikt.** Je zult nog steeds het .env bestand moeten instellen als je Docker Desktop gebruikt.

### 2.2. Vul `.env` bestand in

Laten we snel kijken naar de variabelenamen om te begrijpen wat ze vertegenwoordigen:

| Variabele  | Beschrijving  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Dit is het gebruikers-toegangstoken dat je in je profiel hebt ingesteld |
| OPENAI_API_KEY | Dit is de autorisatiesleutel voor het gebruik van de service voor niet-Azure OpenAI eindpunten |
| AZURE_OPENAI_API_KEY | Dit is de autorisatiesleutel voor het gebruik van die service |
| AZURE_OPENAI_ENDPOINT | Dit is het geïmplementeerde eindpunt voor een Azure OpenAI bron |
| AZURE_OPENAI_DEPLOYMENT | Dit is het _tekst generatie_ model implementatie eindpunt |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Dit is het _tekst embeddings_ model implementatie eindpunt |
| | |

Opmerking: De laatste twee Azure OpenAI variabelen weerspiegelen een standaardmodel voor chat voltooiing (tekst generatie) en vector zoekopdracht (embeddings) respectievelijk. Instructies voor het instellen ervan zullen worden gedefinieerd in relevante opdrachten.

### 2.3 Configureer Azure: Vanuit Portal

De Azure OpenAI eindpunt en sleutelwaarden zullen worden gevonden in het [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) dus laten we daar beginnen.

1. Ga naar het [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klik op de **Keys and Endpoint** optie in de zijbalk (menu aan de linkerkant).
1. Klik op **Show Keys** - je zou het volgende moeten zien: KEY 1, KEY 2 en Endpoint.
1. Gebruik de KEY 1 waarde voor AZURE_OPENAI_API_KEY
1. Gebruik de Endpoint waarde voor AZURE_OPENAI_ENDPOINT

Vervolgens hebben we de eindpunten nodig voor de specifieke modellen die we hebben geïmplementeerd.

1. Klik op de **Model deployments** optie in de zijbalk (linkermenu) voor Azure OpenAI bron.
1. Op de bestemmingspagina klik je op **Manage Deployments**

Dit brengt je naar de Azure OpenAI Studio website, waar we de andere waarden zullen vinden zoals hieronder beschreven.

### 2.4 Configureer Azure: Vanuit Studio

1. Navigeer naar [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **vanuit je bron** zoals hierboven beschreven.
1. Klik op het **Deployments** tabblad (zijbalk, links) om momenteel geïmplementeerde modellen te bekijken.
1. Als je gewenste model niet is geïmplementeerd, gebruik dan **Create new deployment** om het te implementeren.
1. Je zult een _tekst-generatie_ model nodig hebben - we raden aan: **gpt-35-turbo**
1. Je zult een _tekst-embedding_ model nodig hebben - we raden aan **text-embedding-ada-002**

Werk nu de omgevingsvariabelen bij om de _Deployment name_ te weerspiegelen die is gebruikt. Dit zal meestal hetzelfde zijn als de modelnaam, tenzij je deze expliciet hebt gewijzigd. Dus, als voorbeeld, zou je kunnen hebben:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Vergeet niet het .env bestand op te slaan wanneer je klaar bent**. Je kunt nu het bestand sluiten en terugkeren naar de instructies voor het uitvoeren van het notebook.

### 2.5 Configureer OpenAI: Vanuit Profiel

Je OpenAI API-sleutel kan worden gevonden in je [OpenAI account](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Als je er geen hebt, kun je een account aanmaken en een API-sleutel maken. Zodra je de sleutel hebt, kun je deze gebruiken om de `OPENAI_API_KEY` variabele in het `.env` bestand in te vullen.

### 2.6 Configureer Hugging Face: Vanuit Profiel

Je Hugging Face token kan worden gevonden in je profiel onder [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Deel deze niet openbaar. Maak in plaats daarvan een nieuw token voor het gebruik van dit project en kopieer dat in het `.env` bestand onder de `HUGGING_FACE_API_KEY` variabele. _Opmerking:_ Dit is technisch gezien geen API-sleutel, maar wordt gebruikt voor authenticatie, dus we houden die naamgeving consistent.

**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we ons best doen voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.