<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T18:56:21+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "ur"
}
-->
# Mistral ماڈلز کے ساتھ تعمیر

## تعارف

اس سبق میں شامل ہے:  
- مختلف Mistral ماڈلز کی دریافت  
- ہر ماڈل کے استعمال کے کیسز اور حالات کو سمجھنا  
- کوڈ کے نمونے جو ہر ماڈل کی منفرد خصوصیات دکھاتے ہیں۔

## Mistral ماڈلز

اس سبق میں، ہم 3 مختلف Mistral ماڈلز کا جائزہ لیں گے:  
**Mistral Large**, **Mistral Small** اور **Mistral Nemo**۔

یہ تمام ماڈلز Github Model مارکیٹ پلیس پر مفت دستیاب ہیں۔ اس نوٹ بک میں کوڈ چلانے کے لیے انہی ماڈلز کا استعمال کیا جائے گا۔ Github Models کو AI ماڈلز کے ساتھ [prototype کرنے](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) کے بارے میں مزید تفصیلات یہاں دستیاب ہیں۔

## Mistral Large 2 (2407)  
Mistral Large 2 اس وقت Mistral کا فلیگ شپ ماڈل ہے اور انٹرپرائز استعمال کے لیے ڈیزائن کیا گیا ہے۔

یہ ماڈل اصل Mistral Large کا اپ گریڈ ہے جو درج ذیل خصوصیات پیش کرتا ہے:  
- بڑا کانٹیکسٹ ونڈو - 128k بمقابلہ 32k  
- ریاضی اور کوڈنگ کے کاموں میں بہتر کارکردگی - اوسط درستگی 76.9% بمقابلہ 60.4%  
- کثیر لسانی کارکردگی میں اضافہ - زبانوں میں شامل ہیں: انگریزی، فرانسیسی، جرمن، ہسپانوی، اطالوی، پرتگالی، ڈچ، روسی، چینی، جاپانی، کوریائی، عربی، اور ہندی۔

ان خصوصیات کے ساتھ، Mistral Large درج ذیل میں بہترین ہے:  
- *Retrieval Augmented Generation (RAG)* - بڑے کانٹیکسٹ ونڈو کی وجہ سے  
- *Function Calling* - اس ماڈل میں نیٹیو فنکشن کالنگ ہے جو بیرونی ٹولز اور APIs کے ساتھ انٹیگریشن کی اجازت دیتی ہے۔ یہ کالز متوازی یا ترتیب وار کی جا سکتی ہیں۔  
- *Code Generation* - یہ ماڈل Python, Java, TypeScript اور C++ کی جنریشن میں مہارت رکھتا ہے۔

### Mistral Large 2 کے ساتھ RAG کی مثال

اس مثال میں، ہم Mistral Large 2 کا استعمال کرتے ہوئے ایک RAG پیٹرن کو ایک ٹیکسٹ دستاویز پر چلا رہے ہیں۔ سوال کوریائی زبان میں لکھا گیا ہے اور مصنف کی کالج سے پہلے کی سرگرمیوں کے بارے میں پوچھتا ہے۔

یہ Cohere Embeddings Model کا استعمال کرتے ہوئے ٹیکسٹ دستاویز اور سوال دونوں کی ایمبیڈنگز بناتا ہے۔ اس نمونے میں faiss Python پیکیج کو ویکٹر اسٹور کے طور پر استعمال کیا گیا ہے۔

Mistral ماڈل کو بھیجا گیا پرامپٹ سوالات اور ان چنکس دونوں پر مشتمل ہوتا ہے جو سوال سے مشابہت رکھتے ہیں۔ ماڈل پھر قدرتی زبان میں جواب فراہم کرتا ہے۔

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
Mistral Small Mistral فیملی کا ایک اور ماڈل ہے جو پریمیئر/انٹرپرائز کیٹیگری میں آتا ہے۔ جیسا کہ نام سے ظاہر ہے، یہ ایک Small Language Model (SLM) ہے۔ Mistral Small کے استعمال کے فوائد یہ ہیں:  
- Mistral LLMs جیسے Mistral Large اور NeMo کے مقابلے میں لاگت میں بچت - 80% قیمت میں کمی  
- کم تاخیر - Mistral کے LLMs کے مقابلے میں تیز تر جواب  
- لچکدار - مختلف ماحول میں کم وسائل کی پابندیوں کے ساتھ تعینات کیا جا سکتا ہے۔

Mistral Small بہترین ہے:  
- متن پر مبنی کاموں کے لیے جیسے خلاصہ سازی، جذباتی تجزیہ اور ترجمہ  
- ایسی ایپلیکیشنز جہاں بار بار درخواستیں کی جاتی ہیں کیونکہ یہ لاگت کے لحاظ سے مؤثر ہے  
- کم تاخیر والے کوڈ کے کام جیسے جائزہ اور کوڈ کی تجاویز

## Mistral Small اور Mistral Large کا موازنہ

Mistral Small اور Large کے درمیان تاخیر کے فرق کو دکھانے کے لیے نیچے دیے گئے سیلز چلائیں۔

آپ کو 3-5 سیکنڈ کے درمیان جواب کے وقت میں فرق نظر آئے گا۔ اسی پرامپٹ پر جواب کی لمبائی اور انداز پر بھی غور کریں۔

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

اس سبق میں زیر بحث دیگر دو ماڈلز کے مقابلے میں، Mistral NeMo واحد مفت ماڈل ہے جس کے ساتھ Apache2 لائسنس ہے۔

یہ Mistral کے پہلے اوپن سورس LLM، Mistral 7B، کا اپ گریڈ سمجھا جاتا ہے۔

NeMo ماڈل کی کچھ دیگر خصوصیات یہ ہیں:

- *زیادہ مؤثر ٹوکنائزیشن:* یہ ماڈل Tekken tokenizer استعمال کرتا ہے جو عام طور پر استعمال ہونے والے tiktoken سے بہتر کارکردگی دیتا ہے۔ اس سے زیادہ زبانوں اور کوڈ پر بہتر کارکردگی ممکن ہوتی ہے۔

- *Finetuning:* بیس ماڈل فائن ٹیوننگ کے لیے دستیاب ہے۔ یہ ان استعمال کے کیسز کے لیے زیادہ لچک فراہم کرتا ہے جہاں فائن ٹیوننگ کی ضرورت ہو۔

- *نیٹیو فنکشن کالنگ* - Mistral Large کی طرح، اس ماڈل کو فنکشن کالنگ پر تربیت دی گئی ہے۔ یہ اسے پہلے اوپن سورس ماڈلز میں سے ایک بناتا ہے جو یہ خصوصیت رکھتے ہیں۔

### ٹوکنائزروں کا موازنہ

اس نمونے میں، ہم دیکھیں گے کہ Mistral NeMo ٹوکنائزیشن کو Mistral Large کے مقابلے میں کیسے ہینڈل کرتا ہے۔

دونوں نمونے ایک ہی پرامپٹ لیتے ہیں لیکن آپ دیکھیں گے کہ NeMo کم ٹوکنز واپس کرتا ہے بمقابلہ Mistral Large۔

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

## سیکھنا یہاں ختم نہیں ہوتا، سفر جاری رکھیں

اس سبق کو مکمل کرنے کے بعد، ہمارے [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) کو دیکھیں تاکہ آپ اپنی Generative AI کی معلومات کو مزید بڑھا سکیں!

**دستخطی دستبرداری**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔