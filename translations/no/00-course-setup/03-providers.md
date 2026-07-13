# Valg og konfigurasjon av LLM-leverandør 🔑

Oppgaver **kan** også settes opp for å fungere mot én eller flere distribusjoner av store språkmodeller (LLM) gjennom en støttet tjenesteleverandør som OpenAI, Azure eller Hugging Face. Disse tilbyr et _hostet endepunkt_ (API) som vi kan få programmatisk tilgang til med riktige legitimasjoner (API-nøkkel eller token). I dette kurset diskuterer vi disse leverandørene:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) med ulike modeller, inkludert kjerne-GPT-serien.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) for OpenAI-modeller med fokus på bedriftsklarhet
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) for ett enkelt endepunkt og API-nøkkel for å få tilgang til hundrevis av modeller fra OpenAI, Meta, Mistral, Cohere, Microsoft med flere (erstatter GitHub Models, som fases ut i slutten av juli 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) for åpen kildekode modeller og inferensserver
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) eller [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) hvis du heller ønsker å kjøre modeller fullstendig offline på din egen enhet, uten behov for sky-abonnement

**Du må bruke dine egne kontoer for disse øvelsene**. Oppgavene er valgfrie, så du kan velge å sette opp én, alle - eller ingen - av leverandørene basert på dine interesser. Litt veiledning for påmelding:

| Påmelding | Kostnad | API-nøkkel | Lekemiljø | Kommentarer |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Priser](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Prosjektbasert](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Ingen-kode, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Flere modeller tilgjengelige |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Priser](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Må søke på forhånd for tilgang](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Priser](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Prosjektoversikt-side](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Lekemiljø](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Gratisnivå tilgjengelig; ett endepunkt + nøkkel for mange modellleverandører |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Priser](https://huggingface.co/pricing) | [Tilgangstoken](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat har begrensede modeller](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Gratis (kjører på din enhet) | Ikke påkrevd | [Lokal CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Fullt offline, OpenAI-kompatibelt endepunkt |
| | | | | |

Følg instruksjonene nedenfor for å _konfigurere_ dette depotet for bruk med forskjellige leverandører. Oppgaver som krever en spesifikk leverandør vil inneholde en av disse taggene i filnavnet:

- `aoai` - krever Azure OpenAI endepunkt, nøkkel
- `oai` - krever OpenAI endepunkt, nøkkel
- `hf` - krever Hugging Face token
- `githubmodels` - krever Microsoft Foundry Models endepunkt, nøkkel (GitHub Models fases ut i slutten av juli 2026)

Du kan konfigurere én, ingen eller alle leverandører. Relaterte oppgaver vil ganske enkelt feile hvis legitimasjon mangler.

## Opprett `.env`-fil

Vi antar at du allerede har lest veiledningen over, registrert deg hos relevant leverandør, og fått tak i nødvendige autentiseringslegitimasjoner (API_KEY eller token). I tilfellet Azure OpenAI, antar vi også at du har en gyldig distribusjon av Azure OpenAI-tjeneste (endepunkt) med minst én GPT-modell distribuert for samtalekomplettering.

Neste steg er å konfigurere dine **lokale miljøvariabler** som følger:

1. Se i rotmappen etter en `.env.copy`-fil som skal ha innhold som dette:

   ```bash
   # OpenAI-leverandør
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI i Microsoft Foundry
   ## (Azure OpenAI-tjeneste er nå en del av Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Standard er satt! (nåværende stabile GA API-versjon)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry-modeller (multi-leverandør modellkatalog, erstatter GitHub-modeller, som avvikles ved slutten av juli 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopier den filen til `.env` med kommandoen nedenfor. Denne filen er _gitignore-t_, for å holde hemmeligheter trygge.

   ```bash
   cp .env.copy .env
   ```

3. Fyll inn verdiene (erstatt plassholdere på høyre side av `=`) som beskrevet i neste seksjon.

4. (Valgfritt) Hvis du bruker GitHub Codespaces, har du mulighet til å lagre miljøvariabler som _Codespaces-hemmeligheter_ knyttet til dette depotet. I så fall trenger du ikke sette opp en lokal .env-fil. **Merk at dette alternativet bare fungerer hvis du bruker GitHub Codespaces.** Du må fortsatt sette opp .env-filen hvis du bruker Docker Desktop.

## Fyll ut `.env`-filen

La oss ta en rask titt på variabelnavnene for å forstå hva de representerer:

| Variabel  | Beskrivelse  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Dette er brukerens tilgangstoken som du setter opp i profilen din |
| OPENAI_API_KEY | Dette er autorisasjonsnøkkelen for å bruke tjenesten for ikke-Azure OpenAI endepunkter |
| AZURE_OPENAI_API_KEY | Dette er autorisasjonsnøkkelen for å bruke den tjenesten |
| AZURE_OPENAI_ENDPOINT | Dette er det distribuerte endepunktet for en Azure OpenAI-ressurs |
| AZURE_OPENAI_DEPLOYMENT | Dette er _tekstgenererings_-modellens distribusjonsendepunkt |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Dette er _tekstinnbindings_-modellens distribusjonsendepunkt |
| AZURE_INFERENCE_ENDPOINT | Dette er endepunktet for ditt Microsoft Foundry-prosjekt, brukt for Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Dette er API-nøkkelen for ditt Microsoft Foundry-prosjekt |
| | |

Merk: De to siste Azure OpenAI-variablene reflekterer som standard en modell for samtalekomplettering (tekstgenerering) og vektorsøk (innbindinger) henholdsvis. Instruksjoner for å sette dem opp vil bli gitt i relevante oppgaver.

## Konfigurer Azure OpenAI: Fra Portalen

> **Merk:** Azure OpenAI-tjenesten er nå en del av [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Ressurser og distribusjoner vises fortsatt i Azure-portalen, men den daglige modelladministrasjonen (distribusjoner, lekemiljø, overvåking) skjer nå i Foundry-portalen i stedet for det gamle separate "Azure OpenAI Studio".

Azure OpenAI endepunkt- og nøkkelverdier finnes i [Azure-portalen](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), så la oss begynne der.

1. Gå til [Azure-portalen](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klikk på **Nøkler og endepunkt**-valget i sidemenyen (meny til venstre).
1. Klikk **Vis nøkler** - du bør se følgende: NØKKEL 1, NØKKEL 2 og Endepunkt.
1. Bruk NØKKEL 1-verdien for AZURE_OPENAI_API_KEY
1. Bruk Endepunkt-verdien for AZURE_OPENAI_ENDPOINT

Neste, trenger vi endepunktene for de spesifikke modellene vi har distribuert.

1. Klikk på **Modelldistribusjoner** i sidemenyen (venstre meny) for Azure OpenAI-ressursen.
1. På destinasjonssiden, klikk **Gå til Microsoft Foundry-portalen** (eller **Administrer distribusjoner**, avhengig av ressursens type)

Dette vil ta deg til Microsoft Foundry-portalen, hvor vi finner de andre verdiene som beskrevet nedenfor.

## Konfigurer Azure OpenAI: Fra Microsoft Foundry-portalen

1. Naviger til [Microsoft Foundry-portalen](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **fra din ressurs** som beskrevet over.
1. Klikk på **Distribusjoner**-fanen (sidemeny til venstre) for å se modellene som er distribuert nå.
1. Hvis ønsket modell ikke er distribuert, bruk **Distribuer modell** for å distribuere den fra [modellkatalogen](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Du trenger en _tekstgenererings_-modell – vi anbefaler: **gpt-4o-mini**
1. Du trenger en _tekstinnbindings_-modell – vi anbefaler **text-embedding-3-small**

Oppdater nå miljøvariablene for å gjenspeile _Distribusjonsnavnet_ som brukes. Dette vil vanligvis være det samme som modellnavnet med mindre du har endret det eksplisitt. Så, som et eksempel, kan du ha:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Ikke glem å lagre .env-filen når du er ferdig**. Du kan nå lukke filen og gå tilbake til instruksjonene for å kjøre notatboken.

## Konfigurer OpenAI: Fra Profil

Din OpenAI API-nøkkel finner du i din [OpenAI-konto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Hvis du ikke har en, kan du registrere en konto og lage en API-nøkkel. Når du har nøkkelen, kan du bruke den til å fylle inn `OPENAI_API_KEY`-variabelen i `.env`-filen.

## Konfigurer Hugging Face: Fra Profil

Din Hugging Face token finner du i profilen din under [Tilgangstokener](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Ikke del disse offentlig. Lag i stedet en ny token for dette prosjektet og kopier den inn i `.env`-filen under `HUGGING_FACE_API_KEY`-variabelen. _Merk:_ Dette er teknisk sett ikke en API-nøkkel, men brukes til autentisering, så vi beholder den navnekonvensjonen for konsistens.

## Konfigurer Microsoft Foundry Models: Fra Portalen

> **Merk:** GitHub Models fases ut i slutten av juli 2026. Microsoft Foundry Models er den direkte erstatningen, og tilbyr samme gratis-å-prøve modellkatalog og Azure AI Inference SDK / OpenAI SDK-opplevelse.

1. Gå til [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) og opprett (eller åpne) et Foundry-prosjekt.
1. Bla gjennom [modellkatalogen](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) og distribuer en modell, for eksempel `gpt-4o-mini`.
1. På prosjektets **Oversikt**-side, kopier **endepunkt** og **API-nøkkel**.
1. Bruk endepunkt-verdien for `AZURE_INFERENCE_ENDPOINT` og nøkkelverdien for `AZURE_INFERENCE_CREDENTIAL` i din `.env`-fil.

## Offline / Lokale leverandører

Hvis du heller ikke ønsker å bruke et sky-abonnement i det hele tatt, kan du kjøre kompatible åpne modeller direkte på din egen enhet:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsofts lokale runtime. Den velger automatisk den beste utførelsesleverandøren (NPU, GPU eller CPU) og eksponerer et OpenAI-kompatibelt endepunkt, så du kan gjenbruke mesteparten av prøve-koden i dette kurset med minimale endringer. Se [Foundry Local dokumentasjonen](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) for å komme i gang, eller installer med `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - et populært alternativ for å kjøre åpne modeller som Llama, Phi, Mistral, og Gemma lokalt.


Se [Leksjon 19: Bygge med SLM-er](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) for praktiske eksempler som bruker begge alternativene.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->