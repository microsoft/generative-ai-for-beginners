# Lokal oppsett 🖥️

**Bruk denne veiledningen hvis du foretrekker å kjøre alt på din egen laptop.**   
Du har to alternativer: **(A) native Python + virtual-env** eller **(B) VS Code Dev Container med Docker**.  
Velg det som føles enklest—begge fører til de samme leksjonene.

## 1.  Forutsetninger

| Verktøy            | Versjon / Notater                                                                   |
|--------------------|------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (last ned fra <https://python.org>)                                         |
| **Git**            | Nyeste (følger med Xcode / Git for Windows / Linux pakkehåndterer)                  |
| **VS Code**        | Valgfritt, men anbefalt <https://code.visualstudio.com>                            |
| **Docker Desktop** | *Kun* for alternativ B. Gratis installasjon: <https://docs.docker.com/desktop/>   |

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
python -m venv .venv          # lag en
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Ledeteksten skal nå starte med (.venv)—det betyr at du er inne i miljøet.

### Steg 3 Installer avhengigheter

```bash
pip install -r requirements.txt
```

Hopp til Seksjon 3 om [API-nøkler](#3-legg-til-dine-api-nøkler)

## 2. Alternativ B – VS Code Dev Container (Docker)

Vi har satt opp dette repository og kurset med en [utviklingscontainer](https://containers.dev?WT.mc_id=academic-105485-koreyst) som har et universelt runtime som støtter Python3, .NET, Node.js og Java-utvikling. Relatert konfigurasjon er definert i `devcontainer.json`-filen som ligger i `.devcontainer/`-mappen i roten av dette repoet.

>**Hvorfor velge dette?**
>Identisk miljø som Codespaces; ingen avhengighetsdrift.

### Steg 0 Installer ekstrautstyr

Docker Desktop – bekreft ```docker --version``` fungerer.
VS Code Remote – Containers utvidelse (ID: ms-vscode-remote.remote-containers).

### Steg 1 Åpne repoet i VS Code

Fil ▸ Åpne mappe…  → generative-ai-for-beginners

VS Code oppdager .devcontainer/ og viser en prompt.

### Steg 2 Åpne på nytt i container

Klikk “Åpne på nytt i container”. Docker bygger bildet (≈ 3 min første gang).
Når terminalprompten dukker opp, er du inne i containeren.

## 2.  Alternativ C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) er en lettvektsinstallasjon for å installere [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, samt noen få pakker.
Conda selv er en pakkebehandler som gjør det enkelt å sette opp og bytte mellom forskjellige Python [**virtuelle miljøer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) og pakker. Det er også nyttig for å installere pakker som ikke er tilgjengelige via `pip`.

### Steg 0  Installer Miniconda

Følg [MiniConda installasjonsveiledningen](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) for å sette den opp.

```bash
conda --version
```

### Steg 1 Lag et virtuelt miljø

Lag en ny miljøfil (*environment.yml*). Hvis du følger med i Codespaces, lag denne i `.devcontainer` katalogen, altså `.devcontainer/environment.yml`.

### Steg 2  Fyll miljøfilen din

Legg til følgende utdrag til `environment.yml`

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

Kjør kommandoene nedenfor i kommandolinjen/terminalen din

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer understi gjelder kun for Codespace-oppsett
conda activate ai4beg
```

Se [Conda miljøveiledning](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) hvis du får problemer.

## 2  Alternativ D – Klassisk Jupyter / Jupyter Lab (i nettleseren)

> **Hvem er dette for?**  
> Alle som elsker det klassiske Jupyter-grensesnittet eller vil kjøre notebooks uten VS Code.  

### Steg 1  Sørg for at Jupyter er installert

For å starte Jupyter lokalt, gå til terminalen/kommandolinjen, naviger til kursmappen, og kjør:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Dette vil starte en Jupyter-instans og URL-en for å få tilgang til den vises i kommandolinjevinduet.

Når du får tilgang til URL-en, bør du se kursoversikten og kunne navigere til hvilken som helst `*.ipynb` fil. For eksempel, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Legg til dine API-nøkler

Det er viktig å holde API-nøklene dine trygge og sikre når du bygger hvilken som helst type applikasjon. Vi anbefaler at du ikke lagrer API-nøkler direkte i koden din. Å pushe slike detaljer til et offentlig repository kan føre til sikkerhetsproblemer og til og med uønskede kostnader hvis de brukes av en ondsinnet aktør.
Her er en trinn-for-trinn guide for hvordan lage en `.env` fil for Python og legge til dine Microsoft Foundry Models-legitimasjoner:

> **Merk:** GitHub Models (og variabelen `GITHUB_TOKEN`) legges ned ved slutten av juli 2026. Denne guiden bruker [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) i stedet. Foretrekker du å jobbe fullstendig offline? Se [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Gå til prosjektmappen din:** Åpne terminalen eller ledeteksten og naviger til prosjektets rotmappe hvor du ønsker å lage `.env`-filen.

   ```bash
   cd path/to/your/project
   ```

2. **Lag `.env`-filen:** Bruk din foretrukne teksteditor for å lage en ny fil kalt `.env`. Bruker du kommandolinjen, kan du bruke `touch` (på Unix-baserte systemer) eller `echo` (på Windows):

   Unix-baserte systemer:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Rediger `.env`-filen:** Åpne `.env`-filen i en teksteditor (f.eks. VS Code, Notepad++, eller en annen editor). Legg til følgende linjer i filen, og erstatt plassholderne med dine faktiske Microsoft Foundry prosjektendepunkt og API-nøkkel:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Lagre filen:** Lagre endringene og lukk teksteditoren.

5. **Installer `python-dotenv`:** Hvis du ikke allerede har gjort det, må du installere pakken `python-dotenv` for å laste miljøvariablene fra `.env`-filen inn i Python-applikasjonen din. Du kan installere den med `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Last miljøvariabler i Python-skriptet ditt:** I Python-skriptet ditt bruker du `python-dotenv` pakken til å laste miljøvariablene fra `.env`-filen:

   ```python
   from dotenv import load_dotenv
   import os

   # Last miljøvariabler fra .env-fil
   load_dotenv()

   # Få tilgang til Microsoft Foundry Models variabler
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Det var det! Du har nå opprettet en `.env`-fil, lagt til dine Microsoft Foundry Models-legitimasjoner, og lastet dem inn i Python-applikasjonen din.

🔐 Ikke push .env—den er allerede i .gitignore.
Fullstendige leverandørinstruksjoner finnes i [`providers.md`](03-providers.md).

## 4. Hva nå?

| Jeg vil…             | Gå til…                                                                |
|---------------------|-------------------------------------------------------------------------|
| Starte Leksjon 1     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Sette opp en LLM-leverandør | [`providers.md`](03-providers.md)                                 |
| Møte andre deltakere | [Bli med i vår Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Feilsøking

| Symptom                                   | Løsning                                                        |
|-------------------------------------------|----------------------------------------------------------------|
| `python ikke funnet`                      | Legg til Python i PATH eller åpne terminalen på nytt etter installasjon |
| `pip` kan ikke bygge hjul (Windows)       | Kjør `pip install --upgrade pip setuptools wheel` og prøv igjen.           |
| `ModuleNotFoundError: dotenv`             | Kjør `pip install -r requirements.txt` (miljøet var ikke installert).       |
| Docker build feiler *No space left*        | Docker Desktop ▸ *Innstillinger* ▸ *Ressurser* → øk diskstørrelse.          |
| VS Code spør stadig om å åpne på nytt     | Du kan ha begge alternativer aktive; velg én (venv **eller** container)     |
| OpenAI 401 / 429 feil                      | Sjekk `OPENAI_API_KEY`-verdi / forespørselsfrekvensgrenser.                 |
| Feil ved bruk av Conda                     | Installer Microsoft AI-biblioteker med `conda install -c microsoft azure-ai-ml` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->