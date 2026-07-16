# Aan de slag met deze cursus

We zijn erg enthousiast dat je met deze cursus begint en benieuwd bent wat je geïnspireerd raakt te bouwen met Generatieve AI!

Om je succes te verzekeren, geeft deze pagina overzicht van de installatiestappen, technische vereisten en waar je hulp kunt krijgen indien nodig.

## Installatiestappen

Om te beginnen met deze cursus, moet je de volgende stappen voltooien.

### 1. Fork deze Repo

[Fork deze gehele repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) naar je eigen GitHub-account om elke code te kunnen wijzigen en de uitdagingen te voltooien. Je kunt ook [deze repo een ster (🌟) geven](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) om het en gerelateerde repos gemakkelijker terug te vinden.

### 2. Maak een codespace aan

Om afhankelijkheidsproblemen bij het uitvoeren van de code te vermijden, raden we aan deze cursus te draaien in een [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

In je fork: **Code -> Codespaces -> New on main**

![Dialoogvenster toont knoppen om een codespace te maken](../../../translated_images/nl/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Voeg een geheim toe

1. ⚙️ Tandwiel-icoon -> Command Pallete -> Codespaces : Manage user secret -> Voeg een nieuw geheim toe.
2. Naam OPENAI_API_KEY, plak je sleutel, opslaan.

### 3. Wat nu?

| Ik wil…           | Ga naar…                                                                 |
|-------------------|-------------------------------------------------------------------------|
| Les 1 starten      | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Offline werken    | [`setup-local.md`](02-setup-local.md)                                   |
| Een LLM-provider instellen | [`providers.md`](03-providers.md)                                        |
| Andere cursisten ontmoeten | [Doe mee aan onze Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Problemen oplossen


| Symptoom                                 | Oplossing                                                       |
|-----------------------------------------|-----------------------------------------------------------------|
| Container bouwen blijft > 10 min hangen | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`              | Terminal niet gekoppeld; klik **+** ➜ *bash*                    |
| `401 Unauthorized` van OpenAI            | Verkeerde/verlopen `OPENAI_API_KEY`                             |
| VS Code toont “Dev container mounting…”  | Vernieuw het browsertabblad—Codespaces verliest soms verbinding |
| Notebook kernel ontbreekt                | Notebookmenu ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Unix-gebaseerde systemen:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Bewerk het `.env`-bestand**: Open het `.env`-bestand in een teksteditor (bijv. VS Code, Notepad++ of een andere editor). Voeg de volgende regels toe aan het bestand, waarbij je de plaatsaanduidingen vervangt door je daadwerkelijke Microsoft Foundry Models-eindpunt en sleutel (zie [`providers.md`](03-providers.md) voor hoe je deze krijgt):

   > **Opmerking:** GitHub Models (en zijn `GITHUB_TOKEN`-variabele) wordt uitgefaseerd eind juli 2026. Gebruik in plaats daarvan [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Bewaar het bestand**: Sla de wijzigingen op en sluit de teksteditor.

5. **Installeer `python-dotenv`**: Als je het nog niet hebt gedaan, moet je de `python-dotenv`-package installeren om omgevingsvariabelen uit het `.env`-bestand in je Python-applicatie te laden. Je kunt het installeren met `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Laad omgevingsvariabelen in je Python-script**: Gebruik in je Python-script de `python-dotenv`-package om de omgevingsvariabelen uit het `.env`-bestand te laden:

   ```python
   from dotenv import load_dotenv
   import os

   # Laad omgevingsvariabelen uit .env-bestand
   load_dotenv()

   # Toegang tot de Microsoft Foundry Models variabelen
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Dat is het! Je hebt succesvol een `.env`-bestand aangemaakt, je Microsoft Foundry Models-gegevens toegevoegd en ze in je Python-applicatie geladen.

## Hoe lokaal op je computer te draaien

Om de code lokaal op je computer te draaien, moet je een versie van [Python geïnstalleerd hebben](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Om de repository daarna te gebruiken, moet je deze klonen:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Zodra je alles hebt gekloond, kun je aan de slag!

## Optionele stappen

### Miniconda installeren

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) is een lichte installer voor het installeren van [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python en enkele pakketten.
Conda zelf is een package manager die het makkelijk maakt om verschillende Python [**virtuele omgevingen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) en pakketten op te zetten en er tussen te wisselen. Het is ook handig voor het installeren van pakketten die niet via `pip` beschikbaar zijn.

Je kunt de [MiniConda installatiewijzer](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) volgen om het op te zetten.

Met Miniconda geïnstalleerd, moet je de [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) klonen (als je dat nog niet gedaan hebt).

Vervolgens moet je een virtuele omgeving aanmaken. Maak hiervoor een nieuw omgevingsbestand aan (_environment.yml_). Als je de cursus via Codespaces volgt, maak dit bestand dan in de `.devcontainer` directory, dus `.devcontainer/environment.yml`.

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

Als je problemen krijgt met conda, kun je handmatig de Microsoft AI Libraries installeren via het volgende commando in een terminal.

```
conda install -c microsoft azure-ai-ml
```

Het omgevingsbestand specificeert de benodigde afhankelijkheden. `<environment-name>` is de naam die je wilt gebruiken voor je Conda-omgeving, en `<python-version>` is de versie van Python die je wilt gebruiken, bijvoorbeeld `3` is de nieuwste grote versie van Python.

Als dit klaar is, kun je je Conda-omgeving aanmaken door onderstaande commando’s in je command line/terminal uit te voeren.

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer-subpad geldt alleen voor Codespace-configuraties
conda activate ai4beg
```

Raadpleeg de [Conda-omgevingen gids](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) als je problemen ondervindt.

### Visual Studio Code gebruiken met de Python support extensie

We raden aan de editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) te gebruiken met de [Python support extensie](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) geïnstalleerd voor deze cursus. Dit is echter meer een aanbeveling dan een strikte vereiste.

> **Opmerking**: Door de cursusrepository in VS Code te openen, kun je het project binnen een container opzetten. Dit is mogelijk dankzij de [speciale `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) map binnen de repository. Hierover later meer.

> **Opmerking**: Zodra je de directory kloont en opent in VS Code, zal het automatisch een suggestie geven om een Python support extensie te installeren.

> **Opmerking**: Als VS Code voorstelt de repository opnieuw in een container te openen, wees dan terughoudend om dat te accepteren zodat je de lokaal geïnstalleerde Python-versie kunt gebruiken.

### Jupyter in de browser gebruiken

Je kunt ook in de browser werken aan het project met de [Jupyter omgeving](https://jupyter.org?WT.mc_id=academic-105485-koreyst). Zowel klassieke Jupyter als [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) bieden een prettige ontwikkelomgeving met functies zoals automatische voltooiing, code-kleuring, enzovoort.

Om lokaal Jupyter te starten, ga je naar de terminal/command line, navigeer je naar de cursusdirectory, en voer je uit:

```bash
jupyter notebook
```

of

```bash
jupyterhub
```

Dit start een Jupyter-instantie en de URL om deze te openen wordt in het commandline-venster weergegeven.

Als je de URL opent, zie je de cursusopzet en kun je naar elk `*.ipynb`-bestand navigeren. Bijvoorbeeld, `08-building-search-applications/python/oai-solution.ipynb`.

### Draaien in een container

Een alternatief om alles op je computer of Codespace op te zetten, is het gebruik van een [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). De speciale `.devcontainer`-map binnen de cursusrepository maakt het mogelijk voor VS Code om het project binnen een container te zetten. Buiten Codespaces vereist dit de installatie van Docker, en eerlijk gezegd kost het wat werk, dus we bevelen dit alleen aan voor wie ervaring heeft met containers.

Eén van de beste manieren om je API-sleutels veilig te houden bij gebruik van GitHub Codespaces is door gebruik te maken van Codespace Secrets. Volg de [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) gids om hier meer over te leren.


## Lessen en technische vereisten

De cursus heeft "Learn"-lessen die de concepten van Generatieve AI uitleggen en "Build"-lessen met praktische codevoorbeelden in zowel **Python** als **TypeScript** waar mogelijk.

Voor de codeerlessen gebruiken we Azure OpenAI in Microsoft Foundry. Je hebt een Azure-abonnement en een API-sleutel nodig. Toegang is open - geen aanvraag vereist - dus je kunt een [Microsoft Foundry-bron maken en een model implementeren](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) om je eindpunt en sleutel te krijgen.

Elke codeerles bevat ook een `README.md` waarin je de code en resultaten kunt bekijken zonder iets uit te voeren.

## Voor de eerste keer de Azure OpenAI-service gebruiken

Als je voor het eerst met de Azure OpenAI service werkt, volg dan deze gids over hoe je een [Azure OpenAI Service-bron maakt en implementeert.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Voor de eerste keer de OpenAI API gebruiken

Als je voor het eerst met de OpenAI API werkt, volg dan de gids over hoe je [de interface maakt en gebruikt.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Ontmoet andere cursisten

We hebben kanalen gemaakt in onze officiële [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) om andere cursisten te ontmoeten. Dit is een geweldige manier om te netwerken met andere gelijkgestemde ondernemers, bouwers, studenten en iedereen die zich wil ontwikkelen in Generatieve AI.

[![Doe mee met Discord-kanaal](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Het projectteam zal ook op deze Discord-server aanwezig zijn om cursisten te helpen.

## Bijdragen

Deze cursus is een open-source initiatief. Als je verbeterpunten of problemen ziet, maak dan een [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) aan of log een [GitHub-issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Het projectteam zal alle bijdragen volgen. Bijdragen aan open source is een geweldige manier om je carrière in Generatieve AI uit te bouwen.

De meeste bijdragen vereisen dat je instemt met een Contributor License Agreement (CLA) waarin je verklaart dat je het recht hebt en daadwerkelijk toestaat dat wij jouw bijdrage mogen gebruiken. Voor details bezoek [CLA, Contributor License Agreement website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Belangrijk: bij het vertalen van tekst in deze repo, zorg er alsjeblieft voor dat je geen machinevertaling gebruikt. Wij zullen vertalingen via de community verifiëren, dus meld je alleen aan om te vertalen in talen waarin je bekwaam bent.


Wanneer je een pull request indient, bepaalt een CLA-bot automatisch of je een CLA moet aanleveren en voorziet het PR van de juiste decoratie (bijv. label, commentaar). Volg gewoon de instructies van de bot. Dit hoef je maar één keer te doen voor alle repositories die onze CLA gebruiken.

Dit project heeft de [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) overgenomen. Voor meer informatie, lees de Code of Conduct FAQ of neem contact op met [Email opencode](opencode@microsoft.com) voor aanvullende vragen of opmerkingen.

## Laten we beginnen

Nu je de benodigde stappen hebt voltooid om deze cursus af te ronden, laten we beginnen met een [introductie tot Generative AI en LLM's](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->