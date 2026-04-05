# การสร้างด้วยโมเดลตระกูล Meta

## บทนำ

บทเรียนนี้จะครอบคลุม:

- การสำรวจโมเดลหลักสองตัวของตระกูล Meta - Llama 3.1 และ Llama 3.2
- การเข้าใจกรณีการใช้งานและสถานการณ์สำหรับแต่ละโมเดล
- ตัวอย่างโค้ดเพื่อแสดงฟีเจอร์เฉพาะของแต่ละโมเดล

## ตระกูลโมเดล Meta

ในบทเรียนนี้ เราจะสำรวจ 2 โมเดลจากตระกูล Meta หรือที่เรียกว่า "Llama Herd" - Llama 3.1 และ Llama 3.2

โมเดลเหล่านี้มีหลายรูปแบบและสามารถหาได้ในตลาดโมเดลของ GitHub นี่คือรายละเอียดเพิ่มเติมเกี่ยวกับการใช้ GitHub Models เพื่อ [สร้างต้นแบบด้วยโมเดล AI](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)

รูปแบบโมเดล:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*หมายเหตุ: Llama 3 ก็มีให้ใช้บน GitHub Models เช่นกัน แต่จะไม่ครอบคลุมในบทเรียนนี้*

## Llama 3.1

ด้วยพารามิเตอร์ 405 พันล้านตัว Llama 3.1 จัดอยู่ในประเภท LLM แบบโอเพ่นซอร์ส

โมเดลนี้เป็นการอัปเกรดจากรุ่นก่อนหน้า Llama 3 โดยมีคุณสมบัติดังนี้:

- หน้าต่างบริบทที่ใหญ่ขึ้น - 128k tokens เทียบกับ 8k tokens
- จำนวนโทเคนผลลัพธ์สูงสุดที่ใหญ่ขึ้น - 4096 เทียบกับ 2048
- การรองรับหลายภาษาได้ดีขึ้น - เนื่องจากจำนวนโทเคนที่ใช้ในการฝึกเพิ่มขึ้น

สิ่งเหล่านี้ช่วยให้ Llama 3.1 สามารถจัดการกับกรณีการใช้งานที่ซับซ้อนมากขึ้นเมื่อสร้างแอปพลิเคชัน GenAI รวมถึง:
- การเรียกฟังก์ชันเนทีฟ - ความสามารถในการเรียกใช้เครื่องมือและฟังก์ชันภายนอกที่อยู่นอกเหนือจากกระบวนการทำงานของ LLM
- ประสิทธิภาพ RAG ที่ดีขึ้น - เนื่องจากหน้าต่างบริบทที่กว้างขึ้น
- การสร้างข้อมูลสังเคราะห์ - ความสามารถในการสร้างข้อมูลที่มีประสิทธิภาพสำหรับงาน เช่น การทำ fine-tuning

### การเรียกฟังก์ชันเนทีฟ

Llama 3.1 ถูกปรับแต่งมาให้มีประสิทธิภาพมากขึ้นในการเรียกฟังก์ชันหรือเครื่องมือ นอกจากนี้ยังมีเครื่องมือในตัวสองอย่างที่โมเดลสามารถระบุได้ว่าจำเป็นต้องใช้งานตามคำสั่งจากผู้ใช้ เครื่องมือเหล่านี้ได้แก่:

- **Brave Search** - ใช้เพื่อค้นหาข้อมูลล่าสุด เช่น สภาพอากาศ โดยการค้นหาบนเว็บ
- **Wolfram Alpha** - ใช้สำหรับคำนวณทางคณิตศาสตร์ที่ซับซ้อนมากขึ้น โดยไม่จำเป็นต้องเขียนฟังก์ชันเอง

คุณยังสามารถสร้างเครื่องมือของคุณเองที่ LLM สามารถเรียกใช้งานได้

ในตัวอย่างโค้ดด้านล่าง:

- เรากำหนดเครื่องมือที่มีอยู่ (brave_search, wolfram_alpha) ใน system prompt
- ส่ง prompt จากผู้ใช้ที่ถามเกี่ยวกับสภาพอากาศในเมืองหนึ่ง
- LLM จะตอบกลับด้วยการเรียกใช้เครื่องมือ Brave Search ซึ่งจะมีลักษณะเช่นนี้ `<|python_tag|>brave_search.call(query="Stockholm weather")`

*หมายเหตุ: ตัวอย่างนี้ทำแค่การเรียกเครื่องมือเท่านั้น หากต้องการผลลัพธ์จริง ๆ จะต้องสร้างบัญชีฟรีที่หน้า API ของ Brave และกำหนดฟังก์ชันเอง

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

แม้จะเป็น LLM แต่ข้อจำกัดหนึ่งของ Llama 3.1 คือไม่มีความสามารถมัลติโมดัล นั่นคือไม่สามารถใช้อินพุตประเภทต่าง ๆ เช่น รูปภาพเป็น prompt และตอบกลับได้ ความสามารถนี้เป็นหนึ่งในฟีเจอร์หลักของ Llama 3.2 ฟีเจอร์เหล่านี้รวมถึง:

- มัลติโมดัล - มีความสามารถในการประเมินทั้ง prompt แบบข้อความและรูปภาพ
- ขนาดโมเดลแบบเล็กถึงกลาง (11B และ 90B) - ให้ตัวเลือกการติดตั้งที่ยืดหยุ่น
- รูปแบบเฉพาะข้อความ (1B และ 3B) - ช่วยให้โมเดลสามารถใช้งานบนอุปกรณ์ edge / มือถือ และให้เวลาหน่วงต่ำ

การสนับสนุนมัลติโมดัลนี้ถือเป็นก้าวสำคัญในโลกของโมเดลโอเพ่นซอร์ส ตัวอย่างโค้ดด้านล่างใช้ทั้งรูปภาพและ prompt ข้อความเพื่อขอการวิเคราะห์ภาพจาก Llama 3.2 90B

### การสนับสนุนมัลติโมดัลกับ Llama 3.2

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

## การเรียนรู้ไม่ได้หยุดอยู่แค่นี้ ต่อเนื่องการเดินทางของคุณ

หลังจากจบบทเรียนนี้แล้ว ลองไปดู [คอลเลกชันการเรียนรู้ Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) เพื่อพัฒนาความรู้ด้าน Generative AI ของคุณต่อไป!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้มีความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อน เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่มีความสำคัญ ขอแนะนำให้ใช้บริการแปลโดยมนุษย์มืออาชีพ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดพลาดใดๆ ที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->