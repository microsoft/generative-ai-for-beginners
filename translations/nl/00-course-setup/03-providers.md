# Kiezen & Configureren van een LLM-provider 🔑

Opdrachten **kunnen** ook worden ingesteld om te werken met een of meer Large Language Model (LLM) implementaties via een ondersteunde serviceprovider zoals OpenAI, Azure of Hugging Face. Deze bieden een _gehoste endpoint_ (API) die we programmatisch kunnen benaderen met de juiste inloggegevens (API-sleutel of token). In deze cursus bespreken we deze providers:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) met diverse modellen waaronder de kern GPT-serie.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) voor OpenAI-modellen met focus op enterprise gereedheid
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) voor open-source modellen en inference server

**Je moet je eigen accounts gebruiken voor deze oefeningen**. Opdrachten zijn optioneel, dus je kunt ervoor kiezen om één, alle of geen van de providers in te stellen op basis van je interesses. Enkele aanwijzingen voor aanmelding:

| Aanmelden | Kosten | API-sleutel | Playground | Opmerkingen |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Prijzen](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Project-gebaseerd](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Meerdere modellen beschikbaar |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Prijzen](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Toegang vooraf aanvragen](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Prijzen](https://huggingface.co/pricing) | [Toegangstokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat heeft beperkte modellen](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Volg de onderstaande instructies om deze repository te _configureren_ voor gebruik met verschillende providers. Opdrachten die een specifieke provider vereisen, bevatten een van deze tags in hun bestandsnaam:

- `aoai` - vereist Azure OpenAI endpoint, sleutel
- `oai` - vereist OpenAI endpoint, sleutel
- `hf` - vereist Hugging Face token

Je kunt één, geen of alle providers configureren. Gerelateerde opdrachten zullen simpelweg een foutmelding geven bij ontbrekende inloggegevens.

## Maak `.env` bestand aan

We gaan ervan uit dat je de bovenstaande aanwijzingen hebt gelezen, je hebt aangemeld bij de relevante provider en de vereiste authenticatiegegevens (API_KEY of token) hebt verkregen. In het geval van Azure OpenAI gaan we ervan uit dat je ook een geldige implementatie hebt van een Azure OpenAI Service (endpoint) met ten minste één GPT-model geïmplementeerd voor chatcompletie.

De volgende stap is het configureren van je **lokale omgevingsvariabelen** als volgt:

1. Zoek in de hoofdmap naar een `.env.copy` bestand dat inhoud zou moeten hebben zoals dit:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Standaard is ingesteld!
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

3. Vul de waarden in (vervang de tijdelijke aanduidingen rechts van `=`) zoals beschreven in de volgende sectie.

4. (Optie) Als je GitHub Codespaces gebruikt, kun je omgevingsvariabelen opslaan als _Codespaces secrets_ die aan deze repository zijn gekoppeld. In dat geval hoef je geen lokaal .env bestand in te stellen. **Let op: deze optie werkt alleen als je GitHub Codespaces gebruikt.** Je moet het .env bestand nog steeds instellen als je Docker Desktop gebruikt.

## Vul het `.env` bestand in

Laten we snel naar de variabelenamen kijken om te begrijpen wat ze vertegenwoordigen:

| Variabele  | Beschrijving  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Dit is de gebruikersaccesstoken die je in je profiel hebt ingesteld |
| OPENAI_API_KEY | Dit is de autorisatiesleutel voor het gebruik van de service voor niet-Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Dit is de autorisatiesleutel voor het gebruik van die service |
| AZURE_OPENAI_ENDPOINT | Dit is het geïmplementeerde endpoint voor een Azure OpenAI resource |
| AZURE_OPENAI_DEPLOYMENT | Dit is het _tekstgeneratie_ model implementatie endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Dit is het _tekst-embedding_ model implementatie endpoint |
| | |

Opmerking: De laatste twee Azure OpenAI variabelen verwijzen respectievelijk naar een standaardmodel voor chatcompletie (tekstgeneratie) en vectorzoekopdrachten (embeddings). Instructies voor het instellen ervan worden gegeven in relevante opdrachten.

## Configureer Azure: Vanuit Portal

De Azure OpenAI endpoint- en sleutelwaarden zijn te vinden in de [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), dus laten we daar beginnen.

1. Ga naar de [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klik op de optie **Sleutels en Endpoint** in de zijbalk (menu links).
1. Klik op **Toon sleutels** - je zou het volgende moeten zien: SLEUTEL 1, SLEUTEL 2 en Endpoint.
1. Gebruik de waarde van SLEUTEL 1 voor AZURE_OPENAI_API_KEY
1. Gebruik de waarde van Endpoint voor AZURE_OPENAI_ENDPOINT

Vervolgens hebben we de endpoints nodig voor de specifieke modellen die we hebben geïmplementeerd.

1. Klik op de optie **Modelimplementaties** in de zijbalk (linkermenu) voor de Azure OpenAI resource.
1. Klik op de bestemmingspagina op **Beheer implementaties**

Dit brengt je naar de Azure OpenAI Studio website, waar we de andere waarden vinden zoals hieronder beschreven.

## Configureer Azure: Vanuit Studio

1. Navigeer naar [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **vanaf je resource** zoals hierboven beschreven.
1. Klik op het tabblad **Implementaties** (zijbalk, links) om de momenteel geïmplementeerde modellen te bekijken.
1. Als je gewenste model niet is geïmplementeerd, gebruik dan **Nieuwe implementatie maken** om het te implementeren.
1. Je hebt een _tekstgeneratie_ model nodig - wij raden aan: **gpt-35-turbo**
1. Je hebt een _tekst-embedding_ model nodig - wij raden aan **text-embedding-ada-002**

Werk nu de omgevingsvariabelen bij om de gebruikte _Implementatienaam_ weer te geven. Dit is meestal hetzelfde als de modelnaam, tenzij je die expliciet hebt gewijzigd. Dus bijvoorbeeld, je zou kunnen hebben:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Vergeet niet het .env bestand op te slaan als je klaar bent**. Je kunt nu het bestand sluiten en terugkeren naar de instructies voor het uitvoeren van de notebook.

## Configureer OpenAI: Vanuit Profiel

Je OpenAI API-sleutel is te vinden in je [OpenAI-account](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Als je er nog geen hebt, kun je een account aanmaken en een API-sleutel genereren. Zodra je de sleutel hebt, kun je deze gebruiken om de variabele `OPENAI_API_KEY` in het `.env` bestand in te vullen.

## Configureer Hugging Face: Vanuit Profiel

Je Hugging Face token is te vinden in je profiel onder [Toegangstokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Plaats deze niet openbaar of deel ze niet. Maak in plaats daarvan een nieuw token aan voor dit projectgebruik en kopieer dat in het `.env` bestand onder de variabele `HUGGING_FACE_API_KEY`. _Opmerking:_ Dit is technisch gezien geen API-sleutel, maar wordt gebruikt voor authenticatie, dus we houden die naamgeving aan voor consistentie.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->