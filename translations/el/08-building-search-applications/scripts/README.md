# Προετοιμασία δεδομένων μεταγραφής

Τα σενάρια προετοιμασίας δεδομένων μεταγραφής κατεβάζουν τα απομαγνητοφωνημένα κείμενα βίντεο από το YouTube και τα προετοιμάζουν για χρήση με το δείγμα Αναζήτησης Σημασιολογίας με OpenAI Embeddings και Λειτουργίες.

Τα σενάρια προετοιμασίας δεδομένων μεταγραφής έχουν δοκιμαστεί στις τελευταίες εκδόσεις των Windows 11, macOS Ventura και Ubuntu 22.04 (και νεότερα).

## Δημιουργία απαιτούμενων πόρων Azure OpenAI Service

> [!IMPORTANT]
> Σας προτείνουμε να ενημερώσετε το Azure CLI στην τελευταία έκδοση για να εξασφαλίσετε συμβατότητα με το OpenAI
> Δείτε [Documentation](https://learn.microsoft.com/cli/azure/update-azure-cli?WT.mc_id=academic-105485-koreyst)

1. Δημιουργήστε μια ομάδα πόρων

> [!NOTE]
> Για αυτές τις οδηγίες χρησιμοποιούμε την ομάδα πόρων με όνομα "semantic-video-search" στην Ανατολική Αμερική.
> Μπορείτε να αλλάξετε το όνομα της ομάδας πόρων, αλλά όταν αλλάζετε την τοποθεσία των πόρων, 
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
   - `text-embedding-ada-002` έκδοση `2` ή μεγαλύτερη, με όνομα `text-embedding-ada-002`
   - `gpt-5-mini` με όνομα `gpt-5-mini`

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
    --deployment-name gpt-5-mini \
    --model-name gpt-5-mini \
    --model-format OpenAI \
    --sku-capacity 100 \
    --sku-name "Standard"
```

## Απαραίτητο λογισμικό

- [Python 3.9](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst) ή νεότερο

## Μεταβλητές περιβάλλοντος

Οι παρακάτω μεταβλητές περιβάλλοντος είναι απαραίτητες για την εκτέλεση των σεναρίων προετοιμασίας δεδομένων μεταγραφής YouTube.

### Σε Windows

Συνιστάται να προσθέσετε τις μεταβλητές στις μεταβλητές περιβάλλοντος του `user`.
`Έναρξη Windows` > `Επεξεργασία μεταβλητών συστήματος` > `Μεταβλητές περιβάλλοντος` > `Μεταβλητές χρήστη` για [USER] > `Νέο`.

```text
AZURE_OPENAI_API_KEY  \<your Azure OpenAI Service API key>
AZURE_OPENAI_ENDPOINT \<your Azure OpenAI Service endpoint>
AZURE_OPENAI_MODEL_DEPLOYMENT_NAME \<your Azure OpenAI Service model deployment name>
GOOGLE_DEVELOPER_API_KEY = \<your Google developer API key>
```

<!-- Μπορείτε να προσθέσετε τις μεταβλητές περιβάλλοντος στο προφίλ του PowerShell σας.

```powershell
$env:AZURE_OPENAI_API_KEY = "<το κλειδί API της υπηρεσίας Azure OpenAI σας>"
$env:AZURE_OPENAI_ENDPOINT = "<το endpoint της υπηρεσίας Azure OpenAI σας>"
$env:AZURE_OPENAI_MODEL_DEPLOYMENT_NAME = "<το όνομα ανάπτυξης μοντέλου Azure OpenAI σας>"
$env:GOOGLE_DEVELOPER_API_KEY = "<το κλειδί API προγραμματιστή Google σας>"
``` -->

### Σε Linux και macOS

Συνιστάται να προσθέσετε τις παρακάτω εξαγωγές στο αρχείο `~/.bashrc` ή `~/.zshrc`.

```bash
export AZURE_OPENAI_API_KEY=<your Azure OpenAI Service API key>
export AZURE_OPENAI_ENDPOINT=<your Azure OpenAI Service endpoint>
export AZURE_OPENAI_MODEL_DEPLOYMENT_NAME=<your Azure OpenAI Service model deployment name>
export GOOGLE_DEVELOPER_API_KEY=<your Google developer API key>
```

## Εγκατάσταση των απαραίτητων βιβλιοθηκών Python

1. Εγκαταστήστε τον [git client](https://git-scm.com/downloads?WT.mc_id=academic-105485-koreyst) αν δεν είναι ήδη εγκατεστημένος.
1. Από ένα παράθυρο `Τερματικού`, αντιγράψτε το δείγμα στον προτιμώμενο φάκελο αποθετηρίου σας.

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

## Εκτελέστε τα σενάρια προετοιμασίας δεδομένων μεταγραφής YouTube

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