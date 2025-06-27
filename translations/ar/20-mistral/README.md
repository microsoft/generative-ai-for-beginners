<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-06-26T03:11:19+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "ar"
}
-->
# بناء باستخدام نماذج ميسترال

## مقدمة

هذه الدرس سيغطي:
- استكشاف نماذج ميسترال المختلفة
- فهم حالات الاستخدام والسيناريوهات لكل نموذج
- أمثلة على الأكواد تظهر الميزات الفريدة لكل نموذج.

## نماذج ميسترال

في هذا الدرس، سنستكشف ثلاثة نماذج مختلفة من ميسترال: **ميسترال الكبير**، **ميسترال الصغير** و **ميسترال نيمو**.

كل هذه النماذج متاحة مجانًا في سوق النماذج على GitHub. الكود في هذا الدفتر سيستخدم هذه النماذج لتشغيل الكود. هنا المزيد من التفاصيل حول استخدام نماذج GitHub لـ [النماذج الأولية باستخدام نماذج الذكاء الاصطناعي](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## ميسترال الكبير 2 (2407)
ميسترال الكبير 2 هو حاليًا النموذج الرائد من ميسترال ومصمم للاستخدام المؤسسي.

النموذج هو ترقية للنموذج الأصلي ميسترال الكبير من خلال تقديم:
- نافذة سياق أكبر - 128k مقابل 32k
- أداء أفضل في مهام الرياضيات والبرمجة - دقة متوسطة 76.9% مقابل 60.4%
- أداء متعدد اللغات متزايد - اللغات تشمل: الإنجليزية، الفرنسية، الألمانية، الإسبانية، الإيطالية، البرتغالية، الهولندية، الروسية، الصينية، اليابانية، الكورية، العربية، والهندية.

مع هذه الميزات، يتفوق ميسترال الكبير في:
- *توليد معزز بالاسترجاع (RAG)* - بسبب نافذة السياق الأكبر
- *استدعاء الوظائف* - هذا النموذج لديه استدعاء وظائف أصلي مما يسمح بالتكامل مع الأدوات الخارجية وواجهات برمجة التطبيقات. يمكن إجراء هذه الاستدعاءات بشكل متوازي أو واحد بعد الآخر بترتيب تسلسلي.
- *توليد الأكواد* - هذا النموذج يتفوق في توليد Python، Java، TypeScript و C++.

### مثال على RAG باستخدام ميسترال الكبير 2

في هذا المثال، نستخدم ميسترال الكبير 2 لتشغيل نمط RAG على مستند نصي. السؤال مكتوب باللغة الكورية ويسأل عن أنشطة المؤلف قبل الجامعة.

يستخدم نموذج Cohere Embeddings لإنشاء تضمينات للمستند النصي وكذلك السؤال. لهذا المثال، يستخدم حزمة Python faiss كمخزن متجهات.

الإشارة المرسلة إلى نموذج ميسترال تشمل كلا من الأسئلة والأجزاء المسترجعة التي تشبه السؤال. ثم يقدم النموذج استجابة بلغة طبيعية.

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

## ميسترال الصغير
ميسترال الصغير هو نموذج آخر في عائلة نماذج ميسترال تحت فئة النماذج الرائدة/المؤسسية. كما يوحي الاسم، هذا النموذج هو نموذج لغة صغير (SLM). مزايا استخدام ميسترال الصغير هي:
- توفير التكلفة مقارنة بنماذج ميسترال LLMs مثل ميسترال الكبير وNeMo - انخفاض السعر بنسبة 80%
- زمن استجابة منخفض - استجابة أسرع مقارنة بنماذج ميسترال LLMs
- مرونة - يمكن نشره عبر بيئات مختلفة مع قيود أقل على الموارد المطلوبة.

ميسترال الصغير ممتاز في:
- المهام النصية مثل التلخيص، تحليل المشاعر والترجمة.
- التطبيقات حيث يتم تقديم طلبات متكررة بسبب فعاليته من حيث التكلفة.
- مهام الأكواد ذات زمن الاستجابة المنخفض مثل المراجعة واقتراحات الأكواد.

## مقارنة ميسترال الصغير وميسترال الكبير

لإظهار الفروق في زمن الاستجابة بين ميسترال الصغير والكبير، قم بتشغيل الخلايا أدناه.

يجب أن ترى فرقًا في أوقات الاستجابة بين 3-5 ثواني. لاحظ أيضًا أطوال الاستجابة والأسلوب لنفس الإشارة.

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

## ميسترال نيمو

مقارنة بالنموذجين الآخرين الذين تمت مناقشتهم في هذا الدرس، ميسترال نيمو هو النموذج الوحيد المجاني مع رخصة Apache2.

يُنظر إليه على أنه ترقية للنموذج السابق المفتوح المصدر LLM من ميسترال، ميسترال 7B.

بعض الميزات الأخرى لنموذج نيمو هي:

- *تحسين التشفير:* يستخدم هذا النموذج مشفر Tekken بدلاً من المشفر المستخدم بشكل شائع tiktoken. هذا يسمح بأداء أفضل عبر لغات وأكواد أكثر.

- *التخصيص:* النموذج الأساسي متاح للتخصيص. هذا يسمح بمزيد من المرونة لحالات الاستخدام حيث قد يكون التخصيص مطلوبًا.

- *استدعاء الوظائف الأصلي* - مثل ميسترال الكبير، تم تدريب هذا النموذج على استدعاء الوظائف. هذا يجعله فريدًا كونه أحد النماذج المفتوحة المصدر الأولى التي تقوم بذلك.

### مقارنة المشفرات

في هذا المثال، سننظر في كيفية تعامل ميسترال نيمو مع التشفير مقارنة بميسترال الكبير.

كلا المثالين يأخذان نفس الإشارة لكن يجب أن ترى أن نيمو يعيد عدد أقل من الرموز مقابل ميسترال الكبير.

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

## التعلم لا يتوقف هنا، تابع الرحلة

بعد إكمال هذا الدرس، تحقق من [مجموعة تعلم الذكاء الاصطناعي التوليدي](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) لمواصلة تعزيز معرفتك في الذكاء الاصطناعي التوليدي!

**إخلاء المسؤولية**:  
تم ترجمة هذه الوثيقة باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يُرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار الوثيقة الأصلية بلغتها الأم المصدر الموثوق. بالنسبة للمعلومات الهامة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.