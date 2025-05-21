<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f4785899ee92500f524b4acb26e3bb3",
  "translation_date": "2025-05-19T12:26:15+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "el"
}
-->
# Ξεκινώντας με αυτό το μάθημα

Είμαστε πολύ ενθουσιασμένοι που ξεκινάτε αυτό το μάθημα και ανυπομονούμε να δούμε τι θα εμπνευστείτε να δημιουργήσετε με την Γεννητική Τεχνητή Νοημοσύνη!

Για να διασφαλίσουμε την επιτυχία σας, αυτή η σελίδα περιγράφει τα βήματα εγκατάστασης, τις τεχνικές απαιτήσεις και πού να βρείτε βοήθεια εάν χρειαστεί.

## Βήματα Εγκατάστασης

Για να ξεκινήσετε αυτό το μάθημα, θα χρειαστεί να ολοκληρώσετε τα παρακάτω βήματα.

### 1. Κλωνοποιήστε αυτό το Αποθετήριο

[Κλωνοποιήστε ολόκληρο το αποθετήριο](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) στον δικό σας λογαριασμό GitHub για να μπορείτε να αλλάξετε οποιοδήποτε κώδικα και να ολοκληρώσετε τις προκλήσεις. Μπορείτε επίσης να [προσθέσετε αστέρι (🌟) σε αυτό το αποθετήριο](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) για να το βρίσκετε πιο εύκολα και να ανακαλύπτετε σχετικά αποθετήρια.

### 2. Δημιουργήστε έναν χώρο κώδικα

Για να αποφύγετε τυχόν προβλήματα εξαρτήσεων κατά την εκτέλεση του κώδικα, προτείνουμε να εκτελέσετε αυτό το μάθημα σε έναν [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Αυτό μπορεί να δημιουργηθεί επιλέγοντας την επιλογή `Code` στην κλωνοποιημένη έκδοση αυτού του αποθετηρίου και επιλέγοντας την επιλογή **Codespaces**.

![Διάλογος που δείχνει κουμπιά για τη δημιουργία ενός χώρου κώδικα](../../../00-course-setup/images/who-will-pay.webp)

### 3. Αποθήκευση των API Κλειδιών σας

Η διατήρηση των API κλειδιών σας ασφαλή και προστατευμένα είναι σημαντική όταν δημιουργείτε οποιοδήποτε είδος εφαρμογής. Προτείνουμε να μην αποθηκεύετε κανένα API κλειδί απευθείας στον κώδικά σας. Η δέσμευση αυτών των λεπτομερειών σε ένα δημόσιο αποθετήριο μπορεί να οδηγήσει σε ζητήματα ασφαλείας και ακόμη και ανεπιθύμητα κόστη αν χρησιμοποιηθούν από κακόβουλους χρήστες.
Ακολουθεί ένας οδηγός βήμα προς βήμα για το πώς να δημιουργήσετε ένα αρχείο `.env` για την Python και να προσθέσετε το `GITHUB_TOKEN`:

1. **Πλοηγηθείτε στον Κατάλογο του Έργου σας**: Ανοίξτε το τερματικό ή τη γραμμή εντολών και πλοηγηθείτε στον ριζικό κατάλογο του έργου σας όπου θέλετε να δημιουργήσετε το αρχείο `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Δημιουργήστε το Αρχείο `.env`**: Χρησιμοποιήστε τον αγαπημένο σας επεξεργαστή κειμένου για να δημιουργήσετε ένα νέο αρχείο με το όνομα `.env`. Αν χρησιμοποιείτε τη γραμμή εντολών, μπορείτε να χρησιμοποιήσετε `touch` (on Unix-based systems) or `echo` (στα Windows):

   Συστήματα βασισμένα σε Unix:
   ```bash
   touch .env
   ```

   Windows:
   ```cmd
   echo . > .env
   ```

3. **Επεξεργαστείτε το Αρχείο `.env`**: Ανοίξτε το αρχείο `.env` σε έναν επεξεργαστή κειμένου (π.χ., VS Code, Notepad++ ή οποιονδήποτε άλλο επεξεργαστή). Προσθέστε την παρακάτω γραμμή στο αρχείο, αντικαθιστώντας το `your_github_token_here` με το πραγματικό σας GitHub token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Αποθηκεύστε το Αρχείο**: Αποθηκεύστε τις αλλαγές και κλείστε τον επεξεργαστή κειμένου.

5. **Εγκαταστήστε το πακέτο `python-dotenv`**: If you haven't already, you'll need to install the `python-dotenv` για να φορτώσετε τις μεταβλητές περιβάλλοντος από το αρχείο `.env` στην εφαρμογή σας Python. Μπορείτε να το εγκαταστήσετε χρησιμοποιώντας το `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Φορτώστε τις Μεταβλητές Περιβάλλοντος στο Σενάριο Python σας**: Στο σενάριο Python σας, χρησιμοποιήστε το πακέτο `python-dotenv` για να φορτώσετε τις μεταβλητές περιβάλλοντος από το αρχείο `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Αυτό ήταν! Έχετε δημιουργήσει επιτυχώς ένα αρχείο `.env`, προσθέσατε το GitHub token σας και το φορτώσατε στην εφαρμογή σας Python.

## Πώς να Τρέξετε τοπικά στον υπολογιστή σας

Για να εκτελέσετε τον κώδικα τοπικά στον υπολογιστή σας, θα χρειαστεί να έχετε κάποια έκδοση του [Python εγκατεστημένη](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Για να χρησιμοποιήσετε το αποθετήριο, πρέπει να το κλωνοποιήσετε:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Μόλις έχετε όλα τα αρχεία, μπορείτε να ξεκινήσετε!

## Προαιρετικά Βήματα

### Εγκατάσταση του Miniconda

Το [Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) είναι ένας ελαφρύς εγκαταστάτης για την εγκατάσταση του [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), του Python, καθώς και μερικών πακέτων.
Το Conda είναι ένας διαχειριστής πακέτων, που καθιστά εύκολη την εγκατάσταση και την εναλλαγή μεταξύ διαφορετικών [**εικονικών περιβαλλόντων**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) Python και πακέτων. Επίσης, είναι χρήσιμο για την εγκατάσταση πακέτων που δεν είναι διαθέσιμα μέσω του `pip`.

You can follow the [MiniConda installation guide](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) to set it up.

With Miniconda installed, you need to clone the [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (if you haven't already)

Next, you need to create a virtual environment. To do this with Conda, go ahead and create a new environment file (_environment.yml_). If you are following along using Codespaces, create this within the `.devcontainer` directory, thus `.devcontainer/environment.yml`.

Προχωρήστε και γεμίστε το αρχείο περιβάλλοντος σας με το παρακάτω απόσπασμα:

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

Αν αντιμετωπίσετε σφάλματα χρησιμοποιώντας το conda, μπορείτε να εγκαταστήσετε χειροκίνητα τις Βιβλιοθήκες AI της Microsoft χρησιμοποιώντας την ακόλουθη εντολή σε ένα τερματικό.

```
conda install -c microsoft azure-ai-ml
```

Το αρχείο περιβάλλοντος καθορίζει τις εξαρτήσεις που χρειαζόμαστε. `<environment-name>` refers to the name you would like to use for your Conda environment, and `<python-version>` is the version of Python you would like to use, for example, `3` είναι η τελευταία κύρια έκδοση του Python.

Με αυτό ολοκληρωμένο, μπορείτε να προχωρήσετε και να δημιουργήσετε το περιβάλλον Conda σας εκτελώντας τις παρακάτω εντολές στη γραμμή εντολών/τερματικό σας

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Ανατρέξτε στον [οδηγό περιβαλλόντων Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) αν αντιμετωπίσετε προβλήματα.

### Χρήση του Visual Studio Code με την επέκταση υποστήριξης Python

Συνιστούμε να χρησιμοποιήσετε τον επεξεργαστή [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) με την εγκατεστημένη την [επέκταση υποστήριξης Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) για αυτό το μάθημα. Ωστόσο, αυτή είναι περισσότερο μια σύσταση και όχι απαραίτητη προϋπόθεση.

> **Σημείωση**: Ανοίγοντας το αποθετήριο του μαθήματος στο VS Code, έχετε την επιλογή να ρυθμίσετε το έργο μέσα σε ένα κοντέινερ. Αυτό οφείλεται στον [ειδικό κατάλογο `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) που βρίσκεται μέσα στο αποθετήριο του μαθήματος. Περισσότερα για αυτό αργότερα.

> **Σημείωση**: Μόλις κλωνοποιήσετε και ανοίξετε τον κατάλογο στο VS Code, θα σας προτείνει αυτόματα να εγκαταστήσετε μια επέκταση υποστήριξης Python.

> **Σημείωση**: Αν το VS Code σας προτείνει να ξανανοίξετε το αποθετήριο σε ένα κοντέινερ, αρνηθείτε αυτή την πρόταση για να χρησιμοποιήσετε την τοπικά εγκατεστημένη έκδοση του Python.

### Χρήση του Jupyter στο Πρόγραμμα Περιήγησης

Μπορείτε επίσης να εργαστείτε στο έργο χρησιμοποιώντας το περιβάλλον [Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) απευθείας στο πρόγραμμα περιήγησής σας. Τόσο το κλασικό Jupyter όσο και το [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) προσφέρουν ένα ευχάριστο περιβάλλον ανάπτυξης με λειτουργίες όπως αυτόματη συμπλήρωση, επισήμανση κώδικα κ.λπ.

Για να ξεκινήσετε το Jupyter τοπικά, πηγαίνετε στο τερματικό/γραμμή εντολών, πλοηγηθείτε στον κατάλογο του μαθήματος και εκτελέστε:

```bash
jupyter notebook
```

ή

```bash
jupyterhub
```

Αυτό θα ξεκινήσει μια παρουσία του Jupyter και η διεύθυνση URL για πρόσβαση σε αυτήν θα εμφανιστεί μέσα στο παράθυρο της γραμμής εντολών.

Μόλις αποκτήσετε πρόσβαση στη διεύθυνση URL, θα πρέπει να δείτε τη δομή του μαθήματος και να μπορείτε να πλοηγηθείτε σε οποιοδήποτε αρχείο `*.ipynb` file. For example, `08-building-search-applications/python/oai-solution.ipynb`.

### Running in a container

An alternative to setting everything up on your computer or Codespace is to use a [container](https://en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst). The special `.devcontainer` folder within the course repository makes it possible for VS Code to set up the project within a container. Outside of Codespaces, this will require the installation of Docker, and quite frankly, it involves a bit of work, so we recommend this only to those with experience working with containers.

One of the best ways to keep your API keys secure when using GitHub Codespaces is by using Codespace Secrets. Please follow the [Codespaces secrets management](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) guide to learn more about this.

## Lessons and Technical Requirements

The course has 6 concept lessons and 6 coding lessons.

For the coding lessons, we are using the Azure OpenAI Service. You will need access to the Azure OpenAI service and an API key to run this code. You can apply to get access by [completing this application](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

While you wait for your application to be processed, each coding lesson also includes a `README.md` όπου μπορείτε να δείτε τον κώδικα και τα αποτελέσματα.

## Χρήση της Υπηρεσίας Azure OpenAI για πρώτη φορά

Αν είναι η πρώτη φορά που εργάζεστε με την υπηρεσία Azure OpenAI, ακολουθήστε αυτόν τον οδηγό για το πώς να [δημιουργήσετε και να αναπτύξετε έναν πόρο Υπηρεσίας Azure OpenAI.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Χρήση του API OpenAI για πρώτη φορά

Αν είναι η πρώτη φορά που εργάζεστε με το API OpenAI, ακολουθήστε τον οδηγό για το πώς να [δημιουργήσετε και να χρησιμοποιήσετε τη Διεπαφή.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Γνωρίστε Άλλους Μαθητές

Έχουμε δημιουργήσει κανάλια στον επίσημο [διακομιστή AI Community Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) για να γνωρίσετε άλλους μαθητές. Αυτός είναι ένας εξαιρετικός τρόπος για να δικτυωθείτε με άλλους επιχειρηματίες, δημιουργούς, φοιτητές και οποιονδήποτε θέλει να αναβαθμίσει τις δεξιότητές του στη Γεννητική Τεχνητή Νοημοσύνη.

[![Συμμετοχή στο κανάλι discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Η ομάδα του έργου θα βρίσκεται επίσης σε αυτόν τον διακομιστή Discord για να βοηθήσει οποιονδήποτε μαθητή.

## Συνεισφορά

Αυτό το μάθημα είναι μια πρωτοβουλία ανοιχτού κώδικα. Αν δείτε περιοχές για βελτίωση ή προβλήματα, παρακαλώ δημιουργήστε ένα [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ή καταγράψτε ένα [θέμα στο GitHub](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Η ομάδα του έργου θα παρακολουθεί όλες τις συνεισφορές. Η συνεισφορά σε ανοιχτό κώδικα είναι ένας εκπληκτικός τρόπος να χτίσετε την καριέρα σας στη Γεννητική Τεχνητή Νοημοσύνη.

Οι περισσότερες συνεισφορές απαιτούν από εσάς να συμφωνήσετε με μια Συμφωνία Άδειας Χρήσης Συνεισφέροντος (CLA) δηλώνοντας ότι έχετε το δικαίωμα και πραγματικά παραχωρείτε σε εμάς τα δικαιώματα να χρησιμοποιήσουμε τη συνεισφορά σας. Για λεπτομέρειες, επισκεφτείτε τον [ιστότοπο CLA, Συμφωνία Άδειας Χρήσης Συνεισφέροντος](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Σημαντικό: κατά τη μετάφραση κειμένου σε αυτό το αποθετήριο, παρακαλώ διασφαλίστε ότι δεν χρησιμοποιείτε μηχανική μετάφραση. Θα επαληθεύσουμε τις μεταφράσεις μέσω της κοινότητας, οπότε παρακαλώ εθελονθείτε για μεταφράσεις μόνο σε γλώσσες στις οποίες είστε επαρκείς.

Όταν υποβάλετε ένα αίτημα έλξης, ένα CLA-bot θα καθορίσει αυτόματα αν χρειάζεται να παρέχετε μια CLA και θα διακοσμήσει το PR αναλόγως (π.χ., ετικέτα, σχόλιο). Απλώς ακολουθήστε τις οδηγίες που παρέχει το bot. Θα χρειαστεί να το κάνετε αυτό μόνο μία φορά σε όλα τα αποθετήρια που χρησιμοποιούν τη CLA μας.

Αυτό το έργο έχει υιοθετήσει τον [Κώδικα Δεοντολογίας Ανοιχτού Κώδικα της Microsoft](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Για περισσότερες πληροφορίες διαβάστε το FAQ του Κώδικα Δεοντολογίας ή επικοινωνήστε με το [Email opencode](opencode@microsoft.com) για οποιεσδήποτε επιπλέον ερωτήσεις ή σχόλια.

## Ας Ξεκινήσουμε

Τώρα που ολοκληρώσατε τα απαραίτητα βήματα για να ολοκληρώσετε αυτό το μάθημα, ας ξεκινήσουμε με μια [εισαγωγή στη Γεννητική Τεχνητή Νοημοσύνη και τα LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που προσπαθούμε για την ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το αρχικό έγγραφο στη γλώσσα του θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρανοήσεις ή παρερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.