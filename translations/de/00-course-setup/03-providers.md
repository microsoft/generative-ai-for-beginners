<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b5b016b0eb8a1cef2e3097620d8aa23",
  "translation_date": "2025-12-19T12:45:45+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "de"
}
-->
# Auswahl & Konfiguration eines LLM-Anbieters 🔑

Aufgaben **können** auch so eingerichtet werden, dass sie gegen eine oder mehrere Large Language Model (LLM)-Bereitstellungen über einen unterstützten Dienstanbieter wie OpenAI, Azure oder Hugging Face arbeiten. Diese bieten einen _gehosteten Endpunkt_ (API), auf den wir mit den richtigen Anmeldeinformationen (API-Schlüssel oder Token) programmgesteuert zugreifen können. In diesem Kurs besprechen wir diese Anbieter:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) mit diversen Modellen, einschließlich der Kern-GPT-Serie.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) für OpenAI-Modelle mit Fokus auf Unternehmensreife
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) für Open-Source-Modelle und Inferenzserver

**Sie müssen für diese Übungen Ihre eigenen Konten verwenden**. Aufgaben sind optional, sodass Sie je nach Interesse einen, alle oder keinen der Anbieter einrichten können. Einige Hinweise zur Anmeldung:

| Anmeldung | Kosten | API-Schlüssel | Playground | Kommentare |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Preise](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektbasiert](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Mehrere Modelle verfügbar |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Preise](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Zugang muss vorab beantragt werden](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Preise](https://huggingface.co/pricing) | [Zugangstoken](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat hat begrenzte Modelle](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Folgen Sie den untenstehenden Anweisungen, um dieses Repository für die Verwendung mit verschiedenen Anbietern zu _konfigurieren_. Aufgaben, die einen bestimmten Anbieter erfordern, enthalten eines dieser Tags im Dateinamen:

- `aoai` - erfordert Azure OpenAI-Endpunkt, Schlüssel
- `oai` - erfordert OpenAI-Endpunkt, Schlüssel
- `hf` - erfordert Hugging Face-Token

Sie können einen, keinen oder alle Anbieter konfigurieren. Verwandte Aufgaben schlagen einfach mit einem Fehler fehl, wenn Anmeldeinformationen fehlen.

## Erstellen der `.env`-Datei

Wir gehen davon aus, dass Sie die obigen Hinweise bereits gelesen, sich beim entsprechenden Anbieter angemeldet und die erforderlichen Authentifizierungsdaten (API_KEY oder Token) erhalten haben. Im Fall von Azure OpenAI gehen wir davon aus, dass Sie auch eine gültige Bereitstellung eines Azure OpenAI-Dienstes (Endpunkt) mit mindestens einem GPT-Modell für Chat Completion haben.

Der nächste Schritt ist, Ihre **lokalen Umgebungsvariablen** wie folgt zu konfigurieren:

1. Suchen Sie im Stammordner nach einer `.env.copy`-Datei, die Inhalte wie folgt haben sollte:

   ```bash
   # OpenAI Anbieter
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Standard ist gesetzt!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Kopieren Sie diese Datei mit dem folgenden Befehl zu `.env`. Diese Datei ist _gitignore-d_, um Geheimnisse sicher zu halten.

   ```bash
   cp .env.copy .env
   ```

3. Füllen Sie die Werte aus (ersetzen Sie die Platzhalter rechts vom `=`) wie im nächsten Abschnitt beschrieben.

4. (Optional) Wenn Sie GitHub Codespaces verwenden, haben Sie die Möglichkeit, Umgebungsvariablen als _Codespaces-Geheimnisse_ zu speichern, die mit diesem Repository verknüpft sind. In diesem Fall müssen Sie keine lokale .env-Datei einrichten. **Beachten Sie jedoch, dass diese Option nur funktioniert, wenn Sie GitHub Codespaces verwenden.** Wenn Sie stattdessen Docker Desktop verwenden, müssen Sie die .env-Datei weiterhin einrichten.

## Befüllen der `.env`-Datei

Werfen wir einen kurzen Blick auf die Variablennamen, um zu verstehen, was sie repräsentieren:

| Variable  | Beschreibung  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Dies ist das Benutzerzugangstoken, das Sie in Ihrem Profil eingerichtet haben |
| OPENAI_API_KEY | Dies ist der Autorisierungsschlüssel für die Nutzung des Dienstes für Nicht-Azure OpenAI-Endpunkte |
| AZURE_OPENAI_API_KEY | Dies ist der Autorisierungsschlüssel für die Nutzung dieses Dienstes |
| AZURE_OPENAI_ENDPOINT | Dies ist der bereitgestellte Endpunkt für eine Azure OpenAI-Ressource |
| AZURE_OPENAI_DEPLOYMENT | Dies ist der _Textgenerierung_-Modellbereitstellungsendpunkt |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Dies ist der _Text-Embedding_-Modellbereitstellungsendpunkt |
| | |

Hinweis: Die letzten beiden Azure OpenAI-Variablen spiegeln standardmäßig ein Modell für Chat Completion (Textgenerierung) und Vektorsuche (Embeddings) wider. Anweisungen zum Einrichten werden in den entsprechenden Aufgaben definiert.

## Azure konfigurieren: Vom Portal

Die Azure OpenAI-Endpunkt- und Schlüsselwerte finden Sie im [Azure-Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), beginnen wir also dort.

1. Gehen Sie zum [Azure-Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klicken Sie in der Seitenleiste (linkes Menü) auf die Option **Schlüssel und Endpunkt**.
1. Klicken Sie auf **Schlüssel anzeigen** – Sie sollten Folgendes sehen: SCHLÜSSEL 1, SCHLÜSSEL 2 und Endpunkt.
1. Verwenden Sie den Wert von SCHLÜSSEL 1 für AZURE_OPENAI_API_KEY
1. Verwenden Sie den Wert des Endpunkts für AZURE_OPENAI_ENDPOINT

Als Nächstes benötigen wir die Endpunkte für die spezifischen Modelle, die wir bereitgestellt haben.

1. Klicken Sie in der Seitenleiste (linkes Menü) für die Azure OpenAI-Ressource auf die Option **Modellbereitstellungen**.
1. Klicken Sie auf der Zielseite auf **Bereitstellungen verwalten**

Dies führt Sie zur Azure OpenAI Studio-Website, wo wir die anderen Werte wie unten beschrieben finden.

## Azure konfigurieren: Vom Studio

1. Navigieren Sie zu [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **von Ihrer Ressource aus**, wie oben beschrieben.
1. Klicken Sie auf die Registerkarte **Bereitstellungen** (Seitenleiste, links), um die aktuell bereitgestellten Modelle anzuzeigen.
1. Wenn Ihr gewünschtes Modell nicht bereitgestellt ist, verwenden Sie **Neue Bereitstellung erstellen**, um es bereitzustellen.
1. Sie benötigen ein _Textgenerierungs_-Modell – wir empfehlen: **gpt-35-turbo**
1. Sie benötigen ein _Text-Embedding_-Modell – wir empfehlen **text-embedding-ada-002**

Aktualisieren Sie nun die Umgebungsvariablen, um den verwendeten _Bereitstellungsnamen_ widerzuspiegeln. Dies ist normalerweise derselbe wie der Modellname, sofern Sie ihn nicht explizit geändert haben. Zum Beispiel könnten Sie haben:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Vergessen Sie nicht, die .env-Datei nach dem Bearbeiten zu speichern**. Sie können die Datei jetzt schließen und zu den Anweisungen zum Ausführen des Notebooks zurückkehren.

## OpenAI konfigurieren: Vom Profil

 Ihren OpenAI-API-Schlüssel finden Sie in Ihrem [OpenAI-Konto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Wenn Sie noch keinen haben, können Sie sich anmelden und einen API-Schlüssel erstellen. Sobald Sie den Schlüssel haben, können Sie ihn verwenden, um die Variable `OPENAI_API_KEY` in der `.env`-Datei zu befüllen.

## Hugging Face konfigurieren: Vom Profil

Ihr Hugging Face-Token finden Sie in Ihrem Profil unter [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Veröffentlichen oder teilen Sie diese nicht öffentlich. Erstellen Sie stattdessen ein neues Token für die Nutzung in diesem Projekt und kopieren Sie es in die `.env`-Datei unter der Variable `HUGGING_FACE_API_KEY`. _Hinweis:_ Dies ist technisch gesehen kein API-Schlüssel, wird aber für die Authentifizierung verwendet, daher behalten wir diese Namenskonvention zur Konsistenz bei.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->