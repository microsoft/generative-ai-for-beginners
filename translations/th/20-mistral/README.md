# การสร้างด้วยโมเดล Mistral 

## บทนำ 

บทเรียนนี้จะครอบคลุม: 
- การสำรวจโมเดล Mistral ต่างๆ 
- การทำความเข้าใจกรณีการใช้งานและสถานการณ์สำหรับแต่ละโมเดล 
- การสำรวจตัวอย่างโค้ดที่แสดงคุณสมบัติเฉพาะของแต่ละโมเดล 

## โมเดล Mistral 

ในบทเรียนนี้ เราจะสำรวจโมเดล Mistral ทั้ง 3 รุ่น ได้แก่ 
**Mistral Large**, **Mistral Small** และ **Mistral Nemo** 

โมเดลเหล่านี้ให้ใช้งานฟรีบน [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) โค้ดในโน้ตบุ๊กนี้จะใช้โมเดลเหล่านี้ในการรันโค้ด

> **หมายเหตุ:** GitHub Models จะเลิกใช้ปลายเดือนกรกฎาคม 2026 รายละเอียดเพิ่มเติมเกี่ยวกับการใช้ [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) เพื่อสร้างต้นแบบกับโมเดล AI 


## Mistral Large 2 (2407)
Mistral Large 2 เป็นโมเดลหลักปัจจุบันของ Mistral และออกแบบมาเพื่อการใช้งานในองค์กร 

โมเดลนี้เป็นการอัปเกรดจาก Mistral Large เดิมโดยมี 
-  หน้าต่างบริบทที่ใหญ่ขึ้น - 128k เทียบกับ 32k 
-  ประสิทธิภาพที่ดีขึ้นในงานคณิตศาสตร์และการเขียนโปรแกรม - ความถูกต้องเฉลี่ย 76.9% เทียบกับ 60.4% 
-  ประสิทธิภาพหลายภาษาเพิ่มขึ้น - รองรับภาษา: อังกฤษ ฝรั่งเศส เยอรมัน สเปน อิตาลี โปรตุเกส ดัตช์ รัสเซีย จีน ญี่ปุ่น เกาหลี อารบิก และฮินดี

ด้วยคุณสมบัติเหล่านี้ Mistral Large โดดเด่นในการ 
- *Retrieval Augmented Generation (RAG)* - เนื่องจากมีหน้าต่างบริบทขนาดใหญ่
- *Function Calling* - โมเดลนี้มีฟังก์ชันการเรียกใช้งานในตัวที่ช่วยให้เชื่อมต่อกับเครื่องมือและ API ภายนอกได้ การเรียกใช้เหล่านี้สามารถทำแบบขนานหรือเรียงลำดับตามลำดับได้ 
- *การสร้างโค้ด* - โมเดลนี้โดดเด่นในการสร้าง Python, Java, TypeScript และ C++ 

### ตัวอย่าง RAG โดยใช้ Mistral Large 2 

ในตัวอย่างนี้ เราใช้ Mistral Large 2 เพื่อรันรูปแบบ RAG บนเอกสารข้อความ คำถามถูกเขียนเป็นภาษาเกาหลีและถามถึงกิจกรรมของผู้เขียนก่อนเข้ามหาวิทยาลัย 

ใช้โมเดล Cohere Embeddings ในการสร้าง embeddings ของเอกสารข้อความและคำถาม สำหรับตัวอย่างนี้ใช้แพ็กเกจ faiss ของ Python เป็นแหล่งเก็บเวกเตอร์ 

ข้อความ prompt ที่ส่งไปยังโมเดล Mistral รวมทั้งคำถามและส่วนที่ดึงข้อมูลมา (chunks) ที่เหมือนกับคำถาม โมเดลจึงให้คำตอบเป็นภาษาธรรมชาติ 

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

# รับสิ่งเหล่านี้จากหน้ารวม ("Overview") ของโครงการ Microsoft Foundry ของคุณ
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


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # ระยะทาง, ดัชนี
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
Mistral Small เป็นอีกโมเดลหนึ่งในกลุ่มโมเดล Mistral ภายใต้ประเภท premier/enterprise ตามชื่อ โมเดลนี้เป็นโมเดลภาษาเล็ก (SLM) ข้อดีของการใช้ Mistral Small คือ: 
- ประหยัดค่าใช้จ่ายเมื่อเทียบกับ Mistral LLM เช่น Mistral Large และ NeMo - ลดราคาถึง 80%
- ความหน่วงต่ำ - ตอบสนองได้เร็วกว่า LLM ของ Mistral
- ยืดหยุ่น - สามารถติดตั้งได้ในสภาพแวดล้อมต่าง ๆ โดยมีข้อจำกัดน้อยในด้านทรัพยากรที่ต้องการ 


Mistral Small เหมาะสำหรับ: 
- งานที่ใช้ข้อความ เช่น การสรุป วิเคราะห์อารมณ์ และการแปลภาษา 
- แอปพลิเคชันที่มีการเรียกใช้งานบ่อยครั้งเนื่องจากค่าใช้จ่ายที่คุ้มค่า
- งานโค้ดที่ต้องการความหน่วงต่ำ เช่น การตรวจสอบและแนะนำโค้ด 

## การเปรียบเทียบ Mistral Small และ Mistral Large 

เพื่อแสดงความแตกต่างของความหน่วงระหว่าง Mistral Small และ Large ให้รันเซลล์ด้านล่าง

คุณจะเห็นความแตกต่างของเวลาตอบสนองอยู่ระหว่าง 3-5 วินาที และสังเกตความยาวและสไตล์ของการตอบสนองใน prompt เดียวกันด้วย

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

## Mistral NeMo

เมื่อเทียบกับสองโมเดลในบทเรียนนี้ Mistral NeMo เป็นโมเดลฟรีเพียงรุ่นเดียวที่มีสัญญาอนุญาต Apache2 

ถือเป็นการอัปเกรดจากโมเดล LLM แบบโอเพนซอร์สรุ่นก่อนหน้าของ Mistral คือ Mistral 7B 

คุณสมบัติอื่น ๆ ของโมเดล NeMo ได้แก่: 

- *การตัดคำที่มีประสิทธิภาพมากขึ้น:* โมเดลนี้ใช้ตัวตัดคำ Tekken แทนที่จะใช้ tiktoken ที่นิยมทั่วไป ซึ่งช่วยให้ทำงานได้ดีขึ้นกับหลายภาษาและโค้ด 

- *การปรับแต่งเพิ่มเติม:* โมเดลฐานพร้อมให้ปรับแต่ง เพิ่มความยืดหยุ่นในการใช้งานกรณีที่ต้องการการปรับแต่งเพิ่มเติม 

- *การเรียกใช้งานฟังก์ชันในตัว* - เช่นเดียวกับ Mistral Large โมเดลนี้ได้รับการฝึกฝนเรื่องการเรียกใช้งานฟังก์ชัน ทำให้เป็นหนึ่งในโมเดลโอเพนซอร์สรุ่นแรกที่ทำเช่นนี้ได้ 


### การเปรียบเทียบตัวตัดคำ 

ในตัวอย่างนี้ เราจะดูว่าการตัดคำของ Mistral NeMo เป็นอย่างไรเมื่อเทียบกับ Mistral Large 

ทั้งสองตัวอย่างใช้ prompt เดียวกัน แต่คุณจะเห็นว่า NeMo คืน token น้อยกว่า Mistral Large 

```bash
pip install mistral-common
```

```python 
# นำเข้าแพคเกจที่จำเป็น:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# โหลดตัวแบ่งคำ Mistral

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# แบ่งคำจากรายการข้อความ
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

# นับจำนวนโทเค็น
print(len(tokens))
```

```python
# นำเข้าชุดแพ็กเกจที่จำเป็น:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# โหลดตัวแปลงรหัส Mistral

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# แปลงข้อความในรายการเป็นโทเคน
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

# นับจำนวนโทเคน
print(len(tokens))
```

## การเรียนรู้ไม่ได้หยุดอยู่ที่นี่ ต่อยอดเส้นทางของคุณต่อไป

หลังจากจบบทเรียนนี้แล้ว สามารถเข้าไปดู [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) เพื่อพัฒนาความรู้ด้าน Generative AI ของคุณต่อไป!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->