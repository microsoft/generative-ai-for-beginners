<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T17:33:26+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "no"
}
-->
# Velge og konfigurere en LLM-leverandør 🔑

Oppgaver **kan** også settes opp til å fungere mot én eller flere Large Language Model (LLM)-utplasseringer via en støttet tjenesteleverandør som OpenAI, Azure eller Hugging Face. Disse tilbyr et _hostet endepunkt_ (API) som vi kan få tilgang til programmatisk med riktige legitimasjoner (API-nøkkel eller token). I dette kurset diskuterer vi disse leverandørene:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) med ulike modeller, inkludert den sentrale GPT-serien.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) for OpenAI-modeller med fokus på bedriftsbruk
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) for open source-modeller og inferensserver

**Du må bruke dine egne kontoer til disse øvelsene**. Oppgavene er valgfrie, så du kan velge å sette opp én, alle – eller ingen – av leverandørene, avhengig av hva du ønsker. Her er litt veiledning for registrering:

| Registrering | Kostnad | API-nøkkel | Playground | Kommentarer |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Priser](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Prosjektbasert](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Flere modeller tilgjengelig |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Priser](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Må søke om tilgang på forhånd](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Priser](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat har begrensede modeller](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Følg instruksjonene under for å _konfigurere_ dette prosjektet til bruk med ulike leverandører. Oppgaver som krever en spesifikk leverandør vil ha én av disse taggene i filnavnet:

- `aoai` - krever Azure OpenAI-endepunkt og nøkkel
- `oai` - krever OpenAI-endepunkt og nøkkel
- `hf` - krever Hugging Face-token

Du kan konfigurere én, ingen eller alle leverandører. Relaterte oppgaver vil bare feile hvis legitimasjon mangler.

## Opprett `.env`-fil

Vi antar at du allerede har lest veiledningen over, registrert deg hos relevant leverandør, og fått tak i nødvendige autentiseringsdetaljer (API_KEY eller token). For Azure OpenAI antar vi også at du har en gyldig utplassering av Azure OpenAI Service (endepunkt) med minst én GPT-modell utplassert for chat-komplettering.

Neste steg er å konfigurere dine **lokale miljøvariabler** slik:

1. Se i rotmappen etter en `.env.copy`-fil som bør ha innhold som dette:

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

2. Kopier denne filen til `.env` med kommandoen under. Denne filen er _gitignore-t_, så hemmeligheter holdes trygge.

   ```bash
   cp .env.copy .env
   ```

3. Fyll inn verdiene (erstatt plassholdere på høyre side av `=`) som beskrevet i neste seksjon.

4. (Valgfritt) Hvis du bruker GitHub Codespaces, kan du lagre miljøvariabler som _Codespaces secrets_ knyttet til dette prosjektet. Da trenger du ikke sette opp en lokal .env-fil. **Merk at dette kun fungerer hvis du bruker GitHub Codespaces.** Du må fortsatt sette opp .env-filen hvis du bruker Docker Desktop.

## Fyll ut `.env`-filen

La oss se raskt på variabelnavnene for å forstå hva de betyr:

| Variabel  | Beskrivelse  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Dette er brukertokenet du setter opp i profilen din |
| OPENAI_API_KEY | Dette er autorisasjonsnøkkelen for å bruke tjenesten for ikke-Azure OpenAI-endepunkter |
| AZURE_OPENAI_API_KEY | Dette er autorisasjonsnøkkelen for å bruke den tjenesten |
| AZURE_OPENAI_ENDPOINT | Dette er det utplasserte endepunktet for en Azure OpenAI-ressurs |
| AZURE_OPENAI_DEPLOYMENT | Dette er endepunktet for _tekstgenerering_-modellen |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Dette er endepunktet for _tekst-embedding_-modellen |
| | |

Merk: De to siste Azure OpenAI-variablene viser til en standardmodell for chat-komplettering (tekstgenerering) og vektorsøk (embeddings). Instruksjoner for å sette dem opp vil bli gitt i relevante oppgaver.

## Konfigurer Azure: Fra Portal

Azure OpenAI-endepunktet og nøkkelverdiene finner du i [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), så la oss starte der.

1. Gå til [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klikk på **Keys and Endpoint**-valget i sidemenyen (meny til venstre).
1. Klikk **Show Keys** – du skal se følgende: KEY 1, KEY 2 og Endpoint.
1. Bruk verdien fra KEY 1 til AZURE_OPENAI_API_KEY
1. Bruk verdien fra Endpoint til AZURE_OPENAI_ENDPOINT

Neste steg er å finne endepunktene for de spesifikke modellene du har utplassert.

1. Klikk på **Model deployments**-valget i sidemenyen (venstre meny) for Azure OpenAI-ressursen.
1. På siden du kommer til, klikk **Manage Deployments**

Dette tar deg til Azure OpenAI Studio-nettstedet, hvor vi finner de andre verdiene som beskrevet under.

## Konfigurer Azure: Fra Studio

1. Gå til [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **fra ressursen din** som beskrevet over.
1. Klikk på **Deployments**-fanen (sidemeny til venstre) for å se hvilke modeller som er utplassert.
1. Hvis ønsket modell ikke er utplassert, bruk **Create new deployment** for å utplassere den.
1. Du trenger en _tekstgenererings_-modell – vi anbefaler: **gpt-35-turbo**
1. Du trenger en _tekst-embedding_-modell – vi anbefaler **text-embedding-ada-002**

Oppdater nå miljøvariablene til å gjenspeile _Deployment name_ du har brukt. Dette er vanligvis det samme som modellnavnet, med mindre du har endret det. For eksempel kan du ha:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Husk å lagre .env-filen når du er ferdig**. Du kan nå lukke filen og gå tilbake til instruksjonene for å kjøre notebooken.

## Konfigurer OpenAI: Fra Profil

Din OpenAI API-nøkkel finner du i din [OpenAI-konto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Hvis du ikke har en, kan du registrere deg og opprette en API-nøkkel. Når du har nøkkelen, kan du bruke den til å fylle ut `OPENAI_API_KEY`-variabelen i `.env`-filen.

## Konfigurer Hugging Face: Fra Profil

Din Hugging Face-token finner du i profilen din under [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Ikke del eller publiser disse offentlig. Opprett heller en ny token for dette prosjektet og kopier den inn i `.env`-filen under variabelen `HUGGING_FACE_API_KEY`. _Merk:_ Dette er teknisk sett ikke en API-nøkkel, men brukes til autentisering, så vi beholder navngivningen for konsistens.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.