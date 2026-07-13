# Komme i gang med dette kurset

Vi er veldig begeistret for at du skal starte dette kurset og se hva du blir inspirert til å bygge med Generativ AI!

For å sikre din suksess, skisserer denne siden oppsettsteg, tekniske krav og hvor du kan få hjelp hvis nødvendig.

## Oppsettsteg

For å begynne med dette kurset må du fullføre følgende steg.

### 1. Lag en fork av dette repoet

[Lag en fork av hele dette repoet](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) til din egen GitHub-konto for å kunne endre kode og fullføre oppgavene. Du kan også [stjernemerke (🌟) dette repoet](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) for å finne det og relaterte repoer lettere.

### 2. Opprett en codespace

For å unngå avhengighetsproblemer når du kjører koden, anbefaler vi å kjøre dette kurset i en [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

I din fork: **Code -> Codespaces -> New on main**

![Dialog som viser knapper for å opprette en codespace](../../../translated_images/no/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Legg til en hemmelighet

1. ⚙️ Girikon -> Kommandopalett -> Codespaces : Manage user secret -> Legg til en ny hemmelighet.
2. Navn OPENAI_API_KEY, lim inn nøkkelen din, Lagre.

### 3. Hva nå?

| Jeg vil…            | Gå til…                                                                |
|---------------------|------------------------------------------------------------------------|
| Starte leksjon 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Jobbe offline       | [`setup-local.md`](02-setup-local.md)                                  |
| Sette opp en LLM-leverandør | [`providers.md`](03-providers.md)                                     |
| Møte andre deltakere | [Bli med i vår Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Feilsøking


| Symptom                                  | Løsning                                                        |
|------------------------------------------|----------------------------------------------------------------|
| Container bygging sitter fast > 10 min  | **Codespaces ➜ “Rebuild Container”**                           |
| `python: command not found`              | Terminalen koblet ikke til; klikk **+** ➜ *bash*               |
| `401 Unauthorized` fra OpenAI            | Feil / utløpt `OPENAI_API_KEY`                                 |
| VS Code viser “Dev container mounting…” | Oppdater nettleser-fanen—Codespaces mister av og til tilkoblingen |
| Notebook-kjerne mangler                  | Notebook-meny ➜ **Kernel ▸ Velg kjerne ▸ Python 3**           |

   Unix-baserte systemer:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Rediger `.env`-filen**: Åpne `.env`-filen i en teksteditor (f.eks. VS Code, Notepad++ eller annen editor). Legg til følgende linjer i filen, og erstatt plassholderne med din faktiske Microsoft Foundry Models-endepunkt og nøkkel (se [`providers.md`](03-providers.md) for hvordan du får disse):

   > **Merk:** GitHub Models (og dens `GITHUB_TOKEN`-variabel) fases ut ved slutten av juli 2026. Bruk [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) i stedet.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Lagre filen**: Lagre endringene og lukk teksteditoren.

5. **Installer `python-dotenv`**: Hvis du ikke allerede har gjort det, må du installere `python-dotenv`-pakken for å laste miljøvariabler fra `.env`-filen inn i Python-applikasjonen din. Du kan installere den med `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Last inn miljøvariabler i Python-skriptet ditt**: I ditt Python-skript, bruk `python-dotenv`-pakken for å laste miljøvariablene fra `.env`-filen:

   ```python
   from dotenv import load_dotenv
   import os

   # Last inn miljøvariabler fra .env-fil
   load_dotenv()

   # Få tilgang til Microsoft Foundry Models-variablene
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Det er alt! Du har nå opprettet en `.env`-fil, lagt til dine Microsoft Foundry Models-legitimasjoner, og lastet dem inn i Python-applikasjonen din.

## Hvordan kjøre lokalt på din datamaskin

For å kjøre kode lokalt på din datamaskin må du ha en versjon av [Python installert](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

For å bruke repoet må du klone det:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Når du har alt sjekket ut, kan du begynne!

## Valgfrie steg

### Installere Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) er en lettvektsinstaller for å installere [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, samt noen pakker.
Conda er en pakkehåndterer som gjør det enkelt å sette opp og bytte mellom forskjellige Python [**virtuelle miljøer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) og pakker. Den er også nyttig for å installere pakker som ikke er tilgjengelige via `pip`.

Du kan følge [Miniconda-installasjonsveiledningen](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) for å sette den opp.

Med Miniconda installert, må du klone [repoet](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (hvis du ikke allerede har gjort det).

Deretter må du opprette et virtuelt miljø. For å gjøre dette med Conda, kan du lage en ny miljøfil (_environment.yml_). Hvis du følger med i Codespaces, lag denne i `.devcontainer`-mappen, altså `.devcontainer/environment.yml`.

Fyll miljøfilen din med utsnittet nedenfor:

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

Hvis du opplever feil ved bruk av conda kan du manuelt installere Microsoft AI Libraries med følgende kommando i en terminal.

```
conda install -c microsoft azure-ai-ml
```

Miljøfilen spesifiserer hvilke avhengigheter vi trenger. `<environment-name>` er navnet du vil bruke for ditt Conda-miljø, og `<python-version>` er Python-versjonen du ønsker å bruke, for eksempel `3` som er nyeste hovedversjon av Python.

Når dette er gjort, kan du opprette Conda-miljøet ditt ved å kjøre kommandoene nedenfor i kommandolinjen/terminalen

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer understi gjelder bare for Codespace-oppsett
conda activate ai4beg
```

Se [Conda miljøer-veiledningen](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) hvis du støter på problemer.

### Bruke Visual Studio Code med Python-støtteutvidelsen

Vi anbefaler å bruke [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) med [Python-støtteutvidelsen](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installert for dette kurset. Dette er dog bare en anbefaling og ikke et absolutt krav.

> **Merk**: Ved å åpne kursrepoet i VS Code har du mulighet til å sette opp prosjektet i en container. Dette er mulig på grunn av [spesielle `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)-mappen i kursrepoet. Mer om dette senere.

> **Merk**: Når du har klonet og åpnet mappen i VS Code, vil den automatisk foreslå å installere en Python-støtteutvidelse.

> **Merk**: Hvis VS Code foreslår at du åpner repoet i en container på nytt, avslå denne forespørselen hvis du vil bruke den lokalt installerte versjonen av Python.

### Bruke Jupyter i nettleseren

Du kan også jobbe med prosjektet ved å bruke [Jupyter-miljøet](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direkte i nettleseren din. Både klassisk Jupyter og [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) gir en god utviklingsopplevelse med funksjoner som aututfylling, kodeskilling osv.

For å starte Jupyter lokalt, åpne terminalen/kommandolinjen, gå til kursmappen og kjør:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Dette starter en Jupyter-forekomst og URL-en du skal bruke for å komme inn vises i kommandolinjevinduet.

Når du åpner URL-en, skal du se kursinnholdet og kunne navigere til hvilken som helst `*.ipynb`-fil. For eksempel, `08-building-search-applications/python/oai-solution.ipynb`.

### Kjøre i en container

Et alternativ til å sette opp alt på din maskin eller i en Codespace er å bruke en [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Spesielle `.devcontainer`-mappen i kursrepoet gjør det mulig for VS Code å sette opp prosjektet i en container. Utenom Codespaces må du da installere Docker, og det krever en del, så vi anbefaler dette bare for de med erfaring med containere.

En av de beste måtene å holde API-nøkler sikre i GitHub Codespaces på, er å bruke Codespace Secrets. Følg [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) for mer informasjon.


## Leksjoner og tekniske krav

Kurset har 6 konseptuelle leksjoner og 6 programmeringsleksjoner.

For programmeringsleksjonene bruker vi Azure OpenAI Service. Du må ha tilgang til Azure OpenAI-tjenesten og en API-nøkkel for å kjøre denne koden. Du kan søke om tilgang ved å [fylle ut denne søknaden](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Mens du venter på at søknaden skal behandles, inkluderer hver programmeringsleksjon en `README.md`-fil der du kan se kode og resultater.

## Bruke Azure OpenAI-tjenesten for første gang

Hvis dette er første gang du bruker Azure OpenAI-tjenesten, følg denne veiledningen for hvordan du [oppretter og distribuerer en Azure OpenAI Service-ressurs.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Bruke OpenAI API for første gang

Hvis du er ny til OpenAI API, følg veiledningen for hvordan du [oppretter og bruker grensesnittet.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Møte andre deltakere

Vi har opprettet kanaler i vår offisielle [AI Community Discord-server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) for å møte andre deltakere. Dette er en fin måte å bli kjent med andre entreprenører, utviklere, studenter og folk som ønsker å forbedre sine ferdigheter innen Generativ AI.

[![Bli med i discord-kanal](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Prosjektteamet vil også være tilgjengelig på denne Discord-serveren for å hjelpe deltakerne.

## Bidra

Dette kurset er et åpen kildekode-initiativ. Hvis du ser forbedringsområder eller problemer, opprett en [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) eller registrer en [GitHub-issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Prosjektteamet følger med på alle bidrag. Å bidra til åpen kildekode er en flott måte å bygge karrieren din innen Generativ AI.

De fleste bidrag krever at du godtar en Contributor License Agreement (CLA) som bekrefter at du har rettighetene til og faktisk gir oss rettighet til å bruke ditt bidrag. For detaljer, se [CLA, Contributor License Agreement nettside](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Viktig: Når du oversetter tekst i dette repoet, sørg for at du ikke bruker maskinoversettelse. Vi vil verifisere oversettelser via fellesskapet, så vær vennlig og meld deg kun på for oversettelser til språk du behersker godt.

Når du sender en pull request, vil en CLA-bot automatisk avgjøre om du trenger å levere en CLA og merker PR-en passende (f.eks. etikett, kommentar). Følg bare instruksjonene boten gir. Dette må du kun gjøre én gang på tvers av alle repoer som bruker vår CLA.


Dette prosjektet har tatt i bruk [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). For mer informasjon, les FAQ om Code of Conduct eller kontakt [Email opencode](opencode@microsoft.com) med eventuelle ytterligere spørsmål eller kommentarer.

## La oss komme i gang

Nå som du har fullført de nødvendige trinnene for å fullføre dette kurset, la oss komme i gang ved å få en [introduksjon til Generativ AI og LLM-er](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->