# Einstieg in diesen Kurs

Wir freuen uns sehr, dass Sie mit diesem Kurs beginnen und sehen möchten, was Sie mit Generativer KI inspirieren lässt zu bauen!

Um Ihren Erfolg zu gewährleisten, beschreibt diese Seite die Einrichtungs-Schritte, technischen Anforderungen und wo Sie bei Bedarf Hilfe bekommen.

## Einrichtungsschritte

Um mit diesem Kurs zu beginnen, müssen Sie die folgenden Schritte abschließen.

### 1. Forken Sie dieses Repo

[Forken Sie dieses komplette Repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) in Ihr eigenes GitHub-Konto, um jeglichen Code ändern und die Herausforderungen abschließen zu können. Sie können dieses Repo auch [mit einem Stern markieren (🌟)](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), damit Sie es und verwandte Repos leichter finden.

### 2. Erstellen Sie einen Codespace

Um Probleme mit Abhängigkeiten beim Ausführen des Codes zu vermeiden, empfehlen wir, diesen Kurs in einem [GitHub Codespace](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) auszuführen.

In Ihrem Fork: **Code -> Codespaces -> Neu auf main**

![Dialog, der Buttons zur Erstellung eines Codespaces zeigt](../../../translated_images/de/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Fügen Sie ein Secret hinzu

1. ⚙️ Zahnradsymbol -> Befehls-Palette -> Codespaces: Benutzer-Secret verwalten -> Neues Secret hinzufügen.
2. Name OPENAI_API_KEY, fügen Sie Ihren Schlüssel ein, Speichern.

### 3. Was kommt als Nächstes?

| Ich möchte…          | Gehe zu…                                                               |
|---------------------|------------------------------------------------------------------------|
| Lektion 1 starten    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Offline arbeiten     | [`setup-local.md`](02-setup-local.md)                                   |
| LLM-Anbieter einrichten | [`providers.md`](03-providers.md)                                   |
| Andere Lernende treffen | [Tritt unserem Discord bei](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Fehlerbehebung


| Symptom                                   | Lösung                                                          |
|-------------------------------------------|----------------------------------------------------------------|
| Container-Build hängt > 10 Minuten fest   | **Codespaces ➜ „Container neu aufbauen“**                       |
| `python: command not found`               | Terminal nicht verbunden; klicken Sie **+** ➜ *bash*            |
| `401 Unauthorized` von OpenAI              | Falscher / abgelaufener `OPENAI_API_KEY`                         |
| VS Code zeigt „Dev container mounting…“   | Browser-Tab neu laden – Codespaces verliert manchmal die Verbindung |
| Notebook-Kernel fehlt                      | Notebook-Menü ➜ **Kernel ▸ Kernel auswählen ▸ Python 3**         |

   Unix-basierte Systeme:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Bearbeiten Sie die `.env` Datei**: Öffnen Sie die `.env` Datei in einem Texteditor (z. B. VS Code, Notepad++ oder einem anderen Editor). Fügen Sie die folgenden Zeilen ein, wobei Sie die Platzhalter mit Ihrem tatsächlichen Microsoft Foundry Models-Endpunkt und Schlüssel ersetzen (siehe [`providers.md`](03-providers.md), wie Sie diese erhalten):

   > **Hinweis:** GitHub Models (und dessen `GITHUB_TOKEN` Variable) werden Ende Juli 2026 eingestellt. Verwenden Sie stattdessen [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Datei speichern**: Speichern Sie die Änderungen und schließen Sie den Texteditor.

5. **Installieren Sie `python-dotenv`**: Falls noch nicht geschehen, müssen Sie das Paket `python-dotenv` installieren, um Umgebungsvariablen aus der `.env` Datei in Ihre Python-Anwendung zu laden. Sie können es mit `pip` installieren:

   ```bash
   pip install python-dotenv
   ```

6. **Laden Sie Umgebungsvariablen in Ihrem Python-Skript**: Verwenden Sie in Ihrem Python-Skript das Paket `python-dotenv`, um die Umgebungsvariablen aus der `.env` Datei zu laden:

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

Das war’s! Sie haben erfolgreich eine `.env` Datei erstellt, Ihre Microsoft Foundry Models-Zugangsdaten hinzugefügt und diese in Ihre Python-Anwendung geladen.

## Lokales Ausführen auf Ihrem Computer

Um den Code lokal auf Ihrem Computer auszuführen, benötigen Sie eine installierte Version von [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Um das Repository dann zu verwenden, müssen Sie es klonen:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Sobald Sie alles ausgecheckt haben, können Sie loslegen!

## Optionale Schritte

### Installation von Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ist ein leichter Installer, der die Installation von [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python sowie einiger Pakete ermöglicht.
Conda selbst ist ein Paketmanager, der Ihnen das Einrichten und Wechseln zwischen verschiedenen Python [**virtuellen Umgebungen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) und Paketen erleichtert. Er ist auch nützlich, um Pakete zu installieren, die nicht via `pip` verfügbar sind.

Sie können der [MiniConda Installationsanleitung](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) folgen, um sie einzurichten.

Mit installiertem Miniconda müssen Sie das [Repository klonen](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (falls noch nicht geschehen)

Anschließend müssen Sie eine virtuelle Umgebung erstellen. Erstellen Sie dazu eine neue Umgebungs-Datei (_environment.yml_). Falls Sie mit Codespaces arbeiten, legen Sie diese im `.devcontainer`-Verzeichnis ab, also `.devcontainer/environment.yml`.

Füllen Sie Ihre Umgebungsdatei mit dem folgenden Schnipsel:

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

Falls bei der Verwendung von conda Fehler auftreten, können Sie die Microsoft AI-Bibliotheken manuell mit folgendem Terminal-Befehl installieren.

```
conda install -c microsoft azure-ai-ml
```

Die Umgebungsdatei gibt die benötigten Abhängigkeiten an. `<environment-name>` steht für den Namen Ihrer Conda-Umgebung, und `<python-version>` ist die Python-Version, die Sie nutzen möchten, zum Beispiel `3` für die neueste Hauptversion.

Anschließend können Sie Ihre Conda-Umgebung durch Ausführen der folgenden Befehle in der Kommandozeile/dem Terminal erstellen:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer-Unterpfad gilt nur für Codespace-Einrichtungen
conda activate ai4beg
```

Falls Probleme auftreten, konsultieren Sie bitte die [Conda Umgebungsanleitung](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst).

### Visual Studio Code mit Python-Support-Erweiterung verwenden

Wir empfehlen für diesen Kurs den Editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) mit der installierten [Python-Support-Erweiterung](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst). Dies ist jedoch eher eine Empfehlung als eine zwingende Voraussetzung.

> **Hinweis**: Beim Öffnen des Kurs-Repositorys in VS Code haben Sie die Möglichkeit, das Projekt innerhalb eines Containers einzurichten. Das ist möglich dank des [speziellen `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)-Verzeichnisses im Kurs-Repository. Mehr dazu später.

> **Hinweis**: Sobald Sie das Verzeichnis klonen und in VS Code öffnen, schlägt es automatisch vor, die Python-Support-Erweiterung zu installieren.

> **Hinweis**: Falls VS Code vorschlägt, das Repository in einem Container neu zu öffnen, lehnen Sie dies ab, um die lokal installierte Python-Version zu verwenden.

### Jupyter im Browser nutzen

Sie können auch direkt im Browser im [Jupyter-Umfeld](https://jupyter.org?WT.mc_id=academic-105485-koreyst) am Projekt arbeiten. Sowohl das klassische Jupyter als auch [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) bieten eine angenehme Entwicklungsumgebung mit Features wie Autovervollständigung, Syntax-Hervorhebung usw.

Um Jupyter lokal zu starten, öffnen Sie das Terminal/die Kommandozeile, navigieren in das Kursverzeichnis und führen aus:

```bash
jupyter notebook
```

oder

```bash
jupyterhub
```

Dies startet eine Jupyter-Instanz; die Adresse zur Nutzung wird im Terminal angezeigt.

Sobald Sie die Adresse aufrufen, sehen Sie die Kursübersicht und können zu jeder `*.ipynb` Datei navigieren, z. B. `08-building-search-applications/python/oai-solution.ipynb`.

### Ausführung in einem Container

Eine Alternative zur Einrichtung auf Ihrem Computer oder Codespace ist die Nutzung eines [Containers](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Das spezielle `.devcontainer`-Verzeichnis im Kurs-Repository ermöglicht es VS Code, das Projekt in einem Container einzurichten. Außerhalb von Codespaces erfordert dies die Installation von Docker und ehrlich gesagt etwas Aufwand, daher empfehlen wir dies nur erfahrenen Anwendern.

Einer der besten Wege, Ihre API-Schlüssel bei der Nutzung von GitHub Codespaces sicher zu verwahren, ist die Verwendung von Codespace Secrets. Folgen Sie bitte der Anleitung zur [Codespaces-Geheimnisverwaltung](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), um mehr darüber zu erfahren.


## Lektionen und technische Anforderungen

Der Kurs besteht aus „Learn“-Lektionen, die Konzepte der Generativen KI erklären, und „Build“-Lektionen mit praktischen Codebeispielen in **Python** und **TypeScript**, wo möglich.

Für die Coding-Lektionen nutzen wir Azure OpenAI in Microsoft Foundry. Sie benötigen ein Azure-Abonnement und einen API-Schlüssel. Der Zugang ist offen – keine Bewerbung nötig – Sie können also [eine Microsoft Foundry-Ressource erstellen und ein Modell bereitstellen](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst), um Ihren Endpunkt und Schlüssel zu erhalten.

Jede Coding-Lektion enthält außerdem eine `README.md`-Datei, in der Sie den Code und die Ergebnisse einsehen können, ohne etwas ausführen zu müssen.

## Azure OpenAI Service zum ersten Mal nutzen

Wenn Sie zum ersten Mal mit dem Azure OpenAI Service arbeiten, folgen Sie bitte dieser Anleitung, wie Sie [eine Azure OpenAI Service-Ressource erstellen und bereitstellen](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst).

## OpenAI API zum ersten Mal nutzen

Wenn Sie zum ersten Mal mit der OpenAI API arbeiten, folgen Sie bitte der Anleitung, wie Sie [die Schnittstelle erstellen und verwenden](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst).

## Andere Lernende treffen

Wir haben Kanäle in unserem offiziellen [AI Community Discord Server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) erstellt, um andere Lernende zu treffen. Dies ist eine tolle Möglichkeit, sich mit gleichgesinnten Unternehmern, Entwicklern, Studierenden und allen, die sich in Generativer KI weiterentwickeln möchten, zu vernetzen.

[![Discord-Kanal beitreten](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Das Projektteam ist ebenfalls auf diesem Discord-Server, um Lernenden zu helfen.

## Mitwirken

Dieser Kurs ist eine Open-Source-Initiative. Wenn Sie Verbesserungen oder Probleme sehen, erstellen Sie bitte einen [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) oder melden Sie ein [GitHub Issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Das Projektteam verfolgt alle Beiträge. Die Mitwirkung an Open Source ist eine großartige Möglichkeit, Ihre Karriere im Bereich Generative KI auszubauen.

Die meisten Beiträge erfordern Ihre Zustimmung zu einer Contributor License Agreement (CLA), die besagt, dass Sie die Rechte besitzen und tatsächlich gewähren, die wir benötigen, um Ihren Beitrag zu nutzen. Für Details siehe [CLA, Contributor License Agreement-Website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Wichtig: Bitte verwenden Sie bei der Übersetzung von Texten in diesem Repo keine maschinelle Übersetzung. Wir werden die Übersetzungen über die Community prüfen, daher melden Sie sich nur für Übersetzungen in Sprachen, die Sie gut beherrschen.


Wenn Sie eine Pull-Anfrage einreichen, bestimmt ein CLA-Bot automatisch, ob Sie eine CLA bereitstellen müssen, und versieht die PR entsprechend (z. B. mit Label, Kommentar). Folgen Sie einfach den Anweisungen des Bots. Dies müssen Sie nur einmal für alle Repositories mit unserer CLA tun.

Dieses Projekt hat den [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst) übernommen. Für weitere Informationen lesen Sie die FAQ zum Verhaltenskodex oder kontaktieren Sie [Email opencode](opencode@microsoft.com) bei weiteren Fragen oder Anmerkungen.

## Lass uns anfangen

Nun, da Sie die notwendigen Schritte zum Abschluss dieses Kurses abgeschlossen haben, beginnen wir mit einer [Einführung in Generative AI und LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->