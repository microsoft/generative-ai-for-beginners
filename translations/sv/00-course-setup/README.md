# Kom igång med denna kurs

Vi är mycket glada över att du ska börja denna kurs och se vad du blir inspirerad att skapa med Generativ AI!

För att säkerställa din framgång beskriver denna sida installationssteg, tekniska krav och var du kan få hjälp vid behov.

## Installationssteg

För att börja ta denna kurs behöver du slutföra följande steg.

### 1. Forka detta repo

[Forka hela detta repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) till ditt eget GitHub-konto för att kunna ändra kod och slutföra utmaningarna. Du kan också [stjärnmärka (🌟) detta repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) för att lättare hitta det och relaterade repos.

### 2. Skapa en codespace

För att undvika beroendeproblem när du kör koden rekommenderar vi att köra kursen i en [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

I din fork: **Code -> Codespaces -> New on main**

![Dialog som visar knappar för att skapa en codespace](../../../translated_images/sv/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Lägg till en hemlighet

1. ⚙️ Kugghjulsikon -> Command Palette -> Codespaces : Manage user secret -> Add a new secret.
2. Namnge OPENAI_API_KEY, klistra in din nyckel, Spara.

### 3. Vad händer härnäst?

| Jag vill…            | Gå till…                                                                 |
|---------------------|-------------------------------------------------------------------------|
| Starta Lektion 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Arbeta offline       | [`setup-local.md`](02-setup-local.md)                                   |
| Ställ in en LLM-leverantör | [`providers.md`](03-providers.md)                                   |
| Möt andra deltagare  | [Gå med i vår Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Felsökning


| Symptom                                   | Lösning                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| Containerbygge fastnar > 10 min            | **Codespaces ➜ "Rebuild Container"**                           |
| `python: command not found`               | Terminalen anslöt inte; klicka **+** ➜ *bash*                  |
| `401 Unauthorized` från OpenAI            | Felaktig / utgången `OPENAI_API_KEY`                           |
| VS Code visar “Dev container mounting…”   | Uppdatera webbläsarfliken — Codespaces tappar ibland anslutning |
| Notebook-kärna saknas                     | Notebook-meny ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

   Unix-baserade system:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Redigera `.env`-filen**: Öppna `.env`-filen i en textredigerare (t.ex. VS Code, Notepad++ eller annan). Lägg till följande rader i filen och ersätt platshållarna med din faktiska Microsoft Foundry Models-endpoint och nyckel (se [`providers.md`](03-providers.md) för hur du skaffar dessa):

   > **Observera:** GitHub Models (och dess `GITHUB_TOKEN` variabel) pensioneras i slutet av juli 2026. Använd istället [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Spara filen**: Spara ändringarna och stäng textredigeraren.

5. **Installera `python-dotenv`**: Om du inte redan har gjort det behöver du installera paketet `python-dotenv` för att läsa miljövariabler från `.env`-filen i din Python-app. Du kan installera det via `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Läs in miljövariabler i ditt Python-skript**: I ditt Python-skript, använd paketet `python-dotenv` för att läsa in miljövariablerna från `.env`-filen:

   ```python
   from dotenv import load_dotenv
   import os

   # Läs in miljövariabler från .env-fil
   load_dotenv()

   # Få tillgång till Microsoft Foundry Models-variablerna
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Det är allt! Du har nu skapat en `.env`-fil, lagt till dina Microsoft Foundry Models-uppgifter och laddat dem i din Python-app.

## Hur man kör lokalt på din dator

För att köra koden lokalt på din dator behöver du ha någon version av [Python installerat](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

För att sedan använda repot behöver du klona det:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

När du har allt checkat ut kan du börja!

## Valfria steg

### Installera Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) är en lättviktsinstallatör för att installera [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python samt några paket.
Conda är i sig en paketansvarig som gör det enkelt att sätta upp och växla mellan olika Python [**virtuella miljöer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) och paket. Den är också praktisk för att installera paket som inte finns via `pip`.

Följ [MiniConda installationsguide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) för att installera den.

Med Miniconda installerat behöver du klona [repositorn](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (om du inte redan gjort det)

Därefter behöver du skapa en virtuell miljö. För att göra detta med Conda, skapa en ny miljöfil (_environment.yml_). Om du följer med i Codespaces, skapa denna i `.devcontainer`-katalogen, alltså `.devcontainer/environment.yml`.

Fyll i din miljöfil med nedanstående snippet:

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

Om du får fel med conda kan du manuellt installera Microsoft AI Libraries med följande kommando i terminalen.

```
conda install -c microsoft azure-ai-ml
```

Miljöfilen specificerar de beroenden vi behöver. `<environment-name>` är namnet du vill använda för din Conda-miljö, och `<python-version>` är Python-versionen du vill använda, till exempel `3` som är senaste större versionen.

När det är gjort kan du skapa din Conda-miljö genom att köra kommandona nedan i din kommandotolk/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub-sökväg gäller endast för Codespace-konfigurationer
conda activate ai4beg
```

Se [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) om du stöter på problem.

### Använda Visual Studio Code med Python-stödsutökning

Vi rekommenderar att använda [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editorn med [Python-stödsutökningen](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installerad för denna kurs. Detta är dock en rekommendation och inte ett absolut krav.

> **Observera**: Genom att öppna kursrepo i VS Code har du möjligheten att sätta upp projektet inom en container. Detta tack vare den [speciella `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)-mappen i kursrepo. Mer om detta senare.

> **Observera**: När du klonar och öppnar mappen i VS Code kommer den automatiskt föreslå att du installerar en Python-stödsutökning.

> **Observera**: Om VS Code föreslår att du öppnar repot i en container, tacka nej till detta för att använda den lokala Pythonversionen.

### Använda Jupyter i webbläsaren

Du kan också arbeta med projektet i [Jupyter-miljön](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direkt i din webbläsare. Både klassiska Jupyter och [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) erbjuder en trevlig utvecklingsmiljö med funktioner som autokomplettering, kodmarkering osv.

För att starta Jupyter lokalt, gå till terminalen/kommandorad, navigera till kurskatalogen och kör:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Detta startar en Jupyter-instans och URL för åtkomst visas i kommandotolksfönstret.

När du öppnar URL:en bör du se kursens innehållsförteckning och kunna navigera till valfri `*.ipynb`-fil. Till exempel `08-building-search-applications/python/oai-solution.ipynb`.

### Köra i en container

Ett alternativ till att sätta upp allt på datorn eller i Codespace är att använda en [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Den speciella `.devcontainer`-mappen i kursrepo gör det möjligt för VS Code att sätta upp projektet i en container. Utanför Codespaces kräver detta installation av Docker och är ganska komplext, så vi rekommenderar detta endast för dem med erfarenhet av containers.

Ett av de bästa sätten att hålla dina API-nycklar säkra vid användning av GitHub Codespaces är genom Codespace Secrets. Följ [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guiden för att lära dig mer om detta.


## Lektioner och tekniska krav

Kursen innehåller 6 konceptlektioner och 6 kodningslektioner.

För kodningslektionerna använder vi Azure OpenAI Service. Du behöver tillgång till Azure OpenAI service och en API-nyckel för att köra koden. Du kan ansöka om tillgång genom att [fylla i denna ansökan](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Medan du väntar på att ansökan behandlas innehåller varje kodningslektion även en `README.md`-fil där du kan se koden och dess resultat.

## Använda Azure OpenAI Service för första gången

Om detta är första gången du arbetar med Azure OpenAI service, följ denna guide om hur du [skapar och distribuerar en Azure OpenAI Service-resurs.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Använda OpenAI API för första gången

Om du är ny med OpenAI API, följ guiden om hur du [skapar och använder gränssnittet.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Möt andra deltagare

Vi har skapat kanaler i vår officiella [AI Community Discord-server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) för att träffa andra deltagare. Detta är ett utmärkt sätt att nätverka med likasinnade entreprenörer, utvecklare, studenter och alla som vill förbättra sina kunskaper i Generativ AI.

[![Gå med i discord-kanal](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektteamet finns också på denna Discord-server för att hjälpa deltagare.

## Bidra

Denna kurs är ett open-source-initiativ. Om du ser förbättringsområden eller problem, skapa gärna en [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) eller rapportera en [GitHub-issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektteamet följer alla bidrag. Att bidra till open source är ett fantastiskt sätt att bygga din karriär inom Generativ AI.

De flesta bidrag kräver att du godkänner ett Contributor License Agreement (CLA) där du intygar att du har rätt att och faktiskt ger oss rättigheter att använda ditt bidrag. För detaljer, besök [CLA, Contributor License Agreement-webbplatsen](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Viktigt: när du översätter text i detta repo, använd inte maskinöversättning. Vi kommer att verifiera översättningar via communityn, så anmäl dig endast för översättningar på språk där du är skicklig.

När du skickar en pull request kommer en CLA-bot automatiskt avgöra om du behöver lämna CLA och märka PR:n på lämpligt sätt (t.ex. etikett, kommentar). Följ bara instruktionerna från boten. Detta behöver du bara göra en gång för alla repositories som använder vår CLA.


Detta projekt har antagit [Microsofts öppna källkodskod för uppförande](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). För mer information, läs FAQ för uppförandekoden eller kontakta [Email opencode](opencode@microsoft.com) med eventuella ytterligare frågor eller kommentarer.

## Låt oss komma igång

Nu när du har slutfört de nödvändiga stegen för att genomföra den här kursen, låt oss börja med att få en [introduktion till Generativ AI och LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->