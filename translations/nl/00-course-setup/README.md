# Aan de slag met deze cursus

We zijn erg blij dat je met deze cursus begint en benieuwd wat je geïnspireerd raakt om te bouwen met Generatieve AI!

Om je succes te garanderen, beschrijft deze pagina de installatie-stappen, technische vereisten en waar je hulp kunt krijgen indien nodig.

## Installatiestappen

Om met deze cursus te beginnen, moet je de volgende stappen voltooien.

### 1. Fork deze repo

[Fork deze hele repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) naar je eigen GitHub-account zodat je de code kunt wijzigen en de opdrachten kunt maken. Je kunt ook [deze repo een ⭐ geven](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) om hem en gerelateerde repositories gemakkelijker terug te vinden.

### 2. Maak een codespace aan

Om dependency-problemen bij het uitvoeren van de code te voorkomen, raden we aan deze cursus te draaien in een [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

In jouw fork: **Code -> Codespaces -> New on main**

![Dialoog scherm met knoppen om een codespace aan te maken](../../../translated_images/nl/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Voeg een secret toe

1. ⚙️ Tandwiel-icoon -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Noem het OPENAI_API_KEY, plak je sleutel, Sla op.

### 3. Wat nu?

| Ik wil…             | Ga naar…                                                              |
|---------------------|----------------------------------------------------------------------|
| Les 1 starten       | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)  |
| Offline werken      | [`setup-local.md`](02-setup-local.md)                                |
| Een LLM-provider instellen | [`providers.md`](03-providers.md)                                     |
| Andere deelnemers ontmoeten | [Word lid van onze Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)  |

## Problemen oplossen


| Symptom                                  | Oplossing                                                      |
|------------------------------------------|----------------------------------------------------------------|
| Container build blijft langer dan 10 min hangen | **Codespaces ➜ “Rebuild Container”**                       |
| `python: command not found`              | Terminal is niet verbonden; klik op **+** ➜ *bash*             |
| `401 Unauthorized` van OpenAI            | Verkeerde / verlopen `OPENAI_API_KEY`                        |
| VS Code toont “Dev container mounting…” | Vernieuw het browsertabblad—Codespaces verliest soms verbinding |
| Notebook kernel ontbreekt                 | Notebookmenu ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

   Unix-gebaseerde systemen:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Bewerk het `.env` bestand**: Open het `.env` bestand in een teksteditor (bijv. VS Code, Notepad++ of een andere editor). Voeg de volgende regels toe en vervang de placeholders door jouw daadwerkelijke Microsoft Foundry Models endpoint en sleutel (zie [`providers.md`](03-providers.md) voor hoe je deze krijgt):

   > **Opmerking:** GitHub Models (en de variabele `GITHUB_TOKEN`) wordt beëindigd eind juli 2026. Gebruik in plaats daarvan [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Sla het bestand op**: Bewaar de wijzigingen en sluit de teksteditor.

5. **Installeer `python-dotenv`**: Indien nog niet geïnstalleerd, moet je de `python-dotenv` package installeren om omgevingsvariabelen uit het `.env` bestand in je Python-applicatie te laden. Dit kun je doen met `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Laad omgevingsvariabelen in je Python-script**: Gebruik in je Python-script de `python-dotenv` package om de omgevingsvariabelen uit het `.env` bestand te laden:

   ```python
   from dotenv import load_dotenv
   import os

   # Laad omgevingsvariabelen uit het .env-bestand
   load_dotenv()

   # Toegang tot de Microsoft Foundry Models variabelen
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Dat is het! Je hebt succesvol een `.env` bestand aangemaakt, jouw Microsoft Foundry Models inloggegevens toegevoegd en deze in je Python-applicatie geladen.

## Hoe lokaal op je computer te draaien

Om de code lokaal op je computer te draaien, moet je een versie van [Python geïnstalleerd hebben](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Om vervolgens de repository te gebruiken, moet je deze klonen:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Zodra alles is uitgecheckt, kun je beginnen!

## Optionele stappen

### Miniconda installeren

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) is een lichte installer voor het installeren van [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python en een paar packages.
Conda zelf is een package manager die het gemakkelijk maakt om verschillende Python [**virtuele omgevingen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) en packages te beheren. Ook is het handig om packages te installeren die niet beschikbaar zijn via `pip`.

Je kunt de [MiniConda installatiehandleiding](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) volgen om het in te stellen.

Met Miniconda geïnstalleerd moet je de [repository klonen](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (indien nog niet gedaan)

Daarna moet je een virtuele omgeving aanmaken. Dit doe je met Conda door een nieuwe environment file te maken (_environment.yml_). Als je dit volgt in Codespaces, maak dit dan aan in de `.devcontainer` directory, dus `.devcontainer/environment.yml`.

Vul je environment-bestand met onderstaande snippet:

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

Mocht je fouten krijgen bij het gebruik van conda, dan kun je de Microsoft AI Bibliotheken handmatig installeren met het volgende commando in een terminal.

```
conda install -c microsoft azure-ai-ml
```

Het environment-bestand specificeert de benodigde afhankelijkheden. `<environment-name>` is de naam die je wilt geven aan je Conda-omgeving, en `<python-version>` is de gewenste Python-versie, bijvoorbeeld `3` als de nieuwste hoofdversie van Python.

Als dat klaar is, kun je de Conda-omgeving aanmaken door onderstaande commando's uit te voeren in de command line/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer subpad is alleen van toepassing op Codespace-installaties
conda activate ai4beg
```

Raadpleeg de [Conda environments gids](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) als je problemen ondervindt.

### Visual Studio Code gebruiken met de Python extension

We raden aan de [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) editor te gebruiken met de [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) geïnstalleerd voor deze cursus. Dit is echter een aanbeveling en geen harde vereiste.

> **Opmerking**: Door de cursusrepository in VS Code te openen, kun je het project binnen een container opzetten. Dit komt doordat er een speciale [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) map in de cursusrepository staat. Hier komen we later op terug.

> **Opmerking**: Nadat je de map hebt gekloond en geopend in VS Code, zal VS Code automatisch aanraden om een Python-support extensie te installeren.

> **Opmerking**: Als VS Code suggereert de repository opnieuw in een container te openen, wees dan niet akkoord om de lokaal geïnstalleerde Python te gebruiken.

### Jupyter gebruiken in de browser

Je kunt ook aan het project werken met de [Jupyter omgeving](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direct in je browser. Zowel klassieke Jupyter als [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) bieden een fijne ontwikkelomgeving met functies als auto-aanvullen, code-markering, etc.

Start Jupyter lokaal op door in de terminal/command line naar de cursusmap te gaan en uit te voeren:

```bash
jupyter notebook
```

of

```bash
jupyterhub
```

Dit start een Jupyter instance en de URL om toegang te krijgen wordt in het command line venster getoond.

Eenmaal toegang tot de URL, zie je de cursusstructuur en kun je naar elk `*.ipynb` bestand navigeren, bijvoorbeeld `08-building-search-applications/python/oai-solution.ipynb`.

### Draaien in een container

Een alternatief voor het installeren op je computer of Codespace is het gebruik van een [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). De speciale `.devcontainer` map in de cursusrepository maakt het mogelijk voor VS Code om het project binnen een container op te zetten. Buiten Codespaces is dan installatie van Docker vereist; dit kan wat werk zijn, dus we raden dit alleen aan voor wie ervaring heeft met containers.

Eén van de beste manieren om je API-sleutels veilig te houden bij het gebruik van GitHub Codespaces is via Codespace Secrets. Volg de [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) handleiding om meer te leren.


## Lessen en technische vereisten

De cursus heeft 6 conceptlessen en 6 codeerlessen.

Voor de codeerlessen gebruiken we de Azure OpenAI Service. Je hebt toegang tot deze service en een API-sleutel nodig om de code uit te voeren. Je kunt toegang aanvragen door [deze aanvraag in te vullen](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Terwijl je aanvraag verwerkt wordt, bevat elke codeerles ook een `README.md` bestand waar je de code en resultaten kunt bekijken.

## Voor het eerst Azure OpenAI Service gebruiken

Als je voor het eerst met Azure OpenAI Service werkt, volg dan deze gids om een [Azure OpenAI Service resource te maken en uit te rollen.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Voor het eerst OpenAI API gebruiken

Als je voor het eerst met de OpenAI API werkt, volg dan de gids om de [Interface aan te maken en te gebruiken.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Andere deelnemers ontmoeten

We hebben kanalen gecreëerd in onze officiële [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) voor het ontmoeten van andere deelnemers. Dit is een goede manier om te netwerken met andere gelijkgestemde ondernemers, ontwikkelaars, studenten en iedereen die zich wil ontwikkelen in Generatieve AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Het projectteam is ook op deze Discord-server om deelnemers te helpen.

## Bijdragen

Deze cursus is een open-source initiatief. Als je verbetermogelijkheden of problemen ziet, maak dan een [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) aan of log een [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Het projectteam volgt alle bijdragen op. Bijdragen aan open source is een geweldige manier om je carrière in Generatieve AI op te bouwen.

De meeste bijdragen vereisen dat je instemt met een Contributor License Agreement (CLA) waarin je verklaart dat je het recht hebt en de rechten verleent om je bijdrage te gebruiken. Voor details, zie [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Belangrijk: bij het vertalen van tekst in deze repo, zorg er alsjeblieft voor dat je geen machinevertaling gebruikt. We zullen vertalingen door de community laten verifiëren, dus bied alleen vertalingen aan in talen waarin je bekwaam bent.

Wanneer je een pull request indient, bepaalt een CLA-bot automatisch of je een CLA moet aanleveren en voorziet de PR van de juiste markering (bijv. label, commentaar). Volg eenvoudig de instructies van de bot. Dit hoef je maar één keer te doen voor alle repositories die onze CLA gebruiken.


Dit project heeft de [Microsoft Open Source Gedragscode](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) aangenomen. Voor meer informatie lees de FAQ over de Gedragscode of neem contact op met [Email opencode](opencode@microsoft.com) voor aanvullende vragen of opmerkingen.

## Laten we beginnen

Nu je de benodigde stappen hebt voltooid om deze cursus te voltooien, laten we beginnen met een [inleiding tot Generative AI en LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->