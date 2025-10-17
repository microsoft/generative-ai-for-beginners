<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-17T19:20:20+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "no"
}
-->
# Komme i gang med dette kurset

Vi er veldig glade for at du skal starte dette kurset og se hva du blir inspirert til å bygge med Generativ AI!

For å sikre din suksess, beskriver denne siden oppsettsteg, tekniske krav og hvor du kan få hjelp hvis det trengs.

## Oppsettsteg

For å begynne med dette kurset, må du fullføre følgende steg.

### 1. Fork denne repoen

[Fork hele denne repoen](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) til din egen GitHub-konto for å kunne endre kode og fullføre utfordringene. Du kan også [star (🌟) denne repoen](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) for å finne den og relaterte repoer enklere.

### 2. Opprett en codespace

For å unngå avhengighetsproblemer når du kjører koden, anbefaler vi å kjøre dette kurset i en [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

I din fork: **Code -> Codespaces -> New on main**

![Dialog som viser knapper for å opprette en codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Legg til en hemmelighet

1. ⚙️ Gear-ikon -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Navngi OPENAI_API_KEY, lim inn nøkkelen din, Lagre.

### 3. Hva er neste?

| Jeg vil…            | Gå til…                                                                 |
|---------------------|-------------------------------------------------------------------------|
| Starte leksjon 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Jobbe offline       | [`setup-local.md`](02-setup-local.md)                                   |
| Sette opp en LLM-leverandør | [`providers.md`](03-providers.md)                                        |
| Møte andre elever   | [Bli med i vår Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Feilsøking

| Symptom                                   | Løsning                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| Containerbygging sitter fast > 10 min     | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminalen ble ikke koblet til; klikk **+** ➜ *bash*            |
| `401 Unauthorized` fra OpenAI             | Feil / utløpt `OPENAI_API_KEY`                                  |
| VS Code viser “Dev container mounting…”   | Oppdater nettleserfanen—Codespaces mister noen ganger tilkoblingen |
| Notebook-kjerne mangler                   | Notebook-meny ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix-baserte systemer:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Rediger `.env`-filen**: Åpne `.env`-filen i en tekstredigerer (f.eks. VS Code, Notepad++ eller en annen editor). Legg til følgende linje i filen, og erstatt `your_github_token_here` med din faktiske GitHub-token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Lagre filen**: Lagre endringene og lukk tekstredigereren.

5. **Installer `python-dotenv`**: Hvis du ikke allerede har gjort det, må du installere `python-dotenv`-pakken for å laste miljøvariabler fra `.env`-filen inn i Python-applikasjonen din. Du kan installere den med `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Last miljøvariabler i Python-skriptet ditt**: I Python-skriptet ditt, bruk `python-dotenv`-pakken for å laste miljøvariabler fra `.env`-filen:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Det er alt! Du har opprettet en `.env`-fil, lagt til GitHub-tokenet ditt, og lastet det inn i Python-applikasjonen din.

## Hvordan kjøre lokalt på din datamaskin

For å kjøre koden lokalt på din datamaskin, må du ha en versjon av [Python installert](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

For deretter å bruke repoen, må du klone den:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Når du har alt sjekket ut, kan du komme i gang!

## Valgfrie steg

### Installere Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) er en lettvektsinstallasjon for å installere [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, samt noen få pakker.
Conda i seg selv er en pakkebehandler som gjør det enkelt å sette opp og bytte mellom forskjellige Python [**virtuelle miljøer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) og pakker. Det er også nyttig for å installere pakker som ikke er tilgjengelige via `pip`.

Du kan følge [MiniConda installasjonsveiledning](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) for å sette det opp.

Med Miniconda installert, må du klone [repoen](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (hvis du ikke allerede har gjort det).

Deretter må du opprette et virtuelt miljø. For å gjøre dette med Conda, opprett en ny miljøfil (_environment.yml_). Hvis du følger med ved bruk av Codespaces, opprett denne i `.devcontainer`-mappen, altså `.devcontainer/environment.yml`.

Fyll miljøfilen din med følgende kode:

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

Hvis du får feil med conda, kan du manuelt installere Microsoft AI Libraries ved å bruke følgende kommando i en terminal.

```
conda install -c microsoft azure-ai-ml
```

Miljøfilen spesifiserer avhengighetene vi trenger. `<environment-name>` refererer til navnet du ønsker å bruke for ditt Conda-miljø, og `<python-version>` er versjonen av Python du ønsker å bruke, for eksempel `3` som er den nyeste hovedversjonen av Python.

Når det er gjort, kan du opprette ditt Conda-miljø ved å kjøre kommandoene nedenfor i kommandolinjen/terminalen din:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Se [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) hvis du støter på problemer.

### Bruke Visual Studio Code med Python-støtteutvidelsen

Vi anbefaler å bruke [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editoren med [Python-støtteutvidelsen](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installert for dette kurset. Dette er imidlertid mer en anbefaling og ikke et absolutt krav.

> **Merk**: Ved å åpne kursrepoen i VS Code, har du muligheten til å sette opp prosjektet i en container. Dette er på grunn av den [spesielle `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)-mappen som finnes i kursrepoen. Mer om dette senere.

> **Merk**: Når du kloner og åpner mappen i VS Code, vil det automatisk foreslå at du installerer en Python-støtteutvidelse.

> **Merk**: Hvis VS Code foreslår at du åpner repoen i en container, avslå denne forespørselen for å bruke den lokalt installerte versjonen av Python.

### Bruke Jupyter i nettleseren

Du kan også jobbe med prosjektet ved å bruke [Jupyter-miljøet](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direkte i nettleseren din. Både klassisk Jupyter og [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) gir et behagelig utviklingsmiljø med funksjoner som autokomplettering, kodeutheving, osv.

For å starte Jupyter lokalt, gå til terminalen/kommandolinjen, naviger til kursmappen, og utfør:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Dette vil starte en Jupyter-instans, og URL-en for å få tilgang til den vil vises i kommandolinjevinduet.

Når du får tilgang til URL-en, bør du se kursoversikten og kunne navigere til hvilken som helst `*.ipynb`-fil. For eksempel, `08-building-search-applications/python/oai-solution.ipynb`.

### Kjøre i en container

Et alternativ til å sette opp alt på din datamaskin eller Codespace er å bruke en [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Den spesielle `.devcontainer`-mappen i kursrepoen gjør det mulig for VS Code å sette opp prosjektet i en container. Utenfor Codespaces vil dette kreve installasjon av Docker, og det innebærer en del arbeid, så vi anbefaler dette kun til de med erfaring med containere.

En av de beste måtene å holde API-nøklene dine sikre når du bruker GitHub Codespaces er ved å bruke Codespace Secrets. Følg [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst)-veiledningen for å lære mer om dette.

## Leksjoner og tekniske krav

Kurset har 6 konseptleksjoner og 6 kodeleksjoner.

For kodeleksjonene bruker vi Azure OpenAI Service. Du vil trenge tilgang til Azure OpenAI-tjenesten og en API-nøkkel for å kjøre denne koden. Du kan søke om tilgang ved å [fullføre denne søknaden](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Mens du venter på at søknaden din skal behandles, inkluderer hver kodeleksjon også en `README.md`-fil hvor du kan se koden og resultatene.

## Bruke Azure OpenAI Service for første gang

Hvis dette er første gang du jobber med Azure OpenAI-tjenesten, vennligst følg denne veiledningen om hvordan du [oppretter og distribuerer en Azure OpenAI Service-ressurs.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Bruke OpenAI API for første gang

Hvis dette er første gang du jobber med OpenAI API, vennligst følg veiledningen om hvordan du [oppretter og bruker grensesnittet.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Møt andre elever

Vi har opprettet kanaler i vår offisielle [AI Community Discord-server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) for å møte andre elever. Dette er en flott måte å bygge nettverk med andre likesinnede entreprenører, utviklere, studenter og alle som ønsker å utvikle seg innen Generativ AI.

[![Bli med i Discord-kanalen](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Prosjektteamet vil også være på denne Discord-serveren for å hjelpe alle elever.

## Bidra

Dette kurset er et open-source initiativ. Hvis du ser forbedringsområder eller problemer, vennligst opprett en [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) eller logg en [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Prosjektteamet vil spore alle bidrag. Å bidra til open source er en fantastisk måte å bygge din karriere innen Generativ AI.

De fleste bidrag krever at du godtar en Contributor License Agreement (CLA) som erklærer at du har rett til, og faktisk gir oss rett til, å bruke ditt bidrag. For detaljer, besøk [CLA, Contributor License Agreement-nettstedet](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Viktig: når du oversetter tekst i denne repoen, må du sørge for at du ikke bruker maskinoversettelse. Vi vil verifisere oversettelser via fellesskapet, så vennligst meld deg kun som frivillig for oversettelser på språk der du er dyktig.

Når du sender inn en pull request, vil en CLA-bot automatisk avgjøre om du trenger å gi en CLA og dekorere PR-en deretter (f.eks. etikett, kommentar). Følg bare instruksjonene gitt av boten. Du trenger bare å gjøre dette én gang på tvers av alle repoer som bruker vår CLA.

Dette prosjektet har adoptert [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). For mer informasjon, les Code of Conduct FAQ eller kontakt [Email opencode](opencode@microsoft.com) med eventuelle spørsmål eller kommentarer.

## La oss komme i gang
Nå som du har fullført de nødvendige trinnene for å gjennomføre dette kurset, la oss komme i gang med en [introduksjon til Generativ AI og LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.