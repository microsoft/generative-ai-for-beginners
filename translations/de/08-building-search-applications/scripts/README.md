<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T10:27:29+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "de"
}
-->
# Vorbereitung von Transkriptionsdaten

Die Skripte zur Vorbereitung von Transkriptionsdaten laden YouTube-Video-Transkripte herunter und bereiten sie für die Verwendung mit der semantischen Suche mit OpenAI Embeddings und Functions-Beispielen vor.

Die Skripte zur Vorbereitung von Transkriptionsdaten wurden auf den neuesten Versionen von Windows 11, macOS Ventura und Ubuntu 22.04 (und höher) getestet.

## Erstellen der erforderlichen Azure OpenAI Service-Ressourcen

> [!IMPORTANT]
> Wir empfehlen, die Azure CLI auf die neueste Version zu aktualisieren, um die Kompatibilität mit OpenAI sicherzustellen.
> Siehe [Dokumentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Erstellen Sie eine Ressourcengruppe

> [!NOTE]
> Für diese Anweisungen verwenden wir die Ressourcengruppe namens "semantic-video-search" in East US.
> Sie können den Namen der Ressourcengruppe ändern, aber wenn Sie den Standort der Ressourcen ändern,
> überprüfen Sie die [Modellverfügbarkeitstabelle](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Erstellen Sie eine Azure OpenAI Service-Ressource.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Holen Sie sich den Endpunkt und die Schlüssel für die Verwendung in dieser Anwendung

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Bereitstellen der folgenden Modelle:
   - `text-embedding-ada-002` version `2` or greater, named `text-embedding-ada-002`
   - `gpt-35-turbo` version `0613` or greater, named `gpt-35-turbo`

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

Die folgenden Umgebungsvariablen sind erforderlich, um die Skripte zur Vorbereitung von YouTube-Transkriptionsdaten auszuführen.

### Auf Windows

Es wird empfohlen, die Variablen zu Ihrem `Benutzer` environment variables.
`Windows Start` > `Systemumgebungsvariablen bearbeiten` > `Umgebungsvariablen` > `Benutzervariablen` for [USER] > `Neu` hinzuzufügen.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Auf Linux und macOS

Es wird empfohlen, die folgenden Exporte zu Ihrer `~/.bashrc` or `~/.zshrc` Datei hinzuzufügen.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Installieren der erforderlichen Python-Bibliotheken

1. Installieren Sie den [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst), falls noch nicht installiert.
1. Klonen Sie das Beispiel aus einem `Terminal`-Fenster in Ihren bevorzugten Repository-Ordner.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Navigieren Sie zum `data_prep` Ordner.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Erstellen Sie eine Python-virtuelle Umgebung.

    Auf Windows:

    ```powershell
    python -m venv .venv
    ```

    Auf macOS und Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Aktivieren Sie die Python-virtuelle Umgebung.

   Auf Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   Auf macOS und Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Installieren Sie die erforderlichen Bibliotheken.

   Auf Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Auf macOS und Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Ausführen der YouTube-Transkriptionsdaten-Vorbereitungsskripte

### Auf Windows

```powershell
.\transcripts_prepare.ps1
```

### Auf macOS und Linux

```bash
./transcripts_prepare.sh
```

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Verwendung dieser Übersetzung ergeben.