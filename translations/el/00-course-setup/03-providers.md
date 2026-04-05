# Επιλογή & Διαμόρφωση Παρόχου LLM 🔑

Οι εργασίες **μπορεί** επίσης να ρυθμιστούν να λειτουργούν με μία ή περισσότερες αναπτύξεις Μεγάλων Γλωσσικών Μοντέλων (LLM) μέσω ενός υποστηριζόμενου παρόχου υπηρεσιών όπως το OpenAI, το Azure ή το Hugging Face. Αυτοί παρέχουν ένα _φιλοξενούμενο endpoint_ (API) στο οποίο μπορούμε να έχουμε προγραμματισμένη πρόσβαση με τα κατάλληλα διαπιστευτήρια (κλειδί API ή token). Σε αυτό το μάθημα, συζητάμε αυτούς τους παρόχους:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) με διάφορα μοντέλα συμπεριλαμβανομένης της βασικής σειράς GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) για μοντέλα OpenAI με έμφαση στην επιχειρηματική ετοιμότητα
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) για ανοιχτού κώδικα μοντέλα και διακομιστή συμπερασμάτων

**Θα χρειαστεί να χρησιμοποιήσετε τους δικούς σας λογαριασμούς για αυτές τις ασκήσεις**. Οι εργασίες είναι προαιρετικές, οπότε μπορείτε να επιλέξετε να ρυθμίσετε έναν, όλους ή κανέναν από τους παρόχους ανάλογα με τα ενδιαφέροντά σας. Μερικές οδηγίες για εγγραφή:

| Εγγραφή | Κόστος | Κλειδί API | Playground | Σχόλια |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Τιμολόγηση](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Βασισμένο σε έργο](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Χωρίς κώδικα, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Διαθέσιμα Πολλαπλά Μοντέλα |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Τιμολόγηση](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Γρήγορη εκκίνηση SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Γρήγορη εκκίνηση Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Απαιτείται Αίτηση Πρόσβασης](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Τιμολόγηση](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Το Hugging Chat έχει περιορισμένα μοντέλα](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Ακολουθήστε τις παρακάτω οδηγίες για να _διαμορφώσετε_ αυτό το αποθετήριο για χρήση με διαφορετικούς παρόχους. Οι εργασίες που απαιτούν συγκεκριμένο πάροχο θα περιέχουν μία από αυτές τις ετικέτες στο όνομα αρχείου τους:

- `aoai` - απαιτεί endpoint και κλειδί Azure OpenAI
- `oai` - απαιτεί endpoint και κλειδί OpenAI
- `hf` - απαιτεί token Hugging Face

Μπορείτε να διαμορφώσετε έναν, κανέναν ή όλους τους παρόχους. Οι σχετικές εργασίες απλώς θα εμφανίσουν σφάλμα αν λείπουν τα διαπιστευτήρια.

## Δημιουργία αρχείου `.env`

Υποθέτουμε ότι έχετε ήδη διαβάσει τις παραπάνω οδηγίες και έχετε εγγραφεί στον αντίστοιχο πάροχο, και έχετε λάβει τα απαιτούμενα διαπιστευτήρια αυθεντικοποίησης (API_KEY ή token). Στην περίπτωση του Azure OpenAI, υποθέτουμε επίσης ότι έχετε μια έγκυρη ανάπτυξη μιας υπηρεσίας Azure OpenAI (endpoint) με τουλάχιστον ένα μοντέλο GPT αναπτυγμένο για ολοκλήρωση συνομιλίας.

Το επόμενο βήμα είναι να διαμορφώσετε τις **τοπικές μεταβλητές περιβάλλοντος** ως εξής:

1. Κοιτάξτε στον ριζικό φάκελο για ένα αρχείο `.env.copy` που θα πρέπει να έχει περιεχόμενο όπως το παρακάτω:

   ```bash
   # Πάροχος OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI
   AZURE_OPENAI_API_VERSION='2024-02-01' # Η προεπιλογή έχει οριστεί!
   AZURE_OPENAI_API_KEY='<add your AOAI key here>'
   AZURE_OPENAI_ENDPOINT='<add your AOIA service endpoint here>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model name here>' 
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model name here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Αντιγράψτε αυτό το αρχείο σε `.env` χρησιμοποιώντας την παρακάτω εντολή. Αυτό το αρχείο είναι _gitignore-μένο_, κρατώντας τα μυστικά ασφαλή.

   ```bash
   cp .env.copy .env
   ```

3. Συμπληρώστε τις τιμές (αντικαταστήστε τα placeholders στη δεξιά πλευρά του `=`) όπως περιγράφεται στην επόμενη ενότητα.

4. (Προαιρετικό) Αν χρησιμοποιείτε GitHub Codespaces, έχετε την επιλογή να αποθηκεύσετε τις μεταβλητές περιβάλλοντος ως _μυστικά Codespaces_ συνδεδεμένα με αυτό το αποθετήριο. Σε αυτή την περίπτωση, δεν θα χρειαστεί να ρυθμίσετε το τοπικό αρχείο .env. **Ωστόσο, σημειώστε ότι αυτή η επιλογή λειτουργεί μόνο αν χρησιμοποιείτε GitHub Codespaces.** Θα χρειαστείτε ακόμα να ρυθμίσετε το αρχείο .env αν χρησιμοποιείτε Docker Desktop.

## Συμπλήρωση αρχείου `.env`

Ας ρίξουμε μια γρήγορη ματιά στα ονόματα των μεταβλητών για να κατανοήσουμε τι αντιπροσωπεύουν:

| Μεταβλητή  | Περιγραφή  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Αυτό είναι το token πρόσβασης χρήστη που ρυθμίσατε στο προφίλ σας |
| OPENAI_API_KEY | Αυτό είναι το κλειδί εξουσιοδότησης για χρήση της υπηρεσίας για μη-Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Αυτό είναι το κλειδί εξουσιοδότησης για χρήση αυτής της υπηρεσίας |
| AZURE_OPENAI_ENDPOINT | Αυτό είναι το αναπτυγμένο endpoint για έναν πόρο Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Αυτό είναι το endpoint ανάπτυξης μοντέλου _γεννήτριας κειμένου_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Αυτό είναι το endpoint ανάπτυξης μοντέλου _ενσωμάτωσης κειμένου_ |
| | |

Σημείωση: Οι δύο τελευταίες μεταβλητές Azure OpenAI αντιπροσωπεύουν ένα προεπιλεγμένο μοντέλο για ολοκλήρωση συνομιλίας (γεννήτρια κειμένου) και αναζήτηση διανυσμάτων (ενσωματώσεις) αντίστοιχα. Οι οδηγίες για τη ρύθμισή τους θα οριστούν στις σχετικές εργασίες.

## Διαμόρφωση Azure: Από το Portal

Οι τιμές του endpoint και του κλειδιού Azure OpenAI θα βρεθούν στο [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), οπότε ας ξεκινήσουμε από εκεί.

1. Μεταβείτε στο [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Κάντε κλικ στην επιλογή **Keys and Endpoint** στο πλαϊνό μενού (μενού αριστερά).
1. Κάντε κλικ στο **Show Keys** - θα δείτε τα εξής: KEY 1, KEY 2 και Endpoint.
1. Χρησιμοποιήστε την τιμή του KEY 1 για το AZURE_OPENAI_API_KEY
1. Χρησιμοποιήστε την τιμή του Endpoint για το AZURE_OPENAI_ENDPOINT

Στη συνέχεια, χρειαζόμαστε τα endpoints για τα συγκεκριμένα μοντέλα που έχουμε αναπτύξει.

1. Κάντε κλικ στην επιλογή **Model deployments** στο πλαϊνό μενού (αριστερό μενού) για τον πόρο Azure OpenAI.
1. Στη σελίδα προορισμού, κάντε κλικ στο **Manage Deployments**

Αυτό θα σας μεταφέρει στην ιστοσελίδα Azure OpenAI Studio, όπου θα βρούμε τις υπόλοιπες τιμές όπως περιγράφεται παρακάτω.

## Διαμόρφωση Azure: Από το Studio

1. Μεταβείτε στο [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **από τον πόρο σας** όπως περιγράφτηκε παραπάνω.
1. Κάντε κλικ στην καρτέλα **Deployments** (πλαϊνό μενού, αριστερά) για να δείτε τα μοντέλα που είναι αυτή τη στιγμή αναπτυγμένα.
1. Αν το επιθυμητό μοντέλο δεν είναι αναπτυγμένο, χρησιμοποιήστε το **Create new deployment** για να το αναπτύξετε.
1. Θα χρειαστείτε ένα μοντέλο _γεννήτριας κειμένου_ - προτείνουμε: **gpt-35-turbo**
1. Θα χρειαστείτε ένα μοντέλο _ενσωμάτωσης κειμένου_ - προτείνουμε **text-embedding-ada-002**

Τώρα ενημερώστε τις μεταβλητές περιβάλλοντος ώστε να αντικατοπτρίζουν το _Όνομα Ανάπτυξης_ που χρησιμοποιήθηκε. Αυτό συνήθως θα είναι το ίδιο με το όνομα του μοντέλου εκτός αν το αλλάξατε ρητά. Έτσι, για παράδειγμα, μπορεί να έχετε:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Μην ξεχάσετε να αποθηκεύσετε το αρχείο .env όταν τελειώσετε**. Μπορείτε τώρα να κλείσετε το αρχείο και να επιστρέψετε στις οδηγίες για την εκτέλεση του σημειωματάριου.

## Διαμόρφωση OpenAI: Από το Προφίλ

Το κλειδί API του OpenAI μπορείτε να το βρείτε στον [λογαριασμό σας OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Αν δεν έχετε, μπορείτε να εγγραφείτε και να δημιουργήσετε ένα κλειδί API. Μόλις έχετε το κλειδί, μπορείτε να το χρησιμοποιήσετε για να συμπληρώσετε τη μεταβλητή `OPENAI_API_KEY` στο αρχείο `.env`.

## Διαμόρφωση Hugging Face: Από το Προφίλ

Το token Hugging Face μπορείτε να το βρείτε στο προφίλ σας στην ενότητα [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Μην το δημοσιεύετε ή μοιράζεστε δημόσια. Αντίθετα, δημιουργήστε ένα νέο token για τη χρήση αυτού του έργου και αντιγράψτε το στο αρχείο `.env` κάτω από τη μεταβλητή `HUGGING_FACE_API_KEY`. _Σημείωση:_ Τεχνικά αυτό δεν είναι κλειδί API αλλά χρησιμοποιείται για αυθεντικοποίηση, οπότε διατηρούμε αυτή την ονομασία για συνέπεια.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να λάβετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->