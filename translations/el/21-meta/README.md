<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:11:29+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "el"
}
-->
# Κατασκευή με τα μοντέλα της οικογένειας Meta

## Εισαγωγή

Αυτό το μάθημα θα καλύψει:

- Εξερεύνηση των δύο κύριων μοντέλων της οικογένειας Meta - Llama 3.1 και Llama 3.2
- Κατανόηση των περιπτώσεων χρήσης και των σεναρίων για κάθε μοντέλο
- Παράδειγμα κώδικα για να δείξει τα μοναδικά χαρακτηριστικά κάθε μοντέλου

## Η οικογένεια μοντέλων Meta

Σε αυτό το μάθημα, θα εξερευνήσουμε 2 μοντέλα από την οικογένεια Meta ή "Llama Herd" - Llama 3.1 και Llama 3.2.

Αυτά τα μοντέλα έρχονται σε διάφορες παραλλαγές και είναι διαθέσιμα στην αγορά μοντέλων GitHub. Εδώ υπάρχουν περισσότερες λεπτομέρειες για τη χρήση των μοντέλων GitHub για [πρωτότυπο με μοντέλα AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Παραλλαγές μοντέλων:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Σημείωση: Το Llama 3 είναι επίσης διαθέσιμο στα μοντέλα GitHub αλλά δεν θα καλυφθεί σε αυτό το μάθημα*

## Llama 3.1

Με 405 δισεκατομμύρια παραμέτρους, το Llama 3.1 ανήκει στην κατηγορία των ανοιχτών πηγών LLM.

Το μοντέλο αποτελεί αναβάθμιση της προηγούμενης έκδοσης Llama 3 προσφέροντας:

- Μεγαλύτερο παράθυρο περιβάλλοντος - 128k tokens έναντι 8k tokens
- Μεγαλύτερα Μέγιστα Tokens Εξόδου - 4096 έναντι 2048
- Καλύτερη Πολυγλωσσική Υποστήριξη - λόγω αύξησης των εκπαιδευτικών tokens

Αυτά επιτρέπουν στο Llama 3.1 να διαχειρίζεται πιο σύνθετες περιπτώσεις χρήσης κατά την κατασκευή εφαρμογών GenAI, συμπεριλαμβανομένων:
- Κλήση Εγγενών Λειτουργιών - η δυνατότητα να καλεί εξωτερικά εργαλεία και λειτουργίες εκτός της ροής εργασίας LLM
- Καλύτερη Απόδοση RAG - λόγω του μεγαλύτερου παραθύρου περιβάλλοντος
- Δημιουργία Συνθετικών Δεδομένων - η δυνατότητα δημιουργίας αποτελεσματικών δεδομένων για εργασίες όπως η προσαρμογή

### Κλήση Εγγενών Λειτουργιών

Το Llama 3.1 έχει προσαρμοστεί ώστε να είναι πιο αποτελεσματικό στην κλήση λειτουργιών ή εργαλείων. Έχει επίσης δύο ενσωματωμένα εργαλεία που το μοντέλο μπορεί να αναγνωρίσει ως αναγκαία για χρήση βάσει της προτροπής από τον χρήστη. Αυτά τα εργαλεία είναι:

- **Brave Search** - Μπορεί να χρησιμοποιηθεί για να λαμβάνει ενημερωμένες πληροφορίες όπως ο καιρός μέσω αναζήτησης στο διαδίκτυο
- **Wolfram Alpha** - Μπορεί να χρησιμοποιηθεί για πιο σύνθετους μαθηματικούς υπολογισμούς, έτσι δεν απαιτείται να γράψετε τις δικές σας λειτουργίες.

Μπορείτε επίσης να δημιουργήσετε τα δικά σας προσαρμοσμένα εργαλεία που μπορεί να καλέσει το LLM.

Στο παράδειγμα κώδικα παρακάτω:

- Ορίζουμε τα διαθέσιμα εργαλεία (brave_search, wolfram_alpha) στην προτροπή συστήματος.
- Στέλνουμε μια προτροπή χρήστη που ρωτά για τον καιρό σε μια συγκεκριμένη πόλη.
- Το LLM θα απαντήσει με μια κλήση εργαλείου στο εργαλείο Brave Search που θα μοιάζει με `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Σημείωση: Αυτό το παράδειγμα κάνει μόνο την κλήση εργαλείου, αν θέλετε να λάβετε τα αποτελέσματα, θα χρειαστεί να δημιουργήσετε έναν δωρεάν λογαριασμό στη σελίδα Brave API και να ορίσετε την ίδια τη λειτουργία*

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

Παρόλο που είναι ένα LLM, ένας περιορισμός που έχει το Llama 3.1 είναι η πολυτροπικότητα. Δηλαδή, η δυνατότητα χρήσης διαφορετικών τύπων εισόδου όπως εικόνες ως προτροπές και παροχή απαντήσεων. Αυτή η δυνατότητα είναι ένα από τα κύρια χαρακτηριστικά του Llama 3.2. Αυτά τα χαρακτηριστικά περιλαμβάνουν επίσης:

- Πολυτροπικότητα - έχει τη δυνατότητα να αξιολογεί τόσο κείμενο όσο και προτροπές εικόνας
- Παραλλαγές μικρού έως μεσαίου μεγέθους (11B και 90B) - αυτό παρέχει ευέλικτες επιλογές ανάπτυξης
- Παραλλαγές μόνο κειμένου (1B και 3B) - αυτό επιτρέπει στο μοντέλο να αναπτυχθεί σε συσκευές edge / κινητές και παρέχει χαμηλή καθυστέρηση

Η υποστήριξη πολυτροπικότητας αντιπροσωπεύει ένα μεγάλο βήμα στον κόσμο των μοντέλων ανοιχτού κώδικα. Το παράδειγμα κώδικα παρακάτω λαμβάνει τόσο μια εικόνα όσο και μια προτροπή κειμένου για να πάρει μια ανάλυση της εικόνας από το Llama 3.2 90B.

### Υποστήριξη Πολυτροπικότητας με το Llama 3.2

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

Αφού ολοκληρώσετε αυτό το μάθημα, δείτε τη συλλογή μας [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) για να συνεχίσετε να αναβαθμίζετε τις γνώσεις σας στη Generative AI!

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ προσπαθούμε για ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το αρχικό έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για οποιεσδήποτε παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.