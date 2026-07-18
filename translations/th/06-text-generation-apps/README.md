# การสร้างแอปพลิเคชันสร้างข้อความ

[![การสร้างแอปพลิเคชันสร้างข้อความ](../../../translated_images/th/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(คลิกที่ภาพด้านบนเพื่อดูวิดีโอของบทเรียนนี้)_

จากที่คุณเห็นผ่านหลักสูตรนี้ มีแนวคิดหลักอย่างเช่นคำสั่ง (prompts) และแม้แต่วินัยทั้งหมดที่เรียกว่า "การวิศวกรรมคำสั่ง" หลายเครื่องมือที่คุณสามารถโต้ตอบได้ เช่น ChatGPT, Office 365, Microsoft Power Platform และอื่น ๆ รองรับให้คุณใช้คำสั่งเพื่อทำสิ่งต่าง ๆ ให้สำเร็จ

เพื่อให้คุณเพิ่มประสบการณ์แบบนี้ในแอป คุณต้องเข้าใจแนวคิดเช่น คำสั่ง (prompts), การเติมข้อความ (completions) และเลือกไลบรารีที่จะใช้ นั่นคือสิ่งที่คุณจะได้เรียนรู้ในบทนี้

## บทนำ

ในบทนี้ คุณจะ:

- เรียนรู้เกี่ยวกับไลบรารี openai และแนวคิดหลักของมัน
- สร้างแอปพลิเคชันสร้างข้อความโดยใช้ openai
- เข้าใจวิธีการใช้แนวคิดเช่น prompt, temperature และ tokens เพื่อสร้างแอปพลิเคชันสร้างข้อความ

## เป้าหมายการเรียนรู้

เมื่อจบบทเรียนนี้ คุณจะสามารถ:

- อธิบายว่าแอปพลิเคชันสร้างข้อความคืออะไร
- สร้างแอปพลิเคชันสร้างข้อความโดยใช้ openai
- กำหนดค่าแอปของคุณให้ใช้โทเค็นมากขึ้นหรือน้อยลง และเปลี่ยนอุณหภูมิ เพื่อให้ได้ผลลัพธ์ที่หลากหลาย

## แอปพลิเคชันสร้างข้อความคืออะไร?

โดยปกติเมื่อคุณสร้างแอปจะมีอินเทอร์เฟซบางประเภทดังนี้:

- แบบคำสั่ง คอนโซลแอปเป็นแอปปกติที่คุณพิมพ์คำสั่งแล้วมันทำงาน ตามตัวอย่างเช่น `git` เป็นแอปแบบคำสั่ง
- อินเทอร์เฟซผู้ใช้ (UI) แอปบางตัวมีอินเทอร์เฟซผู้ใช้กราฟิก (GUIs) ที่คุณคลิกปุ่ม ป้อนข้อความ เลือกตัวเลือก และอื่น ๆ

### คอนโซลและแอป UI มีข้อจำกัด

เปรียบเทียบกับแอปแบบคำสั่งที่คุณพิมพ์คำสั่ง:

- **มีข้อจำกัด** คุณไม่สามารถพิมพ์คำสั่งอะไรก็ได้ มีแค่คำสั่งที่แอปรองรับเท่านั้น
- **เฉพาะภาษา** แอปบางตัวรองรับหลายภาษา แต่โดยค่าเริ่มต้นแอปจะสร้างมาสำหรับภาษาหนึ่งเฉพาะ ถึงแม้ว่าคุณจะเพิ่มการรองรับภาษาอื่น ๆ ได้

### ข้อดีของแอปพลิเคชันสร้างข้อความ

แล้วแอปสร้างข้อความแตกต่างอย่างไร?

ในแอปสร้างข้อความ คุณมีความยืดหยุ่นมากขึ้น คุณไม่ถูกจำกัดด้วยชุดคำสั่งหรือภาษาป้อนข้อมูลเฉพาะ แต่คุณสามารถใช้ภาษาธรรมชาติเพื่อโต้ตอบกับแอป อีกประโยชน์คือคุณกำลังโต้ตอบกับแหล่งข้อมูลที่ผ่านการฝึกฝนจากข้อมูลจำนวนมหาศาล ในขณะที่แอปทั่วไปอาจถูกจำกัดด้วยข้อมูลในฐานข้อมูล

### ฉันสามารถสร้างอะไรได้บ้างกับแอปพลิเคชันสร้างข้อความ?

มีหลายสิ่งที่คุณสามารถสร้างได้ เช่น:

- **แชทบอท** แชทบอทที่ตอบคำถามเกี่ยวกับหัวข้อต่าง ๆ เช่น บริษัทของคุณและผลิตภัณฑ์ของบริษัท อาจเป็นตัวเลือกที่ดี
- **ผู้ช่วย** LLMs เก่งในงานอย่างการสรุปข้อความ การวิเคราะห์ข้อความ การสร้างข้อความเช่นประวัติการทำงาน และอื่น ๆ
- **ผู้ช่วยโค้ด** ขึ้นอยู่กับโมเดลภาษาที่คุณใช้ คุณสามารถสร้างผู้ช่วยเขียนโค้ด เช่น ใช้ผลิตภัณฑ์อย่าง GitHub Copilot หรือ ChatGPT เพื่อช่วยเขียนโค้ด

## ฉันจะเริ่มต้นอย่างไร?

คุณต้องหาวิธีเชื่อมต่อกับ LLM ซึ่งโดยปกติมีสองวิธีดังนี้:

- ใช้ API ที่นี่คุณจะสร้างคำขอเว็บพร้อมคำสั่งและรับข้อความที่สร้างกลับมา
- ใช้ไลบรารี ไลบรารีช่วยห่อหุ้มการเรียก API และทำให้ง่ายต่อการใช้งาน

## ไลบรารี/SDKs

มีไลบรารีที่เป็นที่รู้จักสำหรับการทำงานกับ LLM เช่น:

- **openai** ไลบรารีนี้ทำให้ง่ายต่อการเชื่อมต่อกับโมเดลของคุณและส่งคำสั่ง

ยังมีไลบรารีที่ทำงานในระดับสูงกว่า เช่น:

- **Langchain** Langchain เป็นที่รู้จักและรองรับ Python
- **Semantic Kernel** Semantic Kernel เป็นไลบรารีของ Microsoft ที่รองรับภาษา C#, Python และ Java

## แอปแรกโดยใช้ openai

มาดูวิธีสร้างแอปแรกของเรากัน ไลบรารีที่ต้องใช้ จำนวนที่ต้องการ และอื่น ๆ

### ติดตั้ง openai

มีไลบรารีมากมายสำหรับโต้ตอบกับ OpenAI หรือ Azure OpenAI คุณสามารถใช้ภาษาโปรแกรมหลายภาษา เช่น C#, Python, JavaScript, Java และอื่น ๆ เราเลือกใช้ไลบรารี `openai` ของ Python ดังนั้นเราจะใช้ `pip` เพื่อติดตั้ง

```bash
pip install openai
```

### สร้างทรัพยากร

คุณต้องดำเนินการตามขั้นตอนดังนี้:

- สร้างบัญชีใน Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)
- ขอสิทธิ์เข้าถึง Azure OpenAI ไปที่ [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) และขอสิทธิ์การเข้าถึง

  > [!NOTE]
  > ณ เวลาที่เขียนนี้ คุณต้องสมัครขอสิทธิ์เข้าถึง Azure OpenAI

- ติดตั้ง Python <https://www.python.org/>
- สร้างทรัพยากร Azure OpenAI Service ดูคู่มือวิธี [สร้างทรัพยากร](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)

### หาคีย์ API และ endpoint

ตอนนี้คุณต้องบอกไลบรารี `openai` ว่าจะใช้คีย์ API ไหน เพื่อหาคีย์ API ของคุณ ให้ไปที่ส่วน "Keys and Endpoint" ของทรัพยากร Azure OpenAI แล้วคัดลอกค่าของ "Key 1"

![หน้าจอ Keys and Endpoint ใน Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

เมื่อคุณคัดลอกข้อมูลนี้แล้ว มาเรียนรู้วิธีสั่งให้ไลบรารีใช้ข้อมูลนี้

> [!NOTE]
> ควรแยกคีย์ API ของคุณออกจากโค้ด คุณสามารถทำได้โดยใช้ตัวแปรแวดล้อม (environment variables)
>
> - ตั้งค่าตัวแปรแวดล้อม `OPENAI_API_KEY` เป็นคีย์ API ของคุณ
>   `export OPENAI_API_KEY='sk-...'`

### ตั้งค่าการกำหนดค่าสำหรับ Azure

หากคุณใช้ Azure OpenAI (ซึ่งตอนนี้เป็นส่วนหนึ่งของ Microsoft Foundry) นี่คือวิธีตั้งค่าการกำหนดค่า เราใช้ไคลเอนต์ `OpenAI` มาตรฐานที่ชี้ไปยัง endpoint `/openai/v1/` ของ Azure OpenAI ซึ่งทำงานกับ Responses API และไม่ต้องการ `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

ข้างบนเรากำลังตั้งค่าดังนี้:

- `api_key` นี่คือคีย์ API ของคุณที่พบใน Azure Portal หรือ Microsoft Foundry portal
- `base_url` นี่คือ endpoint ทรัพยากร Foundry ของคุณติด `/openai/v1/` ต่อท้าย endpoint v1 ที่เสถียรสามารถใช้ได้กับทั้ง OpenAI และ Azure OpenAI โดยไม่ต้องจัดการ `api_version`

> [!NOTE] > `os.environ` อ่านตัวแปรแวดล้อม คุณสามารถใช้มันเพื่ออ่านตัวแปรแวดล้อมเช่น `AZURE_OPENAI_API_KEY` และ `AZURE_OPENAI_ENDPOINT` ตั้งค่าตัวแปรแวดล้อมเหล่านี้ในเทอร์มินอลหรือโดยใช้ไลบรารีเช่น `dotenv`

## การสร้างข้อความ

วิธีสร้างข้อความคือใช้ Responses API ผ่านวิธี `responses.create` ตัวอย่างดังนี้:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # นี่คือชื่อการติดตั้งโมเดลของคุณ
    input=prompt,
    store=False,
)
print(response.output_text)
```

ในโค้ดด้านบน เราสร้างคำตอบและส่งโมเดลที่ต้องการใช้และคำสั่ง จากนั้นเราพิมพ์ข้อความที่สร้างผ่าน `response.output_text`

### การสนทนาแบบหลายรอบ

Responses API เหมาะสำหรับทั้งการสร้างข้อความแบบรอบเดียวและแชทบอทแบบหลายรอบ - คุณให้รายการข้อความใน `input` เพื่อสร้างบทสนทนา:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

จะพูดถึงฟังก์ชันนี้เพิ่มเติมในบทต่อไป

## แบบฝึกหัด - แอปพลิเคชันสร้างข้อความแรกของคุณ

ตอนนี้ที่เราเรียนรู้วิธีตั้งค่าและกำหนดค่า openai แล้ว ถึงเวลาสร้างแอปสร้างข้อความแรกของคุณ ตามขั้นตอนดังนี้:

1. สร้างสภาพแวดล้อมเสมือนและติดตั้ง openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > หากใช้ Windows ให้พิมพ์ `venv\Scripts\activate` แทน `source venv/bin/activate`

   > [!NOTE]
   > หาคีย์ Azure OpenAI ของคุณโดยไปที่ [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) ค้นหา `Open AI` และเลือก `Open AI resource` จากนั้นเลือก `Keys and Endpoint` แล้วคัดลอกค่า `Key 1`

1. สร้างไฟล์ _app.py_ และใส่โค้ดดังต่อไปนี้:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # เพิ่มโค้ดการทำงานของคุณ
   prompt = "Complete the following: Once upon a time there was a"

   # ส่งคำขอโดยใช้ Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # พิมพ์การตอบกลับ
   print(response.output_text)
   ```

   > [!NOTE]
   > หากใช้ OpenAI ธรรมดา (ไม่ใช่ Azure) ให้ใช้ `client = OpenAI(api_key="<แทนที่ด้วยคีย์ OpenAI ของคุณ>")` (ไม่มี `base_url`) และระบุชื่อโมเดลเช่น `gpt-5-mini` แทนชื่อดีพลอยเมนต์

   คุณจะเห็นผลลัพธ์ดังนี้:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## ประเภทต่าง ๆ ของคำสั่งสำหรับงานที่แตกต่างกัน

ตอนนี้คุณได้เห็นวิธีสร้างข้อความด้วย prompt แล้ว คุณมีโปรแกรมที่กำลังทำงานที่สามารถแก้ไขและเปลี่ยนเพื่อสร้างข้อความประเภทต่าง ๆ ได้

คำสั่ง (prompts) สามารถใช้กับงานหลากหลาย ตัวอย่างเช่น:

- **สร้างข้อความประเภทหนึ่ง** เช่น สร้างบทกวี คำถามสำหรับแบบทดสอบ ฯลฯ
- **ค้นหาข้อมูล** คุณสามารถใช้คำสั่งเพื่อค้นหาข้อมูล เช่น ตัวอย่าง "CORS หมายถึงอะไรในการพัฒนาเว็บ?"
- **สร้างโค้ด** คุณสามารถใช้คำสั่งเพื่อสร้างโค้ด เช่น สร้าง regular expression สำหรับตรวจสอบอีเมล หรืออาจสร้างโปรแกรมทั้งหมด เช่น เว็บแอปก็ได้

## กรณีใช้งานที่ใช้งานได้จริงมากขึ้น: เครื่องสร้างสูตรอาหาร

ลองจินตนาการว่าคุณมีวัตถุดิบที่บ้านและต้องการทำอาหาร สำหรับนั้นคุณต้องการสูตรอาหาร วิธีหาสูตรอาหารคือใช้เครื่องมือค้นหาหรือจะใช้ LLM ก็ได้

คุณอาจเขียนคำสั่งดังนี้:

> "แสดงสูตรอาหาร 5 สูตรที่ประกอบด้วยวัตถุดิบ: ไก่ มันฝรั่ง และแครอท สำหรับแต่ละสูตร ให้ระบุวัตถุดิบทั้งหมดที่ใช้"

จากคำสั่งข้างต้น คุณอาจได้รับคำตอบประมาณนี้:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 2 cloves garlic, minced
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
```

ผลลัพธ์นี้ดีมาก ฉันรู้ว่าจะทำอะไร ตอนนี้สิ่งที่อาจปรับปรุงให้ดีขึ้นคือ:

- กรองวัตถุดิบที่ฉันไม่ชอบหรือแพ้
- สร้างรายการช็อปปิ้ง เผื่อฉันไม่มีวัตถุดิบทั้งหมดที่บ้าน

สำหรับกรณีข้างต้น ให้เพิ่มคำสั่งเพิ่มเติมดังนี้:

> "กรุณาลบสูตรอาหารที่มีส่วนผสมกระเทียมเพราะฉันแพ้ และแทนที่ด้วยส่วนผสมอื่น อีกทั้งกรุณาสร้างรายการช็อปปิ้งสำหรับสูตรอาหาร โดยคิดว่าฉันมีไก่ มันฝรั่ง และแครอทอยู่แล้วที่บ้าน"

ตอนนี้คุณจะได้รับผลลัพธ์ใหม่คือ:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano

Shopping List:
- Olive oil
- Onion
- Thyme
- Oregano
- Salt
- Pepper
```

นั่นคือสูตรอาหาร 5 สูตรที่ไม่มีการกล่าวถึงกระเทียม และรวมรายการช็อปปิ้งตามวัตถุดิบที่คุณมีที่บ้านแล้ว

## แบบฝึกหัด - สร้างเครื่องสร้างสูตรอาหาร

ตอนนี้ที่เราเล่าเรื่องสถานการณ์แล้ว มาเขียนโค้ดให้ตรงกับสถานการณ์ที่แสดง ตามขั้นตอนดังนี้:

1. ใช้ไฟล์ _app.py_ ที่มีอยู่แล้วเป็นจุดเริ่มต้น
1. หา `prompt` ตัวแปรและเปลี่ยนโค้ดดังนี้:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   หากคุณรันโค้ดตอนนี้ คุณควรเห็นผลคล้ายกับ:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > หมายเหตุ โปรแกรม LLM ของคุณไม่ใช่แบบน้อยความน่าจะเป็น ดังนั้นคุณอาจได้ผลลัพธ์ที่แตกต่างกันทุกครั้งที่รันโปรแกรม

   ดีมาก มาดูวิธีปรับปรุง เราต้องการให้โค้ดยืดหยุ่น วัตถุดิบและจำนวนสูตรอาหารสามารถปรับปรุงและเปลี่ยนแปลงได้

1. เรามาเปลี่ยนโค้ดดังนี้:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # แทรกจำนวนสูตรลงในพรอมต์และส่วนผสม
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   ตัวอย่างการทดสอบรันโค้ดอาจเป็นแบบนี้:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### ปรับปรุงด้วยการเพิ่มตัวกรองและรายการช็อปปิ้ง

ตอนนี้เรามีแอปทำงานที่สามารถสร้างสูตรอาหารได้ และยืดหยุ่นเพราะขึ้นอยู่กับข้อมูลจากผู้ใช้ ทั้งจำนวนสูตรและวัตถุดิบ

เพื่อปรับปรุงเพิ่ม เราต้องการเพิ่มสิ่งต่อไปนี้:

- **กรองวัตถุดิบ** เราต้องการกรองวัตถุดิบที่เราไม่ชอบหรือแพ้ เพื่อทำสิ่งนี้ให้แก้ไข prompt ปัจจุบันโดยเพิ่มเงื่อนไขตัวกรองเข้าไปท้ายคำสั่ง เช่นนี้:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  ข้างบนนี้เราเพิ่ม `{filter}` เข้าไปท้าย prompt และรับค่าตัวกรองจากผู้ใช้ด้วย

  ตัวอย่างการป้อนข้อมูลเมื่อลองรันโปรแกรมอาจหน้าตาเช่นนี้:

  ```output
  No of recipes (for example, 5): 3
  List of ingredients (for example, chicken, potatoes, and carrots): onion,milk
  Filter (for example, vegetarian, vegan, or gluten-free): no milk

  1. French Onion Soup

  Ingredients:

  -1 large onion, sliced
  -3 cups beef broth
  -1 cup milk
  -6 slices french bread
  -1/4 cup shredded Parmesan cheese
  -1 tablespoon butter
  -1 teaspoon dried thyme
  -1/4 teaspoon salt
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add beef broth, milk, thyme, salt, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Place french bread slices on soup bowls.
  5. Ladle soup over bread.
  6. Sprinkle with Parmesan cheese.

  2. Onion and Potato Soup

  Ingredients:

  -1 large onion, chopped
  -2 cups potatoes, diced
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add potatoes, vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Serve hot.

  3. Creamy Onion Soup

  Ingredients:

  -1 large onion, chopped
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper
  -1/4 cup all-purpose flour
  -1/2 cup shredded Parmesan cheese

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. In a small bowl, whisk together flour and Parmesan cheese until smooth.
  5. Add to soup and simmer for an additional 5 minutes, or until soup has thickened.
  ```

  อย่างที่เห็น สูตรอาหารที่มีนมถูกกรองออกแล้ว แต่ถ้าคุณแพ้แลคโตส อาจต้องการกรองสูตรที่มีชีสด้วย จึงต้องชัดเจนในเงื่อนไขกรอง


- **สร้างรายการซื้อของ** เราต้องการสร้างรายการซื้อของ โดยพิจารณาสิ่งที่เรามีอยู่ที่บ้านแล้ว

  สำหรับฟังก์ชันนี้ เราสามารถลองแก้ปัญหาทั้งหมดในคำสั่งเดียว หรือจะแบ่งออกเป็นสองคำสั่งก็ได้ ลองใช้วิธีหลังดู ที่นี่เรากำลังแนะนำให้เพิ่มคำสั่งเพิ่มเติม แต่เพื่อให้ทำงานได้ เราต้องเพิ่มผลลัพธ์ของคำสั่งแรกเข้าไปเป็นบริบทให้กับคำสั่งที่สอง

  ค้นหาส่วนในโค้ดที่แสดงผลลัพธ์จากคำสั่งแรก และเพิ่มโค้ดต่อไปนี้ด้านล่าง:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # พิมพ์ผลลัพธ์
  print("Shopping list:")
  print(response.output_text)
  ```

  สังเกตดังนี้:

  1. เรากำลังสร้างคำสั่งใหม่โดยการเพิ่มผลลัพธ์จากคำสั่งแรกเข้าไปในคำสั่งใหม่:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. เราส่งคำขอใหม่ แต่พิจารณาจำนวนโทเค็นที่เราขอไปในคำสั่งแรก ดังนั้นครั้งนี้เราตั้งค่า `max_output_tokens` ให้เป็น 1200

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     เมื่อรันโค้ดนี้ เราจะได้ผลลัพธ์ดังนี้:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## ปรับปรุงการตั้งค่าของคุณ

สิ่งที่เรามีตอนนี้คือโค้ดที่ทำงานได้ แต่มีการปรับแต่งบางอย่างที่เราควรทำเพื่อพัฒนาให้ดียิ่งขึ้น บางสิ่งที่เราควรทำมีดังนี้:

- **แยกเก็บความลับออกจากโค้ด** เช่น กุญแจ API ความลับไม่ควรอยู่ในโค้ดและควรเก็บไว้ในที่ปลอดภัย เพื่อแยกความลับออกจากโค้ด เราสามารถใช้ environment variables และไลบรารีอย่าง `python-dotenv` เพื่อโหลดค่าจากไฟล์ วิธีการในโค้ดดูได้ดังนี้:

  1. สร้างไฟล์ `.env` ที่มีเนื้อหาดังนี้:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > หมายเหตุ สำหรับ Azure OpenAI บน Microsoft Foundry คุณต้องตั้งค่าตัวแปรแวดล้อมดังนี้แทน:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     ในโค้ด คุณจะโหลดตัวแปรแวดล้อมแบบนี้:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **คำแนะนำเกี่ยวกับความยาวโทเค็น** เราควรพิจารณาว่าเราต้องการโทเค็นกี่ตัวเพื่อสร้างข้อความที่ต้องการ โทเค็นมีค่าใช้จ่าย ดังนั้นถ้าเป็นไปได้ เราควรพยายามใช้โทเค็นให้น้อยที่สุด เช่น เราสามารถตั้งคำสั่ง prompt ให้ใช้โทเค็นน้อยลงได้หรือไม่?

  ถ้าต้องการเปลี่ยนจำนวนโทเค็นที่ใช้ คุณสามารถใช้พารามิเตอร์ `max_output_tokens` เช่น ถ้าต้องการใช้ 100 โทเค็น ก็จะเขียนแบบนี้:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **ทดลองปรับค่า temperature** Temperature เป็นสิ่งที่เรายังไม่เคยพูดถึงจนถึงตอนนี้ แต่เป็นบริบทสำคัญสำหรับการทำงานของโปรแกรม ค่า temperature ที่สูงจะทำให้ผลลัพธ์มีความสุ่มมากขึ้น และค่าที่ต่ำจะทำให้ผลลัพธ์มีความคาดเดาได้มากขึ้น พิจารณาว่าคุณต้องการความหลากหลายในการแสดงผลหรือไม่

  หากต้องการปรับ temperature สามารถใช้พารามิเตอร์ `temperature` เช่น ถ้าต้องการใช้ค่า 0.5 ก็เขียนแบบนี้:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > หมายเหตุ ยิ่งใกล้ 1.0 ผลลัพธ์จะยิ่งมีความหลากหลายมากขึ้น

- **โมเดล reasoning ไม่ใช้ `temperature`** นี่เป็นการเปลี่ยนแปลงสำคัญในปี 2026 โมเดลปัจจุบันที่ไม่ถูกเลิกใช้ใน Microsoft Foundry เป็น **โมเดล reasoning** (ตระกูล GPT-5, o-series) - และ **ไม่รองรับ `temperature` หรือ `top_p`** (รวมถึง `max_tokens`; ให้ใช้ `max_output_tokens` แทน) หากส่ง `temperature` ไปยัง `gpt-5-mini` คุณจะได้ข้อผิดพลาด "parameter not supported" ดังนั้นถ้าต้องการลองตัวอย่าง temperature ที่กล่าวมา ให้ใช้โมเดลที่ยังรองรับการควบคุม sampling ตัวอย่างเช่น โมเดลโอเพ่นอย่าง **Llama** เช่น `Llama-3.3-70B-Instruct` จาก [Microsoft Foundry model catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) เรียกผ่าน Foundry Models / Azure AI Inference endpoint (เหมือนกับตัวอย่าง `githubmodels-*`) สำหรับโมเดล reasoning อย่าง GPT-5 คุณจะควบคุม output ต่างไป:
  - **Prompt engineering** - คำแนะนำที่ชัดเจน ตัวอย่าง และโครงสร้างผลลัพธ์ (ดูบทเรียน [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) ทำหน้าที่แทนการปรับ sampling knobs
  - **Reasoning controls** - พารามิเตอร์อย่าง effort/verbosity ชั่งน้ำหนักความลึกของ reasoning กับความหน่วงและต้นทุน

  สรุป: `temperature`/`top_p` ยังคงใช้ได้กับโมเดลหลายตัว (Llama, Mistral, Phi และตระกูล GPT-4.x - แม้ GPT-4.x กำลังจะถูกเลิกใช้) แต่แนวทางที่กำลังมาคือ prompt engineering + reasoning controls บนโมเดล reasoning อย่าง GPT-5

## การบ้าน

สำหรับการบ้านนี้ คุณสามารถเลือกสร้างอะไรก็ได้

นี่คือข้อเสนอแนะบางอย่าง:

- ปรับปรุงแอป generator สูตรอาหารให้ดีขึ้น ทดลองปรับค่า temperature และคำสั่ง prompt ดูว่าจะได้ผลลัพธ์อย่างไร
- สร้าง "Study buddy" แอปนี้ควรตอบคำถามเกี่ยวกับหัวข้อ เช่น Python คุณอาจมีคำสั่ง prompt แบบ "อะไรคือหัวข้อหนึ่งใน Python?" หรือคำสั่งให้แสดงโค้ดเกี่ยวกับหัวข้อหนึ่ง เป็นต้น
- History bot ทำให้ประวัติศาสตร์มีชีวิต สั่งให้บอทเล่นบทบาทเป็นตัวละครประวัติศาสตร์และถามคำถามเกี่ยวกับชีวิตและยุคสมัยของเขา

## ตัวอย่างคำตอบ

### Study buddy

ข้างล่างเป็น prompt เริ่มต้น ลองดูและปรับแต่งตามที่คุณต้องการ

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### History bot

นี่คือบางคำสั่ง prompt ที่คุณอาจใช้ได้:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## ตรวจเช็คความรู้

คอนเซปต์ temperature คืออะไร?

1. มันควบคุมความสุ่มของผลลัพธ์
1. มันควบคุมขนาดของการตอบสนอง
1. มันควบคุมจำนวนโทเค็นที่ใช้

## 🚀 ความท้าทาย

เมื่อลองทำการบ้านนี้ ลองเปลี่ยนค่า temperature ตั้งเป็น 0, 0.5 และ 1 จำไว้ว่าค่า 0 จะมีความหลากหลายน้อยที่สุด และ 1 จะมีความหลากหลายมากที่สุด ค่าไหนเหมาะกับแอปของคุณที่สุด?

## เยี่ยมมาก! เรียนรู้ต่อไป

หลังจากจบบทเรียนนี้แล้ว ลองดู [คอลเลกชันการเรียนรู้ Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ของเราเพื่อยกระดับความรู้เกี่ยวกับ Generative AI ต่อไป!

ไปที่บทเรียนที่ 7 ซึ่งเราจะดูวิธีการ [สร้างแอปแชท](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->