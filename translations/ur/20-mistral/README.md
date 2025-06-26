<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-06-26T03:11:51+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "ur"
}
-->
# Mistral ماڈلز کے ساتھ تعمیر

## تعارف

اس سبق میں شامل ہوگا:
- مختلف Mistral ماڈلز کا جائزہ لینا
- ہر ماڈل کے استعمال کے کیسز اور منظرنامے کو سمجھنا
- کوڈ کے نمونے جو ہر ماڈل کی منفرد خصوصیات دکھاتے ہیں۔

## Mistral ماڈلز

اس سبق میں، ہم 3 مختلف Mistral ماڈلز کا جائزہ لیں گے:
**Mistral Large**, **Mistral Small** اور **Mistral Nemo**۔

ان میں سے ہر ماڈل Github Model مارکیٹ پلیس پر مفت دستیاب ہیں۔ اس نوٹ بک میں کوڈ چلانے کے لئے ان ماڈلز کا استعمال کیا جائے گا۔ یہاں Github Models کا استعمال کرتے ہوئے [AI ماڈلز کے ساتھ پروٹوٹائپ بنانے](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) کے بارے میں مزید تفصیلات ہیں۔

## Mistral Large 2 (2407)
Mistral Large 2 اس وقت Mistral کا فلیگ شپ ماڈل ہے اور اسے انٹرپرائز استعمال کے لئے ڈیزائن کیا گیا ہے۔

یہ ماڈل اصل Mistral Large کا اپگریڈ ہے جو پیش کرتا ہے:
- بڑا کانٹیکسٹ ونڈو - 128k بمقابلہ 32k
- میتھ اور کوڈنگ ٹاسکس پر بہتر کارکردگی - 76.9% اوسط درستگی بمقابلہ 60.4%
- بڑھتی ہوئی کثیر اللسانی کارکردگی - زبانیں شامل ہیں: انگریزی، فرانسیسی، جرمن، ہسپانوی، اطالوی، پرتگالی، ڈچ، روسی، چینی، جاپانی، کورین، عربی، اور ہندی۔

ان خصوصیات کے ساتھ، Mistral Large ممتاز ہے:
- *ریٹریول آگمینٹڈ جنریشن (RAG)* - بڑے کانٹیکسٹ ونڈو کی وجہ سے
- *فنکشن کالنگ* - اس ماڈل میں مقامی فنکشن کالنگ ہے جو بیرونی ٹولز اور APIs کے ساتھ انضمام کی اجازت دیتی ہے۔ یہ کالز دونوں متوازی یا ترتیب وار انداز میں کی جا سکتی ہیں۔
- *کوڈ جنریشن* - یہ ماڈل Python، Java، TypeScript اور C++ جنریشن میں ممتاز ہے۔

### Mistral Large 2 کا RAG مثال

اس مثال میں، ہم Mistral Large 2 کا استعمال کرتے ہوئے ایک ٹیکسٹ دستاویز پر RAG پیٹرن چلا رہے ہیں۔ سوال کورین میں لکھا گیا ہے اور کالج سے پہلے مصنف کی سرگرمیوں کے بارے میں پوچھتا ہے۔

یہ ٹیکسٹ دستاویز اور سوال کے ایمبیڈنگز بنانے کے لئے Cohere Embeddings Model کا استعمال کرتا ہے۔ اس نمونے کے لئے، یہ faiss Python پیکج کو بطور ویکٹر اسٹور استعمال کرتا ہے۔

Mistral ماڈل کو بھیجا گیا پرامپٹ سوالات اور بازیافت شدہ چنکس شامل کرتا ہے جو سوال سے ملتے جلتے ہیں۔ پھر ماڈل قدرتی زبان میں جواب فراہم کرتا ہے۔

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
Mistral Small Mistral خاندان کے ماڈلز میں سے ایک اور ماڈل ہے جو premier/enterprise زمرے میں شامل ہے۔ جیسا کہ نام سے ظاہر ہے، یہ ماڈل ایک چھوٹا لینگویج ماڈل (SLM) ہے۔ Mistral Small کے استعمال کے فوائد ہیں کہ یہ:
- Mistral LLMs جیسے Mistral Large اور NeMo کے مقابلے میں لاگت کی بچت - 80% قیمت میں کمی
- کم تاخیر - Mistral کے LLMs کے مقابلے میں تیز ردعمل
- لچکدار - مختلف ماحول میں کم وسائل کی پابندیوں کے ساتھ تعینات کیا جا سکتا ہے۔

Mistral Small بہترین ہے:
- متن پر مبنی کاموں کے لئے جیسے خلاصہ، جذباتی تجزیہ اور ترجمہ۔
- ان ایپلیکیشنز کے لئے جہاں بار بار درخواستیں کی جاتی ہیں اس کی لاگت کی افادیت کی وجہ سے
- کم تاخیر والے کوڈ کاموں جیسے جائزہ اور کوڈ تجاویز

## Mistral Small اور Mistral Large کا موازنہ

Mistral Small اور Large کے درمیان تاخیر کے فرق کو دکھانے کے لئے، نیچے دیے گئے سیلز چلائیں۔

آپ کو ردعمل کے وقت میں 3-5 سیکنڈ کا فرق نظر آنا چاہئے۔ اسی پرامپٹ پر ردعمل کی لمبائی اور انداز پر بھی توجہ دیں۔

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

اس سبق میں زیر بحث دیگر دو ماڈلز کے مقابلے میں، Mistral NeMo واحد مفت ماڈل ہے جس کے پاس Apache2 لائسنس ہے۔

یہ پہلے کے اوپن سورس LLM Mistral 7B کا اپگریڈ سمجھا جاتا ہے۔

NeMo ماڈل کی کچھ دیگر خصوصیات ہیں:

- *زیادہ موثر ٹوکنائزیشن:* یہ ماڈل زیادہ عام استعمال ہونے والے tiktoken کی بجائے Tekken ٹوکنائزر استعمال کرتا ہے۔ یہ زیادہ زبانوں اور کوڈ پر بہتر کارکردگی کی اجازت دیتا ہے۔

- *فائن ٹوننگ:* بنیادی ماڈل فائن ٹوننگ کے لئے دستیاب ہے۔ یہ ان استعمال کے کیسز کے لئے زیادہ لچک کی اجازت دیتا ہے جہاں فائن ٹوننگ کی ضرورت ہو سکتی ہے۔

- *مقامی فنکشن کالنگ* - Mistral Large کی طرح، اس ماڈل کو فنکشن کالنگ پر تربیت دی گئی ہے۔ یہ اسے ایسا منفرد بناتا ہے جیسے کہ یہ اوپن سورس ماڈلز میں سے ایک پہلا ہو۔

### ٹوکنائزرز کا موازنہ

اس نمونے میں، ہم دیکھیں گے کہ Mistral NeMo ٹوکنائزیشن کو Mistral Large کے مقابلے میں کیسے سنبھالتا ہے۔

دونوں نمونے ایک ہی پرامپٹ لیتے ہیں لیکن آپ کو دیکھنا چاہئے کہ NeMo Mistral Large کے مقابلے میں کم ٹوکن واپس کرتا ہے۔

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

اس سبق کو مکمل کرنے کے بعد، ہمارے [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) کو دیکھیں تاکہ آپ اپنی Generative AI معلومات کو مزید بڑھا سکیں!

**ڈس کلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لئے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی مقامی زبان میں مستند ذریعہ سمجھا جانا چاہئے۔ اہم معلومات کے لئے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمہ کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔