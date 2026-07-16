# AGENTS.md

## Projektübersicht

Dieses Repository enthält einen umfassenden 21-Lektionen-Lehrplan, der die Grundlagen der Generativen KI und die Anwendungsentwicklung vermittelt. Der Kurs ist für Anfänger konzipiert und deckt alles ab, von den Grundkonzepten bis hin zum Aufbau produktionsreifer Anwendungen.

**Wichtige Technologien:**
- Python 3.9+ mit Bibliotheken: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript mit Node.js und Bibliotheken: `openai` (Azure OpenAI über den v1-Endpunkt + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Modelle)
- Azure OpenAI Service, OpenAI API und Microsoft Foundry Modelle (GitHub Models wird Ende Juli 2026 eingestellt)
- Jupyter Notebooks für interaktives Lernen
- Dev Containers für eine konsistente Entwicklungsumgebung

**Repository-Struktur:**
- 21 nummerierte Lektionen-Verzeichnisse (00-21) mit READMEs, Codebeispielen und Aufgaben
- Mehrere Implementierungen: Python, TypeScript und manchmal .NET-Beispiele
- Übersetzungsverzeichnis mit über 40 Sprachversionen
- Zentrale Konfiguration über `.env`-Datei (verwenden Sie `.env.copy` als Vorlage)

## Setup-Befehle

### Ersteinrichtung des Repositories

```bash
# Klonen Sie das Repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Vorlage für die Umgebung kopieren
cp .env.copy .env
# Bearbeiten Sie die .env mit Ihren API-Schlüsseln und Endpunkten
```

### Python-Umgebung einrichten

```bash
# Virtuelle Umgebung erstellen
python3 -m venv venv

# Virtuelle Umgebung aktivieren
# Auf macOS/Linux:
source venv/bin/activate
# Auf Windows:
venv\Scripts\activate

# Abhängigkeiten installieren
pip install -r requirements.txt
```

### Node.js/TypeScript Setup

```bash
# Installieren Sie Abhängigkeiten auf Root-Ebene (für Dokumentationswerkzeuge)
npm install

# Für einzelne TypeScript-Beispiele zu Lektionen navigieren Sie zur jeweiligen Lektion:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container Setup (empfohlen)

Das Repository enthält eine `.devcontainer`-Konfiguration für GitHub Codespaces oder VS Code Dev Containers:

1. Repository in GitHub Codespaces oder VS Code mit Dev Containers-Erweiterung öffnen
2. Der Dev Container wird automatisch:
   - Python-Abhängigkeiten aus `requirements.txt` installieren
   - Post-Create-Skript ausführen (`.devcontainer/post-create.sh`)
   - Jupyter-Kernel einrichten

## Entwicklungsworkflow

### Umgebungsvariablen

Alle Lektionen, die API-Zugang benötigen, verwenden in `.env` definierte Umgebungsvariablen:

- `OPENAI_API_KEY` - Für OpenAI API
- `AZURE_OPENAI_API_KEY` - Für Azure OpenAI in Microsoft Foundry (Azure OpenAI Service ist jetzt Teil von Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI Endpunkt-URL (Foundry-Ressourcenendpunkt)
- `AZURE_OPENAI_DEPLOYMENT` - Name des Chat-Completion-Modell-Deployments
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Name des Embeddings-Modell-Deployments
- `AZURE_OPENAI_API_VERSION` - API-Version (Standard: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Für Hugging Face Modelle
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry Modelle Endpunkt (Multi-Provider Modellkatalog)
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry Modelle API-Schlüssel (ersetzt den auslaufenden `GITHUB_TOKEN`)

### Ausführen von Python-Beispielen

```bash
# Navigiere zum Lektionenverzeichnis
cd 06-text-generation-apps/python

# Führe ein Python-Skript aus
python aoai-app.py
```

### Ausführen von TypeScript-Beispielen

```bash
# Zum TypeScript-App-Verzeichnis navigieren
cd 06-text-generation-apps/typescript/recipe-app

# Den TypeScript-Code erstellen
npm run build

# Die Anwendung ausführen
npm start
```

### Ausführen von Jupyter Notebooks

```bash
# Jupyter im Repository-Stammverzeichnis starten
jupyter notebook

# Oder VS Code mit Jupyter-Erweiterung verwenden
```

### Arbeiten mit verschiedenen Lektionstypen

- **"Learn"-Lektionen**: Fokus auf README.md-Dokumentation und Konzepte
- **"Build"-Lektionen**: Enthalten funktionierenden Code in Python und TypeScript
- Jede Lektion hat ein README.md mit Theorie, Code-Durchgängen und Links zu Videoinhalten

## Code Style Richtlinien

### Python

- Verwendung von `python-dotenv` für Umgebungsvariablen-Management
- Import der `openai`-Bibliothek für API-Interaktionen
- Nutzung von `pylint` zum Linting (einige Beispiele enthalten `# pylint: disable=all` zur Vereinfachung)
- Befolgung der PEP 8 Namenskonventionen
- API-Zugangsdaten in `.env`-Datei speichern, niemals im Code

### TypeScript

- Verwendung des `dotenv`-Pakets für Umgebungsvariablen
- TypeScript-Konfiguration in `tsconfig.json` für jede App
- Nutzung des `openai`-Pakets für Azure OpenAI (Client auf `/openai/v1/` Endpunkt stellen und `client.responses.create` aufrufen); Nutzung von `@azure-rest/ai-inference` für Microsoft Foundry Modelle
- `nodemon` für Entwicklung mit Auto-Neuladen verwenden
- Vor dem Ausführen kompilieren: `npm run build` dann `npm start`

### Allgemeine Konventionen

- Codebeispiele einfach und lehrreich halten
- Kommentare einfügen, die zentrale Konzepte erklären
- Code jeder Lektion sollte eigenständig und ausführbar sein
- Einheitliche Benennung verwenden: `aoai-` Präfix für Azure OpenAI, `oai-` für OpenAI API, `githubmodels-` für Microsoft Foundry Modelle (älteres Präfix aus der GitHub Models Zeit)

## Dokumentationsrichtlinien

### Markdown-Stil

- Alle URLs müssen im Format `[text](../../url)` ohne zusätzliche Leerzeichen eingebunden werden
- Relative Links müssen mit `./` oder `../` beginnen
- Alle Links zu Microsoft-Domains müssen eine Tracking-ID enthalten: `?WT.mc_id=academic-105485-koreyst`
- Keine länderspezifischen Lokalisierungen in URLs (kein `/en-us/`)
- Bilder im Ordner `./images` mit aussagekräftigen Namen speichern
- Dateinamen mit englischen Zeichen, Zahlen und Bindestrichen verwenden

### Übersetzungsunterstützung

- Repository unterstützt über 40 Sprachen durch automatisierte GitHub Actions
- Übersetzungen im Verzeichnis `translations/` gespeichert
- Keine Teilübersetzungen einreichen
- Maschinelle Übersetzungen sind nicht akzeptiert
- Übersetzte Bilder im Verzeichnis `translated_images/` abgelegt

## Testen und Validierung

### Vor der Einreichung

Dieses Repository nutzt GitHub Actions zur Validierung. Vor dem Einreichen von Pull Requests:

1. **Markdown-Links prüfen**:
   ```bash
   # Der Workflow validate-markdown.yml überprüft:
   # - Defekte relative Pfade
   # - Fehlende Tracking-IDs bei Pfaden
   # - Fehlende Tracking-IDs bei URLs
   # - URLs mit Länderkürzel
   # - Defekte externe URLs
   ```

2. **Manuelles Testen**:
   - Python-Beispiele testen: Venv aktivieren und Skripte ausführen
   - TypeScript-Beispiele testen: `npm install`, `npm run build`, `npm start`
   - Prüfen, ob Umgebungsvariablen korrekt konfiguriert sind
   - Überprüfen, dass API-Schlüssel mit den Codebeispielen funktionieren

3. **Codebeispiele**:
   - Sicherstellen, dass der gesamte Code fehlerfrei läuft
   - Test mit sowohl Azure OpenAI als auch OpenAI API, sofern relevant
   - Überprüfen, dass Beispiele mit Microsoft Foundry Modellen funktionieren, wo unterstützt

### Keine automatisierten Tests

Dies ist ein Bildungs-Repository mit Fokus auf Tutorials und Beispiele. Es gibt keine Unit- oder Integrationstests. Die Validierung erfolgt hauptsächlich durch:
- Manuelles Testen der Codebeispiele
- GitHub Actions für Markdown-Validierung
- Community-Review der Bildungsinhalte

## Pull-Request-Richtlinien

### Vor dem Einreichen

1. Codeänderungen in Python und TypeScript testen, falls relevant
2. Markdown-Validierung ausführen (wird bei PR automatisch ausgelöst)
3. Sicherstellen, dass Tracking-IDs auf allen Microsoft-URLs vorhanden sind
4. Überprüfen, dass relative Links gültig sind
5. Prüfen, ob Bilder korrekt referenziert werden

### PR-Titel-Format

- Deskriptive Titel verwenden: `[Lesson 06] Korrigiere Tippfehler im Python-Beispiel` oder `README für Lektion 08 aktualisieren`
- Issue-Nummern referenzieren, wenn zutreffend: `Fixes #123`

### PR-Beschreibung

- Erklären, was geändert wurde und warum
- Links zu verwandten Issues einfügen
- Für Codeänderungen angeben, welche Beispiele getestet wurden
- Für Übersetzungs-PRs alle Dateien für eine vollständige Übersetzung einschließen

### Anforderungen für Beiträge

- Microsoft-CLA unterschreiben (automatisch beim ersten PR)
- Repository vor Änderungen auf das eigene Konto forken
- Pro logischer Änderung ein PR (keine Kombination von thematisch nicht verwandten Fixes)
- PRs möglichst fokussiert und klein halten

## Häufige Workflows

### Hinzufügen eines neuen Codebeispiels

1. In das entsprechende Lektionenverzeichnis navigieren
2. Beispiel im Unterverzeichnis `python/` oder `typescript/` erstellen
3. Benennungskonvention folgen: `{provider}-{example-name}.{py|ts|js}`
4. Mit echten API-Zugangsdaten testen
5. Neue Umgebungsvariablen im Lektionen-README dokumentieren

### Aktualisieren der Dokumentation

1. README.md im Lektionenverzeichnis bearbeiten
2. Markdown-Richtlinien befolgen (Tracking-IDs, relative Links)
3. Übersetzungen werden durch GitHub Actions verwaltet (nicht manuell bearbeiten)
4. Alle Links auf Gültigkeit prüfen

### Arbeiten mit Dev Containers

1. Repository enthält `.devcontainer/devcontainer.json`
2. Post-Create-Skript installiert Python-Abhängigkeiten automatisch
3. Erweiterungen für Python und Jupyter sind vorkonfiguriert
4. Umgebung basiert auf `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Deployment und Veröffentlichung

Dies ist ein Lern-Repository – es gibt keinen Bereitstellungsprozess. Der Lehrplan wird konsumiert über:

1. **GitHub Repository**: Direkter Zugriff auf Code und Dokumentation
2. **GitHub Codespaces**: Sofortige Entwicklungsumgebung mit vorkonfigurierter Einrichtung
3. **Microsoft Learn**: Inhalte können auf der offiziellen Lernplattform bereitgestellt werden
4. **docsify**: Dokumentationswebsite, gebaut aus Markdown (siehe `docsifytopdf.js` und `package.json`)

### Erstellen der Dokumentationsseite

```bash
# PDF aus der Dokumentation generieren (falls erforderlich)
npm run convert
```

## Fehlerbehebung

### Häufige Probleme

**Python Importfehler**:
- Sicherstellen, dass die virtuelle Umgebung aktiviert ist
- `pip install -r requirements.txt` ausführen
- Überprüfen, dass Python-Version 3.9+ ist

**TypeScript Build-Fehler**:
- `npm install` im jeweiligen App-Verzeichnis ausführen
- Node.js-Version auf Kompatibilität prüfen
- `node_modules` löschen und ggf. neu installieren

**API-Authentifizierungsfehler**:
- Prüfen, ob `.env`-Datei existiert und korrekte Werte enthält
- Überprüfen, ob API-Schlüssel gültig und nicht abgelaufen sind
- Sicherstellen, dass Endpunkt-URLs für die eigene Region richtig sind

**Fehlende Umgebungsvariablen**:
- Kopiere `.env.copy` nach `.env`
- Alle erforderlichen Werte für die jeweilige Lektion ausfüllen
- Applikation nach `.env`-Aktualisierung neu starten

## Zusätzliche Ressourcen

- [Kurs-Setup-Anleitung](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Beitragsrichtlinien](./CONTRIBUTING.md)
- [Verhaltenskodex](./CODE_OF_CONDUCT.md)
- [Sicherheitsrichtlinie](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Sammlung fortgeschrittener Codebeispiele](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Projektspezifische Hinweise

- Dies ist ein **Bildungs-Repository**, das auf Lernen ausgerichtet ist, nicht auf Produktionscode
- Beispiele sind absichtlich einfach und konzentrieren sich auf das Vermitteln von Konzepten
- Codequalität wird mit pädagogischer Klarheit abgewogen
- Jede Lektion ist eigenständig und kann unabhängig abgeschlossen werden
- Das Repository unterstützt mehrere API-Anbieter: Azure OpenAI, OpenAI, Microsoft Foundry Modelle und Offline-Anbieter wie Foundry Local und Ollama
- Inhalte sind mehrsprachig mit automatisierten Übersetzungs-Workflows
- Aktive Community auf Discord für Fragen und Unterstützung

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->