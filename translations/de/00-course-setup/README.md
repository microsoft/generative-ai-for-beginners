# Erste Schritte mit diesem Kurs

Wir freuen uns sehr, dass du mit diesem Kurs startest und gespannt bist, was dich mit Generativer KI inspiriert zu erschaffen!

Um deinen Erfolg zu gewährleisten, beschreibt diese Seite die Einrichtungsschritte, technischen Anforderungen und wo du bei Bedarf Hilfe bekommst.

## Einrichtungsschritte

Um mit diesem Kurs zu beginnen, musst du die folgenden Schritte abschließen.

### 1. Dieses Repository forken

[Forke dieses gesamte Repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) in dein eigenes GitHub-Konto, um den Code ändern und die Aufgaben bearbeiten zu können. Du kannst auch [das Repo mit einem Stern (🌟) markieren](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), um es und verwandte Repos leichter zu finden.

### 2. Einen Codespace erstellen

Um Abhängigkeitsprobleme beim Ausführen des Codes zu vermeiden, empfehlen wir, diesen Kurs in einem [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) auszuführen.

In deinem Fork: **Code -> Codespaces -> Neu auf main**

![Dialog zeigt Buttons zum Erstellen eines Codespaces](../../../translated_images/de/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Ein Secret hinzufügen

1. ⚙️ Zahnrad-Symbol -> Befehls-Palette -> Codespaces: Benutzer-Secret verwalten -> Neues Secret hinzufügen.
2. Name OPENAI_API_KEY, Schlüssel einfügen, Speichern.

### 3. Was nun?

| Ich möchte…           | Gehe zu…                                                                |
|----------------------|-------------------------------------------------------------------------|
| Lektion 1 starten    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Offline arbeiten     | [`setup-local.md`](02-setup-local.md)                                   |
| LLM-Anbieter einrichten | [`providers.md`](03-providers.md)                                        |
| Andere Lernende treffen | [Tritt unserem Discord bei](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Problemlösung


| Symptom                                 | Lösung                                                         |
|-----------------------------------------|----------------------------------------------------------------|
| Container-Build hängt > 10 min          | **Codespaces ➜ „Container neu aufbauen“**                      |
| `python: command not found`             | Terminal wurde nicht angehängt; klicke **+** ➜ *bash*          |
| `401 Unauthorized` von OpenAI           | Falscher / abgelaufener `OPENAI_API_KEY`                        |
| VS Code zeigt „Dev container mounting…“| Browser-Tab aktualisieren – Codespaces verliert manchmal die Verbindung |
| Notebook Kernel fehlt                   | Notebook-Menü ➜ **Kernel ▸ Kernel auswählen ▸ Python 3**       |

   Unix-basierte Systeme:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Die `.env`-Datei bearbeiten**: Öffne die `.env` Datei in einem Texteditor (z. B. VS Code, Notepad++ oder einem anderen Editor). Füge folgende Zeilen hinzu und ersetze die Platzhalter mit deinem tatsächlichen Microsoft Foundry Models Endpunkt und Schlüssel (siehe [`providers.md`](03-providers.md) für Hinweise zum Erhalt):

   > **Hinweis:** GitHub-Modelle (und die Variable `GITHUB_TOKEN`) werden Ende Juli 2026 eingestellt. Nutze stattdessen [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Datei speichern**: Speichere die Änderungen und schließe den Texteditor.

5. **`python-dotenv` installieren**: Wenn du es nicht schon getan hast, musst du das Paket `python-dotenv` installieren, um Umgebungsvariablen aus der `.env` Datei in deine Python-Anwendung zu laden. Du kannst es mit `pip` installieren:

   ```bash
   pip install python-dotenv
   ```

6. **Umgebungsvariablen im Python-Skript laden**: In deinem Python-Skript nutze das Paket `python-dotenv`, um die Umgebungsvariablen aus der `.env` Datei zu laden:

   ```python
   from dotenv import load_dotenv
   import os

   # Lade Umgebungsvariablen aus der .env-Datei
   load_dotenv()

   # Greife auf die Microsoft Foundry Models Variablen zu
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Das war’s! Du hast erfolgreich eine `.env`-Datei erstellt, deine Microsoft Foundry Models Anmeldeinformationen hinzugefügt und in deine Python-Anwendung geladen.

## Wie man lokal auf deinem Computer ausführt

Um den Code lokal auf deinem Computer auszuführen, benötigst du eine installierte Version von [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Um das Repository zu verwenden, musst du es klonen:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Sobald du alles ausgecheckt hast, kannst du loslegen!

## Optionale Schritte

### Installation von Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ist ein schlanker Installer für die Installation von [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python und einigen Paketen.
Conda ist ein Paketmanager, mit dem es einfach ist, verschiedene Python [**virtuelle Umgebungen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) und Pakete einzurichten und umzuschalten. Es ist auch praktisch, um Pakete zu installieren, die nicht über `pip` verfügbar sind.

Du kannst der [Miniconda Installationsanleitung](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) folgen, um sie einzurichten.

Sobald Miniconda installiert ist, musst du das [Repository klonen](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (falls noch nicht geschehen)

Anschließend musst du eine virtuelle Umgebung erstellen. Um dies mit Conda zu tun, erstelle eine neue Umgebungsdatei (_environment.yml_). Wenn du Codespaces nutzt, lege diese Datei im Verzeichnis `.devcontainer` an, also `.devcontainer/environment.yml`.

Fülle deine Umgebungsdatei mit dem folgenden Snippet:

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

Falls Fehler bei der Nutzung von conda auftreten, kannst du die Microsoft KI-Bibliotheken manuell mit folgendem Terminalbefehl installieren.

```
conda install -c microsoft azure-ai-ml
```

Die Umgebungsdatei gibt die benötigten Abhängigkeiten an. `<environment-name>` steht für den Namen deiner Conda-Umgebung und `<python-version>` für die verwendete Python-Version, z.B. ist `3` die aktuellste Hauptversion.

Danach kannst du deine Conda-Umgebung durch Ausführen der folgenden Befehle in der Kommandozeile / im Terminal erstellen:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer Unterpfad gilt nur für Codespace-Setups
conda activate ai4beg
```

Siehe die [Conda-Umgebungsanleitung](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), falls Probleme auftreten.

### Verwendung von Visual Studio Code mit Python-Unterstützungserweiterung

Wir empfehlen für diesen Kurs den Editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) mit der installierten [Python-Unterstützungserweiterung](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst). Dies ist jedoch eine Empfehlung und keine zwingende Voraussetzung.

> **Hinweis**: Wenn du das Kurs-Repository in VS Code öffnest, kannst du das Projekt innerhalb eines Containers einrichten, da sich im Repository das spezielle `.devcontainer`-Verzeichnis befindet. Mehr dazu später.

> **Hinweis**: Sobald du das Verzeichnis klonst und in VS Code öffnest, wird automatisch vorgeschlagen, eine Python-Unterstützungserweiterung zu installieren.

> **Hinweis**: Wenn VS Code vorschlägt, das Repository in einem Container neu zu öffnen, lehne ab, um die lokal installierte Python-Version zu verwenden.

### Verwendung von Jupyter im Browser

Du kannst auch direkt im Browser mit der [Jupyter-Umgebung](https://jupyter.org?WT.mc_id=academic-105485-koreyst) arbeiten. Sowohl das klassische Jupyter als auch [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) bieten eine angenehme Entwicklungsumgebung mit Funktionen wie Autovervollständigung, Code-Hervorhebung usw.

Zum Starten von Jupyter lokal öffne das Terminal/die Kommandozeile, navigiere ins Kursverzeichnis und führe aus:

```bash
jupyter notebook
```

oder

```bash
jupyterhub
```

Dies startet eine Jupyter-Instanz und die URL zum Zugriff wird im Kommandozeilenfenster angezeigt.

Nach Zugriff auf die URL solltest du die Kursübersicht sehen und jede `*.ipynb`-Datei öffnen können, z. B. `08-building-search-applications/python/oai-solution.ipynb`.

### Ausführung in einem Container

Eine Alternative zur lokalen Einrichtung auf deinem Computer oder Codespace ist die Verwendung eines [Containers](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Der spezielle `.devcontainer`-Ordner im Kursrepo ermöglicht es VS Code, das Projekt innerhalb eines Containers einzurichten. Außerhalb von Codespaces erfordert dies die Installation von Docker und ist durchaus aufwendig, deshalb empfehlen wir diese Option nur erfahrenen Container-Nutzern.

Eine der besten Methoden, API-Schlüssel sicher zu verwahren, wenn du GitHub Codespaces nutzt, ist die Verwendung von Codespaces-Secrets. Folge bitte der [Codespaces Secrets-Verwaltungsanleitung](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), um mehr darüber zu erfahren.


## Lektionen und technische Anforderungen

Der Kurs besteht aus 6 Konzeptlektionen und 6 Programmierlektionen.

Für die Programmierlektionen verwenden wir den Azure OpenAI Service. Du benötigst Zugang zum Azure OpenAI Service und einen API-Schlüssel, um den Code auszuführen. Du kannst den Zugang beantragen, indem du [diesen Antrag ausfüllst](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Während du auf die Bearbeitung deines Antrags wartest, enthält jede Programmierlektion auch eine `README.md`-Datei, in der du den Code und die Ausgaben ansehen kannst.

## Azure OpenAI Service zum ersten Mal nutzen

Falls du zum ersten Mal mit dem Azure OpenAI Service arbeitest, folge bitte dieser Anleitung, wie du eine Ressource für den Azure OpenAI Service [erstellst und bereitstellst.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## OpenAI API zum ersten Mal nutzen

Falls du zum ersten Mal mit der OpenAI API arbeitest, folge der Anleitung, wie du die [Schnittstelle erstellst und verwendest.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Andere Lernende treffen

Wir haben Kanäle in unserem offiziellen [AI Community Discord Server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) eingerichtet, um andere Lernende zu treffen. Das ist eine großartige Möglichkeit, um sich mit anderen gleichgesinnten Unternehmern, Entwicklern, Studierenden und allen, die sich im Bereich Generative KI weiterentwickeln möchten, zu vernetzen.

[![Tritt dem Discord-Kanal bei](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Das Projektteam wird ebenfalls auf diesem Discord-Server sein, um Lernenden zu helfen.

## Mitwirken

Dieser Kurs ist eine Open-Source-Initiative. Wenn du Verbesserungsmöglichkeiten oder Probleme siehst, erstelle bitte einen [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) oder melde ein [GitHub Issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Das Projektteam wird alle Beiträge verfolgen. Zur Open-Source-Community beizutragen ist eine großartige Möglichkeit, deine Karriere im Bereich Generative KI voranzubringen.

Die meisten Beiträge erfordern, dass du einer Contributor License Agreement (CLA) zustimmst, die bestätigt, dass du berechtigt bist und tatsächlich die Rechte überträgst, uns dein Beitrag zu nutzen. Details findest du auf der [Website der CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Wichtig: Wenn du Texte in diesem Repo übersetzt, verwende bitte keine maschinelle Übersetzung. Wir werden Übersetzungen über die Community prüfen, daher melde dich bitte nur für Übersetzungen in Sprachen, in denen du wirklich bewandert bist.

Wenn du einen Pull Request einreichst, bestimmt ein CLA-Bot automatisch, ob du eine CLA vorlegen musst und kennzeichnet den PR entsprechend (z. B. Label, Kommentar). Folge einfach den Anweisungen des Bots. Dies musst du nur einmal für alle Repositories erledigen, die unsere CLA verwenden.


Dieses Projekt hat den [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) übernommen. Für weitere Informationen lesen Sie die FAQ zum Verhaltenskodex oder kontaktieren Sie [Email opencode](opencode@microsoft.com) bei weiteren Fragen oder Anmerkungen.

## Lassen Sie uns anfangen

Da Sie nun die erforderlichen Schritte zum Abschluss dieses Kurses abgeschlossen haben, beginnen wir mit einer [Einführung in Generative KI und LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->