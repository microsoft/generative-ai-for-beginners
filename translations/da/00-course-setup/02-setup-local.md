# Lokal opsætning 🖥️

**Brug denne guide, hvis du foretrækker at køre alt på din egen bærbare computer.**  
Du har to muligheder: **(A) native Python + virtual-env** eller **(B) VS Code Dev Container med Docker**.  
Vælg det, der føles nemmest—begge fører til de samme lektioner.

## 1. Forudsætninger

| Værktøj            | Version / Noter                                                                     |
|--------------------|------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (hent det fra <https://python.org>)                                         |
| **Git**            | Seneste (medfølger Xcode / Git til Windows / Linux pakkehåndtering)                 |
| **VS Code**        | Valgfrit men anbefalet <https://code.visualstudio.com>                              |
| **Docker Desktop** | *Kun* til Option B. Gratis installation: <https://docs.docker.com/desktop/>         |

> 💡 **Tip** – Tjek værktøjer i en terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. Option A – Native Python (hurtigst)

### Trin 1 Klon dette repo

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Trin 2 Opret & aktiver et virtuelt miljø

```bash
python -m venv .venv          # lav en
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Prompten skulle nu starte med (.venv)—det betyder, at du er inde i miljøet.

### Trin 3 Installer afhængigheder

```bash
pip install -r requirements.txt
```

Spring videre til Sektion 3 om [API-nøgler](../../../00-course-setup)

## 2. Option B – VS Code Dev Container (Docker)

Vi har sat dette repository og kursus op med en [udviklingscontainer](https://containers.dev?WT.mc_id=academic-105485-koreyst), som har en Universal runtime, der kan understøtte Python3, .NET, Node.js og Java-udvikling. Den relaterede konfiguration er defineret i `devcontainer.json`-filen, som ligger i `.devcontainer/`-mappen i roden af dette repository.

>**Hvorfor vælge dette?**  
>Identisk miljø som Codespaces; ingen afhængighedsdrift.

### Trin 0 Installer ekstraudstyr

Docker Desktop – bekræft at ```docker --version``` virker.  
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers).

### Trin 1 Åbn repo i VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code registrerer .devcontainer/ og viser en prompt.

### Trin 2 Genåbn i container

Klik på “Reopen in Container”. Docker bygger billedet (≈ 3 min første gang).  
Når terminalprompten vises, er du inde i containeren.

## 2. Option C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) er en letvægtsinstaller til installation af [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python samt nogle få pakker.  
Conda er en pakkehåndtering, der gør det nemt at opsætte og skifte mellem forskellige Python [**virtuelle miljøer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) og pakker. Det er også nyttigt til at installere pakker, som ikke er tilgængelige via `pip`.

### Trin 0 Installer Miniconda

Følg [MiniConda installationsguiden](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) for at sætte det op.

```bash
conda --version
```

### Trin 1 Opret et virtuelt miljø

Opret en ny miljøfil (*environment.yml*). Hvis du følger med i Codespaces, opret denne i `.devcontainer`-mappen, altså `.devcontainer/environment.yml`.

### Trin 2 Udfyld din miljøfil

Tilføj følgende uddrag til din `environment.yml`

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

### Trin 3 Opret dit Conda-miljø

Kør kommandoerne nedenfor i din kommandolinje/terminal

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer understi gælder kun for Codespace-opsætninger
conda activate ai4beg
```

Se [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), hvis du støder på problemer.

## 2 Option D – Klassisk Jupyter / Jupyter Lab (i din browser)

> **Hvem er dette til?**  
> Alle, der elsker det klassiske Jupyter-interface eller ønsker at køre notebooks uden VS Code.

### Trin 1 Sørg for, at Jupyter er installeret

For at starte Jupyter lokalt, gå til terminalen/kommandolinjen, naviger til kursusmappen, og kør:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Dette starter en Jupyter-instans, og URL’en til at tilgå den vises i kommandolinjevinduet.

Når du tilgår URL’en, skulle du kunne se kursusoversigten og navigere til enhver `*.ipynb`-fil. For eksempel `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Tilføj dine API-nøgler

Det er vigtigt at holde dine API-nøgler sikre, når du bygger enhver form for applikation. Vi anbefaler ikke at gemme API-nøgler direkte i din kode. At committe disse oplysninger til et offentligt repository kan føre til sikkerhedsproblemer og endda uønskede omkostninger, hvis de bruges af en ondsindet aktør.  
Her er en trin-for-trin guide til, hvordan du opretter en `.env`-fil til Python og tilføjer `GITHUB_TOKEN`:

1. **Naviger til din projektmappe**: Åbn din terminal eller kommandoprompt og gå til roden af dit projekt, hvor du vil oprette `.env`-filen.

   ```bash
   cd path/to/your/project
   ```

2. **Opret `.env`-filen**: Brug din foretrukne teksteditor til at oprette en ny fil med navnet `.env`. Hvis du bruger kommandolinjen, kan du bruge `touch` (på Unix-baserede systemer) eller `echo` (på Windows):

   Unix-baserede systemer:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Rediger `.env`-filen**: Åbn `.env`-filen i en teksteditor (f.eks. VS Code, Notepad++ eller en anden editor). Tilføj følgende linje til filen, og erstat `your_github_token_here` med din faktiske GitHub-token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Gem filen**: Gem ændringerne og luk teksteditoren.

5. **Installer `python-dotenv`**: Hvis du ikke allerede har gjort det, skal du installere pakken `python-dotenv` for at kunne indlæse miljøvariabler fra `.env`-filen i din Python-applikation. Du kan installere den med `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Indlæs miljøvariabler i dit Python-script**: Brug `python-dotenv`-pakken i dit Python-script til at indlæse miljøvariablerne fra `.env`-filen:

   ```python
   from dotenv import load_dotenv
   import os

   # Indlæs miljøvariabler fra .env fil
   load_dotenv()

   # Få adgang til GITHUB_TOKEN variablen
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Det var det! Du har nu oprettet en `.env`-fil, tilføjet din GitHub-token og indlæst den i din Python-applikation.

🔐 Commit aldrig .env—den er allerede i .gitignore.  
Fuldstændige instruktioner fra leverandørerne findes i [`providers.md`](03-providers.md).

## 4. Hvad nu?

| Jeg vil…            | Gå til…                                                                |
|---------------------|------------------------------------------------------------------------|
| Starte Lektion 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Opsætte en LLM-leverandør | [`providers.md`](03-providers.md)                                   |
| Møde andre elever   | [Deltag i vores Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Fejlfinding

| Symptom                                   | Løsning                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Tilføj Python til PATH eller genåbn terminal efter installation |
| `pip` kan ikke bygge wheels (Windows)    | `pip install --upgrade pip setuptools wheel` og prøv igen.      |
| `ModuleNotFoundError: dotenv`             | Kør `pip install -r requirements.txt` (miljøet var ikke installeret). |
| Docker build fejler *No space left*       | Docker Desktop ▸ *Settings* ▸ *Resources* → øg diskstørrelse.    |
| VS Code bliver ved med at spørge om genåbning | Du har muligvis begge muligheder aktive; vælg én (venv **eller** container) |
| OpenAI 401 / 429 fejl                     | Tjek `OPENAI_API_KEY` værdi / anmodningsgrænser.                |
| Fejl ved brug af Conda                    | Installer Microsoft AI-biblioteker med `conda install -c microsoft azure-ai-ml` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->