<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-05-19T12:30:08+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "nl"
}
-->
# Aan de slag met deze cursus

We zijn erg enthousiast dat je met deze cursus begint en benieuwd naar wat je geïnspireerd raakt om te bouwen met Generatieve AI!

Om je succes te garanderen, worden op deze pagina de stappen voor de setup, technische vereisten en waar je hulp kunt krijgen indien nodig, uiteengezet.

## Setup Stappen

Om deze cursus te volgen, moet je de volgende stappen voltooien.

### 1. Fork deze Repo

[Fork deze hele repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) naar je eigen GitHub-account zodat je de code kunt wijzigen en de uitdagingen kunt voltooien. Je kunt ook [deze repo ster (🌟) geven](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) om het en gerelateerde repo's gemakkelijker te vinden.

### 2. Maak een codespace

Om eventuele afhankelijkheidsproblemen bij het uitvoeren van de code te vermijden, raden we aan deze cursus uit te voeren in een [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Dit kan worden aangemaakt door de optie `Code` te selecteren op je geforkte versie van deze repo en de optie **Codespaces** te kiezen.

![Dialoogvenster met knoppen om een codespace te maken](../../../00-course-setup/images/who-will-pay.webp)

### 3. Opslaan van je API-sleutels

Het veilig en beveiligd houden van je API-sleutels is belangrijk bij het bouwen van elke vorm van applicatie. We raden aan om geen API-sleutels direct in je code op te slaan. Het vastleggen van die gegevens in een openbare repository kan leiden tot beveiligingsproblemen en zelfs ongewenste kosten als ze worden gebruikt door een kwaadwillende.
Hier is een stapsgewijze handleiding over hoe je een `.env`-bestand voor Python maakt en de `GITHUB_TOKEN` toevoegt:

1. **Navigeer naar je projectdirectory**: Open je terminal of opdrachtprompt en navigeer naar de hoofdmap van je project waar je het `.env`-bestand wilt maken.

   ```bash
   cd path/to/your/project
   ```

2. **Maak het `.env`-bestand**: Gebruik je favoriete teksteditor om een nieuw bestand te maken met de naam `.env`. Als je de opdrachtregel gebruikt, kun je `touch` (on Unix-based systems) or `echo` gebruiken (op Windows):

   Unix-gebaseerde systemen:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Bewerk het `.env`-bestand**: Open het `.env`-bestand in een teksteditor (bijv. VS Code, Notepad++, of een andere editor). Voeg de volgende regel toe aan het bestand, waarbij je `your_github_token_here` vervangt door je daadwerkelijke GitHub-token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Sla het bestand op**: Sla de wijzigingen op en sluit de teksteditor.

5. **Installeer `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv`-pakket om omgevingsvariabelen uit het `.env`-bestand in je Python-applicatie te laden. Je kunt het installeren met `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Laad omgevingsvariabelen in je Python-script**: Gebruik in je Python-script het `python-dotenv`-pakket om de omgevingsvariabelen uit het `.env`-bestand te laden:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Dat is het! Je hebt succesvol een `.env`-bestand gemaakt, je GitHub-token toegevoegd en het geladen in je Python-applicatie.

## Hoe lokaal op je computer te draaien

Om de code lokaal op je computer uit te voeren, moet je een versie van [Python geïnstalleerd](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) hebben.

Om vervolgens de repository te gebruiken, moet je deze klonen:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Zodra je alles hebt uitgecheckt, kun je aan de slag!

## Optionele stappen

### Miniconda installeren

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) is een lichte installer voor het installeren van [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, evenals enkele pakketten.
Conda zelf is een pakketbeheerder, die het gemakkelijk maakt om verschillende Python [**virtuele omgevingen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) en pakketten in te stellen en te wisselen. Het is ook handig voor het installeren van pakketten die niet beschikbaar zijn via `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Ga je gang en vul je omgevingsbestand met de onderstaande snippet:

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

Als je fouten krijgt bij het gebruik van conda, kun je de Microsoft AI Libraries handmatig installeren met het volgende commando in een terminal.

```
conda install -c microsoft azure-ai-ml
```

Het omgevingsbestand specificeert de benodigde afhankelijkheden. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` is de nieuwste hoofdversie van Python.

Met dat gedaan, kun je je Conda-omgeving maken door de onderstaande opdrachten in je opdrachtregel/terminal uit te voeren

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Raadpleeg de [Conda omgevingen handleiding](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) als je problemen tegenkomt.

### Gebruik van Visual Studio Code met de Python-ondersteuning extensie

We raden aan om de [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editor te gebruiken met de [Python-ondersteuning extensie](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) geïnstalleerd voor deze cursus. Dit is echter meer een aanbeveling en geen absolute vereiste.

> **Opmerking**: Door de cursusrepository in VS Code te openen, heb je de optie om het project binnen een container op te zetten. Dit komt door de [speciale `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) directory die in de cursusrepository te vinden is. Hierover later meer.

> **Opmerking**: Zodra je de directory kloont en opent in VS Code, zal het automatisch voorstellen om een Python-ondersteuning extensie te installeren.

> **Opmerking**: Als VS Code je vraagt om de repository opnieuw te openen in een container, wijs dit verzoek af om de lokaal geïnstalleerde versie van Python te gebruiken.

### Gebruik van Jupyter in de browser

Je kunt ook aan het project werken met de [Jupyter-omgeving](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direct in je browser. Zowel klassieke Jupyter als [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) bieden een aangename ontwikkelomgeving met functies zoals automatische aanvulling, code-highlighting, enz.

Om Jupyter lokaal te starten, ga naar de terminal/opdrachtregel, navigeer naar de cursusdirectory en voer uit:

```bash
jupyter notebook
```

of

```bash
jupyterhub
```

Dit zal een Jupyter-instance starten en de URL om toegang te krijgen zal binnen het opdrachtregelvenster worden weergegeven.

Zodra je toegang hebt tot de URL, zou je de cursusoutline moeten zien en kunnen navigeren naar elk `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` bestand waar je de code en uitvoer kunt bekijken.

## Gebruik van de Azure OpenAI Service voor de eerste keer

Als dit je eerste keer is dat je met de Azure OpenAI-service werkt, volg dan deze handleiding over hoe je [een Azure OpenAI Service-resource kunt maken en implementeren.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Gebruik van de OpenAI API voor de eerste keer

Als dit je eerste keer is dat je met de OpenAI API werkt, volg dan de handleiding over hoe je [de Interface kunt maken en gebruiken.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Ontmoet andere deelnemers

We hebben kanalen aangemaakt in onze officiële [AI Community Discord-server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) om andere deelnemers te ontmoeten. Dit is een geweldige manier om te netwerken met andere gelijkgestemde ondernemers, bouwers, studenten, en iedereen die zijn vaardigheden in Generatieve AI wil verbeteren.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Het projectteam zal ook op deze Discord-server zijn om deelnemers te helpen.

## Bijdragen

Deze cursus is een open-source initiatief. Als je verbeterpunten of problemen ziet, maak dan een [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) of log een [GitHub-issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Het projectteam zal alle bijdragen volgen. Bijdragen aan open source is een geweldige manier om je carrière in Generatieve AI op te bouwen.

De meeste bijdragen vereisen dat je akkoord gaat met een Contributor License Agreement (CLA) waarin je verklaart dat je het recht hebt om en daadwerkelijk ons de rechten geeft om je bijdrage te gebruiken. Voor details, bezoek de [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Belangrijk: bij het vertalen van tekst in deze repo, zorg ervoor dat je geen gebruik maakt van machinevertaling. We zullen vertalingen via de community verifiëren, dus vrijwillig alleen voor vertalingen in talen waarin je bekwaam bent.

Wanneer je een pull request indient, zal een CLA-bot automatisch bepalen of je een CLA moet verstrekken en de PR dienovereenkomstig decoreren (bijv. label, commentaar). Volg gewoon de instructies die door de bot worden gegeven. Je hoeft dit slechts één keer te doen voor alle repositories die onze CLA gebruiken.

Dit project heeft de [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) aangenomen. Voor meer informatie lees de Code of Conduct FAQ of neem contact op met [Email opencode](opencode@microsoft.com) met eventuele aanvullende vragen of opmerkingen.

## Laten we beginnen

Nu je de benodigde stappen hebt voltooid om deze cursus te voltooien, laten we beginnen met een [introductie tot Generatieve AI en LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, willen we u erop wijzen dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of misinterpretaties die voortvloeien uit het gebruik van deze vertaling.