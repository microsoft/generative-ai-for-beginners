<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T17:24:40+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "da"
}
-->
# Lokal opsætning 🖥️

**Brug denne guide, hvis du foretrækker at køre det hele på din egen laptop.**  
Du har to muligheder: **(A) native Python + virtual-env** eller **(B) VS Code Dev Container med Docker**.  
Vælg det, der føles nemmest—begge fører til de samme lektioner.

## 1.  Forudsætninger

| Værktøj             | Version / Noter                                                                      |
|---------------------|--------------------------------------------------------------------------------------|
| **Python**          | 3.10 + (hent fra <https://python.org>)                                               |
| **Git**             | Seneste (følger med Xcode / Git for Windows / Linux pakkehåndtering)                 |
| **VS Code**         | Valgfrit, men anbefalet <https://code.visualstudio.com>                              |
| **Docker Desktop**  | *Kun* til mulighed B. Gratis installation: <https://docs.docker.com/desktop/>        |

> 💡 **Tip** – Tjek værktøjer i terminalen:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Mulighed A – Native Python (hurtigst)

### Trin 1  Klon dette repo

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Trin 2 Opret & aktiver et virtuelt miljø

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Prompten bør nu starte med (.venv)—det betyder, du er inde i miljøet.

### Trin 3 Installer afhængigheder

```bash
pip install -r requirements.txt
```

Spring til afsnit 3 om [API-nøgler](../../../00-course-setup)

## 2. Mulighed B – VS Code Dev Container (Docker)

Vi har sat dette repository og kursus op med en [udviklingscontainer](https://containers.dev?WT.mc_id=academic-105485-koreyst), der har et universelt runtime, som kan understøtte Python3, .NET, Node.js og Java udvikling. Den tilhørende konfiguration er defineret i filen `devcontainer.json`, som ligger i mappen `.devcontainer/` i roden af dette repository.

>**Hvorfor vælge dette?**
>Identisk miljø som Codespaces; ingen afhængighedsproblemer.

### Trin 0 Installer ekstra værktøjer

Docker Desktop – tjek at ```docker --version``` virker.
VS Code Remote – Containers udvidelse (ID: ms-vscode-remote.remote-containers).

### Trin 1 Åbn repoet i VS Code

Fil ▸ Åbn mappe…  → generative-ai-for-beginners

VS Code opdager .devcontainer/ og viser en prompt.

### Trin 2 Genåbn i container

Klik på “Reopen in Container”. Docker bygger billedet (≈ 3 min første gang).
Når terminalprompten vises, er du inde i containeren.

## 2.  Mulighed C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) er en letvægtsinstaller til at installere [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python og nogle få pakker.
Conda er en pakkehåndtering, der gør det nemt at opsætte og skifte mellem forskellige Python [**virtuelle miljøer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) og pakker. Det er også nyttigt til at installere pakker, der ikke findes via `pip`.

### Trin 0  Installer Miniconda

Følg [MiniConda installationsguiden](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) for at sætte det op.

```bash
conda --version
```

### Trin 1 Opret et virtuelt miljø

Opret en ny miljøfil (*environment.yml*). Hvis du følger med via Codespaces, opret den i `.devcontainer` mappen, altså `.devcontainer/environment.yml`.

### Trin 2  Udfyld din miljøfil

Tilføj følgende til din `environment.yml`

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
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Se [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), hvis du får problemer.

## 2  Mulighed D – Klassisk Jupyter / Jupyter Lab (i din browser)

> **Hvem er dette til?**  
> Alle, der elsker det klassiske Jupyter-interface eller vil køre notebooks uden VS Code.  

### Trin 1  Sørg for at Jupyter er installeret

For at starte Jupyter lokalt, gå til terminalen/kommandolinjen, naviger til kursusmappen, og kør:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Dette starter en Jupyter-instans, og URL’en for adgang vises i kommandolinjevinduet.

Når du åbner URL’en, bør du se kursusoversigten og kunne navigere til enhver `*.ipynb` fil. For eksempel, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Tilføj dine API-nøgler

Det er vigtigt at holde dine API-nøgler sikre, når du bygger applikationer. Vi anbefaler ikke at gemme API-nøgler direkte i din kode. Hvis du kommer til at committe dem til et offentligt repository, kan det føre til sikkerhedsproblemer og uønskede omkostninger, hvis de misbruges.
Her er en trin-for-trin guide til at oprette en `.env` fil til Python og tilføje `GITHUB_TOKEN`:

1. **Naviger til din projektmappe**: Åbn din terminal eller kommandoprompt og gå til roden af dit projekt, hvor du vil oprette `.env` filen.

   ```bash
   cd path/to/your/project
   ```

2. **Opret `.env` filen**: Brug din foretrukne teksteditor til at oprette en ny fil med navnet `.env`. Hvis du bruger kommandolinjen, kan du bruge `touch` (på Unix-baserede systemer) eller `echo` (på Windows):

   Unix-baserede systemer:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Rediger `.env` filen**: Åbn `.env` filen i en teksteditor (fx VS Code, Notepad++ eller en anden editor). Tilføj denne linje til filen, og erstat `your_github_token_here` med din faktiske GitHub-token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Gem filen**: Gem ændringerne og luk teksteditoren.

5. **Installer `python-dotenv`**: Hvis du ikke allerede har gjort det, skal du installere pakken `python-dotenv` for at indlæse miljøvariabler fra `.env` filen i din Python-applikation. Du kan installere den med `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Indlæs miljøvariabler i dit Python-script**: I dit Python-script, brug `python-dotenv` pakken til at indlæse miljøvariabler fra `.env` filen:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Sådan! Du har nu oprettet en `.env` fil, tilføjet din GitHub-token og indlæst den i din Python-applikation.

🔐 Commit aldrig .env—den er allerede med i .gitignore.
Fuld vejledning til udbydere findes i [`providers.md`](03-providers.md).

## 4. Hvad nu?

| Jeg vil…            | Gå til…                                                                  |
|---------------------|-------------------------------------------------------------------------|
| Starte Lektion 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Opsætte en LLM-udbyder | [`providers.md`](03-providers.md)                                       |
| Møde andre kursister | [Deltag i vores Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Fejlfinding

| Symptom                                   | Løsning                                                          |
|-------------------------------------------|------------------------------------------------------------------|
| `python not found`                        | Tilføj Python til PATH eller genstart terminalen efter installation|
| `pip` kan ikke bygge hjul (Windows)       | `pip install --upgrade pip setuptools wheel` og prøv igen.       |
| `ModuleNotFoundError: dotenv`             | Kør `pip install -r requirements.txt` (miljøet blev ikke installeret).|
| Docker build fejler *No space left*       | Docker Desktop ▸ *Indstillinger* ▸ *Ressourcer* → øg diskstørrelsen.|
| VS Code bliver ved med at spørge om genåbning | Du har måske begge muligheder aktive; vælg én (venv **eller** container)|
| OpenAI 401 / 429 fejl                     | Tjek værdien af `OPENAI_API_KEY` / anmodningsratebegrænsninger.  |
| Fejl ved brug af Conda                    | Installer Microsoft AI-biblioteker med `conda install -c microsoft azure-ai-ml`|

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritiske oplysninger anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå ved brug af denne oversættelse.