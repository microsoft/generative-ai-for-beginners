# Κατασκευή με τα Μοντέλα Οικογένειας Meta 

## Εισαγωγή 

Αυτό το μάθημα θα καλύψει: 

- Εξερεύνηση των δύο βασικών μοντέλων οικογένειας Meta - Llama 3.1 και Llama 3.2 
- Κατανόηση των περιπτώσεων χρήσης και σεναρίων για κάθε μοντέλο 
- Παράδειγμα κώδικα για να δείξει τα μοναδικά χαρακτηριστικά κάθε μοντέλου 


## Η Οικογένεια Μοντέλων Meta 

Σε αυτό το μάθημα, θα εξερευνήσουμε 2 μοντέλα από την οικογένεια Meta ή "Llama Herd" - Llama 3.1 και Llama 3.2.

Αυτά τα μοντέλα διατίθενται σε διάφορες παραλλαγές και είναι διαθέσιμα στον [κατάλογο Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Σημείωση:** Το GitHub Models σταματά τη λειτουργία του στο τέλος Ιουλίου 2026. Εδώ θα βρείτε περισσότερες λεπτομέρειες για τη χρήση των [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) για πρωτότυπες εφαρμογές με μοντέλα AI.

Παραλλαγές Μοντέλων: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*Σημείωση: Το Llama 3 είναι επίσης διαθέσιμο στα Microsoft Foundry Models αλλά δεν θα καλυφθεί σε αυτό το μάθημα*

## Llama 3.1 

Με 405 δισεκατομμύρια παραμέτρους, το Llama 3.1 ανήκει στην κατηγορία ανοιχτού κώδικα LLM. 

Το μοντέλο είναι μια αναβάθμιση της προηγούμενης έκδοσης Llama 3 προσφέροντας: 

- Μεγαλύτερο παράθυρο συμφραζομένων - 128k tokens έναντι 8k tokens 
- Μεγαλύτερο μέγιστο αριθμό tokens εξόδου - 4096 έναντι 2048 
- Καλύτερη υποστήριξη πολυγλωσσίας - λόγω αύξησης των tokens εκπαίδευσης 

Αυτά επιτρέπουν στο Llama 3.1 να διαχειρίζεται πιο πολύπλοκες περιπτώσεις χρήσης κατά την κατασκευή εφαρμογών Γεννητικής Τεχνητής Νοημοσύνης, συμπεριλαμβανομένων: 
- Φυσική Κλήση Συναρτήσεων - η ικανότητα να καλεί εξωτερικά εργαλεία και συναρτήσεις εκτός της ροής εργασίας LLM
- Καλύτερη απόδοση RAG - λόγω του μεγαλύτερου παράθυρου συμφραζομένων 
- Σύνθεση Συνθετικών Δεδομένων - η ικανότητα δημιουργίας αποτελεσματικών δεδομένων για εργασίες όπως η λεπτομερή εκπαίδευση 

### Φυσική Κλήση Συναρτήσεων 

Το Llama 3.1 έχει βελτιωθεί ώστε να είναι πιο αποδοτικό στη δημιουργία κλήσεων συναρτήσεων ή εργαλείων. Διαθέτει επίσης δύο ενσωματωμένα εργαλεία που το μοντέλο μπορεί να αναγνωρίσει ως ανάγκη χρήσης βάσει του αιτήματος του χρήστη. Αυτά τα εργαλεία είναι: 

- **Brave Search** - Μπορεί να χρησιμοποιηθεί για να πάρει ενημερωμένες πληροφορίες όπως ο καιρός μέσω διαδικτυακής αναζήτησης 
- **Wolfram Alpha** - Μπορεί να χρησιμοποιηθεί για πιο σύνθετους μαθηματικούς υπολογισμούς ώστε να μην απαιτείται να γράφετε τις δικές σας συναρτήσεις. 

Μπορείτε επίσης να δημιουργήσετε τα δικά σας προσαρμοσμένα εργαλεία που το LLM μπορεί να καλεί. 

Στο παράδειγμα κώδικα παρακάτω: 

- Ορίζουμε τα διαθέσιμα εργαλεία (brave_search, wolfram_alpha) στην υπόδειξη συστήματος. 
- Στέλνουμε ένα αίτημα χρήστη που ρωτά για τον καιρό σε μια συγκεκριμένη πόλη. 
- Το LLM θα ανταποκριθεί με κλήση στο εργαλείο Brave Search που θα μοιάζει έτσι `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Σημείωση: Αυτό το παράδειγμα πραγματοποιεί μόνο την κλήση εργαλείου, αν θέλετε να πάρετε τα αποτελέσματα, θα χρειαστεί να δημιουργήσετε δωρεάν λογαριασμό στη σελίδα Brave API και να ορίσετε τη συνάρτηση μόνοι σας.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Λάβετε αυτά από τη σελίδα "Επισκόπηση" του έργου σας στο Microsoft Foundry
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Meta-Llama-3.1-405B-Instruct"

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

Παρόλο που είναι ένα LLM, ένας περιορισμός του Llama 3.1 είναι η έλλειψη πολυτροπικότητας. Δηλαδή, η αδυναμία χρήσης διαφορετικών τύπων εισόδων όπως εικόνες ως προτροπές και παροχή απαντήσεων. Αυτή η ικανότητα είναι ένα από τα βασικά χαρακτηριστικά του Llama 3.2. Αυτά τα χαρακτηριστικά περιλαμβάνουν επίσης: 

- Πολυτροπικότητα - έχει την ικανότητα να αξιολογεί τόσο κείμενο όσο και εικόνες ως προτροπές 
- Παραλλαγές μικρού έως μεσαίου μεγέθους (11B και 90B) - παρέχουν ευέλικτες επιλογές ανάπτυξης, 
- Μόνο κείμενο παραλλαγές (1B και 3B) - αυτό επιτρέπει στο μοντέλο να αναπτύσσεται σε περιφερειακές / φορητές συσκευές και παρέχει χαμηλή καθυστέρηση 

Η πολυτροπική υποστήριξη αποτελεί μεγάλο βήμα στον κόσμο των μοντέλων ανοιχτού κώδικα. Το παράδειγμα κώδικα παρακάτω λαμβάνει τόσο μια εικόνα όσο και μια κειμενική προτροπή για να πάρει ανάλυση της εικόνας από το Llama 3.2 90B. 


### Πολυτροπική Υποστήριξη με Llama 3.2

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

# Πάρτε τα από τη σελίδα "Επισκόπηση" του έργου Microsoft Foundry σας
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
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

Μετά την ολοκλήρωση αυτού του μαθήματος, ρίξτε μια ματιά στη [συλλογή Μάθησης Γεννητικής Τεχνητής Νοημοσύνης](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) για να συνεχίσετε να ανεβάζετε το επίπεδο γνώσεων σας στη Γεννητική AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->