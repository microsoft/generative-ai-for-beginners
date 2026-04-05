# Κατασκευή με Μοντέλα Mistral 

## Εισαγωγή 

Αυτό το μάθημα θα καλύψει: 
- Εξερεύνηση των διαφορετικών Μοντέλων Mistral 
- Κατανόηση των περιπτώσεων χρήσης και σεναρίων για κάθε μοντέλο 
- Εξερεύνηση παραδειγμάτων κώδικα που δείχνουν τα μοναδικά χαρακτηριστικά κάθε μοντέλου. 

## Τα Μοντέλα Mistral 

Σε αυτό το μάθημα, θα εξερευνήσουμε 3 διαφορετικά μοντέλα Mistral: 
**Mistral Large**, **Mistral Small** και **Mistral Nemo**. 

Κάθε ένα από αυτά τα μοντέλα είναι διαθέσιμο δωρεάν στο GitHub Marketplace για μοντέλα. Ο κώδικας σε αυτό το σημειωματάριο θα χρησιμοποιεί αυτά τα μοντέλα για την εκτέλεση του κώδικα. Εδώ είναι περισσότερες λεπτομέρειες για τη χρήση μοντέλων GitHub για [πρωτοτυποποίηση με μοντέλα AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst). 


## Mistral Large 2 (2407)
Το Mistral Large 2 είναι επί του παρόντος το κορυφαίο μοντέλο της Mistral και έχει σχεδιαστεί για επιχειρησιακή χρήση. 

Το μοντέλο είναι μια αναβάθμιση του αρχικού Mistral Large προσφέροντας 
-  Μεγαλύτερο Παράθυρο Πλαισίου - 128k έναντι 32k 
-  Καλύτερη απόδοση σε Μαθηματικές και Προγραμματιστικές εργασίες - 76,9% μέση ακρίβεια έναντι 60,4% 
-  Αυξημένη πολυγλωσσική απόδοση - οι γλώσσες περιλαμβάνουν: Αγγλικά, Γαλλικά, Γερμανικά, Ισπανικά, Ιταλικά, Πορτογαλικά, Ολλανδικά, Ρωσικά, Κινέζικα, Ιαπωνικά, Κορεάτικα, Αραβικά και Χίντι.

Με αυτά τα χαρακτηριστικά, το Mistral Large διαπρέπει σε 
- *Retrieval Augmented Generation (RAG)* - λόγω του μεγαλύτερου παραθύρου πλαισίου
- *Function Calling* - αυτό το μοντέλο έχει εγγενή κλήση λειτουργιών που επιτρέπει ενσωμάτωση με εξωτερικά εργαλεία και APIs. Αυτές οι κλήσεις μπορούν να γίνουν είτε παράλληλα είτε μία μετά την άλλη σε σειριακή σειρά. 
- *Code Generation* - αυτό το μοντέλο διαπρέπει στην παραγωγή Python, Java, TypeScript και C++. 

### Παράδειγμα RAG με χρήση του Mistral Large 2 

Σε αυτό το παράδειγμα, χρησιμοποιούμε το Mistral Large 2 για να εκτελέσουμε ένα μοτίβο RAG σε ένα έγγραφο κειμένου. Η ερώτηση είναι γραμμένη στα Κορεάτικα και ρωτά για τις δραστηριότητες του συγγραφέα πριν το πανεπιστήμιο. 

Χρησιμοποιεί το Cohere Embeddings Model για να δημιουργήσει embeddings του εγγράφου κειμένου καθώς και της ερώτησης. Για αυτό το δείγμα, χρησιμοποιεί το πακέτο faiss Python ως χώρο αποθήκευσης διανυσμάτων. 

Το prompt που στέλνεται στο μοντέλο Mistral περιλαμβάνει τόσο τις ερωτήσεις όσο και τα ανακτηθέντα κομμάτια που είναι παρόμοια με την ερώτηση. Το Μοντέλο στη συνέχεια παρέχει μια απάντηση σε φυσική γλώσσα. 

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

endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-large"
token = os.environ["GITHUB_TOKEN"]

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
Το Mistral Small είναι ένα άλλο μοντέλο στην οικογένεια μοντέλων Mistral υπό την κατηγορία premier/enterprise. Όπως λέει και το όνομα, αυτό το μοντέλο είναι ένα Μικρό Γλωσσικό Μοντέλο (SLM). Τα πλεονεκτήματα της χρήσης του Mistral Small είναι ότι είναι: 
- Οικονομικό σε σύγκριση με τα Mistral LLMs όπως το Mistral Large και το NeMo - μείωση τιμής 80%
- Χαμηλή καθυστέρηση - ταχύτερη απάντηση σε σύγκριση με τα LLMs της Mistral
- Ευέλικτο - μπορεί να αναπτυχθεί σε διάφορα περιβάλλοντα με λιγότερους περιορισμούς στους απαιτούμενους πόρους. 


Το Mistral Small είναι ιδανικό για: 
- Εργασίες βασισμένες σε κείμενο όπως περίληψη, ανάλυση συναισθήματος και μετάφραση. 
- Εφαρμογές όπου γίνονται συχνά αιτήματα λόγω της οικονομικής του αποδοτικότητας 
- Εργασίες κώδικα με χαμηλή καθυστέρηση όπως ανασκόπηση και προτάσεις κώδικα 

## Σύγκριση Mistral Small και Mistral Large 

Για να δείτε διαφορές στην καθυστέρηση μεταξύ Mistral Small και Large, εκτελέστε τα παρακάτω κελιά. 

Θα πρέπει να δείτε μια διαφορά στους χρόνους απόκρισης μεταξύ 3-5 δευτερολέπτων. Επίσης προσέξτε το μήκος και το στυλ των απαντήσεων πάνω στο ίδιο prompt.  

```python 

import os 
endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-small"
token = os.environ["GITHUB_TOKEN"]

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

endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-large"
token = os.environ["GITHUB_TOKEN"]

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

Εκλαμβάνεται ως αναβάθμιση του προηγούμενου ανοιχτού λογισμικού LLM της Mistral, του Mistral 7B. 

Μερικά άλλα χαρακτηριστικά του μοντέλου NeMo είναι: 

- *Αποδοτικότερη τοκενποίηση:* Αυτό το μοντέλο χρησιμοποιεί τον tokenizier Tekken αντί για τον πιο κοινά χρησιμοποιούμενο tiktoken. Αυτό επιτρέπει καλύτερη απόδοση σε περισσότερες γλώσσες και κώδικα. 

- *Finetuning:* Το βασικό μοντέλο είναι διαθέσιμο για finetuning. Αυτό επιτρέπει μεγαλύτερη ευελιξία για περιπτώσεις χρήσης όπου μπορεί να απαιτηθεί finetuning. 

- *Εγγενής Κλήση Λειτουργιών* - Όπως το Mistral Large, αυτό το μοντέλο έχει εκπαιδευτεί στην κλήση λειτουργιών. Αυτό το καθιστά μοναδικό ως ένα από τα πρώτα μοντέλα ανοιχτού κώδικα που το κάνει. 


### Σύγκριση Tokenizers 

Σε αυτό το δείγμα, θα δούμε πώς το Mistral NeMo χειρίζεται την τοκενποίηση σε σύγκριση με το Mistral Large. 

Και τα δύο δείγματα παίρνουν το ίδιο prompt αλλά θα πρέπει να δείτε το NeMo να επιστρέφει λιγότερους tokens από το Mistral Large. 

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

# Μετατροπή μιας λίστας μηνυμάτων σε tokens
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

# Μέτρηση του αριθμού των tokens
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

# Φορτώστε τον tokenizer Mistral

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Κωδικοποίηση μιας λίστας μηνυμάτων
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

# Μέτρηση του αριθμού των tokens
print(len(tokens))
```

## Η μάθηση δεν σταματά εδώ, συνεχίστε το ταξίδι

Μετά την ολοκλήρωση αυτού του μαθήματος, ρίξτε μια ματιά στη συλλογή μας [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) για να συνεχίσετε να αυξάνετε τις γνώσεις σας στην Γενετική Τεχνητή Νοημοσύνη!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθύνης**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ προσπαθούμε για ακρίβεια, παρακαλούμε να λάβετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική μετάφραση από άνθρωπο. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->