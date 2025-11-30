<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:10:01+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "el"
}
-->
# Κατασκευή με τα Μοντέλα της Οικογένειας Meta

## Εισαγωγή

Αυτό το μάθημα θα καλύψει:

- Εξερεύνηση των δύο βασικών μοντέλων της οικογένειας Meta - Llama 3.1 και Llama 3.2  
- Κατανόηση των περιπτώσεων χρήσης και σεναρίων για κάθε μοντέλο  
- Παράδειγμα κώδικα που δείχνει τα μοναδικά χαρακτηριστικά κάθε μοντέλου  

## Η Οικογένεια Μοντέλων Meta

Σε αυτό το μάθημα, θα εξερευνήσουμε 2 μοντέλα από την οικογένεια Meta ή "Llama Herd" - Llama 3.1 και Llama 3.2

Αυτά τα μοντέλα διατίθενται σε διάφορες παραλλαγές και είναι διαθέσιμα στην αγορά μοντέλων του GitHub. Εδώ θα βρείτε περισσότερες λεπτομέρειες για τη χρήση των GitHub Models για [πρωτοτυποποίηση με μοντέλα AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Παραλλαγές Μοντέλων:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*Σημείωση: Το Llama 3 είναι επίσης διαθέσιμο στα GitHub Models αλλά δεν θα καλυφθεί σε αυτό το μάθημα*

## Llama 3.1

Με 405 δισεκατομμύρια παραμέτρους, το Llama 3.1 ανήκει στην κατηγορία ανοιχτού κώδικα LLM.

Το μοντέλο αποτελεί αναβάθμιση της προηγούμενης έκδοσης Llama 3 προσφέροντας:

- Μεγαλύτερο παράθυρο συμφραζομένων - 128k tokens έναντι 8k tokens  
- Μεγαλύτερο μέγιστο αριθμό tokens εξόδου - 4096 έναντι 2048  
- Καλύτερη υποστήριξη πολυγλωσσίας - λόγω αύξησης των tokens εκπαίδευσης  

Αυτά επιτρέπουν στο Llama 3.1 να διαχειρίζεται πιο σύνθετες περιπτώσεις χρήσης κατά την κατασκευή εφαρμογών GenAI, όπως:  
- Native Function Calling - η δυνατότητα κλήσης εξωτερικών εργαλείων και συναρτήσεων εκτός της ροής εργασίας του LLM  
- Καλύτερη απόδοση RAG - λόγω του μεγαλύτερου παραθύρου συμφραζομένων  
- Δημιουργία συνθετικών δεδομένων - η δυνατότητα παραγωγής αποτελεσματικών δεδομένων για εργασίες όπως η λεπτομερής εκπαίδευση  

### Native Function Calling

Το Llama 3.1 έχει βελτιστοποιηθεί ώστε να είναι πιο αποτελεσματικό στην κλήση συναρτήσεων ή εργαλείων. Διαθέτει επίσης δύο ενσωματωμένα εργαλεία που το μοντέλο μπορεί να αναγνωρίσει ότι πρέπει να χρησιμοποιηθούν βάσει της εντολής του χρήστη. Αυτά τα εργαλεία είναι:

- **Brave Search** - Μπορεί να χρησιμοποιηθεί για να λάβει ενημερωμένες πληροφορίες, όπως ο καιρός, πραγματοποιώντας αναζήτηση στο διαδίκτυο  
- **Wolfram Alpha** - Μπορεί να χρησιμοποιηθεί για πιο σύνθετους μαθηματικούς υπολογισμούς, χωρίς να χρειάζεται να γράψετε δικές σας συναρτήσεις  

Μπορείτε επίσης να δημιουργήσετε τα δικά σας προσαρμοσμένα εργαλεία που το LLM μπορεί να καλέσει.

Στο παράδειγμα κώδικα παρακάτω:

- Ορίζουμε τα διαθέσιμα εργαλεία (brave_search, wolfram_alpha) στην εντολή συστήματος.  
- Στέλνουμε μια εντολή χρήστη που ρωτά για τον καιρό σε μια συγκεκριμένη πόλη.  
- Το LLM θα απαντήσει με κλήση εργαλείου προς το Brave Search, που θα μοιάζει με αυτό `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*Σημείωση: Αυτό το παράδειγμα κάνει μόνο την κλήση εργαλείου, αν θέλετε να λάβετε τα αποτελέσματα, θα χρειαστεί να δημιουργήσετε δωρεάν λογαριασμό στη σελίδα του Brave API και να ορίσετε τη συνάρτηση*  

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

Παρόλο που είναι LLM, ένα περιοριστικό στοιχείο του Llama 3.1 είναι η πολυμορφικότητα (multimodality). Δηλαδή, η δυνατότητα χρήσης διαφορετικών τύπων εισόδου, όπως εικόνες ως εντολές, και η παροχή απαντήσεων. Αυτή η δυνατότητα είναι ένα από τα βασικά χαρακτηριστικά του Llama 3.2. Άλλα χαρακτηριστικά περιλαμβάνουν:

- Πολυμορφικότητα - έχει τη δυνατότητα να αξιολογεί τόσο κείμενο όσο και εικόνες ως εντολές  
- Παραλλαγές μικρού έως μεσαίου μεγέθους (11B και 90B) - προσφέρουν ευέλικτες επιλογές ανάπτυξης  
- Παραλλαγές μόνο κειμένου (1B και 3B) - επιτρέπουν την ανάπτυξη σε edge / κινητές συσκευές με χαμηλή καθυστέρηση  

Η υποστήριξη πολυμορφικότητας αποτελεί μεγάλο βήμα στον κόσμο των μοντέλων ανοιχτού κώδικα. Το παράδειγμα κώδικα παρακάτω δέχεται τόσο εικόνα όσο και κείμενο ως εντολή για να λάβει ανάλυση της εικόνας από το Llama 3.2 90B.

### Υποστήριξη Πολυμορφικότητας με το Llama 3.2

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

Μετά την ολοκλήρωση αυτού του μαθήματος, ρίξτε μια ματιά στη [Συλλογή Μάθησης για Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) για να συνεχίσετε να αναβαθμίζετε τις γνώσεις σας στο Generative AI!

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.