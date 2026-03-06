# میسٹریل ماڈلز کے ساتھ تعمیر

## تعارف

یہ سبق درج ذیل موضوعات کا احاطہ کرے گا:
- مختلف میسٹریل ماڈلز کی تلاش
- ہر ماڈل کے استعمال کے حالات اور مواقع کو سمجھنا
- کوڈ کے نمونے جو ہر ماڈل کی منفرد خصوصیات کو ظاہر کرتے ہیں۔

## میسٹریل ماڈلز

اس سبق میں، ہم 3 مختلف میسٹریل ماڈلز کا جائزہ لیں گے:
**Mistral Large**, **Mistral Small** اور **Mistral Nemo**۔

ان میں سے ہر ماڈل GitHub ماڈل مارکیٹ پلیس پر مفت دستیاب ہے۔ اس نوٹ بک میں کوڈ چلانے کے لیے ہم انہی ماڈلز کا استعمال کریں گے۔ GitHub ماڈلز کو AI ماڈلز کے ساتھ [پروٹوٹائپ بنانے](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) کے حوالے سے مزید تفصیلات یہ ہیں۔


## میسٹریل لارجر 2 (2407)
Mistral Large 2 اس وقت میسٹریل کا فلیگ شپ ماڈل ہے اور اسے ادارہ جاتی استعمال کے لیے ڈیزائن کیا گیا ہے۔

یہ ماڈل اصل Mistral Large کا اپ گریڈ ہے جو درج ذیل خصوصیات پیش کرتا ہے:
- بڑا کانٹیکسٹ ونڈو - 128k بمقابلہ 32k
- ریاضی اور کوڈنگ کے کاموں میں بہتر کارکردگی - اوسط درستگی 76.9% بمقابلہ 60.4%
- متعدد زبانوں میں بہتر کارکردگی - زبانوں میں شامل ہیں: انگریزی، فرانسیسی، جرمن، ہسپانوی، اطالوی، پرتگالی، ڈچ، روسی، چینی، جاپانی، کوریائی، عربی، اور ہندی۔

ان خصوصیات کے ساتھ، Mistral Large درج ذیل میں نمایاں ہے:
- *Retrieval Augmented Generation (RAG)* - بڑے کانٹیکسٹ ونڈو کی وجہ سے
- *Function Calling* - اس ماڈل میں نیٹو فنکشن کالنگ شامل ہے جو خارجی ٹولز اور APIs کے ساتھ انضمام کی اجازت دیتا ہے۔ یہ کالز متوازی یا متتالی ترتیب میں کی جا سکتی ہیں۔
- *Code Generation* - یہ ماڈل Python, Java, TypeScript اور C++ کوڈ کی تخلیق میں بہترین ہے۔

### Mistral Large 2 کا استعمال کرتے ہوئے RAG کی مثال

اس مثال میں، ہم Mistral Large 2 استعمال کر رہے ہیں تاکہ کسی ٹیکسٹ دستاویز پر RAG پیٹرن چلایا جا سکے۔ سوال کوریائی زبان میں لکھا گیا ہے اور مصنف کی کالج سے پہلے کی سرگرمیوں کے بارے میں پوچھتا ہے۔

یہ Cohere Embeddings ماڈل کا استعمال کر کے ٹیکسٹ دستاویز اور سوال دونوں کی embeddings بناتا ہے۔ اس نمونے کے لیے، یہ faiss Python پیکیج کو ویکٹر اسٹور کے طور پر استعمال کرتا ہے۔

Mistral ماڈل کو بھیجا گیا پرامپٹ سوالات اور وہ بازیافت شدہ جُز جن کا سوال سے مماثلت ہے، دونوں شامل کرتا ہے۔ ماڈل پھر ایک قدرتی زبان میں جواب فراہم کرتا ہے۔

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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # فاصلہ، انڈیکس
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


## میسٹریل اسمال
Mistral Small میسٹریل کے خاندان کا ایک اور ماڈل ہے جو پریمیئر/انٹرپرائز زمرے میں آتا ہے۔ جیسا کہ نام سے ظاہر ہے، یہ ایک چھوٹا لینگویج ماڈل (SLM) ہے۔ Mistral Small استعمال کرنے کے فوائد یہ ہیں:
- Mistral LLMs جیسے Mistral Large اور NeMo کے مقابلے میں لاگت میں بچت - 80% قیمت میں کمی
- کم تاخیر - Mistral کے بڑے ماڈلز کے مقابلے میں تیز تر ردعمل
- لچکدار - مختلف ماحول میں کم وسائل کی ضروریات کے ساتھ تعینات کیا جا سکتا ہے۔

Mistral Small بہترین ہے:
- متن پر مبنی کاموں کے لیے جیسے خلاصہ سازی، جذباتی تجزیہ، اور ترجمہ۔
- ایسی ایپلیکیشنز جہاں بار بار درخواستیں کی جاتی ہیں کیونکہ یہ لاگت کی بچت پیش کرتا ہے
- کم تاخیر والے کوڈ کے کام جیسے جائزہ اور کوڈ مشورے

## Mistral Small اور Mistral Large کا موازنہ

Mistral Small اور Mistral Large کے درمیان تاخیر کے فرق کو دکھانے کے لیے، نیچے دیے گئے سیلز چلائیں۔

آپ کو جواب دینے کے اوقات میں 3-5 سیکنڈ کے فرق نظر آنا چاہیے۔ اسی پرامپٹ پر جوابی لمبائی اور انداز کا بھی موازنہ کریں۔

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


## میسٹریل نی مو

اس سبق میں بیان کردہ دیگر دو ماڈلز کے مقابلے میں، Mistral NeMo وہ اکلوتا مفت ماڈل ہے جس کا لائسنس Apache2 ہے۔

اسے Mistral کے شروع کے اوپن سورس LLM، Mistral 7B، کا اپ گریڈ سمجھا جاتا ہے۔

NeMo ماڈل کی کچھ دیگر خصوصیات یہ ہیں:

- *زیادہ موثر ٹوکنائزیشن:* یہ ماڈل Tekken tokenizer استعمال کرتا ہے جو عام طور پر استعمال ہونے والے tiktoken کے مقابلے میں ہے۔ یہ زیادہ زبانوں اور کوڈ پر بہتر کارکردگی ممکن بناتا ہے۔

- *فائن ٹیوننگ:* بنیادی ماڈل فائن ٹیوننگ کے لیے دستیاب ہے۔ یہ ان مواقع کے لیے زیادہ لچک فراہم کرتا ہے جہاں فائن ٹیوننگ کی ضرورت ہوتی ہے۔

- *نیٹو فنکشن کالنگ* - Mistral Large کی طرح، اس ماڈل کو فنکشن کالنگ پر تربیت دی گئی ہے۔ یہ اسے ان اوپن سورس ماڈلز میں سے منفرد بناتا ہے جو یہ خصوصیت رکھتے ہیں۔

### ٹوکنائزرز کا موازنہ

اس نمونے میں، ہم دیکھیں گے کہ Mistral NeMo، Mistral Large کے مقابلے میں ٹوکنائزیشن کیسے ہینڈل کرتا ہے۔

دونوں نمونے ایک ہی پرامپٹ لیتے ہیں لیکن آپ دیکھیں گے کہ NeMo کم ٹوکنز واپس کرتا ہے بنسبت Mistral Large کے۔

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
# درکار پیکیجز درآمد کریں:
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

# ٹوکنز کی تعداد شمار کریں
print(len(tokens))
```


## سیکھنا یہاں ختم نہیں ہوتا، سفر جاری رکھیں

اس سبق کو مکمل کرنے کے بعد، ہماری [Generative AI سیکھنے کی کلیکشن](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) دیکھیں تاکہ آپ کی Generative AI کی معلومات کو مزید ترقی دی جا سکے!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**اعلانِ ذمہ داری**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا نقصانات موجود ہوسکتے ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسان ترجمہ تجویز کیا جاتا ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->