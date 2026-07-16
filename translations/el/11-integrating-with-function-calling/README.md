# Ενσωμάτωση με κλήση λειτουργίας

[![Ενσωμάτωση με κλήση λειτουργίας](../../../translated_images/el/11-lesson-banner.d78860d3e1f041e2.webp)](https://youtu.be/DgUdCLX8qYQ?si=f1ouQU5HQx6F8Gl2)

Έχετε μάθει αρκετά μέχρι τώρα στα προηγούμενα μαθήματα. Ωστόσο, μπορούμε να βελτιώσουμε περαιτέρω. Κάποια πράγματα που μπορούμε να αντιμετωπίσουμε είναι το πώς μπορούμε να αποκτήσουμε μια πιο συνεπή μορφή απάντησης για να γίνει πιο εύκολο να εργαστούμε με την απάντηση στη συνέχεια. Επίσης, ίσως θέλουμε να προσθέσουμε δεδομένα από άλλες πηγές για περαιτέρω ενίσχυση της εφαρμογής μας.

Τα παραπάνω προβλήματα είναι αυτά που επιδιώκει να αντιμετωπίσει αυτό το κεφάλαιο.

## Εισαγωγή

Αυτό το μάθημα θα καλύψει:

- Εξήγηση τι είναι η κλήση λειτουργίας και τις περιπτώσεις χρήσης της.
- Δημιουργία κλήσης λειτουργίας χρησιμοποιώντας το Azure OpenAI.
- Πώς να ενσωματώσετε μια κλήση λειτουργίας σε μια εφαρμογή.

## Στόχοι μάθησης

Μέχρι το τέλος αυτού του μαθήματος, θα μπορείτε να:

- Εξηγείτε τον σκοπό της χρήσης της κλήσης λειτουργίας.
- Ρυθμίσετε την Κλήση Λειτουργίας χρησιμοποιώντας την Υπηρεσία Azure OpenAI.
- Σχεδιάζετε αποτελεσματικές κλήσεις λειτουργιών για τη χρήση στην εφαρμογή σας.

## Σενάριο: Βελτιώνοντας το chatbot μας με λειτουργίες

Για αυτό το μάθημα, θέλουμε να δημιουργήσουμε μια λειτουργία για το εκπαιδευτικό μας startup που επιτρέπει στους χρήστες να χρησιμοποιούν ένα chatbot για να βρουν τεχνικά μαθήματα. Θα προτείνουμε μαθήματα που ταιριάζουν στο επίπεδο δεξιότητας, τον τρέχοντα ρόλο και την τεχνολογία που τους ενδιαφέρει.

Για να ολοκληρώσουμε αυτό το σενάριο, θα χρησιμοποιήσουμε συνδυασμό:

- `Azure OpenAI` για να δημιουργήσουμε μια εμπειρία συνομιλίας για τον χρήστη.
- `Microsoft Learn Catalog API` για να βοηθά τους χρήστες να βρουν μαθήματα βάσει του αιτήματός τους.
- `Κλήση Λειτουργίας` για να πάρουμε το ερώτημα του χρήστη και να το στείλουμε σε μια λειτουργία για να γίνει το αίτημα API.

Για να ξεκινήσουμε, ας δούμε γιατί θα θέλαμε να χρησιμοποιήσουμε την κλήση λειτουργίας από την αρχή:

## Γιατί Κλήση Λειτουργίας

Πριν από την κλήση λειτουργίας, οι απαντήσεις από ένα LLM ήταν μη δομημένες και ασυνεπείς. Οι προγραμματιστές ήταν υποχρεωμένοι να γράφουν πολύπλοκο κώδικα επικύρωσης για να διασφαλίσουν ότι μπορούν να χειριστούν κάθε παραλλαγή της απάντησης. Οι χρήστες δεν μπορούσαν να λάβουν απαντήσεις όπως "Ποιος είναι ο τρέχων καιρός στη Στοκχόλμη;". Αυτό συμβαίνει επειδή τα μοντέλα ήταν περιορισμένα στην περίοδο εκπαίδευσης των δεδομένων.

Η Κλήση Λειτουργίας είναι μια λειτουργία της Υπηρεσίας Azure OpenAI για να ξεπεραστούν οι παρακάτω περιορισμοί:

- **Συνεπής μορφή απάντησης**. Αν μπορούμε να ελέγξουμε καλύτερα τη μορφή της απάντησης, μπορούμε πιο εύκολα να ενσωματώσουμε την απάντηση σε άλλα συστήματα.
- **Εξωτερικά δεδομένα**. Δυνατότητα χρήσης δεδομένων από άλλες πηγές της εφαρμογής σε πλαίσιο συνομιλίας.

## Εικονογράφηση του προβλήματος μέσω ενός σεναρίου

> Σας προτείνουμε να χρησιμοποιήσετε το [περιλαμβανόμενο σημειωματάριο](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) αν θέλετε να εκτελέσετε το παρακάτω σενάριο. Μπορείτε επίσης να διαβάσετε απλά καθώς προσπαθούμε να εικονογραφήσουμε ένα πρόβλημα όπου οι λειτουργίες μπορούν να βοηθήσουν στην επίλυση του προβλήματος.

Ας δούμε το παράδειγμα που εικονογραφεί το πρόβλημα μορφοποίησης απάντησης:

Ας υποθέσουμε ότι θέλουμε να δημιουργήσουμε μια βάση δεδομένων με στοιχεία φοιτητών ώστε να προτείνουμε το σωστό μάθημα σε αυτούς. Παρακάτω έχουμε δύο περιγραφές φοιτητών που είναι πολύ παρόμοιες στα δεδομένα που περιέχουν.

1. Δημιουργήστε μια σύνδεση στην πηγή μας Azure OpenAI:

   ```python
   import os
   import json
   from openai import OpenAI
   from dotenv import load_dotenv
   load_dotenv()

   # Το API Απαντήσεων εξυπηρετείται από το Azure OpenAI (Microsoft Foundry) v1
   # τελικό σημείο, οπότε στοχεύουμε τον πελάτη OpenAI στο <your-endpoint>/openai/v1/.
   endpoint = os.environ['AZURE_OPENAI_ENDPOINT']
   client = OpenAI(
   api_key=os.environ['AZURE_OPENAI_API_KEY'],
   base_url=f"{endpoint.rstrip('/')}/openai/v1/",
   )

   deployment=os.environ['AZURE_OPENAI_DEPLOYMENT']
   ```

   Παρακάτω είναι μερικός κώδικας Python για τη ρύθμιση της σύνδεσης μας στο Azure OpenAI. Επειδή χρησιμοποιούμε το σημείο πρόσβασης v1, χρειάζεται μόνο να ορίσουμε το `api_key` και το `base_url` (δεν απαιτείται `api_version`).

1. Δημιουργία δύο περιγραφών φοιτητών χρησιμοποιώντας τις μεταβλητές `student_1_description` και `student_2_description`.

   ```python
   student_1_description="Emily Johnson is a sophomore majoring in computer science at Duke University. She has a 3.7 GPA. Emily is an active member of the university's Chess Club and Debate Team. She hopes to pursue a career in software engineering after graduating."

   student_2_description = "Michael Lee is a sophomore majoring in computer science at Stanford University. He has a 3.8 GPA. Michael is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after finishing his studies."
   ```

   Θέλουμε να στείλουμε τις παραπάνω περιγραφές φοιτητών σε ένα LLM για να αναλύσουμε τα δεδομένα. Αυτά τα δεδομένα μπορούν αργότερα να χρησιμοποιηθούν στην εφαρμογή μας και να σταλούν σε ένα API ή να αποθηκευτούν σε βάση δεδομένων.

1. Ας δημιουργήσουμε δύο όμοια μηνύματα στα οποία δίνουμε οδηγίες στο LLM σχετικά με τις πληροφορίες που μας ενδιαφέρουν:

   ```python
   prompt1 = f'''
   Please extract the following information from the given text and return it as a JSON object:

   name
   major
   school
   grades
   club

   This is the body of text to extract the information from:
   {student_1_description}
   '''

   prompt2 = f'''
   Please extract the following information from the given text and return it as a JSON object:

   name
   major
   school
   grades
   club

   This is the body of text to extract the information from:
   {student_2_description}
   '''
   ```

   Τα παραπάνω μηνύματα δίνουν εντολές στο LLM να εξάγει πληροφορίες και να επιστρέψει την απάντηση σε μορφή JSON.

1. Αφού ρυθμίσουμε τα μηνύματα και τη σύνδεση στο Azure OpenAI, τώρα θα στείλουμε τα μηνύματα στο LLM χρησιμοποιώντας `client.responses.create`. Αποθηκεύουμε το μήνυμα στη μεταβλητή `input` και αναθέτουμε τον ρόλο σε `user`. Αυτό μιμείται το μήνυμα που γράφει ένας χρήστης σε ένα chatbot.

   ```python
   # απόκριση από το πρώτο αίτημα
   openai_response1 = client.responses.create(
   model=deployment,
   input = [{'role': 'user', 'content': prompt1}],
   store=False,
   )
   openai_response1.output_text

   # απόκριση από το δεύτερο αίτημα
   openai_response2 = client.responses.create(
   model=deployment,
   input = [{'role': 'user', 'content': prompt2}],
   store=False,
   )
   openai_response2.output_text
   ```

Τώρα μπορούμε να στείλουμε και τα δύο αιτήματα στο LLM και να εξετάσουμε την απάντηση που λαμβάνουμε βάζοντάς την ως `openai_response1.output_text`.

1. Τέλος, μπορούμε να μετατρέψουμε την απάντηση σε μορφή JSON καλώντας `json.loads`:

   ```python
   # Φόρτωση της απάντησης ως αντικείμενο JSON
   json_response1 = json.loads(openai_response1.output_text)
   json_response1
   ```

   Απάντηση 1:

   ```json
   {
     "name": "Emily Johnson",
     "major": "computer science",
     "school": "Duke University",
     "grades": "3.7",
     "club": "Chess Club"
   }
   ```

   Απάντηση 2:

   ```json
   {
     "name": "Michael Lee",
     "major": "computer science",
     "school": "Stanford University",
     "grades": "3.8 GPA",
     "club": "Robotics Club"
   }
   ```

   Παρόλο που τα μηνύματα είναι ίδια και οι περιγραφές είναι παρόμοιες, βλέπουμε διαφορετική μορφοποίηση των τιμών της ιδιότητας `Grades`, καθώς μερικές φορές παίρνουμε μορφή όπως `3.7` ή `3.7 GPA` για παράδειγμα.

   Αυτό το αποτέλεσμα οφείλεται στο ότι το LLM παίρνει μη δομημένα δεδομένα με τη μορφή του γραπτού μηνύματος και επιστρέφει επίσης μη δομημένα δεδομένα. Χρειαζόμαστε να έχουμε μια δομημένη μορφή ώστε να ξέρουμε τι να περιμένουμε όταν αποθηκεύουμε ή χρησιμοποιούμε αυτά τα δεδομένα.

Πώς λύνουμε λοιπόν το πρόβλημα μορφοποίησης; Χρησιμοποιώντας την κλήση λειτουργίας, μπορούμε να βεβαιωθούμε ότι λαμβάνουμε δομημένα δεδομένα πίσω. Όταν χρησιμοποιούμε την κλήση λειτουργίας, το LLM δεν καλεί η εκτελεί κάποιον κώδικα λειτουργίας. Αντ’ αυτού, δημιουργούμε μια δομή που το LLM ακολουθεί για τις απαντήσεις του. Έπειτα χρησιμοποιούμε αυτές τις δομημένες απαντήσεις ώστε να ξέρουμε ποια λειτουργία να εκτελέσουμε στις εφαρμογές μας.

![ροή λειτουργίας](../../../translated_images/el/Function-Flow.083875364af4f4bb.webp)

Μπορούμε έπειτα να πάρουμε αυτό που επιστρέφει η λειτουργία και να το στείλουμε πίσω στο LLM. Το LLM θα απαντήσει χρησιμοποιώντας φυσική γλώσσα για να απαντήσει στο ερώτημα του χρήστη.

## Περιπτώσεις χρήσης για κλήσεις λειτουργιών

Υπάρχουν πολλές διαφορετικές περιπτώσεις χρήσης όπου οι κλήσεις λειτουργιών μπορούν να βελτιώσουν την εφαρμογή σας, όπως:

- **Κλήση εξωτερικών εργαλείων**. Τα chatbots είναι εξαιρετικά στο να παρέχουν απαντήσεις σε ερωτήσεις χρηστών. Χρησιμοποιώντας την κλήση λειτουργίας, τα chatbots μπορούν να χρησιμοποιήσουν μηνύματα από χρήστες για να ολοκληρώσουν συγκεκριμένες εργασίες. Για παράδειγμα, ένας φοιτητής μπορεί να ζητήσει από το chatbot να "Στείλει ένα email στον καθηγητή μου λέγοντας ότι χρειάζομαι περισσότερη βοήθεια με αυτό το θέμα". Αυτό μπορεί να κάνει μια κλήση λειτουργίας στο `send_email(to: string, body: string)`

- **Δημιουργία ερωτημάτων API ή βάσης δεδομένων**. Οι χρήστες μπορούν να βρουν πληροφορίες χρησιμοποιώντας φυσική γλώσσα που μετατρέπεται σε μορφοποιημένο ερώτημα ή αίτημα API. Ένα παράδειγμα αυτού μπορεί να είναι ένας δάσκαλος που ζητά "Ποιοι φοιτητές ολοκλήρωσαν την τελευταία εργασία" που μπορεί να καλεί μια λειτουργία με όνομα `get_completed(student_name: string, assignment: int, current_status: string)`

- **Δημιουργία δομημένων δεδομένων**. Οι χρήστες μπορούν να πάρουν ένα μπλοκ κειμένου ή ένα CSV και να χρησιμοποιήσουν το LLM για να εξάγουν σημαντικές πληροφορίες από αυτό. Για παράδειγμα, ένας φοιτητής μπορεί να μετατρέψει ένα άρθρο της Wikipedia για ειρηνευτικές συμφωνίες για να δημιουργήσει κάρτες με AI. Αυτό μπορεί να γίνει χρησιμοποιώντας μια λειτουργία που ονομάζεται `get_important_facts(agreement_name: string, date_signed: string, parties_involved: list)`

## Δημιουργία της πρώτης κλήσης λειτουργίας σας

Η διαδικασία δημιουργίας μιας κλήσης λειτουργίας περιλαμβάνει 3 βασικά βήματα:

1. **Κλήση** του Responses API με μια λίστα των λειτουργιών (εργαλείων) σας και ένα μήνυμα χρήστη.
2. **Ανάγνωση** της απάντησης του μοντέλου για εκτέλεση μιας ενέργειας, δηλαδή εκτέλεση μιας λειτουργίας ή κλήση API.
3. **Κλήση** του Responses API με την απάντηση της λειτουργίας σας για χρήση αυτής της πληροφορίας ώστε να δημιουργήσετε μια απάντηση προς το χρήστη.

![Ροή LLM](../../../translated_images/el/LLM-Flow.3285ed8caf4796d7.webp)

### Βήμα 1 - δημιουργία μηνυμάτων

Το πρώτο βήμα είναι να δημιουργήσουμε ένα μήνυμα χρήστη. Αυτό μπορεί να ανατεθεί δυναμικά παίρνοντας την τιμή από μια είσοδο κειμένου ή μπορείτε να ορίσετε μια τιμή εδώ. Εάν αυτή είναι η πρώτη φορά που δουλεύετε με το Responses API, πρέπει να ορίσουμε το `role` και το `content` του μηνύματος.

Το `role` μπορεί να είναι είτε `system` (δημιουργία κανόνων), `assistant` (το μοντέλο) ή `user` (ο τελικός χρήστης). Για την κλήση λειτουργίας, θα ορίσουμε αυτό ως `user` με ένα παράδειγμα ερώτησης.

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

Αναθέτοντας διαφορετικούς ρόλους, γίνεται σαφές στο LLM αν είναι το σύστημα που λέει κάτι ή ο χρήστης, κάτι που βοηθά στη δημιουργία ιστορικού συνομιλίας στο οποίο μπορεί να βασιστεί το LLM.

### Βήμα 2 - δημιουργία λειτουργιών

Στη συνέχεια, θα ορίσουμε μια λειτουργία και τις παραμέτρους αυτής της λειτουργίας. Θα χρησιμοποιήσουμε μόνο μία λειτουργία εδώ που ονομάζεται `search_courses` αλλά μπορείτε να δημιουργήσετε πολλές λειτουργίες.

> **Σημαντικό** : Οι λειτουργίες περιλαμβάνονται στο μήνυμα συστήματος προς το LLM και θα υπολογίζονται στο ποσό των διαθέσιμων τοκεν που έχετε.

Παρακάτω δημιουργούμε τις λειτουργίες ως έναν πίνακα αντικειμένων. Κάθε αντικείμενο είναι ένα εργαλείο στη μορφή Responses API flat, με τις ιδιότητες `type`, `name`, `description` και `parameters`:

```python
functions = [
   {
      "type":"function",
      "name":"search_courses",
      "description":"Retrieves courses from the search index based on the parameters provided",
      "parameters":{
         "type":"object",
         "properties":{
            "role":{
               "type":"string",
               "description":"The role of the learner (i.e. developer, data scientist, student, etc.)"
            },
            "product":{
               "type":"string",
               "description":"The product that the lesson is covering (i.e. Azure, Power BI, etc.)"
            },
            "level":{
               "type":"string",
               "description":"The level of experience the learner has prior to taking the course (i.e. beginner, intermediate, advanced)"
            }
         },
         "required":[
            "role"
         ]
      }
   }
]
```

Ας περιγράψουμε κάθε περίπτωση λειτουργίας πιο λεπτομερώς παρακάτω:

- `name` - Το όνομα της λειτουργίας που θέλουμε να κληθεί.
- `description` - Αυτή είναι η περιγραφή του πώς λειτουργεί η λειτουργία. Εδώ είναι σημαντικό να είμαστε συγκεκριμένοι και σαφείς.
- `parameters` - Μια λίστα τιμών και μορφής που θέλετε το μοντέλο να παράγει στην απάντησή του. Ο πίνακας παραμέτρων αποτελείται από αντικείμενα με τις εξής ιδιότητες:
  1.  `type` - Ο τύπος δεδομένων στον οποίο θα αποθηκευτούν οι ιδιότητες.
  1.  `properties` - Λίστα συγκεκριμένων τιμών που θα χρησιμοποιήσει το μοντέλο στην απάντησή του.
      1. `name` - Το κλειδί είναι το όνομα της ιδιότητας που θα χρησιμοποιήσει το μοντέλο στην μορφοποιημένη απάντησή του, για παράδειγμα, `product`.
      1. `type` - Ο τύπος δεδομένων αυτής της ιδιότητας, για παράδειγμα, `string`.
      1. `description` - Περιγραφή της συγκεκριμένης ιδιότητας.

Υπάρχει επίσης μια προαιρετική ιδιότητα `required` - υποχρεωτική ιδιότητα ώστε η κλήση λειτουργίας να ολοκληρωθεί.

### Βήμα 3 - Εκτέλεση της κλήσης λειτουργίας

Αφού ορίσουμε μια λειτουργία, τώρα πρέπει να την συμπεριλάβουμε στην κλήση προς το Responses API. Το κάνουμε προσθέτοντας `tools` στο αίτημα. Σε αυτή την περίπτωση `tools=functions`.

Υπάρχει επίσης η επιλογή να ορίσετε `tool_choice` ως `auto`. Αυτό σημαίνει ότι αφήνουμε το LLM να αποφασίσει ποια λειτουργία πρέπει να κληθεί βάσει του μηνύματος χρήστη και όχι να το ορίσουμε εμείς.

Ακολουθεί κώδικας όπου καλούμε `client.responses.create`, να σημειωθεί πώς ορίζουμε `tools=functions` και `tool_choice="auto"` δίνοντας έτσι στο LLM την επιλογή πότε να καλέσει τις λειτουργίες που του παρέχουμε:

```python
response = client.responses.create(model=deployment,
                                        input=messages,
                                        tools=functions,
                                        tool_choice="auto",
                                        store=False)

print(response.output)
```

Η απάντηση που λαμβάνουμε τώρα περιλαμβάνει ένα στοιχείο `function_call` στο `response.output` που μοιάζει έτσι:

```json
{
  "type": "function_call",
  "name": "search_courses",
  "call_id": "call_abc123",
  "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
}
```

Εδώ μπορούμε να δούμε πώς κλήθηκε η λειτουργία `search_courses` και με ποια επιχειρήματα, όπως καταγράφονται στην ιδιότητα `arguments` στην απάντηση JSON.

Το συμπέρασμα είναι ότι το LLM μπόρεσε να βρει τα δεδομένα να ταιριάξουν με τα επιχειρήματα της λειτουργίας καθώς τα εξήγαγε από την τιμή που δόθηκε στην παράμετρο `input` στην κλήση Responses API. Ακολουθεί μια υπενθύμιση της τιμής `messages`:

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

Όπως βλέπετε, `student`, `Azure` και `beginner` εξήχθησαν από τα `messages` και ορίστηκαν ως είσοδος στη λειτουργία. Η χρήση λειτουργιών με αυτόν τον τρόπο είναι ένας εξαιρετικός τρόπος για την εξαγωγή πληροφοριών από ένα prompt αλλά και για την παροχή δομής στο LLM με επαναχρησιμοποιήσιμη λειτουργικότητα.

Επόμενο βήμα, πρέπει να δούμε πώς μπορούμε να το χρησιμοποιήσουμε στην εφαρμογή μας.

## Ενσωμάτωση Κλήσεων Λειτουργιών σε μια Εφαρμογή

Αφού δοκιμάσουμε την μορφοποιημένη απάντηση από το LLM, τώρα μπορούμε να την ενσωματώσουμε σε μια εφαρμογή.

### Διαχείριση της ροής

Για να ενσωματώσουμε αυτό στην εφαρμογή μας, ας ακολουθήσουμε τα παρακάτω βήματα:

1. Πρώτα, ας κάνουμε την κλήση στις υπηρεσίες OpenAI και να εξάγουμε τα στοιχεία κλήσης λειτουργίας από την απάντηση `output`.

   ```python
   response_items = response.output
   tool_calls = [item for item in response_items if item.type == "function_call"]
   ```

1. Τώρα θα ορίσουμε τη λειτουργία που θα καλέσει το Microsoft Learn API για να πάρει μια λίστα μαθημάτων:

   ```python
   import requests

   def search_courses(role, product, level):
     url = "https://learn.microsoft.com/api/catalog/"
     params = {
        "role": role,
        "product": product,
        "level": level
     }
     response = requests.get(url, params=params)
     modules = response.json()["modules"]
     results = []
     for module in modules[:5]:
        title = module["title"]
        url = module["url"]
        results.append({"title": title, "url": url})
     return str(results)
   ```

   Παρατηρήστε πώς τώρα δημιουργούμε μια πραγματική Python λειτουργία που αντιστοιχεί στα ονόματα λειτουργιών που εισάγονται στη μεταβλητή `functions`. Κάνουμε επίσης πραγματικές εξωτερικές κλήσεις API για να πάρουμε τα δεδομένα που χρειαζόμαστε. Σε αυτή την περίπτωση απευθυνόμαστε στο Microsoft Learn API για αναζήτηση εκπαιδευτικών μονάδων.

Εντάξει, δημιουργήσαμε τις μεταβλητές `functions` και μια αντίστοιχη Python λειτουργία, πώς λέμε στο LLM πώς να αντιστοιχίσει τα δύο ώστε να καλέσει τη Python λειτουργία μας;

1. Για να δούμε αν πρέπει να καλέσουμε μια Python λειτουργία, πρέπει να κοιτάξουμε την απάντηση του LLM και να δούμε αν υπάρχει στοιχείο `function_call` σε αυτή και να καλέσουμε τη συγκεκριμένη λειτουργία. Να πώς μπορείτε να κάνετε τον έλεγχο παρακάτω:

   ```python
   # Ελέγξτε αν το μοντέλο θέλει να καλέσει μια συνάρτηση
   if tool_calls:
    for tool_call in tool_calls:
     print("Recommended Function call:")
     print(tool_call.name)
     print()

     # Καλέστε τη συνάρτηση.
     function_name = tool_call.name

     available_functions = {
             "search_courses": search_courses,
     }
     function_to_call = available_functions[function_name]

     function_args = json.loads(tool_call.arguments)
     function_response = function_to_call(**function_args)

     print("Output of function call:")
     print(function_response)
     print(type(function_response))

     # Προσθέστε την κλήση της συνάρτησης και το αποτέλεσμα της ξανά στη συνομιλία.
     # Το στοιχείο function_call του μοντέλου πρέπει να προστεθεί πριν από την έξοδό του.
     messages.append(tool_call)  # το στοιχείο function_call του βοηθού
     messages.append( # το αποτέλεσμα της συνάρτησης
         {
             "type": "function_call_output",
             "call_id": tool_call.call_id,
             "output": function_response,
         }
     )
   ```

   Αυτές οι τρεις γραμμές, διασφαλίζουν ότι εξάγουμε το όνομα της λειτουργίας, τα επιχειρήματα και κάνουμε την κλήση:

   ```python
   function_to_call = available_functions[function_name]

   function_args = json.loads(tool_call.arguments)
   function_response = function_to_call(**function_args)
   ```

   Παρακάτω είναι η έξοδος από τη λειτουργία του κώδικα μας:

   **Έξοδος**

   ```Recommended Function call:
   {
     "name": "search_courses",
     "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
   }

   Output of function call:
   [{'title': 'Describe concepts of cryptography', 'url': 'https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?
   WT.mc_id=api_CatalogApi'}, {'title': 'Introduction to audio classification with TensorFlow', 'url': 'https://learn.microsoft.com/en-
   us/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi'}, {'title': 'Design a Performant Data Model in Azure SQL
   Database with Azure Data Studio', 'url': 'https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?
   WT.mc_id=api_CatalogApi'}, {'title': 'Getting started with the Microsoft Cloud Adoption Framework for Azure', 'url':
   'https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi'}, {'title': 'Set up the
   Rust development environment', 'url': 'https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi'}]
   <class 'str'>
   ```

1. Τώρα θα στείλουμε το ενημερωμένο μήνυμα, `messages` στο LLM ώστε να λάβουμε μια απάντηση σε φυσική γλώσσα αντί για απάντηση API σε μορφή JSON.

   ```python
   print("Messages in next request:")
   print(messages)
   print()

   second_response = client.responses.create(
      input=messages,
      model=deployment,
      tool_choice="auto",
      tools=functions,
      temperature=0,
      store=False,
         )  # λάβετε μια νέα απάντηση από το μοντέλο όπου μπορεί να δει την απόκριση της συνάρτησης


   print(second_response.output_text)
   ```

   **Έξοδος**

   ```text
   I found some good courses for beginner students to learn Azure:

   1. [Describe concepts of cryptography](https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?WT.mc_id=api_CatalogApi)
   2. [Introduction to audio classification with TensorFlow](https://learn.microsoft.com/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi)
   3. [Design a Performant Data Model in Azure SQL Database with Azure Data Studio](https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?WT.mc_id=api_CatalogApi)
   4. [Getting started with the Microsoft Cloud Adoption Framework for Azure](https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi)
   5. [Set up the Rust development environment](https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi)

   You can click on the links to access the courses.
   ```

## Ανάθεση

Για να συνεχίσετε την εκμάθησή σας για την Κλήση Λειτουργίας στο Azure OpenAI μπορείτε να δημιουργήσετε:

- Περισσότερες παραμέτρους της λειτουργίας που μπορεί να βοηθήσουν τους μαθητές να βρουν περισσότερα μαθήματα.

- Δημιουργήστε μια άλλη κλήση συνάρτησης που παίρνει περισσότερες πληροφορίες από τον μαθητή όπως η μητρική του γλώσσα
- Δημιουργήστε διαχείριση σφαλμάτων όταν η κλήση συνάρτησης και/ή η κλήση API δεν επιστρέφει κατάλληλα μαθήματα

Συμβουλή: Ακολουθήστε την [Τεκμηρίωση αναφοράς API του Learn](https://learn.microsoft.com/training/support/catalog-api-developer-reference?WT.mc_id=academic-105485-koreyst) για να δείτε πώς και πού είναι διαθέσιμα αυτά τα δεδομένα.

## Υπέροχη δουλειά! Συνεχίστε το ταξίδι

Μετά την ολοκλήρωση αυτού του μαθήματος, ρίξτε μια ματιά στη [Συλλογή Εκμάθησης Γεννητικής ΤΝ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) για να συνεχίσετε να εξελίσσετε τις γνώσεις σας στη Γεννητική ΤΝ!

Μεταβείτε στο Μάθημα 12, όπου θα δούμε πώς να [σχεδιάζουμε UX για εφαρμογές ΤΝ](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->