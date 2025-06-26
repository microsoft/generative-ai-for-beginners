<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0d69f2d5814a698d3de5d0235940b5ae",
  "translation_date": "2025-06-25T16:55:14+00:00",
  "source_file": "08-building-search-applications/scripts/README.md",
  "language_code": "el"
}
-->
# Προετοιμασία δεδομένων απομαγνητοφώνησης

Τα σενάρια προετοιμασίας δεδομένων απομαγνητοφώνησης κατεβάζουν απομαγνητοφωνήσεις βίντεο από το YouTube και τα προετοιμάζουν για χρήση με το δείγμα Αναζήτησης Σημασιολογίας με Ενσωματώσεις και Λειτουργίες του OpenAI.

Τα σενάρια προετοιμασίας δεδομένων απομαγνητοφώνησης έχουν δοκιμαστεί στις τελευταίες εκδόσεις των Windows 11, macOS Ventura και Ubuntu 22.04 (και άνω).

## Δημιουργία των απαραίτητων πόρων της Υπηρεσίας Azure OpenAI

> [!IMPORTANT]
> Προτείνουμε να ενημερώσετε το Azure CLI στην τελευταία έκδοση για να εξασφαλίσετε τη συμβατότητα με το OpenAI.
> Δείτε [Τεκμηρίωση](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Δημιουργήστε μια ομάδα πόρων

> [!NOTE]
> Για αυτές τις οδηγίες χρησιμοποιούμε την ομάδα πόρων με όνομα "semantic-video-search" στην Ανατολική ΗΠΑ.
> Μπορείτε να αλλάξετε το όνομα της ομάδας πόρων, αλλά όταν αλλάζετε την τοποθεσία για τους πόρους,
> ελέγξτε τον [πίνακα διαθεσιμότητας μοντέλων](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```console
az group create --name semantic-video-search --location eastus
```

1. Δημιουργήστε έναν πόρο της Υπηρεσίας Azure OpenAI.

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

1. Αναπτύξτε τα παρακάτω μοντέλα:
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

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ή νεότερη έκδοση

## Μεταβλητές περιβάλλοντος

Οι παρακάτω μεταβλητές περιβάλλοντος απαιτούνται για την εκτέλεση των σεναρίων προετοιμασίας δεδομένων απομαγνητοφώνησης του YouTube.

### Στα Windows

Συνιστάται η προσθήκη των μεταβλητών στον `user` environment variables.
`Windows Start` > `Edit the system environment variables` > `Environment Variables` > `User variables` for [USER] > `New`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

### Στο Linux και το macOS

Συνιστάται η προσθήκη των παρακάτω εξαγωγών στο αρχείο `~/.bashrc` or `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Εγκατάσταση των απαιτούμενων βιβλιοθηκών Python

1. Εγκαταστήστε τον [πελάτη git](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) αν δεν είναι ήδη εγκατεστημένος.
1. Από ένα παράθυρο `Terminal`, κλωνοποιήστε το δείγμα στον προτιμώμενο φάκελο αποθετηρίου σας.

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

    Στο macOS και το Linux:

    ```bash
    python3 -m venv .venv
    ```

1. Ενεργοποιήστε το εικονικό περιβάλλον Python.

   Στα Windows:

   ```powershell
   .venv\Scripts\activate
   ```

   Στο macOS και το Linux:

   ```bash
   source .venv/bin/activate
   ```

1. Εγκαταστήστε τις απαιτούμενες βιβλιοθήκες.

   Στα Windows:

   ```powershell
   pip install -r requirements.txt
   ```

   Στο macOS και το Linux:

   ```bash
   pip3 install -r requirements.txt
   ```

## Εκτέλεση των σεναρίων προετοιμασίας δεδομένων απομαγνητοφώνησης του YouTube

### Στα Windows

```powershell
.\transcripts_prepare.ps1
```

### Στο macOS και το Linux

```bash
./transcripts_prepare.sh
```

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που προσπαθούμε για την ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτοματοποιημένες μεταφράσεις μπορεί να περιέχουν λάθη ή ανακρίβειες. Το αρχικό έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η έγκυρη πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για οποιεσδήποτε παρανοήσεις ή παρερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.