# ការសាងសង់ជាមួយម៉ូដែល Mistral

## ការណែនាំ

មេរៀននេះនឹងបូកបញ្ចូល៖
- ការស្រាវជ្រាវម៉ូដែល Mistral ផ្សេងៗ
- ការយល់ដឹងអំពីករណីប្រើប្រាស់ និងស្ថានភាពសម្រាប់ម៉ូដែលនីមួយៗ
- ការស្រាវជ្រាវគំរូកូដដែលបង្ហាញលក្ខណៈពិសេសរបស់ម៉ូដែលនីមួយៗ

## ម៉ូដែល Mistral

ក្នុងមេរៀននេះ យើងនឹងស្រាវជ្រាវម៉ូដែល Mistral ផីលិត 3 ប្រភេទ៖
**Mistral Large**, **Mistral Small** និង **Mistral Nemo**។

ម៉ូដែលទាំងនេះអាចរកបានជាឥតគិតថ្លៃលើទីផ្សារម៉ូដែល GitHub។ កូដក្នុងសៀវភៅសម្ងាត់នេះនឹងប្រើម៉ូដែលទាំងនេះដើម្បីរត់កូដ។ នេះជារបាយការណ៍បន្ថែមអំពីការប្រើម៉ូដែល GitHub ដើម្បី [សាកល្បងជាមួយម៉ូដែល AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)។

## Mistral Large 2 (2407)
Mistral Large 2 គឺជាម៉ូដែលឯកទេសចម្បងបច្ចុប្បន្នពី Mistral ហើយបានរចនាសម្រាប់ការប្រើប្រាស់សហគ្រាស។

ម៉ូដែលនេះជាការអាប់ដេតមកពី Mistral Large ដើមដោយផ្តល់ជូនៈ
- ការបើកបង្ហាញរឿងបរិបទធំជាង - 128k មុខ 32k
- ប្រសិទ្ធភាពល្អប្រសើរឡើងលើភារកិច្ចគណិតវិទ្យានិងកូដ - មធ្យមភាពត្រឹមត្រូវ 76.9% ទល់នឹង 60.4%
- ការពង្រឹងប្រសិទ្ធភាពភាសាច្រើន - ភាសាដូចជា៖ អង់គ្លេស, បារាំង, អាល្លឺម៉ង់, អេស្ប៉ាញ, អ៊ីតាលី, ព័រទុយហ្គាល់, ដាច់, រុស្ស៊ី, ចិន, ជប៉ុន, កូរ៉េ, អារ៉ាប់ និងឥណ្ឌា។

ជាមួយលក្ខណៈទាំងនេះ Mistral Large អាចយកឈ្នះបានលើ
- *ការបង្កើតបន្ថែមអំពីការទាញយកព័ត៌មាន (RAG)* - ដោយសារមានបរិបទធំជាង
- *ការហៅមុខងារ* - ម៉ូដែលនេះមានការហៅមុខងារដើមដែលអនុញ្ញាតឲ្យភ្ជាប់ជាមួយឧបករណ៍និង API ខាងក្រៅ។ ការហៅនេះអាចធ្វើបានទាំងវាយតម្លៃធ្វើដំណើរជាមួយគ្នា ឬបន្ទាប់បន្សំៗគ្នាតាមលំដាប់។
- *ការបង្កើតកូដ* - ម៉ូដែលនេះលេចធ្លោលើ Python, Java, TypeScript និង C++។

### ឧទាហរណ៍ RAG ប្រើ Mistral Large 2

នៅក្នុងឧទាហរណ៍នេះ យើងកំពុងប្រើ Mistral Large 2 ដើម្បីរៀបចំលំនាំ RAG លើឯកសារយោងមួយ។ សំណួរត្រូវបានសរសេរជាភាសាកូរ៉េ និងសួរពីសកម្មភាពរបស់អ្នកនិពន្ធមុនចូលមហាវិទ្យាល័យ។

វាប្រើម៉ូដែល Cohere Embeddings ដើម្បីបង្កើត embeddings នៃឯកសារយោង និងសំណួរ។ សម្រាប់គំរូនេះ វាប្រើកញ្ចប់ Python faiss ជាឃ្លាំងវ៉ិចទ័រ។

ការបញ្ចូនសារទៅម៉ូដែល Mistral រួមបញ្ចូលទាំងសំណួរ និងផ្នែកបានទាញយកដែលស្រដៀងទៅនឹងសំណួរ។ ម៉ូដែលនោះនាំឲ្យមានចម្លើយភាសាធម្មតា។

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
Mistral Small គឺជាម៉ូដែលមួយទៀតក្នុងគ្រួសារម៉ូដែល Mistral ដែលស្ថិតក្រោមប្រភេទ-premier/enterprise។ ដូចឈ្មោះវា ម៉ូដែលនេះគឺជាម៉ូដែលភាសាធំតូច (SLM)។ អត្ថប្រយោជន៍នៃការប្រើ Mistral Small គឺ៖
- ជាជម្រើសសន្សំថ្លៃប្រាក់បើប្រៀបធៀបទៅនឹងម៉ូដែល LLM របស់ Mistral ដូចជា Mistral Large និង NeMo - ការកាត់បន្ថយតម្លៃរហូតដល់ 80%
- latency ต่ำ - ឆ្លើយតបបានលឿនជាង LLM របស់ Mistral
- មានភាពបត់បែន - អាចដំណើរការបានក្នុងបរិយាកាសផ្សេងៗដោយមានការកំណត់ធនធានតិចជាងដែលទាមទារ។

Mistral Small ល្អសម្រាប់៖
- ភារកិច្ចផ្អែកលើអត្ថបទដូចជាការស្រង់សេចក្ដីសង្ខេប, វិភាគអារម្មណ៍ និងការប្រែសម្រួល។
- កម្មវិធីដែលមានការស្នើរសុំជាញឹកញាប់ដោយសារតម្លៃប្រសិទ្ធភាព
- ភារកិច្ចកូដ latency ទាបដូចជាការត្រួតពិនិត្យ និងសំណើរឲ្យកូដ

## ប្រៀបធៀបរវាង Mistral Small និង Mistral Large

ដើម្បីបង្ហាញភាពខុសគ្នានៃ latency រវាង Mistral Small និង Large សូមរត់ក្រឡាចុកខាងក្រោម។

អ្នកគួរមើលឃើញភាពខុសគ្នានៃពេលចំលើយអាចចន្លោះ 3-5 វិនាទី។ សូមយកចិត្តទុកដាក់កំរិតនិងរចនាបថនៃចម្លើយលើសំណួរដូចគ្នា។

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

ផ្ទៀងផ្ទាត់នឹងម៉ូដែលពីរផ្សេងទៀតដែលបានពិភាក្សានៅក្នុងមេរៀននេះ Mistral NeMo គឺជាម៉ូដែលតែមួយដែលមានអាជ្ញាបណ្ណ Apache2 ឥតគិតថ្លៃ។

វាត្រូវបានពិចារណាថាជាការកែលម្អទៅលើ LLM ដើមប្រភពបើកពីមុនរបស់ Mistral, Mistral 7B។

លក្ខណៈផ្សេងទៀតរបស់ម៉ូដែល NeMo មានដូចជា៖

- *វាសនាការបំបែក Tokenization ប្រសើរ*: ម៉ូដែលនេះប្រើកម្មវិធី Tekken tokenizer ជំនួស tiktoken ដែលធ្វើឲ្យមានប្រសិទ្ធភាពល្អជាងលើភាសា និងកូដច្រើនជាង។
  
- *ការប្រើប្រាស់ Finetuning:* ម៉ូដែលមូលដ្ឋានមានស្រាប់សម្រាប់ការបូមបូកបន្ថែម (finetuning)។ វាផ្តល់ភាពបត់បែនសម្រាប់ករណីប្រើប្រាស់ដែលត្រូវការបូមបូកបន្ថែម។
  
- *ការហៅមុខងារតែម្តង*- ដូចជា Mistral Large ម៉ូដែលនេះត្រូវបានបណ្តុះបណ្តាលក្នុងការហៅមុខងារ។ វាធ្វើឲ្យវាផ្សេងពីម៉ូដែលប្រភពបើកដំបូងដែលបានបង្កើតមុខងារ​នេះ។

### ប្រៀបធៀប Tokenizers

ក្នុងគំរូនេះ យើងនឹងមើលពីរបៀបដែល Mistral NeMo រៀបចំ tokenization ប្រៀបធៀបនឹង Mistral Large។

គំរូទាំងពីរយកសំណួរដូចគ្នា ប៉ុន្តែអ្នកនឹងឃើញថា NeMo បញ្ចេញ tokens តិចជាង Mistral Large។

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

# ផ្ទុកម៉ាស៊ីនបំបែកពាក្យ Mistral

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# បំបែកបញ្ជីសារជាភាសាពីក្រដាស
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

# រាប់ចំនួនសញ្ញាសំគាល់
print(len(tokens))
```

```python
# នាំចូលកញ្ចប់ដែលចាំបាច់៖
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

# បំបែកបញ្ជីសារទៅជាពាក្យតូចៗ
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

# រាប់ចំនួនពាក្យតូចៗ
print(len(tokens))
```

## ការសិក្សាមិនទប់ស្កាត់នៅទីនេះ បន្តដំណើរការ

បន្ទាប់ពីបញ្ចប់មេរៀននេះ សូមពិនិត្យមើល [សំណុំការសិក្សា AI បង្កើតចេញ](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) របស់យើងដើម្បីបន្តបង្កើនចំណេះដឹង AI របស់អ្នក!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវ​បាន​ប្រែ​សម្រួល​ដោយ​ប្រើ​សេវា​ប្រែ​សម្រួល​ជាមួយ​បច្ចេកវិទ្យា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈ​ពេល​យើង​ព្យាយាម​ប្រឹង​ប្រែង​ទៅ​លើភាព​ត្រឹមត្រូវ សូម​ដឹងថា​ការប្រែសម្រួល​ដោយ​ស្វ័យប្រវត្តិ​អាច​មានកំហុស ឬ​ភាពមិន​ត្រឹមត្រូវ​ខ្លះៗ។ ឯកសារដើម​ជា​ភាសាមូល​ដ្ឋាន​គួរត្រូវ​បាន​គេ​យក​ជា​ប្រភព​ផ្លូវការ។ សម្រាប់​ព័ត៌មាន​សំខាន់ៗ អនុសារណ៍​ឲ្យ​ប្រើ​ការ​ប្រែ​សម្រួល​ដោយ​មនុស្ស​អ្នកជំនាញ។ យើង​មិនទទួលបន្ទុក​ចំពោះ​ការយល់ច្រឡំ ឬ​ការ​បកស្រាយ​ខុស ដោយសារការប្រើប្រាស់​ការ​ប្រែសម្រួល​នេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->