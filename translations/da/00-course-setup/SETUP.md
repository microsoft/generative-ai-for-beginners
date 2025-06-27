<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-06-25T09:21:10+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "da"
}
-->
# Opsæt Dit Udviklingsmiljø

Vi har opsat dette repository og kursus med en [udviklingscontainer](https://containers.dev?WT.mc_id=academic-105485-koreyst), der har en universel runtime, som kan understøtte Python3, .NET, Node.js og Java udvikling. Den tilhørende konfiguration er defineret i filen `devcontainer.json` placeret i mappen `.devcontainer/` ved roden af dette repository.

For at aktivere udviklingscontaineren, start den i [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (for en cloud-hosted runtime) eller i [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (for en lokal enhed-hosted runtime). Læs [denne dokumentation](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) for flere detaljer om, hvordan udviklingscontainere fungerer inden for VS Code.  

> [!TIP]  
> Vi anbefaler at bruge GitHub Codespaces for en hurtig start med minimal indsats. Det giver en generøs [gratis brugskvote](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) for personlige konti. Konfigurer [timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) for at stoppe eller slette inaktive codespaces for at maksimere din kvotebrug.


## 1. Udførelse af Opgaver

Hver lektion vil have _valgfri_ opgaver, der kan leveres i et eller flere programmeringssprog, herunder: Python, .NET/C#, Java og JavaScript/TypeScript. Dette afsnit giver generel vejledning relateret til udførelse af disse opgaver.

### 1.1 Python Opgaver

Python opgaver leveres enten som applikationer (`.py` filer) eller Jupyter notebooks (`.ipynb` filer). 
- For at køre notebooken, åbn den i Visual Studio Code, klik derefter på _Select Kernel_ (øverst til højre) og vælg den viste standard Python 3 mulighed. Du kan nu _Run All_ for at udføre notebooken.
- For at køre Python applikationer fra kommandolinjen, følg opgave-specifikke instruktioner for at sikre, at du vælger de rigtige filer og giver de nødvendige argumenter.

## 2. Konfigurering af Udbydere

Opgaver **kan** også være opsat til at arbejde mod en eller flere Large Language Model (LLM) deploymenter gennem en understøttet tjenesteudbyder som OpenAI, Azure eller Hugging Face. Disse giver en _hosted endpoint_ (API), som vi kan få adgang til programmæssigt med de rigtige legitimationsoplysninger (API nøgle eller token). I dette kursus diskuterer vi disse udbydere:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) med forskellige modeller inklusive kerne GPT-serien.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) for OpenAI modeller med fokus på virksomhedsklarhed.
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) for open-source modeller og inference server.

**Du skal bruge dine egne konti til disse øvelser**. Opgaverne er valgfrie, så du kan vælge at opsætte en, alle - eller ingen - af udbyderne baseret på dine interesser. Nogle vejledninger til tilmelding:

| Tilmelding | Pris | API Nøgle | Playground | Kommentarer |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Pris](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektbaseret](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Flere modeller tilgængelige |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Pris](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Skal ansøge på forhånd for adgang](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Pris](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat har begrænsede modeller](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Følg nedenstående anvisninger for at _konfigurere_ dette repository til brug med forskellige udbydere. Opgaver, der kræver en specifik udbyder, vil indeholde en af disse tags i deres filnavn:
 - `aoai` - kræver Azure OpenAI endpoint, nøgle
 - `oai` - kræver OpenAI endpoint, nøgle
 - `hf` - kræver Hugging Face token

Du kan konfigurere en, ingen eller alle udbydere. Relaterede opgaver vil blot fejle på manglende legitimationsoplysninger.

###  2.1. Opret `.env` fil

Vi antager, at du allerede har læst vejledningen ovenfor og tilmeldt dig den relevante udbyder, og har fået de nødvendige autentificeringsoplysninger (API_KEY eller token). I tilfælde af Azure OpenAI antager vi også, at du har en gyldig deployment af en Azure OpenAI Service (endpoint) med mindst en GPT model implementeret til chat afslutning.

Det næste skridt er at konfigurere dine **lokale miljøvariabler** som følger:


1. Se i rodmappen efter en `.env.copy` fil, der skal have indhold som dette:

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

2. Kopier den fil til `.env` ved hjælp af kommandoen nedenfor. Denne fil er _gitignore-d_, hvilket holder hemmeligheder sikre.

   ```bash
   cp .env.copy .env
   ```

3. Udfyld værdierne (udskift pladsholdere på højre side af `=`) som beskrevet i det næste afsnit.

3. (Option) Hvis du bruger GitHub Codespaces, har du mulighed for at gemme miljøvariabler som _Codespaces secrets_ tilknyttet dette repository. I så fald behøver du ikke opsætte en lokal .env fil. **Bemærk dog, at denne mulighed kun fungerer, hvis du bruger GitHub Codespaces.** Du skal stadig opsætte .env filen, hvis du bruger Docker Desktop i stedet.


### 2.2. Udfyld `.env` fil

Lad os tage et hurtigt kig på variabelnavnene for at forstå, hvad de repræsenterer:

| Variabel  | Beskrivelse  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Dette er brugerens adgangstoken, du opsætter i din profil |
| OPENAI_API_KEY | Dette er autorisationsnøglen til at bruge tjenesten for ikke-Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Dette er autorisationsnøglen til at bruge den tjeneste |
| AZURE_OPENAI_ENDPOINT | Dette er det implementerede endpoint for en Azure OpenAI ressource |
| AZURE_OPENAI_DEPLOYMENT | Dette er _tekstgenererings_ model deployment endpointet |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Dette er _tekst-embeddings_ model deployment endpointet |
| | |

Bemærk: De sidste to Azure OpenAI variabler afspejler en standardmodel for chat afslutning (tekstgenerering) og vektorsøgning (embeddings) henholdsvis. Instruktioner for opsætning af dem vil blive defineret i relevante opgaver.


### 2.3 Konfigurer Azure: Fra Portalen

Azure OpenAI endpoint og nøgleværdierne vil blive fundet i [Azure Portalen](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), så lad os starte der.

1. Gå til [Azure Portalen](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klik på **Keys and Endpoint** muligheden i sidebjælken (menuen til venstre).
1. Klik på **Show Keys** - du skal se følgende: KEY 1, KEY 2 og Endpoint.
1. Brug værdien af KEY 1 for AZURE_OPENAI_API_KEY
1. Brug værdien af Endpoint for AZURE_OPENAI_ENDPOINT

Næste, vi har brug for endpoints for de specifikke modeller, vi har implementeret.

1. Klik på **Model deployments** muligheden i sidebjælken (venstre menu) for Azure OpenAI ressource.
1. På destinationssiden, klik på **Manage Deployments**

Dette vil føre dig til Azure OpenAI Studio hjemmeside, hvor vi vil finde de andre værdier som beskrevet nedenfor.

### 2.4 Konfigurer Azure: Fra Studio

1. Naviger til [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **fra din ressource** som beskrevet ovenfor.
1. Klik på **Deployments** fanen (sidebjælken, venstre) for at se aktuelt implementerede modeller.
1. Hvis din ønskede model ikke er implementeret, brug **Create new deployment** for at implementere den.
1. Du vil have brug for en _tekst-genererings_ model - vi anbefaler: **gpt-35-turbo**
1. Du vil have brug for en _tekst-embedding_ model - vi anbefaler **text-embedding-ada-002**

Opdater nu miljøvariablerne for at afspejle _Deployment name_ brugt. Dette vil typisk være det samme som modelnavnet, medmindre du ændrede det eksplicit. Så, som et eksempel, kunne du have:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Glem ikke at gemme .env filen, når du er færdig**. Du kan nu afslutte filen og vende tilbage til instruktionerne for at køre notebooken.

### 2.5 Konfigurer OpenAI: Fra Profil

Din OpenAI API nøgle kan findes i din [OpenAI konto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Hvis du ikke har en, kan du tilmelde dig en konto og oprette en API nøgle. Når du har nøglen, kan du bruge den til at udfylde `OPENAI_API_KEY` variablen i `.env` filen.

### 2.6 Konfigurer Hugging Face: Fra Profil

Dit Hugging Face token kan findes i din profil under [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Del eller post dem ikke offentligt. I stedet opret et nyt token til dette projektbrug og kopier det ind i `.env` filen under `HUGGING_FACE_API_KEY` variablen. _Bemærk:_ Dette er teknisk set ikke en API nøgle, men bruges til autentificering, så vi holder denne navngivningskonvention for konsistens.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.