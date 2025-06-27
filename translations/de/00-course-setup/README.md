<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-06-25T08:35:08+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "de"
}
-->
# Erste Schritte mit diesem Kurs

Wir freuen uns sehr, dass Sie diesen Kurs beginnen und sehen, was Sie mit Generativer KI inspiriert zu bauen!

Um Ihren Erfolg sicherzustellen, beschreibt diese Seite die Einrichtungsschritte, technischen Anforderungen und wo Sie bei Bedarf Hilfe erhalten können.

## Einrichtungsschritte

Um mit diesem Kurs zu beginnen, müssen Sie die folgenden Schritte abschließen.

### 1. Forken Sie dieses Repository

[Forken Sie dieses gesamte Repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) in Ihr eigenes GitHub-Konto, um jeglichen Code ändern und die Herausforderungen abschließen zu können. Sie können dieses Repository auch [mit einem Stern (🌟) markieren](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), um es und verwandte Repos leichter zu finden.

### 2. Erstellen Sie einen Codespace

Um Abhängigkeitsprobleme beim Ausführen des Codes zu vermeiden, empfehlen wir, diesen Kurs in einem [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) auszuführen.

Dies kann erstellt werden, indem Sie die Option `Code` in Ihrer geforkten Version dieses Repos auswählen und die Option **Codespaces** auswählen.

![Dialogfeld mit Schaltflächen zum Erstellen eines Codespace](../../../00-course-setup/images/who-will-pay.webp)

### 3. Speichern Ihrer API-Schlüssel

Es ist wichtig, Ihre API-Schlüssel sicher und geschützt zu halten, wenn Sie eine Art von Anwendung erstellen. Wir empfehlen, keine API-Schlüssel direkt in Ihrem Code zu speichern. Das Einreichen dieser Details in ein öffentliches Repository könnte Sicherheitsprobleme verursachen und sogar unerwünschte Kosten verursachen, wenn sie von einem böswilligen Akteur verwendet werden.
Hier ist eine Schritt-für-Schritt-Anleitung, wie Sie eine `.env`-Datei für Python erstellen und die `GITHUB_TOKEN` hinzufügen:

1. **Navigieren Sie zu Ihrem Projektverzeichnis**: Öffnen Sie Ihr Terminal oder die Eingabeaufforderung und navigieren Sie zum Stammverzeichnis Ihres Projekts, in dem Sie die `.env`-Datei erstellen möchten.

   ```bash
   cd path/to/your/project
   ```

2. **Erstellen Sie die `.env`-Datei**: Verwenden Sie Ihren bevorzugten Texteditor, um eine neue Datei namens `.env` zu erstellen. Wenn Sie die Befehlszeile verwenden, können Sie `touch` (on Unix-based systems) or `echo` (unter Windows) verwenden:

   Unix-basierte Systeme:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Bearbeiten Sie die `.env`-Datei**: Öffnen Sie die `.env`-Datei in einem Texteditor (z. B. VS Code, Notepad++ oder einem anderen Editor). Fügen Sie die folgende Zeile in die Datei ein und ersetzen Sie `your_github_token_here` durch Ihren tatsächlichen GitHub-Token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Speichern Sie die Datei**: Speichern Sie die Änderungen und schließen Sie den Texteditor.

5. **Installieren Sie das `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv`-Paket, um Umgebungsvariablen aus der `.env`-Datei in Ihre Python-Anwendung zu laden. Sie können es mit `pip` installieren:

   ```bash
   pip install python-dotenv
   ```

6. **Laden Sie Umgebungsvariablen in Ihr Python-Skript**: Verwenden Sie in Ihrem Python-Skript das `python-dotenv`-Paket, um die Umgebungsvariablen aus der `.env`-Datei zu laden:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Das war's! Sie haben erfolgreich eine `.env`-Datei erstellt, Ihren GitHub-Token hinzugefügt und ihn in Ihre Python-Anwendung geladen.

## Wie man lokal auf Ihrem Computer ausführt

Um den Code lokal auf Ihrem Computer auszuführen, benötigen Sie eine Version von [Python installiert](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Um dann das Repository zu verwenden, müssen Sie es klonen:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Sobald Sie alles ausgecheckt haben, können Sie loslegen!

## Optionale Schritte

### Miniconda installieren

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ist ein leichtgewichtiger Installer für die Installation von [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python sowie einigen wenigen Paketen.
Conda selbst ist ein Paketmanager, der es einfach macht, zwischen verschiedenen Python [**virtuellen Umgebungen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) und Paketen zu wechseln. Es ist auch nützlich für die Installation von Paketen, die nicht über `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml` verfügbar sind.

Füllen Sie Ihre Umgebungsdatei mit dem unten stehenden Snippet:

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

Wenn Sie beim Verwenden von conda Fehler erhalten, können Sie die Microsoft AI Libraries manuell mit dem folgenden Befehl in einem Terminal installieren.

```
conda install -c microsoft azure-ai-ml
```

Die Umgebungsdatei gibt die Abhängigkeiten an, die wir benötigen. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` ist die neueste Hauptversion von Python.

Damit können Sie Ihre Conda-Umgebung erstellen, indem Sie die folgenden Befehle in Ihrer Befehlszeile/Terminal ausführen

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Siehe den [Conda-Umgebungsleitfaden](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), wenn Sie auf Probleme stoßen.

### Verwenden von Visual Studio Code mit der Python-Unterstützungserweiterung

Wir empfehlen die Verwendung des [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) Editors mit der [Python-Unterstützungserweiterung](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) für diesen Kurs. Dies ist jedoch eher eine Empfehlung und keine zwingende Anforderung.

> **Hinweis**: Durch das Öffnen des Kurs-Repositories in VS Code haben Sie die Möglichkeit, das Projekt innerhalb eines Containers einzurichten. Dies liegt an dem [speziellen `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) Verzeichnis, das sich im Kurs-Repository befindet. Mehr dazu später.

> **Hinweis**: Sobald Sie das Verzeichnis in VS Code klonen und öffnen, wird Ihnen automatisch vorgeschlagen, eine Python-Unterstützungserweiterung zu installieren.

> **Hinweis**: Wenn VS Code vorschlägt, das Repository in einem Container erneut zu öffnen, lehnen Sie diese Anfrage ab, um die lokal installierte Version von Python zu verwenden.

### Verwendung von Jupyter im Browser

Sie können auch im [Jupyter-Umfeld](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direkt in Ihrem Browser an dem Projekt arbeiten. Sowohl klassisches Jupyter als auch [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) bieten eine angenehme Entwicklungsumgebung mit Funktionen wie Autovervollständigung, Code-Hervorhebung usw.

Um Jupyter lokal zu starten, gehen Sie zum Terminal/Befehlszeile, navigieren Sie zum Kursverzeichnis und führen Sie aus:

```bash
jupyter notebook
```

oder

```bash
jupyterhub
```

Dies startet eine Jupyter-Instanz und die URL, um darauf zuzugreifen, wird im Befehlszeilenfenster angezeigt.

Sobald Sie auf die URL zugreifen, sollten Sie die Kursübersicht sehen und zu jeder `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` Datei navigieren können, wo Sie den Code und die Ausgaben ansehen können.

## Verwendung des Azure OpenAI-Dienstes zum ersten Mal

Wenn Sie zum ersten Mal mit dem Azure OpenAI-Dienst arbeiten, folgen Sie bitte diesem Leitfaden, um eine [Azure OpenAI-Dienstressource zu erstellen und bereitzustellen.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Verwendung der OpenAI API zum ersten Mal

Wenn Sie zum ersten Mal mit der OpenAI API arbeiten, folgen Sie bitte dem Leitfaden, wie Sie die [Schnittstelle erstellen und verwenden.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Treffen Sie andere Lernende

Wir haben Kanäle in unserem offiziellen [AI Community Discord-Server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) erstellt, um andere Lernende zu treffen. Dies ist eine großartige Möglichkeit, sich mit anderen gleichgesinnten Unternehmern, Erbauern, Studenten und allen, die sich in Generativer KI weiterentwickeln möchten, zu vernetzen.

[![Treten Sie dem Discord-Kanal bei](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Das Projektteam wird auch auf diesem Discord-Server sein, um allen Lernenden zu helfen.

## Beitrag leisten

Dieser Kurs ist eine Open-Source-Initiative. Wenn Sie Verbesserungsmöglichkeiten oder Probleme sehen, erstellen Sie bitte eine [Pull-Anfrage](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) oder melden Sie ein [GitHub-Problem](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Das Projektteam wird alle Beiträge verfolgen. Einen Beitrag zu Open Source zu leisten, ist eine großartige Möglichkeit, Ihre Karriere in Generativer KI aufzubauen.

Die meisten Beiträge erfordern, dass Sie einem Contributor License Agreement (CLA) zustimmen, das erklärt, dass Sie das Recht haben und tatsächlich die Rechte gewähren, dass wir Ihren Beitrag nutzen können. Für Details besuchen Sie bitte die [CLA, Contributor License Agreement Website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Wichtig: Wenn Sie Text in diesem Repository übersetzen, stellen Sie bitte sicher, dass Sie keine maschinelle Übersetzung verwenden. Wir werden Übersetzungen über die Community überprüfen, also melden Sie sich bitte nur für Übersetzungen in Sprachen, in denen Sie kompetent sind.

Wenn Sie eine Pull-Anfrage einreichen, wird ein CLA-Bot automatisch bestimmen, ob Sie ein CLA bereitstellen müssen, und die PR entsprechend kennzeichnen (z. B. Label, Kommentar). Folgen Sie einfach den Anweisungen des Bots. Dies müssen Sie nur einmal für alle Repositories tun, die unser CLA verwenden.

Dieses Projekt hat den [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) übernommen. Für weitere Informationen lesen Sie die Code of Conduct FAQ oder kontaktieren Sie [Email opencode](opencode@microsoft.com) mit weiteren Fragen oder Kommentaren.

## Lass uns anfangen

Nachdem Sie die notwendigen Schritte abgeschlossen haben, um diesen Kurs abzuschließen, lassen Sie uns mit einer [Einführung in Generative KI und LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) beginnen.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.