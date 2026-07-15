# Επιλογή & Διαμόρφωση Παρόχου LLM 🔑

Οι εργασίες **μπορεί** επίσης να ρυθμιστούν να λειτουργούν με μία ή περισσότερες εγκαταστάσεις Μεγάλου Γλωσσικού Μοντέλου (LLM) μέσω υποστηριζόμενου παρόχου υπηρεσιών όπως OpenAI, Azure ή Hugging Face. Αυτοί παρέχουν ένα _φιλοξενούμενο σημείο πρόσβασης_ (API) στο οποίο μπορούμε να έχουμε προγραμματιστική πρόσβαση με τα κατάλληλα διαπιστευτήρια (κλειδί API ή διακριτικό). Σε αυτό το μάθημα, συζητούμε αυτούς τους παρόχους:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) με διάφορα μοντέλα, συμπεριλαμβανομένης της βασικής σειράς GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst) για μοντέλα OpenAI με έμφαση στην ετοιμότητα για επιχειρήσεις
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) για ένα ενιαίο σημείο πρόσβασης και κλειδί API ώστε να αποκτήσετε πρόσβαση σε εκατοντάδες μοντέλα από OpenAI, Meta, Mistral, Cohere, Microsoft και άλλα (αντικαθιστά τα GitHub Models, που αποσύρονται στο τέλος Ιουλίου 2026)
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) για μοντέλα ανοιχτού κώδικα και διακομιστή συμπερασμάτων
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ή [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) αν προτιμάτε να τρέχετε μοντέλα πλήρως оффлайн στη δική σας συσκευή, χωρίς να απαιτείται συνδρομή cloud

**Θα χρειαστείτε τα δικά σας λογαριασμούς για αυτές τις ασκήσεις**. Οι εργασίες είναι προαιρετικές οπότε μπορείτε να επιλέξετε να ρυθμίσετε έναν, όλους - ή κανέναν - από τους παρόχους ανάλογα με τα ενδιαφέροντά σας. Κάποιες οδηγίες για εγγραφή:

| Εγγραφή | Κόστος | Κλειδί API | Playground | Σχόλια |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Τιμολόγηση](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Βάσει έργου](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Χωρίς Κώδικα, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Διαθέσιμα Πολλαπλά Μοντέλα |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Τιμολόγηση](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [Γρήγορη εκκίνηση SDK](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Γρήγορη εκκίνηση Studio](https://learn.microsoft.com/azure/ai-services/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Απαιτείται Αίτηση Πρόσβασης](https://learn.microsoft.com/azure/ai-services/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Τιμολόγηση](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Σελίδα Επισκόπησης Έργου](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Διαθέσιμο δωρεάν επίπεδο; ένα endpoint + κλειδί για πολλούς παρόχους μοντέλων |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Τιμολόγηση](https://huggingface.co/pricing) | [Διακριτικά Πρόσβασης](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Το Hugging Chat έχει περιορισμένα μοντέλα](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Δωρεάν (τρέχει στη συσκευή σας) | Δεν απαιτείται | [Τοπικό CLI/SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Πλήρως off-line, endpoint συμβατό με OpenAI |
| | | | | |

Ακολουθήστε τις οδηγίες παρακάτω για να _διαμορφώσετε_ αυτό το αποθετήριο για χρήση με διαφορετικούς παρόχους. Οι εργασίες που απαιτούν συγκεκριμένο πάροχο θα περιέχουν μία από αυτές τις ετικέτες στο όνομα αρχείου τους:

- `aoai` - απαιτεί Azure OpenAI endpoint, κλειδί
- `oai` - απαιτεί OpenAI endpoint, κλειδί
- `hf` - απαιτεί διακριτικό Hugging Face
- `githubmodels` - απαιτεί Microsoft Foundry Models endpoint, κλειδί (τα GitHub Models αποσύρονται στο τέλος Ιουλίου 2026)

Μπορείτε να διαμορφώσετε έναν, κανέναν ή όλους τους παρόχους. Οι σχετικές εργασίες απλά θα εμφανίζουν σφάλμα αν λείπουν τα διαπιστευτήρια.

## Δημιουργία αρχείου `.env`

Υποθέτουμε ότι έχετε ήδη διαβάσει τις οδηγίες παραπάνω και έχετε εγγραφεί στον αντίστοιχο πάροχο, και έχετε αποκτήσει τα απαιτούμενα διαπιστευτήρια αυθεντικοποίησης (API_KEY ή διακριτικό). Στην περίπτωση του Azure OpenAI, υποθέτουμε ότι έχετε επίσης μία έγκυρη ανάπτυξη υπηρεσίας Azure OpenAI (endpoint) με τουλάχιστον ένα μοντέλο GPT αναπτυγμένο για συμπλήρωση συνομιλίας.

Το επόμενο βήμα είναι να διαμορφώσετε τις **τοπικές μεταβλητές περιβάλλοντος** ως εξής:

1. Κοιτάξτε στον ριζικό φάκελο για το αρχείο `.env.copy` που θα πρέπει να έχει περιεχόμενο όπως το παρακάτω:

   ```bash
   # Πάροχος OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI στο Microsoft Foundry
   ## (Η υπηρεσία Azure OpenAI είναι τώρα μέρος του Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Η προεπιλογή έχει οριστεί! (τρέχουσα σταθερή έκδοση GA API)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-4o-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Μοντέλα Microsoft Foundry (κατάλογος μοντέλων πολλαπλών παρόχων, αντικαθιστά τα μοντέλα GitHub, που καταργούνται στο τέλος Ιουλίου 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Αντιγράψτε αυτό το αρχείο σε `.env` χρησιμοποιώντας την παρακάτω εντολή. Αυτό το αρχείο είναι _στο .gitignore_, διατηρώντας τα μυστικά ασφαλή.

   ```bash
   cp .env.copy .env
   ```

3. Συμπληρώστε τις τιμές (αντικαταστήστε τις θέσεις κράτησης στην δεξιά πλευρά του `=`) όπως περιγράφεται στην επόμενη ενότητα.

4. (Προαιρετικό) Αν χρησιμοποιείτε το GitHub Codespaces, έχετε την επιλογή να αποθηκεύσετε μεταβλητές περιβάλλοντος ως _μυστικά Codespaces_ σχετιζόμενα με αυτό το αποθετήριο. Σε αυτή την περίπτωση, δεν θα χρειαστεί να ρυθμίσετε το τοπικό αρχείο .env. **Ωστόσο, σημειώστε ότι αυτή η επιλογή λειτουργεί μόνο εάν χρησιμοποιείτε GitHub Codespaces.** Θα χρειαστεί ακόμη να ρυθμίσετε το αρχείο .env αν χρησιμοποιείτε Docker Desktop.

## Συμπλήρωση αρχείου `.env`

Ας ρίξουμε μια γρήγορη ματιά στα ονόματα των μεταβλητών για να κατανοήσουμε τι αναπαριστούν:

| Μεταβλητή  | Περιγραφή  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Αυτό είναι το διακριτικό πρόσβασης χρήστη που ρυθμίσατε στο προφίλ σας |
| OPENAI_API_KEY | Αυτό είναι το κλειδί εξουσιοδότησης για χρήση της υπηρεσίας για μη-Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Αυτό είναι το κλειδί εξουσιοδότησης για χρήση αυτής της υπηρεσίας |
| AZURE_OPENAI_ENDPOINT | Αυτό είναι το αναπτυγμένο endpoint για πόρο Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Αυτό είναι το endpoint ανάπτυξης μοντέλου _γενιάς κειμένου_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Αυτό είναι το endpoint ανάπτυξης μοντέλου _ενσωματώσεων κειμένου_ |
| AZURE_INFERENCE_ENDPOINT | Αυτό είναι το endpoint για το έργο Microsoft Foundry σας, που χρησιμοποιείται για Microsoft Foundry Models |
| AZURE_INFERENCE_CREDENTIAL | Αυτό είναι το κλειδί API για το έργο Microsoft Foundry σας |
| | |

Σημείωση: Οι δύο τελευταίες μεταβλητές Azure OpenAI αναφέρονται σε προεπιλεγμένο μοντέλο για συμπλήρωση συνομιλίας (γενιά κειμένου) και αναζήτηση διανυσμάτων (ενσωματώσεις) αντίστοιχα. Οι οδηγίες για τη ρύθμισή τους θα οριστούν στις σχετικές ασκήσεις.

## Διαμόρφωση Azure OpenAI: Από το Πύλη

> **Σημείωση:** Η υπηρεσία Azure OpenAI πλέον αποτελεί μέρος του [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Οι πόροι και οι εγκαταστάσεις εξακολουθούν να εμφανίζονται στο Azure Portal, αλλά η καθημερινή διαχείριση μοντέλων (εγκαταστάσεις, playground, παρακολούθηση) γίνεται πλέον στο Foundry portal αντί του παλιού αυτόνομου "Azure OpenAI Studio".

Οι τιμές για το Azure OpenAI endpoint και κλειδί θα βρεθούν στο [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), οπότε ας ξεκινήσουμε από εκεί.

1. Μεταβείτε στο [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Κάντε κλικ στην επιλογή **Κλειδιά και Endpoint** στην πλευρική μπάρα (μενού αριστερά).
1. Κάντε κλικ στο **Εμφάνιση Κλειδιών** - θα δείτε τα ακόλουθα: ΚΛΕΙΔΙ 1, ΚΛΕΙΔΙ 2 και Endpoint.
1. Χρησιμοποιήστε την τιμή ΚΛΕΙΔΙ 1 για το AZURE_OPENAI_API_KEY
1. Χρησιμοποιήστε την τιμή Endpoint για το AZURE_OPENAI_ENDPOINT

Στη συνέχεια, χρειαζόμαστε τα endpoints για τα συγκεκριμένα μοντέλα που έχουμε αναπτύξει.

1. Κάντε κλικ στην επιλογή **Αναπτύξεις μοντέλων** στην πλευρική μπάρα (αριστερό μενού) για τον πόρο Azure OpenAI.
1. Στη σελίδα προορισμού, κάντε κλικ στο **Μετάβαση στην πύλη Microsoft Foundry** (ή **Διαχείριση Αναπτύξεων**, ανάλογα με τον τύπο του πόρου σας)

Αυτό θα σας μεταφέρει στην πύλη Microsoft Foundry, όπου θα βρούμε τις υπόλοιπες τιμές όπως περιγράφεται παρακάτω.

## Διαμόρφωση Azure OpenAI: Από την πύλη Microsoft Foundry

1. Πλοηγηθείτε στην [πύλη Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **από τον πόρο σας** όπως περιγράφηκε παραπάνω.
1. Κάντε κλικ στην καρτέλα **Αναπτύξεις** (πλευρική μπάρα, αριστερά) για να δείτε τα τρέχοντα αναπτυγμένα μοντέλα.
1. Αν το επιθυμητό μοντέλο σας δεν είναι αναπτυγμένο, χρησιμοποιήστε το **Ανάπτυξη μοντέλου** για να το αναπτύξετε από τον [κατάλογο μοντέλων](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Θα χρειαστείτε μοντέλο _γενιάς κειμένου_ - προτείνουμε: **gpt-4o-mini**
1. Θα χρειαστείτε μοντέλο _ενσωματώσεων κειμένου_ - προτείνουμε **text-embedding-3-small**

Τώρα ενημερώστε τις μεταβλητές περιβάλλοντος να αντικατοπτρίζουν το _Όνομα Ανάπτυξης_ που χρησιμοποιήθηκε. Αυτό συνήθως θα είναι το ίδιο με το όνομα του μοντέλου εκτός αν το αλλάξατε ρητά. Για παράδειγμα, μπορεί να έχετε:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-4o-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Μην ξεχάσετε να αποθηκεύσετε το αρχείο .env όταν τελειώσετε**. Μπορείτε τώρα να κλείσετε το αρχείο και να επιστρέψετε στις οδηγίες για την εκτέλεση του σημειωματάριου.

## Διαμόρφωση OpenAI: Από το Προφίλ

Το κλειδί API για OpenAI μπορεί να βρεθεί στον [λογαριασμό OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) σας. Αν δεν έχετε, μπορείτε να εγγραφείτε σε λογαριασμό και να δημιουργήσετε ένα κλειδί API. Αφού έχετε το κλειδί, μπορείτε να το χρησιμοποιήσετε για να συμπληρώσετε τη μεταβλητή `OPENAI_API_KEY` στο αρχείο `.env`.

## Διαμόρφωση Hugging Face: Από το Προφίλ

Το διακριτικό Hugging Face σας βρίσκεται στο προφίλ σας στην ενότητα [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Μην δημοσιεύετε ή μοιράζεστε αυτά δημόσια. Αντίθετα, δημιουργήστε νέο διακριτικό για τη χρήση αυτού του έργου και αντιγράψτε το στο αρχείο `.env` κάτω από τη μεταβλητή `HUGGING_FACE_API_KEY`. _Σημείωση:_ Τεχνικά δεν είναι κλειδί API, αλλά χρησιμοποιείται για αυθεντικοποίηση, οπότε διατηρούμε αυτή την ονομασία για συνέπεια.

## Διαμόρφωση Microsoft Foundry Models: Από Πύλη

> **Σημείωση:** Τα GitHub Models αποσύρονται στο τέλος Ιουλίου 2026. Τα Microsoft Foundry Models είναι η άμεση αντικατάσταση, προσφέροντας τον ίδιο ελεύθερο προς δοκιμή κατάλογο μοντέλων και την εμπειρία SDK Azure AI Inference / OpenAI SDK.

1. Μεταβείτε στο [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) και δημιουργήστε (ή ανοίξτε) ένα έργο Foundry.
1. Περιηγηθείτε στον [κατάλογο μοντέλων](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) και αναπτύξτε ένα μοντέλο, για παράδειγμα `gpt-4o-mini`.
1. Στη σελίδα **Επισκόπησης** του έργου, αντιγράψτε το **endpoint** και το **κλειδί API**.
1. Χρησιμοποιήστε την τιμή endpoint για το `AZURE_INFERENCE_ENDPOINT` και το κλειδί για το `AZURE_INFERENCE_CREDENTIAL` στο αρχείο `.env`.

## Παρόχοι Offline / Τοπικοί

Αν προτιμάτε να μην χρησιμοποιείτε καθόλου συνδρομή cloud, μπορείτε να τρέξετε συμβατά ανοιχτά μοντέλα απευθείας στη δική σας συσκευή:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - το runtime τοπικά της Microsoft. Επιλέγει αυτόματα τον καλύτερο πάροχο εκτέλεσης (NPU, GPU ή CPU) και παρέχει endpoint συμβατό με OpenAI, ώστε να μπορείτε να επαναχρησιμοποιείτε τον περισσότερo κώδικα δειγμάτων σε αυτό το μάθημα με ελάχιστες αλλαγές. Δείτε την [τεκμηρίωση Foundry Local](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) για να ξεκινήσετε ή εγκαταστήστε με `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - μια δημοφιλής εναλλακτική για τρέξιμο ανοιχτών μοντέλων όπως Llama, Phi, Mistral και Gemma τοπικά.


Δείτε το [Μάθημα 19: Κατασκευή με SLM](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) για πρακτικά παραδείγματα που χρησιμοποιούν και τις δύο επιλογές.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->