# Lokal installation 🖥️

**Använd denna guide om du föredrar att köra allt på din egen laptop.**   
Du har två vägar: **(A) native Python + virtual-env** eller **(B) VS Code Dev Container med Docker**.  
Välj det som känns enklast – båda leder till samma lektioner.

## 1.  Förutsättningar

| Verktyg            | Version / Anteckningar                                                              |
|--------------------|------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (hämta från <https://python.org>)                                           |
| **Git**            | Senaste (medföljer Xcode / Git för Windows / Linux paketchef)                      |
| **VS Code**        | Valfritt men rekommenderas <https://code.visualstudio.com>                         |
| **Docker Desktop** | *Endast* för Alternativ B. Kostnadsfri installation: <https://docs.docker.com/desktop/>|

> 💡 **Tips** – Verifiera verktyg i terminalen:  
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

Hoppa till Sektion 3 om [API-nycklar](#3-lägg-till-dina-api-nycklar)

## 2. Alternativ B – VS Code Dev Container (Docker)

Vi har satt upp detta repository och kurs med en [utvecklingscontainer](https://containers.dev?WT.mc_id=academic-105485-koreyst) som har en Universal runtime som kan stödja Python3, .NET, Node.js och Java-utveckling. Den relaterade konfigurationen definieras i `devcontainer.json`-filen som ligger i `.devcontainer/`-mappen i repositoryts rot.

>**Varför välja detta?**
>Identisk miljö som Codespaces; ingen beroendedrift.

### Steg 0 Installera extratillägg

Docker Desktop – bekräfta att ```docker --version``` fungerar.
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers).

### Steg 1 Öppna repo i VS Code

Fil ▸ Öppna mapp…  → generative-ai-for-beginners

VS Code känner av .devcontainer/ och visar en prompt.

### Steg 2 Öppna i container igen

Klicka “Öppna i container”. Docker bygger imagen (≈ 3 min första gången).
När terminalprompten visas är du inne i containern.

## 2.  Alternativ C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) är en lättviktsinstallatör för att installera [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python samt några paket.
Conda är en pakethanterare som gör det enkelt att sätta upp och byta mellan olika Python [**virtuella miljöer**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) och paket. Den är också användbar för att installera paket som inte finns via `pip`.

### Steg 0  Installera Miniconda

Följ [MiniConda installationsguiden](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) för att sätta upp det.

```bash
conda --version
```

### Steg 1 Skapa en virtuell miljö

Skapa en ny miljøfil (*environment.yml*). Om du följer med Codespaces, skapa denna inom `.devcontainer`-mappen, alltså `.devcontainer/environment.yml`.

### Steg 2  Fyll i din miljöfil

Lägg till följande snippet i din `environment.yml`

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

Kör kommandona nedan i din terminal/kommandorad

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer undermapp gäller endast för Codespace-konfigurationer
conda activate ai4beg
```

Se [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) om du stöter på problem.

## 2  Alternativ D – Klassisk Jupyter / Jupyter Lab (i din webbläsare)

> **För vem?**  
> Alla som älskar den klassiska Jupyter-gränssnittet eller vill köra notebooks utan VS Code.  

### Steg 1  Säkerställ att Jupyter är installerat

För att starta Jupyter lokalt, gå till terminalen/kommandoraden, navigera till kurskatalogen och kör:

```bash
jupyter notebook
```

eller

```bash
jupyterhub
```

Detta startar en Jupyter-instans och URL:en för att nå den visas i kommandofönstret.

När du går till URL:en ska du se kursöversikten och kunna navigera till alla `*.ipynb` filer. Till exempel, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Lägg till dina API-nycklar

Att hålla dina API-nycklar säkra är viktigt när du bygger applikationer. Vi rekommenderar att inte lagra några API-nycklar direkt i koden. Att lägga dessa detaljer i ett publikt repository kan orsaka säkerhetsproblem och oönskade kostnader om de används av illvilliga.
Här är en steg-för-steg-guide för hur du skapar en `.env`-fil för Python och lägger till dina Microsoft Foundry Models-inloggningsuppgifter:

> **Notera:** GitHub Models (och dess `GITHUB_TOKEN` variabel) läggs ner i slutet av juli 2026. Denna guide använder istället [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Vill du arbeta helt offline? Se [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Navigera till ditt projektkatalog**: Öppna terminalen eller kommandoprompten och navigera till roten av ditt projekt där du vill skapa `.env`-filen.

   ```bash
   cd path/to/your/project
   ```

2. **Skapa `.env`-filen**: Använd din favorittextredigerare för att skapa en ny fil med namnet `.env`. Om du använder kommandoraden kan du använda `touch` (på Unix-system) eller `echo` (på Windows):

   Unix-system:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Redigera `.env`-filen**: Öppna `.env`-filen i en textredigerare (t.ex. VS Code, Notepad++ eller annan editor). Lägg till följande rader i filen och ersätt platshållarna med dina faktiska Microsoft Foundry projekt endpoint och API-nyckel:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Spara filen**: Spara ändringarna och stäng textredigeraren.

5. **Installera `python-dotenv`**: Om du inte redan gjort det behöver du installera `python-dotenv`-paketet för att läsa in miljövariabler från `.env`-filen i din Python-applikation. Du kan installera det med `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Läs in miljövariabler i ditt Python-skript**: I ditt Python-skript, använd `python-dotenv`-paketet för att läsa in miljövariabler från `.env`-filen:

   ```python
   from dotenv import load_dotenv
   import os

   # Läs in miljövariabler från .env-fil
   load_dotenv()

   # Åtkomst till Microsoft Foundry Models-variablerna
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Det var allt! Du har framgångsrikt skapat en `.env`-fil, lagt till dina Microsoft Foundry Models-uppgifter och läst in dem i din Python-applikation.

🔐 Lämna aldrig in .env—den är redan i .gitignore.
Fullständiga leverantörsinstruktioner finns i [`providers.md`](03-providers.md).

## 4. Vad är nästa steg?

| Jag vill…          | Gå till…                                                                 |
|---------------------|-------------------------------------------------------------------------|
| Starta Lektion 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| Sätta upp en LLM-leverantör | [`providers.md`](03-providers.md)                                  |
| Träffa andra deltagare | [Gå med i vår Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Felsökning

| Symptom                                | Lösning                                                        |
|----------------------------------------|----------------------------------------------------------------|
| `python not found`                     | Lägg till Python i PATH eller öppna terminalen på nytt efter installation |
| `pip` kan inte bygga wheels (Windows) | `pip install --upgrade pip setuptools wheel` och försök igen.   |
| `ModuleNotFoundError: dotenv`          | Kör `pip install -r requirements.txt` (miljön installerades inte). |
| Docker build misslyckas *No space left*| Docker Desktop ▸ *Inställningar* ▸ *Resurser* → öka diskutrymme.|
| VS Code uppmanar att öppna på nytt       | Du kan ha båda alternativen aktiva; välj ett (venv **eller** container)|
| OpenAI 401 / 429-fel                   | Kontrollera värdet på `OPENAI_API_KEY` / förfrågningsbegränsningar. |
| Fel vid användning av Conda            | Installera Microsoft AI-bibliotek med `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->