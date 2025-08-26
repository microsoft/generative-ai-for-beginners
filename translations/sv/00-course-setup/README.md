<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T17:16:29+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sv"
}
-->
# Kom igång med den här kursen

Vi är väldigt glada att du ska börja den här kursen och ser fram emot att se vad du blir inspirerad att bygga med Generativ AI!

För att du ska lyckas går vi här igenom installationssteg, tekniska krav och var du kan få hjälp om du behöver.

## Installationssteg

För att börja med kursen behöver du genomföra följande steg.

### 1. Forka detta repo

[Forka hela detta repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) till ditt eget GitHub-konto för att kunna ändra kod och slutföra utmaningarna. Du kan också [stjärnmärka (🌟) detta repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) för att enklare hitta det och relaterade repos.

### 2. Skapa en codespace

För att undvika beroendeproblem när du kör koden rekommenderar vi att du kör kursen i en [GitHub Codespace](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

I din fork: **Code -> Codespaces -> New on main**

![Dialogruta som visar knappar för att skapa en codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Lägg till en hemlighet

1. ⚙️ Kugghjulsikon -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Namnge OPENAI_API_KEY, klistra in din nyckel, Spara.

### 3.  Vad händer nu?

| Jag vill…            | Gå till…                                                                |
|----------------------|-------------------------------------------------------------------------|
| Starta Lektion 1     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Arbeta offline       | [`setup-local.md`](02-setup-local.md)                                   |
| Ställa in en LLM-leverantör | [`providers.md`](providers.md)                                   |
| Träffa andra deltagare | [Gå med i vår Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Felsökning

| Symptom                                   | Lösning                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| Container-bygget fastnar > 10 min         | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminalen anslöt inte; klicka **+** ➜ *bash*                   |
| `401 Unauthorized` från OpenAI            | Fel / utgången `OPENAI_API_KEY`                                 |
| VS Code visar “Dev container mounting…”   | Uppdatera webbläsarfliken—Codespaces tappar ibland anslutningen |
| Notebook-kärna saknas                     | Notebook-menyn ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

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

5. **Installera `python-dotenv`**: Om du inte redan gjort det behöver du installera paketet `python-dotenv` för att ladda miljövariabler från `.env`-filen till din Python-applikation. Du kan installera det med `pip`:

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

Klart! Du har nu skapat en `.env`-fil, lagt till din GitHub-token och laddat in den i din Python-applikation.

## Så här kör du lokalt på din dator

För att köra koden lokalt på din dator behöver du ha någon version av [Python installerad](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

För att använda repot behöver du klona det:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

När du har allt på plats kan du börja!

## Valfria steg

### Installera Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) är en lättviktig installerare för att installera [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python och några paket.
Conda är en pakethanterare som gör det enkelt att sätta upp och byta mellan olika Python-[**virtuella miljöer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) och paket. Det är också användbart för att installera paket som inte finns via `pip`.

Du kan följa [MiniConda installationsguide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) för att installera det.

När Miniconda är installerat behöver du klona [repot](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (om du inte redan gjort det).

Därefter behöver du skapa en virtuell miljö. För att göra detta med Conda, skapa en ny miljöfil (_environment.yml_). Om du följer med i Codespaces, skapa den i `.devcontainer`-katalogen, alltså `.devcontainer/environment.yml`.

Fyll i din miljöfil med koden nedan:

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

Om du får problem med conda kan du manuellt installera Microsoft AI Libraries med följande kommando i terminalen.

```
conda install -c microsoft azure-ai-ml
```

Miljöfilen specificerar de beroenden vi behöver. `<environment-name>` är namnet du vill ge din Conda-miljö, och `<python-version>` är den version av Python du vill använda, till exempel `3` för senaste huvudversionen.

När det är klart kan du skapa din Conda-miljö genom att köra kommandona nedan i din terminal/kommandorad

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Se [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) om du stöter på problem.

### Använda Visual Studio Code med Python-tillägget

Vi rekommenderar att du använder [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) med [Python-tillägget](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installerat för den här kursen. Detta är dock bara en rekommendation och inget krav.

> **Note**: När du öppnar kursens repo i VS Code får du möjlighet att sätta upp projektet i en container. Detta tack vare den [speciella `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)-katalogen i kursens repo. Mer om detta senare.

> **Note**: När du klonar och öppnar katalogen i VS Code kommer du automatiskt få förslag om att installera Python-tillägget.

> **Note**: Om VS Code föreslår att du ska öppna repot i en container, tacka nej till detta för att använda den lokalt installerade versionen av Python.

### Använda Jupyter i webbläsaren

Du kan också arbeta med projektet i [Jupyter-miljön](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direkt i webbläsaren. Både klassiska Jupyter och [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) erbjuder en trevlig utvecklingsmiljö med funktioner som autokomplettering, kodfärgning m.m.

För att starta Jupyter lokalt, gå till terminalen/kommandoraden, navigera till kurskatalogen och kör:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Detta startar en Jupyter-instans och URL:en för att komma åt den visas i terminalfönstret.

När du öppnar URL:en bör du se kursöversikten och kunna navigera till valfri `*.ipynb`-fil. Till exempel `08-building-search-applications/python/oai-solution.ipynb`.

### Köra i en container

Ett alternativ till att sätta upp allt på din dator eller i Codespace är att använda en [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Den speciella `.devcontainer`-mappen i kursens repo gör det möjligt för VS Code att sätta upp projektet i en container. Utanför Codespaces kräver detta att du installerar Docker, och det är lite mer avancerat, så vi rekommenderar detta bara för dig som har erfarenhet av containers.

Ett av de bästa sätten att hålla dina API-nycklar säkra när du använder GitHub Codespaces är att använda Codespace Secrets. Följ gärna [guiden för hantering av Codespaces secrets](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) för att lära dig mer.

## Lektioner och tekniska krav

Kursen har 6 konceptlektioner och 6 kodningslektioner.

För kodningslektionerna använder vi Azure OpenAI Service. Du behöver tillgång till Azure OpenAI-tjänsten och en API-nyckel för att köra koden. Du kan ansöka om tillgång genom att [fylla i denna ansökan](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Medan du väntar på att din ansökan behandlas innehåller varje kodningslektion även en `README.md`-fil där du kan se koden och resultaten.

## Använda Azure OpenAI Service för första gången

Om det är första gången du arbetar med Azure OpenAI-tjänsten, följ denna guide för hur du [skapar och distribuerar en Azure OpenAI Service-resurs.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Använda OpenAI API för första gången

Om det är första gången du arbetar med OpenAI API, följ guiden för hur du [skapar och använder gränssnittet.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Träffa andra deltagare

Vi har skapat kanaler i vår officiella [AI Community Discord-server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) för att du ska kunna träffa andra deltagare. Det är ett utmärkt sätt att nätverka med andra entreprenörer, utvecklare, studenter och alla som vill utvecklas inom Generativ AI.

[![Gå med i discord-kanalen](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektteamet kommer också att finnas på Discord-servern för att hjälpa deltagare.

## Bidra

Den här kursen är ett open source-initiativ. Om du ser förbättringsmöjligheter eller problem, skapa gärna en [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) eller rapportera ett [GitHub-ärende](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektteamet kommer att följa alla bidrag. Att bidra till open source är ett fantastiskt sätt att bygga din karriär inom Generativ AI.

De flesta bidrag kräver att du godkänner ett Contributor License Agreement (CLA) där du intygar att du har rätt att, och faktiskt gör, ge oss rätt att använda ditt bidrag. För mer information, besök [CLA, Contributor License Agreement-webbplatsen](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Viktigt: när du översätter text i detta repo, se till att du inte använder maskinöversättning. Vi kommer att verifiera översättningar via communityn, så anmäl dig bara för översättningar till språk du behärskar.

När du skickar in en pull request kommer en CLA-bot automatiskt att avgöra om du behöver godkänna ett CLA och märka PR:en därefter (t.ex. etikett, kommentar). Följ bara instruktionerna från boten. Du behöver bara göra detta en gång för alla repos som använder vårt CLA.

Detta projekt har antagit [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). För mer information, läs Code of Conduct FAQ eller kontakta [Email opencode](opencode@microsoft.com) om du har frågor eller synpunkter.

## Nu kör vi!
Nu när du har slutfört de nödvändiga stegen för att gå klart kursen, låt oss börja med en [introduktion till Generativ AI och LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Vi strävar efter noggrannhet, men var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.