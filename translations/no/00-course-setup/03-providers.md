# Velge og konfigurere en LLM-leverandør 🔑

Oppgaver **kan** også settes opp for å fungere mot en eller flere store språkmodell-implementasjoner (LLM) gjennom en støttet tjenesteleverandør som OpenAI, Azure eller Hugging Face. Disse tilbyr et _hostet endepunkt_ (API) som vi kan få tilgang til programmatisk med riktig legitimasjon (API-nøkkel eller token). I dette kurset diskuterer vi disse leverandørene:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) med forskjellige modeller inkludert den kjente GPT-serien.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) for OpenAI-modeller med fokus på bedriftsklarhet
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) for et enkelt endepunkt og API-nøkkel for tilgang til hundrevis av modeller fra OpenAI, Meta, Mistral, Cohere, Microsoft og flere (erstatter GitHub Models, som fases ut i slutten av juli 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) for åpen kildekode-modeller og inferens-server
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) eller [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) hvis du heller vil kjøre modeller helt offline på din egen enhet, uten behov for skysubscription

**Du må bruke dine egne kontoer for disse øvelsene**. Oppgavene er valgfrie, så du kan velge å sette opp én, alle — eller ingen — av leverandørene basert på dine interesser. Noe veiledning for registrering:

| Registrering | Kostnad | API-nøkkel | Prøveområde | Kommentarer |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Priser](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Prosjektbasert](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Flere modeller tilgjengelige |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Priser](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Må søke på forhånd for tilgang](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Priser](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Prosjektoversikt-side](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Gratisnivå tilgjengelig; ett endepunkt + nøkkel for mange modellleverandører |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Priser](https://huggingface.co/pricing) | [Tilgangs tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat har begrensede modeller](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Gratis (kjører på din enhet) | Ikke nødvendig | [Lokal CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Fullstendig offline, OpenAI-kompatibelt endepunkt |
| | | | | |

Følg instruksjonene nedenfor for å _konfigurere_ dette depotet for bruk med forskjellige leverandører. Oppgaver som krever en spesifikk leverandør vil inneholde en av disse taggene i filnavnet:

- `aoai` - krever Azure OpenAI endepunkt, nøkkel
- `oai` - krever OpenAI endepunkt, nøkkel
- `hf` - krever Hugging Face token
- `githubmodels` - krever Microsoft Foundry Models endepunkt, nøkkel (GitHub Models fases ut i slutten av juli 2026)

Du kan konfigurere en, ingen, eller alle leverandørene. Relaterte oppgaver vil bare feile hvis legitimasjon mangler.

## Opprett `.env`-fil

Vi antar at du allerede har lest veiledningen ovenfor og registrert deg hos den relevante leverandøren, og skaffet nødvendig autentiseringsinformasjon (API_KEY eller token). Når det gjelder Azure OpenAI, antar vi også at du har en gyldig implementasjon av en Azure OpenAI-tjeneste (endepunkt) med minst én GPT-modell utplassert for chat-fullføring.

Neste steg er å konfigurere dine **lokale miljøvariabler** som følger:

1. Se i rotmappen etter en `.env.copy`-fil som bør ha innhold som dette:

   ```bash
   # OpenAI-leverandør
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI i Microsoft Foundry
   ## (Azure OpenAI-tjenesten er nå en del av Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Standard er satt! (nåværende stabile GA API-versjon)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry-modeller (multi-leverandør modellkatalog, erstatter GitHub-modeller, som avsluttes i slutten av juli 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopier denne filen til `.env` med følgende kommando. Denne filen er _gitignore-d_, for å holde hemmeligheter trygge.

   ```bash
   cp .env.copy .env
   ```

3. Fyll inn verdiene (erstatt plassholdere på høyre side av `=`) som beskrevet i neste seksjon.

4. (Valgfritt) Hvis du bruker GitHub Codespaces, har du mulighet til å lagre miljøvariabler som _Codespaces-hemmeligheter_ knyttet til dette depotet. I så fall trenger du ikke sette opp en lokal .env-fil. **Merk likevel at denne muligheten kun fungerer hvis du bruker GitHub Codespaces.** Du må fortsatt sette opp .env-filen hvis du bruker Docker Desktop i stedet.

## Fyll ut `.env`-filen

La oss se raskt på variabelnavnene for å forstå hva de representerer:

| Variabel  | Beskrivelse  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Dette er brukertokenet du setter opp i profilen din |
| OPENAI_API_KEY | Dette er autorisasjonsnøkkelen for å bruke tjenesten for ikke-Azure OpenAI-endepunkter |
| AZURE_OPENAI_API_KEY | Dette er autorisasjonsnøkkelen for denne tjenesten |
| AZURE_OPENAI_ENDPOINT | Dette er det implementerte endepunktet for en Azure OpenAI-ressurs |
| AZURE_OPENAI_DEPLOYMENT | Dette er endepunktet for en _tekstgenererings_-modellimplementering |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Dette er endepunktet for en _tekst-embedding_-modellimplementering |
| AZURE_INFERENCE_ENDPOINT | Dette er endepunktet for ditt Microsoft Foundry-prosjekt, brukt for Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Dette er API-nøkkelen for ditt Microsoft Foundry-prosjekt |
| | |

Merk: De to siste Azure OpenAI-variablene angir som standardmodell for chat-fullføring (tekstgenerering) og vektorsøk (embedding) henholdsvis. Instruksjoner for å sette disse vil bli gitt i relevante oppgaver.

## Konfigurer Azure OpenAI: Fra portalen

> **Merk:** Azure OpenAI Service er nå en del av [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Ressurser og implementasjoner vises fortsatt i Azure-portalen, men daglig modelladministrasjon (implementasjoner, prøveområde, overvåking) skjer nå i Foundry-portalen i stedet for den gamle frittstående "Azure OpenAI Studio".

Azure OpenAI endepunkt- og nøkkelverdier finner du i [Azure-portalen](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), så la oss starte der.

1. Gå til [Azure-portalen](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klikk på **Keys and Endpoint**-valget i sidemenyen (meny til venstre).
1. Klikk **Vis nøkler** - du skal se følgende: KEY 1, KEY 2 og Endepunkt.
1. Bruk verdien til KEY 1 for AZURE_OPENAI_API_KEY
1. Bruk Endepunkt-verdien for AZURE_OPENAI_ENDPOINT

Deretter trenger vi endepunktene for de spesifikke modellene vi har implementert.

1. Klikk på **Model deployments**-valget i sidemenyen (venstremeny) for Azure OpenAI-ressursen.
1. På destinasjonssiden klikker du **Gå til Microsoft Foundry-portalen** (eller **Administrer implementasjoner**, avhengig av ressurs type)

Dette tar deg til Microsoft Foundry-portalen, hvor vi finner de andre verdiene som beskrevet nedenfor.

## Konfigurer Azure OpenAI: Fra Microsoft Foundry-portalen

1. Naviger til [Microsoft Foundry-portalen](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **fra din ressurs** som beskrevet ovenfor.
1. Klikk på fanen **Deployments** (sidemeny, venstre) for å se nåværende implementerte modeller.
1. Hvis ønsket modell ikke er implementert, bruk **Deploy model** for å implementere den fra [modellkatalogen](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Du trenger en _tekstgenerering_-modell — vi anbefaler: **gpt-5-mini**
1. Du trenger en _tekst-embedding_-modell — vi anbefaler **text-embedding-3-small**

Oppdater nå miljøvariablene for å reflektere det _Implementeringsnavnet_ som brukes. Dette vil vanligvis være det samme som modellnavnet med mindre det er endret eksplisitt. For eksempel kan du ha:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Ikke glem å lagre .env-filen når du er ferdig**. Du kan nå lukke filen og gå tilbake til instruksjonene for å kjøre notebooken.

## Konfigurer OpenAI: Fra profil

Din OpenAI API-nøkkel finner du i din [OpenAI-konto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Hvis du ikke har en, kan du registrere deg for konto og opprette en API-nøkkel. Når du har nøkkelen, kan du bruke den til å fylle ut `OPENAI_API_KEY` variabelen i `.env`-filen.

## Konfigurer Hugging Face: Fra profil

Din Hugging Face-token finner du i profilen din under [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Del eller publiser ikke disse offentlig. Lag i stedet en ny token for dette prosjektet og kopier den inn i `.env`-filen under `HUGGING_FACE_API_KEY` variabelen. _Merk:_ Dette er teknisk sett ikke en API-nøkkel, men brukes for autentisering, så vi beholder navnekonvensjonen for konsistens.

## Konfigurer Microsoft Foundry Models: Fra portalen

> **Merk:** GitHub Models fases ut i slutten av juli 2026. Microsoft Foundry Models er direkte erstatning, som tilbyr samme gratis-å-prøve modellkatalog og Azure AI Inferanse SDK / OpenAI SDK-opplevelse.

1. Gå til [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) og opprett (eller åpne) et Foundry-prosjekt.
1. Bla gjennom [modellkatalogen](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) og implementer en modell, for eksempel `gpt-5-mini`.
1. På prosjektets **Oversikt**-side, kopier **endepunktet** og **API-nøkkelen**.
1. Bruk endepunktverdien for `AZURE_INFERENCE_ENDPOINT` og nøkkelverdien for `AZURE_INFERENCE_CREDENTIAL` i din `.env`-fil.

## Offline / Lokale leverandører

Hvis du heller ikke vil bruke en skytjeneste i det hele tatt, kan du kjøre kompatible åpne modeller direkte på din egen enhet:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsofts lokale kjøretidsmiljø. Den velger automatisk den beste kjørings-tilbyderen (NPU, GPU, eller CPU) og eksponerer et OpenAI-kompatibelt endepunkt, slik at du kan gjenbruke mesteparten av eksempelkoden i dette kurset med minimale endringer. Se [Foundry Local-dokumentasjonen](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) for å komme i gang, eller installer med `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - et populært alternativ for å kjøre åpne modeller som Llama, Phi, Mistral og Gemma lokalt.


Se [Leksjon 19: Bygge med SLM-er](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) for praktiske eksempler som bruker begge alternativer.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->