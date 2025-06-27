<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:53:01+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "nl"
}
-->
# Aan de slag met deze cursus

We zijn erg enthousiast dat je aan deze cursus begint en zijn benieuwd wat je geïnspireerd raakt om te bouwen met Generatieve AI!

Om je succes te garanderen, beschrijft deze pagina de installatie stappen, technische vereisten en waar je hulp kunt krijgen indien nodig.

## Installatiestappen

Om deze cursus te volgen, moet je de volgende stappen voltooien.

### 1. Fork deze Repo

[Fork de hele repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) naar je eigen GitHub-account om de code te kunnen wijzigen en de uitdagingen te voltooien. Je kunt ook [deze repo ster (🌟) geven](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) om het en gerelateerde repo's gemakkelijker te vinden.

### 2. Maak een codespace

Om afhankelijkheidsproblemen te voorkomen bij het uitvoeren van de code, raden we aan om deze cursus in een [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) te draaien.

Dit kan worden aangemaakt door de `Code` optie te selecteren op je geforkte versie van deze repo en de **Codespaces** optie te kiezen.

![Dialoogvenster met knoppen om een codespace te maken](../../../00-course-setup/images/who-will-pay.webp)

### 3. Je API-sleutels opslaan

Het is belangrijk om je API-sleutels veilig en beveiligd te houden bij het bouwen van een applicatie. We raden aan om geen API-sleutels direct in je code op te slaan. Het vastleggen van die details in een openbare repository kan leiden tot beveiligingsproblemen en zelfs ongewenste kosten als ze door een kwaadwillende worden gebruikt. Hier is een stapsgewijze handleiding over hoe je een `.env` bestand voor Python maakt en de `GITHUB_TOKEN` toevoegt:

1. **Navigeer naar je projectdirectory**: Open je terminal of opdrachtprompt en navigeer naar de hoofdmap van je project waar je het `.env` bestand wilt maken.

   ```bash
   cd path/to/your/project
   ```

2. **Maak het `.env` bestand**: Gebruik je favoriete teksteditor om een nieuw bestand genaamd `.env` te maken. Als je de opdrachtregel gebruikt, kun je `touch` (on Unix-based systems) or `echo` gebruiken (op Windows):

   Unix-gebaseerde systemen:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Bewerk het `.env` bestand**: Open het `.env` bestand in een teksteditor (bijv. VS Code, Notepad++ of een andere editor). Voeg de volgende regel toe aan het bestand en vervang `your_github_token_here` door je eigen GitHub-token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Sla het bestand op**: Sla de wijzigingen op en sluit de teksteditor.

5. **Installeer het `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` pakket om omgevingsvariabelen uit het `.env` bestand in je Python-applicatie te laden. Je kunt het installeren met `pip`:

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

Dat is het! Je hebt met succes een `.env` bestand aangemaakt, je GitHub-token toegevoegd en het in je Python-applicatie geladen.

## Hoe lokaal op je computer uit te voeren

Om de code lokaal op je computer uit te voeren, moet je een versie van [Python geïnstalleerd hebben](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Om de repository vervolgens te gebruiken, moet je deze klonen:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Zodra je alles hebt uitgecheckt, kun je aan de slag!

## Optionele stappen

### Miniconda installeren

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) is een lichte installer voor het installeren van [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, en enkele pakketten.
Conda zelf is een pakketbeheerder die het gemakkelijk maakt om verschillende Python [**virtuele omgevingen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) en pakketten op te zetten en te wisselen. Het is ook handig voor het installeren van pakketten die niet beschikbaar zijn via `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

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

Als je fouten krijgt bij het gebruik van conda, kun je handmatig de Microsoft AI Libraries installeren met het volgende commando in een terminal.

```
conda install -c microsoft azure-ai-ml
```

Het omgevingsbestand specificeert de vereiste afhankelijkheden. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` is de nieuwste hoofdversie van Python.

Als dat is gedaan, kun je je Conda-omgeving aanmaken door de onderstaande commando's in je opdrachtregel/terminal uit te voeren

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Raadpleeg de [Conda environments handleiding](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) als je problemen ondervindt.

### Visual Studio Code gebruiken met de Python ondersteuningsextensie

We raden aan om de [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editor te gebruiken met de [Python ondersteuningsextensie](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) geïnstalleerd voor deze cursus. Dit is echter meer een aanbeveling en geen vereiste.

> **Opmerking**: Door de cursusrepository in VS Code te openen, heb je de optie om het project binnen een container in te stellen. Dit komt door de [speciale `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) directory die binnen de cursusrepository te vinden is. Meer hierover later.

> **Opmerking**: Zodra je de directory kloont en opent in VS Code, zal het automatisch voorstellen om een Python ondersteuningsextensie te installeren.

> **Opmerking**: Als VS Code je voorstelt om de repository in een container opnieuw te openen, weiger dit verzoek om de lokaal geïnstalleerde versie van Python te gebruiken.

### Jupyter in de browser gebruiken

Je kunt ook aan het project werken met behulp van de [Jupyter-omgeving](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direct in je browser. Zowel klassieke Jupyter als [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) bieden een prettige ontwikkelomgeving met functies zoals autocompletion, code highlighting, enz.

Om Jupyter lokaal te starten, ga naar de terminal/opdrachtregel, navigeer naar de cursusdirectory en voer uit:

```bash
jupyter notebook
```

of

```bash
jupyterhub
```

Dit zal een Jupyter-instantie starten en de URL om toegang te krijgen zal binnen het opdrachtregelvenster worden getoond.

Zodra je toegang hebt tot de URL, zou je het cursusoverzicht moeten zien en naar elk `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` bestand kunnen navigeren waar je de code en uitvoer kunt bekijken.

## Voor het eerst de Azure OpenAI Service gebruiken

Als dit de eerste keer is dat je met de Azure OpenAI-service werkt, volg dan deze handleiding over hoe je een [Azure OpenAI Service-resource aanmaakt en implementeert.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Voor het eerst de OpenAI API gebruiken

Als dit de eerste keer is dat je met de OpenAI API werkt, volg dan de handleiding over hoe je de [Interface aanmaakt en gebruikt.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Andere Lerenden Ontmoeten

We hebben kanalen aangemaakt in onze officiële [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) om andere lerenden te ontmoeten. Dit is een geweldige manier om te netwerken met andere gelijkgestemde ondernemers, bouwers, studenten en iedereen die zijn vaardigheden in Generatieve AI wil verbeteren.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Het projectteam zal ook op deze Discord-server zijn om lerenden te helpen.

## Bijdragen

Deze cursus is een open-source initiatief. Als je verbeterpunten of problemen ziet, maak dan een [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) of log een [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Het projectteam zal alle bijdragen bijhouden. Bijdragen aan open source is een geweldige manier om je carrière in Generatieve AI op te bouwen.

De meeste bijdragen vereisen dat je akkoord gaat met een Contributor License Agreement (CLA) waarin je verklaart dat je het recht hebt om ons de rechten te verlenen om je bijdrage te gebruiken. Voor details, bezoek de [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Belangrijk: bij het vertalen van tekst in deze repo, zorg ervoor dat je geen machinevertaling gebruikt. We zullen vertalingen via de gemeenschap verifiëren, dus meld je alleen aan voor vertalingen in talen waarin je bekwaam bent.

Wanneer je een pull request indient, zal een CLA-bot automatisch bepalen of je een CLA moet verstrekken en de PR op de juiste manier labelen (bijv. label, opmerking). Volg gewoon de instructies die door de bot worden gegeven. Je hoeft dit slechts één keer te doen voor alle repositories die onze CLA gebruiken.

Dit project heeft de [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) aangenomen. Voor meer informatie lees de Code of Conduct FAQ of neem contact op met [Email opencode](opencode@microsoft.com) met eventuele aanvullende vragen of opmerkingen.

## Laten we beginnen

Nu je de benodigde stappen hebt voltooid om deze cursus te voltooien, laten we beginnen met een [introductie tot Generatieve AI en LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Disclaimer**:  
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of misinterpretaties die voortvloeien uit het gebruik van deze vertaling.