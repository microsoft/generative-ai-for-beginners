<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T13:43:34+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "de"
}
-->
# Auswahl & Konfiguration eines LLM-Anbieters 🔑

Aufgaben **können** so eingerichtet werden, dass sie mit einer oder mehreren Bereitstellungen von Large Language Models (LLM) über einen unterstützten Dienstanbieter wie OpenAI, Azure oder Hugging Face funktionieren. Diese stellen einen _gehosteten Endpunkt_ (API) bereit, auf den wir mit den richtigen Zugangsdaten (API-Schlüssel oder Token) programmatisch zugreifen können. In diesem Kurs besprechen wir folgende Anbieter:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) mit verschiedenen Modellen, darunter die zentrale GPT-Reihe.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) für OpenAI-Modelle mit Fokus auf Unternehmensanforderungen
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) für Open-Source-Modelle und Inferenz-Server

**Für diese Übungen benötigst du eigene Konten.** Die Aufgaben sind optional, du kannst also je nach Interesse einen, alle oder keinen der Anbieter einrichten. Einige Hinweise zur Anmeldung:

| Anmeldung | Kosten | API-Schlüssel | Playground | Hinweise |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Preise](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Projektbasiert](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Mehrere Modelle verfügbar |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Preise](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Schnellstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Schnellstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Zugang muss vorab beantragt werden](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Preise](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Hugging Chat bietet nur begrenzte Modelle](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Folge den untenstehenden Anweisungen, um dieses Repository für die Nutzung mit verschiedenen Anbietern _zu konfigurieren_. Aufgaben, die einen bestimmten Anbieter benötigen, enthalten einen dieser Tags im Dateinamen:

- `aoai` – benötigt Azure OpenAI-Endpunkt und Schlüssel
- `oai` – benötigt OpenAI-Endpunkt und Schlüssel
- `hf` – benötigt Hugging Face Token

Du kannst einen, keinen oder alle Anbieter konfigurieren. Zugehörige Aufgaben schlagen einfach fehl, wenn Zugangsdaten fehlen.

## Erstellen der `.env`-Datei

Wir gehen davon aus, dass du die obigen Hinweise gelesen, dich beim jeweiligen Anbieter angemeldet und die erforderlichen Zugangsdaten (API_KEY oder Token) erhalten hast. Im Fall von Azure OpenAI gehen wir davon aus, dass du bereits eine gültige Bereitstellung eines Azure OpenAI-Dienstes (Endpunkt) mit mindestens einem GPT-Modell für Chat Completion hast.

Der nächste Schritt ist, deine **lokalen Umgebungsvariablen** wie folgt zu konfigurieren:

1. Suche im Hauptverzeichnis nach einer Datei namens `.env.copy`, die in etwa so aussieht:

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

2. Kopiere diese Datei mit folgendem Befehl nach `.env`. Diese Datei ist _gitignore-d_, damit Geheimnisse sicher bleiben.

   ```bash
   cp .env.copy .env
   ```

3. Trage die Werte ein (ersetze Platzhalter rechts vom `=`) wie im nächsten Abschnitt beschrieben.

4. (Optional) Wenn du GitHub Codespaces verwendest, kannst du Umgebungsvariablen als _Codespaces secrets_ für dieses Repository speichern. In diesem Fall musst du keine lokale .env-Datei anlegen. **Beachte jedoch, dass diese Option nur mit GitHub Codespaces funktioniert.** Wenn du stattdessen Docker Desktop verwendest, musst du weiterhin die .env-Datei einrichten.

## `.env`-Datei ausfüllen

Schauen wir uns kurz die Variablennamen an, um zu verstehen, was sie bedeuten:

| Variable  | Beschreibung  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Das ist das Benutzer-Access-Token, das du in deinem Profil eingerichtet hast |
| OPENAI_API_KEY | Das ist der Autorisierungsschlüssel für die Nutzung des Dienstes bei nicht-Azure OpenAI-Endpunkten |
| AZURE_OPENAI_API_KEY | Das ist der Autorisierungsschlüssel für diesen Dienst |
| AZURE_OPENAI_ENDPOINT | Das ist der bereitgestellte Endpunkt für eine Azure OpenAI-Ressource |
| AZURE_OPENAI_DEPLOYMENT | Das ist der Endpunkt für das _Textgenerierungsmodell_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Das ist der Endpunkt für das _Text-Embeddings-Modell_ |
| | |

Hinweis: Die letzten beiden Azure OpenAI-Variablen stehen jeweils für ein Standardmodell für Chat Completion (Textgenerierung) und Vektorsuche (Embeddings). Anweisungen zur Einrichtung findest du in den jeweiligen Aufgaben.

## Azure konfigurieren: Über das Portal

Die Werte für Azure OpenAI-Endpunkt und -Schlüssel findest du im [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst). Gehe dazu wie folgt vor:

1. Gehe zum [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Klicke im Seitenmenü (links) auf **Schlüssel und Endpunkt**.
1. Klicke auf **Schlüssel anzeigen** – du solltest nun sehen: SCHLÜSSEL 1, SCHLÜSSEL 2 und Endpunkt.
1. Verwende den Wert von SCHLÜSSEL 1 für AZURE_OPENAI_API_KEY
1. Verwende den Wert von Endpunkt für AZURE_OPENAI_ENDPOINT

Als Nächstes benötigen wir die Endpunkte für die spezifischen Modelle, die wir bereitgestellt haben.

1. Klicke im Seitenmenü (links) der Azure OpenAI-Ressource auf **Modellbereitstellungen**.
1. Klicke auf der Zielseite auf **Bereitstellungen verwalten**

Das führt dich zur Azure OpenAI Studio-Website, wo wir die weiteren Werte wie unten beschrieben finden.

## Azure konfigurieren: Über das Studio

1. Navigiere zu [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **ausgehend von deiner Ressource** wie oben beschrieben.
1. Klicke auf den Tab **Bereitstellungen** (Seitenleiste links), um die aktuell bereitgestellten Modelle zu sehen.
1. Falls dein gewünschtes Modell nicht bereitgestellt ist, verwende **Neue Bereitstellung erstellen**, um es bereitzustellen.
1. Du benötigst ein _Textgenerierungsmodell_ – wir empfehlen: **gpt-35-turbo**
1. Du benötigst ein _Text-Embeddings-Modell_ – wir empfehlen **text-embedding-ada-002**

Aktualisiere nun die Umgebungsvariablen entsprechend dem verwendeten _Bereitstellungsnamen_. Dieser ist in der Regel identisch mit dem Modellnamen, sofern du ihn nicht explizit geändert hast. Zum Beispiel könntest du folgendes haben:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Vergiss nicht, die .env-Datei nach dem Ausfüllen zu speichern.** Du kannst die Datei nun schließen und zu den Anweisungen zum Ausführen des Notebooks zurückkehren.

## OpenAI konfigurieren: Über das Profil

Deinen OpenAI API-Schlüssel findest du in deinem [OpenAI-Konto](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Falls du noch keinen hast, kannst du ein Konto anlegen und einen API-Schlüssel erstellen. Sobald du den Schlüssel hast, kannst du ihn in der `.env`-Datei in die Variable `OPENAI_API_KEY` eintragen.

## Hugging Face konfigurieren: Über das Profil

Dein Hugging Face Token findest du in deinem Profil unter [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Teile diese Tokens nicht öffentlich. Erstelle stattdessen ein neues Token speziell für dieses Projekt und trage es in der `.env`-Datei unter der Variable `HUGGING_FACE_API_KEY` ein. _Hinweis:_ Technisch gesehen ist dies kein API-Schlüssel, wird aber zur Authentifizierung verwendet, daher behalten wir diese Bezeichnung zur Konsistenz bei.

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ausgangssprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.