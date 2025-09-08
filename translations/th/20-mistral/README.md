<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T19:00:18+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "th"
}
-->
# การสร้างด้วย Mistral Models

## บทนำ

บทเรียนนี้จะครอบคลุม:  
- การสำรวจ Mistral Models ที่แตกต่างกัน  
- การเข้าใจกรณีการใช้งานและสถานการณ์สำหรับแต่ละโมเดล  
- ตัวอย่างโค้ดที่แสดงคุณสมบัติเฉพาะของแต่ละโมเดล  

## Mistral Models

ในบทเรียนนี้ เราจะสำรวจ 3 โมเดล Mistral ที่แตกต่างกัน:  
**Mistral Large**, **Mistral Small** และ **Mistral Nemo**

โมเดลเหล่านี้ทั้งหมดสามารถใช้งานได้ฟรีบน Github Model marketplace โค้ดในโน้ตบุ๊กนี้จะใช้โมเดลเหล่านี้ในการรันโค้ด รายละเอียดเพิ่มเติมเกี่ยวกับการใช้ Github Models เพื่อ [สร้างต้นแบบด้วย AI models](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)

## Mistral Large 2 (2407)  
Mistral Large 2 เป็นโมเดลเรือธงจาก Mistral ที่ออกแบบมาเพื่อการใช้งานในองค์กร

โมเดลนี้เป็นการอัปเกรดจาก Mistral Large รุ่นแรก โดยมี  
- ขนาดหน้าต่างบริบทที่ใหญ่ขึ้น - 128k เทียบกับ 32k  
- ประสิทธิภาพที่ดีขึ้นในงานคณิตศาสตร์และการเขียนโค้ด - ความแม่นยำเฉลี่ย 76.9% เทียบกับ 60.4%  
- ประสิทธิภาพหลายภาษาเพิ่มขึ้น - รองรับภาษาอังกฤษ ฝรั่งเศส เยอรมัน สเปน อิตาลี โปรตุเกส ดัตช์ รัสเซีย จีน ญี่ปุ่น เกาหลี อาหรับ และฮินดี

ด้วยคุณสมบัติเหล่านี้ Mistral Large โดดเด่นในด้าน  
- *Retrieval Augmented Generation (RAG)* - เนื่องจากมีหน้าต่างบริบทที่ใหญ่ขึ้น  
- *Function Calling* - โมเดลนี้รองรับการเรียกฟังก์ชันโดยตรง ทำให้สามารถเชื่อมต่อกับเครื่องมือและ API ภายนอกได้ การเรียกฟังก์ชันสามารถทำได้ทั้งแบบขนานหรือเรียงลำดับทีละคำสั่ง  
- *Code Generation* - โมเดลนี้โดดเด่นในการสร้างโค้ด Python, Java, TypeScript และ C++

### ตัวอย่าง RAG โดยใช้ Mistral Large 2

ในตัวอย่างนี้ เราใช้ Mistral Large 2 เพื่อรันรูปแบบ RAG บนเอกสารข้อความ คำถามถูกเขียนเป็นภาษาเกาหลีและถามเกี่ยวกับกิจกรรมของผู้เขียนก่อนเข้ามหาวิทยาลัย

โมเดลใช้ Cohere Embeddings Model เพื่อสร้าง embeddings ของเอกสารและคำถาม สำหรับตัวอย่างนี้ใช้แพ็กเกจ faiss ของ Python เป็นที่เก็บเวกเตอร์

คำสั่งที่ส่งไปยังโมเดล Mistral รวมทั้งคำถามและส่วนที่ถูกดึงมา (retrieved chunks) ที่มีความคล้ายคลึงกับคำถาม โมเดลจึงให้คำตอบในรูปแบบภาษาธรรมชาติ

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
Mistral Small เป็นอีกหนึ่งโมเดลในตระกูล Mistral ที่อยู่ในกลุ่ม premier/enterprise ตามชื่อ โมเดลนี้เป็น Small Language Model (SLM) ข้อดีของการใช้ Mistral Small คือ  
- ประหยัดค่าใช้จ่ายเมื่อเทียบกับ Mistral LLMs เช่น Mistral Large และ NeMo - ลดราคาลง 80%  
- ความหน่วงต่ำ - ตอบสนองได้เร็วกว่า LLMs ของ Mistral  
- ยืดหยุ่น - สามารถติดตั้งในสภาพแวดล้อมต่าง ๆ ได้ง่ายขึ้นโดยมีข้อจำกัดด้านทรัพยากรน้อยกว่า

Mistral Small เหมาะสำหรับ:  
- งานที่ใช้ข้อความ เช่น การสรุปความ วิเคราะห์ความรู้สึก และการแปลภาษา  
- แอปพลิเคชันที่มีการร้องขอบ่อย ๆ เนื่องจากประหยัดค่าใช้จ่าย  
- งานโค้ดที่ต้องการความหน่วงต่ำ เช่น การตรวจสอบและแนะนำโค้ด

## การเปรียบเทียบ Mistral Small และ Mistral Large

เพื่อแสดงความแตกต่างของความหน่วงระหว่าง Mistral Small และ Large ให้รันเซลล์ด้านล่าง

คุณจะเห็นความแตกต่างของเวลาตอบสนองประมาณ 3-5 วินาที และสังเกตความยาวและสไตล์ของคำตอบจากคำสั่งเดียวกัน

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

เมื่อเทียบกับสองโมเดลที่กล่าวถึงในบทเรียนนี้ Mistral NeMo เป็นโมเดลเดียวที่ฟรีและมีใบอนุญาต Apache2

โมเดลนี้ถือเป็นการอัปเกรดจาก LLM โอเพนซอร์สรุ่นก่อนของ Mistral คือ Mistral 7B

คุณสมบัติอื่น ๆ ของโมเดล NeMo ได้แก่

- *การตัดคำที่มีประสิทธิภาพมากขึ้น:* โมเดลนี้ใช้ Tekken tokenizer แทน tiktoken ที่ใช้กันทั่วไป ซึ่งช่วยให้ทำงานได้ดีขึ้นกับหลายภาษาและโค้ด

- *การปรับแต่งเพิ่มเติม (Finetuning):* โมเดลฐานพร้อมให้ปรับแต่งเพิ่มเติมได้ ซึ่งเพิ่มความยืดหยุ่นสำหรับกรณีการใช้งานที่ต้องการการปรับแต่ง

- *Native Function Calling* - เช่นเดียวกับ Mistral Large โมเดลนี้ได้รับการฝึกฝนให้รองรับการเรียกฟังก์ชันโดยตรง ซึ่งทำให้เป็นหนึ่งในโมเดลโอเพนซอร์สรุ่นแรกที่มีฟีเจอร์นี้

### การเปรียบเทียบ Tokenizers

ในตัวอย่างนี้ เราจะดูว่า Mistral NeMo จัดการการตัดคำอย่างไรเมื่อเทียบกับ Mistral Large

ตัวอย่างทั้งสองใช้คำสั่งเดียวกัน แต่คุณจะเห็นว่า NeMo คืน token น้อยกว่า Mistral Large

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

## การเรียนรู้ไม่ได้หยุดเพียงเท่านี้ ต่อเนื่องการเดินทางของคุณ

หลังจากจบบทเรียนนี้แล้ว ลองดู [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) เพื่อพัฒนาความรู้ด้าน Generative AI ของคุณให้ก้าวหน้าต่อไป!

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้