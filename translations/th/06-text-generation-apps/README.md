<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-05-19T16:58:57+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "th"
}
-->
# การสร้างแอปพลิเคชันสร้างข้อความ

[![การสร้างแอปพลิเคชันสร้างข้อความ](../../../translated_images/06-lesson-banner.90d8a665630e46b2990412d7c7d3d43c30f2441c95c0ee93e0763fb252734e83.th.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(คลิกที่ภาพด้านบนเพื่อดูวิดีโอของบทเรียนนี้)_

คุณได้เห็นแล้วว่าในหลักสูตรนี้มีแนวคิดหลัก ๆ เช่น prompt และแม้กระทั่งสาขาที่เรียกว่า "การจัดการ prompt" เครื่องมือหลายอย่างที่คุณสามารถโต้ตอบได้ เช่น ChatGPT, Office 365, Microsoft Power Platform และอื่น ๆ รองรับการใช้ prompt เพื่อทำสิ่งต่าง ๆ

หากคุณต้องการเพิ่มประสบการณ์ดังกล่าวลงในแอป คุณต้องเข้าใจแนวคิดเช่น prompt, completions และเลือกไลบรารีที่จะใช้ ซึ่งเป็นสิ่งที่คุณจะได้เรียนรู้ในบทนี้

## บทนำ

ในบทนี้ คุณจะ:

- เรียนรู้เกี่ยวกับไลบรารี openai และแนวคิดหลักของมัน
- สร้างแอปสร้างข้อความโดยใช้ openai
- เข้าใจวิธีการใช้แนวคิดเช่น prompt, temperature, และ tokens เพื่อสร้างแอปสร้างข้อความ

## เป้าหมายการเรียนรู้

เมื่อจบบทเรียนนี้ คุณจะสามารถ:

- อธิบายว่าแอปสร้างข้อความคืออะไร
- สร้างแอปสร้างข้อความโดยใช้ openai
- กำหนดค่าแอปของคุณเพื่อใช้ tokens มากหรือน้อยและเปลี่ยนแปลง temperature เพื่อให้ได้ผลลัพธ์ที่หลากหลาย

## แอปสร้างข้อความคืออะไร?

โดยปกติเมื่อคุณสร้างแอป มันจะมีอินเตอร์เฟซบางอย่างเช่น:

- คำสั่งพื้นฐาน แอปคอนโซลเป็นแอปทั่วไปที่คุณพิมพ์คำสั่งและมันจะดำเนินการตามคำสั่งนั้น ตัวอย่างเช่น `git` เป็นแอปที่ใช้คำสั่งพื้นฐาน
- อินเตอร์เฟซผู้ใช้ (UI) บางแอปมีอินเตอร์เฟซผู้ใช้แบบกราฟิก (GUI) ที่คุณคลิกปุ่ม, ป้อนข้อความ, เลือกตัวเลือกและอื่น ๆ

### แอปคอนโซลและ UI มีข้อจำกัด

เปรียบเทียบกับแอปที่ใช้คำสั่งพื้นฐานที่คุณพิมพ์คำสั่ง:

- **มีข้อจำกัด** คุณไม่สามารถพิมพ์คำสั่งใด ๆ ได้ตามใจชอบ มีเพียงคำสั่งที่แอปรองรับเท่านั้น
- **ภาษาที่เฉพาะเจาะจง** บางแอปรองรับหลายภาษา แต่โดยปกติแอปจะถูกสร้างขึ้นสำหรับภาษาที่เฉพาะเจาะจง แม้ว่าคุณจะสามารถเพิ่มการรองรับภาษาเพิ่มเติมได้

### ข้อดีของแอปสร้างข้อความ

แล้วแอปสร้างข้อความแตกต่างอย่างไร?

ในแอปสร้างข้อความ คุณมีความยืดหยุ่นมากขึ้น ไม่จำกัดเฉพาะชุดคำสั่งหรือภาษาป้อนข้อมูลเฉพาะ คุณสามารถใช้ภาษาธรรมชาติในการโต้ตอบกับแอป ข้อดีอีกอย่างคือเนื่องจากคุณกำลังโต้ตอบกับแหล่งข้อมูลที่ได้รับการฝึกอบรมจากข้อมูลจำนวนมาก ในขณะที่แอปแบบดั้งเดิมอาจถูกจำกัดด้วยสิ่งที่อยู่ในฐานข้อมูล

### ฉันสามารถสร้างอะไรได้บ้างด้วยแอปสร้างข้อความ?

มีหลายสิ่งที่คุณสามารถสร้างได้ ตัวอย่างเช่น:

- **แชทบอท** แชทบอทตอบคำถามเกี่ยวกับหัวข้อต่าง ๆ เช่น บริษัทและผลิตภัณฑ์ของคุณอาจเป็นตัวเลือกที่ดี
- **ตัวช่วย** LLMs เก่งในการสรุปข้อความ, การหาข้อมูลจากข้อความ, การสร้างข้อความเช่นประวัติการทำงานและอื่น ๆ
- **ผู้ช่วยเขียนโค้ด** ขึ้นอยู่กับโมเดลภาษาที่คุณใช้ คุณสามารถสร้างผู้ช่วยเขียนโค้ดที่ช่วยคุณเขียนโค้ด ตัวอย่างเช่น คุณสามารถใช้ผลิตภัณฑ์เช่น GitHub Copilot รวมถึง ChatGPT เพื่อช่วยคุณเขียนโค้ด

## ฉันจะเริ่มต้นได้อย่างไร?

คุณต้องหาวิธีการรวมกับ LLM ซึ่งมักจะมีสองวิธีดังนี้:

- ใช้ API ในที่นี้คุณกำลังสร้างคำขอเว็บพร้อมกับ prompt ของคุณและรับข้อความที่สร้างขึ้นกลับมา
- ใช้ไลบรารี ไลบรารีช่วยห่อหุ้มการเรียก API และทำให้ง่ายต่อการใช้งาน

## ไลบรารี/SDKs

มีไลบรารีที่เป็นที่รู้จักดีสำหรับการทำงานกับ LLMs เช่น:

- **openai** ไลบรารีนี้ทำให้ง่ายต่อการเชื่อมต่อกับโมเดลของคุณและส่ง prompt เข้าไป

จากนั้นมีไลบรารีที่ทำงานในระดับสูงกว่าเช่น:

- **Langchain** Langchain เป็นที่รู้จักดีและรองรับ Python
- **Semantic Kernel** Semantic Kernel เป็นไลบรารีโดย Microsoft ที่รองรับภาษา C#, Python, และ Java

## แอปแรกที่ใช้ openai

มาดูกันว่าเราสามารถสร้างแอปแรกของเราได้อย่างไร ไลบรารีที่เราต้องการใช้มีอะไรบ้างและต้องการอะไรบ้าง

### ติดตั้ง openai

มีไลบรารีมากมายสำหรับการโต้ตอบกับ OpenAI หรือ Azure OpenAI คุณสามารถใช้ภาษาการเขียนโปรแกรมหลายภาษาได้เช่น C#, Python, JavaScript, Java และอื่น ๆ เราเลือกใช้ไลบรารี `openai` Python ดังนั้นเราจะใช้ `pip` เพื่อติดตั้งมัน

```bash
pip install openai
```

### สร้างทรัพยากร

คุณต้องดำเนินการตามขั้นตอนต่อไปนี้:

- สร้างบัญชีบน Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)
- เข้าถึง Azure OpenAI ไปที่ [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) และขอการเข้าถึง

  > [!NOTE]
  > ในขณะที่เขียนนี้ คุณต้องสมัครเพื่อเข้าถึง Azure OpenAI

- ติดตั้ง Python <https://www.python.org/>
- ได้สร้างทรัพยากร Azure OpenAI Service ดูคำแนะนำนี้เกี่ยวกับวิธีการ [สร้างทรัพยากร](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)

### ค้นหาคีย์ API และ endpoint

ในจุดนี้ คุณต้องบอกไลบรารี `openai` ของคุณว่าจะใช้คีย์ API ใด ในการหาคีย์ API ของคุณ ไปที่ส่วน "Keys and Endpoint" ของทรัพยากร Azure OpenAI ของคุณและคัดลอกค่าของ "Key 1"

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

ตอนนี้คุณมีข้อมูลนี้คัดลอกแล้ว มาสั่งให้ไลบรารีใช้มันกันเถอะ

> [!NOTE]
> ควรแยกคีย์ API ของคุณออกจากโค้ด คุณสามารถทำได้โดยใช้ตัวแปรสภาพแวดล้อม
>
> - ตั้งค่าตัวแปรสภาพแวดล้อม `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'`

### ตั้งค่าการกำหนดค่า Azure

หากคุณใช้ Azure OpenAI นี่คือวิธีการตั้งค่าการกำหนดค่า:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

ด้านบนเรากำลังตั้งค่าต่อไปนี้:

- `api_type` to `azure`. This tells the library to use Azure OpenAI and not OpenAI.
- `api_key`, this is your API key found in the Azure Portal.
- `api_version`, this is the version of the API you want to use. At the time of writing, the latest version is `2023-05-15`.
- `api_base`, this is the endpoint of the API. You can find it in the Azure Portal next to your API key.

> [!NOTE] > `os.getenv` is a function that reads environment variables. You can use it to read environment variables like `OPENAI_API_KEY` and `API_BASE`. Set these environment variables in your terminal or by using a library like `dotenv`.

## Generate text

The way to generate text is to use the `Completion` class นี่คือตัวอย่าง:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

ในโค้ดด้านบน เราสร้างอ็อบเจ็กต์ completion และส่งโมเดลที่เราต้องการใช้และ prompt จากนั้นเราพิมพ์ข้อความที่สร้างขึ้น

### Chat completions

จนถึงตอนนี้ คุณได้เห็นว่าเราใช้ `Completion` to generate text. But there's another class called `ChatCompletion` ที่เหมาะสมกว่าสำหรับแชทบอท นี่คือตัวอย่างการใช้มัน:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

รายละเอียดเพิ่มเติมเกี่ยวกับฟังก์ชันนี้ในบทต่อไป

## แบบฝึกหัด - แอปสร้างข้อความแรกของคุณ

ตอนนี้เราได้เรียนรู้วิธีการตั้งค่าและกำหนดค่า openai แล้ว ถึงเวลาสร้างแอปสร้างข้อความแรกของคุณ ในการสร้างแอปของคุณ ให้ทำตามขั้นตอนเหล่านี้:

1. สร้างสภาพแวดล้อมเสมือนและติดตั้ง openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > หากคุณใช้ Windows ให้พิมพ์ `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1` value

1. สร้างไฟล์ _app.py_ และใส่โค้ดต่อไปนี้:

   ```python
   import openai

   openai.api_key = "<replace this value with your open ai key or Azure OpenAI key>"

   openai.api_type = 'azure'
   openai.api_version = '2023-05-15'
   openai.api_base = "<endpoint found in Azure Portal where your API key is>"
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"
   messages = [{"role": "user", "content": prompt}]

   # make completion
   completion = openai.chat.completions.create(model=deployment_name, messages=messages)

   # print response
   print(completion.choices[0].message.content)
   ```

   > [!NOTE]
   > หากคุณใช้ Azure OpenAI คุณต้องตั้งค่า `api_type` to `azure` and set the `api_key` เป็นคีย์ Azure OpenAI ของคุณ

   คุณควรเห็นผลลัพธ์เช่นต่อไปนี้:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## ประเภทของ prompt ที่แตกต่างกันสำหรับสิ่งต่าง ๆ

ตอนนี้คุณได้เห็นวิธีการสร้างข้อความโดยใช้ prompt แล้ว คุณยังมีโปรแกรมที่ทำงานอยู่ที่คุณสามารถปรับแต่งและเปลี่ยนแปลงเพื่อสร้างข้อความประเภทต่าง ๆ ได้

Prompt สามารถใช้สำหรับงานต่าง ๆ ได้ ตัวอย่างเช่น:

- **สร้างประเภทของข้อความ** ตัวอย่างเช่น คุณสามารถสร้างบทกวี คำถามสำหรับการสอบ เป็นต้น
- **ค้นหาข้อมูล** คุณสามารถใช้ prompt เพื่อค้นหาข้อมูล เช่น ตัวอย่างต่อไปนี้ 'CORS หมายถึงอะไรในเว็บดีเวลอปเมนต์?'
- **สร้างโค้ด** คุณสามารถใช้ prompt เพื่อสร้างโค้ด เช่น การพัฒนานิพจน์ปกติที่ใช้ในการตรวจสอบอีเมลหรือทำไมไม่สร้างโปรแกรมทั้งหมด เช่น เว็บแอป?

## กรณีการใช้งานที่เป็นประโยชน์มากขึ้น: ตัวสร้างสูตรอาหาร

ลองนึกภาพว่าคุณมีวัตถุดิบที่บ้านและต้องการทำอาหารบางอย่าง สำหรับนั้น คุณต้องการสูตรอาหาร วิธีหนึ่งในการหาสูตรอาหารคือการใช้เครื่องมือค้นหาหรือคุณอาจใช้ LLM เพื่อทำเช่นนั้น

คุณอาจเขียน prompt แบบนี้:

> "แสดงสูตรอาหาร 5 สูตรสำหรับจานที่มีส่วนผสมดังต่อไปนี้: ไก่, มันฝรั่ง, และแครอท ต่อสูตร ให้แสดงรายการส่วนผสมทั้งหมดที่ใช้"

จาก prompt ข้างต้น คุณอาจได้รับการตอบสนองที่คล้ายกัน:

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

ผลลัพธ์นี้ยอดเยี่ยม ฉันรู้ว่าควรทำอะไรตอนนี้ สิ่งที่อาจจะเป็นการปรับปรุงที่มีประโยชน์คือ:

- การกรองส่วนผสมที่ฉันไม่ชอบหรือแพ้
- สร้างรายการช็อปปิ้ง ในกรณีที่ฉันไม่มีส่วนผสมทั้งหมดที่บ้าน

สำหรับกรณีข้างต้น ให้เพิ่ม prompt เพิ่มเติม:

> "กรุณาลบสูตรที่มีส่วนผสมของกระเทียมเพราะฉันแพ้และแทนที่ด้วยอย่างอื่น และโปรดสร้างรายการช็อปปิ้งสำหรับสูตรอาหาร โดยพิจารณาว่าฉันมีไก่, มันฝรั่ง และแครอทที่บ้านแล้ว"

ตอนนี้คุณมีผลลัพธ์ใหม่ ได้แก่:

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

นั่นคือสูตรอาหารทั้งห้าของคุณ โดยไม่มีการกล่าวถึงกระเทียมและคุณยังมีรายการช็อปปิ้งที่พิจารณาสิ่งที่คุณมีที่บ้านแล้ว

## แบบฝึกหัด - สร้างตัวสร้างสูตรอาหาร

ตอนนี้เราได้เล่นสถานการณ์ออกมาแล้ว มาลองเขียนโค้ดให้ตรงกับสถานการณ์ที่แสดงกันเถอะ ในการทำเช่นนั้น ให้ทำตามขั้นตอนเหล่านี้:

1. ใช้ไฟล์ _app.py_ ที่มีอยู่เป็นจุดเริ่มต้น
1. ค้นหาตัวแปร `prompt` และเปลี่ยนโค้ดของมันเป็นดังนี้:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   หากคุณรันโค้ดตอนนี้ คุณควรเห็นผลลัพธ์ที่คล้ายกับ:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > หมายเหตุ LLM ของคุณไม่แน่นอน ดังนั้นคุณอาจได้รับผลลัพธ์ที่แตกต่างกันทุกครั้งที่คุณรันโปรแกรม

   เยี่ยม มาดูกันว่าเราจะปรับปรุงสิ่งต่าง ๆ ได้อย่างไร ในการปรับปรุงสิ่งต่าง ๆ เราต้องการให้แน่ใจว่าโค้ดยืดหยุ่น ดังนั้นส่วนผสมและจำนวนสูตรสามารถปรับปรุงและเปลี่ยนแปลงได้

1. มาปรับเปลี่ยนโค้ดดังนี้:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   การทดสอบโค้ดนี้อาจมีลักษณะดังนี้:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### ปรับปรุงโดยการเพิ่มตัวกรองและรายการช็อปปิ้ง

ตอนนี้เรามีแอปที่ทำงานได้แล้วที่สามารถผลิตสูตรอาหารและยืดหยุ่นได้เนื่องจากพึ่งพาข้อมูลจากผู้ใช้ทั้งในจำนวนสูตรและส่วนผสมที่ใช้

เพื่อปรับปรุงเพิ่มเติม เราต้องการเพิ่มสิ่งต่อไปนี้:

- **กรองส่วนผสม** เราต้องการความสามารถในการกรองส่วนผสมที่เราไม่ชอบหรือแพ้ เพื่อทำการเปลี่ยนแปลงนี้ เราสามารถแก้ไข prompt ที่มีอยู่และเพิ่มเงื่อนไขการกรองที่ท้ายสุดเช่นนี้:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  ด้านบนเราเพิ่ม `{filter}` ที่ท้าย prompt และเรายังจับค่าของตัวกรองจากผู้ใช้

  ตัวอย่างการป้อนข้อมูลของการรันโปรแกรมอาจมีลักษณะดังนี้:

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

  ดังที่คุณเห็น สูตรใด ๆ ที่มีนมในนั้นถูกกรองออก แต่ถ้าคุณแพ้แลคโตส คุณอาจต้องการกรองสูตรที่มีชีสในนั้นด้วย ดังนั้นจึงมีความจำเป็นต้องชัดเจน

- **สร้างรายการช็อปปิ้ง** เราต้องการสร้างรายการช็อปปิ้ง โดยพิจารณาสิ่งที่เรามีที่บ้านแล้ว

  สำหรับฟังก์ชันนี้ เราอาจพยายามแก้ไขทุกอย่างใน prompt เดียวหรือเราอาจแบ่งมันออกเป็นสอง prompt ลองใช้วิธีหลังกัน ในที่นี้เราเสนอให้เพิ่ม prompt เพิ่มเติม แต่สำหรับนั้นที่จะทำงานได้ เราจำเป็นต้องเพิ่มผลลัพธ์จาก prompt แรกเป็นบริบทให้กับ prompt ที่สอง

  ค้นหาส่วนในโค้ดที่พิมพ์ผลลัพธ์จาก prompt แรกและเพิ่มโค้ดต่อไปนี้ด้านล่าง:

  ```python
  old_prompt_result = completion.choices[0].message.content
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  messages = [{"role": "user", "content": new_prompt}]
  completion = openai.Completion.create(engine=deployment_name, messages=messages, max_tokens=1200)

  # print response
  print("Shopping list:")
  print(completion.choices[0].message.content)
  ```

  หมายเหตุสิ่งต่อไปนี้:

  1. เรากำลังสร้าง prompt ใหม่โดยการเพิ่มผลลัพธ์จาก prompt แรกไปยัง prompt ใหม่:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. เราทำการร้องขอใหม่ แต่ยังพิจารณาจำนวน tokens ที่เราถามหาใน prompt แรก ดังนั้นครั้งนี้เราบอกว่า `max_tokens` คือ 1200

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     การทดสอบโค้ดนี้เราจะได้ผลลัพธ์ดังนี้:

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

สิ่งที่เรามีอยู่ตอนนี้คือโค้ดที่ทำงานได้ แต่มีการปรับแต่งบางอย่างที่เราควรทำเพื่อปรับปรุงสิ่งต่าง ๆ ให้ดียิ่งขึ้น สิ่งที่เราควรทำคือ:

- **แยกความลับออกจากโค้ด** เช่น คีย์ API ความลับไม่ควรอยู่ในโค้ดและควรเก็บไว้ในที่ปลอดภัย เพื่อแยกความลับออกจากโค้ด เราสามารถใช้ตัวแปรสภาพแวดล้อมและไลบรารีเช่น `python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env` ไฟล์ที่มีเนื้อหาดังนี้:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > หมายเหตุ สำหรับ Azure คุณต้องตั้งค่าตัวแปรสภาพแวดล้อมดังนี้:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     ในโค้ด คุณจะโหลดตัวแปรสภาพแวดล้อมดังนี้:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **คำแนะนำเกี่ยวกับความยาวของ token** เราควรพิจารณาว่าเราต้องการใช้ token จำนวนเท่าใดในการสร้างข้อความที่เราต้องการ Tokens มีค่าใช้จ่าย ดังนั้นหากเป็นไปได้เราควรพยายามใช้ token อย่างประหยัด ตัวอย่างเช่น

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้องมากที่สุด แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถูกพิจารณาว่าเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่มีความสำคัญ แนะนำให้ใช้การแปลโดยมืออาชีพ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้