<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "19b8d432e5ed3ab209641dd8dad643fb",
  "translation_date": "2025-10-03T10:50:51+00:00",
  "source_file": "AGENTS.md",
  "language_code": "de"
}
-->
# AGENTS.md

## Projektübersicht

Dieses Repository enthält einen umfassenden 21-Lektionen-Lehrplan, der die Grundlagen und Anwendungsentwicklung von Generativer KI vermittelt. Der Kurs ist für Anfänger konzipiert und behandelt alles von den grundlegenden Konzepten bis hin zum Aufbau produktionsreifer Anwendungen.

**Wichtige Technologien:**
- Python 3.9+ mit Bibliotheken: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript mit Node.js und Bibliotheken: `@azure/openai`, `@azure-rest/ai-inference`, `openai`
- Azure OpenAI Service, OpenAI API und GitHub Models
- Jupyter Notebooks für interaktives Lernen
- Dev Containers für eine konsistente Entwicklungsumgebung

**Repository-Struktur:**
- 21 nummerierte Lektionen-Verzeichnisse (00-21) mit READMEs, Codebeispielen und Aufgaben
- Mehrere Implementierungen: Python, TypeScript und manchmal .NET-Beispiele
- Übersetzungsverzeichnis mit Versionen in über 40 Sprachen
- Zentralisierte Konfiguration über `.env`-Datei (verwenden Sie `.env.copy` als Vorlage)

## Setup-Befehle

### Initiales Repository-Setup

```bash
# Clone the repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Copy environment template
cp .env.copy .env
# Edit .env with your API keys and endpoints
```

### Python-Umgebung einrichten

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Node.js/TypeScript-Setup

```bash
# Install root-level dependencies (for documentation tooling)
npm install

# For individual lesson TypeScript examples, navigate to the specific lesson:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container Setup (empfohlen)

Das Repository enthält eine `.devcontainer`-Konfiguration für GitHub Codespaces oder VS Code Dev Containers:

1. Öffnen Sie das Repository in GitHub Codespaces oder VS Code mit der Dev Containers-Erweiterung.
2. Der Dev Container wird automatisch:
   - Python-Abhängigkeiten aus `requirements.txt` installieren
   - Post-Creation-Skript ausführen (`.devcontainer/post-create.sh`)
   - Jupyter-Kernel einrichten

## Entwicklungsworkflow

### Umgebungsvariablen

Alle Lektionen, die API-Zugriff erfordern, verwenden Umgebungsvariablen, die in `.env` definiert sind:

- `OPENAI_API_KEY` - Für die OpenAI API
- `AZURE_OPENAI_API_KEY` - Für den Azure OpenAI Service
- `AZURE_OPENAI_ENDPOINT` - URL des Azure OpenAI-Endpunkts
- `AZURE_OPENAI_DEPLOYMENT` - Name der Bereitstellung des Chat-Vervollständigungsmodells
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Name der Bereitstellung des Embeddings-Modells
- `AZURE_OPENAI_API_VERSION` - API-Version (Standard: `2024-02-01`)
- `HUGGING_FACE_API_KEY` - Für Hugging Face-Modelle
- `GITHUB_TOKEN` - Für GitHub Models

### Python-Beispiele ausführen

```bash
# Navigate to lesson directory
cd 06-text-generation-apps/python

# Run a Python script
python aoai-app.py
```

### TypeScript-Beispiele ausführen

```bash
# Navigate to TypeScript app directory
cd 06-text-generation-apps/typescript/recipe-app

# Build the TypeScript code
npm run build

# Run the application
npm start
```

### Jupyter Notebooks ausführen

```bash
# Start Jupyter in the repository root
jupyter notebook

# Or use VS Code with Jupyter extension
```

### Arbeiten mit verschiedenen Lektionstypen

- **"Learn"-Lektionen**: Konzentrieren sich auf README.md-Dokumentation und Konzepte
- **"Build"-Lektionen**: Enthalten funktionierende Codebeispiele in Python und TypeScript
- Jede Lektion hat eine README.md mit Theorie, Code-Durchgängen und Links zu Videoinhalten

## Richtlinien für Code-Stil

### Python

- Verwenden Sie `python-dotenv` für die Verwaltung von Umgebungsvariablen
- Importieren Sie die `openai`-Bibliothek für API-Interaktionen
- Verwenden Sie `pylint` für Linting (einige Beispiele enthalten `# pylint: disable=all` der Einfachheit halber)
- Befolgen Sie die PEP 8-Namenskonventionen
- Speichern Sie API-Zugangsdaten in der `.env`-Datei, niemals im Code

### TypeScript

- Verwenden Sie das `dotenv`-Paket für Umgebungsvariablen
- TypeScript-Konfiguration in `tsconfig.json` für jede App
- Verwenden Sie `@azure/openai` oder `@azure-rest/ai-inference` für Azure-Dienste
- Verwenden Sie `nodemon` für die Entwicklung mit automatischem Reload
- Vor dem Ausführen bauen: `npm run build` und dann `npm start`

### Allgemeine Konventionen

- Halten Sie Codebeispiele einfach und lehrreich
- Fügen Sie Kommentare hinzu, die wichtige Konzepte erklären
- Der Code jeder Lektion sollte eigenständig und ausführbar sein
- Verwenden Sie konsistente Namensgebung: `aoai-` Präfix für Azure OpenAI, `oai-` für OpenAI API, `githubmodels-` für GitHub Models

## Richtlinien für Dokumentation

### Markdown-Stil

- Alle URLs müssen im Format `[Text](../../URL)` ohne zusätzliche Leerzeichen eingebettet sein
- Relative Links müssen mit `./` oder `../` beginnen
- Alle Links zu Microsoft-Domains müssen eine Tracking-ID enthalten: `?WT.mc_id=academic-105485-koreyst`
- Keine länderspezifischen Lokalisierungen in URLs (vermeiden Sie `/en-us/`)
- Bilder werden im Ordner `./images` mit beschreibenden Namen gespeichert
- Verwenden Sie englische Zeichen, Zahlen und Bindestriche in Dateinamen

### Unterstützung für Übersetzungen

- Das Repository unterstützt über 40 Sprachen durch automatisierte GitHub Actions
- Übersetzungen werden im Verzeichnis `translations/` gespeichert
- Reichen Sie keine unvollständigen Übersetzungen ein
- Maschinelle Übersetzungen werden nicht akzeptiert
- Übersetzte Bilder werden im Verzeichnis `translated_images/` gespeichert

## Tests und Validierung

### Vor der Einreichung

Dieses Repository verwendet GitHub Actions für die Validierung. Vor der Einreichung von PRs:

1. **Markdown-Links überprüfen**:
   ```bash
   # The validate-markdown.yml workflow checks:
   # - Broken relative paths
   # - Missing tracking IDs on paths
   # - Missing tracking IDs on URLs
   # - URLs with country locale
   # - Broken external URLs
   ```

2. **Manuelles Testen**:
   - Python-Beispiele testen: Aktivieren Sie venv und führen Sie Skripte aus
   - TypeScript-Beispiele testen: `npm install`, `npm run build`, `npm start`
   - Überprüfen Sie, ob Umgebungsvariablen korrekt konfiguriert sind
   - Stellen Sie sicher, dass API-Schlüssel mit den Codebeispielen funktionieren

3. **Codebeispiele**:
   - Stellen Sie sicher, dass alle Codes fehlerfrei ausgeführt werden
   - Testen Sie sowohl mit Azure OpenAI als auch mit OpenAI API, wenn zutreffend
   - Überprüfen Sie, ob Beispiele mit GitHub Models funktionieren, wo unterstützt

### Keine automatisierten Tests

Dies ist ein Bildungs-Repository, das sich auf Tutorials und Beispiele konzentriert. Es gibt keine Unit-Tests oder Integrationstests. Die Validierung erfolgt hauptsächlich durch:
- Manuelles Testen der Codebeispiele
- GitHub Actions für die Markdown-Validierung
- Community-Review der Bildungsinhalte

## Richtlinien für Pull Requests

### Vor der Einreichung

1. Testen Sie Codeänderungen sowohl in Python als auch in TypeScript, wenn zutreffend
2. Führen Sie die Markdown-Validierung aus (automatisch bei PR ausgelöst)
3. Stellen Sie sicher, dass Tracking-IDs in allen Microsoft-URLs vorhanden sind
4. Überprüfen Sie, ob relative Links gültig sind
5. Vergewissern Sie sich, dass Bilder korrekt referenziert werden

### Format des PR-Titels

- Verwenden Sie beschreibende Titel: `[Lesson 06] Fix Python example typo` oder `Update README for lesson 08`
- Verweisen Sie auf Issue-Nummern, wenn zutreffend: `Fixes #123`

### PR-Beschreibung

- Erklären Sie, was geändert wurde und warum
- Verlinken Sie zu verwandten Issues
- Für Codeänderungen angeben, welche Beispiele getestet wurden
- Für Übersetzungs-PRs alle Dateien für eine vollständige Übersetzung einfügen

### Anforderungen an Beiträge

- Microsoft CLA unterzeichnen (automatisch beim ersten PR)
- Repository vor Änderungen in Ihrem Konto forken
- Ein PR pro logischer Änderung (keine Kombination von nicht zusammenhängenden Fixes)
- Halten Sie PRs fokussiert und klein, wenn möglich

## Häufige Workflows

### Hinzufügen eines neuen Codebeispiels

1. Navigieren Sie zum entsprechenden Lektionen-Verzeichnis
2. Erstellen Sie ein Beispiel im Unterverzeichnis `python/` oder `typescript/`
3. Befolgen Sie die Namenskonvention: `{provider}-{example-name}.{py|ts|js}`
4. Testen Sie mit tatsächlichen API-Zugangsdaten
5. Dokumentieren Sie neue Umgebungsvariablen in der README der Lektion

### Aktualisierung der Dokumentation

1. Bearbeiten Sie README.md im Lektionen-Verzeichnis
2. Befolgen Sie die Markdown-Richtlinien (Tracking-IDs, relative Links)
3. Übersetzungen werden von GitHub Actions gehandhabt (nicht manuell bearbeiten)
4. Testen Sie, ob alle Links gültig sind

### Arbeiten mit Dev Containers

1. Das Repository enthält `.devcontainer/devcontainer.json`
2. Das Post-Creation-Skript installiert automatisch Python-Abhängigkeiten
3. Erweiterungen für Python und Jupyter sind vorkonfiguriert
4. Die Umgebung basiert auf `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Bereitstellung und Veröffentlichung

Dies ist ein Lern-Repository - es gibt keinen Bereitstellungsprozess. Der Lehrplan wird konsumiert durch:

1. **GitHub Repository**: Direkter Zugriff auf Code und Dokumentation
2. **GitHub Codespaces**: Sofortige Entwicklungsumgebung mit vorkonfiguriertem Setup
3. **Microsoft Learn**: Inhalte können auf der offiziellen Lernplattform syndiziert werden
4. **docsify**: Dokumentationsseite, die aus Markdown erstellt wird (siehe `docsifytopdf.js` und `package.json`)

### Dokumentationsseite erstellen

```bash
# Generate PDF from documentation (if needed)
npm run convert
```

## Fehlerbehebung

### Häufige Probleme

**Python-Importfehler**:
- Stellen Sie sicher, dass die virtuelle Umgebung aktiviert ist
- Führen Sie `pip install -r requirements.txt` aus
- Überprüfen Sie, ob die Python-Version 3.9+ ist

**TypeScript-Build-Fehler**:
- Führen Sie `npm install` im spezifischen App-Verzeichnis aus
- Überprüfen Sie, ob die Node.js-Version kompatibel ist
- Löschen Sie `node_modules` und installieren Sie neu, falls erforderlich

**API-Authentifizierungsfehler**:
- Überprüfen Sie, ob `.env` existiert und korrekte Werte enthält
- Stellen Sie sicher, dass API-Schlüssel gültig und nicht abgelaufen sind
- Überprüfen Sie, ob Endpunkt-URLs für Ihre Region korrekt sind

**Fehlende Umgebungsvariablen**:
- Kopieren Sie `.env.copy` nach `.env`
- Füllen Sie alle erforderlichen Werte für die Lektion aus, an der Sie arbeiten
- Starten Sie Ihre Anwendung nach dem Aktualisieren von `.env` neu

## Zusätzliche Ressourcen

- [Kurs-Setup-Anleitung](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Richtlinien für Beiträge](./CONTRIBUTING.md)
- [Verhaltenskodex](./CODE_OF_CONDUCT.md)
- [Sicherheitsrichtlinie](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Sammlung fortgeschrittener Codebeispiele](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Projektspezifische Hinweise

- Dies ist ein **Bildungs-Repository**, das sich auf Lernen und nicht auf Produktionscode konzentriert
- Beispiele sind absichtlich einfach und auf die Vermittlung von Konzepten ausgerichtet
- Die Codequalität wird mit der pädagogischen Klarheit abgewogen
- Jede Lektion ist eigenständig und kann unabhängig abgeschlossen werden
- Das Repository unterstützt mehrere API-Anbieter: Azure OpenAI, OpenAI und GitHub Models
- Inhalte sind mehrsprachig mit automatisierten Übersetzungs-Workflows
- Aktive Community auf Discord für Fragen und Unterstützung

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.