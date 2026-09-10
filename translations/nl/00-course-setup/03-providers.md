# Het kiezen en configureren van een LLM-provider 🔑

Opdrachten **kunnen** ook worden opgezet om te werken met een of meerdere Large Language Model (LLM) implementaties via een ondersteunde serviceprovider zoals OpenAI, Azure of Hugging Face. Deze bieden een _gehoste endpoint_ (API) waar we programmatisch toegang toe hebben met de juiste referenties (API-sleutel of token). In deze cursus bespreken we deze providers:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) met diverse modellen, inclusief de kernserie GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) voor OpenAI-modellen met focus op bedrijfsrijpheid
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) voor een enkele endpoint en API-sleutel om honderden modellen van OpenAI, Meta, Mistral, Cohere, Microsoft en meer te bereiken (vervangt GitHub Models, dat wordt stopgezet eind juli 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) voor open-source modellen en inferentieserver
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) of [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) als je liever modellen volledig offline op je eigen apparaat draait, zonder cloudabonnement

**Je moet je eigen accounts gebruiken voor deze oefeningen**. Opdrachten zijn optioneel, dus je kunt ervoor kiezen om één, alle of geen enkele provider op te zetten op basis van jouw interesses. Enkele aanwijzingen voor aanmelden:

| Aanmelden | Kosten | API-sleutel | Playground | Opmerkingen |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Prijsstelling](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projectgebaseerd](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Meerdere modellen beschikbaar |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Prijsstelling](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Toegang Moet Vooraf Worden Aangevraagd](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Prijsstelling](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Projectoverzichtspagina](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Gratis laag beschikbaar; één endpoint + sleutel voor vele modelproviders |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Prijsstelling](https://huggingface.co/pricing) | [Toegangstokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat heeft beperkte modellen](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Gratis (draait op je apparaat) | Niet vereist | [Local CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Volledig offline, OpenAI-compatibele endpoint |
| | | | | |

Volg de onderstaande instructies om deze repository te _configureren_ voor gebruik met verschillende providers. Opdrachten die een specifieke provider vereisen, bevatten een van deze tags in hun bestandsnaam:

- `aoai` - vereist Azure OpenAI endpoint, sleutel
- `oai` - vereist OpenAI endpoint, sleutel
- `hf` - vereist Hugging Face token
- `githubmodels` - vereist Microsoft Foundry Models endpoint, sleutel (GitHub Models wordt stopgezet eind juli 2026)

Je kunt één, geen of alle providers configureren. Gerelateerde opdrachten zullen eenvoudigweg een foutmelding geven bij ontbrekende referenties.

## Maak `.env` bestand aan

We gaan ervan uit dat je de bovenstaande instructies hebt gelezen, je hebt aangemeld bij de relevante provider en de vereiste authenticatiegegevens (API_SLEUTEL of token) hebt verkregen. In het geval van Azure OpenAI gaan we ervan uit dat je ook een geldige implementatie hebt van een Azure OpenAI Service (endpoint) met ten minste één GPT-model ingezet voor chatvoltooiing.

De volgende stap is het configureren van je **lokale omgevingsvariabelen** als volgt:

1. Kijk in de hoofdmap naar een `.env.copy` bestand dat inhoud moet hebben zoals deze:

   ```bash
   # OpenAI-provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI in Microsoft Foundry
   ## (Azure OpenAI-service maakt nu deel uit van Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Standaard is ingesteld! (huidige stabiele GA API-versie)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry-modellen (multi-provider modelcatalogus, vervangt GitHub-modellen, die eind juli 2026 met pensioen gaan)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopieer dat bestand naar `.env` met het onderstaande commando. Dit bestand is _gitignore-d_, waardoor geheimen veilig blijven.

   ```bash
   cp .env.copy .env
   ```

3. Vul de waarden in (vervang de tijdelijke aanduidingen rechts van `=`) zoals beschreven in de volgende sectie.

4. (Optie) Als je GitHub Codespaces gebruikt, heb je de optie om omgevingsvariabelen op te slaan als _Codespaces secrets_ die gekoppeld zijn aan deze repository. In dat geval hoef je geen lokaal .env bestand op te zetten. **Let op: deze optie werkt alleen als je GitHub Codespaces gebruikt.** Je moet nog steeds het .env bestand opzetten als je Docker Desktop gebruikt.

## Vul het `.env` bestand in

Laten we kort naar de variabelenamen kijken om te begrijpen wat ze vertegenwoordigen:

| Variabele  | Beschrijving  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Dit is de gebruikersaccesstoken die je in je profiel hebt ingesteld |
| OPENAI_API_KEY | Dit is de autorisatiesleutel voor het gebruik van de service voor niet-Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Dit is de autorisatiesleutel voor het gebruik van die service |
| AZURE_OPENAI_ENDPOINT | Dit is het geïmplementeerde endpoint voor een Azure OpenAI-resource |
| AZURE_OPENAI_DEPLOYMENT | Dit is de _tekstgeneratie_ modelimplementatie-endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Dit is de _tekstemeddings_ modelimplementatie-endpoint |
| AZURE_INFERENCE_ENDPOINT | Dit is het endpoint voor je Microsoft Foundry-project, gebruikt voor Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Dit is de API-sleutel voor je Microsoft Foundry-project |
| | |

Opmerking: De laatste twee Azure OpenAI-variabelen verwijzen respectievelijk naar een standaardmodel voor chatvoltooiing (tekstgeneratie) en vectorzoekopdrachten (embeddings). Instructies voor het instellen ervan worden gegeven in relevante opdrachten.

## Configureer Azure OpenAI: Vanuit Portal

> **Opmerking:** Azure OpenAI Service is nu onderdeel van [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Resources en implementaties verschijnen nog wel in de Azure Portal, maar het dagelijkse modelbeheer (implementaties, playground, monitoring) gebeurt nu in de Foundry-portal in plaats van de oude zelfstandige "Azure OpenAI Studio".

De endpoint- en sleutelwaarden voor Azure OpenAI vind je in de [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst). Laten we daar beginnen.

1. Ga naar de [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klik op de optie **Sleutels en Endpoint** in de zijbalk (menu aan de linkerkant).
1. Klik op **Toon sleutels** - je zou het volgende moeten zien: SLEUTEL 1, SLEUTEL 2 en Endpoint.
1. Gebruik de waarde van SLEUTEL 1 voor AZURE_OPENAI_API_KEY
1. Gebruik de waarde van Endpoint voor AZURE_OPENAI_ENDPOINT

Vervolgens hebben we de endpoints nodig voor de specifieke modellen die we hebben ingezet.

1. Klik op de optie **Modelimplementaties** in de zijbalk (linkermenu) voor de Azure OpenAI-resource.
1. Klik op de bestemmingspagina op **Ga naar Microsoft Foundry portal** (of **Beheer implementaties**, afhankelijk van je resourcetype)

Dit brengt je naar de Microsoft Foundry-portal, waar we de andere waarden vinden zoals hieronder beschreven.

## Configureer Azure OpenAI: Vanuit Microsoft Foundry portal

1. Navigeer naar de [Microsoft Foundry portal](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **vanaf je resource** zoals hierboven beschreven.
1. Klik op het tabblad **Implementaties** (zijbalk, links) om de momenteel geïmplementeerde modellen te bekijken.
1. Als je gewenste model niet geïmplementeerd is, gebruik dan **Model implementeren** om het te implementeren vanuit de [modelcatalogus](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Je hebt een _tekstgeneratiemodel_ nodig - wij bevelen aan: **gpt-5-mini**
1. Je hebt een _tekstemeddingsmodel_ nodig - wij bevelen aan **text-embedding-3-small**

Werk nu de omgevingsvariabelen bij om de gebruikte _Deployment name_ weer te geven. Dit is meestal hetzelfde als de modelnaam, tenzij je het expliciet hebt gewijzigd. Dus bijvoorbeeld zou je kunnen hebben:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Vergeet niet het .env bestand op te slaan wanneer je klaar bent**. Je kunt nu het bestand afsluiten en terugkeren naar de instructies voor het uitvoeren van de notebook.

## Configureer OpenAI: Vanuit profiel

Je OpenAI API-sleutel vind je in je [OpenAI-account](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Als je er nog geen hebt, kun je een account aanmaken en een API-sleutel genereren. Zodra je de sleutel hebt, kun je die gebruiken om de variabele `OPENAI_API_KEY` in het `.env` bestand in te vullen.

## Configureer Hugging Face: Vanuit profiel

Je Hugging Face token vind je in je profiel onder [Toegangstokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Plaats deze niet publiekelijk. Maak in plaats daarvan een nieuw token aan voor dit project en kopieer dat in het `.env` bestand onder de variabele `HUGGING_FACE_API_KEY`. _Opmerking:_ Dit is technisch gezien geen API-sleutel maar wordt gebruikt voor authenticatie, dus behouden we die naamgeving voor consistentie.

## Configureer Microsoft Foundry Models: Vanuit Portal

> **Opmerking:** GitHub Models wordt stopgezet eind juli 2026. Microsoft Foundry Models is de directe vervanger en biedt dezelfde gratis te proberen modelcatalogus en Azure AI Inference SDK / OpenAI SDK ervaring.

1. Ga naar [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) en maak een Foundry-project aan (of open een bestaand project).
1. Blader door de [modelcatalogus](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) en implementeer een model, bijvoorbeeld `gpt-5-mini`.
1. Kopieer op de **Overzicht**-pagina van het project de **endpoint** en **API-sleutel**.
1. Gebruik de endpointwaarde voor `AZURE_INFERENCE_ENDPOINT` en de sleutelwaarde voor `AZURE_INFERENCE_CREDENTIAL` in je `.env` bestand.

## Offline / Lokale providers

Als je liever helemaal geen cloudabonnement gebruikt, kun je compatibele open modellen direct op je eigen apparaat draaien:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsoft's on-device runtime. Het selecteert automatisch de beste uitvoeringsprovider (NPU, GPU of CPU) en biedt een OpenAI-compatibele endpoint, waardoor je de meeste voorbeeldcode in deze cursus met minimale aanpassingen kunt hergebruiken. Zie de [Foundry Local documentatie](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) om te starten, of installeer met `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - een populair alternatief om open modellen zoals Llama, Phi, Mistral en Gemma lokaal te draaien.


Zie [Les 19: Bouwen met SLM's](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) voor praktische voorbeelden met beide opties.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->