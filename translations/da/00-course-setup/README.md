# Kom godt i gang med dette kursus

Vi er meget begejstrede for, at du starter dette kursus og ser, hvad du bliver inspireret til at bygge med Generativ AI!

For at sikre din succes skitserer denne side opsætnings trin, tekniske krav og, hvor du kan få hjælp, hvis det er nødvendigt.

## Opsætningstrin

For at begynde at tage dette kursus skal du gennemføre følgende trin.

### 1. Fork dette Repo

[Fork hele dette repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) til din egen GitHub-konto for at kunne ændre kode og gennemføre udfordringerne. Du kan også [stjerne (🌟) dette repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) for nemmere at finde det og relaterede repoer.

### 2. Opret et codespace

For at undgå afhængighedsproblemer ved kørsel af koden anbefaler vi at køre dette kursus i en [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

I din fork: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/da/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Tilføj en hemmelighed

1. ⚙️ Gear-ikon -> Command Pallete -> Codespaces : Manage user secret -> Tilføj en ny hemmelighed.
2. Navngiv OPENAI_API_KEY, indsæt din nøgle, gem.

### 3. Hvad nu?

| Jeg vil…             | Gå til…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| Start Lektion 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Arbejde offline      | [`setup-local.md`](02-setup-local.md)                                   |
| Opsæt en LLM-udbyder | [`providers.md`](03-providers.md)                                        |
| Mød andre lærende    | [Deltag i vores Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Fejlfinding


| Symptom                                   | Løsning                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| Container build sidder fast > 10 min      | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`                | Terminalen tilknyttede ikke; klik **+** ➜ *bash*                |
| `401 Unauthorized` fra OpenAI              | Forkert / udløbet `OPENAI_API_KEY`                              |
| VS Code viser “Dev container mounting…”    | Opdater browserfanen—Codespaces mister somme tider forbindelse   |
| Notebook kernel mangler                     | Notebook-menu ➜ **Kernel ▸ Vælg Kernel ▸ Python 3**             |

   Unix-baserede systemer:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Rediger `.env`-filen**: Åbn `.env`-filen i en teksteditor (f.eks. VS Code, Notepad++ eller en anden editor). Tilføj følgende linjer i filen, og erstat pladsholderne med din faktiske Microsoft Foundry Models-endpoint og -nøgle (se [`providers.md`](03-providers.md) for, hvordan du får disse):

   > **Bemærk:** GitHub Models (og dens `GITHUB_TOKEN`-variabel) udfases ved udgangen af juli 2026. Brug i stedet [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Gem filen**: Gem ændringerne og luk teksteditoren.

5. **Installer `python-dotenv`**: Hvis du ikke allerede har gjort det, skal du installere `python-dotenv`-pakken for at indlæse miljøvariabler fra `.env`-filen i din Python-applikation. Du kan installere den ved hjælp af `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Indlæs miljøvariabler i dit Python-script**: Brug i dit Python-script `python-dotenv`-pakken til at indlæse miljøvariablerne fra `.env`-filen:

   ```python
   from dotenv import load_dotenv
   import os

   # Indlæs miljøvariabler fra .env-fil
   load_dotenv()

   # Få adgang til Microsoft Foundry Models-variablerne
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Det var det! Du har med succes oprettet en `.env`-fil, tilføjet dine Microsoft Foundry Models legitimationsoplysninger og indlæst dem i din Python-applikation.

## Sådan kører du lokalt på din computer

For at køre koden lokalt på din computer skal du have en version af [Python installeret](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

For at bruge depotet skal du klone det:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Når du har klonet alt, kan du gå i gang!

## Valgfrie trin

### Installation af Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) er en letvægt installer til installation af [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python samt nogle få pakker.
Conda er en pakkehåndtering, der gør det nemt at opsætte og skifte mellem forskellige Python [**virtuelle miljøer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) og pakker. Det er også nyttigt til installation af pakker, der ikke er tilgængelige via `pip`.

Du kan følge [Miniconda installationsvejledningen](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) for at sætte det op.

Når Miniconda er installeret, skal du klone [depotet](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (hvis du ikke allerede har gjort det)

Dernæst skal du oprette et virtuelt miljø. For at gøre dette med Conda, opret en ny miljøfil (_environment.yml_). Hvis du følger med i Codespaces, opret denne fil i `.devcontainer`-mappen, altså `.devcontainer/environment.yml`.

Fyld miljøfilen med følgende snippet:

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

Hvis du får fejl ved brug af conda, kan du manuelt installere Microsoft AI Libraries med følgende kommando i en terminal.

```
conda install -c microsoft azure-ai-ml
```

Miljøfilen specificerer de afhængigheder, vi har brug for. `<environment-name>` henviser til navnet, du ønsker at bruge til dit Conda-miljø, og `<python-version>` er den version af Python, du ønsker at bruge, for eksempel `3`, som er den nyeste major version af Python.

Når det er gjort, kan du oprette dit Conda-miljø ved at køre nedenstående kommandoer i din kommandolinje/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer undermappe gælder kun for Codespace-opsætninger
conda activate ai4beg
```

Se [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), hvis du støder på problemer.

### Brug af Visual Studio Code med Python-supportudvidelsen

Vi anbefaler at bruge editoren [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) med [Python supportudvidelsen](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installeret til dette kursus. Dette er dog mere en anbefaling end et krav.

> **Bemærk**: Ved at åbne kursus-depotet i VS Code kan du vælge at sætte projektet op i en container. Dette er muligt på grund af den [specielle `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) mappe i kursus-depotet. Mere om dette senere.

> **Bemærk**: Når du kloner og åbner mappen i VS Code, vil det automatisk foreslå dig at installere Python-supportudvidelsen.

> **Bemærk**: Hvis VS Code foreslår at åbne depotet i en container, skal du afslå dette for at bruge den lokalt installerede version af Python.

### Brug af Jupyter i browseren

Du kan også arbejde på projektet ved hjælp af [Jupyter-miljøet](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direkte i din browser. Både klassisk Jupyter og [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) giver et behageligt udviklingsmiljø med funktioner som autoudfyldelse, kodefremhævning mv.

For at starte Jupyter lokalt, gå til terminal/kommandolinje, naviger til kursusmappen, og kør:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Dette starter en Jupyter-instans, og URL’en til at få adgang vises i kommandolinjevinduet.

Når du har adgang til URL’en, bør du se kursusoversigten og kunne navigere til en hvilken som helst `*.ipynb`-fil. For eksempel `08-building-search-applications/python/oai-solution.ipynb`.

### Kørsel i en container

Et alternativ til at sætte alt op på din computer eller i Codespace er at bruge en [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Den specielle `.devcontainer`-mappe i kursus-depotet gør det muligt for VS Code at sætte projektet op i en container. Uden for Codespaces kræver dette installation af Docker, og ærligt talt involverer det en del arbejde, så vi anbefaler dette kun til dem med erfaring i at arbejde med containere.

En af de bedste måder at sikre dine API nøgler på ved brug af GitHub Codespaces er ved at bruge Codespace Secrets. Følg venligst [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) vejledningen for at lære mere.


## Lektioner og tekniske krav

Kurset består af 6 konceptlektioner og 6 kodningslektioner.

For kodningslektionerne bruger vi Azure OpenAI Service. Du skal have adgang til Azure OpenAI service og en API-nøgle for at kunne køre denne kode. Du kan ansøge om adgang ved at [udfylde denne ansøgning](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Imens du venter på, at din ansøgning behandles, indeholder hver kodningslektion også en `README.md`-fil, hvor du kan se kode og output.

## Brug af Azure OpenAI Service første gang

Hvis det er første gang, du arbejder med Azure OpenAI service, følg venligst denne guide om, hvordan du [opretter og implementerer en Azure OpenAI Service-ressource](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst).

## Brug af OpenAI API første gang

Hvis det er første gang, du arbejder med OpenAI API, så følg guiden om, hvordan du [opretter og bruger interfacet.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Mød andre lærende

Vi har oprettet kanaler i vores officielle [AI Community Discord-server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) til at møde andre lærende. Dette er en god måde at netværke med ligesindede iværksættere, udviklere, studerende og alle, der ønsker at blive bedre til Generativ AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektteamet vil også være på denne Discord-server for at hjælpe lærende.

## Bidrag

Dette kursus er et open source-initiativ. Hvis du ser forbedringsområder eller problemer, bedes du oprette en [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) eller oprette en [GitHub-issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektteamet vil følge alle bidrag. Bidrag til open source er en fantastisk måde at opbygge din karriere inden for Generativ AI.

De fleste bidrag kræver, at du accepterer en Contributor License Agreement (CLA), som erklærer, at du har ret til og faktisk giver os rettighederne til at bruge dit bidrag. For detaljer, se [CLA, Contributor License Agreement hjemmeside](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Vigtigt: Når du oversætter tekst i dette repo, skal du sikre, at du ikke bruger maskinoversættelse. Vi vil verificere oversættelser gennem fællesskabet, så vær venlig kun at påtage dig oversættelser på sprog, du mestrer.

Når du sender en pull request, vil en CLA-bot automatisk afgøre, om du skal give en CLA og markere PR passende (f.eks. mærke, kommentar). Følg blot instruktionerne fra botten. Du skal kun gøre dette én gang på tværs af alle repoer, der bruger vores CLA.


Dette projekt har vedtaget [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). For mere information læs Code of Conduct FAQ eller kontakt [Email opencode](opencode@microsoft.com) med eventuelle yderligere spørgsmål eller kommentarer.

## Lad os komme i gang

Nu hvor du har gennemført de nødvendige trin for at afslutte dette kursus, lad os komme i gang med en [introduktion til Generative AI og LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->