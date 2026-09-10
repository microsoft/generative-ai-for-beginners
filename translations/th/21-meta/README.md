# การสร้างด้วยโมเดลตระกูล Meta 

## บทนำ 

บทเรียนนี้จะครอบคลุม: 

- การสำรวจโมเดลหลักสองรุ่นของตระกูล Meta - Llama 3.1 และ Llama 3.2 
- การทำความเข้าใจกรณีการใช้งานและสถานการณ์สำหรับแต่ละโมเดล 
- ตัวอย่างโค้ดเพื่อแสดงคุณสมบัติที่เป็นเอกลักษณ์ของแต่ละโมเดล 


## ตระกูลโมเดล Meta 

ในบทเรียนนี้ เราจะสำรวจ 2 โมเดลจากตระกูล Meta หรือที่เรียกว่า "ฝูง Llama" - Llama 3.1 และ Llama 3.2

โมเดลเหล่านี้มีหลายรุ่นและสามารถใช้งานได้ใน [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)

> **หมายเหตุ:** GitHub Models จะเลิกให้บริการในสิ้นเดือนกรกฎาคม 2026 รายละเอียดเพิ่มเติมเกี่ยวกับการใช้ [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) เพื่อสร้างต้นแบบด้วยโมเดล AI

รุ่นโมเดล: 
- Llama 3.1 - 70B Instruct 
- Llama 3.1 - 405B Instruct 
- Llama 3.2 - 11B Vision Instruct 
- Llama 3.2 - 90B Vision Instruct 

*หมายเหตุ: Llama 3 ก็มีให้บริการใน Microsoft Foundry Models เช่นกัน แต่จะไม่ครอบคลุมในบทเรียนนี้*

## Llama 3.1 

ด้วยพารามิเตอร์ 405 พันล้าน Llama 3.1 จัดอยู่ในหมวดหมู่ LLM แบบโอเพ่นซอร์ส 

โมเดลนี้เป็นการอัปเกรดจาก Llama 3 รุ่นก่อนโดยมี: 

- หน้าต่างบริบทที่ใหญ่ขึ้น - 128k tokens เทียบกับ 8k tokens 
- Max Output Tokens ที่ใหญ่ขึ้น - 4096 เทียบกับ 2048 
- การรองรับหลายภาษาได้ดีขึ้น - เนื่องจากมี token การฝึกที่มากขึ้น 

สิ่งเหล่านี้ช่วยให้ Llama 3.1 สามารถจัดการกรณีการใช้งานที่ซับซ้อนมากขึ้นเมื่อสร้างแอปพลิเคชัน GenAI รวมถึง: 
- การเรียกฟังก์ชันในตัว - ความสามารถในการเรียกใช้เครื่องมือและฟังก์ชันภายนอกนอกเหนือจากเวิร์กโฟลว์ของ LLM
- ประสิทธิภาพ RAG ดีขึ้น - เนื่องจากหน้าต่างบริบทที่กว้างขึ้น 
- การสร้างข้อมูลสังเคราะห์ - ความสามารถในการสร้างข้อมูลที่มีประสิทธิภาพสำหรับงาน เช่น การปรับแต่งเพิ่มเติม 

### การเรียกฟังก์ชันในตัว 

Llama 3.1 ได้รับการปรับแต่งให้มีประสิทธิภาพมากขึ้นในการเรียกฟังก์ชันหรือเครื่องมือ นอกจากนี้ยังมีเครื่องมือในตัวสองอย่างที่โมเดลสามารถระบุได้ว่าสอดคล้องกับคำสั่งของผู้ใช้ เครื่องมือเหล่านี้คือ: 

- **Brave Search** - ใช้สำหรับการค้นหาข้อมูลปัจจุบันเช่นสภาพอากาศโดยการค้นหาเว็บ 
- **Wolfram Alpha** - ใช้สำหรับการคำนวณทางคณิตศาสตร์ที่ซับซ้อนมากขึ้น ดังนั้นไม่จำเป็นต้องเขียนฟังก์ชันเอง 

คุณยังสามารถสร้างเครื่องมือที่กำหนดเองที่ LLM สามารถเรียกใช้ได้ 

ในตัวอย่างโค้ดด้านล่าง: 

- เรากำหนดเครื่องมือที่ใช้ได้ (brave_search, wolfram_alpha) ในพรอมต์ระบบ 
- ส่งพรอมต์ผู้ใช้ที่ถามเกี่ยวกับสภาพอากาศในเมืองใดเมืองหนึ่ง 
- LLM จะตอบกลับด้วยการเรียกเครื่องมือไปยัง Brave Search ซึ่งจะมีลักษณะดังนี้ `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*หมายเหตุ: ตัวอย่างนี้ทำการเรียกเครื่องมือเท่านั้น หากต้องการผลลัพธ์ คุณต้องสร้างบัญชีฟรีบนหน้า Brave API และกำหนดฟังก์ชันเอง

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# รับค่านี้จากหน้า "ภาพรวม" ของโครงการ Microsoft Foundry ของคุณ
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Meta-Llama-3.1-405B-Instruct"

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

แม้จะเป็น LLM แต่ข้อจำกัดหนึ่งของ Llama 3.1 คือขาดคุณสมบัติแบบมัลติโมดัล นั่นคือตัวไม่สามารถใช้ข้อมูลนำเข้าหลายประเภท เช่น ภาพเป็นพรอมต์และให้คำตอบได้ ความสามารถนี้เป็นหนึ่งในคุณสมบัติหลักของ Llama 3.2 คุณสมบัติเหล่านี้รวมถึง: 

- มัลติโมดัล - สามารถประเมินทั้งพรอมต์ข้อความและภาพ 
- ขนาดรุ่นเล็กถึงกลาง (11B และ 90B) - ให้ตัวเลือกการปรับใช้ที่ยืดหยุ่น, 
- รูปแบบข้อความเท่านั้น (1B และ 3B) - ช่วยให้โมเดลสามารถติดตั้งบนอุปกรณ์ขอบ / มือถือ และให้ความหน่วงต่ำ 

การรองรับมัลติโมดัลนี้เป็นก้าวสำคัญในโลกของโมเดลโอเพ่นซอร์ส ตัวอย่างโค้ดด้านล่างใช้ทั้งภาพและพรอมต์ข้อความเพื่อรับการวิเคราะห์ภาพจาก Llama 3.2 90B 


### การรองรับมัลติโมดัลกับ Llama 3.2

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

# รับข้อมูลเหล่านี้จากหน้า "ภาพรวม" ของโครงการ Microsoft Foundry ของคุณ
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
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

## การเรียนรู้ยังไม่จบที่นี่ ต่อเนื่องไปยังเส้นทางต่อไป

หลังจากจบบทเรียนนี้แล้ว ตรวจสอบ [ชุดเรียนรู้ Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ของเราเพื่อเพิ่มพูนความรู้ Generative AI ของคุณ!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->