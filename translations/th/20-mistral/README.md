# การสร้างด้วยโมเดล Mistral 

## บทนำ 

บทเรียนนี้จะครอบคลุม: 
- การสำรวจโมเดล Mistral ต่าง ๆ 
- ความเข้าใจเกี่ยวกับกรณีการใช้งานและสถานการณ์สำหรับแต่ละโมเดล 
- การสำรวจตัวอย่างโค้ดที่แสดงฟีเจอร์เฉพาะของแต่ละโมเดล 

## โมเดล Mistral 

ในบทเรียนนี้ เราจะสำรวจโมเดล Mistral 3 รุ่นที่แตกต่างกัน: 
**Mistral Large**, **Mistral Small** และ **Mistral Nemo** 

โมเดลแต่ละตัวนี้สามารถใช้งานได้ฟรีบน [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) โค้ดในโน้ตบุ๊คนี้จะใช้โมเดลเหล่านี้ในการรันโค้ด

> **หมายเหตุ:** GitHub Models จะหยุดให้บริการในสิ้นเดือนกรกฎาคม 2026 รายละเอียดเพิ่มเติมเกี่ยวกับการใช้ [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) สำหรับทำต้นแบบกับโมเดล AI


## Mistral Large 2 (2407)
Mistral Large 2 คือโมเดลเรือธงปัจจุบันของ Mistral และออกแบบมาเพื่อการใช้งานในองค์กร 

โมเดลนี้เป็นการอัปเกรดจาก Mistral Large เดิม โดยมีคุณสมบัติดังนี้ 
-  หน้าต่างบริบทที่ใหญ่ขึ้น - 128k เทียบกับ 32k 
-  ประสิทธิภาพที่ดีขึ้นในงานคณิตศาสตร์และเขียนโค้ด - ความแม่นยำเฉลี่ย 76.9% เทียบกับ 60.4% 
-  ประสิทธิภาพหลายภาษาที่เพิ่มขึ้น - รองรับภาษา: อังกฤษ, ฝรั่งเศส, เยอรมัน, สเปน, อิตาลี, โปรตุเกส, ดัตช์, รัสเซีย, จีน, ญี่ปุ่น, เกาหลี, อาหรับ และฮินดี 

ด้วยฟีเจอร์เหล่านี้ Mistral Large โดดเด่นในด้าน 
- *Retrieval Augmented Generation (RAG)* - เนื่องจากหน้าต่างบริบทที่ใหญ่ขึ้น
- *Function Calling* - โมเดลนี้มีฟีเจอร์เรียกใช้งานฟังก์ชันแบบเนทีฟ ซึ่งช่วยให้รวมกับเครื่องมือและ API ภายนอกได้ สามารถเรียกได้ทั้งแบบขนานหรือทีละตัวเรียงลำดับ
- *Code Generation* - โมเดลนี้โดดเด่นในการเขียนโปรแกรม Python, Java, TypeScript และ C++ 

### ตัวอย่าง RAG โดยใช้ Mistral Large 2 

ในตัวอย่างนี้ เราใช้ Mistral Large 2 เพื่อรันรูปแบบ RAG บนเอกสารข้อความ คำถามถูกเขียนเป็นภาษาเกาหลีและถามเกี่ยวกับกิจกรรมของผู้เขียนก่อนเข้ามหาวิทยาลัย 

ใช้ Cohere Embeddings Model เพื่อสร้าง embeddings ของเอกสารข้อความและคำถาม สำหรับตัวอย่างนี้ใช้แพ็กเกจ Python faiss เป็นฐานเก็บเวกเตอร์ 

ข้อความ prompt ที่ส่งไปยังโมเดล Mistral รวมทั้งคำถามและส่วนที่นำกลับมาซึ่งคล้ายกับคำถาม โมเดลจะให้คำตอบเป็นภาษาธรรมชาติ 

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

# รับข้อมูลเหล่านี้จากหน้า "ภาพรวม" ของโครงการ Microsoft Foundry ของคุณ
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
Mistral Small เป็นอีกโมเดลหนึ่งในตระกูล Mistral ภายใต้หมวด premier/enterprise ตามชื่อบ่งบอกว่าเป็น Small Language Model (SLM) ข้อดีของการใช้ Mistral Small คือ: 
- ประหยัดค่าใช้จ่ายเมื่อเทียบกับ LLM ของ Mistral เช่น Mistral Large และ NeMo - ลดราคาถึง 80%
- ความหน่วงต่ำ - ตอบสนองรวดเร็วกว่ารุ่น LLM ของ Mistral
- ยืดหยุ่น - สามารถปรับใช้ในหลายสภาพแวดล้อม โดยมีข้อจำกัดด้านทรัพยากรน้อยกว่า 


Mistral Small เหมาะสำหรับ: 
- งานที่ใช้ข้อความเป็นหลัก เช่น สรุปข้อความ วิเคราะห์อารมณ์ และแปลภาษา 
- แอปพลิเคชันที่มีการเรียกใช้งานบ่อยครั้ง เนื่องจากประหยัดค่าใช้จ่าย 
- งานเขียนโค้ดที่ต้องการความหน่วงต่ำ เช่น ตรวจสอบและแนะนำโค้ด 

## การเปรียบเทียบ Mistral Small และ Mistral Large 

เพื่อแสดงความแตกต่างในความหน่วงระหว่าง Mistral Small และ Large ให้รันโค้ดด้านล่างนี้ 

คุณจะเห็นความแตกต่างของเวลาตอบสนองประมาณ 3-5 วินาที นอกจากนี้ยังสังเกตความยาวและรูปแบบการตอบสนองของคำถามเดียวกันได้ด้วย  

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

เมื่อเทียบกับสองโมเดลอื่นที่กล่าวถึงในบทเรียนนี้ Mistral NeMo เป็นโมเดลเดียวที่ให้ใช้ฟรีพร้อมใบอนุญาต Apache2 

มันถูกมองว่าเป็นการอัปเกรดจาก LLM โอเพ่นซอร์สรุ่นก่อนของ Mistral คือ Mistral 7B 

ฟีเจอร์อื่น ๆ ของโมเดล NeMo ได้แก่: 

- *การแบ่งโทเคนที่มีประสิทธิภาพมากขึ้น:* โมเดลนี้ใช้ตัวแยกโทเคน Tekken แทน tiktoken ที่ใช้กันแพร่หลายกว่า ซึ่งช่วยเพิ่มประสิทธิภาพในหลายภาษาและโค้ด 

- *การปรับแต่ง (Finetuning):* โมเดลฐานเปิดให้ปรับแต่งได้ซึ่งช่วยให้อิสระในการใช้งานในกรณีที่ต้องการปรับแต่งเพิ่มเติม 

- *การเรียกใช้งานฟังก์ชันแบบเนทีฟ* - เช่นเดียวกับ Mistral Large โมเดลนี้ถูกฝึกอบรมให้รองรับการเรียกใช้งานฟังก์ชัน ซึ่งถือเป็นหนึ่งในโมเดลโอเพ่นซอร์สรุ่นแรกที่ทำได้


### การเปรียบเทียบ Tokenizers 

ในตัวอย่างนี้ เราจะดูว่า Mistral NeMo จัดการการแบ่งโทเคนอย่างไรเมื่อเทียบกับ Mistral Large 

ตัวอย่างทั้งสองใช้ prompt เดียวกัน แต่คุณจะเห็นว่า NeMo ให้จำนวนโทเคนน้อยกว่า Mistral Large 

```bash
pip install mistral-common
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

# โหลดตัวแบ่งคำ Mistral

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# แบ่งคำจากรายชื่อข้อความ
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

# โหลดตัวแบ่งคำ Mistral

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# แบ่งคำในรายการข้อความ
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

## การเรียนรู้ไม่ได้หยุดเพียงเท่านี้ เดินหน้าต่อไป

หลังจากจบบทเรียนนี้แล้ว ลองดูที่ [คอลเลกชันการเรียนรู้ Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) เพื่อเพิ่มพูนความรู้ Generative AI ของคุณ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->