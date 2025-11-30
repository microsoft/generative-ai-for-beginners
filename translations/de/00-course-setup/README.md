<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-17T22:55:41+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "de"
}
-->
# Einführung in diesen Kurs

Wir freuen uns sehr, dass Sie mit diesem Kurs beginnen und gespannt sind, welche Ideen Sie mit Generativer KI umsetzen werden!

Um Ihren Erfolg sicherzustellen, finden Sie auf dieser Seite die Schritte zur Einrichtung, technische Anforderungen und Hinweise, wo Sie bei Bedarf Hilfe erhalten können.

## Einrichtungsschritte

Um mit diesem Kurs zu beginnen, müssen Sie die folgenden Schritte ausführen.

### 1. Dieses Repository forken

[Forken Sie dieses gesamte Repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) in Ihr eigenes GitHub-Konto, um den Code ändern und die Herausforderungen abschließen zu können. Sie können dieses Repository auch [mit einem Stern (🌟) markieren](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), um es und verwandte Repositories leichter zu finden.

### 2. Erstellen Sie einen Codespace

Um Abhängigkeitsprobleme beim Ausführen des Codes zu vermeiden, empfehlen wir, diesen Kurs in einem [GitHub Codespace](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) auszuführen.

In Ihrem Fork: **Code -> Codespaces -> New on main**

![Dialog mit Schaltflächen zum Erstellen eines Codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Fügen Sie ein Geheimnis hinzu

1. ⚙️ Zahnrad-Symbol -> Befehlspalette -> Codespaces: Benutzergeheimnis verwalten -> Neues Geheimnis hinzufügen.
2. Benennen Sie es OPENAI_API_KEY, fügen Sie Ihren Schlüssel ein und speichern Sie.

### 3. Was kommt als Nächstes?

| Ich möchte…          | Gehe zu…                                                                  |
|-----------------------|---------------------------------------------------------------------------|
| Lektion 1 starten     | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)      |
| Offline arbeiten      | [`setup-local.md`](02-setup-local.md)                                    |
| Einen LLM-Anbieter einrichten | [`providers.md`](03-providers.md)                                     |
| Andere Lernende treffen | [Treten Sie unserem Discord bei](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Fehlerbehebung

| Symptom                                   | Lösung                                                          |
|-------------------------------------------|-----------------------------------------------------------------|
| Container-Build hängt > 10 Minuten        | **Codespaces ➜ „Rebuild Container“**                           |
| `python: command not found`               | Terminal wurde nicht verbunden; klicken Sie auf **+** ➜ *bash* |
| `401 Unauthorized` von OpenAI             | Falscher / abgelaufener `OPENAI_API_KEY`                       |
| VS Code zeigt „Dev container mounting…“   | Aktualisieren Sie den Browser-Tab – Codespaces verliert manchmal die Verbindung |
| Notebook-Kernel fehlt                     | Notebook-Menü ➜ **Kernel ▸ Kernel auswählen ▸ Python 3**       |

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

5. **Installieren Sie `python-dotenv`**: Falls noch nicht geschehen, müssen Sie das Paket `python-dotenv` installieren, um Umgebungsvariablen aus der `.env`-Datei in Ihre Python-Anwendung zu laden. Sie können es mit `pip` installieren:

   ```bash
   pip install python-dotenv
   ```

6. **Laden Sie Umgebungsvariablen in Ihr Python-Skript**: Verwenden Sie in Ihrem Python-Skript das Paket `python-dotenv`, um die Umgebungsvariablen aus der `.env`-Datei zu laden:

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

## Lokales Ausführen auf Ihrem Computer

Um den Code lokal auf Ihrem Computer auszuführen, benötigen Sie eine Version von [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Um das Repository zu verwenden, müssen Sie es klonen:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Sobald Sie alles heruntergeladen haben, können Sie loslegen!

## Optionale Schritte

### Miniconda installieren

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ist ein schlanker Installer für die Installation von [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python sowie einigen Paketen.  
Conda selbst ist ein Paketmanager, der es einfach macht, verschiedene Python-[**virtuelle Umgebungen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) und Pakete einzurichten und zwischen ihnen zu wechseln. Es ist auch nützlich, um Pakete zu installieren, die nicht über `pip` verfügbar sind.

Sie können der [MiniConda-Installationsanleitung](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) folgen, um es einzurichten.

Mit installiertem Miniconda müssen Sie das [Repository klonen](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (falls noch nicht geschehen).

Als Nächstes müssen Sie eine virtuelle Umgebung erstellen. Um dies mit Conda zu tun, erstellen Sie eine neue Umgebungsdatei (_environment.yml_). Wenn Sie mit Codespaces arbeiten, erstellen Sie diese innerhalb des Verzeichnisses `.devcontainer`, also `.devcontainer/environment.yml`.

Füllen Sie Ihre Umgebungsdatei mit folgendem Code-Snippet:

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

Falls Sie Fehler mit Conda erhalten, können Sie die Microsoft AI-Bibliotheken manuell mit folgendem Befehl in einem Terminal installieren:

```
conda install -c microsoft azure-ai-ml
```

Die Umgebungsdatei gibt die benötigten Abhängigkeiten an. `<environment-name>` bezieht sich auf den Namen, den Sie für Ihre Conda-Umgebung verwenden möchten, und `<python-version>` ist die Version von Python, die Sie verwenden möchten, z. B. `3` für die neueste Hauptversion von Python.

Damit können Sie Ihre Conda-Umgebung erstellen, indem Sie die folgenden Befehle in Ihrer Befehlszeile/Terminal ausführen:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Falls Sie auf Probleme stoßen, lesen Sie den [Conda-Umgebungsleitfaden](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Verwendung von Visual Studio Code mit der Python-Erweiterung

Wir empfehlen die Verwendung des Editors [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) mit der [Python-Erweiterung](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) für diesen Kurs. Dies ist jedoch nur eine Empfehlung und keine zwingende Voraussetzung.

> **Hinweis**: Wenn Sie das Kurs-Repository in VS Code öffnen, haben Sie die Möglichkeit, das Projekt in einem Container einzurichten. Dies ist aufgrund des speziellen [`.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)-Verzeichnisses im Kurs-Repository möglich. Mehr dazu später.

> **Hinweis**: Sobald Sie das Verzeichnis in VS Code klonen und öffnen, wird Ihnen automatisch vorgeschlagen, eine Python-Erweiterung zu installieren.

> **Hinweis**: Wenn VS Code vorschlägt, das Repository in einem Container erneut zu öffnen, lehnen Sie diese Anfrage ab, um die lokal installierte Version von Python zu verwenden.

### Verwendung von Jupyter im Browser

Sie können auch im [Jupyter-Umfeld](https://jupyter.org?WT.mc_id=academic-105485-koreyst) direkt in Ihrem Browser an dem Projekt arbeiten. Sowohl das klassische Jupyter als auch [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) bieten eine angenehme Entwicklungsumgebung mit Funktionen wie Autovervollständigung, Syntaxhervorhebung usw.

Um Jupyter lokal zu starten, öffnen Sie das Terminal/die Befehlszeile, navigieren Sie zum Kursverzeichnis und führen Sie aus:

```bash
jupyter notebook
```

oder

```bash
jupyterhub
```

Dies startet eine Jupyter-Instanz, und die URL zum Zugriff darauf wird im Befehlszeilenfenster angezeigt.

Sobald Sie die URL aufrufen, sollten Sie die Kursübersicht sehen und zu jeder beliebigen `*.ipynb`-Datei navigieren können. Zum Beispiel `08-building-search-applications/python/oai-solution.ipynb`.

### Ausführung in einem Container

Eine Alternative zur Einrichtung auf Ihrem Computer oder im Codespace ist die Verwendung eines [Containers](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Der spezielle Ordner `.devcontainer` im Kurs-Repository ermöglicht es VS Code, das Projekt in einem Container einzurichten. Außerhalb von Codespaces erfordert dies die Installation von Docker und ist mit etwas Aufwand verbunden. Daher empfehlen wir dies nur Personen, die Erfahrung im Umgang mit Containern haben.

Eine der besten Möglichkeiten, Ihre API-Schlüssel bei der Verwendung von GitHub Codespaces sicher zu halten, ist die Verwendung von Codespace Secrets. Bitte folgen Sie der Anleitung zur [Verwaltung von Codespaces-Geheimnissen](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), um mehr darüber zu erfahren.

## Lektionen und technische Anforderungen

Der Kurs umfasst 6 Konzeptlektionen und 6 Programmierlektionen.

Für die Programmierlektionen verwenden wir den Azure OpenAI Service. Sie benötigen Zugriff auf den Azure OpenAI Service und einen API-Schlüssel, um diesen Code auszuführen. Sie können den Zugang beantragen, indem Sie [dieses Formular ausfüllen](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Während Sie auf die Bearbeitung Ihres Antrags warten, enthält jede Programmierlektion auch eine `README.md`-Datei, in der Sie den Code und die Ausgaben einsehen können.

## Erster Einsatz des Azure OpenAI Service

Wenn Sie zum ersten Mal mit dem Azure OpenAI Service arbeiten, folgen Sie bitte dieser Anleitung, um eine [Azure OpenAI Service-Ressource zu erstellen und bereitzustellen.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Erster Einsatz der OpenAI API

Wenn Sie zum ersten Mal mit der OpenAI API arbeiten, folgen Sie bitte der Anleitung, wie Sie die [Schnittstelle erstellen und verwenden.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Andere Lernende treffen

Wir haben Kanäle in unserem offiziellen [AI Community Discord-Server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) erstellt, um andere Lernende zu treffen. Dies ist eine großartige Möglichkeit, sich mit anderen gleichgesinnten Unternehmern, Entwicklern, Studierenden und allen, die sich im Bereich Generative KI weiterentwickeln möchten, zu vernetzen.

[![Treten Sie dem Discord-Kanal bei](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Das Projektteam wird ebenfalls auf diesem Discord-Server sein, um den Lernenden zu helfen.

## Mitwirken

Dieser Kurs ist eine Open-Source-Initiative. Wenn Sie Verbesserungsmöglichkeiten oder Probleme sehen, erstellen Sie bitte eine [Pull-Anfrage](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) oder melden Sie ein [GitHub-Problem](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Das Projektteam wird alle Beiträge verfolgen. Einen Beitrag zu Open Source zu leisten, ist eine großartige Möglichkeit, Ihre Karriere im Bereich Generative KI voranzutreiben.

Die meisten Beiträge erfordern, dass Sie einer Contributor License Agreement (CLA) zustimmen, in der Sie erklären, dass Sie das Recht haben und uns tatsächlich die Rechte einräumen, Ihren Beitrag zu nutzen. Weitere Informationen finden Sie auf der [CLA-Website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Wenn Sie eine Pull-Anfrage einreichen, wird ein CLA-Bot automatisch feststellen, ob Sie eine CLA bereitstellen müssen, und die PR entsprechend kennzeichnen (z. B. mit einem Label oder Kommentar). Befolgen Sie einfach die Anweisungen des Bots. Sie müssen dies nur einmal für alle Repositories tun, die unsere CLA verwenden.

Dieses Projekt hat den [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) übernommen. Weitere Informationen finden Sie in den FAQ zum Verhaltenskodex oder kontaktieren Sie [Email opencode](opencode@microsoft.com) bei weiteren Fragen oder Anmerkungen.

## Los geht's!
Jetzt, da Sie die erforderlichen Schritte abgeschlossen haben, um diesen Kurs zu absolvieren, lassen Sie uns mit einer [Einführung in Generative KI und LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) beginnen.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.