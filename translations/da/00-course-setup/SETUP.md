<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:31:33+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "da"
}
-->
# Opsæt dit udviklingsmiljø

Vi har sat dette repository og kursus op med en [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst), som har et universelt runtime-miljø, der understøtter Python3, .NET, Node.js og Java-udvikling. Den tilhørende konfiguration er defineret i filen `devcontainer.json`, som ligger i `.devcontainer/` mappen i roden af dette repository.

For at aktivere dev containeren, start den i [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (for et cloud-hostet runtime) eller i [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (for et lokalt enhed-hostet runtime). Læs [denne dokumentation](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) for flere detaljer om, hvordan dev containere fungerer i VS Code.

> [!TIP]  
> Vi anbefaler at bruge GitHub Codespaces for en hurtig start med minimal indsats. Det giver en generøs [gratis brugskvote](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) for personlige konti. Konfigurer [timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) til at stoppe eller slette inaktive codespaces for at maksimere din kvoteudnyttelse.

## 1. Udførelse af opgaver

Hver lektion vil have _valgfri_ opgaver, som kan være tilgængelige i et eller flere programmeringssprog, herunder: Python, .NET/C#, Java og JavaScript/TypeScript. Dette afsnit giver generelle retningslinjer for, hvordan du udfører disse opgaver.

### 1.1 Python-opgaver

Python-opgaver leveres enten som applikationer (`.py` filer) eller Jupyter notebooks (`.ipynb` filer).  
- For at køre notebook’en, åbn den i Visual Studio Code, klik derefter på _Select Kernel_ (øverst til højre) og vælg standard Python 3-muligheden. Du kan nu vælge _Run All_ for at køre hele notebook’en.  
- For at køre Python-applikationer fra kommandolinjen, følg de opgavespecifikke instruktioner for at sikre, at du vælger de rigtige filer og angiver nødvendige argumenter.

## 2. Konfigurering af udbydere

Opgaver **kan** også være sat op til at arbejde med en eller flere Large Language Model (LLM) deployment gennem en understøttet serviceudbyder som OpenAI, Azure eller Hugging Face. Disse tilbyder et _hostet endpoint_ (API), som vi kan tilgå programmatisk med de rette legitimationsoplysninger (API-nøgle eller token). I dette kursus gennemgår vi disse udbydere:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) med forskellige modeller, herunder den centrale GPT-serie.  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) for OpenAI-modeller med fokus på enterprise-klarhed  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) for open source-modeller og inference-server

**Du skal bruge dine egne konti til disse øvelser**. Opgaverne er valgfrie, så du kan vælge at sætte én, alle eller ingen af udbyderne op, alt efter dine interesser. Her er lidt vejledning til tilmelding:

| Tilmelding | Pris | API-nøgle | Playground | Kommentarer |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [Priser](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [Projektbaseret](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Flere modeller tilgængelige |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [Priser](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Adgang kræver forudgående ansøgning](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Priser](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Hugging Chat har begrænsede modeller](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Følg nedenstående vejledning for at _konfigurere_ dette repository til brug med forskellige udbydere. Opgaver, der kræver en specifik udbyder, vil indeholde et af disse tags i deres filnavn:  
 - `aoai` - kræver Azure OpenAI endpoint og nøgle  
 - `oai` - kræver OpenAI endpoint og nøgle  
 - `hf` - kræver Hugging Face token

Du kan konfigurere én, ingen eller alle udbydere. Relaterede opgaver vil blot fejle, hvis legitimationsoplysninger mangler.

###  2.1. Opret `.env` fil

Vi antager, at du allerede har læst vejledningen ovenfor, tilmeldt dig den relevante udbyder og fået de nødvendige autentificeringsoplysninger (API_KEY eller token). I tilfælde af Azure OpenAI antager vi også, at du har en gyldig deployment af en Azure OpenAI Service (endpoint) med mindst én GPT-model deployeret til chat completion.

Næste skridt er at konfigurere dine **lokale miljøvariabler** som følger:

1. Kig i rodmappen efter en `.env.copy` fil, som burde indeholde noget i stil med:

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

2. Kopiér denne fil til `.env` med kommandoen nedenfor. Denne fil er _gitignore-d_, så hemmeligheder holdes sikre.

   ```bash
   cp .env.copy .env
   ```

3. Udfyld værdierne (erstat pladsholdere til højre for `=`) som beskrevet i næste afsnit.

3. (Valgfrit) Hvis du bruger GitHub Codespaces, har du mulighed for at gemme miljøvariabler som _Codespaces secrets_ tilknyttet dette repository. I så fald behøver du ikke opsætte en lokal .env-fil. **Bemærk dog, at denne mulighed kun virker, hvis du bruger GitHub Codespaces.** Du skal stadig opsætte .env-filen, hvis du bruger Docker Desktop.

### 2.2. Udfyld `.env` fil

Lad os hurtigt se på variabelnavnene for at forstå, hvad de repræsenterer:

| Variabel  | Beskrivelse  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Dette er brugerens adgangstoken, som du har sat op i din profil |
| OPENAI_API_KEY | Dette er autorisationsnøglen til brug af servicen for ikke-Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Dette er autorisationsnøglen til brug af Azure OpenAI servicen |
| AZURE_OPENAI_ENDPOINT | Dette er det deployerede endpoint for en Azure OpenAI-ressource |
| AZURE_OPENAI_DEPLOYMENT | Dette er deployment endpoint for _tekstgenererings_-modellen |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Dette er deployment endpoint for _tekst-embedding_-modellen |
| | |

Bemærk: De to sidste Azure OpenAI-variabler refererer til en standardmodel for chat completion (tekstgenerering) og vektorsøgning (embeddings) henholdsvis. Instruktioner til opsætning af disse vil være defineret i relevante opgaver.

### 2.3 Konfigurer Azure: Fra portalen

Azure OpenAI endpoint og nøgle findes i [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), så lad os starte der.

1. Gå til [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
1. Klik på **Keys and Endpoint** i sidebaren (menuen til venstre).  
1. Klik på **Show Keys** - du skulle nu se følgende: KEY 1, KEY 2 og Endpoint.  
1. Brug værdien fra KEY 1 til AZURE_OPENAI_API_KEY  
1. Brug værdien fra Endpoint til AZURE_OPENAI_ENDPOINT

Dernæst skal vi finde endpoints for de specifikke modeller, vi har deployeret.

1. Klik på **Model deployments** i sidebaren (venstre menu) for Azure OpenAI-ressourcen.  
1. På destinationssiden klik på **Manage Deployments**

Dette fører dig til Azure OpenAI Studio-websitet, hvor vi finder de øvrige værdier som beskrevet nedenfor.

### 2.4 Konfigurer Azure: Fra Studio

1. Naviger til [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **fra din ressource** som beskrevet ovenfor.  
1. Klik på fanen **Deployments** (sidebar, venstre) for at se de modeller, der er deployeret.  
1. Hvis din ønskede model ikke er deployeret, brug **Create new deployment** til at deployere den.  
1. Du skal bruge en _text-generation_ model – vi anbefaler: **gpt-35-turbo**  
1. Du skal bruge en _text-embedding_ model – vi anbefaler **text-embedding-ada-002**

Opdater nu miljøvariablerne, så de afspejler det _Deployment name_, der er brugt. Det vil typisk være det samme som modelnavnet, medmindre du har ændret det eksplicit. For eksempel kan du have:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Glem ikke at gemme .env-filen, når du er færdig**. Du kan nu lukke filen og vende tilbage til instruktionerne for at køre notebook’en.

### 2.5 Konfigurer OpenAI: Fra profil

Din OpenAI API-nøgle kan findes i din [OpenAI-konto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Hvis du ikke har en, kan du oprette en konto og generere en API-nøgle. Når du har nøglen, kan du bruge den til at udfylde `OPENAI_API_KEY` variablen i `.env` filen.

### 2.6 Konfigurer Hugging Face: Fra profil

Din Hugging Face token kan findes i din profil under [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Del eller offentliggør dem ikke. Opret i stedet en ny token til brug for dette projekt, og kopier den ind i `.env` filen under variablen `HUGGING_FACE_API_KEY`. _Bemærk:_ Dette er teknisk set ikke en API-nøgle, men bruges til autentificering, så vi bevarer denne navngivningskonvention for konsistens.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.