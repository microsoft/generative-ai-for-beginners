# Δημιουργία Εφαρμογών Γεννήτριας Κειμένου

[![Building Text Generation Applications](../../../translated_images/el/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Κάντε κλικ στην εικόνα παραπάνω για να δείτε το βίντεο αυτής της ενότητας)_

Μέχρι τώρα, μέσα από αυτό το πρόγραμμα σπουδών έχετε δει βασικές έννοιες όπως τα prompts και ακόμη και μια ολόκληρη επιστήμη που ονομάζεται "μηχανική των prompts". Πολλά εργαλεία με τα οποία μπορείτε να αλληλεπιδράσετε, όπως το ChatGPT, το Office 365, το Microsoft Power Platform και άλλα, σας υποστηρίζουν χρησιμοποιώντας prompts για να πετύχετε κάτι.

Για να προσθέσετε τέτοιου είδους εμπειρία σε μια εφαρμογή, πρέπει να κατανοήσετε έννοιες όπως prompts, completions και να επιλέξετε μια βιβλιοθήκη για να δουλέψετε μαζί της. Αυτό ακριβώς θα μάθετε σε αυτό το κεφάλαιο.

## Εισαγωγή

Σε αυτό το κεφάλαιο, θα:

- Μάθετε για τη βιβλιοθήκη openai και τις βασικές της έννοιες.
- Δημιουργήσετε μια εφαρμογή γεννήτριας κειμένου χρησιμοποιώντας το openai.
- Κατανοήσετε πώς να χρησιμοποιείτε έννοιες όπως prompt, temperature και tokens για να δημιουργήσετε μια εφαρμογή γεννήτριας κειμένου.

## Στόχοι μάθησης

Στο τέλος αυτής της ενότητας, θα είστε σε θέση να:

- Εξηγείτε τι είναι μια εφαρμογή γεννήτριας κειμένου.
- Δημιουργήσετε μια εφαρμογή γεννήτριας κειμένου χρησιμοποιώντας το openai.
- Διαμορφώσετε την εφαρμογή σας για να χρησιμοποιεί περισσότερα ή λιγότερα tokens και επίσης να αλλάξετε την θερμοκρασία, για ποικιλία στο αποτέλεσμα.

## Τι είναι μια εφαρμογή γεννήτριας κειμένου;

Κανονικά, όταν δημιουργείτε μια εφαρμογή, έχει κάποιο είδος διεπαφής όπως η παρακάτω:

- Βασισμένη σε εντολές. Οι κονσόλες είναι τυπικές εφαρμογές όπου πληκτρολογείτε μια εντολή και εκτελείται μια εργασία. Για παράδειγμα, το `git` είναι μια εφαρμογή βασισμένη σε εντολές.
- Διεπαφή χρήστη (UI). Κάποιες εφαρμογές έχουν γραφική διεπαφή χρήστη (GUI), όπου πατάτε κουμπιά, εισάγετε κείμενο, επιλέγετε επιλογές και άλλα.

### Οι εφαρμογές κονσόλας και UI είναι περιορισμένες

Συγκρίνετέ το με μια εφαρμογή βασισμένη σε εντολές όπου πληκτρολογείτε εντολή:

- **Είναι περιορισμένη**. Δεν μπορείτε απλά να πληκτρολογήσετε οποιαδήποτε εντολή, μόνο αυτές που υποστηρίζει η εφαρμογή.
- **Ειδική γλώσσα**. Κάποιες εφαρμογές υποστηρίζουν πολλές γλώσσες, αλλά από προεπιλογή η εφαρμογή είναι φτιαγμένη για συγκεκριμένη γλώσσα, ακόμα και αν μπορείτε να προσθέσετε υποστήριξη για περισσότερες.

### Οφέλη των εφαρμογών γεννήτριας κειμένου

Πώς διαφέρει λοιπόν μια εφαρμογή γεννήτριας κειμένου;

Σε μια εφαρμογή γεννήτριας κειμένου έχετε μεγαλύτερη ευελιξία, δεν είστε περιορισμένοι σε ένα σύνολο εντολών ή σε μια συγκεκριμένη γλώσσα εισόδου. Αντίθετα, μπορείτε να χρησιμοποιήσετε φυσική γλώσσα για να αλληλεπιδράσετε με την εφαρμογή. Ένα επιπλέον όφελος είναι ότι ήδη αλληλεπιδράτε με μια πηγή δεδομένων που έχει εκπαιδευτεί σε ένα τεράστιο σώμα πληροφοριών, ενώ μια παραδοσιακή εφαρμογή μπορεί να είναι περιορισμένη σε ό,τι περιέχεται στη βάση δεδομένων της.

### Τι μπορώ να δημιουργήσω με μια εφαρμογή γεννήτριας κειμένου;

Μπορείτε να δημιουργήσετε πολλά πράγματα. Για παράδειγμα:

- **Ένα chatbot**. Ένα chatbot που απαντά σε ερωτήσεις για θέματα, όπως η εταιρεία σας και τα προϊόντα της, μπορεί να είναι μια καλή εφαρμογή.
- **Βοηθό**. Τα LLM (μεγάλα γλωσσικά μοντέλα) είναι εξαιρετικά σε εργασίες όπως περίληψη κειμένου, εξαγωγή πληροφοριών από κείμενο, παραγωγή κειμένου όπως βιογραφικά και άλλα.
- **Βοηθό κώδικα**. Ανάλογα με το γλωσσικό μοντέλο που χρησιμοποιείτε, μπορείτε να δημιουργήσετε έναν βοηθό που σας βοηθά να γράφετε κώδικα. Για παράδειγμα, μπορείτε να χρησιμοποιήσετε προϊόντα όπως το GitHub Copilot καθώς και το ChatGPT για να γράφετε κώδικα.

## Πώς μπορώ να ξεκινήσω;

Λοιπόν, πρέπει να βρείτε έναν τρόπο να ενσωματωθείτε με ένα LLM, που συνήθως περιλαμβάνει τις ακόλουθες δύο προσεγγίσεις:

- Χρήση ενός API. Εδώ κατασκευάζετε web αιτήματα με το prompt σας και λαμβάνετε πίσω το παραγόμενο κείμενο.
- Χρήση μιας βιβλιοθήκης. Οι βιβλιοθήκες βοηθούν στην ενσωμάτωση των κλήσεων API και καθιστούν τη χρήση τους πιο εύκολη.

## Βιβλιοθήκες/SDKs

Υπάρχουν μερικές γνωστές βιβλιοθήκες για εργασία με LLM όπως:

- **openai**, αυτή η βιβλιοθήκη κάνει εύκολη τη σύνδεση με το μοντέλο σας και την αποστολή prompts.

Έπειτα υπάρχουν βιβλιοθήκες που λειτουργούν σε πιο υψηλό επίπεδο όπως:

- **Langchain**. Το Langchain είναι γνωστό και υποστηρίζει Python.
- **Semantic Kernel**. Το Semantic Kernel είναι μια βιβλιοθήκη της Microsoft που υποστηρίζει τις γλώσσες C#, Python και Java.

## Πρώτη εφαρμογή με χρήση openai

Ας δούμε πώς μπορούμε να δημιουργήσουμε την πρώτη μας εφαρμογή, ποιες βιβλιοθήκες χρειαζόμαστε, πόσο απαιτείται και ούτω καθεξής.

### Εγκατάσταση openai

Υπάρχουν πολλές βιβλιοθήκες εκεί έξω για αλληλεπίδραση με το OpenAI ή το Azure OpenAI. Είναι δυνατό να χρησιμοποιηθούν πολλές γλώσσες προγραμματισμού καθώς και C#, Python, JavaScript, Java και περισσότερες. Έχουμε επιλέξει να χρησιμοποιήσουμε τη βιβλιοθήκη `openai` της Python, οπότε θα χρησιμοποιήσουμε το `pip` για να την εγκαταστήσουμε.

```bash
pip install openai
```

### Δημιουργία πόρου

Πρέπει να κάνετε τα εξής βήματα:

- Δημιουργήστε λογαριασμό στο Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Αποκτήστε πρόσβαση στο Azure OpenAI. Πηγαίνετε στο [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) και ζητήστε πρόσβαση.

  > [!NOTE]
  > Κατά τη στιγμή της συγγραφής, πρέπει να κάνετε αίτηση για πρόσβαση στο Azure OpenAI.

- Εγκαταστήστε την Python <https://www.python.org/>
- Έχετε δημιουργήσει έναν πόρο Azure OpenAI Service. Δείτε αυτόν τον οδηγό για το πώς να [δημιουργήσετε πόρο](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Εντοπισμός κλειδιού API και τελικού σημείου (endpoint)

Σε αυτό το σημείο, πρέπει να πείτε στη βιβλιοθήκη `openai` ποιο API key να χρησιμοποιήσει. Για να βρείτε το API key σας, πηγαίνετε στην ενότητα "Keys and Endpoint" του πόρου Azure OpenAI και αντιγράψτε την τιμή "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Τώρα που έχετε αντιγράψει αυτές τις πληροφορίες, ας δώσουμε οδηγίες στις βιβλιοθήκες να τις χρησιμοποιήσουν.

> [!NOTE]
> Αξίζει να διαχωρίσετε το API key σας από τον κώδικά σας. Μπορείτε να το κάνετε χρησιμοποιώντας μεταβλητές περιβάλλοντος.
>
> - Ορίστε τη μεταβλητή περιβάλλοντος `OPENAI_API_KEY` στο API key σας.
>   `export OPENAI_API_KEY='sk-...'`

### Ρύθμιση διαμόρφωσης Azure

Αν χρησιμοποιείτε Azure OpenAI (τώρα μέρος του Microsoft Foundry), εδώ είναι πώς ρυθμίζετε τη διαμόρφωση. Χρησιμοποιούμε τον στάνταρ πελάτη `OpenAI` που δείχνει στο τελικό σημείο Azure OpenAI `/openai/v1/`, που λειτουργεί με το Responses API και δεν χρειάζεται `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Πάνω, ρυθμίζουμε τα εξής:

- `api_key`, αυτό είναι το API key σας που βρέθηκε στο Azure Portal ή στο Microsoft Foundry portal.
- `base_url`, αυτό είναι το τελικό σημείο (endpoint) του Foundry resource σας με το `/openai/v1/` προστιθέμενο. Το σταθερό endpoint v1 λειτουργεί και με το OpenAI και με το Azure OpenAI χωρίς διαχείριση `api_version`.

> [!NOTE] > `os.environ` διαβάζει τις μεταβλητές περιβάλλοντος. Μπορείτε να το χρησιμοποιήσετε για να διαβάσετε μεταβλητές όπως `AZURE_OPENAI_API_KEY` και `AZURE_OPENAI_ENDPOINT`. Ορίστε αυτές τις μεταβλητές στο τερματικό σας ή χρησιμοποιώντας μια βιβλιοθήκη όπως το `dotenv`.

## Παραγωγή κειμένου

Ο τρόπος να παράγετε κείμενο είναι χρησιμοποιώντας το Responses API μέσω της μεθόδου `responses.create`. Να ένα παράδειγμα:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # αυτό είναι το όνομα της ανάπτυξης του μοντέλου σας
    input=prompt,
    store=False,
)
print(response.output_text)
```

Στον παραπάνω κώδικα, δημιουργούμε μια απάντηση και περνάμε το μοντέλο που θέλουμε να χρησιμοποιήσουμε και το prompt. Έπειτα εκτυπώνουμε το παραγόμενο κείμενο μέσω `response.output_text`.

### Συζητήσεις με πολλούς γύρους (multi-turn conversations)

Το Responses API είναι κατάλληλο τόσο για παραγωγή κειμένου με έναν γύρο όσο και για chatbots πολλών γύρων - παρέχετε μια λίστα μηνυμάτων στο `input` για να δημιουργήσετε μια συνομιλία:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Περισσότερα για αυτή τη λειτουργικότητα σε επόμενο κεφάλαιο.

## Άσκηση - η πρώτη σας εφαρμογή γεννήτριας κειμένου

Τώρα που μάθαμε πώς να ρυθμίσουμε και να διαμορφώσουμε το openai, είναι ώρα να δημιουργήσετε την πρώτη σας εφαρμογή γεννήτριας κειμένου. Για να την δημιουργήσετε, ακολουθήστε τα εξής βήματα:

1. Δημιουργήστε ένα εικονικό περιβάλλον και εγκαταστήστε το openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Αν χρησιμοποιείτε Windows, πληκτρολογήστε `venv\Scripts\activate` αντί για `source venv/bin/activate`.

   > [!NOTE]
   > Εντοπίστε το Azure OpenAI κλειδί σας πηγαίνοντας στο [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) και ψάξτε για το `Open AI`, επιλέξτε τον `Open AI πόρο` και μετά επιλέξτε `Keys and Endpoint` και αντιγράψτε την τιμή `Key 1`.

1. Δημιουργήστε ένα αρχείο _app.py_ και γράψτε τον παρακάτω κώδικα:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # προσθέστε τον κώδικα ολοκλήρωσής σας
   prompt = "Complete the following: Once upon a time there was a"

   # κάντε ένα αίτημα χρησιμοποιώντας το API Απαντήσεων
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # εκτυπώστε την απάντηση
   print(response.output_text)
   ```

   > [!NOTE]
   > Αν χρησιμοποιείτε το απλό OpenAI (όχι Azure), χρησιμοποιήστε `client = OpenAI(api_key="<αντικαταστήστε αυτήν την τιμή με το OpenAI κλειδί σας>")` (χωρίς `base_url`) και περάστε όνομα μοντέλου όπως `gpt-5-mini` αντί για όνομα ανάπτυξης.

   Θα δείτε ένα αποτέλεσμα σαν το παρακάτω:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Διαφορετικοί τύποι prompts για διαφορετικά πράγματα

Τώρα που έχετε δει πώς να παράγετε κείμενο χρησιμοποιώντας ένα prompt. Έχετε ακόμη και ένα πρόγραμμα σε λειτουργία που μπορείτε να τροποποιήσετε και να αλλάξετε για να παράγετε διαφορετικούς τύπους κειμένου.

Τα prompts μπορούν να χρησιμοποιηθούν για κάθε είδους εργασία. Για παράδειγμα:

- **Παραγωγή ενός τύπου κειμένου**. Για παράδειγμα, μπορείτε να δημιουργήσετε ένα ποίημα, ερωτήσεις για κουίζ κ.ά.
- **Αναζήτηση πληροφοριών**. Μπορείτε να χρησιμοποιήσετε prompts για να αναζητήσετε πληροφορίες όπως στο παράδειγμα «Τι σημαίνει CORS στην ανάπτυξη ιστού;».
- **Παραγωγή κώδικα**. Μπορείτε να χρησιμοποιήσετε prompts για να δημιουργήσετε κώδικα, για παράδειγμα να αναπτύξετε μια κανονική έκφραση για να ελέγχετε email ή γιατί όχι να δημιουργήσετε ολόκληρο πρόγραμμα, όπως μια web εφαρμογή;

## Ένα πιο πρακτικό παράδειγμα: γεννήτρια συνταγών

Φανταστείτε ότι έχετε υλικά στο σπίτι και θέλετε να μαγειρέψετε κάτι. Για αυτό, χρειάζεστε μια συνταγή. Ένας τρόπος να βρείτε συνταγές είναι να χρησιμοποιήσετε μια μηχανή αναζήτησης ή να χρησιμοποιήσετε ένα LLM γι' αυτό.

Μπορείτε να γράψετε ένα prompt ως εξής:

> "Δείξε μου 5 συνταγές για πιάτο με τα εξής υλικά: κοτόπουλο, πατάτες και καρότα. Σε κάθε συνταγή, να παρατίθενται όλα τα χρησιμοποιούμενα υλικά."

Βάσει του παραπάνω prompt, μπορεί να λάβετε απάντηση παρόμοια με:

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

Το αποτέλεσμα είναι εξαιρετικό, ξέρω τι να μαγειρέψω. Σε αυτό το σημείο, χρήσιμες βελτιώσεις που θα μπορούσαν να γίνουν είναι:

- Να φιλτραριστούν υλικά που δεν μου αρέσουν ή σε αυτά είμαι αλλεργικός.
- Να παραχθεί μια λίστα αγορών, σε περίπτωση που δεν έχω όλα τα υλικά στο σπίτι.

Για τις παραπάνω περιπτώσεις, ας προσθέσουμε ένα επιπλέον prompt:

> "Παρακαλώ απαλείψτε συνταγές που περιέχουν σκόρδο, είμαι αλλεργικός και αντικαταστήστε το με κάτι άλλο. Επίσης, παρακαλώ δημιουργήστε μια λίστα αγορών για τις συνταγές, λαμβάνοντας υπόψη ότι ήδη έχω κοτόπουλο, πατάτες και καρότα στο σπίτι."

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

Αυτές είναι οι πέντε συνταγές σας, χωρίς να αναφέρεται σκόρδο και επίσης έχετε μια λίστα αγορών λαμβάνοντας υπόψη όσα ήδη έχετε στο σπίτι.

## Άσκηση - δημιουργία γεννήτριας συνταγών

Τώρα που παίξαμε ένα σενάριο, ας γράψουμε κώδικα που ταιριάζει με το επιδειχθέν σενάριο. Για να το κάνετε, ακολουθήστε αυτά τα βήματα:

1. Χρησιμοποιήστε το υπάρχον αρχείο _app.py_ ως σημείο εκκίνησης
1. Εντοπίστε τη μεταβλητή `prompt` και αλλάξτε τον κώδικά της ως εξής:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Αν τώρα τρέξετε τον κώδικα, θα πρέπει να δείτε ένα αποτέλεσμα παρόμοιο με:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > ΣΗΜΕΙΩΣΗ, το LLM σας είναι μη-νηματοδοτικό (nondeterministic), οπότε μπορεί να πάρετε διαφορετικά αποτελέσματα κάθε φορά που τρέχετε το πρόγραμμα.

   Τέλεια, ας δούμε πώς μπορούμε να βελτιώσουμε τα πράγματα. Για να βελτιώσουμε, θέλουμε ο κώδικας να είναι ευέλικτος, ώστε τα υλικά και ο αριθμός των συνταγών να μπορούν να βελτιωθούν και να αλλάξουν.

1. Αλλάξτε τον κώδικα με τον εξής τρόπο:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # ενσωματώστε τον αριθμό των συνταγών στο αίτημα και τα συστατικά
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Η εκτέλεση δοκιμής με τον κώδικα μπορεί να μοιάζει ως εξής:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Βελτίωση μέσω προσθήκης φίλτρου και λίστας αγορών

Τώρα έχουμε μια λειτουργική εφαρμογή ικανή να παράγει συνταγές και είναι ευέλικτη καθώς βασίζεται σε δεδομένα από τον χρήστη, τόσο για τον αριθμό των συνταγών όσο και για τα χρησιμοποιούμενα υλικά.

Για περαιτέρω βελτίωση, θέλουμε να προσθέσουμε τα εξής:

- **Φιλτράρισμα υλικών**. Θέλουμε να μπορούμε να φιλτράρουμε υλικά που δεν μας αρέσουν ή στα οποία έχουμε αλλεργία. Για να γίνει αυτό, μπορούμε να επεξεργαστούμε το υπάρχον prompt και να προσθέσουμε μια συνθήκη φίλτρου στο τέλος του ως εξής:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Πάνω, προσθέτουμε το `{filter}` στο τέλος του prompt και επίσης λαμβάνουμε την τιμή του φίλτρου από τον χρήστη.

  Ένα παράδειγμα εισόδου εκτέλεσης του προγράμματος μπορεί τώρα να είναι ως εξής:

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

  Όπως βλέπετε, οποιεσδήποτε συνταγές που περιέχουν γάλα έχουν φιλτραριστεί. Αλλά, αν είστε δυσανεκτικός στη λακτόζη, μπορεί να θελήσετε να φιλτράρετε επίσης συνταγές που περιέχουν τυρί, άρα χρειάζεται να είμαστε σαφείς.


- **Παράγετε μια λίστα αγορών**. Θέλουμε να παράγουμε μια λίστα αγορών, λαμβάνοντας υπόψη τι έχουμε ήδη στο σπίτι.

  Για αυτή τη λειτουργία, θα μπορούσαμε είτε να προσπαθήσουμε να λύσουμε τα πάντα σε ένα prompt είτε να το χωρίσουμε σε δύο prompts. Ας δοκιμάσουμε τη δεύτερη προσέγγιση. Εδώ προτείνουμε να προσθέσουμε ένα επιπλέον prompt, αλλά για να δουλέψει αυτό, πρέπει να προσθέσουμε το αποτέλεσμα του πρώτου prompt ως πλαίσιο στο δεύτερο prompt.

  Εντοπίστε το σημείο στον κώδικα που εκτυπώνει το αποτέλεσμα από το πρώτο prompt και προσθέστε τον ακόλουθο κώδικα από κάτω:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # εκτύπωσε την απόκριση
  print("Shopping list:")
  print(response.output_text)
  ```

  Σημειώστε τα εξής:

  1. Κατασκευάζουμε ένα νέο prompt προσθέτοντας το αποτέλεσμα από το πρώτο prompt στο νέο prompt:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Κάνουμε νέο αίτημα, αλλά λαμβάνοντας υπόψη τον αριθμό των tokens που ζητήσαμε στο πρώτο prompt, οπότε αυτή τη φορά λέμε ότι το `max_output_tokens` είναι 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Δοκιμάζοντας αυτόν τον κώδικα, φτάνουμε τώρα στην ακόλουθη έξοδο:

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

Αυτό που έχουμε μέχρι στιγμής είναι κώδικας που λειτουργεί, αλλά υπάρχουν ορισμένες προσαρμογές που θα πρέπει να κάνουμε για να βελτιώσουμε περαιτέρω τα πράγματα. Κάποια πράγματα που θα πρέπει να κάνουμε είναι:

- **Ξεχωρίστε τα μυστικά από τον κώδικα**, όπως το κλειδί API. Τα μυστικά δεν ανήκουν στον κώδικα και θα πρέπει να αποθηκεύονται σε ασφαλές μέρος. Για να ξεχωρίσετε τα μυστικά από τον κώδικα, μπορούμε να χρησιμοποιήσουμε μεταβλητές περιβάλλοντος και βιβλιοθήκες όπως το `python-dotenv` για να τα φορτώσουμε από ένα αρχείο. Δείτε πώς θα μοιάζει αυτό στον κώδικα:

  1. Δημιουργήστε ένα αρχείο `.env` με το ακόλουθο περιεχόμενο:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Σημείωση, για το Azure OpenAI στο Microsoft Foundry, πρέπει να ορίσετε τις ακόλουθες μεταβλητές περιβάλλοντος αντί:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Στον κώδικα, θα φορτώνατε τις μεταβλητές περιβάλλοντος ως εξής:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Λίγα λόγια για το μήκος των tokens**. Πρέπει να σκεφτούμε πόσα tokens χρειαζόμαστε για να δημιουργήσουμε το κείμενο που θέλουμε. Τα tokens κοστίζουν χρήματα, οπότε όπου είναι δυνατό, πρέπει να προσπαθούμε να είμαστε οικονομικοί με τον αριθμό των tokens που χρησιμοποιούμε. Για παράδειγμα, μπορούμε να μορφοποιήσουμε το prompt έτσι ώστε να χρησιμοποιήσουμε λιγότερα tokens;

  Για να αλλάξετε τα χρησιμοποιούμενα tokens, μπορείτε να χρησιμοποιήσετε την παράμετρο `max_output_tokens`. Για παράδειγμα, αν θέλετε να χρησιμοποιήσετε 100 tokens, θα κάνατε:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Επειραματισμός με τη θερμοκρασία**. Η θερμοκρασία είναι κάτι που δεν έχουμε αναφέρει μέχρι τώρα αλλά είναι ένα σημαντικό πλαίσιο για το πώς λειτουργεί το πρόγραμμά μας. Όσο υψηλότερη είναι η τιμή της θερμοκρασίας, τόσο πιο τυχαία θα είναι η έξοδος. Αντίθετα, όσο χαμηλότερη είναι η θερμοκρασία, τόσο πιο προβλέψιμη θα είναι η έξοδος. Σκεφτείτε αν θέλετε ποικιλία στην έξοδό σας ή όχι.

  Για να αλλάξετε τη θερμοκρασία, μπορείτε να χρησιμοποιήσετε την παράμετρο `temperature`. Για παράδειγμα, αν θέλετε να χρησιμοποιήσετε θερμοκρασία 0,5, θα κάνατε:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Σημείωση, όσο πιο κοντά στο 1.0, τόσο πιο ποικίλη είναι η έξοδος.

- **Τα μοντέλα λογικής δεν χρησιμοποιούν το `temperature`**. Αυτή είναι μια σημαντική αλλαγή για το 2026. Τα τρέχοντα, μη αποσυρθέντα μοντέλα στο Microsoft Foundry είναι **μοντέλα λογικής** (η οικογένεια GPT-5, ο-σειρά) - και **δεν υποστηρίζουν το `temperature` ή το `top_p`** (ούτε το `max_tokens`; χρησιμοποιήστε το `max_output_tokens`). Αν στείλετε `temperature` στο `gpt-5-mini`, θα λάβετε σφάλμα "parameter not supported". Για να δοκιμάσετε το παράδειγμα της θερμοκρασίας παραπάνω, επιλέξτε ένα μοντέλο που ακόμη υποστηρίζει ελέγχους δειγματοληψίας - για παράδειγμα ένα ανοιχτό **Llama** μοντέλο όπως το `Llama-3.3-70B-Instruct` από τον [κατάλογο μοντέλων Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), που καλείται μέσω του Foundry Models / Azure AI Inference endpoint (με τον ίδιο τρόπο όπως τα δείγματα `githubmodels-*`). Για μοντέλα λογικής όπως το GPT-5, καθοδηγείτε την έξοδο διαφορετικά:
  - **Μηχανική prompt** - καθαρές οδηγίες, παραδείγματα και δομημένη έξοδος (δείτε το μάθημα [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) κάνουν τη δουλειά που συνήθιζαν να κάνουν τα sampling controls.
  - **Έλεγχοι λογικής** - παράμετροι όπως η προσπάθεια/λεπτομέρεια λογικής ανταλλάσσουν βάθος σκέψης με καθυστέρηση και κόστος.

  Εν συντομία: το `temperature`/`top_p` εξακολουθούν να ισχύουν σε πολλά μοντέλα (Llama, Mistral, Phi, και η οικογένεια GPT-4.x - αν και το GPT-4.x καταργείται), αλλά η κατεύθυνση είναι η μηχανική prompt + έλεγχοι λογικής σε μοντέλα λογικής όπως το GPT-5.

## Εργασία

Για αυτή την εργασία, μπορείτε να επιλέξετε τι θα δημιουργήσετε.

Ορίστε μερικές προτάσεις:

- Τροποποιήστε την εφαρμογή γεννήτριας συνταγών για να την βελτιώσετε περαιτέρω. Πειραματιστείτε με τις τιμές θερμοκρασίας και τα prompts για να δείτε τι μπορείτε να φτιάξετε.
- Φτιάξτε έναν "φίλο μελέτης". Αυτή η εφαρμογή θα πρέπει να μπορεί να απαντά σε ερωτήσεις για ένα θέμα, για παράδειγμα Python, μπορείτε να έχετε prompts όπως "Τι είναι ένα συγκεκριμένο θέμα στην Python;", ή ένα prompt που λέει, δείξε μου κώδικα για ένα συγκεκριμένο θέμα κ.λπ.
- Ιστορικό ρομπότ, κάντε την ιστορία να ζωντανέψει, διδάξτε το ρομπότ να παίζει έναν συγκεκριμένο ιστορικό χαρακτήρα και ρωτήστε το ερωτήσεις για τη ζωή και τους καιρούς του.

## Λύση

### Φίλος μελέτης

Παρακάτω είναι ένα αρχικό prompt, δείτε πώς μπορείτε να το χρησιμοποιήσετε και να το τροποποιήσετε κατά βούληση.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Ιστορικό ρομπότ

Ορίστε μερικά prompts που θα μπορούσατε να χρησιμοποιείτε:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Έλεγχος γνώσεων

Τι κάνει η έννοια της θερμοκρασίας;

1. Ελέγχει πόσο τυχαία είναι η έξοδος.
1. Ελέγχει πόσο μεγάλη είναι η απάντηση.
1. Ελέγχει πόσα tokens χρησιμοποιούνται.

## 🚀 Πρόκληση

Καθώς εργάζεστε στην εργασία, προσπαθήστε να ποικίλλετε τη θερμοκρασία, δοκιμάζοντας τις τιμές 0, 0,5 και 1. Θυμηθείτε ότι το 0 είναι το λιγότερο ποικίλο και το 1 το περισσότερο. Ποια τιμή ταιριάζει καλύτερα στην εφαρμογή σας;

## Άριστη δουλειά! Συνεχίστε τη μάθησή σας

Αφού ολοκληρώσετε αυτό το μάθημα, ρίξτε μια ματιά στη [συλλογή μας για τη Μάθηση της Γενετικής Τεχνητής Νοημοσύνης](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) για να συνεχίσετε να αναβαθμίζετε τις γνώσεις σας!

Μεταβείτε στο Μάθημα 7 όπου θα δούμε πώς να [δημιουργούμε εφαρμογές συνομιλίας](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->