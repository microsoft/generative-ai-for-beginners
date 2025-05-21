<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:11:48+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "th"
}
-->
# การสร้างด้วยโมเดลตระกูล Meta

## บทนำ

บทเรียนนี้จะครอบคลุม:

- สำรวจโมเดลหลักสองตัวในตระกูล Meta - Llama 3.1 และ Llama 3.2
- เข้าใจการใช้งานและสถานการณ์สำหรับแต่ละโมเดล
- ตัวอย่างโค้ดเพื่อแสดงคุณสมบัติเฉพาะของแต่ละโมเดล

## ตระกูลโมเดล Meta

ในบทเรียนนี้ เราจะสำรวจโมเดล 2 ตัวจากตระกูล Meta หรือ "Llama Herd" - Llama 3.1 และ Llama 3.2

โมเดลเหล่านี้มีหลายรูปแบบและสามารถหาได้ในตลาดโมเดลของ GitHub นี่คือรายละเอียดเพิ่มเติมเกี่ยวกับการใช้ GitHub Models เพื่อ [ต้นแบบด้วยโมเดล AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)

รูปแบบโมเดล:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*หมายเหตุ: Llama 3 ยังมีใน GitHub Models แต่จะไม่ครอบคลุมในบทเรียนนี้*

## Llama 3.1

ด้วย 405 พันล้านพารามิเตอร์ Llama 3.1 จัดอยู่ในประเภท LLM โอเพนซอร์ส

โมเดลนี้เป็นการอัพเกรดจาก Llama 3 รุ่นก่อน โดยเสนอ:

- หน้าต่างบริบทที่ใหญ่ขึ้น - 128k โทเค็นเทียบกับ 8k โทเค็น
- โทเค็นเอาต์พุตสูงสุดที่ใหญ่ขึ้น - 4096 เทียบกับ 2048
- การสนับสนุนหลายภาษาที่ดียิ่งขึ้น - เนื่องจากการเพิ่มขึ้นของโทเค็นการฝึกอบรม

สิ่งเหล่านี้ทำให้ Llama 3.1 สามารถจัดการกับกรณีการใช้งานที่ซับซ้อนมากขึ้นเมื่อสร้างแอปพลิเคชัน GenAI รวมถึง:
- การเรียกฟังก์ชันพื้นฐาน - ความสามารถในการเรียกใช้เครื่องมือและฟังก์ชันภายนอกนอกกระบวนการ LLM
- ประสิทธิภาพ RAG ที่ดียิ่งขึ้น - เนื่องจากหน้าต่างบริบทที่สูงขึ้น
- การสร้างข้อมูลสังเคราะห์ - ความสามารถในการสร้างข้อมูลที่มีประสิทธิภาพสำหรับงานเช่นการปรับแต่ง

### การเรียกฟังก์ชันพื้นฐาน

Llama 3.1 ได้รับการปรับแต่งให้มีประสิทธิภาพมากขึ้นในการเรียกใช้ฟังก์ชันหรือเครื่องมือ นอกจากนี้ยังมีเครื่องมือในตัวสองตัวที่โมเดลสามารถระบุว่าจำเป็นต้องใช้งานตามคำถามจากผู้ใช้ เครื่องมือเหล่านี้คือ:

- **Brave Search** - สามารถใช้เพื่อรับข้อมูลล่าสุดเช่นสภาพอากาศโดยการค้นหาเว็บ
- **Wolfram Alpha** - สามารถใช้สำหรับการคำนวณทางคณิตศาสตร์ที่ซับซ้อนมากขึ้น ดังนั้นไม่จำเป็นต้องเขียนฟังก์ชันของคุณเอง

คุณยังสามารถสร้างเครื่องมือที่กำหนดเองที่ LLM สามารถเรียกได้

ในตัวอย่างโค้ดด้านล่าง:

- เรากำหนดเครื่องมือที่มีอยู่ (brave_search, wolfram_alpha) ในระบบ prompt
- ส่งคำถามจากผู้ใช้ที่ถามเกี่ยวกับสภาพอากาศในเมืองหนึ่ง
- LLM จะตอบกลับด้วยการเรียกใช้เครื่องมือ Brave Search ซึ่งจะมีลักษณะดังนี้ `<|python_tag|>brave_search.call(query="Stockholm weather")`

*หมายเหตุ: ตัวอย่างนี้ทำการเรียกเครื่องมือเท่านั้น หากคุณต้องการรับผลลัพธ์ คุณจะต้องสร้างบัญชีฟรีในหน้า Brave API และกำหนดฟังก์ชันเอง*

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

แม้ว่า Llama 3.1 จะเป็น LLM แต่ข้อจำกัดหนึ่งที่มีคือการรองรับหลายโหมด นั่นคือ ความสามารถในการใช้ประเภทอินพุตต่างๆ เช่น ภาพเป็นคำถามและให้คำตอบ ความสามารถนี้เป็นหนึ่งในคุณสมบัติหลักของ Llama 3.2 คุณสมบัติเหล่านี้ยังรวมถึง:

- การรองรับหลายโหมด - มีความสามารถในการประเมินทั้งคำถามที่เป็นข้อความและภาพ
- ขนาดเล็กถึงขนาดกลาง (11B และ 90B) - ซึ่งให้ตัวเลือกการปรับใช้ที่ยืดหยุ่น
- ขนาดที่มีเฉพาะข้อความ (1B และ 3B) - ซึ่งช่วยให้โมเดลสามารถปรับใช้บนอุปกรณ์ edge / มือถือและให้ความหน่วงต่ำ

การสนับสนุนหลายโหมดแสดงถึงก้าวสำคัญในโลกของโมเดลโอเพนซอร์ส ตัวอย่างโค้ดด้านล่างใช้ทั้งภาพและคำถามที่เป็นข้อความเพื่อรับการวิเคราะห์ภาพจาก Llama 3.2 90B

### การสนับสนุนหลายโหมดด้วย Llama 3.2

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

## การเรียนรู้ไม่หยุดเพียงแค่นี้, ต่อการเดินทางของคุณ

หลังจากจบบทเรียนนี้ ลองดู [คอลเล็กชันการเรียนรู้ AI เชิงกำเนิด](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ของเราเพื่อพัฒนาความรู้ด้าน AI เชิงกำเนิดของคุณต่อไป!

**คำปฏิเสธความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามอย่างเต็มที่เพื่อความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาที่เป็นต้นฉบับควรถูกพิจารณาว่าเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้บริการแปลภาษามนุษย์ที่มีความเชี่ยวชาญ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้