<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f1413b349a65b4e9eda3f48807656a6d",
  "translation_date": "2025-08-26T16:56:37+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "el"
}
-->
# Ξεκινώντας με αυτό το μάθημα

Είμαστε πολύ ενθουσιασμένοι που ξεκινάς αυτό το μάθημα και ανυπομονούμε να δούμε τι θα σε εμπνεύσει να δημιουργήσεις με τη Γενετική Τεχνητή Νοημοσύνη!

Για να εξασφαλίσουμε την επιτυχία σου, αυτή η σελίδα περιγράφει τα βήματα εγκατάστασης, τις τεχνικές απαιτήσεις και πού μπορείς να βρεις βοήθεια αν χρειαστεί.

## Βήματα Εγκατάστασης

Για να ξεκινήσεις το μάθημα, θα χρειαστεί να ολοκληρώσεις τα παρακάτω βήματα.

### 1. Κάνε Fork το Repo

[Κάνε fork σε αυτό το repo](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) στον δικό σου λογαριασμό στο GitHub ώστε να μπορείς να αλλάξεις τον κώδικα και να ολοκληρώσεις τις προκλήσεις. Μπορείς επίσης να [βάλεις αστέρι (🌟) στο repo](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars?WT.mc_id=academic-105485-koreyst) για να το βρίσκεις πιο εύκολα μαζί με σχετικά repos.

### 2. Δημιούργησε ένα codespace

Για να αποφύγεις προβλήματα με εξαρτήσεις όταν τρέχεις τον κώδικα, προτείνουμε να δουλέψεις το μάθημα σε ένα [GitHub Codespaces](https://github.com/features/codespaces?WT.mc_id=academic-105485-koreyst).

Στο fork σου: **Code -> Codespaces -> New on main**

![Διάλογος με κουμπιά για δημιουργία codespace](../../../00-course-setup/images/who-will-pay.webp)

#### 2.1 Πρόσθεσε ένα secret

1. ⚙️ Εικονίδιο γραναζιού -> Command Pallete-> Codespaces : Manage user secret -> Add a new secret.
2. Όνομα OPENAI_API_KEY, επικόλλησε το κλειδί σου, Αποθήκευση.

### 3.  Τι ακολουθεί;

| Θέλω να…            | Πήγαινε σε…                                                              |
|---------------------|-------------------------------------------------------------------------|
| Ξεκινήσω το Μάθημα 1| [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)     |
| Δουλέψω offline     | [`setup-local.md`](02-setup-local.md)                                   |
| Ρυθμίσω LLM Provider| [`providers.md`](providers.md)                                          |
| Γνωρίσω άλλους μαθητές| [Join our Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)   |

## Επίλυση Προβλημάτων

| Σύμπτωμα                                 | Λύση                                                            |
|------------------------------------------|-----------------------------------------------------------------|
| Το build του container κολλάει > 10 λεπτά| **Codespaces ➜ “Rebuild Container”**                            |
| `python: command not found`              | Το Terminal δεν συνδέθηκε· κάνε κλικ στο **+** ➜ *bash*          |
| `401 Unauthorized` από OpenAI            | Λάθος / ληγμένο `OPENAI_API_KEY`                                |
| VS Code δείχνει “Dev container mounting…”| Κάνε ανανέωση στο tab του browser—μερικές φορές χάνεται η σύνδεση|
| Λείπει το kernel στο Notebook            | Μενού Notebook ➜ **Kernel ▸ Select Kernel ▸ Python 3**           |

   Συστήματα Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Επεξεργασία του αρχείου `.env`**: Άνοιξε το αρχείο `.env` σε έναν text editor (π.χ. VS Code, Notepad++, ή όποιον άλλο editor). Πρόσθεσε την παρακάτω γραμμή, αντικαθιστώντας το `your_github_token_here` με το πραγματικό σου GitHub token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Αποθήκευσε το αρχείο**: Αποθήκευσε τις αλλαγές και κλείσε τον editor.

5. **Εγκατάσταση του `python-dotenv`**: Αν δεν το έχεις ήδη, θα χρειαστεί να εγκαταστήσεις το πακέτο `python-dotenv` για να φορτώσεις τις μεταβλητές περιβάλλοντος από το `.env` αρχείο στην Python εφαρμογή σου. Μπορείς να το εγκαταστήσεις με `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Φόρτωσε τις μεταβλητές περιβάλλοντος στο Python script σου**: Στο Python script σου, χρησιμοποίησε το πακέτο `python-dotenv` για να φορτώσεις τις μεταβλητές από το `.env` αρχείο:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Αυτό ήταν! Δημιούργησες με επιτυχία το αρχείο `.env`, πρόσθεσες το GitHub token σου και το φόρτωσες στην Python εφαρμογή σου.

## Πώς να τρέξεις τοπικά στον υπολογιστή σου

Για να τρέξεις τον κώδικα τοπικά στον υπολογιστή σου, θα χρειαστεί να έχεις κάποια έκδοση του [Python εγκατεστημένη](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

Για να χρησιμοποιήσεις το repository, πρέπει να το κάνεις clone:

```shell
git clone https://github.com/microsoft/generative-ai-for-beginners
cd generative-ai-for-beginners
```

Μόλις έχεις όλα έτοιμα, μπορείς να ξεκινήσεις!

## Προαιρετικά Βήματα

### Εγκατάσταση Miniconda

Το [Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) είναι ένας ελαφρύς installer για την εγκατάσταση του [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), της Python, και μερικών πακέτων.
Το Conda είναι ένας διαχειριστής πακέτων που διευκολύνει τη δημιουργία και εναλλαγή μεταξύ διαφορετικών [**εικονικών περιβαλλόντων**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) και πακέτων. Είναι επίσης χρήσιμο για την εγκατάσταση πακέτων που δεν υπάρχουν μέσω του `pip`.

Μπορείς να ακολουθήσεις τον [οδηγό εγκατάστασης του MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) για να το ρυθμίσεις.

Αφού εγκαταστήσεις το Miniconda, πρέπει να κάνεις clone το [repository](https://github.com/microsoft/generative-ai-for-beginners/fork?WT.mc_id=academic-105485-koreyst) (αν δεν το έχεις ήδη).

Στη συνέχεια, πρέπει να δημιουργήσεις ένα εικονικό περιβάλλον. Για να το κάνεις με το Conda, δημιούργησε ένα νέο αρχείο περιβάλλοντος (_environment.yml_). Αν δουλεύεις με Codespaces, δημιούργησέ το μέσα στον φάκελο `.devcontainer`, δηλαδή `.devcontainer/environment.yml`.

Γέμισε το αρχείο περιβάλλοντος με το παρακάτω snippet:

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

Αν συναντήσεις σφάλματα με το conda, μπορείς να εγκαταστήσεις χειροκίνητα τις Microsoft AI Libraries με την παρακάτω εντολή στο terminal.

```
conda install -c microsoft azure-ai-ml
```

Το αρχείο περιβάλλοντος ορίζει τις εξαρτήσεις που χρειαζόμαστε. Το `<environment-name>` είναι το όνομα που θέλεις να δώσεις στο Conda περιβάλλον σου, και το `<python-version>` είναι η έκδοση της Python που θέλεις να χρησιμοποιήσεις, π.χ. `3` είναι η τελευταία κύρια έκδοση.

Αφού το κάνεις αυτό, μπορείς να δημιουργήσεις το Conda περιβάλλον σου τρέχοντας τις παρακάτω εντολές στο command line/terminal

```bash
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Ανατρέξτε στον [οδηγό για περιβάλλοντα Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) αν αντιμετωπίσεις προβλήματα.

### Χρήση του Visual Studio Code με την επέκταση Python

Προτείνουμε να χρησιμοποιήσεις τον editor [Visual Studio Code (VS Code)](https://code.visualstudio.com/?WT.mc_id=academic-105485-koreyst) με την [επέκταση Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) εγκατεστημένη για αυτό το μάθημα. Αυτό είναι απλώς μια σύσταση και όχι απαίτηση.

> **Note**: Ανοίγοντας το repository του μαθήματος στο VS Code, έχεις τη δυνατότητα να ρυθμίσεις το project μέσα σε container. Αυτό γίνεται λόγω του [ειδικού φακέλου `.devcontainer`](https://code.visualstudio.com/docs/devcontainers/containers?itemName=ms-python.python&WT.mc_id=academic-105485-koreyst) που υπάρχει στο repository. Περισσότερα γι’ αυτό αργότερα.

> **Note**: Μόλις κάνεις clone και ανοίξεις τον φάκελο στο VS Code, θα σου προτείνει αυτόματα να εγκαταστήσεις την επέκταση Python.

> **Note**: Αν το VS Code σου προτείνει να ξανανοίξεις το repository σε container, αρνήσου για να χρησιμοποιήσεις την τοπικά εγκατεστημένη έκδοση της Python.

### Χρήση του Jupyter στον Browser

Μπορείς επίσης να δουλέψεις το project χρησιμοποιώντας το [περιβάλλον Jupyter](https://jupyter.org?WT.mc_id=academic-105485-koreyst) απευθείας στον browser σου. Τόσο το κλασικό Jupyter όσο και το [Jupyter Hub](https://jupyter.org/hub?WT.mc_id=academic-105485-koreyst) προσφέρουν ένα ευχάριστο περιβάλλον ανάπτυξης με δυνατότητες όπως αυτόματη συμπλήρωση, επισήμανση κώδικα κ.ά.

Για να ξεκινήσεις το Jupyter τοπικά, άνοιξε το terminal/command line, πήγαινε στον φάκελο του μαθήματος και εκτέλεσε:

```bash
jupyter notebook
```

ή

```bash
jupyterhub
```

Αυτό θα ξεκινήσει μια Jupyter instance και το URL για πρόσβαση θα εμφανιστεί στο παράθυρο της γραμμής εντολών.

Μόλις μπεις στο URL, θα δεις τη δομή του μαθήματος και θα μπορείς να πλοηγηθείς σε οποιοδήποτε αρχείο `*.ipynb`. Για παράδειγμα, `08-building-search-applications/python/oai-solution.ipynb`.

### Τρέξιμο σε container

Μια εναλλακτική στο να ρυθμίσεις τα πάντα στον υπολογιστή σου ή στο Codespace είναι να χρησιμοποιήσεις ένα [container](../../../00-course-setup/<https:/en.wikipedia.org/wiki/Containerization_(computing)?WT.mc_id=academic-105485-koreyst>). Ο ειδικός φάκελος `.devcontainer` στο repository του μαθήματος επιτρέπει στο VS Code να ρυθμίσει το project μέσα σε container. Εκτός Codespaces, αυτό απαιτεί εγκατάσταση του Docker και είναι λίγο πιο περίπλοκο, οπότε το προτείνουμε μόνο σε όσους έχουν εμπειρία με containers.

Ένας από τους καλύτερους τρόπους να κρατήσεις ασφαλή τα API keys σου όταν χρησιμοποιείς GitHub Codespaces είναι μέσω των Codespace Secrets. Ακολούθησε τον [οδηγό διαχείρισης secrets στο Codespaces](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-secrets-for-your-codespaces?WT.mc_id=academic-105485-koreyst) για να μάθεις περισσότερα.

## Μαθήματα και Τεχνικές Απαιτήσεις

Το μάθημα περιλαμβάνει 6 θεωρητικά μαθήματα και 6 μαθήματα με κώδικα.

Για τα μαθήματα με κώδικα, χρησιμοποιούμε το Azure OpenAI Service. Θα χρειαστείς πρόσβαση στην υπηρεσία Azure OpenAI και ένα API key για να τρέξεις τον κώδικα. Μπορείς να κάνεις αίτηση για πρόσβαση [συμπληρώνοντας αυτή την αίτηση](https://azure.microsoft.com/products/ai-services/openai-service?WT.mc_id=academic-105485-koreyst).

Όσο περιμένεις να εγκριθεί η αίτησή σου, κάθε μάθημα με κώδικα περιλαμβάνει και ένα αρχείο `README.md` όπου μπορείς να δεις τον κώδικα και τα αποτελέσματα.

## Πρώτη φορά με το Azure OpenAI Service

Αν είναι η πρώτη φορά που δουλεύεις με το Azure OpenAI service, ακολούθησε αυτόν τον οδηγό για το πώς να [δημιουργήσεις και να αναπτύξεις ένα Azure OpenAI Service resource.](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)

## Πρώτη φορά με το OpenAI API

Αν είναι η πρώτη φορά που δουλεύεις με το OpenAI API, ακολούθησε τον οδηγό για το πώς να [δημιουργήσεις και να χρησιμοποιήσεις το Interface.](https://platform.openai.com/docs/quickstart?context=pythont&WT.mc_id=academic-105485-koreyst)

## Γνώρισε άλλους μαθητές

Έχουμε δημιουργήσει κανάλια στον επίσημο [AI Community Discord server](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) για να γνωρίσεις άλλους μαθητές. Είναι ένας εξαιρετικός τρόπος να δικτυωθείς με άλλους επιχειρηματίες, δημιουργούς, φοιτητές και όσους θέλουν να εξελιχθούν στη Γενετική Τεχνητή Νοημοσύνη.

[![Join discord channel](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst)

Η ομάδα του project θα είναι επίσης σε αυτόν τον Discord server για να βοηθήσει τους μαθητές.

## Συνεισφορά

Αυτό το μάθημα είναι μια πρωτοβουλία ανοιχτού κώδικα. Αν δεις σημεία για βελτίωση ή προβλήματα, δημιούργησε ένα [Pull Request](https://github.com/microsoft/generative-ai-for-beginners/pulls?WT.mc_id=academic-105485-koreyst) ή ανέφερε ένα [GitHub issue](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

Η ομάδα του project θα παρακολουθεί όλες τις συνεισφορές. Η συνεισφορά σε ανοιχτό κώδικα είναι ένας εξαιρετικός τρόπος να χτίσεις την καριέρα σου στη Γενετική Τεχνητή Νοημοσύνη.

Οι περισσότερες συνεισφορές απαιτούν να συμφωνήσεις με μια Συμφωνία Άδειας Συνεισφέροντα (CLA), δηλώνοντας ότι έχεις το δικαίωμα και πράγματι μας παραχωρείς τα δικαιώματα να χρησιμοποιήσουμε τη συνεισφορά σου. Για λεπτομέρειες, επισκέψου το [site της CLA, Contributor License Agreement](https://cla.microsoft.com?WT.mc_id=academic-105485-koreyst).

Σημαντικό: όταν μεταφράζεις κείμενο σε αυτό το repo, βεβαιώσου ότι δεν χρησιμοποιείς αυτόματη μετάφραση. Θα ελέγξουμε τις μεταφράσεις μέσω της κοινότητας, οπότε παρακαλούμε να προσφέρεις εθελοντικά μόνο για γλώσσες στις οποίες είσαι άνετος.

Όταν υποβάλλεις pull request, ένα CLA-bot θα ελέγξει αυτόματα αν χρειάζεται να παρέχεις CLA και θα διακοσμήσει το PR κατάλληλα (π.χ. label, σχόλιο). Απλώς ακολούθησε τις οδηγίες του bot. Θα χρειαστεί να το κάνεις μόνο μία φορά για όλα τα repos που χρησιμοποιούν το CLA μας.

Αυτό το project ακολουθεί τον [Κώδικα Δεοντολογίας Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). Για περισσότερες πληροφορίες διάβασε το FAQ του Κώδικα Δεοντολογίας ή επικοινώνησε με [Email opencode](opencode@microsoft.com) για επιπλέον ερωτήσεις ή σχόλια.

## Ξεκινάμε!
Τώρα που ολοκληρώσατε τα απαραίτητα βήματα για να τελειώσετε αυτό το μάθημα, ας ξεκινήσουμε με μια [εισαγωγή στη Γενετική Τεχνητή Νοημοσύνη και τα LLMs](../01-introduction-to-genai/README.md?WT.mc_id=academic-105485-koreyst).

---

**Αποποίηση Ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρότι καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρανοήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.