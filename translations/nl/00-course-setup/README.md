<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-17T19:53:16+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "nl"
}
-->
# Aan de slag met deze cursus

We zijn erg enthousiast dat je met deze cursus begint en we zijn benieuwd wat je geïnspireerd raakt om te bouwen met Generatieve AI!

Om je succes te garanderen, beschrijft deze pagina de stappen voor de setup, technische vereisten en waar je hulp kunt krijgen indien nodig.

## Setup Stappen

Om deze cursus te starten, moet je de volgende stappen voltooien.

### 1. Fork deze Repo

[Fork deze hele repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) naar je eigen GitHub-account om de code te kunnen wijzigen en de uitdagingen te voltooien. Je kunt ook [deze repo ster (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) om het en gerelateerde repos gemakkelijker terug te vinden.

### 2. Maak een codespace

Om afhankelijkheidsproblemen bij het uitvoeren van de code te vermijden, raden we aan deze cursus te volgen in een [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

In je fork: **Code -> Codespaces -> Nieuw op main**

![Dialoogvenster met knoppen om een codespace te maken](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Voeg een geheim toe

1. ⚙️ Tandwielicoon -> Command Pallete -> Codespaces: Beheer gebruikersgeheim -> Voeg een nieuw geheim toe.
2. Naam OPENAI_API_KEY, plak je sleutel, Opslaan.

### 3. Wat nu?

| Ik wil…             | Ga naar…                                                               |
|---------------------|------------------------------------------------------------------------|
| Start Les 1         | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)    |
| Offline werken      | [`setup-local.md`](02-setup-local.md)                                  |
| Een LLM-provider instellen | [`providers.md`](03-providers.md)                                     |
| Andere deelnemers ontmoeten | [Word lid van onze Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Problemen oplossen

| Symptoom                                  | Oplossing                                                       |
|-------------------------------------------|-----------------------------------------------------------------|
| Container build blijft hangen > 10 min    | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Terminal is niet gekoppeld; klik **+** ➜ *bash*                 |
| `401 Unauthorized` van OpenAI             | Verkeerde/verlopen `OPENAI_API_KEY`                             |
| VS Code toont “Dev container mounting…”   | Vernieuw het browsertabblad—Codespaces verliest soms verbinding |
| Notebook kernel ontbreekt                 | Notebook menu ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix-gebaseerde systemen:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Bewerk het `.env` bestand**: Open het `.env` bestand in een teksteditor (bijv. VS Code, Notepad++, of een andere editor). Voeg de volgende regel toe aan het bestand, waarbij je `your_github_token_here` vervangt door je daadwerkelijke GitHub-token:

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

Dat is alles! Je hebt succesvol een `.env` bestand aangemaakt, je GitHub-token toegevoegd en het geladen in je Python-applicatie.

## Hoe lokaal op je computer uitvoeren

Om de code lokaal op je computer uit te voeren, moet je een versie van [Python geïnstalleerd hebben](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Om vervolgens de repository te gebruiken, moet je deze clonen:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Zodra je alles hebt gedownload, kun je aan de slag!

## Optionele stappen

### Miniconda installeren

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) is een lichte installer voor het installeren van [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python en enkele pakketten.
Conda zelf is een pakketbeheerder die het eenvoudig maakt om verschillende Python [**virtuele omgevingen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) en pakketten in te stellen en te wisselen. Het is ook handig voor het installeren van pakketten die niet beschikbaar zijn via `pip`.

Je kunt de [MiniConda installatiegids](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) volgen om het in te stellen.

Met Miniconda geïnstalleerd, moet je de [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) clonen (als je dat nog niet hebt gedaan).

Vervolgens moet je een virtuele omgeving aanmaken. Om dit met Conda te doen, maak je een nieuw omgevingsbestand aan (_environment.yml_). Als je Codespaces gebruikt, maak je dit bestand aan binnen de `.devcontainer` directory, dus `.devcontainer/environment.yml`.

Vul je omgevingsbestand met de onderstaande snippet:

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

Als je fouten tegenkomt bij het gebruik van Conda, kun je handmatig de Microsoft AI Libraries installeren met het volgende commando in een terminal.

```
conda install -c microsoft azure-ai-ml
```

Het omgevingsbestand specificeert de benodigde afhankelijkheden. `<environment-name>` verwijst naar de naam die je wilt gebruiken voor je Conda-omgeving, en `<python-version>` is de versie van Python die je wilt gebruiken, bijvoorbeeld `3` is de nieuwste hoofdversie van Python.

Als dat gedaan is, kun je je Conda-omgeving aanmaken door de onderstaande commando's uit te voeren in je command line/terminal:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Raadpleeg de [Conda omgevingsgids](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) als je problemen tegenkomt.

### Visual Studio Code gebruiken met de Python-ondersteuning extensie

We raden aan om de [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editor te gebruiken met de [Python-ondersteuning extensie](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) geïnstalleerd voor deze cursus. Dit is echter meer een aanbeveling en geen vereiste.

> **Let op**: Door de cursusrepository te openen in VS Code, heb je de optie om het project binnen een container op te zetten. Dit komt door de [speciale `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) directory die in de cursusrepository te vinden is. Hierover later meer.

> **Let op**: Zodra je de directory clonet en opent in VS Code, zal het automatisch voorstellen om een Python-ondersteuning extensie te installeren.

> **Let op**: Als VS Code je vraagt om de repository opnieuw te openen in een container, weiger dit verzoek om de lokaal geïnstalleerde versie van Python te gebruiken.

### Jupyter in de browser gebruiken

Je kunt ook aan het project werken met behulp van de [Jupyter-omgeving](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direct in je browser. Zowel klassieke Jupyter als [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) bieden een prettige ontwikkelomgeving met functies zoals automatische aanvulling, code-highlighting, enz.

Om Jupyter lokaal te starten, ga naar de terminal/command line, navigeer naar de cursusdirectory en voer uit:

```bash
jupyter notebook
```

of

```bash
jupyterhub
```

Dit start een Jupyter-instantie en de URL om toegang te krijgen wordt weergegeven in het command line-venster.

Zodra je toegang hebt tot de URL, zou je de cursusindeling moeten zien en kun je navigeren naar elk `*.ipynb` bestand. Bijvoorbeeld, `08-building-search-applications/python/oai-solution.ipynb`.

### Uitvoeren in een container

Een alternatief voor het lokaal instellen van alles op je computer of Codespace is het gebruik van een [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). De speciale `.devcontainer` map binnen de cursusrepository maakt het mogelijk voor VS Code om het project binnen een container op te zetten. Buiten Codespaces vereist dit de installatie van Docker, en eerlijk gezegd, het kost wat werk, dus we raden dit alleen aan voor degenen met ervaring in het werken met containers.

Een van de beste manieren om je API-sleutels veilig te houden bij het gebruik van GitHub Codespaces is door Codespace Secrets te gebruiken. Volg de [Codespaces geheimenbeheer](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) gids om hier meer over te leren.

## Lessen en technische vereisten

De cursus bestaat uit 6 conceptlessen en 6 coderingslessen.

Voor de coderingslessen maken we gebruik van de Azure OpenAI Service. Je hebt toegang tot de Azure OpenAI-service en een API-sleutel nodig om deze code uit te voeren. Je kunt toegang aanvragen door [deze aanvraag in te vullen](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Terwijl je wacht op de verwerking van je aanvraag, bevat elke coderingsles ook een `README.md` bestand waarin je de code en uitvoer kunt bekijken.

## Voor het eerst de Azure OpenAI Service gebruiken

Als dit de eerste keer is dat je werkt met de Azure OpenAI-service, volg dan deze gids over hoe je [een Azure OpenAI Service resource kunt maken en implementeren.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Voor het eerst de OpenAI API gebruiken

Als dit de eerste keer is dat je werkt met de OpenAI API, volg dan de gids over hoe je [de interface kunt maken en gebruiken.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Andere deelnemers ontmoeten

We hebben kanalen aangemaakt in onze officiële [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) om andere deelnemers te ontmoeten. Dit is een geweldige manier om te netwerken met andere gelijkgestemde ondernemers, bouwers, studenten en iedereen die zijn vaardigheden in Generatieve AI wil verbeteren.

[![Word lid van Discord-kanaal](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Het projectteam zal ook aanwezig zijn op deze Discord-server om deelnemers te helpen.

## Bijdragen

Deze cursus is een open-source initiatief. Als je verbeterpunten of problemen ziet, maak dan een [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) of log een [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Het projectteam zal alle bijdragen bijhouden. Bijdragen aan open source is een geweldige manier om je carrière in Generatieve AI op te bouwen.

De meeste bijdragen vereisen dat je akkoord gaat met een Contributor License Agreement (CLA) waarin je verklaart dat je het recht hebt om en daadwerkelijk de rechten verleent om je bijdrage te gebruiken. Voor meer informatie, bezoek [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Belangrijk: bij het vertalen van tekst in deze repo, zorg ervoor dat je geen gebruik maakt van automatische vertaling. We zullen vertalingen verifiëren via de community, dus bied alleen aan om te vertalen in talen waarin je bekwaam bent.

Wanneer je een pull request indient, zal een CLA-bot automatisch bepalen of je een CLA moet indienen en de PR dienovereenkomstig voorzien van een label of opmerking. Volg gewoon de instructies van de bot. Je hoeft dit slechts één keer te doen voor alle repositories die onze CLA gebruiken.

Dit project heeft de [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) aangenomen. Voor meer informatie lees de Code of Conduct FAQ of neem contact op met [Email opencode](opencode@microsoft.com) voor eventuele aanvullende vragen of opmerkingen.

## Laten we beginnen
Nu je de benodigde stappen hebt voltooid om deze cursus af te ronden, laten we beginnen met een [introductie tot Generatieve AI en LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.