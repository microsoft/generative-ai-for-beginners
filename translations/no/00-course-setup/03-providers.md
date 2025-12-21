<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b5b016b0eb8a1cef2e3097620d8aa23",
  "translation_date": "2025-12-19T15:35:17+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "no"
}
-->
# Valg og konfigurasjon av LLM-leverandør 🔑

Oppgaver **kan** også settes opp til å fungere mot en eller flere distribusjoner av store språkmodeller (LLM) gjennom en støttet tjenesteleverandør som OpenAI, Azure eller Hugging Face. Disse tilbyr et _hostet endepunkt_ (API) som vi kan få tilgang til programmessig med riktige legitimasjoner (API-nøkkel eller token). I dette kurset diskuterer vi disse leverandørene:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) med ulike modeller inkludert kjerne-GPT-serien.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) for OpenAI-modeller med fokus på bedriftsklarhet
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) for åpen kildekode-modeller og inferensserver

**Du må bruke dine egne kontoer for disse øvelsene**. Oppgaver er valgfrie, så du kan velge å sette opp én, alle - eller ingen - av leverandørene basert på dine interesser. Litt veiledning for registrering:

| Registrering | Kostnad | API-nøkkel | Lekemiljø | Kommentarer |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Priser](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Prosjektbasert](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Ingen koding, web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Flere modeller tilgjengelig |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Priser](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Må søke om tilgang på forhånd](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Priser](https://huggingface.co/pricing) | [Tilgangstokener](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat har begrensede modeller](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Følg instruksjonene nedenfor for å _konfigurere_ dette depotet for bruk med forskjellige leverandører. Oppgaver som krever en spesifikk leverandør vil inneholde en av disse taggene i filnavnet:

- `aoai` - krever Azure OpenAI-endepunkt, nøkkel
- `oai` - krever OpenAI-endepunkt, nøkkel
- `hf` - krever Hugging Face-token

Du kan konfigurere én, ingen eller alle leverandører. Relaterte oppgaver vil bare gi feil ved manglende legitimasjon.

## Opprett `.env`-fil

Vi antar at du allerede har lest veiledningen ovenfor, registrert deg hos relevant leverandør, og fått de nødvendige autentiseringslegitimasjonene (API_KEY eller token). I tilfellet Azure OpenAI antar vi også at du har en gyldig distribusjon av en Azure OpenAI-tjeneste (endepunkt) med minst én GPT-modell distribuert for chatfullføring.

Neste steg er å konfigurere dine **lokale miljøvariabler** som følger:

1. Se i rotmappen etter en `.env.copy`-fil som skal ha innhold som dette:

   ```bash
   # OpenAI-leverandør
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Standard er satt!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopier den filen til `.env` med kommandoen nedenfor. Denne filen er _gitignore-t_, og holder hemmeligheter trygge.

   ```bash
   cp .env.copy .env
   ```

3. Fyll inn verdiene (erstatt plassholdere på høyre side av `=`) som beskrevet i neste seksjon.

4. (Valgfritt) Hvis du bruker GitHub Codespaces, har du mulighet til å lagre miljøvariabler som _Codespaces secrets_ knyttet til dette depotet. I så fall trenger du ikke sette opp en lokal .env-fil. **Merk likevel at dette alternativet kun fungerer hvis du bruker GitHub Codespaces.** Du må fortsatt sette opp .env-filen hvis du bruker Docker Desktop i stedet.

## Fyll ut `.env`-filen

La oss ta en rask titt på variabelnavnene for å forstå hva de representerer:

| Variabel  | Beskrivelse  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Dette er brukertilgangstokenet du setter opp i profilen din |
| OPENAI_API_KEY | Dette er autorisasjonsnøkkelen for bruk av tjenesten for ikke-Azure OpenAI-endepunkter |
| AZURE_OPENAI_API_KEY | Dette er autorisasjonsnøkkelen for bruk av den tjenesten |
| AZURE_OPENAI_ENDPOINT | Dette er det distribuerte endepunktet for en Azure OpenAI-ressurs |
| AZURE_OPENAI_DEPLOYMENT | Dette er endepunktet for _tekstgenererings_-modell distribusjon |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Dette er endepunktet for _tekstinnbeddings_-modell distribusjon |
| | |

Merk: De to siste Azure OpenAI-variablene reflekterer en standardmodell for chatfullføring (tekstgenerering) og vektorsøk (innbeddings) henholdsvis. Instruksjoner for å sette disse vil bli definert i relevante oppgaver.

## Konfigurer Azure: Fra portalen

Azure OpenAI-endepunktet og nøkkelverdiene finnes i [Azure-portalen](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), så la oss starte der.

1. Gå til [Azure-portalen](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klikk på **Keys and Endpoint**-valget i sidepanelet (meny til venstre).
1. Klikk **Show Keys** - du skal se følgende: KEY 1, KEY 2 og Endpoint.
1. Bruk verdien for KEY 1 som AZURE_OPENAI_API_KEY
1. Bruk verdien for Endpoint som AZURE_OPENAI_ENDPOINT

Neste trenger vi endepunktene for de spesifikke modellene vi har distribuert.

1. Klikk på **Model deployments**-valget i sidepanelet (venstre meny) for Azure OpenAI-ressursen.
1. På destinasjonssiden klikker du **Manage Deployments**

Dette tar deg til Azure OpenAI Studio-nettstedet, hvor vi finner de andre verdiene som beskrevet nedenfor.

## Konfigurer Azure: Fra Studio

1. Naviger til [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **fra ressursen din** som beskrevet ovenfor.
1. Klikk på **Deployments**-fanen (sidepanel, venstre) for å se modeller som er distribuert nå.
1. Hvis ønsket modell ikke er distribuert, bruk **Create new deployment** for å distribuere den.
1. Du trenger en _tekstgenererings_-modell - vi anbefaler: **gpt-35-turbo**
1. Du trenger en _tekstinnbeddings_-modell - vi anbefaler **text-embedding-ada-002**

Oppdater nå miljøvariablene for å reflektere _Deployment name_ som brukes. Dette vil vanligvis være det samme som modellnavnet med mindre du har endret det eksplisitt. Så, som et eksempel, kan du ha:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Ikke glem å lagre .env-filen når du er ferdig**. Du kan nå lukke filen og gå tilbake til instruksjonene for å kjøre notatboken.

## Konfigurer OpenAI: Fra profil

Din OpenAI API-nøkkel kan finnes i din [OpenAI-konto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Hvis du ikke har en, kan du registrere deg for en konto og opprette en API-nøkkel. Når du har nøkkelen, kan du bruke den til å fylle ut `OPENAI_API_KEY`-variabelen i `.env`-filen.

## Konfigurer Hugging Face: Fra profil

Din Hugging Face-token kan finnes i profilen din under [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Ikke legg ut eller del disse offentlig. Lag i stedet en ny token for dette prosjektet og kopier den inn i `.env`-filen under variabelen `HUGGING_FACE_API_KEY`. _Merk:_ Dette er teknisk sett ikke en API-nøkkel, men brukes til autentisering, så vi beholder denne navngivningskonvensjonen for konsistens.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->