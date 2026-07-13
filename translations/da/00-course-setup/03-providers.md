# Valg og konfiguration af en LLM-udbyder 🔑

Opgaver **kan** også sættes op til at arbejde mod en eller flere Large Language Model (LLM) implementeringer gennem en understøttet tjenesteudbyder som OpenAI, Azure eller Hugging Face. Disse leverer en _hostet endpoint_ (API), som vi kan tilgå programmatisk med de rette legitimationsoplysninger (API-nøgle eller token). I dette kursus diskuterer vi disse udbydere:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) med forskelligartede modeller inklusive den grundlæggende GPT-serie.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) for OpenAI-modeller med fokus på erhvervsklarhed
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) for et enkelt endpoint og API-nøgle til adgang til hundreder af modeller fra OpenAI, Meta, Mistral, Cohere, Microsoft og flere (erstatter GitHub Models, som udfases ved udgangen af juli 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) for open source-modeller og inferensserver
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) eller [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) hvis du foretrækker at køre modeller helt offline på din egen enhed uden behov for cloud-abonnement

**Du skal bruge dine egne konti til disse øvelser**. Opgaver er valgfrie, så du kan vælge at sætte én, alle eller ingen af udbyderne op baseret på dine interesser. Her er lidt vejledning til tilmelding:

| Tilmelding | Pris | API-nøgle | Playground | Kommentarer |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [Prisfastsættelse](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [Projektspecifik](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Flere modeller tilgængelige |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [Prisfastsættelse](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Skal ansøges om på forhånd](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Prisfastsættelse](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Projektoversigt](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Gratis niveau tilgængeligt; ét endpoint + nøgle for mange modeludbydere |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Prisfastsættelse](https://huggingface.co/pricing) | [Adgangs-token](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Hugging Chat har begrænsede modeller](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Gratis (kører på din enhed) | Ikke påkrævet | [Lokal CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Fuldstændig offline, OpenAI-kompatibelt endpoint |
| | | | | |

Følg nedenstående instruktioner for at _konfigurere_ dette repository til brug med forskellige udbydere. Opgaver, der kræver en bestemt udbyder, vil indeholde et af disse tags i deres filnavn:

- `aoai` - kræver Azure OpenAI endpoint, nøgle
- `oai` - kræver OpenAI endpoint, nøgle
- `hf` - kræver Hugging Face token
- `githubmodels` - kræver Microsoft Foundry Models endpoint, nøgle (GitHub Models udfases ved udgangen af juli 2026)

Du kan konfigurere én, ingen eller alle udbydere. Relaterede opgaver vil blot fejle ved mangel på legitimationsoplysninger.

## Opret `.env` fil

Vi antager, at du allerede har læst ovenstående vejledning og tilmeldt dig den relevante udbyder og fået de nødvendige autentificeringsoplysninger (API_KEY eller token). I tilfælde af Azure OpenAI antager vi desuden, at du har en gyldig implementering af en Azure OpenAI-tjeneste (endpoint) med mindst én GPT-model implementeret til chat-fuldførelse.

Næste trin er at konfigurere dine **lokale miljøvariabler** som følger:

1. Kig i rodmappen efter en `.env.copy` fil, som bør have indhold som dette:

   ```bash
   # OpenAI Udbyder
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI i Microsoft Foundry
   ## (Azure OpenAI Service er nu en del af Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Standard er sat! (nuværende stabile GA API-version)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry Modeller (multi-udbyder modelkatalog, erstatter GitHub Modeller, som træder ud af brug i slutningen af juli 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopiér denne fil til `.env` med kommandoen nedenfor. Denne fil er _gitignore-d_, så hemmeligheder holdes sikre.

   ```bash
   cp .env.copy .env
   ```

3. Udfyld værdierne (erstat pladsholderne til højre for `=`) som beskrevet i næste afsnit.

4. (Valgfrit) Hvis du bruger GitHub Codespaces, har du mulighed for at gemme miljøvariabler som _Codespaces secrets_ knyttet til dette repository. I det tilfælde behøver du ikke opsætte en lokal .env-fil. **Bemærk dog, at denne mulighed kun virker, hvis du bruger GitHub Codespaces.** Du skal stadig opsætte .env-filen, hvis du bruger Docker Desktop i stedet.

## Udfyld `.env` filen

Lad os hurtigt se på variabelnavnene for at forstå, hvad de repræsenterer:

| Variabel  | Beskrivelse  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Dette er brugerens adgangstoken, som du sætter op i din profil |
| OPENAI_API_KEY | Dette er autorisationsnøglen til brug af tjenesten for ikke-Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Dette er autorisationsnøglen til brug af denne tjeneste |
| AZURE_OPENAI_ENDPOINT | Dette er det deployerede endpoint for en Azure OpenAI-ressource |
| AZURE_OPENAI_DEPLOYMENT | Dette er _tekstgenererings_-modelens deployments-endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Dette er _tekstemeddings_-modelens deployments-endpoint |
| AZURE_INFERENCE_ENDPOINT | Dette er endpointet for dit Microsoft Foundry-projekt, brugt til Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Dette er API-nøglen til dit Microsoft Foundry-projekt |
| | |

Bemærk: De to sidste Azure OpenAI-variabler angiver en standardmodel til chat-fuldførelse (tekstgenerering) og vektor-søgning (embeddings) henholdsvis. Instruktioner til opsætning vil blive defineret i relevante opgaver.

## Konfigurer Azure OpenAI: Fra portalen

> **Bemærk:** Azure OpenAI Service er nu en del af [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Ressourcer og deployment vises stadig i Azure Portal, men daglig modeladministration (deployments, playground, overvågning) foregår nu i Foundry-portal i stedet for den gamle selvstændige "Azure OpenAI Studio".

Azure OpenAI-endpointet og nøgleværdier findes i [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), så lad os starte der.

1. Gå til [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klik på **Nøgler og Endpoint** valgmuligheden i sidebjælken (menu til venstre).
1. Klik på **Vis nøgler** - du bør se følgende: NØGLE 1, NØGLE 2 og Endpoint.
1. Brug værdien fra NØGLE 1 til AZURE_OPENAI_API_KEY
1. Brug værdien fra Endpoint til AZURE_OPENAI_ENDPOINT

Næste skal vi finde endpoints til de specifikke modeller, vi har implementeret.

1. Klik på **Model deployments** valgmuligheden i sidebjælken (venstremenu) for Azure OpenAI-ressourcen.
1. På destinationssiden klik på **Gå til Microsoft Foundry portal** (eller **Administrer deployments**, afhængigt af din ressource-type)

Dette tager dig til Microsoft Foundry-portalen, hvor vi finder de andre værdier som beskrevet nedenfor.

## Konfigurer Azure OpenAI: Fra Microsoft Foundry portal

1. Naviger til [Microsoft Foundry-portalen](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **fra din ressource** som beskrevet ovenfor.
1. Klik på fanen **Deployments** (sidebjælke, venstre) for at se aktuelt implementerede modeller.
1. Hvis din ønskede model ikke er implementeret, brug **Deploy model** for at implementere den fra [modelkataloget](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Du skal bruge en _tekstgenererings_-model – vi anbefaler: **gpt-4o-mini**
1. Du skal bruge en _tekst-embedding_-model – vi anbefaler **text-embedding-3-small**

Opdater nu miljøvariablerne for at afspejle det _Lokale navn_ brugt til deployeringen. Dette vil typisk være det samme som modelnavnet, medmindre du har ændret det eksplicit. Så for eksempel kan du have:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Glem ikke at gemme .env-filen, når du er færdig**. Du kan nu lukke filen og vende tilbage til instruktionerne for at køre notebooken.

## Konfigurer OpenAI: Fra profil

Din OpenAI API-nøgle kan findes i din [OpenAI konto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Hvis du ikke har en, kan du tilmelde dig en konto og oprette en API-nøgle. Når du har nøglen, kan du bruge den til at udfylde `OPENAI_API_KEY` variablen i `.env` filen.

## Konfigurer Hugging Face: Fra profil

Dit Hugging Face token kan findes i din profil under [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Del eller offentliggør dem ikke. Opret i stedet en ny token til dette projekts brug og kopier den ind i `.env` filen under variablen `HUGGING_FACE_API_KEY`. _Bemærk:_ Dette er teknisk set ikke en API-nøgle, men bruges til autentificering, så vi bevarer denne navngivningskonvention for konsistens.

## Konfigurer Microsoft Foundry Models: Fra portal

> **Bemærk:** GitHub Models udfases ved udgangen af juli 2026. Microsoft Foundry Models er den direkte erstatning, og tilbyder det samme gratis prøve-katalog og Azure AI Inference SDK / OpenAI SDK oplevelse.

1. Gå til [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) og opret (eller åbn) et Foundry-projekt.
1. Gennemse [modelkataloget](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) og implementer en model, fx `gpt-4o-mini`.
1. På projektets **Oversigt**-side, kopier **endpoint** og **API-nøgle**.
1. Brug endpoint-værdien til `AZURE_INFERENCE_ENDPOINT` og nøgleværdien til `AZURE_INFERENCE_CREDENTIAL` i din `.env` fil.

## Offline / Lokale udbydere

Hvis du ikke ønsker at bruge et cloud-abonnement overhovedet, kan du køre kompatible åbne modeller direkte på din egen enhed:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsofts on-device runtime. Den vælger automatisk den bedste eksekveringsudbyder (NPU, GPU eller CPU) og eksponerer et OpenAI-kompatibelt endpoint, så du kan genbruge det meste af eksempel-koden i dette kursus med minimale ændringer. Se [Foundry Local dokumentationen](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) for at komme i gang, eller installer med `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - et populært alternativ til at køre åbne modeller som Llama, Phi, Mistral og Gemma lokalt.


Se [Lesson 19: Building with SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) for praktiske eksempler, der bruger begge muligheder.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->