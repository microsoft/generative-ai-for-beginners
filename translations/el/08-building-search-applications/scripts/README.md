# Προετοιμασία δεδομένων μεταγραφής

Τα σενάρια προετοιμασίας δεδομένων μεταγραφής κατεβάζουν μεταγραφές βίντεο από το YouTube και τις προετοιμάζουν για χρήση με το δείγμα Semantic Search with OpenAI Embeddings and Functions.

Τα σενάρια προετοιμασίας δεδομένων μεταγραφής έχουν δοκιμαστεί στις τελευταίες εκδόσεις των Windows 11, macOS Ventura και Ubuntu 22.04 (και νεότερα).

## Δημιουργία απαιτούμενων πόρων Azure OpenAI Service

> [!IMPORTANT]
> Προτείνουμε να ενημερώσετε το Azure CLI στην πιο πρόσφατη έκδοση για να διασφαλίσετε τη συμβατότητα με το OpenAI
> Δείτε την [Τεκμηρίωση](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Δημιουργήστε μια ομάδα πόρων

> [!NOTE]
> Για αυτές τις οδηγίες χρησιμοποιούμε την ομάδα πόρων με όνομα "semantic-video-search" στην περιοχή East US.
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

1. Πάρτε το endpoint και τα κλειδιά για χρήση σε αυτή την εφαρμογή

```console
az cognitiveservices account show --name semantic-video-openai \
   --resource-group  semantic-video-search | jq -r .properties.endpoint
az cognitiveservices account keys list --name semantic-video-openai \
   --resource-group semantic-video-search | jq -r .key1
```

1. Αναπτύξτε τα παρακάτω μοντέλα:
   - `text-embedding-ada-002` έκδοση `2` ή μεγαλύτερη, με όνομα `text-embedding-ada-002`
   - `gpt-4o-mini` με όνομα `gpt-4o-mini`

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
    --deployment-name gpt-4o-mini \
    --model-name gpt-4o-mini \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## Απαιτούμενο λογισμικό

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ή νεότερο

## Μεταβλητές περιβάλλοντος

Οι ακόλουθες μεταβλητές περιβάλλοντος είναι απαραίτητες για την εκτέλεση των σεναρίων προετοιμασίας δεδομένων μεταγραφής YouTube.

### Σε Windows

Συνιστάται να προσθέσετε τις μεταβλητές στα περιβάλλοντα μεταβλητά `user`.
`Έναρξη Windows` > `Επεξεργασία μεταβλητών συστήματος` > `Μεταβλητές Περιβάλλοντος` > `Μεταβλητές χρήστη` για [USER] > `Νέο`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Μπορείτε να προσθέσετε τις μεταβλητές περιβάλλοντος στο προφίλ PowerShell σας.

```powershell
$env:AZURE_OPENAI_API_KEY = "<το κλειδί API της υπηρεσίας Azure OpenAI>"
$env:AZURE_OPENAI_ENDPOINT = "<το endpoint της υπηρεσίας Azure OpenAI>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<το όνομα ανάπτυξης μοντέλου της υπηρεσίας Azure OpenAI>"
$env:GOOGLE_DEVELOPER_API_KEY = "<το κλειδί API προγραμματιστή Google>"
``` -->

### Σε Linux και macOS

Συνιστάται να προσθέσετε τα παρακάτω exports στο αρχείο `~/.bashrc` ή `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Εγκατάσταση των απαιτούμενων βιβλιοθηκών Python

1. Εγκαταστήστε τον [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) εάν δεν είναι ήδη εγκατεστημένος.
1. Από ένα παράθυρο `Τερματικού`, κλωνοποιήστε το δείγμα στο προτιμώμενο φάκελο αποθετηρίου σας.

    ```bash
    git clone https://github.com/gloveboxes/semanic-search-openai-embeddings-functions.git
    ```

1. Μεταβείτε στο φάκελο `data_prep`.

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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->