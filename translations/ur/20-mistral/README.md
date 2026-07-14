# میسٹرل ماڈلز کے ساتھ تعمیر

## تعارف

یہ سبق آپ کو درج ذیل موضوعات سے روشناس کرائے گا:
- مختلف میسٹرل ماڈلز کا جائزہ لینا
- ہر ماڈل کے استعمال کی صورتوں اور منظرناموں کو سمجھنا
- ایسے کوڈ نمونے دریافت کرنا جو ہر ماڈل کی منفرد خصوصیات کو ظاہر کرتے ہیں۔

## میسٹرل ماڈلز

اس سبق میں، ہم تین مختلف میسٹرل ماڈلز کو دریافت کریں گے:
**میسٹرل بڑا**، **میسٹرل چھوٹا** اور **میسٹرل نیمو**۔

ان میں سے ہر ماڈل [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) پر مفت دستیاب ہے۔ اس نوٹ بک میں کوڈ ان ماڈلز کو استعمال کرتے ہوئے چلایا جائے گا۔

> **نوٹ:** GitHub ماڈلز جولائی 2026 کے آخر میں بند ہو رہے ہیں۔ زیادہ تفصیلات کے لیے [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) کا استعمال کرتے ہوئے AI ماڈلز کے ساتھ تجربہ کاری کے طریقے دیکھیں۔


## میسٹرل بڑا 2 (2407)
میسٹرل بڑا 2 فی الحال میسٹرل کا فلیگ شپ ماڈل ہے اور اسے انٹرپرائز استعمال کے لیے ڈیزائن کیا گیا ہے۔

یہ ماڈل اصل میسٹرل بڑے کا اپ گریڈ ہے جو درج ذیل پیش کرتا ہے:
-  بڑا سیاق و سباق ونڈو - 128k بمقابلہ 32k
-  ریاضی اور کوڈنگ کے کاموں پر بہتر کارکردگی - 76.9٪ اوسط درستگی بمقابلہ 60.4٪
-  کثیراللسانی کارکردگی میں اضافہ - زبانوں میں شامل ہیں: انگریزی، فرانسیسی، جرمن، ہسپانوی، اطالوی، پرتگالی، ڈچ، روسی، چینی، جاپانی، کوریائی، عربی، اور ہندی۔

ان خصوصیات کے ساتھ، میسٹرل بڑا درج ذیل میں بہترین ہے:
- *ریٹریول آگمینٹڈ جنریشن (RAG)* - بڑے سیاق و سباق ونڈو کی بدولت
- *فنکشن کالنگ* - اس ماڈل میں مقامی فنکشن کالنگ ہوتی ہے جو بیرونی ٹولز اور APIs کے ساتھ انضمام کی اجازت دیتی ہے۔ یہ کالز متوازی یا ایک کے بعد ایک تسلسل میں کی جا سکتی ہیں۔
- *کوڈ جنریشن* - یہ ماڈل Python، Java، TypeScript اور C++ جنریشن میں مہارت رکھتا ہے۔

### میسٹرل بڑا 2 کے ساتھ RAG کی مثال

اس مثال میں، ہم میسٹرل بڑا 2 کو ایک ٹیکسٹ دستاویز پر RAG پیٹرن چلانے کے لیے استعمال کر رہے ہیں۔ سوال کوریائی زبان میں لکھا گیا ہے اور مصنف کی کالج سے پہلے کی سرگرمیوں کے بارے میں پوچھتا ہے۔

یہ Cohere ایمبیڈنگز ماڈل کو استعمال کرتا ہے تاکہ ٹیکسٹ دستاویز اور سوال دونوں کی ایمبیڈنگز بنائی جا سکیں۔ اس نمونے میں، faiss Python پیکیج کو ویکٹر اسٹور کے طور پر استعمال کیا گیا ہے۔

جو پرامپٹ میسٹرل ماڈل کو بھیجا جاتا ہے اس میں سوالات اور وہ ریکوری شدہ چنکس شامل ہوتے ہیں جو سوال کے مشابہ ہیں۔ ماڈل پھر قدرتی زبان میں جواب فراہم کرتا ہے۔

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

# انہیں اپنے Microsoft Foundry پروجیکٹ کے "اوورویو" صفحے سے حاصل کریں
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # فاصلے، اشاریہ
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

## میسٹرل چھوٹا
میسٹرل چھوٹا میسٹرل خاندان کا ایک اور ماڈل ہے جو پرائمئر/انٹرپرائز زمرہ میں آتا ہے۔ نام کی طرح، یہ ماڈل ایک چھوٹا لینگویج ماڈل (SLM) ہے۔ میسٹرل چھوٹا استعمال کرنے کے فوائد یہ ہیں کہ یہ:
- میسٹرل LLMs جیسے میسٹرل بڑا اور نیمو کے مقابلے میں لاگت میں بچت - 80٪ قیمت میں کمی
- کم تاخیر - میسٹرل کے LLMs کے مقابلے میں تیز تر جواب دہی
- لچکدار - کم وسائل کی ضرورت کے ساتھ مختلف ماحول میں تعینات کیا جا سکتا ہے۔


میسٹرل چھوٹا کے لیے بہترین ہے:
- متن کی بنیاد پر کام جیسے خلاصہ کاری، جذباتی تجزیہ اور ترجمہ۔
- ایسی ایپلیکیشنز جہاں بار بار درخواستیں آئیں، اس کی لاگت کی افادیت کی وجہ سے
- کم تاخیر والے کوڈ کے کام جیسے جائزہ اور کوڈ تجاویز

## میسٹرل چھوٹا اور میسٹرل بڑا کا موازنہ

میسٹرل چھوٹا اور بڑا کے درمیان تاخیر کے فرق کو دکھانے کے لیے، نیچے دیے گئے سیلز چلائیں۔

آپ کو 3-5 سیکنڈ کے درمیان جواب دینے کے وقت میں فرق دیکھنے کو ملے گا۔ اسی پرامپٹ کے لیے جواب کی لمبائی اور انداز کو بھی نوٹ کریں۔

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

## میسٹرل نیمو

اس سبق میں زیر بحث دیگر دو ماڈلز کے مقابلے میں، میسٹرل نیمو واحد مفت ماڈل ہے جس کے پاس Apache2 لائسنس ہے۔

اسے میسٹرل کے پہلے اوپن سورس LLM، میسٹرل 7B کا اپ گریڈ سمجھا جاتا ہے۔

نیمو ماڈل کی کچھ دیگر خصوصیات یہ ہیں:

- *مزید مؤثر ٹوکنائزیشن:* یہ ماڈل عام استعمال ہونے والے tiktoken کے بجائے Tekken ٹوکنائزر استعمال کرتا ہے۔ اس سے زیادہ زبانوں اور کوڈ پر بہتر کارکردگی ممکن ہوتی ہے۔

- *فائن ٹیوننگ:* بنیادی ماڈل فائن ٹیوننگ کے لیے دستیاب ہے۔ یہ ان استعمال کی صورتوں کے لیے زیادہ لچک فراہم کرتا ہے جہاں فائن ٹیوننگ ضروری ہو سکتی ہے۔

- *مقامی فنکشن کالنگ* - میسٹرل بڑے کی طرح، اس ماڈل کو فنکشن کالنگ پر تربیت دی گئی ہے۔ یہ اسے منفرد بناتا ہے کیونکہ یہ پہلے ایسے اوپن سورس ماڈلز میں سے ایک ہے جو یہ خصوصیت رکھتا ہے۔


### ٹوکنائزروں کا موازنہ

اس نمونے میں، ہم دیکھیں گے کہ میسٹرل نیمو میسٹرل بڑے کے مقابلے میں ٹوکنائزیشن کو کیسے ہینڈل کرتا ہے۔

دونوں نمونے ایک ہی پرامپٹ لیتے ہیں لیکن آپ دیکھیں گے کہ نیمو میسٹرل بڑے کے مقابلے میں کم ٹوکنز لوٹاتا ہے۔

```bash
pip install mistral-common
```

```python 
# ضروری پیکجز درآمد کریں:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Mistral ٹوکنائزر لوڈ کریں

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# پیغامات کی ایک فہرست کو ٹوکنائز کریں
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

# ٹوکنز کی تعداد گنیں
print(len(tokens))
```

```python
# ضروری پیکیجز درآمد کریں:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# مسٹرال ٹوکنائزر لوڈ کریں

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# پیغامات کی فہرست کو ٹوکنائز کریں
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

# ٹوکن کی تعداد شمار کریں
print(len(tokens))
```

## سیکھنا یہاں نہیں رکتا، سفر جاری رکھیں

اس سبق کی تکمیل کے بعد، ہمارے [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) کو دیکھیں تاکہ اپنی Generative AI معلومات کو مزید بڑھایا جا سکے!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->