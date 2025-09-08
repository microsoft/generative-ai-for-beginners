<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:10:14+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "th"
}
-->
# การสร้างด้วยโมเดลตระกูล Meta

## บทนำ

บทเรียนนี้จะครอบคลุม:

- การสำรวจโมเดลหลักสองตัวในตระกูล Meta - Llama 3.1 และ Llama 3.2
- ทำความเข้าใจกรณีการใช้งานและสถานการณ์สำหรับแต่ละโมเดล
- ตัวอย่างโค้ดเพื่อแสดงคุณสมบัติพิเศษของแต่ละโมเดล

## ตระกูลโมเดล Meta

ในบทเรียนนี้ เราจะสำรวจโมเดล 2 ตัวจากตระกูล Meta หรือที่เรียกว่า "Llama Herd" ได้แก่ Llama 3.1 และ Llama 3.2

โมเดลเหล่านี้มีหลายเวอร์ชันและสามารถใช้งานได้บน GitHub Model marketplace รายละเอียดเพิ่มเติมเกี่ยวกับการใช้ GitHub Models เพื่อ [สร้างต้นแบบด้วยโมเดล AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)

รุ่นโมเดล:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*หมายเหตุ: Llama 3 ก็มีให้ใช้งานบน GitHub Models เช่นกัน แต่จะไม่ถูกกล่าวถึงในบทเรียนนี้*

## Llama 3.1

ด้วยพารามิเตอร์ 405 พันล้านตัว Llama 3.1 จัดอยู่ในหมวดหมู่ LLM แบบโอเพนซอร์ส

โมเดลนี้เป็นการอัปเกรดจาก Llama 3 รุ่นก่อนหน้า โดยมีข้อดีดังนี้:

- หน้าต่างบริบทที่ใหญ่ขึ้น - 128k โทเคน เทียบกับ 8k โทเคน
- จำนวนโทเคนผลลัพธ์สูงสุดที่มากขึ้น - 4096 เทียบกับ 2048
- การรองรับหลายภาษาได้ดีขึ้น - เนื่องจากจำนวนโทเคนในการฝึกที่เพิ่มขึ้น

สิ่งเหล่านี้ช่วยให้ Llama 3.1 สามารถจัดการกับกรณีการใช้งานที่ซับซ้อนมากขึ้นเมื่อสร้างแอปพลิเคชัน GenAI รวมถึง:
- Native Function Calling - ความสามารถในการเรียกใช้เครื่องมือและฟังก์ชันภายนอกนอกเหนือจากกระบวนการทำงานของ LLM
- ประสิทธิภาพ RAG ที่ดีขึ้น - เนื่องจากหน้าต่างบริบทที่ใหญ่ขึ้น
- การสร้างข้อมูลสังเคราะห์ - ความสามารถในการสร้างข้อมูลที่มีประสิทธิภาพสำหรับงานต่างๆ เช่น การปรับแต่งโมเดล

### Native Function Calling

Llama 3.1 ได้รับการปรับแต่งให้มีประสิทธิภาพมากขึ้นในการเรียกใช้ฟังก์ชันหรือเครื่องมือ นอกจากนี้ยังมีเครื่องมือในตัวสองตัวที่โมเดลสามารถระบุได้ว่าจำเป็นต้องใช้ตามคำสั่งจากผู้ใช้ เครื่องมือเหล่านี้ได้แก่:

- **Brave Search** - ใช้สำหรับค้นหาข้อมูลล่าสุด เช่น สภาพอากาศ ผ่านการค้นหาเว็บ
- **Wolfram Alpha** - ใช้สำหรับการคำนวณทางคณิตศาสตร์ที่ซับซ้อนโดยไม่ต้องเขียนฟังก์ชันเอง

คุณยังสามารถสร้างเครื่องมือของคุณเองที่ LLM สามารถเรียกใช้ได้

ในตัวอย่างโค้ดด้านล่าง:

- เรากำหนดเครื่องมือที่มีให้ใช้งาน (brave_search, wolfram_alpha) ใน system prompt
- ส่งคำสั่งจากผู้ใช้ที่ถามเกี่ยวกับสภาพอากาศในเมืองหนึ่ง
- LLM จะตอบกลับด้วยการเรียกใช้เครื่องมือ Brave Search ซึ่งจะมีลักษณะเช่นนี้ `<|python_tag|>brave_search.call(query="Stockholm weather")`

*หมายเหตุ: ตัวอย่างนี้เป็นเพียงการเรียกใช้เครื่องมือเท่านั้น หากต้องการผลลัพธ์จริง คุณจะต้องสร้างบัญชีฟรีบนหน้า Brave API และกำหนดฟังก์ชันเอง*

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

แม้จะเป็น LLM แต่ข้อจำกัดอย่างหนึ่งของ Llama 3.1 คือความสามารถในการรองรับหลายรูปแบบข้อมูล (multimodality) นั่นคือ การใช้ข้อมูลป้อนเข้าหลากหลายประเภท เช่น รูปภาพเป็นคำสั่ง และให้คำตอบตามนั้น ความสามารถนี้เป็นหนึ่งในฟีเจอร์หลักของ Llama 3.2 ฟีเจอร์อื่นๆ ได้แก่:

- Multimodality - สามารถประเมินคำสั่งทั้งข้อความและภาพได้
- ขนาดโมเดลขนาดเล็กถึงกลาง (11B และ 90B) - ให้ตัวเลือกการปรับใช้ที่ยืดหยุ่น
- รุ่นข้อความเท่านั้น (1B และ 3B) - ช่วยให้โมเดลสามารถปรับใช้บนอุปกรณ์ edge / มือถือ และให้ความหน่วงต่ำ

การรองรับ multimodal ถือเป็นก้าวสำคัญในโลกของโมเดลโอเพนซอร์ส ตัวอย่างโค้ดด้านล่างใช้ทั้งภาพและข้อความเป็นคำสั่งเพื่อรับการวิเคราะห์ภาพจาก Llama 3.2 90B

### การรองรับ Multimodal กับ Llama 3.2

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

## การเรียนรู้ไม่ได้หยุดเพียงเท่านี้ ต่อเนื่องเส้นทางของคุณ

หลังจากจบบทเรียนนี้แล้ว ลองดู [คอลเลกชันการเรียนรู้ Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ของเราเพื่อพัฒนาความรู้ด้าน Generative AI ของคุณให้ก้าวหน้าต่อไป!

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้