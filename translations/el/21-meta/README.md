# Κατασκευή με τα Μοντέλα Οικογένειας Meta

## Εισαγωγή

Αυτό το μάθημα θα καλύψει:

- Εξερεύνηση των δύο βασικών μοντέλων της οικογένειας Meta - Llama 3.1 και Llama 3.2
- Κατανόηση των περιπτώσεων χρήσης και σεναρίων για κάθε μοντέλο
- Παράδειγμα κώδικα για να δείξει τα μοναδικά χαρακτηριστικά κάθε μοντέλου

## Η Οικογένεια Μοντέλων Meta

Σε αυτό το μάθημα, θα εξερευνήσουμε 2 μοντέλα από την οικογένεια Meta ή "Llama Herd" - Llama 3.1 και Llama 3.2.

Αυτά τα μοντέλα υπάρχουν σε διαφορετικές παραλλαγές και είναι διαθέσιμα στην αγορά μοντέλων του GitHub. Εδώ υπάρχουν περισσότερες λεπτομέρειες για τη χρήση των GitHub Μοντέλων για [πρωτοτυπία με μοντέλα AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Παραλλαγές Μοντέλων:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Σημείωση: Το Llama 3 είναι επίσης διαθέσιμο στα GitHub Models αλλά δεν θα καλυφθεί σε αυτό το μάθημα*

## Llama 3.1

Με 405 Δισεκατομμύρια Παραμέτρους, το Llama 3.1 ανήκει στην κατηγορία ανοιχτού κώδικα LLM.

Το μοντέλο αποτελεί αναβάθμιση της προηγούμενης έκδοσης Llama 3 προσφέροντας:

- Μεγαλύτερο παράθυρο συμφραζομένων - 128k tokens έναντι 8k tokens
- Μεγαλύτερο Max Output Tokens - 4096 έναντι 2048
- Καλύτερη πολυγλωσσική υποστήριξη - λόγω αύξησης των tokens εκπαίδευσης

Αυτά επιτρέπουν στο Llama 3.1 να διαχειρίζεται πιο σύνθετες περιπτώσεις χρήσης κατά την κατασκευή εφαρμογών GenAI που περιλαμβάνουν:
- Φυσική κλήση λειτουργιών - η δυνατότητα κλήσης εξωτερικών εργαλείων και λειτουργιών εκτός της ροής εργασίας LLM
- Καλύτερη απόδοση RAG - λόγω του μεγαλύτερου παραθύρου συμφραζομένων
- Δημιουργία συνθετικών δεδομένων - η δυνατότητα δημιουργίας αποτελεσματικών δεδομένων για εργασίες όπως η λεπτομερής προσαρμογή

### Φυσική Κλήση Λειτουργιών

Το Llama 3.1 έχει βελτιωθεί ώστε να είναι πιο αποτελεσματικό στο να κάνει κλήσεις λειτουργίας ή εργαλείου. Διαθέτει επίσης δύο ενσωματωμένα εργαλεία που το μοντέλο μπορεί να αναγνωρίσει ότι πρέπει να χρησιμοποιήσει βάσει της προτροπής από τον χρήστη. Αυτά τα εργαλεία είναι:

- **Brave Search** - Μπορεί να χρησιμοποιηθεί για να πάρει ενημερωμένες πληροφορίες όπως ο καιρός μέσω αναζήτησης στον ιστό
- **Wolfram Alpha** - Μπορεί να χρησιμοποιηθεί για πιο σύνθετους μαθηματικούς υπολογισμούς, οπότε δεν απαιτείται να γράψετε τις δικές σας λειτουργίες.

Μπορείτε επίσης να δημιουργήσετε δικά σας εργαλεία που το LLM μπορεί να καλέσει.

Στο παρακάτω παράδειγμα κώδικα:

- Ορίζουμε τα διαθέσιμα εργαλεία (brave_search, wolfram_alpha) στην οδηγία συστήματος.
- Στέλνουμε μια προτροπή χρήστη που ρωτά για τον καιρό σε μια συγκεκριμένη πόλη.
- Το LLM θα απαντήσει με μια κλήση εργαλείου προς το Brave Search εργαλείο που θα μοιάζει σαν `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Σημείωση: Αυτό το παράδειγμα πραγματοποιεί μόνο την κλήση εργαλείου, αν θέλετε να πάρετε τα αποτελέσματα, θα πρέπει να δημιουργήσετε έναν δωρεάν λογαριασμό στη σελίδα Brave API και να ορίσετε τη λειτουργία.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "meta-llama-3.1-405b-instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)


tool_prompt=f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Environment: ipython
Tools: brave_search, wolfram_alpha
Cutting Knowledge Date: December 2023
Today Date: 23 July 2024

You are a helpful assistant<|eot_id|>
"""

messages = [
    SystemMessage(content=tool_prompt),
    UserMessage(content="What is the weather in Stockholm?"),

]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```

## Llama 3.2

Παρόλο που είναι LLM, ένας περιορισμός του Llama 3.1 είναι η έλλειψη πολυμορφικότητας. Δηλαδή, η αδυναμία χρήσης διαφορετικών τύπων εισόδου όπως εικόνες ως προτροπές και παροχή απαντήσεων. Αυτή η δυνατότητα είναι ένα από τα βασικά χαρακτηριστικά του Llama 3.2. Αυτά τα χαρακτηριστικά περιλαμβάνουν επίσης:

- Πολυμορφικότητα - έχει τη δυνατότητα αξιολόγησης τόσο κειμενικών όσο και εικόνων προτροπών
- Παραλλαγές μικρού έως μεσαίου μεγέθους (11B και 90B) - αυτό παρέχει ευέλικτες επιλογές ανάπτυξης,
- Παραλλαγές μόνο με κείμενο (1B και 3B) - αυτό επιτρέπει στο μοντέλο να αναπτυχθεί σε edge / κινητές συσκευές και παρέχει χαμηλή καθυστέρηση

Η υποστήριξη πολυμορφικότητας αντιπροσωπεύει ένα σημαντικό βήμα στον κόσμο των μοντέλων ανοιχτού κώδικα. Το παρακάτω παράδειγμα κώδικα λαμβάνει τόσο μια εικόνα όσο και μια κειμενική προτροπή για να πάρει ανάλυση της εικόνας από το Llama 3.2 90B.


### Πολυμορφική Υποστήριξη με το Llama 3.2

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    SystemMessage,
    UserMessage,
    TextContentItem,
    ImageContentItem,
    ImageUrl,
    ImageDetailLevel,
)
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "Llama-3.2-90B-Vision-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(
            content="You are a helpful assistant that describes images in details."
        ),
        UserMessage(
            content=[
                TextContentItem(text="What's in this image?"),
                ImageContentItem(
                    image_url=ImageUrl.load(
                        image_file="sample.jpg",
                        image_format="jpg",
                        detail=ImageDetailLevel.LOW)
                ),
            ],
        ),
    ],
    model=model_name,
)

print(response.choices[0].message.content)
```

## Η μάθηση δεν σταματά εδώ, συνεχίστε το ταξίδι

Αφού ολοκληρώσετε αυτό το μάθημα, ελέγξτε τη συλλογή μας [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) για να συνεχίσετε να ανεβάζετε το επίπεδό σας στη Γεννητική Τεχνητή Νοημοσύνη!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να λάβετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θεωρείται η επίσημη πηγή. Για κρίσιμες πληροφορίες, συνιστάται η επαγγελματική μετάφραση από ανθρώπους. Δεν φέρουμε ευθύνη για οποιεσδήποτε παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->