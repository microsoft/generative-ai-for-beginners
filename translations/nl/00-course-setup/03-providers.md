# Kiezen & Configureren van een LLM Provider 🔑

Opdrachten **kunnen** ook worden ingesteld om te werken met één of meer Large Language Model (LLM) implementaties via een ondersteunde serviceprovider zoals OpenAI, Azure of Hugging Face. Deze bieden een _gehoste endpoint_ (API) waar we programmatisch toegang toe kunnen krijgen met de juiste referenties (API-sleutel of token). In deze cursus bespreken we deze providers:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) met diverse modellen, inclusief de kern GPT-serie.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) voor OpenAI-modellen met focus op enterprise gereedheid
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) voor één enkele endpoint en API-sleutel om toegang te krijgen tot honderden modellen van OpenAI, Meta, Mistral, Cohere, Microsoft en meer (vervangt GitHub Models, dat eind juli 2026 wordt uitgefaseerd)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) voor opensource-modellen en inference-server
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) of [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) als je modellen liever volledig offline op je eigen apparaat draait, zonder cloudabonnement

**Je zult je eigen accounts nodig hebben voor deze oefeningen**. Opdrachten zijn optioneel, dus je kunt ervoor kiezen om één, alle of geen van de providers in te stellen op basis van je interesses. Enkele aanwijzingen voor aanmelding:

| Aanmelden | Kosten | API-sleutel | Playground | Opmerkingen |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Prijzen](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projectgebaseerd](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Meerdere beschikbare modellen |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Prijzen](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Moet van tevoren Toegang aanvragen](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Prijzen](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Project Overzichtspagina](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Gratis laag beschikbaar; één endpoint + sleutel voor vele modelproviders |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Prijzen](https://huggingface.co/pricing) | [Toegangstokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat heeft beperkte modellen](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Gratis (draait op je apparaat) | Niet vereist | [Lokale CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Volledig offline, OpenAI-compatibele endpoint |
| | | | | |

Volg de onderstaande instructies om deze repository te _configureren_ voor gebruik met verschillende providers. Opdrachten die een specifieke provider vereisen, bevatten een van deze tags in hun bestandsnaam:

- `aoai` - vereist Azure OpenAI endpoint, sleutel
- `oai` - vereist OpenAI endpoint, sleutel
- `hf` - vereist Hugging Face token
- `githubmodels` - vereist Microsoft Foundry Models endpoint, sleutel (GitHub Models wordt uitgefaseerd eind juli 2026)

Je kunt één, geen of alle providers configureren. Gerelateerde opdrachten zullen eenvoudigweg een fout geven bij ontbrekende referenties.

## Maak `.env` bestand aan

We gaan ervan uit dat je de bovenstaande richtlijnen al hebt gelezen, je hebt aangemeld bij de relevante provider en de benodigde authenticatiegegevens (API_KEY of token) hebt verkregen. In het geval van Azure OpenAI gaan we ervan uit dat je ook een geldige implementatie hebt van een Azure OpenAI Service (endpoint) met ten minste één GPT-model ingezet voor chatcompletie.

De volgende stap is om je **lokale omgevingsvariabelen** als volgt te configureren:

1. Zoek in de hoofdfolder naar een `.env.copy` bestand met inhoud zoals deze:

   ```bash
   # OpenAI-aanbieder
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI in Microsoft Foundry
   ## (Azure OpenAI-service is nu onderdeel van Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Standaard is ingesteld! (huidige stabiele GA API-versie)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry-modellen (multi-aanbieder modelcatalogus, vervangt GitHub-modellen, die eind juli 2026 wordt stopgezet)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopieer dat bestand naar `.env` met het onderstaande commando. Dit bestand is _gitignore-d_, zodat geheimen veilig blijven.

   ```bash
   cp .env.copy .env
   ```

3. Vul de waarden in (vervang de aanduidingen rechts van `=`) zoals beschreven in de volgende sectie.

4. (Optioneel) Als je GitHub Codespaces gebruikt, kun je omgevingsvariabelen opslaan als _Codespaces geheimen_ die aan deze repository zijn gekoppeld. In dat geval hoef je het lokale .env-bestand niet in te stellen. **Let wel op: deze optie werkt alleen als je GitHub Codespaces gebruikt.** Je moet nog steeds het .env-bestand instellen als je Docker Desktop gebruikt.

## Vul `.env` bestand in

Laten we snel kijken naar de variabelenamen om te begrijpen wat ze vertegenwoordigen:

| Variabele  | Beschrijving  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Dit is het gebruikers toegangstoken dat je hebt ingesteld in je profiel |
| OPENAI_API_KEY | Dit is de autorisatiesleutel voor het gebruik van de service voor niet-Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Dit is de autorisatiesleutel voor die service |
| AZURE_OPENAI_ENDPOINT | Dit is het uitgerolde endpoint voor een Azure OpenAI resource |
| AZURE_OPENAI_DEPLOYMENT | Dit is het _tekstgeneratie_ model implementatie endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Dit is het _tekst embeddings_ model implementatie endpoint |
| AZURE_INFERENCE_ENDPOINT | Dit is het endpoint voor je Microsoft Foundry-project, gebruikt voor Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Dit is de API-sleutel voor je Microsoft Foundry-project |
| | |

Opmerking: De laatste twee Azure OpenAI variabelen verwijzen naar een standaardmodel voor chatcompletie (tekstgeneratie) en vectorzoekopdrachten (embeddings) respectievelijk. Instructies voor het instellen worden gegeven in gerelateerde opdrachten.

## Configureer Azure OpenAI: Vanaf Portal

> **Opmerking:** Azure OpenAI Service maakt nu deel uit van [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Resources en implementaties zijn nog steeds zichtbaar in de Azure Portal, maar het dagelijkse modelbeheer (implementaties, playground, monitoring) gebeurt nu in het Foundry-portaal in plaats van het oude zelfstandige "Azure OpenAI Studio".

De Azure OpenAI endpoint en sleutel waarden zijn te vinden in de [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), dus laten we daar beginnen.

1. Ga naar de [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klik op de optie **Keys and Endpoint** in de zijbalk (menu links).
1. Klik op **Toon sleutels** - je zou het volgende moeten zien: KEY 1, KEY 2 en Endpoint.
1. Gebruik de waarde van KEY 1 voor AZURE_OPENAI_API_KEY
1. Gebruik de waarde van Endpoint voor AZURE_OPENAI_ENDPOINT

Vervolgens hebben we de endpoints nodig voor de specifieke modellen die we hebben uitgerold.

1. Klik op de optie **Model deployments** in de zijbalk (linkermenu) van de Azure OpenAI resource.
1. Klik op de bestemmingspagina op **Ga naar Microsoft Foundry portal** (of **Beheer Implementaties**, afhankelijk van je type resource)

Dit brengt je naar het Microsoft Foundry portaal, waar we de andere waarden zullen vinden zoals hieronder beschreven.

## Configureer Azure OpenAI: Vanaf Microsoft Foundry portal

1. Navigeer naar het [Microsoft Foundry portal](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **vanaf je resource** zoals hierboven beschreven.
1. Klik op het tabblad **Deployments** (zijbalk, links) om de momenteel uitgerolde modellen te bekijken.
1. Als je gewenste model niet is uitgerold, gebruik dan **Model uitrollen** om het uit de [modelcatalogus](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) te implementeren.
1. Je hebt een _tekstgeneratie_-model nodig - wij raden aan: **gpt-4o-mini**
1. Je hebt een _tekst-embedding_-model nodig - wij raden aan **text-embedding-3-small**

Werk nu de omgevingsvariabelen bij om de naam van de _implementatie_ weer te geven die gebruikt is. Dit is doorgaans hetzelfde als de modelnaam, tenzij je die expliciet hebt gewijzigd. Bijvoorbeeld, je zou kunnen hebben:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Vergeet niet het .env-bestand op te slaan als je klaar bent**. Je kunt nu het bestand afsluiten en terugkeren naar de instructies om de notebook uit te voeren.

## Configureer OpenAI: Vanuit Profiel

Je OpenAI API-sleutel is te vinden in je [OpenAI-account](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Als je er nog geen hebt, kun je een account aanmaken en een API-sleutel genereren. Zodra je de sleutel hebt, kun je deze gebruiken om de variabele `OPENAI_API_KEY` in het `.env` bestand in te vullen.

## Configureer Hugging Face: Vanuit Profiel

Je Hugging Face token is te vinden in je profiel onder [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Plaats deze niet publiekelijk. Maak in plaats daarvan een nieuw token aan voor gebruik in dit project en kopieer dat naar het `.env` bestand onder de variabele `HUGGING_FACE_API_KEY`. _Opmerking:_ Dit is technisch gezien geen API-sleutel maar wordt gebruikt voor authenticatie, dus we behouden de naamgeving voor consistentie.

## Configureer Microsoft Foundry Models: Vanaf Portal

> **Opmerking:** GitHub Models wordt uitgefaseerd aan het eind van juli 2026. Microsoft Foundry Models is de directe vervanging, biedt dezelfde gratis te proberen modelcatalogus en Azure AI Inference SDK / OpenAI SDK ervaring.

1. Ga naar [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) en maak een Foundry-project aan (of open er een).
1. Blader door de [modelcatalogus](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) en rol een model uit, bijvoorbeeld `gpt-4o-mini`.
1. Kopieer op de **Overzicht** pagina van het project de **endpoint** en **API-sleutel**.
1. Gebruik de waarde van de endpoint voor `AZURE_INFERENCE_ENDPOINT` en de sleutel voor `AZURE_INFERENCE_CREDENTIAL` in je `.env` bestand.

## Offline / Lokale Providers

Als je liever helemaal geen cloudabonnement gebruikt, kun je compatibele open modellen rechtstreeks op je eigen apparaat draaien:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoft's runtime op het apparaat. Het selecteert automatisch de beste uitvoeringsprovider (NPU, GPU of CPU) en biedt een OpenAI-compatibele endpoint, zodat je het grootste deel van de voorbeeldcode in deze cursus met minimale aanpassingen kunt hergebruiken. Zie de [Foundry Local documentatie](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) om te beginnen, of installeer met `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - een populair alternatief om open modellen zoals Llama, Phi, Mistral en Gemma lokaal te draaien.


Zie [Les 19: Bouwen met SLM's](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) voor praktijkvoorbeelden met beide opties.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->