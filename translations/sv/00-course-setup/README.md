<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-05-19T12:27:43+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sv"
}
-->
# Komma igång med den här kursen

Vi är väldigt glada över att du börjar den här kursen och ser fram emot att se vad du blir inspirerad att bygga med Generativ AI!

För att säkerställa din framgång beskriver denna sida installationssteg, tekniska krav och var du kan få hjälp om det behövs.

## Installationssteg

För att börja denna kurs behöver du slutföra följande steg.

### 1. Forka detta repo

[Forka hela detta repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) till ditt eget GitHub-konto för att kunna ändra kod och slutföra utmaningarna. Du kan också [stjärnmärka (🌟) detta repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) för att lättare hitta det och relaterade repos.

### 2. Skapa en codespace

För att undvika beroendeproblem när du kör koden rekommenderar vi att du kör denna kurs i en [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Detta kan skapas genom att välja alternativet `Code` på din forkade version av detta repo och välja alternativet **Codespaces**.

![Dialogruta som visar knappar för att skapa en codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Lagra dina API-nycklar

Att hålla dina API-nycklar säkra är viktigt när du bygger vilken typ av applikation som helst. Vi rekommenderar att du inte lagrar några API-nycklar direkt i din kod. Att lägga till dessa detaljer i ett offentligt repo kan leda till säkerhetsproblem och oönskade kostnader om de används av en illasinnad aktör.
Här är en steg-för-steg-guide om hur du skapar en `.env`-fil för Python och lägger till `GITHUB_TOKEN`:

1. **Navigera till din projektkatalog**: Öppna din terminal eller kommandotolk och navigera till din projekts rotkatalog där du vill skapa `.env`-filen.

   ```bash
   cd path/to/your/project
   ```

2. **Skapa `.env`-filen**: Använd din föredragna textredigerare för att skapa en ny fil med namnet `.env`. Om du använder kommandoraden kan du använda `touch` (on Unix-based systems) or `echo` (på Windows):

   Unix-baserade system:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Redigera `.env`-filen**: Öppna `.env`-filen i en textredigerare (t.ex. VS Code, Notepad++ eller någon annan redigerare). Lägg till följande rad i filen och ersätt `your_github_token_here` med din faktiska GitHub-token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Spara filen**: Spara ändringarna och stäng textredigeraren.

5. **Installera `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv`-paketet för att ladda miljövariabler från `.env`-filen till din Python-applikation. Du kan installera det med `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Ladda miljövariabler i ditt Python-skript**: I ditt Python-skript, använd `python-dotenv`-paketet för att ladda miljövariablerna från `.env`-filen:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Det var allt! Du har nu framgångsrikt skapat en `.env`-fil, lagt till din GitHub-token och laddat den i din Python-applikation.

## Hur man kör lokalt på din dator

För att köra koden lokalt på din dator behöver du ha någon version av [Python installerad](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

För att sedan använda repot behöver du klona det:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

När du har allt utcheckat kan du börja!

## Valfria steg

### Installera Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) är en lättviktsinstallerare för att installera [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, samt några få paket.
Conda i sig är en pakethanterare som gör det enkelt att ställa in och byta mellan olika Python [**virtuella miljöer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) och paket. Det är också användbart för att installera paket som inte är tillgängliga via `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

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

Om du får fel när du använder conda kan du manuellt installera Microsoft AI Libraries med följande kommando i en terminal.

```
conda install -c microsoft azure-ai-ml
```

Miljöfilen specificerar de beroenden vi behöver. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` är den senaste stora versionen av Python.

När det är klart kan du skapa din Conda-miljö genom att köra kommandona nedan i din kommandorad/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Se [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) om du stöter på några problem.

### Använda Visual Studio Code med Python-tillägget

Vi rekommenderar att du använder [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) med det installerade [Python-tillägget](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) för denna kurs. Detta är dock mer av en rekommendation och inget krav.

> **Obs**: Genom att öppna kursrepot i VS Code har du möjlighet att sätta upp projektet i en container. Detta beror på den [speciella `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) katalogen som finns inom kursrepot. Mer om detta senare.

> **Obs**: När du klonar och öppnar katalogen i VS Code kommer det automatiskt att föreslå att du installerar ett Python-tillägg.

> **Obs**: Om VS Code föreslår att du öppnar repot i en container, avböj denna begäran för att använda den lokalt installerade versionen av Python.

### Använda Jupyter i webbläsaren

Du kan också arbeta med projektet i [Jupyter-miljön](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direkt i din webbläsare. Både klassisk Jupyter och [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) erbjuder en mycket trevlig utvecklingsmiljö med funktioner som autokomplettering, kodmarkering, etc.

För att starta Jupyter lokalt, gå till terminalen/kommandoraden, navigera till kurskatalogen och kör:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Detta startar en Jupyter-instans och URL:en för att komma åt den visas i kommandoradsfönstret.

När du kommer åt URL:en bör du se kursöversikten och kunna navigera till vilken `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` fil som helst där du kan se koden och utdata.

## Använda Azure OpenAI Service för första gången

Om detta är första gången du arbetar med Azure OpenAI-tjänsten, följ denna guide om hur du [skapar och distribuerar en Azure OpenAI Service-resurs.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Använda OpenAI API för första gången

Om detta är första gången du arbetar med OpenAI API, följ guiden om hur du [skapar och använder gränssnittet.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Möt andra deltagare

Vi har skapat kanaler i vår officiella [AI Community Discord-server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) för att träffa andra deltagare. Detta är ett utmärkt sätt att nätverka med andra likasinnade entreprenörer, byggare, studenter och alla som vill utvecklas inom Generativ AI.

[![Gå med i Discord-kanalen](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektteamet kommer också att finnas på denna Discord-server för att hjälpa alla deltagare.

## Bidra

Denna kurs är ett open-source-initiativ. Om du ser förbättringsområden eller problem, skapa gärna en [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) eller logga ett [GitHub-ärende](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektteamet kommer att följa alla bidrag. Att bidra till open source är ett fantastiskt sätt att bygga din karriär inom Generativ AI.

De flesta bidrag kräver att du godkänner ett Contributor License Agreement (CLA) som deklarerar att du har rätt att, och faktiskt gör, ge oss rättigheterna att använda ditt bidrag. För detaljer, besök [CLA, Contributor License Agreement-webbplatsen](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Viktigt: när du översätter text i detta repo, se till att du inte använder maskinöversättning. Vi kommer att verifiera översättningar via communityn, så var vänlig och anmäl dig bara för översättningar på språk där du är skicklig.

När du skickar in en pull-begäran kommer en CLA-bot automatiskt att avgöra om du behöver tillhandahålla en CLA och dekorera PR:n på lämpligt sätt (t.ex. etikett, kommentar). Följ helt enkelt instruktionerna från boten. Du behöver bara göra detta en gång över alla repos som använder vår CLA.

Detta projekt har antagit [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). För mer information läs Code of Conduct FAQ eller kontakta [Email opencode](opencode@microsoft.com) med eventuella ytterligare frågor eller kommentarer.

## Låt oss börja

Nu när du har slutfört de nödvändiga stegen för att genomföra denna kurs, låt oss börja med en [introduktion till Generativ AI och LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var medveten om att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår från användningen av denna översättning.