# Komma igång med den här kursen

Vi är mycket glada över att du ska börja den här kursen och se vad du blir inspirerad att bygga med Generativ AI!

För att säkerställa din framgång, beskriver den här sidan installationssteg, tekniska krav och var du kan få hjälp om det behövs.

## Installationssteg

För att börja ta den här kursen behöver du genomföra följande steg.

### 1. Forka detta repo

[Forka hela detta repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) till ditt eget GitHub-konto för att kunna ändra någon kod och slutföra utmaningarna. Du kan även [stjärnmärka (🌟) detta repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) för att lättare hitta det och relaterade repos.

### 2. Skapa en codespace

För att undvika beroendeproblem när du kör koden rekommenderar vi att du kör den här kursen i en [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

I din fork: **Code -> Codespaces -> New on main**

![Dialog som visar knappar för att skapa en codespace](../../../translated_images/sv/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Lägg till en hemlighet

1. ⚙️ Kugghjulsikon -> Command Palette -> Codespaces : Manage user secret -> Lägg till en ny hemlighet.
2. Namnge OPENAI_API_KEY, klistra in din nyckel, Spara.

### 3. Vad händer härnäst?

| Jag vill…          | Gå till…                                                              |
|---------------------|----------------------------------------------------------------------|
| Börja Lektion 1     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)  |
| Arbeta offline      | [`setup-local.md`](02-setup-local.md)                                |
| Ställ in en LLM-leverantör | [`providers.md`](03-providers.md)                              |
| Träffa andra deltagare | [Gå med i vår Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Felsökning


| Symptom                                   | Lösning                                                     |
|-------------------------------------------|-------------------------------------------------------------|
| Containerbyggnation fastnar > 10 min      | **Codespaces ➜ “Rebuild Container”**                        |
| `python: command not found`               | Terminalen kopplades inte; klicka **+** ➜ *bash*            |
| `401 Unauthorized` från OpenAI            | Felaktig/utgången `OPENAI_API_KEY`                          |
| VS Code visar “Dev container mounting…”   | Uppdatera webbläsarfliken—Codespaces tappar ibland anslutningen |
| Notebook-kärna saknas                     | Notebook-meny ➜ **Kernel ▸ Select Kernel ▸ Python 3**       |

   Unix-baserade system:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Redigera `.env`-filen**: Öppna `.env`-filen i en textredigerare (t.ex. VS Code, Notepad++ eller någon annan editor). Lägg till följande rader i filen och ersätt platshållarna med din faktiska Microsoft Foundry Models endpoint och nyckel (se [`providers.md`](03-providers.md) för hur du får dessa):

   > **Notera:** GitHub Models (och dess variabel `GITHUB_TOKEN`) kommer att sluta användas i slutet av juli 2026. Använd istället [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Spara filen**: Spara ändringarna och stäng textredigeraren.

5. **Installera `python-dotenv`**: Om du inte redan har det måste du installera paketet `python-dotenv` för att kunna ladda miljövariabler från `.env`-filen till din Python-applikation. Du kan installera det med `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Ladda miljövariabler i ditt Python-skript**: I ditt Python-skript använder du paketet `python-dotenv` för att ladda miljövariablerna från `.env`-filen:

   ```python
   from dotenv import load_dotenv
   import os

   # Ladda miljövariabler från .env-fil
   load_dotenv()

   # Få åtkomst till Microsoft Foundry Models-variablerna
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Klart! Du har framgångsrikt skapat en `.env`-fil, lagt till dina Microsoft Foundry Models-uppgifter och laddat in dem i din Python-applikation.

## Hur man kör lokalt på din dator

För att köra koden lokalt på din dator behöver du ha någon version av [Python installerad](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

För att sedan använda repot behöver du klona det:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

När du har checkat ut allt kan du börja!

## Valfria steg

### Installera Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) är en lättviktig installerare för att installera [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python samt några paket.
Conda är en pakethanterare som gör det enkelt att ställa in och växla mellan olika Python [**virtuella miljöer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) och paket. Det är också användbart för att installera paket som inte är tillgängliga via `pip`.

Du kan följa [MiniConda installationsguiden](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) för att sätta upp det.

Med Miniconda installerat behöver du klona [repositioriet](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (om du inte redan gjort det)

Nästa steg är att skapa en virtuell miljö. För att göra detta med Conda, skapa en ny miljöfil (_environment.yml_). Om du följer med i Codespaces, skapa denna i `.devcontainer`-katalogen, alltså `.devcontainer/environment.yml`.

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

Om du får felmeddelanden när du använder conda kan du manuellt installera Microsoft AI-biblioteken med följande kommando i terminalen.

```
conda install -c microsoft azure-ai-ml
```

Miljöfilen anger vilka beroenden som behövs. `<environment-name>` är namnet du vill använda för din Conda-miljö och `<python-version>` är Python-versionen du vill använda, till exempel `3` för den senaste huvudversionen av Python.

När detta är klart kan du skapa din Conda-miljö genom att köra kommandona nedan i din kommandorad/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer delväg gäller endast för Codespace-konfigurationer
conda activate ai4beg
```

Se [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) om du stöter på problem.

### Använda Visual Studio Code med Python-stöd

Vi rekommenderar att använda [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) med [Python-supporttillägget](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installerat för den här kursen. Detta är dock en rekommendation och inte ett krav.

> **Notera**: Genom att öppna kursens repo i VS Code har du möjlighet att konfigurera projektet inom en container. Detta är tack vare den [speciella `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) mappen som finns i repo. Mer om detta senare.

> **Notera**: När du klonar och öppnar mappen i VS Code kommer det automatiskt att föreslå att du installerar ett Python-supporttillägg.

> **Notera**: Om VS Code föreslår att du öppnar repon i en container, avböj detta för att använda den lokalt installerade versionen av Python.

### Använda Jupyter i webbläsaren

Du kan också arbeta med projektet via [Jupyter-miljön](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direkt i din webbläsare. Både klassisk Jupyter och [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) erbjuder en behaglig utvecklingsmiljö med funktioner som autokomplettering, kodmarkering med mera.

För att starta Jupyter lokalt, öppna terminalen, navigera till kursmappen och kör:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Detta startar en Jupyter-instans och URL:en för åtkomst visas i terminalfönstret.

När du går till URL:en bör du se kursöversikten och kunna navigera till valfri `*.ipynb`-fil, till exempel `08-building-search-applications/python/oai-solution.ipynb`.

### Köra i en container

Ett alternativ till att ställa in allt på din dator eller Codespace är att använda en [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Den speciella `.devcontainer`-mappen i kursrepositoriet gör det möjligt för VS Code att konfigurera projektet i en container. Utanför Codespaces krävs installation av Docker och är ärligt talat lite mer arbete, så vi rekommenderar detta endast för dig som har erfarenhet av att arbeta med containers.

Ett av de bästa sätten att skydda dina API-nycklar när du använder GitHub Codespaces är att använda Codespace Secrets. Följ guiden om [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) för att lära dig mer.


## Lektioner och tekniska krav

Kursen har "Learn"-lektioner som förklarar koncept inom Generativ AI och "Build"-lektioner med praktiska kodexempel, både i **Python** och **TypeScript** där det är möjligt.

För kodningslektionerna använder vi Azure OpenAI i Microsoft Foundry. Du behöver en Azure-prenumeration och en API-nyckel. Åtkomsten är öppen - ingen ansökan krävs - så du kan [skapa en Microsoft Foundry-resurs och distribuera en modell](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) för att få din endpoint och nyckel.

Varje kodningslektion inkluderar också en `README.md`-fil där du kan se koden och resultaten utan att köra något.

## Använda Azure OpenAI-tjänsten för första gången

Om detta är första gången du arbetar med Azure OpenAI-tjänsten, följ denna guide om hur du [skapar och distribuerar en Azure OpenAI-tjänstresurs.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Använda OpenAI-API:et för första gången

Om detta är första gången du arbetar med OpenAI-API:et, följ guiden om hur du [skapar och använder gränssnittet.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Träffa andra deltagare

Vi har skapat kanaler i vår officiella [AI Community Discord-server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) för att du ska kunna träffa andra deltagare. Detta är ett utmärkt sätt att nätverka med likasinnade entreprenörer, utvecklare, studenter och alla som vill ta nästa steg inom Generativ AI.

[![Gå med i Discord-kanalen](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektteamet kommer också finnas på den här Discord-servern för att hjälpa deltagare.

## Bidra

Den här kursen är ett öppen källkodsinitiativ. Om du ser förbättringsområden eller problem, vänligen skapa en [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) eller rapportera ett [GitHub-issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektteamet följer alla bidrag. Att bidra till öppen källkod är ett fantastiskt sätt att bygga din karriär inom Generativ AI.

De flesta bidrag kräver att du godkänner ett Contributor License Agreement (CLA), som intygar att du har rätt att och faktiskt ger oss rätten att använda ditt bidrag. För detaljer besök [CLA, Contributor License Agreement-webbplatsen](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Viktigt: när du översätter text i detta repo, se till att inte använda maskinöversättning. Vi kommer att verifiera översättningarna via communityn, så vänligen anmäl dig endast till översättningar på språk där du är flytande.


När du skickar in en pull-begäran kommer en CLA-bot automatiskt att avgöra om du behöver tillhandahålla en CLA och märka PR:n på lämpligt sätt (t.ex. etikett, kommentar). Följ helt enkelt instruktionerna som boten ger. Du behöver bara göra detta en gång för alla arkiv som använder vår CLA.

Detta projekt har antagit [Microsofts öppna källkodsbeteendekod](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). För mer information, läs vanliga frågor om uppförandekoden eller kontakta [Email opencode](opencode@microsoft.com) med eventuella ytterligare frågor eller kommentarer.

## Låt oss komma igång

Nu när du har slutfört de nödvändiga stegen för att slutföra denna kurs, låt oss börja med att få en [introduktion till Generativ AI och LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->