# Ξεκινώντας με αυτό το μάθημα

Είμαστε πολύ ενθουσιασμένοι που ξεκινάτε αυτό το μάθημα και να δείτε τι θα εμπνευστείτε να δημιουργήσετε με τη Γεννητική Τεχνητή Νοημοσύνη!

Για να διασφαλίσουμε την επιτυχία σας, αυτή η σελίδα περιγράφει τα βήματα εγκατάστασης, τις τεχνικές απαιτήσεις και πού μπορείτε να ζητήσετε βοήθεια αν χρειαστεί.

## Βήματα Εγκατάστασης

Για να ξεκινήσετε το μάθημα, θα χρειαστεί να ολοκληρώσετε τα ακόλουθα βήματα.

### 1. Κάντε Fork αυτό το Repo

[Κάντε Fork ολόκληρο αυτό το αποθετήριο](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) στον δικό σας λογαριασμό GitHub για να μπορείτε να αλλάξετε οποιονδήποτε κώδικα και να ολοκληρώσετε τις προκλήσεις. Μπορείτε επίσης να [βαθμολογήσετε (🌟) αυτό το αποθετήριο](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) για να το βρίσκετε εσείς και σχετικά αποθετήρια πιο εύκολα.

### 2. Δημιουργήστε ένα codespace

Για να αποφύγετε προβλήματα με εξαρτήσεις κατά την εκτέλεση του κώδικα, προτείνουμε να τρέχετε αυτό το μάθημα σε ένα [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Στο fork σας: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/el/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Προσθέστε ένα μυστικό

1. ⚙️ Εικονίδιο ρυθμίσεων -> Command Pallete-> Codespaces: Διαχείριση μυστικού χρήστη -> Προσθήκη νέου μυστικού.
2. Όνομα OPENAI_API_KEY, επικολλήστε το κλειδί σας, Αποθήκευση.

### 3. Τι ακολουθεί;

| Θέλω να…          | Μεταβείτε σε…                                                          |
|---------------------|-------------------------------------------------------------------------|
| Ξεκινήσω το Μάθημα 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Εργαστώ εκτός σύνδεσης | [`setup-local.md`](02-setup-local.md)                                   |
| Ρυθμίσω έναν πάροχο LLM | [`providers.md`](03-providers.md)                                        |
| Γνωρίσω άλλους μαθητές | [Γίνετε μέλος στο Discord μας](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Αντιμετώπιση Προβλημάτων


| Σύμπτωμα                              | Διόρθωση                                                       |
|---------------------------------------|---------------------------------------------------------------|
| Η κατασκευή του container κολλάει > 10 λ | **Codespaces ➜ “Rebuild Container”**                          |
| `python: command not found`            | Το τερματικό δεν συνδέθηκε· κάντε κλικ στο **+** ➜ *bash*       |
| `401 Unauthorized` από OpenAI          | Λανθασμένο / ληγμένο `OPENAI_API_KEY`                           |
| Το VS Code δείχνει “Dev container mounting…” | Ανανέωση της καρτέλας του browser—Τα Codespaces μερικές φορές χάνουν τη σύνδεση  |
| Λείπει ο πυρήνας του Notebook          | Μενού Notebook ➜ **Kernel ▸ Επιλέξτε Kernel ▸ Python 3**         |

   Συστήματα βασισμένα σε Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Επεξεργαστείτε το αρχείο `.env`**: Ανοίξτε το αρχείο `.env` σε έναν επεξεργαστή κειμένου (π.χ., VS Code, Notepad++ ή κάποιον άλλον). Προσθέστε τις ακόλουθες γραμμές στο αρχείο, αντικαθιστώντας τα placeholders με το πραγματικό σας endpoint και κλειδί για τα Microsoft Foundry Models (βλέπε [`providers.md`](03-providers.md) για το πώς να τα αποκτήσετε):

   > **Σημείωση:** Τα GitHub Models (και η μεταβλητή `GITHUB_TOKEN`) θα καταργηθούν στα τέλη Ιουλίου 2026. Χρησιμοποιήστε [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) αντί αυτού.

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Αποθηκεύστε το αρχείο**: Αποθηκεύστε τις αλλαγές και κλείστε τον επεξεργαστή κειμένου.

5. **Εγκαταστήστε το `python-dotenv`**: Εάν δεν το έχετε ήδη, θα χρειαστεί να εγκαταστήσετε το πακέτο `python-dotenv` για να φορτώνετε τις μεταβλητές περιβάλλοντος από το αρχείο `.env` στην εφαρμογή Python σας. Μπορείτε να το εγκαταστήσετε με χρήση `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Φορτώστε τις Μεταβλητές Περιβάλλοντος στο σενάριό σας Python**: Στο σενάριό σας Python, χρησιμοποιήστε το πακέτο `python-dotenv` για να φορτώσετε τις μεταβλητές περιβάλλοντος από το αρχείο `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Φόρτωση μεταβλητών περιβάλλοντος από το αρχείο .env
   load_dotenv()

   # Πρόσβαση στις μεταβλητές Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Αυτό ήταν! Έχετε δημιουργήσει επιτυχώς ένα αρχείο `.env`, προσθέσατε τα διαπιστευτήρια των Microsoft Foundry Models, και τα φορτώσατε στην Python εφαρμογή σας.

## Πώς να εκτελέσετε τοπικά στον υπολογιστή σας

Για να τρέξετε τον κώδικα τοπικά στον υπολογιστή σας, θα χρειαστεί να έχετε εγκαταστήσει κάποια έκδοση [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Για να χρησιμοποιήσετε το αποθετήριο, θα πρέπει να το κλωνοποιήσετε:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Μόλις έχετε τα πάντα, μπορείτε να ξεκινήσετε!

## Προαιρετικά Βήματα

### Εγκατάσταση Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) είναι ένας ελαφρύς εγκαταστάτης για την εγκατάσταση του [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), της Python, καθώς και μερικών πακέτων.
Το Conda είναι ένας διαχειριστής πακέτων, που κάνει εύκολη τη ρύθμιση και την εναλλαγή ανάμεσα σε διαφορετικά Python [**εικονικά περιβάλλοντα**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) και πακέτα. Είναι επίσης χρήσιμο για την εγκατάσταση πακέτων που δεν είναι διαθέσιμα μέσω `pip`.

Μπορείτε να ακολουθήσετε τον [οδηγό εγκατάστασης MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) για να το ρυθμίσετε.

Με το Miniconda εγκατεστημένο, πρέπει να κλωνοποιήσετε το [αποθετήριο](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (αν δεν το έχετε κάνει ήδη)

Έπειτα, πρέπει να δημιουργήσετε ένα εικονικό περιβάλλον. Για να το κάνετε αυτό με το Conda, προχωρήστε και δημιουργήστε ένα νέο αρχείο περιβάλλοντος (_environment.yml_). Αν ακολουθείτε με Codespaces, δημιουργήστε το μέσα στον φάκελο `.devcontainer`, δηλαδή `.devcontainer/environment.yml`.

Προχωρήστε και συμπληρώστε το αρχείο περιβάλλοντός σας με το απόσπασμα παρακάτω:

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

Αν αντιμετωπίζετε σφάλματα με το conda, μπορείτε να εγκαταστήσετε χειροκίνητα τις βιβλιοθήκες Microsoft AI με την ακόλουθη εντολή σε τερματικό.

```
conda install -c microsoft azure-ai-ml
```

Το αρχείο περιβάλλοντος καθορίζει τις εξαρτήσεις που χρειαζόμαστε. Το `<environment-name>` αναφέρεται στο όνομα που θέλετε να χρησιμοποιήσετε για το περιβάλλον Conda σας, και το `<python-version>` είναι η έκδοση της Python που θέλετε να χρησιμοποιήσετε, για παράδειγμα, το `3` είναι η πιο πρόσφατη κύρια έκδοση της Python.

Αφού το κάνετε αυτό, μπορείτε να δημιουργήσετε το Conda περιβάλλον σας εκτελώντας τις εντολές παρακάτω στο τερματικό/γραμμή εντολών

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Η υποδιαδρομή .devcontainer ισχύει μόνο για ρυθμίσεις Codespace
conda activate ai4beg
```

Αναφερθείτε στον [οδηγό περιβαλλόντων Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) αν αντιμετωπίσετε προβλήματα.

### Χρήση Visual Studio Code με την επέκταση υποστήριξης Python

Προτείνουμε τη χρήση του επεξεργαστή [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) με την [επέκταση υποστήριξης Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) εγκατεστημένη για αυτό το μάθημα. Αυτό, ωστόσο, είναι περισσότερο μια σύσταση και όχι απαραίτητη προϋπόθεση.

> **Σημείωση**: Ανοίγοντας το αποθετήριο του μαθήματος στο VS Code, έχετε την επιλογή να ρυθμίσετε το έργο μέσα σε ένα container. Αυτό οφείλεται στον [ειδικό φάκελο `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) που βρίσκεται μέσα στο αποθετήριο του μαθήματος. Θα το δούμε αργότερα.

> **Σημείωση**: Μόλις κλωνοποιήσετε και ανοίξετε το φάκελο στο VS Code, θα σας προταθεί αυτόματα να εγκαταστήσετε μια επέκταση υποστήριξης Python.

> **Σημείωση**: Αν το VS Code σας προτείνει να ξανανοίξετε το αποθετήριο μέσα σε container, αρνηθείτε για να χρησιμοποιήσετε την τοπικά εγκατεστημένη έκδοση Python.

### Χρήση Jupyter στον Browser

Μπορείτε επίσης να εργαστείτε στο έργο χρησιμοποιώντας το [περιβάλλον Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) ακριβώς μέσα από τον browser σας. Τόσο το κλασικό Jupyter όσο και το [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) προσφέρουν ένα ευχάριστο περιβάλλον ανάπτυξης με λειτουργίες όπως αυτόματη συμπλήρωση, υπογράμμιση κώδικα κ.ά.

Για να ξεκινήσετε το Jupyter τοπικά, μεταβείτε σε τερματικό/γραμμή εντολών, πηγαίνετε στον φάκελο του μαθήματος, και εκτελέστε:

```bash
jupyter notebook
```

ή

```bash
jupyterhub
```

Αυτό θα ξεκινήσει ένα Jupyter instance και η URL για να το ανοίξετε θα εμφανιστεί στο παράθυρο της γραμμής εντολών.

Μόλις αποκτήσετε πρόσβαση στη URL, θα δείτε το περίγραμμα του μαθήματος και θα μπορείτε να μετακινηθείτε σε οποιοδήποτε αρχείο `*.ipynb`. Για παράδειγμα, `08-building-search-applications/python/oai-solution.ipynb`.

### Εκτέλεση σε container

Μια εναλλακτική στο να κάνετε όλη τη ρύθμιση στον υπολογιστή σας ή σε Codespace είναι να χρησιμοποιήσετε ένα [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Ο ειδικός φάκελος `.devcontainer` μέσα στο αποθετήριο του μαθήματος επιτρέπει στο VS Code να ρυθμίσει το έργο μέσα σε ένα container. Εκτός από τα Codespaces, αυτό απαιτεί την εγκατάσταση του Docker και, ειλικρινά, χρειάζεται λίγη δουλειά, οπότε το προτείνουμε μόνο σε όσους έχουν εμπειρία με containers.

Ένας από τους καλύτερους τρόπους να κρατήσετε τα API κλειδιά σας ασφαλή όταν χρησιμοποιείτε GitHub Codespaces είναι η χρήση των Codespace Secrets. Ακολουθήστε τον οδηγό [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) για να μάθετε περισσότερα.


## Μαθήματα και Τεχνικές Απαιτήσεις

Το μάθημα έχει 6 μαθήματα εννοιών και 6 μαθημάτων κώδικα.

Για τα μαθήματα κώδικα, χρησιμοποιούμε την υπηρεσία Azure OpenAI. Θα χρειαστεί να έχετε πρόσβαση στην υπηρεσία Azure OpenAI και ένα API κλειδί για να τρέξετε αυτόν τον κώδικα. Μπορείτε να κάνετε αίτηση για πρόσβαση [συμπληρώνοντας αυτή την αίτηση](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Ενώ περιμένετε να επεξεργαστεί η αίτησή σας, κάθε μάθημα κώδικα περιλαμβάνει επίσης ένα αρχείο `README.md` όπου μπορείτε να δείτε τον κώδικα και τα αποτελέσματα.

## Χρήση της υπηρεσίας Azure OpenAI για πρώτη φορά

Αν είναι η πρώτη φορά που εργάζεστε με την υπηρεσία Azure OpenAI, παρακαλώ ακολουθήστε αυτόν τον οδηγό για το πώς να [δημιουργήσετε και αναπτύξετε ένα πόρο Azure OpenAI Service.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Χρήση του OpenAI API για πρώτη φορά

Αν είναι η πρώτη φορά που εργάζεστε με το OpenAI API, παρακαλώ ακολουθήστε τον οδηγό για το πώς να [δημιουργήσετε και να χρησιμοποιήσετε το Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Γνωρίστε άλλους μαθητές

Έχουμε δημιουργήσει κανάλια στον επίσημο [Discord server της AI Community](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) για να γνωρίσετε άλλους μαθητές. Αυτή είναι μια εξαιρετική ευκαιρία να δικτυωθείτε με άλλους ομοϊδεάτες επιχειρηματίες, δημιουργούς, φοιτητές και όποιον θέλει να ανέβει επίπεδο στη Γεννητική Τεχνητή Νοημοσύνη.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Η ομάδα του έργου θα είναι επίσης σε αυτόν τον Discord server για να βοηθά κάθε μαθητή.

## Συμβολή

Αυτό το μάθημα είναι μια πρωτοβουλία ανοιχτού κώδικα. Αν δείτε βελτιώσεις ή προβλήματα, παρακαλώ δημιουργήστε ένα [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ή καταχωρήστε ένα [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Η ομάδα του έργου θα παρακολουθεί όλες τις συμβολές. Η συμβολή σε ανοιχτό κώδικα είναι ένας υπέροχος τρόπος να χτίσετε την καριέρα σας στη Γεννητική Τεχνητή Νοημοσύνη.

Οι περισσότερες συμβολές απαιτούν να συμφωνήσετε με μια Συμφωνία Άδειας Συμβολής (CLA) που δηλώνει ότι έχετε το δικαίωμα και πραγματικά παραχωρείτε τα δικαιώματα να χρησιμοποιήσουμε τη συμβολή σας. Για περισσότερες πληροφορίες, επισκεφθείτε την [ιστοσελίδα της CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Σημαντικό: όταν μεταφράζετε κείμενο σε αυτό το αποθετήριο, παρακαλούμε βεβαιωθείτε ότι δεν χρησιμοποιείτε μηχανική μετάφραση. Θα ελέγξουμε τις μεταφράσεις μέσω της κοινότητας, οπότε παρακαλούμε να προσφέρετε μετάφραση μόνο σε γλώσσες που γνωρίζετε καλά.

Όταν υποβάλετε ένα pull request, ένα bot CLA-bot θα καθορίσει αυτόματα αν πρέπει να παρέχετε μια CLA και θα επισημάνει κατάλληλα το PR (π.χ., με ετικέτα, σχόλιο). Απλώς ακολουθήστε τις οδηγίες του bot. Θα το χρειαστεί να το κάνετε μόνο μία φορά σε όλα τα αποθετήρια που χρησιμοποιούν την CLA μας.


Αυτό το έργο έχει υιοθετήσει τον [Κώδικα Δεοντολογίας για τον Ανοιχτό Κώδικα της Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Για περισσότερες πληροφορίες, διαβάστε τις Συχνές Ερωτήσεις για τον Κώδικα Δεοντολογίας ή επικοινωνήστε με το [Email opencode](opencode@microsoft.com) για οποιεσδήποτε επιπλέον ερωτήσεις ή σχόλια.

## Ας Ξεκινήσουμε

Τώρα που έχετε ολοκληρώσει τα απαραίτητα βήματα για την ολοκλήρωση αυτού του μαθήματος, ας ξεκινήσουμε με μια [εισαγωγή στην Γενετική Τεχνητή Νοημοσύνη και τα Μεγάλα Γλωσσικά Μοντέλα](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->