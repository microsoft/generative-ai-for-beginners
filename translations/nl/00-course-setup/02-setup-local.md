<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f5cf0b10ab3c485e6334101f5784f1f3",
  "translation_date": "2025-12-19T15:49:42+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "nl"
}
-->
# Lokale Setup 🖥️

**Gebruik deze gids als je alles liever op je eigen laptop draait.**  
Je hebt twee opties: **(A) native Python + virtual-env** of **(B) VS Code Dev Container met Docker**.  
Kies wat voor jou het makkelijkst voelt—beide leiden naar dezelfde lessen.

## 1.  Vereisten

| Tool               | Versie / Opmerkingen                                                                |
|--------------------|-------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (haal het van <https://python.org>)                                          |
| **Git**            | Laatste versie (komt met Xcode / Git voor Windows / Linux pakketbeheerder)           |
| **VS Code**        | Optioneel maar aanbevolen <https://code.visualstudio.com>                           |
| **Docker Desktop** | *Alleen* voor Optie B. Gratis installatie: <https://docs.docker.com/desktop/>       |

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
python -m venv .venv          # maak er één
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Prompt zou nu moeten beginnen met (.venv)—dat betekent dat je binnen de omgeving zit.

### Stap 3 Installeer afhankelijkheden

```bash
pip install -r requirements.txt
```

Ga door naar Sectie 3 over [API-sleutels](../../../00-course-setup)

## 2. Optie B – VS Code Dev Container (Docker)

We hebben deze repository en cursus opgezet met een [ontwikkelcontainer](https://containers.dev?WT.mc_id=academic-105485-koreyst) die een universele runtime heeft die Python3, .NET, Node.js en Java ontwikkeling ondersteunt. De bijbehorende configuratie is gedefinieerd in het `devcontainer.json` bestand in de `.devcontainer/` map aan de root van deze repository.

>**Waarom kiezen hiervoor?**  
>Identieke omgeving als Codespaces; geen afhankelijkheidsverschuiving.

### Stap 0 Installeer de extra’s

Docker Desktop – controleer of ```docker --version``` werkt.  
VS Code Remote – Containers extensie (ID: ms-vscode-remote.remote-containers).

### Stap 1 Open de repo in VS Code

Bestand ▸ Map openen…  → generative-ai-for-beginners

VS Code detecteert .devcontainer/ en toont een prompt.

### Stap 2 Heropen in container

Klik op “Heropen in Container”. Docker bouwt de image (≈ 3 min eerste keer).  
Wanneer de terminal prompt verschijnt, zit je binnen de container.

## 2.  Optie C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) is een lichte installer voor het installeren van [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, en een paar pakketten.  
Conda zelf is een pakketbeheerder, die het makkelijk maakt om verschillende Python [**virtuele omgevingen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) en pakketten op te zetten en te wisselen. Het is ook handig voor het installeren van pakketten die niet via `pip` beschikbaar zijn.

### Stap 0  Installeer Miniconda

Volg de [MiniConda installatiehandleiding](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) om het op te zetten.

```bash
conda --version
```

### Stap 1 Maak een virtuele omgeving

Maak een nieuw omgeving bestand (*environment.yml*). Als je Codespaces gebruikt, maak dit dan aan binnen de `.devcontainer` map, dus `.devcontainer/environment.yml`.

### Stap 2  Vul je omgeving bestand

Voeg de volgende snippet toe aan je `environment.yml`

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

### Stap 3 Maak je Conda omgeving aan

Voer de onderstaande commando’s uit in je command line/terminal

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer subpad is alleen van toepassing op Codespace-setup's
conda activate ai4beg
```

Raadpleeg de [Conda omgevingen gids](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) als je problemen ondervindt.

## 2  Optie D – Klassieke Jupyter / Jupyter Lab (in je browser)

> **Voor wie is dit?**  
> Iedereen die van de klassieke Jupyter interface houdt of notebooks wil draaien zonder VS Code.  

### Stap 1  Zorg dat Jupyter geïnstalleerd is

Om Jupyter lokaal te starten, ga naar de terminal/command line, navigeer naar de cursusmap, en voer uit:

```bash
jupyter notebook
```

of

```bash
jupyterhub
```

Dit start een Jupyter instantie en de URL om deze te bereiken wordt getoond in het command line venster.

Als je de URL opent, zou je de cursusindeling moeten zien en naar elk `*.ipynb` bestand kunnen navigeren. Bijvoorbeeld, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Voeg je API-sleutels toe

Het is belangrijk om je API-sleutels veilig te houden bij het bouwen van welke applicatie dan ook. We raden aan om geen API-sleutels direct in je code op te slaan. Het committeren van deze gegevens naar een openbare repository kan leiden tot beveiligingsproblemen en zelfs ongewenste kosten als ze door kwaadwillenden worden gebruikt.  
Hier is een stapsgewijze handleiding om een `.env` bestand te maken voor Python en de `GITHUB_TOKEN` toe te voegen:

1. **Navigeer naar je projectmap**: Open je terminal of opdrachtprompt en ga naar de rootmap van je project waar je het `.env` bestand wilt aanmaken.

   ```bash
   cd path/to/your/project
   ```

2. **Maak het `.env` bestand aan**: Gebruik je favoriete teksteditor om een nieuw bestand met de naam `.env` te maken. Als je de command line gebruikt, kun je `touch` (op Unix-systemen) of `echo` (op Windows) gebruiken:

   Unix-systemen:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Bewerk het `.env` bestand**: Open het `.env` bestand in een teksteditor (bijv. VS Code, Notepad++, of een andere editor). Voeg de volgende regel toe, waarbij je `your_github_token_here` vervangt door je eigen GitHub token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Sla het bestand op**: Sla de wijzigingen op en sluit de teksteditor.

5. **Installeer `python-dotenv`**: Als je dit nog niet hebt gedaan, moet je het `python-dotenv` pakket installeren om omgevingsvariabelen uit het `.env` bestand in je Python applicatie te laden. Je kunt het installeren met `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Laad omgevingsvariabelen in je Python script**: Gebruik in je Python script het `python-dotenv` pakket om de omgevingsvariabelen uit het `.env` bestand te laden:

   ```python
   from dotenv import load_dotenv
   import os

   # Laad omgevingsvariabelen uit het .env-bestand
   load_dotenv()

   # Toegang tot de GITHUB_TOKEN variabele
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Dat is alles! Je hebt succesvol een `.env` bestand gemaakt, je GitHub token toegevoegd, en deze geladen in je Python applicatie.

🔐 Commit .env nooit—het staat al in .gitignore.  
Volledige provider instructies vind je in [`providers.md`](03-providers.md).

## 4. Wat nu?

| Ik wil…             | Ga naar…                                                                |
|---------------------|-------------------------------------------------------------------------|
| Start Les 1         | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Een LLM Provider instellen | [`providers.md`](03-providers.md)                                       |
| Andere leerlingen ontmoeten | [Word lid van onze Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Problemen oplossen

| Symbool                                   | Oplossing                                                        |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Voeg Python toe aan PATH of heropen terminal na installatie     |
| `pip` kan geen wheels bouwen (Windows)   | `pip install --upgrade pip setuptools wheel` en probeer opnieuw.|
| `ModuleNotFoundError: dotenv`             | Voer `pip install -r requirements.txt` uit (omgeving niet geïnstalleerd). |
| Docker build faalt *No space left*        | Docker Desktop ▸ *Instellingen* ▸ *Resources* → vergroot schijfruimte. |
| VS Code blijft vragen om te heropenen     | Mogelijk zijn beide opties actief; kies er één (venv **of** container)|
| OpenAI 401 / 429 fouten                   | Controleer `OPENAI_API_KEY` waarde / verzoeklimieten.           |
| Fouten met Conda                          | Installeer Microsoft AI libraries met `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->