<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T09:05:48+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "de"
}
-->
# Richten Sie Ihre Entwicklungsumgebung ein

Wir haben dieses Repository und den Kurs mit einem [Entwicklungscontainer](https://containers.dev?WT.mc_id=academic-105485-koreyst) eingerichtet, der eine universelle Laufzeitumgebung bietet, die Python3, .NET, Node.js und Java-Entwicklung unterstützt. Die zugehörige Konfiguration ist in der Datei `devcontainer.json` im Ordner `.devcontainer/` am Stamm dieses Repositorys definiert.

Um den Entwicklungscontainer zu aktivieren, starten Sie ihn in [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (für eine cloudbasierte Laufzeitumgebung) oder in [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (für eine lokal gehostete Laufzeitumgebung). Lesen Sie [diese Dokumentation](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) für weitere Details, wie Entwicklungscontainer innerhalb von VS Code funktionieren.

> [!TIP]  
> Wir empfehlen die Verwendung von GitHub Codespaces für einen schnellen Start mit minimalem Aufwand. Es bietet ein großzügiges [freies Nutzungskontingent](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) für persönliche Konten. Konfigurieren Sie [Timeouts](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst), um inaktive Codespaces zu stoppen oder zu löschen, um Ihre Kontingentnutzung zu maximieren.

## 1. Ausführen von Aufgaben

Jede Lektion wird _optionale_ Aufgaben haben, die in einer oder mehreren Programmiersprachen bereitgestellt werden können, darunter: Python, .NET/C#, Java und JavaScript/TypeScript. Dieser Abschnitt bietet allgemeine Anleitungen zur Ausführung dieser Aufgaben.

### 1.1 Python-Aufgaben

Python-Aufgaben werden entweder als Anwendungen (`.py`-Dateien) oder Jupyter-Notebooks (`.ipynb`-Dateien) bereitgestellt.
- Um das Notebook auszuführen, öffnen Sie es in Visual Studio Code und klicken Sie dann auf _Kernel auswählen_ (oben rechts) und wählen Sie die angezeigte Standardoption Python 3. Sie können nun _Alles ausführen_, um das Notebook auszuführen.
- Um Python-Anwendungen über die Befehlszeile auszuführen, folgen Sie den aufgabenspezifischen Anweisungen, um sicherzustellen, dass Sie die richtigen Dateien auswählen und die erforderlichen Argumente bereitstellen.

## 2. Konfigurieren von Anbietern

Aufgaben **können** auch so eingerichtet werden, dass sie mit einer oder mehreren Large Language Model (LLM)-Bereitstellungen über einen unterstützten Dienstanbieter wie OpenAI, Azure oder Hugging Face funktionieren. Diese bieten einen _gehosteten Endpunkt_ (API), auf den wir mit den richtigen Zugangsdaten (API-Schlüssel oder Token) programmatisch zugreifen können. In diesem Kurs besprechen wir diese Anbieter:

- [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) mit diversen Modellen, darunter die Kern-GPT-Serie.
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) für OpenAI-Modelle mit Fokus auf Unternehmensbereitschaft.
- [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) für Open-Source-Modelle und Inferenzserver.

**Sie müssen Ihre eigenen Konten für diese Übungen verwenden**. Aufgaben sind optional, sodass Sie sich entscheiden können, einen, alle oder keinen der Anbieter basierend auf Ihren Interessen einzurichten. Einige Hinweise zur Anmeldung:

| Anmeldung | Kosten | API-Schlüssel | Playground | Kommentare |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Preise](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektbasiert](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Mehrere Modelle verfügbar |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Preise](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Schnellstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Schnellstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Muss im Voraus beantragt werden](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Preise](https://huggingface.co/pricing) | [Zugriffstoken](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat hat begrenzte Modelle](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Befolgen Sie die unten stehenden Anweisungen, um dieses Repository für die Verwendung mit verschiedenen Anbietern zu _konfigurieren_. Aufgaben, die einen bestimmten Anbieter erfordern, enthalten eines dieser Tags in ihrem Dateinamen:
- `aoai` - erfordert Azure OpenAI-Endpunkt, Schlüssel
- `oai` - erfordert OpenAI-Endpunkt, Schlüssel
- `hf` - erfordert Hugging Face-Token

Sie können einen, keinen oder alle Anbieter konfigurieren. Verwandte Aufgaben werden einfach bei fehlenden Zugangsdaten fehlschlagen.

### 2.1. Erstellen Sie die Datei `.env`

Wir gehen davon aus, dass Sie die obige Anleitung gelesen und sich beim entsprechenden Anbieter angemeldet haben und die erforderlichen Authentifizierungsdaten (API_KEY oder Token) erhalten haben. Im Fall von Azure OpenAI gehen wir davon aus, dass Sie auch eine gültige Bereitstellung eines Azure OpenAI-Dienstes (Endpunkt) mit mindestens einem GPT-Modell für Chat-Abschluss bereitgestellt haben.

Der nächste Schritt besteht darin, Ihre **lokalen Umgebungsvariablen** wie folgt zu konfigurieren:

1. Suchen Sie im Stammordner nach einer Datei `.env.copy`, die Inhalte wie diese haben sollte:

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

2. Kopieren Sie diese Datei mit dem unten stehenden Befehl in `.env`. Diese Datei wird _gitignore-d_, um Geheimnisse sicher zu halten.

   ```bash
   cp .env.copy .env
   ```

3. Füllen Sie die Werte aus (ersetzen Sie Platzhalter auf der rechten Seite von `=`), wie im nächsten Abschnitt beschrieben.

3. (Optional) Wenn Sie GitHub Codespaces verwenden, haben Sie die Möglichkeit, Umgebungsvariablen als _Codespaces-Geheimnisse_ zu speichern, die mit diesem Repository verknüpft sind. In diesem Fall müssen Sie keine lokale .env-Datei einrichten. **Beachten Sie jedoch, dass diese Option nur funktioniert, wenn Sie GitHub Codespaces verwenden.** Sie müssen die .env-Datei dennoch einrichten, wenn Sie Docker Desktop verwenden.

### 2.2. Datei `.env` ausfüllen

Werfen wir einen kurzen Blick auf die Variablennamen, um zu verstehen, was sie darstellen:

| Variable  | Beschreibung  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Dies ist das Benutzerzugriffstoken, das Sie in Ihrem Profil eingerichtet haben |
| OPENAI_API_KEY | Dies ist der Autorisierungsschlüssel für die Nutzung des Dienstes für nicht-Azure OpenAI-Endpunkte |
| AZURE_OPENAI_API_KEY | Dies ist der Autorisierungsschlüssel für die Nutzung dieses Dienstes |
| AZURE_OPENAI_ENDPOINT | Dies ist der bereitgestellte Endpunkt für eine Azure OpenAI-Ressource |
| AZURE_OPENAI_DEPLOYMENT | Dies ist der _Textgenerierungs_-Modellbereitstellungsendpunkt |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Dies ist der _Text-Einbettungs_-Modellbereitstellungsendpunkt |
| | |

Hinweis: Die letzten beiden Azure OpenAI-Variablen spiegeln ein Standardmodell für Chat-Abschluss (Textgenerierung) und Vektorsuche (Einbettungen) wider. Anweisungen zu deren Einrichtung werden in den entsprechenden Aufgaben definiert.

### 2.3 Konfigurieren von Azure: Vom Portal

Die Azure OpenAI-Endpunkt- und Schlüsselwerte finden Sie im [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), also beginnen wir dort.

1. Gehen Sie zum [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klicken Sie auf die Option **Schlüssel und Endpunkt** in der Seitenleiste (Menü links).
1. Klicken Sie auf **Schlüssel anzeigen** - Sie sollten Folgendes sehen: SCHLÜSSEL 1, SCHLÜSSEL 2 und Endpunkt.
1. Verwenden Sie den SCHLÜSSEL 1-Wert für AZURE_OPENAI_API_KEY
1. Verwenden Sie den Endpunktwert für AZURE_OPENAI_ENDPOINT

Als nächstes benötigen wir die Endpunkte für die spezifischen Modelle, die wir bereitgestellt haben.

1. Klicken Sie auf die Option **Modellbereitstellungen** in der Seitenleiste (linkes Menü) für die Azure OpenAI-Ressource.
1. Klicken Sie auf der Zielseite auf **Bereitstellungen verwalten**

Dies führt Sie zur Azure OpenAI Studio-Website, auf der wir die anderen Werte wie unten beschrieben finden.

### 2.4 Konfigurieren von Azure: Vom Studio

1. Navigieren Sie zu [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **von Ihrer Ressource** wie oben beschrieben.
1. Klicken Sie auf die Registerkarte **Bereitstellungen** (Seitenleiste, links), um derzeit bereitgestellte Modelle anzuzeigen.
1. Wenn Ihr gewünschtes Modell nicht bereitgestellt ist, verwenden Sie **Neue Bereitstellung erstellen**, um es bereitzustellen.
1. Sie benötigen ein _Textgenerierungs_-Modell - wir empfehlen: **gpt-35-turbo**
1. Sie benötigen ein _Text-Einbettungs_-Modell - wir empfehlen **text-embedding-ada-002**

Aktualisieren Sie nun die Umgebungsvariablen, um den verwendeten _Bereitstellungsnamen_ widerzuspiegeln. Dies wird normalerweise derselbe wie der Modellname sein, es sei denn, Sie haben ihn explizit geändert. Als Beispiel könnten Sie haben:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Vergessen Sie nicht, die .env-Datei zu speichern, wenn Sie fertig sind**. Sie können jetzt die Datei schließen und zu den Anweisungen zum Ausführen des Notebooks zurückkehren.

### 2.5 Konfigurieren von OpenAI: Vom Profil

Ihr OpenAI-API-Schlüssel kann in Ihrem [OpenAI-Konto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) gefunden werden. Wenn Sie keinen haben, können Sie sich für ein Konto anmelden und einen API-Schlüssel erstellen. Sobald Sie den Schlüssel haben, können Sie ihn verwenden, um die `OPENAI_API_KEY`-Variable in der Datei `.env` auszufüllen.

### 2.6 Konfigurieren von Hugging Face: Vom Profil

Ihr Hugging Face-Token kann in Ihrem Profil unter [Zugriffstoken](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst) gefunden werden. Veröffentlichen oder teilen Sie diese nicht öffentlich. Erstellen Sie stattdessen ein neues Token für diese Projektverwendung und kopieren Sie es in die Datei `.env` unter der Variable `HUGGING_FACE_API_KEY`. _Hinweis:_ Dies ist technisch gesehen kein API-Schlüssel, wird jedoch für die Authentifizierung verwendet, daher behalten wir diese Namenskonvention bei.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir haften nicht für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.