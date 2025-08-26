<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T17:16:06+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "sv"
}
-->
# Välja & Konfigurera en LLM-leverantör 🔑

Uppgifter **kan** även ställas in för att fungera mot en eller flera Large Language Model (LLM)-distributioner via en stödd tjänsteleverantör som OpenAI, Azure eller Hugging Face. Dessa erbjuder ett _hostat endpoint_ (API) som vi kan komma åt programmatiskt med rätt autentiseringsuppgifter (API-nyckel eller token). I den här kursen diskuterar vi dessa leverantörer:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) med olika modeller, inklusive kärnserien GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) för OpenAI-modeller med fokus på företagsanpassning
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) för öppen källkodsmodeller och inferensservrar

**Du behöver använda egna konton för dessa övningar**. Uppgifterna är valfria, så du kan välja att sätta upp en, alla – eller ingen – av leverantörerna beroende på vad du är intresserad av. Några tips för registrering:

| Registrering | Kostnad | API-nyckel | Playground | Kommentarer |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Priser](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektbaserad](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Flera modeller tillgängliga |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Priser](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Snabbstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Snabbstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Måste ansöka i förväg för åtkomst](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Priser](https://huggingface.co/pricing) | [Åtkomsttoken](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat har begränsade modeller](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Följ instruktionerna nedan för att _konfigurera_ detta repo för användning med olika leverantörer. Uppgifter som kräver en specifik leverantör kommer att ha någon av dessa taggar i filnamnet:

- `aoai` - kräver Azure OpenAI endpoint och nyckel
- `oai` - kräver OpenAI endpoint och nyckel
- `hf` - kräver Hugging Face-token

Du kan konfigurera en, ingen eller alla leverantörer. Relaterade uppgifter kommer helt enkelt att ge fel om autentiseringsuppgifter saknas.

## Skapa `.env`-fil

Vi utgår från att du redan har läst instruktionerna ovan och registrerat dig hos relevant leverantör samt fått de autentiseringsuppgifter (API_KEY eller token) som behövs. För Azure OpenAI antar vi också att du har en giltig distribution av Azure OpenAI Service (endpoint) med minst en GPT-modell distribuerad för chat completion.

Nästa steg är att konfigurera dina **lokala miljövariabler** enligt följande:

1. Leta i rotmappen efter en `.env.copy`-fil som bör ha innehåll som detta:

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

2. Kopiera den filen till `.env` med kommandot nedan. Denna fil är _gitignore-ad_, vilket håller hemligheter säkra.

   ```bash
   cp .env.copy .env
   ```

3. Fyll i värdena (ersätt platshållarna till höger om `=`) enligt beskrivningen i nästa avsnitt.

4. (Valfritt) Om du använder GitHub Codespaces kan du spara miljövariabler som _Codespaces secrets_ kopplade till detta repo. Då behöver du inte skapa en lokal .env-fil. **Observera dock att detta endast fungerar om du använder GitHub Codespaces.** Om du istället använder Docker Desktop måste du fortfarande skapa .env-filen.

## Fyll i `.env`-filen

Vi tittar snabbt på variabelnamnen för att förstå vad de står för:

| Variabel  | Beskrivning  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Detta är användarens åtkomsttoken som du ställer in i din profil |
| OPENAI_API_KEY | Detta är auktoriseringsnyckeln för att använda tjänsten för icke-Azure OpenAI-endpoints |
| AZURE_OPENAI_API_KEY | Detta är auktoriseringsnyckeln för att använda den tjänsten |
| AZURE_OPENAI_ENDPOINT | Detta är det distribuerade endpointet för en Azure OpenAI-resurs |
| AZURE_OPENAI_DEPLOYMENT | Detta är endpointet för _textgenereringsmodellen_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Detta är endpointet för _text-embeddingsmodellen_ |
| | |

Obs: De två sista Azure OpenAI-variablerna avser en standardmodell för chat completion (textgenerering) respektive vektorsökning (embeddings). Instruktioner för att ställa in dem ges i relevanta uppgifter.

## Konfigurera Azure: Från Portalen

Azure OpenAI endpoint och nyckel hittar du i [Azure-portalen](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), så vi börjar där.

1. Gå till [Azure-portalen](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klicka på **Keys and Endpoint** i sidomenyn (menyn till vänster).
1. Klicka på **Show Keys** – du bör se följande: KEY 1, KEY 2 och Endpoint.
1. Använd värdet för KEY 1 till AZURE_OPENAI_API_KEY
1. Använd värdet för Endpoint till AZURE_OPENAI_ENDPOINT

Nu behöver vi endpoints för de specifika modeller vi har distribuerat.

1. Klicka på **Model deployments** i sidomenyn (vänster meny) för Azure OpenAI-resursen.
1. På målsidan, klicka på **Manage Deployments**

Detta tar dig till Azure OpenAI Studio-webbplatsen, där vi hittar de andra värdena enligt nedan.

## Konfigurera Azure: Från Studio

1. Navigera till [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **från din resurs** enligt ovan.
1. Klicka på fliken **Deployments** (sidomeny till vänster) för att se aktuella modeller som är distribuerade.
1. Om din önskade modell inte är distribuerad, använd **Create new deployment** för att distribuera den.
1. Du behöver en _textgenereringsmodell_ – vi rekommenderar: **gpt-35-turbo**
1. Du behöver en _text-embeddingmodell_ – vi rekommenderar **text-embedding-ada-002**

Uppdatera nu miljövariablerna så att de speglar det _distributionsnamn_ du använt. Detta är oftast samma som modellnamnet om du inte ändrat det själv. Till exempel kan du ha:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Glöm inte att spara .env-filen när du är klar**. Du kan nu stänga filen och återgå till instruktionerna för att köra notebooken.

## Konfigurera OpenAI: Från Profil

Din OpenAI API-nyckel hittar du i ditt [OpenAI-konto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Om du inte har någon kan du registrera ett konto och skapa en API-nyckel. När du har nyckeln kan du använda den för att fylla i variabeln `OPENAI_API_KEY` i `.env`-filen.

## Konfigurera Hugging Face: Från Profil

Din Hugging Face-token hittar du i din profil under [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Dela eller publicera inte dessa offentligt. Skapa istället en ny token för detta projekt och kopiera in den i `.env`-filen under variabeln `HUGGING_FACE_API_KEY`. _Obs:_ Detta är tekniskt sett inte en API-nyckel men används för autentisering, så vi behåller det namnet för konsekvensens skull.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.