<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T17:33:48+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "no"
}
-->
# Kom i gang med dette kurset

Vi gleder oss til at du skal starte dette kurset og se hva du blir inspirert til å bygge med Generativ AI!

For at du skal lykkes, har vi samlet oppsettsteg, tekniske krav og hvor du kan få hjelp om du trenger det.

## Oppsettsteg

For å komme i gang med kurset, må du gjøre følgende:

### 1. Fork dette repoet

[Fork hele dette repoet](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) til din egen GitHub-konto, slik at du kan endre kode og løse oppgavene. Du kan også [star (🌟) dette repoet](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) for å finne det og relaterte repoer enklere.

### 2. Opprett en codespace

For å unngå avhengighetsproblemer når du kjører koden, anbefaler vi å bruke [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) til dette kurset.

I din fork: **Code -> Codespaces -> New on main**

![Dialog som viser knapper for å opprette codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Legg til en hemmelighet

1. ⚙️ Tannhjul-ikon -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Navngi OPENAI_API_KEY, lim inn nøkkelen din, og lagre.

### 3. Hva skjer videre?

| Jeg vil…             | Gå til…                                                                 |
|----------------------|-------------------------------------------------------------------------|
| Starte leksjon 1     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Jobbe offline        | [`setup-local.md`](02-setup-local.md)                                   |
| Sette opp en LLM-leverandør | [`providers.md`](providers.md)                                   |
| Møte andre deltakere | [Bli med på Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Feilsøking

| Symptom                                   | Løsning                                                        |
|-------------------------------------------|----------------------------------------------------------------|
| Container-bygget henger > 10 min          | **Codespaces ➜ “Rebuild Container”**                           |
| `python: command not found`               | Terminalen er ikke koblet til; klikk **+** ➜ *bash*            |
| `401 Unauthorized` fra OpenAI             | Feil / utløpt `OPENAI_API_KEY`                                 |
| VS Code viser “Dev container mounting…”   | Oppdater nettleserfanen—Codespaces mister noen ganger tilkoblingen |
| Notebook-kjerne mangler                   | Notebook-meny ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

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

5. **Installer `python-dotenv`**: Hvis du ikke har gjort det før, må du installere `python-dotenv`-pakken for å laste miljøvariabler fra `.env`-filen inn i Python-applikasjonen din. Du kan installere den med `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Last miljøvariabler i Python-scriptet ditt**: I Python-scriptet ditt, bruk `python-dotenv`-pakken for å laste miljøvariablene fra `.env`-filen:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Det var det! Du har nå opprettet en `.env`-fil, lagt til GitHub-tokenet ditt, og lastet det inn i Python-applikasjonen din.

## Slik kjører du lokalt på din datamaskin

For å kjøre koden lokalt på din datamaskin, må du ha en versjon av [Python installert](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

For å bruke repoet, må du klone det:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Når du har alt klart, kan du starte!

## Valgfrie steg

### Installere Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) er en lettvektsinstaller for å installere [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python og noen få pakker.
Conda er en pakkebehandler som gjør det enkelt å sette opp og bytte mellom ulike Python [**virtuelle miljøer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) og pakker. Den er også nyttig for å installere pakker som ikke er tilgjengelige via `pip`.

Du kan følge [MiniConda installasjonsguide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) for å sette det opp.

Når Miniconda er installert, må du klone [repoet](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (hvis du ikke har gjort det allerede).

Deretter må du opprette et virtuelt miljø. For å gjøre dette med Conda, lag en ny miljøfil (_environment.yml_). Hvis du følger med i Codespaces, lag denne i `.devcontainer`-mappen, altså `.devcontainer/environment.yml`.

Fyll miljøfilen med følgende kode:

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

Hvis du får feil med conda, kan du manuelt installere Microsoft AI Libraries med følgende kommando i terminalen.

```
conda install -c microsoft azure-ai-ml
```

Miljøfilen spesifiserer avhengighetene vi trenger. `<environment-name>` er navnet du vil bruke på Conda-miljøet ditt, og `<python-version>` er versjonen av Python du vil bruke, for eksempel `3` som er siste hovedversjon.

Når det er gjort, kan du opprette Conda-miljøet ditt ved å kjøre disse kommandoene i kommandolinjen/terminalen

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Se [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) hvis du får problemer.

### Bruke Visual Studio Code med Python-utvidelsen

Vi anbefaler å bruke [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) med [Python-utvidelsen](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installert til dette kurset. Dette er kun en anbefaling, ikke et krav.

> **Note**: Når du åpner kursrepoet i VS Code, kan du sette opp prosjektet i en container. Dette er mulig på grunn av [spesiell `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)-mappen i repoet. Mer om dette senere.

> **Note**: Når du kloner og åpner mappen i VS Code, vil du automatisk få forslag om å installere Python-utvidelsen.

> **Note**: Hvis VS Code foreslår å åpne repoet i en container, avvis dette for å bruke den lokale Python-versjonen.

### Bruke Jupyter i nettleseren

Du kan også jobbe med prosjektet i [Jupyter-miljøet](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direkte i nettleseren. Både klassisk Jupyter og [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) gir et godt utviklingsmiljø med funksjoner som autoutfylling, kodefremheving osv.

For å starte Jupyter lokalt, gå til terminalen/kommandolinjen, naviger til kursmappen, og kjør:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Dette starter en Jupyter-instans, og du får opp URL-en for å åpne den i nettleseren.

Når du åpner URL-en, vil du se kursoversikten og kan navigere til hvilken som helst `*.ipynb`-fil. For eksempel, `08-building-search-applications/python/oai-solution.ipynb`.

### Kjøre i en container

Et alternativ til å sette opp alt på din datamaskin eller Codespace er å bruke en [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Den spesielle `.devcontainer`-mappen i kursrepoet gjør det mulig for VS Code å sette opp prosjektet i en container. Utenfor Codespaces krever dette at du installerer Docker, og det er litt mer arbeid, så vi anbefaler dette kun for de som har erfaring med containere.

En av de beste måtene å holde API-nøklene dine sikre når du bruker GitHub Codespaces, er å bruke Codespace Secrets. Følg [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst)-guiden for å lære mer om dette.

## Leksjoner og tekniske krav

Kurset har 6 konseptleksjoner og 6 kodeleksjoner.

For kodeleksjonene bruker vi Azure OpenAI Service. Du må ha tilgang til Azure OpenAI-tjenesten og en API-nøkkel for å kjøre koden. Du kan søke om tilgang ved å [fylle ut denne søknaden](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Mens du venter på at søknaden din blir behandlet, har hver kodeleksjon også en `README.md`-fil hvor du kan se kode og resultater.

## Bruke Azure OpenAI Service for første gang

Hvis dette er første gang du jobber med Azure OpenAI-tjenesten, følg denne guiden for å [opprette og distribuere en Azure OpenAI Service-ressurs.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Bruke OpenAI API for første gang

Hvis dette er første gang du jobber med OpenAI API, følg guiden for å [opprette og bruke grensesnittet.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Møt andre deltakere

Vi har opprettet kanaler på vår offisielle [AI Community Discord-server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) for å møte andre deltakere. Dette er en fin måte å knytte kontakter med andre gründere, utviklere, studenter og alle som vil lære mer om Generativ AI.

[![Bli med i discord-kanalen](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Prosjektteamet vil også være på Discord-serveren for å hjelpe deltakere.

## Bidra

Dette kurset er et åpen kildekode-initiativ. Hvis du ser forbedringsmuligheter eller problemer, lag gjerne en [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) eller opprett en [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Prosjektteamet følger med på alle bidrag. Å bidra til åpen kildekode er en flott måte å bygge karrieren din innen Generativ AI.

De fleste bidrag krever at du godtar en Contributor License Agreement (CLA) som bekrefter at du har rett til, og faktisk gir oss rett til å bruke bidraget ditt. For detaljer, se [CLA, Contributor License Agreement-nettsiden](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Viktig: Når du oversetter tekst i dette repoet, må du ikke bruke maskinoversettelse. Vi vil verifisere oversettelser via fellesskapet, så kun frivillige med gode språkkunnskaper bør bidra.

Når du sender inn en pull request, vil en CLA-bot automatisk sjekke om du må godta en CLA og merke PR-en deretter (f.eks. med etikett, kommentar). Følg bare instruksjonene fra boten. Du trenger kun å gjøre dette én gang for alle repoer som bruker vår CLA.

Dette prosjektet følger [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). For mer informasjon, les Code of Conduct FAQ eller kontakt [Email opencode](opencode@microsoft.com) hvis du har spørsmål eller kommentarer.

## La oss komme i gang
Nå som du har fullført de nødvendige stegene for å ta dette kurset, la oss starte med å få en [introduksjon til Generativ AI og LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.