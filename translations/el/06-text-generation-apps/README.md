<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-05-19T16:56:59+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "el"
}
-->
# Δημιουργία Εφαρμογών Γενιάς Κειμένου

> _(Κάντε κλικ στην εικόνα παραπάνω για να δείτε το βίντεο αυτού του μαθήματος)_

Έχετε δει μέχρι τώρα μέσω αυτού του προγράμματος σπουδών ότι υπάρχουν βασικές έννοιες όπως τα prompts και ακόμη μια ολόκληρη επιστήμη που ονομάζεται "prompt engineering". Πολλά εργαλεία με τα οποία μπορείτε να αλληλεπιδράσετε όπως το ChatGPT, το Office 365, το Microsoft Power Platform και άλλα, σας υποστηρίζουν στη χρήση prompts για να πετύχετε κάτι.

Για να προσθέσετε μια τέτοια εμπειρία σε μια εφαρμογή, πρέπει να κατανοήσετε έννοιες όπως τα prompts, τις ολοκληρώσεις και να επιλέξετε μια βιβλιοθήκη για να δουλέψετε. Αυτό ακριβώς θα μάθετε σε αυτό το κεφάλαιο.

## Εισαγωγή

Σε αυτό το κεφάλαιο, θα:

- Μάθετε για τη βιβλιοθήκη openai και τις βασικές της έννοιες.
- Δημιουργήσετε μια εφαρμογή γενιάς κειμένου χρησιμοποιώντας το openai.
- Κατανοήσετε πώς να χρησιμοποιήσετε έννοιες όπως prompt, θερμοκρασία και tokens για να δημιουργήσετε μια εφαρμογή γενιάς κειμένου.

## Στόχοι μάθησης

Στο τέλος αυτού του μαθήματος, θα μπορείτε να:

- Εξηγήσετε τι είναι μια εφαρμογή γενιάς κειμένου.
- Δημιουργήσετε μια εφαρμογή γενιάς κειμένου χρησιμοποιώντας το openai.
- Ρυθμίσετε την εφαρμογή σας να χρησιμοποιεί περισσότερα ή λιγότερα tokens και να αλλάξετε τη θερμοκρασία για ποικιλία στο αποτέλεσμα.

## Τι είναι μια εφαρμογή γενιάς κειμένου;

Κανονικά όταν δημιουργείτε μια εφαρμογή έχει κάποιο είδος διεπαφής όπως τα εξής:

- Βασισμένη σε εντολές. Οι εφαρμογές κονσόλας είναι τυπικές εφαρμογές όπου πληκτρολογείτε μια εντολή και εκτελεί μια εργασία. Για παράδειγμα, `git` είναι μια εφαρμογή βασισμένη σε εντολές.
- Διεπαφή χρήστη (UI). Ορισμένες εφαρμογές έχουν γραφικές διεπαφές χρήστη (GUIs) όπου κάνετε κλικ σε κουμπιά, εισάγετε κείμενο, επιλέγετε επιλογές και άλλα.

### Οι εφαρμογές κονσόλας και UI έχουν περιορισμούς

Συγκρίνετε το με μια εφαρμογή βασισμένη σε εντολές όπου πληκτρολογείτε μια εντολή:

- **Είναι περιορισμένη**. Δεν μπορείτε απλά να πληκτρολογήσετε οποιαδήποτε εντολή, μόνο αυτές που υποστηρίζει η εφαρμογή.
- **Γλωσσική εξειδίκευση**. Ορισμένες εφαρμογές υποστηρίζουν πολλές γλώσσες, αλλά από προεπιλογή η εφαρμογή είναι κατασκευασμένη για μια συγκεκριμένη γλώσσα, ακόμη και αν μπορείτε να προσθέσετε περισσότερη υποστήριξη γλωσσών.

### Οφέλη των εφαρμογών γενιάς κειμένου

Πώς είναι λοιπόν διαφορετική μια εφαρμογή γενιάς κειμένου;

Σε μια εφαρμογή γενιάς κειμένου, έχετε περισσότερη ευελιξία, δεν περιορίζεστε σε ένα σύνολο εντολών ή μια συγκεκριμένη γλώσσα εισόδου. Αντίθετα, μπορείτε να χρησιμοποιήσετε φυσική γλώσσα για να αλληλεπιδράσετε με την εφαρμογή. Ένα άλλο όφελος είναι ότι επειδή ήδη αλληλεπιδράτε με μια πηγή δεδομένων που έχει εκπαιδευτεί σε μια τεράστια συλλογή πληροφοριών, ενώ μια παραδοσιακή εφαρμογή μπορεί να περιορίζεται σε ό,τι υπάρχει σε μια βάση δεδομένων.

### Τι μπορώ να δημιουργήσω με μια εφαρμογή γενιάς κειμένου;

Υπάρχουν πολλά πράγματα που μπορείτε να δημιουργήσετε. Για παράδειγμα:

- **Ένα chatbot**. Ένα chatbot που απαντά σε ερωτήσεις σχετικά με θέματα, όπως η εταιρεία σας και τα προϊόντα της, θα μπορούσε να είναι μια καλή επιλογή.
- **Βοηθός**. Τα LLMs είναι εξαιρετικά σε πράγματα όπως η περίληψη κειμένου, η απόκτηση πληροφοριών από κείμενο, η παραγωγή κειμένου όπως βιογραφικά και άλλα.
- **Βοηθός κώδικα**. Ανάλογα με το μοντέλο γλώσσας που χρησιμοποιείτε, μπορείτε να δημιουργήσετε έναν βοηθό κώδικα που σας βοηθά να γράψετε κώδικα. Για παράδειγμα, μπορείτε να χρησιμοποιήσετε ένα προϊόν όπως το GitHub Copilot καθώς και το ChatGPT για να σας βοηθήσει να γράψετε κώδικα.

## Πώς μπορώ να ξεκινήσω;

Λοιπόν, πρέπει να βρείτε έναν τρόπο να ενσωματωθείτε με ένα LLM, το οποίο συνήθως περιλαμβάνει τις ακόλουθες δύο προσεγγίσεις:

- Χρησιμοποιήστε ένα API. Εδώ δημιουργείτε αιτήματα ιστού με το prompt σας και λαμβάνετε πίσω το παραγόμενο κείμενο.
- Χρησιμοποιήστε μια βιβλιοθήκη. Οι βιβλιοθήκες βοηθούν στην ενθυλάκωση των κλήσεων API και τις καθιστούν ευκολότερες στη χρήση.

## Βιβλιοθήκες/SDKs

Υπάρχουν μερικές γνωστές βιβλιοθήκες για εργασία με LLMs όπως:

- **openai**, αυτή η βιβλιοθήκη καθιστά εύκολη τη σύνδεση με το μοντέλο σας και την αποστολή prompts.

Στη συνέχεια, υπάρχουν βιβλιοθήκες που λειτουργούν σε υψηλότερο επίπεδο όπως:

- **Langchain**. Το Langchain είναι γνωστό και υποστηρίζει Python.
- **Semantic Kernel**. Το Semantic Kernel είναι μια βιβλιοθήκη από τη Microsoft που υποστηρίζει τις γλώσσες C#, Python και Java.

## Πρώτη εφαρμογή χρησιμοποιώντας openai

Ας δούμε πώς μπορούμε να δημιουργήσουμε την πρώτη μας εφαρμογή, ποιες βιβλιοθήκες χρειαζόμαστε, πόσο απαιτείται και ούτω καθεξής.

### Εγκαταστήστε το openai

Υπάρχουν πολλές βιβλιοθήκες εκεί έξω για την αλληλεπίδραση με το OpenAI ή το Azure OpenAI. Είναι δυνατό να χρησιμοποιήσετε πολλές γλώσσες προγραμματισμού επίσης όπως C#, Python, JavaScript, Java και άλλα. Έχουμε επιλέξει να χρησιμοποιήσουμε τη βιβλιοθήκη `openai` Python, οπότε θα χρησιμοποιήσουμε `pip` για να την εγκαταστήσουμε.

```bash
pip install openai
```

### Δημιουργήστε έναν πόρο

Πρέπει να πραγματοποιήσετε τα ακόλουθα βήματα:

- Δημιουργήστε έναν λογαριασμό στο Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Αποκτήστε πρόσβαση στο Azure OpenAI. Μεταβείτε στο [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) και ζητήστε πρόσβαση.

  > [!NOTE]
  > Τη στιγμή της γραφής, πρέπει να υποβάλετε αίτηση για πρόσβαση στο Azure OpenAI.

- Εγκαταστήστε το Python <https://www.python.org/>
- Έχετε δημιουργήσει έναν πόρο υπηρεσίας Azure OpenAI. Δείτε αυτόν τον οδηγό για το πώς να [δημιουργήσετε έναν πόρο](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Εντοπίστε το κλειδί API και το endpoint

Σε αυτό το σημείο, πρέπει να πείτε στη βιβλιοθήκη `openai` ποιο κλειδί API να χρησιμοποιήσει. Για να βρείτε το κλειδί API σας, μεταβείτε στην ενότητα "Keys and Endpoint" του πόρου Azure OpenAI σας και αντιγράψτε την τιμή "Key 1".

Τώρα που έχετε αντιγράψει αυτές τις πληροφορίες, ας δώσουμε οδηγίες στις βιβλιοθήκες να τις χρησιμοποιήσουν.

> [!NOTE]
> Αξίζει να διαχωρίσετε το κλειδί API από τον κώδικά σας. Μπορείτε να το κάνετε χρησιμοποιώντας μεταβλητές περιβάλλοντος.

### Ρύθμιση παραμέτρων Azure

Αν χρησιμοποιείτε το Azure OpenAI, δείτε πώς ρυθμίζετε τις παραμέτρους:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Πάνω, ρυθμίζουμε τα εξής:

Στον παραπάνω κώδικα, δημιουργούμε ένα αντικείμενο ολοκλήρωσης και περνάμε το μοντέλο που θέλουμε να χρησιμοποιήσουμε και το prompt. Στη συνέχεια, εκτυπώνουμε το παραγόμενο κείμενο.

### Ολοκληρώσεις συνομιλίας

Μέχρι τώρα, έχετε δει πώς χρησιμοποιούμε την `Completion` to generate text. But there's another class called `ChatCompletion` που είναι πιο κατάλληλη για chatbots. Δείτε ένα παράδειγμα χρήσης της:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Περισσότερα για αυτή τη λειτουργικότητα σε ένα επερχόμενο κεφάλαιο.

## Άσκηση - η πρώτη σας εφαρμογή γενιάς κειμένου

Τώρα που μάθαμε πώς να ρυθμίσουμε και να διαμορφώσουμε το openai, είναι ώρα να δημιουργήσετε την πρώτη σας εφαρμογή γενιάς κειμένου. Για να δημιουργήσετε την εφαρμογή σας, ακολουθήστε τα εξής βήματα:

1. Δημιουργήστε ένα εικονικό περιβάλλον και εγκαταστήστε το openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Αν χρησιμοποιείτε Windows πληκτρολογήστε `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1` value.

1. Δημιουργήστε ένα αρχείο _app.py_ και δώστε του τον ακόλουθο κώδικα:

   ```python
   import openai

   openai.api_key = "<replace this value with your open ai key or Azure OpenAI key>"

   openai.api_type = 'azure'
   openai.api_version = '2023-05-15'
   openai.api_base = "<endpoint found in Azure Portal where your API key is>"
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"
   messages = [{"role": "user", "content": prompt}]

   # make completion
   completion = openai.chat.completions.create(model=deployment_name, messages=messages)

   # print response
   print(completion.choices[0].message.content)
   ```

   > [!NOTE]
   > Αν χρησιμοποιείτε το Azure OpenAI, πρέπει να ρυθμίσετε το `api_type` to `azure` and set the `api_key` στο κλειδί Azure OpenAI σας.

   Θα πρέπει να δείτε ένα αποτέλεσμα όπως το εξής:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Διάφοροι τύποι prompts για διαφορετικά πράγματα

Τώρα έχετε δει πώς να δημιουργήσετε κείμενο χρησιμοποιώντας ένα prompt. Έχετε ακόμη ένα πρόγραμμα που λειτουργεί και μπορείτε να το τροποποιήσετε και να το αλλάξετε για να δημιουργήσετε διαφορετικούς τύπους κειμένου.

Τα prompts μπορούν να χρησιμοποιηθούν για διάφορες εργασίες. Για παράδειγμα:

- **Δημιουργία τύπου κειμένου**. Για παράδειγμα, μπορείτε να δημιουργήσετε ένα ποίημα, ερωτήσεις για ένα κουίζ κλπ.
- **Αναζήτηση πληροφοριών**. Μπορείτε να χρησιμοποιήσετε prompts για να αναζητήσετε πληροφορίες όπως το ακόλουθο παράδειγμα 'Τι σημαίνει CORS στην ανάπτυξη ιστού?'.
- **Δημιουργία κώδικα**. Μπορείτε να χρησιμοποιήσετε prompts για να δημιουργήσετε κώδικα, για παράδειγμα να αναπτύξετε μια κανονική έκφραση που χρησιμοποιείται για την επικύρωση email ή γιατί όχι να δημιουργήσετε ένα ολόκληρο πρόγραμμα, όπως μια εφαρμογή ιστού;

## Μια πιο πρακτική περίπτωση χρήσης: δημιουργός συνταγών

Φανταστείτε ότι έχετε υλικά στο σπίτι και θέλετε να μαγειρέψετε κάτι. Για αυτό, χρειάζεστε μια συνταγή. Ένας τρόπος να βρείτε συνταγές είναι να χρησιμοποιήσετε μια μηχανή αναζήτησης ή θα μπορούσατε να χρησιμοποιήσετε ένα LLM για να το κάνετε.

Θα μπορούσατε να γράψετε ένα prompt όπως το εξής:

> "Δείξε μου 5 συνταγές για ένα πιάτο με τα ακόλουθα υλικά: κοτόπουλο, πατάτες και καρότα. Για κάθε συνταγή, απαρίθμησε όλα τα χρησιμοποιούμενα υλικά"

Δεδομένου του παραπάνω prompt, μπορεί να λάβετε μια απάντηση παρόμοια με:

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

Αυτό το αποτέλεσμα είναι εξαιρετικό, ξέρω τι να μαγειρέψω. Σε αυτό το σημείο, τι θα μπορούσαν να είναι χρήσιμες βελτιώσεις είναι:

- Φιλτράρισμα υλικών που δεν μου αρέσουν ή είμαι αλλεργικός.
- Δημιουργία λίστας αγορών, σε περίπτωση που δεν έχω όλα τα υλικά στο σπίτι.

Για τις παραπάνω περιπτώσεις, ας προσθέσουμε ένα επιπλέον prompt:

> "Παρακαλώ αφαιρέστε συνταγές με σκόρδο καθώς είμαι αλλεργικός και αντικαταστήστε το με κάτι άλλο. Επίσης, δημιουργήστε μια λίστα αγορών για τις συνταγές, λαμβάνοντας υπόψη ότι ήδη έχω κοτόπουλο, πατάτες και καρότα στο σπίτι."

Τώρα έχετε ένα νέο αποτέλεσμα, δηλαδή:

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

Αυτές είναι οι πέντε συνταγές σας, χωρίς να αναφέρεται το σκόρδο και έχετε επίσης μια λίστα αγορών λαμβάνοντας υπόψη τι έχετε ήδη στο σπίτι.

## Άσκηση - δημιουργήστε έναν δημιουργό συνταγών

Τώρα που έχουμε αναπαραστήσει ένα σενάριο, ας γράψουμε κώδικα για να ταιριάξουμε με το αναπαρασταθέν σενάριο. Για να το κάνετε, ακολουθήστε αυτά τα βήματα:

1. Χρησιμοποιήστε το υπάρχον αρχείο _app.py_ ως σημείο εκκίνησης
1. Εντοπίστε τη μεταβλητή `prompt` και αλλάξτε τον κώδικα της στο εξής:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Αν τώρα εκτελέσετε τον κώδικα, θα πρέπει να δείτε ένα αποτέλεσμα παρόμοιο με:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > Σημείωση, το LLM σας είναι μη ντετερμινιστικό, οπότε μπορεί να λάβετε διαφορετικά αποτελέσματα κάθε φορά που εκτελείτε το πρόγραμμα.

   Εξαιρετικά, ας δούμε πώς μπορούμε να βελτιώσουμε τα πράγματα. Για να βελτιώσουμε τα πράγματα, θέλουμε να βεβαιωθούμε ότι ο κώδικας είναι ευέλικτος, ώστε τα υλικά και ο αριθμός των συνταγών να μπορούν να βελτιωθούν και να αλλάξουν.

1. Ας αλλάξουμε τον κώδικα με τον εξής τρόπο:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Η δοκιμή του κώδικα θα μπορούσε να μοιάζει με αυτό:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Βελτίωση προσθέτοντας φίλτρο και λίστα αγορών

Τώρα έχουμε μια λειτουργική εφαρμογή ικανή να παράγει συνταγές και είναι ευέλικτη καθώς βασίζεται σε εισόδους από τον χρήστη, τόσο στον αριθμό των συνταγών όσο και στα χρησιμοποιούμενα υλικά.

Για να το βελτιώσουμε περαιτέρω, θέλουμε να προσθέσουμε τα εξής:

- **Φιλτράρισμα υλικών**. Θέλουμε να είμαστε σε θέση να φιλτράρουμε υλικά που δεν μας αρέσουν ή είμαστε αλλεργικοί. Για να επιτύχουμε αυτήν την αλλαγή, μπορούμε να επεξεργαστούμε το υπάρχον prompt μας και να προσθέσουμε μια συνθήκη φίλτρου στο τέλος του όπως εξής:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Πάνω, προσθέτουμε `{filter}` στο τέλος του prompt και επίσης καταγράφουμε την τιμή φίλτρου από τον χρήστη.

  Ένα παράδειγμα εισόδου εκτέλεσης του προγράμματος μπορεί τώρα να μοιάζει με αυτό:

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

  Όπως μπορείτε να δείτε, οποιεσδήποτε συνταγές με γάλα έχουν φιλτραριστεί. Αλλά, αν είστε δυσανεκτικοί στη λακτόζη, μπορεί να θέλετε να φιλτράρετε συνταγές με τυρί επίσης, οπότε υπάρχει ανάγκη να είστε σαφείς.

- **Παραγωγή λίστας αγορών**. Θέλουμε να παράγουμε μια λίστα αγορών, λαμβάνοντας υπόψη τι έχουμε ήδη στο σπίτι.

  Για αυτήν τη λειτουργικότητα, θα μπορούσαμε είτε να προσπαθήσουμε να λύσουμε τα πάντα σε ένα prompt είτε να τα χωρίσουμε σε δύο prompts. Ας δοκιμάσουμε τη δεύτερη προσέγγιση. Εδώ προτείνουμε να προσθέσουμε ένα επιπλέον prompt, αλλά για να λειτουργήσει αυτό, πρέπει να προσθέσουμε το αποτέλεσμα του πρώτου prompt ως περιεχόμενο στο δεύτερο prompt.

  Εντοπίστε το μέρος του κώδικα που εκτυπώνει

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που προσπαθούμε για ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το αρχικό έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.