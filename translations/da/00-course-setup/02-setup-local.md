# Lokal Opsætning 🖥️

**Brug denne vejledning, hvis du foretrækker at køre det hele på din egen bærbare computer.**   
Du har to muligheder: **(A) native Python + virtual-env** eller **(B) VS Code Dev Container med Docker**.  
Vælg den, der føles nemmest – begge fører til de samme lektioner.

## 1. Forudsætninger

| Værktøj            | Version / Noter                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (hent det fra <https://python.org>)                                         |
| **Git**            | Seneste (følger med Xcode / Git til Windows / Linux pakkeadministrator)            |
| **VS Code**        | Valgfrit men anbefalet <https://code.visualstudio.com>                             |
| **Docker Desktop** | *Kun* til Option B. Gratis installation: <https://docs.docker.com/desktop/>       |

> 💡 **Tip** – Verificer værktøjer i en terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. Option A – Native Python (hurtigst)

### Trin 1 Klon dette repo

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Trin 2 Opret & aktivér et virtuelt miljø

```bash
python -m venv .venv          # lav en
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Prompten skulle nu starte med (.venv) – det betyder, du er inde i miljøet.

### Trin 3 Installer afhængigheder

```bash
pip install -r requirements.txt
```

Gå videre til afsnit 3 om [API-nøgler](#3-tilføj-dine-api-nøgler)

## 2. Option B – VS Code Dev Container (Docker)

Vi opsætter dette repository og kursus med en [udviklingscontainer](https://containers.dev?WT.mc_id=academic-105485-koreyst), der har en Universal runtime, der understøtter Python3, .NET, Node.js og Java udvikling. Den relaterede konfiguration er defineret i `devcontainer.json` filen placeret i `.devcontainer/` mappen i roden af dette repository.

>**Hvorfor vælge denne?**
>Identisk miljø med Codespaces; ingen afhængighedsdrift.

### Trin 0 Installer det ekstra

Docker Desktop – bekræft at ```docker --version``` virker.
VS Code Remote – Containers udvidelsen (ID: ms-vscode-remote.remote-containers).

### Trin 1 Åbn repoet i VS Code

Fil ▸ Åbn Mappe… → generative-ai-for-beginners

VS Code registrerer .devcontainer/ og viser en prompt.

### Trin 2 Genåbn i container

Klik på “Genåbn i Container”. Docker bygger billedet (≈ 3 min første gang).
Når terminalprompten dukker op, er du inde i containeren.

## 2. Option C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) er en letvægtsinstaller til installation af [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python samt nogle pakker.
Conda selv er en pakkehåndtering, som gør det nemt at opsætte og skifte mellem forskellige Python [**virtuelle miljøer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) og pakker. Det er også nyttigt til installation af pakker, som ikke er tilgængelige via `pip`.

### Trin 0 Installer Miniconda

Følg [MiniConda installationsvejledningen](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) for at sætte den op.

```bash
conda --version
```

### Trin 1 Opret et virtuelt miljø

Opret en ny miljøfil (*environment.yml*). Hvis du følger med via Codespaces, opret da denne i `.devcontainer` mappen, altså `.devcontainer/environment.yml`.

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

### Trin 3 Opret dit Conda miljø

Kør kommandoerne nedenfor i din kommandolinje/terminal

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer-undermappe gælder kun for Codespace-opsætninger
conda activate ai4beg
```

Se [Conda miljøvejledning](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), hvis du støder på problemer.

## 2 Option D – Klassisk Jupyter / Jupyter Lab (i din browser)

> **Hvem er dette til?**  
> Alle der elsker det klassiske Jupyter-interface eller vil køre notebooks uden VS Code.  

### Trin 1 Sørg for at Jupyter er installeret

For at starte Jupyter lokalt, gå til terminalen/kommandolinjen, naviger til kursusmappen og kør:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Dette starter en Jupyter instans, og URL'en til adgang vises i kommandolinjevinduet.

Når du tilgår URL'en, skulle du kunne se kursusoversigten og navigere til enhver `*.ipynb` fil. For eksempel, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Tilføj dine API-nøgler

Det er vigtigt at holde dine API-nøgler sikre, når du bygger enhver form for applikation. Vi anbefaler ikke at gemme API-nøgler direkte i din kode. At tilføje disse detaljer i et offentligt repository kan føre til sikkerhedsproblemer og endda uønskede omkostninger, hvis de misbruges af en ondsindet aktør.
Her er en trin-for-trin guide til at oprette en `.env` fil til Python og tilføje dine Microsoft Foundry Models legitimationsoplysninger:

> **Bemærk:** GitHub Models (og dets `GITHUB_TOKEN` variabel) udfases ved udgangen af juli 2026. Denne guide bruger i stedet [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Foretrækker du at arbejde helt offline? Se [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Naviger til dit projektmappe**: Åbn din terminal eller kommandoprompt og naviger til projektets rodkatalog, hvor du vil oprette `.env` filen.

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

3. **Rediger `.env` filen**: Åbn `.env` filen i en teksteditor (fx VS Code, Notepad++ eller anden editor). Tilføj følgende linjer til filen, og erstat pladsholderne med dine faktiske Microsoft Foundry projekt endepunkt og API-nøgle:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Gem filen**: Gem ændringerne og luk teksteditoren.

5. **Installer `python-dotenv`**: Hvis du ikke allerede har det, skal du installere `python-dotenv` pakken for at kunne indlæse miljøvariabler fra `.env` filen i din Python-applikation. Du kan installere den med `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Indlæs miljøvariabler i dit Python-script**: Brug `python-dotenv` pakken i dit Python-script til at indlæse miljøvariablerne fra `.env` filen:

   ```python
   from dotenv import load_dotenv
   import os

   # Indlæs miljøvariabler fra .env-fil
   load_dotenv()

   # Adgang til Microsoft Foundry Models variabler
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Det var det! Du har nu oprettet en `.env` fil, tilføjet dine Microsoft Foundry Models legitimationsoplysninger og indlæst dem i din Python-applikation.

🔐 Skriv aldrig `.env` i git – det er allerede inkluderet i `.gitignore`.
De komplette udbyderinstruktioner findes i [`providers.md`](03-providers.md).

## 4. Hvad nu?

| Jeg vil…            | Gå til…                                                                 |
|---------------------|-----------------------------------------------------------------------|
| Starte Lektion 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)   |
| Sætte en LLM Udbyder op | [`providers.md`](03-providers.md)                                   |
| Møde andre kursister | [Deltag i vores Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Fejlfinding

| Symptom                                   | Løsning                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| `python ikke fundet`                       | Tilføj Python til PATH eller genåbn terminalen efter installation|
| `pip` kan ikke bygge hjul (Windows)       | `pip install --upgrade pip setuptools wheel` og prøv igen.      |
| `ModuleNotFoundError: dotenv`              | Kør `pip install -r requirements.txt` (env var ikke installeret).|
| Docker build fejler *Ingen plads tilbage* | Docker Desktop ▸ *Indstillinger* ▸ *Ressourcer* → øg diskkapacitet.|
| VS Code bliver ved med at bede om genåbning| Du har muligvis begge muligheder aktive; vælg en (venv **eller** container)|
| OpenAI 401 / 429 fejl                      | Tjek værdien af `OPENAI_API_KEY` / anmodningsgrænser.            |
| Fejl med Conda                             | Installer Microsoft AI biblioteker med `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->