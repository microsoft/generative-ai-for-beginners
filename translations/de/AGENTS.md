# AGENTS.md

## Projektübersicht

Dieses Repository enthält einen umfassenden Lehrplan mit 21 Lektionen, der die Grundlagen der Generativen KI und die Anwendungsentwicklung vermittelt. Der Kurs ist für Anfänger konzipiert und deckt alles von den Grundkonzepten bis hin zum Aufbau produktionsreifer Anwendungen ab.

**Wichtige Technologien:**
- Python 3.9+ mit Bibliotheken: `openai`, `python-dotenv`, `tiktoken`, `azure-ai-inference`, `pandas`, `numpy`, `matplotlib`
- TypeScript/JavaScript mit Node.js und Bibliotheken: `openai` (Azure OpenAI über den v1-Endpunkt + Responses API), `@azure-rest/ai-inference` (Microsoft Foundry Modelle)
- Azure OpenAI Service, OpenAI API und Microsoft Foundry Modelle (GitHub Models wird Ende Juli 2026 eingestellt)
- Jupyter Notebooks für interaktives Lernen
- Dev Containers für eine konsistente Entwicklungsumgebung

**Repository-Struktur:**
- 21 nummerierte Lektion-Ordner (00-21) mit READMEs, Code-Beispielen und Aufgaben
- Mehrere Implementierungen: Python, TypeScript und manchmal .NET Beispiele
- Übersetzungsverzeichnis mit 40+ Sprachversionen
- Zentrale Konfiguration über `.env` Datei (verwenden Sie `.env.copy` als Vorlage)

## Einrichtungsbefehle

### Erste Repository-Einrichtung

```bash
# Klonen Sie das Repository
git clone https://github.com/microsoft/generative-ai-for-beginners.git
cd generative-ai-for-beginners

# Kopiere die Umgebungs-Vorlage
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

### Node.js/TypeScript-Einrichtung

```bash
# Installieren Sie Abhängigkeiten auf Root-Ebene (für Dokumentationstools)
npm install

# Für einzelne TypeScript-Beispiele zu Lektionen navigieren Sie zur jeweiligen Lektion:
cd 06-text-generation-apps/typescript/recipe-app
npm install
```

### Dev Container Einrichtung (Empfohlen)

Das Repository beinhaltet eine `.devcontainer`-Konfiguration für GitHub Codespaces oder VS Code Dev Containers:

1. Repository in GitHub Codespaces oder VS Code mit Dev Containers-Erweiterung öffnen
2. Dev Container wird automatisch:
   - Python-Abhängigkeiten aus `requirements.txt` installieren
   - Post-Create-Skript ausführen (`.devcontainer/post-create.sh`)
   - Jupyter Kernel einrichten

## Entwicklungsablauf

### Umgebungsvariablen

Alle Lektionen, die API-Zugriff benötigen, verwenden Umgebungsvariablen, die in `.env` definiert sind:

- `OPENAI_API_KEY` - Für OpenAI API
- `AZURE_OPENAI_API_KEY` - Für Azure OpenAI in Microsoft Foundry (Azure OpenAI Service ist jetzt Teil von Microsoft Foundry: https://ai.azure.com)
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI Endpunkt-URL (Foundry Ressource Endpunkt)
- `AZURE_OPENAI_DEPLOYMENT` - Chat Completion Modell Deployment Name (Kursstandard: `gpt-5-mini`)
- `AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT` - Embeddings Modell Deployment Name (Kursstandard: `text-embedding-3-small`)
- `AZURE_OPENAI_API_VERSION` - API Version (Standard: `2024-10-21`)
- `HUGGING_FACE_API_KEY` - Für Hugging Face Modelle
- `AZURE_INFERENCE_ENDPOINT` - Microsoft Foundry Models Endpunkt (Multi-Provider Model-Katalog)
- `AZURE_INFERENCE_CREDENTIAL` - Microsoft Foundry Models API Schlüssel (ersetzt das auslaufende `GITHUB_TOKEN`)
- `AZURE_INFERENCE_CHAT_MODEL` - Ein Nicht-Reasoning-Modell (z.B. `Llama-3.3-70B-Instruct`), das für die `temperature` Beispiele verwendet wird, da Reasoning-Modelle keine Sampling-Kontrollen unterstützen

### Modell-Konventionen (wichtig)

- **Standard-Chatmodell ist `gpt-5-mini`** - ein aktuelles, nicht veraltetes **Reasoning**-Modell. Ab 2026 werden die älteren temperaturfähigen "mini" Modelle (`gpt-4o-mini`, `gpt-4.1-mini`) *ausgephast*, daher verwendet der Lehrplan die GPT-5 Familie.
- **Reasoning-Modelle lehnen `temperature` und `top_p` ab**, und verwenden stattdessen `max_output_tokens` (Responses API) / `max_completion_tokens` (Chat Completions) anstelle von `max_tokens`. Fügen Sie **nicht** `temperature`/`top_p`/`max_tokens` in Beispiele ein, die `gpt-5-mini` aufrufen.
- **Um `temperature` zu demonstrieren**, verwenden Beispiele ein **Llama** Modell (`Llama-3.3-70B-Instruct`) über den Microsoft Foundry Models Endpunkt (`AZURE_INFERENCE_CHAT_MODEL`). Steuern Sie Reasoning-Modelle lieber mit Prompt Engineering + Reasoning-Kontrollen anstelle von Sampling-Reglern.
- **Feinabstimmung (Lektion 18)** verwendet weiterhin `gpt-4.1-mini`: GPT-5 unterstützt nur Verstärkungsfeinabstimmung (RFT), nicht die dort gezeigte überwachte Feinabstimmung (SFT).
- Lektionen 20 (Mistral) und 21 (Meta) behalten `temperature`/`max_tokens` bei, da sie Mistral/Llama Modelle ansprechen, welche diese unterstützen.

### Ausführen von Python-Beispielen

```bash
# Navigiere zum Unterrichtsverzeichnis
cd 06-text-generation-apps/python

# Führe ein Python-Skript aus
python aoai-app.py
```

### Ausführen von TypeScript-Beispielen

```bash
# Navigiere zum TypeScript-App-Verzeichnis
cd 06-text-generation-apps/typescript/recipe-app

# Baue den TypeScript-Code
npm run build

# Starte die Anwendung
npm start
```

### Ausführen von Jupyter Notebooks

```bash
# Starte Jupyter im Wurzelverzeichnis des Repositories
jupyter notebook

# Oder verwende VS Code mit der Jupyter-Erweiterung
```

### Arbeiten mit verschiedenen Lektionstypen

- **"Learn" Lektionen**: Fokus auf README.md Dokumentation und Konzepte
- **"Build" Lektionen**: Enthalten funktionierenden Code in Python und TypeScript
- Jede Lektion hat ein README.md mit Theorie, Code-Erklärungen und Links zu Video-Inhalten

## Code-Stil Richtlinien

### Python

- Verwendung von `python-dotenv` zur Verwaltung von Umgebungsvariablen
- Import der `openai` Bibliothek für API-Interaktionen
- Verwendung von `pylint` zum Linting (einige Beispiele enthalten `# pylint: disable=all` zur Vereinfachung)
- Folgen Sie den Namenskonventionen von PEP 8
- API-Anmeldedaten in `.env` Datei speichern, niemals im Code

### TypeScript

- Verwendung des `dotenv` Pakets für Umgebungsvariablen
- TypeScript-Konfiguration in `tsconfig.json` für jede App
- Verwendung des `openai` Pakets für Azure OpenAI (Client zeigt auf `/openai/v1/` Endpunkt und nutzt `client.responses.create`); Verwendung von `@azure-rest/ai-inference` für Microsoft Foundry Modelle
- Verwendung von `nodemon` für Entwicklung mit automatischem Reload
- Vor dem Ausführen bauen: `npm run build` dann `npm start`

### Allgemeine Konventionen

- Halten Sie Code-Beispiele einfach und lehrreich
- Kommentare einfügen, die wichtige Konzepte erklären
- Der Code jeder Lektion sollte eigenständig und ausführbar sein
- Konsistente Namensgebung: `aoai-` Präfix für Azure OpenAI, `oai-` für OpenAI API, `githubmodels-` für Microsoft Foundry Modelle (Legacy-Präfix aus der GitHub Models Ära)

## Dokumentationsrichtlinien

### Markdown-Stil

- Alle URLs müssen im Format `[Text](../../URL)` ohne zusätzliches Leerzeichen eingebettet sein
- Relative Links müssen mit `./` oder `../` beginnen
- Alle Links zu Microsoft-Domains müssen eine Tracking-ID enthalten: `?WT.mc_id=academic-105485-koreyst`
- Vermeiden Sie länderspezifische Lokalisierungen in URLs (vermeiden Sie `/en-us/`)
- Bilder im Ordner `./images` mit beschreibenden Namen speichern
- Verwenden Sie im Dateinamen englische Buchstaben, Zahlen und Bindestriche

### Übersetzungsunterstützung

- Das Repository unterstützt über 40 Sprachen über automatisierte GitHub Actions
- Übersetzungen werden im Verzeichnis `translations/` gespeichert
- Bitte keine teilweisen Übersetzungen einreichen
- Maschinelle Übersetzungen werden nicht akzeptiert
- Übersetzte Bilder werden im Verzeichnis `translated_images/` gespeichert

## Tests und Validierung

### Vor dem Einreichen prüfen

Dieses Repository verwendet GitHub Actions zur Validierung. Vor dem Einreichen von PRs:

1. **Markdown Links prüfen**:
   ```bash
   # Der Workflow validate-markdown.yml überprüft:
   # - Fehlerhafte relative Pfade
   # - Fehlende Tracking-IDs bei Pfaden
   # - Fehlende Tracking-IDs bei URLs
   # - URLs mit Landeslokalisierung
   # - Fehlerhafte externe URLs
   ```

2. **Manuelles Testen**:
   - Testen Sie Python-Beispiele: Aktivieren Sie venv und führen Sie Skripte aus
   - Testen Sie TypeScript-Beispiele: `npm install`, `npm run build`, `npm start`
   - Verifizieren Sie, dass Umgebungsvariablen korrekt konfiguriert sind
   - Prüfen Sie, dass API-Schlüssel mit den Code-Beispielen funktionieren

3. **Code-Beispiele**:
   - Stellen Sie sicher, dass allen Code fehlerfrei läuft
   - Testen Sie sowohl mit Azure OpenAI als auch OpenAI API, wenn zutreffend
   - Verifizieren Sie, dass Beispiele mit Microsoft Foundry Modellen funktionieren, sofern unterstützt

### Keine automatischen Tests

Dies ist ein edukatives Repository, das sich auf Tutorials und Beispiele konzentriert. Es gibt keine Unit- oder Integrationstests zum Ausführen. Validierung erfolgt hauptsächlich durch:
- Manuelles Testen der Code-Beispiele
- GitHub Actions zur Markdown-Validierung
- Community-Review der Bildungsinhalte

## Pull Request Richtlinien

### Vor dem Einreichen

1. Ändern Sie Code und testen Sie in Python und TypeScript, wenn zugänglich
2. Führen Sie die Markdown-Validierung aus (wird automatisch beim PR ausgelöst)
3. Stellen Sie sicher, dass Tracking-IDs für alle Microsoft URLs vorhanden sind
4. Prüfen Sie, dass relative Links gültig sind
5. Verifizieren Sie die korrekte Referenzierung von Bildern

### PR-Titel-Format

- Verwenden Sie aussagekräftige Titel: `[Lesson 06] Fix Python example typo` oder `Update README for lesson 08`
- Verweisen Sie auf Issue-Nummern, wenn zutreffend: `Fixes #123`

### PR-Beschreibung

- Erklären Sie, was geändert wurde und warum
- Verlinken Sie zu verwandten Issues
- Für Codeänderungen spezifizieren Sie, welche Beispiele getestet wurden
- Für Übersetzungs-PRs fügen Sie alle Dateien für eine vollständige Übersetzung hinzu

### Beitragserfordernisse

- Unterzeichnen Sie die Microsoft CLA (automatisch beim ersten PR)
- Forken Sie das Repository in Ihr Konto, bevor Sie Änderungen vornehmen
- Ein PR pro logische Änderung (nicht unrelated fixes kombinieren)
- Halten Sie PRs fokussiert und möglichst klein

## Übliche Arbeitsabläufe

### Hinzufügen eines neuen Code-Beispiels

1. Navigieren Sie zum passenden Lektion-Ordner
2. Erstellen Sie Beispiel im `python/` oder `typescript/` Unterverzeichnis
3. Folgen Sie der Namenskonvention: `{provider}-{example-name}.{py|ts|js}`
4. Testen Sie mit echten API-Zugangsdaten
5. Dokumentieren Sie alle neuen Umgebungsvariablen im Lektion README

### Aktualisieren der Dokumentation

1. Bearbeiten Sie README.md im Lektion-Ordner
2. Befolgen Sie die Markdown-Richtlinien (Tracking-IDs, relative Links)
3. Übersetzungen werden von GitHub Actions verwaltet (nicht manuell bearbeiten)
4. Testen Sie, dass alle Links gültig sind

### Arbeiten mit Dev Containers

1. Repository enthält `.devcontainer/devcontainer.json`
2. Post-Create-Skript installiert Python-Abhängigkeiten automatisch
3. Erweiterungen für Python und Jupyter sind vorkonfiguriert
4. Die Umgebung basiert auf `mcr.microsoft.com/devcontainers/universal:2.11.2`

## Deployment und Veröffentlichung

Dies ist ein Lern-Repository - es gibt keinen Deployment-Prozess. Der Lehrplan wird genutzt über:

1. **GitHub Repository**: Direkter Zugriff auf Code und Dokumentation
2. **GitHub Codespaces**: Sofortige Entwicklungsumgebung mit vorkonfigurierter Einrichtung
3. **Microsoft Learn**: Inhalte können auf der offiziellen Lernplattform bereitgestellt werden
4. **docsify**: Dokumentationsseite aus Markdown gebaut (siehe `docsifytopdf.js` und `package.json`)

### Erstellen der Dokumentationsseite

```bash
# PDF aus der Dokumentation erstellen (falls erforderlich)
npm run convert
```

## Fehlerbehebung

### Häufige Probleme

**Python Importfehler**:
- Stellen Sie sicher, dass die virtuelle Umgebung aktiviert ist
- Führen Sie `pip install -r requirements.txt` aus
- Überprüfen Sie, dass Python Version 3.9+ verwendet wird

**TypeScript Build-Fehler**:
- Führen Sie `npm install` im jeweiligen App-Verzeichnis aus
- Überprüfen Sie, ob die Node.js Version kompatibel ist
- Löschen Sie `node_modules` und installieren Sie bei Bedarf neu

**API-Authentifizierungsfehler**:
- Verifizieren Sie, dass `.env` Datei existiert und korrekte Werte enthält
- Überprüfen Sie, dass API-Schlüssel gültig und nicht abgelaufen sind
- Stellen Sie sicher, dass die Endpunkt-URLs für Ihre Region korrekt sind

**Fehlende Umgebungsvariablen**:
- Kopieren Sie `.env.copy` nach `.env`
- Füllen Sie alle erforderlichen Werte für die jeweilige Lektion aus
- Starten Sie Ihre Anwendung nach Aktualisierung der `.env` neu

## Zusätzliche Ressourcen

- [Kurs-Einrichtungsanleitung](./00-course-setup/README.md?WT.mc_id=academic-105485-koreyst)
- [Beitragsrichtlinien](./CONTRIBUTING.md)
- [Verhaltenskodex](./CODE_OF_CONDUCT.md)
- [Sicherheitspolitik](./SECURITY.md)
- [Azure AI Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)
- [Sammlung fortgeschrittener Code-Beispiele](https://aka.ms/genai-beg-code?WT.mc_id=academic-105485-koreyst)

## Projektspezifische Hinweise

- Dies ist ein **edukatives Repository**, das sich auf Lernen und nicht auf produktiven Code konzentriert
- Beispiele sind bewusst einfach gehalten und fokussieren auf die Vermittlung von Konzepten
- Die Codequalität ist ausgewogen zwischen Qualität und pädagogischer Klarheit
- Jede Lektion ist eigenständig und kann unabhängig abgeschlossen werden
- Das Repository unterstützt mehrere API-Anbieter: Azure OpenAI, OpenAI, Microsoft Foundry Modelle und Offline-Anbieter wie Foundry Local und Ollama
- Inhalte sind mehrsprachig mit automatisierten Übersetzungs-Workflows
- Aktive Community auf Discord für Fragen und Support

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->