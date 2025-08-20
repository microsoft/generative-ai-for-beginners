<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:31:12+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "sv"
}
-->
# Ställ in din utvecklingsmiljö

Vi har satt upp detta repository och kurs med en [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) som har en universell runtime som kan stödja utveckling i Python3, .NET, Node.js och Java. Den relaterade konfigurationen definieras i filen `devcontainer.json` som finns i mappen `.devcontainer/` i roten av detta repository.

För att aktivera dev-containern, starta den i [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (för en molnbaserad runtime) eller i [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (för en lokal runtime på din enhet). Läs [den här dokumentationen](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) för mer information om hur dev-containrar fungerar i VS Code.

> [!TIP]  
> Vi rekommenderar att använda GitHub Codespaces för en snabb start med minimal ansträngning. Det erbjuder en generös [gratis användningskvot](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) för personliga konton. Konfigurera [timeout](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) för att stoppa eller ta bort inaktiva codespaces för att maximera din kvotanvändning.

## 1. Köra uppgifter

Varje lektion kan ha _valfria_ uppgifter som kan erbjudas i en eller flera programmeringsspråk, inklusive: Python, .NET/C#, Java och JavaScript/TypeScript. Denna sektion ger allmän vägledning kring hur du kör dessa uppgifter.

### 1.1 Python-uppgifter

Python-uppgifter tillhandahålls antingen som applikationer (`.py`-filer) eller Jupyter-notebooks (`.ipynb`-filer).  
- För att köra notebooken, öppna den i Visual Studio Code, klicka sedan på _Select Kernel_ (uppe till höger) och välj standardalternativet Python 3. Du kan nu välja _Run All_ för att köra hela notebooken.  
- För att köra Python-applikationer från kommandoraden, följ uppgiftsspecifika instruktioner för att säkerställa att du väljer rätt filer och anger nödvändiga argument.

## 2. Konfigurera leverantörer

Uppgifter **kan** också vara inställda för att fungera mot en eller flera Large Language Model (LLM)-distributioner via en stödd tjänsteleverantör som OpenAI, Azure eller Hugging Face. Dessa erbjuder en _hostad endpoint_ (API) som vi kan nå programmässigt med rätt autentiseringsuppgifter (API-nyckel eller token). I denna kurs diskuterar vi dessa leverantörer:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) med olika modeller inklusive kärnserien GPT.  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) för OpenAI-modeller med fokus på företagsanpassning.  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) för öppen källkod-modeller och inferensserver.

**Du behöver använda egna konton för dessa övningar**. Uppgifterna är frivilliga så du kan välja att konfigurera en, alla eller inga av leverantörerna beroende på dina intressen. Här är lite vägledning för registrering:

| Registrering | Kostnad | API-nyckel | Playground | Kommentarer |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [Prissättning](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [Projektbaserad](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Flera modeller tillgängliga |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [Prissättning](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Måste ansöka i förväg för åtkomst](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Prissättning](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Hugging Chat har begränsade modeller](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Följ instruktionerna nedan för att _konfigurera_ detta repository för användning med olika leverantörer. Uppgifter som kräver en specifik leverantör kommer att innehålla en av dessa taggar i filnamnet:  
 - `aoai` - kräver Azure OpenAI endpoint och nyckel  
 - `oai` - kräver OpenAI endpoint och nyckel  
 - `hf` - kräver Hugging Face token  

Du kan konfigurera en, inga eller alla leverantörer. Relaterade uppgifter kommer helt enkelt att ge fel om autentiseringsuppgifter saknas.

### 2.1. Skapa `.env`-fil

Vi förutsätter att du redan har läst vägledningen ovan, registrerat dig hos relevant leverantör och fått de nödvändiga autentiseringsuppgifterna (API_KEY eller token). I fallet med Azure OpenAI förutsätter vi också att du har en giltig distribution av en Azure OpenAI-tjänst (endpoint) med minst en GPT-modell distribuerad för chattkomplettering.

Nästa steg är att konfigurera dina **lokala miljövariabler** enligt följande:

1. Leta i rotmappen efter en fil som heter `.env.copy` som bör innehålla något liknande detta:

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

3. (Valfritt) Om du använder GitHub Codespaces kan du spara miljövariabler som _Codespaces secrets_ kopplade till detta repository. I så fall behöver du inte skapa en lokal .env-fil. **Observera dock att detta alternativ endast fungerar om du använder GitHub Codespaces.** Du måste fortfarande skapa .env-filen om du använder Docker Desktop.

### 2.2. Fyll i `.env`-filen

Låt oss snabbt titta på variabelnamnen för att förstå vad de representerar:

| Variabel  | Beskrivning  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Detta är användarens access-token som du ställt in i din profil |
| OPENAI_API_KEY | Detta är auktoriseringsnyckeln för att använda tjänsten för icke-Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Detta är auktoriseringsnyckeln för att använda den tjänsten |
| AZURE_OPENAI_ENDPOINT | Detta är den distribuerade endpointen för en Azure OpenAI-resurs |
| AZURE_OPENAI_DEPLOYMENT | Detta är endpointen för _textgenererings_-modellens distribution |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Detta är endpointen för _text embeddings_-modellens distribution |
| | |

Notera: De två sista Azure OpenAI-variablerna speglar en standardmodell för chattkomplettering (textgenerering) respektive vektorsökning (embeddings). Instruktioner för att ställa in dem kommer att definieras i relevanta uppgifter.

### 2.3 Konfigurera Azure: Från portalen

Värdena för Azure OpenAI endpoint och nyckel finns i [Azure-portalen](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), så vi börjar där.

1. Gå till [Azure-portalen](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
1. Klicka på alternativet **Keys and Endpoint** i sidomenyn (menyn till vänster).  
1. Klicka på **Show Keys** – du bör se följande: KEY 1, KEY 2 och Endpoint.  
1. Använd värdet för KEY 1 som AZURE_OPENAI_API_KEY  
1. Använd värdet för Endpoint som AZURE_OPENAI_ENDPOINT  

Nästa steg är att hitta endpoints för de specifika modeller vi har distribuerat.

1. Klicka på alternativet **Model deployments** i sidomenyn (vänster meny) för Azure OpenAI-resursen.  
1. På destinationssidan klickar du på **Manage Deployments**  

Detta tar dig till Azure OpenAI Studio-webbplatsen, där vi hittar de andra värdena enligt beskrivningen nedan.

### 2.4 Konfigurera Azure: Från Studio

1. Navigera till [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **från din resurs** som beskrivits ovan.  
1. Klicka på fliken **Deployments** (sidomeny, vänster) för att se de modeller som är distribuerade.  
1. Om din önskade modell inte är distribuerad, använd **Create new deployment** för att distribuera den.  
1. Du behöver en _text-generation_-modell – vi rekommenderar: **gpt-35-turbo**  
1. Du behöver en _text-embedding_-modell – vi rekommenderar **text-embedding-ada-002**  

Uppdatera nu miljövariablerna för att spegla det _Deployment name_ som används. Detta är vanligtvis samma som modellnamnet om du inte ändrat det explicit. Så, som exempel, kan du ha:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Glöm inte att spara .env-filen när du är klar**. Du kan nu stänga filen och återgå till instruktionerna för att köra notebooken.

### 2.5 Konfigurera OpenAI: Från profil

Din OpenAI API-nyckel finns i ditt [OpenAI-konto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Om du inte har en kan du registrera dig och skapa en API-nyckel. När du har nyckeln kan du använda den för att fylla i variabeln `OPENAI_API_KEY` i `.env`-filen.

### 2.6 Konfigurera Hugging Face: Från profil

Din Hugging Face-token finns i din profil under [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Dela inte dessa offentligt. Skapa istället en ny token för detta projekt och kopiera in den i `.env`-filen under variabeln `HUGGING_FACE_API_KEY`. _Notera:_ Detta är tekniskt sett inte en API-nyckel men används för autentisering, så vi behåller namngivningen för konsekvensens skull.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.