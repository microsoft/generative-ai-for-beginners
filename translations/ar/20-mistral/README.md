# البناء باستخدام نماذج Mistral

## المقدمة

هذا الدرس سيغطي:
- استكشاف نماذج Mistral المختلفة
- فهم حالات الاستخدام والسيناريوهات لكل نموذج
- استكشاف أمثلة برمجية تُظهر الميزات الفريدة لكل نموذج.

## نماذج Mistral

في هذا الدرس، سنستكشف 3 نماذج مختلفة من Mistral:
**Mistral Large**، **Mistral Small** و **Mistral Nemo**.

كل من هذه النماذج متاح مجانًا على [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). الكود في هذا الدفتر سيستخدم هذه النماذج لتشغيل الكود.

> **ملاحظة:** نماذج GitHub سيتوقف دعمها في نهاية يوليو 2026. هنا مزيد من التفاصيل حول استخدام [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) لعمل نماذج أولية مع نماذج الذكاء الاصطناعي.


## Mistral Large 2 (2407)
Mistral Large 2 هو حاليًا النموذج الرئيسي من Mistral ومصمم للاستخدام المؤسسي.

النموذج هو ترقية لـ Mistral Large الأصلي من خلال تقديم
- نافذة سياق أكبر - 128k مقابل 32k
- أداء أفضل في مهام الرياضيات والبرمجة - دقة متوسطة 76.9% مقابل 60.4%
- زيادة الأداء متعدد اللغات - اللغات تشمل: الإنجليزية، الفرنسية، الألمانية، الإسبانية، الإيطالية، البرتغالية، الهولندية، الروسية، الصينية، اليابانية، الكورية، العربية، والهندية.

مع هذه الميزات، يتفوق Mistral Large في
- *التوليد المعزز بالاسترجاع (RAG)* - بسبب نافذة السياق الأكبر
- *استدعاء الوظائف* - لهذا النموذج استدعاء وظائف مدمج يسمح بالتكامل مع الأدوات والواجهات البرمجية الخارجية. يمكن إجراء هذه الاستدعاءات متوازية أو متتابعة.
- *توليد الكود* - يتفوق هذا النموذج في توليد كود Python وJava وTypeScript وC++.

### مثال RAG باستخدام Mistral Large 2

في هذا المثال، نستخدم Mistral Large 2 لتشغيل نمط RAG على مستند نصي. السؤال مكتوب بالكورية ويسأل عن أنشطة المؤلف قبل الجامعة.

يستخدم نموذج تضمين Cohere لإنشاء تضمينات لمستند النص وكذلك للسؤال. لهذه العينة، يستخدم مكتبة faiss للبايثون كمخزن متجهات.

الموجه المرسل إلى نموذج Mistral يشمل كل من الأسئلة والقطع المسترجعة المشابهة للسؤال. ثم يقدم النموذج ردًا بلغة طبيعية.

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

# احصل على هذه من صفحة "نظرة عامة" في مشروع Microsoft Foundry الخاص بك
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # المسافة، الفهرس
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
Mistral Small هو نموذج آخر في عائلة Mistral ضمن فئة النماذج المتميزة / المؤسسية. كما يشير الاسم، هذا النموذج هو نموذج لغة صغير (SLM). مزايا استخدام Mistral Small هي أنه:
- موفر للتكاليف مقارنة بنماذج Mistral الكبيرة مثل Mistral Large وNeMo - انخفاض السعر بنسبة 80%
- منخفض الكمون - استجابة أسرع مقارنة بنماذج Mistral الكبيرة
- مرن - يمكن نشره عبر بيئات مختلفة مع قيود أقل من حيث الموارد المطلوبة.


Mistral Small ممتاز لـ:
- المهام النصية مثل التلخيص، تحليل المشاعر، والترجمة.
- التطبيقات التي تتطلب طلبات متكررة بسبب فعاليته من حيث التكلفة
- مهام الكود ذات الكمون المنخفض مثل المراجعة واقتراحات الكود

## مقارنة بين Mistral Small وMistral Large

لإظهار الفروق في الكمون بين Mistral Small وLarge، قم بتشغيل الخلايا أدناه.

يجب أن ترى فرقًا في أوقات الاستجابة بين 3-5 ثواني. لاحظ أيضًا أطوال الردود وأسلوبها على نفس الموجه.

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

مقارنة بالنموذجين الآخرين الذين نوقشوا في هذا الدرس، Mistral NeMo هو النموذج المجاني الوحيد مع ترخيص Apache2.

يُعتبر ترقية للنموذج السابق مفتوح المصدر من Mistral، Mistral 7B.

بعض الميزات الأخرى لنموذج NeMo هي:

- *التقسيم إلى رموز أكثر كفاءة:* يستخدم هذا النموذج مُقسِم Tekken بدلاً من tiktoken الأكثر استخدامًا. هذا يسمح بأداء أفضل عبر المزيد من اللغات والكود.

- *التدريب الدقيق:* النموذج الأساسي متاح للتدريب الدقيق. هذا يوفر مرونة أكبر لحالات الاستخدام التي قد تتطلب تدريبًا دقيقًا.

- *استدعاء الوظائف الأصلي* - مثل Mistral Large، تم تدريب هذا النموذج على استدعاء الوظائف. هذا يجعله فريدًا كونه واحدًا من أول النماذج مفتوحة المصدر التي تقوم بذلك.


### مقارنة بين المقسمات (Tokenizers)

في هذه العينة، سننظر كيف يتعامل Mistral NeMo مع التقسيم إلى رموز مقارنة بـ Mistral Large.

كلا العيّنات تأخذ نفس الموجه لكن يجب أن ترى أن NeMo يعيد رموزًا أقل من Mistral Large.

```bash
pip install mistral-common
```

```python 
# استيراد الحزم اللازمة:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# تحميل محول الرموز Mistral

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# تحويل قائمة الرسائل إلى رموز
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

# عد عدد الرموز
print(len(tokens))
```

```python
# استيراد الحزم الضرورية:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# تحميل مفسر الرموز Mistral

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# تقسيم قائمة الرسائل إلى رموز
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

# حساب عدد الرموز
print(len(tokens))
```

## التعلم لا يتوقف هنا، استمر في الرحلة

بعد إكمال هذا الدرس، تحقق من [مجموعة تعلم الذكاء الاصطناعي التوليدي](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) لمواصلة رفع مستوى معرفتك في الذكاء الاصطناعي التوليدي!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->