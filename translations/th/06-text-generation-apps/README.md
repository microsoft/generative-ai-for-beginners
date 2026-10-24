# การสร้างแอปพลิเคชันการสร้างข้อความ

[![การสร้างแอปพลิเคชันการสร้างข้อความ](../../../translated_images/th/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(คลิกที่ภาพด้านบนเพื่อดูวิดีโอของบทเรียนนี้)_

จนถึงตอนนี้คุณได้เห็นในหลักสูตรนี้ว่ามีแนวคิดหลักอย่าง prompt และแม้แต่สาขาวิชาทั้งหมดที่เรียกว่า "prompt engineering" เครื่องมือหลายอย่างที่คุณสามารถโต้ตอบด้วย เช่น ChatGPT, Office 365, Microsoft Power Platform และอื่น ๆ สนับสนุนให้คุณใช้ prompt เพื่อทำบางสิ่งให้สำเร็จ

เพื่อให้คุณสามารถเพิ่มประสบการณ์แบบนี้ลงในแอปได้ คุณต้องเข้าใจแนวคิดอย่าง prompt, completion และเลือกไลบรารีเพื่อใช้งาน นั่นคือสิ่งที่คุณจะได้เรียนรู้ในบทนี้

## บทนำ

ในบทนี้ คุณจะได้:

- เรียนรู้เกี่ยวกับไลบรารี openai และแนวคิดหลักของมัน
- สร้างแอปพลิเคชันสร้างข้อความโดยใช้ openai
- เข้าใจวิธีใช้แนวคิดอย่าง prompt, temperature และ tokens เพื่อสร้างแอปพลิเคชันสร้างข้อความ

## เป้าหมายการเรียนรู้

เมื่อจบบทเรียนนี้ คุณจะสามารถ:

- อธิบายว่าแอปพลิเคชันสร้างข้อความคืออะไร
- สร้างแอปพลิเคชันสร้างข้อความโดยใช้ openai
- กำหนดค่าแอปของคุณให้ใช้ tokens มากขึ้นหรือน้อยลงและเปลี่ยนค่า temperature เพื่อให้ได้ผลลัพธ์หลากหลาย

## แอปพลิเคชันสร้างข้อความคืออะไร?

โดยปกติเมื่อคุณสร้างแอป มันจะมีอินเทอร์เฟซบางอย่างดังต่อไปนี้:

- แบบคำสั่ง (Command-based) แอปคอนโซลเป็นแอปทั่วไปที่คุณพิมพ์คำสั่งแล้วมันทำงานตามคำสั่ง เช่น `git` เป็นแอปแบบคำสั่ง
- อินเทอร์เฟซผู้ใช้ (UI) แอปบางตัวมีอินเทอร์เฟซผู้ใช้แบบกราฟิก (GUI) ที่คุณคลิกปุ่ม ป้อนข้อความ เลือกตัวเลือก และอื่น ๆ

### แอปคอนโซลและ UI มีข้อจำกัด

เปรียบเทียบกับแอปแบบคำสั่งที่คุณพิมพ์คำสั่ง:

- **มีข้อจำกัด** คุณไม่สามารถพิมพ์คำสั่งอะไรก็ได้ มีเพียงคำสั่งที่แอปสนับสนุนเท่านั้น
- **เจาะจงภาษา** แอปบางตัวสนับสนุนหลายภาษา แต่แอปถูกสร้างสำหรับภาษาหนึ่งเป็นหลัก แม้ว่าคุณจะสามารถเพิ่มการสนับสนุนภาษามากขึ้นได้

### ข้อดีของแอปพลิเคชันสร้างข้อความ

แล้วแอปพลิเคชันสร้างข้อความต่างกันอย่างไร?

ในแอปพลิเคชันสร้างข้อความ คุณมีความยืดหยุ่นมากขึ้น คุณไม่ถูกจำกัดด้วยชุดคำสั่งหรือภาษาป้อนข้อมูลเฉพาะ แต่คุณสามารถใช้ภาษาธรรมชาติในการโต้ตอบกับแอป อีกข้อดีคือคุณกำลังโต้ตอบกับแหล่งข้อมูลที่ได้รับการฝึกฝนจากข้อมูลจำนวนมาก ในขณะที่แอปธรรมดาอาจถูกจำกัดด้วยสิ่งที่อยู่ในฐานข้อมูล

### ฉันสามารถสร้างอะไรได้บ้างด้วยแอปพลิเคชันสร้างข้อความ?

คุณสามารถสร้างหลายอย่าง เช่น:

- **แชทบ็อต** แชทบ็อตที่ตอบคำถามเกี่ยวกับหัวข้อต่าง ๆ เช่น บริษัทของคุณและผลิตภัณฑ์ของมัน อาจเป็นสิ่งที่เหมาะสม
- **ผู้ช่วย** LLMs เหมาะสำหรับงานเช่น สรุปข้อความ, หาข้อมูลเชิงลึกจากข้อความ, สร้างข้อความเช่นเรซูเม่ เป็นต้น
- **ผู้ช่วยเขียนโค้ด** ขึ้นอยู่กับโมเดลภาษาที่คุณใช้ คุณสามารถสร้างผู้ช่วยเขียนโค้ดเพื่อช่วยเขียนโค้ด เช่น คุณสามารถใช้ผลิตภัณฑ์อย่าง GitHub Copilot หรือ ChatGPT เพื่อช่วยเขียนโค้ด

## ฉันจะเริ่มได้อย่างไร?

คุณจำเป็นต้องหาวิธีเชื่อมต่อกับ LLM ซึ่งโดยปกติจะมีสองแนวทางดังนี้:

- ใช้ API คุณสร้างคำขอเว็บด้วย prompt ของคุณและรับข้อความที่ถูกสร้างกลับมา
- ใช้ไลบรารี ไลบรารีช่วยรวมการเรียก API และทำให้ง่ายต่อการใช้งาน

## ไลบรารี/SDK

มีไลบรารีที่รู้จักดีในการทำงานกับ LLM หลายตัว เช่น:

- **openai** ไลบรารีนี้ทำให้ง่ายในการเชื่อมต่อกับโมเดลของคุณและส่ง prompt เข้าไป

นอกจากนี้ยังมีไลบรารีที่ทำงานในระดับสูงกว่า เช่น:

- **Langchain** Langchain มีชื่อเสียงและรองรับ Python
- **Semantic Kernel** Semantic Kernel เป็นไลบรารีโดย Microsoft รองรับภาษา C#, Python, และ Java

## แอปแรกโดยใช้ openai

มาดูวิธีสร้างแอปตัวแรกของเรา ไลบรารีที่เราต้องใช้ จำนวนสิ่งที่ต้องเตรียม และอื่น ๆ

### ติดตั้ง openai

มีไลบรารีมากมายสำหรับโต้ตอบกับ OpenAI หรือ Azure OpenAI และสามารถใช้หลายภาษาการเขียนโปรแกรมได้ เช่น C#, Python, JavaScript, Java และอื่น ๆ เราเลือกใช้ไลบรารี Python `openai` ดังนั้นเราจะใช้ `pip` เพื่อติดตั้ง

```bash
pip install openai
```

### สร้าง resource

คุณต้องทำขั้นตอนดังต่อไปนี้:

- สร้างบัญชีใน Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)
- เข้าถึง Azure OpenAI ไปที่ [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) และร้องขอการเข้าถึง

  > [!NOTE]
  > ในเวลาที่เขียนนี้ คุณต้องสมัครขอเข้าถึง Azure OpenAI

- ติดตั้ง Python <https://www.python.org/>
- สร้าง resource ของ Azure OpenAI Service ดูคำแนะนำนี้เพื่อดูวิธี [สร้าง resource](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)

### หาคีย์ API และ endpoint

ขณะนี้ คุณต้องแจ้งให้ไลบรารี `openai` รู้ว่าควรใช้ API key ใด ในการหาคีย์ API ไปที่ส่วน "Keys and Endpoint" ของ resource Azure OpenAI ของคุณและคัดลอกค่า "Key 1"

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

ตอนนี้ที่คุณคัดลอกข้อมูลนี้แล้ว ให้สั่งไลบรารีให้ใช้ข้อมูลนี้

> [!NOTE]
> ควรแยกคีย์ API ของคุณออกจากโค้ด คุณสามารถทำได้โดยใช้ environment variables
>
> - ตั้ง environment variable `OPENAI_API_KEY` ให้เป็นคีย์ API ของคุณ
>   `export OPENAI_API_KEY='sk-...'`

### ตั้งค่าคอนฟิก Azure

หากคุณใช้ Azure OpenAI (ตอนนี้เป็นส่วนหนึ่งของ Microsoft Foundry) วิธีตั้งค่าคอนฟิกคือ เราใช้ไคลเอนต์ `OpenAI` มาตรฐานที่ชี้ไปยัง endpoint Azure OpenAI `/openai/v1/` ซึ่งทำงานกับ Responses API และไม่ต้องการ `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

ข้างบนเราตั้งค่าดังนี้:

- `api_key` คือคีย์ API ของคุณพบได้ใน Azure Portal หรือ Microsoft Foundry portal
- `base_url` คือ endpoint resource ของ Foundry ของคุณที่ต่อท้ายด้วย `/openai/v1/` Endpoint stable v1 ใช้ได้ทั้ง OpenAI และ Azure OpenAI โดยไม่ต้องจัดการ `api_version`

> [!NOTE] > `os.environ` อ่าน environment variables คุณสามารถใช้มันเพื่ออ่าน environment variables เช่น `AZURE_OPENAI_API_KEY` และ `AZURE_OPENAI_ENDPOINT` ตั้ง environment variables เหล่านี้ในเทอร์มินัล หรือใช้ไลบรารีอย่าง `dotenv`

## การสร้างข้อความ

วิธีการสร้างข้อความคือใช้ Responses API ผ่านวิธี `responses.create` นี่คือตัวอย่าง:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

ในโค้ดข้างบน เราสร้าง response และส่งโมเดลที่ต้องการใช้งานและ prompt เข้าไป จากนั้นเราพิมพ์ข้อความที่ถูกสร้างผ่าน `response.output_text`

### การสนทนาหลายรอบ

Responses API เหมาะสำหรับทั้งการสร้างข้อความครั้งเดียวและแชทบ็อตหลายรอบ – คุณให้รายการข้อความใน `input` เพื่อสร้างการสนทนา:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

จะมีการพูดถึงฟังก์ชันนี้มากขึ้นในบทถัดไป

## แบบฝึกหัด – แอปพลิเคชันสร้างข้อความแอปแรกของคุณ

เมื่อตอนนี้เราเรียนรู้วิธีตั้งค่าและคอนฟิก openai แล้ว ได้เวลาสร้างแอปพลิเคชันสร้างข้อความแอปแรกของคุณ ทำตามขั้นตอนดังนี้:

1. สร้าง environment เสมือนและติดตั้ง openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > หากคุณใช้ Windows ให้พิมพ์ `venv\Scripts\activate` แทน `source venv/bin/activate`

   > [!NOTE]
   > หา Azure OpenAI key ของคุณโดยไปที่ [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) ค้นหา `Open AI` แล้วเลือก `Open AI resource` จากนั้นเลือก `Keys and Endpoint` และคัดลอกค่าของ `Key 1`

1. สร้างไฟล์ _app.py_ และใส่โค้ดดังนี้:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"

   # make a request using the Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # print response
   print(response.output_text)
   ```

   > [!NOTE]
   > หากคุณใช้ OpenAI ปกติ (ไม่ใช่ Azure) ใช้ `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (ไม่มี `base_url`) และส่งชื่อโมเดล เช่น `gpt-5-mini` แทนชื่อ deployment

   คุณควรเห็นผลลัพธ์ประมาณนี้:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## ประเภทของ prompt ที่แตกต่างกัน สำหรับสิ่งที่แตกต่างกัน

ตอนนี้คุณเห็นวิธีสร้างข้อความโดยใช้ prompt แล้ว คุณมีโปรแกรมที่พร้อมใช้งานที่คุณสามารถแก้ไขและเปลี่ยนเพื่อสร้างข้อความหลากหลายประเภท

Prompt สามารถใช้ทำงานหลายอย่าง เช่น:

- **สร้างข้อความประเภทหนึ่ง** เช่น คุณสามารถสร้างบทกวี คำถามสำหรับแบบทดสอบ เป็นต้น
- **ค้นหาข้อมูล** คุณสามารถใช้ prompt เพื่อค้นหาข้อมูล เช่น ตัวอย่างนี้ 'CORS ในการพัฒนาเว็บหมายความว่าอะไร?'
- **สร้างโค้ด** คุณสามารถใช้ prompt เพื่อสร้างโค้ด เช่น การพัฒนากฎนิพจน์ปกติ (regular expression) สำหรับตรวจสอบอีเมล หรือแม้แต่สร้างโปรแกรมทั้งโปรแกรม เช่น เว็บแอป

## กรณีใช้งานที่ใช้งานได้จริงมากขึ้น: ตัวสร้างสูตรอาหาร

ลองนึกภาพว่าคุณมีวัตถุดิบที่บ้านและต้องการทำอาหาร สำหรับเรื่องนี้ คุณต้องการสูตรอาหาร วิธีค้นหาสูตรอาหารคือใช้เครื่องมือค้นหาหรือใช้ LLM เพื่อทำเช่นนั้น

คุณสามารถเขียน prompt แบบนี้ได้:

> "ขอแสดง 5 สูตรอาหารที่ใช้วัตถุดิบต่อไปนี้: ไก่, มันฝรั่ง และแครอท สำหรับแต่ละสูตร ให้นับรวมวัตถุดิบทั้งหมดที่ใช้"

จาก prompt ข้างต้น คุณอาจได้รับคำตอบประมาณนี้:

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

ผลลัพธ์นี้ดีมาก ฉันรู้ว่าจะทำอะไร ในตอนนี้ สิ่งที่อาจปรับปรุงได้คือ:

- กรองวัตถุดิบที่ฉันไม่ชอบหรือแพ้
- สร้างรายการของชำไว้ในกรณีที่ฉันไม่มีวัตถุดิบทั้งหมดที่บ้าน

สำหรับกรณีข้างต้น เพิ่ม prompt ดังนี้:

> "โปรดลบสูตรอาหารที่มีหัวกระเทียมเนื่องจากฉันแพ้และแทนที่ด้วยสิ่งอื่นด้วย นอกจากนี้ โปรดสร้างรายการของชำสำหรับสูตรอาหารโดยพิจารณาว่าฉันมีไก่, มันฝรั่ง และแครอทที่บ้านแล้ว"

ตอนนี้คุณจะได้ผลลัพธ์ใหม่ ดังนี้:

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

นี่คือ 5 สูตรอาหารของคุณ โดยไม่มีการกล่าวถึงหัวกระเทียม และคุณยังมีรายการของชำโดยพิจารณาสิ่งที่คุณมีที่บ้าน

## แบบฝึกหัด – สร้างตัวสร้างสูตรอาหาร

ตอนนี้ที่เราทดลองสถานการณ์แล้ว มาลองเขียนโค้ดให้ตรงกับสถานการณ์ตัวอย่าง ทำตามขั้นตอนนี้:

1. ใช้ไฟล์ _app.py_ ที่มีอยู่เป็นจุดเริ่มต้น
1. หา `prompt` ตัวแปรและเปลี่ยนโค้ดของมันเป็นดังนี้:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   หากคุณรันโค้ดตอนนี้ คุณควรเห็นผลลัพธ์ประมาณนี้:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > หมายเหตุ LLM ของคุณเป็น nondeterministic ดังนั้นคุณอาจได้ผลลัพธ์แตกต่างกันทุกครั้งที่รันโปรแกรม

   ดีมาก มาดูวิธีปรับปรุงสิ่งต่าง ๆ เพื่อให้โค้ดยืดหยุ่น วัตถุดิบและจำนวนสูตรอาหารสามารถปรับปรุงและเปลี่ยนแปลงได้

1. เปลี่ยนโค้ดดังนี้:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   การนำโค้ดนี้มาทดสอบ อาจดูเป็นแบบนี้:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### ปรับปรุงโดยเพิ่มตัวกรองและรายการของชำ

ตอนนี้เรามีแอปใช้งานได้ที่สามารถสร้างสูตรอาหารและยืดหยุ่นเพราะขึ้นกับอินพุตจากผู้ใช้ ทั้งจำนวนสูตรและวัตถุดิบที่ใช้

เพื่อปรับปรุงเพิ่มเติม เราต้องการเพิ่มสิ่งเหล่านี้:

- **กรองวัตถุดิบออก** เราต้องการกรองวัตถุดิบที่เราไม่ชอบหรือแพ้ เพื่อทำการเปลี่ยนแปลงนี้ เราสามารถแก้ไข prompt ที่มีอยู่และเพิ่มเงื่อนไขตัวกรองเข้าไปที่ท้าย prompt ดังนี้:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  ข้างบน เราเพิ่ม `{filter}` ไปที่ท้าย prompt และรับค่าตัวกรองจากผู้ใช้ด้วย

  ตัวอย่างอินพุตเมื่อรันโปรแกรมตอนนี้อาจเป็นแบบนี้:

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

  เห็นได้ว่าสูตรอาหารที่มีนมถูกกรองออก หากคุณแพ้แลคโตส คุณอาจจะกรองสูตรอาหารที่มีชีสด้วย ดังนั้นจึงจำเป็นต้องระบุให้ชัดเจน

- **สร้างรายการของชำ** เราต้องการสร้างรายการของชำโดยพิจารณาสิ่งที่เรามีที่บ้านแล้ว

  สำหรับฟังก์ชันนี้ เราอาจลองแก้ไขทุกอย่างใน prompt เดียว หรือแยกเป็นสอง prompt มาลองวิธีหลัง ซึ่งเราจะเพิ่ม prompt เพิ่มเติม แต่เพื่อให้ได้ผล เราต้องเพิ่มผลลัพธ์จาก prompt แรกเป็นบริบทของ prompt ที่สอง

  หาโค้ดส่วนที่พิมพ์ผลลัพธ์จาก prompt แรกและเพิ่มโค้ดต่อไปนี้ด้านล่าง:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  สังเกตดังนี้:

  1. เราสร้าง prompt ใหม่โดยเพิ่มผลลัพธ์จาก prompt แรกเข้าไปใน prompt ใหม่:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. เราส่งคำขอใหม่ โดยพิจารณาจำนวน tokens ที่เราขอใน prompt แรก ดังนั้นครั้งนี้เราระบุ `max_output_tokens` เป็น 1200

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     เมื่อนำโค้ดนี้มาทดสอบ เราจะได้ผลลัพธ์ดังนี้:

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

สิ่งที่เรามีจนถึงตอนนี้คือโค้ดที่ทำงานได้ แต่มีบางอย่างที่เราควรปรับแต่งเพื่อปรับปรุงไปได้มากขึ้น สิ่งที่เราควรทำได้แก่:

- **แยกความลับออกจากโค้ด** เช่น คีย์ API ความลับไม่ควรอยู่ในโค้ดและควรถูกเก็บไว้ในสถานที่ที่ปลอดภัย เพื่อแยกความลับออกจากโค้ด เราสามารถใช้ตัวแปรสภาพแวดล้อมและไลบรารีอย่าง `python-dotenv` เพื่อโหลดจากไฟล์ นี่คือตัวอย่างโค้ด:

  1. สร้างไฟล์ `.env` ที่มีเนื้อหาดังนี้:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > หมายเหตุ สำหรับ Azure OpenAI ใน Microsoft Foundry คุณจำเป็นต้องตั้งค่าตัวแปรสภาพแวดล้อมดังนี้แทน:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     ในโค้ด คุณจะโหลดตัวแปรสภาพแวดล้อมได้แบบนี้:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **เรื่องของความยาวโทเค็น** เราควรพิจารณาว่าเราต้องใช้โทเค็นจำนวนเท่าใดเพื่อสร้างข้อความที่ต้องการ โทเค็นมีค่าใช้จ่าย ดังนั้นถ้าเป็นไปได้ควรประหยัดจำนวนโทเค็นที่ใช้ เช่น เราสามารถปรับแต่งข้อความแจ้งให้ใช้โทเค็นน้อยลงได้หรือไม่?

  เพื่อเปลี่ยนจำนวนโทเค็นที่ใช้ คุณสามารถใช้พารามิเตอร์ `max_output_tokens` เช่น ถ้าคุณต้องการใช้ 100 โทเค็น คุณจะทำแบบนี้:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **ทดลองใช้ค่า temperature** ค่าสำหรับ temperature เป็นสิ่งที่เรายังไม่เคยพูดถึงมาก่อน แต่มันสำคัญสำหรับการทำงานของโปรแกรม ยิ่งค่า temperature สูง ผลลัพธ์จะยิ่งสุ่มมากขึ้น ในขณะที่ค่าต่ำจะทำให้ผลลัพธ์ที่ได้คาดเดาได้มากขึ้น พิจารณาว่าคุณต้องการให้ผลงานของคุณมีความหลากหลายหรือไม่

  เพื่อปรับเปลี่ยนค่า temperature คุณสามารถใช้พารามิเตอร์ `temperature` เช่น ถ้าคุณต้องการใช้ temperature ที่ 0.5 คุณจะทำแบบนี้:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > หมายเหตุ ยิ่งค่าใกล้ 1.0 ผลลัพธ์จะยิ่งหลากหลายมากขึ้น

- **โมเดลสำหรับการให้เหตุผลไม่ใช้ `temperature`** นี่คือการเปลี่ยนแปลงสำคัญในปี 2026 โมเดลปัจจุบันที่ไม่เลิกใช้งานบน Microsoft Foundry คือ **โมเดลสำหรับการให้เหตุผล** (ตระกูล GPT-5, ซีรีส์ o) - และพวกมัน **ไม่รองรับ `temperature` หรือ `top_p`** (รวมถึงไม่รองรับ `max_tokens`; ให้ใช้ `max_output_tokens` แทน) หากคุณส่ง `temperature` ไปที่ `gpt-5-mini` คุณจะได้รับข้อผิดพลาด "พารามิเตอร์ไม่รองรับ" ดังนั้นถ้าต้องการลองใช้ตัวอย่าง temperature ข้างต้น ให้เลือกโมเดลที่ยังรองรับการควบคุมการสุ่ม เช่น โมเดล Llama แบบเปิดอย่าง `Llama-3.3-70B-Instruct` จาก [Microsoft Foundry model catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) เรียกใช้งานผ่าน Foundry Models / Azure AI Inference endpoint (เช่นเดียวกับตัวอย่าง `githubmodels-*`) สำหรับโมเดลให้เหตุผลอย่าง GPT-5 คุณควบคุมผลลัพธ์ต่างออกไป:
  - **การออกแบบ prompt** - คำสั่งที่ชัดเจน ตัวอย่าง และผลลัพธ์ที่มีโครงสร้าง (ดูบทเรียน [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) ทดแทนการใช้อุปกรณ์ควบคุมการสุ่ม
  - **การควบคุมเหตุผล** - พารามิเตอร์เช่นความพยายามให้เหตุผล/ความละเอียดช่วยปรับสมดุลระหว่างความลึกของเหตุผลกับความหน่วงและต้นทุน

  สรุป: `temperature`/`top_p` ยังใช้ได้กับโมเดลหลายตัว (Llama, Mistral, Phi และกลุ่ม GPT-4.x - แม้ GPT-4.x จะกำลังเลิกใช้งาน) แต่แนวทางคือการออกแบบ prompt ร่วมกับการควบคุมเหตุผลในโมเดลให้เหตุผลเช่น GPT-5

## งานที่มอบหมาย

สำหรับงานนี้คุณสามารถเลือกสร้างสิ่งที่ต้องการได้

นี่คือข้อเสนอแนะบางอย่าง:

- ปรับแต่งแอปสร้างสูตรอาหารให้ดีขึ้น เล่นกับค่า temperature และข้อความแจ้งเพื่อดูสิ่งที่คุณพัฒนาได้
- สร้าง "เพื่อนเรียนรู้" แอปนี้ควรตอบคำถามเกี่ยวกับหัวข้อ เช่น Python คุณอาจมี prompt อย่าง "อะไรคือหัวข้อหนึ่งใน Python?" หรือ prompt ที่ขอให้แสดงโค้ดหัวข้อนั้น ๆ เป็นต้น
- บอทประวัติศาสตร์ ทำให้ประวัติศาสตร์มีชีวิต สั่งให้บอทสวมบทเป็นตัวละครประวัติศาสตร์ตัวหนึ่งและถามคำถามเกี่ยวกับชีวิตและยุคสมัยของตัวละครนั้น

## ตัวอย่างวิธีแก้ไข

### เพื่อนเรียนรู้

ด้านล่างนี้คือ prompt เริ่มต้น ลองใช้ดูและปรับแต่งตามชอบใจ

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### บอทประวัติศาสตร์

นี่คือข้อความแจ้งที่คุณอาจใช้ได้:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## ตรวจสอบความรู้

คอนเซปต์ temperature มีหน้าที่อะไร?

1. ควบคุมความสุ่มของผลลัพธ์
1. ควบคุมขนาดของการตอบกลับ
1. ควบคุมจำนวนโทเค็นที่ใช้

## 🚀 ความท้าทาย

ขณะทำงานตามมอบหมาย พยายามเปลี่ยนค่า temperature ตั้งเป็น 0, 0.5 และ 1 จำไว้ว่าค่า 0 คือความหลากหลายน้อยที่สุด และ 1 คือมากที่สุด ค่าใดเหมาะกับแอปของคุณที่สุด?

## ทำได้ดีมาก! เรียนรู้ต่อเนื่อง

หลังจากเรียนบทเรียนนี้เสร็จแล้ว ลองดู [คอลเลกชันเรียนรู้ Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) เพื่อยกระดับความรู้ด้าน Generative AI ของคุณต่อไป!

ไปที่บทเรียน 7 ซึ่งเราจะเรียนรู้วิธี [สร้างแอปแชท](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->