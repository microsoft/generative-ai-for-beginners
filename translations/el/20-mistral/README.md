<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-06-26T03:17:14+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "el"
}
-->
# Κατασκευή με Μοντέλα Mistral

## Εισαγωγή

Αυτό το μάθημα θα καλύψει:
- Εξερεύνηση των διαφορετικών Μοντέλων Mistral
- Κατανόηση των περιπτώσεων χρήσης και σεναρίων για κάθε μοντέλο
- Παραδείγματα κώδικα που δείχνουν τα μοναδικά χαρακτηριστικά κάθε μοντέλου.

## Τα Μοντέλα Mistral

Σε αυτό το μάθημα, θα εξερευνήσουμε 3 διαφορετικά μοντέλα Mistral: **Mistral Large**, **Mistral Small** και **Mistral Nemo**.

Κάθε ένα από αυτά τα μοντέλα είναι διαθέσιμο δωρεάν στην αγορά μοντέλων του Github. Ο κώδικας σε αυτό το σημειωματάριο θα χρησιμοποιεί αυτά τα μοντέλα για να εκτελέσει τον κώδικα. Εδώ υπάρχουν περισσότερες λεπτομέρειες για τη χρήση των Μοντέλων Github για [πρωτοτυποποίηση με μοντέλα AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
Το Mistral Large 2 είναι επί του παρόντος το κύριο μοντέλο από την Mistral και έχει σχεδιαστεί για χρήση από επιχειρήσεις.

Το μοντέλο είναι μια αναβάθμιση του αρχικού Mistral Large προσφέροντας
- Μεγαλύτερο Παράθυρο Συμφραζομένων - 128k έναντι 32k
- Καλύτερη απόδοση σε εργασίες Μαθηματικών και Κωδικοποίησης - 76,9% μέση ακρίβεια έναντι 60,4%
- Αυξημένη πολυγλωσσική απόδοση - οι γλώσσες περιλαμβάνουν: Αγγλικά, Γαλλικά, Γερμανικά, Ισπανικά, Ιταλικά, Πορτογαλικά, Ολλανδικά, Ρωσικά, Κινέζικα, Ιαπωνικά, Κορεάτικα, Αραβικά και Χίντι.

Με αυτά τα χαρακτηριστικά, το Mistral Large διαπρέπει σε
- *Ανάκτηση Εμπλουτισμένης Γεννήτριας (RAG)* - λόγω του μεγαλύτερου παραθύρου συμφραζομένων
- *Κλήση Λειτουργιών* - αυτό το μοντέλο έχει εγγενή κλήση λειτουργιών που επιτρέπει την ενσωμάτωση με εξωτερικά εργαλεία και APIs. Αυτές οι κλήσεις μπορούν να γίνουν είτε παράλληλα είτε διαδοχικά.
- *Γεννήτρια Κώδικα* - αυτό το μοντέλο διαπρέπει στη δημιουργία κώδικα σε Python, Java, TypeScript και C++.

### Παράδειγμα RAG με το Mistral Large 2

Σε αυτό το παράδειγμα, χρησιμοποιούμε το Mistral Large 2 για να εκτελέσουμε ένα μοτίβο RAG σε ένα κείμενο εγγράφου. Η ερώτηση είναι γραμμένη στα Κορεάτικα και ρωτά για τις δραστηριότητες του συγγραφέα πριν το κολέγιο.

Χρησιμοποιεί το Cohere Embeddings Model για να δημιουργήσει ενσωματώσεις του κειμένου του εγγράφου καθώς και της ερώτησης. Για αυτό το δείγμα, χρησιμοποιεί το πακέτο faiss της Python ως κατάστημα διανυσμάτων.

Η προτροπή που στέλνεται στο μοντέλο Mistral περιλαμβάνει τόσο τις ερωτήσεις όσο και τα ανακτημένα τμήματα που είναι παρόμοια με την ερώτηση. Το μοντέλο παρέχει στη συνέχεια μια απάντηση σε φυσική γλώσσα.

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

question = "저자가 대학에 오기 전에 주로 했던 두 가지 일은 무엇이었나요?？"

question_embedding = embed_client.embed(
    input=[question],
    model=embed_model_name
)

question_embeddings = np.array(question_embedding.data[0].embedding)


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # distance, index
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
Το Mistral Small είναι ένα άλλο μοντέλο στην οικογένεια μοντέλων Mistral στην κατηγορία premier/enterprise. Όπως υποδηλώνει το όνομα, αυτό το μοντέλο είναι ένα Μικρό Μοντέλο Γλώσσας (SLM). Τα πλεονεκτήματα της χρήσης του Mistral Small είναι ότι είναι:
- Οικονομικό σε σχέση με τα Mistral LLMs όπως το Mistral Large και το NeMo - 80% μείωση κόστους
- Χαμηλή καθυστέρηση - ταχύτερη απόκριση σε σχέση με τα LLMs της Mistral
- Ευέλικτο - μπορεί να αναπτυχθεί σε διαφορετικά περιβάλλοντα με λιγότερους περιορισμούς στους απαιτούμενους πόρους.

Το Mistral Small είναι ιδανικό για:
- Εργασίες βασισμένες σε κείμενο όπως περίληψη, ανάλυση συναισθήματος και μετάφραση.
- Εφαρμογές όπου γίνονται συχνά αιτήματα λόγω της οικονομικής του αποδοτικότητας
- Εργασίες κώδικα με χαμηλή καθυστέρηση όπως αναθεώρηση και προτάσεις κώδικα

## Σύγκριση Mistral Small και Mistral Large

Για να δείξουμε τις διαφορές στην καθυστέρηση μεταξύ Mistral Small και Large, εκτελέστε τα παρακάτω κελιά.

Θα πρέπει να δείτε μια διαφορά στους χρόνους απόκρισης μεταξύ 3-5 δευτερολέπτων. Επίσης, σημειώστε τα μήκη και το στυλ των απαντήσεων στην ίδια προτροπή.

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

Σε σύγκριση με τα άλλα δύο μοντέλα που συζητήθηκαν σε αυτό το μάθημα, το Mistral NeMo είναι το μόνο δωρεάν μοντέλο με Άδεια Apache2.

Θεωρείται ως αναβάθμιση του προηγούμενου ανοιχτού κώδικα LLM από την Mistral, Mistral 7B.

Ορισμένα άλλα χαρακτηριστικά του μοντέλου NeMo είναι:

- *Πιο αποδοτική τοκενιζάτωση:* Αυτό το μοντέλο χρησιμοποιεί το tokenizer Tekken αντί για το πιο κοινά χρησιμοποιούμενο tiktoken. Αυτό επιτρέπει καλύτερη απόδοση σε περισσότερες γλώσσες και κώδικα.

- *Προσαρμογή:* Το βασικό μοντέλο είναι διαθέσιμο για προσαρμογή. Αυτό επιτρέπει μεγαλύτερη ευελιξία για περιπτώσεις χρήσης όπου μπορεί να χρειαστεί προσαρμογή.

- *Εγγενής Κλήση Λειτουργιών* - Όπως το Mistral Large, αυτό το μοντέλο έχει εκπαιδευτεί στην κλήση λειτουργιών. Αυτό το καθιστά μοναδικό καθώς είναι ένα από τα πρώτα μοντέλα ανοιχτού κώδικα που το κάνει.

### Σύγκριση Tokenizers

Σε αυτό το δείγμα, θα δούμε πώς το Mistral NeMo διαχειρίζεται την τοκενιζάτωση σε σύγκριση με το Mistral Large.

Και τα δύο δείγματα λαμβάνουν την ίδια προτροπή, αλλά θα πρέπει να δείτε ότι το NeMo επιστρέφει λιγότερα tokens σε σχέση με το Mistral Large.

```bash
pip install mistral-common
```

```python 
# Import needed packages:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Load Mistral tokenizer

model_name = "open-mistral-nemo	"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenize a list of messages
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
                                "description": "The temperature unit to use. Infer this from the users location.",
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

# Count the number of tokens
print(len(tokens))
```

```python
# Import needed packages:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Load Mistral tokenizer

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenize a list of messages
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
                                "description": "The temperature unit to use. Infer this from the users location.",
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

# Count the number of tokens
print(len(tokens))
```

## Η Μάθηση δεν σταματά εδώ, συνεχίστε το Ταξίδι

Αφού ολοκληρώσετε αυτό το μάθημα, ρίξτε μια ματιά στη συλλογή μας [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) για να συνεχίσετε να βελτιώνετε τις γνώσεις σας για το Generative AI!

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που προσπαθούμε για ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή παρερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.