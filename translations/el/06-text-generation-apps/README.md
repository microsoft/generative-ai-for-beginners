# Κατασκευή Εφαρμογών Δημιουργίας Κειμένου

[![Κατασκευή Εφαρμογών Δημιουργίας Κειμένου](../../../translated_images/el/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Κάντε κλικ στην εικόνα παραπάνω για να δείτε το βίντεο αυτού του μαθήματος)_

Μέχρι τώρα μέσα από αυτό το πρόγραμμα σπουδών έχετε δει ότι υπάρχουν βασικές έννοιες όπως οι προτροπές και ακόμη ένα ολόκληρο γνωστικό πεδίο που ονομάζεται "μηχανική προτροπών". Πολλά εργαλεία με τα οποία μπορείτε να αλληλεπιδράσετε όπως το ChatGPT, το Office 365, το Microsoft Power Platform και άλλα, σας υποστηρίζουν χρησιμοποιώντας προτροπές για να επιτύχετε κάτι.

Για να προσθέσετε μια τέτοια εμπειρία σε μια εφαρμογή, χρειάζεται να κατανοήσετε έννοιες όπως οι προτροπές, οι συμπληρώσεις και να επιλέξετε μια βιβλιοθήκη για να εργαστείτε. Αυτό ακριβώς θα μάθετε σε αυτό το κεφάλαιο.

## Εισαγωγή

Σε αυτό το κεφάλαιο θα:

- Μάθετε για τη βιβλιοθήκη openai και τις βασικές της έννοιες.
- Κατασκευάσετε μια εφαρμογή δημιουργίας κειμένου χρησιμοποιώντας το openai.
- Κατανοήσετε πώς να χρησιμοποιείτε έννοιες όπως προτροπή, θερμοκρασία και τοκέν για να κατασκευάσετε μια εφαρμογή δημιουργίας κειμένου.

## Στόχοι μάθησης

Στο τέλος αυτού του μαθήματος, θα μπορείτε να:

- Εξηγήσετε τι είναι μια εφαρμογή δημιουργίας κειμένου.
- Κατασκευάσετε μια εφαρμογή δημιουργίας κειμένου χρησιμοποιώντας το openai.
- Διαμορφώσετε την εφαρμογή σας ώστε να χρησιμοποιεί περισσότερα ή λιγότερα τοκέν και επίσης να αλλάξετε τη θερμοκρασία, για ποικιλία στο αποτέλεσμα.

## Τι είναι μια εφαρμογή δημιουργίας κειμένου;

Κανονικά, όταν κατασκευάζετε μια εφαρμογή έχει κάποιο είδος διεπαφής όπως η ακόλουθη:

- Βασισμένη σε εντολές. Οι εφαρμογές κονσόλας είναι τυπικές εφαρμογές όπου πληκτρολογείτε μια εντολή και εκτελείται μια εργασία. Για παράδειγμα, `git` είναι μια εφαρμογή βασισμένη σε εντολές.
- Διεπαφή χρήστη (UI). Ορισμένες εφαρμογές έχουν γραφικές διεπαφές χρήστη (GUIs) όπου κάνετε κλικ σε κουμπιά, εισάγετε κείμενο, επιλέγετε επιλογές και άλλα.

### Οι εφαρμογές κονσόλας και UI έχουν περιορισμούς

Συγκρίνετέ το με μια εφαρμογή βασισμένη σε εντολές όπου πληκτρολογείτε μια εντολή:

- **Είναι περιορισμένη**. Δεν μπορείτε απλά να πληκτρολογήσετε οποιαδήποτε εντολή, μόνο τις εντολές που υποστηρίζει η εφαρμογή.
- **Ειδική γλώσσα**. Ορισμένες εφαρμογές υποστηρίζουν πολλές γλώσσες, αλλά από προεπιλογή η εφαρμογή είναι κατασκευασμένη για μια συγκεκριμένη γλώσσα, ακόμα κι αν μπορείτε να προσθέσετε επιπλέον γλωσσική υποστήριξη.

### Οφέλη των εφαρμογών δημιουργίας κειμένου

Τι διαφορά έχει μια εφαρμογή δημιουργίας κειμένου;

Σε μια εφαρμογή δημιουργίας κειμένου έχετε περισσότερη ευελιξία, δεν είστε περιορισμένοι σε ένα σύνολο εντολών ή σε μια συγκεκριμένη γλώσσα εισόδου. Αντίθετα, μπορείτε να χρησιμοποιήσετε φυσική γλώσσα για να αλληλεπιδράσετε με την εφαρμογή. Ένα ακόμη όφελος είναι ότι ήδη αλληλεπιδράτε με μια πηγή δεδομένων που έχει εκπαιδευτεί σε ένα τεράστιο σώμα πληροφοριών, ενώ μια παραδοσιακή εφαρμογή μπορεί να περιορίζεται σε αυτά που περιέχονται σε μια βάση δεδομένων.

### Τι μπορώ να κατασκευάσω με μια εφαρμογή δημιουργίας κειμένου;

Μπορείτε να κατασκευάσετε πολλά πράγματα. Για παράδειγμα:

- **Μια chatbot**. Ένα chatbot που απαντά σε ερωτήσεις για θέματα, όπως η εταιρεία σας και τα προϊόντα της, θα μπορούσε να είναι μια καλή επιλογή.
- **Βοηθό**. Τα LLMs είναι εξαιρετικά σε πράγματα όπως η σύνοψη κειμένου, η λήψη πληροφοριών από κείμενο, η παραγωγή κειμένου όπως βιογραφικά και άλλα.
- **Βοηθό κώδικα**. Αναλόγως του γλωσσικού μοντέλου που χρησιμοποιείτε, μπορείτε να κατασκευάσετε έναν βοηθό κώδικα που σας βοηθά να γράφετε κώδικα. Για παράδειγμα, μπορείτε να χρησιμοποιήσετε ένα προϊόν όπως το GitHub Copilot καθώς και το ChatGPT για να σας βοηθήσουν να γράψετε κώδικα.

## Πώς μπορώ να ξεκινήσω;

Λοιπόν, χρειάζεται να βρείτε έναν τρόπο να ενσωματωθείτε με ένα LLM το οποίο συνήθως περιλαμβάνει τις ακόλουθες δύο προσεγγίσεις:

- Χρήση API. Εδώ κατασκευάζετε αιτήματα web με την προτροπή σας και λαμβάνετε πίσω το παραγόμενο κείμενο.
- Χρήση βιβλιοθήκης. Οι βιβλιοθήκες βοηθούν να είναι πιο εύκολη η χρήση των κλήσεων API.

## Βιβλιοθήκες/SDKs

Υπάρχουν μερικές γνωστές βιβλιοθήκες για την εργασία με LLMs όπως:

- **openai**, αυτή η βιβλιοθήκη διευκολύνει τη σύνδεση με το μοντέλο σας και την αποστολή προτροπών.

Έπειτα υπάρχουν βιβλιοθήκες που λειτουργούν σε υψηλότερο επίπεδο όπως:

- **Langchain**. Το Langchain είναι γνωστό και υποστηρίζει Python.
- **Semantic Kernel**. Το Semantic Kernel είναι μια βιβλιοθήκη της Microsoft που υποστηρίζει τις γλώσσες C#, Python, και Java.

## Πρώτη εφαρμογή χρησιμοποιώντας το openai

Ας δούμε πώς μπορούμε να κατασκευάσουμε την πρώτη μας εφαρμογή, ποιες βιβλιοθήκες χρειαζόμαστε, πόσο απαιτείται και τα λοιπά.

### Εγκατάσταση openai

Υπάρχουν πολλές βιβλιοθήκες εκεί έξω για αλληλεπίδραση με το OpenAI ή το Azure OpenAI. Είναι δυνατό να χρησιμοποιηθούν πολλές γλώσσες προγραμματισμού όπως C#, Python, JavaScript, Java και άλλες. Επιλέξαμε να χρησιμοποιήσουμε τη βιβλιοθήκη Python `openai`, οπότε θα χρησιμοποιήσουμε `pip` για να την εγκαταστήσουμε.

```bash
pip install openai
```

### Δημιουργία πόρου

Πρέπει να εκτελέσετε τα εξής βήματα:

- Δημιουργήστε έναν λογαριασμό στο Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Αποκτήστε πρόσβαση στο Azure OpenAI. Μεταβείτε στο [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) και ζητήστε πρόσβαση.

  > [!NOTE]
  > Κατά τη στιγμή της συγγραφής, χρειάζεται να κάνετε αίτηση για πρόσβαση στο Azure OpenAI.

- Εγκαταστήστε το Python <https://www.python.org/>
- Έχετε δημιουργήσει έναν πόρο Azure OpenAI Service. Δείτε αυτόν τον οδηγό για το πώς να [δημιουργήσετε ένα πόρο](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Εύρεση κλειδιού API και endpoint

Σε αυτό το σημείο χρειάζεται να πείτε στη βιβλιοθήκη `openai` ποιο κλειδί API να χρησιμοποιήσει. Για να βρείτε το κλειδί API σας, πηγαίνετε στην ενότητα "Κλειδιά και Endpoint" του πόρου Azure OpenAI και αντιγράψτε την τιμή "Κλειδί 1".

![Ενότητα κλειδιών και endpoint στο Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Τώρα που έχετε αντιγράψει αυτές τις πληροφορίες, ας δώσουμε οδηγίες στις βιβλιοθήκες να τις χρησιμοποιήσουν.

> [!NOTE]
> Αξίζει να απομονώσετε το κλειδί API από τον κώδικά σας. Μπορείτε να το κάνετε χρησιμοποιώντας μεταβλητές περιβάλλοντος.
>
> - Ορίστε τη μεταβλητή περιβάλλοντος `OPENAI_API_KEY` στο κλειδί API σας.
>   `export OPENAI_API_KEY='sk-...'`

### Ρύθμιση παραμέτρων Azure

Αν χρησιμοποιείτε το Azure OpenAI (που τώρα είναι μέρος του Microsoft Foundry), ιδού πώς ρυθμίζετε τις παραμέτρους. Χρησιμοποιούμε τον στάνταρ `OpenAI` client που δείχνει στο Azure OpenAI `/openai/v1/` endpoint, ο οποίος συνεργάζεται με το Responses API και δεν χρειάζεται `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Πάνω ορίζουμε τα εξής:

- `api_key`, αυτό είναι το κλειδί API σας που βρέθηκε στο Azure Portal ή στο Microsoft Foundry portal.
- `base_url`, αυτό είναι το endpoint του Foundry πόρου σας με `/openai/v1/` προσαρτημένο. Το σταθερό endpoint v1 λειτουργεί και στο OpenAI και στο Azure OpenAI χωρίς διαχείριση `api_version`.

> [!NOTE] > `os.environ` διαβάζει μεταβλητές περιβάλλοντος. Μπορείτε να το χρησιμοποιήσετε για να διαβάσετε μεταβλητές περιβάλλοντος όπως `AZURE_OPENAI_API_KEY` και `AZURE_OPENAI_ENDPOINT`. Ορίστε αυτές τις μεταβλητές περιβάλλοντος στο τερματικό σας ή χρησιμοποιώντας μια βιβλιοθήκη όπως `dotenv`.

## Παραγωγή κειμένου

Ο τρόπος για να παράγετε κείμενο είναι να χρησιμοποιήσετε το Responses API μέσω της μεθόδου `responses.create`. Ιδού ένα παράδειγμα:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

Στον παραπάνω κώδικα, δημιουργούμε μια απόκριση και περνάμε το μοντέλο που θέλουμε να χρησιμοποιήσουμε και την προτροπή. Έπειτα εκτυπώνουμε το παραγόμενο κείμενο μέσω του `response.output_text`.

### Συζητήσεις πολλαπλών βημάτων

Το Responses API είναι κατάλληλο για τόσο απλή παραγωγή κειμένου μίας πρότασης όσο και για chatbot πολλαπλών βημάτων - παρέχετε μια λίστα μηνυμάτων στο `input` για να συναρμολογήσετε μια συνομιλία:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Περισσότερα για αυτή τη λειτουργία σε ένα επερχόμενο κεφάλαιο.

## Άσκηση - η πρώτη σας εφαρμογή δημιουργίας κειμένου

Τώρα που μάθαμε πώς να ρυθμίσουμε και να διαμορφώσουμε το openai, είναι ώρα να κατασκευάσετε την πρώτη σας εφαρμογή δημιουργίας κειμένου. Για να κατασκευάσετε την εφαρμογή σας, ακολουθήστε τα εξής βήματα:

1. Δημιουργήστε ένα εικονικό περιβάλλον και εγκαταστήστε το openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Αν χρησιμοποιείτε Windows, πληκτρολογήστε `venv\Scripts\activate` αντί για `source venv/bin/activate`.

   > [!NOTE]
   > Εντοπίστε το κλειδί Azure OpenAI πηγαίνοντας στο [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), αναζητήστε `Open AI`, επιλέξτε το `Open AI resource` και έπειτα επιλέξτε `Keys and Endpoint` και αντιγράψτε την τιμή `Key 1`.

1. Δημιουργήστε ένα αρχείο _app.py_ και δώστε του τον ακόλουθο κώδικα:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"

   # make a request using the Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # print response
   print(response.output_text)
   ```

   > [!NOTE]
   > Αν χρησιμοποιείτε την απλή OpenAI (όχι Azure), χρησιμοποιήστε `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (χωρίς `base_url`) και περάστε ένα όνομα μοντέλου όπως `gpt-5-mini` αντί για όνομα ανάπτυξης.

   Θα δείτε μια έξοδο όπως η παρακάτω:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Διαφορετικοί τύποι προτροπών, για διαφορετικά πράγματα

Τώρα που είδατε πώς να δημιουργείτε κείμενο χρησιμοποιώντας μια προτροπή. Έχετε ακόμη ένα πρόγραμμα σε λειτουργία που μπορείτε να τροποποιήσετε και να αλλάξετε για να δημιουργήσετε διαφορετικούς τύπους κειμένου.

Οι προτροπές μπορούν να χρησιμοποιηθούν για κάθε είδους εργασίες. Για παράδειγμα:

- **Δημιουργία κάποιου τύπου κειμένου**. Για παράδειγμα, μπορείτε να δημιουργήσετε ένα ποίημα, ερωτήσεις για ένα κουίζ κλπ.
- **Εύρεση πληροφοριών**. Μπορείτε να χρησιμοποιήσετε προτροπές για να αναζητήσετε πληροφορίες όπως το εξής παράδειγμα 'Τι σημαίνει το CORS στην ανάπτυξη ιστοσελίδων;'.
- **Δημιουργία κώδικα**. Μπορείτε να χρησιμοποιήσετε προτροπές για να δημιουργήσετε κώδικα, για παράδειγμα να αναπτύξετε μια κανονική έκφραση που χρησιμοποιείται για την επικύρωση e-mail ή γιατί όχι να δημιουργήσετε ολόκληρη εφαρμογή, όπως μια web app;

## Μια πιο πρακτική περίπτωση χρήσης: ένας γεννήτορας συνταγών

Φανταστείτε ότι έχετε υλικά στο σπίτι και θέλετε να μαγειρέψετε κάτι. Για αυτό χρειάζεστε μια συνταγή. Ένας τρόπος να βρείτε συνταγές είναι να χρησιμοποιήσετε μια μηχανή αναζήτησης ή να χρησιμοποιήσετε ένα LLM για αυτό.

Μπορείτε να γράψετε μια προτροπή όπως:

> "Δείξε μου 5 συνταγές για ένα πιάτο με τα ακόλουθα υλικά: κοτόπουλο, πατάτες και καρότα. Για κάθε συνταγή, απαριθμήστε όλα τα χρησιμοποιούμενα υλικά."

Με δεδομένη την παραπάνω προτροπή, μπορεί να λάβετε μια απάντηση παρόμοια με:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 2 cloves garlic, minced
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
```

Αυτό το αποτέλεσμα είναι εξαιρετικό, ξέρω τι να μαγειρέψω. Σε αυτό το σημείο, χρήσιμες βελτιώσεις θα μπορούσαν να είναι:

- Φιλτράρισμα υλικών που δεν μου αρέσουν ή στα οποία έχω αλλεργία.
- Παραγωγή λίστας αγορών, σε περίπτωση που δεν έχω όλα τα υλικά στο σπίτι.

Για τις παραπάνω περιπτώσεις, ας προσθέσουμε μια επιπλέον προτροπή:

> "Παρακαλώ αφαιρέστε τις συνταγές με σκόρδο καθώς είμαι αλλεργικός και αντικαταστήστε το με κάτι άλλο. Επίσης, παρακαλώ δημιουργήστε μια λίστα αγορών για τις συνταγές, λαμβάνοντας υπόψη ότι ήδη έχω κοτόπουλο, πατάτες και καρότα στο σπίτι."

Τώρα έχετε ένα νέο αποτέλεσμα, συγκεκριμένα:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano

Shopping List:
- Olive oil
- Onion
- Thyme
- Oregano
- Salt
- Pepper
```

Αυτές είναι οι πέντε συνταγές σας, χωρίς καμία αναφορά σε σκόρδο και έχετε επίσης μια λίστα αγορών λαμβάνοντας υπόψη αυτά που ήδη έχετε στο σπίτι.

## Άσκηση - δημιουργία γεννήτορα συνταγών

Τώρα που έχουμε παίξει ένα σενάριο, ας γράψουμε κώδικα που αντιστοιχεί στο παρουσιασμένο σενάριο. Για να το κάνετε αυτό, ακολουθήστε τα βήματα:

1. Χρησιμοποιήστε το υπάρχον αρχείο _app.py_ ως σημείο εκκίνησης
1. Εντοπίστε τη μεταβλητή `prompt` και αλλάξτε τον κώδικα της ως εξής:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Αν τώρα εκτελέσετε τον κώδικα, θα πρέπει να δείτε μια έξοδο παρόμοια με:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > ΣΗΜΕΙΩΣΗ, το LLM σας δεν είναι καθοριστικό, οπότε μπορεί να λάβετε διαφορετικά αποτελέσματα κάθε φορά που τρέχετε το πρόγραμμα.

   Τέλεια, ας δούμε πώς μπορούμε να βελτιώσουμε τα πράγματα. Για να τα βελτιώσουμε, θέλουμε να βεβαιωθούμε ότι ο κώδικας είναι ευέλικτος, ώστε να μπορούν να αλλάζουν και να βελτιώνονται τα υλικά και ο αριθμός των συνταγών.

1. Ας αλλάξουμε τον κώδικα ως εξής:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Η εκτέλεση του κώδικα για δοκιμή μπορεί να μοιάζει με αυτό:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Βελτίωση με προσθήκη φίλτρου και λίστας αγορών

Τώρα έχουμε μια λειτουργική εφαρμογή ικανή να παράγει συνταγές και είναι ευέλικτη καθώς βασίζεται σε εισόδους από τον χρήστη, τόσο στον αριθμό των συνταγών όσο και στα χρησιμοποιούμενα υλικά.

Για να την βελτιώσουμε περαιτέρω, θέλουμε να προσθέσουμε τα εξής:

- **Φιλτράρισμα υλικών**. Θέλουμε να μπορούμε να φιλτράρουμε τα υλικά που δεν μας αρέσουν ή στα οποία έχουμε αλλεργία. Για να επιτύχουμε αυτή την αλλαγή, μπορούμε να επεξεργαστούμε την υπάρχουσα προτροπή μας και να προσθέσουμε στο τέλος μια συνθήκη φίλτρου ως εξής:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Πάνω, προσθέτουμε `{filter}` στο τέλος της προτροπής και επίσης λαμβάνουμε την τιμή του φίλτρου από τον χρήστη.

  Ένα παράδειγμα εισόδου κατά την εκτέλεση του προγράμματος μπορεί τώρα να μοιάζει ως εξής:

  ```output
  No of recipes (for example, 5): 3
  List of ingredients (for example, chicken, potatoes, and carrots): onion,milk
  Filter (for example, vegetarian, vegan, or gluten-free): no milk

  1. French Onion Soup

  Ingredients:

  -1 large onion, sliced
  -3 cups beef broth
  -1 cup milk
  -6 slices french bread
  -1/4 cup shredded Parmesan cheese
  -1 tablespoon butter
  -1 teaspoon dried thyme
  -1/4 teaspoon salt
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add beef broth, milk, thyme, salt, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Place french bread slices on soup bowls.
  5. Ladle soup over bread.
  6. Sprinkle with Parmesan cheese.

  2. Onion and Potato Soup

  Ingredients:

  -1 large onion, chopped
  -2 cups potatoes, diced
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add potatoes, vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Serve hot.

  3. Creamy Onion Soup

  Ingredients:

  -1 large onion, chopped
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper
  -1/4 cup all-purpose flour
  -1/2 cup shredded Parmesan cheese

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. In a small bowl, whisk together flour and Parmesan cheese until smooth.
  5. Add to soup and simmer for an additional 5 minutes, or until soup has thickened.
  ```

  Όπως βλέπετε, όλες οι συνταγές που περιέχουν γάλα έχουν φιλτραριστεί. Αλλά, αν είστε δυσανεκτικός στη λακτόζη, ίσως θέλετε να φιλτράρετε και τις συνταγές με τυρί, οπότε χρειάζεται να είστε σαφείς.

- **Παραγωγή λίστας αγορών**. Θέλουμε να παράγουμε λίστα αγορών, λαμβάνοντας υπόψη αυτά που ήδη έχουμε στο σπίτι.

  Για αυτή τη λειτουργικότητα, μπορούμε είτε να προσπαθήσουμε να λύσουμε τα πάντα σε μια προτροπή είτε να τη χωρίσουμε σε δύο προτροπές. Ας δοκιμάσουμε τη δεύτερη προσέγγιση. Εδώ προτείνουμε να προσθέσουμε μια επιπλέον προτροπή, αλλά για να λειτουργήσει αυτό, πρέπει να προσθέσουμε το αποτέλεσμα της πρώτης προτροπής ως πλαίσιο στη δεύτερη προτροπή.

  Εντοπίστε το μέρος του κώδικα που εκτυπώνει το αποτέλεσμα της πρώτης προτροπής και προσθέστε τον ακόλουθο κώδικα από κάτω:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Σημειώστε τα εξής:

  1. Δημιουργούμε μια νέα προτροπή προσθέτοντας το αποτέλεσμα από την πρώτη προτροπή στη νέα προτροπή:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Κάνουμε νέο αίτημα, λαμβάνοντας υπόψη και τον αριθμό τοκέν που ζητήσαμε στην πρώτη προτροπή, οπότε αυτή τη φορά λέμε ότι `max_output_tokens` είναι 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Εκτελώντας αυτόν τον κώδικα φτάνουμε τώρα στο παρακάτω αποτέλεσμα:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Βελτιώστε τη ρύθμισή σας

Αυτό που έχουμε μέχρι στιγμής είναι κώδικας που λειτουργεί, αλλά υπάρχουν κάποιες βελτιώσεις που θα πρέπει να κάνουμε για να το βελτιώσουμε περαιτέρω. Κάποια πράγματα που θα πρέπει να κάνουμε είναι:

- **Διαχωρίστε τα μυστικά από τον κώδικα**, όπως το API key. Τα μυστικά δεν ανήκουν στον κώδικα και θα πρέπει να αποθηκεύονται σε ασφαλή θέση. Για να διαχωρίσουμε τα μυστικά από τον κώδικα, μπορούμε να χρησιμοποιήσουμε μεταβλητές περιβάλλοντος και βιβλιοθήκες όπως `python-dotenv` για να τα φορτώσουμε από ένα αρχείο. Δείτε πώς θα φαίνεται αυτό στον κώδικα:

  1. Δημιουργήστε ένα αρχείο `.env` με το ακόλουθο περιεχόμενο:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Σημείωση, για το Azure OpenAI στο Microsoft Foundry, χρειάζεται να ορίσετε τις παρακάτω μεταβλητές περιβάλλοντος αντί γι' αυτές:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Στον κώδικα, θα φορτώσετε τις μεταβλητές περιβάλλοντος ως εξής:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Μια λέξη για το μήκος των token**. Πρέπει να σκεφτούμε πόσα tokens χρειάζονται για να παραχθεί το κείμενο που θέλουμε. Τα tokens κοστίζουν χρήματα, οπότε όπου είναι δυνατόν, θα πρέπει να προσπαθούμε να είμαστε οικονομικοί με τον αριθμό των token που χρησιμοποιούμε. Για παράδειγμα, μπορούμε να διατυπώσουμε το prompt ώστε να χρησιμοποιούμε λιγότερα tokens;

  Για να αλλάξετε τα tokens που χρησιμοποιούνται, μπορείτε να χρησιμοποιήσετε την παράμετρο `max_output_tokens`. Για παράδειγμα, αν θέλετε να χρησιμοποιήσετε 100 tokens, θα κάνετε:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Πειραματισμός με τη θερμοκρασία**. Η θερμοκρασία είναι κάτι που δεν έχουμε αναφέρει μέχρι τώρα αλλά είναι ένα σημαντικό πλαίσιο για το πώς λειτουργεί το πρόγραμμά μας. Όσο μεγαλύτερη είναι η τιμή της θερμοκρασίας, τόσο πιο τυχαίο θα είναι το αποτέλεσμα. Αντίθετα, όσο χαμηλότερη είναι η τιμή, τόσο πιο προβλέψιμο θα είναι το αποτέλεσμα. Σκεφτείτε αν θέλετε ποικιλία στην έξοδο σας ή όχι.

  Για να αλλάξετε τη θερμοκρασία, μπορείτε να χρησιμοποιήσετε την παράμετρο `temperature`. Για παράδειγμα, αν θέλετε να χρησιμοποιήσετε θερμοκρασία 0.5, θα κάνετε:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Σημείωση, όσο πιο κοντά στο 1.0, τόσο πιο ποικίλη είναι η έξοδος.

- **Τα μοντέλα συλλογισμού δεν χρησιμοποιούν `temperature`**. Αυτή είναι μια σημαντική αλλαγή για το 2026. Τα τρέχοντα, μη αποσυρμένα μοντέλα στο Microsoft Foundry είναι **μοντέλα συλλογισμού** (η οικογένεια GPT-5, σειρά o) - και δεν υποστηρίζουν `temperature` ή `top_p` (ούτε `max_tokens`, χρησιμοποιήστε `max_output_tokens`). Αν στείλετε `temperature` στο `gpt-5-mini` θα λάβετε σφάλμα "parameter not supported". Έτσι, για να δοκιμάσετε το παράδειγμα της θερμοκρασίας παραπάνω, χρησιμοποιήστε ένα μοντέλο που εξακολουθεί να υποστηρίζει ελέγχους δειγματοληψίας - για παράδειγμα ένα ανοιχτό **Llama** μοντέλο όπως `Llama-3.3-70B-Instruct` από το [κατάλογο μοντέλων Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), που καλείται μέσω του Foundry Models / Azure AI Inference endpoint (με τον ίδιο τρόπο που καλούνται τα `githubmodels-*` δείγματα). Για μοντέλα συλλογισμού όπως το GPT-5, η κατεύθυνση της εξόδου γίνεται διαφορετικά:
  - **Prompt engineering** - σαφείς οδηγίες, παραδείγματα και δομημένη έξοδος (δείτε το μάθημα [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) κάνουν τη δουλειά που παλιότερα έκαναν οι διακόπτες δειγματοληψίας.
  - **Έλεγχοι συλλογισμού** - παράμετροι όπως η προσπάθεια συλλογισμού/εκτενής απάντηση ανταλλάσσουν το βάθος συλλογισμού με την καθυστέρηση και το κόστος.

  Εν συντομία: `temperature`/`top_p` είναι ακόμα έγκυρες σε πολλά μοντέλα (Llama, Mistral, Phi, και η οικογένεια GPT-4.x - αν και το GPT-4.x αποσύρεται), αλλά η κατεύθυνση είναι prompt engineering + έλεγχοι συλλογισμού σε μοντέλα συλλογισμού όπως το GPT-5.

## Ανάθεση

Για αυτή την ανάθεση, μπορείτε να επιλέξετε τι θέλετε να κατασκευάσετε.

Εδώ είναι μερικές προτάσεις:

- Βελτιώστε περαιτέρω την εφαρμογή δημιουργίας συνταγών. Πειραματιστείτε με τις τιμές θερμοκρασίας και τα prompts για να δείτε τι μπορείτε να φτιάξετε.
- Δημιουργήστε ένα "study buddy". Αυτή η εφαρμογή θα πρέπει να μπορεί να απαντά σε ερωτήσεις σχετικά με ένα θέμα, για παράδειγμα την Python, με prompts όπως "Τι είναι ένα συγκεκριμένο θέμα στην Python;", ή ένα prompt που λέει, δείξε μου κώδικα για ένα συγκεκριμένο θέμα κτλ.
- Bot ιστορίας, φέρτε την ιστορία στη ζωή, δώστε εντολές στο bot να υποδυθεί έναν συγκεκριμένο ιστορικό χαρακτήρα και κάντε του ερωτήσεις για τη ζωή και την εποχή του.

## Λύση

### Study buddy

Παρακάτω είναι ένα αρχικό μήνυμα, δείτε πώς μπορείτε να το χρησιμοποιήσετε και να το τροποποιήσετε κατά βούληση.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Bot Ιστορίας

Εδώ είναι μερικά μηνύματα που θα μπορούσατε να χρησιμοποιήσετε:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Έλεγχος γνώσεων

Τι κάνει η έννοια temperature;

1. Ελέγχει πόσο τυχαία είναι η έξοδος.
1. Ελέγχει πόσο μεγάλη είναι η απάντηση.
1. Ελέγχει πόσοι τοκεν χρησιμοποιούνται.

## 🚀 Πρόκληση

Όταν εργάζεστε στο καθήκον, δοκιμάστε να μεταβάλλετε τη θερμοκρασία, δοκιμάστε να την ορίσετε σε 0, 0.5 και 1. Να θυμάστε ότι το 0 είναι το λιγότερο ποικίλο και το 1 το πιο πολύ. Ποια τιμή λειτουργεί καλύτερα για την εφαρμογή σας;

## Μπράβο! Συνεχίστε τη μάθησή σας

Μετά την ολοκλήρωση αυτού του μαθήματος, ρίξτε μια ματιά στη [Συλλογή Μαθημάτων Γενετικής Τεχνητής Νοημοσύνης](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) για να συνεχίσετε να εξελίσσετε τις γνώσεις σας στη Γενετική ΤΝ!

Πηγαίνετε στο Μάθημα 7 όπου θα δούμε πώς να [δημιουργήσετε εφαρμογές συνομιλίας](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->