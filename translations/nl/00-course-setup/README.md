<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T17:49:47+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "nl"
}
-->
# Aan de slag met deze cursus

We zijn ontzettend enthousiast dat je met deze cursus begint en benieuwd wat jij gaat bouwen met Generative AI!

Om je te helpen slagen, vind je op deze pagina de stappen voor de setup, technische vereisten en waar je hulp kunt krijgen als dat nodig is.

## Stappen voor de setup

Om te starten met deze cursus, moet je de volgende stappen doorlopen.

### 1. Fork deze repo

[Fork deze hele repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) naar je eigen GitHub-account zodat je de code kunt aanpassen en de uitdagingen kunt voltooien. Je kunt deze repo ook [sterren (🌟) geven](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) om hem en gerelateerde repos makkelijker terug te vinden.

### 2. Maak een codespace aan

Om problemen met afhankelijkheden te voorkomen bij het uitvoeren van de code, raden we aan om deze cursus te volgen in een [GitHub Codespace](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

In je fork: **Code -> Codespaces -> New on main**

![Dialoogvenster met knoppen om een codespace aan te maken](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Voeg een secret toe

1. ⚙️ Tandwiel icoon -> Command Pallete-> Codespaces : Manage user secret -> Voeg een nieuwe secret toe.
2. Geef de naam OPENAI_API_KEY, plak je sleutel, Opslaan.

### 3. Wat nu?

| Ik wil…              | Ga naar…                                                                |
|----------------------|-------------------------------------------------------------------------|
| Starten met Les 1    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Offline werken       | [`setup-local.md`](02-setup-local.md)                                   |
| Een LLM Provider instellen | [`providers.md`](providers.md)                                    |
| Andere deelnemers ontmoeten | [Word lid van onze Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Problemen oplossen

| Symptoom                                   | Oplossing                                                      |
|--------------------------------------------|----------------------------------------------------------------|
| Container build blijft hangen > 10 min     | **Codespaces ➜ “Rebuild Container”**                           |
| `python: command not found`                | Terminal is niet verbonden; klik op **+** ➜ *bash*             |
| `401 Unauthorized` van OpenAI              | Verkeerde / verlopen `OPENAI_API_KEY`                          |
| VS Code toont “Dev container mounting…”    | Vernieuw het browsertabblad—Codespaces verliest soms verbinding|
| Notebook kernel ontbreekt                  | Notebook menu ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

   Unix-gebaseerde systemen:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Bewerk het `.env`-bestand**: Open het `.env`-bestand in een teksteditor (bijv. VS Code, Notepad++, of een andere editor). Voeg de volgende regel toe aan het bestand, waarbij je `your_github_token_here` vervangt door je echte GitHub-token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Sla het bestand op**: Sla de wijzigingen op en sluit de teksteditor.

5. **Installeer `python-dotenv`**: Als je dit nog niet hebt gedaan, moet je het pakket `python-dotenv` installeren om omgevingsvariabelen uit het `.env`-bestand in je Python-applicatie te laden. Je kunt het installeren met `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Laad omgevingsvariabelen in je Python-script**: Gebruik in je Python-script het pakket `python-dotenv` om de omgevingsvariabelen uit het `.env`-bestand te laden:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Dat is alles! Je hebt succesvol een `.env`-bestand aangemaakt, je GitHub-token toegevoegd en deze geladen in je Python-applicatie.

## Hoe je lokaal op je computer kunt werken

Om de code lokaal op je computer uit te voeren, heb je een versie van [Python nodig](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Om de repository te gebruiken, moet je deze clonen:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Als je alles hebt binnengehaald, kun je aan de slag!

## Optionele stappen

### Miniconda installeren

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) is een lichte installer voor het installeren van [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python en enkele pakketten.
Conda zelf is een pakketbeheerder die het makkelijk maakt om verschillende Python [**virtuele omgevingen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) en pakketten te beheren. Het is ook handig voor het installeren van pakketten die niet via `pip` beschikbaar zijn.

Je kunt de [MiniConda installatiegids](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) volgen om het te installeren.

Met Miniconda geïnstalleerd, moet je de [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) clonen (als je dat nog niet hebt gedaan).

Daarna moet je een virtuele omgeving aanmaken. Met Conda doe je dit door een nieuw omgevingsbestand (_environment.yml_) aan te maken. Als je Codespaces gebruikt, maak je dit aan in de `.devcontainer`-map, dus `.devcontainer/environment.yml`.

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

Als je fouten krijgt met conda, kun je de Microsoft AI Libraries handmatig installeren met het volgende commando in een terminal.

```
conda install -c microsoft azure-ai-ml
```

Het omgevingsbestand geeft de benodigde afhankelijkheden aan. `<environment-name>` is de naam die je wilt geven aan je Conda-omgeving, en `<python-version>` is de versie van Python die je wilt gebruiken, bijvoorbeeld `3` is de nieuwste hoofdversie van Python.

Daarna kun je je Conda-omgeving aanmaken door de onderstaande commando’s uit te voeren in je command line/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Raadpleeg de [Conda environments gids](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) als je problemen tegenkomt.

### Visual Studio Code gebruiken met de Python-extensie

We raden aan om de [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editor te gebruiken met de [Python-extensie](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) voor deze cursus. Dit is echter een aanbeveling en geen vereiste.

> **Note**: Door de cursusrepository te openen in VS Code, kun je het project in een container opzetten. Dit komt door de [speciale `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) map in de cursusrepository. Hierover later meer.

> **Note**: Zodra je de directory hebt gekloond en geopend in VS Code, zal het automatisch voorstellen om een Python-extensie te installeren.

> **Note**: Als VS Code voorstelt om de repository in een container te openen, weiger dit verzoek om de lokaal geïnstalleerde versie van Python te gebruiken.

### Jupyter in de browser gebruiken

Je kunt ook aan het project werken via de [Jupyter-omgeving](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direct in je browser. Zowel klassieke Jupyter als [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) bieden een prettige ontwikkelomgeving met functies zoals automatisch aanvullen, code-highlighting, enzovoort.

Om Jupyter lokaal te starten, ga je naar de terminal/command line, navigeer je naar de cursusmap en voer je uit:

```bash
jupyter notebook
```

of

```bash
jupyterhub
```

Hiermee start je een Jupyter-instantie en het URL-adres om toegang te krijgen wordt in het command line venster getoond.

Als je het URL-adres opent, zie je het cursusoverzicht en kun je naar elk `*.ipynb`-bestand navigeren. Bijvoorbeeld, `08-building-search-applications/python/oai-solution.ipynb`.

### Uitvoeren in een container

Een alternatief voor alles lokaal of in Codespace opzetten is werken in een [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). De speciale `.devcontainer`-map in de cursusrepository maakt het mogelijk voor VS Code om het project in een container op te zetten. Buiten Codespaces vereist dit de installatie van Docker, en eerlijk gezegd is dit wat meer werk, dus we raden dit alleen aan voor mensen met ervaring met containers.

Een van de beste manieren om je API-sleutels veilig te houden in GitHub Codespaces is door Codespace Secrets te gebruiken. Volg de [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) gids om hier meer over te leren.


## Lessen en technische vereisten

De cursus bestaat uit 6 conceptlessen en 6 programmeerlessen.

Voor de programmeerlessen gebruiken we de Azure OpenAI Service. Je hebt toegang tot de Azure OpenAI service en een API-sleutel nodig om deze code uit te voeren. Je kunt toegang aanvragen door [deze aanvraag in te vullen](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Terwijl je wacht op goedkeuring van je aanvraag, bevat elke programmeerles ook een `README.md`-bestand waarin je de code en resultaten kunt bekijken.

## Azure OpenAI Service voor het eerst gebruiken

Als je voor het eerst werkt met de Azure OpenAI service, volg dan deze gids om te leren [hoe je een Azure OpenAI Service resource aanmaakt en uitrolt.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## OpenAI API voor het eerst gebruiken

Als je voor het eerst werkt met de OpenAI API, volg dan de gids over [hoe je de Interface aanmaakt en gebruikt.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Andere deelnemers ontmoeten

We hebben kanalen aangemaakt in onze officiële [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) om andere deelnemers te ontmoeten. Dit is een mooie manier om te netwerken met andere ondernemers, makers, studenten en iedereen die zich wil verdiepen in Generative AI.

[![Word lid van het discordkanaal](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Het projectteam is ook aanwezig op deze Discord server om deelnemers te helpen.

## Bijdragen

Deze cursus is een open-source initiatief. Als je verbeteringen of problemen ziet, maak dan een [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) aan of meld een [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Het projectteam houdt alle bijdragen bij. Bijdragen aan open source is een geweldige manier om je carrière in Generative AI op te bouwen.

Voor de meeste bijdragen moet je akkoord gaan met een Contributor License Agreement (CLA) waarin je verklaart dat je het recht hebt om je bijdrage te leveren en ons toestemming geeft om deze te gebruiken. Meer informatie vind je op de [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Belangrijk: bij het vertalen van tekst in deze repo, zorg ervoor dat je geen machinevertaling gebruikt. We controleren vertalingen via de community, dus bied alleen vertalingen aan in talen waarin je vaardig bent.

Wanneer je een pull request indient, bepaalt een CLA-bot automatisch of je een CLA moet ondertekenen en voegt het juiste label of commentaar toe. Volg gewoon de instructies van de bot. Je hoeft dit maar één keer te doen voor alle repositories die onze CLA gebruiken.

Dit project hanteert de [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Voor meer informatie lees de Code of Conduct FAQ of neem contact op met [Email opencode](opencode@microsoft.com) voor vragen of opmerkingen.

## Laten we beginnen
Nu je de benodigde stappen hebt doorlopen om deze cursus te voltooien, gaan we van start met een [introductie tot Generatieve AI en LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritische informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.