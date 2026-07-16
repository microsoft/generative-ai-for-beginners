# Auswahl & Konfiguration eines LLM-Anbieters 🔑

Aufgaben **können** auch so eingerichtet werden, dass sie gegen eine oder mehrere Large Language Model (LLM) Bereitstellungen über einen unterstützten Dienstleister wie OpenAI, Azure oder Hugging Face arbeiten. Diese bieten einen _gehosteten Endpunkt_ (API), auf den wir programmatisch mit den richtigen Zugangsdaten (API-Schlüssel oder Token) zugreifen können. In diesem Kurs besprechen wir diese Anbieter:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) mit verschiedenen Modellen einschließlich der Kern-GPT-Serie.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) für OpenAI-Modelle mit Fokus auf Unternehmensfähigkeit
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) für einen einzigen Endpunkt und API-Schlüssel, um hunderte Modelle von OpenAI, Meta, Mistral, Cohere, Microsoft und mehr zuzugreifen (ersetzt GitHub Models, das Ende Juli 2026 eingestellt wird)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) für Open-Source-Modelle und Inferenzserver
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) oder [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst), falls Sie Modelle komplett offline auf Ihrem eigenen Gerät ausführen möchten, ohne Cloud-Abonnement

**Sie müssen für diese Übungen eigene Konten verwenden**. Die Aufgaben sind optional, sodass Sie einen, alle oder keinen der Anbieter je nach Interesse einrichten können. Einige Hinweise zur Anmeldung:

| Anmeldung | Kosten | API-Schlüssel | Playground | Kommentare |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Preise](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektbasiert](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Mehrere verfügbare Modelle |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Preise](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Schnellstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Schnellstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Zugang muss vorher beantragt werden](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Preise](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Projektübersichtsseite](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Kostenlose Stufe verfügbar; ein Endpunkt + Schlüssel für viele Modellanbieter |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Preise](https://huggingface.co/pricing) | [Zugangstoken](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat hat eingeschränkte Modelle](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Kostenlos (läuft auf Ihrem Gerät) | Nicht erforderlich | [Lokale CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Vollständig offline, OpenAI-kompatibler Endpunkt |
| | | | | |

Befolgen Sie die untenstehenden Anweisungen, um dieses Repository für die Verwendung mit verschiedenen Anbietern zu _konfigurieren_. Aufgaben, die einen bestimmten Anbieter erfordern, enthalten einen dieser Tags im Dateinamen:

- `aoai` - benötigt Azure OpenAI Endpunkt, Schlüssel
- `oai` - benötigt OpenAI Endpunkt, Schlüssel
- `hf` - benötigt Hugging Face Token
- `githubmodels` - benötigt Microsoft Foundry Models Endpunkt, Schlüssel (GitHub Models wird Ende Juli 2026 eingestellt)

Sie können einen, keinen oder alle Anbieter einrichten. Verwandte Aufgaben geben bei fehlenden Zugangsdaten einfach Fehler aus.

## `.env`-Datei erstellen

Wir gehen davon aus, dass Sie die obigen Hinweise gelesen, sich beim relevanten Anbieter angemeldet und die erforderlichen Authentifizierungsdaten (API_KEY oder Token) erhalten haben. Im Falle von Azure OpenAI gehen wir außerdem davon aus, dass Sie eine gültige Bereitstellung eines Azure OpenAI Services (Endpunkt) mit mindestens einem GPT-Modell für Chat Completion bereitgestellt haben.

Der nächste Schritt ist, Ihre **lokalen Umgebungsvariablen** wie folgt zu konfigurieren:

1. Suchen Sie im Stammverzeichnis nach einer `.env.copy`-Datei, die etwa wie folgt aussieht:

   ```bash
   # OpenAI-Anbieter
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI in Microsoft Foundry
   ## (Azure OpenAI-Dienst ist jetzt Teil von Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Standard ist gesetzt! (aktuelle stabile GA-API-Version)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry-Modelle (Multi-Provider-Modellkatalog, ersetzt GitHub-Modelle, die Ende Juli 2026 eingestellt werden)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopieren Sie diese Datei mit dem folgenden Befehl zu `.env`. Diese Datei ist _in .gitignore_, um Geheimnisse zu schützen.

   ```bash
   cp .env.copy .env
   ```

3. Füllen Sie die Werte aus (ersetzen Sie die Platzhalter rechts vom `=`) wie im nächsten Abschnitt beschrieben.

4. (Option) Wenn Sie GitHub Codespaces verwenden, können Sie Umgebungsvariablen als _Codespaces Secrets_ speichern, die mit diesem Repository verknüpft sind. In diesem Fall müssen Sie die lokale .env-Datei nicht einrichten. **Beachten Sie jedoch, dass diese Option nur funktioniert, wenn Sie GitHub Codespaces verwenden.** Sie müssen die .env-Datei weiterhin einrichten, wenn Sie Docker Desktop verwenden.

## `.env`-Datei befüllen

Werfen wir einen kurzen Blick auf die Variablennamen, um zu verstehen, was sie repräsentieren:

| Variable  | Beschreibung  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Dies ist das Benutzerzugangstoken, das Sie in Ihrem Profil eingerichtet haben |
| OPENAI_API_KEY | Dies ist der Autorisierungsschlüssel für die Nutzung des Dienstes für Nicht-Azure OpenAI Endpunkte |
| AZURE_OPENAI_API_KEY | Dies ist der Autorisierungsschlüssel für die Nutzung dieses Dienstes |
| AZURE_OPENAI_ENDPOINT | Dies ist der bereitgestellte Endpunkt für eine Azure OpenAI Ressource |
| AZURE_OPENAI_DEPLOYMENT | Dies ist der _Textgenerierung_-Modellbereitstellungs-Endpunkt |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Dies ist der _Text-Embeddings_-Modellbereitstellungs-Endpunkt |
| AZURE_INFERENCE_ENDPOINT | Dies ist der Endpunkt für Ihr Microsoft Foundry Projekt, verwendet für Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Dies ist der API-Schlüssel für Ihr Microsoft Foundry Projekt |
| | |

Hinweis: Die letzten beiden Azure OpenAI Variablen beziehen sich jeweils auf ein Standardmodell für Chat Completion (Textgenerierung) bzw. Vektorsuche (Embeddings). Anweisungen zum Setzen dieser Variablen werden in den jeweiligen Aufgaben definiert.

## Azure OpenAI konfigurieren: Vom Portal

> **Hinweis:** Der Azure OpenAI Service ist jetzt Teil von [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Ressourcen und Bereitstellungen sind weiterhin im Azure Portal sichtbar, aber das tägliche Modellmanagement (Bereitstellungen, Playground, Überwachung) erfolgt jetzt im Foundry-Portal statt im alten eigenständigen „Azure OpenAI Studio“.

Die Azure OpenAI Endpunkt- und Schlüsselwerte finden Sie im [Azure-Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), also beginnen wir dort.

1. Gehen Sie zum [Azure-Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klicken Sie in der Seitenleiste (links) auf die Option **Keys and Endpoint**.
1. Klicken Sie auf **Show Keys** – Sie sollten Folgendes sehen: KEY 1, KEY 2 und Endpunkt.
1. Verwenden Sie den Wert von KEY 1 für AZURE_OPENAI_API_KEY
1. Verwenden Sie den Endpunkt-Wert für AZURE_OPENAI_ENDPOINT

Als Nächstes benötigen wir die Endpunkte für die spezifischen bereitgestellten Modelle.

1. Klicken Sie bei der Azure OpenAI-Ressource in der Seitenleiste (linkes Menü) auf **Model deployments**.
1. Klicken Sie auf der Zielseite auf **Go to Microsoft Foundry portal** (oder **Manage Deployments**, je nach Ressourcentyp)

Dies führt Sie zum Microsoft Foundry-Portal, wo wir die weiteren Werte wie unten beschrieben finden.

## Azure OpenAI konfigurieren: Vom Microsoft Foundry-Portal

1. Navigieren Sie wie oben beschrieben vom Ihrer Ressource aus zum [Microsoft Foundry-Portal](https://ai.azure.com?WT.mc_id=academic-105485-koreyst).
1. Klicken Sie auf den Tab **Deployments** (Seitenleiste, links), um die aktuell bereitgestellten Modelle anzuzeigen.
1. Wenn Ihr gewünschtes Modell nicht bereitgestellt ist, verwenden Sie **Deploy model**, um es aus dem [Modellkatalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) bereitzustellen.
1. Sie benötigen ein _Textgenerierungs_-Modell – wir empfehlen: **gpt-4o-mini**
1. Sie benötigen ein _Text-Embedding_-Modell – wir empfehlen **text-embedding-3-small**

Aktualisieren Sie nun die Umgebungsvariablen, um den verwendeten _Bereitstellungsnamen_ widerzuspiegeln. Dies ist in der Regel derselbe wie der Modellname, sofern Sie ihn nicht explizit geändert haben. Zum Beispiel könnten Sie haben:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Vergessen Sie nicht, die .env-Datei beim Abschluss zu speichern**. Sie können die Datei nun schließen und zu den Anweisungen zum Ausführen des Notebooks zurückkehren.

## OpenAI konfigurieren: Vom Profil

Ihren OpenAI-API-Schlüssel finden Sie in Ihrem [OpenAI-Konto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Falls Sie noch keinen haben, können Sie sich anmelden und einen API-Schlüssel erstellen. Sobald Sie den Schlüssel haben, können Sie ihn verwenden, um die Variable `OPENAI_API_KEY` in der `.env`-Datei zu befüllen.

## Hugging Face konfigurieren: Vom Profil

Ihr Hugging Face Token finden Sie in Ihrem Profil unter [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Posten oder teilen Sie diese nicht öffentlich. Erstellen Sie stattdessen einen neuen Token für die Nutzung in diesem Projekt und kopieren Sie diesen in die `.env`-Datei unter der Variable `HUGGING_FACE_API_KEY`. _Hinweis:_ Technisch ist dies kein API-Schlüssel, wird aber für die Authentifizierung verwendet, daher behalten wir die Namenskonvention zur Konsistenz bei.

## Microsoft Foundry Models konfigurieren: Vom Portal

> **Hinweis:** GitHub Models wird Ende Juli 2026 eingestellt. Microsoft Foundry Models ist der direkte Ersatz und bietet denselben kostenlosen Modellkatalog zum Ausprobieren sowie das Azure AI Inference SDK / OpenAI SDK-Erlebnis.

1. Gehen Sie zu [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) und erstellen oder öffnen Sie ein Foundry-Projekt.
1. Durchsuchen Sie den [Modellkatalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) und stellen Sie ein Modell bereit, z.B. `gpt-4o-mini`.
1. Kopieren Sie auf der **Übersichts**-Seite des Projekts den **Endpunkt** und den **API-Schlüssel**.
1. Verwenden Sie den Endpunktwert für `AZURE_INFERENCE_ENDPOINT` und den Schlüsselwert für `AZURE_INFERENCE_CREDENTIAL` in Ihrer `.env`-Datei.

## Offline / Lokale Anbieter

Wenn Sie lieber komplett ohne Cloud-Abonnement auskommen möchten, können Sie kompatible offene Modelle direkt auf Ihrem eigenen Gerät ausführen:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - Microsofts Laufzeitumgebung auf dem Gerät. Sie wählt automatisch den besten Ausführungsanbieter (NPU, GPU oder CPU) aus und bietet einen OpenAI-kompatiblen Endpunkt, sodass Sie den Großteil des Beispielcodes in diesem Kurs mit minimalen Änderungen wiederverwenden können. Siehe die [Foundry Local-Dokumentation](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) für den Einstieg, oder installieren Sie mit `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - eine beliebte Alternative zum lokalen Ausführen offener Modelle wie Llama, Phi, Mistral und Gemma.


Siehe [Lektion 19: Bauen mit SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) für praktische Beispiele mit beiden Optionen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->