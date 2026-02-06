# Kom igång med denna kurs

Vi är mycket glada att du ska börja denna kurs och se vad du blir inspirerad att bygga med Generativ AI!

För att säkerställa din framgång beskriver denna sida installationssteg, tekniska krav och var du kan få hjälp om det behövs.

## Installationssteg

För att börja med denna kurs behöver du slutföra följande steg.

### 1. Forka detta repo

[Forka hela detta repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) till ditt eget GitHub-konto för att kunna ändra någon kod och slutföra utmaningarna. Du kan också [stjärnmärka (🌟) detta repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) för att enklare hitta det och relaterade repos.

### 2. Skapa en codespace

För att undvika beroendeproblem när du kör koden rekommenderar vi att du kör denna kurs i en [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

I din fork: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/sv/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Lägg till en hemlighet

1. ⚙️ Kugghjulsikon -> Kommandopaletten -> Codespaces : Manage user secret -> Lägg till en ny hemlighet.
2. Namnge OPENAI_API_KEY, klistra in din nyckel, Spara.

### 3. Vad händer härnäst?

| Jag vill…           | Gå till…                                                               |
|---------------------|------------------------------------------------------------------------|
| Börja Lektion 1     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Arbeta offline      | [`setup-local.md`](02-setup-local.md)                                  |
| Konfigurera en LLM-leverantör | [`providers.md`](03-providers.md)                                  |
| Träffa andra deltagare | [Gå med i vår Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)  |

## Felsökning


| Symptom                                   | Lösning                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| Containerbygget fastnar > 10 min          | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`                | Terminalen kopplades inte; klicka **+** ➜ *bash*                |
| `401 Unauthorized` från OpenAI             | Felaktig / utgången `OPENAI_API_KEY`                            |
| VS Code visar “Dev container mounting…”   | Uppdatera webbläsarfliken—Codespaces tappar ibland anslutning  |
| Notebook-kärna saknas                      | Notebook-meny ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix-baserade system:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Redigera `.env`-filen**: Öppna `.env`-filen i en textredigerare (exempelvis VS Code, Notepad++ eller någon annan redigerare). Lägg till följande rad i filen och byt ut `your_github_token_here` mot din faktiska GitHub-token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Spara filen**: Spara ändringarna och stäng textredigeraren.

5. **Installera `python-dotenv`**: Om du inte redan har gjort det behöver du installera paketet `python-dotenv` för att läsa in miljövariabler från `.env`-filen i din Python-applikation. Du kan installera det med `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Ladda miljövariabler i ditt Python-skript**: I ditt Python-skript, använd paketet `python-dotenv` för att ladda miljövariablerna från `.env`-filen:

   ```python
   from dotenv import load_dotenv
   import os

   # Läs in miljövariabler från .env-fil
   load_dotenv()

   # Få tillgång till variabeln GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Klart! Du har framgångsrikt skapat en `.env`-fil, lagt till din GitHub-token och laddat in den i din Python-applikation.

## Hur man kör lokalt på din dator

För att köra koden lokalt på din dator behöver du ha någon version av [Python installerad](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

För att sedan använda repot behöver du klona det:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

När du har allt på plats kan du börja köra igång!

## Valfria steg

### Installera Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) är en lättviktsinstallatör för att installera [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python samt några paket.
Conda är en pakethanterare som gör det enkelt att sätta upp och växla mellan olika Python [**virtuella miljöer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) och paket. Det är också bra för att installera paket som inte finns tillgängliga via `pip`.

Du kan följa [MiniConda installationsguiden](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) för att sätta upp det.

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

Om du får fel när du använder conda kan du manuellt installera Microsoft AI Libraries med följande kommando i en terminal.

```
conda install -c microsoft azure-ai-ml
```

Miljöfilen specificerar de beroenden vi behöver. `<environment-name>` är namnet du vill använda för din Conda-miljö, och `<python-version>` är vilken Python-version du vill använda, till exempel är `3` den senaste större Python-versionen.

När det är klart kan du skapa din Conda-miljö genom att köra kommandona nedan i din kommandorad/terminal:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer undermapp gäller endast för Codespace-konfigurationer
conda activate ai4beg
```

Se [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) om du stöter på problem.

### Använda Visual Studio Code med Python support extension

Vi rekommenderar att du använder [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) med [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installerad för denna kurs. Detta är dock mer en rekommendation än ett krav.

> **Notera**: Genom att öppna kursrepositoriet i VS Code har du möjlighet att sätta upp projektet i en container. Detta är möjligt tack vare den [speciella `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) mappen i kursrepositoriet. Mer om detta senare.

> **Notera**: När du klonar och öppnar mappen i VS Code kommer det automatiskt att föreslå att du installerar ett Python-stöd.

> **Notera**: Om VS Code föreslår att du öppnar repot i en container, tacka nej till detta för att kunna använda den lokalt installerade versionen av Python.

### Använda Jupyter i webbläsaren

Du kan också arbeta med projektet via [Jupyter-miljön](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direkt i din webbläsare. Både klassisk Jupyter och [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) erbjuder en trevlig utvecklingsmiljö med funktioner som autokomplettering, kodmarkering, osv.

För att starta Jupyter lokalt öppnar du terminalen/kommandoraden, navigerar till kursmappen och kör:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Detta startar en Jupyter-instans och URL:en för att komma åt den visas i kommandoradsfönstret.

När du ansluter till URL:en bör du se kursöversikten och kunna navigera till vilken `*.ipynb`-fil som helst, till exempel `08-building-search-applications/python/oai-solution.ipynb`.

### Kör i en container

Ett alternativ till att sätta upp allt på din dator eller i Codespace är att använda en [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Den speciella `.devcontainer`-mappen i kursrepositoriet gör det möjligt för VS Code att sätta upp projektet i en container. Utanför Codespaces kräver detta installation av Docker, och det är lite mer arbete, så det rekommenderas främst för dig med erfarenhet av containers.

Ett av de bästa sätten att hålla dina API-nycklar säkra när du använder GitHub Codespaces är genom att använda Codespaces Secrets. Följ guiden för [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) för att lära dig mer.

## Lektioner och tekniska krav

Kursen består av 6 konceptlektioner och 6 kodlektioner.

För kodlektionerna använder vi Azure OpenAI Service. Du behöver tillgång till Azure OpenAI service och en API-nyckel för att köra denna kod. Du kan ansöka om tillgång genom att [komplett denna ansökan](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Medan du väntar på att din ansökan behandlas innehåller varje kodlektion även en `README.md`-fil där du kan se koden och resultaten.

## Använda Azure OpenAI Service för första gången

Om detta är första gången du använder Azure OpenAI service, följ denna guide för hur du [skapar och distribuerar en Azure OpenAI Service-resurs.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Använda OpenAI API för första gången

Om detta är första gången du arbetar med OpenAI API:n, följ guiden för hur du [skapar och använder gränssnittet.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Träffa andra deltagare

Vi har skapat kanaler i vår officiella [AI Community Discord-server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) för att träffa andra deltagare. Det är ett utmärkt sätt att nätverka med andra likasinnade entreprenörer, utvecklare, studenter och alla som vill höja sin nivå inom Generativ AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektteamet kommer också finnas i denna Discord-server för att hjälpa deltagare.

## Bidra

Denna kurs är ett open-source-initiativ. Om du ser förbättringsområden eller problem, skapa gärna en [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) eller rapportera ett [GitHub-issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektteamet kommer att följa alla bidrag. Att bidra till open source är ett fantastiskt sätt att bygga din karriär inom Generativ AI.

De flesta bidrag kräver att du godkänner ett Contributor License Agreement (CLA) som klargör att du har rätt att och faktiskt ger oss rätt att använda ditt bidrag. För detaljer, besök [CLA, Contributor License Agreement webbplats](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Viktigt: när du översätter text i detta repo, se till att du inte använder maskinöversättning. Vi verifierar översättningarna via communityn, så vänligen anmäl dig bara för översättningar på språk där du är skicklig.

När du skickar en pull request kommer en CLA-bot automatiskt avgöra om du behöver godkänna CLA och märka PR:en på rätt sätt (t.ex. etikett, kommentar). Följ bara instruktionerna från boten. Du behöver bara göra detta en gång för alla repos som använder vårt CLA.

Detta projekt har antagit [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). För mer information läs Code of Conduct FAQ eller kontakta [Email opencode](opencode@microsoft.com) med eventuella frågor eller kommentarer.

## Nu kör vi!
Nu när du har slutfört de nödvändiga stegen för att slutföra den här kursen, låt oss börja med att få en [introduktion till Generativ AI och LLM:s](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->