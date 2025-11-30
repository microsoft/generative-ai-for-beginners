<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T13:42:58+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "de"
}
-->
# Lokale Einrichtung 🖥️

**Nutze diese Anleitung, wenn du alles auf deinem eigenen Laptop ausführen möchtest.**  
Du hast zwei Möglichkeiten: **(A) natives Python + virtual-env** oder **(B) VS Code Dev Container mit Docker**.  
Wähle einfach das, was dir leichter erscheint – beide Wege führen zu den gleichen Lektionen.

## 1. Voraussetzungen

| Tool               | Version / Hinweise                                                                      |
|--------------------|----------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (erhältlich unter <https://python.org>)                                          |
| **Git**            | Neueste Version (enthalten in Xcode / Git for Windows / Linux-Paketmanager)             |
| **VS Code**        | Optional, aber empfohlen <https://code.visualstudio.com>                                |
| **Docker Desktop** | *Nur* für Option B. Kostenlose Installation: <https://docs.docker.com/desktop/>         |

> 💡 **Tipp** – Überprüfe die Tools im Terminal:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2. Option A – Natives Python (am schnellsten)

### Schritt 1  Klone dieses Repository

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Schritt 2 Erstelle & aktiviere eine virtuelle Umgebung

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Die Eingabeaufforderung sollte jetzt mit (.venv) beginnen – das bedeutet, du bist in der Umgebung.

### Schritt 3 Installiere Abhängigkeiten

```bash
pip install -r requirements.txt
```

Springe zu Abschnitt 3 zu [API-Schlüsseln](../../../00-course-setup)

## 2. Option B – VS Code Dev Container (Docker)

Wir haben dieses Repository und den Kurs mit einem [Development Container](https://containers.dev?WT.mc_id=academic-105485-koreyst) eingerichtet, der eine universelle Laufzeitumgebung bietet und Python3, .NET, Node.js und Java-Entwicklung unterstützt. Die zugehörige Konfiguration ist in der Datei `devcontainer.json` im Ordner `.devcontainer/` im Wurzelverzeichnis dieses Repositories definiert.

>**Warum diese Option wählen?**
>Identische Umgebung wie Codespaces; keine Abweichungen bei Abhängigkeiten.

### Schritt 0 Installiere die Extras

Docker Desktop – prüfe, ob ```docker --version``` funktioniert.
VS Code Remote – Containers Erweiterung (ID: ms-vscode-remote.remote-containers).

### Schritt 1 Öffne das Repository in VS Code

Datei ▸ Ordner öffnen…  → generative-ai-for-beginners

VS Code erkennt .devcontainer/ und zeigt eine entsprechende Meldung an.

### Schritt 2 Im Container neu öffnen

Klicke auf „Im Container neu öffnen“. Docker baut das Image (≈ 3 Minuten beim ersten Mal).
Wenn die Terminal-Eingabe erscheint, bist du im Container.

## 2. Option C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) ist ein schlanker Installer für [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python und einige Pakete.
Conda selbst ist ein Paketmanager, der das Einrichten und Wechseln zwischen verschiedenen Python-[**virtuellen Umgebungen**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) und Paketen erleichtert. Außerdem ist es praktisch, um Pakete zu installieren, die nicht über `pip` verfügbar sind.

### Schritt 0  Installiere Miniconda

Folge der [MiniConda-Installationsanleitung](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst), um es einzurichten.

```bash
conda --version
```

### Schritt 1 Erstelle eine virtuelle Umgebung

Erstelle eine neue Umgebungsdatei (*environment.yml*). Wenn du Codespaces verwendest, erstelle diese im Verzeichnis `.devcontainer`, also `.devcontainer/environment.yml`.

### Schritt 2  Fülle deine Umgebungsdatei

Füge den folgenden Ausschnitt zu deiner `environment.yml` hinzu

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

### Schritt 3 Erstelle deine Conda-Umgebung

Führe die folgenden Befehle in deiner Kommandozeile/deinem Terminal aus

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Sieh dir den [Conda-Umgebungen-Guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) an, falls du auf Probleme stößt.

## 2  Option D – Klassisches Jupyter / Jupyter Lab (im Browser)

> **Für wen ist das?**  
> Für alle, die die klassische Jupyter-Oberfläche mögen oder Notebooks ohne VS Code ausführen möchten.  

### Schritt 1  Stelle sicher, dass Jupyter installiert ist

Um Jupyter lokal zu starten, öffne das Terminal/die Kommandozeile, navigiere zum Kursverzeichnis und führe aus:

```bash
jupyter notebook
```

oder

```bash
jupyterhub
```

Dadurch wird eine Jupyter-Instanz gestartet und die URL zum Zugriff wird im Terminal angezeigt.

Sobald du die URL aufrufst, solltest du die Kursübersicht sehen und zu jeder `*.ipynb`-Datei navigieren können. Zum Beispiel `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Füge deine API-Schlüssel hinzu

Es ist wichtig, deine API-Schlüssel sicher aufzubewahren, wenn du Anwendungen entwickelst. Wir empfehlen, keine API-Schlüssel direkt im Code zu speichern. Wenn du diese Details in ein öffentliches Repository eincheckst, kann das zu Sicherheitsproblemen und sogar zu unerwünschten Kosten führen, falls sie missbraucht werden.
Hier ist eine Schritt-für-Schritt-Anleitung, wie du eine `.env`-Datei für Python erstellst und den `GITHUB_TOKEN` hinzufügst:

1. **Wechsle in dein Projektverzeichnis**: Öffne dein Terminal oder die Eingabeaufforderung und navigiere in das Wurzelverzeichnis deines Projekts, wo du die `.env`-Datei erstellen möchtest.

   ```bash
   cd path/to/your/project
   ```

2. **Erstelle die `.env`-Datei**: Erstelle mit deinem bevorzugten Texteditor eine neue Datei namens `.env`. Wenn du die Kommandozeile verwendest, kannst du `touch` (auf Unix-Systemen) oder `echo` (unter Windows) nutzen:

   Unix-basierte Systeme:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Bearbeite die `.env`-Datei**: Öffne die `.env`-Datei in einem Texteditor (z.B. VS Code, Notepad++ oder einem anderen Editor). Füge folgende Zeile hinzu und ersetze `your_github_token_here` durch deinen echten GitHub-Token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Datei speichern**: Speichere die Änderungen und schließe den Editor.

5. **Installiere `python-dotenv`**: Falls noch nicht geschehen, installiere das Paket `python-dotenv`, um Umgebungsvariablen aus der `.env`-Datei in deine Python-Anwendung zu laden. Installiere es mit `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Lade Umgebungsvariablen in deinem Python-Skript**: Nutze in deinem Python-Skript das Paket `python-dotenv`, um die Umgebungsvariablen aus der `.env`-Datei zu laden:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Das war’s! Du hast erfolgreich eine `.env`-Datei erstellt, deinen GitHub-Token hinzugefügt und ihn in deine Python-Anwendung geladen.

🔐 Niemals .env committen – sie steht bereits in .gitignore.
Vollständige Anweisungen zu Anbietern findest du in [`providers.md`](03-providers.md).

## 4. Wie geht’s weiter?

| Ich möchte…         | Gehe zu…                                                                  |
|---------------------|---------------------------------------------------------------------------|
| Lektion 1 starten   | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)       |
| Einen LLM-Anbieter einrichten | [`providers.md`](03-providers.md)                                 |
| Andere Lernende treffen | [Tritt unserem Discord bei](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## 5. Fehlerbehebung

| Symptom                                   | Lösung                                                          |
|-------------------------------------------|-----------------------------------------------------------------|
| `python not found`                        | Füge Python zum PATH hinzu oder öffne das Terminal nach der Installation neu |
| `pip` kann keine Wheels bauen (Windows)   | `pip install --upgrade pip setuptools wheel` und erneut versuchen. |
| `ModuleNotFoundError: dotenv`             | Führe `pip install -r requirements.txt` aus (Umgebung war nicht installiert). |
| Docker-Build schlägt fehl *No space left* | Docker Desktop ▸ *Einstellungen* ▸ *Ressourcen* → Speicherplatz erhöhen. |
| VS Code fordert ständig zum Neuöffnen auf | Möglicherweise sind beide Optionen aktiv; wähle eine (venv **oder** Container)|
| OpenAI 401 / 429 Fehler                   | Überprüfe den Wert von `OPENAI_API_KEY` / Anfrage-Limits.       |
| Fehler bei der Verwendung von Conda       | Installiere Microsoft AI-Bibliotheken mit `conda install -c microsoft azure-ai-ml`|

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ausgangssprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.