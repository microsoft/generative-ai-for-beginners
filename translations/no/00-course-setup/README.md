<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T07:11:40+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "no"
}
-->
# Kom i gang med dette kurset

Vi er veldig glade for at du skal starte dette kurset og se hva du blir inspirert til å bygge med Generativ AI!

For å sikre at du lykkes, beskriver denne siden oppsettsteg, tekniske krav og hvor du kan få hjelp om nødvendig.

## Oppsettsteg

For å begynne på dette kurset må du fullføre følgende steg.

### 1. Fork dette repoet

[Fork hele dette repoet](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) til din egen GitHub-konto for å kunne endre kode og fullføre utfordringene. Du kan også [starte (🌟) dette repoet](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) for å finne det og relaterte repoer enklere.

### 2. Opprett en codespace

For å unngå avhengighetsproblemer når du kjører koden, anbefaler vi å kjøre dette kurset i en [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Dette kan opprettes ved å velge `Code`-alternativet på din forkede versjon av dette repoet og deretter velge **Codespaces**-alternativet.

![Dialog som viser knapper for å opprette en codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Lagring av API-nøkler

Det er viktig å holde API-nøklene dine trygge og sikre når du bygger applikasjoner. Vi anbefaler at du ikke lagrer API-nøkler direkte i koden din. Å legge disse detaljene i et offentlig repo kan føre til sikkerhetsproblemer og uønskede kostnader hvis de blir misbrukt.

Her er en steg-for-steg guide for hvordan du lager en `.env`-fil for Python og legger til `GITHUB_TOKEN`:

1. **Naviger til prosjektmappen din**: Åpne terminalen eller kommandolinjen og gå til rotmappen for prosjektet der du vil opprette `.env`-filen.

   ```bash
   cd path/to/your/project
   ```

2. **Opprett `.env`-filen**: Bruk din foretrukne teksteditor for å lage en ny fil kalt `.env`. Hvis du bruker kommandolinjen, kan du bruke `touch` (på Unix-baserte systemer) eller `echo` (på Windows):

   Unix-baserte systemer:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Rediger `.env`-filen**: Åpne `.env`-filen i en teksteditor (f.eks. VS Code, Notepad++ eller annen editor). Legg til følgende linje i filen, og erstatt `your_github_token_here` med din faktiske GitHub-token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Lagre filen**: Lagre endringene og lukk teksteditoren.

5. **Installer `python-dotenv`**: Hvis du ikke allerede har gjort det, må du installere `python-dotenv`-pakken for å kunne laste miljøvariabler fra `.env`-filen inn i Python-applikasjonen din. Du kan installere den med `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Last miljøvariabler i Python-skriptet ditt**: I Python-skriptet ditt, bruk `python-dotenv`-pakken for å laste miljøvariablene fra `.env`-filen:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Det var det! Du har nå opprettet en `.env`-fil, lagt til GitHub-tokenen din, og lastet den inn i Python-applikasjonen.

## Hvordan kjøre lokalt på din datamaskin

For å kjøre koden lokalt på din datamaskin, må du ha en versjon av [Python installert](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

For å bruke repoet må du klone det:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Når du har alt på plass, kan du sette i gang!

## Valgfrie steg

### Installere Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) er en lettvektsinstaller for å installere [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, samt noen pakker.

Conda er en pakkebehandler som gjør det enkelt å sette opp og bytte mellom ulike Python [**virtuelle miljøer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) og pakker. Det er også nyttig for å installere pakker som ikke er tilgjengelige via `pip`.

Du kan følge [Miniconda installasjonsguide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) for å sette det opp.

Når Miniconda er installert, må du klone [repoet](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (hvis du ikke allerede har gjort det).

Deretter må du opprette et virtuelt miljø. For å gjøre dette med Conda, lag en ny miljøfil (_environment.yml_). Hvis du følger med i Codespaces, opprett denne i `.devcontainer`-mappen, altså `.devcontainer/environment.yml`.

Fyll miljøfilen med kodesnutten under:

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

Hvis du får feil ved bruk av conda, kan du manuelt installere Microsoft AI Libraries med følgende kommando i terminalen.

```
conda install -c microsoft azure-ai-ml
```

Miljøfilen spesifiserer avhengighetene vi trenger. `<environment-name>` er navnet du ønsker å bruke for Conda-miljøet ditt, og `<python-version>` er Python-versjonen du vil bruke, for eksempel `3` som er siste hovedversjon av Python.

Når dette er gjort, kan du opprette Conda-miljøet ved å kjøre kommandoene under i kommandolinjen/terminalen:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Se [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) hvis du støter på problemer.

### Bruke Visual Studio Code med Python-støtteutvidelsen

Vi anbefaler å bruke [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) med [Python-støtteutvidelsen](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installert for dette kurset. Dette er imidlertid en anbefaling, ikke et absolutt krav.

> **Note**: Ved å åpne kursrepoet i VS Code, har du muligheten til å sette opp prosjektet i en container. Dette er mulig på grunn av den [spesielle `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)-mappen i kursrepoet. Mer om dette senere.

> **Note**: Når du kloner og åpner mappen i VS Code, vil det automatisk foreslå å installere Python-støtteutvidelsen.

> **Note**: Hvis VS Code foreslår at du åpner repoet i en container, kan du avslå dette for å bruke den lokalt installerte versjonen av Python.

### Bruke Jupyter i nettleseren

Du kan også jobbe med prosjektet ved å bruke [Jupyter-miljøet](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direkte i nettleseren. Både klassisk Jupyter og [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) gir et behagelig utviklingsmiljø med funksjoner som autfullføring, kodesyntaksutheving, osv.

For å starte Jupyter lokalt, gå til terminalen/kommandolinjen, naviger til kursmappen, og kjør:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Dette starter en Jupyter-instans, og URL-en for å få tilgang til den vises i kommandolinjevinduet.

Når du åpner URL-en, skal du se kursoversikten og kunne navigere til alle `*.ipynb`-filer. For eksempel `08-building-search-applications/python/oai-solution.ipynb`.

### Kjøre i en container

Et alternativ til å sette opp alt på din datamaskin eller i Codespace er å bruke en [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Den spesielle `.devcontainer`-mappen i kursrepoet gjør det mulig for VS Code å sette opp prosjektet i en container. Utenfor Codespaces krever dette installasjon av Docker, og det kan være litt arbeid, så vi anbefaler dette kun for de med erfaring med containere.

En av de beste måtene å holde API-nøklene dine sikre når du bruker GitHub Codespaces, er ved å bruke Codespace Secrets. Følg [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) for å lære mer om dette.

## Leksjoner og tekniske krav

Kurset har 6 konseptleksjoner og 6 kodelesjoner.

For kodeleksjonene bruker vi Azure OpenAI Service. Du må ha tilgang til Azure OpenAI-tjenesten og en API-nøkkel for å kjøre koden. Du kan søke om tilgang ved å [fullføre denne søknaden](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Mens du venter på at søknaden din behandles, inkluderer hver kodeleksjon også en `README.md`-fil hvor du kan se koden og resultatene.

## Bruke Azure OpenAI Service for første gang

Hvis dette er første gang du bruker Azure OpenAI-tjenesten, følg denne guiden for hvordan du [oppretter og distribuerer en Azure OpenAI Service-ressurs.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Bruke OpenAI API for første gang

Hvis dette er første gang du bruker OpenAI API, følg guiden for hvordan du [oppretter og bruker grensesnittet.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Møt andre deltakere

Vi har opprettet kanaler i vår offisielle [AI Community Discord-server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) for å møte andre deltakere. Dette er en flott måte å knytte nettverk med andre likesinnede gründere, utviklere, studenter og alle som ønsker å bli bedre innen Generativ AI.

[![Bli med i discord-kanalen](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Prosjektteamet vil også være på denne Discord-serveren for å hjelpe deltakere.

## Bidra

Dette kurset er et åpen kildekode-initiativ. Hvis du ser forbedringsmuligheter eller problemer, vennligst opprett en [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) eller logg en [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Prosjektteamet følger med på alle bidrag. Å bidra til åpen kildekode er en fantastisk måte å bygge karrieren din innen Generativ AI.

De fleste bidrag krever at du godtar en Contributor License Agreement (CLA) som bekrefter at du har rett til, og faktisk gir oss rettighetene til å bruke bidraget ditt. For detaljer, besøk [CLA, Contributor License Agreement-nettsiden](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Viktig: når du oversetter tekst i dette repoet, må du sørge for at du ikke bruker maskinoversettelse. Vi vil verifisere oversettelser via fellesskapet, så vær vennlig å bare melde deg som frivillig for oversettelser på språk du behersker godt.

Når du sender inn en pull request, vil en CLA-bot automatisk avgjøre om du må levere en CLA og merke PR-en deretter (f.eks. med etikett eller kommentar). Følg bare instruksjonene fra boten. Du trenger bare gjøre dette én gang for alle repoer som bruker vår CLA.

Dette prosjektet har tatt i bruk [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). For mer informasjon, les Code of Conduct FAQ eller kontakt [Email opencode](opencode@microsoft.com) ved spørsmål eller kommentarer.

## La oss komme i gang

Nå som du har fullført nødvendige steg for å gjennomføre kurset, la oss starte med en [introduksjon til Generativ AI og LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.