<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T13:43:53+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "de"
}
-->
# Einstieg in diesen Kurs

Wir freuen uns sehr, dass du mit diesem Kurs startest und sind gespannt, wozu dich Generative KI inspiriert!

Damit du erfolgreich bist, findest du auf dieser Seite die Schritte zur Einrichtung, technische Voraussetzungen und Hinweise, wo du bei Bedarf Hilfe bekommst.

## Einrichtungsschritte

Um mit dem Kurs zu beginnen, solltest du die folgenden Schritte durchführen.

### 1. Forke dieses Repository

[Forke das gesamte Repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) in deinen eigenen GitHub-Account, damit du den Code ändern und die Aufgaben bearbeiten kannst. Du kannst das Repository auch [mit einem Stern (🌟) markieren](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst), um es und verwandte Repos leichter wiederzufinden.

### 2. Erstelle einen Codespace

Um Abhängigkeitsprobleme beim Ausführen des Codes zu vermeiden, empfehlen wir, diesen Kurs in einem [GitHub Codespace](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst) zu absolvieren.

In deinem Fork: **Code -> Codespaces -> New on main**

![Dialog mit Buttons zum Erstellen eines Codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Füge ein Secret hinzu

1. ⚙️ Zahnrad-Symbol -> Command Palette -> Codespaces : Manage user secret -> Add a new secret.
2. Name OPENAI_API_KEY, füge deinen Schlüssel ein, Speichern.

### 3.  Wie geht es weiter?

| Ich möchte…         | Gehe zu…                                                                 |
|---------------------|--------------------------------------------------------------------------|
| Mit Lektion 1 starten | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)    |
| Offline arbeiten      | [`setup-local.md`](02-setup-local.md)                                  |
| Einen LLM-Anbieter einrichten | [`providers.md`](providers.md)                                 |
| Andere Lernende treffen | [Tritt unserem Discord bei](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Fehlerbehebung

| Symptom                                   | Lösung                                                        |
|-------------------------------------------|---------------------------------------------------------------|
| Container-Build hängt > 10 min            | **Codespaces ➜ „Rebuild Container“**                          |
| `python: command not found`               | Terminal wurde nicht verbunden; klicke auf **+** ➜ *bash*     |
| `401 Unauthorized` von OpenAI             | Falscher / abgelaufener `OPENAI_API_KEY`                      |
| VS Code zeigt „Dev container mounting…“   | Browser-Tab neu laden – Codespaces verliert manchmal die Verbindung |
| Notebook-Kernel fehlt                     | Notebook-Menü ➜ **Kernel ▸ Select Kernel ▸ Python 3**         |

   Unix-basierte Systeme:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Bearbeite die `.env`-Datei**: Öffne die `.env`-Datei in einem Texteditor (z.B. VS Code, Notepad++ oder einem anderen Editor). Füge folgende Zeile hinzu und ersetze `your_github_token_here` durch deinen tatsächlichen GitHub-Token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Datei speichern**: Speichere die Änderungen und schließe den Editor.

5. **Installiere `python-dotenv`**: Falls noch nicht geschehen, installiere das Paket `python-dotenv`, um Umgebungsvariablen aus der `.env`-Datei in deine Python-Anwendung zu laden. Installiere es mit `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Lade Umgebungsvariablen in deinem Python-Skript**: Nutze in deinem Python-Skript das Paket `python-dotenv`, um die Variablen aus der `.env`-Datei zu laden:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Das war's! Du hast erfolgreich eine `.env`-Datei erstellt, deinen GitHub-Token hinzugefügt und ihn in deine Python-Anwendung geladen.

## So führst du den Code lokal auf deinem Computer aus

Um den Code lokal auf deinem Rechner auszuführen, benötigst du eine [installierte Python-Version](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Um das Repository zu nutzen, musst du es klonen:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Sobald alles heruntergeladen ist, kannst du loslegen!

## Optionale Schritte

### Miniconda installieren

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ist ein schlanker Installer für [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python und einige Pakete.
Conda selbst ist ein Paketmanager, der es einfach macht, verschiedene Python-[**virtuelle Umgebungen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) und Pakete einzurichten und zu wechseln. Außerdem ist es praktisch, um Pakete zu installieren, die nicht über `pip` verfügbar sind.

Du kannst der [MiniConda-Installationsanleitung](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) folgen, um es einzurichten.

Mit installiertem Miniconda musst du das [Repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) klonen (falls noch nicht geschehen).

Als Nächstes musst du eine virtuelle Umgebung erstellen. Mit Conda geht das, indem du eine neue Umgebungsdatei (_environment.yml_) anlegst. Wenn du Codespaces verwendest, erstelle diese Datei im Verzeichnis `.devcontainer`, also `.devcontainer/environment.yml`.

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

Falls du mit conda Fehler bekommst, kannst du die Microsoft AI Libraries auch manuell mit folgendem Befehl im Terminal installieren.

```
conda install -c microsoft azure-ai-ml
```

Die Umgebungsdatei legt die benötigten Abhängigkeiten fest. `<environment-name>` ist der Name, den du für deine Conda-Umgebung verwenden möchtest, und `<python-version>` ist die gewünschte Python-Version, z.B. `3` für die aktuelle Hauptversion.

Danach kannst du deine Conda-Umgebung mit den folgenden Befehlen im Terminal erstellen:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Sieh dir den [Conda-Umgebungen-Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) an, falls du auf Probleme stößt.

### Visual Studio Code mit Python-Erweiterung verwenden

Wir empfehlen für diesen Kurs den Editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) mit der [Python-Erweiterung](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst). Das ist aber nur eine Empfehlung und keine zwingende Voraussetzung.

> **Note**: Wenn du das Kurs-Repository in VS Code öffnest, kannst du das Projekt in einem Container einrichten. Das liegt an dem [speziellen `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst)-Verzeichnis im Repository. Mehr dazu später.

> **Note**: Sobald du das Verzeichnis in VS Code öffnest, wird dir automatisch vorgeschlagen, die Python-Erweiterung zu installieren.

> **Note**: Falls VS Code vorschlägt, das Repository in einem Container zu öffnen, lehne dies ab, um die lokal installierte Python-Version zu verwenden.

### Jupyter im Browser nutzen

Du kannst auch direkt im Browser mit der [Jupyter-Umgebung](https://jupyter.org?WT.mc_id=academic-105485-koreyst) am Projekt arbeiten. Sowohl das klassische Jupyter als auch [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) bieten eine angenehme Entwicklungsumgebung mit Features wie Autovervollständigung, Syntax-Highlighting usw.

Um Jupyter lokal zu starten, öffne das Terminal, wechsle ins Kursverzeichnis und führe aus:

```bash
jupyter notebook
```

oder

```bash
jupyterhub
```

Dadurch wird eine Jupyter-Instanz gestartet und die URL zum Zugriff wird im Terminal angezeigt.

Wenn du die URL aufrufst, siehst du die Kursübersicht und kannst zu jeder `*.ipynb`-Datei navigieren, z.B. `08-building-search-applications/python/oai-solution.ipynb`.

### Ausführung in einem Container

Eine Alternative zur lokalen Einrichtung oder Codespace ist die Nutzung eines [Containers](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Der spezielle Ordner `.devcontainer` im Repository ermöglicht es VS Code, das Projekt in einem Container einzurichten. Außerhalb von Codespaces ist dafür die Installation von Docker nötig und es ist etwas aufwändiger – wir empfehlen das daher nur, wenn du bereits Erfahrung mit Containern hast.

Eine der besten Möglichkeiten, deine API-Schlüssel in GitHub Codespaces sicher zu verwahren, ist die Nutzung von Codespace Secrets. Folge der Anleitung zur [Verwaltung von Codespaces-Secrets](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst), um mehr darüber zu erfahren.

## Lektionen und technische Voraussetzungen

Der Kurs besteht aus 6 Konzept-Lektionen und 6 Coding-Lektionen.

Für die Coding-Lektionen nutzen wir den Azure OpenAI Service. Du benötigst Zugriff auf den Azure OpenAI Service und einen API-Schlüssel, um den Code auszuführen. Du kannst [hier einen Antrag stellen](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst), um Zugriff zu erhalten.

Während du auf die Bearbeitung deines Antrags wartest, findest du in jeder Coding-Lektion auch eine `README.md`-Datei, in der du den Code und die Ausgaben ansehen kannst.

## Azure OpenAI Service zum ersten Mal nutzen

Wenn du zum ersten Mal mit dem Azure OpenAI Service arbeitest, folge bitte dieser Anleitung, wie du [eine Azure OpenAI Service-Ressource erstellst und bereitstellst.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## OpenAI API zum ersten Mal nutzen

Wenn du zum ersten Mal mit der OpenAI API arbeitest, folge bitte der Anleitung, wie du [das Interface erstellst und verwendest.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Andere Lernende treffen

Wir haben in unserem offiziellen [AI Community Discord-Server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) Kanäle eingerichtet, um andere Lernende zu treffen. Das ist eine tolle Möglichkeit, dich mit anderen Gründer:innen, Entwickler:innen, Studierenden und allen, die sich für Generative KI interessieren, zu vernetzen.

[![Discord-Kanal beitreten](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Auch das Projektteam ist auf diesem Discord-Server und hilft gerne weiter.

## Mitmachen

Dieser Kurs ist ein Open-Source-Projekt. Wenn du Verbesserungen oder Probleme siehst, erstelle bitte einen [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) oder melde ein [GitHub-Issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Das Projektteam verfolgt alle Beiträge. Open Source beizutragen ist eine großartige Möglichkeit, deine Karriere im Bereich Generative KI voranzubringen.

Für die meisten Beiträge musst du einer Contributor License Agreement (CLA) zustimmen, die bestätigt, dass du das Recht hast, deinen Beitrag einzureichen und uns die Nutzungsrechte daran gewährst. Details findest du auf der [CLA-Website](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Wichtig: Wenn du Texte in diesem Repository übersetzt, verwende bitte keine maschinelle Übersetzung. Die Übersetzungen werden von der Community überprüft, also übernimm bitte nur Sprachen, in denen du wirklich fit bist.

Wenn du einen Pull Request einreichst, prüft ein CLA-Bot automatisch, ob du eine CLA abgeben musst, und versieht den PR entsprechend (z.B. mit Label, Kommentar). Folge einfach den Anweisungen des Bots. Das musst du nur einmal für alle Repositories machen, die unsere CLA verwenden.

Dieses Projekt folgt dem [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Weitere Informationen findest du in den FAQ zum Code of Conduct oder kontaktiere [Email opencode](opencode@microsoft.com) bei Fragen oder Anmerkungen.

## Los geht's
Jetzt, da du die notwendigen Schritte für diesen Kurs abgeschlossen hast, lass uns mit einer [Einführung in Generative KI und LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst) beginnen.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ausgangssprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.