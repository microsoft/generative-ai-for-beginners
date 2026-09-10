# Kom godt i gang med dette kursus

Vi er meget spændte på, at du begynder på dette kursus og ser, hvad du bliver inspireret til at bygge med Generativ AI!

For at sikre din succes beskriver denne side opsætningstrin, tekniske krav og hvor du kan få hjælp, hvis det bliver nødvendigt.

## Opsætnings trin

For at komme i gang med dette kursus skal du gennemføre følgende trin.

### 1. Fork dette repo

[Fork hele dette repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) til din egen GitHub-konto for at kunne ændre kode og gennemføre udfordringerne. Du kan også [stjerne (🌟) dette repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) for lettere at finde det og relaterede repos.

### 2. Opret en codespace

For at undgå afhængighedsproblemer ved kørsel af koden anbefaler vi at køre dette kursus i en [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

I din fork: **Kode -> Codespaces -> Ny på main**

![Dialog, der viser knapper for at oprette en codespace](../../../translated_images/da/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Tilføj en hemmelighed

1. ⚙️ Gear-ikon -> Command Pallette -> Codespaces : Administrer brugerhemmelighed -> Tilføj en ny hemmelighed.
2. Navngiv OPENAI_API_KEY, indsæt din nøgle, Gem.

### 3. Hvad så?

| Jeg vil…            | Gå til…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| Starte Lektion 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Arbejde offline    | [`setup-local.md`](02-setup-local.md)                                   |
| Opsæt en LLM-udbyder | [`providers.md`](03-providers.md)                                        |
| Mød andre studerende | [Deltag i vores Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Fejlfinding


| Symptom                                  | Løsning                                                       |
|------------------------------------------|--------------------------------------------------------------|
| Container build sidder fast > 10 min     | **Codespaces ➜ “Genopbyg container”**                        |
| `python: kommando ikke fundet`            | Terminalen blev ikke tilknyttet; klik **+** ➜ *bash*          |
| `401 Unauthorized` fra OpenAI              | Forkert / udløbet `OPENAI_API_KEY`                            |
| VS Code viser “Dev container mounting…”    | Opdater browserfanen—Codespaces mister nogle gange forbindelsen |
| Notebook-kerne mangler                    | Notebook-menu ➜ **Kernel ▸ Vælg Kernel ▸ Python 3**           |

   Unix-baserede systemer:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Rediger `.env` filen**: Åbn `.env` filen i en teksteditor (fx VS Code, Notepad++ eller en anden editor). Tilføj følgende linjer i filen og erstat pladsholderne med dit faktiske Microsoft Foundry Models-endpoint og nøgle (se [`providers.md`](03-providers.md) for hvordan du får disse):

   > **Bemærk:** GitHub Models (og dens `GITHUB_TOKEN` variabel) udfases ved udgangen af juli 2026. Brug i stedet [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Gem filen**: Gem ændringerne og luk teksteditoren.

5. **Installer `python-dotenv`**: Hvis du ikke allerede har gjort det, skal du installere pakken `python-dotenv` for at indlæse miljøvariable fra `.env` filen i din Python-applikation. Du kan installere den med `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Indlæs miljøvariable i dit Python-script**: Brug i dit Python-script `python-dotenv` pakken til at hente miljøvariablene fra `.env` filen:

   ```python
   from dotenv import load_dotenv
   import os

   # Indlæs miljøvariabler fra .env-fil
   load_dotenv()

   # Tilgå Microsoft Foundry Models-variablerne
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Sådan! Du har nu oprettet en `.env` fil, tilføjet dine Microsoft Foundry Models-legitimationsoplysninger og indlæst dem i din Python-applikation.

## Sådan kører du lokalt på din computer

For at køre koden lokalt på din computer, skal du have en version af [Python installeret](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

For at bruge repositoriet skal du derefter klone det:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Når du har fået alt tjekket ud, kan du komme i gang!

## Valgfrie trin

### Installation af Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) er en letvægtsinstaller til installation af [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python samt nogle pakker.
Conda er en pakkehåndtering, der gør det nemt at opsætte og skifte mellem forskellige Python [**virtuelle miljøer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) og pakker. Den er også nyttig til at installere pakker, som ikke er tilgængelige via `pip`.

Du kan følge [Miniconda installationsvejledningen](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) for at sætte det op.

Når Miniconda er installeret, skal du klone [repositoriet](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (hvis du ikke allerede har gjort det)

Dernæst skal du oprette et virtuelt miljø. For at gøre det med Conda, skal du oprette en miljø-fil (_environment.yml_). Følger du med i Codespaces, skal denne oprettes i `.devcontainer` mappen, altså `.devcontainer/environment.yml`.

Fyld din miljøfil med nedenstående snippet:

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

Hvis du oplever fejl ved brug af conda, kan du manuelt installere Microsoft AI Libraries med følgende kommando i terminalen.

```
conda install -c microsoft azure-ai-ml
```

Miljøfilen angiver de nødvendige afhængigheder. `<environment-name>` henviser til det navn, du vil give dit Conda-miljø, og `<python-version>` er den version af Python, du vil bruge, f.eks. `3` som den seneste hovedversion af Python.

Når det er gjort, kan du oprette dit Conda-miljø ved at køre nedenstående kommandoer i kommandolinjen/terminalen

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer understi anvendes kun til Codespace-opsætninger
conda activate ai4beg
```

Se [Conda miljøvejledningen](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) hvis du støder på problemer.

### Brug af Visual Studio Code med Python-understøttelsesudvidelsen

Vi anbefaler at bruge [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editoren med [Python-understøttelsesudvidelsen](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installeret til dette kursus. Dette er dog mere en anbefaling og ikke et krav.

> **Bemærk**: Ved at åbne kursusrepositoriet i VS Code har du mulighed for at opsætte projektet i en container. Det skyldes den [specielle `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) mappe i kursusrepositoriet. Mere om dette senere.

> **Bemærk**: Når du har klonet og åbnet mappen i VS Code, vil det automatisk foreslå, at du installerer en Python-understøttelsesudvidelse.

> **Bemærk**: Hvis VS Code foreslår, at du åbner repositoriet igen i en container, skal du afslå dette for at bruge den lokalt installerede version af Python.

### Brug af Jupyter i browseren

Du kan også arbejde med projektet ved hjælp af [Jupyter-miljøet](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direkte i din browser. Både klassisk Jupyter og [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) tilbyder et behageligt udviklingsmiljø med funktioner som autoudfyldning, kodefremhævning osv.

For at starte Jupyter lokalt, gå til terminalen/kommandolinjen, naviger til kursusmappen og kør:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Dette vil starte en Jupyter-instans, og URL'en til at tilgå den vil blive vist i kommandolinjevinduet.

Når du tilgår URL'en, bør du se kursusoversigten og kunne navigere til enhver `*.ipynb` fil. For eksempel `08-building-search-applications/python/oai-solution.ipynb`.

### Kørsel i en container

Et alternativ til at sætte alt op på din computer eller Codespace er at bruge en [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Den specielle `.devcontainer` mappe i kursusrepositoriet gør det muligt for VS Code at opsætte projektet i en container. Uden for Codespaces kræver det, at Docker installeres, og ærligt talt kræver det lidt arbejde, så vi anbefaler kun dette til dem med erfaring i at arbejde med containere.

En af de bedste måder at sikre dine API-nøgler, når du bruger GitHub Codespaces, er ved at bruge Codespace Secrets. Følg venligst [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guiden for at lære mere om dette.


## Lektioner og tekniske krav

Kurset indeholder "Lær" lektioner, der forklarer Generativ AI-koncepter, og "Byg" lektioner med praktiske kodeeksempler i både **Python** og **TypeScript** hvor muligt.

Til kodningslektionerne bruger vi Azure OpenAI i Microsoft Foundry. Du skal have et Azure-abonnement og en API-nøgle. Adgangen er åben - ingen ansøgning nødvendig - så du kan [oprette en Microsoft Foundry-ressource og implementere en model](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) for at få dit endpoint og nøgle.

Hver kodningslektion inkluderer også en `README.md` fil, hvor du kan se koden og output uden at køre noget.

## Brug af Azure OpenAI-tjenesten første gang

Hvis det er første gang, du arbejder med Azure OpenAI-tjenesten, så følg venligst denne guide til hvordan du [opretter og implementerer en Azure OpenAI Service-ressource.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Brug af OpenAI API for første gang

Hvis det er første gang, du arbejder med OpenAI API, så følg guiden til hvordan man [opretter og bruger interfacet.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Mød andre studerende

Vi har oprettet kanaler i vores officielle [AI Community Discord-server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) til at møde andre studerende. Dette er en god måde at netværke med andre ligesindede iværksættere, udviklere, studerende og alle, der ønsker at blive bedre til Generativ AI.

[![Deltag i discord kanal](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Projektteamet vil også være på denne Discord-server for at hjælpe alle studerende.

## Bidrag

Dette kursus er en open source-initiativ. Hvis du ser områder til forbedring eller problemer, bedes du oprette en [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) eller oprette en [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Projektteamet vil følge alle bidrag. At bidrage til open source er en fantastisk måde at opbygge din karriere inden for Generativ AI.

De fleste bidrag kræver, at du accepterer en Contributor License Agreement (CLA), der erklærer, at du har ret til og faktisk giver os retten til at bruge dit bidrag. For detaljer, besøg [CLA, Contributor License Agreement-webstedet](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Vigtigt: Når du oversætter tekst i dette repo, bedes du sikre, at du ikke bruger maskinoversættelse. Vi vil verificere oversættelser via fællesskabet, så vær venlig kun at tilmelde dig oversættelser i sprog, hvor du er flydende.


Når du indsender en pull request, vil en CLA-bot automatisk afgøre, om du skal give en CLA og dekorere PR'en passende (f.eks. label, kommentar). Følg blot instruktionerne fra botten. Du skal kun gøre dette én gang på tværs af alle repositories, der bruger vores CLA.

Dette projekt har vedtaget [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). For mere information læs Code of Conduct FAQ eller kontakt [Email opencode](opencode@microsoft.com) med eventuelle yderligere spørgsmål eller kommentarer.

## Lad os komme i gang

Nu hvor du har fuldført de nødvendige trin for at gennemføre dette kursus, lad os komme i gang med at få en [introduktion til Generative AI og LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->