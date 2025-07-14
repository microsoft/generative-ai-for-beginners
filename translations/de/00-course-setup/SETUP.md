<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:21:22+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "de"
}
-->
# Richte Deine Entwicklungsumgebung ein

Wir haben dieses Repository und den Kurs mit einem [Development Container](https://containers.dev?WT.mc_id=academic-105485-koreyst) eingerichtet, der eine universelle Laufzeitumgebung bietet und die Entwicklung mit Python3, .NET, Node.js und Java unterstützt. Die zugehörige Konfiguration ist in der Datei `devcontainer.json` im Ordner `.devcontainer/` im Stammverzeichnis dieses Repositories definiert.

Um den Dev Container zu aktivieren, starte ihn in [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (für eine cloudbasierte Laufzeit) oder in [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (für eine lokal gehostete Laufzeit). Lies [diese Dokumentation](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) für weitere Details, wie Dev Container in VS Code funktionieren.

> [!TIP]  
> Wir empfehlen GitHub Codespaces für einen schnellen Einstieg mit minimalem Aufwand. Es bietet ein großzügiges [kostenloses Nutzungskontingent](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) für persönliche Konten. Konfiguriere [Timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst), um inaktive Codespaces zu stoppen oder zu löschen und so dein Kontingent optimal zu nutzen.

## 1. Ausführen von Aufgaben

Jede Lektion enthält _optionale_ Aufgaben, die in einer oder mehreren Programmiersprachen bereitgestellt werden können, darunter Python, .NET/C#, Java und JavaScript/TypeScript. Dieser Abschnitt gibt allgemeine Hinweise zum Ausführen dieser Aufgaben.

### 1.1 Python-Aufgaben

Python-Aufgaben werden entweder als Anwendungen (`.py` Dateien) oder Jupyter-Notebooks (`.ipynb` Dateien) bereitgestellt.  
- Um das Notebook auszuführen, öffne es in Visual Studio Code, klicke dann oben rechts auf _Select Kernel_ und wähle die standardmäßige Python 3-Option aus. Du kannst nun _Run All_ auswählen, um das Notebook auszuführen.  
- Um Python-Anwendungen über die Kommandozeile auszuführen, folge den aufgabenspezifischen Anweisungen, um sicherzustellen, dass du die richtigen Dateien auswählst und die erforderlichen Argumente übergibst.

## 2. Konfigurieren der Provider

Aufgaben **können** auch so eingerichtet sein, dass sie mit einem oder mehreren Large Language Model (LLM) Deployments über einen unterstützten Service Provider wie OpenAI, Azure oder Hugging Face arbeiten. Diese bieten einen _gehosteten Endpunkt_ (API), auf den wir mit den richtigen Zugangsdaten (API-Schlüssel oder Token) programmgesteuert zugreifen können. In diesem Kurs behandeln wir folgende Provider:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) mit verschiedenen Modellen, darunter die Kern-GPT-Serie.  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) für OpenAI-Modelle mit Fokus auf Unternehmensreife  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) für Open-Source-Modelle und Inferenzserver

**Für diese Übungen benötigst du eigene Accounts**. Die Aufgaben sind optional, du kannst also je nach Interesse einen, alle oder keinen der Provider einrichten. Hier einige Hinweise zur Anmeldung:

| Anmeldung | Kosten | API-Schlüssel | Playground | Kommentare |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [Preise](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [Projektbasiert](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Mehrere Modelle verfügbar |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [Preise](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Zugang muss vorab beantragt werden](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Preise](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Hugging Chat hat begrenzte Modelle](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Folge den untenstehenden Anweisungen, um dieses Repository für die Nutzung mit verschiedenen Providern zu _konfigurieren_. Aufgaben, die einen bestimmten Provider erfordern, enthalten einen dieser Tags im Dateinamen:  
 - `aoai` - erfordert Azure OpenAI Endpunkt und Schlüssel  
 - `oai` - erfordert OpenAI Endpunkt und Schlüssel  
 - `hf` - erfordert Hugging Face Token

Du kannst einen, keinen oder alle Provider konfigurieren. Fehlende Zugangsdaten führen bei den entsprechenden Aufgaben zu Fehlern.

### 2.1 Erstelle die `.env` Datei

Wir gehen davon aus, dass du die obigen Hinweise gelesen, dich beim jeweiligen Provider registriert und die erforderlichen Zugangsdaten (API_KEY oder Token) erhalten hast. Im Fall von Azure OpenAI solltest du außerdem eine gültige Bereitstellung eines Azure OpenAI Service (Endpunkt) mit mindestens einem GPT-Modell für Chat Completion eingerichtet haben.

Der nächste Schritt ist, deine **lokalen Umgebungsvariablen** wie folgt zu konfigurieren:

1. Suche im Stammverzeichnis nach einer Datei `.env.copy`, die etwa folgenden Inhalt hat:

   ```bash
   # OpenAI Provider
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Default is set!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopiere diese Datei mit folgendem Befehl zu `.env`. Diese Datei ist in `.gitignore` eingetragen, um Geheimnisse zu schützen.

   ```bash
   cp .env.copy .env
   ```

3. Fülle die Werte aus (ersetze die Platzhalter rechts vom `=`) wie im nächsten Abschnitt beschrieben.

3. (Optional) Wenn du GitHub Codespaces nutzt, kannst du Umgebungsvariablen als _Codespaces Secrets_ speichern, die mit diesem Repository verknüpft sind. Dann ist keine lokale `.env` Datei nötig. **Beachte jedoch, dass diese Option nur mit GitHub Codespaces funktioniert.** Wenn du Docker Desktop verwendest, musst du die `.env` Datei weiterhin einrichten.

### 2.2 Fülle die `.env` Datei aus

Hier ein kurzer Überblick über die Variablennamen und ihre Bedeutung:

| Variable  | Beschreibung  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Das Benutzerzugangstoken, das du in deinem Profil eingerichtet hast |
| OPENAI_API_KEY | Der Autorisierungsschlüssel für die Nutzung des Dienstes bei nicht-Azure OpenAI Endpunkten |
| AZURE_OPENAI_API_KEY | Der Autorisierungsschlüssel für die Nutzung des Azure OpenAI Dienstes |
| AZURE_OPENAI_ENDPOINT | Der bereitgestellte Endpunkt für eine Azure OpenAI Ressource |
| AZURE_OPENAI_DEPLOYMENT | Der Endpunkt für das _Textgenerierungs_-Modell Deployment |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Der Endpunkt für das _Text-Embedding_-Modell Deployment |
| | |

Hinweis: Die letzten beiden Azure OpenAI Variablen beziehen sich auf ein Standardmodell für Chat Completion (Textgenerierung) bzw. Vektorsuche (Embeddings). Die Anweisungen zum Setzen dieser Werte findest du in den jeweiligen Aufgaben.

### 2.3 Azure konfigurieren: Über das Portal

Die Werte für Azure OpenAI Endpunkt und Schlüssel findest du im [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst). Beginnen wir dort:

1. Gehe zum [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
1. Klicke in der Seitenleiste (linkes Menü) auf **Keys and Endpoint**  
1. Klicke auf **Show Keys** – du solltest folgende Werte sehen: KEY 1, KEY 2 und Endpoint  
1. Verwende den Wert von KEY 1 für AZURE_OPENAI_API_KEY  
1. Verwende den Wert von Endpoint für AZURE_OPENAI_ENDPOINT

Als Nächstes benötigen wir die Endpunkte für die spezifischen Modelle, die wir bereitgestellt haben.

1. Klicke in der Seitenleiste (linkes Menü) auf **Model deployments** für die Azure OpenAI Ressource  
1. Klicke auf der Zielseite auf **Manage Deployments**

Du gelangst zur Azure OpenAI Studio Webseite, wo du die weiteren Werte wie unten beschrieben findest.

### 2.4 Azure konfigurieren: Über Studio

1. Navigiere zu [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **über deine Ressource**, wie oben beschrieben.  
1. Klicke auf den Tab **Deployments** (linke Seitenleiste), um die aktuell bereitgestellten Modelle zu sehen.  
1. Falls dein gewünschtes Modell nicht bereitgestellt ist, nutze **Create new deployment**, um es zu deployen.  
1. Du benötigst ein _Text-Generation_-Modell – wir empfehlen: **gpt-35-turbo**  
1. Du benötigst ein _Text-Embedding_-Modell – wir empfehlen **text-embedding-ada-002**

Aktualisiere nun die Umgebungsvariablen, um den _Deployment-Namen_ widerzuspiegeln, der verwendet wird. Dieser entspricht in der Regel dem Modellnamen, sofern du ihn nicht explizit geändert hast. Zum Beispiel könnte das so aussehen:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Vergiss nicht, die `.env` Datei nach dem Bearbeiten zu speichern**. Du kannst die Datei jetzt schließen und zu den Anweisungen zum Ausführen des Notebooks zurückkehren.

### 2.5 OpenAI konfigurieren: Über Profil

Deinen OpenAI API-Schlüssel findest du in deinem [OpenAI Account](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Falls du noch keinen hast, kannst du dich registrieren und einen API-Schlüssel erstellen. Sobald du den Schlüssel hast, kannst du ihn in der `.env` Datei in der Variable `OPENAI_API_KEY` eintragen.

### 2.6 Hugging Face konfigurieren: Über Profil

Dein Hugging Face Token findest du in deinem Profil unter [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Teile diese Tokens nicht öffentlich. Erstelle stattdessen einen neuen Token für dieses Projekt und trage ihn in der `.env` Datei unter der Variable `HUGGING_FACE_API_KEY` ein. _Hinweis:_ Technisch gesehen ist dies kein API-Schlüssel, wird aber zur Authentifizierung verwendet, weshalb wir die Namenskonvention beibehalten.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.