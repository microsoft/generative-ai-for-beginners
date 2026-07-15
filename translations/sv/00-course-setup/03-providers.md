# Välja & konfigurera en LLM-leverantör 🔑

Uppgifter **kan** också ställas in för att fungera mot en eller flera stora språkmodellinstallationer (LLM) genom en stödd tjänsteleverantör som OpenAI, Azure eller Hugging Face. Dessa tillhandahåller en _värdbaserad endpoint_ (API) som vi kan nå programmässigt med rätt autentiseringsuppgifter (API-nyckel eller token). I denna kurs diskuterar vi dessa leverantörer:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) med olika modeller inklusive kärnserien GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) för OpenAI-modeller med fokus på företagsberedskap
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) för en enda endpoint och API-nyckel för att komma åt hundratals modeller från OpenAI, Meta, Mistral, Cohere, Microsoft med flera (ersätter GitHub Models, som fasas ut i slutet av juli 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) för öppen källkodmodeller och inferenstjänst
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) eller [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) om du hellre vill köra modeller helt offline på din egen enhet, utan behov av molnabonnemang

**Du behöver använda egna konton för dessa övningar**. Uppgifter är frivilliga så du kan välja att konfigurera en, alla - eller inga - av leverantörerna utifrån ditt intresse. Lite vägledning för registrering:

| Registrering | Kostnad | API-nyckel | Playground | Kommentarer |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Prissättning](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektbaserad](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Kodfri, Webb](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Flera modeller tillgängliga |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Prissättning](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Måste ansöka i förväg för åtkomst](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Prissättning](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Projektöversiktsida](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Gratisnivå tillgänglig; en endpoint + nyckel för många modellleverantörer |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Prissättning](https://huggingface.co/pricing) | [Åtkomsttokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat har begränsade modeller](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Gratis (körs på din enhet) | Ej nödvändig | [Lokal CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Helt offline, OpenAI-kompatibel endpoint |
| | | | | |

Följ instruktionerna nedan för att _konfigurera_ detta arkiv för användning med olika leverantörer. Uppgifter som kräver en specifik leverantör kommer att ha någon av dessa taggar i filnamnet:

- `aoai` - kräver Azure OpenAI endpoint, nyckel
- `oai` - kräver OpenAI endpoint, nyckel
- `hf` - kräver Hugging Face-token
- `githubmodels` - kräver Microsoft Foundry Models endpoint, nyckel (GitHub Models fasas ut i slutet av juli 2026)

Du kan konfigurera en, inga eller alla leverantörer. Relaterade uppgifter kommer helt enkelt att ge fel vid saknade autentiseringsuppgifter.

## Skapa `.env`-fil

Vi antar att du redan har tagit del av vägledningen ovan och registrerat dig hos relevant leverantör, och fått de nödvändiga autentiseringsuppgifterna (API_KEY eller token). I fallet med Azure OpenAI antar vi också att du har en giltig distribution av en Azure OpenAI-tjänst (endpoint) med minst en GPT-modell distribuerad för chattkomplettering.

Nästa steg är att konfigurera dina **lokala miljövariabler** på följande sätt:

1. Leta i rotmappen efter en `.env.copy`-fil som bör ha innehåll som detta:

   ```bash
   # OpenAI-leverantör
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI i Microsoft Foundry
   ## (Azure OpenAI Service är nu en del av Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Standard är inställd! (nuvarande stabila GA API-version)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry-modeller (multi-leverantörsmodellkatalog, ersätter GitHub-modeller, som pensioneras i slutet av juli 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopiera den filen till `.env` med kommandot nedan. Denna fil är _ignorerad av git_ och håller hemligheter säkra.

   ```bash
   cp .env.copy .env
   ```

3. Fyll i värdena (ersätt platshållare till höger om `=`) som beskrivs i nästa avsnitt.

4. (Valfritt) Om du använder GitHub Codespaces kan du spara miljövariabler som _Codespaces-hemligheter_ kopplade till detta arkiv. I så fall behöver du inte konfigurera en lokal .env-fil. **Observera dock att detta alternativ endast fungerar om du använder GitHub Codespaces.** Du måste ändå konfigurera .env-filen om du använder Docker Desktop.

## Fyll i `.env`-filen

Låt oss snabbt titta på variabelnamnen för att förstå vad de representerar:

| Variabel  | Beskrivning  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Detta är användaråtkomsttoken du ställt in i din profil |
| OPENAI_API_KEY | Detta är auktoriseringsnyckeln för att använda tjänsten för icke-Azure OpenAI-endpoints |
| AZURE_OPENAI_API_KEY | Detta är auktoriseringsnyckeln för att använda den tjänsten |
| AZURE_OPENAI_ENDPOINT | Detta är den distribuerade endpointen för en Azure OpenAI-resurs |
| AZURE_OPENAI_DEPLOYMENT | Detta är endpoint för distribution av _textgenererings_ modellen |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Detta är endpoint för distribution av _textembedding_ modellen |
| AZURE_INFERENCE_ENDPOINT | Detta är endpointen för ditt Microsoft Foundry-projekt, används för Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Detta är API-nyckeln för ditt Microsoft Foundry-projekt |
| | |

Obs: De två sista Azure OpenAI-variablerna speglar en standardmodell för chattkomplettering (textgenerering) respektive vektorsökning (embedding). Anvisningar för att ställa in dem kommer att definieras i relevanta uppgifter.

## Konfigurera Azure OpenAI: Från portalen

> **Notera:** Azure OpenAI Service är nu en del av [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Resurser och distributioner syns fortfarande i Azure-portalen, men den dagliga modellhanteringen (distributioner, playground, övervakning) sker nu i Foundry-portalen istället för den gamla fristående "Azure OpenAI Studio".

Azure OpenAI-endpointen och nyckelvärdena hittar du i [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), så vi börjar där.

1. Gå till [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klicka på alternativet **Nycklar och endpoint** i sidomenyn (menyn till vänster).
1. Klicka på **Visa nycklar** - du ska se följande: NYCKEL 1, NYCKEL 2 och Endpoint.
1. Använd värdet för NYCKEL 1 som AZURE_OPENAI_API_KEY
1. Använd endpoint-värdet som AZURE_OPENAI_ENDPOINT

Nästa steg är att få endpoints för modellerna vi har distribuerat.

1. Klicka på alternativet **Modelldistributioner** i sidomenyn (vänstermenyn) för Azure OpenAI-resursen.
1. På destinationssidan klickar du på **Gå till Microsoft Foundry-portalen** (eller **Hantera distributioner**, beroende på resurstyp)

Detta tar dig till Microsoft Foundry-portalen, där vi hittar de andra värdena som beskrivs nedan.

## Konfigurera Azure OpenAI: Från Microsoft Foundry-portalen

1. Navigera till [Microsoft Foundry-portalen](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **från din resurs** som beskrivet ovan.
1. Klicka på fliken **Distributioner** (sidomeny, vänster) för att se de modeller som är distribuerade.
1. Om önskad modell inte är distribuerad, använd **Distribuera modell** för att distribuera den från [modellkatalogen](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Du behöver en _text-genererings_ modell – vi rekommenderar: **gpt-4o-mini**
1. Du behöver en _text-embedding_-modell – vi rekommenderar **text-embedding-3-small**

Uppdatera nu miljövariablerna för att återspegla det _distributionsnamn_ som använts. Detta är typiskt samma som modellnamnet om du inte ändrat det uttryckligen. Så till exempel kan du ha:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Glöm inte att spara .env-filen när du är klar**. Du kan nu stänga filen och återgå till instruktionerna för att köra notebooken.

## Konfigurera OpenAI: Från Profil

Din OpenAI API-nyckel finns i ditt [OpenAI-konto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Om du inte har någon kan du registrera ett konto och skapa en API-nyckel. När du fått nyckeln kan du använda den för att fylla i variabeln `OPENAI_API_KEY` i `.env`-filen.

## Konfigurera Hugging Face: Från Profil

Din Hugging Face-token finns i din profil under [Åtkomsttokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Publicera eller dela inte dessa offentligt. Skapa istället en ny token för detta projekt och kopiera den till `.env`-filen under variabeln `HUGGING_FACE_API_KEY`. _Obs:_ Detta är tekniskt sett inte en API-nyckel men används för autentisering, så vi behåller den namngivningen för konsekvens.

## Konfigurera Microsoft Foundry Models: Från portalen

> **Notera:** GitHub Models fasas ut i slutet av juli 2026. Microsoft Foundry Models är den direkta ersättaren och erbjuder samma gratis att prova modellkatalog och Azure AI Inference SDK / OpenAI SDK-upplevelse.

1. Gå till [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) och skapa (eller öppna) ett Foundry-projekt.
1. Bläddra i [modellkatalogen](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) och distribuera en modell, till exempel `gpt-4o-mini`.
1. På projektets **Översikt**-sida kopierar du **endpoint** och **API-nyckel**.
1. Använd endpoint-värdet för `AZURE_INFERENCE_ENDPOINT` och nyckelvärdet för `AZURE_INFERENCE_CREDENTIAL` i din `.env`-fil.

## Offline / Lokala leverantörer

Om du hellre inte vill använda något molnabonnemang alls kan du köra kompatibla öppna modeller direkt på din egen enhet:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsofts körmiljö på enheten. Den väljer automatiskt den bästa exekveringsleverantören (NPU, GPU eller CPU) och exponerar en OpenAI-kompatibel endpoint, så du kan återanvända majoriteten av exempel-koden i denna kurs med minimala ändringar. Se [Foundry Local-dokumentationen](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) för att komma igång, eller installera med `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - ett populärt alternativ för att köra öppna modeller som Llama, Phi, Mistral och Gemma lokalt.


Se [Lektion 19: Bygga med SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) för praktiska exempel som använder båda alternativen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->