<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f12faf55ab620aef9f6761679b7ac68b",
  "translation_date": "2025-07-09T07:30:19+00:00",
  "source_file": "00-course-setup/SETUP.md",
  "language_code": "el"
}
-->
# Ρύθμιση του Περιβάλλοντος Ανάπτυξής σας

Έχουμε ρυθμίσει αυτό το αποθετήριο και το μάθημα με ένα [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) που διαθέτει ένα Universal runtime το οποίο υποστηρίζει ανάπτυξη σε Python3, .NET, Node.js και Java. Η σχετική διαμόρφωση ορίζεται στο αρχείο `devcontainer.json` που βρίσκεται στον φάκελο `.devcontainer/` στη ρίζα αυτού του αποθετηρίου.

Για να ενεργοποιήσετε το dev container, εκκινήστε το σε [GitHub Codespaces](https://docs.github.com/en/codespaces/overview?WT.mc_id=academic-105485-koreyst) (για cloud-hosted runtime) ή σε [Docker Desktop](https://docs.docker.com/desktop/?WT.mc_id=academic-105485-koreyst) (για τοπικό runtime στη συσκευή σας). Διαβάστε [αυτή την τεκμηρίωση](https://code.visualstudio.com/docs/devcontainers/containers?WT.mc_id=academic-105485-koreyst) για περισσότερες λεπτομέρειες σχετικά με τη λειτουργία των dev containers μέσα στο VS Code.

> [!TIP]  
> Συνιστούμε τη χρήση του GitHub Codespaces για γρήγορη εκκίνηση με ελάχιστη προσπάθεια. Παρέχει έναν γενναιόδωρο [δωρεάν όριο χρήσης](https://docs.github.com/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts?WT.mc_id=academic-105485-koreyst) για προσωπικούς λογαριασμούς. Ρυθμίστε [χρονικά όρια](https://docs.github.com/codespaces/setting-your-user-preferences/setting-your-timeout-period-for-github-codespaces?WT.mc_id=academic-105485-koreyst) για να σταματούν ή να διαγράφονται ανενεργά codespaces ώστε να μεγιστοποιήσετε τη χρήση του ορίου σας.

## 1. Εκτέλεση Ασκήσεων

Κάθε μάθημα θα έχει _προαιρετικές_ ασκήσεις που μπορεί να παρέχονται σε μία ή περισσότερες γλώσσες προγραμματισμού, όπως: Python, .NET/C#, Java και JavaScript/TypeScript. Αυτή η ενότητα παρέχει γενικές οδηγίες σχετικά με την εκτέλεση αυτών των ασκήσεων.

### 1.1 Ασκήσεις Python

Οι ασκήσεις Python παρέχονται είτε ως εφαρμογές (`.py` αρχεία) είτε ως Jupyter notebooks (`.ipynb` αρχεία).  
- Για να τρέξετε το notebook, ανοίξτε το στο Visual Studio Code, κάντε κλικ στο _Select Kernel_ (πάνω δεξιά) και επιλέξτε την προεπιλεγμένη επιλογή Python 3 που εμφανίζεται. Τώρα μπορείτε να κάνετε _Run All_ για να εκτελέσετε το notebook.  
- Για να τρέξετε εφαρμογές Python από τη γραμμή εντολών, ακολουθήστε τις συγκεκριμένες οδηγίες της άσκησης για να βεβαιωθείτε ότι επιλέγετε τα σωστά αρχεία και παρέχετε τα απαιτούμενα ορίσματα.

## 2. Ρύθμιση Παρόχων

Οι ασκήσεις **μπορεί** επίσης να ρυθμιστούν ώστε να λειτουργούν με μία ή περισσότερες αναπτύξεις Μεγάλων Γλωσσικών Μοντέλων (LLM) μέσω υποστηριζόμενου παρόχου υπηρεσιών όπως OpenAI, Azure ή Hugging Face. Αυτοί παρέχουν ένα _hosted endpoint_ (API) στο οποίο μπορούμε να έχουμε πρόσβαση προγραμματιστικά με τα σωστά διαπιστευτήρια (API key ή token). Σε αυτό το μάθημα, συζητάμε τους παρακάτω παρόχους:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) με διάφορα μοντέλα, συμπεριλαμβανομένης της βασικής σειράς GPT.  
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) για μοντέλα OpenAI με έμφαση στην επιχειρησιακή ετοιμότητα  
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) για ανοιχτού κώδικα μοντέλα και inference server

**Θα χρειαστεί να χρησιμοποιήσετε τους δικούς σας λογαριασμούς για αυτές τις ασκήσεις**. Οι ασκήσεις είναι προαιρετικές, οπότε μπορείτε να επιλέξετε να ρυθμίσετε έναν, όλους ή κανέναν από τους παρόχους ανάλογα με τα ενδιαφέροντά σας. Μερικές οδηγίες για εγγραφή:

| Εγγραφή | Κόστος | API Key | Playground | Σχόλια |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst) | [Τιμολόγηση](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst) | [Βασισμένο σε project](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Διαθέσιμα Πολλαπλά Μοντέλα |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst) | [Τιμολόγηση](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst) | [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) | [Απαιτείται Προέγκριση Πρόσβασης](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Τιμολόγηση](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst) | [Το Hugging Chat έχει περιορισμένα μοντέλα](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Ακολουθήστε τις παρακάτω οδηγίες για να _ρυθμίσετε_ αυτό το αποθετήριο ώστε να λειτουργεί με διαφορετικούς παρόχους. Οι ασκήσεις που απαιτούν συγκεκριμένο πάροχο θα περιέχουν ένα από αυτά τα tags στο όνομα αρχείου τους:  
 - `aoai` - απαιτεί Azure OpenAI endpoint, key  
 - `oai` - απαιτεί OpenAI endpoint, key  
 - `hf` - απαιτεί Hugging Face token

Μπορείτε να ρυθμίσετε έναν, κανέναν ή όλους τους παρόχους. Οι σχετικές ασκήσεις απλά θα εμφανίσουν σφάλμα αν λείπουν τα διαπιστευτήρια.

### 2.1. Δημιουργία αρχείου `.env`

Υποθέτουμε ότι έχετε ήδη διαβάσει τις παραπάνω οδηγίες, έχετε εγγραφεί στον αντίστοιχο πάροχο και έχετε λάβει τα απαιτούμενα διαπιστευτήρια αυθεντικοποίησης (API_KEY ή token). Στην περίπτωση του Azure OpenAI, υποθέτουμε επίσης ότι έχετε μια έγκυρη ανάπτυξη Azure OpenAI Service (endpoint) με τουλάχιστον ένα μοντέλο GPT αναπτυγμένο για chat completion.

Το επόμενο βήμα είναι να ρυθμίσετε τις **τοπικές μεταβλητές περιβάλλοντος** ως εξής:

1. Αναζητήστε στον ριζικό φάκελο ένα αρχείο `.env.copy` που θα έχει περιεχόμενο όπως το παρακάτω:

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

2. Αντιγράψτε αυτό το αρχείο σε `.env` χρησιμοποιώντας την παρακάτω εντολή. Αυτό το αρχείο είναι _gitignore-d_, ώστε να κρατά τα μυστικά ασφαλή.

   ```bash
   cp .env.copy .env
   ```

3. Συμπληρώστε τις τιμές (αντικαταστήστε τα placeholders στα δεξιά του `=`) όπως περιγράφεται στην επόμενη ενότητα.

3. (Προαιρετικό) Αν χρησιμοποιείτε GitHub Codespaces, έχετε την επιλογή να αποθηκεύσετε τις μεταβλητές περιβάλλοντος ως _Codespaces secrets_ συνδεδεμένα με αυτό το αποθετήριο. Σε αυτή την περίπτωση, δεν θα χρειαστεί να ρυθμίσετε το τοπικό αρχείο .env. **Ωστόσο, σημειώστε ότι αυτή η επιλογή λειτουργεί μόνο αν χρησιμοποιείτε GitHub Codespaces.** Θα χρειαστεί να ρυθμίσετε το αρχείο .env αν χρησιμοποιείτε Docker Desktop.

### 2.2. Συμπλήρωση αρχείου `.env`

Ας ρίξουμε μια γρήγορη ματιά στα ονόματα των μεταβλητών για να κατανοήσουμε τι αντιπροσωπεύουν:

| Μεταβλητή  | Περιγραφή  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Αυτό είναι το token πρόσβασης χρήστη που έχετε ρυθμίσει στο προφίλ σας |
| OPENAI_API_KEY | Αυτό είναι το κλειδί εξουσιοδότησης για χρήση της υπηρεσίας σε μη Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Αυτό είναι το κλειδί εξουσιοδότησης για χρήση της υπηρεσίας Azure OpenAI |
| AZURE_OPENAI_ENDPOINT | Αυτό είναι το αναπτυγμένο endpoint για έναν πόρο Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Αυτό είναι το endpoint ανάπτυξης μοντέλου _text generation_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Αυτό είναι το endpoint ανάπτυξης μοντέλου _text embeddings_ |
| | |

Σημείωση: Οι δύο τελευταίες μεταβλητές του Azure OpenAI αντιστοιχούν σε προεπιλεγμένα μοντέλα για chat completion (παραγωγή κειμένου) και αναζήτηση με διανύσματα (embeddings) αντίστοιχα. Οι οδηγίες για τη ρύθμισή τους θα οριστούν στις σχετικές ασκήσεις.

### 2.3 Ρύθμιση Azure: Από το Portal

Οι τιμές για το Azure OpenAI endpoint και το κλειδί θα βρεθούν στο [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), οπότε ας ξεκινήσουμε από εκεί.

1. Μεταβείτε στο [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)  
2. Κάντε κλικ στην επιλογή **Keys and Endpoint** στο πλαϊνό μενού (αριστερά).  
3. Κάντε κλικ στο **Show Keys** - θα δείτε τα εξής: KEY 1, KEY 2 και Endpoint.  
4. Χρησιμοποιήστε την τιμή του KEY 1 για το AZURE_OPENAI_API_KEY  
5. Χρησιμοποιήστε την τιμή του Endpoint για το AZURE_OPENAI_ENDPOINT

Στη συνέχεια, χρειαζόμαστε τα endpoints για τα συγκεκριμένα μοντέλα που έχετε αναπτύξει.

1. Κάντε κλικ στην επιλογή **Model deployments** στο πλαϊνό μενού (αριστερά) για τον πόρο Azure OpenAI.  
2. Στη σελίδα που ανοίγει, κάντε κλικ στο **Manage Deployments**

Αυτό θα σας μεταφέρει στην ιστοσελίδα Azure OpenAI Studio, όπου θα βρείτε τις υπόλοιπες τιμές όπως περιγράφεται παρακάτω.

### 2.4 Ρύθμιση Azure: Από το Studio

1. Μεταβείτε στο [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **από τον πόρο σας** όπως περιγράφτηκε παραπάνω.  
2. Κάντε κλικ στην καρτέλα **Deployments** (πλαϊνό μενού, αριστερά) για να δείτε τα μοντέλα που είναι ήδη αναπτυγμένα.  
3. Αν το επιθυμητό μοντέλο δεν είναι αναπτυγμένο, χρησιμοποιήστε το **Create new deployment** για να το αναπτύξετε.  
4. Θα χρειαστείτε ένα μοντέλο _text-generation_ - προτείνουμε: **gpt-35-turbo**  
5. Θα χρειαστείτε ένα μοντέλο _text-embedding_ - προτείνουμε **text-embedding-ada-002**

Τώρα ενημερώστε τις μεταβλητές περιβάλλοντος ώστε να αντικατοπτρίζουν το _Deployment name_ που χρησιμοποιήθηκε. Συνήθως αυτό είναι το ίδιο με το όνομα του μοντέλου, εκτός αν το έχετε αλλάξει ρητά. Για παράδειγμα, μπορεί να έχετε:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Μην ξεχάσετε να αποθηκεύσετε το αρχείο .env όταν τελειώσετε**. Μπορείτε τώρα να κλείσετε το αρχείο και να επιστρέψετε στις οδηγίες για την εκτέλεση του notebook.

### 2.5 Ρύθμιση OpenAI: Από το Προφίλ

Το κλειδί API του OpenAI μπορείτε να το βρείτε στον [λογαριασμό σας στο OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Αν δεν έχετε, μπορείτε να εγγραφείτε και να δημιουργήσετε ένα κλειδί API. Μόλις το αποκτήσετε, μπορείτε να το χρησιμοποιήσετε για να συμπληρώσετε τη μεταβλητή `OPENAI_API_KEY` στο αρχείο `.env`.

### 2.6 Ρύθμιση Hugging Face: Από το Προφίλ

Το token σας στο Hugging Face βρίσκεται στο προφίλ σας στην ενότητα [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Μην το δημοσιοποιείτε ή μοιράζεστε δημόσια. Αντίθετα, δημιουργήστε ένα νέο token για τη χρήση αυτού του έργου και αντιγράψτε το στο αρχείο `.env` στη μεταβλητή `HUGGING_FACE_API_KEY`. _Σημείωση:_ Τεχνικά αυτό δεν είναι API key, αλλά χρησιμοποιείται για αυθεντικοποίηση, οπότε διατηρούμε αυτή την ονομασία για λόγους συνέπειας.

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.