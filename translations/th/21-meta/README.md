<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:31:28+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "th"
}
-->
# การสร้างด้วยโมเดลตระกูล Meta

## บทนำ

บทเรียนนี้จะครอบคลุม:

- สำรวจโมเดลหลักสองตัวของตระกูล Meta - Llama 3.1 และ Llama 3.2
- ทำความเข้าใจการใช้งานและสถานการณ์สำหรับแต่ละโมเดล
- ตัวอย่างโค้ดเพื่อแสดงคุณลักษณะเฉพาะของแต่ละโมเดล

## ตระกูลโมเดล Meta

ในบทเรียนนี้ เราจะสำรวจ 2 โมเดลจากตระกูล Meta หรือ "Llama Herd" - Llama 3.1 และ Llama 3.2

โมเดลเหล่านี้มีหลายรูปแบบและสามารถใช้ได้ในตลาดโมเดล GitHub รายละเอียดเพิ่มเติมเกี่ยวกับการใช้โมเดล GitHub เพื่อ [ต้นแบบกับโมเดล AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)

รูปแบบโมเดล:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*หมายเหตุ: Llama 3 ยังมีให้ใช้งานบน GitHub Models แต่จะไม่ครอบคลุมในบทเรียนนี้*

## Llama 3.1

ที่มีพารามิเตอร์ 405 พันล้าน Llama 3.1 อยู่ในหมวดหมู่ LLM แบบโอเพ่นซอร์ส

โหมดนี้เป็นการอัพเกรดจาก Llama 3 รุ่นก่อนโดยมีการเสนอ:

- หน้าต่างบริบทที่ใหญ่ขึ้น - 128k โทเคนเทียบกับ 8k โทเคน
- โทเคนเอาต์พุตสูงสุดที่ใหญ่ขึ้น - 4096 เทียบกับ 2048
- การสนับสนุนหลายภาษาที่ดีกว่า - เนื่องจากการเพิ่มขึ้นของโทเคนการฝึกอบรม

สิ่งเหล่านี้ช่วยให้ Llama 3.1 สามารถจัดการกรณีการใช้งานที่ซับซ้อนมากขึ้นเมื่อสร้างแอปพลิเคชัน GenAI รวมถึง:
- การเรียกฟังก์ชันเนทีฟ - ความสามารถในการเรียกเครื่องมือและฟังก์ชันภายนอกนอกกระบวนการทำงานของ LLM
- ประสิทธิภาพ RAG ที่ดีกว่า - เนื่องจากหน้าต่างบริบทที่สูงขึ้น
- การสร้างข้อมูลสังเคราะห์ - ความสามารถในการสร้างข้อมูลที่มีประสิทธิภาพสำหรับงานเช่นการปรับแต่ง

### การเรียกฟังก์ชันเนทีฟ

Llama 3.1 ได้รับการปรับแต่งให้มีประสิทธิภาพมากขึ้นในการทำการเรียกฟังก์ชันหรือเครื่องมือ นอกจากนี้ยังมีเครื่องมือในตัวสองตัวที่โมเดลสามารถระบุได้ว่าจำเป็นต้องใช้ตามพรอมต์จากผู้ใช้ เครื่องมือเหล่านี้คือ:

- **Brave Search** - สามารถใช้เพื่อรับข้อมูลล่าสุดเช่นสภาพอากาศโดยการค้นหาทางเว็บ
- **Wolfram Alpha** - สามารถใช้สำหรับการคำนวณทางคณิตศาสตร์ที่ซับซ้อนมากขึ้นดังนั้นการเขียนฟังก์ชันของคุณเองไม่จำเป็น

คุณยังสามารถสร้างเครื่องมือที่กำหนดเองของคุณเองที่ LLM สามารถเรียกใช้ได้

ในตัวอย่างโค้ดด้านล่าง:

- เรากำหนดเครื่องมือที่มีอยู่ (brave_search, wolfram_alpha) ในระบบพรอมต์
- ส่งพรอมต์ผู้ใช้ที่ถามเกี่ยวกับสภาพอากาศในเมืองหนึ่ง
- LLM จะตอบกลับด้วยการเรียกเครื่องมือไปยังเครื่องมือ Brave Search ซึ่งจะมีลักษณะดังนี้ `<|python_tag|>brave_search.call(query="Stockholm weather")`

*หมายเหตุ: ตัวอย่างนี้เพียงแค่ทำการเรียกเครื่องมือ หากคุณต้องการรับผลลัพธ์ คุณจะต้องสร้างบัญชีฟรีในหน้า Brave API และกำหนดฟังก์ชันเอง

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "meta-llama-3.1-405b-instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)


tool_prompt=f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Environment: ipython
Tools: brave_search, wolfram_alpha
Cutting Knowledge Date: December 2023
Today Date: 23 July 2024

You are a helpful assistant<|eot_id|>
"""

messages = [
    SystemMessage(content=tool_prompt),
    UserMessage(content="What is the weather in Stockholm?"),

]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```

## Llama 3.2

แม้ว่าจะเป็น LLM ข้อจำกัดอย่างหนึ่งที่ Llama 3.1 มีคือการทำงานหลายรูปแบบ นั่นคือความสามารถในการใช้ประเภทอินพุตที่แตกต่างกันเช่นภาพเป็นพรอมต์และให้การตอบสนอง ความสามารถนี้เป็นหนึ่งในคุณสมบัติหลักของ Llama 3.2 คุณสมบัติเหล่านี้ยังรวมถึง:

- การทำงานหลายรูปแบบ - มีความสามารถในการประเมินทั้งข้อความและพรอมต์ภาพ
- รูปแบบขนาดเล็กถึงขนาดกลาง (11B และ 90B) - ให้ตัวเลือกการปรับใช้ที่ยืดหยุ่น
- รูปแบบเฉพาะข้อความ (1B และ 3B) - ช่วยให้โมเดลสามารถปรับใช้บนอุปกรณ์ขอบ / มือถือและให้ความหน่วงต่ำ

การสนับสนุนหลายรูปแบบแสดงถึงก้าวใหญ่ในโลกของโมเดลโอเพ่นซอร์ส ตัวอย่างโค้ดด้านล่างใช้ทั้งภาพและพรอมต์ข้อความเพื่อรับการวิเคราะห์ภาพจาก Llama 3.2 90B

### การสนับสนุนหลายรูปแบบด้วย Llama 3.2

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    SystemMessage,
    UserMessage,
    TextContentItem,
    ImageContentItem,
    ImageUrl,
    ImageDetailLevel,
)
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "Llama-3.2-90B-Vision-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(
            content="You are a helpful assistant that describes images in details."
        ),
        UserMessage(
            content=[
                TextContentItem(text="What's in this image?"),
                ImageContentItem(
                    image_url=ImageUrl.load(
                        image_file="sample.jpg",
                        image_format="jpg",
                        detail=ImageDetailLevel.LOW)
                ),
            ],
        ),
    ],
    model=model_name,
)

print(response.choices[0].message.content)
```

## การเรียนรู้ไม่หยุดเพียงเท่านี้ เดินทางต่อไป

หลังจากจบบทเรียนนี้ ตรวจสอบ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ของเราเพื่อเพิ่มพูนความรู้ด้าน Generative AI ของคุณ!

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้มีความถูกต้อง โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาที่เป็นต้นฉบับควรถูกพิจารณาว่าเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้