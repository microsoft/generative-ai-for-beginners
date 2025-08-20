<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:31:55+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "no"
}
-->
# Sett opp utviklingsmiljøet ditt

Vi har satt opp dette depotet og kurset med en [utviklingscontainer](https://containers.dev?WT.mc_id=academic-105485-koreyst) som har en universell runtime som støtter utvikling i Python3, .NET, Node.js og Java. Den tilhørende konfigurasjonen er definert i `devcontainer.json`-filen som ligger i `.devcontainer/`-mappen i roten av dette depotet.

For å aktivere utviklingscontaineren, start den i [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (for en skybasert runtime) eller i [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (for en lokal runtime på enheten din). Les [denne dokumentasjonen](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) for mer informasjon om hvordan utviklingscontainere fungerer i VS Code.

> [!TIP]  
> Vi anbefaler å bruke GitHub Codespaces for en rask start med minimal innsats. Det gir en generøs [gratis kvote](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) for personlige kontoer. Konfigurer [tidsavbrudd](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) for å stoppe eller slette inaktive codespaces for å maksimere bruken av kvoten din.

## 1. Kjøre oppgaver

Hver leksjon vil ha _valgfri_ oppgaver som kan tilbys i ett eller flere programmeringsspråk, inkludert: Python, .NET/C#, Java og JavaScript/TypeScript. Denne seksjonen gir generell veiledning for hvordan du kan kjøre disse oppgavene.

### 1.1 Python-oppgaver

Python-oppgaver leveres enten som applikasjoner (`.py`-filer) eller Jupyter-notatbøker (`.ipynb`-filer).  
- For å kjøre notatboken, åpne den i Visual Studio Code, klikk deretter på _Select Kernel_ (øverst til høyre) og velg standard Python 3-alternativet som vises. Du kan nå velge _Run All_ for å kjøre hele notatboken.  
- For å kjøre Python-applikasjoner fra kommandolinjen, følg oppgavespesifikke instruksjoner for å sikre at du velger riktige filer og oppgir nødvendige argumenter.

## 2. Konfigurere leverandører

Oppgaver **kan** også være satt opp til å fungere mot én eller flere distribusjoner av store språkmodeller (LLM) gjennom en støttet tjenesteleverandør som OpenAI, Azure eller Hugging Face. Disse tilbyr et _hostet endepunkt_ (API) som vi kan få tilgang til programmatisk med riktige legitimasjoner (API-nøkkel eller token). I dette kurset diskuterer vi disse leverandørene:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) med ulike modeller, inkludert kjerne-GPT-serien.  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) for OpenAI-modeller med fokus på bedriftsklarhet  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) for open source-modeller og inferensserver

**Du må bruke dine egne kontoer for disse øvelsene**. Oppgavene er valgfrie, så du kan velge å sette opp én, alle eller ingen av leverandørene basert på dine interesser. Litt veiledning for registrering:

| Registrering | Kostnad | API-nøkkel | Playground | Kommentarer |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [Priser](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [Prosjektbasert](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Flere modeller tilgjengelig |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [Priser](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Må søke om tilgang på forhånd](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Priser](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Hugging Chat har begrensede modeller](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Følg instruksjonene nedenfor for å _konfigurere_ dette depotet for bruk med ulike leverandører. Oppgaver som krever en spesifikk leverandør vil ha en av disse taggene i filnavnet:  
 - `aoai` - krever Azure OpenAI-endepunkt og nøkkel  
 - `oai` - krever OpenAI-endepunkt og nøkkel  
 - `hf` - krever Hugging Face-token

Du kan konfigurere én, ingen eller alle leverandører. Oppgaver som krever en leverandør uten riktige legitimasjoner vil gi feilmelding.

###  2.1. Opprett `.env`-fil

Vi antar at du allerede har lest veiledningen ovenfor, registrert deg hos relevant leverandør, og fått nødvendige autentiseringsopplysninger (API_KEY eller token). I tilfellet Azure OpenAI antar vi også at du har en gyldig distribusjon av en Azure OpenAI-tjeneste (endepunkt) med minst én GPT-modell distribuert for chat fullføring.

Neste steg er å konfigurere dine **lokale miljøvariabler** som følger:

1. Se i rotmappen etter en `.env.copy`-fil som skal inneholde noe slikt:

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

2. Kopier denne filen til `.env` med kommandoen nedenfor. Denne filen er _gitignore-d_, slik at hemmeligheter holdes trygge.

   ```bash
   cp .env.copy .env
   ```

3. Fyll inn verdiene (erstatt plassholdere på høyre side av `=`) som beskrevet i neste seksjon.

3. (Valgfritt) Hvis du bruker GitHub Codespaces, kan du lagre miljøvariabler som _Codespaces secrets_ knyttet til dette depotet. I så fall trenger du ikke sette opp en lokal .env-fil. **Merk at dette kun fungerer hvis du bruker GitHub Codespaces.** Du må fortsatt sette opp .env-filen hvis du bruker Docker Desktop.

### 2.2. Fyll ut `.env`-filen

La oss ta en rask titt på variabelnavnene for å forstå hva de representerer:

| Variabel  | Beskrivelse  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Dette er brukertokenet du har satt opp i profilen din |
| OPENAI_API_KEY | Dette er autorisasjonsnøkkelen for bruk av tjenesten for ikke-Azure OpenAI-endepunkter |
| AZURE_OPENAI_API_KEY | Dette er autorisasjonsnøkkelen for bruk av den tjenesten |
| AZURE_OPENAI_ENDPOINT | Dette er det distribuerte endepunktet for en Azure OpenAI-ressurs |
| AZURE_OPENAI_DEPLOYMENT | Dette er endepunktet for _tekstgenererings_-modellens distribusjon |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Dette er endepunktet for _tekst-embedding_-modellens distribusjon |
| | |

Merk: De to siste Azure OpenAI-variablene representerer en standardmodell for henholdsvis chat fullføring (tekstgenerering) og vektorsøk (embedding). Instruksjoner for å sette disse vil bli gitt i relevante oppgaver.

### 2.3 Konfigurer Azure: Fra portalen

Verdiene for Azure OpenAI-endepunkt og nøkkel finner du i [Azure-portalen](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), så la oss starte der.

1. Gå til [Azure-portalen](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
1. Klikk på **Keys and Endpoint** i sidemenyen (meny til venstre).  
1. Klikk på **Show Keys** – du skal se følgende: KEY 1, KEY 2 og Endpoint.  
1. Bruk verdien for KEY 1 som AZURE_OPENAI_API_KEY  
1. Bruk verdien for Endpoint som AZURE_OPENAI_ENDPOINT

Neste steg er å finne endepunktene for de spesifikke modellene vi har distribuert.

1. Klikk på **Model deployments** i sidemenyen (venstre meny) for Azure OpenAI-ressursen.  
1. På destinasjonssiden klikker du på **Manage Deployments**

Dette tar deg til Azure OpenAI Studio-nettstedet, hvor vi finner de andre verdiene som beskrevet nedenfor.

### 2.4 Konfigurer Azure: Fra Studio

1. Naviger til [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **fra ressursen din** som beskrevet ovenfor.  
1. Klikk på fanen **Deployments** (sidemeny, venstre) for å se modeller som er distribuert.  
1. Hvis ønsket modell ikke er distribuert, bruk **Create new deployment** for å distribuere den.  
1. Du trenger en _tekstgenererings_-modell – vi anbefaler: **gpt-35-turbo**  
1. Du trenger en _tekst-embedding_-modell – vi anbefaler **text-embedding-ada-002**

Oppdater nå miljøvariablene for å reflektere _Deployment name_ som brukes. Dette vil vanligvis være det samme som modellnavnet med mindre du har endret det eksplisitt. For eksempel kan du ha:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Ikke glem å lagre .env-filen når du er ferdig**. Du kan nå lukke filen og gå tilbake til instruksjonene for å kjøre notatboken.

### 2.5 Konfigurer OpenAI: Fra profil

Din OpenAI API-nøkkel finner du i din [OpenAI-konto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Hvis du ikke har en, kan du registrere deg for en konto og opprette en API-nøkkel. Når du har nøkkelen, kan du bruke den til å fylle ut `OPENAI_API_KEY`-variabelen i `.env`-filen.

### 2.6 Konfigurer Hugging Face: Fra profil

Din Hugging Face-token finner du i profilen din under [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Ikke del eller publiser disse offentlig. Lag i stedet en ny token for bruk i dette prosjektet og kopier den inn i `.env`-filen under variabelen `HUGGING_FACE_API_KEY`. _Merk:_ Dette er teknisk sett ikke en API-nøkkel, men brukes til autentisering, så vi beholder denne navngivningen for konsistens.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.