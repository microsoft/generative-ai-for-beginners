# Δημιουργία με τα Μοντέλα Mistral 

## Εισαγωγή 

Αυτό το μάθημα θα καλύψει: 
- Εξερεύνηση των διαφορετικών Μοντέλων Mistral 
- Κατανόηση των περιπτώσεων χρήσης και των σεναρίων για κάθε μοντέλο 
- Εξερεύνηση παραδειγμάτων κώδικα που δείχνουν τα μοναδικά χαρακτηριστικά κάθε μοντέλου. 

## Τα Μοντέλα Mistral 

Σε αυτό το μάθημα, θα εξερευνήσουμε 3 διαφορετικά μοντέλα Mistral: 
**Mistral Large**, **Mistral Small** και **Mistral Nemo**. 

Κάθε ένα από αυτά τα μοντέλα είναι διαθέσιμο δωρεάν στο [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). Ο κώδικας σε αυτό το τετράδιο θα χρησιμοποιεί αυτά τα μοντέλα για την εκτέλεση του κώδικα.

> **Σημείωση:** Τα GitHub Models θα αποσυρθούν στο τέλος Ιουλίου 2026. Εδώ είναι περισσότερες λεπτομέρειες για τη χρήση των [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) για πρωτότυπα με μοντέλα τεχνητής νοημοσύνης. 


## Mistral Large 2 (2407)
Το Mistral Large 2 είναι επί του παρόντος το κύριο μοντέλο της Mistral και έχει σχεδιαστεί για χρήση σε επιχειρήσεις. 

Το μοντέλο αποτελεί αναβάθμιση του αρχικού Mistral Large προσφέροντας 
-  Μεγαλύτερο Παράθυρο Συμφραζομένων - 128k έναντι 32k 
-  Καλύτερη απόδοση σε Μαθηματικές και Κωδικοποιητικές Εργασίες - μέση ακρίβεια 76,9% έναντι 60,4% 
-  Αυξημένη πολυγλωσσική απόδοση - οι γλώσσες περιλαμβάνουν: Αγγλικά, Γαλλικά, Γερμανικά, Ισπανικά, Ιταλικά, Πορτογαλικά, Ολλανδικά, Ρωσικά, Κινέζικα, Ιαπωνικά, Κορεατικά, Αραβικά και Χίντι.

Με αυτά τα χαρακτηριστικά, το Mistral Large ξεχωρίζει σε 
- *Ανακτηση Βοηθημένη Δημιουργία (RAG)* - λόγω του μεγαλύτερου παραθύρου συμφραζομένων
- *Κλήση Λειτουργιών* - αυτό το μοντέλο διαθέτει εγγενή κλήση λειτουργιών που επιτρέπει την ενσωμάτωση με εξωτερικά εργαλεία και APIs. Αυτές οι κλήσεις μπορούν να γίνουν είτε παράλληλα είτε μία μετά την άλλη σε σειριακή σειρά. 
- *Δημιουργία Κώδικα* - το μοντέλο αυτό διαπρέπει στη δημιουργία Python, Java, TypeScript και C++. 

### Παράδειγμα RAG χρησιμοποιώντας το Mistral Large 2 

Σε αυτό το παράδειγμα, χρησιμοποιούμε το Mistral Large 2 για να εκτελέσουμε ένα πρότυπο RAG πάνω σε ένα κείμενο. Η ερώτηση είναι γραμμένη στα κορεατικά και ρωτά για τις δραστηριότητες του συγγραφέα πριν το πανεπιστήμιο. 

Χρησιμοποιεί το Cohere Embeddings Model για να δημιουργήσει τις ενσωματώσεις του κειμένου καθώς και της ερώτησης. Για αυτό το δείγμα, χρησιμοποιεί το πακέτο faiss Python ως αποθήκη διανυσμάτων. 

Το prompt που αποστέλλεται στο μοντέλο Mistral περιλαμβάνει και τις ερωτήσεις και τα ανακτηθέντα τμήματα που είναι παρόμοια με την ερώτηση. Το μοντέλο παρέχει στη συνέχεια μια απάντηση σε φυσική γλώσσα. 

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

# Πάρε αυτά από τη σελίδα "Επισκόπηση" του έργου σου Microsoft Foundry
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
Το Mistral Small είναι ένα ακόμη μοντέλο στην οικογένεια Mistral κάτω από την κατηγορία premier/enterprise. Όπως υποδηλώνει το όνομα, αυτό το μοντέλο είναι ένα Μικρό Μοντέλο Γλώσσας (SLM). Τα πλεονεκτήματα της χρήσης του Mistral Small είναι ότι είναι: 
- Εξοικονόμηση κόστους σε σύγκριση με τα Mistral LLMs όπως το Mistral Large και NeMo - μείωση τιμής κατά 80%
- Χαμηλή καθυστέρηση - ταχύτερη απόκριση σε σύγκριση με τα LLMs της Mistral
- Ευέλικτο - μπορεί να αναπτυχθεί σε διαφορετικά περιβάλλοντα με λιγότερους περιορισμούς στους απαιτούμενους πόρους. 


Το Mistral Small είναι ιδανικό για: 
- Εργασίες βασισμένες σε κείμενο όπως περίληψη, ανάλυση συναισθήματος και μετάφραση. 
- Εφαρμογές όπου γίνονται συχνά αιτήματα λόγω της οικονομικής αποδοτικότητας 
- Κωδικοποιητικές εργασίες με χαμηλή καθυστέρηση όπως αναθεώρηση και προτάσεις κώδικα 

## Σύγκριση Mistral Small και Mistral Large 

Για να δείτε τις διαφορές στην καθυστέρηση μεταξύ Mistral Small και Large, εκτελέστε τα παρακάτω κελιά. 

Θα πρέπει να δείτε μια διαφορά στους χρόνους απόκρισης μεταξύ 3-5 δευτερολέπτων. Επίσης προσέξτε τα μήκη και το στυλ των απαντήσεων στο ίδιο prompt.  

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

Θεωρείται αναβάθμιση του προηγούμενου ανοιχτού LLM της Mistral, Mistral 7B. 

Μερικά άλλα χαρακτηριστικά του μοντέλου NeMo είναι: 

- *Πιο αποδοτική τοκενποίηση:* Αυτό το μοντέλο χρησιμοποιεί τον tokenizer Tekken αντί του πιο κοινά χρησιμοποιούμενου tiktoken. Αυτό επιτρέπει καλύτερη απόδοση σε περισσότερες γλώσσες και κώδικα. 

- *Λεπτομερής εκπαίδευση:* Το βασικό μοντέλο είναι διαθέσιμο για λεπτομερή εκπαίδευση. Αυτό επιτρέπει μεγαλύτερη ευελιξία για περιπτώσεις χρήσης όπου απαιτείται λεπτομερής εκπαίδευση. 

- *Εγγενής Κλήση Λειτουργιών* - Όπως το Mistral Large, αυτό το μοντέλο έχει εκπαιδευτεί στην κλήση λειτουργιών. Αυτό το καθιστά μοναδικό καθώς είναι από τα πρώτα ανοιχτά μοντέλα που το κάνουν. 


### Σύγκριση Tokenizers 

Σε αυτό το δείγμα, θα δούμε πώς το Mistral NeMo διαχειρίζεται την τοκενποίηση σε σύγκριση με το Mistral Large. 

Και τα δύο δείγματα παίρνουν το ίδιο prompt αλλά θα δείτε ότι το NeMo επιστρέφει λιγότερα tokens από το Mistral Large. 

```bash
pip install mistral-common
```

```python 
# Εισαγωγή των απαιτούμενων πακέτων:
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

```python
# Εισαγωγή των απαιτούμενων πακέτων:
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

# Τοκενικοποίηση μιας λίστας μηνυμάτων
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

Αφού ολοκληρώσετε αυτό το μάθημα, δείτε τη [Συλλογή Μάθησης για Γενετική Τεχνητή Νοημοσύνη](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) για να συνεχίσετε να βελτιώνετε τις γνώσεις σας στην Γενετική Τεχνητή Νοημοσύνη!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->