# Komme i gang med dette kurset

Vi er veldig spente på at du skal starte dette kurset og se hva du blir inspirert til å bygge med Generativ AI!

For å sikre din suksess, skisserer denne siden oppsettstrinn, tekniske krav og hvor du kan få hjelp hvis nødvendig.

## Oppsettstrinn

For å begynne å ta dette kurset, må du fullføre følgende trinn.

### 1. Fork dette repositoriet

[Fork hele dette repositoriet](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) til din egen GitHub-konto for å kunne endre kode og fullføre utfordringene. Du kan også [starte (🌟) dette repoet](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) for å lettere finne det og relaterte repoer.

### 2. Opprett et codespace

For å unngå avhengighetsproblemer når du kjører koden, anbefaler vi å kjøre dette kurset i en [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

I din fork: **Code -> Codespaces -> New on main**

![Dialog som viser knapper for å opprette en codespace](../../../translated_images/no/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Legg til en hemmelighet

1. ⚙️ Gear-ikon -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Navn OPENAI_API_KEY, lim inn nøkkelen din, Lagre.

### 3. Hva nå?

| Jeg vil…           | Gå til…                                                                |
|---------------------|-------------------------------------------------------------------------|
| Starte Lekse 1      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Jobbe offline       | [`setup-local.md`](02-setup-local.md)                                   |
| Sett opp en LLM-leverandør | [`providers.md`](03-providers.md)                                        |
| Møte andre lærende  | [Bli med i vår Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Feilsøking


| Symptom                                   | Løsning                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| Containeroppsett sitter fast > 10 min      | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminalen festet ikke; klikk **+** ➜ *bash*                    |
| `401 Unauthorized` fra OpenAI             | Feil / utløpt `OPENAI_API_KEY`                                  |
| VS Code viser “Dev container mounting…”   | Oppdater nettleserfanen—Codespaces mister noen ganger tilkoblingen   |
| Manglende notebook-kjerne                  | Notebook-meny ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix-baserte systemer:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Rediger `.env`-filen**: Åpne `.env`-filen i en tekstredigerer (f.eks. VS Code, Notepad++ eller en annen redigerer). Legg til følgende linjer i filen, og erstatt plassholderne med din faktiske Microsoft Foundry Models-endepunkt og nøkkel (se [`providers.md`](03-providers.md) for hvordan du får disse):

   > **Merk:** GitHub Models (og dens `GITHUB_TOKEN`-variabel) avvikles ved slutten av juli 2026. Bruk [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) i stedet.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Lagre filen**: Lagre endringene og lukk tekstredigereren.

5. **Installer `python-dotenv`**: Hvis du ikke allerede har gjort det, må du installere `python-dotenv`-pakken for å laste miljøvariabler fra `.env`-filen inn i Python-applikasjonen din. Du kan installere den med `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Last miljøvariabler i Python-scriptet ditt**: Bruk i Python-scriptet ditt `python-dotenv`-pakken for å laste miljøvariablene fra `.env`-filen:

   ```python
   from dotenv import load_dotenv
   import os

   # Last miljøvariabler fra .env-fil
   load_dotenv()

   # Få tilgang til Microsoft Foundry Models-variablene
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Det var det! Du har nå opprettet en `.env`-fil, lagt til Microsoft Foundry Models-legitimasjonen din og lastet den inn i Python-applikasjonen.

## Hvordan kjøre lokalt på din datamaskin

For å kjøre koden lokalt på datamaskinen din, må du ha en versjon av [Python installert](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

For å bruke depotet må du klone det:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Når du har alt sjekket ut, kan du begynne!

## Valgfrie trinn

### Installere Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) er en lettvektsinstallerer for installasjon av [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, samt noen pakker.
Conda i seg selv er en pakkeadministrator som gjør det enkelt å sette opp og bytte mellom ulike Python [**virtuelle miljøer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) og pakker. Det er også nyttig for å installere pakker som ikke er tilgjengelige via `pip`.

Du kan følge [Miniconda installasjonsveiledningen](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) for å sette det opp.

Med Miniconda installert, må du klone [depotet](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (hvis du ikke allerede har gjort det)

Deretter må du opprette et virtuelt miljø. For å gjøre dette med Conda, lag en ny miljøfil (_environment.yml_). Hvis du følger med på Codespaces, opprett denne innenfor `.devcontainer`-mappen, altså `.devcontainer/environment.yml`.

Fyll ut miljøfilen din med utdraget nedenfor:

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

Hvis du får feil ved bruk av conda, kan du manuelt installere Microsoft AI Libraries med følgende kommando i en terminal.

```
conda install -c microsoft azure-ai-ml
```

Miljøfilen spesifiserer avhengighetene vi trenger. `<environment-name>` refererer til navnet du ønsker å bruke for Conda-miljøet ditt, og `<python-version>` er Python-versjonen du vil bruke, for eksempel `3` som er siste hovedversjon av Python.

Når dette er gjort, kan du opprette Conda-miljøet ved å kjøre kommandoene nedenfor i kommandolinjen/terminalen

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer understi gjelder kun for Codespace-oppsett
conda activate ai4beg
```

Se [Conda miljøguide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) hvis du får problemer.

### Bruke Visual Studio Code med Python-støtteutvidelsen

Vi anbefaler å bruke [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) med [Python-støtteutvidelsen](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) installert for dette kurset. Dette er imidlertid en anbefaling og ikke et absolutt krav.

> **Merk**: Ved å åpne kursdepotet i VS Code, har du muligheten til å sette opp prosjektet i en container. Dette er mulig på grunn av den [spesielle `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)-mappen som finnes i kursdepotet. Mer om dette senere.

> **Merk**: Når du kloner og åpner katalogen i VS Code, vil det automatisk foreslå å installere en Python-støtteutvidelse.

> **Merk**: Hvis VS Code foreslår at du åpner depotet i en container, avvis denne forespørselen for å bruke den lokalt installerte versjonen av Python.

### Bruke Jupyter i nettleseren

Du kan også jobbe med prosjektet ved å bruke [Jupyter-miljøet](https://jupyter.org?WT.mc_id=academic-105485-koreyst) rett i nettleseren din. Både klassisk Jupyter og [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) gir et hyggelig utviklingsmiljø med funksjoner som autokomplettering, kodeutheving osv.

For å starte Jupyter lokalt, gå til terminalen/kommandolinjen, naviger til kurskatalogen, og kjør:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Dette starter en Jupyter-instans, og URL-en for tilgang vises i kommandolinjevinduet.

Når du får tilgang til URL-en, bør du se kursoversikten og kunne navigere til hvilken som helst `*.ipynb`-fil. For eksempel `08-building-search-applications/python/oai-solution.ipynb`.

### Kjøre i en container

Et alternativ til å sette opp alt på datamaskinen eller i Codespace er å bruke en [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Den spesielle `.devcontainer`-mappen i kursdepotet gjør det mulig for VS Code å sette opp prosjektet i en container. Utenfor Codespaces krever dette installasjon av Docker, og det krever en del arbeid, så vi anbefaler dette kun for de med erfaring med containere.

En av de beste metodene for å holde API-nøkler sikre når du bruker GitHub Codespaces er ved å bruke Codespace Secrets. Følg gjerne [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst)-veiledningen for å lære mer om dette.


## Leksjoner og tekniske krav

Kurset inneholder "Lær"-leksjoner som forklarer konsepter innen Generativ AI, og "Bygg"-leksjoner med praktiske kodeeksempler i både **Python** og **TypeScript** der det er mulig.

For koding bruker vi Azure OpenAI i Microsoft Foundry. Du trenger et Azure-abonnement og en API-nøkkel. Tilgangen er åpen - ingen søknad nødvendig - så du kan [opprette en Microsoft Foundry-ressurs og distribuere en modell](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) for å få endepunkt og nøkkel.

Hver koding-leksjon inneholder også en `README.md`-fil der du kan se kode og resultater uten å kjøre noe.

## Bruke Azure OpenAI-tjenesten for første gang

Hvis du bruker Azure OpenAI-tjenesten for første gang, følg denne veiledningen om hvordan du [oppretter og distribuerer en Azure OpenAI-tjenesteressurs.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Bruke OpenAI-APIen for første gang

Hvis du bruker OpenAI-APIen for første gang, følg veiledningen om hvordan du [oppretter og bruker grensesnittet.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Møt andre lærende

Vi har opprettet kanaler i vår offisielle [AI Community Discord-server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) for å møte andre lærende. Dette er en flott måte å knytte nettverk med andre med lignende interesser, entreprenører, utviklere, studenter og alle som ønsker å bli bedre i Generativ AI.

[![Bli med i discord-kanal](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Prosjektteamet vil også være på denne Discord-serveren for å hjelpe alle lærende.

## Bidra

Dette kurset er et åpen kildekode-initiativ. Hvis du ser forbedringsområder eller problemer, vennligst opprett en [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) eller registrer en [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Prosjektteamet følger med på alle bidrag. Å bidra til åpen kildekode er en fantastisk måte å bygge karrieren din innen Generativ AI.

De fleste bidrag krever at du godtar en Contributor License Agreement (CLA) som erklærer at du har rett til, og faktisk gir oss, rettigheter til å bruke bidraget ditt. For detaljer, se [CLA, Contributor License Agreement-nettsiden](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Viktig: Når du oversetter tekst i dette repoet, vennligst ikke bruk maskinoversettelse. Vi vil verifisere oversettelser via fellesskapet, så vær vennlig å kun bidra med oversettelser på språk du behersker.


Når du sender inn en pull request, vil en CLA-bot automatisk avgjøre om du må levere en CLA og dekorere PR-en på passende måte (for eksempel etikett, kommentar). Følg bare instruksjonene som gis av boten. Du trenger bare å gjøre dette én gang på tvers av alle repositorier som bruker vår CLA.

Dette prosjektet har tatt i bruk [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). For mer informasjon, les Code of Conduct FAQ eller kontakt [Email opencode](opencode@microsoft.com) med eventuelle tilleggsspørsmål eller kommentarer.

## La oss komme i gang

Nå som du har fullført de nødvendige trinnene for å fullføre dette kurset, la oss komme i gang med en [introduksjon til Generative AI og LLMer](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->