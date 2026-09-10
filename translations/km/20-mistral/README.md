# ការសង់ជាមួយម៉ូដែល Mistral 

## ការណែនាំ 

មេរៀននេះនឹងគ្របដណ្តប់: 
- ការស្វែងយល់អំពីម៉ូដែល Mistral ផ្សេងៗ 
- ការយល់ដឹងពីករណីប្រើប្រាស់ និងសេណារីយ៉ូនសម្រាប់ម៉ូដែលនីមួយៗ 
- ការស្វែងយល់អំពីឧទាហរណ៍កូដដែលបង្ហាញលក្ខណៈពិសេសខ្លាំងរបស់ម៉ូដែលនីមួយៗ។ 

## ម៉ូដែល Mistral 

ក្នុងមេរៀននេះ យើងនឹងស្វែងយល់ពីម៉ូដែល Mistral 3 តែប៉ុណ្ណោះ៖ 
**Mistral Large**, **Mistral Small** និង **Mistral Nemo**។ 

ម៉ូដែលទាំងនេះសុខប្រើប្រាស់ដោយសេរីនៅលើ [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)។ កូដនៅក្នុងកំណត់ហេតុនេះនឹងប្រើម៉ូដែលទាំងនេះដើម្បីដំណើរការកូដ។

> **កំណត់ចំណាំ:** GitHub Models នឹងផ្អាកប្រើនៅចុងខែកក្កដា ឆ្នាំ 2026។ ទីនេះមានព័ត៌មានលម្អិតបន្ថែមអំពីការប្រើ [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ដើម្បីបង្កើតគំរូជាមួយម៉ូដែល AI។ 


## Mistral Large 2 (2407)
Mistral Large 2 គឺជាម៉ូដែលដឹកនាំបច្ចុប្បន្នពី Mistral ហើយត្រូវបានរចនាឡើងសម្រាប់ការប្រើប្រាស់អាជីវកម្ម។ 

ម៉ូដែលនេះគឺជាការអាប់ដេតទៅម៉ូដែល Mistral Large ដើម ដោយផ្តល់ជូន 
- ​បង្អួតវីនដូបរិបទធំជាង - 128k ជំនួស 32k 
- ​មុខងារល្អប្រសើរឡើងលើការងារគណិតវិទ្យា និងកម្មវិធីកូដ - ភាគរយត្រឹមត្រូវមធ្យម 76.9% ជំនួស 60.4% 
- ​ការសម្តែងភាសាប្រែប្រួលល្អប្រសើរជាងមុន - ភាសារួមមាន៖ អង់គ្លេស បារាំង អាឡឺម៉ង់ ស្ប៉ាញ អ៊ីតាលី ប៉័រទុយហ្គាល់ ហូឡង់ រុស្ស៊ី ចិន ជប៉ុន កូរ៉េ អារ៉ាប់ និងហិណ្ឌី។ 

ជាមួយនឹងលក្ខណៈទាំងនេះ Mistral Large លេចធ្លោក្នុង 
- *ការ​បង្កើតឯកសារដោយប្រើការ​ស្វែងរកបន្ថែម (RAG)* - ដោយសារវីនដូបរិបទធំជាង 
- *ការហៅម៉ូឌុល* - ម៉ូដែលនេះមានការហៅមុខងារដែលមានជំនាញធម្មជាតិដែលអាចប្តូរជាមួយឧបករណ៍ក្រៅ និង API។ ការហៅទាំងនេះអាចធ្វើបាននៅក្នុងលំដាប់ស្របពេល ឬតាមរយៈលំដាប់ជាលំដាប់។ 
- *ការបង្កើតកូដ* - ម៉ូដែលនេះលេចធ្លោលើការបង្កើត Python, Java, TypeScript និង C++។ 

### ឧទាហរណ៍ RAG ប្រើ Mistral Large 2 

ក្នុងឧទាហរណ៍នេះ យើងប្រើ Mistral Large 2 ដើម្បីបញ្ជាលក្ខណៈ RAG លើឯកសារសរសេរ។ សំណួរត្រូវបានសរសេរជាភាសាកូរ៉េ ហើយសួរអំពីសកម្មភាពរបស់អ្នកនិពន្ធមុនពេលចូលបណ្ឌិត្យភាព។ 

វាប្រើម៉ូដែល Cohere Embeddings ដើម្បីបង្កើត embeddings សម្រាប់ឯកសារសរសេរនិងសំណួរផងដែរ។ សម្រាប់ឧទាហរណ៍នេះ វាប្រើកញ្ចប់ Python faiss ជារទេះសម្រាប់វ៉ិចទ័រ។ 

Prompt ដែលបានផ្ញើទៅម៉ូដែល Mistral រួមមានសំណួរនិងអត្ថបទដែលទាញយកដែលស្រដៀងនឹងសំណួរ។ ម៉ូដែលនោះបញ្ជូនចម្លើយជាភាសាធម្មជាតិ។ 

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

# ទទួលបានទាំងនេះពីទំព័រ "ព័ត៌មានជាអ៊ិនធឺហ្វេស" របស់គម្រោង Microsoft Foundry របស់អ្នក
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # ចម្ងាយ, លេខសំគាល់
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
Mistral Small គឺជាម៉ូដែលមួយផ្សេងទៀតនៅក្នុងគ្រួសារម៉ូដែល Mistral ដែលស្ថិតនៅក្រោមប្រភេទ premye/enterprise។ ដូចឈ្មោះ វាជាម៉ូដែលភាសាធំតូច (SLM)។ គុណសម្បត្តិដែលប្រើប្រាស់ Mistral Small គឺ: 
- ការសន្សំថ្លៃប្រាក់ ប្រៀបធៀបនឹង Mistral LLMs ដូចជា Mistral Large និង NeMo - ថ្លៃធ្លាក់ចុះ 80%
- ល្បឿនទទួលប្រតិកម្មទាប - មានចម្លើយលឿនជាង Mistral's LLMs
- មានភាពបត់បែន - អាចដំណើរការបាននៅក្នុងបរិយាកាសផ្សេងៗដោយមានការចង្អុលតិចក្នុងធនធានដែលត្រូវការជាចាំបាច់។ 


Mistral Small ល្អសម្រាប់: 
- ការងារក្នុងលក្ខណៈអត្ថបទ ដូចជាការសង្ខេប វិភាគអារម្មណ៍ និងការបកប្រែ។ 
- កម្មវិធីដែលមានការស្នើសុំជាប្រចាំដោយសារតម្លៃមានប្រសិទ្ធភាព 
- ការងារកូដល្បឿនទាបដូចជា ការពិនិត្យ និងអនុសាសន៍កូដ 

## ធៀបបញ្ចូល Mistral Small និង Mistral Large 

ដើម្បីបង្ហាញភាពខុសគ្នានៃល្បឿនរវាង Mistral Small និង Large សូមដំណើរការជួរឈរ​កូដខាងក្រោម។ 

យើងគួរតែឃើញភាពខុសគ្នានៃពេលវេលាឆ្លើយតបក្នុងរយៈពេល 3-5 វិនាទី។ ក៏ដូចជាគួរប្រុងប្រយ័ត្នពីប្រវែងនិងបែបផែនចម្លើយលើ prompt ដូចគ្នា។  

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

ប្រៀបធៀបនឹងម៉ូដែលពីរក្នុងមេរៀននេះ Mistral NeMo គឺជាម៉ូដែលមួយតែប៉ុណ្ណោះដែលមានលក្ខខណ្ឌ Apache2 License ដោយឥតគិតថ្លៃ។ 

វាត្រូវបានឃើញថាជាការអាប់ដេតទៅម៉ូដែល LLM ប្រភពបើកដែល Mistral បញ្ចេញមុនគេ Mistral 7B។ 

មុខងារផ្សេងទៀតរបស់ម៉ូដែល NeMo មានដូចជា: 

- *ការតភ្ជាប់សញ្ញាអត្ថបទបានប្រសើរ:* ម៉ូដែលនេះប្រើ tokenizer Tekken ជំនួស tiktoken ដែលត្រូវបានប្រើប្រាស់ជាញឹកញាប់។ វាអនុញ្ញាតឱ្យមានមុខងារល្អប្រសើរលើភាសា និងកូដច្រើនជាង។ 

- *ការតំរូវផ្តល់ទិន្នន័យបន្ថែម:* ម៉ូដែលមូលដ្ឋានអាចប្រើសម្រាប់បន្ថែមការបង្ហាត់ឡើងវិញ។ វាអនុញ្ញាតឱ្យមានភាពបត់បែនបន្ថែមសម្រាប់ករណីប្រើប្រាស់ដែលតម្រូវការការបង្ហាត់ឡើងវិញ។ 

- *ការហៅមុខងារផ្ទាល់ខ្លួន* - ដូចជាគំរូ Mistral Large ម៉ូដែលនេះត្រូវបានបង្ហាត់លើការហៅមុខងារ។ វាធ្វើឱ្យវាមានលក្ខណៈពិសេសក្នុងនាមជាម៉ូដែលដែលប្រភពបើកដំបូងៗដែលមានមុខងារនេះ។ 


### ធៀបទៅនឹង Tokenizers 

ក្នុងឧទាហរណ៍នេះ យើងនឹងមើលថា Mistral NeMo រៀបចំ tokenization យ៉ាងដូចម្តេច ប្រៀបធៀបនឹង Mistral Large។ 

លំនាំទាំងពីរទទួលយក prompt ដូចគ្នា ប៉ុន្តែអ្នកគួរតែនៅឃើញថា NeMo ត្រឡប់ token គ្រាន់តែទាបជាង Mistral Large។ 

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

# ផ្ទុកជំពូកលេខ Mistral

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# បំបែកបញ្ជីសារទ្រង់ទ្រាយជាជំពូកលេខ
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

# រាប់ចំនួនជំពូកលេខ
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

# ផ្ទុកម៉ាស៊ីនបំបែកពាក្យ Mistral

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# បំបែកបញ្ជីសារ
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

# រាប់ចំនួនតូកិន
print(len(tokens))
```

## ការសិក្សាមិនបានបញ្ចប់នៅទីនេះ បន្តផ្លូវកំណត់

បន្ទាប់ពីបញ្ចប់មេរៀននេះ សូមពិនិត្យមើល [កម្រងការសិក្សា Generative AI របស់យើង](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ដើម្បីបន្តបណ្តុះបណ្តាលជំនាញ Generative AI របស់អ្នក! 

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->