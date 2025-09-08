<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T17:25:23+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "da"
}
-->
# Kom godt i gang med dette kursus

Vi er meget glade for, at du skal i gang med dette kursus, og vi glæder os til at se, hvad du bliver inspireret til at bygge med Generativ AI!

For at sikre din succes gennemgår denne side opsætningsvejledning, tekniske krav og hvor du kan få hjælp, hvis du får brug for det.

## Opsætningsvejledning

For at komme i gang med kurset skal du gennemføre følgende trin.

### 1. Fork dette repo

[Fork hele dette repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) til din egen GitHub-konto, så du kan ændre i koden og løse udfordringerne. Du kan også [stjerne (🌟) dette repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) for nemmere at finde det og relaterede repos.

### 2. Opret et codespace

For at undgå problemer med afhængigheder, når du kører koden, anbefaler vi at køre kurset i et [GitHub Codespace](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

I dit fork: **Code -> Codespaces -> New on main**

![Dialog der viser knapper til at oprette et codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Tilføj en hemmelighed

1. ⚙️ Tandhjulsikon -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Navngiv OPENAI_API_KEY, indsæt din nøgle, Gem.

### 3.  Hvad nu?

| Jeg vil gerne…      | Gå til…                                                                 |
|---------------------|-------------------------------------------------------------------------|
| Starte Lektion 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Arbejde offline     | [`setup-local.md`](02-setup-local.md)                                   |
| Opsætte en LLM-udbyder | [`providers.md`](providers.md)                                       |
| Møde andre deltagere | [Deltag i vores Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Fejlfinding

| Symptom                                   | Løsning                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| Container-bygning sidder fast > 10 min    | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminalen er ikke tilsluttet; klik **+** ➜ *bash*              |
| `401 Unauthorized` fra OpenAI             | Forkert / udløbet `OPENAI_API_KEY`                              |
| VS Code viser “Dev container mounting…”   | Opdater browsertabben—Codespaces mister nogle gange forbindelsen|
| Notebook-kerne mangler                    | Notebook-menu ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

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

6. **Indlæs miljøvariabler i dit Python-script**: Brug `python-dotenv`-pakken i dit Python-script for at indlæse miljøvariablerne fra `.env`-filen:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Sådan! Du har nu oprettet en `.env`-fil, tilføjet din GitHub-token og indlæst den i din Python-applikation.

## Sådan kører du lokalt på din computer

For at køre koden lokalt på din computer skal du have en version af [Python installeret](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

For at bruge repoet skal du klone det:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Når du har hentet det hele, er du klar til at gå i gang!

## Valgfrie trin

### Installation af Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) er en letvægtsinstaller til at installere [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python og nogle få pakker.
Conda er en pakkehåndtering, der gør det nemt at opsætte og skifte mellem forskellige Python [**virtuelle miljøer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) og pakker. Det er også nyttigt til at installere pakker, der ikke er tilgængelige via `pip`.

Du kan følge [MiniConda installationsguiden](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) for at sætte det op.

Når Miniconda er installeret, skal du klone [repoet](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (hvis du ikke allerede har gjort det)

Dernæst skal du oprette et virtuelt miljø. For at gøre dette med Conda, skal du oprette en ny miljøfil (_environment.yml_). Hvis du følger med i Codespaces, skal du oprette denne i `.devcontainer`-mappen, altså `.devcontainer/environment.yml`.

Udfyld din miljøfil med nedenstående kode:

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

Hvis du oplever fejl med conda, kan du manuelt installere Microsoft AI Libraries med følgende kommando i en terminal.

```
conda install -c microsoft azure-ai-ml
```

Miljøfilen angiver de nødvendige afhængigheder. `<environment-name>` er navnet på det Conda-miljø, du vil bruge, og `<python-version>` er den version af Python, du ønsker, f.eks. `3` for den nyeste hovedversion.

Når det er gjort, kan du oprette dit Conda-miljø ved at køre nedenstående kommandoer i din kommandoprompt/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Se [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), hvis du støder på problemer.

### Brug af Visual Studio Code med Python-udvidelsen

Vi anbefaler at bruge [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editoren med [Python-udvidelsen](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installeret til dette kursus. Dette er dog kun en anbefaling og ikke et krav.

> **Note**: Når du åbner kursus-repoet i VS Code, har du mulighed for at sætte projektet op i en container. Dette skyldes den [specielle `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)-mappe, der findes i repoet. Mere om dette senere.

> **Note**: Når du kloner og åbner mappen i VS Code, vil den automatisk foreslå, at du installerer Python-udvidelsen.

> **Note**: Hvis VS Code foreslår, at du genåbner repoet i en container, så afvis dette for at bruge den lokalt installerede version af Python.

### Brug af Jupyter i browseren

Du kan også arbejde på projektet i [Jupyter-miljøet](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direkte i din browser. Både klassisk Jupyter og [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) giver et behageligt udviklingsmiljø med funktioner som autoudfyldning, kodefremhævning osv.

For at starte Jupyter lokalt, gå til terminalen/kommandoprompten, naviger til kursusmappen, og kør:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Dette starter en Jupyter-instans, og URL’en til at tilgå den vises i kommandoprompten.

Når du åbner URL’en, bør du se kursusoversigten og kunne navigere til enhver `*.ipynb`-fil. For eksempel `08-building-search-applications/python/oai-solution.ipynb`.

### Kørsel i en container

Et alternativ til at sætte det hele op på din computer eller i Codespace er at bruge en [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Den specielle `.devcontainer`-mappe i kursus-repoet gør det muligt for VS Code at sætte projektet op i en container. Uden for Codespaces kræver dette installation af Docker, og det er lidt mere avanceret, så vi anbefaler det kun til dem, der har erfaring med containere.

En af de bedste måder at holde dine API-nøgler sikre, når du bruger GitHub Codespaces, er ved at bruge Codespace Secrets. Følg venligst [vejledningen til håndtering af Codespaces secrets](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) for at lære mere om dette.


## Lektioner og tekniske krav

Kurset består af 6 konceptuelle lektioner og 6 kodningslektioner.

Til kodningslektionerne bruger vi Azure OpenAI Service. Du skal have adgang til Azure OpenAI-tjenesten og en API-nøgle for at kunne køre koden. Du kan ansøge om adgang ved at [udfylde denne ansøgning](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Mens du venter på, at din ansøgning behandles, indeholder hver kodningslektion også en `README.md`-fil, hvor du kan se koden og output.

## Brug af Azure OpenAI Service for første gang

Hvis det er første gang, du arbejder med Azure OpenAI-tjenesten, så følg denne vejledning til, hvordan du [opretter og udruller en Azure OpenAI Service-ressource.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Brug af OpenAI API for første gang

Hvis det er første gang, du arbejder med OpenAI API, så følg vejledningen til, hvordan du [opretter og bruger interfacet.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Mød andre deltagere

Vi har oprettet kanaler på vores officielle [AI Community Discord-server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) til at møde andre deltagere. Det er en god måde at netværke med andre iværksættere, udviklere, studerende og alle, der ønsker at blive bedre til Generativ AI.

[![Deltag i discord-kanalen](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektteamet vil også være til stede på denne Discord-server for at hjælpe deltagerne.

## Bidrag

Dette kursus er et open source-initiativ. Hvis du ser forbedringsmuligheder eller problemer, så opret et [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) eller log et [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektteamet holder øje med alle bidrag. At bidrage til open source er en fantastisk måde at styrke din karriere inden for Generativ AI.

De fleste bidrag kræver, at du accepterer en Contributor License Agreement (CLA), hvor du erklærer, at du har ret til og faktisk giver os rettighederne til at bruge dit bidrag. Læs mere på [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Vigtigt: Når du oversætter tekst i dette repo, skal du sikre dig, at du ikke bruger maskinoversættelse. Vi vil verificere oversættelser via fællesskabet, så meld dig kun som oversætter til sprog, du er fortrolig med.

Når du indsender et pull request, vil en CLA-bot automatisk afgøre, om du skal underskrive en CLA og markere PR’en derefter (f.eks. label, kommentar). Følg blot instruktionerne fra botten. Du skal kun gøre dette én gang på tværs af alle repos, der bruger vores CLA.

Dette projekt har vedtaget [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). For mere information, læs Code of Conduct FAQ eller kontakt [Email opencode](opencode@microsoft.com) med yderligere spørgsmål eller kommentarer.

## Lad os komme i gang
Nu hvor du har gennemført de nødvendige trin for at færdiggøre dette kursus, lad os komme i gang med at få en [introduktion til Generativ AI og LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritiske oplysninger anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå ved brug af denne oversættelse.