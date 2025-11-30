<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "578a2d20d79cbe5a33eac32d4eabb9b0",
  "translation_date": "2025-10-17T18:20:14+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "el"
}
-->
# Ξεκινώντας με αυτό το μάθημα

Είμαστε πολύ ενθουσιασμένοι που ξεκινάτε αυτό το μάθημα και ανυπομονούμε να δούμε τι θα εμπνευστείτε να δημιουργήσετε με τη Γενετική Τεχνητή Νοημοσύνη!

Για να εξασφαλίσουμε την επιτυχία σας, αυτή η σελίδα περιγράφει τα βήματα εγκατάστασης, τις τεχνικές απαιτήσεις και πού να βρείτε βοήθεια αν χρειαστεί.

## Βήματα Εγκατάστασης

Για να ξεκινήσετε αυτό το μάθημα, θα χρειαστεί να ολοκληρώσετε τα παρακάτω βήματα.

### 1. Κλωνοποίηση αυτού του Αποθετηρίου

[Κλωνοποιήστε ολόκληρο το αποθετήριο](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) στον δικό σας λογαριασμό GitHub για να μπορείτε να αλλάξετε οποιονδήποτε κώδικα και να ολοκληρώσετε τις προκλήσεις. Μπορείτε επίσης να [προσθέσετε αστέρι (🌟) σε αυτό το αποθετήριο](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) για να το βρίσκετε πιο εύκολα, καθώς και σχετικά αποθετήρια.

### 2. Δημιουργία ενός Codespace

Για να αποφύγετε προβλήματα εξαρτήσεων κατά την εκτέλεση του κώδικα, συνιστούμε να εκτελέσετε αυτό το μάθημα σε ένα [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Στο κλωνοποιημένο αποθετήριο σας: **Code -> Codespaces -> New on main**

![Διάλογος που δείχνει κουμπιά για τη δημιουργία ενός codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Προσθήκη ενός μυστικού

1. ⚙️ Εικονίδιο γραναζιού -> Command Pallete -> Codespaces : Manage user secret -> Add a new secret.
2. Όνομα OPENAI_API_KEY, επικολλήστε το κλειδί σας, Αποθήκευση.

### 3. Τι ακολουθεί;

| Θέλω να…            | Πήγαινε στο…                                                             |
|---------------------|-------------------------------------------------------------------------|
| Ξεκινήστε το Μάθημα 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Εργαστείτε εκτός σύνδεσης | [`setup-local.md`](02-setup-local.md)                                   |
| Ρυθμίστε έναν Πάροχο LLM | [`providers.md`](03-providers.md)                                        |
| Γνωρίστε άλλους μαθητές | [Γίνετε μέλος στο Discord μας](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Επίλυση Προβλημάτων

| Σύμπτωμα                                   | Λύση                                                             |
|-------------------------------------------|-----------------------------------------------------------------|
| Η κατασκευή του container κολλάει > 10 λεπτά | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Το τερματικό δεν συνδέθηκε· κάντε κλικ **+** ➜ *bash*            |
| `401 Unauthorized` από OpenAI             | Λάθος / ληγμένο `OPENAI_API_KEY`                                |
| Το VS Code δείχνει “Dev container mounting…” | Ανανεώστε την καρτέλα του προγράμματος περιήγησης—μερικές φορές το Codespaces χάνει τη σύνδεση |
| Λείπει ο πυρήνας του Notebook             | Μενού Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Συστήματα βασισμένα σε Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Επεξεργαστείτε το αρχείο `.env`**: Ανοίξτε το αρχείο `.env` σε έναν επεξεργαστή κειμένου (π.χ., VS Code, Notepad++ ή οποιονδήποτε άλλο επεξεργαστή). Προσθέστε την παρακάτω γραμμή στο αρχείο, αντικαθιστώντας το `your_github_token_here` με το πραγματικό σας GitHub token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Αποθηκεύστε το Αρχείο**: Αποθηκεύστε τις αλλαγές και κλείστε τον επεξεργαστή κειμένου.

5. **Εγκαταστήστε το `python-dotenv`**: Αν δεν το έχετε ήδη, θα χρειαστεί να εγκαταστήσετε το πακέτο `python-dotenv` για να φορτώσετε μεταβλητές περιβάλλοντος από το αρχείο `.env` στην εφαρμογή Python σας. Μπορείτε να το εγκαταστήσετε χρησιμοποιώντας `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Φορτώστε Μεταβλητές Περιβάλλοντος στο Python Script σας**: Στο Python script σας, χρησιμοποιήστε το πακέτο `python-dotenv` για να φορτώσετε τις μεταβλητές περιβάλλοντος από το αρχείο `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Αυτό είναι! Έχετε δημιουργήσει επιτυχώς ένα αρχείο `.env`, προσθέσατε το GitHub token σας και το φορτώσατε στην εφαρμογή Python σας.

## Πώς να Εκτελέσετε τοπικά στον υπολογιστή σας

Για να εκτελέσετε τον κώδικα τοπικά στον υπολογιστή σας, θα χρειαστεί να έχετε κάποια έκδοση του [Python εγκατεστημένη](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Στη συνέχεια, για να χρησιμοποιήσετε το αποθετήριο, πρέπει να το κλωνοποιήσετε:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Μόλις έχετε όλα τα αρχεία, μπορείτε να ξεκινήσετε!

## Προαιρετικά Βήματα

### Εγκατάσταση Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) είναι ένας ελαφρύς εγκαταστάτης για την εγκατάσταση του [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), του Python, καθώς και μερικών πακέτων.
Το Conda είναι ένας διαχειριστής πακέτων που διευκολύνει τη ρύθμιση και την εναλλαγή μεταξύ διαφορετικών [**εικονικών περιβαλλόντων**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python και πακέτων. Είναι επίσης χρήσιμο για την εγκατάσταση πακέτων που δεν είναι διαθέσιμα μέσω `pip`.

Μπορείτε να ακολουθήσετε τον [οδηγό εγκατάστασης MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) για να το ρυθμίσετε.

Με το Miniconda εγκατεστημένο, πρέπει να κλωνοποιήσετε το [αποθετήριο](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (αν δεν το έχετε ήδη κάνει).

Στη συνέχεια, πρέπει να δημιουργήσετε ένα εικονικό περιβάλλον. Για να το κάνετε αυτό με το Conda, δημιουργήστε ένα νέο αρχείο περιβάλλοντος (_environment.yml_). Αν ακολουθείτε μέσω Codespaces, δημιουργήστε το μέσα στον φάκελο `.devcontainer`, δηλαδή `.devcontainer/environment.yml`.

Προσθέστε το παρακάτω απόσπασμα στο αρχείο περιβάλλοντος σας:

```yml
name: <environment-name>
channels:
  - defaults
  - microsoft
dependencies:
  - python=<python-version>
  - openai
  - python-dotenv
  - pip
  - pip:
      - azure-ai-ml
```

Αν αντιμετωπίσετε σφάλματα χρησιμοποιώντας το conda, μπορείτε να εγκαταστήσετε χειροκίνητα τις Βιβλιοθήκες AI της Microsoft χρησιμοποιώντας την παρακάτω εντολή σε ένα τερματικό.

```
conda install -c microsoft azure-ai-ml
```

Το αρχείο περιβάλλοντος καθορίζει τις εξαρτήσεις που χρειαζόμαστε. Το `<environment-name>` αναφέρεται στο όνομα που θέλετε να χρησιμοποιήσετε για το περιβάλλον Conda σας, και το `<python-version>` είναι η έκδοση του Python που θέλετε να χρησιμοποιήσετε, για παράδειγμα, `3` είναι η τελευταία κύρια έκδοση του Python.

Με αυτό ολοκληρωμένο, μπορείτε να δημιουργήσετε το περιβάλλον Conda σας εκτελώντας τις παρακάτω εντολές στη γραμμή εντολών/τερματικό σας:

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Ανατρέξτε στον [οδηγό περιβαλλόντων Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) αν αντιμετωπίσετε προβλήματα.

### Χρήση του Visual Studio Code με την επέκταση υποστήριξης Python

Συνιστούμε τη χρήση του [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) με την [επέκταση υποστήριξης Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) εγκατεστημένη για αυτό το μάθημα. Ωστόσο, αυτό είναι περισσότερο μια σύσταση και όχι απαραίτητη προϋπόθεση.

> **Σημείωση**: Ανοίγοντας το αποθετήριο του μαθήματος στο VS Code, έχετε την επιλογή να ρυθμίσετε το έργο μέσα σε ένα container. Αυτό οφείλεται στον [ειδικό φάκελο `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) που βρίσκεται μέσα στο αποθετήριο του μαθήματος. Περισσότερα για αυτό αργότερα.

> **Σημείωση**: Μόλις κλωνοποιήσετε και ανοίξετε τον φάκελο στο VS Code, θα σας προτείνει να εγκαταστήσετε μια επέκταση υποστήριξης Python.

> **Σημείωση**: Αν το VS Code σας προτείνει να ανοίξετε ξανά το αποθετήριο σε ένα container, απορρίψτε αυτή την πρόταση για να χρησιμοποιήσετε την τοπικά εγκατεστημένη έκδοση του Python.

### Χρήση του Jupyter στο Πρόγραμμα Περιήγησης

Μπορείτε επίσης να εργαστείτε στο έργο χρησιμοποιώντας το [περιβάλλον Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) απευθείας μέσα από το πρόγραμμα περιήγησής σας. Τόσο το κλασικό Jupyter όσο και το [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) παρέχουν ένα ευχάριστο περιβάλλον ανάπτυξης με χαρακτηριστικά όπως αυτόματη συμπλήρωση, επισήμανση κώδικα, κ.λπ.

Για να ξεκινήσετε το Jupyter τοπικά, ανοίξτε το τερματικό/γραμμή εντολών, μεταβείτε στον φάκελο του μαθήματος και εκτελέστε:

```bash
jupyter notebook
```

ή

```bash
jupyterhub
```

Αυτό θα ξεκινήσει μια παρουσία του Jupyter και η διεύθυνση URL για πρόσβαση θα εμφανιστεί στο παράθυρο της γραμμής εντολών.

Μόλις αποκτήσετε πρόσβαση στη διεύθυνση URL, θα πρέπει να δείτε τη δομή του μαθήματος και να μπορείτε να πλοηγηθείτε σε οποιοδήποτε αρχείο `*.ipynb`. Για παράδειγμα, `08-building-search-applications/python/oai-solution.ipynb`.

### Εκτέλεση σε container

Μια εναλλακτική λύση για τη ρύθμιση όλων στον υπολογιστή σας ή στο Codespace είναι η χρήση ενός [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Ο ειδικός φάκελος `.devcontainer` μέσα στο αποθετήριο του μαθήματος καθιστά δυνατή τη ρύθμιση του έργου μέσα σε ένα container μέσω του VS Code. Εκτός από το Codespaces, αυτό θα απαιτήσει την εγκατάσταση του Docker, και ειλικρινά, περιλαμβάνει αρκετή δουλειά, οπότε το συνιστούμε μόνο σε όσους έχουν εμπειρία με containers.

Ένας από τους καλύτερους τρόπους για να διατηρήσετε ασφαλή τα API keys σας όταν χρησιμοποιείτε το GitHub Codespaces είναι μέσω της χρήσης των Secrets του Codespace. Ακολουθήστε τον [οδηγό διαχείρισης μυστικών του Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) για να μάθετε περισσότερα.

## Μαθήματα και Τεχνικές Απαιτήσεις

Το μάθημα περιλαμβάνει 6 μαθήματα εννοιών και 6 μαθήματα κώδικα.

Για τα μαθήματα κώδικα, χρησιμοποιούμε την Υπηρεσία Azure OpenAI. Θα χρειαστείτε πρόσβαση στην υπηρεσία Azure OpenAI και ένα API key για να εκτελέσετε αυτόν τον κώδικα. Μπορείτε να κάνετε αίτηση για πρόσβαση [συμπληρώνοντας αυτή την αίτηση](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Ενώ περιμένετε να επεξεργαστεί η αίτησή σας, κάθε μάθημα κώδικα περιλαμβάνει επίσης ένα αρχείο `README.md` όπου μπορείτε να δείτε τον κώδικα και τα αποτελέσματα.

## Χρήση της Υπηρεσίας Azure OpenAI για πρώτη φορά

Αν είναι η πρώτη σας φορά που εργάζεστε με την υπηρεσία Azure OpenAI, παρακαλούμε ακολουθήστε αυτόν τον οδηγό για το πώς να [δημιουργήσετε και να αναπτύξετε έναν πόρο της Υπηρεσίας Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Χρήση του OpenAI API για πρώτη φορά

Αν είναι η πρώτη σας φορά που εργάζεστε με το OpenAI API, παρακαλούμε ακολουθήστε τον οδηγό για το πώς να [δημιουργήσετε και να χρησιμοποιήσετε τη διεπαφή.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Γνωρίστε Άλλους Μαθητές

Έχουμε δημιουργήσει κανάλια στον επίσημο [Discord server της AI Κοινότητας](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) για να γνωρίσετε άλλους μαθητές. Είναι ένας εξαιρετικός τρόπος να δικτυωθείτε με άλλους επιχειρηματίες, δημιουργούς, φοιτητές και οποιονδήποτε θέλει να εξελιχθεί στη Γενετική Τεχνητή Νοημοσύνη.

[![Γίνετε μέλος στο κανάλι Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Η ομάδα του έργου θα βρίσκεται επίσης σε αυτόν τον Discord server για να βοηθήσει οποιονδήποτε μαθητή.

## Συνεισφορά

Αυτό το μάθημα είναι μια πρωτοβουλία ανοιχτού κώδικα. Αν δείτε περιοχές για βελτίωση ή προβλήματα, παρακαλούμε δημιουργήστε ένα [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ή καταγράψτε ένα [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Η ομάδα του έργου θα παρακολουθεί όλες τις συνεισφορές. Η συνεισφορά σε ανοιχτό κώδικα είναι ένας καταπληκτικός τρόπος να χτίσετε την καριέρα σας στη Γενετική Τεχνητή Νοημοσύνη.

Οι περισσότερες συνεισφορές απαιτούν να συμφωνήσετε με μια Συμφωνία Άδειας Χρήσης Συνεισφέροντος (CLA) δηλώνοντας ότι έχετε το δικαίωμα και πραγματικά παραχωρείτε σε εμάς τα δικαιώματα να χρησιμοποιήσουμε τη συνεισφορά σας. Για λεπτομέρειες, επισκεφθείτε τον [ιστότοπο CLA, Συμφωνία Άδειας Χρήσης Συνεισφέροντος](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Σημαντικό: όταν μεταφράζετε κείμενο σε αυτό το αποθετήριο, παρακαλούμε βεβαιωθείτε ότι δεν χρησιμοποιείτε μηχανική μετάφραση. Θα επαληθεύσουμε τις μεταφράσεις μέσω της κοινότητας, οπότε παρακαλούμε να προσφέρετε μεταφράσεις μόνο σε γλώσσες στις οποίες είστε επαρκείς.

Όταν υποβάλετε ένα pull request, ένα CLA-bot θα καθορίσει αυτόματα αν χρειάζεται να παρέχετε CLA και θα διακοσμήσει το PR κατάλληλα (π.χ., ετικέτα,
Τώρα που έχετε ολοκληρώσει τα απαραίτητα βήματα για να ολοκληρώσετε αυτό το μάθημα, ας ξεκινήσουμε με μια [εισαγωγή στη Γενετική Τεχνητή Νοημοσύνη και τα LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.