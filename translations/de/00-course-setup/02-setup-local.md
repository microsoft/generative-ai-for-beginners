<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f5cf0b10ab3c485e6334101f5784f1f3",
  "translation_date": "2025-12-19T12:46:43+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "de"
}
-->
# Lokale Einrichtung 🖥️

**Verwenden Sie diese Anleitung, wenn Sie alles auf Ihrem eigenen Laptop ausführen möchten.**  
Sie haben zwei Möglichkeiten: **(A) natives Python + virtual-env** oder **(B) VS Code Dev Container mit Docker**.  
Wählen Sie, was Ihnen einfacher erscheint – beide führen zu denselben Lektionen.

## 1. Voraussetzungen

| Werkzeug           | Version / Hinweise                                                                 |
|--------------------|-----------------------------------------------------------------------------------|
| **Python**         | 3.10 + (erhältlich unter <https://python.org>)                                    |
| **Git**            | Neueste Version (wird mit Xcode / Git für Windows / Linux-Paketmanager geliefert) |
| **VS Code**        | Optional, aber empfohlen <https://code.visualstudio.com>                          |
| **Docker Desktop** | *Nur* für Option B. Kostenlose Installation: <https://docs.docker.com/desktop/>   |

> 💡 **Tipp** – Überprüfen Sie die Werkzeuge im Terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. Option A – Natives Python (am schnellsten)

### Schritt 1  Klonen Sie dieses Repository

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Schritt 2 Erstellen & aktivieren Sie eine virtuelle Umgebung

```bash
python -m venv .venv          # mache eins
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Die Eingabeaufforderung sollte jetzt mit (.venv) beginnen – das bedeutet, Sie sind in der Umgebung.

### Schritt 3 Installieren Sie die Abhängigkeiten

```bash
pip install -r requirements.txt
```

Springen Sie zu Abschnitt 3 über [API-Schlüssel](../../../00-course-setup)

## 2. Option B – VS Code Dev Container (Docker)

Wir haben dieses Repository und den Kurs mit einem [Entwicklungscontainer](https://containers.dev?WT.mc_id=academic-105485-koreyst) eingerichtet, der eine universelle Laufzeitumgebung bietet, die Python3, .NET, Node.js und Java-Entwicklung unterstützt. Die zugehörige Konfiguration ist in der Datei `devcontainer.json` im Ordner `.devcontainer/` im Stammverzeichnis dieses Repositories definiert.

>**Warum diese Option wählen?**  
>Identische Umgebung wie Codespaces; keine Abhängigkeitsabweichungen.

### Schritt 0 Installieren Sie die Extras

Docker Desktop – bestätigen Sie, dass ```docker --version``` funktioniert.  
VS Code Remote – Containers Erweiterung (ID: ms-vscode-remote.remote-containers).

### Schritt 1 Öffnen Sie das Repository in VS Code

Datei ▸ Ordner öffnen… → generative-ai-for-beginners

VS Code erkennt `.devcontainer/` und zeigt eine Eingabeaufforderung an.

### Schritt 2 Im Container neu öffnen

Klicken Sie auf „Im Container neu öffnen“. Docker baut das Image (≈ 3 Min. beim ersten Mal).  
Wenn die Terminal-Eingabeaufforderung erscheint, sind Sie im Container.

## 2. Option C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ist ein leichter Installer zum Installieren von [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python sowie einiger Pakete.  
Conda selbst ist ein Paketmanager, der das Einrichten und Wechseln zwischen verschiedenen Python [**virtuellen Umgebungen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) und Paketen erleichtert. Es ist auch nützlich, um Pakete zu installieren, die nicht über `pip` verfügbar sind.

### Schritt 0  Installieren Sie Miniconda

Folgen Sie der [MiniConda-Installationsanleitung](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), um es einzurichten.

```bash
conda --version
```

### Schritt 1 Erstellen Sie eine virtuelle Umgebung

Erstellen Sie eine neue Umgebungsdatei (*environment.yml*). Wenn Sie mit Codespaces arbeiten, erstellen Sie diese im Verzeichnis `.devcontainer`, also `.devcontainer/environment.yml`.

### Schritt 2  Füllen Sie Ihre Umgebungsdatei

Fügen Sie den folgenden Ausschnitt zu Ihrer `environment.yml` hinzu

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

### Schritt 3 Erstellen Sie Ihre Conda-Umgebung

Führen Sie die folgenden Befehle in Ihrer Kommandozeile/Terminal aus

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer-Unterpfad gilt nur für Codespace-Einrichtungen
conda activate ai4beg
```

Siehe die [Conda-Umgebungsanleitung](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst), falls Probleme auftreten.

## 2  Option D – Klassisches Jupyter / Jupyter Lab (im Browser)

> **Für wen ist das??**  
> Für alle, die die klassische Jupyter-Oberfläche lieben oder Notebooks ohne VS Code ausführen möchten.

### Schritt 1  Stellen Sie sicher, dass Jupyter installiert ist

Um Jupyter lokal zu starten, öffnen Sie das Terminal/die Eingabeaufforderung, navigieren Sie zum Kursverzeichnis und führen Sie aus:

```bash
jupyter notebook
```

oder

```bash
jupyterhub
```

Dies startet eine Jupyter-Instanz, und die URL zum Zugriff wird im Befehlszeilenfenster angezeigt.

Sobald Sie die URL aufrufen, sollten Sie die Kursübersicht sehen und zu jeder `*.ipynb`-Datei navigieren können. Zum Beispiel `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Fügen Sie Ihre API-Schlüssel hinzu

Es ist wichtig, Ihre API-Schlüssel sicher aufzubewahren, wenn Sie eine Anwendung entwickeln. Wir empfehlen, keine API-Schlüssel direkt im Code zu speichern. Das Hochladen dieser Details in ein öffentliches Repository kann zu Sicherheitsproblemen und unerwünschten Kosten führen, wenn sie von Dritten missbraucht werden.  
Hier eine Schritt-für-Schritt-Anleitung, wie Sie eine `.env`-Datei für Python erstellen und den `GITHUB_TOKEN` hinzufügen:

1. **Navigieren Sie zu Ihrem Projektverzeichnis**: Öffnen Sie Ihr Terminal oder die Eingabeaufforderung und wechseln Sie in das Stammverzeichnis Ihres Projekts, in dem Sie die `.env`-Datei erstellen möchten.

   ```bash
   cd path/to/your/project
   ```

2. **Erstellen Sie die `.env`-Datei**: Verwenden Sie Ihren bevorzugten Texteditor, um eine neue Datei namens `.env` zu erstellen. Wenn Sie die Kommandozeile verwenden, können Sie `touch` (unter Unix-basierten Systemen) oder `echo` (unter Windows) verwenden:

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

4. **Speichern Sie die Datei**: Speichern Sie die Änderungen und schließen Sie den Texteditor.

5. **Installieren Sie `python-dotenv`**: Falls noch nicht geschehen, müssen Sie das Paket `python-dotenv` installieren, um Umgebungsvariablen aus der `.env`-Datei in Ihre Python-Anwendung zu laden. Sie können es mit `pip` installieren:

   ```bash
   pip install python-dotenv
   ```

6. **Laden Sie Umgebungsvariablen in Ihrem Python-Skript**: Verwenden Sie in Ihrem Python-Skript das Paket `python-dotenv`, um die Umgebungsvariablen aus der `.env`-Datei zu laden:

   ```python
   from dotenv import load_dotenv
   import os

   # Lade Umgebungsvariablen aus der .env-Datei
   load_dotenv()

   # Greife auf die GITHUB_TOKEN-Variable zu
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Das war’s! Sie haben erfolgreich eine `.env`-Datei erstellt, Ihren GitHub-Token hinzugefügt und in Ihre Python-Anwendung geladen.

🔐 Niemals .env committen – es steht bereits in .gitignore.  
Vollständige Anbieteranweisungen finden Sie in [`providers.md`](03-providers.md).

## 4. Was kommt als Nächstes?

| Ich möchte…          | Gehe zu…                                                                |
|----------------------|-------------------------------------------------------------------------|
| Lektion 1 starten    | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Einen LLM-Anbieter einrichten | [`providers.md`](03-providers.md)                                       |
| Andere Lernende treffen | [Tritt unserem Discord bei](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Fehlerbehebung

| Symptom                                   | Lösung                                                          |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Fügen Sie Python zum PATH hinzu oder öffnen Sie das Terminal nach der Installation neu |
| `pip` kann keine Wheels bauen (Windows)  | `pip install --upgrade pip setuptools wheel` und erneut versuchen |
| `ModuleNotFoundError: dotenv`             | Führen Sie `pip install -r requirements.txt` aus (Umgebung wurde nicht installiert) |
| Docker-Build schlägt fehl *Kein Speicherplatz* | Docker Desktop ▸ *Einstellungen* ▸ *Ressourcen* → Festplattengröße erhöhen |
| VS Code fordert ständig zum erneuten Öffnen auf | Möglicherweise sind beide Optionen aktiv; wählen Sie eine (venv **oder** Container) |
| OpenAI 401 / 429 Fehler                   | Überprüfen Sie den Wert von `OPENAI_API_KEY` / Anfragelimits     |
| Fehler bei Verwendung von Conda           | Installieren Sie Microsoft AI-Bibliotheken mit `conda install -c microsoft azure-ai-ml` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->