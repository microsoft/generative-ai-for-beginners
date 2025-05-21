<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T12:50:03+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "sv"
}
-->
# Ställ in din utvecklingsmiljö

Vi har satt upp detta arkiv och kurs med en [utvecklingscontainer](https://containers.dev?WT.mc_id=academic-105485-koreyst) som har en universell runtime som kan stödja utveckling i Python3, .NET, Node.js och Java. Den relaterade konfigurationen är definierad i filen `devcontainer.json` som finns i mappen `.devcontainer/` vid roten av detta arkiv.

För att aktivera utvecklingscontainern, starta den i [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (för en molnvärd runtime) eller i [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (för en lokalt värd runtime). Läs [denna dokumentation](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) för mer information om hur utvecklingscontainrar fungerar inom VS Code.

> [!TIP]  
> Vi rekommenderar att använda GitHub Codespaces för en snabb start med minimal ansträngning. Det erbjuder en generös [gratis användningskvot](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) för personliga konton. Konfigurera [timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) för att stoppa eller radera inaktiva codespaces för att maximera din kvotanvändning.

## 1. Utföra uppgifter

Varje lektion kommer att ha _valfria_ uppgifter som kan ges i ett eller flera programmeringsspråk, inklusive: Python, .NET/C#, Java och JavaScript/TypeScript. Detta avsnitt ger allmän vägledning relaterad till att utföra dessa uppgifter.

### 1.1 Python-uppgifter

Python-uppgifter ges antingen som applikationer (`.py`-filer) eller Jupyter-notebooks (`.ipynb`-filer).
- För att köra notebooken, öppna den i Visual Studio Code och klicka sedan på _Select Kernel_ (uppe till höger) och välj det förvalda alternativet Python 3 som visas. Du kan nu _Run All_ för att köra notebooken.
- För att köra Python-applikationer från kommandoraden, följ uppgiftsspecifika instruktioner för att säkerställa att du väljer rätt filer och tillhandahåller nödvändiga argument.

## 2. Konfigurera leverantörer

Uppgifter **kan** också ställas in för att arbeta mot en eller flera Large Language Model (LLM) distributioner via en stödd tjänsteleverantör som OpenAI, Azure eller Hugging Face. Dessa tillhandahåller en _värd endpoint_ (API) som vi kan komma åt programmatiskt med rätt referenser (API-nyckel eller token). I denna kurs diskuterar vi dessa leverantörer:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) med olika modeller inklusive kärnserien GPT.
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) för OpenAI-modeller med fokus på företagsberedskap
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) för öppen källkodsmodeller och inferensserver

**Du kommer att behöva använda dina egna konton för dessa övningar**. Uppgifter är valfria så du kan välja att ställa in en, alla - eller ingen - av leverantörerna baserat på dina intressen. Några riktlinjer för registrering:

| Registrering | Kostnad | API-nyckel | Lekplats | Kommentarer |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Prissättning](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektbaserad](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Kodfri, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Flera modeller tillgängliga |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Prissättning](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Snabbstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Snabbstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Måste ansöka i förväg för åtkomst](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Prissättning](https://huggingface.co/pricing) | [Åtkomsttoken](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat har begränsade modeller](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Följ anvisningarna nedan för att _konfigurera_ detta arkiv för användning med olika leverantörer. Uppgifter som kräver en specifik leverantör kommer att innehålla en av dessa taggar i deras filnamn:
- `aoai` - kräver Azure OpenAI-endpoint, nyckel
- `oai` - kräver OpenAI-endpoint, nyckel
- `hf` - kräver Hugging Face-token

Du kan konfigurera en, ingen eller alla leverantörer. Relaterade uppgifter kommer helt enkelt att ge fel på saknade referenser.

### 2.1. Skapa `.env`-fil

Vi antar att du redan har läst riktlinjerna ovan och registrerat dig hos den relevanta leverantören och fått de nödvändiga autentiseringsuppgifterna (API_KEY eller token). I fallet med Azure OpenAI antar vi också att du har en giltig distribution av en Azure OpenAI-tjänst (endpoint) med minst en GPT-modell distribuerad för chattslutförande.

Nästa steg är att konfigurera dina **lokala miljövariabler** enligt följande:

1. Titta i rotmappen efter en `.env.copy`-fil som bör ha innehåll som detta:

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

2. Kopiera den filen till `.env` med kommandot nedan. Denna fil är _gitignore-d_, vilket håller hemligheter säkra.

   ```bash
   cp .env.copy .env
   ```

3. Fyll i värdena (ersätt platshållare på höger sida av `=`) som beskrivs i nästa avsnitt.

3. (Valfritt) Om du använder GitHub Codespaces har du möjlighet att spara miljövariabler som _Codespaces hemligheter_ associerade med detta arkiv. I så fall behöver du inte ställa in en lokal .env-fil. **Observera dock att detta alternativ endast fungerar om du använder GitHub Codespaces.** Du måste fortfarande ställa in .env-filen om du använder Docker Desktop istället.

### 2.2. Fyll i `.env`-filen

Låt oss ta en snabb titt på variabelnamnen för att förstå vad de representerar:

| Variabel | Beskrivning |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Detta är användarens åtkomsttoken du ställer in i din profil |
| OPENAI_API_KEY | Detta är auktoriseringsnyckeln för att använda tjänsten för icke-Azure OpenAI-endpoints |
| AZURE_OPENAI_API_KEY | Detta är auktoriseringsnyckeln för att använda den tjänsten |
| AZURE_OPENAI_ENDPOINT | Detta är den distribuerade endpointen för en Azure OpenAI-resurs |
| AZURE_OPENAI_DEPLOYMENT | Detta är endpointen för _textgenerering_ modellens distribution |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Detta är endpointen för _textinbäddningar_ modellens distribution |
| | |

Notera: De sista två Azure OpenAI-variablerna återspeglar en standardmodell för chattslutförande (textgenerering) och vektorsökning (inbäddningar) respektive. Instruktioner för att ställa in dem kommer att definieras i relevanta uppgifter.

### 2.3 Konfigurera Azure: Från Portalen

Azure OpenAI-endpointen och nyckelvärdena kommer att hittas i [Azure Portalen](https://portal.azure.com?WT.mc_id=academic-105485-koreyst) så låt oss börja där.

1. Gå till [Azure Portalen](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klicka på alternativet **Nycklar och Endpoint** i sidofältet (menyn till vänster).
1. Klicka på **Visa nycklar** - du bör se följande: KEY 1, KEY 2 och Endpoint.
1. Använd värdet för KEY 1 för AZURE_OPENAI_API_KEY
1. Använd värdet för Endpoint för AZURE_OPENAI_ENDPOINT

Nästa steg är att få endpoints för de specifika modeller vi har distribuerat.

1. Klicka på alternativet **Modell distributioner** i sidofältet (menyn till vänster) för Azure OpenAI-resursen.
1. På målsidan, klicka på **Hantera distributioner**

Detta tar dig till webbplatsen för Azure OpenAI Studio, där vi hittar de andra värdena som beskrivs nedan.

### 2.4 Konfigurera Azure: Från Studion

1. Navigera till [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **från din resurs** som beskrivs ovan.
1. Klicka på fliken **Distributioner** (sidofältet, till vänster) för att visa för närvarande distribuerade modeller.
1. Om din önskade modell inte är distribuerad, använd **Skapa ny distribution** för att distribuera den.
1. Du kommer att behöva en _textgenereringsmodell_ - vi rekommenderar: **gpt-35-turbo**
1. Du kommer att behöva en _textinbäddningsmodell_ - vi rekommenderar **text-embedding-ada-002**

Uppdatera nu miljövariablerna för att återspegla det _Distributionsnamn_ som används. Detta kommer vanligtvis att vara samma som modellnamnet om du inte ändrade det uttryckligen. Så, som ett exempel, kan du ha:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Glöm inte att spara .env-filen när du är klar**. Du kan nu avsluta filen och återgå till instruktionerna för att köra notebooken.

### 2.5 Konfigurera OpenAI: Från Profilen

Din OpenAI API-nyckel kan hittas i ditt [OpenAI-konto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Om du inte har en, kan du registrera dig för ett konto och skapa en API-nyckel. När du har nyckeln kan du använda den för att fylla i variabeln `OPENAI_API_KEY` i `.env`-filen.

### 2.6 Konfigurera Hugging Face: Från Profilen

Din Hugging Face-token kan hittas i din profil under [Åtkomsttoken](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Dela eller publicera inte dessa offentligt. Skapa istället en ny token för detta projekt och kopiera det till `.env`-filen under variabeln `HUGGING_FACE_API_KEY`. _Notera:_ Detta är tekniskt sett inte en API-nyckel men används för autentisering så vi behåller den namngivningskonventionen för konsekvens.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var medveten om att automatiserade översättningar kan innehålla fel eller oriktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi är inte ansvariga för missförstånd eller misstolkningar som uppstår från användningen av denna översättning.