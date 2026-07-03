# Erste Schritte mit diesem Kurs

Wir sind sehr gespannt, dass Sie diesen Kurs beginnen und sehen, wozu Sie sich von Generativer KI inspirieren lassen!

Um Ihren Erfolg sicherzustellen, beschreibt diese Seite Einrichtungsschritte, technische Anforderungen und wo Sie bei Bedarf Hilfe bekommen.

## Einrichtungsschritte

Um mit diesem Kurs zu starten, müssen Sie die folgenden Schritte abschließen.

### 1. Dieses Repo forken

[Forken Sie dieses gesamte Repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) in Ihr eigenes GitHub-Konto, um beliebigen Code ändern und die Herausforderungen absolvieren zu können. Sie können auch [dieses Repo mit einem Stern (🌟) versehen](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), um es und verwandte Repos leichter zu finden.

### 2. Erstellen Sie einen Codespace

Um Abhängigkeitsprobleme beim Ausführen des Codes zu vermeiden, empfehlen wir, diesen Kurs in einem [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) auszuführen.

In Ihrem Fork: **Code -> Codespaces -> New on main**

![Dialog mit Schaltflächen zur Erstellung eines Codespaces](../../../translated_images/de/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Fügen Sie ein Secret hinzu

1. ⚙️ Zahnrad-Symbol -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Name: OPENAI_API_KEY, fügen Sie Ihren Schlüssel ein, Speichern.

### 3. Was nun?

| Ich möchte…          | Gehe zu…                                                               |
|----------------------|------------------------------------------------------------------------|
| Lektion 1 starten    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Offline arbeiten     | [`setup-local.md`](02-setup-local.md)                                   |
| Einen LLM-Anbieter einrichten | [`providers.md`](03-providers.md)                                 |
| Andere Lernende treffen | [Tritt unserem Discord bei](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Fehlerbehebung

| Symptom                                   | Lösung                                                            |
|-------------------------------------------|------------------------------------------------------------------|
| Container-Build bleibt > 10 Min hängen    | **Codespaces ➜ „Rebuild Container“**                             |
| `python: command not found`               | Terminal wurde nicht angehängt; klicken Sie auf **+** ➜ *bash*    |
| `401 Unauthorized` von OpenAI             | Falscher / abgelaufener `OPENAI_API_KEY`                         |
| VS Code zeigt „Dev container mounting…“   | Browser-Tab aktualisieren — Codespaces verliert manchmal Verbindung |
| Notebook-Kernel fehlt                      | Notebook-Menü ➜ **Kernel ▸ Select Kernel ▸ Python 3**            |

   Unix-basierte Systeme:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Bearbeiten Sie die `.env`-Datei**: Öffnen Sie die `.env`-Datei in einem Texteditor (z. B. VS Code, Notepad++ oder einem anderen Editor). Fügen Sie die folgende Zeile hinzu und ersetzen Sie `your_github_token_here` durch Ihren tatsächlichen GitHub-Token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Datei speichern**: Speichern Sie die Änderungen und schließen Sie den Texteditor.

5. **`python-dotenv` installieren**: Falls noch nicht installiert, müssen Sie das Paket `python-dotenv` installieren, um Umgebungsvariablen aus der `.env`-Datei in Ihre Python-Anwendung zu laden. Sie können es mit `pip` installieren:

   ```bash
   pip install python-dotenv
   ```

6. **Umgebungsvariablen im Python-Skript laden**: Verwenden Sie in Ihrem Python-Skript das Paket `python-dotenv`, um die Umgebungsvariablen aus der `.env`-Datei zu laden:

   ```python
   from dotenv import load_dotenv
   import os

   # Lade Umgebungsvariablen aus der .env-Datei
   load_dotenv()

   # Greife auf die GITHUB_TOKEN-Variable zu
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Das war’s! Sie haben erfolgreich eine `.env`-Datei erstellt, Ihren GitHub-Token hinzugefügt und diesen in Ihre Python-Anwendung geladen.

## Lokale Ausführung auf Ihrem Computer

Um den Code lokal auf Ihrem Computer auszuführen, benötigen Sie eine installierte Version von [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Um das Repository zu verwenden, müssen Sie es klonen:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Sobald Sie alles ausgecheckt haben, können Sie loslegen!

## Optionale Schritte

### Miniconda installieren

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ist ein leichter Installer zur Installation von [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python und einigen Paketen.  
Conda selbst ist ein Paketmanager, der es einfach macht, verschiedene Python [**virtuelle Umgebungen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) und Pakete einzurichten und zu wechseln. Es ist auch praktisch zum Installieren von Paketen, die nicht über `pip` verfügbar sind.

Folgen Sie der [Miniconda-Installationsanleitung](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), um es einzurichten.

Nachdem Miniconda installiert ist, müssen Sie das [Repository klonen](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (falls noch nicht geschehen).

Als Nächstes müssen Sie eine virtuelle Umgebung erstellen. Erstellen Sie dazu eine neue Umgebungsdatei (_environment.yml_). Wenn Sie Codespaces verwenden, erstellen Sie diese im `.devcontainer`-Verzeichnis, also `.devcontainer/environment.yml`.

Füllen Sie Ihre Umgebungsdatei mit dem Folgenden aus:

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

Wenn bei der Verwendung von conda Fehler auftreten, können Sie die Microsoft AI-Bibliotheken auch manuell mit folgendem Befehl im Terminal installieren:

```
conda install -c microsoft azure-ai-ml
```

Die Umgebungsdatei spezifiziert die benötigten Abhängigkeiten. `<environment-name>` bezeichnet den Namen, den Sie Ihrer Conda-Umgebung geben möchten, und `<python-version>` die Python-Version, die Sie verwenden wollen, z. B. `3` für die aktuelle Hauptversion.

Anschließend können Sie Ihre Conda-Umgebung mit folgenden Befehlen in der Kommandozeile/dem Terminal erstellen:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer-Unterpfad gilt nur für Codespace-Einrichtungen
conda activate ai4beg
```

Bei Problemen hilft Ihnen die [Conda-Umgebungsanleitung](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Verwendung von Visual Studio Code mit der Python-Unterstützungserweiterung

Für diesen Kurs empfehlen wir den Editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) mit der [Python-Unterstützungserweiterung](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst). Dies ist jedoch eine Empfehlung, keine zwingende Voraussetzung.

> **Hinweis**: Wenn Sie das Kurs-Repository in VS Code öffnen, können Sie das Projekt innerhalb eines Containers einrichten. Dies ist dank des [speziellen `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)-Verzeichnisses im Repository möglich. Mehr dazu später.

> **Hinweis**: Sobald Sie das Verzeichnis klonen und in VS Code öffnen, wird Ihnen automatisch vorgeschlagen, eine Python-Unterstützungserweiterung zu installieren.

> **Hinweis**: Wenn VS Code vorschlägt, das Repository in einem Container neu zu öffnen, lehnen Sie dies ab, um die lokal installierte Python-Version zu verwenden.

### Verwendung von Jupyter im Browser

Sie können auch direkt im Browser mit der [Jupyter-Umgebung](https://jupyter.org?WT.mc_id=academic-105485-koreyst) arbeiten. Sowohl klassisches Jupyter als auch [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) bieten eine angenehme Entwicklungsumgebung mit Funktionen wie Autovervollständigung und Codehervorhebung.

Um Jupyter lokal zu starten, öffnen Sie das Terminal/die Kommandozeile, navigieren Sie zum Kursverzeichnis und führen Sie aus:

```bash
jupyter notebook
```

oder

```bash
jupyterhub
```

Dadurch wird eine Jupyter-Instanz gestartet, und die URL zum Zugriff wird im Kommandozeilenfenster angezeigt.

Wenn Sie die URL öffnen, sollte die Kursübersicht erscheinen, und Sie können zu jeder `*.ipynb`-Datei navigieren, z. B. `08-building-search-applications/python/oai-solution.ipynb`.

### Ausführung in einem Container

Eine Alternative zum Einrichten auf Ihrem Computer oder Codespace ist die Nutzung eines [Containers](https://en.wikipedia.org/wiki/Containerization_%28computing%29?WT.mc_id=academic-105485-koreyst). Das spezielle `.devcontainer`-Verzeichnis im Kurs-Repository ermöglicht es VS Code, das Projekt in einem Container einzurichten. Außerhalb von Codespaces ist dafür die Installation von Docker erforderlich und es braucht etwas Erfahrung. Wir empfehlen dies daher nur für Nutzer mit Erfahrung im Umgang mit Containern.

Eine der besten Möglichkeiten, Ihre API-Schlüssel bei Nutzung von GitHub Codespaces sicher zu verwahren, sind Codespace Secrets. Folgen Sie bitte der [Codespaces-Secrets-Verwaltung](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), um mehr darüber zu erfahren.

## Lektionen und technische Anforderungen

Der Kurs besteht aus 6 Konzept-Lektionen und 6 Codierungslektionen.

Für die Codierungslektionen verwenden wir den Azure OpenAI Service. Sie benötigen Zugriff auf den Azure OpenAI Dienst und einen API-Schlüssel, um diesen Code auszuführen. Sie können den Zugang über [dieses Antragsformular](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst) beantragen.

Während Sie auf die Bearbeitung Ihres Antrags warten, enthält jede Codierungslektion auch eine `README.md`-Datei, in der Sie den Code und die Ausgaben ansehen können.

## Erster Gebrauch des Azure OpenAI Service

Wenn Sie zum ersten Mal mit dem Azure OpenAI Service arbeiten, folgen Sie dieser Anleitung, wie Sie eine Azure OpenAI Service-Ressource [erstellen und bereitstellen](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst).

## Erster Gebrauch der OpenAI API

Wenn Sie die OpenAI API zum ersten Mal verwenden, folgen Sie der Anleitung zum [Erstellen und Nutzen der Schnittstelle](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst).

## Andere Lernende treffen

Wir haben Kanäle in unserem offiziellen [AI Community Discord Server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) eingerichtet, um andere Lernende zu treffen. Dies ist eine großartige Möglichkeit, sich mit Gleichgesinnten, Unternehmern, Entwicklern, Studierenden und allen, die in Generativer KI besser werden möchten, zu vernetzen.

[![Trete dem Discord-Kanal bei](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Das Projektteam ist ebenfalls auf diesem Discord-Server, um Lernenden zu helfen.

## Mitwirken

Dieser Kurs ist eine Open-Source-Initiative. Wenn Sie Verbesserungsvorschläge oder Fehler finden, erstellen Sie bitte einen [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) oder melden Sie ein [GitHub Issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Das Projektteam verfolgt alle Beiträge. Beitragen zu Open Source ist ein großartiger Weg, Ihre Karriere in Generativer KI zu fördern.

Die meisten Beiträge erfordern, dass Sie einer Contributor License Agreement (CLA) zustimmen, die besagt, dass Sie das Recht haben und tatsächlich die Rechte besitzen, uns die Nutzung Ihres Beitrags zu erlauben. Details finden Sie auf der [CLA-Website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Wichtig: Bitte verwenden Sie keine maschinelle Übersetzung für Texte in diesem Repo. Wir werden die Übersetzungen durch die Community prüfen, also melden Sie sich nur für Übersetzungen in Sprachen, in denen Sie sicher sind.

Wenn Sie einen Pull Request einreichen, prüft ein CLA-Bot automatisch, ob Sie ein CLA bereitstellen müssen, und versieht die PR entsprechend (z. B. mit Label, Kommentar). Folgen Sie einfach den Anweisungen des Bots. Dies müssen Sie nur einmal für alle Repositories mit unserer CLA tun.

Dieses Projekt hat den [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) übernommen. Für weitere Informationen lesen Sie die FAQ zum Verhaltenskodex oder kontaktieren Sie [opencode@microsoft.com](opencode@microsoft.com) bei Fragen oder Anmerkungen.

## Lassen Sie uns starten!
Da Sie nun die notwendigen Schritte abgeschlossen haben, um diesen Kurs abzuschließen, beginnen wir mit einer [Einführung in Generative KI und LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, kann die automatisierte Übersetzung Fehler oder Ungenauigkeiten enthalten. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->