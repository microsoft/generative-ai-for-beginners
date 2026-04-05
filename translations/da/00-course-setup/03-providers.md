# Valg & Konfiguration af en LLM-udbyder 🔑

Opgaver **kan** også sættes op til at arbejde mod en eller flere Large Language Model (LLM) implementeringer gennem en understøttet serviceudbyder som OpenAI, Azure eller Hugging Face. Disse leverer et _hostet endpoint_ (API), som vi kan tilgå programmatisk med de rette legitimationsoplysninger (API-nøgle eller token). I dette kursus diskuterer vi disse udbydere:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) med forskellige modeller inklusive den centrale GPT-serie.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) for OpenAI-modeller med fokus på virksomhedsklarhed
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) for open source-modeller og inferensserver

**Du skal bruge dine egne konti til disse øvelser**. Opgaver er valgfrie, så du kan vælge at sætte en, alle - eller ingen - af udbyderne op baseret på dine interesser. Her er lidt vejledning til tilmelding:

| Tilmelding | Pris | API-nøgle | Playground | Kommentarer |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Priser](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektbaseret](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Flere modeller tilgængelige |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Priser](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Skal ansøges om adgang på forhånd](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Priser](https://huggingface.co/pricing) | [Adgangstokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat har begrænsede modeller](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Følg nedenstående anvisninger for at _konfigurere_ dette repository til brug med forskellige udbydere. Opgaver, der kræver en specifik udbyder, vil indeholde et af disse tags i deres filnavn:

- `aoai` - kræver Azure OpenAI endpoint, nøgle
- `oai` - kræver OpenAI endpoint, nøgle
- `hf` - kræver Hugging Face token

Du kan konfigurere en, ingen eller alle udbydere. Relaterede opgaver vil blot give fejl ved manglende legitimationsoplysninger.

## Opret `.env` fil

Vi antager, at du allerede har læst vejledningen ovenfor og tilmeldt dig den relevante udbyder, og fået de nødvendige autentificeringsoplysninger (API_KEY eller token). I tilfælde af Azure OpenAI antager vi også, at du har en gyldig implementering af en Azure OpenAI Service (endpoint) med mindst én GPT-model implementeret til chat completion.

Næste skridt er at konfigurere dine **lokale miljøvariabler** som følger:

1. Kig i rodmappen efter en `.env.copy` fil, som bør have indhold som dette:

   ```bash
   # OpenAI Udbyder
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Standard er sat!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopiér den fil til `.env` med kommandoen nedenfor. Denne fil er _gitignore-d_, så hemmeligheder holdes sikre.

   ```bash
   cp .env.copy .env
   ```

3. Udfyld værdierne (erstat pladsholdere til højre for `=`) som beskrevet i næste afsnit.

4. (Valgfrit) Hvis du bruger GitHub Codespaces, har du mulighed for at gemme miljøvariabler som _Codespaces secrets_ tilknyttet dette repository. I så fald behøver du ikke sætte en lokal .env fil op. **Bemærk dog, at denne mulighed kun virker, hvis du bruger GitHub Codespaces.** Du skal stadig sætte .env filen op, hvis du bruger Docker Desktop i stedet.

## Udfyld `.env` fil

Lad os hurtigt se på variabelnavnene for at forstå, hvad de repræsenterer:

| Variabel  | Beskrivelse  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Dette er brugerens adgangstoken, som du har sat op i din profil |
| OPENAI_API_KEY | Dette er autorisationsnøglen til brug af tjenesten for ikke-Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Dette er autorisationsnøglen til brug af den tjeneste |
| AZURE_OPENAI_ENDPOINT | Dette er det implementerede endpoint for en Azure OpenAI-ressource |
| AZURE_OPENAI_DEPLOYMENT | Dette er _tekstgenererings_-modelimplementerings-endpointet |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Dette er _tekstindlejrings_-modelimplementerings-endpointet |
| | |

Bemærk: De sidste to Azure OpenAI variabler afspejler en standardmodel til chat completion (tekstgenerering) og vektorsøgning (indlejringer) henholdsvis. Instruktioner til opsætning af dem vil blive defineret i relevante opgaver.

## Konfigurer Azure: Fra Portal

Azure OpenAI endpoint og nøgleværdier findes i [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), så lad os starte der.

1. Gå til [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klik på **Keys and Endpoint** valgmuligheden i sidebaren (menu til venstre).
1. Klik på **Show Keys** - du bør se følgende: KEY 1, KEY 2 og Endpoint.
1. Brug værdien for KEY 1 til AZURE_OPENAI_API_KEY
1. Brug Endpoint værdien til AZURE_OPENAI_ENDPOINT

Dernæst skal vi bruge endpoints for de specifikke modeller, vi har implementeret.

1. Klik på **Model deployments** valgmuligheden i sidebaren (venstre menu) for Azure OpenAI ressourcen.
1. På destinationssiden klik på **Manage Deployments**

Dette tager dig til Azure OpenAI Studio-websitet, hvor vi finder de andre værdier som beskrevet nedenfor.

## Konfigurer Azure: Fra Studio

1. Naviger til [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **fra din ressource** som beskrevet ovenfor.
1. Klik på fanen **Deployments** (sidebar, venstre) for at se de aktuelt implementerede modeller.
1. Hvis din ønskede model ikke er implementeret, brug **Create new deployment** til at implementere den.
1. Du skal bruge en _text-generation_ model - vi anbefaler: **gpt-35-turbo**
1. Du skal bruge en _text-embedding_ model - vi anbefaler **text-embedding-ada-002**

Opdater nu miljøvariablerne til at afspejle det _Deployment name_, der bruges. Dette vil typisk være det samme som modelnavnet, medmindre du har ændret det eksplicit. Så som eksempel kan du have:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Glem ikke at gemme .env filen, når du er færdig**. Du kan nu lukke filen og vende tilbage til instruktionerne for at køre notebooken.

## Konfigurer OpenAI: Fra Profil

Din OpenAI API-nøgle kan findes i din [OpenAI-konto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Hvis du ikke har en, kan du tilmelde dig en konto og oprette en API-nøgle. Når du har nøglen, kan du bruge den til at udfylde `OPENAI_API_KEY` variablen i `.env` filen.

## Konfigurer Hugging Face: Fra Profil

Din Hugging Face token kan findes i din profil under [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Del eller offentliggør dem ikke. Opret i stedet en ny token til dette projekt og kopier den ind i `.env` filen under variablen `HUGGING_FACE_API_KEY`. _Bemærk:_ Dette er teknisk set ikke en API-nøgle, men bruges til autentificering, så vi bevarer denne navngivningskonvention for konsistens.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->