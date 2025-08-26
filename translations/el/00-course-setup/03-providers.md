<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "49ededa179004ea998664c780fbeac39",
  "translation_date": "2025-08-26T16:56:14+00:00",
  "source_file": "00-course-setup/03-providers.md",
  "language_code": "el"
}
-->
# Επιλογή & Ρύθμιση Παρόχου LLM 🔑

Οι ασκήσεις **μπορεί** να ρυθμιστούν ώστε να λειτουργούν με μία ή περισσότερες αναπτύξεις Μεγάλων Γλωσσικών Μοντέλων (LLM) μέσω ενός υποστηριζόμενου παρόχου υπηρεσιών όπως το OpenAI, το Azure ή το Hugging Face. Αυτοί παρέχουν ένα _φιλοξενούμενο endpoint_ (API) στο οποίο έχουμε πρόσβαση προγραμματιστικά με τα κατάλληλα διαπιστευτήρια (API key ή token). Σε αυτό το μάθημα, συζητάμε τους εξής παρόχους:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) με διάφορα μοντέλα, συμπεριλαμβανομένης της βασικής σειράς GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) για μοντέλα OpenAI με έμφαση στην επιχειρησιακή ετοιμότητα
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) για ανοιχτού κώδικα μοντέλα και inference server

**Θα χρειαστεί να χρησιμοποιήσετε τους δικούς σας λογαριασμούς για αυτές τις ασκήσεις**. Οι ασκήσεις είναι προαιρετικές, οπότε μπορείτε να επιλέξετε να ρυθμίσετε έναν, όλους - ή κανέναν - από τους παρόχους ανάλογα με τα ενδιαφέροντά σας. Μερικές οδηγίες για εγγραφή:

| Εγγραφή | Κόστος | API Key | Playground | Σχόλια |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Τιμές](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Ανά έργο](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [No-Code, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Διαθέσιμα πολλά μοντέλα |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Τιμές](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Απαιτείται αίτηση πρόσβασης εκ των προτέρων](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Τιμές](https://huggingface.co/pricing) | [Access Tokens](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Το Hugging Chat έχει περιορισμένα μοντέλα](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| | | | | |

Ακολουθήστε τις παρακάτω οδηγίες για να _ρυθμίσετε_ αυτό το αποθετήριο ώστε να χρησιμοποιεί διαφορετικούς παρόχους. Οι ασκήσεις που απαιτούν συγκεκριμένο πάροχο θα έχουν ένα από τα παρακάτω tags στο όνομά τους:

- `aoai` - απαιτεί Azure OpenAI endpoint, key
- `oai` - απαιτεί OpenAI endpoint, key
- `hf` - απαιτεί Hugging Face token

Μπορείτε να ρυθμίσετε έναν, κανέναν ή όλους τους παρόχους. Οι σχετικές ασκήσεις θα εμφανίσουν σφάλμα αν λείπουν τα διαπιστευτήρια.

## Δημιουργία αρχείου `.env`

Υποθέτουμε ότι έχετε ήδη διαβάσει τις παραπάνω οδηγίες, έχετε εγγραφεί στον σχετικό πάροχο και έχετε αποκτήσει τα απαραίτητα διαπιστευτήρια αυθεντικοποίησης (API_KEY ή token). Για το Azure OpenAI, υποθέτουμε επίσης ότι έχετε μια έγκυρη ανάπτυξη της υπηρεσίας Azure OpenAI (endpoint) με τουλάχιστον ένα μοντέλο GPT εγκατεστημένο για chat completion.

Το επόμενο βήμα είναι να ρυθμίσετε τις **τοπικές μεταβλητές περιβάλλοντος** ως εξής:

1. Βρείτε στο root φάκελο το αρχείο `.env.copy` που θα πρέπει να έχει περιεχόμενο όπως το παρακάτω:

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

2. Αντιγράψτε αυτό το αρχείο σε `.env` με την παρακάτω εντολή. Αυτό το αρχείο είναι _gitignore-d_, ώστε να παραμένουν ασφαλή τα μυστικά.

   ```bash
   cp .env.copy .env
   ```

3. Συμπληρώστε τις τιμές (αντικαταστήστε τα placeholders στη δεξιά πλευρά του `=`) όπως περιγράφεται στην επόμενη ενότητα.

4. (Προαιρετικά) Αν χρησιμοποιείτε GitHub Codespaces, μπορείτε να αποθηκεύσετε τις μεταβλητές περιβάλλοντος ως _Codespaces secrets_ που σχετίζονται με αυτό το αποθετήριο. Σε αυτή την περίπτωση, δεν χρειάζεται να ρυθμίσετε τοπικό αρχείο .env. **Προσοχή, αυτή η επιλογή λειτουργεί μόνο αν χρησιμοποιείτε GitHub Codespaces.** Θα χρειαστεί να ρυθμίσετε το αρχείο .env αν χρησιμοποιείτε Docker Desktop.

## Συμπλήρωση αρχείου `.env`

Ας δούμε γρήγορα τα ονόματα των μεταβλητών για να καταλάβουμε τι αντιπροσωπεύουν:

| Μεταβλητή  | Περιγραφή  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Αυτό είναι το access token χρήστη που ρυθμίζετε στο προφίλ σας |
| OPENAI_API_KEY | Αυτό είναι το authorization key για χρήση της υπηρεσίας σε μη-Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Αυτό είναι το authorization key για χρήση της υπηρεσίας |
| AZURE_OPENAI_ENDPOINT | Αυτό είναι το endpoint που έχει αναπτυχθεί για το Azure OpenAI resource |
| AZURE_OPENAI_DEPLOYMENT | Αυτό είναι το endpoint ανάπτυξης μοντέλου _text generation_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Αυτό είναι το endpoint ανάπτυξης μοντέλου _text embeddings_ |
| | |

Σημείωση: Οι δύο τελευταίες μεταβλητές του Azure OpenAI αντιστοιχούν σε προεπιλεγμένο μοντέλο για chat completion (text generation) και αναζήτηση με vectors (embeddings) αντίστοιχα. Οι οδηγίες για τη ρύθμισή τους θα δοθούν στις σχετικές ασκήσεις.

## Ρύθμιση Azure: Από το Portal

Οι τιμές για το Azure OpenAI endpoint και το key θα βρεθούν στο [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), οπότε ας ξεκινήσουμε από εκεί.

1. Μεταβείτε στο [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Κάντε κλικ στην επιλογή **Keys and Endpoint** στο sidebar (μενού αριστερά).
1. Κάντε κλικ στο **Show Keys** - θα δείτε τα εξής: KEY 1, KEY 2 και Endpoint.
1. Χρησιμοποιήστε την τιμή του KEY 1 για το AZURE_OPENAI_API_KEY
1. Χρησιμοποιήστε την τιμή του Endpoint για το AZURE_OPENAI_ENDPOINT

Στη συνέχεια, χρειαζόμαστε τα endpoints για τα συγκεκριμένα μοντέλα που έχουμε αναπτύξει.

1. Κάντε κλικ στην επιλογή **Model deployments** στο sidebar (αριστερό μενού) για το Azure OpenAI resource.
1. Στη σελίδα προορισμού, κάντε κλικ στο **Manage Deployments**

Αυτό θα σας μεταφέρει στην ιστοσελίδα Azure OpenAI Studio, όπου θα βρούμε τις υπόλοιπες τιμές όπως περιγράφεται παρακάτω.

## Ρύθμιση Azure: Από το Studio

1. Μεταβείτε στο [Azure OpenAI Studio](https://oai.azure.com?WT.mc_id=academic-105485-koreyst) **από το resource σας** όπως περιγράφηκε παραπάνω.
1. Κάντε κλικ στην καρτέλα **Deployments** (sidebar, αριστερά) για να δείτε τα μοντέλα που έχουν ήδη αναπτυχθεί.
1. Αν το επιθυμητό μοντέλο δεν έχει αναπτυχθεί, χρησιμοποιήστε το **Create new deployment** για να το αναπτύξετε.
1. Θα χρειαστείτε ένα μοντέλο _text-generation_ - προτείνουμε: **gpt-35-turbo**
1. Θα χρειαστείτε ένα μοντέλο _text-embedding_ - προτείνουμε **text-embedding-ada-002**

Τώρα ενημερώστε τις μεταβλητές περιβάλλοντος ώστε να αντανακλούν το _Deployment name_ που χρησιμοποιήσατε. Συνήθως είναι ίδιο με το όνομα του μοντέλου εκτός αν το αλλάξατε εσείς. Για παράδειγμα, μπορεί να έχετε:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-35-turbo'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Μην ξεχάσετε να αποθηκεύσετε το αρχείο .env όταν τελειώσετε**. Μπορείτε τώρα να κλείσετε το αρχείο και να επιστρέψετε στις οδηγίες για την εκτέλεση του notebook.

## Ρύθμιση OpenAI: Από το Προφίλ

Το OpenAI API key σας βρίσκεται στον [OpenAI λογαριασμό σας](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Αν δεν έχετε, μπορείτε να εγγραφείτε και να δημιουργήσετε ένα API key. Μόλις το αποκτήσετε, μπορείτε να το χρησιμοποιήσετε για να συμπληρώσετε τη μεταβλητή `OPENAI_API_KEY` στο αρχείο `.env`.

## Ρύθμιση Hugging Face: Από το Προφίλ

Το token σας για το Hugging Face βρίσκεται στο προφίλ σας στην ενότητα [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Μην το δημοσιεύετε ή το μοιράζεστε δημόσια. Αντίθετα, δημιουργήστε ένα νέο token για χρήση σε αυτό το project και αντιγράψτε το στο αρχείο `.env` στη μεταβλητή `HUGGING_FACE_API_KEY`. _Σημείωση:_ Τεχνικά δεν είναι API key αλλά χρησιμοποιείται για αυθεντικοποίηση, οπότε κρατάμε αυτή την ονομασία για συνέπεια.

---

**Αποποίηση Ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρότι καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρανοήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.