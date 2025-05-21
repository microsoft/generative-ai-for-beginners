<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-05-19T12:48:45+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "el"
}
-->
# Ρύθμιση του Περιβάλλοντος Ανάπτυξης

Έχουμε δημιουργήσει αυτό το αποθετήριο και το μάθημα με ένα [container ανάπτυξης](https://containers.dev?WT.mc_id=academic-105485-koreyst) που διαθέτει έναν καθολικό χρόνο εκτέλεσης για ανάπτυξη σε Python3, .NET, Node.js και Java. Η σχετική διαμόρφωση ορίζεται στο αρχείο `devcontainer.json` που βρίσκεται στον φάκελο `.devcontainer/` στη ρίζα αυτού του αποθετηρίου.

Για να ενεργοποιήσετε το container ανάπτυξης, εκκινήστε το στο [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (για χρόνο εκτέλεσης φιλοξενούμενο στο cloud) ή στο [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (για χρόνο εκτέλεσης φιλοξενούμενο σε τοπική συσκευή). Διαβάστε [αυτήν την τεκμηρίωση](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) για περισσότερες λεπτομέρειες σχετικά με το πώς λειτουργούν τα containers ανάπτυξης στο VS Code.

> [!TIP]  
> Προτείνουμε τη χρήση του GitHub Codespaces για γρήγορη εκκίνηση με ελάχιστη προσπάθεια. Παρέχει μια γενναιόδωρη [ποσόστωση δωρεάν χρήσης](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) για προσωπικούς λογαριασμούς. Ρυθμίστε [χρονικά όρια](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) για να σταματήσετε ή να διαγράψετε ανενεργά codespaces για μέγιστη χρήση της ποσόστωσης σας.

## 1. Εκτέλεση Εργασιών

Κάθε μάθημα θα περιλαμβάνει _προαιρετικές_ εργασίες που μπορεί να προσφέρονται σε μία ή περισσότερες γλώσσες προγραμματισμού όπως: Python, .NET/C#, Java και JavaScript/TypeScript. Αυτή η ενότητα παρέχει γενικές οδηγίες για την εκτέλεση αυτών των εργασιών.

### 1.1 Εργασίες Python

Οι εργασίες Python παρέχονται είτε ως εφαρμογές (αρχεία `.py`) είτε ως σημειωματάρια Jupyter (αρχεία `.ipynb`). 
- Για να εκτελέσετε το σημειωματάριο, ανοίξτε το στο Visual Studio Code και κάντε κλικ στο _Select Kernel_ (πάνω δεξιά) και επιλέξτε την προεπιλεγμένη επιλογή Python 3 που εμφανίζεται. Μπορείτε τώρα να εκτελέσετε _Run All_ για να εκτελέσετε το σημειωματάριο.
- Για να εκτελέσετε εφαρμογές Python από τη γραμμή εντολών, ακολουθήστε τις οδηγίες της εργασίας για να βεβαιωθείτε ότι επιλέγετε τα σωστά αρχεία και παρέχετε τα απαιτούμενα επιχειρήματα.

## 2. Διαμόρφωση Παρόχων

Οι εργασίες **μπορεί** να είναι επίσης ρυθμισμένες για να λειτουργούν με μία ή περισσότερες αναπτύξεις Μεγάλων Γλωσσικών Μοντέλων (LLM) μέσω ενός υποστηριζόμενου παρόχου υπηρεσιών όπως OpenAI, Azure ή Hugging Face. Αυτοί παρέχουν ένα _φιλοξενούμενο σημείο πρόσβασης_ (API) που μπορούμε να προσεγγίσουμε προγραμματιστικά με τα σωστά διαπιστευτήρια (API key ή token). Σε αυτό το μάθημα, συζητάμε αυτούς τους παρόχους:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) με διάφορα μοντέλα, συμπεριλαμβανομένης της βασικής σειράς GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) για μοντέλα OpenAI με έμφαση στην επιχειρηματική ετοιμότητα
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) για ανοιχτού κώδικα μοντέλα και εξυπηρετητή υπολογισμών

**Θα χρειαστεί να χρησιμοποιήσετε τους δικούς σας λογαριασμούς για αυτές τις ασκήσεις**. Οι εργασίες είναι προαιρετικές, επομένως μπορείτε να επιλέξετε να ρυθμίσετε έναν, όλους - ή κανέναν - από τους παρόχους με βάση τα ενδιαφέροντά σας. Κάποιες οδηγίες για την εγγραφή:

| Εγγραφή | Κόστος | Κλειδί API | Χώρος Παιχνιδιού | Σχόλια |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Τιμές](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Με βάση το έργο](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Χωρίς κώδικα, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Διαθέσιμα πολλαπλά μοντέλα |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Τιμές](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Γρήγορη εκκίνηση SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Γρήγορη εκκίνηση Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Πρέπει να εφαρμόσετε εκ των προτέρων για πρόσβαση](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Τιμές](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Το Hugging Chat έχει περιορισμένα μοντέλα](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Ακολουθήστε τις παρακάτω οδηγίες για να _διαμορφώσετε_ αυτό το αποθετήριο για χρήση με διαφορετικούς παρόχους. Οι εργασίες που απαιτούν συγκεκριμένο πάροχο θα περιέχουν μία από αυτές τις ετικέτες στο όνομα του αρχείου τους:
 - `aoai` - απαιτεί το Azure OpenAI endpoint, key
 - `oai` - απαιτεί το OpenAI endpoint, key
 - `hf` - απαιτεί το Hugging Face token

Μπορείτε να διαμορφώσετε έναν, κανέναν ή όλους τους παρόχους. Οι σχετικές εργασίες απλά θα εμφανίσουν σφάλμα αν λείπουν τα διαπιστευτήρια.

### 2.1 Δημιουργία `.env` αρχείου

Υποθέτουμε ότι έχετε ήδη διαβάσει τις παραπάνω οδηγίες και έχετε εγγραφεί στον σχετικό πάροχο, και έχετε αποκτήσει τα απαιτούμενα διαπιστευτήρια αυθεντικοποίησης (API_KEY ή token). Στην περίπτωση του Azure OpenAI, υποθέτουμε ότι έχετε επίσης μια έγκυρη ανάπτυξη μιας υπηρεσίας Azure OpenAI (endpoint) με τουλάχιστον ένα GPT μοντέλο αναπτυγμένο για ολοκλήρωση συνομιλίας.

Το επόμενο βήμα είναι να διαμορφώσετε τις **τοπικές μεταβλητές περιβάλλοντος** σας ως εξής:

1. Κοιτάξτε στο φάκελο ρίζας για ένα `.env.copy` αρχείο που θα πρέπει να έχει περιεχόμενο όπως αυτό:

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

2. Αντιγράψτε αυτό το αρχείο στο `.env` χρησιμοποιώντας την παρακάτω εντολή. Αυτό το αρχείο είναι _gitignore-d_, διατηρώντας τα μυστικά ασφαλή.

   ```bash
   cp .env.copy .env
   ```

3. Συμπληρώστε τις τιμές (αντικαταστήστε τα placeholders στη δεξιά πλευρά του `=`) όπως περιγράφεται στην επόμενη ενότητα.

3. (Προαιρετικά) Εάν χρησιμοποιείτε το GitHub Codespaces, έχετε την επιλογή να αποθηκεύσετε τις μεταβλητές περιβάλλοντος ως _Codespaces secrets_ που σχετίζονται με αυτό το αποθετήριο. Σε αυτήν την περίπτωση, δεν θα χρειαστεί να ρυθμίσετε ένα τοπικό αρχείο .env. **Ωστόσο, σημειώστε ότι αυτή η επιλογή λειτουργεί μόνο εάν χρησιμοποιείτε το GitHub Codespaces.** Θα χρειαστεί να ρυθμίσετε το αρχείο .env εάν χρησιμοποιείτε το Docker Desktop αντί αυτού.

### 2.2 Συμπλήρωση `.env` αρχείου

Ας ρίξουμε μια γρήγορη ματιά στα ονόματα των μεταβλητών για να κατανοήσουμε τι αντιπροσωπεύουν:

| Μεταβλητή  | Περιγραφή  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Αυτό είναι το token πρόσβασης χρήστη που ρυθμίσατε στο προφίλ σας |
| OPENAI_API_KEY | Αυτό είναι το κλειδί εξουσιοδότησης για τη χρήση της υπηρεσίας για μη-Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Αυτό είναι το κλειδί εξουσιοδότησης για τη χρήση αυτής της υπηρεσίας |
| AZURE_OPENAI_ENDPOINT | Αυτό είναι το αναπτυγμένο endpoint για έναν Azure OpenAI πόρο |
| AZURE_OPENAI_DEPLOYMENT | Αυτό είναι το _text generation_ μοντέλο ανάπτυξης endpoint |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Αυτό είναι το _text embeddings_ μοντέλο ανάπτυξης endpoint |
| | |

Σημείωση: Οι τελευταίες δύο μεταβλητές του Azure OpenAI αντανακλούν ένα προεπιλεγμένο μοντέλο για ολοκλήρωση συνομιλίας (text generation) και αναζήτηση με διανύσματα (embeddings) αντίστοιχα. Οι οδηγίες για τη ρύθμισή τους θα οριστούν στις σχετικές εργασίες.

### 2.3 Διαμόρφωση Azure: Από το Portal

Οι τιμές του Azure OpenAI endpoint και key θα βρεθούν στο [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), οπότε ας ξεκινήσουμε από εκεί.

1. Πηγαίνετε στο [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Κάντε κλικ στην επιλογή **Keys and Endpoint** στην πλευρική μπάρα (μενού στα αριστερά).
1. Κάντε κλικ στο **Show Keys** - θα πρέπει να δείτε τα εξής: KEY 1, KEY 2 και Endpoint.
1. Χρησιμοποιήστε την τιμή KEY 1 για το AZURE_OPENAI_API_KEY
1. Χρησιμοποιήστε την τιμή Endpoint για το AZURE_OPENAI_ENDPOINT

Στη συνέχεια, χρειαζόμαστε τα endpoints για τα συγκεκριμένα μοντέλα που έχουμε αναπτύξει.

1. Κάντε κλικ στην επιλογή **Model deployments** στην πλευρική μπάρα (αριστερό μενού) για τον πόρο Azure OpenAI.
1. Στη σελίδα προορισμού, κάντε κλικ στο **Manage Deployments**

Αυτό θα σας οδηγήσει στην ιστοσελίδα Azure OpenAI Studio, όπου θα βρούμε τις άλλες τιμές όπως περιγράφεται παρακάτω.

### 2.4 Διαμόρφωση Azure: Από το Studio

1. Μεταβείτε στο [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **από τον πόρο σας** όπως περιγράφεται παραπάνω.
1. Κάντε κλικ στην καρτέλα **Deployments** (πλευρική μπάρα, αριστερά) για να δείτε τα μοντέλα που έχουν ήδη αναπτυχθεί.
1. Εάν το επιθυμητό μοντέλο σας δεν έχει αναπτυχθεί, χρησιμοποιήστε το **Create new deployment** για να το αναπτύξετε.
1. Θα χρειαστείτε ένα _text-generation_ μοντέλο - προτείνουμε: **gpt-35-turbo**
1. Θα χρειαστείτε ένα _text-embedding_ μοντέλο - προτείνουμε **text-embedding-ada-002**

Τώρα ενημερώστε τις μεταβλητές περιβάλλοντος για να αντανακλούν το _Deployment name_ που χρησιμοποιήθηκε. Αυτό θα είναι συνήθως το ίδιο με το όνομα του μοντέλου, εκτός αν το αλλάξατε ρητά. Έτσι, ως παράδειγμα, μπορεί να έχετε:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Μην ξεχάσετε να αποθηκεύσετε το αρχείο .env όταν τελειώσετε**. Μπορείτε τώρα να κλείσετε το αρχείο και να επιστρέψετε στις οδηγίες για την εκτέλεση του σημειωματάριου.

### 2.5 Διαμόρφωση OpenAI: Από το Προφίλ

Το OpenAI API key σας μπορεί να βρεθεί στον [OpenAI λογαριασμό σας](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Εάν δεν έχετε, μπορείτε να εγγραφείτε για έναν λογαριασμό και να δημιουργήσετε ένα API key. Μόλις έχετε το κλειδί, μπορείτε να το χρησιμοποιήσετε για να συμπληρώσετε τη μεταβλητή `OPENAI_API_KEY` στο `.env` αρχείο.

### 2.6 Διαμόρφωση Hugging Face: Από το Προφίλ

Το Hugging Face token σας μπορεί να βρεθεί στο προφίλ σας κάτω από [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Μην το δημοσιεύετε ή το μοιράζεστε δημόσια. Αντίθετα, δημιουργήστε ένα νέο token για τη χρήση αυτού του έργου και αντιγράψτε το στο `.env` αρχείο κάτω από τη μεταβλητή `HUGGING_FACE_API_KEY`. _Σημείωση:_ Αυτό τεχνικά δεν είναι ένα API key αλλά χρησιμοποιείται για αυθεντικοποίηση, επομένως διατηρούμε αυτήν τη συμβατική ονομασία για συνέπεια.

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ προσπαθούμε για ακρίβεια, παρακαλώ λάβετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις μπορεί να περιέχουν λάθη ή ανακρίβειες. Το αρχικό έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για οποιεσδήποτε παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.