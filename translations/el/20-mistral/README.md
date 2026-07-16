# Κατασκευή με Μοντέλα Mistral 

## Εισαγωγή 

Το μάθημα αυτό θα καλύψει: 
- Εξερεύνηση των διαφορετικών Μοντέλων Mistral 
- Κατανόηση των περιπτώσεων χρήσης και σεναρίων για κάθε μοντέλο 
- Εξερεύνηση δειγμάτων κώδικα που δείχνουν τα μοναδικά χαρακτηριστικά κάθε μοντέλου. 

## Τα Μοντέλα Mistral 

Σε αυτό το μάθημα, θα εξερευνήσουμε 3 διαφορετικά μοντέλα Mistral: 
**Mistral Large**, **Mistral Small** και **Mistral Nemo**. 

Κάθε ένα από αυτά τα μοντέλα είναι διαθέσιμο δωρεάν στο [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Ο κώδικας σε αυτό το σημειωματάριο θα χρησιμοποιεί αυτά τα μοντέλα για την εκτέλεση του κώδικα.

> **Σημείωση:** Τα GitHub Models θα αποσυρθούν στο τέλος Ιουλίου 2026. Εδώ θα βρείτε περισσότερες λεπτομέρειες σχετικά με τη χρήση των [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) για πρωτοτυποποίηση με μοντέλα AI. 


## Mistral Large 2 (2407)
Το Mistral Large 2 είναι αυτή τη στιγμή το ναυαρχίδα μοντέλο της Mistral και έχει σχεδιαστεί για επιχειρησιακή χρήση. 

Το μοντέλο αποτελεί αναβάθμιση του αρχικού Mistral Large προσφέροντας 
-  Μεγαλύτερο Παράθυρο Συμφραζομένων - 128k έναντι 32k 
-  Καλύτερη απόδοση σε Μαθηματικά και Εργασίες Κώδικα - 76,9% μέση ακρίβεια έναντι 60,4% 
-  Αυξημένη πολυγλωσσική απόδοση - οι γλώσσες περιλαμβάνουν: Αγγλικά, Γαλλικά, Γερμανικά, Ισπανικά, Ιταλικά, Πορτογαλικά, Ολλανδικά, Ρωσικά, Κινέζικα, Ιαπωνικά, Κορεατικά, Αραβικά και Χίντι.

Με αυτά τα χαρακτηριστικά, το Mistral Large διαπρέπει σε 
- *Αναζήτηση με Επαυξημένη Παραγωγή (RAG)* - λόγω του μεγαλύτερου παραθύρου συμφραζομένων
- *Κλήση Συναρτήσεων* - αυτό το μοντέλο διαθέτει εγγενή κλήση συναρτήσεων που επιτρέπει ενσωμάτωση με εξωτερικά εργαλεία και APIs. Αυτές οι κλήσεις μπορούν να γίνουν είτε παράλληλα είτε μία μετά την άλλη σε διαδοχική σειρά. 
- *Παραγωγή Κώδικα* - αυτό το μοντέλο διαπρέπει στη δημιουργία κώδικα Python, Java, TypeScript και C++. 

### Παράδειγμα RAG με χρήση του Mistral Large 2 

Σε αυτό το παράδειγμα, χρησιμοποιούμε το Mistral Large 2 για να εκτελέσουμε ένα μοτίβο RAG πάνω σε ένα κείμενο. Η ερώτηση είναι γραμμένη στα Κορεατικά και ρωτά για τις δραστηριότητες του συγγραφέα πριν το πανεπιστήμιο. 

Χρησιμοποιείται το Μοντέλο Ενσωματώσεων Cohere για τη δημιουργία ενσωματώσεων του κειμένου καθώς και της ερώτησης. Για αυτό το δείγμα, χρησιμοποιεί το πακέτο faiss της Python ως αποθήκη διανυσμάτων. 

Η πρόταση που στέλνεται στο μοντέλο Mistral περιλαμβάνει τόσο τις ερωτήσεις όσο και τα ανακτηθέντα τμήματα που είναι παρόμοια με την ερώτηση. Το μοντέλο παρέχει στη συνέχεια μια απάντηση σε φυσική γλώσσα. 

```python 
pip install faiss-cpu
```

```python 
import requests
import numpy as np
import faiss
import os

from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference import EmbeddingsClient

# Λάβετε αυτά από τη σελίδα "Επισκόπηση" του έργου σας Microsoft Foundry
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Mistral-large"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = requests.get('https://raw.githubusercontent.com/run-llama/llama_index/main/docs/docs/examples/data/paul_graham/paul_graham_essay.txt')
text = response.text

chunk_size = 2048
chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
len(chunks)

embed_model_name = "cohere-embed-v3-multilingual" 

embed_client = EmbeddingsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(token)
)

embed_response = embed_client.embed(
    input=chunks,
    model=embed_model_name
)



text_embeddings = []
for item in embed_response.data:
    length = len(item.embedding)
    text_embeddings.append(item.embedding)
text_embeddings = np.array(text_embeddings)


d = text_embeddings.shape[1]
index = faiss.IndexFlatL2(d)
index.add(text_embeddings)

question = "저자가 대학에 오기 전에 주로 했던 두 가지 일은 무엇이었나요?"

question_embedding = embed_client.embed(
    input=[question],
    model=embed_model_name
)

question_embeddings = np.array(question_embedding.data[0].embedding)


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # απόσταση, δείκτης
retrieved_chunks = [chunks[i] for i in I.tolist()[0]]

prompt = f"""
Context information is below.
---------------------
{retrieved_chunks}
---------------------
Given the context information and not prior knowledge, answer the query.
Query: {question}
Answer:
"""


chat_response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content=prompt),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(chat_response.choices[0].message.content)
```

## Mistral Small 
Το Mistral Small είναι ένα άλλο μοντέλο στην οικογένεια Mistral στην κατηγορία premier/enterprise. Όπως υποδηλώνει το όνομα, αυτό το μοντέλο είναι ένα Μικρό Γλωσσικό Μοντέλο (SLM). Τα πλεονεκτήματα της χρήσης του Mistral Small είναι: 
- Οικονομία κόστους σε σύγκριση με τα LLMs της Mistral όπως το Mistral Large και NeMo - μείωση τιμής 80%
- Χαμηλή καθυστέρηση - ταχύτερη απόκριση σε σύγκριση με τα LLMs της Mistral
- Ευέλικτο - μπορεί να αναπτυχθεί σε διαφορετικά περιβάλλοντα με λιγότερους περιορισμούς στα απαιτούμενα μέσα. 


Το Mistral Small είναι ιδανικό για: 
- Εργασίες βασισμένες σε κείμενο όπως περίληψη, ανάλυση συναισθήματος και μετάφραση. 
- Εφαρμογές όπου γίνονται συχνά αιτήματα λόγω της οικονομικής αποδοτικότητας 
- Εργασίες κώδικα με χαμηλή καθυστέρηση όπως ανασκόπηση και προτάσεις κώδικα 

## Σύγκριση Mistral Small και Mistral Large 

Για να δείτε τις διαφορές στην καθυστέρηση μεταξύ Mistral Small και Large, τρέξτε τα παρακάτω κελιά. 

Θα δείτε διαφορά στους χρόνους απόκρισης μεταξύ 3-5 δευτερολέπτων. Σημειώστε επίσης τα μήκη και το στυλ απόκρισης πάνω στην ίδια πρόταση.  

```python 

import os 
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Mistral-small"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful coding assistant."),
        UserMessage(content="Can you write a Python function to the fizz buzz test?"),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(response.choices[0].message.content)

```

```python 

import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Mistral-large"
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful coding assistant."),
        UserMessage(content="Can you write a Python function to the fizz buzz test?"),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(response.choices[0].message.content)

```

## Mistral NeMo

Σε σύγκριση με τα άλλα δύο μοντέλα που συζητήθηκαν σε αυτό το μάθημα, το Mistral NeMo είναι το μόνο δωρεάν μοντέλο με άδεια Apache2. 

Θεωρείται ως αναβάθμιση του πρώιμου ανοιχτού LLM της Mistral, Mistral 7B. 

Μερικά άλλα χαρακτηριστικά του μοντέλου NeMo είναι: 

- *Πιο αποδοτική τοκενιοποίηση:* Αυτό το μοντέλο χρησιμοποιεί τον τοκενιζατέρ Tekken αντί του πιο διαδεδομένου tiktoken. Αυτό επιτρέπει καλύτερη απόδοση σε περισσότερες γλώσσες και κώδικα. 

- *Εκπαίδευση με προσαρμογή (finetuning):* Το βασικό μοντέλο είναι διαθέσιμο για προσαρμογή. Αυτό επιτρέπει μεγαλύτερη ευελιξία για περιπτώσεις χρήσης όπου μπορεί να χρειαστεί προσαρμογή. 

- *Εγγενής Κλήση Συναρτήσεων* - Όπως το Mistral Large, αυτό το μοντέλο έχει εκπαιδευτεί στην κλήση συναρτήσεων. Αυτό το καθιστά μοναδικό ως ένα από τα πρώτα ανοιχτά μοντέλα που το κάνουν. 


### Σύγκριση Τοκενιζατέρ 

Σε αυτό το παράδειγμα, θα δούμε πώς το Mistral NeMo χειρίζεται την τοκενιοποίηση σε σύγκριση με το Mistral Large. 

Και τα δύο δείγματα παίρνουν την ίδια πρόταση αλλά θα δείτε ότι το NeMo επιστρέφει λιγότερα tokens από το Mistral Large. 

```bash
pip install mistral-common
```

```python 
# Εισαγωγή των απαραίτητων πακέτων:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Φόρτωση του tokenizer Mistral

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# Κάντε token μια λίστα από μηνύματα
tokenized = tokenizer.encode_chat_completion(
    ChatCompletionRequest(
        tools=[
            Tool(
                function=Function(
                    name="get_current_weather",
                    description="Get the current weather",
                    parameters={
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA",
                            },
                            "format": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"],
                                "description": "The temperature unit to use. Infer this from the user's location.",
                            },
                        },
                        "required": ["location", "format"],
                    },
                )
            )
        ],
        messages=[
            UserMessage(content="What's the weather like today in Paris"),
        ],
        model=model_name,
    )
)
tokens, text = tokenized.tokens, tokenized.text

# Μετρήστε τον αριθμό των tokens
print(len(tokens))
```

```python
# Εισαγωγή των απαραίτητων πακέτων:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Φόρτωση του tokenizer Mistral

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Τοκενισμός μιας λίστας μηνυμάτων
tokenized = tokenizer.encode_chat_completion(
    ChatCompletionRequest(
        tools=[
            Tool(
                function=Function(
                    name="get_current_weather",
                    description="Get the current weather",
                    parameters={
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA",
                            },
                            "format": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"],
                                "description": "The temperature unit to use. Infer this from the user's location.",
                            },
                        },
                        "required": ["location", "format"],
                    },
                )
            )
        ],
        messages=[
            UserMessage(content="What's the weather like today in Paris"),
        ],
        model=model_name,
    )
)
tokens, text = tokenized.tokens, tokenized.text

# Μέτρηση του αριθμού των τοκενς
print(len(tokens))
```

## Η μάθηση δεν σταματά εδώ, συνεχίστε το ταξίδι

Αφού ολοκληρώσετε αυτό το μάθημα, ρίξτε μια ματιά στη [συλλογή Μαθαίνω Γεννητική AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) για να συνεχίσετε να βελτιώνετε τις γνώσεις σας στην Γεννητική AI!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->