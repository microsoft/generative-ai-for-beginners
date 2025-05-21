<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-05-20T10:57:46+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "th"
}
-->
# การสร้างด้วยโมเดล Mistral

## บทนำ

บทเรียนนี้จะครอบคลุมถึง:
- การสำรวจโมเดล Mistral ที่แตกต่างกัน
- การทำความเข้าใจกรณีการใช้งานและสถานการณ์สำหรับแต่ละโมเดล
- ตัวอย่างโค้ดที่แสดงคุณสมบัติเฉพาะของแต่ละโมเดล

## โมเดล Mistral

ในบทเรียนนี้ เราจะสำรวจโมเดล Mistral ที่แตกต่างกัน 3 แบบ ได้แก่ **Mistral Large**, **Mistral Small** และ **Mistral Nemo**

โมเดลเหล่านี้สามารถใช้ได้ฟรีในตลาดโมเดลของ Github โค้ดในโน้ตบุ๊กนี้จะใช้โมเดลเหล่านี้เพื่อรันโค้ด นี่คือรายละเอียดเพิ่มเติมเกี่ยวกับการใช้โมเดล Github เพื่อ [ต้นแบบด้วยโมเดล AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)

## Mistral Large 2 (2407)

Mistral Large 2 เป็นโมเดลเรือธงจาก Mistral และออกแบบมาเพื่อใช้ในองค์กร

โมเดลนี้เป็นการอัปเกรดจาก Mistral Large ดั้งเดิมโดยเสนอ:
- หน้าต่างบริบทที่ใหญ่ขึ้น - 128k เทียบกับ 32k
- ประสิทธิภาพที่ดีขึ้นในงานคณิตศาสตร์และการเขียนโค้ด - ความแม่นยำเฉลี่ย 76.9% เทียบกับ 60.4%
- เพิ่มประสิทธิภาพหลายภาษา - ภาษาที่รองรับได้แก่ อังกฤษ, ฝรั่งเศส, เยอรมัน, สเปน, อิตาลี, โปรตุเกส, ดัตช์, รัสเซีย, จีน, ญี่ปุ่น, เกาหลี, อาหรับ และ ฮินดี

ด้วยคุณสมบัติเหล่านี้ Mistral Large จึงโดดเด่นใน:
- *การสร้างเนื้อหาเสริมการดึงข้อมูล (RAG)* - เนื่องจากหน้าต่างบริบทที่ใหญ่ขึ้น
- *การเรียกใช้ฟังก์ชัน* - โมเดลนี้มีการเรียกใช้ฟังก์ชันในตัวที่ช่วยให้สามารถผสานรวมกับเครื่องมือและ API ภายนอกได้ การเรียกใช้สามารถทำได้ทั้งแบบขนานหรือแบบต่อเนื่อง
- *การสร้างโค้ด* - โมเดลนี้โดดเด่นในการสร้าง Python, Java, TypeScript และ C++

### ตัวอย่าง RAG โดยใช้ Mistral Large 2

ในตัวอย่างนี้ เราใช้ Mistral Large 2 เพื่อรันรูปแบบ RAG บนเอกสารข้อความ คำถามเขียนเป็นภาษาเกาหลีและถามเกี่ยวกับกิจกรรมของผู้เขียนก่อนเข้าเรียนมหาวิทยาลัย

มันใช้ Cohere Embeddings Model เพื่อสร้างการฝังของเอกสารข้อความรวมถึงคำถาม สำหรับตัวอย่างนี้ใช้แพ็กเกจ Python faiss เป็นแหล่งเก็บเวกเตอร์

พรอมต์ที่ส่งไปยังโมเดล Mistral รวมถึงทั้งคำถามและส่วนที่ดึงมาที่คล้ายกับคำถาม จากนั้นโมเดลจะให้คำตอบในภาษาธรรมชาติ

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

Mistral Small เป็นอีกโมเดลหนึ่งในตระกูลโมเดล Mistral ภายใต้หมวดหมู่พรีเมียม/องค์กร ตามชื่อที่แสดง โมเดลนี้เป็นโมเดลภาษาขนาดเล็ก (SLM) ข้อดีของการใช้ Mistral Small คือ:
- ประหยัดต้นทุนเมื่อเทียบกับ Mistral LLMs เช่น Mistral Large และ NeMo - ลดราคาลง 80%
- ความหน่วงต่ำ - ตอบสนองเร็วกว่า LLMs ของ Mistral
- ยืดหยุ่น - สามารถใช้งานในสภาพแวดล้อมต่าง ๆ ด้วยข้อจำกัดของทรัพยากรที่น้อยลง

Mistral Small เหมาะสำหรับ:
- งานที่ใช้ข้อความเช่นการสรุป, การวิเคราะห์ความรู้สึก และการแปล
- แอปพลิเคชันที่มีการร้องขอบ่อยเนื่องจากมีความคุ้มค่า
- งานโค้ดที่มีความหน่วงต่ำ เช่น การตรวจสอบและข้อเสนอแนะโค้ด

## การเปรียบเทียบ Mistral Small และ Mistral Large

เพื่อแสดงความแตกต่างในความหน่วงระหว่าง Mistral Small และ Large ให้รันเซลล์ด้านล่าง

คุณควรเห็นความแตกต่างในเวลาตอบสนองระหว่าง 3-5 วินาที นอกจากนี้ให้สังเกตความยาวและสไตล์ของคำตอบในพรอมต์เดียวกัน

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

เมื่อเปรียบเทียบกับโมเดลอีกสองแบบที่กล่าวถึงในบทเรียนนี้ Mistral NeMo เป็นโมเดลเดียวที่มีใบอนุญาต Apache2 ฟรี

มันถูกมองว่าเป็นการอัปเกรดจาก LLM แบบโอเพนซอร์สดั้งเดิมจาก Mistral, Mistral 7B

คุณสมบัติอื่น ๆ ของโมเดล NeMo ได้แก่:

- *การโทเคนที่มีประสิทธิภาพมากขึ้น:* โมเดลนี้ใช้ตัวโทเคน Tekken แทนที่จะเป็น tiktoken ที่ใช้กันทั่วไป สิ่งนี้ช่วยให้มีประสิทธิภาพที่ดีขึ้นในหลายภาษาและโค้ด

- *การปรับแต่ง:* โมเดลพื้นฐานพร้อมสำหรับการปรับแต่ง สิ่งนี้ช่วยให้มีความยืดหยุ่นมากขึ้นสำหรับกรณีการใช้งานที่อาจต้องการการปรับแต่ง

- *การเรียกใช้ฟังก์ชันในตัว* - เช่นเดียวกับ Mistral Large โมเดลนี้ได้รับการฝึกฝนในด้านการเรียกใช้ฟังก์ชัน สิ่งนี้ทำให้มันโดดเด่นเป็นหนึ่งในโมเดลโอเพนซอร์สตัวแรกที่ทำเช่นนั้น

### การเปรียบเทียบตัวโทเคน

ในตัวอย่างนี้ เราจะดูว่า Mistral NeMo จัดการกับการโทเคนเมื่อเปรียบเทียบกับ Mistral Large อย่างไร

ทั้งสองตัวอย่างใช้พรอมต์เดียวกัน แต่คุณควรเห็นว่า NeMo ส่งคืนโทเคนน้อยกว่าเมื่อเทียบกับ Mistral Large

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

## การเรียนรู้ไม่ได้หยุดอยู่ที่นี่ ดำเนินการต่อไป

หลังจากจบบทเรียนนี้แล้ว ให้ตรวจสอบ [คอลเลกชันการเรียนรู้ Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ของเราเพื่อพัฒนาความรู้ด้าน Generative AI ของคุณให้ก้าวหน้าต่อไป!

**คำปฏิเสธความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้มีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่แม่นยำ เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาว่าเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้บริการแปลภาษามนุษย์มืออาชีพ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้