<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T17:15:43+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "sv"
}
-->
# Lokal installation 🖥️

**Använd den här guiden om du föredrar att köra allt på din egen dator.**  
Du har två vägar: **(A) native Python + virtual-env** eller **(B) VS Code Dev Container med Docker**.  
Välj det som känns enklast—båda leder till samma lektioner.

## 1. Förutsättningar

| Verktyg             | Version / Kommentarer                                                                |
|---------------------|--------------------------------------------------------------------------------------|
| **Python**          | 3.10 + (hämta från <https://python.org>)                                             |
| **Git**             | Senaste (följer med Xcode / Git for Windows / Linux-pakethanterare)                  |
| **VS Code**         | Valfritt men rekommenderas <https://code.visualstudio.com>                           |
| **Docker Desktop**  | *Endast* för alternativ B. Gratis installation: <https://docs.docker.com/desktop/>   |

> 💡 **Tips** – Kontrollera verktygen i terminalen:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. Alternativ A – Native Python (snabbast)

### Steg 1  Klona detta repo

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Steg 2 Skapa & aktivera en virtuell miljö

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Prompten ska nu börja med (.venv)—det betyder att du är inne i miljön.

### Steg 3 Installera beroenden

```bash
pip install -r requirements.txt
```

Hoppa till avsnitt 3 om [API-nycklar](../../../00-course-setup)

## 2. Alternativ B – VS Code Dev Container (Docker)

Vi har satt upp detta repo och kurs med en [utvecklingscontainer](https://containers.dev?WT.mc_id=academic-105485-koreyst) som har en universell runtime som stödjer Python3, .NET, Node.js och Java-utveckling. Den relaterade konfigurationen finns i filen `devcontainer.json` i mappen `.devcontainer/` i rooten av detta repo.

>**Varför välja detta?**
>Identisk miljö som Codespaces; inga beroendeproblem.

### Steg 0 Installera extratillägg

Docker Desktop – kontrollera att ```docker --version``` fungerar.
VS Code Remote – Containers-tillägg (ID: ms-vscode-remote.remote-containers).

### Steg 1 Öppna repot i VS Code

Arkiv ▸ Öppna mapp…  → generative-ai-for-beginners

VS Code hittar .devcontainer/ och visar en prompt.

### Steg 2 Öppna igen i container

Klicka på “Reopen in Container”. Docker bygger imagen (≈ 3 min första gången).
När terminalprompten visas är du inne i containern.

## 2. Alternativ C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) är en lättviktig installerare för att installera [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python och några paket.
Conda är en pakethanterare som gör det enkelt att sätta upp och byta mellan olika Python-[**virtuella miljöer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) och paket. Det är också användbart för att installera paket som inte finns via `pip`.

### Steg 0  Installera Miniconda

Följ [MiniConda installationsguiden](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) för att installera.

```bash
conda --version
```

### Steg 1 Skapa en virtuell miljö

Skapa en ny miljöfil (*environment.yml*). Om du följer med i Codespaces, skapa den i `.devcontainer`-mappen, alltså `.devcontainer/environment.yml`.

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

Kör kommandona nedan i din terminal

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Se [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) om du stöter på problem.

## 2  Alternativ D – Klassisk Jupyter / Jupyter Lab (i webbläsaren)

> **Vem är detta för?**  
> Alla som gillar det klassiska Jupyter-gränssnittet eller vill köra notebooks utan VS Code.  

### Steg 1  Kontrollera att Jupyter är installerat

För att starta Jupyter lokalt, gå till terminalen/kommandoraden, navigera till kursmappen och kör:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Detta startar en Jupyter-instans och URL:en för att komma åt den visas i terminalfönstret.

När du öppnar URL:en ska du se kursöversikten och kunna navigera till valfri `*.ipynb`-fil. Till exempel, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Lägg till dina API-nycklar

Att hålla dina API-nycklar säkra är viktigt när du bygger applikationer. Vi rekommenderar att du inte sparar API-nycklar direkt i koden. Om du råkar lägga till dem i ett publikt repo kan det leda till säkerhetsproblem och oväntade kostnader om någon missbrukar dem.
Här är en steg-för-steg-guide för att skapa en `.env`-fil för Python och lägga till `GITHUB_TOKEN`:

1. **Navigera till din projektmapp**: Öppna terminalen eller kommandoprompten och gå till projektets root-mapp där du vill skapa `.env`-filen.

   ```bash
   cd path/to/your/project
   ```

2. **Skapa `.env`-filen**: Använd din favorittextredigerare för att skapa en ny fil som heter `.env`. Om du använder kommandoraden kan du använda `touch` (på Unix-baserade system) eller `echo` (på Windows):

   Unix-baserade system:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Redigera `.env`-filen**: Öppna `.env`-filen i en textredigerare (t.ex. VS Code, Notepad++ eller någon annan editor). Lägg till följande rad i filen, och ersätt `your_github_token_here` med din faktiska GitHub-token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Spara filen**: Spara ändringarna och stäng editorn.

5. **Installera `python-dotenv`**: Om du inte redan gjort det, installera paketet `python-dotenv` för att ladda miljövariabler från `.env`-filen till din Python-app. Installera med `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Ladda miljövariabler i ditt Python-skript**: I ditt Python-skript, använd `python-dotenv` för att ladda miljövariablerna från `.env`-filen:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Klart! Du har nu skapat en `.env`-fil, lagt till din GitHub-token och laddat in den i din Python-app.

🔐 Committa aldrig .env—den finns redan i .gitignore.
Fullständiga instruktioner för leverantörer finns i [`providers.md`](03-providers.md).

## 4. Vad händer nu?

| Jag vill…           | Gå till…                                                                  |
|---------------------|---------------------------------------------------------------------------|
| Starta Lektion 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)       |
| Sätta upp en LLM-leverantör | [`providers.md`](03-providers.md)                                 |
| Träffa andra deltagare | [Gå med i vår Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Felsökning

| Symptom                                   | Lösning                                                          |
|-------------------------------------------|------------------------------------------------------------------|
| `python not found`                        | Lägg till Python i PATH eller starta om terminalen efter installation|
| `pip` kan inte bygga wheels (Windows)     | `pip install --upgrade pip setuptools wheel` och försök igen.    |
| `ModuleNotFoundError: dotenv`             | Kör `pip install -r requirements.txt` (miljön var inte installerad).|
| Docker build misslyckas *No space left*   | Docker Desktop ▸ *Inställningar* ▸ *Resurser* → öka diskutrymme. |
| VS Code frågar om att öppna igen          | Du kan ha båda alternativen aktiva; välj ett (venv **eller** container)|
| OpenAI 401 / 429-fel                      | Kontrollera värdet på `OPENAI_API_KEY` / gränser för förfrågningar.|
| Fel vid användning av Conda               | Installera Microsoft AI-bibliotek med `conda install -c microsoft azure-ai-ml`|

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.