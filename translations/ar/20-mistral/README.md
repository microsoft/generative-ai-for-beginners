# بناء باستخدام نماذج Mistral

## المقدمة

سيغطي هذا الدرس:
- استكشاف نماذج Mistral المختلفة
- فهم حالات الاستخدام والسيناريوهات لكل نموذج
- استكشاف عينات من الشفرات التي تعرض الميزات الفريدة لكل نموذج.

## نماذج Mistral

في هذا الدرس، سوف نستكشف ٣ نماذج مختلفة من Mistral:
**Mistral Large**، **Mistral Small** و **Mistral Nemo**.

كل هذه النماذج متاحة مجانًا على سوق نماذج GitHub. سيستخدم الكود في هذا الدفتر هذه النماذج لتشغيل الشفرة. فيما يلي المزيد من التفاصيل حول استخدام نماذج GitHub لـ [النمذجة الأولية مع نماذج الذكاء الاصطناعي](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)
يعد Mistral Large 2 حاليًا النموذج الرائد من Mistral ومصمم للاستخدام المؤسسي.

يعد النموذج ترقية لـ Mistral Large الأصلي من خلال تقديم:
- نافذة سياق أكبر - 128k مقابل 32k
- أداء أفضل في مهام الرياضيات والترميز - دقة متوسطة 76.9% مقابل 60.4%
- أداء متعدد اللغات معزز - تشمل اللغات: الإنجليزية، الفرنسية، الألمانية، الإسبانية، الإيطالية، البرتغالية، الهولندية، الروسية، الصينية، اليابانية، الكورية، العربية، والهندية.

مع هذه الميزات، يتفوق Mistral Large في:
- *التوليد المعزز بالاستخراج (RAG)* - بسبب نافذة السياق الأكبر
- *استدعاء الدوال* - يحتوي هذا النموذج على استدعاء دوال أصلي يسمح بالتكامل مع الأدوات و APIs الخارجية. يمكن إجراء هذه الاستدعاءات بالتوازي أو بالتتابع الواحدة تلو الأخرى.
- *توليد الشفرات* - يتفوق هذا النموذج في توليد شفرات Python, Java, TypeScript و C++.

### مثال على RAG باستخدام Mistral Large 2

في هذا المثال، نستخدم Mistral Large 2 لتشغيل نمط RAG على مستند نصي. السؤال مكتوب باللغة الكورية ويسأل عن أنشطة المؤلف قبل الجامعة.

يستخدم نموذج Embeddings من Cohere لإنشاء تمثيلات للنص وكذلك للسؤال. في هذه العينة، يستخدم حزمة faiss في Python كمخزن متجه.

تشمل المُطالبة المرسلة إلى نموذج Mistral كلًا من الأسئلة والقطع المسترجعة المشابهة للسؤال. ثم يقدم النموذج ردًا باللغة الطبيعية.

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
Mistral Small هو نموذج آخر في عائلة نماذج Mistral تحت الفئة المتميزة/المؤسسية. كما يشير الاسم، هذا النموذج هو نموذج لغة صغير (SLM). مزايا استخدام Mistral Small هي أنه:
- موفّر للتكلفة مقارنة بناماذج Mistral العملاقة مثل Mistral Large و NeMo - انخفاض السعر بنسبة ٨٠٪
- زمن استجابة منخفض - استجابة أسرع مقارنة بنماذج Mistral الأخرى
- مرن - يمكن نشره عبر بيئات مختلفة مع قيود أقل على الموارد المطلوبة.

يعد Mistral Small ممتازًا لـ:
- المهام النصية مثل التلخيص، تحليل المشاعر، والترجمة.
- التطبيقات التي يتم فيها إرسال طلبات متكررة بسبب فعاليته من حيث التكلفة.
- مهام الشفرة ذات الاستجابة السريعة مثل مراجعة الشفرات والاقتراحات.

## مقارنة بين Mistral Small و Mistral Large

لعرض الفروق في زمن الاستجابة بين Mistral Small و Large، شغّل الخلايا أدناه.

ينبغي أن تلاحظ فرقًا في أوقات الاستجابة يتراوح بين ٣-٥ ثوانٍ. لاحظ أيضًا أطوال الردود والأسلوب عبر نفس المُطالبة.

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

بالمقارنة مع النموذجين الآخرين الذين نوقشوا في هذا الدرس، يعد Mistral NeMo هو النموذج الحر الوحيد برخصة Apache2.

يُعتبر ترقية للإصدار المفتوح المصدر السابق من Mistral، وهو Mistral 7B.

بعض الميزات الأخرى لنموذج NeMo هي:

- *تقطيع أكثر كفاءة:* يستخدم هذا النموذج قاطع الكلمات Tekken بدلاً من القاطع الشائع tiktoken. هذا يسمح بأداء أفضل عبر المزيد من اللغات والرموز البرمجية.

- *الضبط الدقيق:* النموذج الأساسي متاح للضبط الدقيق. هذا يمنح المزيد من المرونة لحالات الاستخدام التي قد تتطلب الضبط.

- *استدعاء الدوال الأصلي* - مثل Mistral Large، تم تدريب هذا النموذج على استدعاء الدوال. هذا يجعله فريدًا كونه أحد أول النماذج مفتوحة المصدر التي تفعل ذلك.

### مقارنة قواطع النص

في هذه العينة، سوف نرى كيف يتعامل Mistral NeMo مع تقطيع النص مقارنة بـ Mistral Large.

تأخذ كلتا العينتين نفس المُطالبة، لكن يجب أن ترى أن NeMo يعيد عددًا أقل من الرموز من Mistral Large.

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

# تحميل محلل رموز Mistral

model_name = "open-mistral-nemo"

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

# تحميل محلل ميسرال للنصوص

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# ترميز قائمة الرسائل
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

# عدّ عدد الرموز
print(len(tokens))
```


## التعلم لا يتوقف هنا، استمر في الرحلة

بعد إكمال هذا الدرس، تفقد مجموعتنا [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) للارتقاء بمعرفتك في مجال الذكاء الاصطناعي التوليدي!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). وعلى الرغم من سعينا لتحقيق الدقة، يُرجى العلم بأن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. وللحصول على معلومات حرجة، يُنصح بالترجمة الاحترافية البشرية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->