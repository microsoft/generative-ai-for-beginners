<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T17:49:25+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "nl"
}
-->
# Een LLM-provider kiezen & configureren 🔑

Opdrachten **kunnen** ook worden ingesteld om te werken met één of meerdere Large Language Model (LLM) deployments via een ondersteunde serviceprovider zoals OpenAI, Azure of Hugging Face. Deze bieden een _gehoste endpoint_ (API) die we programmatisch kunnen benaderen met de juiste inloggegevens (API-sleutel of token). In deze cursus bespreken we de volgende providers:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) met diverse modellen, waaronder de kern GPT-serie.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) voor OpenAI-modellen met focus op enterprise-toepassingen
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) voor open-source modellen en inference server

**Je hebt je eigen accounts nodig voor deze oefeningen**. De opdrachten zijn optioneel, dus je kunt ervoor kiezen om één, alle of geen van de providers in te stellen, afhankelijk van je interesse. Enkele tips voor het aanmelden:

| Aanmelden | Kosten | API-sleutel | Playground | Opmerkingen |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Prijzen](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Project-gebaseerd](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Meerdere modellen beschikbaar |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Prijzen](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Toegang vooraf aanvragen vereist](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Prijzen](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat heeft beperkte modellen](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Volg de onderstaande instructies om deze repository te _configureren_ voor gebruik met verschillende providers. Opdrachten die een specifieke provider vereisen, bevatten één van deze tags in de bestandsnaam:

- `aoai` - vereist Azure OpenAI endpoint, sleutel
- `oai` - vereist OpenAI endpoint, sleutel
- `hf` - vereist Hugging Face token

Je kunt één, geen of alle providers configureren. Gerelateerde opdrachten zullen simpelweg een foutmelding geven als de benodigde inloggegevens ontbreken.

## Maak een `.env`-bestand aan

We gaan ervan uit dat je de bovenstaande uitleg hebt gelezen, je hebt aangemeld bij de relevante provider en de benodigde authenticatiegegevens (API_KEY of token) hebt verkregen. In het geval van Azure OpenAI gaan we er ook van uit dat je een geldige deployment hebt van een Azure OpenAI Service (endpoint) met ten minste één GPT-model voor chat completion.

De volgende stap is het instellen van je **lokale omgevingsvariabelen** als volgt:

1. Kijk in de hoofdmap voor een bestand `.env.copy` dat er ongeveer zo uit zou moeten zien:

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

3. Vul de waarden in (vervang de placeholders aan de rechterkant van de `=`) zoals beschreven in de volgende sectie.

4. (Optioneel) Als je GitHub Codespaces gebruikt, kun je ervoor kiezen om omgevingsvariabelen op te slaan als _Codespaces secrets_ die aan deze repository zijn gekoppeld. In dat geval hoef je geen lokaal .env-bestand aan te maken. **Let op: deze optie werkt alleen als je GitHub Codespaces gebruikt.** Je moet nog steeds het .env-bestand instellen als je Docker Desktop gebruikt.

## Vul het `.env`-bestand in

Laten we kort naar de variabelen kijken om te begrijpen waar ze voor staan:

| Variabele  | Beschrijving  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Dit is de toegangstoken die je in je profiel hebt ingesteld |
| OPENAI_API_KEY | Dit is de autorisatiesleutel voor het gebruik van de service voor niet-Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Dit is de autorisatiesleutel voor het gebruik van die service |
| AZURE_OPENAI_ENDPOINT | Dit is het gedeployde endpoint voor een Azure OpenAI-resource |
| AZURE_OPENAI_DEPLOYMENT | Dit is het _tekstgeneratie_-model deployment endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Dit is het _tekst-embeddings_-model deployment endpoint |
| | |

Opmerking: De laatste twee Azure OpenAI-variabelen verwijzen naar een standaardmodel voor chat completion (tekstgeneratie) en vector search (embeddings). Instructies voor het instellen hiervan worden gegeven in de relevante opdrachten.

## Azure configureren: via Portal

De Azure OpenAI endpoint- en sleutelwaarden vind je in de [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), dus laten we daar beginnen.

1. Ga naar de [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klik op de optie **Keys and Endpoint** in de zijbalk (menu links).
1. Klik op **Show Keys** - je zou het volgende moeten zien: KEY 1, KEY 2 en Endpoint.
1. Gebruik de waarde van KEY 1 voor AZURE_OPENAI_API_KEY
1. Gebruik de waarde van Endpoint voor AZURE_OPENAI_ENDPOINT

Vervolgens hebben we de endpoints nodig voor de specifieke modellen die we hebben gedeployed.

1. Klik op de optie **Model deployments** in de zijbalk (linkermenu) van de Azure OpenAI-resource.
1. Klik op de bestemmingspagina op **Manage Deployments**

Dit brengt je naar de Azure OpenAI Studio-website, waar we de andere waarden vinden zoals hieronder beschreven.

## Azure configureren: via Studio

1. Navigeer naar [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **vanuit je resource** zoals hierboven beschreven.
1. Klik op het tabblad **Deployments** (zijbalk, links) om de momenteel gedeployde modellen te bekijken.
1. Als je gewenste model niet is gedeployed, gebruik dan **Create new deployment** om het te deployen.
1. Je hebt een _tekstgeneratie_-model nodig - wij raden aan: **gpt-35-turbo**
1. Je hebt een _tekst-embedding_-model nodig - wij raden aan **text-embedding-ada-002**

Werk nu de omgevingsvariabelen bij zodat ze overeenkomen met de gebruikte _Deployment name_. Dit is meestal gelijk aan de modelnaam, tenzij je deze expliciet hebt aangepast. Dus, als voorbeeld, kun je het volgende hebben:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Vergeet niet het .env-bestand op te slaan als je klaar bent**. Je kunt het bestand nu afsluiten en teruggaan naar de instructies om de notebook uit te voeren.

## OpenAI configureren: via Profiel

Je OpenAI API-sleutel vind je in je [OpenAI-account](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Als je er nog geen hebt, kun je een account aanmaken en een API-sleutel genereren. Zodra je de sleutel hebt, kun je deze invullen bij de variabele `OPENAI_API_KEY` in het `.env`-bestand.

## Hugging Face configureren: via Profiel

Je Hugging Face-token vind je in je profiel onder [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Deel deze niet openbaar. Maak in plaats daarvan een nieuw token aan voor dit project en kopieer dat naar het `.env`-bestand onder de variabele `HUGGING_FACE_API_KEY`. _Opmerking:_ Dit is technisch gezien geen API-sleutel, maar wordt wel gebruikt voor authenticatie, dus we houden deze naamgeving aan voor de consistentie.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor kritische informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.