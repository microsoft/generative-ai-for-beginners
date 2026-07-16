# ការសាងសង់ជាមួយម៉ូដែល Mistral 

## សេចក្ដីណែនាំ 

មេរៀននេះនឹងគ្របដណ្តប់៖ 
- ការស្វែងយល់អំពីម៉ូដែល Mistral ដំណាក់កាលផ្សេងៗ 
- ការយល់ដឹងពីករណីប្រើ និងស្ថានភាពសម្រាប់ម៉ូដែលនិមួយៗ 
- ការស្វែងយល់ពីឧទាហរណ៍កូដដែលបង្ហាញលក្ខណៈពិសេសនៃម៉ូដែលនិមួយៗ។ 

## ម៉ូដែល Mistral 

នៅក្នុងមេរៀននេះ យើងនឹងស្វែងយល់អំពីម៉ូដែលMistral 3 ប្រភេទផ្សេងៗគ្នា៖ 
**Mistral Large**, **Mistral Small** និង **Mistral Nemo**។ 

ម៉ូដែលទាំងនេះរាប់បញ្ចូលជាភាគហ៊ុនដោយឥតគិតថ្លៃនៅលើ [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)។ កូដនៅក្នុងសៀវភៅកំណត់ត្រានេះនឹងប្រើម៉ូដែលទាំងនេះដើម្បីរត់កូដ។

> **កំណត់ចិត្ត៖** GitHub Models នឹងបញ្ចប់នៅចុងខែកក្កដា ២០២៦។ យើងមានព័ត៌មានលម្អិតបន្ថែមអំពីការប្រើប្រាស់ [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) សម្រាប់ការបង្កើតគំរូជាមួយម៉ូដែល AI។ 


## Mistral Large 2 (2407)
Mistral Large 2 គឺជាម៉ូដែលឈានមុខគេរបស់ Mistral នៅពេលនេះ ហើយត្រូវបានបង្កើតសម្រាប់ការប្រើប្រាស់សហគ្រាស។ 

ម៉ូដែលនេះគឺជាការអាប់បេតទៅលើ Mistral Large ដើមដោយផ្តល់ជូន 
- បង្អួចបរិបទធំជាង - 128k ប្រៀបធៀបនឹង 32k 
- សមត្ថភាពល្អប្រសើរជាងលើកិច្ចការគណិតវិទ្យា និងកូដ - ភាគរយភាពត្រឹមត្រូវមធ្យម 76.9% ប្រៀបធៀបនឹង 60.4% 
- ការសមត្ថភាពអភិវឌ្ឍភាសាច្រើនជាង - ភាសារដូចជា: អង់គ្លេស បារាំង អាល្លឺម៉ង់ ប្រទេសអេស្ប៉ាញ អ៊ីតាលី ប៉ូរទុយហ្កាល់ ដើម ដូច ខ្មែរ រុស្ស៊ី ចិន ជប៉ុន កូរ៉េ អារ៉ាប់ និងឥណ្ឌា។

ជាមួយលក្ខណៈពិសេសទាំងនេះ Mistral Large មានលក្ខណៈល្អក្នុង 
- *បង្កើតបន្ថែមដោយការទាញយក (RAG)* - ដោយសារបង្អួចបរិបទធំជាង
- *ការហៅមុខងារ* - ម៉ូដែលនេះមានការហៅមុខងារដើមដែលអនុញ្ញាតឱ្យចូលរួមជាប់ជាមួយឧបករណ៍ និង API ខាងក្រៅ។ ការហៅទាំងនេះអាចធ្វើបានទាំងទម្រង់ស្របពេល ឬម្នាក់ទាំងក្រោយម្នាក់តាមលំដាប់ជាប់គ្នា។ 
- *ការបង្កើតកូដ* - ម៉ូដែលនេះមានសមត្ថភាពល្អលើការបង្កើត Python, Java, TypeScript និង C++។ 

### ឧទាហរណ៍ RAG ដោយប្រើ Mistral Large 2 

ក្នុងឧទាហរណ៍នេះ យើងកំពុងប្រើ Mistral Large 2 ដើម្បីរត់គំរោង RAG លើឯកសារអត្ថបទមួយ។ សំណួរត្រូវបានសរសេរជាភាសាកូរ៉េ ហើយសួរអំពីសកម្មភាពរបស់អ្នកនិពន្ធមុនពេលចូលសាកលវិទ្យាល័យ។ 

វាប្រើម៉ូដែល Cohere Embeddings ដូចគ្នា ដើម្បីបង្កើត embeddings នៃឯកសារអត្ថបទ និងសំណួរផងដែរ។ សំរាប់ឧទាហរណ៍នេះ វាប្រើកញ្ចប់ Python faiss ជារទេះវ៉ិចទ័រ។ 

ពីការបញ្ចូលទៅម៉ូដែល Mistral រួមមានសំណួរនិងផ្នែកដែលបានយកភ្ជាប់ដែលមានភាពស្រដៀងនឹងសំណួរ។ ម៉ូដែលនោះផ្តល់ចម្លើយភាសាធម្មជាតិមួយ។ 

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

# ទទួលយកទាំងនេះពីទំព័រ "ទិដ្ឋភាពទូទៅ" នៃគម្រោង Microsoft Foundry របស់អ្នក
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # ចម្ងាយ, សន្ទស្សន៍
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
Mistral Small គឺជាម៉ូដែលមួយទៀតក្នុងគ្រួសារម៉ូដែល Mistral ក្រោមប្រភេទ premier/enterprise។ ដូចដែលឈ្មោះគ្រាន់បញ្ជាក់ ម៉ូដែលនេះគឺជា ម៉ូដែលភាសាតិចតូច (SLM)។ អត្ថប្រយោជន៌នៃការប្រើ Mistral Small គឺ៖ 
- ការសន្សំថ្លៃប្រកួតប្រជែងជាមួយ Mistral LLMs ដូចជា Mistral Large និង NeMo - បញ្ចុះតម្លៃចំនួន 80%
- កំណត់ពេលវេលាតិច - ចម្លើយរហ័សជាង Mistral LLMs
- មានភាពបត់បែន - អាចដំណើរការបាននៅបរិយាកាសផ្សេងៗដោយមានកំណត់តិចជាងលើធនធានដែលត្រូវការ។ 


Mistral Small សមស្របសម្រាប់៖ 
- កិច្ចការដូចជាការសង្ខេបអត្ថបទ ការវិភាគអារម្មណ៍ និងការបកប្រែភាសា។ 
- កម្មវិធីដែលមានការស្នើសុំជាញឹកញាប់ដោយសារតម្លៃទាប
- កិច្ចការកូដដែលមានកំណត់ពេលវេលាទាបដូចជាការពិនិត្យ និងការផ្តល់យោបល់កូដ 

## ការប្រៀបធៀបរវាង Mistral Small និង Mistral Large 

ដើម្បីបង្ហាញភាពខុសគ្នារវាងពេលឆ្លើយតបរបស់ Mistral Small និង Large សូមរត់កោសិកាខាងក្រោម។ 

អ្នកគួរមើលឃើញភាពខុសគ្នារវាងពេលឆ្លើយតបប្រហែល ៣-៥ វិនាទី។ ក៏ចំណាំផងដែរពីប្រវែងនិងរចនាបថនៃចម្លើយក្នុងការចេញផ្សាយដដែល។  

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

ប្រៀបធៀបទៅនឹងម៉ូដែលទាំងពីរពិភាក្សាក្នុងមេរៀននេះ Mistral NeMo គឺជាម៉ូដែលឥតគិតថ្លៃតែមួយមានអាជ្ញាបណ្ណ Apache2 License។ 

វាត្រូវបានយល់ថាជាការអាប់ដេតទៅលើ LLM សូម្បីការបើកប្រភពមួយរបស់ Mistral 7B។ 

លក្ខណៈពិសេសផ្សេងទៀតនៃម៉ូដែល NeMo មានដូចជា៖ 

- *ការ tokenize ប្រសើរជាងមុន:* ម៉ូដែលនេះប្រើ Tekken tokenizer ជំនួស tiktoken ដែលគេប្រើប្រាស់ជាទូទៅ។ វាអនុញ្ញាតឱ្យមានសមត្ថភាពល្អលើភាសា និងកូដច្រើនជាង។ 

- *ការបណ្តុះបណ្តាលបន្ថែម:* ម៉ូដែលមូលដ្ឋានអាចប្រើសម្រាប់ការបណ្តុះបណ្តាលបន្ថែម។ វាអនុញ្ញាតឱ្យមានភាពបត់បែនបន្ថែមសម្រាប់ករណីប្រើដែលត្រូវការបណ្តុះបណ្តាលបន្ថែម។ 

- *ការហៅមុខងារដើម* - ដូចជា Mistral Large ម៉ូដែលនេះត្រូវបានបណ្តុះបណ្តាលលើការហៅមុខងារ។ នេះធ្វើឱ្យវាផ្សេងពីម៉ូដែលបើកប្រភពដំបូងមួយចំនួនក្នុងការធ្វើបែបនេះ។ 


### ការប្រៀបធៀបទៅនឹង tokenizers 

ក្នុងឧទាហរណ៍នេះ យើងនឹងមើលថាតើ Mistral NeMo ដោះស្រាយការចែក tokenization ដូចម្តេចប្រៀបធៀបនឹង Mistral Large។ 

គំរូទាំងពីរប្រើ prompt ដូចគ្នា ប៉ុន្តែអ្នកគួរមើលឃើញថា NeMo បញ្ជូន token ខ្សែលេខតិចជាង Mistral Large។ 

```bash
pip install mistral-common
```

```python 
# នាំចូលកញ្ចប់ដែលត្រូវការ:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# បញ្ចូលម៉ាស៊ីនបំបែកពាក្យ Mistral

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# បំបែកបញ្ជីសារទៅជាពាក្យ
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

# រាប់ចំនួនពាក្យ
print(len(tokens))
```

```python
# នាំចូលកញ្ចប់ដែលត្រូវការ៖
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# ផ្ទុកកម្មវិធីបំបែកពាក្យ Mistral

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# បំបែកពាក្យបញ្ជីសារមួយ
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

# រាប់ចំនួនពាក្យនៅក្នុងtokens
print(len(tokens))
```

## ការសិក្សាមិនបានផ្អាកនៅទីនេះ បន្តដំណើររបស់អ្នក

បន្ទាប់ពីបញ្ចប់មេរៀននេះ សូមពិនិត្យមើល [ការប្រមូលផ្តុំការសិក្សា Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) របស់យើងដើម្បីបន្តបង្កើនជំនាញ Generative AI របស់អ្នក!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->