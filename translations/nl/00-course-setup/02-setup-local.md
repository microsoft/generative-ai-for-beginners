# Lokale Setup 🖥️

**Gebruik deze gids als je alles liever op je eigen laptop draait.**   
Je hebt twee opties: **(A) native Python + virtual-env** of **(B) VS Code Dev Container met Docker**.  
Kies wat jou het makkelijkst lijkt—beide leiden tot dezelfde lessen.

## 1.  Vereisten

| Tool               | Versie / Opmerkingen                                                               |
|--------------------|-----------------------------------------------------------------------------------|
| **Python**         | 3.10 + (download het van <https://python.org>)                                    |
| **Git**            | Laatste versie (komt met Xcode / Git voor Windows / Linux pakketbeheerder)         |
| **VS Code**        | Optioneel maar aanbevolen <https://code.visualstudio.com>                        |
| **Docker Desktop** | *Alleen* voor Optie B. Gratis installatie: <https://docs.docker.com/desktop/>    |

> 💡 **Tip** – Controleer de tools in een terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Optie A – Native Python (snelste)

### Stap 1  Clone deze repo

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Stap 2 Maak en activeer een virtual environment

```bash
python -m venv .venv          # maak er één
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Prompt zou nu met (.venv) moeten beginnen—dat betekent dat je in de omgeving zit.

### Stap 3 Installeer dependencies

```bash
pip install -r requirements.txt
```

Ga door naar Sectie 3 over [API sleutels](#3-voeg-je-api-sleutels-toe)

## 2. Optie B – VS Code Dev Container (Docker)

We hebben deze repository en cursus opgezet met een [ontwikkelcontainer](https://containers.dev?WT.mc_id=academic-105485-koreyst) die een universele runtime heeft die Python3, .NET, Node.js en Java ontwikkeling ondersteunt. De bijbehorende configuratie is gedefinieerd in het `devcontainer.json` bestand in de `.devcontainer/` map aan de root van deze repository.

>**Waarom kiezen hiervoor?**
>Identieke omgeving als Codespaces; geen afhankelijkheidsverschuivingen.

### Stap 0 Installeer de extra’s

Docker Desktop – controleer of ```docker --version``` werkt.
VS Code Remote – Containers extensie (ID: ms-vscode-remote.remote-containers).

### Stap 1 Open de repo in VS Code

Bestand ▸ Map openen… → generative-ai-for-beginners

VS Code detecteert .devcontainer/ en toont een prompt.

### Stap 2 Heropen in container

Klik op “Heropen in Container”. Docker bouwt de image (≈ 3 min de eerste keer).
Wanneer de terminal prompt verschijnt, zit je in de container.

## 2.  Optie C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) is een lichte installer voor het installeren van [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, en een paar pakketten.
Conda zelf is een pakketbeheerder, die het eenvoudig maakt om verschillende Python [**virtuele omgevingen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) en pakketten op te zetten en te wisselen. Het is ook handig voor het installeren van pakketten die niet via `pip` beschikbaar zijn.

### Stap 0  Installeer Miniconda

Volg de [MiniConda installatiewijzer](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) om het op te zetten.

```bash
conda --version
```

### Stap 1 Maak een virtuele omgeving

Maak een nieuw omgevingsbestand (*environment.yml*). Als je Codespaces gebruikt, maak dit dan aan in de `.devcontainer` map, dus `.devcontainer/environment.yml`.

### Stap 2  Vul je omgevingsbestand in

Voeg de volgende snippet toe aan je  `environment.yml`

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

Voer onderstaande commando’s uit in je command line/terminal

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer subpad is alleen van toepassing op Codespace-setup
conda activate ai4beg
```

Raadpleeg de [Conda omgevingen gids](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) als je problemen tegenkomt.

## 2  Optie D – Klassieke Jupyter / Jupyter Lab (in je browser)

> **Voor wie is dit?**  
> Iedereen die van de klassieke Jupyter interface houdt of notebooks wil draaien zonder VS Code.  

### Stap 1  Zorg dat Jupyter geïnstalleerd is

Om Jupyter lokaal te starten, ga je naar de terminal/command line, navigeer je naar de cursusmap en voer je uit:

```bash
jupyter notebook
```

of

```bash
jupyterhub
```

Dit start een Jupyter instantie en de URL om deze te benaderen wordt getoond in het command line venster.

Zodra je de URL opent, zie je de cursusindeling en kun je naar elk `*.ipynb` bestand navigeren. Bijvoorbeeld `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Voeg je API Sleutels toe

Het veilig bewaren van je API sleutels is belangrijk bij het bouwen van toepassingen. We raden aan om geen API sleutels direct in je code op te slaan. Committen naar een publieke repository kan veiligheidsproblemen en ongewilde kosten veroorzaken als het misbruikt wordt.
Hier is een stapsgewijze gids om een `.env` bestand voor Python te maken en je Microsoft Foundry Models gegevens toe te voegen:

> **Opmerking:** GitHub Models (en zijn `GITHUB_TOKEN` variabele) wordt uitgefaseerd eind juli 2026. Deze gids gebruikt [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) in plaats daarvan. Wil je volledig offline werken? Zie [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Navigeer naar je projectmap**: Open je terminal of command prompt en ga naar de root map van je project waar je het `.env` bestand wilt aanmaken.

   ```bash
   cd path/to/your/project
   ```

2. **Maak het `.env` bestand aan**: Gebruik je favoriete teksteditor om een nieuw bestand genaamd `.env` te maken. Vanuit de command line kan dat met `touch` (Unix-systemen) of `echo` (Windows):

   Unix-systemen:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Bewerk het `.env` bestand**: Open het `.env` bestand in een teksteditor (bijv. VS Code, Notepad++, of een andere editor). Voeg de volgende regels toe aan het bestand, vervang de placeholders met je eigen Microsoft Foundry project endpoint en API sleutel:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Sla het bestand op**: Sla de wijzigingen op en sluit de teksteditor.

5. **Installeer `python-dotenv`**: Als je dat nog niet gedaan hebt, moet je het `python-dotenv` pakket installeren om omgevingsvariabelen uit het `.env` bestand te laden in je Python applicatie. Installeer het via `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Laad omgevingsvariabelen in je Python script**: Gebruik in je Python script het `python-dotenv` pakket om de variabelen uit het `.env` bestand te laden:

   ```python
   from dotenv import load_dotenv
   import os

   # Laad omgevingsvariabelen uit het .env-bestand
   load_dotenv()

   # Toegang tot de Microsoft Foundry Models-variabelen
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Dat is alles! Je hebt succesvol een `.env` bestand aangemaakt, je Microsoft Foundry Models gegevens toegevoegd en deze geladen in je Python toepassing.

🔐 Commit nooit .env—het staat al in .gitignore.
Volledige provider instructies vind je in [`providers.md`](03-providers.md).

## 4. Wat nu?

| Ik wil…              | Ga naar…                                                               |
|---------------------|------------------------------------------------------------------------|
| Les 1 starten        | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Een LLM Provider instellen | [`providers.md`](03-providers.md)                                       |
| Andere leerlingen ontmoeten | [Word lid van onze Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Problemen oplossen

| Symptoom                                  | Oplossing                                                      |
|-------------------------------------------|----------------------------------------------------------------|
| `python niet gevonden`                     | Voeg Python toe aan PATH of heropen terminal na installatie    |
| `pip` kan geen wheels bouwen (Windows)    | `pip install --upgrade pip setuptools wheel` en probeer opnieuw.|
| `ModuleNotFoundError: dotenv`              | Voer `pip install -r requirements.txt` uit (omgeving was niet geïnstalleerd).|
| Docker build mislukt *Geen ruimte meer*   | Docker Desktop ▸ *Instellingen* ▸ *Resources* → schijfgrootte vergroten.|
| VS Code blijft vragen om opnieuw te openen| Mogelijk zijn beide opties actief; kies er één (venv **of** container)|
| OpenAI 401 / 429 fouten                    | Controleer waarde van `OPENAI_API_KEY` / aanvraag limieten.     |
| Fouten bij gebruik van Conda               | Installeer Microsoft AI libraries met `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->