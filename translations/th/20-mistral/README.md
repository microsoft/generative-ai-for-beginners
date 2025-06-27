<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-06-26T03:17:39+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "th"
}
-->
# การสร้างด้วยโมเดล Mistral

## บทนำ

บทเรียนนี้จะครอบคลุม:
- สำรวจโมเดล Mistral ที่แตกต่างกัน
- เข้าใจการใช้งานและสถานการณ์สำหรับแต่ละโมเดล
- ตัวอย่างโค้ดแสดงคุณสมบัติที่เป็นเอกลักษณ์ของแต่ละโมเดล

## โมเดล Mistral

ในบทเรียนนี้ เราจะสำรวจโมเดล Mistral 3 แบบ: **Mistral Large**, **Mistral Small** และ **Mistral Nemo**

โมเดลเหล่านี้สามารถใช้งานได้ฟรีบนตลาดโมเดล Github โค้ดในโน้ตบุ๊คนี้จะใช้โมเดลเหล่านี้เพื่อรันโค้ด รายละเอียดเพิ่มเติมเกี่ยวกับการใช้โมเดล Github เพื่อ [สร้างต้นแบบด้วยโมเดล AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)

## Mistral Large 2 (2407)

Mistral Large 2 เป็นโมเดลหลักจาก Mistral ที่ออกแบบมาเพื่อการใช้งานในองค์กร

โมเดลนี้เป็นการอัปเกรดจาก Mistral Large รุ่นเดิมโดยเสนอ:
- หน้าต่างบริบทที่ใหญ่ขึ้น - 128k เทียบกับ 32k
- ประสิทธิภาพที่ดีกว่าในงานคณิตศาสตร์และการเขียนโค้ด - ความแม่นยำเฉลี่ย 76.9% เทียบกับ 60.4%
- เพิ่มประสิทธิภาพหลายภาษา - ภาษาได้แก่ อังกฤษ, ฝรั่งเศส, เยอรมัน, สเปน, อิตาลี, โปรตุเกส, ดัตช์, รัสเซีย, จีน, ญี่ปุ่น, เกาหลี, อาหรับ และ ฮินดี

ด้วยคุณสมบัติเหล่านี้ Mistral Large โดดเด่นที่:
- *Retrieval Augmented Generation (RAG)* - เนื่องจากหน้าต่างบริบทที่ใหญ่ขึ้น
- *การเรียกฟังก์ชัน* - โมเดลนี้มีการเรียกฟังก์ชันแบบเนทีฟที่อนุญาตให้รวมเข้ากับเครื่องมือและ API ภายนอก การเรียกนี้สามารถทำได้ทั้งแบบคู่ขนานหรือแบบต่อเนื่องตามลำดับ
- *การสร้างโค้ด* - โมเดลนี้โดดเด่นในการสร้าง Python, Java, TypeScript และ C++

### ตัวอย่าง RAG โดยใช้ Mistral Large 2

ในตัวอย่างนี้ เราใช้ Mistral Large 2 เพื่อรันรูปแบบ RAG บนเอกสารข้อความ คำถามเขียนเป็นภาษาเกาหลีและถามเกี่ยวกับกิจกรรมของผู้เขียนก่อนเข้าวิทยาลัย

มันใช้ Cohere Embeddings Model เพื่อสร้างการฝังของเอกสารข้อความรวมถึงคำถาม สำหรับตัวอย่างนี้ ใช้แพ็กเกจ Python faiss เป็นที่เก็บเวกเตอร์

คำถามที่ส่งไปยังโมเดล Mistral รวมถึงคำถามและชิ้นส่วนที่ดึงมาเหมือนกับคำถาม จากนั้นโมเดลให้คำตอบในภาษาธรรมชาติ

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

Mistral Small เป็นอีกหนึ่งโมเดลในตระกูลโมเดล Mistral ภายใต้หมวดหมู่หลัก/องค์กร ตามชื่อที่บอก โมเดลนี้เป็น Small Language Model (SLM) ข้อดีของการใช้ Mistral Small คือ:
- ประหยัดค่าใช้จ่ายเมื่อเทียบกับ Mistral LLMs เช่น Mistral Large และ NeMo - ลดราคาลง 80%
- ความหน่วงต่ำ - ตอบสนองได้เร็วกว่า LLMs ของ Mistral
- ยืดหยุ่น - สามารถนำไปใช้ในสภาพแวดล้อมต่างๆ ได้ด้วยข้อจำกัดทรัพยากรที่น้อยลง

Mistral Small เหมาะสำหรับ:
- งานที่ใช้ข้อความ เช่น การสรุป การวิเคราะห์ความรู้สึก และการแปล
- แอปพลิเคชันที่มีการร้องขอบ่อยๆ เนื่องจากความคุ้มค่า
- งานโค้ดที่มีความหน่วงต่ำ เช่น การตรวจสอบและข้อเสนอแนะโค้ด

## การเปรียบเทียบ Mistral Small และ Mistral Large

เพื่อแสดงความแตกต่างในความหน่วงระหว่าง Mistral Small และ Large ให้รันเซลล์ด้านล่าง

คุณควรเห็นความแตกต่างในเวลาตอบสนองระหว่าง 3-5 วินาที นอกจากนี้ยังสังเกตความยาวและรูปแบบการตอบสนองจากคำถามเดียวกัน

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

เมื่อเปรียบเทียบกับโมเดลอื่นสองแบบที่กล่าวถึงในบทเรียนนี้ Mistral NeMo เป็นโมเดลฟรีเดียวที่มีใบอนุญาต Apache2

มันถูกมองว่าเป็นการอัปเกรดจาก LLM แบบโอเพนซอร์สรุ่นก่อนของ Mistral, Mistral 7B

คุณสมบัติอื่นๆ ของโมเดล NeMo ได้แก่:

- *การจัดการโทเค็นที่มีประสิทธิภาพมากขึ้น:* โมเดลนี้ใช้ตัวจัดการโทเค็น Tekken แทนที่ tiktoken ที่ใช้กันทั่วไป ซึ่งช่วยให้มีประสิทธิภาพดีกว่าในหลายภาษาและโค้ด

- *การปรับแต่ง:* โมเดลพื้นฐานสามารถปรับแต่งได้ ซึ่งช่วยให้มีความยืดหยุ่นมากขึ้นสำหรับการใช้งานที่อาจต้องการการปรับแต่ง

- *การเรียกฟังก์ชันแบบเนทีฟ* - เช่นเดียวกับ Mistral Large โมเดลนี้ได้รับการฝึกฝนในการเรียกฟังก์ชัน ซึ่งทำให้มันเป็นหนึ่งในโมเดลโอเพนซอร์สแรกที่ทำได้

### การเปรียบเทียบตัวจัดการโทเค็น

ในตัวอย่างนี้ เราจะดูว่า Mistral NeMo จัดการโทเค็นอย่างไรเมื่อเปรียบเทียบกับ Mistral Large

ทั้งสองตัวอย่างใช้คำถามเดียวกัน แต่คุณควรเห็นว่า NeMo คืนโทเค็นน้อยกว่าเมื่อเทียบกับ Mistral Large

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

## การเรียนรู้ไม่หยุดเพียงเท่านี้, สานต่อการเดินทาง

หลังจากจบบทเรียนนี้ ลองดู [คอลเลกชันการเรียนรู้ AI สร้างสรรค์](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ของเราเพื่อสานต่อการเพิ่มพูนความรู้ AI สร้างสรรค์ของคุณ!

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้เกิดความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมืออาชีพที่เป็นมนุษย์ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้