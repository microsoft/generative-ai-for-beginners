# Δημιουργία Εφαρμογών Δημιουργίας Κειμένου

[![Δημιουργία Εφαρμογών Δημιουργίας Κειμένου](../../../translated_images/el/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Κάντε κλικ στην παραπάνω εικόνα για να δείτε το βίντεο αυτού του μαθήματος)_

Έχετε δει μέχρι τώρα σε αυτό το πρόγραμμα σπουδών ότι υπάρχουν θεμελιώδεις έννοιες όπως οι προτροπές και ακόμη και ολόκληρος κλάδος που ονομάζεται "μηχανική προτροπών". Πολλά εργαλεία με τα οποία μπορείτε να αλληλεπιδράσετε όπως το ChatGPT, το Office 365, η Microsoft Power Platform και άλλα, σας υποστηρίζουν χρησιμοποιώντας προτροπές για να επιτύχετε κάτι.

Για να προσθέσετε μια τέτοια εμπειρία σε μια εφαρμογή, πρέπει να κατανοήσετε έννοιες όπως προτροπές, ολοκληρώσεις και να επιλέξετε μια βιβλιοθήκη για να εργαστείτε μαζί της. Αυτό ακριβώς θα μάθετε σε αυτό το κεφάλαιο.

## Εισαγωγή

Σε αυτό το κεφάλαιο, θα:

- Μάθετε για τη βιβλιοθήκη openai και τις βασικές της έννοιες.
- Δημιουργήσετε μια εφαρμογή δημιουργίας κειμένου χρησιμοποιώντας το openai.
- Κατανοήσετε πώς να χρησιμοποιείτε έννοιες όπως η προτροπή, η θερμοκρασία και τα tokens για να δημιουργήσετε μια εφαρμογή δημιουργίας κειμένου.

## Στόχοι μάθησης

Στο τέλος αυτού του μαθήματος, θα μπορείτε να:

- Εξηγήσετε τι είναι μια εφαρμογή δημιουργίας κειμένου.
- Δημιουργήσετε μια εφαρμογή δημιουργίας κειμένου χρησιμοποιώντας το openai.
- Διαμορφώσετε την εφαρμογή σας ώστε να χρησιμοποιεί περισσότερα ή λιγότερα tokens και επίσης να αλλάξετε τη θερμοκρασία, για ένα ποικίλο αποτέλεσμα.

## Τι είναι μια εφαρμογή δημιουργίας κειμένου;

Κανονικά όταν δημιουργείτε μια εφαρμογή έχει κάποιο είδος διεπαφής όπως η ακόλουθη:

- Βασισμένη σε εντολές. Οι εφαρμογές κονσόλας είναι τυπικές εφαρμογές όπου πληκτρολογείτε μια εντολή και εκτελεί κάποια εργασία. Για παράδειγμα, `git` είναι μια εφαρμογή βασισμένη σε εντολές.
- Γραφική διεπαφή χρήστη (UI). Κάποιες εφαρμογές έχουν γραφικές διεπαφές (GUIs) όπου κάνετε κλικ σε κουμπιά, εισάγετε κείμενο, επιλέγετε επιλογές και άλλα.

### Οι εφαρμογές κονσόλας και UI έχουν περιορισμούς

Συγκρίνετε το με μια εφαρμογή βασισμένη σε εντολές όπου πληκτρολογείτε μια εντολή:

- **Έχει περιορισμούς**. Δεν μπορείτε απλώς να πληκτρολογήσετε όποια εντολή θέλετε, μόνο αυτές που υποστηρίζει η εφαρμογή.
- **Ειδική γλώσσα**. Κάποιες εφαρμογές υποστηρίζουν πολλές γλώσσες, αλλά από προεπιλογή η εφαρμογή είναι κατασκευασμένη για μια συγκεκριμένη γλώσσα, ακόμα κι αν μπορείτε να προσθέσετε επιπλέον υποστήριξη γλωσσών.

### Οφέλη των εφαρμογών δημιουργίας κειμένου

Πώς λοιπόν διαφέρει μια εφαρμογή δημιουργίας κειμένου;

Σε μια εφαρμογή δημιουργίας κειμένου, έχετε μεγαλύτερη ευελιξία, δεν περιορίζεστε σε ένα σύνολο εντολών ή σε μια συγκεκριμένη γλώσσα εισόδου. Αντίθετα, μπορείτε να χρησιμοποιήσετε φυσική γλώσσα για να αλληλεπιδράσετε με την εφαρμογή. Ένα ακόμη όφελος είναι ότι ήδη αλληλεπιδράτε με μια πηγή δεδομένων που έχει εκπαιδευτεί σε ένα τεράστιο σώμα πληροφοριών, ενώ μια παραδοσιακή εφαρμογή μπορεί να είναι περιορισμένη στα δεδομένα μιας βάσης δεδομένων.

### Τι μπορώ να δημιουργήσω με μια εφαρμογή δημιουργίας κειμένου;

Μπορείτε να δημιουργήσετε πολλά πράγματα. Για παράδειγμα:

- **Ένα chatbot**. Ένα chatbot που απαντά σε ερωτήσεις σχετικά με θέματα, όπως η εταιρεία σας και τα προϊόντα της, θα μπορούσε να είναι μια καλή επιλογή.
- **Βοηθός**. Τα LLMs είναι εξαιρετικά σε πράγματα όπως η περίληψη κειμένου, η εξαγωγή πληροφοριών από κείμενο, η παραγωγή κειμένου όπως βιογραφικά και πολλά άλλα.
- **Βοηθός κώδικα**. Ανάλογα με το μοντέλο γλώσσας που χρησιμοποιείτε, μπορείτε να δημιουργήσετε έναν βοηθό κώδικα που θα σας βοηθά να γράφετε κώδικα. Για παράδειγμα, μπορείτε να χρησιμοποιήσετε ένα προϊόν όπως το GitHub Copilot καθώς και το ChatGPT για να σας βοηθήσουν να γράψετε κώδικα.

## Πώς μπορώ να ξεκινήσω;

Λοιπόν, πρέπει να βρείτε έναν τρόπο να ενσωματωθείτε με ένα LLM που συνήθως περιλαμβάνει τις ακόλουθες δύο προσεγγίσεις:

- Χρησιμοποιείστε ένα API. Εδώ κατασκευάζετε αιτήσεις web με την προτροπή σας και λαμβάνετε πίσω το παραγόμενο κείμενο.
- Χρησιμοποιείστε μια βιβλιοθήκη. Οι βιβλιοθήκες βοηθούν να εγκιβωτίσετε τις κλήσεις API και να τις κάνετε πιο εύκολες στη χρήση.

## Βιβλιοθήκες/SDKs

Υπάρχουν μερικές γνωστές βιβλιοθήκες για εργασία με LLMs όπως:

- **openai**, αυτή η βιβλιοθήκη καθιστά εύκολη τη σύνδεση με το μοντέλο σας και την αποστολή προτροπών.

Στη συνέχεια, υπάρχουν βιβλιοθήκες που λειτουργούν σε υψηλότερο επίπεδο, όπως:

- **Langchain**. Το Langchain είναι γνωστό και υποστηρίζει Python.
- **Semantic Kernel**. Το Semantic Kernel είναι μια βιβλιοθήκη της Microsoft που υποστηρίζει τις γλώσσες C#, Python και Java.

## Πρώτη εφαρμογή χρησιμοποιώντας openai

Ας δούμε πώς μπορούμε να δημιουργήσουμε την πρώτη μας εφαρμογή, ποιες βιβλιοθήκες χρειαζόμαστε, πόσα απαιτούνται και ούτω καθεξής.

### Εγκατάσταση του openai

Υπάρχουν πολλές βιβλιοθήκες για αλληλεπίδραση με το OpenAI ή το Azure OpenAI. Είναι δυνατό να χρησιμοποιηθούν πολλές γλώσσες προγραμματισμού όπως C#, Python, JavaScript, Java και άλλες. Επιλέξαμε να χρησιμοποιήσουμε τη βιβλιοθήκη Python `openai`, οπότε θα χρησιμοποιήσουμε το `pip` για να την εγκαταστήσουμε.

```bash
pip install openai
```

### Δημιουργία πόρου

Πρέπει να ακολουθήσετε τα παρακάτω βήματα:

- Δημιουργήστε έναν λογαριασμό στο Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Αποκτήστε πρόσβαση στο Azure OpenAI. Πηγαίνετε στο [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) και ζητήστε πρόσβαση.

  > [!NOTE]
  > Τη στιγμή που γράφεται αυτό, πρέπει να κάνετε αίτηση για πρόσβαση στο Azure OpenAI.

- Εγκαταστήστε Python <https://www.python.org/>
- Έχετε δημιουργήσει έναν πόρο Azure OpenAI Service. Δείτε αυτόν τον οδηγό για το πώς να [δημιουργήσετε πόρο](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Εντοπισμός κλειδιού API και τερματικού σημείου

Σε αυτό το σημείο, πρέπει να πείτε στη βιβλιοθήκη `openai` ποιο κλειδί API να χρησιμοποιήσει. Για να βρείτε το κλειδί API σας, πηγαίνετε στην ενότητα "Κλειδιά και Τερματικά Σημεία" του πόρου Azure OpenAI και αντιγράψτε την τιμή "Key 1".

![Λεπίδα πόρου Κλειδιά και Τερματικό στο Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Τώρα που έχετε αντιγράψει αυτές τις πληροφορίες, ας δώσουμε οδηγίες στις βιβλιοθήκες να τις χρησιμοποιήσουν.

> [!NOTE]
> Αξίζει να αποχωρίσετε το κλειδί API από τον κώδικα σας. Μπορείτε να το κάνετε χρησιμοποιώντας μεταβλητές περιβάλλοντος.
>
> - Ορίστε τη μεταβλητή περιβάλλοντος `OPENAI_API_KEY` στο κλειδί API σας.
>   `export OPENAI_API_KEY='sk-...'`

### Ρύθμιση διαμόρφωσης Azure

Εάν χρησιμοποιείτε το Azure OpenAI (που τώρα είναι μέρος της Microsoft Foundry), ορίστε πώς να ρυθμίσετε τη διαμόρφωση. Χρησιμοποιούμε τον τυπικό πελάτη `OpenAI` στρεφόμενο στο τερματικό σημείο Azure OpenAI `/openai/v1/`, που λειτουργεί με το Responses API και δεν χρειάζεται `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Ανωτέρω ορίζουμε τα εξής:

- `api_key`, αυτό είναι το κλειδί API που βρίσκετε στο Azure Portal ή στο Microsoft Foundry portal.
- `base_url`, αυτό είναι το τερματικό σημείο του Foundry πόρου σας με `/openai/v1/` προσαρτημένο. Το σταθερό τερματικό v1 λειτουργεί μεταξύ OpenAI και Azure OpenAI χωρίς διαχείριση `api_version`.

> [!NOTE] > `os.environ` διαβάζει μεταβλητές περιβάλλοντος. Μπορείτε να το χρησιμοποιήσετε για να διαβάσετε μεταβλητές περιβάλλοντος όπως `AZURE_OPENAI_API_KEY` και `AZURE_OPENAI_ENDPOINT`. Ορίστε αυτές τις μεταβλητές περιβάλλοντος στο τερματικό σας ή χρησιμοποιώντας μια βιβλιοθήκη όπως `dotenv`.

## Δημιουργία κειμένου

Ο τρόπος να δημιουργήσετε κείμενο είναι να χρησιμοποιήσετε το Responses API μέσω της μεθόδου `responses.create`. Να ένα παράδειγμα:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

Στον παραπάνω κώδικα, δημιουργούμε μια απόκριση και περνάμε το μοντέλο που θέλουμε να χρησιμοποιήσουμε και την προτροπή. Στη συνέχεια τυπώνουμε το παραγόμενο κείμενο μέσω `response.output_text`.

### Συνομιλίες πολλαπλών γύρων

Το Responses API είναι κατάλληλο τόσο για δημιουργία κειμένου ενός γύρου όσο και για chatbots πολλαπλών γύρων — παρέχετε μια λίστα μηνυμάτων στο `input` για να δημιουργήσετε μια συνομιλία:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Περισσότερα γι' αυτή τη λειτουργικότητα σε ένα επερχόμενο κεφάλαιο.

## Άσκηση - η πρώτη σας εφαρμογή δημιουργίας κειμένου

Τώρα που μάθαμε πώς να ρυθμίσουμε και να διαμορφώσουμε το openai, είναι ώρα να δημιουργήσετε την πρώτη σας εφαρμογή δημιουργίας κειμένου. Για να δημιουργήσετε την εφαρμογή σας, ακολουθήστε τα εξής βήματα:

1. Δημιουργήστε ένα εικονικό περιβάλλον και εγκαταστήστε το openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Εάν χρησιμοποιείτε Windows πληκτρολογήστε `venv\Scripts\activate` αντί για `source venv/bin/activate`.

   > [!NOTE]
   > Βρείτε το κλειδί Azure OpenAI πηγαίνοντας στο [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), αναζητήστε `Open AI`, επιλέξτε το `Open AI resource` και στη συνέχεια επιλέξτε `Keys and Endpoint` και αντιγράψτε την τιμή `Key 1`.

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
   > Εάν χρησιμοποιείτε το απλό OpenAI (όχι Azure), χρησιμοποιήστε `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (χωρίς `base_url`) και δώστε ένα όνομα μοντέλου όπως `gpt-5-mini` αντί για όνομα ανάπτυξης.

   Θα δείτε μια έξοδο σαν την ακόλουθη:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Διάφοροι τύποι προτροπών, για διαφορετικά πράγματα

Τώρα έχετε δει πώς να δημιουργείτε κείμενο χρησιμοποιώντας μια προτροπή. Έχετε και ένα πρόγραμμα που τρέχει και μπορείτε να το τροποποιήσετε και να το αλλάξετε για να δημιουργήσετε διαφορετικούς τύπους κειμένου.

Οι προτροπές μπορούν να χρησιμοποιηθούν για διάφορες εργασίες. Για παράδειγμα:

- **Να δημιουργήσετε έναν τύπο κειμένου**. Για παράδειγμα, μπορείτε να δημιουργήσετε ένα ποίημα, ερωτήσεις για ένα κουίζ κ.ά.
- **Αναζήτηση πληροφοριών**. Μπορείτε να χρησιμοποιήσετε προτροπές για να αναζητήσετε πληροφορίες όπως το παράδειγμα "Τι σημαίνει CORS στην ανάπτυξη ιστού;".
- **Δημιουργία κώδικα**. Μπορείτε να χρησιμοποιήσετε προτροπές για να δημιουργήσετε κώδικα, για παράδειγμα εξελίσσοντας μια κανονική έκφραση που χρησιμοποιείται για την επικύρωση email ή γιατί όχι να δημιουργήσετε ολόκληρο πρόγραμμα, όπως μια web εφαρμογή;

## Μια πιο πρακτική περίπτωση χρήσης: γεννήτρια συνταγών

Φανταστείτε ότι έχετε υλικά στο σπίτι και θέλετε να μαγειρέψετε κάτι. Για αυτό χρειάζεστε μια συνταγή. Ένας τρόπος να βρείτε συνταγές είναι να χρησιμοποιήσετε μια μηχανή αναζήτησης ή θα μπορούσατε να χρησιμοποιήσετε ένα LLM γι' αυτό.

Μπορείτε να γράψετε μια προτροπή ως εξής:

> "Δείξε μου 5 συνταγές για ένα πιάτο με τα ακόλουθα υλικά: κοτόπουλο, πατάτες και καρότα. Ανά συνταγή, απαριθμήστε όλα τα υλικά που χρησιμοποιούνται"

Με την παραπάνω προτροπή, μπορεί να λάβετε μια απάντηση παρόμοια με:

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

Αυτό το αποτέλεσμα είναι υπέροχο, ξέρω τι να μαγειρέψω. Σε αυτό το σημείο, χρήσιμες βελτιώσεις θα μπορούσαν να είναι:

- Φιλτράρισμα υλικών που δεν μου αρέσουν ή έχω αλλεργία.
- Δημιουργία λίστας αγορών, σε περίπτωση που δεν έχω όλα τα υλικά στο σπίτι.

Για τις παραπάνω περιπτώσεις, ας προσθέσουμε μια επιπλέον προτροπή:

> "Παρακαλώ αφαιρέστε τις συνταγές με σκόρδο, καθώς έχω αλλεργία, και αντικαταστήστε το με κάτι άλλο. Επίσης, παρακαλώ δημιουργήστε μια λίστα αγορών για τις συνταγές, λαμβάνοντας υπόψη ότι ήδη έχω κοτόπουλο, πατάτες και καρότα στο σπίτι."

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

Αυτές είναι οι πέντε συνταγές σας, χωρίς να αναφέρεται σκόρδο και έχετε επίσης μια λίστα αγορών λαμβάνοντας υπόψη τα ήδη υπάρχοντα υλικά στο σπίτι.

## Άσκηση - δημιουργία γεννήτριας συνταγών

Τώρα που έχουμε παίξει ένα σενάριο, ας γράψουμε κώδικα που να ταιριάζει στο παρουσιασμένο σενάριο. Για να το κάνετε αυτό, ακολουθήστε τα εξής βήματα:

1. Χρησιμοποιήστε το υπάρχον αρχείο _app.py_ ως σημείο εκκίνησης
1. Εντοπίστε τη μεταβλητή `prompt` και αλλάξτε τον κώδικά της ως εξής:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Τώρα, αν τρέξετε τον κώδικα, θα πρέπει να δείτε μια έξοδο παρόμοια με:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > ΣΗΜΕΙΩΣΗ, το LLM σας είναι μη ντετερμινιστικό, οπότε μπορεί να έχετε διαφορετικά αποτελέσματα κάθε φορά που τρέχετε το πρόγραμμα.

   Υπέροχα, ας δούμε πώς μπορούμε να βελτιώσουμε τα πράγματα. Για να βελτιώσουμε τα πράγματα, θέλουμε να βεβαιωθούμε ότι ο κώδικας είναι ευέλικτος, ώστε τα υλικά και ο αριθμός των συνταγών να μπορούν να βελτιωθούν και να αλλάξουν.

1. Ας αλλάξουμε τον κώδικα ως εξής:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Η λήψη αυτού του κώδικα για μια δοκιμαστική εκτέλεση, μπορεί να μοιάζει ως εξής:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Βελτίωση με προσθήκη φίλτρου και λίστας αγορών

Τώρα έχουμε μια λειτουργική εφαρμογή ικανή να παράγει συνταγές και είναι ευέλικτη καθώς βασίζεται σε εισροές από τον χρήστη, τόσο στον αριθμό των συνταγών όσο και στα χρησιμοποιούμενα υλικά.

Για περαιτέρω βελτίωση, θέλουμε να προσθέσουμε τα εξής:

- **Φίλτρο υλικών**. Θέλουμε να μπορούμε να φιλτράρουμε υλικά που δεν μας αρέσουν ή έχουμε αλλεργία. Για να επιτύχουμε αυτή την αλλαγή, μπορούμε να επεξεργαστούμε την υπάρχουσα προτροπή και να προσθέσουμε μια συνθήκη φίλτρου στο τέλος της ως εξής:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Ανωτέρω, προσθέτουμε το `{filter}` στο τέλος της προτροπής και επίσης λαμβάνουμε την τιμή φίλτρου από τον χρήστη.

  Ένα παράδειγμα εισαγωγής κατά την εκτέλεση του προγράμματος μπορεί τώρα να μοιάζει ως εξής:

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

  Όπως βλέπετε, οποιεσδήποτε συνταγές με γάλα έχουν φιλτραριστεί. Αν, όμως, έχετε δυσανεξία στη λακτόζη, μπορεί να θέλετε να φιλτράρετε συνταγές με τυρί επίσης, έτσι χρειάζεστε να είστε σαφείς.

- **Παραγωγή λίστας αγορών**. Θέλουμε να παράγουμε μια λίστα αγορών, λαμβάνοντας υπόψη τα υλικά που έχουμε ήδη στο σπίτι.

  Για αυτή τη λειτουργικότητα, θα μπορούσαμε είτε να προσπαθήσουμε να λύσουμε τα πάντα σε μια προτροπή, είτε να τη χωρίσουμε σε δύο προτροπές. Ας δοκιμάσουμε τη δεύτερη προσέγγιση. Εδώ προτείνουμε να προσθέσουμε μια επιπλέον προτροπή, αλλά για να λειτουργήσει αυτό, πρέπει να προσθέσουμε το αποτέλεσμα της πρώτης προτροπής ως πλαίσιο στη δεύτερη προτροπή.

  Εντοπίστε το σημείο στον κώδικα που τυπώνει το αποτέλεσμα από την πρώτη προτροπή και προσθέστε τον ακόλουθο κώδικα παρακάτω:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Σημειώστε τα παρακάτω:

  1. Κατασκευάζουμε μια νέα προτροπή προσθέτοντας το αποτέλεσμα από την πρώτη προτροπή στη νέα προτροπή:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Κάνουμε νέο αίτημα, αλλά επίσης λαμβάνοντας υπόψη τον αριθμό των tokens που ζητήσαμε στην πρώτη προτροπή, έτσι αυτή τη φορά λέμε ότι `max_output_tokens` είναι 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Με την εκτέλεση αυτού του κώδικα, τώρα φτάνουμε στην ακόλουθη έξοδο:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Βελτιώστε το περιβάλλον σας

Αυτό που έχουμε μέχρι στιγμής είναι κώδικας που λειτουργεί, αλλά υπάρχουν μερικές βελτιώσεις που θα πρέπει να κάνουμε για να βελτιώσουμε τα πράγματα περαιτέρω. Κάποια πράγματα που θα πρέπει να κάνουμε είναι:

- **Διαχωρίστε τα μυστικά από τον κώδικα**, όπως το κλειδί API. Τα μυστικά δεν ανήκουν στον κώδικα και θα πρέπει να αποθηκεύονται σε ασφαλή τοποθεσία. Για να διαχωρίσουμε τα μυστικά από τον κώδικα, μπορούμε να χρησιμοποιήσουμε μεταβλητές περιβάλλοντος και βιβλιοθήκες όπως η `python-dotenv` για να τις φορτώνουμε από ένα αρχείο. Να πώς θα μοιάζει αυτό στον κώδικα:

  1. Δημιουργήστε ένα αρχείο `.env` με το ακόλουθο περιεχόμενο:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Σημείωση, για το Azure OpenAI στο Microsoft Foundry, πρέπει να ορίσετε τις ακόλουθες μεταβλητές περιβάλλοντος αντ' αυτού:

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

- **Μια λέξη για το μήκος των τοκενς**. Πρέπει να εξετάσουμε πόσα τοκενς χρειάζονται για να δημιουργήσουμε το κείμενο που θέλουμε. Τα τοκενς κοστίζουν χρήματα, οπότε όπου είναι δυνατόν, πρέπει να προσπαθούμε να είμαστε οικονομικοί με τον αριθμό των τοκενς που χρησιμοποιούμε. Για παράδειγμα, μπορούμε να διατυπώσουμε την ερώτηση έτσι ώστε να χρησιμοποιήσουμε λιγότερα τοκενς;

  Για να αλλάξετε τα τοκενς που χρησιμοποιούνται, μπορείτε να χρησιμοποιήσετε την παράμετρο `max_output_tokens`. Για παράδειγμα, αν θέλετε να χρησιμοποιήσετε 100 τοκενς, θα κάνατε:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Πειραματισμός με τη θερμοκρασία**. Η θερμοκρασία είναι κάτι που δεν έχουμε αναφέρει μέχρι τώρα, αλλά είναι ένα σημαντικό πλαίσιο για το πώς λειτουργεί το πρόγραμμά μας. Όσο υψηλότερη είναι η τιμή της θερμοκρασίας τόσο πιο τυχαίο θα είναι το αποτέλεσμα. Αντιστρόφως, όσο χαμηλότερη είναι η τιμή της θερμοκρασίας τόσο πιο προβλέψιμο θα είναι το αποτέλεσμα. Σκεφτείτε αν θέλετε παραλλαγή στο αποτέλεσμα ή όχι.

  Για να αλλάξετε τη θερμοκρασία, μπορείτε να χρησιμοποιήσετε την παράμετρο `temperature`. Για παράδειγμα, αν θέλετε να ορίσετε θερμοκρασία 0.5, θα κάνατε:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Σημείωση, όσο πιο κοντά στο 1.0, τόσο πιο ποικίλο είναι το αποτέλεσμα.

- **Τα μοντέλα συλλογισμού δεν χρησιμοποιούν `temperature`**. Αυτή είναι μια σημαντική αλλαγή για το 2026. Τα τρέχοντα, μη αποσυρμένα μοντέλα στο Microsoft Foundry είναι **μοντέλα συλλογισμού** (η οικογένεια GPT-5, ο-σειρά) - και **δεν υποστηρίζουν `temperature` ή `top_p`** (ούτε `max_tokens`· χρησιμοποιήστε `max_output_tokens`). Αν στείλετε `temperature` στο `gpt-5-mini` θα πάρετε σφάλμα "παράμετρος μη υποστηριζόμενη". Έτσι, για να δοκιμάσετε το παράδειγμα της θερμοκρασίας παραπάνω, δείξτε το σε ένα μοντέλο που εξακολουθεί να υποστηρίζει ελέγχους δειγματοληψίας - για παράδειγμα ένα ανοιχτό **Llama** μοντέλο όπως το `Llama-3.3-70B-Instruct` από τον [κατάλογο μοντέλων Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), που καλείται μέσω του Foundry Models / Azure AI Inference endpoint (με τον ίδιο τρόπο όπως τα `githubmodels-*` δείγματα). Για μοντέλα συλλογισμού όπως το GPT-5, κατευθύνετε την έξοδο διαφορετικά:
  - **Μηχανική προτροπών** - σαφείς οδηγίες, παραδείγματα, και δομημένη έξοδος (δείτε το μάθημα [04 - Μηχανική Προτροπών](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) κάνουν τη δουλειά που παλιότερα έκαναν τα κουμπιά δειγματοληψίας.
  - **Έλεγχοι συλλογισμού** - παράμετροι όπως η προσπάθεια/λεπτομέρεια συλλογισμού ανταλλάσσουν το βάθος συλλογισμού με τη λανθάνουσα κατάσταση και το κόστος.

  Συνοπτικά: `temperature`/`top_p` παραμένουν έγκυροι σε πολλά μοντέλα (Llama, Mistral, Phi, και η οικογένεια GPT-4.x - αν και το GPT-4.x καταργείται), αλλά η κατεύθυνση είναι μηχανική προτροπών + έλεγχοι συλλογισμού σε μοντέλα συλλογισμού όπως το GPT-5.

## Ανάθεση

Για αυτήν την ανάθεση, μπορείτε να επιλέξετε τι να κατασκευάσετε.

Εδώ είναι μερικές προτάσεις:

- Τροποποιήστε την εφαρμογή γεννήτριας συνταγών για να την βελτιώσετε περαιτέρω. Πειραματιστείτε με τις τιμές θερμοκρασίας και τις προτροπές για να δείτε τι μπορείτε να δημιουργήσετε.
- Δημιουργήστε έναν "συμμαθητή". Αυτή η εφαρμογή θα πρέπει να μπορεί να απαντά σε ερωτήσεις για ένα θέμα, για παράδειγμα Python, θα μπορούσατε να έχετε προτροπές όπως "Τι είναι ένα συγκεκριμένο θέμα στην Python;", ή να έχετε μια προτροπή που λέει, δείξε μου κώδικα για ένα συγκεκριμένο θέμα κτλ.
- Ιστορικό bot, κάντε την ιστορία να ζωντανέψει, δώστε εντολές στο bot να υποδυθεί έναν συγκεκριμένο ιστορικό χαρακτήρα και ρωτήστε το για τη ζωή και τους καιρούς του.

## Λύση

### Συμμαθητής

Παρακάτω είναι μια αρχική προτροπή, δείτε πώς μπορείτε να τη χρησιμοποιήσετε και να την τροποποιήσετε κατά το κέφι σας.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Ιστορικό bot

Εδώ είναι μερικές προτροπές που μπορείτε να χρησιμοποιήσετε:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Έλεγχος γνώσης

Τι κάνει η έννοια της θερμοκρασίας;

1. Ελέγχει πόσο τυχαία είναι η έξοδος.
1. Ελέγχει πόσο μεγάλη είναι η απάντηση.
1. Ελέγχει πόσοι τοκέν χρησιμοποιούνται.

## 🚀 Πρόκληση

Όταν εργάζεστε στην ανάθεση, δοκιμάστε να μεταβάλλετε τη θερμοκρασία, δοκιμάστε να την ορίσετε σε 0, 0.5 και 1. Θυμηθείτε ότι το 0 είναι το λιγότερο ποικιλόμορφο και το 1 το πιο πολύ. Ποια τιμή λειτουργεί καλύτερα για την εφαρμογή σας;

## Μπράβο! Συνεχίστε τη Μάθησή σας

Μετά την ολοκλήρωση αυτού του μαθήματος, ρίξτε μια ματιά στη [συλλογή μαθημάτων για Γενετική Τεχνητή Νοημοσύνη](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) για να συνεχίσετε να αναβαθμίζετε τις γνώσεις σας στη Γενετική ΤΝ!

Πηγαίνετε στο Μάθημα 7 όπου θα δούμε πώς να [δημιουργούμε εφαρμογές συνομιλίας](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->