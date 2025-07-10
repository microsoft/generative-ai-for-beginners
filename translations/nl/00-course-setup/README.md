<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T07:12:31+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "nl"
}
-->
# Aan de slag met deze cursus

We zijn erg enthousiast dat je deze cursus gaat starten en benieuwd wat je geïnspireerd raakt om te bouwen met Generative AI!

Om je succes te garanderen, geeft deze pagina een overzicht van de installatie stappen, technische vereisten en waar je hulp kunt krijgen indien nodig.

## Installatiestappen

Om met deze cursus te beginnen, moet je de volgende stappen doorlopen.

### 1. Fork deze Repo

[Fork deze hele repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) naar je eigen GitHub-account zodat je de code kunt aanpassen en de uitdagingen kunt voltooien. Je kunt ook [deze repo een ster (🌟) geven](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) om het en gerelateerde repos makkelijker terug te vinden.

### 2. Maak een codespace aan

Om afhankelijkheidsproblemen bij het uitvoeren van de code te voorkomen, raden we aan deze cursus te draaien in een [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Dit kun je aanmaken door de optie `Code` te selecteren in jouw geforkte versie van deze repo en vervolgens de **Codespaces** optie te kiezen.

![Dialoogvenster met knoppen om een codespace aan te maken](../../../00-course-setup/images/who-will-pay.webp)

### 3. Je API-sleutels opslaan

Het is belangrijk om je API-sleutels veilig te bewaren bij het bouwen van welke applicatie dan ook. We raden af om API-sleutels direct in je code op te slaan. Als je deze gegevens in een openbare repository zet, kan dat leiden tot beveiligingsproblemen en zelfs ongewenste kosten als kwaadwillenden ze gebruiken.  
Hier is een stapsgewijze handleiding om een `.env` bestand aan te maken voor Python en de `GITHUB_TOKEN` toe te voegen:

1. **Navigeer naar je projectmap**: Open je terminal of opdrachtprompt en ga naar de hoofdmap van je project waar je het `.env` bestand wilt aanmaken.

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

3. **Bewerk het `.env` bestand**: Open het `.env` bestand in een teksteditor (bijv. VS Code, Notepad++ of een andere editor). Voeg de volgende regel toe, waarbij je `your_github_token_here` vervangt door je eigen GitHub-token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Sla het bestand op**: Sla de wijzigingen op en sluit de teksteditor.

5. **Installeer `python-dotenv`**: Als je dit nog niet hebt gedaan, moet je het `python-dotenv` pakket installeren om omgevingsvariabelen uit het `.env` bestand in je Python-applicatie te laden. Dit kan met `pip`:

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

## Hoe lokaal op je computer te draaien

Om de code lokaal op je computer uit te voeren, moet je een versie van [Python geïnstalleerd hebben](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Om vervolgens de repository te gebruiken, moet je deze clonen:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Als je alles hebt klaargezet, kun je aan de slag!

## Optionele stappen

### Miniconda installeren

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) is een lichte installer voor het installeren van [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python en een aantal pakketten.  
Conda zelf is een pakketbeheerder die het makkelijk maakt om verschillende Python [**virtuele omgevingen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) en pakketten op te zetten en te wisselen. Het is ook handig voor het installeren van pakketten die niet via `pip` beschikbaar zijn.

Je kunt de [MiniConda installatiehandleiding](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) volgen om het op te zetten.

Met Miniconda geïnstalleerd, moet je de [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) clonen (als je dat nog niet gedaan hebt).

Vervolgens moet je een virtuele omgeving aanmaken. Om dit met Conda te doen, maak je een nieuw omgevingsbestand aan (_environment.yml_). Als je Codespaces gebruikt, maak dit dan aan in de `.devcontainer` map, dus `.devcontainer/environment.yml`.

Vul je omgevingsbestand met onderstaande snippet:

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

Het omgevingsbestand specificeert de benodigde dependencies. `<environment-name>` is de naam die je wilt gebruiken voor je Conda-omgeving, en `<python-version>` is de Python-versie die je wilt gebruiken, bijvoorbeeld `3` voor de nieuwste grote versie van Python.

Als dat klaar is, kun je je Conda-omgeving aanmaken door onderstaande commando’s in je command line/terminal uit te voeren:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Raadpleeg de [Conda omgevingen handleiding](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) als je problemen tegenkomt.

### Visual Studio Code gebruiken met de Python support extensie

We raden aan om de editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) te gebruiken met de [Python support extensie](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) geïnstalleerd voor deze cursus. Dit is echter een aanbeveling en geen harde vereiste.

> **Note**: Door de cursusrepository in VS Code te openen, kun je het project opzetten binnen een container. Dit komt door de [speciale `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) map in de cursusrepository. Hierover later meer.

> **Note**: Zodra je de directory clonet en opent in VS Code, zal het automatisch voorstellen om een Python support extensie te installeren.

> **Note**: Als VS Code je vraagt om de repository opnieuw te openen in een container, weiger dit verzoek om de lokaal geïnstalleerde versie van Python te gebruiken.

### Jupyter in de browser gebruiken

Je kunt ook aan het project werken met de [Jupyter omgeving](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direct in je browser. Zowel klassieke Jupyter als [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) bieden een prettige ontwikkelomgeving met functies zoals auto-aanvullen, code-highlighting, enzovoort.

Om Jupyter lokaal te starten, ga je naar de terminal/opdrachtprompt, navigeer je naar de cursusmap en voer je uit:

```bash
jupyter notebook
```

of

```bash
jupyterhub
```

Dit start een Jupyter instantie en de URL om deze te bereiken wordt getoond in het commandovenster.

Als je de URL opent, zie je de cursusindeling en kun je navigeren naar elk `*.ipynb` bestand. Bijvoorbeeld `08-building-search-applications/python/oai-solution.ipynb`.

### Draaien in een container

Een alternatief voor het lokaal of in Codespaces opzetten is het gebruik van een [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). De speciale `.devcontainer` map in de cursusrepository maakt het mogelijk voor VS Code om het project binnen een container op te zetten. Buiten Codespaces vereist dit de installatie van Docker en eerlijk gezegd is het wat werk, dus we raden dit alleen aan voor mensen met ervaring met containers.

Een van de beste manieren om je API-sleutels veilig te houden bij het gebruik van GitHub Codespaces is door gebruik te maken van Codespace Secrets. Volg de [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) handleiding om hier meer over te leren.

## Lessen en technische vereisten

De cursus bevat 6 conceptlessen en 6 programmeerlessen.

Voor de programmeerlessen gebruiken we de Azure OpenAI Service. Je hebt toegang tot de Azure OpenAI service en een API-sleutel nodig om deze code te draaien. Je kunt toegang aanvragen door [deze aanvraag in te vullen](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Terwijl je wacht op de verwerking van je aanvraag, bevat elke programmeerles ook een `README.md` bestand waarin je de code en resultaten kunt bekijken.

## De Azure OpenAI Service voor het eerst gebruiken

Als dit je eerste keer is dat je met de Azure OpenAI service werkt, volg dan deze handleiding over hoe je een [Azure OpenAI Service resource aanmaakt en uitrolt.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## De OpenAI API voor het eerst gebruiken

Als dit je eerste keer is dat je met de OpenAI API werkt, volg dan de handleiding over hoe je [de interface aanmaakt en gebruikt.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Ontmoet andere cursisten

We hebben kanalen aangemaakt in onze officiële [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) om andere cursisten te ontmoeten. Dit is een geweldige manier om te netwerken met gelijkgestemde ondernemers, bouwers, studenten en iedereen die zich wil ontwikkelen in Generative AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Het projectteam is ook aanwezig op deze Discord server om cursisten te helpen.

## Bijdragen

Deze cursus is een open-source initiatief. Zie je verbeterpunten of problemen, maak dan een [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) aan of meld een [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Het projectteam houdt alle bijdragen bij. Bijdragen aan open source is een geweldige manier om je carrière in Generative AI op te bouwen.

De meeste bijdragen vereisen dat je akkoord gaat met een Contributor License Agreement (CLA) waarin je verklaart dat je het recht hebt en daadwerkelijk toestemming geeft om je bijdrage te gebruiken. Voor details, bezoek de [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Belangrijk: bij het vertalen van tekst in deze repo, zorg ervoor dat je geen machinevertaling gebruikt. We zullen vertalingen via de community controleren, dus meld je alleen aan voor vertalingen in talen waarin je goed bent.

Wanneer je een pull request indient, bepaalt een CLA-bot automatisch of je een CLA moet aanleveren en voorziet het PR van de juiste labels of opmerkingen. Volg gewoon de instructies van de bot. Dit hoef je maar één keer te doen voor alle repositories die onze CLA gebruiken.

Dit project heeft de [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) aangenomen. Voor meer informatie lees de Code of Conduct FAQ of neem contact op via [Email opencode](opencode@microsoft.com) bij vragen of opmerkingen.

## Laten we beginnen

Nu je de benodigde stappen hebt voltooid om deze cursus te volgen, beginnen we met een [introductie tot Generative AI en LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.