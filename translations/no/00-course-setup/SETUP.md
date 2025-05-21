<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T12:51:20+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "no"
}
-->
# Sett opp utviklingsmiljøet ditt

Vi har satt opp dette repositoriet og kurset med en [utviklingscontainer](https://containers.dev?WT.mc_id=academic-105485-koreyst) som har en universell runtime som kan støtte Python3, .NET, Node.js og Java-utvikling. Den relaterte konfigurasjonen er definert i `devcontainer.json`-filen som ligger i `.devcontainer/`-mappen ved roten av dette repositoriet.

For å aktivere utviklingscontaineren, start den i [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (for en skybasert runtime) eller i [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (for en lokal enhet-hostet runtime). Les [denne dokumentasjonen](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) for mer detaljer om hvordan utviklingscontainere fungerer innenfor VS Code.

> [!TIP]  
> Vi anbefaler å bruke GitHub Codespaces for en rask start med minimal innsats. Det gir en generøs [gratis bruksgrense](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) for personlige kontoer. Konfigurer [timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) for å stoppe eller slette inaktive codespaces for å maksimere bruken av kvoten din.

## 1. Utføre oppgaver

Hver leksjon vil ha _valgfrie_ oppgaver som kan bli gitt i en eller flere programmeringsspråk inkludert: Python, .NET/C#, Java og JavaScript/TypeScript. Denne delen gir generell veiledning relatert til utførelsen av disse oppgavene.

### 1.1 Python-oppgaver

Python-oppgaver er gitt enten som applikasjoner (`.py`-filer) eller Jupyter-notatbøker (`.ipynb`-filer). 
- For å kjøre notatboken, åpne den i Visual Studio Code, klikk deretter _Select Kernel_ (øverst til høyre) og velg standard Python 3-alternativet som vises. Du kan nå _Run All_ for å utføre notatboken.
- For å kjøre Python-applikasjoner fra kommandolinjen, følg oppgave-spesifikke instruksjoner for å sikre at du velger de riktige filene og gir nødvendige argumenter.

## 2. Konfigurere leverandører

Oppgaver **kan** også være satt opp til å fungere mot en eller flere Large Language Model (LLM)-utplasseringer gjennom en støttet tjenesteleverandør som OpenAI, Azure eller Hugging Face. Disse gir et _hostet endepunkt_ (API) som vi kan få tilgang til programmessig med de riktige legitimasjonene (API-nøkkel eller token). I dette kurset diskuterer vi disse leverandørene:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) med diverse modeller inkludert kjerneserien GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) for OpenAI-modeller med fokus på bedriftsklarhet
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) for open-source modeller og inference server

**Du må bruke dine egne kontoer for disse øvelsene**. Oppgaver er valgfrie, så du kan velge å sette opp én, alle - eller ingen - av leverandørene basert på dine interesser. Noen veiledning for registrering:

| Registrering | Kostnad | API-nøkkel | Lekeplass | Kommentarer |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Priser](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Prosjektbasert](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Flere modeller tilgjengelig |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Priser](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Må søke i forkant for tilgang](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Priser](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat har begrensede modeller](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Følg instruksjonene nedenfor for å _konfigurere_ dette repositoriet for bruk med forskjellige leverandører. Oppgaver som krever en spesifikk leverandør vil inneholde en av disse taggene i filnavnet:
 - `aoai` - krever Azure OpenAI endepunkt, nøkkel
 - `oai` - krever OpenAI endepunkt, nøkkel
 - `hf` - krever Hugging Face token

Du kan konfigurere én, ingen, eller alle leverandører. Relaterte oppgaver vil bare feile på manglende legitimasjon.

###  2.1. Opprett `.env`-fil

Vi antar at du allerede har lest veiledningen ovenfor og registrert deg hos den relevante leverandøren, og fått de nødvendige autentiseringslegitimasjonene (API_KEY eller token). I tilfelle Azure OpenAI, antar vi at du også har en gyldig utplassering av en Azure OpenAI-tjeneste (endepunkt) med minst én GPT-modell utplassert for chat-komplettering.

Neste steg er å konfigurere dine **lokale miljøvariabler** som følger:


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

2. Kopier den filen til `.env` ved å bruke kommandoen nedenfor. Denne filen er _gitignore-d_, holder hemmeligheter trygge.

   ```bash
   cp .env.copy .env
   ```

3. Fyll inn verdiene (erstatt plassholdere på høyre side av `=`) som beskrevet i neste seksjon.

3. (Valg) Hvis du bruker GitHub Codespaces, har du muligheten til å lagre miljøvariabler som _Codespaces secrets_ knyttet til dette repositoriet. I så fall trenger du ikke å sette opp en lokal .env-fil. **Men merk at dette alternativet bare fungerer hvis du bruker GitHub Codespaces.** Du vil fortsatt måtte sette opp .env-filen hvis du bruker Docker Desktop i stedet.

### 2.2. Fyll inn `.env`-filen

La oss ta en rask titt på variabelnavnene for å forstå hva de representerer:

| Variabel  | Beskrivelse  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Dette er brukerens tilgangstoken du satte opp i profilen din |
| OPENAI_API_KEY | Dette er autorisasjonsnøkkelen for bruk av tjenesten for ikke-Azure OpenAI endepunkter |
| AZURE_OPENAI_API_KEY | Dette er autorisasjonsnøkkelen for bruk av den tjenesten |
| AZURE_OPENAI_ENDPOINT | Dette er det utplasserte endepunktet for en Azure OpenAI ressurs |
| AZURE_OPENAI_DEPLOYMENT | Dette er _tekstgenerering_ modell utplassering endepunktet |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Dette er _tekst-embedding_ modell utplassering endepunktet |
| | |

Merk: De siste to Azure OpenAI-variablene reflekterer en standardmodell for chat-komplettering (tekstgenerering) og vektorsøk (embedding) henholdsvis. Instruksjoner for å sette dem vil bli definert i relevante oppgaver.

### 2.3 Konfigurer Azure: Fra Portal

Azure OpenAI endepunkt og nøkkelverdier vil bli funnet i [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) så la oss starte der.

1. Gå til [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klikk på **Keys and Endpoint**-alternativet i sidepanelet (menyen til venstre).
1. Klikk på **Show Keys** - du bør se følgende: KEY 1, KEY 2 og Endpoint.
1. Bruk verdien KEY 1 for AZURE_OPENAI_API_KEY
1. Bruk endepunktverdien for AZURE_OPENAI_ENDPOINT

Neste, trenger vi endepunktene for de spesifikke modellene vi har utplassert.

1. Klikk på **Model deployments**-alternativet i sidepanelet (venstre meny) for Azure OpenAI ressurs.
1. På destinasjonssiden, klikk **Manage Deployments**

Dette vil ta deg til Azure OpenAI Studio-nettstedet, hvor vi finner de andre verdiene som beskrevet nedenfor.

### 2.4 Konfigurer Azure: Fra Studio

1. Naviger til [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **fra ressursen din** som beskrevet ovenfor.
1. Klikk på **Deployments**-fanen (sidepanelet, venstre) for å se nåværende utplasserte modeller.
1. Hvis din ønskede modell ikke er utplassert, bruk **Create new deployment** for å utplassere den.
1. Du vil trenge en _tekst-generering_ modell - vi anbefaler: **gpt-35-turbo**
1. Du vil trenge en _tekst-embedding_ modell - vi anbefaler **text-embedding-ada-002**

Oppdater nå miljøvariablene for å reflektere _Deployment name_ brukt. Dette vil typisk være det samme som modellnavnet med mindre du endret det eksplisitt. Så, som et eksempel, kan du ha:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Ikke glem å lagre .env-filen når du er ferdig**. Du kan nå avslutte filen og returnere til instruksjonene for å kjøre notatboken.

### 2.5 Konfigurer OpenAI: Fra Profil

Din OpenAI API-nøkkel kan bli funnet i din [OpenAI-konto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Hvis du ikke har en, kan du registrere deg for en konto og opprette en API-nøkkel. Når du har nøkkelen, kan du bruke den til å fylle inn `OPENAI_API_KEY`-variabelen i `.env`-filen.

### 2.6 Konfigurer Hugging Face: Fra Profil

Din Hugging Face token kan bli funnet i profilen din under [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Ikke legg ut eller del disse offentlig. I stedet, opprett et nytt token for dette prosjektet og kopier det inn i `.env`-filen under `HUGGING_FACE_API_KEY`-variabelen. _Merk:_ Dette er teknisk sett ikke en API-nøkkel, men brukes til autentisering, så vi holder den navnekonvensjonen for konsistens.

**Ansvarsfraskrivelse**:  
Dette dokumentet har blitt oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Vi streber etter nøyaktighet, men vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.