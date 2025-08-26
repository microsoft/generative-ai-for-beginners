<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T17:33:07+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "no"
}
-->
# Lokal oppsett 🖥️

**Bruk denne guiden hvis du vil kjøre alt på din egen laptop.**  
Du har to valg: **(A) native Python + virtual-env** eller **(B) VS Code Dev Container med Docker**.  
Velg det som føles enklest—begge gir deg samme kurs.

## 1.  Forutsetninger

| Verktøy             | Versjon / Notater                                                                |
|---------------------|----------------------------------------------------------------------------------|
| **Python**          | 3.10 + (last ned fra <https://python.org>)                                       |
| **Git**             | Siste versjon (følger med Xcode / Git for Windows / Linux pakke-manager)         |
| **VS Code**         | Valgfritt, men anbefalt <https://code.visualstudio.com>                          |
| **Docker Desktop**  | *Kun* for alternativ B. Gratis installasjon: <https://docs.docker.com/desktop/>  |

> 💡 **Tips** – Sjekk verktøyene i terminalen:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Alternativ A – Native Python (raskest)

### Steg 1  Klon dette repoet

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Steg 2 Opprett & aktiver et virtuelt miljø

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Prompten skal nå starte med (.venv)—da er du inne i miljøet.

### Steg 3 Installer avhengigheter

```bash
pip install -r requirements.txt
```

Hopp til seksjon 3 om [API-nøkler](../../../00-course-setup)

## 2. Alternativ B – VS Code Dev Container (Docker)

Vi har satt opp dette repoet og kurset med en [utviklingscontainer](https://containers.dev?WT.mc_id=academic-105485-koreyst) som har et universelt runtime-miljø for Python3, .NET, Node.js og Java. Konfigurasjonen ligger i `devcontainer.json`-filen i `.devcontainer/`-mappen i rotkatalogen.

>**Hvorfor velge dette?**
>Identisk miljø som Codespaces; ingen avhengighetsproblemer.

### Steg 0 Installer tilleggene

Docker Desktop – sjekk at ```docker --version``` fungerer.
VS Code Remote – Containers-utvidelsen (ID: ms-vscode-remote.remote-containers).

### Steg 1 Åpne repoet i VS Code

Fil ▸ Åpne mappe…  → generative-ai-for-beginners

VS Code oppdager .devcontainer/ og viser et varsel.

### Steg 2 Åpne på nytt i container

Klikk “Reopen in Container”. Docker bygger bildet (≈ 3 min første gang).
Når terminalen vises, er du inne i containeren.

## 2.  Alternativ C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) er en lettvektsinstaller for [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python og noen få pakker.
Conda er en pakke-manager som gjør det enkelt å sette opp og bytte mellom ulike Python [**virtuelle miljøer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) og pakker. Den er også nyttig for å installere pakker som ikke finnes via `pip`.

### Steg 0  Installer Miniconda

Følg [MiniConda installasjonsguiden](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) for å sette det opp.

```bash
conda --version
```

### Steg 1 Opprett et virtuelt miljø

Lag en ny miljøfil (*environment.yml*). Hvis du følger med i Codespaces, lag denne i `.devcontainer`-mappen, altså `.devcontainer/environment.yml`.

### Steg 2  Fyll ut miljøfilen

Legg inn følgende i `environment.yml`

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

### Steg 3 Opprett Conda-miljøet ditt

Kjør kommandoene under i terminalen/kommandolinjen

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Se [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) hvis du får problemer.

## 2  Alternativ D – Klassisk Jupyter / Jupyter Lab (i nettleseren)

> **Hvem passer dette for?**  
> Alle som liker klassisk Jupyter-grensesnitt eller vil kjøre notatbøker uten VS Code.  

### Steg 1  Sjekk at Jupyter er installert

For å starte Jupyter lokalt, åpne terminalen/kommandolinjen, gå til kursmappen og kjør:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Dette starter en Jupyter-instans og URL-en for tilgang vises i kommandolinjevinduet.

Når du åpner URL-en, ser du kursoversikten og kan navigere til hvilken som helst `*.ipynb`-fil. For eksempel, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Legg til API-nøklene dine

Det er viktig å holde API-nøklene dine trygge når du lager applikasjoner. Vi anbefaler å ikke lagre API-nøkler direkte i koden. Hvis du legger dem i et offentlig repo, kan det føre til sikkerhetsproblemer og uønskede kostnader hvis noen misbruker dem.
Her er en steg-for-steg-guide for å lage en `.env`-fil for Python og legge til `GITHUB_TOKEN`:

1. **Gå til prosjektmappen din**: Åpne terminalen eller kommandoprompten og gå til rotmappen der du vil lage `.env`-filen.

   ```bash
   cd path/to/your/project
   ```

2. **Lag `.env`-filen**: Bruk din favoritt teksteditor for å lage en ny fil som heter `.env`. Hvis du bruker kommandolinjen, kan du bruke `touch` (Unix-baserte systemer) eller `echo` (Windows):

   Unix-baserte systemer:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Rediger `.env`-filen**: Åpne `.env`-filen i en teksteditor (f.eks. VS Code, Notepad++ eller en annen editor). Legg til denne linjen, og bytt ut `your_github_token_here` med din faktiske GitHub-token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Lagre filen**: Lagre endringene og lukk editoren.

5. **Installer `python-dotenv`**: Hvis du ikke har gjort det, må du installere `python-dotenv`-pakken for å laste inn miljøvariabler fra `.env`-filen i Python-applikasjonen din. Installer med `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Last inn miljøvariabler i Python-scriptet ditt**: I Python-scriptet ditt, bruk `python-dotenv`-pakken for å laste inn miljøvariabler fra `.env`-filen:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Ferdig! Du har nå laget en `.env`-fil, lagt til GitHub-tokenet ditt og lastet det inn i Python-applikasjonen.

🔐 Ikke legg .env til commit—den er allerede i .gitignore.
Fullstendige instruksjoner for leverandører finner du i [`providers.md`](03-providers.md).

## 4. Hva skjer nå?

| Jeg vil…            | Gå til…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| Starte leksjon 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Sette opp LLM-leverandør | [`providers.md`](03-providers.md)                                   |
| Møte andre deltakere | [Bli med på Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Feilsøking

| Symptom                                   | Løsning                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Legg Python til PATH eller åpne terminalen på nytt etter installasjon |
| `pip` kan ikke bygge hjul (Windows)       | `pip install --upgrade pip setuptools wheel` og prøv igjen.     |
| `ModuleNotFoundError: dotenv`             | Kjør `pip install -r requirements.txt` (miljøet ble ikke installert). |
| Docker build feiler *No space left*       | Docker Desktop ▸ *Settings* ▸ *Resources* → øk diskstørrelsen.  |
| VS Code spør stadig om å åpne på nytt     | Du har kanskje begge alternativer aktive; velg ett (venv **eller** container)|
| OpenAI 401 / 429-feil                     | Sjekk verdien til `OPENAI_API_KEY` / forespørselsgrenser.       |
| Feil med Conda                            | Installer Microsoft AI-biblioteker med `conda install -c microsoft azure-ai-ml`|

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.