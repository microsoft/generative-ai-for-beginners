<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-17T19:10:25+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "da"
}
-->
# Kom godt i gang med dette kursus

Vi er meget begejstrede for, at du starter dette kursus og ser, hvad du bliver inspireret til at bygge med Generativ AI!

For at sikre din succes beskriver denne side opsætningstrin, tekniske krav og hvor du kan få hjælp, hvis det er nødvendigt.

## Opsætningstrin

For at begynde på dette kursus skal du fuldføre følgende trin.

### 1. Fork denne repo

[Fork hele denne repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) til din egen GitHub-konto for at kunne ændre kode og fuldføre udfordringerne. Du kan også [stjerne (🌟) denne repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) for nemmere at finde den og relaterede repos.

### 2. Opret en codespace

For at undgå afhængighedsproblemer, når du kører koden, anbefaler vi at køre dette kursus i en [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

I din fork: **Code -> Codespaces -> New on main**

![Dialog der viser knapper til at oprette en codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Tilføj en hemmelighed

1. ⚙️ Gear-ikon -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Navngiv OPENAI_API_KEY, indsæt din nøgle, Gem.

### 3. Hvad er det næste?

| Jeg vil…            | Gå til…                                                                 |
|---------------------|-------------------------------------------------------------------------|
| Starte Lektion 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Arbejde offline     | [`setup-local.md`](02-setup-local.md)                                   |
| Opsætte en LLM-udbyder | [`providers.md`](03-providers.md)                                        |
| Møde andre lærende  | [Deltag i vores Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Fejlfinding

| Symptom                                   | Løsning                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| Container build sidder fast > 10 min      | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal blev ikke tilsluttet; klik **+** ➜ *bash*              |
| `401 Unauthorized` fra OpenAI             | Forkert / udløbet `OPENAI_API_KEY`                              |
| VS Code viser “Dev container mounting…”   | Opdater browserfanen—Codespaces mister nogle gange forbindelsen |
| Notebook kernel mangler                   | Notebook menu ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

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

5. **Installer `python-dotenv`**: Hvis du ikke allerede har gjort det, skal du installere `python-dotenv`-pakken for at indlæse miljøvariabler fra `.env`-filen i din Python-applikation. Du kan installere den med `pip`:

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

Det er det! Du har succesfuldt oprettet en `.env`-fil, tilføjet din GitHub-token og indlæst den i din Python-applikation.

## Sådan kører du lokalt på din computer

For at køre koden lokalt på din computer skal du have en version af [Python installeret](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

For derefter at bruge repositoryen skal du klone den:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Når du har alt tjekket ud, kan du komme i gang!

## Valgfrie trin

### Installation af Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) er en letvægtsinstaller til installation af [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python samt nogle få pakker.
Conda er en pakkehåndtering, der gør det nemt at opsætte og skifte mellem forskellige Python [**virtuelle miljøer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) og pakker. Det er også nyttigt til at installere pakker, der ikke er tilgængelige via `pip`.

Du kan følge [MiniConda installationsguiden](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) for at sætte det op.

Med Miniconda installeret skal du klone [repositoryen](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (hvis du ikke allerede har gjort det).

Derefter skal du oprette et virtuelt miljø. For at gøre dette med Conda skal du oprette en ny miljøfil (_environment.yml_). Hvis du følger med ved hjælp af Codespaces, skal du oprette denne inden for `.devcontainer`-mappen, altså `.devcontainer/environment.yml`.

Gå videre og udfyld din miljøfil med nedenstående snippet:

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

Hvis du oplever fejl med conda, kan du manuelt installere Microsoft AI Libraries ved hjælp af følgende kommando i en terminal.

```
conda install -c microsoft azure-ai-ml
```

Miljøfilen specificerer de nødvendige afhængigheder. `<environment-name>` refererer til det navn, du ønsker at bruge til dit Conda-miljø, og `<python-version>` er den version af Python, du ønsker at bruge, for eksempel `3`, som er den nyeste hovedversion af Python.

Når det er gjort, kan du oprette dit Conda-miljø ved at køre nedenstående kommandoer i din kommandolinje/terminal:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Se [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), hvis du støder på problemer.

### Brug af Visual Studio Code med Python-supportudvidelsen

Vi anbefaler at bruge [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editoren med [Python-supportudvidelsen](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installeret til dette kursus. Dette er dog mere en anbefaling end et krav.

> **Bemærk**: Ved at åbne kursusrepositoryen i VS Code har du mulighed for at opsætte projektet inden for en container. Dette skyldes den [specielle `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) mappe, der findes i kursusrepositoryen. Mere om dette senere.

> **Bemærk**: Når du kloner og åbner mappen i VS Code, vil det automatisk foreslå, at du installerer en Python-supportudvidelse.

> **Bemærk**: Hvis VS Code foreslår, at du genåbner repositoryen i en container, skal du afvise denne anmodning for at bruge den lokalt installerede version af Python.

### Brug af Jupyter i browseren

Du kan også arbejde på projektet ved hjælp af [Jupyter-miljøet](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direkte i din browser. Både klassisk Jupyter og [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) giver en behagelig udviklingsoplevelse med funktioner som autoudfyldning, kodefremhævning osv.

For at starte Jupyter lokalt skal du gå til terminalen/kommandolinjen, navigere til kursusmappen og udføre:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Dette vil starte en Jupyter-instans, og URL'en for adgang vil blive vist i kommandolinjevinduet.

Når du får adgang til URL'en, bør du se kursusoversigten og kunne navigere til enhver `*.ipynb`-fil. For eksempel `08-building-search-applications/python/oai-solution.ipynb`.

### Kørsel i en container

Et alternativ til at opsætte alt på din computer eller Codespace er at bruge en [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Den specielle `.devcontainer`-mappe i kursusrepositoryen gør det muligt for VS Code at opsætte projektet inden for en container. Uden for Codespaces kræver dette installation af Docker, og det involverer ærligt talt en del arbejde, så vi anbefaler dette kun til dem med erfaring med at arbejde med containere.

En af de bedste måder at holde dine API-nøgler sikre, når du bruger GitHub Codespaces, er ved at bruge Codespace Secrets. Følg venligst [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guiden for at lære mere om dette.

## Lektioner og tekniske krav

Kurset har 6 konceptuelle lektioner og 6 kodningslektioner.

Til kodningslektionerne bruger vi Azure OpenAI Service. Du skal have adgang til Azure OpenAI Service og en API-nøgle for at køre denne kode. Du kan ansøge om adgang ved at [udfylde denne ansøgning](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Mens du venter på, at din ansøgning bliver behandlet, inkluderer hver kodningslektion også en `README.md`-fil, hvor du kan se koden og output.

## Brug af Azure OpenAI Service for første gang

Hvis det er første gang, du arbejder med Azure OpenAI Service, skal du følge denne guide til, hvordan du [opretter og implementerer en Azure OpenAI Service-ressource.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Brug af OpenAI API for første gang

Hvis det er første gang, du arbejder med OpenAI API, skal du følge guiden til, hvordan du [opretter og bruger interfacet.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Mød andre lærende

Vi har oprettet kanaler i vores officielle [AI Community Discord-server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) for at møde andre lærende. Dette er en fantastisk måde at netværke med andre ligesindede entreprenører, udviklere, studerende og alle, der ønsker at forbedre sig inden for Generativ AI.

[![Deltag i Discord-kanalen](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektteamet vil også være på denne Discord-server for at hjælpe lærende.

## Bidrag

Dette kursus er en open-source-initiativ. Hvis du ser områder, der kan forbedres eller problemer, skal du oprette en [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) eller logge et [GitHub-issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektteamet vil spore alle bidrag. At bidrage til open source er en fantastisk måde at opbygge din karriere inden for Generativ AI.

De fleste bidrag kræver, at du accepterer en Contributor License Agreement (CLA), der erklærer, at du har ret til og faktisk giver os rettighederne til at bruge dit bidrag. For detaljer, besøg [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Vigtigt: Når du oversætter tekst i denne repo, skal du sikre dig, at du ikke bruger maskinoversættelse. Vi vil verificere oversættelser via fællesskabet, så venligst kun frivilligt oversæt til sprog, hvor du er dygtig.

Når du indsender en pull request, vil en CLA-bot automatisk afgøre, om du skal give en CLA og dekorere PR'en passende (f.eks. label, kommentar). Følg blot instruktionerne fra botten. Du skal kun gøre dette én gang på tværs af alle repositories, der bruger vores CLA.

Dette projekt har vedtaget [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). For mere information, læs Code of Conduct FAQ eller kontakt [Email opencode](opencode@microsoft.com) med eventuelle yderligere spørgsmål eller kommentarer.

## Lad os komme i gang
Nu hvor du har gennemført de nødvendige trin for at afslutte dette kursus, lad os komme i gang med en [introduktion til Generativ AI og LLM'er](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.