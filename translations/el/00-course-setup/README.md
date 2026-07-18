# Ξεκινώντας με αυτό το μάθημα

Είμαστε πολύ ενθουσιασμένοι που ξεκινάτε αυτό το μάθημα και θα δείτε τι θα εμπνευστείτε να δημιουργήσετε με την Γενετική AI!

Για να διασφαλίσουμε την επιτυχία σας, αυτή η σελίδα περιγράφει τα βήματα εγκατάστασης, τις τεχνικές απαιτήσεις και πού να λάβετε βοήθεια εάν χρειάζεται.

## Βήματα Εγκατάστασης

Για να ξεκινήσετε να παρακολουθείτε αυτό το μάθημα, θα χρειαστεί να ολοκληρώσετε τα ακόλουθα βήματα.

### 1. Κάντε fork αυτό το αποθετήριο

[Κάντε fork ολόκληρο αυτό το αποθετήριο](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) στον δικό σας λογαριασμό GitHub για να μπορείτε να τροποποιήσετε οποιονδήποτε κώδικα και να ολοκληρώσετε τις προκλήσεις. Μπορείτε επίσης να [σημειώσετε με αστέρι (🌟) αυτό το αποθετήριο](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) για να το βρείτε και σχετικά αποθετήρια ευκολότερα.

### 2. Δημιουργήστε έναν codespace

Για να αποφύγετε τυχόν προβλήματα εξαρτήσεων κατά την εκτέλεση του κώδικα, συνιστούμε να εκτελέσετε αυτό το μάθημα σε ένα [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Στο fork σας: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/el/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Προσθέστε ένα μυστικό

1. ⚙️ Εικονίδιο γραναζιού -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Όνομα OPENAI_API_KEY, επικολλήστε το κλειδί σας, Αποθήκευση.

### 3. Τι ακολουθεί;

| Θέλω να…              | Πηγαίνω σε…                                                                |
|---------------------|-------------------------------------------------------------------------|
| Ξεκινήσω το Μάθημα 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Δουλέψω εκτός σύνδεσης | [`setup-local.md`](02-setup-local.md)                                   |
| Ρυθμίσω έναν Πάροχο LLM | [`providers.md`](03-providers.md)                                        |
| Γνωρίσω άλλους μαθητές | [Join our Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Αντιμετώπιση Προβλημάτων


| Σύμπτωμα                                 | Διόρθωση                                                      |
|------------------------------------------|--------------------------------------------------------------|
| Η κατασκευή κοντέινερ κολλάει > 10 λεπτά | **Codespaces ➜ “Rebuild Container”**                         |
| `python: command not found`               | Το τερματικό δεν συνδέθηκε· κάντε κλικ στο **+** ➜ *bash*    |
| `401 Unauthorized` από OpenAI             | Λάθος / ληγμένο `OPENAI_API_KEY`                             |
| Το VS Code δείχνει “Dev container mounting…” | Ανανέωση της καρτέλας του browser — μερικές φορές Codespaces χάνει τη σύνδεση |
| Λείπει ο πυρήνας του Notebook             | Μενού Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**       |

   Unix-based συστήματα:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Επεξεργαστείτε το αρχείο `.env`**: Ανοίξτε το αρχείο `.env` σε ένα κειμενογράφο (π.χ., VS Code, Notepad++ ή οποιοδήποτε άλλο πρόγραμμα). Προσθέστε τις ακόλουθες γραμμές στο αρχείο, αντικαθιστώντας τις θέσεις κρατήσεων με το πραγματικό σας endpoint και κλειδί για Microsoft Foundry Models (βλέπε [`providers.md`](03-providers.md) για οδηγίες λήψης):

   > **Σημείωση:** Τα GitHub Models (και η μεταβλητή `GITHUB_TOKEN`) αποσύρονται στο τέλος Ιουλίου 2026. Χρησιμοποιήστε αντί αυτού τα [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Αποθηκεύστε το αρχείο**: Αποθηκεύστε τις αλλαγές και κλείστε τον κειμενογράφο.

5. **Εγκαταστήστε το `python-dotenv`**: Αν δεν το έχετε ήδη, πρέπει να εγκαταστήσετε το πακέτο `python-dotenv` για να φορτώσει τις μεταβλητές περιβάλλοντος από το αρχείο `.env` στην εφαρμογή Python σας. Μπορείτε να το εγκαταστήσετε με `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Φορτώστε τις Μεταβλητές Περιβάλλοντος στο Python Script σας**: Στο Python script σας, χρησιμοποιήστε το πακέτο `python-dotenv` για να φορτώσετε τις μεταβλητές περιβάλλοντος από το αρχείο `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Φόρτωση μεταβλητών περιβάλλοντος από το αρχείο .env
   load_dotenv()

   # Πρόσβαση στις μεταβλητές των Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Αυτό ήταν! Έχετε δημιουργήσει επιτυχώς αρχείο `.env`, προσθέσατε τα διαπιστευτήρια Microsoft Foundry Models και τα φορτώσατε στην εφαρμογή Python σας.

## Πώς να τρέξετε τοπικά στον υπολογιστή σας

Για να τρέξετε τον κώδικα τοπικά στον υπολογιστή σας, θα χρειαστεί να έχετε κάποια έκδοση του [εγκατεστημένου Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Για να χρησιμοποιήσετε το αποθετήριο, πρέπει να το κλωνοποιήσετε:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Μόλις έχετε όλα ετοιμα, μπορείτε να ξεκινήσετε!

## Προαιρετικά Βήματα

### Εγκατάσταση Miniconda

Το [Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) είναι ένας ελαφρύς εγκαταστάτης για την εγκατάσταση του [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), του Python, καθώς και μερικών πακέτων.
Το Conda είναι ένας διαχειριστής πακέτων που διευκολύνει τη ρύθμιση και την εναλλαγή ανάμεσα σε διαφορετικά [**εικονικά περιβάλλοντα**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) και πακέτα Python. Είναι επίσης χρήσιμο για την εγκατάσταση πακέτων που δεν είναι διαθέσιμα μέσω `pip`.

Μπορείτε να ακολουθήσετε τον [οδηγό εγκατάστασης MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) για να το ρυθμίσετε.

Με το Miniconda εγκατεστημένο, χρειάζεται να κλωνοποιήσετε το [αποθετήριο](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (αν δεν το έχετε κάνει ήδη)

Στη συνέχεια, πρέπει να δημιουργήσετε ένα εικονικό περιβάλλον. Για να το κάνετε αυτό με το Conda, προχωρήστε και δημιουργήστε ένα νέο αρχείο περιβάλλοντος (_environment.yml_). Αν ακολουθείτε μέσω Codespaces, δημιουργήστε το μέσα στον κατάλογο `.devcontainer`, δηλαδή `.devcontainer/environment.yml`.

Προχωρήστε και συμπληρώστε το αρχείο περιβάλλοντος με το παρακάτω απόσπασμα:

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

Αν λαμβάνετε σφάλματα χρησιμοποιώντας το conda, μπορείτε να εγκαταστήσετε χειροκίνητα τις Βιβλιοθήκες Microsoft AI χρησιμοποιώντας την ακόλουθη εντολή σε ένα τερματικό.

```
conda install -c microsoft azure-ai-ml
```

Το αρχείο περιβάλλοντος ορίζει τις εξαρτήσεις που χρειαζόμαστε. Το `<environment-name>` αναφέρεται στο όνομα που θέλετε να χρησιμοποιήσετε για το Conda περιβάλλον σας, και το `<python-version>` είναι η έκδοση του Python που θέλετε να χρησιμοποιήσετε, για παράδειγμα, το `3` είναι η τελευταία κύρια έκδοση του Python.

Με αυτόν τον τρόπο, μπορείτε να δημιουργήσετε το περιβάλλον Conda εκτελώντας τις παρακάτω εντολές στη γραμμή εντολών/τερματικό σας

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Η υποδιαδρομή .devcontainer ισχύει μόνο για ρυθμίσεις Codespace
conda activate ai4beg
```

Ανατρέξτε στον [οδηγό περιβαλλόντων Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) αν αντιμετωπίσετε οποιοδήποτε πρόβλημα.

### Χρήση Visual Studio Code με την επέκταση υποστήριξης Python  

Συνιστούμε τη χρήση του επεξεργαστή [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) με την εγκατάσταση της [εφαρμογής υποστήριξης Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) για αυτό το μάθημα. Αυτό, ωστόσο, είναι περισσότερο σύσταση παρά απαίτηση.

> **Σημείωση**: Ανοίγοντας το αποθετήριο του μαθήματος στο VS Code, έχετε τη δυνατότητα να ρυθμίσετε το έργο εντός ενός container. Αυτό οφείλεται στον [ειδικό φάκελο `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) που περιέχεται στο αποθετήριο. Περισσότερα αργότερα.

> **Σημείωση**: Μόλις κλωνοποιήσετε και ανοίξετε το φάκελο στο VS Code, θα σας προταθεί αυτόματα να εγκαταστήσετε την επέκταση υποστήριξης Python.

> **Σημείωση**: Αν το VS Code προτείνει να ξανανοίξετε το αποθετήριο μέσα σε container, αρνηθείτε αυτό το αίτημα για να χρησιμοποιήσετε την τοπικά εγκατεστημένη έκδοση του Python.

### Χρήση Jupyter στον Browser

Μπορείτε επίσης να δουλέψετε στο έργο χρησιμοποιώντας το [περιβάλλον Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) απευθείας μέσα από τον browser σας. Τόσο το κλασικό Jupyter όσο και το [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) παρέχουν ένα ευχάριστο περιβάλλον ανάπτυξης με λειτουργίες όπως αυτόματη συμπλήρωση, επισήμανση κώδικα κλπ.

Για να ξεκινήσετε τοπικά το Jupyter, ανοίξτε το τερματικό/γραμμή εντολών, μεταβείτε στον κατάλογο του μαθήματος και εκτελέστε:

```bash
jupyter notebook
```

ή

```bash
jupyterhub
```

Αυτό θα ξεκινήσει μια παρουσία Jupyter και το URL για πρόσβαση θα εμφανιστεί στο παράθυρο της γραμμής εντολών.

Μόλις αποκτήσετε πρόσβαση στο URL, θα δείτε την περίληψη του μαθήματος και θα μπορείτε να μεταβείτε σε οποιοδήποτε αρχείο `*.ipynb`, για παράδειγμα, `08-building-search-applications/python/oai-solution.ipynb`.

### Εκτέλεση σε container

Μια εναλλακτική στο να ρυθμίσετε τα πάντα στον υπολογιστή ή το Codespace σας είναι να χρησιμοποιήσετε ένα [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Ο ειδικός φάκελος `.devcontainer` μέσα στο αποθετήριο του μαθήματος επιτρέπει στο VS Code να ρυθμίσει το έργο μέσα σε ένα container. Εκτός Codespaces, αυτό απαιτεί την εγκατάσταση του Docker, και ειλικρινά, περιλαμβάνει κάποια δουλειά, οπότε το προτείνουμε μόνο σε όσους έχουν εμπειρία με containers.

Ένας από τους καλύτερους τρόπους για να διατηρείτε ασφαλή τα API κλειδιά σας όταν χρησιμοποιείτε GitHub Codespaces είναι μέσω της χρήσης Codespace Secrets. Παρακαλώ ακολουθήστε τον οδηγό [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) για να μάθετε περισσότερα γι' αυτό.


## Μαθήματα και Τεχνικές Απαιτήσεις

Το μάθημα περιλαμβάνει μαθήματα "Μάθε" που εξηγούν έννοιες της Γενετικής AI και μαθήματα "Κατασκευή" με πρακτικά παραδείγματα κώδικα σε **Python** και **TypeScript** όπου είναι δυνατόν.

Για τα μαθήματα κώδικα, χρησιμοποιούμε το Azure OpenAI στο Microsoft Foundry. Θα χρειαστείτε μια συνδρομή Azure και ένα API key. Η πρόσβαση είναι ανοιχτή - δεν απαιτείται αίτηση - οπότε μπορείτε να [δημιουργήσετε έναν πόρο Microsoft Foundry και να αναπτύξετε ένα μοντέλο](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) για να πάρετε το endpoint και το κλειδί σας.

Κάθε μάθημα κώδικα περιλαμβάνει επίσης ένα αρχείο `README.md` όπου μπορείτε να δείτε τον κώδικα και τα αποτελέσματα χωρίς να τρέξετε τίποτα.

## Χρήση της υπηρεσίας Azure OpenAI για πρώτη φορά

Αν είναι η πρώτη φορά που δουλεύετε με την υπηρεσία Azure OpenAI, παρακαλώ ακολουθήστε αυτόν τον οδηγό για το πώς να [δημιουργήσετε και αναπτύξετε πόρο Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Χρήση της OpenAI API για πρώτη φορά

Αν είναι η πρώτη φορά που δουλεύετε με το OpenAI API, παρακαλώ ακολουθήστε τον οδηγό για το πώς να [δημιουργήσετε και χρησιμοποιήσετε το Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Γνωρίστε Άλλους Μαθητές

Έχουμε δημιουργήσει κανάλια στον επίσημο [Discord server AI Community](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) για να γνωρίσετε άλλους μαθητές. Αυτός είναι ένας εξαιρετικός τρόπος να δικτυωθείτε με άλλους ομοϊδεάτες επιχειρηματίες, δημιουργούς, φοιτητές και οποιονδήποτε θέλει να βελτιωθεί στο Generative AI.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Η ομάδα του έργου θα είναι επίσης σε αυτόν το Discord server για να βοηθά οποιουσδήποτε μαθητές.

## Συνεισφορά

Αυτό το μάθημα είναι πρωτοβουλία ανοιχτού κώδικα. Αν δείτε πεδία βελτίωσης ή προβλήματα, παρακαλώ δημιουργήστε ένα [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ή καταγράψτε ένα [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Η ομάδα του έργου θα παρακολουθεί όλες τις συνεισφορές. Η συνεισφορά σε ανοιχτό κώδικα είναι ένας υπέροχος τρόπος να χτίσετε την καριέρα σας στη Γενετική AI.

Οι περισσότερες συνεισφορές απαιτούν να συμφωνήσετε με μια Συμφωνία Άδειας Συνεισφοράς (CLA) που δηλώνει ότι έχετε το δικαίωμα και στην πραγματικότητα παραχωρείτε σε εμάς τα δικαιώματα να χρησιμοποιήσουμε τη συνεισφορά σας. Για λεπτομέρειες, επισκεφτείτε [την ιστοσελίδα CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Σημαντικό: όταν μεταφράζετε κείμενο σε αυτό το αποθετήριο, παρακαλώ βεβαιωθείτε πως δεν χρησιμοποιείτε μηχανική μετάφραση. Θα επαληθεύσουμε τις μεταφράσεις μέσω της κοινότητας, οπότε παρακαλώ εθελοντικά μόνο για μεταφράσεις σε γλώσσες που γνωρίζετε καλά.


Όταν υποβάλλετε ένα pull request, ένα CLA-bot θα καθορίσει αυτόματα αν χρειάζεται να παράσχετε ένα CLA και θα διακοσμήσει κατάλληλα το PR (π.χ., ετικέτα, σχόλιο). Απλώς ακολουθήστε τις οδηγίες που παρέχονται από το bot. Θα χρειαστεί να το κάνετε μόνο μία φορά σε όλα τα αποθετήρια που χρησιμοποιούν το CLA μας.

Αυτό το έργο έχει υιοθετήσει τον [Κώδικα Δεοντολογίας Ανοιχτού Κώδικα της Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Για περισσότερες πληροφορίες διαβάστε το FAQ του Κώδικα Δεοντολογίας ή επικοινωνήστε με το [Email opencode](opencode@microsoft.com) για οποιεσδήποτε επιπλέον ερωτήσεις ή σχόλια.

## Ας Ξεκινήσουμε

Τώρα που ολοκληρώσατε τα απαραίτητα βήματα για να ολοκληρώσετε αυτό το μάθημα, ας ξεκινήσουμε με μια [εισαγωγή στην Παραγωγική Τεχνητή Νοημοσύνη και τα LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->