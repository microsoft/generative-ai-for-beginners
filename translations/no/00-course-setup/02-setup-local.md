# Lokal oppsett 🖥️

**Bruk denne guiden hvis du foretrekker å kjøre alt på din egen laptop.**  
Du har to veier: **(A) native Python + virtual-env** eller **(B) VS Code Dev Container med Docker**.  
Velg det som føles enklest—begge fører til de samme leksjonene.

## 1.  Forutsetninger

| Verktøy            | Versjon / Notater                                                                    |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (last det ned fra <https://python.org>)                                       |
| **Git**            | Nyeste (følger med Xcode / Git for Windows / Linux pakkehåndterer)                   |
| **VS Code**        | Valgfritt, men anbefalt <https://code.visualstudio.com>                              |
| **Docker Desktop** | *Kun* for Alternativ B. Gratis installasjon: <https://docs.docker.com/desktop/>      |

> 💡 **Tips** – Verifiser verktøy i terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Alternativ A – Native Python (raskest)

### Steg 1  Klon dette repoet

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Steg 2 Lag og aktiver et virtuelt miljø

```bash
python -m venv .venv          # lag en
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Ledeteksten skal nå starte med (.venv)—det betyr at du er inne i miljøet.

### Steg 3 Installer avhengigheter

```bash
pip install -r requirements.txt
```

Hopp til Seksjon 3 om [API-nøkler](../../../00-course-setup)

## 2. Alternativ B – VS Code Dev Container (Docker)

Vi har satt opp dette repositoriet og kurset med en [utviklingscontainer](https://containers.dev?WT.mc_id=academic-105485-koreyst) som har en universell runtime som kan støtte Python3, .NET, Node.js og Java-utvikling. Den relaterte konfigurasjonen er definert i `devcontainer.json`-filen som ligger i `.devcontainer/`-mappen i roten av dette repositoriet.

>**Hvorfor velge dette?**  
>Identisk miljø som Codespaces; ingen avhengighetsdrift.

### Steg 0 Installer tilleggene

Docker Desktop – bekreft at ```docker --version``` fungerer.  
VS Code Remote – Containers-utvidelsen (ID: ms-vscode-remote.remote-containers).

### Steg 1 Åpne repoet i VS Code

Fil ▸ Åpne mappe…  → generative-ai-for-beginners

VS Code oppdager .devcontainer/ og viser en prompt.

### Steg 2 Åpne på nytt i container

Klikk “Reopen in Container”. Docker bygger bildet (≈ 3 min første gang).  
Når terminalprompten vises, er du inne i containeren.

## 2.  Alternativ C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) er en lettvektsinstaller for å installere [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, samt noen få pakker.  
Conda er en pakkebehandler som gjør det enkelt å sette opp og bytte mellom forskjellige Python [**virtuelle miljøer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) og pakker. Den er også nyttig for å installere pakker som ikke er tilgjengelige via `pip`.

### Steg 0  Installer Miniconda

Følg [MiniConda installasjonsguide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) for å sette det opp.

```bash
conda --version
```

### Steg 1 Lag et virtuelt miljø

Lag en ny miljøfil (*environment.yml*). Hvis du følger med i Codespaces, lag denne i `.devcontainer`-mappen, altså `.devcontainer/environment.yml`.

### Steg 2  Fyll miljøfilen din

Legg til følgende utdrag i din `environment.yml`

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

### Steg 3 Lag ditt Conda-miljø

Kjør kommandoene nedenfor i kommandolinjen/terminalen

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer undermappe gjelder kun for Codespace-oppsett
conda activate ai4beg
```

Se [Conda miljøguide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) hvis du støter på problemer.

## 2  Alternativ D – Klassisk Jupyter / Jupyter Lab (i nettleseren din)

> **Hvem er dette for?**  
> Alle som elsker det klassiske Jupyter-grensesnittet eller ønsker å kjøre notebooks uten VS Code.  

### Steg 1  Sørg for at Jupyter er installert

For å starte Jupyter lokalt, gå til terminalen/kommandolinjen, naviger til kursmappen, og kjør:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Dette starter en Jupyter-instans og URL-en for å få tilgang til den vises i kommandolinjevinduet.

Når du åpner URL-en, skal du se kursoversikten og kunne navigere til hvilken som helst `*.ipynb`-fil. For eksempel, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Legg til dine API-nøkler

Det er viktig å holde API-nøklene dine trygge og sikre når du bygger applikasjoner. Vi anbefaler å ikke lagre API-nøkler direkte i koden din. Å legge disse detaljene i et offentlig repo kan føre til sikkerhetsproblemer og uønskede kostnader hvis de brukes av uvedkommende.  
Her er en steg-for-steg guide for hvordan du lager en `.env`-fil for Python og legger til `GITHUB_TOKEN`:

1. **Naviger til prosjektmappen din**: Åpne terminalen eller kommandoprompten og gå til rotmappen for prosjektet der du vil lage `.env`-filen.

   ```bash
   cd path/to/your/project
   ```

2. **Lag `.env`-filen**: Bruk din foretrukne teksteditor for å lage en ny fil kalt `.env`. Hvis du bruker kommandolinjen, kan du bruke `touch` (på Unix-baserte systemer) eller `echo` (på Windows):

   Unix-baserte systemer:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Rediger `.env`-filen**: Åpne `.env`-filen i en teksteditor (f.eks. VS Code, Notepad++, eller annen editor). Legg til følgende linje i filen, og erstatt `your_github_token_here` med din faktiske GitHub-token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Lagre filen**: Lagre endringene og lukk teksteditoren.

5. **Installer `python-dotenv`**: Hvis du ikke allerede har gjort det, må du installere `python-dotenv`-pakken for å laste miljøvariabler fra `.env`-filen inn i Python-applikasjonen din. Du kan installere den med `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Last miljøvariabler i Python-skriptet ditt**: I Python-skriptet ditt, bruk `python-dotenv`-pakken for å laste miljøvariablene fra `.env`-filen:

   ```python
   from dotenv import load_dotenv
   import os

   # Last miljøvariabler fra .env-fil
   load_dotenv()

   # Få tilgang til GITHUB_TOKEN-variabelen
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Det var det! Du har nå laget en `.env`-fil, lagt til GitHub-tokenen din, og lastet den inn i Python-applikasjonen din.

🔐 Ikke legg .env i versjonskontroll—den er allerede i .gitignore.  
Fullstendige leverandørinstruksjoner finnes i [`providers.md`](03-providers.md).

## 4. Hva nå?

| Jeg vil…            | Gå til…                                                                |
|---------------------|------------------------------------------------------------------------|
| Starte Leksjon 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Sette opp en LLM-leverandør | [`providers.md`](03-providers.md)                                   |
| Møte andre elever   | [Bli med i vår Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Feilsøking

| Symptom                                   | Løsning                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Legg til Python i PATH eller åpne terminalen på nytt etter installasjon |
| `pip` kan ikke bygge wheels (Windows)    | `pip install --upgrade pip setuptools wheel` og prøv igjen.     |
| `ModuleNotFoundError: dotenv`             | Kjør `pip install -r requirements.txt` (miljøet var ikke installert). |
| Docker build feiler *No space left*       | Docker Desktop ▸ *Settings* ▸ *Resources* → øk diskstørrelse.    |
| VS Code spør stadig om å åpne på nytt     | Du kan ha begge alternativer aktive; velg ett (venv **eller** container) |
| OpenAI 401 / 429 feil                      | Sjekk `OPENAI_API_KEY`-verdien / forespørselsratebegrensninger.  |
| Feil ved bruk av Conda                     | Installer Microsoft AI-biblioteker med `conda install -c microsoft azure-ai-ml` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->