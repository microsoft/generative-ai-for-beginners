<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T17:25:00+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "da"
}
-->
# Valg og konfiguration af en LLM-udbyder 🔑

Opgaver **kan** også opsættes til at fungere med en eller flere Large Language Model (LLM) udrulninger via en understøttet tjenesteudbyder som OpenAI, Azure eller Hugging Face. Disse tilbyder et _hostet endpoint_ (API), som vi kan tilgå programmæssigt med de rette legitimationsoplysninger (API-nøgle eller token). I dette kursus gennemgår vi disse udbydere:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) med forskellige modeller, herunder den centrale GPT-serie.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) for OpenAI-modeller med fokus på virksomhedsklarhed
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) for open source-modeller og inferensserver

**Du skal bruge dine egne konti til disse øvelser**. Opgaverne er valgfrie, så du kan vælge at opsætte én, alle – eller ingen – af udbyderne alt efter interesse. Her er lidt vejledning til tilmelding:

| Tilmelding | Pris | API-nøgle | Playground | Kommentarer |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Priser](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektbaseret](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Flere modeller tilgængelige |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Priser](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Adgang skal ansøges på forhånd](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Priser](https://huggingface.co/pricing) | [Adgangstokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat har begrænsede modeller](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Følg vejledningen nedenfor for at _konfigurere_ dette repository til brug med forskellige udbydere. Opgaver, der kræver en bestemt udbyder, vil have et af disse tags i filnavnet:

- `aoai` - kræver Azure OpenAI endpoint og nøgle
- `oai` - kræver OpenAI endpoint og nøgle
- `hf` - kræver Hugging Face token

Du kan konfigurere én, ingen eller alle udbydere. Relaterede opgaver vil blot give fejl, hvis legitimationsoplysninger mangler.

## Opret `.env`-fil

Vi antager, at du allerede har læst vejledningen ovenfor og tilmeldt dig den relevante udbyder samt fået de nødvendige autentificeringsoplysninger (API_KEY eller token). For Azure OpenAI antager vi også, at du har en gyldig udrulning af en Azure OpenAI-tjeneste (endpoint) med mindst én GPT-model udrullet til chat-komplettering.

Næste skridt er at konfigurere dine **lokale miljøvariabler** således:

1. Find i rodmappen en `.env.copy`-fil, som bør indeholde noget i stil med dette:

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

2. Kopiér denne fil til `.env` med kommandoen nedenfor. Denne fil er _gitignore-t_, så hemmeligheder holdes sikre.

   ```bash
   cp .env.copy .env
   ```

3. Udfyld værdierne (erstat pladsholderne til højre for `=`) som beskrevet i næste afsnit.

4. (Valgfrit) Hvis du bruger GitHub Codespaces, har du mulighed for at gemme miljøvariabler som _Codespaces secrets_ tilknyttet dette repository. I så fald behøver du ikke opsætte en lokal .env-fil. **Bemærk dog, at denne mulighed kun virker, hvis du bruger GitHub Codespaces.** Du skal stadig opsætte .env-filen, hvis du bruger Docker Desktop i stedet.

## Udfyld `.env`-filen

Lad os hurtigt gennemgå variabelnavnene for at forstå, hvad de repræsenterer:

| Variabel  | Beskrivelse  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Dette er det adgangstoken, du opsætter i din profil |
| OPENAI_API_KEY | Dette er autorisationsnøglen til brug af tjenesten for ikke-Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Dette er autorisationsnøglen til brug af den tjeneste |
| AZURE_OPENAI_ENDPOINT | Dette er det udrullede endpoint for en Azure OpenAI-ressource |
| AZURE_OPENAI_DEPLOYMENT | Dette er _text generation_-modeludrulnings-endpointet |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Dette er _text embeddings_-modeludrulnings-endpointet |
| | |

Bemærk: De to sidste Azure OpenAI-variabler afspejler en standardmodel til chat-komplettering (tekstgenerering) og vektorsøgning (embeddings) henholdsvis. Instruktioner til opsætning af dem vil fremgå i relevante opgaver.

## Konfigurer Azure: Fra Portal

Azure OpenAI endpoint og nøgleværdier findes i [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), så lad os starte der.

1. Gå til [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klik på **Keys and Endpoint** i sidepanelet (menuen til venstre).
1. Klik på **Show Keys** – du bør nu se: KEY 1, KEY 2 og Endpoint.
1. Brug værdien fra KEY 1 til AZURE_OPENAI_API_KEY
1. Brug værdien fra Endpoint til AZURE_OPENAI_ENDPOINT

Nu skal vi bruge endpoints for de specifikke modeller, vi har udrullet.

1. Klik på **Model deployments** i sidepanelet (venstre menu) for Azure OpenAI-ressourcen.
1. På destinationssiden klikker du på **Manage Deployments**

Dette fører dig til Azure OpenAI Studio-websitet, hvor vi finder de øvrige værdier som beskrevet nedenfor.

## Konfigurer Azure: Fra Studio

1. Gå til [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **fra din ressource** som beskrevet ovenfor.
1. Klik på fanen **Deployments** (sidepanel, venstre) for at se aktuelt udrullede modeller.
1. Hvis din ønskede model ikke er udrullet, brug **Create new deployment** for at udrulle den.
1. Du skal bruge en _text-generation_-model – vi anbefaler: **gpt-35-turbo**
1. Du skal bruge en _text-embedding_-model – vi anbefaler **text-embedding-ada-002**

Opdater nu miljøvariablerne, så de afspejler det _Deployment name_, du har brugt. Dette vil typisk være det samme som modelnavnet, medmindre du har ændret det. For eksempel kan du have:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Husk at gemme .env-filen, når du er færdig**. Du kan nu lukke filen og vende tilbage til instruktionerne for at køre notebooken.

## Konfigurer OpenAI: Fra Profil

Din OpenAI API-nøgle findes i din [OpenAI-konto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Hvis du ikke har en, kan du oprette en konto og lave en API-nøgle. Når du har nøglen, kan du bruge den til at udfylde variablen `OPENAI_API_KEY` i `.env`-filen.

## Konfigurer Hugging Face: Fra Profil

Dit Hugging Face-token findes i din profil under [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Del eller offentliggør ikke disse. Opret i stedet et nyt token til dette projekt og kopier det ind i `.env`-filen under variablen `HUGGING_FACE_API_KEY`. _Bemærk:_ Dette er teknisk set ikke en API-nøgle, men bruges til autentificering, så vi beholder denne navngivning for konsistens.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritiske oplysninger anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå ved brug af denne oversættelse.