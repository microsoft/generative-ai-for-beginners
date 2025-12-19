<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b5b016b0eb8a1cef2e3097620d8aa23",
  "translation_date": "2025-12-19T15:20:57+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "sv"
}
-->
# Välja & konfigurera en LLM-leverantör 🔑

Uppgifter **kan** också ställas in för att fungera mot en eller flera Large Language Model (LLM)-distributioner via en stödd tjänsteleverantör som OpenAI, Azure eller Hugging Face. Dessa tillhandahåller en _hostad endpoint_ (API) som vi kan komma åt programmässigt med rätt autentiseringsuppgifter (API-nyckel eller token). I denna kurs diskuterar vi dessa leverantörer:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) med olika modeller inklusive kärnserien GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) för OpenAI-modeller med fokus på företagsberedskap
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) för öppen källkod-modeller och inferensserver

**Du behöver använda egna konton för dessa övningar**. Uppgifter är frivilliga så du kan välja att konfigurera en, alla - eller inga - av leverantörerna baserat på dina intressen. Några riktlinjer för registrering:

| Registrering | Kostnad | API-nyckel | Playground | Kommentarer |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Prissättning](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektbaserad](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Flera modeller tillgängliga |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Prissättning](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Måste ansöka i förväg för åtkomst](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Prissättning](https://huggingface.co/pricing) | [Åtkomsttoken](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat har begränsade modeller](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Följ anvisningarna nedan för att _konfigurera_ detta repository för användning med olika leverantörer. Uppgifter som kräver en specifik leverantör kommer att innehålla en av dessa taggar i deras filnamn:

- `aoai` - kräver Azure OpenAI endpoint, nyckel
- `oai` - kräver OpenAI endpoint, nyckel
- `hf` - kräver Hugging Face token

Du kan konfigurera en, inga eller alla leverantörer. Relaterade uppgifter kommer helt enkelt att ge fel vid saknade autentiseringsuppgifter.

## Skapa `.env`-fil

Vi antar att du redan har läst riktlinjerna ovan och registrerat dig hos relevant leverantör, samt erhållit nödvändiga autentiseringsuppgifter (API_KEY eller token). I fallet med Azure OpenAI antar vi också att du har en giltig distribution av en Azure OpenAI-tjänst (endpoint) med minst en GPT-modell distribuerad för chattkomplettering.

Nästa steg är att konfigurera dina **lokala miljövariabler** enligt följande:

1. Titta i rotmappen efter en `.env.copy`-fil som bör innehålla något liknande detta:

   ```bash
   # OpenAI-leverantör
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Standard är inställt!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopiera den filen till `.env` med kommandot nedan. Denna fil är _gitignore-ad_, vilket håller hemligheter säkra.

   ```bash
   cp .env.copy .env
   ```

3. Fyll i värdena (ersätt platshållare på höger sida om `=`) som beskrivs i nästa avsnitt.

4. (Valfritt) Om du använder GitHub Codespaces har du möjlighet att spara miljövariabler som _Codespaces-hemligheter_ kopplade till detta repository. I så fall behöver du inte konfigurera en lokal .env-fil. **Observera dock att detta alternativ endast fungerar om du använder GitHub Codespaces.** Du måste fortfarande konfigurera .env-filen om du använder Docker Desktop istället.

## Fyll i `.env`-filen

Låt oss snabbt titta på variabelnamnen för att förstå vad de representerar:

| Variabel  | Beskrivning  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Detta är användaråtkomsttoken du ställt in i din profil |
| OPENAI_API_KEY | Detta är auktoriseringsnyckeln för att använda tjänsten för icke-Azure OpenAI-endpoints |
| AZURE_OPENAI_API_KEY | Detta är auktoriseringsnyckeln för att använda den tjänsten |
| AZURE_OPENAI_ENDPOINT | Detta är den distribuerade endpointen för en Azure OpenAI-resurs |
| AZURE_OPENAI_DEPLOYMENT | Detta är _textgenererings_-modellens distributionsendpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Detta är _textembedding_-modellens distributionsendpoint |
| | |

Notera: De två sista Azure OpenAI-variablerna speglar en standardmodell för chattkomplettering (textgenerering) respektive vektorsökning (embedding). Instruktioner för att ställa in dem definieras i relevanta uppgifter.

## Konfigurera Azure: Från portalen

Azure OpenAI endpoint och nyckelvärden finns i [Azure-portalen](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) så vi börjar där.

1. Gå till [Azure-portalen](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klicka på alternativet **Keys and Endpoint** i sidomenyn (menyn till vänster).
1. Klicka på **Show Keys** - du bör se följande: KEY 1, KEY 2 och Endpoint.
1. Använd värdet för KEY 1 som AZURE_OPENAI_API_KEY
1. Använd värdet för Endpoint som AZURE_OPENAI_ENDPOINT

Nästa steg är att hämta endpoints för de specifika modeller vi distribuerat.

1. Klicka på alternativet **Model deployments** i sidomenyn (vänstermenyn) för Azure OpenAI-resursen.
1. På destinationssidan klickar du på **Manage Deployments**

Detta tar dig till Azure OpenAI Studio-webbplatsen, där vi hittar de andra värdena som beskrivs nedan.

## Konfigurera Azure: Från Studio

1. Navigera till [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **från din resurs** som beskrivits ovan.
1. Klicka på fliken **Deployments** (sidomeny, vänster) för att visa för närvarande distribuerade modeller.
1. Om din önskade modell inte är distribuerad, använd **Create new deployment** för att distribuera den.
1. Du behöver en _text-generation_-modell - vi rekommenderar: **gpt-35-turbo**
1. Du behöver en _text-embedding_-modell - vi rekommenderar **text-embedding-ada-002**

Uppdatera nu miljövariablerna för att spegla det _Deployment name_ som används. Detta är vanligtvis samma som modellnamnet om du inte ändrat det explicit. Så, som exempel, kan du ha:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Glöm inte att spara .env-filen när du är klar**. Du kan nu stänga filen och återgå till instruktionerna för att köra notebooken.

## Konfigurera OpenAI: Från profil

Din OpenAI API-nyckel finns i ditt [OpenAI-konto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Om du inte har en kan du registrera ett konto och skapa en API-nyckel. När du har nyckeln kan du använda den för att fylla i variabeln `OPENAI_API_KEY` i `.env`-filen.

## Konfigurera Hugging Face: Från profil

Din Hugging Face-token finns i din profil under [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Publicera eller dela inte dessa offentligt. Skapa istället en ny token för detta projekt och kopiera in den i `.env`-filen under variabeln `HUGGING_FACE_API_KEY`. _Notera:_ Detta är tekniskt sett inte en API-nyckel men används för autentisering, så vi behåller namngivningskonventionen för konsekvens.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->