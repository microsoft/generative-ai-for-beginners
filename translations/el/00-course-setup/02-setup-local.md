# Τοπική Ρύθμιση 🖥️

**Χρησιμοποιήστε αυτόν τον οδηγό αν προτιμάτε να τρέχετε τα πάντα στον δικό σας φορητό υπολογιστή.**   
Έχετε δύο επιλογές: **(A) εγγενές Python + virtual-env** ή **(B) VS Code Dev Container με Docker**.  
Επιλέξτε αυτό που σας φαίνεται πιο εύκολο—και οι δύο οδηγούν στα ίδια μαθήματα.

## 1.  Προαπαιτούμενα

| Εργαλείο           | Έκδοση / Σημειώσεις                                                                |
|--------------------|------------------------------------------------------------------------------------|
| **Python**         | 3.10 + (κατεβάστε το από <https://python.org>)                                     |
| **Git**            | Τελευταία έκδοση (έρχεται με Xcode / Git για Windows / διαχειριστή πακέτων Linux)   |
| **VS Code**        | Προαιρετικό αλλά συνιστάται <https://code.visualstudio.com>                         |
| **Docker Desktop** | *Μόνο* για Επιλογή B. Δωρεάν εγκατάσταση: <https://docs.docker.com/desktop/>        |

> 💡 **Συμβουλή** – Ελέγξτε τα εργαλεία σε ένα τερματικό:  
> `python --version`, `git --version`, `docker --version`, `code --version`  

## 2.  Επιλογή A – Εγγενές Python (γρηγορότερο)

### Βήμα 1  Κλωνοποιήστε αυτό το αποθετήριο

```bash
git clone https://github.com/<your-github>/generative-ai-for-beginners
cd generative-ai-for-beginners
```

### Βήμα 2 Δημιουργία & ενεργοποίηση ενός εικονικού περιβάλλοντος

```bash
python -m venv .venv          # κάνε ένα
source .venv/bin/activate     # macOS / Linux
.\.venv\Scripts\activate      # Windows PowerShell
```

✅ Η εντολή τώρα πρέπει να ξεκινά με (.venv)—που σημαίνει ότι είστε μέσα στο περιβάλλον.

### Βήμα 3 Εγκατάσταση εξαρτήσεων

```bash
pip install -r requirements.txt
```

Παραλείψτε στο Τμήμα 3 σχετικά με τα [API keys](#3-προσθέστε-τα-api-keys-σας)

## 2. Επιλογή B – VS Code Dev Container (Docker)

Ρυθμίσαμε αυτό το αποθετήριο και το μάθημα με ένα [development container](https://containers.dev?WT.mc_id=academic-105485-koreyst) που έχει ένα Universal runtime που υποστηρίζει Python3, .NET, Node.js και ανάπτυξη Java. Η σχετική διαμόρφωση ορίζεται στο αρχείο `devcontainer.json` που βρίσκεται στο φάκελο `.devcontainer/` στη ρίζα αυτού του αποθετηρίου.

>**Γιατί να το επιλέξετε;**
>Ταυτόσημο περιβάλλον με Codespaces· χωρίς εκτροχιασμό εξαρτήσεων.

### Βήμα 0 Εγκαταστήστε τα επιπλέον

Docker Desktop – επιβεβαιώστε ότι ```docker --version``` λειτουργεί.
Επέκταση VS Code Remote – Containers (ID: ms-vscode-remote.remote-containers).

### Βήμα 1 Ανοίξτε το αποθετήριο στο VS Code

File ▸ Open Folder…  → generative-ai-for-beginners

Το VS Code ανιχνεύει το .devcontainer/ και εμφανίζει ένα prompt.

### Βήμα 2 Ανοίξτε ξανά μέσα στο container

Κάντε κλικ στο “Reopen in Container”. Το Docker κατασκευάζει το image (≈ 3 λεπτά την πρώτη φορά).
Όταν εμφανιστεί η γραμμή εντολών, είστε μέσα στο container.

## 2.  Επιλογή C – Miniconda

Το [Miniconda](https://conda.io/en/latest/miniconda.html?WT.mc_id=academic-105485-koreyst) είναι ένας ελαφρύς εγκαταστάτης για την εγκατάσταση του [Conda](https://docs.conda.io/en/latest?WT.mc_id=academic-105485-koreyst), του Python, καθώς και ορισμένων πακέτων.
Το Conda είναι ένας διαχειριστής πακέτων, που καθιστά εύκολη τη ρύθμιση και τη μετάβαση μεταξύ διαφορετικών Python [**εικονικών περιβαλλόντων**](https://docs.python.org/3/tutorial/venv.html?WT.mc_id=academic-105485-koreyst) και πακέτων. Είναι επίσης χρήσιμο για την εγκατάσταση πακέτων που δεν είναι διαθέσιμα μέσω `pip`.

### Βήμα 0  Εγκατάσταση Miniconda

Ακολουθήστε τον [οδηγό εγκατάστασης MiniConda](https://docs.anaconda.com/free/miniconda/#quick-command-line-install?WT.mc_id=academic-105485-koreyst) για να το ρυθμίσετε.

```bash
conda --version
```

### Βήμα 1 Δημιουργία εικονικού περιβάλλοντος

Δημιουργήστε ένα νέο αρχείο περιβάλλοντος (*environment.yml*). Αν ακολουθείτε χρησιμοποιώντας Codespaces, δημιουργήστε το μέσα στον κατάλογο `.devcontainer`, δηλαδή `.devcontainer/environment.yml`.

### Βήμα 2  Γεμίστε το αρχείο περιβάλλοντος σας

Προσθέστε το ακόλουθο απόσπασμα στο `environment.yml`

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

### Βήμα 3 Δημιουργία του περιβάλλοντος Conda σας

Εκτελέστε τις εντολές παρακάτω στη γραμμή εντολών/τερματικό σας

```bash 
conda env create --name ai4beg --file .devcontainer/environment.yml # Η υποδιαδρομή .devcontainer εφαρμόζεται μόνο σε ρυθμίσεις Codespace
conda activate ai4beg
```

Ανατρέξτε στον [οδηγό περιβαλλόντων Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html?WT.mc_id=academic-105485-koreyst) αν αντιμετωπίσετε προβλήματα.

## 2  Επιλογή D – Κλασικό Jupyter / Jupyter Lab (στον περιηγητή σας)

> **Για ποιον είναι αυτό;**  
> Όποιον αγαπά το κλασικό περιβάλλον Jupyter ή θέλει να τρέξει σημειωματάρια χωρίς το VS Code.  

### Βήμα 1  Βεβαιωθείτε ότι έχετε εγκαταστήσει το Jupyter

Για να ξεκινήσετε το Jupyter τοπικά, ανοίξτε το τερματικό/γραμμή εντολών, μεταβείτε στον κατάλογο του μαθήματος και εκτελέστε:

```bash
jupyter notebook
```

ή

```bash
jupyterhub
```

Αυτό θα ξεκινήσει μια παρουσία Jupyter και η διεύθυνση URL για πρόσβαση θα εμφανιστεί στο παράθυρο της γραμμής εντολών.

Μόλις ανοίξετε τη διεύθυνση URL, θα δείτε το περίγραμμα του μαθήματος και θα μπορείτε να πλοηγηθείτε σε οποιοδήποτε αρχείο `*.ipynb`. Για παράδειγμα, `08-building-search-applications/python/oai-solution.ipynb`.

## 3. Προσθέστε τα API Keys σας

Η διασφάλιση της ασφάλειας των API keys σας είναι σημαντική όταν δημιουργείτε οποιοδήποτε τύπο εφαρμογής. Συνιστούμε να μην αποθηκεύετε καθόλου τα API keys άμεσα στον κώδικά σας. Η αποστολή αυτών των στοιχείων σε δημόσιο αποθετήριο μπορεί να προκαλέσει προβλήματα ασφάλειας και ακόμα ανεπιθύμητα έξοδα αν τα χρησιμοποιήσει κάποιος κακόβουλος.
Ακολουθεί ένας βήμα προς βήμα οδηγός για το πώς να δημιουργήσετε ένα αρχείο `.env` για Python και να προσθέσετε τα διαπιστευτήρια Microsoft Foundry Models:

> **Σημείωση:** Τα GitHub Models (και η μεταβλητή `GITHUB_TOKEN`) παύουν να λειτουργούν στο τέλος Ιουλίου 2026. Αυτός ο οδηγός χρησιμοποιεί αντί αυτού τα [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Προτιμάτε να εργάζεστε εντελώς offline; Δείτε [Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst).

1. **Μεταβείτε στον Κατάλογο του Έργου σας**: Ανοίξτε το τερματικό ή τη γραμμή εντολών και μεταβείτε στη ρίζα του έργου σας όπου θέλετε να δημιουργήσετε το αρχείο `.env`.

   ```bash
   cd path/to/your/project
   ```

2. **Δημιουργήστε το Αρχείο `.env`**: Χρησιμοποιήστε τον αγαπημένο σας επεξεργαστή κειμένου για να δημιουργήσετε ένα νέο αρχείο με όνομα `.env`. Αν χρησιμοποιείτε τη γραμμή εντολών, μπορείτε να χρησιμοποιήσετε `touch` (σε Unix-based συστήματα) ή `echo` (στα Windows):

   Unix-based συστήματα:

   ```bash
   touch .env
   ```

   Windows:

   ```cmd
   echo . > .env
   ```

3. **Επεξεργαστείτε το Αρχείο `.env`**: Ανοίξτε το αρχείο `.env` σε έναν επεξεργαστή κειμένου (π.χ., VS Code, Notepad++ ή οποιονδήποτε άλλο επεξεργαστή). Προσθέστε τις ακόλουθες γραμμές στο αρχείο, αντικαθιστώντας τους δείκτες θέσης με το πραγματικό endpoint του έργου Microsoft Foundry και το API key σας:

   ```env
   AZURE_INFERENCE_ENDPOINT=your_foundry_endpoint_here
   AZURE_INFERENCE_CREDENTIAL=your_foundry_api_key_here
   ```

4. **Αποθηκεύστε το Αρχείο**: Αποθηκεύστε τις αλλαγές και κλείστε τον επεξεργαστή κειμένου.

5. **Εγκαταστήστε το `python-dotenv`**: Αν δεν το έχετε ήδη, θα χρειαστεί να εγκαταστήσετε το πακέτο `python-dotenv` για να φορτώνετε τις μεταβλητές περιβάλλοντος από το αρχείο `.env` στην Python εφαρμογή σας. Μπορείτε να το εγκαταστήσετε με `pip`:

   ```bash
   pip install python-dotenv
   ```

6. **Φορτώστε τις Μεταβλητές Περιβάλλοντος στο Python Script σας**: Στο Python script σας, χρησιμοποιήστε το πακέτο `python-dotenv` για να φορτώσετε τις μεταβλητές περιβάλλοντος από το αρχείο `.env`:

   ```python
   from dotenv import load_dotenv
   import os

   # Φορτώστε τις μεταβλητές περιβάλλοντος από το αρχείο .env
   load_dotenv()

   # Πρόσβαση στις μεταβλητές Microsoft Foundry Models
   endpoint = os.getenv("AZURE_INFERENCE_ENDPOINT")
   token = os.getenv("AZURE_INFERENCE_CREDENTIAL")

   print(endpoint)
   ```

Αυτό ήταν! Δημιουργήσατε με επιτυχία ένα αρχείο `.env`, προσθέσατε τα διαπιστευτήρια Microsoft Foundry Models και τα φορτώσατε στην Python εφαρμογή σας.

🔐 Μην κάνετε ποτέ commit το .env—είναι ήδη στο .gitignore.
Αναλυτικές οδηγίες παρέχονται στο [`providers.md`](03-providers.md).

## 4. Τι ακολουθεί;

| Θέλω να…         | Μεταβείτε στο…                                                         |
|-------------------|-----------------------------------------------------------------------|
| Ξεκινήσω το Μάθημα 1 | [`01-introduction-to-genai`](../01-introduction-to-genai/README.md)  |
| Ρυθμίσω έναν πάροχο LLM | [`providers.md`](03-providers.md)                                    |
| Γνωρίσω άλλους μαθητές | [Join our Discord](https://aka.ms/genai-discord?WT.mc_id=academic-105485-koreyst) |

## 5. Επίλυση Προβλημάτων

| Σύμπτωμα                                  | Επίλυση                                                       |
|--------------------------------------------|-----------------------------------------------------------------|
| `python not found`                         | Προσθέστε το Python στο PATH ή ανοίξτε ξανά το τερματικό μετά την εγκατάσταση |
| `pip` δεν μπορεί να κατασκευάσει wheels (Windows) | `pip install --upgrade pip setuptools wheel` και δοκιμάστε ξανά.   |
| `ModuleNotFoundError: dotenv`              | Εκτελέστε `pip install -r requirements.txt` (το env δεν εγκαταστάθηκε). |
| Η κατασκευή Docker αποτυγχάνει *No space left* | Docker Desktop ▸ *Settings* ▸ *Resources* → αυξήστε το μέγεθος δίσκου. |
| Το VS Code συνεχώς ζητά να ανοίξετε ξανά | Μπορεί να έχετε ενεργές και τις δύο επιλογές· επιλέξτε μία (venv **ή** container) |
| Σφάλματα OpenAI 401 / 429                 | Ελέγξτε την τιμή του `OPENAI_API_KEY` / όρια αιτήσεων.         |
| Σφάλματα κατά τη χρήση Conda               | Εγκαταστήστε τις βιβλιοθήκες Microsoft AI με `conda install -c microsoft azure-ai-ml`|

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->