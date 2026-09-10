# البناء باستخدام نماذج Mistral 

## المقدمة 

ستغطي هذه الدرس: 
- استكشاف نماذج Mistral المختلفة 
- فهم حالات الاستخدام والسيناريوهات لكل نموذج 
- استكشاف عينات الشيفرة التي توضح الميزات الفريدة لكل نموذج. 

## نماذج Mistral 

في هذا الدرس، سوف نستكشف 3 نماذج مختلفة من Mistral: 
**Mistral Large**، **Mistral Small** و **Mistral Nemo**. 

كل واحد من هذه النماذج متاح مجانًا على [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst). سيتم استخدام هذه النماذج في هذا الدفتر لتشغيل الشيفرة.

> **ملاحظة:** نماذج GitHub سيتم إنهاؤها في نهاية يوليو 2026. هنا المزيد من التفاصيل حول استخدام [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) لنمذجة نماذج الذكاء الاصطناعي. 


## Mistral Large 2 (2407)
Mistral Large 2 هو حاليًا النموذج الرائد من Mistral ومصمم للاستخدام المؤسسي. 

هذا النموذج هو ترقية للنموذج الأصلي Mistral Large من خلال تقديم  
-  نافذة سياق أكبر - 128k مقابل 32k 
-  أداء أفضل في مهام الرياضيات والترميز - دقة متوسطة 76.9% مقابل 60.4% 
-  زيادة الأداء متعدد اللغات - اللغات تشمل: الإنجليزية، الفرنسية، الألمانية، الإسبانية، الإيطالية، البرتغالية، الهولندية، الروسية، الصينية، اليابانية، الكورية، العربية، والهندية.

مع هذه الميزات، يتميز Mistral Large في 
- *التوليد المعزز بالاسترجاع (RAG)* - بسبب نافذة السياق الأكبر
- *استدعاء الوظائف* - هذا النموذج يحتوي على استدعاء وظائف أصلي يسمح بالاندماج مع الأدوات وواجهات برمجة التطبيقات الخارجية. يمكن إجراء هذه الاستدعاءات بالتوازي أو بالتسلسل الواحدة تلو الأخرى. 
- *توليد الشيفرة* - يتميز هذا النموذج في توليد البرمجة بـ Python و Java و TypeScript و C++. 

### مثال على RAG باستخدام Mistral Large 2 

في هذا المثال، نستخدم Mistral Large 2 لتشغيل نمط RAG على مستند نصي. السؤال مكتوب بالكورية ويسأل عن نشاطات المؤلف قبل الكلية. 

يستخدم نموذج تجسيد النصوص Cohere لإنشاء تمثيلات نصية لكل من المستند والسؤال. في هذا المثال، يستخدم حزمة faiss للبايثون لتخزين المتجهات. 

الحافز المرسل إلى نموذج Mistral يتضمن كلا من الأسئلة والقطع المسترجعة التي تشبه السؤال. ثم يقدم النموذج إجابة بلغة طبيعية. 

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

# احصل على هذه من صفحة "نظرة عامة" لمشروع Microsoft Foundry الخاص بك
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
Mistral Small هو نموذج آخر في عائلة Mistral ضمن فئة النماذج المتميزة / المؤسسية. كما يوحي الاسم، هذا النموذج هو نموذج لغة صغير (SLM). مزايا استخدام Mistral Small هي: 
- توفير التكلفة مقارنة بنماذج LLM من Mistral مثل Mistral Large وNeMo - انخفاض سعر بنسبة 80%
- زمن استجابة منخفض - استجابة أسرع مقارنة بنماذج Mistral LLMs
- مرونة - يمكن نشره عبر بيئات مختلفة مع قيود أقل على الموارد المطلوبة. 


Mistral Small ممتاز لـ: 
- مهام تعتمد على النص مثل التلخيص، وتحليل المشاعر، والترجمة. 
- التطبيقات التي تتطلب طلبات متكررة بسبب كفاءته من حيث التكلفة 
- مهام الشيفرة بزمن استجابة منخفض مثل المراجعة واقتراحات الشيفرة 

## مقارنة بين Mistral Small و Mistral Large 

لعرض الفروقات في زمن الاستجابة بين Mistral Small و Large، شغل الخلايا أدناه. 

يجب أن ترى فرقًا في أوقات الاستجابة يتراوح بين 3-5 ثوانٍ. لاحظ أيضًا طول الاستجابات والأسلوب على نفس الحافز.  

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

بالمقارنة مع النموذجين الآخرين اللذين نوقشا في هذا الدرس، Mistral NeMo هو النموذج المجاني الوحيد المرخص برخصة Apache2. 

يُنظر إليه كترقية للنموذج المفتوح المصدر السابق من Mistral، Mistral 7B. 

بعض الميزات الأخرى لنموذج NeMo هي: 

- *تشغيل الترميز بشكل أكثر كفاءة:* يستخدم هذا النموذج مشفر Tekken بدلاً من المشفر الشائع الاستخدام tiktoken. هذا يسمح بأداء أفضل عبر لغات وشيفرات أكثر. 

- *التخصيص الدقيق (Finetuning):* النموذج الأساسي متاح للتخصيص الدقيق. هذا يوفر مرونة أكثر لحالات الاستخدام التي قد تحتاج إلى تخصيص. 

- *استدعاء الوظائف الأصلي* - مثل Mistral Large، تم تدريب هذا النموذج على استدعاء الوظائف. هذا يجعله فريدًا كونه واحدًا من أول النماذج مفتوحة المصدر التي تقوم بذلك. 


### مقارنة بين مشفرات النصوص (Tokenizers) 

في هذا المثال، سننظر إلى كيفية تعامل Mistral NeMo مع تشغيل الترميز مقارنة بـ Mistral Large. 

كلا المثالين يستخدمان نفس الحافز لكن يجب أن تشاهد أن NeMo يعيد رموز أقل من Mistral Large. 

```bash
pip install mistral-common
```

```python 
# استيراد الحزم المطلوبة:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# تحميل محلل الرموز Mistral

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# تجزئة قائمة من الرسائل
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

# تحميل محلل الرموز Mistral

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# تحليل قائمة من الرسائل إلى رموز
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

## التعلم لا يتوقف هنا، واصل الرحلة

بعد إنهاء هذا الدرس، اطلع على [مجموعة تعلم الذكاء الاصطناعي التوليدي](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) للاستمرار في رفع مستوى معرفتك بالذكاء الاصطناعي التوليدي!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->