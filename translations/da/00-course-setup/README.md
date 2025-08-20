<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T07:11:15+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "da"
}
-->
# Kom godt i gang med dette kursus

Vi er meget begejstrede for, at du skal i gang med dette kursus og se, hvad du bliver inspireret til at bygge med Generativ AI!

For at sikre din succes beskriver denne side opsætningsprocessen, tekniske krav og hvor du kan få hjælp, hvis det bliver nødvendigt.

## Opsætningstrin

For at komme i gang med kurset skal du gennemføre følgende trin.

### 1. Fork dette repo

[Fork hele dette repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) til din egen GitHub-konto, så du kan ændre i koden og løse udfordringerne. Du kan også [starte (🌟) dette repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) for nemmere at finde det og relaterede repos.

### 2. Opret en codespace

For at undgå afhængighedsproblemer, når du kører koden, anbefaler vi at køre kurset i en [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Dette kan oprettes ved at vælge `Code`-muligheden på din forkede version af dette repo og derefter vælge **Codespaces**.

![Dialog der viser knapper til at oprette en codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Opbevaring af dine API-nøgler

Det er vigtigt at holde dine API-nøgler sikre, når du bygger applikationer. Vi anbefaler, at du ikke gemmer API-nøgler direkte i din kode. Hvis disse oplysninger bliver committet til et offentligt repository, kan det føre til sikkerhedsproblemer og uønskede omkostninger, hvis de misbruges af uvedkommende.  
Her er en trin-for-trin guide til, hvordan du opretter en `.env`-fil til Python og tilføjer `GITHUB_TOKEN`:

1. **Naviger til dit projektmappe**: Åbn din terminal eller kommandoprompt og gå til rodmappen for dit projekt, hvor du vil oprette `.env`-filen.

   ```bash
   cd path/to/your/project
   ```

2. **Opret `.env`-filen**: Brug din foretrukne teksteditor til at oprette en ny fil med navnet `.env`. Hvis du bruger kommandolinjen, kan du bruge `touch` (på Unix-baserede systemer) eller `echo` (på Windows):

   Unix-baserede systemer:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Rediger `.env`-filen**: Åbn `.env`-filen i en teksteditor (f.eks. VS Code, Notepad++ eller en anden editor). Tilføj følgende linje, hvor du erstatter `your_github_token_here` med din faktiske GitHub-token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Gem filen**: Gem ændringerne og luk teksteditoren.

5. **Installer `python-dotenv`**: Hvis du ikke allerede har det, skal du installere pakken `python-dotenv` for at kunne indlæse miljøvariabler fra `.env`-filen i din Python-applikation. Det kan du gøre med `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Indlæs miljøvariabler i dit Python-script**: I dit Python-script skal du bruge `python-dotenv` til at indlæse miljøvariablerne fra `.env`-filen:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Så er du klar! Du har nu oprettet en `.env`-fil, tilføjet din GitHub-token og indlæst den i din Python-applikation.

## Sådan kører du lokalt på din computer

For at køre koden lokalt på din computer skal du have en version af [Python installeret](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

For at bruge repositoryet skal du klone det:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Når du har hentet alt, kan du gå i gang!

## Valgfrie trin

### Installation af Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) er en letvægtsinstaller til installation af [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python samt nogle få pakker.  
Conda er en pakkehåndtering, der gør det nemt at opsætte og skifte mellem forskellige Python [**virtuelle miljøer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) og pakker. Det er også nyttigt til at installere pakker, som ikke findes via `pip`.

Du kan følge [MiniConda installationsguiden](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) for at sætte det op.

Når Miniconda er installeret, skal du klone [repositoryet](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (hvis du ikke allerede har gjort det).

Dernæst skal du oprette et virtuelt miljø. For at gøre dette med Conda, opret en ny miljøfil (_environment.yml_). Hvis du følger med i Codespaces, skal du oprette denne i `.devcontainer`-mappen, altså `.devcontainer/environment.yml`.

Fyld din miljøfil med følgende snippet:

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

Hvis du oplever fejl med conda, kan du manuelt installere Microsoft AI Libraries med følgende kommando i terminalen.

```
conda install -c microsoft azure-ai-ml
```

Miljøfilen angiver de afhængigheder, vi har brug for. `<environment-name>` er navnet på dit Conda-miljø, og `<python-version>` er den version af Python, du ønsker at bruge, for eksempel `3` som den nyeste store version.

Når det er gjort, kan du oprette dit Conda-miljø ved at køre kommandoerne nedenfor i din kommandolinje/terminal:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Se [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), hvis du støder på problemer.

### Brug af Visual Studio Code med Python-udvidelsen

Vi anbefaler at bruge [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) med [Python-udvidelsen](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installeret til dette kursus. Det er dog kun en anbefaling og ikke et krav.

> **Note**: Når du åbner kursus-repositoryet i VS Code, har du mulighed for at opsætte projektet i en container. Det skyldes den [specielle `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) mappe i repositoryet. Mere om dette senere.

> **Note**: Når du har klonet og åbnet mappen i VS Code, vil den automatisk foreslå, at du installerer Python-udvidelsen.

> **Note**: Hvis VS Code foreslår, at du genåbner repositoryet i en container, skal du afslå dette for at bruge den lokalt installerede version af Python.

### Brug af Jupyter i browseren

Du kan også arbejde på projektet ved hjælp af [Jupyter-miljøet](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direkte i din browser. Både klassisk Jupyter og [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) giver et behageligt udviklingsmiljø med funktioner som autoudfyldelse, kodefremhævning osv.

For at starte Jupyter lokalt, gå til terminalen/kommandolinjen, naviger til kursusmappen og kør:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Dette starter en Jupyter-instans, og URL’en til at tilgå den vises i kommandolinjevinduet.

Når du åbner URL’en, bør du kunne se kursusoversigten og navigere til enhver `*.ipynb`-fil. For eksempel `08-building-search-applications/python/oai-solution.ipynb`.

### Kørsel i en container

Et alternativ til at sætte alt op på din computer eller i Codespace er at bruge en [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Den specielle `.devcontainer`-mappe i kursus-repositoryet gør det muligt for VS Code at opsætte projektet i en container. Uden for Codespaces kræver dette installation af Docker, og det kan være lidt kompliceret, så vi anbefaler kun dette for dem med erfaring i at arbejde med containere.

En af de bedste måder at holde dine API-nøgler sikre i GitHub Codespaces er ved at bruge Codespace Secrets. Følg venligst [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guiden for at lære mere.

## Lektioner og tekniske krav

Kurset består af 6 konceptlektioner og 6 kodningslektioner.

Til kodningslektionerne bruger vi Azure OpenAI Service. Du skal have adgang til Azure OpenAI service og en API-nøgle for at kunne køre koden. Du kan ansøge om adgang ved at [udfylde denne ansøgning](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Mens du venter på, at din ansøgning bliver behandlet, indeholder hver kodningslektion også en `README.md`-fil, hvor du kan se koden og resultaterne.

## Brug af Azure OpenAI Service for første gang

Hvis det er første gang, du arbejder med Azure OpenAI service, så følg denne guide til, hvordan du [opretter og deployerer en Azure OpenAI Service-ressource.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Brug af OpenAI API for første gang

Hvis det er første gang, du arbejder med OpenAI API, så følg guiden til, hvordan du [opretter og bruger interfacet.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Mød andre kursister

Vi har oprettet kanaler i vores officielle [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) til at møde andre kursister. Det er en god måde at netværke med ligesindede iværksættere, udviklere, studerende og alle, der ønsker at blive bedre til Generativ AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektteamet vil også være til stede på denne Discord-server for at hjælpe kursister.

## Bidrag

Dette kursus er et open source-initiativ. Hvis du ser forbedringsmuligheder eller fejl, så opret venligst en [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) eller log en [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektteamet følger alle bidrag. At bidrage til open source er en fantastisk måde at opbygge din karriere inden for Generativ AI.

De fleste bidrag kræver, at du accepterer en Contributor License Agreement (CLA), som erklærer, at du har ret til og faktisk giver os rettighederne til at bruge dit bidrag. For detaljer, se [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Vigtigt: Når du oversætter tekst i dette repo, skal du sikre dig, at du ikke bruger maskinoversættelse. Vi vil verificere oversættelser via fællesskabet, så meld dig kun til oversættelser på sprog, du er flydende i.

Når du opretter en pull request, vil en CLA-bot automatisk afgøre, om du skal indsende en CLA og markere PR’en korrekt (f.eks. med label eller kommentar). Følg blot instruktionerne fra botten. Du skal kun gøre dette én gang på tværs af alle repositories, der bruger vores CLA.

Dette projekt har tilsluttet sig [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). For mere information, læs Code of Conduct FAQ eller kontakt [Email opencode](opencode@microsoft.com) med spørgsmål eller kommentarer.

## Lad os komme i gang

Nu hvor du har gennemført de nødvendige trin for at gennemføre kurset, så lad os komme i gang med en [introduktion til Generativ AI og LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.