# Κατασκευή με τα Μοντέλα της Οικογένειας Meta

## Εισαγωγή

Αυτό το μάθημα θα καλύψει:

- Εξερεύνηση των δύο βασικών μοντέλων της οικογένειας Meta - Llama 3.1 και Llama 3.2
- Κατανόηση των περιπτώσεων χρήσης και σεναρίων για κάθε μοντέλο
- Δείγμα κώδικα για να δείξει τα μοναδικά χαρακτηριστικά κάθε μοντέλου


## Η Οικογένεια Μοντέλων Meta

Σε αυτό το μάθημα, θα εξερευνήσουμε 2 μοντέλα από την οικογένεια Meta ή "Llama Herd" - Llama 3.1 και Llama 3.2.

Αυτά τα μοντέλα διατίθενται σε διάφορες παραλλαγές και είναι διαθέσιμα στον [Κατάλογο Μοντέλων Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Σημείωση:** Το GitHub Models καταργείται στο τέλος Ιουλίου 2026. Εδώ είναι περισσότερες λεπτομέρειες για τη χρήση των [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) για πρωτοτυποποίηση με μοντέλα AI.

Παραλλαγές Μοντέλων:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Σημείωση: Το Llama 3 είναι επίσης διαθέσιμο στα Microsoft Foundry Models αλλά δεν θα καλυφθεί σε αυτό το μάθημα*

## Llama 3.1

Με 405 δισεκατομμύρια παραμέτρους, το Llama 3.1 ανήκει στην κατηγορία των ανοικτών μοντέλων μεγάλων γλωσσών (LLM).

Το μοντέλο είναι μια αναβάθμιση της προηγούμενης έκδοσης Llama 3 παρέχοντας:

- Μεγαλύτερο παράθυρο συμφραζομένων - 128k tokens έναντι 8k tokens
- Μεγαλύτερο μέγιστο αριθμό tokens εξόδου - 4096 έναντι 2048
- Καλύτερη υποστήριξη πολυγλωσσίας - λόγω αύξησης των tokens εκπαίδευσης

Αυτά επιτρέπουν στο Llama 3.1 να χειρίζεται πιο σύνθετες περιπτώσεις χρήσης κατά την ανάπτυξη εφαρμογών Generative AI, όπως:
- Native Function Calling - η δυνατότητα κλήσης εξωτερικών εργαλείων και συναρτήσεων εκτός της ροής LLM
- Καλύτερη απόδοση RAG - λόγω του μεγαλύτερου παραθύρου συμφραζομένων
- Παραγωγή συνθετικών δεδομένων - η δυνατότητα δημιουργίας αποτελεσματικών δεδομένων για εργασίες όπως το fine-tuning

### Native Function Calling

Το Llama 3.1 έχει βελτιωθεί για να είναι πιο αποτελεσματικό στην κλήση συναρτήσεων ή εργαλείων. Διαθέτει επίσης δύο ενσωματωμένα εργαλεία που το μοντέλο μπορεί να αναγνωρίσει ότι πρέπει να χρησιμοποιήσει βάσει της εντολής από τον χρήστη. Αυτά τα εργαλεία είναι:

- **Brave Search** - Μπορεί να χρησιμοποιηθεί για την αναζήτηση ενημερωμένων πληροφοριών όπως ο καιρός μέσω αναζήτησης στο διαδίκτυο
- **Wolfram Alpha** - Μπορεί να χρησιμοποιηθεί για πιο σύνθετους μαθηματικούς υπολογισμούς ώστε να μην χρειάζεται να γράφετε τις δικές σας συναρτήσεις.

Μπορείτε επίσης να δημιουργήσετε δικά σας προσαρμοσμένα εργαλεία που το LLM μπορεί να καλέσει.

Στο παράδειγμα κώδικα παρακάτω:

- Ορίζουμε τα διαθέσιμα εργαλεία (brave_search, wolfram_alpha) στο σύστημα προτροπής.
- Στέλνουμε μια προτροπή χρήστη που ρωτά για τον καιρό σε μια συγκεκριμένη πόλη.
- Το LLM θα απαντήσει με μια κλήση εργαλείου προς το Brave Search tool που θα μοιάζει ως εξής `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Σημείωση: Αυτό το παράδειγμα κάνει μόνο την κλήση του εργαλείου, αν θέλετε να λάβετε τα αποτελέσματα, θα χρειαστεί να δημιουργήσετε δωρεάν λογαριασμό στη σελίδα Brave API και να ορίσετε τη συνάρτηση η ίδια.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Λάβετε αυτά από τη σελίδα "Επισκόπηση" του έργου σας Microsoft Foundry
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

Παρά το ότι είναι LLM, ένας περιορισμός του Llama 3.1 είναι η έλλειψη πολυτροπικότητας. Δηλαδή, η αδυναμία χρήσης διαφορετικών τύπων εισόδου όπως εικόνες ως προτροπές και παροχή απαντήσεων. Αυτή η δυνατότητα είναι ένα από τα κύρια χαρακτηριστικά του Llama 3.2. Αυτά τα χαρακτηριστικά περιλαμβάνουν επίσης:

- Πολυτροπικότητα - η ικανότητα αξιολόγησης τόσο κειμένων όσο και εικόνων ως προτροπών
- Παραλλαγές μικρού έως μεσαίου μεγέθους (11B και 90B) - παρέχει ευέλικτες επιλογές ανάπτυξης,
- Παραλλαγές μόνο κειμένου (1B και 3B) - επιτρέπει την ανάπτυξη του μοντέλου σε edge / κινητές συσκευές και παρέχει χαμηλή καθυστέρηση

Η υποστήριξη πολυτροπικότητας αντιπροσωπεύει ένα μεγάλο βήμα στον κόσμο των ανοικτών μοντέλων. Το παράδειγμα κώδικα παρακάτω παίρνει τόσο μια εικόνα όσο και μια προτροπή κειμένου για να πάρει μια ανάλυση της εικόνας από το Llama 3.2 90B.


### Υποστήριξη πολυτροπικότητας με το Llama 3.2

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

# Πάρτε αυτά από τη σελίδα "Επισκόπηση" του έργου σας στο Microsoft Foundry
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

Αφού ολοκληρώσετε αυτό το μάθημα, ρίξτε μια ματιά στη [Συλλογή Εκμάθησης Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) για να συνεχίσετε να ανεβάζετε το επίπεδο γνώσεών σας στα Generative AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->