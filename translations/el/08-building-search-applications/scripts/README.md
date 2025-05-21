<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-05-19T18:50:26+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "el"
}
-->
# Προετοιμασία δεδομένων μεταγραφής

Τα σενάρια προετοιμασίας δεδομένων μεταγραφής κατεβάζουν μεταγραφές βίντεο από το YouTube και τα προετοιμάζουν για χρήση με το δείγμα Αναζήτησης Σημασιολογικού περιεχομένου με OpenAI Embeddings και Functions.

Τα σενάρια προετοιμασίας δεδομένων μεταγραφής έχουν δοκιμαστεί στις τελευταίες εκδόσεις Windows 11, macOS Ventura και Ubuntu 22.04 (και άνω).

## Δημιουργία απαιτούμενων πόρων Azure OpenAI Service

> [!IMPORTANT]
> Προτείνουμε να ενημερώσετε το Azure CLI στην τελευταία έκδοση για να εξασφαλίσετε συμβατότητα με το OpenAI
> Δείτε [Τεκμηρίωση](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Δημιουργήστε μια ομάδα πόρων

> [!NOTE]
> Για αυτές τις οδηγίες χρησιμοποιούμε την ομάδα πόρων με το όνομα "semantic-video-search" στην Ανατολική ΗΠΑ.
> Μπορείτε να αλλάξετε το όνομα της ομάδας πόρων, αλλά όταν αλλάζετε την τοποθεσία για τους πόρους, 
> ελέγξτε τον [πίνακα διαθεσιμότητας μοντέλων](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Δημιουργήστε έναν πόρο Azure OpenAI Service.

```console
az cognitiveservices account create --name semantic-video-openai --resource-group semantic-video-search \
    --location eastus --kind OpenAI --sku s0
```

1. Αποκτήστε το endpoint και τα κλειδιά για χρήση σε αυτήν την εφαρμογή

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Αναπτύξτε τα ακόλουθα μοντέλα:
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

## Απαιτούμενο λογισμικό

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ή νεότερη

## Μεταβλητές περιβάλλοντος

Οι ακόλουθες μεταβλητές περιβάλλοντος απαιτούνται για να εκτελέσετε τα σενάρια προετοιμασίας δεδομένων μεταγραφής YouTube.

### Στα Windows

Συνιστούμε να προσθέσετε τις μεταβλητές στον `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Σε Linux και macOS

Συνιστούμε να προσθέσετε τις ακόλουθες εντολές export στο αρχείο σας `~/.bashrc` or `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Εγκατάσταση των απαιτούμενων βιβλιοθηκών Python

1. Εγκαταστήστε τον [πελάτη git](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) αν δεν είναι ήδη εγκατεστημένος.
1. Από ένα παράθυρο `Terminal`, κλωνοποιήστε το δείγμα στο φάκελο αποθετηρίου της επιλογής σας.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Μεταβείτε στο φάκελο `data_prep`.

   ```bash
   cd semanic-search-openai-embeddings-functions/src/data_prep
   ```

1. Δημιουργήστε ένα εικονικό περιβάλλον Python.

    Στα Windows:

    ```powershell
    python -m venv .venv
    ```

    Σε macOS και Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Ενεργοποιήστε το εικονικό περιβάλλον Python.

   Στα Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   Σε macOS και Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Εγκαταστήστε τις απαιτούμενες βιβλιοθήκες.

   Στα Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Σε macOS και Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Εκτέλεση των σεναρίων προετοιμασίας δεδομένων μεταγραφής YouTube

### Στα Windows

```powershell
.\transcripts_prepare.ps1
```

### Σε macOS και Linux

```bash
./transcripts_prepare.sh
```

**Αποποίηση Ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θα πρέπει να θεωρείται η έγκυρη πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή παρερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.