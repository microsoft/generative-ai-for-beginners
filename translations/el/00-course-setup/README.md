# Ξεκινώντας με αυτό το μάθημα

Είμαστε πολύ ενθουσιασμένοι που ξεκινάτε αυτό το μάθημα και θα δείτε τι εμπνευσμένοι θα γίνετε να δημιουργήσετε με τη Δημιουργική Τεχνητή Νοημοσύνη!

Για να εξασφαλίσουμε την επιτυχία σας, αυτή η σελίδα περιγράφει τα βήματα εγκατάστασης, τις τεχνικές απαιτήσεις και πού να βρείτε βοήθεια αν χρειαστεί.

## Βήματα Εγκατάστασης

Για να ξεκινήσετε να παρακολουθείτε αυτό το μάθημα, θα χρειαστεί να ολοκληρώσετε τα παρακάτω βήματα.

### 1. Κλωνοποίηση αυτού του repository

[Κλωνοποιήστε ολόκληρο το repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) στον δικό σας λογαριασμό GitHub για να μπορείτε να αλλάξετε οποιονδήποτε κώδικα και να ολοκληρώσετε τις προκλήσεις. Μπορείτε επίσης να [κάνετε star (🌟) στο repository αυτό](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) ώστε να το βρίσκετε εσείς και σχετικές αποθετηριακές πιο εύκολα.

### 2. Δημιουργήστε ένα codespace

Για να αποφύγετε τυχόν προβλήματα με εξαρτήσεις κατά την εκτέλεση του κώδικα, συνιστούμε να εκτελέσετε αυτό το μάθημα σε ένα [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Στον clone σας: **Code -> Codespaces -> New on main**

![Dialog showing buttons to create a codespace](../../../translated_images/el/who-will-pay.4c0609b1c7780f44.webp)

#### 2.1 Προσθήκη μυστικού

1. ⚙️ Εικονίδιο ρυθμίσεων -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Ονομάστε το OPENAI_API_KEY, επικολλήστε το κλειδί σας, Αποθηκεύστε.

### 3. Τι ακολουθεί;

| Θέλω να…           | Μετάβαση σε…                                                         |
|---------------------|---------------------------------------------------------------------|
| Ξεκινήσω το Μάθημα 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)  |
| Δουλέψω εκτός σύνδεσης | [`setup-local.md`](02-setup-local.md)                                |
| Ρυθμίσω έναν πάροχο LLM | [`providers.md`](03-providers.md)                                    |
| Γνωρίσω άλλους μαθητές | [Εγγραφείτε στο Discord μας](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## Επίλυση προβλημάτων

| Σύμπτωμα                                  | Επίλυση                                                         |
|-------------------------------------------|-----------------------------------------------------------------|
| Η δημιουργία container "κολλάει" > 10 λεπτά | **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`               | Το τερματικό δεν συνδέθηκε· κάντε κλικ στο **+** ➜ *bash*       |
| `401 Unauthorized` από OpenAI              | Λάθος / ληγμένο `OPENAI_API_KEY`                                |
| Το VS Code δείχνει “Dev container mounting…”   | Ανανέωση της καρτέλας του browser — Τα Codespaces χάνουν μερικές φορές σύνδεση |
| Απουσία kernel στο Notebook               | Μενού Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**          |

   Unix-based συστήματα:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Επεξεργασία του αρχείου `.env`**: Ανοίξτε το αρχείο `.env` σε έναν επεξεργαστή κειμένου (π.χ., VS Code, Notepad++ ή οποιονδήποτε άλλο). Προσθέστε την ακόλουθη γραμμή στο αρχείο, αντικαθιστώντας το `your_github_token_here` με το πραγματικό σας token GitHub:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Αποθηκεύστε το αρχείο**: Αποθηκεύστε τις αλλαγές και κλείστε τον επεξεργαστή κειμένου.

5. **Εγκατάσταση `python-dotenv`**: Αν δεν το έχετε ήδη κάνει, θα χρειαστεί να εγκαταστήσετε το πακέτο `python-dotenv` για να φορτώσετε μεταβλητές περιβάλλοντος από το αρχείο `.env` στην Python εφαρμογή σας. Μπορείτε να το εγκαταστήσετε με `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Φόρτωση μεταβλητών περιβάλλοντος στο Python script σας**: Στο Python script σας, χρησιμοποιήστε το πακέτο `python-dotenv` για να φορτώσετε τις μεταβλητές περιβάλλοντος από το αρχείο `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Φορτώστε τις μεταβλητές περιβάλλοντος από το αρχείο .env
   load_dotenv()

   # Πρόσβαση στη μεταβλητή GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Αυτό είναι όλο! Δημιουργήσατε επιτυχώς αρχείο `.env`, προσθέσατε το token GitHub και το φορτώσατε στην Python εφαρμογή σας.

## Πώς να τρέξετε τοπικά στον υπολογιστή σας

Για να τρέξετε τον κώδικα τοπικά στον υπολογιστή σας, πρέπει να έχετε εγκατεστημένη κάποια έκδοση [Python](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Στη συνέχεια, για να χρησιμοποιήσετε το αποθετήριο, πρέπει να το κλωνοποιήσετε:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Μόλις έχετε όλα ρυθμισμένα, μπορείτε να ξεκινήσετε!

## Προαιρετικά Βήματα

### Εγκατάσταση Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) είναι ένας ελαφρύς installer για την εγκατάσταση του [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, καθώς και μερικών πακέτων. 
Το Conda είναι ένας διαχειριστής πακέτων, που καθιστά εύκολη τη ρύθμιση και εναλλαγή μεταξύ διαφορετικών [εικονικών περιβαλλόντων](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) και πακέτων Python. Είναι επίσης χρήσιμο για εγκατάσταση πακέτων που δεν διατίθενται μέσω του `pip`.

Μπορείτε να ακολουθήσετε τον [οδηγό εγκατάστασης MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) για να την εγκαταστήσετε.

Αφού εγκαταστήσετε το Miniconda, πρέπει να κλωνοποιήσετε το [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (αν δεν το έχετε ήδη κάνει)

Επόμενο βήμα είναι να δημιουργήσετε ένα εικονικό περιβάλλον. Για να το κάνετε αυτό με το Conda, φτιάξτε ένα νέο αρχείο περιβάλλοντος ( _environment.yml_). Αν ακολουθείτε τα βήματα χρησιμοποιώντας τα Codespaces, δημιουργήστε το μέσα στον φάκελο `.devcontainer`, δηλαδή `.devcontainer/environment.yml`.

Συμπληρώστε το αρχείο περιβάλλοντός σας με την παρακάτω απεικόνιση:

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

Αν λαμβάνετε σφάλματα χρησιμοποιώντας το conda, μπορείτε να εγκαταστήσετε χειροκίνητα τις Βιβλιοθήκες Microsoft AI εκτελώντας την παρακάτω εντολή σε τερματικό.

```
conda install -c microsoft azure-ai-ml
```

Το αρχείο περιβάλλοντος καθορίζει τις εξαρτήσεις που χρειάζονται. Το `<environment-name>` αναφέρεται στο όνομα που θέλετε να δώσετε στο περιβάλλον Conda, και το `<python-version>` είναι η έκδοση της Python που θέλετε να χρησιμοποιήσετε, για παράδειγμα, το `3` είναι η πιο πρόσφατη σημαντική έκδοση της Python.

Αφού ολοκληρώσετε, μπορείτε να δημιουργήσετε το Conda περιβάλλον σας εκτελώντας τις παρακάτω εντολές στο τερματικό/γραμμή εντολών σας

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # Η υποδιαδρομή .devcontainer ισχύει μόνο για ρυθμίσεις Codespace
conda activate ai4beg
```

Ανατρέξτε στον [οδηγό περιβαλλόντων Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) αν αντιμετωπίσετε προβλήματα.

### Χρήση του Visual Studio Code με την επέκταση υποστήριξης Python

Συνιστούμε τη χρήση του [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) με την [εξέταση υποστήριξης Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) εγκατεστημένη για αυτό το μάθημα. Αυτό όμως είναι περισσότερο μια σύσταση και όχι απόλυτη απαίτηση.

> **Σημείωση**: Ανοίγοντας το repository του μαθήματος στο VS Code, έχετε την επιλογή να ρυθμίσετε το έργο μέσα σε ένα container. Αυτό γίνεται λόγω του [ειδικού φακέλου `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) που υπάρχει μέσα στο repository του μαθήματος. Περισσότερα για αυτό αργότερα.

> **Σημείωση**: Μόλις κλωνοποιήσετε και ανοίξετε τον φάκελο στο VS Code, θα σας προταθεί αυτόματα η εγκατάσταση μιας επέκτασης υποστήριξης Python.

> **Σημείωση**: Αν το VS Code σας προτείνει να ξανανοίξετε το repository μέσα σε container, απορρίψτε αυτή την πρόταση ώστε να χρησιμοποιήσετε την τοπική εγκατάσταση Python.

### Χρήση Jupyter στον περιηγητή

Μπορείτε επίσης να δουλέψετε στο έργο χρησιμοποιώντας το [περιβάλλον Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) απευθείας μέσα στον περιηγητή σας. Τόσο το κλασικό Jupyter όσο και το [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) παρέχουν ένα πολύ ευχάριστο περιβάλλον ανάπτυξης με δυνατότητες όπως αυτόματη ολοκλήρωση, επισήμανση κώδικα κλπ.

Για να ξεκινήσετε τοπικά τον Jupyter, ανοίξτε το τερματικό/γραμμή εντολών, μεταβείτε στο φάκελο του μαθήματος και εκτελέστε:

```bash
jupyter notebook
```

ή

```bash
jupyterhub
```

Αυτό θα ξεκινήσει ένα instance του Jupyter και η διεύθυνση URL για να το επισκεφτείτε θα εμφανιστεί στο παράθυρο εντολών.

Μόλις έχετε πρόσβαση στο URL, θα δείτε το περίγραμμα του μαθήματος και μπορείτε να πλοηγηθείτε σε οποιοδήποτε αρχείο `*.ipynb`. Για παράδειγμα, `08-building-search-applications/python/oai-solution.ipynb`.

### Εκτέλεση μέσα σε container

Μια εναλλακτική στο να ρυθμίσετε τα πάντα στον υπολογιστή σας ή στο Codespace είναι να χρησιμοποιήσετε ένα [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Ο ειδικός φάκελος `.devcontainer` μέσα στο repository του μαθήματος επιτρέπει στο VS Code να ρυθμίσει το έργο μέσα σε container. Εκτός Codespaces, αυτό απαιτεί την εγκατάσταση του Docker και, για να είμαστε ειλικρινείς, περιλαμβάνει λίγη δουλειά, οπότε το συνιστούμε μόνο σε όσους έχουν εμπειρία με containers.

Ένας από τους καλύτερους τρόπους να κρατήσετε τα API κλειδιά σας ασφαλή όταν χρησιμοποιείτε GitHub Codespaces είναι να χρησιμοποιήσετε τα Codespace Secrets. Παρακαλούμε ακολουθήστε τον [οδηγό διαχείρισης μυστικών για Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) για να μάθετε περισσότερα.

## Μαθήματα και Τεχνικές Απαιτήσεις

Το μάθημα περιλαμβάνει 6 ενότητες με θεωρία και 6 ενότητες με κώδικα.

Για τις ενότητες κώδικα, χρησιμοποιούμε την υπηρεσία Azure OpenAI. Θα χρειαστείτε πρόσβαση στην υπηρεσία Azure OpenAI και ένα API key για να εκτελέσετε αυτόν τον κώδικα. Μπορείτε να υποβάλετε αίτηση για πρόσβαση [συμπληρώνοντας αυτή την αίτηση](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Ενώ περιμένετε να επεξεργαστεί η αίτησή σας, κάθε ενότητα κώδικα περιέχει και ένα αρχείο `README.md` όπου μπορείτε να δείτε τον κώδικα και τα αποτελέσματα.

## Χρήση της υπηρεσίας Azure OpenAI για πρώτη φορά

Αν είναι η πρώτη φορά που δουλεύετε με την υπηρεσία Azure OpenAI, παρακαλούμε ακολουθήστε αυτόν τον οδηγό για το πώς να [δημιουργήσετε και αναπτύξετε μια Azure OpenAI Service εφαρμογή.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Χρήση της OpenAI API για πρώτη φορά

Αν είναι η πρώτη φορά που χρησιμοποιείτε το OpenAI API, παρακαλούμε ακολουθήστε τον οδηγό για το πώς να [δημιουργήσετε και χρησιμοποιήσετε το Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Γνωρίστε άλλους μαθητές

Έχουμε δημιουργήσει κανάλια στον επίσημο [Discord server της κοινότητας AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) για να συναντήσετε άλλους μαθητές. Αυτός είναι ένας εξαιρετικός τρόπος να δικτυωθείτε με άλλους ομοϊδεάτες επιχειρηματίες, δημιουργούς, φοιτητές και οποιονδήποτε θέλει να εξελιχθεί στη Δημιουργική Τεχνητή Νοημοσύνη.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Η ομάδα του έργου θα είναι επίσης παρούσα σε αυτόν τον Discord server για να βοηθά οποιουσδήποτε μαθητές.

## Συμβολή

Αυτό το μάθημα είναι μια πρωτοβουλία ανοιχτού κώδικα. Αν δείτε σημεία βελτίωσης ή προβλήματα, παρακαλούμε δημιουργήστε ένα [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ή καταχωρήστε ένα [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Η ομάδα του έργου παρακολουθεί όλες τις συνεισφορές. Η συμβολή σε έργα ανοιχτού κώδικα είναι ένας εκπληκτικός τρόπος να αναπτύξετε την καριέρα σας στη Δημιουργική Τεχνητή Νοημοσύνη.

Οι περισσότερες συνεισφορές απαιτούν να συμφωνήσετε με μια Συμφωνία Άδειας Συνεταιριστή (CLA) που δηλώνει ότι έχετε το δικαίωμα και ότι πράγματι παραχωρείτε σε εμάς τα δικαιώματα να χρησιμοποιήσουμε τη συνεισφορά σας. Για λεπτομέρειες, επισκεφτείτε [την ιστοσελίδα CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Σημαντικό: κατά τη μετάφραση κειμένου σε αυτό το αποθετήριο, παρακαλούμε να μην χρησιμοποιείτε μηχανική μετάφραση. Θα επικυρώνουμε τις μεταφράσεις μέσω της κοινότητας, οπότε παρακαλούμε να αναλαμβάνετε μεταφράσεις μόνο σε γλώσσες που γνωρίζετε καλά.

Όταν υποβάλλετε ένα pull request, ένας CLA-bot θα καθορίσει αυτόματα αν χρειάζεται να παράσχετε CLA και θα επισημάνει ανάλογα το PR (π.χ., με ετικέτα, σχόλιο). Απλώς ακολουθήστε τις οδηγίες που δίνει ο bot. Θα χρειαστεί να το κάνετε αυτό μόνο μία φορά σε όλα τα repositories που χρησιμοποιούν το CLA μας.

Αυτό το έργο έχει υιοθετήσει τον [Κώδικα Συμπεριφοράς Ανοιχτού Κώδικα της Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Για περισσότερες πληροφορίες, διαβάστε τις Συχνές Ερωτήσεις ή επικοινωνήστε με το [Email opencode](opencode@microsoft.com) για επιπλέον ερωτήσεις ή σχόλια.

## Ας ξεκινήσουμε!
Τώρα που έχετε ολοκληρώσει τα απαραίτητα βήματα για την ολοκλήρωση αυτού του μαθήματος, ας ξεκινήσουμε με μια [εισαγωγή στην Γενετική Τεχνητή Νοημοσύνη και τα LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθεια για ακρίβεια, παρακαλούμε να σημειώσετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η επίσημη πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για οποιεσδήποτε παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->