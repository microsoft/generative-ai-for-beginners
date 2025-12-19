<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f5cf0b10ab3c485e6334101f5784f1f3",
  "translation_date": "2025-12-19T15:07:15+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "el"
}
-->
# Τοπική Ρύθμιση 🖥️

**Χρησιμοποιήστε αυτόν τον οδηγό αν προτιμάτε να τρέχετε τα πάντα στον δικό σας φορητό υπολογιστή.**  
Έχετε δύο επιλογές: **(A) εγγενές Python + virtual-env** ή **(B) VS Code Dev Container με Docker**.  
Επιλέξτε όποιο σας φαίνεται πιο εύκολο—και οι δύο οδηγούν στα ίδια μαθήματα.

## 1.  Προαπαιτούμενα

| Εργαλείο           | Έκδοση / Σημειώσεις                                                                 |
|--------------------|-------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (κατεβάστε το από <https://python.org>)                                      |
| **Git**            | Τελευταία (έρχεται με Xcode / Git για Windows / διαχειριστή πακέτων Linux)           |
| **VS Code**        | Προαιρετικό αλλά συνιστάται <https://code.visualstudio.com>                         |
| **Docker Desktop** | *Μόνο* για Επιλογή B. Δωρεάν εγκατάσταση: <https://docs.docker.com/desktop/>        |

> 💡 **Συμβουλή** – Επαληθεύστε τα εργαλεία σε τερματικό:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Επιλογή A – Εγγενές Python (το γρηγορότερο)

### Βήμα 1  Κλωνοποιήστε αυτό το αποθετήριο

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Βήμα 2 Δημιουργήστε & ενεργοποιήστε ένα εικονικό περιβάλλον

```bash
python -m venv .venv          # φτιάξε ένα
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Το prompt θα πρέπει τώρα να ξεκινά με (.venv)—που σημαίνει ότι βρίσκεστε μέσα στο περιβάλλον.

### Βήμα 3 Εγκαταστήστε τις εξαρτήσεις

```bash
pip install -r requirements.txt
```

Παραλείψτε στο Τμήμα 3 για [API keys](../../../00-course-setup)

## 2. Επιλογή B – VS Code Dev Container (Docker)

Ρυθμίζουμε αυτό το αποθετήριο και το μάθημα με ένα [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) που έχει ένα Universal runtime που υποστηρίζει Python3, .NET, Node.js και Java ανάπτυξη. Η σχετική διαμόρφωση ορίζεται στο αρχείο `devcontainer.json` που βρίσκεται στον φάκελο `.devcontainer/` στη ρίζα αυτού του αποθετηρίου.

>**Γιατί να το επιλέξετε;**  
>Ταυτόσημο περιβάλλον με τα Codespaces· χωρίς εκτροπή εξαρτήσεων.

### Βήμα 0 Εγκαταστήστε τα επιπλέον

Docker Desktop – επιβεβαιώστε ότι το ```docker --version``` λειτουργεί.  
Επέκταση VS Code Remote – Containers (ID: ms-vscode-remote.remote-containers).

### Βήμα 1 Ανοίξτε το αποθετήριο στο VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

Το VS Code ανιχνεύει το .devcontainer/ και εμφανίζει ένα prompt.

### Βήμα 2 Ξανανοίξτε μέσα στο container

Κάντε κλικ στο “Reopen in Container”. Το Docker χτίζει την εικόνα (≈ 3 λεπτά την πρώτη φορά).  
Όταν εμφανιστεί το prompt του τερματικού, βρίσκεστε μέσα στο container.

## 2.  Επιλογή C – Miniconda

[Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) είναι ένας ελαφρύς εγκαταστάτης για την εγκατάσταση του [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), Python, καθώς και μερικών πακέτων.  
Το Conda είναι ένας διαχειριστής πακέτων, που διευκολύνει τη ρύθμιση και την εναλλαγή μεταξύ διαφορετικών Python [**εικονικών περιβαλλόντων**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) και πακέτων. Είναι επίσης χρήσιμο για την εγκατάσταση πακέτων που δεν είναι διαθέσιμα μέσω `pip`.

### Βήμα 0  Εγκαταστήστε το Miniconda

Ακολουθήστε τον [οδηγό εγκατάστασης MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) για να το ρυθμίσετε.

```bash
conda --version
```

### Βήμα 1 Δημιουργήστε ένα εικονικό περιβάλλον

Δημιουργήστε ένα νέο αρχείο περιβάλλοντος (*environment.yml*). Αν ακολουθείτε με Codespaces, δημιουργήστε το μέσα στον φάκελο `.devcontainer`, δηλαδή `.devcontainer/environment.yml`.

### Βήμα 2  Συμπληρώστε το αρχείο περιβάλλοντος

Προσθέστε το παρακάτω απόσπασμα στο `environment.yml`

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

### Βήμα 3 Δημιουργήστε το Conda περιβάλλον σας

Τρέξτε τις παρακάτω εντολές στη γραμμή εντολών/τερματικό σας

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # Η υποδιαδρομή .devcontainer ισχύει μόνο για ρυθμίσεις Codespace
conda activate ai4beg
```

Ανατρέξτε στον [οδηγό περιβαλλόντων Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) αν αντιμετωπίσετε προβλήματα.

## 2  Επιλογή D – Κλασικό Jupyter / Jupyter Lab (στον browser σας)

> **Για ποιον είναι αυτό;**  
> Όποιον αγαπάει το κλασικό περιβάλλον Jupyter ή θέλει να τρέχει notebooks χωρίς VS Code.

### Βήμα 1  Βεβαιωθείτε ότι το Jupyter είναι εγκατεστημένο

Για να ξεκινήσετε το Jupyter τοπικά, ανοίξτε το τερματικό/γραμμή εντολών, πλοηγηθείτε στον φάκελο του μαθήματος και εκτελέστε:

```bash
jupyter notebook
```

ή

```bash
jupyterhub
```

Αυτό θα ξεκινήσει μια παρουσία Jupyter και το URL για πρόσβαση θα εμφανιστεί στο παράθυρο της γραμμής εντολών.

Μόλις αποκτήσετε πρόσβαση στο URL, θα δείτε το περίγραμμα του μαθήματος και θα μπορείτε να πλοηγηθείτε σε οποιοδήποτε αρχείο `*.ipynb`. Για παράδειγμα, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Προσθέστε τα API Keys σας

Η διατήρηση των API keys σας ασφαλών είναι σημαντική όταν δημιουργείτε οποιοδήποτε είδος εφαρμογής. Συνιστούμε να μην αποθηκεύετε κανένα API key απευθείας στον κώδικά σας. Η αποθήκευση αυτών των στοιχείων σε δημόσιο αποθετήριο μπορεί να προκαλέσει ζητήματα ασφαλείας και ακόμη και ανεπιθύμητα κόστη αν χρησιμοποιηθούν από κακόβουλο χρήστη.  
Ακολουθεί ένας βήμα-βήμα οδηγός για το πώς να δημιουργήσετε ένα αρχείο `.env` για Python και να προσθέσετε το `GITHUB_TOKEN`:

1. **Πλοηγηθείτε στον φάκελο του έργου σας**: Ανοίξτε το τερματικό ή τη γραμμή εντολών και πλοηγηθείτε στον ριζικό φάκελο του έργου σας όπου θέλετε να δημιουργήσετε το αρχείο `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Δημιουργήστε το αρχείο `.env`**: Χρησιμοποιήστε τον αγαπημένο σας επεξεργαστή κειμένου για να δημιουργήσετε ένα νέο αρχείο με όνομα `.env`. Αν χρησιμοποιείτε τη γραμμή εντολών, μπορείτε να χρησιμοποιήσετε `touch` (σε συστήματα Unix) ή `echo` (στα Windows):

   Συστήματα Unix:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Επεξεργαστείτε το αρχείο `.env`**: Ανοίξτε το `.env` σε έναν επεξεργαστή κειμένου (π.χ. VS Code, Notepad++, ή οποιονδήποτε άλλο). Προσθέστε την παρακάτω γραμμή στο αρχείο, αντικαθιστώντας το `your_github_token_here` με το πραγματικό σας GitHub token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Αποθηκεύστε το αρχείο**: Αποθηκεύστε τις αλλαγές και κλείστε τον επεξεργαστή κειμένου.

5. **Εγκαταστήστε το `python-dotenv`**: Αν δεν το έχετε ήδη, θα χρειαστεί να εγκαταστήσετε το πακέτο `python-dotenv` για να φορτώνετε μεταβλητές περιβάλλοντος από το αρχείο `.env` στην Python εφαρμογή σας. Μπορείτε να το εγκαταστήσετε με `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Φορτώστε τις μεταβλητές περιβάλλοντος στο Python script σας**: Στο Python script σας, χρησιμοποιήστε το πακέτο `python-dotenv` για να φορτώσετε τις μεταβλητές περιβάλλοντος από το αρχείο `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Φόρτωση μεταβλητών περιβάλλοντος από το αρχείο .env
   load_dotenv()

   # Πρόσβαση στη μεταβλητή GITHUB_TOKEN
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Αυτό ήταν! Δημιουργήσατε με επιτυχία ένα αρχείο `.env`, προσθέσατε το GitHub token σας και το φορτώσατε στην Python εφαρμογή σας.

🔐 Μην κάνετε ποτέ commit το .env—είναι ήδη στο .gitignore.  
Ο πλήρης οδηγός παρόχων βρίσκεται στο [`providers.md`](03-providers.md).

## 4. Τι ακολουθεί;

| Θέλω να…           | Πηγαίνω σε…                                                             |
|---------------------|------------------------------------------------------------------------|
| Ξεκινήσω το Μάθημα 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)    |
| Ρυθμίσω έναν πάροχο LLM | [`providers.md`](03-providers.md)                                    |
| Γνωρίσω άλλους μαθητές | [Join our Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Επίλυση Προβλημάτων

| Σύμπτωμα                                  | Διόρθωση                                                        |
|-------------------------------------------|----------------------------------------------------------------|
| `python not found`                        | Προσθέστε το Python στο PATH ή ξανανοίξτε το τερματικό μετά την εγκατάσταση |
| `pip` δεν μπορεί να φτιάξει wheels (Windows) | `pip install --upgrade pip setuptools wheel` και δοκιμάστε ξανά. |
| `ModuleNotFoundError: dotenv`             | Τρέξτε `pip install -r requirements.txt` (δεν εγκαταστάθηκε το env). |
| Αποτυχία Docker build *No space left*    | Docker Desktop ▸ *Settings* ▸ *Resources* → αυξήστε το μέγεθος δίσκου. |
| Το VS Code συνεχίζει να ζητάει επανεκκίνηση | Μπορεί να έχετε ενεργές και τις δύο Επιλογές· επιλέξτε μία (venv **ή** container) |
| Σφάλματα OpenAI 401 / 429                  | Ελέγξτε την τιμή `OPENAI_API_KEY` / όρια ρυθμού αιτήσεων.       |
| Σφάλματα με Conda                         | Εγκαταστήστε τις βιβλιοθήκες Microsoft AI με `conda install -c microsoft azure-ai-ml` |

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να λάβετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->