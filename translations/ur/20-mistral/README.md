<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T10:51:36+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "ur"
}
-->
# مسٹرال ماڈلز کے ساتھ تعمیر کرنا

## تعارف

یہ سبق شامل کرے گا:
- مختلف مسٹرال ماڈلز کی تلاش
- ہر ماڈل کے استعمال کے کیسز اور منظرناموں کی سمجھ
- کوڈ نمونے ہر ماڈل کی منفرد خصوصیات دکھاتے ہیں۔

## مسٹرال ماڈلز

اس سبق میں، ہم 3 مختلف مسٹرال ماڈلز کی تلاش کریں گے: **مسٹرال لارج**، **مسٹرال سمال** اور **مسٹرال نیمو**۔

یہ ماڈلز مفت میں گٹ ہب ماڈل مارکیٹ پلیس پر دستیاب ہیں۔ اس نوٹ بک میں کوڈ ان ماڈلز کو استعمال کرے گا تاکہ کوڈ چلایا جا سکے۔ یہاں مزید تفصیلات ہیں کہ گٹ ہب ماڈلز کو کیسے استعمال کیا جائے [AI ماڈلز کے ساتھ پروٹوٹائپ کرنے کے لیے](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)۔

## مسٹرال لارج 2 (2407)

مسٹرال لارج 2 اس وقت مسٹرال کا اہم ماڈل ہے اور اسے انٹرپرائز استعمال کے لیے بنایا گیا ہے۔

یہ ماڈل اصل مسٹرال لارج کا اپ گریڈ ہے جس میں پیشکش کی جاتی ہے:
- بڑا کانٹیکسٹ ونڈو - 128k بمقابلہ 32k
- ریاضی اور کوڈنگ ٹاسکس پر بہتر کارکردگی - 76.9% اوسط درستگی بمقابلہ 60.4%
- بڑھتی ہوئی کثیراللسانی کارکردگی - زبانوں میں شامل ہیں: انگریزی، فرانسیسی، جرمن، ہسپانوی، اطالوی، پرتگالی، ڈچ، روسی، چینی، جاپانی، کورین، عربی، اور ہندی۔

ان خصوصیات کے ساتھ، مسٹرال لارج بہترین ہے:
- *ریٹریول اگمینٹڈ جنریشن (RAG)* - بڑے کانٹیکسٹ ونڈو کی وجہ سے
- *فنکشن کالنگ* - اس ماڈل میں مقامی فنکشن کالنگ موجود ہے جو خارجی آلات اور API کے ساتھ انٹیگریشن کی اجازت دیتا ہے۔ یہ کالز دونوں ایک ساتھ یا ایک کے بعد ایک ترتیب میں کی جا سکتی ہیں۔
- *کوڈ جنریشن* - یہ ماڈل پائتھن، جاوا، ٹائپ اسکرپٹ اور C++ جنریشن میں بہترین ہے۔

### مسٹرال لارج 2 کا RAG مثال

اس مثال میں، ہم مسٹرال لارج 2 کو استعمال کر رہے ہیں تاکہ ایک متن دستاویز پر RAG پیٹرن چلایا جا سکے۔ سوال کورین میں لکھا گیا ہے اور مصنف کی کالج سے پہلے کی سرگرمیوں کے بارے میں پوچھتا ہے۔

یہ کوہیر ایمبیڈنگ ماڈل کو استعمال کرتا ہے تاکہ متن دستاویز اور سوال کی ایمبیڈنگز بنائی جا سکیں۔ اس نمونے کے لیے، یہ فیس پائتھن پیکج کو وییکٹر اسٹور کے طور پر استعمال کرتا ہے۔

جواب میں مسٹرال ماڈل کو بھیجا گیا پرامپٹ میں سوالات اور بازیافت کردہ حصے شامل ہیں جو سوال کے مشابہ ہیں۔ ماڈل پھر قدرتی زبان میں جواب فراہم کرتا ہے۔

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

## مسٹرال سمال

مسٹرال سمال مسٹرال ماڈلز کے خاندان میں ایک اور ماڈل ہے جو پرائمئر/انٹرپرائز کیٹیگری کے تحت آتا ہے۔ جیسا کہ نام ظاہر کرتا ہے، یہ ماڈل ایک سمال لینگویج ماڈل (SLM) ہے۔ مسٹرال سمال کے استعمال کے فوائد یہ ہیں کہ یہ:
- مسٹرال LLMs جیسے مسٹرال لارج اور نیمو کے مقابلے میں لاگت کی بچت - 80% قیمت میں کمی
- کم لیٹنسی - مسٹرال کے LLMs کے مقابلے میں تیز جواب
- لچکدار - مختلف ماحول میں کم وسائل کی ضرورت کے ساتھ تعینات کیا جا سکتا ہے۔

مسٹرال سمال بہترین ہے:
- متن پر مبنی کاموں کے لیے جیسے کہ خلاصہ سازی، جذباتی تجزیہ اور ترجمہ۔
- ایسی ایپلیکیشنز جہاں اکثر درخواستیں کی جاتی ہیں اس کی لاگت کی مؤثریت کی وجہ سے
- کم لیٹنسی کوڈ کے کام جیسے جائزہ اور کوڈ تجاویز

## مسٹرال سمال اور مسٹرال لارج کا موازنہ

مسٹرال سمال اور لارج کے درمیان لیٹنسی میں فرق دکھانے کے لیے، نیچے دیے گئے سیلز چلائیں۔

آپ کو 3-5 سیکنڈ کے درمیان جواب کے وقت میں فرق نظر آنا چاہیے۔ نیز اسی پرامپٹ پر جواب کی لمبائی اور انداز پر بھی غور کریں۔

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

## مسٹرال نیمو

اس سبق میں زیر بحث دیگر دو ماڈلز کے مقابلے میں، مسٹرال نیمو واحد مفت ماڈل ہے جو اپاچی2 لائسنس کے ساتھ آتا ہے۔

یہ پہلے کے اوپن سورس LLM سے مسٹرال، مسٹرال 7B کا اپ گریڈ سمجھا جاتا ہے۔

نیمو ماڈل کی کچھ دیگر خصوصیات ہیں:

- *زیادہ موثر ٹوکنائزیشن:* یہ ماڈل زیادہ عام طور پر استعمال ہونے والے ٹکٹوکن کے مقابلے میں ٹیککن ٹوکنائزر کا استعمال کرتا ہے۔ یہ زیادہ زبانوں اور کوڈ پر بہتر کارکردگی کی اجازت دیتا ہے۔

- *فائن ٹوننگ:* بنیادی ماڈل فائن ٹوننگ کے لیے دستیاب ہے۔ یہ استعمال کے کیسز کے لیے زیادہ لچک کی اجازت دیتا ہے جہاں فائن ٹوننگ کی ضرورت ہو سکتی ہے۔

- *مقامی فنکشن کالنگ* - مسٹرال لارج کی طرح، اس ماڈل کو فنکشن کالنگ پر تربیت دی گئی ہے۔ یہ اسے ان اولین اوپن سورس ماڈلز میں سے ایک بناتا ہے جو ایسا کرتے ہیں۔

### ٹوکنائزرز کا موازنہ

اس نمونے میں، ہم دیکھیں گے کہ مسٹرال نیمو ٹوکنائزیشن کو کیسے سنبھالتا ہے مسٹرال لارج کے مقابلے میں۔

دونوں نمونے ایک ہی پرامپٹ لیتے ہیں لیکن آپ کو دیکھنا چاہیے کہ نیمو کم ٹوکن واپس کرتا ہے بمقابلہ مسٹرال لارج۔

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

## سیکھنا یہاں نہیں رکتی، سفر جاری رکھیں

اس سبق کو مکمل کرنے کے بعد، ہمارے [جنریٹو AI لرننگ کلیکشن](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) کو دیکھیں تاکہ آپ جنریٹو AI کی معلومات کو بڑھا سکیں!

**ڈس کلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشاں ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی مقامی زبان میں معتبر ماخذ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمہ کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔