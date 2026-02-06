# Lokal installation 🖥️

**Använd denna guide om du föredrar att köra allt på din egen laptop.**  
Du har två vägar: **(A) native Python + virtual-env** eller **(B) VS Code Dev Container med Docker**.  
Välj det som känns enklast – båda leder till samma lektioner.

## 1.  Förutsättningar

| Verktyg            | Version / Noteringar                                                                 |
|--------------------|-------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (hämta från <https://python.org>)                                            |
| **Git**            | Senaste (följer med Xcode / Git för Windows / Linux paketchef)                      |
| **VS Code**        | Valfritt men rekommenderas <https://code.visualstudio.com>                          |
| **Docker Desktop** | *Endast* för alternativ B. Gratis installation: <https://docs.docker.com/desktop/>  |

> 💡 **Tips** – Verifiera verktyg i terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Alternativ A – Native Python (snabbast)

### Steg 1  Klona detta repo

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Steg 2 Skapa & aktivera en virtuell miljö

```bash
python -m venv .venv          # skapa en
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Prompten bör nu börja med (.venv)—det betyder att du är inne i miljön.

### Steg 3 Installera beroenden

```bash
pip install -r requirements.txt
```

Hoppa till Sektion 3 om [API-nycklar](../../../00-course-setup)

## 2. Alternativ B – VS Code Dev Container (Docker)

Vi har satt upp detta repository och kurs med en [utvecklingscontainer](https://containers.dev?WT.mc_id=academic-105485-koreyst) som har en universell runtime som kan stödja Python3, .NET, Node.js och Java-utveckling. Den relaterade konfigurationen definieras i filen `devcontainer.json` som finns i mappen `.devcontainer/` i roten av detta repository.

>**Varför välja detta?**  
>Identisk miljö som Codespaces; ingen beroendedrift.

### Steg 0 Installera tillägg

Docker Desktop – bekräfta att ```docker --version``` fungerar.  
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers).

### Steg 1 Öppna repot i VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

VS Code känner av .devcontainer/ och visar en prompt.

### Steg 2 Öppna om i container

Klicka på “Reopen in Container”. Docker bygger bilden (≈ 3 min första gången).  
När terminalprompten visas är du inne i containern.

## 2.  Alternativ C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) är en lättviktsinstallerare för att installera [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python samt några paket.  
Conda är en pakethanterare som gör det enkelt att sätta upp och växla mellan olika Python [**virtuella miljöer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) och paket. Den är också användbar för att installera paket som inte finns via `pip`.

### Steg 0  Installera Miniconda

Följ [MiniConda installationsguide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) för att installera.

```bash
conda --version
```

### Steg 1 Skapa en virtuell miljö

Skapa en ny miljöfil (*environment.yml*). Om du följer med i Codespaces, skapa denna i `.devcontainer`-katalogen, alltså `.devcontainer/environment.yml`.

### Steg 2  Fyll i din miljöfil

Lägg till följande kodsnutt i din `environment.yml`

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

### Steg 3 Skapa din Conda-miljö

Kör kommandona nedan i din kommandorad/terminal

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer underkatalog gäller endast för Codespace-konfigurationer
conda activate ai4beg
```

Se [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) om du stöter på problem.

## 2  Alternativ D – Klassisk Jupyter / Jupyter Lab (i din webbläsare)

> **Vem är detta för?**  
> Alla som älskar det klassiska Jupyter-gränssnittet eller vill köra notebooks utan VS Code.

### Steg 1  Säkerställ att Jupyter är installerat

För att starta Jupyter lokalt, gå till terminalen/kommandoraden, navigera till kurskatalogen och kör:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Detta startar en Jupyter-instans och URL:en för att komma åt den visas i kommandoradsfönstret.

När du öppnar URL:en bör du se kursöversikten och kunna navigera till valfri `*.ipynb`-fil. Till exempel, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Lägg till dina API-nycklar

Att hålla dina API-nycklar säkra är viktigt när du bygger någon typ av applikation. Vi rekommenderar att du inte lagrar några API-nycklar direkt i din kod. Att committa dessa detaljer till ett offentligt repository kan leda till säkerhetsproblem och även oönskade kostnader om de används av illasinnade aktörer.  
Här är en steg-för-steg-guide för hur du skapar en `.env`-fil för Python och lägger till `GITHUB_TOKEN`:

1. **Navigera till din projektmapp**: Öppna terminalen eller kommandoprompten och gå till din projekts rotmapp där du vill skapa `.env`-filen.

   ```bash
   cd path/to/your/project
   ```

2. **Skapa `.env`-filen**: Använd din favorittextredigerare för att skapa en ny fil med namnet `.env`. Om du använder kommandoraden kan du använda `touch` (på Unix-baserade system) eller `echo` (på Windows):

   Unix-baserade system:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Redigera `.env`-filen**: Öppna `.env`-filen i en textredigerare (t.ex. VS Code, Notepad++ eller annan editor). Lägg till följande rad i filen och ersätt `your_github_token_here` med din faktiska GitHub-token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Spara filen**: Spara ändringarna och stäng textredigeraren.

5. **Installera `python-dotenv`**: Om du inte redan gjort det behöver du installera paketet `python-dotenv` för att kunna läsa in miljövariabler från `.env`-filen i din Python-applikation. Du kan installera det med `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Läs in miljövariabler i ditt Python-skript**: I ditt Python-skript, använd paketet `python-dotenv` för att läsa in miljövariablerna från `.env`-filen:

   ```python
   from dotenv import load_dotenv
   import os

   # Ladda miljövariabler från .env-fil
   load_dotenv()

   # Åtkomst till GITHUB_TOKEN-variabeln
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Klart! Du har nu skapat en `.env`-fil, lagt till din GitHub-token och läst in den i din Python-applikation.

🔐 Lämna aldrig in .env i git – den finns redan i .gitignore.  
Fullständiga instruktioner från leverantörerna finns i [`providers.md`](03-providers.md).

## 4. Vad händer härnäst?

| Jag vill…           | Gå till…                                                               |
|---------------------|------------------------------------------------------------------------|
| Starta Lektion 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)    |
| Sätta upp en LLM-leverantör | [`providers.md`](03-providers.md)                                  |
| Träffa andra deltagare | [Gå med i vår Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Felsökning

| Symptom                                   | Lösning                                                          |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Lägg till Python i PATH eller öppna terminalen på nytt efter installation |
| `pip` kan inte bygga wheels (Windows)     | `pip install --upgrade pip setuptools wheel` och försök igen.   |
| `ModuleNotFoundError: dotenv`             | Kör `pip install -r requirements.txt` (miljön installerades inte).|
| Docker build misslyckas *No space left*   | Docker Desktop ▸ *Settings* ▸ *Resources* → öka diskstorlek.     |
| VS Code fortsätter fråga om att öppna om  | Du kan ha båda alternativen aktiva; välj ett (venv **eller** container) |
| OpenAI 401 / 429 fel                      | Kontrollera värdet på `OPENAI_API_KEY` / begäranstak.            |
| Fel vid användning av Conda               | Installera Microsoft AI-bibliotek med `conda install -c microsoft azure-ai-ml` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->