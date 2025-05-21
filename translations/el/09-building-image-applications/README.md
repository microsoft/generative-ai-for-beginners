<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T19:10:41+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "el"
}
-->
# Δημιουργία Εφαρμογών Παραγωγής Εικόνων

Υπάρχουν περισσότερα πράγματα στα LLMs από την παραγωγή κειμένου. Είναι επίσης δυνατό να δημιουργηθούν εικόνες από περιγραφές κειμένου. Η ύπαρξη εικόνων ως μέσο μπορεί να είναι εξαιρετικά χρήσιμη σε πολλούς τομείς όπως η ιατρική τεχνολογία, η αρχιτεκτονική, ο τουρισμός, η ανάπτυξη παιχνιδιών και άλλα. Σε αυτό το κεφάλαιο, θα εξετάσουμε τα δύο πιο δημοφιλή μοντέλα παραγωγής εικόνων, το DALL-E και το Midjourney.

## Εισαγωγή

Σε αυτό το μάθημα, θα καλύψουμε:

- Την παραγωγή εικόνων και γιατί είναι χρήσιμη.
- Τα DALL-E και Midjourney, τι είναι και πώς λειτουργούν.
- Πώς μπορείτε να δημιουργήσετε μια εφαρμογή παραγωγής εικόνων.

## Στόχοι Μάθησης

Μετά την ολοκλήρωση αυτού του μαθήματος, θα μπορείτε να:

- Δημιουργήσετε μια εφαρμογή παραγωγής εικόνων.
- Ορίσετε όρια για την εφαρμογή σας με μεταπροτροπές.
- Εργαστείτε με DALL-E και Midjourney.

## Γιατί να δημιουργήσετε μια εφαρμογή παραγωγής εικόνων;

Οι εφαρμογές παραγωγής εικόνων είναι ένας εξαιρετικός τρόπος για να εξερευνήσετε τις δυνατότητες της Γενετικής Τεχνητής Νοημοσύνης. Μπορούν να χρησιμοποιηθούν, για παράδειγμα:

- **Επεξεργασία και σύνθεση εικόνων**. Μπορείτε να δημιουργήσετε εικόνες για διάφορες χρήσεις, όπως επεξεργασία εικόνων και σύνθεση εικόνων.

- **Εφαρμογή σε διάφορες βιομηχανίες**. Μπορούν επίσης να χρησιμοποιηθούν για να δημιουργήσουν εικόνες για διάφορες βιομηχανίες όπως η ιατρική τεχνολογία, ο τουρισμός, η ανάπτυξη παιχνιδιών και άλλα.

## Σενάριο: Edu4All

Ως μέρος αυτού του μαθήματος, θα συνεχίσουμε να εργαζόμαστε με τη startup μας, την Edu4All. Οι μαθητές θα δημιουργήσουν εικόνες για τις αξιολογήσεις τους, τι ακριβώς εικόνες θα είναι εξαρτάται από τους μαθητές, αλλά θα μπορούσαν να είναι εικονογραφήσεις για το δικό τους παραμύθι ή να δημιουργήσουν έναν νέο χαρακτήρα για την ιστορία τους ή να τους βοηθήσουν να οπτικοποιήσουν τις ιδέες και τις έννοιες τους.

Να τι θα μπορούσαν να δημιουργήσουν οι μαθητές της Edu4All για παράδειγμα αν εργάζονται στην τάξη για μνημεία:

χρησιμοποιώντας μια προτροπή όπως

> "Σκύλος δίπλα στον Πύργο του Άιφελ στο πρωινό φως"

## Τι είναι το DALL-E και το Midjourney;

Τα [DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) και [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) είναι δύο από τα πιο δημοφιλή μοντέλα παραγωγής εικόνων, επιτρέπουν τη χρήση προτροπών για τη δημιουργία εικόνων.

### DALL-E

Ας ξεκινήσουμε με το DALL-E, που είναι ένα μοντέλο Γενετικής Τεχνητής Νοημοσύνης που δημιουργεί εικόνες από περιγραφές κειμένου.

- **CLIP**, είναι ένα μοντέλο που δημιουργεί ενσωματώσεις, οι οποίες είναι αριθμητικές αναπαραστάσεις δεδομένων, από εικόνες και κείμενο.

- **Διαχυμένη προσοχή**, είναι ένα μοντέλο που δημιουργεί εικόνες από ενσωματώσεις. Το DALL-E εκπαιδεύεται σε ένα σύνολο δεδομένων εικόνων και κειμένου και μπορεί να χρησιμοποιηθεί για να δημιουργήσει εικόνες από περιγραφές κειμένου. Για παράδειγμα, το DALL-E μπορεί να χρησιμοποιηθεί για να δημιουργήσει εικόνες μιας γάτας με καπέλο, ή ενός σκύλου με μοϊκάνα.

### Midjourney

Το Midjourney λειτουργεί με παρόμοιο τρόπο με το DALL-E, δημιουργεί εικόνες από προτροπές κειμένου. Το Midjourney μπορεί επίσης να χρησιμοποιηθεί για να δημιουργήσει εικόνες χρησιμοποιώντας προτροπές όπως "μια γάτα με καπέλο", ή ένας "σκύλος με μοϊκάνα".

## Πώς λειτουργούν τα DALL-E και Midjourney

Πρώτα, το [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). Το DALL-E είναι ένα μοντέλο Γενετικής Τεχνητής Νοημοσύνης βασισμένο στην αρχιτεκτονική του μετασχηματιστή με έναν _αυτοπαραγωγικό μετασχηματιστή_.

Ένας _αυτοπαραγωγικός μετασχηματιστής_ καθορίζει πώς ένα μοντέλο δημιουργεί εικόνες από περιγραφές κειμένου, δημιουργεί ένα πίξελ τη φορά και στη συνέχεια χρησιμοποιεί τα δημιουργημένα πίξελ για να δημιουργήσει το επόμενο πίξελ. Διαπερνώντας πολλαπλά στρώματα σε ένα νευρωνικό δίκτυο, μέχρι να ολοκληρωθεί η εικόνα.

Με αυτή τη διαδικασία, το DALL-E ελέγχει χαρακτηριστικά, αντικείμενα, χαρακτηριστικά και άλλα στην εικόνα που δημιουργεί. Ωστόσο, το DALL-E 2 και 3 έχουν περισσότερο έλεγχο πάνω στην παραγόμενη εικόνα.

## Δημιουργία της πρώτης σας εφαρμογής παραγωγής εικόνων

Λοιπόν, τι χρειάζεται για να δημιουργήσετε μια εφαρμογή παραγωγής εικόνων; Χρειάζεστε τις ακόλουθες βιβλιοθήκες:

- **python-dotenv**, συνιστάται να χρησιμοποιήσετε αυτή τη βιβλιοθήκη για να κρατήσετε τα μυστικά σας σε ένα αρχείο _.env_ μακριά από τον κώδικα.
- **openai**, αυτή η βιβλιοθήκη είναι αυτή που θα χρησιμοποιήσετε για να αλληλεπιδράσετε με το OpenAI API.
- **pillow**, για να δουλέψετε με εικόνες στην Python.
- **requests**, για να σας βοηθήσει να κάνετε HTTP αιτήματα.

1. Δημιουργήστε ένα αρχείο _.env_ με το ακόλουθο περιεχόμενο:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Εντοπίστε αυτές τις πληροφορίες στην Πύλη Azure για τον πόρο σας στην ενότητα "Κλειδιά και Τέλος Σημείου".

1. Συλλέξτε τις παραπάνω βιβλιοθήκες σε ένα αρχείο που ονομάζεται _requirements.txt_ όπως εξής:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Στη συνέχεια, δημιουργήστε εικονικό περιβάλλον και εγκαταστήστε τις βιβλιοθήκες:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Για Windows, χρησιμοποιήστε τις ακόλουθες εντολές για να δημιουργήσετε και να ενεργοποιήσετε το εικονικό σας περιβάλλον:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Προσθέστε τον ακόλουθο κώδικα σε ένα αρχείο που ονομάζεται _app.py_:

   ```python
   import openai
   import os
   import requests
   from PIL import Image
   import dotenv

   # import dotenv
   dotenv.load_dotenv()

   # Get endpoint and key from environment variables
   openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
   openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

   # Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
   openai.api_version = '2023-06-01-preview'
   openai.api_type = 'azure'


   try:
       # Create an image by using the image generation API
       generation_response = openai.Image.create(
           prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
           size='1024x1024',
           n=2,
           temperature=0,
       )
       # Set the directory for the stored image
       image_dir = os.path.join(os.curdir, 'images')

       # If the directory doesn't exist, create it
       if not os.path.isdir(image_dir):
           os.mkdir(image_dir)

       # Initialize the image path (note the filetype should be png)
       image_path = os.path.join(image_dir, 'generated-image.png')

       # Retrieve the generated image
       image_url = generation_response["data"][0]["url"]  # extract image URL from response
       generated_image = requests.get(image_url).content  # download the image
       with open(image_path, "wb") as image_file:
           image_file.write(generated_image)

       # Display the image in the default image viewer
       image = Image.open(image_path)
       image.show()

   # catch exceptions
   except openai.InvalidRequestError as err:
       print(err)

   ```

Ας εξηγήσουμε αυτόν τον κώδικα:

- Πρώτα, εισάγουμε τις βιβλιοθήκες που χρειαζόμαστε, συμπεριλαμβανομένης της βιβλιοθήκης OpenAI, της βιβλιοθήκης dotenv, της βιβλιοθήκης requests και της βιβλιοθήκης Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Στη συνέχεια, φορτώνουμε τις μεταβλητές περιβάλλοντος από το αρχείο _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Μετά από αυτό, ορίζουμε το τέλος σημείου, το κλειδί για το OpenAI API, την έκδοση και τον τύπο.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- Στη συνέχεια, δημιουργούμε την εικόνα:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  Ο παραπάνω κώδικας ανταποκρίνεται με ένα αντικείμενο JSON που περιέχει τη διεύθυνση URL της παραγόμενης εικόνας. Μπορούμε να χρησιμοποιήσουμε τη διεύθυνση URL για να κατεβάσουμε την εικόνα και να την αποθηκεύσουμε σε ένα αρχείο.

- Τέλος, ανοίγουμε την εικόνα και χρησιμοποιούμε το πρότυπο πρόγραμμα προβολής εικόνων για να την εμφανίσουμε:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Περισσότερες λεπτομέρειες για τη δημιουργία της εικόνας

Ας δούμε τον κώδικα που δημιουργεί την εικόνα με περισσότερες λεπτομέρειες:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, είναι η προτροπή κειμένου που χρησιμοποιείται για τη δημιουργία της εικόνας. Σε αυτή την περίπτωση, χρησιμοποιούμε την προτροπή "Κουνέλι πάνω σε άλογο, κρατώντας γλειφιτζούρι, σε ομιχλώδες λιβάδι όπου φυτρώνουν νάρκισσοι".
- **size**, είναι το μέγεθος της εικόνας που δημιουργείται. Σε αυτή την περίπτωση, δημιουργούμε μια εικόνα που είναι 1024x1024 pixels.
- **n**, είναι ο αριθμός των εικόνων που δημιουργούνται. Σε αυτή την περίπτωση, δημιουργούμε δύο εικόνες.
- **temperature**, είναι μια παράμετρος που ελέγχει την τυχαιότητα του αποτελέσματος ενός μοντέλου Γενετικής Τεχνητής Νοημοσύνης. Η θερμοκρασία είναι μια τιμή μεταξύ 0 και 1 όπου το 0 σημαίνει ότι το αποτέλεσμα είναι ντετερμινιστικό και το 1 σημαίνει ότι το αποτέλεσμα είναι τυχαίο. Η προεπιλεγμένη τιμή είναι 0.7.

Υπάρχουν περισσότερα πράγματα που μπορείτε να κάνετε με εικόνες που θα καλύψουμε στην επόμενη ενότητα.

## Πρόσθετες δυνατότητες της παραγωγής εικόνων

Έχετε δει μέχρι στιγμής πώς μπορέσαμε να δημιουργήσουμε μια εικόνα χρησιμοποιώντας λίγες γραμμές στην Python. Ωστόσο, υπάρχουν περισσότερα πράγματα που μπορείτε να κάνετε με εικόνες.

Μπορείτε επίσης να κάνετε τα εξής:

- **Εκτέλεση επεξεργασιών**. Παρέχοντας μια υπάρχουσα εικόνα, μια μάσκα και μια προτροπή, μπορείτε να τροποποιήσετε μια εικόνα. Για παράδειγμα, μπορείτε να προσθέσετε κάτι σε ένα μέρος μιας εικόνας. Φανταστείτε την εικόνα του κουνελιού μας, μπορείτε να προσθέσετε ένα καπέλο στο κουνέλι. Πώς θα το κάνετε αυτό είναι παρέχοντας την εικόνα, μια μάσκα (που αναγνωρίζει το μέρος της περιοχής για την αλλαγή) και μια προτροπή κειμένου για να πείτε τι πρέπει να γίνει.

  ```python
  response = openai.Image.create_edit(
    image=open("base_image.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="An image of a rabbit with a hat on its head.",
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  Η βασική εικόνα θα περιέχει μόνο το κουνέλι, αλλά η τελική εικόνα θα έχει το καπέλο στο κουνέλι.

- **Δημιουργία παραλλαγών**. Η ιδέα είναι να πάρετε μια υπάρχουσα εικόνα και να ζητήσετε να δημιουργηθούν παραλλαγές. Για να δημιουργήσετε μια παραλλαγή, παρέχετε μια εικόνα και μια προτροπή κειμένου και κώδικα όπως εξής:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Σημείωση, αυτό υποστηρίζεται μόνο στο OpenAI

## Θερμοκρασία

Η θερμοκρασία είναι μια παράμετρος που ελέγχει την τυχαιότητα του αποτελέσματος ενός μοντέλου Γενετικής Τεχνητής Νοημοσύνης. Η θερμοκρασία είναι μια τιμή μεταξύ 0 και 1 όπου το 0 σημαίνει ότι το αποτέλεσμα είναι ντετερμινιστικό και το 1 σημαίνει ότι το αποτέλεσμα είναι τυχαίο. Η προεπιλεγμένη τιμή είναι 0.7.

Ας δούμε ένα παράδειγμα για το πώς λειτουργεί η θερμοκρασία, εκτελώντας αυτή την προτροπή δύο φορές:

> Προτροπή: "Κουνέλι πάνω σε άλογο, κρατώντας γλειφιτζούρι, σε ομιχλώδες λιβάδι όπου φυτρώνουν νάρκισσοι"

Τώρα ας εκτελέσουμε την ίδια προτροπή μόνο για να δούμε ότι δεν θα πάρουμε την ίδια εικόνα δύο φορές:

Όπως μπορείτε να δείτε, οι εικόνες είναι παρόμοιες, αλλά όχι ίδιες. Ας δοκιμάσουμε να αλλάξουμε την τιμή της θερμοκρασίας σε 0.1 και να δούμε τι θα συμβεί:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Αλλαγή της θερμοκρασίας

Ας προσπαθήσουμε λοιπόν να κάνουμε την απόκριση πιο ντετερμινιστική. Μπορούσαμε να παρατηρήσουμε από τις δύο εικόνες που δημιουργήσαμε ότι στην πρώτη εικόνα υπάρχει ένα κουνέλι και στη δεύτερη εικόνα υπάρχει ένα άλογο, οπότε οι εικόνες ποικίλουν πολύ.

Ας αλλάξουμε λοιπόν τον κώδικά μας και ας ορίσουμε τη θερμοκρασία στο 0, όπως εξής:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Τώρα, όταν εκτελέσετε αυτόν τον κώδικα, θα πάρετε αυτές τις δύο εικόνες:

Εδώ μπορείτε να δείτε καθαρά πώς οι εικόνες μοιάζουν περισσότερο μεταξύ τους.

## Πώς να ορίσετε όρια για την εφαρμογή σας με μεταπροτροπές

Με την επίδειξή μας, μπορούμε ήδη να δημιουργήσουμε εικόνες για τους πελάτες μας. Ωστόσο, πρέπει να δημιουργήσουμε ορισμένα όρια για την εφαρμογή μας.

Για παράδειγμα, δεν θέλουμε να δημιουργούμε εικόνες που δεν είναι κατάλληλες για εργασία ή που δεν είναι κατάλληλες για παιδιά.

Μπορούμε να το κάνουμε αυτό με _μεταπροτροπές_. Οι μεταπροτροπές είναι προτροπές κειμένου που χρησιμοποιούνται για να ελέγξουν το αποτέλεσμα ενός μοντέλου Γενετικής Τεχνητής Νοημοσύνης. Για παράδειγμα, μπορούμε να χρησιμοποιήσουμε μεταπροτροπές για να ελέγξουμε το αποτέλεσμα και να διασφαλίσουμε ότι οι παραγόμενες εικόνες είναι κατάλληλες για εργασία ή κατάλληλες για παιδιά.

### Πώς λειτουργεί;

Τώρα, πώς λειτουργούν οι μεταπροτροπές;

Οι μεταπροτροπές είναι προτροπές κειμένου που χρησιμοποιούνται για να ελέγξουν το αποτέλεσμα ενός μοντέλου Γενετικής Τεχνητής Νοημοσύνης, τοποθετούνται πριν από την προτροπή κειμένου και χρησιμοποιούνται για να ελέγξουν το αποτέλεσμα του μοντέλου και ενσωματώνονται σε εφαρμογές για να ελέγξουν το αποτέλεσμα του μοντέλου. Εγκλεισμό της εισόδου προτροπής και της εισόδου μεταπροτροπής σε μια ενιαία προτροπή κειμένου.

Ένα παράδειγμα μεταπροτροπής θα ήταν το εξής:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Τώρα, ας δούμε πώς μπορούμε να χρησιμοποιήσουμε μεταπροτροπές στην επίδειξή μας.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt =f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"{meta_prompt}
Create an image of a bunny on a horse, holding a lollipop"

# TODO add request to generate image
```

Από την παραπάνω προτροπή, μπορείτε να δείτε πώς όλες οι εικόνες που δημιουργούνται λαμβάνουν υπόψη τη μεταπροτροπή.

## Ανάθεση - ας ενεργοποιήσουμε τους μαθητές

Εισαγάγαμε το Edu4All στην αρχή αυτού του μαθήματος. Τώρα είναι καιρός να επιτρέψουμε στους μαθητές να δημιουργήσουν εικόνες για τις αξιολογήσεις τους.

Οι μαθητές θα δημιουργήσουν εικόνες για τις αξιολογήσεις τους που περιέχουν μνημεία, τι ακριβώς μνημεία είναι θέμα των μαθητών. Οι μαθητές καλούνται να χρησιμοποιήσουν τη δημιουργικότητά τους σε αυτή την εργασία για να τοποθετήσουν αυτά τα μνημεία σε διαφορετικά πλαίσια.

## Λύση

Να μια πιθανή λύση:

```python
import openai
import os
import requests
from PIL import Image
import dotenv

# import dotenv
dotenv.load_dotenv()

# Get endpoint and key from environment variables
openai.api_base = "<replace with endpoint>"
openai.api_key = "<replace with api key>"

# Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
openai.api_version = '2023-06-01-preview'
openai.api_type = 'azure'

disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}"""

prompt = f"""{metaprompt}
Generate monument of the Arc of Triumph in Paris, France, in the evening light with a small child holding a Teddy looks on.
""""

try:
    # Create an image by using the image generation API
    generation_response = openai.Image.create(
        prompt=prompt,    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    image_url = generation_response["data"][0]["url"]  # extract image URL from response
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
except openai.InvalidRequestError as err:
    print(err)
```

## Καλή δουλειά! Συνεχίστε τη Μάθησή σας

Μετά την ολοκλήρωση αυτού του μαθήματος, ελέγξτε τη [Συλλογή Μάθησης Γενετικής Τεχνητής Νοημοσύνης](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) για να συνεχίσετε να βελτιώνετε τις γνώσεις σας στη Γενετική Τεχνητή Νοημοσύνη!

Προχωρήστε στο Μάθημα 10 όπου θα δούμε πώς να [δημιουργήσετε εφαρμογές AI με χαμηλό κώδικα](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλώ να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις μπορεί να περιέχουν λάθη ή ανακρίβειες. Το αρχικό έγγραφο στη γλώσσα του θα πρέπει να θεωρείται η έγκυρη πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.