<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "063a2ac57d6b71bea0eaa880c68770d2",
  "translation_date": "2025-09-29T21:44:03+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "el"
}
-->
# Δημιουργία Εφαρμογών Γεννήτριας Εικόνων

[![Δημιουργία Εφαρμογών Γεννήτριας Εικόνων](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.el.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Τα LLMs δεν περιορίζονται μόνο στη δημιουργία κειμένου. Είναι επίσης δυνατό να δημιουργηθούν εικόνες από περιγραφές κειμένου. Η χρήση εικόνων ως μέσο μπορεί να είναι εξαιρετικά χρήσιμη σε πολλούς τομείς, όπως η ιατρική τεχνολογία, η αρχιτεκτονική, ο τουρισμός, η ανάπτυξη παιχνιδιών και άλλα. Σε αυτό το κεφάλαιο, θα εξετάσουμε τα δύο πιο δημοφιλή μοντέλα δημιουργίας εικόνων, το DALL-E και το Midjourney.

## Εισαγωγή

Σε αυτό το μάθημα, θα καλύψουμε:

- Τη δημιουργία εικόνων και γιατί είναι χρήσιμη.
- Τα DALL-E και Midjourney, τι είναι και πώς λειτουργούν.
- Πώς μπορείτε να δημιουργήσετε μια εφαρμογή γεννήτριας εικόνων.

## Στόχοι Μάθησης

Μετά την ολοκλήρωση αυτού του μαθήματος, θα μπορείτε:

- Να δημιουργήσετε μια εφαρμογή γεννήτριας εικόνων.
- Να ορίσετε όρια για την εφαρμογή σας με μετα-προτροπές.
- Να εργαστείτε με τα DALL-E και Midjourney.

## Γιατί να δημιουργήσετε μια εφαρμογή γεννήτριας εικόνων;

Οι εφαρμογές γεννήτριας εικόνων είναι ένας εξαιρετικός τρόπος για να εξερευνήσετε τις δυνατότητες της Γεννητικής Τεχνητής Νοημοσύνης. Μπορούν να χρησιμοποιηθούν, για παράδειγμα:

- **Επεξεργασία και σύνθεση εικόνων**. Μπορείτε να δημιουργήσετε εικόνες για διάφορες χρήσεις, όπως επεξεργασία και σύνθεση εικόνων.

- **Εφαρμογή σε διάφορους κλάδους**. Μπορούν επίσης να χρησιμοποιηθούν για τη δημιουργία εικόνων για διάφορους κλάδους, όπως η ιατρική τεχνολογία, ο τουρισμός, η ανάπτυξη παιχνιδιών και άλλα.

## Σενάριο: Edu4All

Στο πλαίσιο αυτού του μαθήματος, θα συνεχίσουμε να εργαζόμαστε με τη startup μας, Edu4All. Οι μαθητές θα δημιουργήσουν εικόνες για τις εργασίες τους. Το είδος των εικόνων εξαρτάται από τους μαθητές, αλλά θα μπορούσαν να είναι εικονογραφήσεις για το δικό τους παραμύθι, να δημιουργήσουν έναν νέο χαρακτήρα για την ιστορία τους ή να τους βοηθήσουν να οπτικοποιήσουν τις ιδέες και τις έννοιές τους.

Για παράδειγμα, αν οι μαθητές της Edu4All εργάζονται στην τάξη πάνω σε μνημεία, θα μπορούσαν να δημιουργήσουν κάτι σαν:

![Startup Edu4All, τάξη για μνημεία, Πύργος του Άιφελ](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.el.png)

χρησιμοποιώντας μια προτροπή όπως:

> "Σκύλος δίπλα στον Πύργο του Άιφελ στο πρωινό φως του ήλιου"

## Τι είναι τα DALL-E και Midjourney;

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) και [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) είναι δύο από τα πιο δημοφιλή μοντέλα δημιουργίας εικόνων, που σας επιτρέπουν να χρησιμοποιείτε προτροπές για τη δημιουργία εικόνων.

### DALL-E

Ας ξεκινήσουμε με το DALL-E, το οποίο είναι ένα μοντέλο Γεννητικής Τεχνητής Νοημοσύνης που δημιουργεί εικόνες από περιγραφές κειμένου.

> [Το DALL-E είναι ένας συνδυασμός δύο μοντέλων, CLIP και diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, είναι ένα μοντέλο που δημιουργεί ενσωματώσεις, οι οποίες είναι αριθμητικές αναπαραστάσεις δεδομένων, από εικόνες και κείμενο.

- **Diffused attention**, είναι ένα μοντέλο που δημιουργεί εικόνες από ενσωματώσεις. Το DALL-E εκπαιδεύεται σε ένα σύνολο δεδομένων εικόνων και κειμένου και μπορεί να χρησιμοποιηθεί για τη δημιουργία εικόνων από περιγραφές κειμένου. Για παράδειγμα, το DALL-E μπορεί να χρησιμοποιηθεί για τη δημιουργία εικόνων μιας γάτας με καπέλο ή ενός σκύλου με μοϊκάνα.

### Midjourney

Το Midjourney λειτουργεί με παρόμοιο τρόπο με το DALL-E, δημιουργεί εικόνες από προτροπές κειμένου. Το Midjourney μπορεί επίσης να χρησιμοποιηθεί για τη δημιουργία εικόνων χρησιμοποιώντας προτροπές όπως "μια γάτα με καπέλο" ή "ένας σκύλος με μοϊκάνα".

![Εικόνα που δημιουργήθηκε από το Midjourney, μηχανικό περιστέρι](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Πηγή εικόνας Wikipedia, εικόνα που δημιουργήθηκε από το Midjourney_

## Πώς λειτουργούν τα DALL-E και Midjourney

Πρώτα, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). Το DALL-E είναι ένα μοντέλο Γεννητικής Τεχνητής Νοημοσύνης βασισμένο στην αρχιτεκτονική transformer με έναν _autoregressive transformer_.

Ένας _autoregressive transformer_ καθορίζει πώς ένα μοντέλο δημιουργεί εικόνες από περιγραφές κειμένου, δημιουργεί ένα pixel τη φορά και στη συνέχεια χρησιμοποιεί τα παραγόμενα pixels για να δημιουργήσει το επόμενο pixel. Περνώντας μέσα από πολλαπλά επίπεδα σε ένα νευρωνικό δίκτυο, μέχρι να ολοκληρωθεί η εικόνα.

Με αυτή τη διαδικασία, το DALL-E ελέγχει χαρακτηριστικά, αντικείμενα, ιδιότητες και άλλα στην εικόνα που δημιουργεί. Ωστόσο, το DALL-E 2 και 3 έχουν μεγαλύτερο έλεγχο πάνω στην παραγόμενη εικόνα.

## Δημιουργία της πρώτης σας εφαρμογής γεννήτριας εικόνων

Τι χρειάζεται λοιπόν για να δημιουργήσετε μια εφαρμογή γεννήτριας εικόνων; Χρειάζεστε τις εξής βιβλιοθήκες:

- **python-dotenv**, συνιστάται ιδιαίτερα να χρησιμοποιήσετε αυτήν τη βιβλιοθήκη για να κρατήσετε τα μυστικά σας σε ένα αρχείο _.env_ μακριά από τον κώδικα.
- **openai**, αυτή η βιβλιοθήκη είναι αυτή που θα χρησιμοποιήσετε για να αλληλεπιδράσετε με το OpenAI API.
- **pillow**, για να εργαστείτε με εικόνες σε Python.
- **requests**, για να σας βοηθήσει να κάνετε αιτήματα HTTP.

## Δημιουργία και ανάπτυξη μοντέλου Azure OpenAI

Αν δεν το έχετε κάνει ήδη, ακολουθήστε τις οδηγίες στη σελίδα [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) 
για να δημιουργήσετε έναν πόρο και μοντέλο Azure OpenAI. Επιλέξτε το DALL-E 3 ως μοντέλο.

## Δημιουργία της εφαρμογής

1. Δημιουργήστε ένα αρχείο _.env_ με το εξής περιεχόμενο:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Εντοπίστε αυτές τις πληροφορίες στο Azure OpenAI Foundry Portal για τον πόρο σας στην ενότητα "Deployments".

1. Συγκεντρώστε τις παραπάνω βιβλιοθήκες σε ένα αρχείο που ονομάζεται _requirements.txt_ όπως παρακάτω:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Στη συνέχεια, δημιουργήστε ένα εικονικό περιβάλλον και εγκαταστήστε τις βιβλιοθήκες:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Για Windows, χρησιμοποιήστε τις παρακάτω εντολές για να δημιουργήσετε και να ενεργοποιήσετε το εικονικό σας περιβάλλον:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Προσθέστε τον παρακάτω κώδικα σε ένα αρχείο που ονομάζεται _app.py_:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # import dotenv
    dotenv.load_dotenv()
    
    # configure Azure OpenAI service client 
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
    try:
        # Create an image by using the image generation API
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # Set the directory for the stored image
        image_dir = os.path.join(os.curdir, 'images')

        # If the directory doesn't exist, create it
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Initialize the image path (note the filetype should be png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Retrieve the generated image
        image_url = generation_response.data[0].url  # extract image URL from response
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

- Πρώτα, εισάγουμε τις βιβλιοθήκες που χρειαζόμαστε, συμπεριλαμβανομένων των OpenAI, dotenv, requests και Pillow.

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

- Μετά από αυτό, διαμορφώνουμε τον πελάτη υπηρεσίας Azure OpenAI.

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- Στη συνέχεια, δημιουργούμε την εικόνα:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  Ο παραπάνω κώδικας επιστρέφει ένα αντικείμενο JSON που περιέχει τη διεύθυνση URL της παραγόμενης εικόνας. Μπορούμε να χρησιμοποιήσουμε τη διεύθυνση URL για να κατεβάσουμε την εικόνα και να την αποθηκεύσουμε σε ένα αρχείο.

- Τέλος, ανοίγουμε την εικόνα και χρησιμοποιούμε τον τυπικό προβολέα εικόνων για να την εμφανίσουμε:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Περισσότερες λεπτομέρειες για τη δημιουργία της εικόνας

Ας δούμε τον κώδικα που δημιουργεί την εικόνα πιο αναλυτικά:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, είναι η προτροπή κειμένου που χρησιμοποιείται για τη δημιουργία της εικόνας. Σε αυτήν την περίπτωση, χρησιμοποιούμε την προτροπή "Λαγός πάνω σε άλογο, κρατώντας γλειφιτζούρι, σε ομιχλώδες λιβάδι όπου φυτρώνουν νάρκισσοι".
- **size**, είναι το μέγεθος της εικόνας που δημιουργείται. Σε αυτήν την περίπτωση, δημιουργούμε μια εικόνα 1024x1024 pixels.
- **n**, είναι ο αριθμός των εικόνων που δημιουργούνται. Σε αυτήν την περίπτωση, δημιουργούμε δύο εικόνες.
- **temperature**, είναι μια παράμετρος που ελέγχει την τυχαιότητα του αποτελέσματος ενός μοντέλου Γεννητικής Τεχνητής Νοημοσύνης. Η θερμοκρασία είναι μια τιμή μεταξύ 0 και 1, όπου το 0 σημαίνει ότι το αποτέλεσμα είναι ντετερμινιστικό και το 1 σημαίνει ότι το αποτέλεσμα είναι τυχαίο. Η προεπιλεγμένη τιμή είναι 0.7.

Υπάρχουν περισσότερα πράγματα που μπορείτε να κάνετε με εικόνες, τα οποία θα καλύψουμε στην επόμενη ενότητα.

## Πρόσθετες δυνατότητες δημιουργίας εικόνων

Έχετε δει μέχρι τώρα πώς μπορέσαμε να δημιουργήσουμε μια εικόνα χρησιμοποιώντας λίγες γραμμές κώδικα σε Python. Ωστόσο, υπάρχουν περισσότερα πράγματα που μπορείτε να κάνετε με εικόνες.

Μπορείτε επίσης να κάνετε τα εξής:

- **Επεξεργασία εικόνων**. Παρέχοντας μια υπάρχουσα εικόνα, μια μάσκα και μια προτροπή, μπορείτε να τροποποιήσετε μια εικόνα. Για παράδειγμα, μπορείτε να προσθέσετε κάτι σε ένα μέρος της εικόνας. Φανταστείτε την εικόνα του λαγού μας, μπορείτε να προσθέσετε ένα καπέλο στον λαγό. Πώς θα το κάνετε αυτό είναι παρέχοντας την εικόνα, μια μάσκα (που προσδιορίζει το μέρος της περιοχής για την αλλαγή) και μια προτροπή κειμένου που λέει τι πρέπει να γίνει. 
> Σημείωση: αυτό δεν υποστηρίζεται στο DALL-E 3.

Εδώ είναι ένα παράδειγμα χρησιμοποιώντας το GPT Image:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  Η βασική εικόνα θα περιείχε μόνο το lounge με την πισίνα, αλλά η τελική εικόνα θα είχε ένα φλαμίνγκο:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.el.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.el.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.el.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **Δημιουργία παραλλαγών**. Η ιδέα είναι ότι παίρνετε μια υπάρχουσα εικόνα και ζητάτε να δημιουργηθούν παραλλαγές. Για να δημιουργήσετε μια παραλλαγή, παρέχετε μια εικόνα και μια προτροπή κειμένου και κώδικα όπως παρακάτω:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Σημείωση, αυτό υποστηρίζεται μόνο στο OpenAI.

## Θερμοκρασία

Η θερμοκρασία είναι μια παράμετρος που ελέγχει την τυχαιότητα του αποτελέσματος ενός μοντέλου Γεννητικής Τεχνητής Νοημοσύνης. Η θερμοκρασία είναι μια τιμή μεταξύ 0 και 1, όπου το 0 σημαίνει ότι το αποτέλεσμα είναι ντετερμινιστικό και το 1 σημαίνει ότι το αποτέλεσμα είναι τυχαίο. Η προεπιλεγμένη τιμή είναι 0.7.

Ας δούμε ένα παράδειγμα για το πώς λειτουργεί η θερμοκρασία, εκτελώντας αυτήν την προτροπή δύο φορές:

> Προτροπή: "Λαγός πάνω σε άλογο, κρατώντας γλειφιτζούρι, σε ομιχλώδες λιβάδι όπου φυτρώνουν νάρκισσοι"

![Λαγός πάνω σε άλογο κρατώντας γλειφιτζούρι, έκδοση 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.el.png)

Τώρα ας εκτελέσουμε την ίδια προτροπή για να δούμε ότι δεν θα πάρουμε την ίδια εικόνα δύο φορές:

![Παραγόμενη εικόνα λαγού πάνω σε άλογο](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.el.png)

Όπως μπορείτε να δείτε, οι εικόνες είναι παρόμοιες, αλλά όχι ίδιες. Ας δοκιμάσουμε να αλλάξουμε την τιμή της θερμοκρασίας σε 0.1 και να δούμε τι συμβαίνει:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Αλλαγή της θερμοκρασίας

Ας προσπαθήσουμε να κάνουμε την απάντηση πιο ντετερμινιστική. Μπορούμε να παρατηρήσουμε από τις δύο εικόνες που δημιουργήσαμε ότι στην πρώτη εικόνα υπάρχει ένας λαγός και στη δεύτερη εικόνα υπάρχει ένα άλογο, οπότε οι εικόνες διαφέρουν πολύ.

Ας αλλάξουμε λοιπόν τον κώδικά μας και να ορίσουμε τη θερμοκρασία στο 0, όπως παρακάτω:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Τώρα όταν εκτελέσετε αυτόν τον κώδικα, θα πάρετε αυτές τις δύο εικόνες:

- ![Θερμοκρασία 0, έκδοση 1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.el.png)
- ![Θερμοκρασία 0, έκδοση 2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.el.png)

Εδώ μπορείτε να δείτε καθαρά πώς οι εικόνες μοιάζουν περισσότερο μεταξύ τους.

## Πώς να ορίσετε όρια για την εφαρμογή σας με μετα-προτροπές

Με το demo μας, μπορούμε ήδη να δημιουργούμε εικόνες για τους πελάτες μας. Ωστόσο, πρέπει να δημιουργήσουμε κάποια όρια για την εφαρμογή μας.

Για παράδειγμα, δεν θέλουμε να δημιουργούμε εικόνες που δεν είναι κατάλληλες για εργασία ή που δεν είναι κατάλληλες για παιδιά.

Μπορούμε να το κάνουμε αυτό με _μετα-προτροπές_. Οι μετα-προτροπές είναι προτροπές κειμένου που χρησιμοποιούνται για τον έλεγχο του αποτελέσματος ενός μοντέλου Γεννητικής Τεχνητής Νοημοσύνης. Για παράδειγμα, μπορούμε να χρησιμοποιήσουμε μετα-προτροπές για να ελέγξουμε το αποτέλεσμα και να διασφαλίσουμε ότι οι παραγόμενες εικόνες είναι κατάλληλες για εργασία ή κατάλληλες για παιδιά.

### Πώς λειτουργεί;

Πώς λειτουργούν λοιπόν οι μετα-προτροπές;

Οι μετα-προτροπές είναι προτροπές κειμένου που χρησιμοποιούνται για τον έλεγχο του αποτελέσματος ενός μοντέλου Γεννητικής Τεχνητής Νοημοσύνης. Τοποθετούνται πριν από την προτροπή κειμένου και χρησιμοποιούνται για τον έλεγχο του αποτελέσματος του μοντέλου και ενσωματώνονται στις εφαρμογές για τον έλεγχο του αποτελέσματος του μοντέλου. Ενσωματώνοντας την είσο
```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# import dotenv
dotenv.load_dotenv()

# Get endpoint and key from environment variables
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
  api_key=os.environ['AZURE_OPENAI_API_KEY'],
  api_version = "2024-02-01"
  )


disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"""{meta_prompt}
Generate monument of the Arc of Triumph in Paris, France, in the evening light with a small child holding a Teddy looks on.
""""

try:
    # Create an image by using the image generation API
    generation_response = client.images.generate(
        prompt=prompt,    # Enter your prompt text here
        size='1024x1024',
        n=1,
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    image_url = generation_response.data[0].url  # extract image URL from response
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
except openai.BadRequestError as err:
    print(err)
```

## Εξαιρετική Δουλειά! Συνεχίστε τη Μάθηση

Αφού ολοκληρώσετε αυτό το μάθημα, δείτε τη [συλλογή μάθησης για Γενετική Τεχνητή Νοημοσύνη](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) για να συνεχίσετε να αναβαθμίζετε τις γνώσεις σας στη Γενετική Τεχνητή Νοημοσύνη!

Προχωρήστε στο Μάθημα 10, όπου θα εξετάσουμε πώς να [δημιουργήσετε εφαρμογές Τεχνητής Νοημοσύνης με low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.