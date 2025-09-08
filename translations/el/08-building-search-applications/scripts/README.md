<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-07-09T13:10:04+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "el"
}
-->
# Προετοιμασία δεδομένων μεταγραφής

Τα σενάρια προετοιμασίας δεδομένων μεταγραφής κατεβάζουν απομαγνητοφωνήσεις βίντεο από το YouTube και τα προετοιμάζουν για χρήση με το παράδειγμα Semantic Search με OpenAI Embeddings και Functions.

Τα σενάρια προετοιμασίας δεδομένων μεταγραφής έχουν δοκιμαστεί στις πιο πρόσφατες εκδόσεις Windows 11, macOS Ventura και Ubuntu 22.04 (και νεότερες).

## Δημιουργία απαιτούμενων πόρων Azure OpenAI Service

> [!IMPORTANT]
> Σας προτείνουμε να ενημερώσετε το Azure CLI στην πιο πρόσφατη έκδοση για να διασφαλίσετε τη συμβατότητα με το OpenAI
> Δείτε [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Δημιουργήστε μια ομάδα πόρων

> [!NOTE]
> Για αυτές τις οδηγίες χρησιμοποιούμε την ομάδα πόρων με όνομα "semantic-video-search" στην περιοχή East US.
> Μπορείτε να αλλάξετε το όνομα της ομάδας πόρων, αλλά αν αλλάξετε την τοποθεσία των πόρων,
> ελέγξτε τον [πίνακα διαθεσιμότητας μοντέλων](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Δημιουργήστε έναν πόρο Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Πάρτε το endpoint και τα κλειδιά για χρήση σε αυτήν την εφαρμογή

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Αναπτύξτε τα παρακάτω μοντέλα:
   - `text-embedding-ada-002` έκδοση `2` ή νεότερη, με όνομα `text-embedding-ada-002`
   - `gpt-35-turbo` έκδοση `0613` ή νεότερη, με όνομα `gpt-35-turbo`

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

## Απαιτούμενο λογισμικό

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ή νεότερη

## Μεταβλητές περιβάλλοντος

Οι παρακάτω μεταβλητές περιβάλλοντος απαιτούνται για την εκτέλεση των σεναρίων προετοιμασίας δεδομένων μεταγραφής YouTube.

### Σε Windows

Συνιστάται να προσθέσετε τις μεταβλητές στα περιβάλλοντα μεταβλητών `user`.
`Έναρξη των Windows` > `Επεξεργασία μεταβλητών συστήματος` > `Μεταβλητές περιβάλλοντος` > `Μεταβλητές χρήστη` για [USER] > `Νέο`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Σε Linux και macOS

Συνιστάται να προσθέσετε τις παρακάτω εντολές εξαγωγής στο αρχείο `~/.bashrc` ή `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Εγκατάσταση των απαιτούμενων βιβλιοθηκών Python

1. Εγκαταστήστε τον [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) αν δεν είναι ήδη εγκατεστημένος.
1. Από ένα παράθυρο `Terminal`, κλωνοποιήστε το παράδειγμα στον προτιμώμενο φάκελο αποθετηρίου.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Μεταβείτε στον φάκελο `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Δημιουργήστε ένα εικονικό περιβάλλον Python.

    Σε Windows:

    ```powershell
    python -m venv .venv
    ```

    Σε macOS και Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Ενεργοποιήστε το εικονικό περιβάλλον Python.

   Σε Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   Σε macOS και Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Εγκαταστήστε τις απαιτούμενες βιβλιοθήκες.

   Σε Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Σε macOS και Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Εκτέλεση των σεναρίων προετοιμασίας δεδομένων μεταγραφής YouTube

### Σε Windows

```powershell
.\transcripts_prepare.ps1
```

### Σε macOS και Linux

```bash
./transcripts_prepare.sh
```

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.