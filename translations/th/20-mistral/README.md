# การสร้างด้วยโมเดล Mistral

## บทนำ

บทเรียนนี้จะครอบคลุม:  
- การสำรวจโมเดล Mistral ที่แตกต่างกัน  
- ความเข้าใจในกรณีการใช้งานและสถานการณ์ของแต่ละโมเดล  
- การสำรวจตัวอย่างโค้ดที่แสดงคุณสมบัติเฉพาะของแต่ละโมเดล  

## โมเดล Mistral

ในบทเรียนนี้ เราจะสำรวจโมเดล Mistral 3 ตัว ได้แก่  
**Mistral Large**, **Mistral Small** และ **Mistral Nemo**

โมเดลแต่ละตัวนี้มีให้ใช้งานฟรีในตลาดโมเดล GitHub โค้ดในโน้ตบุ๊กนี้จะใช้โมเดลเหล่านี้ในการรันโค้ด รายละเอียดเพิ่มเติมเกี่ยวกับการใช้โมเดล GitHub เพื่อ [สร้างต้นแบบด้วยโมเดล AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)

## Mistral Large 2 (2407)  
Mistral Large 2 เป็นโมเดลหลักของ Mistral ในขณะนี้และออกแบบมาสำหรับการใช้งานในองค์กร

โมเดลนี้เป็นการอัปเกรดจาก Mistral Large ดั้งเดิม โดยมี  
- หน้าต่างบริบทขนาดใหญ่ขึ้น - 128k เทียบกับ 32k  
- ประสิทธิภาพที่ดีกว่าในงานคณิตศาสตร์และการเขียนโค้ด - ความแม่นยำเฉลี่ย 76.9% เทียบกับ 60.4%  
- ประสิทธิภาพหลายภาษาเพิ่มขึ้น - รองรับภาษาต่าง ๆ ได้แก่ อังกฤษ ฝรั่งเศส เยอรมัน สเปน อิตาเลียน โปรตุเกส ดัตช์ รัสเซีย จีน ญี่ปุ่น เกาหลี อาหรับ และฮินดี

ด้วยคุณสมบัติเหล่านี้ Mistral Large ทำงานได้ดีใน  
- *การสร้างด้วยการเสริมการดึงข้อมูล (RAG)* - ด้วยหน้าต่างบริบทที่ใหญ่ขึ้น  
- *การเรียกใช้งานฟังก์ชัน* - โมเดลนี้รองรับการเรียกใช้งานฟังก์ชันในตัวซึ่งช่วยให้การผสานรวมกับเครื่องมือและ API ภายนอกเป็นไปได้ การเรียกใช้งานเหล่านี้สามารถทำพร้อมกันหรือทำทีละคำสั่งตามลำดับ  
- *การสร้างโค้ด* - โมเดลนี้โดดเด่นในการสร้างโค้ด Python, Java, TypeScript และ C++

### ตัวอย่าง RAG โดยใช้ Mistral Large 2  

ในตัวอย่างนี้ เราใช้ Mistral Large 2 เพื่อรันรูปแบบ RAG กับเอกสารข้อความ คำถามถูกเขียนเป็นภาษาเกาหลีและถามเกี่ยวกับกิจกรรมของผู้เขียนก่อนเข้ามหาวิทยาลัย

โมเดลใช้ Cohere Embeddings ในการสร้าง embedding ของเอกสารข้อความและคำถาม สำหรับตัวอย่างนี้ใช้แพ็กเกจ faiss ของ Python เป็นฐานข้อมูลเวกเตอร์

พรอมท์ที่ส่งไปยังโมเดล Mistral รวมคำถามและส่วนที่ดึงมาที่คล้ายกับคำถาม โมเดลจึงให้คำตอบในรูปแบบภาษาธรรมชาติ

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
Mistral Small เป็นอีกโมเดลหนึ่งในตระกูล Mistral ภายใต้หมวดหมู่พรีเมียม/องค์กร ตามชื่อที่บ่งบอก โมเดลนี้เป็น Small Language Model (SLM) ข้อดีของการใช้ Mistral Small คือ  
- ประหยัดค่าใช้จ่ายเมื่อเทียบกับ Mistral LLM เช่น Mistral Large และ NeMo - ลดราคาถึง 80%  
- ความหน่วงต่ำ - ตอบสนองได้เร็วกว่า LLM ของ Mistral  
- ยืดหยุ่น - สามารถปรับใช้งานในสภาพแวดล้อมต่าง ๆ ได้ง่ายโดยมีข้อจำกัดทรัพยากรน้อยกว่า

Mistral Small เหมาะสำหรับ:  
- งานเกี่ยวกับข้อความ เช่น การสรุป ความคิดเห็นเชิงบวก/ลบ และการแปล  
- แอปพลิเคชันที่ต้องการคำขอบ่อย ๆ เนื่องจากมีค่าใช้จ่ายประหยัด  
- งานโค้ดที่ต้องการความหน่วงต่ำ เช่น การตรวจสอบและข้อเสนอแนะโค้ด

## การเปรียบเทียบ Mistral Small และ Mistral Large  

เพื่อแสดงความแตกต่างของความหน่วงระหว่าง Mistral Small และ Mistral Large ให้รันโค้ดในเซลล์ด้านล่าง

คุณจะเห็นความแตกต่างในเวลาตอบสนองประมาณ 3-5 วินาที และสังเกตความยาวและสไตล์ของคำตอบกับพรอมท์เดียวกัน

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

เมื่อเทียบกับสองโมเดลที่กล่าวมา Mistral NeMo เป็นโมเดลฟรีตัวเดียวที่ใช้ใบอนุญาต Apache2

โมเดลนี้ถือเป็นการอัปเกรดจาก LLM โอเพนซอร์สก่อนหน้าของ Mistral, Mistral 7B

คุณสมบัติอื่น ๆ ของโมเดล NeMo ได้แก่

- *การตัดคำที่มีประสิทธิภาพมากขึ้น:* โมเดลนี้ใช้ตัวตัดคำ Tekken แทนที่ตัวตัดคำ tiktoken ที่นิยมใช้กันทั่วไป ซึ่งช่วยให้ทำงานได้ดีขึ้นกับหลายภาษาและโค้ด

- *ปรับแต่งเพิ่มเติม:* โมเดลฐานมีให้สำหรับการปรับแต่งเพิ่มเติม ซึ่งช่วยให้ความยืดหยุ่นเมื่อต้องการปรับแต่งแบบจำเพาะ

- *การเรียกใช้ฟังก์ชันในตัว* - เช่นเดียวกับ Mistral Large โมเดลนี้ได้รับการฝึกฝนให้รองรับการเรียกใช้ฟังก์ชัน ซึ่งทำให้เป็นหนึ่งในโมเดลโอเพนซอร์สรุ่นแรกที่มีคุณสมบัตินี้

### การเปรียบเทียบตัวตัดคำ

ในตัวอย่างนี้ เราจะดูว่า Mistral NeMo จัดการการตัดคำอย่างไรเมื่อเทียบกับ Mistral Large

ทั้งสองตัวอย่างใช้พรอมท์เดียวกัน แต่คุณจะเห็นว่า NeMo คืนค่าจำนวนน้อยกว่าของโทเค็นเมื่อเทียบกับ Mistral Large

```bash
pip install mistral-common
```
  
```python 
# นำเข้าแพ็กเกจที่จำเป็น:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# โหลดตัวตัดคำ Mistral

model_name = "open-mistral-nemo"

tokenizer = MistralTokenizer.from_model(model_name)

# ตัดคำข้อความในรายการข้อความ
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
# นำเข้าชุดแพ็คเกจที่จำเป็น:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# โหลดตัวแปลงโทเคน Mistral

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# แปลงรายการข้อความเป็นโทเคน
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
  
## การเรียนรู้ไม่หยุดเพียงเท่านี้ ต่อเส้นทางของคุณต่อไป

หลังจากทำบทเรียนนี้เสร็จแล้ว ให้ตรวจสอบ [คอลเลกชันการเรียนรู้ Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ของเราเพื่อพัฒนาความรู้ Generative AI ของคุณต่อไป!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่แม่นยำ เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ ในกรณีที่ข้อมูลมีความสำคัญสูง แนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์อย่างมืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->