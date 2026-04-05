# Kom godt i gang med dette kursus

Vi er meget glade for, at du starter på dette kursus og ser, hvad du bliver inspireret til at bygge med Generativ AI!

For at sikre din succes beskriver denne side opsætningsskridt, tekniske krav samt, hvor du kan få hjælp, hvis det bliver nødvendigt.

## Opsætningsskridt

For at begynde på kurset skal du gennemføre følgende skridt.

### 1. Fork dette repo

[Forforsk dette hele repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) til din egen GitHub-konto for at kunne ændre koden og løse udfordringerne. Du kan også [stjerne (🌟) dette repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) for nemmere at kunne finde det og beslægtede repoer.

### 2. Opret en codespace

For at undgå afhængighedsproblemer, når du kører koden, anbefaler vi at køre dette kursus i en [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

I dit fork: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/da/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Tilføj en secret

1. ⚙️ Gear ikon -> Command Pallete-> Codespaces : Manage user secret -> Tilføj en ny secret.  
2. Navngiv OPENAI_API_KEY, indsæt din nøgle, Gem.

### 3. Hvad nu?

| Jeg vil…           | Gå til…                                                                |
|--------------------|------------------------------------------------------------------------|
| Starte Lektion 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Arbejde offline    | [`setup-local.md`](02-setup-local.md)                                  |
| Sætte en LLM-udbyder op | [`providers.md`](03-providers.md)                                    |
| Møde andre kursister | [Deltag i vores Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Fejlfinding

| Symptom                                  | Løsning                                                       |
|-------------------------------------------|--------------------------------------------------------------|
| Container build hænger > 10 min          | **Codespaces ➜ “Rebuild Container”**                         |
| `python: command not found`               | Terminalen tilknyttede sig ikke; klik **+** ➜ *bash*         |
| `401 Unauthorized` fra OpenAI             | Forkert / udløbet `OPENAI_API_KEY`                           |
| VS Code viser “Dev container mounting…”  | Genindlæs browserfanen—Codespaces mister undertiden forbindelsen  |
| Notebook-kerne mangler                    | Notebook-menu ➜ **Kernel ▸ Select Kernel ▸ Python 3**        |

   Unix-baserede systemer:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Rediger `.env`-filen**: Åbn `.env`-filen i en teksteditor (f.eks. VS Code, Notepad++ eller en anden editor). Tilføj følgende linje til filen, hvor `your_github_token_here` erstattes med dit faktiske GitHub-token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Gem filen**: Gem ændringerne og luk teksteditoren.

5. **Installer `python-dotenv`**: Hvis du ikke allerede har det, skal du installere pakken `python-dotenv` for at læse miljøvariabler fra `.env`-filen ind i din Python-applikation. Du kan installere den via `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Indlæs miljøvariabler i dit Python-script**: Brug pakken `python-dotenv` i dit Python-script til at indlæse miljøvariablerne fra `.env`-filen:

   ```python
   from dotenv import load_dotenv
   import os

   # Indlæs miljøvariabler fra .env fil
   load_dotenv()

   # Få adgang til GITHUB_TOKEN variablen
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Det var det! Du har succesfuldt oprettet en `.env`-fil, tilføjet dit GitHub-token og indlæst det i din Python-applikation.

## Sådan kører du lokalt på din computer

For at køre koden lokalt på din computer skal du have en version af [Python installeret](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

For at bruge repositoriet skal du derefter klone det:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Når du har alt på plads, kan du komme i gang!

## Valgfrie skridt

### Installation af Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) er en letvægtsinstaller til installation af [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python samt nogle pakker.  
Conda er en pakkestyring, der gør det nemt at opsætte og skifte mellem forskellige Python [**virtuelle miljøer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) og pakker. Det er også nyttigt til installation af pakker, som ikke er tilgængelige via `pip`.

Du kan følge [Miniconda installationsvejledningen](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) for at sætte det op.

Når Miniconda er installeret, skal du klone [repositoriet](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (hvis du ikke allerede har gjort det).

Dernæst skal du oprette et virtuelt miljø. For at gøre dette med Conda skal du oprette en ny miljøfil (_environment.yml_). Hvis du følger med i Codespaces, opret denne i `.devcontainer`-mappen, altså `.devcontainer/environment.yml`.

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

Hvis du oplever fejl med conda, kan du manuelt installere Microsoft AI Libraries med denne kommando i terminalen.

```
conda install -c microsoft azure-ai-ml
```

Miljøfilen angiver de afhængigheder, vi har brug for. `<environment-name>` refererer til det navn, du ønsker til dit Conda-miljø, og `<python-version>` er hvilken Python-version, du ønsker at bruge, eksempelvis `3` som den seneste større version af Python.

Med det på plads kan du oprette dit Conda-miljø ved at køre nedenstående kommandoer i din kommandolinje/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer understi anvendes kun til Codespace opsætninger
conda activate ai4beg
```

Se [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), hvis du støder på problemer.

### Brug af Visual Studio Code med Python-udvidelsen

Vi anbefaler at bruge editoren [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) med [Python-supportudvidelsen](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installeret til dette kursus. Det er dog en anbefaling og ikke et krav.

> **Bemærk**: Ved at åbne kursusrepoet i VS Code har du mulighed for at opsætte projektet i en container. Dette skyldes den [specielle `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) mappe i kursusrepoet. Mere om dette senere.

> **Bemærk**: Når du har klonet og åbnet mappen i VS Code, vil den automatisk foreslå at installere Python-supportudvidelsen.

> **Bemærk**: Hvis VS Code foreslår, at du åbner repositoriet i en container, skal du afvise dette for at bruge den lokalt installerede version af Python.

### Brug af Jupyter i browseren

Du kan også arbejde på projektet ved at bruge [Jupyter-miljøet](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direkte i din browser. Både klassisk Jupyter og [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) giver et behageligt udviklingsmiljø med funktioner som autoudfyldelse, kodefremhævning osv.

For at starte Jupyter lokalt, åbn terminalen/kommandolinjen, naviger til kursusmappen, og kør:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Denne kommando starter en Jupyter-instanse, og URL’en til at tilgå den vises i kommandolinjevinduet.

Når du tilgår URL’en, vil du se kursusoversigten og kan navigere til en hvilken som helst `*.ipynb` fil. For eksempel `08-building-search-applications/python/oai-solution.ipynb`.

### Kørsel i en container

Et alternativ til at sætte alt op på din computer eller i en Codespace er at bruge en [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Den særlige `.devcontainer`-mappe i kursusrepoet gør det muligt for VS Code at opsætte projektet i en container. Udenfor Codespaces kræver det installation af Docker, og det indebærer en del arbejde, så vi anbefaler det kun til personer med erfaring i at arbejde med containere.

En af de bedste måder til at holde dine API-nøgler sikre ved brug af GitHub Codespaces er ved at bruge Codespace Secrets. Følg venligst [Codespaces secrets management-guiden](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) for at lære mere herom.

## Lektioner og tekniske krav

Kurset har 6 konceptuelle lektioner og 6 kodningslektioner.

Til kodningslektionerne bruger vi Azure OpenAI Service. Du skal have adgang til Azure OpenAI-servicen og en API-nøgle for at kunne køre denne kode. Du kan ansøge om adgang ved at [udfylde denne ansøgning](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Mens du venter på, at din ansøgning bliver behandlet, indeholder hver kodningslektion også en `README.md`-fil, hvor du kan se koden og output.

## Brug af Azure OpenAI Service for første gang

Hvis du for første gang arbejder med Azure OpenAI Service, følg denne vejledning om, hvordan du [opretter og deployerer en Azure OpenAI Service-ressource.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Brug af OpenAI API for første gang

Hvis du for første gang arbejder med OpenAI API, følg vejledningen om, hvordan du [opretter og bruger interfacet.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Mød andre kursister

Vi har oprettet kanaler i vores officielle [AI Community Discord-server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) for at møde andre kursister. Dette er en fantastisk måde at netværke med ligesindede iværksættere, udviklere, studerende og alle, der ønsker at dygtiggøre sig indenfor Generativ AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektteamet vil også være til stede på denne Discord-server for at hjælpe kursister.

## Bidrag

Dette kursus er en open source-initiativ. Hvis du ser forbedringsmuligheder eller problemer, så opret en [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) eller rapporter en [GitHub-issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektteamet holder styr på alle bidrag. At bidrage til open source er en fremragende måde at udvikle din karriere inden for Generativ AI.

De fleste bidrag kræver, at du accepterer en Contributor License Agreement (CLA), der erklærer, at du har ret til – og rent faktisk giver os retten til – at bruge dit bidrag. For detaljer, besøg venligst [CLA, Contributor License Agreement-websiden](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Vigtigt: Når du oversætter tekst i dette repo, må du ikke benytte maskinoversættelse. Vi vil verificere oversættelser via communityen, så påtag dig kun oversættelser for sprog, hvor du er kompetent.

Når du indsender en pull request, vil en CLA-bot automatisk afgøre, om du skal indsende en CLA, og påføre PR’en den rette mærkning eller kommentar. Følg blot instruktionerne fra botten. Du skal kun gøre det én gang for alle repositories, der bruger vores CLA.

Dette projekt har adopteret [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). For mere information, læs Code of Conduct FAQ eller kontakt [Email opencode](opencode@microsoft.com) med spørgsmål eller kommentarer.

## Lad os komme i gang!
Nu hvor du har gennemført de nødvendige trin for at færdiggøre dette kursus, lad os komme i gang med at få en [introduktion til Generativ AI og LLM’er](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokument er oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog betragtes som den autoritative kilde. For vigtig information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->