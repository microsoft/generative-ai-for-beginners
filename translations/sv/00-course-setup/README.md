<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T07:10:52+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sv"
}
-->
# Kom igång med den här kursen

Vi är väldigt glada över att du ska börja den här kursen och se vad du blir inspirerad att skapa med Generativ AI!

För att säkerställa din framgång beskriver den här sidan installationssteg, tekniska krav och var du kan få hjälp om det behövs.

## Installationssteg

För att börja ta den här kursen behöver du genomföra följande steg.

### 1. Forka detta repo

[Forka hela detta repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) till ditt eget GitHub-konto för att kunna ändra i koden och klara av utmaningarna. Du kan också [stjärnmärka (🌟) detta repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) för att lättare hitta det och relaterade repos.

### 2. Skapa en codespace

För att undvika beroendeproblem när du kör koden rekommenderar vi att du kör kursen i en [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Detta kan skapas genom att välja `Code`-alternativet på din forkade version av detta repo och sedan välja **Codespaces**.

![Dialog som visar knappar för att skapa en codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Spara dina API-nycklar

Det är viktigt att hålla dina API-nycklar säkra när du bygger någon typ av applikation. Vi rekommenderar att du inte sparar några API-nycklar direkt i din kod. Att lägga upp dessa uppgifter i ett offentligt repo kan leda till säkerhetsproblem och till och med oönskade kostnader om de används av någon illvillig aktör.  
Här är en steg-för-steg-guide för hur du skapar en `.env`-fil för Python och lägger till `GITHUB_TOKEN`:

1. **Navigera till din projektmapp**: Öppna terminalen eller kommandoprompten och gå till projektets rotmapp där du vill skapa `.env`-filen.

   ```bash
   cd path/to/your/project
   ```

2. **Skapa `.env`-filen**: Använd din favorittextredigerare för att skapa en ny fil med namnet `.env`. Om du använder kommandoraden kan du använda `touch` (på Unix-baserade system) eller `echo` (på Windows):

   Unix-baserade system:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Redigera `.env`-filen**: Öppna `.env`-filen i en textredigerare (t.ex. VS Code, Notepad++ eller någon annan editor). Lägg till följande rad i filen och ersätt `your_github_token_here` med din faktiska GitHub-token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Spara filen**: Spara ändringarna och stäng textredigeraren.

5. **Installera `python-dotenv`**: Om du inte redan har gjort det behöver du installera paketet `python-dotenv` för att kunna läsa in miljövariabler från `.env`-filen i din Python-applikation. Du kan installera det med `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Läs in miljövariabler i ditt Python-skript**: I ditt Python-skript använder du `python-dotenv` för att läsa in miljövariablerna från `.env`-filen:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Klart! Du har nu skapat en `.env`-fil, lagt till din GitHub-token och läst in den i din Python-applikation.

## Hur man kör lokalt på din dator

För att köra koden lokalt på din dator behöver du ha någon version av [Python installerad](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

För att sedan använda repot behöver du klona det:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

När du har allt på plats kan du börja!

## Valfria steg

### Installera Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) är en lättviktsinstallerare för att installera [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python samt några paket.  
Conda är en pakethanterare som gör det enkelt att sätta upp och växla mellan olika Python [**virtuella miljöer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) och paket. Den är också användbar för att installera paket som inte finns via `pip`.

Du kan följa [Miniconda installationsguide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) för att komma igång.

När Miniconda är installerat behöver du klona [repositoriet](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (om du inte redan gjort det).

Därefter behöver du skapa en virtuell miljö. För att göra detta med Conda, skapa en ny miljöfil (_environment.yml_). Om du följer med i Codespaces, skapa denna i `.devcontainer`-mappen, alltså `.devcontainer/environment.yml`.

Fyll i din miljöfil med nedanstående kodsnutt:

```yml
name: <environment-name>
channels:
  - defaults
  - microsoft
dependencies:
  - python=<python-version>
  - openai
  - python-dotenv
  - pip
  - pip:
      - azure-ai-ml
```

Om du får fel när du använder conda kan du manuellt installera Microsoft AI Libraries med följande kommando i terminalen.

```
conda install -c microsoft azure-ai-ml
```

Miljöfilen specificerar de beroenden vi behöver. `<environment-name>` är namnet du vill ge din Conda-miljö och `<python-version>` är den Python-version du vill använda, till exempel `3` som är den senaste stora versionen.

När detta är gjort kan du skapa din Conda-miljö genom att köra kommandona nedan i din terminal/kommandorad:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Se [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) om du stöter på problem.

### Använda Visual Studio Code med Python-tillägget

Vi rekommenderar att du använder [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) med [Python-tillägget](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installerat för den här kursen. Detta är dock mer en rekommendation än ett krav.

> **Note**: Genom att öppna kursrepositoriet i VS Code har du möjlighet att sätta upp projektet i en container. Detta tack vare den [speciella `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)-mappen som finns i kursrepositoriet. Mer om detta senare.

> **Note**: När du klonar och öppnar mappen i VS Code kommer det automatiskt föreslå att du installerar Python-tillägget.

> **Note**: Om VS Code föreslår att du öppnar repot i en container, tacka nej till detta för att använda den lokalt installerade versionen av Python.

### Använda Jupyter i webbläsaren

Du kan också arbeta med projektet i [Jupyter-miljön](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direkt i din webbläsare. Både klassiska Jupyter och [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) erbjuder en trevlig utvecklingsmiljö med funktioner som autokomplettering, kodmarkering med mera.

För att starta Jupyter lokalt, gå till terminalen/kommandoraden, navigera till kursmappen och kör:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Detta startar en Jupyter-instans och URL:en för att komma åt den visas i terminalfönstret.

När du öppnar URL:en bör du se kursöversikten och kunna navigera till valfri `*.ipynb`-fil, till exempel `08-building-search-applications/python/oai-solution.ipynb`.

### Köra i en container

Ett alternativ till att sätta upp allt på din dator eller i Codespace är att använda en [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Den speciella `.devcontainer`-mappen i kursrepositoriet gör det möjligt för VS Code att sätta upp projektet i en container. Utanför Codespaces kräver detta installation av Docker och är ganska avancerat, så vi rekommenderar detta endast för dig som har erfarenhet av containers.

Ett av de bästa sätten att hålla dina API-nycklar säkra när du använder GitHub Codespaces är att använda Codespace Secrets. Följ guiden för [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) för att lära dig mer.

## Lektioner och tekniska krav

Kursen innehåller 6 konceptlektioner och 6 kodlektioner.

För kodlektionerna använder vi Azure OpenAI Service. Du behöver tillgång till Azure OpenAI service och en API-nyckel för att köra koden. Du kan ansöka om tillgång genom att [fylla i denna ansökan](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Medan du väntar på att din ansökan behandlas innehåller varje kodlektion även en `README.md`-fil där du kan se koden och resultaten.

## Använda Azure OpenAI Service för första gången

Om det är första gången du arbetar med Azure OpenAI service, följ denna guide för hur du [skapar och distribuerar en Azure OpenAI Service-resurs.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Använda OpenAI API för första gången

Om det är första gången du arbetar med OpenAI API, följ guiden för hur du [skapar och använder gränssnittet.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Träffa andra deltagare

Vi har skapat kanaler i vår officiella [AI Community Discord-server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) för att du ska kunna träffa andra deltagare. Det är ett utmärkt sätt att nätverka med likasinnade entreprenörer, utvecklare, studenter och alla som vill ta nästa steg inom Generativ AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektteamet finns också på denna Discord-server för att hjälpa deltagare.

## Bidra

Den här kursen är ett open source-initiativ. Om du ser förbättringsområden eller problem, skapa gärna en [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) eller rapportera ett [GitHub-issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektteamet följer alla bidrag. Att bidra till open source är ett fantastiskt sätt att bygga din karriär inom Generativ AI.

De flesta bidrag kräver att du godkänner ett Contributor License Agreement (CLA) som intygar att du har rätt att och faktiskt ger oss rätt att använda ditt bidrag. För mer information, besök [CLA, Contributor License Agreement-webbplatsen](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Viktigt: när du översätter text i detta repo, se till att du inte använder maskinöversättning. Vi kommer att verifiera översättningarna via communityn, så anmäl dig endast för översättningar på språk du behärskar väl.

När du skickar en pull request kommer en CLA-bot automatiskt avgöra om du behöver lämna in en CLA och märka PR:n på rätt sätt (t.ex. med etikett eller kommentar). Följ bara instruktionerna från boten. Du behöver bara göra detta en gång för alla repos som använder vår CLA.

Detta projekt har antagit [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). För mer information, läs Code of Conduct FAQ eller kontakta [Email opencode](opencode@microsoft.com) vid frågor eller kommentarer.

## Nu kör vi!

Nu när du har genomfört de nödvändiga stegen för att ta kursen, låt oss börja med en [introduktion till Generativ AI och LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.