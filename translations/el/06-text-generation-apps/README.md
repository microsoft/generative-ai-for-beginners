# Δημιουργία Εφαρμογών Γεννήτριας Κειμένου

[![Δημιουργία Εφαρμογών Γεννήτριας Κειμένου](../../../translated_images/el/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Κάντε κλικ στην παραπάνω εικόνα για να δείτε το βίντεο αυτής της μαθήματος)_

Μέχρι τώρα, μέσα από αυτό το πρόγραμμα σπουδών έχετε δει ότι υπάρχουν βασικές έννοιες όπως τα prompts και ακόμα ένα ολόκληρο πεδίο που ονομάζεται «μηχανική των prompts». Πολλά εργαλεία με τα οποία αλληλεπιδράτε, όπως το ChatGPT, το Office 365, το Microsoft Power Platform και άλλα, σας υποστηρίζουν χρησιμοποιώντας prompts για να επιτύχετε κάτι.

Για να προσθέσετε μια τέτοια εμπειρία σε μια εφαρμογή, πρέπει να κατανοήσετε έννοιες όπως τα prompts, τις ολοκληρώσεις (completions) και να επιλέξετε μια βιβλιοθήκη για να εργαστείτε. Αυτό ακριβώς θα μάθετε σε αυτό το κεφάλαιο.

## Εισαγωγή

Σε αυτό το κεφάλαιο, θα:

- Μάθετε για τη βιβλιοθήκη openai και τις βασικές της έννοιες.
- Δημιουργήσετε μια εφαρμογή γεννήτριας κειμένου χρησιμοποιώντας το openai.
- Κατανοήσετε πώς να χρησιμοποιείτε έννοιες όπως prompt, temperature και tokens για να δημιουργήσετε μια εφαρμογή γεννήτριας κειμένου.

## Στόχοι μάθησης

Στο τέλος αυτού του μαθήματος, θα μπορείτε να:

- Εξηγήσετε τι είναι μια εφαρμογή γεννήτριας κειμένου.
- Δημιουργήσετε μια εφαρμογή γεννήτριας κειμένου χρησιμοποιώντας το openai.
- Ρυθμίσετε την εφαρμογή σας ώστε να χρησιμοποιεί περισσότερα ή λιγότερα tokens και να αλλάζει την παράμετρο temperature, για ποικιλία εξόδου.

## Τι είναι μια εφαρμογή γεννήτριας κειμένου;

Κανονικά όταν δημιουργείτε μια εφαρμογή, έχει κάποιο είδος διεπαφής όπως το παρακάτω:

- Βασισμένη σε εντολές. Οι εφαρμογές κονσόλας είναι τυπικές εφαρμογές όπου πληκτρολογείτε μια εντολή και εκτελεί μια εργασία. Για παράδειγμα, το `git` είναι μια εφαρμογή βασισμένη σε εντολές.
- Διεπαφή χρήστη (UI). Κάποιες εφαρμογές έχουν γραφικές διεπαφές χρήστη (GUIs) όπου κάνετε κλικ σε κουμπιά, εισάγετε κείμενο, επιλέγετε επιλογές και άλλα.

### Οι εφαρμογές κονσόλας και UI έχουν περιορισμούς

Συγκρίνετέ το με μια εφαρμογή βασισμένη σε εντολές όπου πληκτρολογείτε μια εντολή:

- **Είναι περιορισμένη**. Δεν μπορείτε απλά να πληκτρολογήσετε οποιαδήποτε εντολή, μόνο αυτές που υποστηρίζει η εφαρμογή.
- **Ειδική για γλώσσα**. Κάποιες εφαρμογές υποστηρίζουν πολλές γλώσσες, αλλά από προεπιλογή η εφαρμογή κατασκευάζεται για μια συγκεκριμένη γλώσσα, ακόμη και αν μπορείτε να προσθέσετε περισσότερη υποστήριξη γλωσσών.

### Οφέλη των εφαρμογών γεννήτριας κειμένου

Πώς λοιπόν διαφέρει μια εφαρμογή γεννήτριας κειμένου;

Σε μια εφαρμογή γεννήτριας κειμένου, έχετε περισσότερη ευελιξία, δεν περιορίζεστε σε ένα σύνολο εντολών ή συγκεκριμένη γλώσσα εισόδου. Αντίθετα, μπορείτε να χρησιμοποιήσετε φυσική γλώσσα για να αλληλεπιδράσετε με την εφαρμογή. Ένα άλλο πλεονέκτημα είναι ότι ήδη αλληλεπιδράτε με μια πηγή δεδομένων που έχει εκπαιδευτεί σε ένα τεράστιο σώμα πληροφοριών, ενώ μια παραδοσιακή εφαρμογή μπορεί να είναι περιορισμένη σε ό, τι περιέχει μια βάση δεδομένων.

### Τι μπορώ να δημιουργήσω με μια εφαρμογή γεννήτριας κειμένου;

Μπορείτε να δημιουργήσετε πολλά πράγματα. Για παράδειγμα:

- **Έναν chatbot**. Ένας chatbot που απαντά σε ερωτήσεις για θέματα, όπως η εταιρεία σας και τα προϊόντα της, θα ήταν κατάλληλος.
- **Βοηθό**. Τα LLM είναι εξαιρετικά σε πράγματα όπως η σύνοψη κειμένου, η εξαγωγή πληροφοριών από κείμενο, η παραγωγή κειμένου όπως βιογραφικά και άλλα.
- **Βοηθό προγραμματισμού**. Ανάλογα με το γλωσσικό μοντέλο που χρησιμοποιείτε, μπορείτε να δημιουργήσετε έναν βοηθό κώδικα που σας βοηθά να γράψετε κώδικα. Για παράδειγμα, μπορείτε να χρησιμοποιήσετε προϊόντα όπως το GitHub Copilot καθώς και το ChatGPT για να σας βοηθήσουν στην συγγραφή κώδικα.

## Πώς μπορώ να ξεκινήσω;

Λοιπόν, χρειάζεται να βρείτε έναν τρόπο να ενσωματωθείτε με ένα LLM που συνήθως περιλαμβάνει τις ακόλουθες δύο προσεγγίσεις:

- Χρησιμοποιήστε ένα API. Εδώ κατασκευάζετε αιτήματα web με το prompt σας και λαμβάνετε πίσω το παραγόμενο κείμενο.
- Χρησιμοποιήστε μια βιβλιοθήκη. Οι βιβλιοθήκες βοηθούν να ενσωματώσετε τις κλήσεις API και τις κάνουν πιο εύκολες στη χρήση.

## Βιβλιοθήκες/SDKs

Υπάρχουν μερικές γνωστές βιβλιοθήκες για εργασία με LLM, όπως:

- **openai**, αυτή η βιβλιοθήκη καθιστά εύκολη τη σύνδεση με το μοντέλο σας και την αποστολή prompts.

Μετά υπάρχουν βιβλιοθήκες που λειτουργούν σε ανώτερο επίπεδο, όπως:

- **Langchain**. Το Langchain είναι γνωστό και υποστηρίζει Python.
- **Semantic Kernel**. Το Semantic Kernel είναι μια βιβλιοθήκη της Microsoft που υποστηρίζει τις γλώσσες C#, Python και Java.

## Πρώτη εφαρμογή χρησιμοποιώντας το openai

Ας δούμε πώς μπορούμε να δημιουργήσουμε την πρώτη μας εφαρμογή, ποιες βιβλιοθήκες χρειάζονται, πόσο απαιτείται και λοιπά.

### Εγκατάσταση openai

Υπάρχουν πολλές βιβλιοθήκες για την αλληλεπίδραση με το OpenAI ή Azure OpenAI. Είναι επίσης εφικτό να χρησιμοποιήσετε διάφορες γλώσσες προγραμματισμού όπως C#, Python, JavaScript, Java και άλλες. Επιλέξαμε να χρησιμοποιήσουμε τη βιβλιοθήκη Python `openai`, οπότε θα χρησιμοποιήσουμε το `pip` για να την εγκαταστήσουμε.

```bash
pip install openai
```

### Δημιουργία πόρου

Πρέπει να εκτελέσετε τα εξής βήματα:

- Δημιουργήστε λογαριασμό στο Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Αποκτήστε πρόσβαση στο Azure OpenAI. Μεταβείτε στο [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) και ζητήστε πρόσβαση.

  > [!NOTE]
  > Τη στιγμή που γράφονται αυτές οι γραμμές, πρέπει να κάνετε αίτηση για πρόσβαση στο Azure OpenAI.

- Εγκαταστήστε την Python <https://www.python.org/>
- Έχετε δημιουργήσει έναν πόρο Azure OpenAI Service. Δείτε αυτόν τον οδηγό για το πώς να [δημιουργήσετε πόρο](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Βρείτε το κλειδί API και το endpoint

Σε αυτό το σημείο, πρέπει να πείτε στη βιβλιοθήκη `openai` ποιο κλειδί API να χρησιμοποιήσει. Για να βρείτε το κλειδί API, μεταβείτε στην ενότητα "Keys and Endpoint" του πόρου Azure OpenAI και αντιγράψτε την τιμή "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Τώρα που έχετε αντιγράψει αυτές τις πληροφορίες, ας υποδείξουμε στις βιβλιοθήκες να τις χρησιμοποιήσουν.

> [!NOTE]
> Αξίζει να κρατάτε το κλειδί API ξεχωριστά από τον κώδικά σας. Μπορείτε να το κάνετε χρησιμοποιώντας μεταβλητές περιβάλλοντος.
>
> - Ορίστε τη μεταβλητή περιβάλλοντος `OPENAI_API_KEY` με το κλειδί API σας.
>   `export OPENAI_API_KEY='sk-...'`

### Ρύθμιση παραμετροποίησης Azure

Εάν χρησιμοποιείτε το Azure OpenAI (τώρα μέρος του Microsoft Foundry), έτσι ρυθμίζετε την παραμετροποίηση. Χρησιμοποιούμε τον τυπικό πελάτη `OpenAI` με endpoint Azure OpenAI `/openai/v1/`, που λειτουργεί με το Responses API και δεν απαιτεί `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Παραπάνω ρυθμίζουμε τα εξής:

- `api_key`, αυτό είναι το κλειδί API που βρίσκετε στο Azure Portal ή το Microsoft Foundry portal.
- `base_url`, αυτό είναι το endpoint του Foundry resource με προσαρμογή `/openai/v1/`. Το σταθερό v1 endpoint δουλεύει τόσο για OpenAI όσο και για Azure OpenAI χωρίς διαχείριση `api_version`.

> [!NOTE] > Το `os.environ` διαβάζει μεταβλητές περιβάλλοντος. Μπορείτε να το χρησιμοποιήσετε για να διαβάσετε μεταβλητές όπως `AZURE_OPENAI_API_KEY` και `AZURE_OPENAI_ENDPOINT`. Ορίστε αυτές τις μεταβλητές στο τερματικό σας ή χρησιμοποιώντας βιβλιοθήκη όπως το `dotenv`.

## Δημιουργία κειμένου

Ο τρόπος δημιουργίας κειμένου είναι να χρησιμοποιήσετε το Responses API μέσω της μεθόδου `responses.create`. Να ένα παράδειγμα:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # αυτό είναι το όνομα ανάπτυξης του μοντέλου σας
    input=prompt,
    store=False,
)
print(response.output_text)
```

Στον παραπάνω κώδικα, δημιουργούμε μια απάντηση και περνάμε το μοντέλο που θέλουμε να χρησιμοποιήσουμε και το prompt. Έπειτα εκτυπώνουμε το παραγόμενο κείμενο μέσω `response.output_text`.

### Συνομιλίες πολλών στροφών

Το Responses API είναι κατάλληλο τόσο για γεννήτρια κειμένου μιας μόνο στροφής όσο και για chatbots πολλών στροφών - παρέχετε μια λίστα μηνυμάτων στο `input` για να χτίσετε μια συνομιλία:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

Περισσότερα για αυτή τη λειτουργία σε επόμενο κεφάλαιο.

## Άσκηση - η πρώτη σας εφαρμογή γεννήτριας κειμένου

Τώρα που μάθαμε πώς να ρυθμίζουμε και να παραμετροποιούμε το openai, είναι ώρα να δημιουργήσετε την πρώτη σας εφαρμογή γεννήτριας κειμένου. Για να το κάνετε, ακολουθήστε τα παρακάτω βήματα:

1. Δημιουργήστε ένα εικονικό περιβάλλον και εγκαταστήστε το openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Εάν χρησιμοποιείτε Windows, πληκτρολογήστε `venv\Scripts\activate` αντί για `source venv/bin/activate`.

   > [!NOTE]
   > Βρείτε το κλειδί Azure OpenAI μεταβαίνοντας στο [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) και αναζητώντας `Open AI`. Επιλέξτε τον `Open AI resource` και μετά την επιλογή `Keys and Endpoint` και αντιγράψτε την τιμή `Key 1`.

1. Δημιουργήστε ένα αρχείο _app.py_ και δώστε του τον παρακάτω κώδικα:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # πρόσθεσε τον κώδικα ολοκλήρωσής σου
   prompt = "Complete the following: Once upon a time there was a"

   # κάνε ένα αίτημα χρησιμοποιώντας το API των Απαντήσεων
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # εκτύπωσε την απάντηση
   print(response.output_text)
   ```

   > [!NOTE]
   > Εάν χρησιμοποιείτε το απλό OpenAI (όχι Azure), χρησιμοποιήστε `client = OpenAI(api_key="<αντικαταστήστε αυτή την τιμή με το κλειδί OpenAI>")` (χωρίς `base_url`) και περάστε ένα όνομα μοντέλου όπως `gpt-4o-mini` αντί για όνομα ανάπτυξης.

   Θα δείτε μια έξοδο όπως η παρακάτω:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Διαφορετικοί τύποι prompts, για διάφορα πράγματα

Τώρα που είδατε πώς να δημιουργείτε κείμενο χρησιμοποιώντας ένα prompt. Έχετε ακόμη ένα πρόγραμμα σε λειτουργία που μπορείτε να τροποποιήσετε και να αλλάξετε για να παράγετε διαφορετικά είδη κειμένου.

Τα prompts μπορούν να χρησιμοποιηθούν για διάφορες εργασίες. Για παράδειγμα:

- **Παράγετε έναν τύπο κειμένου**. Για παράδειγμα, μπορείτε να παράγετε ένα ποίημα, ερωτήσεις για ένα κουίζ κτλ.
- **Αναζητήστε πληροφορίες**. Μπορείτε να χρησιμοποιήσετε prompts για να αναζητήσετε πληροφορίες όπως το παράδειγμα «Τι σημαίνει CORS στην ανάπτυξη ιστοσελίδων;».
- **Παράγετε κώδικα**. Μπορείτε να χρησιμοποιήσετε prompts για να δημιουργήσετε κώδικα, π.χ. να αναπτύξετε μια κανονική έκφραση που χρησιμοποιείται για να ελέγξει emails ή γιατί όχι να δημιουργήσετε ολόκληρο πρόγραμμα, όπως μια web εφαρμογή;

## Μια πιο πρακτική περίπτωση χρήσης: ένας γεννήτορας συνταγών

Φανταστείτε ότι έχετε υλικά στο σπίτι και θέλετε να μαγειρέψετε κάτι. Για αυτό χρειάζεστε μια συνταγή. Ένας τρόπος να βρείτε συνταγές είναι να χρησιμοποιήσετε μια μηχανή αναζήτησης ή θα μπορούσατε να χρησιμοποιήσετε ένα LLM.

Μπορείτε να γράψετε ένα prompt ως εξής:

> "Δείξε μου 5 συνταγές για ένα πιάτο με τα εξής υλικά: κοτόπουλο, πατάτες και καρότα. Για κάθε συνταγή, απαριθμήστε όλα τα υλικά που χρησιμοποιούνται"

Δεδομένου του παραπάνω prompt, ίσως λάβετε μια απάντηση παρόμοια με:

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

Αυτό το αποτέλεσμα είναι εξαιρετικό, ξέρω τι να μαγειρέψω. Σε αυτό το σημείο, χρήσιμες βελτιώσεις μπορεί να είναι:

- Φιλτράρισμα υλικών που δεν μου αρέσουν ή είμαι αλλεργικός σε αυτά.
- Δημιουργία λίστας αγορών, σε περίπτωση που δεν έχω όλα τα υλικά στο σπίτι.

Για τις παραπάνω περιπτώσεις, ας προσθέσουμε ένα επιπλέον prompt:

> "Παρακαλώ αφαιρέστε τις συνταγές με σκόρδο καθώς είμαι αλλεργικός και αντικαταστήστε το με κάτι άλλο. Επίσης, παρακαλώ δημιουργήστε μια λίστα αγορών για τις συνταγές, λαμβάνοντας υπόψη ότι έχω ήδη κοτόπουλο, πατάτες και καρότα στο σπίτι."

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

Αυτές είναι οι πέντε συνταγές σας, χωρίς να αναφέρεται σκόρδο και επίσης έχετε μια λίστα αγορών λαμβάνοντας υπόψη τι έχετε ήδη στο σπίτι.

## Άσκηση - δημιουργήστε έναν γεννήτορα συνταγών

Τώρα που έχουμε περιγράψει ένα σενάριο, ας γράψουμε κώδικα που ταιριάζει με το παρουσιασμένο σενάριο. Για να το κάνετε αυτό, ακολουθήστε τα βήματα:

1. Χρησιμοποιήστε το υπάρχον αρχείο _app.py_ ως σημείο εκκίνησης
1. Εντοπίστε τη μεταβλητή `prompt` και αλλάξτε τον κώδικά της ως εξής:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Εάν τώρα εκτελέσετε τον κώδικα, θα πρέπει να δείτε μια έξοδο παρόμοια με:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > ΣΗΜΕΙΩΣΗ, το LLM σας είναι μη ντετερμινιστικό, οπότε μπορεί να λάβετε διαφορετικά αποτελέσματα κάθε φορά που τρέχετε το πρόγραμμα.

   Τέλεια, ας δούμε πώς μπορούμε να βελτιώσουμε τα πράγματα. Για να βελτιώσουμε τα πράγματα, θέλουμε να διασφαλίσουμε ότι ο κώδικας είναι ευέλικτος, ώστε τα υλικά και ο αριθμός των συνταγών να μπορούν να βελτιωθούν και να αλλάξουν.

1. Ας αλλάξουμε τον κώδικα ως εξής:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # παρεμβάλλετε τον αριθμό των συνταγών στην προτροπή και τα συστατικά
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Ένα παράδειγμα για μια δοκιμαστική εκτέλεση του κώδικα μπορεί να είναι το εξής:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Βελτιώστε προσθέτοντας φίλτρο και λίστα αγορών

Τώρα έχουμε μια λειτουργική εφαρμογή ικανή να παράγει συνταγές και είναι ευέλικτη καθώς βασίζεται σε εισόδους από τον χρήστη, τόσο στον αριθμό των συνταγών όσο και στα χρησιμοποιούμενα υλικά.

Για περαιτέρω βελτίωση, θέλουμε να προσθέσουμε τα εξής:

- **Φιλτράρισμα υλικών**. Θέλουμε να μπορούμε να φιλτράρουμε υλικά που δεν μας αρέσουν ή είμαστε αλλεργικοί σε αυτά. Για να επιτύχουμε αυτή την αλλαγή, μπορούμε να επεξεργαστούμε το υπάρχον prompt και να προσθέσουμε μια συνθήκη φίλτρου στο τέλος του, ως εξής:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Από πάνω, προσθέτουμε το `{filter}` στο τέλος του prompt και επίσης λαμβάνουμε την τιμή του φίλτρου από τον χρήστη.

  Ένα παράδειγμα εισόδου κατά την εκτέλεση του προγράμματος μπορεί τώρα να μοιάζει με:

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

  Όπως βλέπετε, οποιεσδήποτε συνταγές με γάλα έχουν φιλτραριστεί. Όμως, αν είστε δυσανεκτικός στη λακτόζη, ίσως θέλετε επίσης να φιλτράρετε συνταγές με τυρί, οπότε χρειάζεται να είστε σαφείς.


- **Δημιουργήστε μια λίστα αγορών**. Θέλουμε να δημιουργήσουμε μια λίστα αγορών, λαμβάνοντας υπόψη τι έχουμε ήδη στο σπίτι.

  Για αυτή τη λειτουργία, θα μπορούσαμε είτε να προσπαθήσουμε να λύσουμε τα πάντα σε ένα prompt είτε να το χωρίσουμε σε δύο prompts. Ας δοκιμάσουμε τη δεύτερη προσέγγιση. Εδώ προτείνουμε να προσθέσουμε ένα επιπλέον prompt, αλλά για να λειτουργήσει αυτό, πρέπει να προσθέσουμε το αποτέλεσμα του πρώτου prompt ως πλαίσιο στο δεύτερο prompt.

  Εντοπίστε το σημείο στον κώδικα που τυπώνει το αποτέλεσμα από το πρώτο prompt και προσθέστε τον ακόλουθο κώδικα παρακάτω:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # εκτύπωση απόκρισης
  print("Shopping list:")
  print(response.output_text)
  ```

  Σημειώστε τα εξής:

  1. Κατασκευάζουμε ένα νέο prompt προσθέτοντας το αποτέλεσμα από το πρώτο prompt στο νέο prompt:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Κάνουμε ένα νέο αίτημα, αλλά λαμβάνοντας επίσης υπόψη τον αριθμό των tokens που ζητήσαμε στο πρώτο prompt, έτσι αυτή τη φορά λέμε `max_output_tokens` είναι 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Δοκιμάζοντας αυτόν τον κώδικα, καταλήγουμε τώρα στην παρακάτω έξοδο:

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

Αυτό που έχουμε μέχρι στιγμής είναι κώδικας που δουλεύει, αλλά υπάρχουν μερικές διορθώσεις που θα πρέπει να κάνουμε για να βελτιώσουμε τα πράγματα περαιτέρω. Κάποια πράγματα που πρέπει να κάνουμε είναι:

- **Διαχωρίστε μυστικά από τον κώδικα**, όπως το API key. Τα μυστικά δεν ανήκουν στον κώδικα και θα πρέπει να αποθηκεύονται σε ασφαλή τοποθεσία. Για να διαχωρίσουμε τα μυστικά από τον κώδικα, μπορούμε να χρησιμοποιήσουμε μεταβλητές περιβάλλοντος και βιβλιοθήκες όπως το `python-dotenv` για να τα φορτώσουμε από ένα αρχείο. Δείτε πώς θα φαίνεται αυτό στον κώδικα:

  1. Δημιουργήστε ένα αρχείο `.env` με το εξής περιεχόμενο:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Σημείωση, για το Azure OpenAI στο Microsoft Foundry, πρέπει αντ' αυτού να ορίσετε τις ακόλουθες μεταβλητές περιβάλλοντος:

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

- **Μια λέξη για το μήκος των tokens**. Πρέπει να σκεφτούμε πόσα tokens χρειαζόμαστε για να δημιουργήσουμε το κείμενο που θέλουμε. Τα tokens κοστίζουν χρήματα, οπότε όπου είναι δυνατόν, θα πρέπει να προσπαθούμε να είμαστε οικονομικοί με τον αριθμό των tokens που χρησιμοποιούμε. Για παράδειγμα, μπορούμε να διατυπώσουμε το prompt έτσι ώστε να χρησιμοποιούμε λιγότερα tokens;

  Για να αλλάξετε τα χρησιμοποιηθέντα tokens, μπορείτε να χρησιμοποιήσετε την παράμετρο `max_output_tokens`. Για παράδειγμα, αν θέλετε να χρησιμοποιήσετε 100 tokens, θα κάνατε:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Πειραματισμός με τη θερμοκρασία**. Η θερμοκρασία είναι κάτι που δεν έχουμε αναφέρει μέχρι στιγμής αλλά είναι ένα σημαντικό πλαίσιο για το πώς αποδίδει το πρόγραμμα μας. Όσο υψηλότερη είναι η τιμή της θερμοκρασίας, τόσο πιο τυχαία θα είναι η έξοδος. Αντίθετα, όσο χαμηλότερη είναι η τιμή της θερμοκρασίας, τόσο πιο προβλέψιμη θα είναι η έξοδος. Σκεφτείτε αν θέλετε ποικιλία στην έξοδό σας ή όχι.

  Για να αλλάξετε τη θερμοκρασία, μπορείτε να χρησιμοποιήσετε την παράμετρο `temperature`. Για παράδειγμα, αν θέλετε να χρησιμοποιήσετε θερμοκρασία 0.5, θα κάνατε:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Σημείωση, όσο πιο κοντά στο 1.0, τόσο πιο ποικίλη είναι η έξοδος.

## Αποστολή

Για αυτή την αποστολή, μπορείτε να επιλέξετε τι θέλετε να φτιάξετε.

Εδώ είναι μερικές προτάσεις:

- Τροποποιήστε την εφαρμογή δημιουργίας συνταγών για να την βελτιώσετε ακόμη περισσότερο. Πειραματιστείτε με τιμές θερμοκρασίας και τα prompts για να δείτε τι μπορείτε να δημιουργήσετε.
- Δημιουργήστε ένα "σύντροφο μελέτης". Αυτή η εφαρμογή θα πρέπει να μπορεί να απαντά σε ερωτήσεις σχετικά με ένα θέμα, για παράδειγμα Python, θα μπορούσατε να έχετε prompts όπως "Τι είναι ένα συγκεκριμένο θέμα στην Python;", ή θα μπορούσατε να έχετε ένα prompt που να λέει, δείξε μου κώδικα για ένα συγκεκριμένο θέμα κ.λπ.
- Ιστορικό bot, κάντε την ιστορία να ζωντανέψει, δώστε εντολή στο bot να υποδυθεί έναν συγκεκριμένο ιστορικό χαρακτήρα και ρωτήστε το ερωτήσεις για τη ζωή και την εποχή του.

## Λύση

### Σύντροφος μελέτης

Παρακάτω είναι ένα αρχικό prompt, δείτε πώς μπορείτε να το χρησιμοποιήσετε και να το τροποποιήσετε κατά βούληση.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Ιστορικό bot

Εδώ είναι μερικά prompts που θα μπορούσατε να χρησιμοποιήσετε:

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

Όταν εργάζεστε στην αποστολή, προσπαθήστε να διαφοροποιήσετε τη θερμοκρασία, δοκιμάζοντας να την ορίσετε σε 0, 0.5, και 1. Θυμηθείτε ότι το 0 είναι η λιγότερη ποικιλία και το 1 η περισσότερη. Ποια τιμή λειτουργεί καλύτερα για την εφαρμογή σας;

## Μεγάλη δουλειά! Συνεχίστε τη μάθηση σας

Μετά την ολοκλήρωση αυτού του μαθήματος, ρίξτε μια ματιά στη [Συλλογή μάθησης για Γεννητική Τεχνητή Νοημοσύνη](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) για να συνεχίσετε να εξελίσσετε τις γνώσεις σας στη Γεννητική Τεχνητή Νοημοσύνη!

Πηγαίνετε στο Μάθημα 7 όπου θα δούμε πώς να [δημιουργούμε εφαρμογές συνομιλίας](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->