# میسٹرال ماڈلز کے ساتھ تعمیر کرنا

## تعارف

یہ سبق درج ذیل موضوعات کا احاطہ کرے گا:
- مختلف میسٹرال ماڈلز کی تلاش
- ہر ماڈل کے استعمال کے کیسز اور منظرناموں کو سمجھنا
- کوڈ نمونوں کا جائزہ لینا جو ہر ماڈل کی منفرد خصوصیات دکھاتے ہیں۔

## میسٹرال ماڈلز

اس سبق میں، ہم 3 مختلف میسٹرال ماڈلز کا جائزہ لیں گے:
**میسٹرال لارجر**, **میسٹرال اسمال**، اور **میسٹرال نیمو**۔

یہ ماڈلز [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) پر مفت دستیاب ہیں۔ اس نوٹ بک میں کوڈ ان ماڈلز کو استعمال کرتے ہوئے چلایا جائے گا۔

> **نوٹ:** GitHub Models جولائی 2026 کے آخر میں بند ہو رہے ہیں۔ AI ماڈلز کے ساتھ پروٹوٹائپ بنانے کے لیے مزید تفصیلات [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) پر دستیاب ہیں۔


## میسٹرال لارجر 2 (2407)
میسٹرال لارجر 2 فی الحال میسٹرال کا اہم ماڈل ہے اور انٹرپرائز کے استعمال کے لیے ڈیزائن کیا گیا ہے۔

یہ ماڈل اصل میسٹرال لارجر کی اپ گریڈ ہے جو درج ذیل خصوصیات فراہم کرتا ہے:
- بڑا کانٹیکسٹ ونڈو - 128k بمقابلہ 32k
- ریاضی اور کوڈنگ کے کاموں پر بہتر کارکردگی - 76.9% اوسط درستگی بمقابلہ 60.4%
- کثیر لسانی کارکردگی میں اضافہ - زبانیں شامل ہیں: انگریزی، فرانسیسی، جرمن، ہسپانوی، اطالوی، پرتگالی، ڈچ، روسی، چینی، جاپانی، کوریائی، عربی، اور ہندی۔

ان خصوصیات کے ساتھ، میسٹرال لارجر درج ذیل میں نمایاں ہے:
- *ریکٹرئیول اگمینٹیڈ جنریشن (RAG)* - بڑے کانٹیکسٹ ونڈو کی وجہ سے
- *فنکشن کالنگ* - اس ماڈل میں نیٹو فنکشن کالنگ ہے جو بیرونی ٹولز اور APIs کے انضمام کی اجازت دیتا ہے۔ یہ کالز متوازی یا ترتیب وار کی جا سکتی ہیں۔
- *کوڈ جنریشن* - یہ ماڈل Python، Java، TypeScript، اور C++ کی تخلیق میں مہارت رکھتا ہے۔

### میسٹرال لارجر 2 کا استعمال کرتے ہوئے RAG کی مثال

اس مثال میں، ہم میسٹرال لارجر 2 کا استعمال ایک ٹیکسٹ دستاویز پر RAG پیٹرن چلانے کے لیے کر رہے ہیں۔ سوال کوریائی زبان میں لکھا گیا ہے اور مصنف کی کالج سے پہلے کی سرگرمیوں کے بارے میں پوچھتا ہے۔

یہ کوہیر ایمبیڈنگ ماڈل استعمال کرتا ہے تاکہ ٹیکسٹ دستاویز اور سوال دونوں کی امبیڈنگ تیار کی جا سکیں۔ اس نمونے کے لیے faiss Python پیکیج کو ویکٹر اسٹور کے طور پر استعمال کیا جاتا ہے۔

میسٹرال ماڈل کو بھیجے جانے والا پرامپٹ سوالات اور بازیافت کیے گئے ایسے ٹکڑوں پر مشتمل ہوتا ہے جو سوال کے مشابہ ہوتے ہیں۔ ماڈل پھر قدرتی زبان میں جواب فراہم کرتا ہے۔

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

# انہیں اپنے مائیکروسافٹ فاؤنڈری پروجیکٹ کے "جائزہ" صفحہ سے حاصل کریں
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # فاصلہ، اشاریہ
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

## میسٹرال اسمال
میسٹرال اسمال میسٹرال فیملی کا ایک اور ماڈل ہے جو پریمیئر/انٹرپرائز زمرے میں آتا ہے۔ جیسا کہ نام سے ظاہر ہے، یہ ماڈل ایک چھوٹا زبان ماڈل (SLM) ہے۔ میسٹرال اسمال کے استعمال کے فائدے یہ ہیں کہ یہ:
- میسٹرال کے بڑے LLMs جیسے میسٹرال لارجر اور نی مو کے مقابلے میں قیمت میں بچت - 80٪ کمی
- کم تاخیر - میسٹرال LLMs کے مقابلے میں تیز تر جواب دہی
- لچکدار - مختلف ماحول میں کم وسائل کی پابندیوں کے ساتھ تعینات کیا جا سکتا ہے۔


میسٹرال اسمال کے لیے بہترین ہیں:
- متن پر مبنی کام جیسے خلاصہ سازی، جذبات کا تجزیہ اور ترجمہ۔
- ایسے اطلاقات جہاں بار بار درخواستیں کی جاتی ہیں کیونکہ یہ لاگت کے اعتبار سے مؤثر ہے
- کم تاخیر والے کوڈ کے کام جیسے کوڈ کا جائزہ اور کوڈ تجاویز

## میسٹرال اسمال اور میسٹرال لارجر کا موازنہ

میسٹرال اسمال اور لارجر کے درمیان تاخیر کے فرق کو دکھانے کے لیے، نیچے دیے گئے سیلز چلائیں۔

آپ کو ردعمل کے اوقات میں 3-5 سیکنڈ کا فرق نظر آئے گا۔ اسی پرامپٹ پر جواب کی لمبائی اور انداز پر بھی غور کریں۔

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

## میسٹرال نیمو

اس سبق میں زیر بحث دیگر دو ماڈلز کے مقابلے میں، میسٹرال نیمو واحد مفت ماڈل ہے جس کی اپاچی 2 لائسنس ہے۔

اسے میسٹرال کے پہلے اوپن سورس LLM، میسٹرال 7B کی اپ گریڈ کے طور پر دیکھا جاتا ہے۔

نیمو ماڈل کی کچھ دیگر خصوصیات یہ ہیں:

- *زیادہ مؤثر ٹوکنائزیشن:* یہ ماڈل عام طور پر استعمال ہونے والے tiktoken کے بجائے Tekken ٹوکنائزر استعمال کرتا ہے۔ اس سے زیادہ زبانوں اور کوڈ پر بہتر کارکردگی ممکن ہوتی ہے۔

- *فن ٹیوننگ:* بیس ماڈل فن ٹیوننگ کے لیے دستیاب ہے۔ اس سے ایسے استعمال کے معاملات کے لیے زیادہ لچک ملتی ہے جہاں فن ٹیوننگ کی ضرورت ہو سکتی ہے۔

- *نیٹو فنکشن کالنگ* - میسٹرال لارجر کی طرح، اس ماڈل کو فنکشن کالنگ پر تربیت دی گئی ہے۔ یہ اسے پہلی اوپن سورس ماڈلز میں سے ایک بناتا ہے جو یہ خصوصیت رکھتا ہے۔


### ٹوکنائزرز کا موازنہ

اس نمونے میں، ہم دیکھیں گے کہ میسٹرال نیمو میسٹرال لارجر کے مقابلے میں ٹوکنائزیشن کو کیسے ہینڈل کرتا ہے۔

دونوں نمونے ایک ہی پرامپٹ لیتے ہیں لیکن آپ کو نظر آئے گا کہ نیمو میسٹرال لارجر کے مقابلے میں کم ٹوکنز واپس کرتا ہے۔

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

# ٹوکنز کی تعداد گنیں
print(len(tokens))
```

```python
# ضروری پیکج درآمد کریں:
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

# ٹوکنز کی تعداد گنیں
print(len(tokens))
```

## سیکھنا یہاں ختم نہیں ہوتا، سفر جاری رکھیں

اس سبق کو مکمل کرنے کے بعد، ہمارا [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) دیکھیں تاکہ اپنے جنریٹو AI کے علم کو مزید بڑھا سکیں!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->