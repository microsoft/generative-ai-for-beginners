# Välja & Konfigurera en LLM-leverantör 🔑

Uppgifter **kan** också ställas in för att arbeta mot en eller flera stora språkmodellsimplementationer (LLM) via en stödd tjänsteleverantör som OpenAI, Azure eller Hugging Face. Dessa tillhandahåller en _hostad endpoint_ (API) som vi kan komma åt programmässigt med rätt autentiseringsuppgifter (API-nyckel eller token). I denna kurs diskuterar vi dessa leverantörer:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) med olika modeller inklusive kärnserien GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) för OpenAI-modeller med fokus på företagsanpassning
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) för en enda endpoint och API-nyckel för att nå hundratals modeller från OpenAI, Meta, Mistral, Cohere, Microsoft med flera (ersätter GitHub Models som pensioneras i slutet av juli 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) för öppen källkod-modeller och inferensserver
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) eller [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) om du hellre vill köra modeller helt offline på din egen enhet, utan något molnabonnemang

**Du behöver använda egna konton för dessa övningar**. Uppgifterna är frivilliga så du kan välja att konfigurera en, alla - eller inga - av leverantörerna baserat på dina intressen. Lite vägledning för registrering:

| Registrera | Kostnad | API-nyckel | Lekplats | Kommentarer |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Prissättning](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektbaserad](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Ingen kod, Webb](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Flera modeller tillgängliga |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Prissättning](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Snabbstart](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Snabbstart](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Måste ansöka i förväg för åtkomst](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Prissättning](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Projektöversikt](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Lekplats](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Gratisnivå tillgänglig; en endpoint + nyckel för många modellleverantörer |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Prissättning](https://huggingface.co/pricing) | [Åtkomsttoken](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat har begränsade modeller](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Gratis (kör på din enhet) | Ej nödvändig | [Lokal CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Helt offline, OpenAI-kompatibel endpoint |
| | | | | |

Följ anvisningarna nedan för att _konfigurera_ detta repo för användning med olika leverantörer. Uppgifter som kräver en specifik leverantör kommer att innehålla en av dessa taggar i filnamnet:

- `aoai` - kräver Azure OpenAI endpoint, nyckel
- `oai` - kräver OpenAI endpoint, nyckel
- `hf` - kräver Hugging Face token
- `githubmodels` - kräver Microsoft Foundry Models endpoint, nyckel (GitHub Models pensioneras i slutet av juli 2026)

Du kan konfigurera en, inga eller alla leverantörer. Relaterade uppgifter kommer helt enkelt att ge fel om autentiseringsuppgifter saknas.

## Skapa `.env`-fil

Vi utgår från att du redan läst vägledningen ovan och registrerat dig hos relevant leverantör, samt fått erforderliga autentiseringsuppgifter (API_KEY eller token). I fallet Azure OpenAI antar vi även att du har en giltig deployment av Azure OpenAI Service (endpoint) med minst en GPT-modell distribuerad för chat-komplettering.

Nästa steg är att configurera dina **lokala miljövariabler** enligt nedan:

1. Titta i rotmappen efter en fil `.env.copy` som bör innehålla något i stil med detta:

   ```bash
   # OpenAI-leverantör
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI i Microsoft Foundry
   ## (Azure OpenAI-tjänsten är nu en del av Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Standard är inställd! (nuvarande stabila GA API-version)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry-modeller (flerleverantörs modellkatalog, ersätter GitHub-modeller, som pensioneras i slutet av juli 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopiera den filen till `.env` med kommandot nedan. Den här filen är _gitignore:ad_, för att hålla hemligheter säkra.

   ```bash
   cp .env.copy .env
   ```

3. Fyll i värdena (ersätt platshållare till höger om `=`) enligt beskrivningen i nästa avsnitt.

4. (Valfritt) Om du använder GitHub Codespaces har du möjlighet att spara miljövariabler som _Codespaces-hemligheter_ kopplade till detta repo. I det fallet behöver du inte konfigurera en lokal .env-fil. **Observera dock att detta alternativ endast fungerar om du använder GitHub Codespaces.** Du behöver fortfarande konfigurera .env-filen om du använder Docker Desktop istället.

## Fyll i `.env`-filen

Låt oss ta en snabb titt på variabelnamnen för att förstå vad de representerar:

| Variabel  | Beskrivning  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Detta är användaråtkomsttoken som du ställer in i din profil |
| OPENAI_API_KEY | Detta är auktorisationsnyckeln för att använda tjänsten för icke-Azure OpenAI-endpoints |
| AZURE_OPENAI_API_KEY | Detta är auktorisationsnyckeln för att använda den tjänsten |
| AZURE_OPENAI_ENDPOINT | Detta är den deployade endpointen för en Azure OpenAI-resurs |
| AZURE_OPENAI_DEPLOYMENT | Detta är endpointen för _textgenererings_ modellens deployment |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Detta är endpointen för _text embeddings_ modellens deployment |
| AZURE_INFERENCE_ENDPOINT | Detta är endpointen för ditt Microsoft Foundry-projekt, använt för Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Detta är API-nyckeln för ditt Microsoft Foundry-projekt |
| | |

Obs: De två sista Azure OpenAI variablerna avser som standardmodell för chat-komplettering (textgenerering) respektive vektorsökning (embeddings). Instruktioner för att ställa in dessa definieras i relevanta uppgifter.

## Konfigurera Azure OpenAI: Från Portal

> **OBS:** Azure OpenAI Service ingår numera i [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Resurser och deployment visas fortfarande i Azure Portal, men modellhantering i vardagen (deployment, lekplats, övervakning) sker numera i Foundry-portalen istället för den gamla fristående "Azure OpenAI Studio".

Azure OpenAI endpoint och nyckelvärden finns i [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) så låt oss börja där.

1. Gå till [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klicka på **Keys and Endpoint** i sidomenyn (menyn till vänster).
1. Klicka på **Visa nycklar** - du bör se följande: KEY 1, KEY 2 och Endpoint.
1. Använd värdet för KEY 1 för AZURE_OPENAI_API_KEY
1. Använd värdet Endpoint för AZURE_OPENAI_ENDPOINT

Nästa steg är att få endpointsen för de specifika modeller vi distribuerat.

1. Klicka på **Model deployments** i sidomenyn (vänstermenyn) för Azure OpenAI-resursen.
1. På sidan som öppnas, klicka på **Gå till Microsoft Foundry-portalen** (eller **Hantera deployment**, beroende på din resurstyp)

Detta tar dig till Microsoft Foundry-portalen där vi hittar de andra värdena som beskrivs nedan.

## Konfigurera Azure OpenAI: Från Microsoft Foundry-portalen

1. Navigera till [Microsoft Foundry-portalen](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **från din resurs** som beskrivet ovan.
1. Klicka på fliken **Deployments** (sidomeny, vänster) för att se nuvarande distribuerade modeller.
1. Om din önskade modell inte är distribuerad, använd **Deploy model** för att distribuera den från [modellkatalogen](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Du behöver en _textgenererings_ modell – vi rekommenderar: **gpt-5-mini**
1. Du behöver en _text-embedding_ modell – vi rekommenderar **text-embedding-3-small**

Uppdatera nu miljövariablerna för att återspegla det _Deployment name_ som används. Detta är oftast samma som modellnamnet om du inte ändrat det uttryckligen. Som ett exempel kan du ha:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Glöm inte att spara .env-filen när du är klar**. Du kan nu stänga filen och återgå till instruktionerna för att köra notebooken.

## Konfigurera OpenAI: Från Profil

Din OpenAI API-nyckel finns i ditt [OpenAI-konto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Om du inte har en kan du registrera ett konto och skapa en API-nyckel. När du har nyckeln kan du använda den för att fylla i variabeln `OPENAI_API_KEY` i `.env`-filen.

## Konfigurera Hugging Face: Från Profil

Din Hugging Face-token finns i din profil under [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Publicera eller dela dem inte offentligt. Skapa istället en ny token för projektanvändning och kopiera den till `.env`-filen under variabeln `HUGGING_FACE_API_KEY`. _Obs:_ Detta är tekniskt sett inte en API-nyckel men används för autentisering, så vi behåller den namngivningen för konsekvensens skull.

## Konfigurera Microsoft Foundry Models: Från Portal

> **Obs:** GitHub Models pensioneras i slutet av juli 2026. Microsoft Foundry Models är den direkta ersättaren, med samma modellkatalog för gratis provkörning och Azure AI Inference SDK / OpenAI SDK-upplevelse.

1. Gå till [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) och skapa (eller öppna) ett Foundry-projekt.
1. Bläddra i [modellkatalogen](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) och distribuera en modell, till exempel `gpt-5-mini`.
1. På projektets **Översikt** sida, kopiera **endpoint** och **API-nyckel**.
1. Använd endpointvärdet för `AZURE_INFERENCE_ENDPOINT` och nyckelvärdet för `AZURE_INFERENCE_CREDENTIAL` i din `.env`-fil.

## Offline / Lokala Leverantörer

Om du inte vill använda något molnabonnemang alls kan du köra kompatibla öppna modeller direkt på din egen enhet:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsofts lokala runtime. Den väljer automatiskt bästa exekveringsleverantör (NPU, GPU eller CPU) och exponerar en OpenAI-kompatibel endpoint, så du kan återanvända det mesta av exempel-koden i denna kurs med minimala förändringar. Se [Foundry Local-dokumentationen](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) för att komma igång, eller installera med `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - ett populärt alternativ för att köra öppna modeller som Llama, Phi, Mistral och Gemma lokalt.


Se [Lektion 19: Bygga med SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) för praktiska exempel som använder båda alternativen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->