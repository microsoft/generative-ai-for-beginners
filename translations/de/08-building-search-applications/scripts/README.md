<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:06:35+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "de"
}
-->
# Vorbereitung der Transkriptionsdaten

Die Skripte zur Vorbereitung der Transkriptionsdaten laden YouTube-Video-Transkripte herunter und bereiten sie für die Verwendung mit dem Beispiel Semantic Search mit OpenAI Embeddings und Funktionen vor.

Die Skripte zur Vorbereitung der Transkriptionsdaten wurden auf den neuesten Versionen von Windows 11, macOS Ventura und Ubuntu 22.04 (und höher) getestet.

## Erstellen der erforderlichen Azure OpenAI Service-Ressourcen

> [!IMPORTANT]
> Wir empfehlen, die Azure CLI auf die neueste Version zu aktualisieren, um die Kompatibilität mit OpenAI sicherzustellen.
> Siehe [Dokumentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Erstellen Sie eine Ressourcengruppe

> [!NOTE]
> Für diese Anleitung verwenden wir die Ressourcengruppe mit dem Namen "semantic-video-search" in East US.
> Sie können den Namen der Ressourcengruppe ändern, aber wenn Sie den Standort der Ressourcen ändern, 
> prüfen Sie die [Modellverfügbarkeitstabelle](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Erstellen Sie eine Azure OpenAI Service-Ressource.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Holen Sie sich den Endpunkt und die Schlüssel zur Verwendung in dieser Anwendung

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Stellen Sie die folgenden Modelle bereit:
   - `text-embedding-ada-002` Version `2` oder höher, benannt `text-embedding-ada-002`
   - `gpt-35-turbo` Version `0613` oder höher, benannt `gpt-35-turbo`

```console
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name text-embedding-ada-002 \
    --model-name text-embedding-ada-002 \
    --model-version "2"  \
    --model-format OpenAI \
    --scale-settings-scale-type "Standard"
az cognitiveservices account deployment create \
    --name semantic-video-openai \
    --resource-group  semantic-video-search \
    --deployment-name gpt-35-turbo \
    --model-name gpt-35-turbo \
    --model-version "0613"  \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## Erforderliche Software

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) oder höher

## Umgebungsvariablen

Die folgenden Umgebungsvariablen sind erforderlich, um die Skripte zur Vorbereitung der YouTube-Transkriptionsdaten auszuführen.

### Unter Windows

Es wird empfohlen, die Variablen zu den `Benutzer`-Umgebungsvariablen hinzuzufügen.
`Windows Start` > `Systemumgebungsvariablen bearbeiten` > `Umgebungsvariablen` > `Benutzervariablen` für [USER] > `Neu`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Unter Linux und macOS

Es wird empfohlen, die folgenden Exporte in Ihre `~/.bashrc` oder `~/.zshrc` Datei einzufügen.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Installation der erforderlichen Python-Bibliotheken

1. Installieren Sie den [git-Client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), falls noch nicht installiert.
1. Klonen Sie aus einem `Terminal`-Fenster das Beispiel in Ihren bevorzugten Repo-Ordner.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Navigieren Sie zum Ordner `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Erstellen Sie eine Python-virtuelle Umgebung.

    Unter Windows:

    ```powershell
    python -m venv .venv
    ```

    Unter macOS und Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Aktivieren Sie die Python-virtuelle Umgebung.

   Unter Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   Unter macOS und Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Installieren Sie die erforderlichen Bibliotheken.

   Unter Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Unter macOS und Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Ausführen der Skripte zur Vorbereitung der YouTube-Transkriptionsdaten

### Unter Windows

```powershell
.\transcripts_prepare.ps1
```

### Unter macOS und Linux

```bash
./transcripts_prepare.sh
```

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.