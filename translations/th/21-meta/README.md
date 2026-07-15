# การสร้างด้วยโมเดลในตระกูล Meta  

## บทนำ  

บทเรียนนี้จะครอบคลุม:  

- การสำรวจโมเดลหลักสองตัวในตระกูล Meta - Llama 3.1 และ Llama 3.2  
- การเข้าใจกรณีการใช้งานและสถานการณ์สำหรับแต่ละโมเดล  
- ตัวอย่างโค้ดเพื่อแสดงคุณสมบัติเฉพาะของแต่ละโมเดล  


## ตระกูลโมเดล Meta  

ในบทเรียนนี้ เราจะสำรวจโมเดล 2 ตัวจากตระกูล Meta หรือที่เรียกว่า "Llama Herd" - Llama 3.1 และ Llama 3.2  

โมเดลเหล่านี้มีหลากหลายเวอร์ชันและมีให้ใช้งานใน [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)  

> **หมายเหตุ:** GitHub Models จะปิดให้บริการภายในสิ้นเดือนกรกฎาคม 2026 รายละเอียดเพิ่มเติมเกี่ยวกับการใช้ [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) ในการทดลองกับโมเดล AI  

รุ่นของโมเดล:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*หมายเหตุ: Llama 3 มีให้ใช้ใน Microsoft Foundry Models ด้วยแต่จะไม่ถูกครอบคลุมในบทเรียนนี้*  

## Llama 3.1  

ด้วยพารามิเตอร์ 405 พันล้านตัว Llama 3.1 อยู่ในประเภท LLM แบบโอเพ่นซอร์ส  

โมเดลนี้เป็นการอัปเกรดจาก Llama 3 รุ่นก่อน โดยเสนอ:  

- หน้าต่างบริบทที่ใหญ่ขึ้น - 128k โทเค็น เทียบกับ 8k โทเค็น  
- จำนวนโทเค็นเอาต์พุตสูงสุดที่เพิ่มขึ้น - 4096 เทียบกับ 2048  
- การสนับสนุนหลายภาษาได้ดีขึ้น - เนื่องจากจำนวนโทเค็นในการฝึกเพิ่มขึ้น  

สิ่งเหล่านี้ช่วยให้ Llama 3.1 สามารถจัดการกับกรณีการใช้งานที่ซับซ้อนมากขึ้นเมื่อสร้างแอปพลิเคชัน GenAI รวมถึง:  
- Native Function Calling - ความสามารถในการเรียกใช้เครื่องมือและฟังก์ชันภายนอกนอกเหนือจากกระบวนการ LLM  
- ประสิทธิภาพ RAG ที่ดีขึ้น - เนื่องจากหน้าต่างบริบทที่ใหญ่ขึ้น  
- การสร้างข้อมูลสังเคราะห์ - ความสามารถในการสร้างข้อมูลที่มีประสิทธิผลสำหรับงานเช่นการปรับแต่งละเอียด  

### Native Function Calling  

Llama 3.1 ได้รับการปรับแต่งเพิ่มเติมให้มีประสิทธิภาพมากขึ้นในการเรียกฟังก์ชันหรือเครื่องมือ นอกจากนี้ยังมีเครื่องมือในตัวสองตัวที่โมเดลสามารถระบุได้ว่าจำเป็นต้องใช้ตามพรอมต์จากผู้ใช้ เครื่องมือเหล่านี้คือ:  

- **Brave Search** - ใช้เพื่อค้นหาข้อมูลปัจจุบันเช่นสภาพอากาศโดยการค้นหาผ่านเว็บ  
- **Wolfram Alpha** - ใช้สำหรับคำนวณทางคณิตศาสตร์ที่ซับซ้อนมากขึ้นโดยไม่จำเป็นต้องเขียนฟังก์ชันเอง  

คุณยังสามารถสร้างเครื่องมือของคุณเองที่ LLM สามารถเรียกใช้งานได้  

ในตัวอย่างโค้ดด้านล่าง:  

- เรากำหนดเครื่องมือที่พร้อมใช้งาน (brave_search, wolfram_alpha) ในพรอมต์ระบบ  
- ส่งพรอมต์จากผู้ใช้ที่ถามเกี่ยวกับสภาพอากาศในเมืองหนึ่ง  
- LLM จะตอบกลับด้วยการเรียกเครื่องมือ Brave Search ซึ่งจะมีลักษณะเช่นนี้ `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*หมายเหตุ: ตัวอย่างนี้แค่เรียกใช้เครื่องมือ หากต้องการรับผลลัพธ์ คุณจะต้องสร้างบัญชีฟรีบนหน้าของ Brave API และกำหนดฟังก์ชันเอง  

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# ดึงสิ่งเหล่านี้จากหน้า "ภาพรวม" ของโครงการ Microsoft Foundry ของคุณ
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

แม้จะเป็น LLM แต่ข้อจำกัดหนึ่งของ Llama 3.1 คือขาดความสามารถแบบมัลติโมดัล นั่นคือ ไม่สามารถใช้ชนิดอินพุตที่หลากหลาย เช่นภาพเป็นพรอมต์และตอบสนองได้ ความสามารถนี้เป็นหนึ่งในคุณสมบัติหลักของ Llama 3.2 คุณสมบัติเหล่านี้ยังรวมถึง:  

- มัลติโมดัล - มีความสามารถในการประเมินทั้งพรอมต์ข้อความและภาพ  
- รุ่นขนาดเล็กถึงกลาง (11B และ 90B) - ให้ตัวเลือกการปรับใช้ที่ยืดหยุ่น  
- รุ่นข้อความเท่านั้น (1B และ 3B) - ช่วยให้โมเดลสามารถปรับใช้บนอุปกรณ์ edge / มือถือและให้ความหน่วงต่ำ  

การสนับสนุนมัลติโมดัลเป็นก้าวสำคัญในโลกของโมเดลโอเพ่นซอร์ส ตัวอย่างโค้ดด้านล่างรับทั้งภาพและพรอมต์ข้อความเพื่อรับการวิเคราะห์ภาพจาก Llama 3.2 90B  


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

## การเรียนรู้ไม่หยุดเพียงเท่านี้ เดินทางต่อไป  

หลังจากทำบทเรียนนี้เสร็จแล้ว ลองดู [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) เพื่อพัฒนาความรู้ของคุณเกี่ยวกับ Generative AI ต่อไป!  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->