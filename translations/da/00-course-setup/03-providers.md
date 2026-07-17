# Valg & Konfiguration af en LLM-udbyder 🔑

Opgaver **kan** også opsættes til at arbejde mod en eller flere stort sprogmodel (LLM) implementeringer via en understøttet tjenesteudbyder som OpenAI, Azure eller Hugging Face. Disse tilbyder et _hostet endpoint_ (API), som vi kan tilgå programmatisk med de rette legitimationsoplysninger (API-nøgle eller token). I dette kursus diskuterer vi disse udbydere:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) med diverse modeller inklusive den centrale GPT-serie.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) for OpenAI-modeller med fokus på virksomhedsparathed
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) for et enkelt endpoint og API-nøgle til at tilgå hundreder af modeller fra OpenAI, Meta, Mistral, Cohere, Microsoft og flere (erstatter GitHub Models, som udfases ved udgangen af juli 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) for open source-modeller og inferensserver
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) eller [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst), hvis du hellere vil køre modeller fuldt offline på din egen enhed uden behov for abonnement i skyen

**Du skal bruge dine egne konti til disse øvelser**. Opgaverne er valgfrie, så du kan vælge at opsætte en, alle eller ingen af udbyderne baseret på dine interesser. Her er lidt vejledning til tilmelding:

| Tilmelding | Pris | API-nøgle | Playground | Kommentarer |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Priser](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektbaseret](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Flere modeller tilgængelige |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Priser](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Du skal søge om adgang på forhånd](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Priser](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Projektoversigt](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Gratisniveau tilgængeligt; ét endpoint + nøgle til mange modeludbydere |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Priser](https://huggingface.co/pricing) | [Adgangstokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat har begrænsede modeller](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Gratis (kører på din enhed) | Ikke påkrævet | [Lokal CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Fuldt offline, OpenAI-kompatibelt endpoint |
| | | | | |

Følg nedenstående anvisninger for at _konfigurere_ dette repository til brug med forskellige udbydere. Opgaver, der kræver en specifik udbyder, vil indeholde ét af disse tags i deres filnavn:

- `aoai` - kræver Azure OpenAI-endpoint, nøgle
- `oai` - kræver OpenAI-endpoint, nøgle
- `hf` - kræver Hugging Face-token
- `githubmodels` - kræver Microsoft Foundry Models-endpoint, nøgle (GitHub Models udfases ved udgangen af juli 2026)

Du kan konfigurere én, ingen eller alle udbydere. Relaterede opgaver vil blot fejle, hvis legitimationsoplysninger mangler.

## Opret `.env` fil

Vi antager, at du allerede har læst ovenstående vejledning og tilmeldt dig den relevante udbyder samt fået de nødvendige godkendelseslegitimationsoplysninger (API_KEY eller token). I tilfælde af Azure OpenAI antager vi også, at du har en gyldig implementering af en Azure OpenAI Service (endpoint) med mindst én GPT-model udrullet til chat-komplettering.

Næste trin er at konfigurere dine **lokale miljøvariabler** som følger:

1. Kig i rodmappen efter en `.env.copy` fil, som burde indeholde noget i stil med dette:

   ```bash
   # OpenAI Udbyder
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI i Microsoft Foundry
   ## (Azure OpenAI Service er nu en del af Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Standard er sat! (nuværende stabile GA API-version)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry Modeller (multi-udbyder modelkatalog, erstatter GitHub Modeller, som udfases ved udgangen af juli 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopiér denne fil til `.env` ved hjælp af kommandoen nedenfor. Denne fil er _gitignore-d_ og holder hemmeligheder sikre.

   ```bash
   cp .env.copy .env
   ```

3. Udfyld værdierne (erstat pladsholderne til højre for `=`) som beskrevet i næste sektion.

4. (Valgfrit) Hvis du bruger GitHub Codespaces, kan du vælge at gemme miljøvariabler som _Codespaces-hemmeligheder_ tilknyttet dette repository. I så fald behøver du ikke opsætte en lokal .env-fil. **Bemærk dog, at denne mulighed kun virker, hvis du bruger GitHub Codespaces.** Du skal stadig opsætte .env-filen, hvis du bruger Docker Desktop i stedet.

## Udfyld `.env` fil

Lad os hurtigt se på variabelnavnene for at forstå, hvad de repræsenterer:

| Variabel  | Beskrivelse  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Dette er brugeradgangstokenet, du har opsat i din profil |
| OPENAI_API_KEY | Dette er autorisationsnøglen til at bruge tjenesten for ikke-Azure OpenAI-endpoints |
| AZURE_OPENAI_API_KEY | Dette er autorisationsnøglen til at bruge den tjeneste |
| AZURE_OPENAI_ENDPOINT | Dette er det udrullede endpoint for en Azure OpenAI-ressource |
| AZURE_OPENAI_DEPLOYMENT | Dette er _tekstgenererings_-modeludrulnings-endpointet |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Dette er _tekstindlejrings_-modeludrulnings-endpointet |
| AZURE_INFERENCE_ENDPOINT | Dette er endpointet for dit Microsoft Foundry-projekt, brugt til Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Dette er API-nøglen til dit Microsoft Foundry-projekt |
| | |

Bemærk: De sidste to Azure OpenAI-variabler afspejler en standardmodel til chat-komplettering (tekstgenerering) og vektorsøgning (indlejringer) henholdsvis. Instruktioner til opsætning vil blive defineret i relevante opgaver.

## Konfigurer Azure OpenAI: Fra portal

> **Bemærk:** Azure OpenAI Service er nu en del af [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Ressourcer og udrulninger vises stadig i Azure Portal, men den daglige modeladministration (udrulninger, playground, overvågning) foregår nu i Foundry-portalen i stedet for det gamle selvstændige "Azure OpenAI Studio".

Azure OpenAI-endpointet og nøgleværdier findes i [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), så lad os starte der.

1. Gå til [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klik på **Keys and Endpoint** i sidebjælken (menuen til venstre).
1. Klik på **Show Keys** - du burde se følgende: KEY 1, KEY 2 og Endpoint.
1. Brug værdien af KEY 1 som AZURE_OPENAI_API_KEY
1. Brug Endpoint-værdien som AZURE_OPENAI_ENDPOINT

Næste skal vi bruge endpoints for de specifikke modeller, vi har udrullet.

1. Klik på **Model deployments** i sidebjælken (venstre menu) for Azure OpenAI-ressourcen.
1. På destinationssiden klik på **Go to Microsoft Foundry portal** (eller **Manage Deployments**, afhængig af din ressource-type)

Dette vil føre dig til Microsoft Foundry-portalen, hvor vi finder de andre værdier som beskrevet nedenfor.

## Konfigurer Azure OpenAI: Fra Microsoft Foundry-portalen

1. Naviger til [Microsoft Foundry-portalen](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **fra din ressource** som beskrevet ovenfor.
1. Klik på fanen **Deployments** (sidebjælke, venstre) for at se de aktuelt udrullede modeller.
1. Hvis din ønskede model ikke er udrullet, brug **Deploy model** til at udrulle den fra [modelkataloget](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Du vil få brug for en _tekstgenererings_ model – vi anbefaler: **gpt-5-mini**
1. Du vil få brug for en _tekstindlejrings_ model – vi anbefaler **text-embedding-3-small**

Opdater nu miljøvariablerne for at afspejle det _Deployment name_, der bruges. Det vil typisk være det samme som modelnavnet, medmindre du har ændret det eksplicit. For eksempel kunne du have:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Glem ikke at gemme .env-filen, når du er færdig**. Du kan nu lukke filen og vende tilbage til instruktionerne for at køre notebook'en.

## Konfigurer OpenAI: Fra profil

Din OpenAI API-nøgle kan findes i din [OpenAI-konto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Hvis du ikke har en, kan du tilmelde dig en konto og oprette en API-nøgle. Når du har nøglen, kan du bruge den til at udfylde `OPENAI_API_KEY` variablen i `.env` filen.

## Konfigurer Hugging Face: Fra profil

Din Hugging Face-token kan findes i din profil under [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Del eller offentliggør dem ikke. Opret i stedet en ny token til dette projekt og kopier den ind i `.env` filen under variablen `HUGGING_FACE_API_KEY`. _Bemærk:_ Dette er teknisk set ikke en API-nøgle, men bruges til godkendelse, så vi beholder navngivningen for konsistens.

## Konfigurer Microsoft Foundry Models: Fra portal

> **Bemærk:** GitHub Models udfases ved udgangen af juli 2026. Microsoft Foundry Models er den direkte erstatning og tilbyder samme gratis-at-prøve modelkatalog og Azure AI Inference SDK / OpenAI SDK oplevelse.

1. Gå til [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) og opret (eller åbn) et Foundry-projekt.
1. Gennemse [modelkataloget](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) og udrul en model, fx `gpt-5-mini`.
1. På projektets **Oversigt**-side kopier **endpoint** og **API nøgle**.
1. Brug endpoint-værdien til `AZURE_INFERENCE_ENDPOINT` og nøgle-værdien til `AZURE_INFERENCE_CREDENTIAL` i din `.env` fil.

## Offline / Lokale udbydere

Hvis du ikke ønsker at bruge abonnement i skyen, kan du køre kompatible åbne modeller direkte på din egen enhed:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsofts on-device runtime. Den vælger automatisk den bedste køreprovider (NPU, GPU eller CPU) og eksponerer et OpenAI-kompatibelt endpoint, så du kan genbruge det meste af eksempelkoden i dette kursus med minimale ændringer. Se [Foundry Local-dokumentationen](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) for at komme i gang, eller installer med `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - et populært alternativ til at køre åbne modeller som Llama, Phi, Mistral og Gemma lokalt.


Se [Lesson 19: Building with SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) for praktiske eksempler, der bruger begge muligheder.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->