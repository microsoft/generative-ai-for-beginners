<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T10:45:51+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "ar"
}
-->
# بناء باستخدام نماذج ميسترال

## مقدمة

ستغطي هذه الدرس:
- استكشاف النماذج المختلفة لميسترال
- فهم حالات الاستخدام والسيناريوهات لكل نموذج
- أمثلة على الشيفرة توضح الميزات الفريدة لكل نموذج.

## نماذج ميسترال

في هذه الدرس، سنستكشف ثلاثة نماذج مختلفة من ميسترال: **ميسترال كبير**، **ميسترال صغير** و**ميسترال نيمو**.

كل من هذه النماذج متاح مجانًا في سوق النماذج على GitHub. سيتم استخدام الشيفرة في هذا الدفتر لاستخدام هذه النماذج لتشغيل الشيفرة. إليك المزيد من التفاصيل حول استخدام نماذج GitHub لـ [النمذجة باستخدام نماذج الذكاء الاصطناعي](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## ميسترال كبير 2 (2407)

يُعد ميسترال كبير 2 حاليًا النموذج الرائد من ميسترال ومصمم للاستخدام المؤسسي.

النموذج هو ترقية للنموذج الأصلي ميسترال كبير من خلال تقديم:
- نافذة سياق أكبر - 128k مقابل 32k
- أداء أفضل في مهام الرياضيات والبرمجة - متوسط دقة 76.9% مقابل 60.4%
- زيادة الأداء متعدد اللغات - اللغات تشمل: الإنجليزية، الفرنسية، الألمانية، الإسبانية، الإيطالية، البرتغالية، الهولندية، الروسية، الصينية، اليابانية، الكورية، العربية، والهندية.

مع هذه الميزات، يتفوق ميسترال كبير في:
- *التوليد المعزز بالاسترجاع (RAG)* - بفضل نافذة السياق الأكبر
- *استدعاء الوظائف* - يحتوي هذا النموذج على استدعاء وظائف أصلي يسمح بالتكامل مع الأدوات وواجهات برمجة التطبيقات الخارجية. يمكن إجراء هذه الاستدعاءات بالتوازي أو واحدًا تلو الآخر بترتيب تسلسلي.
- *توليد الشيفرة* - يتفوق هذا النموذج في توليد شيفرة Python وJava وTypeScript وC++.

### مثال على RAG باستخدام ميسترال كبير 2

في هذا المثال، نستخدم ميسترال كبير 2 لتشغيل نمط RAG على مستند نصي. السؤال مكتوب باللغة الكورية ويسأل عن أنشطة المؤلف قبل الكلية.

يستخدم نموذج Cohere Embeddings لإنشاء تمثيلات نصية للمستند النصي وكذلك السؤال. لهذا المثال، يستخدم حزمة Python faiss كمخزن متجهات.

يشمل الموجه المرسل إلى نموذج ميسترال كلا من الأسئلة والقطع المسترجعة التي تشبه السؤال. ثم يوفر النموذج استجابة بلغة طبيعية.

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

## ميسترال صغير

ميسترال صغير هو نموذج آخر في عائلة نماذج ميسترال تحت فئة النماذج المؤسسية/الرائدة. كما يوحي الاسم، فإن هذا النموذج هو نموذج لغة صغير (SLM). فوائد استخدام ميسترال صغير هي أنه:
- توفير التكاليف مقارنة بنماذج LLM لميسترال مثل ميسترال كبير وNeMo - انخفاض في السعر بنسبة 80%
- زمن استجابة منخفض - استجابة أسرع مقارنة بنماذج LLM لميسترال
- مرن - يمكن نشره عبر بيئات مختلفة مع قيود أقل على الموارد المطلوبة.

ميسترال صغير مثالي لـ:
- المهام النصية مثل التلخيص، وتحليل المشاعر، والترجمة.
- التطبيقات التي تتطلب طلبات متكررة بفضل فعاليته من حيث التكلفة.
- مهام الشيفرة ذات زمن الاستجابة المنخفض مثل المراجعة واقتراحات الشيفرة.

## مقارنة بين ميسترال صغير وميسترال كبير

لإظهار الفروق في زمن الاستجابة بين ميسترال صغير وكبير، قم بتشغيل الخلايا أدناه.

يجب أن تلاحظ فرقًا في أوقات الاستجابة بين 3-5 ثوانٍ. لاحظ أيضًا أطوال الاستجابة والأسلوب على نفس الموجه.

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

مقارنة بالنموذجين الآخرين الذين تمت مناقشتهما في هذه الدرس، ميسترال نيمو هو النموذج المجاني الوحيد برخصة Apache2.

يُعتبر ترقية للنموذج مفتوح المصدر السابق من ميسترال، ميسترال 7B.

بعض الميزات الأخرى لنموذج نيمو هي:

- *ترميز أكثر كفاءة:* يستخدم هذا النموذج أداة الترميز Tekken بدلاً من tiktoken الأكثر شيوعًا. يتيح ذلك أداءً أفضل عبر المزيد من اللغات والشيفرة.

- *التخصيص الدقيق:* النموذج الأساسي متاح للتخصيص الدقيق. يتيح ذلك مزيدًا من المرونة لحالات الاستخدام التي قد تحتاج إلى تخصيص دقيق.

- *استدعاء الوظائف الأصلي* - مثل ميسترال كبير، تم تدريب هذا النموذج على استدعاء الوظائف. يجعله ذلك فريدًا كونه أحد أول النماذج مفتوحة المصدر التي تقوم بذلك.

### مقارنة أدوات الترميز

في هذا المثال، سنلقي نظرة على كيفية تعامل ميسترال نيمو مع الترميز مقارنة بميسترال كبير.

كلا المثالين يأخذان نفس الموجه ولكن يجب أن تلاحظ أن نيمو يعيد عددًا أقل من الرموز مقابل ميسترال كبير.

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

## التعلم لا يتوقف هنا، واصل الرحلة

بعد إكمال هذه الدرس، تحقق من [مجموعة تعلم الذكاء الاصطناعي التوليدي](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) لمواصلة تعزيز معرفتك في مجال الذكاء الاصطناعي التوليدي!

**إخلاء المسؤولية**:  
تمت ترجمة هذه الوثيقة باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار الوثيقة الأصلية بلغتها الأم المصدر الموثوق. للمعلومات الحساسة، يوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.