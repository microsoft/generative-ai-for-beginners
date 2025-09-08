<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T18:55:56+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "ar"
}
-->
# البناء باستخدام نماذج Mistral

## المقدمة

ستتناول هذه الدرس:  
- استكشاف نماذج Mistral المختلفة  
- فهم حالات الاستخدام والسيناريوهات لكل نموذج  
- أمثلة برمجية توضح الميزات الفريدة لكل نموذج.

## نماذج Mistral

في هذا الدرس، سنستعرض 3 نماذج مختلفة من Mistral:  
**Mistral Large**، **Mistral Small** و **Mistral Nemo**.

كل هذه النماذج متاحة مجانًا على سوق نماذج Github. الكود في هذا الدفتر سيستخدم هذه النماذج لتشغيل الأكواد. إليك المزيد من التفاصيل حول استخدام نماذج Github لـ [النمذجة الأولية مع نماذج الذكاء الاصطناعي](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)  
يُعتبر Mistral Large 2 حاليًا النموذج الرائد من Mistral ومصمم للاستخدام المؤسسي.

هذا النموذج هو ترقية لـ Mistral Large الأصلي من خلال تقديم:  
- نافذة سياق أكبر - 128k مقابل 32k  
- أداء أفضل في مهام الرياضيات والبرمجة - دقة متوسطة 76.9% مقابل 60.4%  
- تحسين الأداء متعدد اللغات - تشمل اللغات: الإنجليزية، الفرنسية، الألمانية، الإسبانية، الإيطالية، البرتغالية، الهولندية، الروسية، الصينية، اليابانية، الكورية، العربية، والهندية.

بفضل هذه الميزات، يتفوق Mistral Large في:  
- *التوليد المعزز بالاسترجاع (RAG)* - بسبب نافذة السياق الأكبر  
- *استدعاء الدوال* - يحتوي هذا النموذج على استدعاء دوال مدمج يسمح بالتكامل مع الأدوات والواجهات البرمجية الخارجية. يمكن تنفيذ هذه الاستدعاءات بشكل متوازي أو متسلسل.  
- *توليد الأكواد* - يتفوق هذا النموذج في توليد أكواد Python وJava وTypeScript وC++.

### مثال RAG باستخدام Mistral Large 2

في هذا المثال، نستخدم Mistral Large 2 لتشغيل نمط RAG على مستند نصي. السؤال مكتوب بالكورية ويسأل عن أنشطة المؤلف قبل الجامعة.

يستخدم نموذج Cohere Embeddings لإنشاء تمثيلات نصية للمستند وكذلك للسؤال. في هذا المثال، يستخدم حزمة faiss في Python كمخزن متجهات.

الموجه المرسل إلى نموذج Mistral يتضمن كل من الأسئلة والقطع المسترجعة المشابهة للسؤال. ثم يقدم النموذج ردًا بلغة طبيعية.

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
Mistral Small هو نموذج آخر ضمن عائلة نماذج Mistral تحت فئة النماذج المتميزة/المؤسسية. كما يوحي الاسم، هذا النموذج هو نموذج لغة صغير (SLM). مزايا استخدام Mistral Small هي:  
- توفير في التكلفة مقارنة بنماذج Mistral LLM مثل Mistral Large وNeMo - انخفاض السعر بنسبة 80%  
- زمن استجابة منخفض - أسرع مقارنة بنماذج Mistral LLM  
- مرونة - يمكن نشره في بيئات مختلفة مع قيود أقل على الموارد المطلوبة.

Mistral Small مناسب لـ:  
- المهام النصية مثل التلخيص، تحليل المشاعر، والترجمة.  
- التطبيقات التي تتطلب طلبات متكررة بسبب فعاليته من حيث التكلفة  
- مهام الأكواد ذات زمن الاستجابة المنخفض مثل المراجعة واقتراحات الأكواد

## مقارنة بين Mistral Small و Mistral Large

لإظهار الفروقات في زمن الاستجابة بين Mistral Small و Large، قم بتشغيل الخلايا أدناه.

يجب أن تلاحظ فرقًا في أوقات الاستجابة يتراوح بين 3-5 ثوانٍ. كما لاحظ طول الردود والأسلوب على نفس الموجه.

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

مقارنة بالنموذجين الآخرين الذين نوقشوا في هذا الدرس، يُعتبر Mistral NeMo هو النموذج المجاني الوحيد المرخص برخصة Apache2.

يُنظر إليه كترقية للنموذج مفتوح المصدر السابق من Mistral، وهو Mistral 7B.

بعض الميزات الأخرى لنموذج NeMo هي:

- *تحسين التقطيع إلى رموز (tokenization):* يستخدم هذا النموذج مقطع Tekken بدلاً من tiktoken الأكثر شيوعًا. هذا يسمح بأداء أفضل عبر لغات وأكواد متعددة.

- *التدريب الدقيق (Finetuning):* النموذج الأساسي متاح للتدريب الدقيق، مما يوفر مرونة أكبر لحالات الاستخدام التي قد تحتاج إلى تخصيص.

- *استدعاء الدوال المدمج* - مثل Mistral Large، تم تدريب هذا النموذج على استدعاء الدوال. وهذا يجعله فريدًا كأحد أول النماذج مفتوحة المصدر التي تدعم هذه الميزة.

### مقارنة بين أدوات التقطيع (Tokenizers)

في هذا المثال، سنرى كيف يتعامل Mistral NeMo مع التقطيع مقارنة بـ Mistral Large.

كلا النموذجين يستخدمان نفس الموجه، لكن ستلاحظ أن NeMo يعيد عددًا أقل من الرموز مقارنة بـ Mistral Large.

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

## التعلم لا يتوقف هنا، استمر في الرحلة

بعد إكمال هذا الدرس، اطلع على [مجموعة تعلم الذكاء الاصطناعي التوليدي](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) لمواصلة تطوير معرفتك في مجال الذكاء الاصطناعي التوليدي!

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.