<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T17:49:05+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "nl"
}
-->
# Lokale Setup 🖥️

**Gebruik deze handleiding als je alles liever op je eigen laptop draait.**  
Je hebt twee opties: **(A) native Python + virtual-env** of **(B) VS Code Dev Container met Docker**.  
Kies wat je het makkelijkst vindt—beide leiden naar dezelfde lessen.

## 1.  Vereisten

| Tool               | Versie / Opmerkingen                                                                  |
|--------------------|--------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (download via <https://python.org>)                                            |
| **Git**            | Laatste versie (zit bij Xcode / Git for Windows / Linux package manager)              |
| **VS Code**        | Optioneel maar aanbevolen <https://code.visualstudio.com>                             |
| **Docker Desktop** | *Alleen* voor Optie B. Gratis te installeren: <https://docs.docker.com/desktop/>      |

> 💡 **Tip** – Controleer tools in een terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Optie A – Native Python (snelste)

### Stap 1  Clone deze repo

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Stap 2 Maak & activeer een virtuele omgeving

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ De prompt zou nu moeten beginnen met (.venv)—dat betekent dat je in de omgeving zit.

### Stap 3 Installeer afhankelijkheden

```bash
pip install -r requirements.txt
```

Ga verder naar Sectie 3 over [API-sleutels](../../../00-course-setup)

## 2. Optie B – VS Code Dev Container (Docker)

We hebben deze repository en cursus opgezet met een [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) die een universele runtime heeft die Python3, .NET, Node.js en Java development ondersteunt. De bijbehorende configuratie staat in het `devcontainer.json` bestand in de `.devcontainer/` map in de root van deze repository.

>**Waarom hiervoor kiezen?**
>Identieke omgeving als Codespaces; geen afhankelijkheidsproblemen.

### Stap 0 Installeer de extra’s

Docker Desktop – controleer of ```docker --version``` werkt.
VS Code Remote – Containers extensie (ID: ms-vscode-remote.remote-containers).

### Stap 1 Open de repo in VS Code

Bestand ▸ Map openen…  → generative-ai-for-beginners

VS Code detecteert .devcontainer/ en geeft een melding.

### Stap 2 Heropen in container

Klik op “Reopen in Container”. Docker bouwt het image (≈ 3 min de eerste keer).
Als de terminal prompt verschijnt, zit je in de container.

## 2.  Optie C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) is een lichte installer voor het installeren van [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, en enkele pakketten.
Conda zelf is een pakketbeheerder, waarmee je makkelijk verschillende Python [**virtuele omgevingen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) en pakketten kunt instellen en wisselen. Het is ook handig voor het installeren van pakketten die niet via `pip` beschikbaar zijn.

### Stap 0  Installeer Miniconda

Volg de [MiniConda installatiegids](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) om het te installeren.

```bash
conda --version
```

### Stap 1 Maak een virtuele omgeving

Maak een nieuw omgevingsbestand aan (*environment.yml*). Als je Codespaces gebruikt, maak dit bestand dan aan in de `.devcontainer` map, dus `.devcontainer/environment.yml`.

### Stap 2  Vul je omgevingsbestand

Voeg het volgende fragment toe aan je `environment.yml`

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

### Stap 3 Maak je Conda-omgeving aan

Voer de onderstaande commando’s uit in je command line/terminal

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Raadpleeg de [Conda environments gids](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) als je problemen tegenkomt.

## 2  Optie D – Klassieke Jupyter / Jupyter Lab (in je browser)

> **Voor wie is dit?**  
> Iedereen die de klassieke Jupyter-interface fijn vindt of notitieboeken wil draaien zonder VS Code.  

### Stap 1  Zorg dat Jupyter geïnstalleerd is

Om Jupyter lokaal te starten, ga naar de terminal/command line, navigeer naar de cursusmap en voer uit:

```bash
jupyter notebook
```

of

```bash
jupyterhub
```

Hiermee start je een Jupyter-instantie en het URL-adres om toegang te krijgen wordt in het command line venster getoond.

Als je het URL-adres opent, zie je het cursusoverzicht en kun je naar elk `*.ipynb` bestand navigeren. Bijvoorbeeld, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Voeg je API-sleutels toe

Het is belangrijk om je API-sleutels veilig te bewaren bij het bouwen van applicaties. We raden aan om geen API-sleutels direct in je code op te slaan. Als je deze details in een openbare repository zet, kan dat leiden tot beveiligingsproblemen en zelfs ongewenste kosten als iemand er misbruik van maakt.
Hier is een stapsgewijze handleiding om een `.env` bestand aan te maken voor Python en de `GITHUB_TOKEN` toe te voegen:

1. **Navigeer naar je projectmap**: Open je terminal of opdrachtprompt en ga naar de hoofdmap van je project waar je het `.env` bestand wilt aanmaken.

   ```bash
   cd path/to/your/project
   ```

2. **Maak het `.env` bestand aan**: Gebruik je favoriete teksteditor om een nieuw bestand genaamd `.env` te maken. Als je de command line gebruikt, kun je `touch` (op Unix-systemen) of `echo` (op Windows) gebruiken:

   Unix-systemen:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Bewerk het `.env` bestand**: Open het `.env` bestand in een teksteditor (bijv. VS Code, Notepad++, of een andere editor). Voeg de volgende regel toe aan het bestand, waarbij je `your_github_token_here` vervangt door je eigen GitHub-token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Sla het bestand op**: Sla de wijzigingen op en sluit de teksteditor.

5. **Installeer `python-dotenv`**: Als je dit nog niet hebt gedaan, moet je het `python-dotenv` pakket installeren om omgevingsvariabelen uit het `.env` bestand in je Python-applicatie te laden. Je kunt het installeren met `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Laad omgevingsvariabelen in je Python-script**: Gebruik in je Python-script het `python-dotenv` pakket om de omgevingsvariabelen uit het `.env` bestand te laden:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Dat is alles! Je hebt nu succesvol een `.env` bestand aangemaakt, je GitHub-token toegevoegd en deze geladen in je Python-applicatie.

🔐 Commit nooit .env—het staat al in .gitignore.
Volledige instructies voor providers vind je in [`providers.md`](03-providers.md).

## 4. Wat nu?

| Ik wil…             | Ga naar…                                                                  |
|---------------------|---------------------------------------------------------------------------|
| Starten met Les 1   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)       |
| Een LLM-provider instellen | [`providers.md`](03-providers.md)                                  |
| Andere deelnemers ontmoeten | [Word lid van onze Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Problemen oplossen

| Symptoom                                   | Oplossing                                                        |
|--------------------------------------------|------------------------------------------------------------------|
| `python not found`                         | Voeg Python toe aan PATH of herstart de terminal na installatie  |
| `pip` kan geen wheels bouwen (Windows)     | `pip install --upgrade pip setuptools wheel` en probeer opnieuw. |
| `ModuleNotFoundError: dotenv`              | Voer `pip install -r requirements.txt` uit (env was niet geïnstalleerd). |
| Docker build faalt *No space left*         | Docker Desktop ▸ *Instellingen* ▸ *Resources* → vergroot schijfruimte. |
| VS Code blijft vragen om te heropenen      | Je hebt mogelijk beide opties actief; kies er één (venv **of** container)|
| OpenAI 401 / 429 fouten                    | Controleer de waarde van `OPENAI_API_KEY` / limieten voor verzoeken. |
| Fouten bij gebruik van Conda               | Installeer Microsoft AI libraries met `conda install -c microsoft azure-ai-ml`|

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritische informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.