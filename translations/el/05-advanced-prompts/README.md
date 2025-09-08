<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:32:42+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "el"
}
-->

# Δημιουργία κώδικα για ένα Python Web API

Σε αυτόν τον οδηγό, θα μάθουμε πώς να δημιουργήσουμε ένα απλό Web API χρησιμοποιώντας Python. Θα χρησιμοποιήσουμε το πλαίσιο Flask για να δημιουργήσουμε endpoints που θα ανταποκρίνονται σε αιτήματα HTTP.

## Βήματα

1. Εγκατάσταση του Flask:
   Χρησιμοποιήστε την εντολή `pip install Flask` για να εγκαταστήσετε το Flask.

2. Δημιουργία της εφαρμογής:
   Δημιουργήστε ένα αρχείο `app.py` και γράψτε τον βασικό κώδικα για την εφαρμογή Flask.

3. Ορισμός routes:
   Προσθέστε endpoints που θα χειρίζονται αιτήματα GET, POST, κλπ.

4. Εκτέλεση της εφαρμογής:
   Τρέξτε την εφαρμογή και δοκιμάστε τα endpoints χρησιμοποιώντας εργαλεία όπως το Postman ή το curl.

## Παράδειγμα κώδικα

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Απλό endpoint που επιστρέφει ένα μήνυμα καλωσορίσματος
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Γεια σου, κόσμε!"})

# Endpoint που δέχεται δεδομένα μέσω POST και τα επιστρέφει
@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"you_sent": data})

if __name__ == '__main__':
    app.run(debug=True)
```

## Συμβουλές

- Χρησιμοποιήστε το `debug=True` μόνο κατά την ανάπτυξη.
- Εξετάστε το ενδεχόμενο χρήσης περιβαλλοντικών μεταβλητών για ρυθμίσεις.
- Προσθέστε κατάλληλο χειρισμό σφαλμάτων για πιο αξιόπιστη εφαρμογή.

Με αυτά τα βήματα, μπορείτε να δημιουργήσετε ένα βασικό Web API σε Python και να το επεκτείνετε ανάλογα με τις ανάγκες σας.
```python
#import necessary libraries
import flask
from flask import request, jsonify

#create an instance of the Flask class
app = flask.Flask(__name__)

#create an endpoint for the API
@app.route('/api/v1/endpoint', methods=['GET'])
def api_endpoint():
    #get the request data
    data = request.get_json()

    #process the data
    result = process_data(data)

    #return the result
    return jsonify(result)

#function to process the data
def process_data(data):
    #process the data
    result = {'result': 'success'}

    #return the result
    return result

#run the Flask app
if __name__ == '__main__':
    app.run()

```

Η εκτέλεση του prompt ξανά μας δίνει αυτό το αποτέλεσμα:

```python
#import necessary libraries
import flask
from flask import request, jsonify

#create a Flask app
app = flask.Flask(__name__)

#create a route for the API
@app.route('/api', methods=['GET'])
def api_call():
    #get the data from the request
    data = request.get_json()

    #process the data
    result = process_data(data)

    #return the result
    return jsonify(result)

#define the process_data function
def process_data(data):
    #do something with the data
    result = data + 1

    #return the result
    return result

#run the app
if __name__ == '__main__':
    app.run()

```

Υπάρχει μόνο μια μικρή διαφορά ανάμεσα σε αυτά τα δύο αποτελέσματα. Ας κάνουμε το αντίθετο αυτή τη φορά, ας ορίσουμε τη θερμοκρασία στο 0.9:

```python
# Import necessary libraries
import flask
from flask import request, jsonify

# Create a Flask app
app = flask.Flask(__name__)

# Create a route for the API
@app.route('/api', methods=['GET'])
def api_call():
    # Get the data from the request
    data = request.args

    # Process the data
    result = process_data(data)

    # Return the result
    return jsonify(result)

# Function to process the data
def process_data(data):
    # Do something with the data
    result = data + 1

    # Return the result
    return result

# Run the app
if __name__ == '__main__':
    app.run()

```

και η δεύτερη προσπάθεια με τιμή θερμοκρασίας 0.9:

```python
import flask
from flask import request, jsonify

# create the Flask app
app = flask.Flask(__name__)
app.config['DEBUG'] = True

# create some test data
books = [
    {'id': 0, 'title': 'A Fire Upon The Deep', 'author': 'Vernor Vinge', 'first_sentence': 'The coldsleep itself was dreamless.', 'year_published': '1992'},
    {'id': 1, 'title': 'The Ones Who Walk Away From Omelas', 'author': 'Ursula K. Le Guin', 'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.', 'published': '1973'},
    {'id': 2, 'title': 'Dhalgren', 'author': 'Samuel R. Delany', 'first_sentence': 'to wound the autumnal city.', 'published': '1975'}
]

# create an endpoint
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to our book API!</h1>'''

@app.route('/api/v1/resources/books

```

Όπως βλέπετε, τα αποτελέσματα δεν θα μπορούσαν να είναι πιο διαφορετικά.

> Note, ότι υπάρχουν και άλλες παράμετροι που μπορείτε να αλλάξετε για να διαφοροποιήσετε το αποτέλεσμα, όπως top-k, top-p, repetition penalty, length penalty και diversity penalty, αλλά αυτές είναι εκτός του πεδίου αυτού του μαθήματος.

## Καλές πρακτικές

Υπάρχουν πολλές πρακτικές που μπορείτε να εφαρμόσετε για να προσπαθήσετε να πάρετε αυτό που θέλετε. Θα βρείτε το δικό σας στυλ καθώς χρησιμοποιείτε το prompting όλο και περισσότερο.

Επιπλέον των τεχνικών που καλύψαμε, υπάρχουν κάποιες καλές πρακτικές που αξίζει να λάβετε υπόψη όταν κάνετε prompting σε ένα LLM.

Ακολουθούν μερικές καλές πρακτικές που μπορείτε να σκεφτείτε:

- **Καθορίστε το πλαίσιο**. Το πλαίσιο έχει σημασία, όσο πιο συγκεκριμένα μπορείτε να ορίσετε όπως το πεδίο, το θέμα κτλ., τόσο το καλύτερο.
- Περιορίστε το αποτέλεσμα. Αν θέλετε συγκεκριμένο αριθμό αντικειμένων ή συγκεκριμένο μήκος, καθορίστε το.
- **Καθορίστε τι και πώς**. Θυμηθείτε να αναφέρετε τόσο τι θέλετε όσο και πώς το θέλετε, για παράδειγμα "Δημιουργήστε ένα Python Web API με διαδρομές products και customers, χωρισμένο σε 3 αρχεία".
- **Χρησιμοποιήστε πρότυπα**. Συχνά, θα θέλετε να εμπλουτίσετε τα prompts σας με δεδομένα από την εταιρεία σας. Χρησιμοποιήστε πρότυπα για αυτό. Τα πρότυπα μπορούν να έχουν μεταβλητές που αντικαθιστάτε με πραγματικά δεδομένα.
- **Ορθογραφείτε σωστά**. Τα LLM μπορεί να σας δώσουν σωστή απάντηση, αλλά αν ορθογραφείτε σωστά, θα πάρετε καλύτερη απάντηση.

## Άσκηση

Εδώ είναι κώδικας σε Python που δείχνει πώς να φτιάξετε ένα απλό API χρησιμοποιώντας Flask:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run()
```

Χρησιμοποιήστε έναν AI βοηθό όπως το GitHub Copilot ή το ChatGPT και εφαρμόστε την τεχνική "self-refine" για να βελτιώσετε τον κώδικα.

## Λύση

Παρακαλώ προσπαθήστε να λύσετε την άσκηση προσθέτοντας κατάλληλα prompts στον κώδικα.

> [!TIP]
> Διατυπώστε ένα prompt που να ζητά βελτίωση, είναι καλή ιδέα να περιορίσετε πόσες βελτιώσεις θέλετε. Μπορείτε επίσης να ζητήσετε να βελτιωθεί με συγκεκριμένο τρόπο, π.χ. αρχιτεκτονική, απόδοση, ασφάλεια κτλ.

[Solution](../../../05-advanced-prompts/python/aoai-solution.py)

## Έλεγχος γνώσεων

Γιατί θα χρησιμοποιούσα chain-of-thought prompting; Δείξτε μου 1 σωστή απάντηση και 2 λανθασμένες.

1. Για να διδάξω το LLM πώς να λύσει ένα πρόβλημα.  
1. B, Για να διδάξω το LLM να βρίσκει λάθη στον κώδικα.  
1. C, Για να δώσω εντολή στο LLM να βρει διαφορετικές λύσεις.

Α: 1, επειδή το chain-of-thought αφορά το να δείξετε στο LLM πώς να λύσει ένα πρόβλημα παρέχοντάς του μια σειρά βημάτων, παρόμοια προβλήματα και πώς λύθηκαν.

## 🚀 Πρόκληση

Μόλις χρησιμοποιήσατε την τεχνική self-refine στην άσκηση. Πάρτε οποιοδήποτε πρόγραμμα έχετε φτιάξει και σκεφτείτε ποιες βελτιώσεις θα θέλατε να εφαρμόσετε. Τώρα χρησιμοποιήστε την τεχνική self-refine για να εφαρμόσετε τις προτεινόμενες αλλαγές. Τι πιστεύετε για το αποτέλεσμα, καλύτερο ή χειρότερο;

## Μπράβο! Συνεχίστε τη μάθησή σας

Αφού ολοκληρώσετε αυτό το μάθημα, ρίξτε μια ματιά στη [συλλογή μας για τη Μάθηση Γεννητικής AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) για να συνεχίσετε να ανεβάζετε το επίπεδο των γνώσεών σας στη Γεννητική AI!

Πηγαίνετε στο Μάθημα 6 όπου θα εφαρμόσουμε τις γνώσεις μας στο Prompt Engineering φτιάχνοντας [εφαρμογές δημιουργίας κειμένου](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.