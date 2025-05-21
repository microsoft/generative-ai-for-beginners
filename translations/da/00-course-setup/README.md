<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-05-19T12:28:21+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "da"
}
-->
# Kom godt i gang med dette kursus

Vi er meget begejstrede for, at du starter dette kursus og ser, hvad du bliver inspireret til at bygge med Generativ AI!

For at sikre din succes beskriver denne side opsætningstrin, tekniske krav og hvor du kan få hjælp, hvis det er nødvendigt.

## Opsætningstrin

For at begynde at tage dette kursus skal du fuldføre følgende trin.

### 1. Fork dette Repo

[Fork hele dette repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) til din egen GitHub-konto for at kunne ændre enhver kode og fuldføre udfordringerne. Du kan også [star (🌟) dette repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) for lettere at finde det og relaterede repos.

### 2. Opret en codespace

For at undgå afhængighedsproblemer, når du kører koden, anbefaler vi at køre dette kursus i en [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Dette kan oprettes ved at vælge `Code`-muligheden på din forkede version af dette repo og vælge **Codespaces**-muligheden.

![Dialog der viser knapper til at oprette en codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Opbevaring af dine API-nøgler

Det er vigtigt at holde dine API-nøgler sikre, når du bygger enhver form for applikation. Vi anbefaler ikke at opbevare nogen API-nøgler direkte i din kode. At begå disse detaljer til et offentligt repository kan resultere i sikkerhedsproblemer og endda uønskede omkostninger, hvis de bruges af en dårlig aktør.
Her er en trin-for-trin guide til, hvordan du opretter en `.env`-fil til Python og tilføjer `GITHUB_TOKEN`:

1. **Naviger til din projektmappe**: Åbn din terminal eller kommandoprompt og naviger til projektets rodmappe, hvor du vil oprette `.env`-filen.

   ```bash
   cd path/to/your/project
   ```

2. **Opret `.env`-filen**: Brug din foretrukne teksteditor til at oprette en ny fil med navnet `.env`. Hvis du bruger kommandolinjen, kan du bruge `touch` (on Unix-based systems) or `echo` (på Windows):

   Unix-baserede systemer:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Rediger `.env`-filen**: Åbn `.env`-filen i en teksteditor (f.eks. VS Code, Notepad++ eller en anden editor). Tilføj følgende linje til filen, og erstat `your_github_token_here` med din faktiske GitHub-token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Gem filen**: Gem ændringerne og luk teksteditoren.

5. **Installer `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv`-pakken for at indlæse miljøvariabler fra `.env`-filen i din Python-applikation. Du kan installere den ved hjælp af `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Indlæs miljøvariabler i dit Python-script**: Brug `python-dotenv`-pakken i dit Python-script til at indlæse miljøvariabler fra `.env`-filen:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Det var det! Du har succesfuldt oprettet en `.env`-fil, tilføjet din GitHub-token og indlæst den i din Python-applikation.

## Sådan kører du lokalt på din computer

For at køre koden lokalt på din computer, skal du have en version af [Python installeret](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

For derefter at bruge repository, skal du klone det:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Når du har alt tjekket ud, kan du komme i gang!

## Valgfrie trin

### Installere Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) er en letvægtsinstallationsprogram til installation af [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python samt nogle få pakker.
Conda i sig selv er en pakkemanager, der gør det nemt at opsætte og skifte mellem forskellige Python [**virtuelle miljøer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) og pakker. Det er også praktisk til installation af pakker, der ikke er tilgængelige via `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Gå videre og fyld din miljøfil med nedenstående snippet:

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

Hvis du oplever fejl ved brug af conda, kan du manuelt installere Microsoft AI Libraries ved at bruge følgende kommando i en terminal.

```
conda install -c microsoft azure-ai-ml
```

Miljøfilen specificerer de afhængigheder, vi har brug for. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` er den nyeste større version af Python.

Når det er gjort, kan du gå videre og oprette dit Conda-miljø ved at køre kommandoerne nedenfor i din kommandolinje/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Se [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) hvis du støder på problemer.

### Brug af Visual Studio Code med Python support-udvidelsen

Vi anbefaler at bruge [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editoren med [Python support-udvidelsen](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installeret til dette kursus. Dette er dog mere en anbefaling og ikke et definitivt krav.

> **Bemærk**: Ved at åbne kursusrepositoryet i VS Code har du mulighed for at opsætte projektet inden for en container. Dette skyldes den [specielle `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) mappe, der findes inden for kursusrepositoryet. Mere om dette senere.

> **Bemærk**: Når du kloner og åbner mappen i VS Code, vil det automatisk foreslå dig at installere en Python support-udvidelse.

> **Bemærk**: Hvis VS Code foreslår, at du genåbner repositoryet i en container, afvis denne anmodning for at bruge den lokalt installerede version af Python.

### Brug af Jupyter i browseren

Du kan også arbejde på projektet ved hjælp af [Jupyter-miljøet](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direkte i din browser. Både klassisk Jupyter og [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) giver et ret behageligt udviklingsmiljø med funktioner som auto-fuldførelse, kodefremhævning osv.

For at starte Jupyter lokalt, gå til terminalen/kommandolinjen, naviger til kursusmappen, og udfør:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Dette vil starte en Jupyter-instans, og URL'en til at få adgang til den vil blive vist i kommandolinjevinduet.

Når du får adgang til URL'en, bør du se kursusoversigten og kunne navigere til enhver `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` fil, hvor du kan se koden og output.

## Brug af Azure OpenAI Service for første gang

Hvis dette er første gang, du arbejder med Azure OpenAI-tjenesten, skal du følge denne vejledning om, hvordan du [opretter og implementerer en Azure OpenAI Service-ressource.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Brug af OpenAI API for første gang

Hvis dette er første gang, du arbejder med OpenAI API, skal du følge vejledningen om, hvordan du [opretter og bruger interfacet.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Mød andre elever

Vi har oprettet kanaler på vores officielle [AI Community Discord-server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) for at møde andre elever. Dette er en fantastisk måde at netværke med andre ligesindede iværksættere, bygherrer, studerende og alle, der ønsker at forbedre sig inden for Generativ AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektteamet vil også være på denne Discord-server for at hjælpe enhver elev.

## Bidrage

Dette kursus er en open-source-initiativ. Hvis du ser områder til forbedring eller problemer, skal du oprette en [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) eller logge et [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektteamet vil følge alle bidrag. At bidrage til open source er en fantastisk måde at bygge din karriere inden for Generativ AI.

De fleste bidrag kræver, at du accepterer en Contributor License Agreement (CLA), der erklærer, at du har ret til og faktisk giver os rettighederne til at bruge dit bidrag. For detaljer, besøg [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Vigtigt: når du oversætter tekst i dette repo, skal du sørge for ikke at bruge maskinoversættelse. Vi vil verificere oversættelser via fællesskabet, så vær venlig kun at melde dig til oversættelser på sprog, hvor du er dygtig.

Når du sender en pull request, vil en CLA-bot automatisk afgøre, om du skal give en CLA og dekorere PR'en passende (f.eks. label, kommentar). Følg blot de instruktioner, der gives af botten. Du skal kun gøre dette én gang på tværs af alle repositories, der bruger vores CLA.

Dette projekt har vedtaget [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). For mere information, læs Code of Conduct FAQ eller kontakt [Email opencode](opencode@microsoft.com) med eventuelle yderligere spørgsmål eller kommentarer.

## Lad os komme i gang

Nu hvor du har fuldført de nødvendige trin for at fuldføre dette kursus, lad os komme i gang med at få en [introduktion til Generativ AI og LLM'er](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiske oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.