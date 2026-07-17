# Auswahl & Konfiguration eines LLM-Anbieters 🔑

Aufgaben **können** auch so eingerichtet werden, dass sie gegen eine oder mehrere Large Language Model (LLM)-Bereitstellungen über einen unterstützten Serviceanbieter wie OpenAI, Azure oder Hugging Face arbeiten. Diese bieten einen _gehosteten Endpunkt_ (API), auf den wir programmatisch mit den richtigen Zugangsdaten (API-Schlüssel oder Token) zugreifen können. In diesem Kurs besprechen wir diese Anbieter:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) mit diversen Modellen einschließlich der Kern-GPT-Serie.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) für OpenAI-Modelle mit Fokus auf Unternehmensreife
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) für einen einzigen Endpunkt und API-Schlüssel zum Zugriff auf hunderte Modelle von OpenAI, Meta, Mistral, Cohere, Microsoft und mehr (ersetzt GitHub Models, das Ende Juli 2026 eingestellt wird)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) für Open-Source-Modelle und Inferenzserver
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) oder [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst), wenn Sie Modelle vollständig offline auf Ihrem eigenen Gerät ausführen möchten, ohne dass ein Cloud-Abonnement erforderlich ist

**Sie müssen für diese Übungen Ihre eigenen Accounts verwenden**. Die Aufgaben sind optional, sodass Sie je nach Interesse einen, alle oder keinen der Anbieter einrichten können. Einige Hinweise zur Anmeldung:

| Anmeldung | Kosten | API-Schlüssel | Playground | Kommentare |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Preise](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektbasiert](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Mehrere Modelle verfügbar |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Preise](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Zugang muss vorher beantragt werden](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Preise](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Projektübersichtsseite](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Kostenloser Tarif verfügbar; ein Endpunkt + Schlüssel für viele Modellanbieter |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Preise](https://huggingface.co/pricing) | [Zugangstoken](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat hat begrenzte Modelle](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Kostenlos (läuft auf Ihrem Gerät) | Nicht erforderlich | [Lokale CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Vollständig offline, OpenAI-kompatibler Endpunkt |
| | | | | |

Folgen Sie den Anweisungen unten, um dieses Repository für die Nutzung mit verschiedenen Anbietern _zu konfigurieren_. Aufgaben, die einen bestimmten Anbieter erfordern, enthalten einen dieser Tags im Dateinamen:

- `aoai` - erfordert Azure OpenAI Endpunkt, Schlüssel
- `oai` - erfordert OpenAI Endpunkt, Schlüssel
- `hf` - erfordert Hugging Face Token
- `githubmodels` - erfordert Microsoft Foundry Models Endpunkt, Schlüssel (GitHub Models wird Ende Juli 2026 eingestellt)

Sie können einen, keinen oder alle Anbieter konfigurieren. Verwandte Aufgaben schlagen einfach mit einem Fehler fehl, wenn Zugangsdaten fehlen.

## Erstellen Sie die Datei `.env`

Wir gehen davon aus, dass Sie die obigen Hinweise gelesen, sich beim relevanten Anbieter angemeldet und die erforderlichen Authentifizierungsdaten (API_KEY oder Token) erhalten haben. Im Fall von Azure OpenAI setzen wir voraus, dass Sie auch eine gültige Bereitstellung eines Azure OpenAI-Dienstes (Endpunkt) mit mindestens einem GPT-Modell für Chat Completion haben.

Der nächste Schritt ist das Konfigurieren Ihrer **lokalen Umgebungsvariablen** wie folgt:

1. Suchen Sie im Stammordner die Datei `.env.copy`, die folgenden Inhalt haben sollte:

   ```bash
   # OpenAI Anbieter
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI in Microsoft Foundry
   ## (Azure OpenAI-Dienst ist jetzt Teil von Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Standard ist gesetzt! (aktuelle stabile GA API-Version)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Microsoft Foundry Modelle (Multi-Provider-Modellkatalog, ersetzt GitHub-Modelle, die Ende Juli 2026 eingestellt werden)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopieren Sie diese Datei mit dem untenstehenden Befehl nach `.env`. Diese Datei ist _gitignore-d_, wodurch Geheimnisse geschützt bleiben.

   ```bash
   cp .env.copy .env
   ```

3. Füllen Sie die Werte aus (ersetzen Sie die Platzhalter rechts vom `=`) wie im nächsten Abschnitt beschrieben.

4. (Optional) Wenn Sie GitHub Codespaces verwenden, können Sie Umgebungsvariablen als _Codespaces-Geheimnisse_ speichern, die mit diesem Repository verknüpft sind. In diesem Fall müssen Sie keine lokale .env-Datei einrichten. **Beachten Sie jedoch, dass diese Option nur funktioniert, wenn Sie GitHub Codespaces verwenden.** Wenn Sie stattdessen Docker Desktop verwenden, müssen Sie die .env-Datei weiterhin einrichten.

## Befüllen der `.env`-Datei

Werfen wir einen kurzen Blick auf die Variablennamen, um zu verstehen, wofür sie stehen:

| Variable  | Beschreibung  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Dies ist der Zugangstoken des Benutzers, den Sie in Ihrem Profil eingerichtet haben |
| OPENAI_API_KEY | Dies ist der Autorisierungsschlüssel für die Nutzung des Dienstes bei nicht-Azure OpenAI Endpunkten |
| AZURE_OPENAI_API_KEY | Dies ist der Autorisierungsschlüssel für die Nutzung dieses Dienstes |
| AZURE_OPENAI_ENDPOINT | Dies ist der bereitgestellte Endpunkt für eine Azure OpenAI Ressource |
| AZURE_OPENAI_DEPLOYMENT | Dies ist der Endpunkt für die _Textgenerierung_ des Modell-Deployments |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Dies ist der Endpunkt für die _Text-Einbettungen_ des Modell-Deployments |
| AZURE_INFERENCE_ENDPOINT | Dies ist der Endpunkt für Ihr Microsoft Foundry-Projekt, verwendet für Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Dies ist der API-Schlüssel für Ihr Microsoft Foundry-Projekt |
| | |

Hinweis: Die letzten beiden Azure OpenAI-Variablen beziehen sich auf ein Standardmodell für Chat Completion (Textgenerierung) bzw. Vektorsuche (Einbettungen). Anweisungen zum Setzen dieser Variablen werden in den jeweiligen Aufgaben definiert.

## Azure OpenAI konfigurieren: Über das Portal

> **Hinweis:** Azure OpenAI Service ist jetzt Teil von [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Ressourcen und Bereitstellungen werden weiterhin im Azure-Portal angezeigt, aber das tägliche Modellmanagement (Bereitstellungen, Playground, Überwachung) erfolgt nun im Foundry-Portal anstelle des alten eigenständigen "Azure OpenAI Studio".

Die Azure OpenAI-Endpunkt- und Schlüsselwerte finden Sie im [Azure-Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), beginnen wir also dort.

1. Gehen Sie zum [Azure-Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klicken Sie im Seitenmenü (links) auf die Option **Schlüssel und Endpunkt**.
1. Klicken Sie auf **Schlüssel anzeigen** – Sie sollten Folgendes sehen: SCHLÜSSEL 1, SCHLÜSSEL 2 und Endpunkt.
1. Verwenden Sie den Wert von SCHLÜSSEL 1 für AZURE_OPENAI_API_KEY
1. Verwenden Sie den Endpunktwert für AZURE_OPENAI_ENDPOINT

Als nächstes benötigen wir die Endpunkte für die spezifischen Modelle, die wir bereitgestellt haben.

1. Klicken Sie im Seitenmenü (links) auf die Option **Modellbereitstellungen** für die Azure OpenAI-Ressource.
1. Klicken Sie auf der Zielseite auf **Zum Microsoft Foundry-Portal gehen** (oder **Bereitstellungen verwalten**, je nach Ressourcentyp)

Dadurch gelangen Sie zum Microsoft Foundry-Portal, wo wir die weiteren Werte wie unten beschrieben finden.

## Azure OpenAI konfigurieren: Über das Microsoft Foundry-Portal

1. Navigieren Sie zum [Microsoft Foundry-Portal](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **über Ihre Ressource**, wie oben beschrieben.
1. Klicken Sie auf den Tab **Bereitstellungen** (Seitenleiste, links), um aktuell bereitgestellte Modelle anzuzeigen.
1. Falls Ihr gewünschtes Modell nicht bereitgestellt ist, verwenden Sie **Modell bereitstellen**, um es aus dem [Modellkatalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) zu installieren.
1. Sie benötigen ein _Textgenerierungsmodell_ – wir empfehlen: **gpt-5-mini**
1. Sie benötigen ein _Textembedding-Modell_ – wir empfehlen **text-embedding-3-small**

Aktualisieren Sie nun die Umgebungsvariablen mit dem verwendeten _Bereitstellungsnamen_. Dieser ist typischerweise derselbe wie der Modellname, sofern Sie ihn nicht explizit geändert haben. Beispielsweise könnten Sie folgendes haben:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Vergessen Sie nicht, die .env-Datei nach dem Bearbeiten zu speichern**. Sie können die Datei nun schließen und zu den Anweisungen zum Ausführen des Notebooks zurückkehren.

## OpenAI konfigurieren: Über das Profil

Ihren OpenAI-API-Schlüssel finden Sie in Ihrem [OpenAI-Konto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Falls Sie keinen haben, können Sie sich anmelden und einen API-Schlüssel erstellen. Sobald Sie den Schlüssel haben, können Sie ihn in der `.env`-Datei in der Variablen `OPENAI_API_KEY` eintragen.

## Hugging Face konfigurieren: Über das Profil

Ihren Hugging Face-Token finden Sie in Ihrem Profil unter [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Veröffentlichen oder teilen Sie diese Tokens nicht öffentlich. Erstellen Sie stattdessen einen neuen Token für dieses Projekt und kopieren Sie ihn in der `.env`-Datei unter der Variable `HUGGING_FACE_API_KEY`. _Hinweis:_ Technisch gesehen ist dies kein API-Schlüssel, wird aber zur Authentifizierung genutzt, weshalb wir dieses Namensschema zur Konsistenz beibehalten.

## Microsoft Foundry Models konfigurieren: Über das Portal

> **Hinweis:** GitHub Models wird Ende Juli 2026 eingestellt. Microsoft Foundry Models ist der direkte Ersatz und bietet denselben kostenfreien Modellkatalog und die Azure AI Inference SDK / OpenAI SDK Erfahrung.

1. Gehen Sie zu [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) und erstellen (oder öffnen) Sie ein Foundry-Projekt.
1. Durchsuchen Sie den [Modellkatalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) und stellen Sie ein Modell bereit, zum Beispiel `gpt-5-mini`.
1. Kopieren Sie auf der **Übersichtsseite** des Projekts den **Endpunkt** und den **API-Schlüssel**.
1. Verwenden Sie den Endpunktwert für `AZURE_INFERENCE_ENDPOINT` und den Schlüsselwert für `AZURE_INFERENCE_CREDENTIAL` in Ihrer `.env`-Datei.

## Offline- / lokale Anbieter

Wenn Sie lieber überhaupt kein Cloud-Abonnement verwenden möchten, können Sie kompatible Open-Modelle direkt auf Ihrem eigenen Gerät ausführen:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** – Microsofts Laufzeitumgebung auf dem Gerät. Sie wählt automatisch den besten Ausführungsanbieter (NPU, GPU oder CPU) aus und stellt einen OpenAI-kompatiblen Endpunkt bereit, sodass Sie den Großteil des Beispielcodes in diesem Kurs mit minimalen Änderungen wiederverwenden können. Siehe [Foundry Local Dokumentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) für den Einstieg oder Installation mit `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** – eine beliebte Alternative zum lokalen Ausführen offener Modelle wie Llama, Phi, Mistral und Gemma.


Siehe [Lektionen 19: Arbeiten mit SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) für praktische Beispiele mit beiden Optionen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->