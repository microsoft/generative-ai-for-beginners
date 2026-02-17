# Aan de slag met deze cursus

We zijn erg enthousiast dat je aan deze cursus begint en wilt zien wat je geïnspireerd raakt om te bouwen met Generatieve AI!

Om je succes te verzekeren, beschrijft deze pagina de installatiestappen, technische vereisten en waar je hulp kunt krijgen indien nodig.

## Installatiestappen

Om met deze cursus te beginnen, moet je de volgende stappen voltooien.

### 1. Fork deze Repo

[Fork deze hele repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) naar je eigen GitHub-account zodat je code kunt aanpassen en de uitdagingen kunt voltooien. Je kunt ook deze repo [star (🌟) geven](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) om hem en gerelateerde repos makkelijker terug te vinden.

### 2. Maak een codespace aan

Om afhankelijkheidsproblemen bij het uitvoeren van de code te vermijden, raden we aan deze cursus te draaien in een [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

In je fork: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/nl/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Voeg een geheim toe

1. ⚙️ Tandwiel icoon -> Command Palette -> Codespaces : Manage user secret -> Voeg een nieuw geheim toe.
2. Naam OPENAI_API_KEY, plak je sleutel, Opslaan.

### 3. Wat nu?

| Ik wil…             | Ga naar…                                                               |
|---------------------|------------------------------------------------------------------------|
| Beginnen met Les 1  | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Offline werken      | [`setup-local.md`](02-setup-local.md)                                   |
| Een LLM Provider instellen | [`providers.md`](03-providers.md)                                        |
| Andere cursisten ontmoeten | [Word lid van onze Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Problemen oplossen


| Symptoom                                   | Oplossing                                                        |
|--------------------------------------------|-----------------------------------------------------------------|
| Container build blijft hangen > 10 min     | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`                  | Terminal is niet verbonden; klik **+** ➜ *bash*                 |
| `401 Unauthorized` van OpenAI                | Verkeerde / verlopen `OPENAI_API_KEY`                           |
| VS Code toont “Dev container mounting…”     | Vernieuw het browserscherm—Codespaces verliest soms de verbinding |
| Notebook kernel ontbreekt                    | Notebook menu ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix-gebaseerde systemen:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Bewerk het `.env`-bestand**: Open het `.env`-bestand in een teksteditor (zoals VS Code, Notepad++ of een andere editor). Voeg de volgende regel toe aan het bestand, vervang `your_github_token_here` door je eigen GitHub-token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Sla het bestand op**: Sla de wijzigingen op en sluit de teksteditor.

5. **Installeer `python-dotenv`**: Als je dit nog niet gedaan hebt, moet je het `python-dotenv` pakket installeren om omgevingsvariabelen uit het `.env`-bestand in je Python-applicatie te laden. Dat doe je via `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Laad Omgevingsvariabelen in je Python-script**: Gebruik in je Python-script het `python-dotenv` pakket om de variabelen uit het `.env`-bestand te laden:

   ```python
   from dotenv import load_dotenv
   import os

   # Laad omgevingsvariabelen uit het .env-bestand
   load_dotenv()

   # Toegang tot de GITHUB_TOKEN variabele
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Dat is alles! Je hebt nu succesvol een `.env`-bestand aangemaakt, je GitHub-token toegevoegd en deze geladen in je Python-applicatie.

## Hoe lokaal op je computer te draaien

Om de code lokaal op je computer te draaien, moet je een versie van [Python geïnstalleerd hebben](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Om dan de repository te gebruiken, moet je hem klonen:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Als je alles eenmaal hebt klaargezet, kun je aan de slag!

## Optionele stappen

### Miniconda installeren

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) is een lichte installer voor het installeren van [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python en een paar pakketten.
Conda zelf is een package manager, waarmee het makkelijk is om verschillende Python [**virtuele omgevingen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) en pakketten op te zetten en te wisselen. Het helpt ook bij het installeren van pakketten die niet via `pip` beschikbaar zijn.

Je kunt de [MiniConda installatiehandleiding](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) volgen om het op te zetten.

Met Miniconda geïnstalleerd, moet je de [repository klonen](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (als je dat nog niet gedaan hebt).

Vervolgens moet je een virtuele omgeving maken. Om dat met Conda te doen, maak je een nieuw environment-bestand aan (_environment.yml_). Als je Codespaces gebruikt, maak dit aan binnen de `.devcontainer` map, dus `.devcontainer/environment.yml`.

Vul je environment-bestand met de onderstaande snippet:

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

Het omgeving-bestand specificeert de benodigde afhankelijkheden. `<environment-name>` verwijst naar de naam die je wilt gebruiken voor je Conda-omgeving, en `<python-version>` is de versie van Python die je wilt gebruiken, bijvoorbeeld `3` is de meest recente hoofdversie van Python.

Als dat klaar is, kun je je Conda-omgeving aanmaken door onderstaande commando’s uit te voeren in je commandoregel/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer-subpad is alleen van toepassing op Codespace-setup
conda activate ai4beg
```

Raadpleeg de [Conda environments guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) indien je problemen ondervindt.

### Visual Studio Code gebruiken met de Python ondersteunings-extensie

We raden aan de [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editor te gebruiken met de [Python ondersteunde extensie](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) geïnstalleerd voor deze cursus. Dit is echter meer een aanbeveling en geen harde vereiste.

> **Opmerking**: Door de cursusrepository te openen in VS Code, kun je het project binnen een container opzetten. Dit dankzij de [speciale `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) map in de cursusrepository. Hierover later meer.

> **Opmerking**: Zodra je de directory klonet en opent in VS Code, zal het automatisch voorstellen de Python support extensie te installeren.

> **Opmerking**: Als VS Code je voorstelt de repo opnieuw te openen in een container, weiger dat verzoek om de lokaal geïnstalleerde versie van Python te gebruiken.

### Jupyter in de browser gebruiken

Je kunt ook met het project werken via de [Jupyter omgeving](https://jupyter.org?WT.mc_id=academic-105485-koreyst) in je browser. Zowel klassiek Jupyter als [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) bieden een prettige ontwikkelomgeving met functies zoals auto-completion, code-highlighting, enzovoort.

Om lokaal Jupyter te starten, ga naar de terminal/commandoregel, navigeer naar de cursuscatalogus en voer uit:

```bash
jupyter notebook
```

of

```bash
jupyterhub
```

Dit start een Jupyter-instantie en de URL om deze te benaderen wordt getoond in het commandovenster.

Zodra je de URL opent, zou je de cursusinhoud moeten zien en kun je naar elk `*.ipynb` bestand navigeren. Bijvoorbeeld, `08-building-search-applications/python/oai-solution.ipynb`.

### In een container draaien

Een alternatief voor het lokaal alles opzetten op je computer of in Codespaces is het gebruik van een [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). De speciale `.devcontainer` map binnen de cursusrepository maakt het mogelijk voor VS Code het project binnen een container op te zetten. Buiten Codespaces vereist dit de installatie van Docker, en eerlijk gezegd kost het wel wat werk, daarom raden we dit aan alleen te doen als je ervaring hebt met containers.

Een van de beste manieren om je API-sleutels veilig te houden bij het gebruik van GitHub Codespaces is door Codespace Secrets te gebruiken. Volg de [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) handleiding om hier meer over te leren.


## Lessen en technische vereisten

De cursus heeft 6 conceptlessen en 6 programmeerlessen.

Voor de programmeerlessen gebruiken we de Azure OpenAI Service. Je hebt toegang tot de Azure OpenAI service en een API-sleutel nodig om deze code te draaien. Je kunt toegang aanvragen door [deze aanvraag in te vullen](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Terwijl je wacht tot je aanvraag verwerkt is, bevat elke programmeerles ook een `README.md` bestand waarin je de code en resultaten kunt bekijken.

## De Azure OpenAI Service voor het eerst gebruiken

Als dit de eerste keer is dat je met de Azure OpenAI service werkt, volg dan deze gids over hoe je een Azure OpenAI Service-resource kunt [aanmaken en uitrollen.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## De OpenAI API voor het eerst gebruiken

Als dit je eerste keer is met de OpenAI API, volg dan de gids over hoe je [de Interface kunt aanmaken en gebruiken.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Andere cursisten ontmoeten

We hebben kanalen gemaakt in onze officiële [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) voor het ontmoeten van andere cursisten. Dit is een geweldige manier om te netwerken met andere gelijkgestemde ondernemers, bouwers, studenten en iedereen die zich wil verbeteren in Generatieve AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Het projectteam is ook aanwezig op deze Discord-server om cursisten te helpen.

## Bijdragen

Deze cursus is een open-source initiatief. Zie je verbeterpunten of problemen? Maak dan een [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) of meld een [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Het projectteam houdt alle bijdragen bij. Bijdragen aan open source is een fantastische manier om je carrière in Generatieve AI te bouwen.

De meeste bijdragen vereisen dat je instemt met een Contributor License Agreement (CLA) waarin je verklaart het recht te hebben en daadwerkelijk verleent om je bijdragen te gebruiken. Voor details, bezoek [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Belangrijk: bij het vertalen van tekst in deze repo, zorg dat je geen machinale vertalingen gebruikt. We zullen vertalingen controleren via de community, dus meldt je alleen aan voor vertalingen in talen waarin je goed bent.

Wanneer je een pull request aanmaakt, bepaalt een CLA-bot automatisch of je een CLA moet voorzien en markeert het PR overeenkomstig (bijv. label, commentaar). Volg gewoon de aanwijzingen van de bot. Je hoeft dit maar één keer te doen voor alle repositories die onze CLA gebruiken.

Dit project heeft de [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) overgenomen. Voor meer informatie lees de Code of Conduct FAQ of neem contact op via [Email opencode](opencode@microsoft.com) voor vragen of opmerkingen.

## Laten we beginnen
Nu je de benodigde stappen hebt voltooid om deze cursus te voltooien, laten we beginnen met een [introductie tot Generatieve AI en LLM's](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI- vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal geldt als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aangeraden. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->