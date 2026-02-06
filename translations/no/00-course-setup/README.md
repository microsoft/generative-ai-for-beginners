# Komme i gang med dette kurset

Vi er veldig begeistret for at du skal starte dette kurset og se hva du blir inspirert til å bygge med Generativ AI!

For å sikre din suksess, skisserer denne siden oppsettstrinn, tekniske krav og hvor du kan få hjelp om nødvendig.

## Oppsettstrinn

For å begynne å ta dette kurset, må du fullføre følgende trinn.

### 1. Fork dette repoet

[Fork hele repoet](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) til din egen GitHub-konto for å kunne endre kode og fullføre utfordringene. Du kan også [starte (🌟) dette repoet](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) for å finne det og relaterte repoer enklere.

### 2. Opprett en codespace

For å unngå avhengighetsproblemer når du kjører koden, anbefaler vi å kjøre dette kurset i en [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

I din fork: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/no/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Legg til en hemmelighet

1. ⚙️ Girkuleikon -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Navn OPENAI_API_KEY, lim inn nøkkelen din, Lagre.

### 3. Hva nå?

| Jeg vil…               | Gå til…                                                                  |
|------------------------|-------------------------------------------------------------------------|
| Starte Lekse 1         | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Jobbe offline          | [`setup-local.md`](02-setup-local.md)                                   |
| Sette opp en LLM-leverandør | [`providers.md`](03-providers.md)                                       |
| Møte andre deltakere   | [Bli med i Discorden vår](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Feilsøking


| Symptom                                    | Løsning                                                           |
|--------------------------------------------|------------------------------------------------------------------|
| Bygging av container står fast > 10 min   | **Codespaces ➜ “Rebuild Container”**                             |
| `python: command not found`                  | Terminalen er ikke koblet; klikk **+** ➜ *bash*                  |
| `401 Unauthorized` fra OpenAI               | Feil / utløpt `OPENAI_API_KEY`                                   |
| VS Code viser “Dev container mounting…”     | Oppdater nettleserfanen—Codespaces mister noen ganger tilkobling |
| Manglende notebook-kjerne                   | Notebook-meny ➜ **Kernel ▸ Select Kernel ▸ Python 3**            |

   Unix-baserte systemer:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Rediger `.env`-filen**: Åpne `.env`-filen i en teksteditor (f.eks. VS Code, Notepad++, eller en annen editor). Legg til følgende linje i filen, erstatt `your_github_token_here` med din faktiske GitHub-token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Lagre filen**: Lagre endringene og lukk teksteditoren.

5. **Installer `python-dotenv`**: Hvis du ikke har gjort det allerede, må du installere `python-dotenv`-pakken for å kunne laste miljøvariabler fra `.env`-filen inn i Python-applikasjonen din. Du kan installere den med `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Last miljøvariabler inn i Python-skriptet ditt**: I Python-skriptet ditt, bruk `python-dotenv`-pakken for å laste miljøvariabler fra `.env`-filen:

   ```python
   from dotenv import load_dotenv
   import os

   # Last miljøvariabler fra .env-fil
   load_dotenv()

   # Få tilgang til GITHUB_TOKEN-variabelen
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Det er det! Du har nå opprettet en `.env`-fil, lagt til din GitHub-token og lastet den inn i Python-applikasjonen din.

## Hvordan kjøre lokalt på datamaskinen din

For å kjøre koden lokalt på datamaskinen din, må du ha en versjon av [Python installert](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

For å bruke repoet, må du deretter klone det:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Når alt er sjekket ut, kan du komme i gang!

## Valgfrie trinn

### Installere Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) er en lettvektsinstallerer for å installere [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, samt noen pakker.  
Conda er i seg selv en pakkehåndterer som gjør det enkelt å sette opp og bytte mellom forskjellige Python [**virtuelle miljøer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) og pakker. Det er også nyttig for å installere pakker som ikke er tilgjengelige via `pip`.

Du kan følge [MiniConda installasjonsveiledning](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) for å få det opp og gå.

Når Miniconda er installert, trenger du å klone [repoet](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (om du ikke allerede har gjort det)

Deretter må du lage et virtuelt miljø. For å gjøre dette med Conda, opprett en ny miljøfil (_environment.yml_). Hvis du følger med i Codespaces, opprett denne i `.devcontainer`-mappen, altså `.devcontainer/environment.yml`.

Fyll miljøfilen med følgende utdrag:

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

Miljøfilen spesifiserer avhengighetene vi trenger. `<environment-name>` refererer til navnet du vil bruke for ditt Conda-miljø, og `<python-version>` er versjonen av Python du ønsker å bruke, for eksempel er `3` den nyeste hovedversjonen av Python.

Når dette er gjort kan du opprette Conda-miljøet ved å kjøre kommandoene nedenfor i kommandolinjen/terminalen

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer understi gjelder kun for Codespace-oppsett
conda activate ai4beg
```

Se [Conda miljøveiledning](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) hvis du støter på problemer.

### Bruke Visual Studio Code med Python-støtteutvidelsen

Vi anbefaler å bruke [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editoren med [Python-støtteutvidelsen](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installert for dette kurset. Dette er imidlertid et anbefalt valg, ikke et absolutt krav.

> **Merk**: Ved å åpne kursrepoet i VS Code har du muligheten til å sette opp prosjektet i en container. Dette er på grunn av den [spesielle `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) mappen som finnes i kursrepoet. Mer om dette senere.

> **Merk**: Når du kloner og åpner mappen i VS Code, vil det automatisk foreslå at du installerer en Python-støtteutvidelse.

> **Merk**: Hvis VS Code foreslår at du åpner repoet i en container på nytt, avslå dette for å bruke den lokalt installerte versjonen av Python.

### Bruke Jupyter i nettleseren

Du kan også jobbe med prosjektet ved å bruke [Jupyter-miljøet](https://jupyter.org?WT.mc_id=academic-105485-koreyst) rett i nettleseren din. Både klassisk Jupyter og [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) gir et meget behagelig utviklingsmiljø med funksjoner som autokomplettering, kodeutheving, osv.

For å starte Jupyter lokalt, gå til terminalen/kommandolinjen, naviger til kursmappen og kjør:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Dette vil starte en Jupyter-forekomst, og URL-en for å få tilgang til den vises i kommandolinjevinduet.

Når du får tilgang til URL-en, skal du se kursoversikten og kunne navigere til enhver `*.ipynb`-fil. For eksempel `08-building-search-applications/python/oai-solution.ipynb`.

### Kjøring i en container

Et alternativ til å sette opp alt på din egen datamaskin eller Codespace er å kjøre i en [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Den spesielle `.devcontainer`-mappen i kursrepoet gjør det mulig for VS Code å sette opp prosjektet i en container. Utover Codespaces krever dette installasjon av Docker, og for å være ærlig, krever dette noe mer arbeid, så vi anbefaler dette kun til de med erfaring med containere.

En av de beste måtene å holde API-nøkler sikre når du bruker GitHub Codespaces, er å bruke Codespace Secrets. Vennligst følg [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guiden for mer informasjon.

## Leksjoner og tekniske krav

Kurset inneholder 6 konseptuelle leksjoner og 6 kodelesjoner.

For kodeleksjonene bruker vi Azure OpenAI Service. Du må ha tilgang til Azure OpenAI-tjenesten og en API-nøkkel for å kjøre denne koden. Du kan søke om tilgang ved å [fullføre denne søknaden](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Mens du venter på at søknaden din skal behandles, inkluderer hver kodeleksjon også en `README.md`-fil hvor du kan se koden og resultatene.

## Bruke Azure OpenAI Service for første gang

Hvis dette er første gang du bruker Azure OpenAI-tjenesten, vennligst følg denne guiden om hvordan du [oppretter og distribuerer en Azure OpenAI Service-ressurs.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Bruke OpenAI API for første gang

Hvis dette er første gang du jobber med OpenAI API, vennligst følg guiden for hvordan du [oppretter og bruker grensesnittet.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Møt andre deltakere

Vi har opprettet kanaler i vår offisielle [AI Community Discord-server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) for å møte andre deltakere. Dette er en flott måte å knytte nettverk med likesinnede gründere, utviklere, studenter og alle som ønsker å bli bedre innen Generativ AI.

[![Bli med i discordkanalen](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Prosjektteamet vil også være på denne Discord-serveren for å hjelpe deltakerne.

## Bidra

Dette kurset er et åpen kildekode-initiativ. Hvis du ser forbedringsområder eller problemer, vennligst opprett en [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) eller loggfør en [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Prosjektteamet vil følge med på alle bidrag. Å bidra til åpen kildekode er en fantastisk måte å bygge din karriere innen Generativ AI på.

De fleste bidrag krever at du godtar en Contributor License Agreement (CLA) som erklærer at du har rett til og faktisk gir oss rett til å bruke ditt bidrag. For detaljer, besøk [CLA, Contributor License Agreement nettsiden](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Viktig: når du oversetter tekst i dette repoet, vennligst sørg for å ikke bruke maskinoversettelse. Vi vil verifisere oversettelser via samfunnet, så vennligst meld deg kun til oversettelser i språk du behersker godt.

Når du sender inn en pull request, vil en CLA-bot automatisk avgjøre om du må levere en CLA og merke PR-en deretter (f.eks. med etikett, kommentar). Følg bare instruksjonene bot-en gir. Du trenger bare å gjøre dette én gang for alle repoene som bruker vår CLA.

Dette prosjektet har adoptert [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). For mer informasjon, les Code of Conduct FAQ eller kontakt [Email opencode](opencode@microsoft.com) med spørsmål eller kommentarer.

## La oss komme i gang
Nå som du har fullført de nødvendige trinnene for å fullføre dette kurset, la oss komme i gang med en [introduksjon til generativ AI og LLM-er](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell, menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->