# Επιλογή & Διαμόρφωση Παρόχου LLM 🔑

Οι εργασίες **μπορεί** επίσης να ρυθμιστούν να λειτουργούν με μία ή περισσότερες αναπτύξεις Μεγάλων Γλωσσικών Μοντέλων (LLM) μέσω ενός υποστηριζόμενου παρόχου υπηρεσιών όπως OpenAI, Azure ή Hugging Face. Αυτοί παρέχουν ένα _φιλοξενούμενο endpoint_ (API) στο οποίο μπορούμε να έχουμε προγραμματισμένη πρόσβαση με τα σωστά διαπιστευτήρια (API key ή token). Σε αυτό το μάθημα, συζητάμε αυτούς τους παρόχους:

 - [OpenAI](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst) με ποικίλα μοντέλα, συμπεριλαμβανομένης της βασικής σειράς GPT.
 - [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst) για μοντέλα OpenAI με έμφαση στην επιχειρησιακή ετοιμότητα.
 - [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) για ένα ενιαίο endpoint και κλειδί API για πρόσβαση σε εκατοντάδες μοντέλα από OpenAI, Meta, Mistral, Cohere, Microsoft και άλλα (αντικαθιστά τα GitHub Models, που αποσύρονται στο τέλος Ιουλίου 2026).
 - [Hugging Face](https://huggingface.co/docs/hub/index?WT.mc_id=academic-105485-koreyst) για ανοιχτού κώδικα μοντέλα και inference server.
 - [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ή [Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) αν προτιμάτε να τρέχετε μοντέλα πλήρως εκτός σύνδεσης στη δική σας συσκευή, χωρίς να απαιτείται συνδρομή στο cloud.

**Θα χρειαστεί να χρησιμοποιήσετε τους δικούς σας λογαριασμούς για αυτές τις ασκήσεις**. Οι εργασίες είναι προαιρετικές, οπότε μπορείτε να επιλέξετε να ρυθμίσετε έναν, όλους ή κανέναν από τους παρόχους ανάλογα με τα ενδιαφέροντά σας. Κάποιες οδηγίες για εγγραφή:

| Εγγραφή | Κόστος | Κλειδί API | Playground | Σχόλια |
|:---|:---|:---|:---|:---|
| [OpenAI](https://platform.openai.com/signup?WT.mc_id=academic-105485-koreyst)| [Τιμολόγηση](https://openai.com/pricing#language-models?WT.mc_id=academic-105485-koreyst)| [Βάσει έργου](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst) | [Χωρίς Κώδικα, Web](https://platform.openai.com/playground?WT.mc_id=academic-105485-koreyst) | Διαθέσιμα Πολλά Μοντέλα |
| [Azure](https://aka.ms/azure/free?WT.mc_id=academic-105485-koreyst)| [Τιμολόγηση](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/?WT.mc_id=academic-105485-koreyst)| [SDK Quickstart](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst)| [Studio Quickstart](https://learn.microsoft.com/azure/ai-foundry/openai/quickstart?WT.mc_id=academic-105485-koreyst) |  [Απαιτείται Πρότερη Αίτηση Πρόσβασης](https://learn.microsoft.com/azure/ai-foundry/openai/?WT.mc_id=academic-105485-koreyst)|
| [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) | [Τιμολόγηση](https://azure.microsoft.com/pricing/details/ai-foundry/?WT.mc_id=academic-105485-koreyst) | [Σελίδα Επισκόπησης Έργου](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) | [Foundry Playground](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) | Διαθέσιμη δωρεάν βαθμίδα; ένα endpoint + κλειδί για πολλούς παρόχους μοντέλων |
| [Hugging Face](https://huggingface.co/join?WT.mc_id=academic-105485-koreyst) | [Τιμολόγηση](https://huggingface.co/pricing) | [Tokens Πρόσβασης](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=academic-105485-koreyst) | [Hugging Chat](https://huggingface.co/chat/?WT.mc_id=academic-105485-koreyst)| [Το Hugging Chat έχει περιορισμένα μοντέλα](https://huggingface.co/chat/models?WT.mc_id=academic-105485-koreyst) |
| [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) | Δωρεάν (τρέχει στη συσκευή σας) | Δεν απαιτείται | [Τοπικό CLI/SDK](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) | Πλήρως εκτός σύνδεσης, OpenAI-συμβατό endpoint |
| | | | | |

Ακολουθήστε τις παρακάτω οδηγίες για να _διαμορφώσετε_ αυτό το αποθετήριο για χρήση με διαφορετικούς παρόχους. Οι εργασίες που απαιτούν συγκεκριμένο πάροχο θα έχουν ένα από αυτά τα tags στο όνομα αρχείου:

- `aoai` - απαιτεί endpoint Azure OpenAI, κλειδί
- `oai` - απαιτεί endpoint OpenAI, κλειδί
- `hf` - απαιτεί token Hugging Face
- `githubmodels` - απαιτεί endpoint Microsoft Foundry Models, κλειδί (τα GitHub Models αποσύρονται στο τέλος Ιουλίου 2026)

Μπορείτε να ρυθμίσετε έναν, κανέναν ή όλους τους παρόχους. Οι σχετικές εργασίες απλά θα εμφανίζουν σφάλμα αν λείπουν τα διαπιστευτήρια.

## Δημιουργία αρχείου `.env`

Υποθέτουμε ότι έχετε ήδη διαβάσει τις παραπάνω οδηγίες, έχετε εγγραφεί στον αντίστοιχο πάροχο και έχετε αποκτήσει τα απαιτούμενα διαπιστευτήρια πιστοποίησης (API_KEY ή token). Στην περίπτωση του Azure OpenAI, υποθέτουμε επίσης ότι έχετε μια έγκυρη ανάπτυξη Azure OpenAI Service (endpoint) με τουλάχιστον ένα μοντέλο GPT αναπτυγμένο για ολοκλήρωση συνομιλίας.

Το επόμενο βήμα είναι να διαμορφώσετε τις **τοπικές μεταβλητές περιβάλλοντος** ως εξής:

1. Βρείτε στον ριζικό φάκελο το αρχείο `.env.copy` που θα πρέπει να έχει περιεχόμενο όπως το παρακάτω:

   ```bash
   # Παροχέας OpenAI
   OPENAI_API_KEY='<add your OpenAI API key here>'

   ## Azure OpenAI στο Microsoft Foundry
   ## (Η Υπηρεσία Azure OpenAI είναι τώρα μέρος του Microsoft Foundry: https://ai.azure.com)
   AZURE_OPENAI_API_VERSION='2024-10-21' # Η προεπιλογή έχει οριστεί! (τρέχουσα σταθερή έκδοση GA API)
   AZURE_OPENAI_API_KEY='<add your Foundry resource key here>'
   AZURE_OPENAI_ENDPOINT='<add your Foundry resource endpoint here, e.g. https://<resource-name>.openai.azure.com>'
   AZURE_OPENAI_DEPLOYMENT='<add your chat completion model deployment name here, e.g. gpt-5-mini>'
   AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='<add your embeddings model deployment name here, e.g. text-embedding-3-small>'

   ## Μοντέλα Microsoft Foundry (κατάλογος μοντέλων πολλαπλών παρόχων, αντικαθιστά τα Μοντέλα GitHub, που αποσύρονται το τέλος Ιουλίου 2026)
   AZURE_INFERENCE_ENDPOINT='<add your Microsoft Foundry project endpoint here>'
   AZURE_INFERENCE_CREDENTIAL='<add your Microsoft Foundry Models API key here>'

   ## Hugging Face
   HUGGING_FACE_API_KEY='<add your HuggingFace API or token here>'
   ```

2. Αντιγράψτε το αρχείο σε `.env` χρησιμοποιώντας την παρακάτω εντολή. Αυτό το αρχείο είναι στο _gitignore_, διατηρώντας τα μυστικά ασφαλή.

   ```bash
   cp .env.copy .env
   ```

3. Συμπληρώστε τις τιμές (αντικαταστήστε τις θέσεις κρατήματος δεξιά του `=`) όπως περιγράφεται στην επόμενη ενότητα.

4. (Προαιρετικό) Αν χρησιμοποιείτε GitHub Codespaces, έχετε την επιλογή να αποθηκεύσετε μεταβλητές περιβάλλοντος ως _μυστικά Codespaces_ συνδεδεμένα με αυτό το αποθετήριο. Σε αυτή την περίπτωση, δεν θα χρειαστεί να στήσετε τοπικό αρχείο .env. **Ωστόσο, σημειώστε ότι αυτή η επιλογή λειτουργεί μόνο αν χρησιμοποιείτε GitHub Codespaces.** Θα χρειαστεί να στήσετε το αρχείο .env αν χρησιμοποιείτε Docker Desktop.

## Συμπλήρωση αρχείου `.env`

Ας ρίξουμε μια γρήγορη ματιά στα ονόματα των μεταβλητών για να κατανοήσουμε τι αντιπροσωπεύουν:

| Μεταβλητή  | Περιγραφή  |
| :--- | :--- |
| HUGGING_FACE_API_KEY | Αυτό είναι το token πρόσβασης χρήστη που ρυθμίσατε στο προφίλ σας |
| OPENAI_API_KEY | Αυτό είναι το κλειδί εξουσιοδότησης για χρήση της υπηρεσίας σε μη Azure OpenAI endpoints |
| AZURE_OPENAI_API_KEY | Αυτό είναι το κλειδί εξουσιοδότησης για χρήση αυτής της υπηρεσίας |
| AZURE_OPENAI_ENDPOINT | Πρόκειται για το αναπτυγμένο endpoint ενός πόρου Azure OpenAI |
| AZURE_OPENAI_DEPLOYMENT | Endpoint ανάπτυξης μοντέλου _γεννήτριας κειμένου_ |
| AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT | Endpoint ανάπτυξης μοντέλου _ενσωμάτωσης κειμένου_ |
| AZURE_INFERENCE_ENDPOINT | Endpoint για το έργο Microsoft Foundry, χρησιμοποιείται για τα μοντέλα Microsoft Foundry |
| AZURE_INFERENCE_CREDENTIAL | Το κλειδί API για το έργο Microsoft Foundry |
| | |

Σημείωση: Οι δύο τελευταίες μεταβλητές του Azure OpenAI αναφέρονται σε προεπιλεγμένο μοντέλο για ολοκλήρωση συνομιλίας (γεννήτρια κειμένου) και αναζήτηση μέσω διανυσμάτων (ενσωμάτωσης) αντίστοιχα. Οι οδηγίες για τη ρύθμισή τους θα καθοριστούν σε σχετικές εργασίες.

## Διαμόρφωση Azure OpenAI: Από Portal

> **Σημείωση:** Η υπηρεσία Azure OpenAI αποτελεί τώρα μέρος του [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst). Οι πόροι και οι αναπτύξεις εξακολουθούν να εμφανίζονται στο Azure Portal, αλλά η καθημερινή διαχείριση μοντέλων (αναπτύξεις, playground, παρακολούθηση) γίνεται πλέον μέσω του Foundry portal αντί για το παλιό αυτόνομο "Azure OpenAI Studio".

Οι τιμές του endpoint και του κλειδιού του Azure OpenAI βρίσκονται στο [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), οπότε ας ξεκινήσουμε από εκεί.

1. Μεταβείτε στο [Azure Portal](https://portal.azure.com?WT.mc_id=academic-105485-koreyst)
1. Κάντε κλικ στην επιλογή **Keys and Endpoint** στο πλαϊνό μενού (μενού αριστερά).
1. Κάντε κλικ στο **Show Keys** - θα δείτε τα εξής: KEY 1, KEY 2 και Endpoint.
1. Χρησιμοποιήστε την τιμή KEY 1 για το AZURE_OPENAI_API_KEY
1. Χρησιμοποιήστε την τιμή Endpoint για το AZURE_OPENAI_ENDPOINT

Στη συνέχεια, χρειαζόμαστε τα endpoints για τα συγκεκριμένα μοντέλα που έχουμε αναπτύξει.

1. Κάντε κλικ στην επιλογή **Model deployments** στο πλαϊνό μενού (αριστερό μενού) για τον πόρο Azure OpenAI.
1. Στη σελίδα προορισμού, κάντε κλικ στο **Go to Microsoft Foundry portal** (ή **Manage Deployments**, ανάλογα με τον τύπο πόρου σας)

Αυτό θα σας μεταφέρει στο Microsoft Foundry portal, όπου θα βρούμε τις υπόλοιπες τιμές όπως περιγράφεται παρακάτω.

## Διαμόρφωση Azure OpenAI: Από το Microsoft Foundry portal

1. Μεταβείτε στο [Microsoft Foundry portal](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) **από τον πόρο σας** όπως περιγράφηκε παραπάνω.
1. Κάντε κλικ στην καρτέλα **Deployments** (πλαϊνό μενού, αριστερά) για να δείτε τα μοντέλα που έχουν αναπτυχθεί.
1. Αν το επιθυμητό μοντέλο δεν είναι αναπτυγμένο, χρησιμοποιήστε το **Deploy model** για να το αναπτύξετε από τον [κατάλογο μοντέλων](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).
1. Θα χρειαστείτε ένα μοντέλο _γεννήτριας κειμένου_ - προτείνουμε: **gpt-5-mini**
1. Θα χρειαστείτε ένα μοντέλο _ενσωμάτωσης κειμένου_ - προτείνουμε **text-embedding-3-small**

Τώρα ενημερώστε τις μεταβλητές περιβάλλοντος ώστε να αντανακλούν το όνομα _Deployment_ που χρησιμοποιήθηκε. Αυτό συνήθως είναι ίδιο με το όνομα του μοντέλου εκτός αν το άλλαξατε ρητά. Για παράδειγμα, μπορεί να έχετε:

```bash
AZURE_OPENAI_DEPLOYMENT='gpt-5-mini'
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-3-small'
```

**Μην ξεχάσετε να αποθηκεύσετε το αρχείο .env όταν τελειώσετε**. Μπορείτε πλέον να κλείσετε το αρχείο και να επιστρέψετε στις οδηγίες για την εκτέλεση του notebook.

## Διαμόρφωση OpenAI: Από το Προφίλ

Το κλειδί API του OpenAI μπορείτε να το βρείτε στον [λογαριασμό σας OpenAI](https://platform.openai.com/api-keys?WT.mc_id=academic-105485-koreyst). Αν δεν έχετε, μπορείτε να εγγραφείτε και να δημιουργήσετε ένα κλειδί API. Μόλις το έχετε, το χρησιμοποιείτε για να συμπληρώσετε τη μεταβλητή `OPENAI_API_KEY` στο αρχείο `.env`.

## Διαμόρφωση Hugging Face: Από το Προφίλ

Το token Hugging Face το βρίσκετε στο προφίλ σας στην ενότητα [Access Tokens](https://huggingface.co/settings/tokens?WT.mc_id=academic-105485-koreyst). Μην το δημοσιοποιείτε ή μοιράζεστε δημόσια. Αντίθετα, δημιουργήστε ένα νέο token για τη χρήση αυτού του έργου και αντιγράψτε το στο αρχείο `.env` κάτω από τη μεταβλητή `HUGGING_FACE_API_KEY`. _Σημείωση:_ Τεχνικά δεν είναι κλειδί API, αλλά χρησιμοποιείται για αυθεντικοποίηση, οπότε κρατάμε αυτή τη ονομασία για συνέπεια.

## Διαμόρφωση Microsoft Foundry Models: Από Portal

> **Σημείωση:** Τα GitHub Models αποσύρονται στο τέλος Ιουλίου 2026. Τα Microsoft Foundry Models αποτελούν την άμεση αντικατάσταση και προσφέρουν τον ίδιο δωρεάν δοκιμαστικό κατάλογο μοντέλων και την εμπειρία Azure AI Inference SDK / OpenAI SDK.

1. Πηγαίνετε στο [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) και δημιουργήστε (ή ανοίξτε) ένα έργο Foundry.
1. Περιηγηθείτε στον [κατάλογο μοντέλων](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) και αναπτύξτε ένα μοντέλο, για παράδειγμα `gpt-5-mini`.
1. Στη σελίδα **Επισκόπησης** του έργου, αντιγράψτε το **endpoint** και το **κλειδί API**.
1. Χρησιμοποιήστε την τιμή endpoint για `AZURE_INFERENCE_ENDPOINT` και την τιμή κλειδιού για `AZURE_INFERENCE_CREDENTIAL` στο αρχείο σας `.env`.

## Εκτός σύνδεσης / Τοπικοί Πάροχοι

Αν προτιμάτε να μην χρησιμοποιήσετε καθόλου συνδρομή cloud, μπορείτε να τρέξετε συμβατά ανοιχτά μοντέλα απευθείας στη δική σας συσκευή:

- **[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst)** - το runtime της Microsoft στη συσκευή σας. Επιλέγει αυτόματα τον καλύτερο πάροχο εκτέλεσης (NPU, GPU ή CPU) και παρέχει ένα OpenAI-συμβατό endpoint, ώστε να μπορείτε να ξαναχρησιμοποιήσετε τον περισσότερο κώδικα δειγμάτων αυτής της εκπαιδευτικής ενότητας με ελάχιστες αλλαγές. Δείτε την [τεκμηρίωση Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) για να ξεκινήσετε, ή εγκαταστήστε με `winget install Microsoft.FoundryLocal` (Windows) / `brew install microsoft/foundrylocal/foundrylocal` (macOS).
- **[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst)** - μια δημοφιλής εναλλακτική για τοπική εκτέλεση ανοιχτών μοντέλων όπως Llama, Phi, Mistral και Gemma.


Δείτε [Μάθημα 19: Δημιουργία με SLMs](../19-slm/README.md?WT.mc_id=academic-105485-koreyst) για πρακτικά παραδείγματα που χρησιμοποιούν και τις δύο επιλογές.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->