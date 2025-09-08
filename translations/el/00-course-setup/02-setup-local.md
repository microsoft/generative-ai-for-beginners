<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8a50125da1d2836fab30bb91c19def97",
  "translation_date": "2025-08-26T16:55:44+00:00",
  "source_file": "00-course-setup/02-setup-local.md",
  "language_code": "el"
}
-->
# Τοπική Εγκατάσταση 🖥️

**Ακολουθήστε αυτόν τον οδηγό αν προτιμάτε να τρέχετε τα πάντα στο δικό σας laptop.**  
Έχετε δύο επιλογές: **(A) native Python + virtual-env** ή **(B) VS Code Dev Container με Docker**.  
Διαλέξτε όποια σας βολεύει περισσότερο—και οι δύο οδηγούν στα ίδια μαθήματα.

## 1.  Προαπαιτούμενα

| Εργαλείο            | Έκδοση / Σημειώσεις                                                                  |
|---------------------|--------------------------------------------------------------------------------------|
| **Python**          | 3.10 + (κατεβάστε το από <https://python.org>)                                       |
| **Git**             | Τελευταία έκδοση (έρχεται με Xcode / Git for Windows / Linux package manager)         |
| **VS Code**         | Προαιρετικό αλλά προτείνεται <https://code.visualstudio.com>                         |
| **Docker Desktop**  | *Μόνο* για την Επιλογή B. Δωρεάν εγκατάσταση: <https://docs.docker.com/desktop/>     |

> 💡 **Tip** – Επαληθεύστε τα εργαλεία σε ένα τερματικό:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Επιλογή A – Native Python (πιο γρήγορη)

### Βήμα 1  Κλωνοποιήστε αυτό το repo

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Βήμα 2 Δημιουργήστε & ενεργοποιήστε ένα virtual environment

```bash
python -m venv .venv          # make one
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Το prompt τώρα πρέπει να ξεκινά με (.venv)—αυτό σημαίνει ότι είστε μέσα στο περιβάλλον.

### Βήμα 3 Εγκαταστήστε τις εξαρτήσεις

```bash
pip install -r requirements.txt
```

Προχωρήστε στην Ενότητα 3 για τα [API keys](../../../00-course-setup)

## 2. Επιλογή B – VS Code Dev Container (Docker)

Έχουμε ρυθμίσει αυτό το αποθετήριο και το μάθημα με ένα [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) που έχει ένα Universal runtime και υποστηρίζει Python3, .NET, Node.js και Java development. Η σχετική ρύθμιση βρίσκεται στο αρχείο `devcontainer.json` στον φάκελο `.devcontainer/` στη ρίζα του αποθετηρίου.

>**Γιατί να το επιλέξετε;**
>Ίδιο περιβάλλον με το Codespaces· καμία απόκλιση εξαρτήσεων.

### Βήμα 0 Εγκαταστήστε τα επιπλέον εργαλεία

Docker Desktop – επιβεβαιώστε ότι το ```docker --version``` λειτουργεί.
VS Code Remote – Containers extension (ID: ms-vscode-remote.remote-containers).

### Βήμα 1 Ανοίξτε το repo στο VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

Το VS Code ανιχνεύει το .devcontainer/ και εμφανίζει σχετικό μήνυμα.

### Βήμα 2 Ανοίξτε ξανά μέσα στο container

Πατήστε “Reopen in Container”. Το Docker χτίζει το image (≈ 3 λεπτά την πρώτη φορά).
Όταν εμφανιστεί το prompt στο τερματικό, είστε μέσα στο container.

## 2.  Επιλογή C – Miniconda

Το [Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) είναι ένας ελαφρύς εγκαταστάτης για το [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), την Python, και μερικά πακέτα.
Το Conda είναι ένας διαχειριστής πακέτων που διευκολύνει τη δημιουργία και εναλλαγή μεταξύ διαφορετικών [**εικονικών περιβαλλόντων**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) και πακέτων Python. Είναι επίσης χρήσιμο για την εγκατάσταση πακέτων που δεν υπάρχουν μέσω του `pip`.

### Βήμα 0  Εγκαταστήστε το Miniconda

Ακολουθήστε τον [οδηγό εγκατάστασης του MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) για να το ρυθμίσετε.

```bash
conda --version
```

### Βήμα 1 Δημιουργήστε ένα εικονικό περιβάλλον

Δημιουργήστε ένα νέο αρχείο περιβάλλοντος (*environment.yml*). Αν ακολουθείτε τα βήματα μέσω Codespaces, δημιουργήστε το μέσα στον φάκελο `.devcontainer`, δηλαδή `.devcontainer/environment.yml`.

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

Τρέξτε τις παρακάτω εντολές στο τερματικό/γραμμή εντολών

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # .devcontainer sub path applies to only Codespace setups
conda activate ai4beg
```

Δείτε τον [οδηγό για περιβάλλοντα Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) αν αντιμετωπίσετε προβλήματα.

## 2  Επιλογή D – Κλασικό Jupyter / Jupyter Lab (στον browser σας)

> **Για ποιον είναι αυτό;**  
> Για όσους προτιμούν το κλασικό περιβάλλον Jupyter ή θέλουν να τρέχουν notebooks χωρίς το VS Code.  

### Βήμα 1  Βεβαιωθείτε ότι το Jupyter είναι εγκατεστημένο

Για να ξεκινήσετε το Jupyter τοπικά, ανοίξτε το τερματικό/γραμμή εντολών, πλοηγηθείτε στον φάκελο του μαθήματος και εκτελέστε:

```bash
jupyter notebook
```

ή

```bash
jupyterhub
```

Αυτό θα ξεκινήσει μια συνεδρία Jupyter και το URL για πρόσβαση θα εμφανιστεί στο παράθυρο της γραμμής εντολών.

Μόλις μπείτε στο URL, θα δείτε τη δομή του μαθήματος και θα μπορείτε να πλοηγηθείτε σε οποιοδήποτε αρχείο `*.ipynb`. Για παράδειγμα, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Προσθέστε τα API Keys σας

Η ασφάλεια των API keys είναι σημαντική όταν φτιάχνετε οποιαδήποτε εφαρμογή. Προτείνουμε να μην αποθηκεύετε τα API keys απευθείας στον κώδικά σας. Αν τα ανεβάσετε σε δημόσιο αποθετήριο, μπορεί να προκύψουν θέματα ασφαλείας ή και ανεπιθύμητα κόστη αν τα χρησιμοποιήσει κάποιος κακόβουλος.
Δείτε πώς να δημιουργήσετε ένα αρχείο `.env` για Python και να προσθέσετε το `GITHUB_TOKEN`:

1. **Μεταβείτε στον φάκελο του project σας**: Ανοίξτε το τερματικό ή τη γραμμή εντολών και πλοηγηθείτε στον βασικό φάκελο του project όπου θέλετε να δημιουργήσετε το `.env` αρχείο.

   ```bash
   cd path/to/your/project
   ```

2. **Δημιουργήστε το αρχείο `.env`**: Χρησιμοποιήστε τον αγαπημένο σας editor για να δημιουργήσετε ένα νέο αρχείο με όνομα `.env`. Αν είστε στη γραμμή εντολών, μπορείτε να χρησιμοποιήσετε `touch` (σε Unix) ή `echo` (σε Windows):

   Unix-based συστήματα:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Επεξεργαστείτε το αρχείο `.env`**: Ανοίξτε το `.env` σε έναν editor (π.χ. VS Code, Notepad++ ή όποιον άλλο προτιμάτε). Προσθέστε την παρακάτω γραμμή, αντικαθιστώντας το `your_github_token_here` με το πραγματικό σας GitHub token:

   ```env
   GITHUB_TOKEN=your_github_token_here
   ```

4. **Αποθηκεύστε το αρχείο**: Αποθηκεύστε τις αλλαγές και κλείστε τον editor.

5. **Εγκαταστήστε το `python-dotenv`**: Αν δεν το έχετε ήδη, θα χρειαστεί να εγκαταστήσετε το πακέτο `python-dotenv` για να φορτώσετε τις μεταβλητές περιβάλλοντος από το `.env` στο Python app σας. Εγκαταστήστε το με `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Φορτώστε τις μεταβλητές περιβάλλοντος στο Python script σας**: Στο Python script σας, χρησιμοποιήστε το `python-dotenv` για να φορτώσετε τις μεταβλητές από το `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the GITHUB_TOKEN variable
   github_token = os.getenv("GITHUB_TOKEN")

   print(github_token)
   ```

Αυτό ήταν! Δημιουργήσατε το `.env`, προσθέσατε το GitHub token και το φορτώσατε στην Python εφαρμογή σας.

🔐 Μην κάνετε ποτέ commit το .env—είναι ήδη στο .gitignore.
Οδηγίες για όλους τους providers υπάρχουν στο [`providers.md`](03-providers.md).

## 4. Τι ακολουθεί;

| Θέλω να…            | Πήγαινε σε…                                                                |
|---------------------|----------------------------------------------------------------------------|
| Ξεκινήστε το Μάθημα 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)       |
| Ρύθμιση LLM Provider | [`providers.md`](03-providers.md)                                         |
| Γνωρίστε άλλους μαθητές | [Join our Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Επίλυση Προβλημάτων

| Σύμπτωμα                                   | Λύση                                                            |
|--------------------------------------------|-----------------------------------------------------------------|
| `python not found`                         | Προσθέστε το Python στο PATH ή ξανανοίξτε το τερματικό μετά την εγκατάσταση |
| `pip` δεν μπορεί να χτίσει wheels (Windows)| `pip install --upgrade pip setuptools wheel` και ξαναδοκιμάστε. |
| `ModuleNotFoundError: dotenv`              | Τρέξτε `pip install -r requirements.txt` (δεν εγκαταστάθηκε το env). |
| Docker build fails *No space left*         | Docker Desktop ▸ *Settings* ▸ *Resources* → αυξήστε το μέγεθος δίσκου. |
| Το VS Code ζητά συνέχεια να ανοίξει ξανά   | Ίσως έχετε ενεργές και τις δύο επιλογές· διαλέξτε μία (venv **ή** container)|
| OpenAI 401 / 429 errors                    | Ελέγξτε το `OPENAI_API_KEY` ή τα όρια αιτημάτων.                |
| Σφάλματα με Conda                          | Εγκαταστήστε τις βιβλιοθήκες AI της Microsoft με `conda install -c microsoft azure-ai-ml`|

---

**Αποποίηση Ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρότι καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρανοήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.