<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00f2643fec1571acc5d38cc1a3b972d5",
  "translation_date": "2025-07-09T06:58:45+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "de"
}
-->
# Erste Schritte mit diesem Kurs

Wir freuen uns sehr, dass du mit diesem Kurs startest und gespannt bist, was du mit Generativer KI erschaffen wirst!

Um deinen Erfolg sicherzustellen, findest du auf dieser Seite die Einrichtungsschritte, technischen Anforderungen und Hinweise, wo du bei Bedarf Hilfe bekommst.

## Einrichtungsschritte

Um mit diesem Kurs zu beginnen, musst du die folgenden Schritte abschließen.

### 1. Forke dieses Repository

[Forke dieses gesamte Repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) in dein eigenes GitHub-Konto, um den Code ändern und die Herausforderungen bearbeiten zu können. Du kannst dieses Repository auch [mit einem Stern (🌟) markieren](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), um es und verwandte Repos leichter wiederzufinden.

### 2. Erstelle einen Codespace

Um Abhängigkeitsprobleme beim Ausführen des Codes zu vermeiden, empfehlen wir, diesen Kurs in einem [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) auszuführen.

Diesen kannst du erstellen, indem du in deiner geforkten Version des Repos die Option `Code` auswählst und dann die **Codespaces**-Option anklickst.

![Dialog mit Buttons zur Erstellung eines Codespaces](../../../00-course-setup/images/who-will-pay.webp)

### 3. Speichern deiner API-Schlüssel

Es ist wichtig, deine API-Schlüssel sicher aufzubewahren, wenn du Anwendungen entwickelst. Wir empfehlen, keine API-Schlüssel direkt im Code zu speichern. Das Hochladen solcher Daten in ein öffentliches Repository kann zu Sicherheitsproblemen und unerwünschten Kosten führen, falls sie von Dritten missbraucht werden.
Hier eine Schritt-für-Schritt-Anleitung, wie du eine `.env`-Datei für Python erstellst und den `GITHUB_TOKEN` hinzufügst:

1. **Navigiere zu deinem Projektverzeichnis**: Öffne dein Terminal oder die Eingabeaufforderung und wechsle in das Stammverzeichnis deines Projekts, in dem du die `.env`-Datei erstellen möchtest.

   ```bash
   cd path/to/your/project
   ```

2. **Erstelle die `.env`-Datei**: Erstelle mit deinem bevorzugten Texteditor eine neue Datei namens `.env`. Wenn du die Kommandozeile nutzt, kannst du `touch` (unter Unix-Systemen) oder `echo` (unter Windows) verwenden:

   Unix-Systeme:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Bearbeite die `.env`-Datei**: Öffne die `.env`-Datei in einem Texteditor (z. B. VS Code, Notepad++ oder einem anderen Editor). Füge folgende Zeile hinzu und ersetze `your_github_token_here` durch deinen tatsächlichen GitHub-Token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Speichere die Datei**: Speichere die Änderungen und schließe den Editor.

5. **Installiere `python-dotenv`**: Falls noch nicht geschehen, installiere das Paket `python-dotenv`, um Umgebungsvariablen aus der `.env`-Datei in deine Python-Anwendung zu laden. Du kannst es mit `pip` installieren:

   ```bash
   pip install python-dotenv
   ```

6. **Lade Umgebungsvariablen in deinem Python-Skript**: Verwende in deinem Python-Skript das Paket `python-dotenv`, um die Umgebungsvariablen aus der `.env`-Datei zu laden:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Das war’s! Du hast erfolgreich eine `.env`-Datei erstellt, deinen GitHub-Token hinzugefügt und in deine Python-Anwendung geladen.

## Lokales Ausführen auf deinem Computer

Um den Code lokal auf deinem Computer auszuführen, benötigst du eine installierte Version von [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Um das Repository zu nutzen, musst du es klonen:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Sobald du alles ausgecheckt hast, kannst du loslegen!

## Optionale Schritte

### Installation von Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ist ein schlanker Installer für die Installation von [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python und einigen Paketen.
Conda ist ein Paketmanager, der es einfach macht, verschiedene Python [**virtuelle Umgebungen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) und Pakete einzurichten und zwischen ihnen zu wechseln. Außerdem ist es praktisch, um Pakete zu installieren, die nicht über `pip` verfügbar sind.

Du kannst der [Miniconda-Installationsanleitung](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) folgen, um es einzurichten.

Nach der Installation von Miniconda musst du das [Repository klonen](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (falls noch nicht geschehen).

Als Nächstes erstellst du eine virtuelle Umgebung. Erstelle dazu eine neue Umgebungsdatei (_environment.yml_). Wenn du Codespaces verwendest, lege diese im `.devcontainer`-Verzeichnis an, also `.devcontainer/environment.yml`.

Fülle deine Umgebungsdatei mit folgendem Snippet:

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

Falls du Fehler bei der Verwendung von conda bekommst, kannst du die Microsoft AI Libraries manuell mit folgendem Befehl im Terminal installieren:

```
conda install -c microsoft azure-ai-ml
```

Die Umgebungsdatei gibt die benötigten Abhängigkeiten an. `<environment-name>` steht für den Namen deiner Conda-Umgebung, und `<python-version>` für die Python-Version, die du verwenden möchtest, z. B. `3` für die aktuelle Hauptversion.

Anschließend kannst du deine Conda-Umgebung mit den folgenden Befehlen in der Kommandozeile/Terminal erstellen:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Bei Problemen hilft dir die [Conda-Umgebungsanleitung](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) weiter.

### Verwendung von Visual Studio Code mit der Python-Erweiterung

Für diesen Kurs empfehlen wir den Editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) mit der installierten [Python-Erweiterung](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst). Dies ist jedoch nur eine Empfehlung und keine zwingende Voraussetzung.

> **Hinweis**: Wenn du das Kurs-Repository in VS Code öffnest, kannst du das Projekt innerhalb eines Containers einrichten. Das ist möglich dank des [speziellen `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)-Verzeichnisses im Kurs-Repository. Mehr dazu später.

> **Hinweis**: Sobald du das Verzeichnis in VS Code klonst und öffnest, wird dir automatisch vorgeschlagen, die Python-Erweiterung zu installieren.

> **Hinweis**: Wenn VS Code vorschlägt, das Repository in einem Container neu zu öffnen, lehne dies ab, wenn du die lokal installierte Python-Version verwenden möchtest.

### Verwendung von Jupyter im Browser

Du kannst auch direkt im Browser mit der [Jupyter-Umgebung](https://jupyter.org?WT.mc_id=academic-105485-koreyst) arbeiten. Sowohl das klassische Jupyter als auch [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) bieten eine angenehme Entwicklungsumgebung mit Funktionen wie Autovervollständigung, Syntaxhervorhebung usw.

Um Jupyter lokal zu starten, öffne das Terminal/die Eingabeaufforderung, navigiere in das Kursverzeichnis und führe aus:

```bash
jupyter notebook
```

oder

```bash
jupyterhub
```

Dadurch wird eine Jupyter-Instanz gestartet, und die URL zum Zugriff wird im Terminal angezeigt.

Wenn du die URL öffnest, solltest du die Kursübersicht sehen und zu jeder `*.ipynb`-Datei navigieren können, z. B. `08-building-search-applications/python/oai-solution.ipynb`.

### Ausführen in einem Container

Eine Alternative zur Einrichtung auf deinem Computer oder Codespace ist die Verwendung eines [Containers](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Das spezielle `.devcontainer`-Verzeichnis im Kurs-Repository ermöglicht es VS Code, das Projekt innerhalb eines Containers einzurichten. Außerhalb von Codespaces erfordert dies die Installation von Docker und ist etwas aufwändiger, daher empfehlen wir dies nur erfahrenen Nutzern mit Container-Erfahrung.

Eine der besten Methoden, um deine API-Schlüssel bei der Nutzung von GitHub Codespaces sicher zu halten, ist die Verwendung von Codespace Secrets. Bitte folge der Anleitung zur [Codespaces Secrets-Verwaltung](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), um mehr darüber zu erfahren.

## Lektionen und technische Anforderungen

Der Kurs besteht aus 6 Konzept-Lektionen und 6 Programmier-Lektionen.

Für die Programmier-Lektionen verwenden wir den Azure OpenAI Service. Du benötigst Zugriff auf den Azure OpenAI Service und einen API-Schlüssel, um den Code auszuführen. Du kannst den Zugriff beantragen, indem du [diesen Antrag ausfüllst](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Während du auf die Bearbeitung deines Antrags wartest, enthält jede Programmier-Lektion auch eine `README.md`-Datei, in der du den Code und die Ergebnisse ansehen kannst.

## Erster Umgang mit dem Azure OpenAI Service

Wenn du zum ersten Mal mit dem Azure OpenAI Service arbeitest, folge bitte dieser Anleitung, wie du eine [Azure OpenAI Service-Ressource erstellst und bereitstellst.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Erster Umgang mit der OpenAI API

Wenn du zum ersten Mal mit der OpenAI API arbeitest, folge der Anleitung, wie du die [Schnittstelle erstellst und nutzt.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Andere Lernende kennenlernen

Wir haben Kanäle in unserem offiziellen [AI Community Discord-Server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) eingerichtet, um andere Lernende zu treffen. Das ist eine großartige Möglichkeit, sich mit gleichgesinnten Unternehmern, Entwicklern, Studierenden und allen, die sich im Bereich Generative KI weiterentwickeln wollen, zu vernetzen.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Das Projektteam ist ebenfalls auf diesem Discord-Server, um Lernenden zu helfen.

## Mitwirken

Dieser Kurs ist ein Open-Source-Projekt. Wenn du Verbesserungsmöglichkeiten oder Probleme entdeckst, erstelle bitte einen [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) oder melde ein [GitHub-Issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Das Projektteam verfolgt alle Beiträge. Beiträge zu Open Source sind eine großartige Möglichkeit, deine Karriere im Bereich Generative KI voranzutreiben.

Die meisten Beiträge erfordern, dass du einer Contributor License Agreement (CLA) zustimmst, die bestätigt, dass du die Rechte hast und tatsächlich gewährst, dass wir deine Beiträge nutzen dürfen. Details findest du auf der [CLA-Website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Wichtig: Bitte verwende bei der Übersetzung von Texten in diesem Repository keine maschinelle Übersetzung. Wir überprüfen Übersetzungen über die Community, daher solltest du nur Übersetzungen in Sprachen anbieten, in denen du sicher bist.

Wenn du einen Pull Request einreichst, prüft ein CLA-Bot automatisch, ob du eine CLA bereitstellen musst, und versieht den PR entsprechend (z. B. mit Label oder Kommentar). Folge einfach den Anweisungen des Bots. Dies musst du nur einmal für alle Repositories mit unserer CLA tun.

Dieses Projekt hat den [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) übernommen. Weitere Informationen findest du in den FAQ zum Verhaltenskodex oder kontaktiere [Email opencode](opencode@microsoft.com) bei Fragen oder Anmerkungen.

## Lass uns starten

Nachdem du die notwendigen Schritte abgeschlossen hast, können wir loslegen mit einer [Einführung in Generative KI und LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.