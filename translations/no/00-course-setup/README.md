<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:51:51+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "no"
}
-->
# Komme i gang med dette kurset

Vi er veldig begeistret for at du skal starte dette kurset og se hva du blir inspirert til å bygge med Generativ AI!

For å sikre din suksess, beskriver denne siden oppsettstrinn, tekniske krav og hvor du kan få hjelp om nødvendig.

## Oppsettstrinn

For å begynne å ta dette kurset, må du fullføre følgende trinn.

### 1. Fork denne Repo

[Fork hele dette repoet](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) til din egen GitHub-konto for å kunne endre kode og fullføre utfordringene. Du kan også [stjerne (🌟) dette repoet](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) for å finne det og relaterte repoer enklere.

### 2. Opprett en codespace

For å unngå eventuelle avhengighetsproblemer når du kjører koden, anbefaler vi å kjøre dette kurset i en [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Dette kan opprettes ved å velge `Code`-alternativet på din forkede versjon av dette repoet og velge **Codespaces**-alternativet.

![Dialog som viser knapper for å opprette en codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Lagring av API-nøklene dine

Det er viktig å holde API-nøklene dine trygge og sikre når du bygger applikasjoner. Vi anbefaler å ikke lagre API-nøkler direkte i koden din. Å legge disse detaljene til et offentlig repo kan føre til sikkerhetsproblemer og til og med uønskede kostnader hvis de brukes av en uønsket aktør. Her er en steg-for-steg guide om hvordan du oppretter en `.env`-fil for Python og legger til `GITHUB_TOKEN`:

1. **Naviger til prosjektmappen din**: Åpne terminalen eller kommandoprompten og naviger til rotmappen for prosjektet ditt der du vil opprette `.env`-filen.

   ```bash
   cd path/to/your/project
   ```

2. **Opprett `.env`-filen**: Bruk din foretrukne teksteditor for å opprette en ny fil kalt `.env`. Hvis du bruker kommandolinjen, kan du bruke `touch` (on Unix-based systems) or `echo` (på Windows):

   Unix-baserte systemer:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Rediger `.env`-filen**: Åpne `.env`-filen i en teksteditor (f.eks. VS Code, Notepad++, eller en annen editor). Legg til følgende linje i filen, og erstatt `your_github_token_here` med din faktiske GitHub-token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Lagre filen**: Lagre endringene og lukk teksteditoren.

5. **Installer `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv`-pakken for å laste miljøvariabler fra `.env`-filen inn i din Python-applikasjon. Du kan installere det ved å bruke `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Last miljøvariabler i Python-skriptet ditt**: I ditt Python-skript, bruk `python-dotenv`-pakken for å laste miljøvariablene fra `.env`-filen:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Det var det! Du har nå opprettet en `.env`-fil, lagt til din GitHub-token, og lastet den inn i din Python-applikasjon.

## Hvordan kjøre lokalt på din datamaskin

For å kjøre koden lokalt på datamaskinen din, må du ha en versjon av [Python installert](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

For å bruke repoet, må du klone det:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Når du har alt sjekket ut, kan du komme i gang!

## Valgfrie trinn

### Installere Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) er en lettvektsinstallatør for å installere [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, samt noen få pakker. Conda i seg selv er en pakkebehandler, som gjør det enkelt å sette opp og bytte mellom forskjellige Python [**virtuelle miljøer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) og pakker. Det er også nyttig for å installere pakker som ikke er tilgjengelige via `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Gå videre og fyll ut miljøfilen din med koden nedenfor:

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

Hvis du opplever feil ved bruk av conda, kan du manuelt installere Microsoft AI Libraries ved å bruke følgende kommando i en terminal.

```
conda install -c microsoft azure-ai-ml
```

Miljøfilen spesifiserer avhengighetene vi trenger. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` er den nyeste hovedversjonen av Python.

Når det er gjort, kan du gå videre og opprette ditt Conda-miljø ved å kjøre kommandoene nedenfor i kommandolinjen/terminalen din

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Se [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) hvis du støter på problemer.

### Bruke Visual Studio Code med Python-støtteutvidelse

Vi anbefaler å bruke [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editoren med [Python-støtteutvidelsen](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installert for dette kurset. Dette er imidlertid mer en anbefaling og ikke et absolutt krav.

> **Merk**: Ved å åpne kursrepoet i VS Code, har du muligheten til å sette opp prosjektet i en container. Dette skyldes den [spesielle `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) katalogen som finnes i kursrepoet. Mer om dette senere.

> **Merk**: Når du kloner og åpner katalogen i VS Code, vil det automatisk foreslå at du installerer en Python-støtteutvidelse.

> **Merk**: Hvis VS Code foreslår at du åpner repoet i en container, avslå denne forespørselen for å bruke den lokalt installerte versjonen av Python.

### Bruke Jupyter i nettleseren

Du kan også jobbe med prosjektet ved å bruke [Jupyter-miljøet](https://jupyter.org?WT.mc_id=academic-105485-koreyst) rett i nettleseren din. Både klassisk Jupyter og [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) gir et behagelig utviklingsmiljø med funksjoner som automatisk utfylling, kodeutheving, osv.

For å starte Jupyter lokalt, gå til terminalen/kommandolinjen, naviger til kurskatalogen, og kjør:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Dette vil starte en Jupyter-instans, og URL-en for å få tilgang til den vil bli vist i kommandolinjevinduet.

Når du får tilgang til URL-en, bør du se kursoversikten og kunne navigere til hvilken som helst `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md`-fil hvor du kan se koden og resultatene.

## Bruke Azure OpenAI-tjenesten for første gang

Hvis dette er første gang du jobber med Azure OpenAI-tjenesten, vennligst følg denne guiden om hvordan du [oppretter og distribuerer en Azure OpenAI-tjenesteressurs.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Bruke OpenAI API for første gang

Hvis dette er første gang du jobber med OpenAI API, vennligst følg guiden om hvordan du [oppretter og bruker grensesnittet.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Møt andre lærere

Vi har opprettet kanaler i vår offisielle [AI Community Discord-server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) for å møte andre lærere. Dette er en flott måte å knytte nettverk med andre likesinnede entreprenører, byggere, studenter og alle som ønsker å utvikle seg innen Generativ AI.

[![Bli med i Discord-kanalen](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Prosjektteamet vil også være på denne Discord-serveren for å hjelpe lærere.

## Bidra

Dette kurset er et åpen kildekode-initiativ. Hvis du ser områder som kan forbedres eller problemer, vennligst opprett en [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) eller logg et [GitHub-problem](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Prosjektteamet vil spore alle bidrag. Å bidra til åpen kildekode er en fantastisk måte å bygge karrieren din innen Generativ AI.

De fleste bidrag krever at du godtar en Contributor License Agreement (CLA) som erklærer at du har rett til og faktisk gir oss rettighetene til å bruke ditt bidrag. For detaljer, besøk [CLA, Contributor License Agreement-nettstedet](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Viktig: når du oversetter tekst i dette repoet, vennligst sørg for at du ikke bruker maskinoversettelse. Vi vil verifisere oversettelser via samfunnet, så vennligst bare meld deg frivillig for oversettelser på språk der du er dyktig.

Når du sender inn en pull request, vil en CLA-bot automatisk bestemme om du trenger å gi en CLA og dekorere PR-en deretter (f.eks. etikett, kommentar). Følg bare instruksjonene gitt av boten. Du trenger bare å gjøre dette én gang på tvers av alle repositorier som bruker vår CLA.

Dette prosjektet har vedtatt [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). For mer informasjon, les Code of Conduct FAQ eller kontakt [Email opencode](opencode@microsoft.com) med eventuelle spørsmål eller kommentarer.

## La oss komme i gang

Nå som du har fullført de nødvendige trinnene for å fullføre dette kurset, la oss komme i gang med en [introduksjon til Generativ AI og LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Ansvarsfraskrivelse**:  
Dette dokumentet har blitt oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår fra bruken av denne oversettelsen.