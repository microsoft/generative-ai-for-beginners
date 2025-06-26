<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-06-25T14:27:59+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "th"
}
-->
# การสร้างแอปพลิเคชันสร้างข้อความ

คุณได้เห็นแล้วในหลักสูตรนี้ว่ามีแนวคิดหลักๆ เช่น prompt และแม้กระทั่งวิชา "prompt engineering" ที่สมบูรณ์แบบ เครื่องมือต่างๆ ที่คุณสามารถโต้ตอบด้วย เช่น ChatGPT, Office 365, Microsoft Power Platform และอื่นๆ สนับสนุนการใช้ prompt เพื่อทำสิ่งต่างๆ ให้สำเร็จ

สำหรับคุณที่จะเพิ่มประสบการณ์แบบนี้ในแอป คุณจำเป็นต้องเข้าใจแนวคิดอย่าง prompt, completions และเลือกไลบรารีที่จะทำงานด้วย ซึ่งเป็นสิ่งที่คุณจะได้เรียนรู้ในบทนี้

## บทนำ

ในบทนี้ คุณจะ:

- เรียนรู้เกี่ยวกับไลบรารี openai และแนวคิดหลักๆ ของมัน
- สร้างแอปพลิเคชันสร้างข้อความโดยใช้ openai
- เข้าใจวิธีใช้แนวคิดอย่าง prompt, temperature และ tokens เพื่อสร้างแอปพลิเคชันสร้างข้อความ

## เป้าหมายการเรียนรู้

เมื่อจบบทเรียนนี้ คุณจะสามารถ:

- อธิบายว่าแอปพลิเคชันสร้างข้อความคืออะไร
- สร้างแอปพลิเคชันสร้างข้อความโดยใช้ openai
- กำหนดค่าแอปของคุณเพื่อใช้ tokens มากหรือน้อย และเปลี่ยน temperature เพื่อให้ได้ผลลัพธ์ที่หลากหลาย

## แอปพลิเคชันสร้างข้อความคืออะไร?

โดยปกติเมื่อคุณสร้างแอป มันจะมีอินเทอร์เฟซบางอย่างเช่นต่อไปนี้:

- แบบคำสั่ง แอปคอนโซลเป็นแอปทั่วไปที่คุณพิมพ์คำสั่งและมันจะทำงานตามที่สั่ง ตัวอย่างเช่น `git` เป็นแอปแบบคำสั่ง
- อินเทอร์เฟซผู้ใช้ (UI) บางแอปมีอินเทอร์เฟซผู้ใช้แบบกราฟิก (GUI) ที่คุณคลิกปุ่ม, ป้อนข้อความ, เลือกตัวเลือก และอื่นๆ

### แอปคอนโซลและ UI มีข้อจำกัด

เปรียบเทียบกับแอปแบบคำสั่งที่คุณพิมพ์คำสั่ง:

- **มันมีข้อจำกัด** คุณไม่สามารถพิมพ์คำสั่งใดๆ ได้ เพียงแค่คำสั่งที่แอปรองรับ
- **เฉพาะเจาะจงกับภาษา** บางแอปรองรับหลายภาษา แต่โดยปกติแอปถูกสร้างสำหรับภาษาหนึ่งๆ ถึงแม้ว่าคุณจะสามารถเพิ่มการรองรับภาษาเพิ่มเติมได้

### ประโยชน์ของแอปพลิเคชันสร้างข้อความ

แอปพลิเคชันสร้างข้อความแตกต่างอย่างไร?

ในแอปพลิเคชันสร้างข้อความ คุณมีความยืดหยุ่นมากขึ้น ไม่ถูกจำกัดด้วยชุดคำสั่งหรือภาษาป้อนข้อมูลเฉพาะ คุณสามารถใช้ภาษาธรรมชาติเพื่อโต้ตอบกับแอปได้ อีกประโยชน์คือคุณกำลังโต้ตอบกับแหล่งข้อมูลที่ได้รับการฝึกอบรมด้วยข้อมูลจำนวนมาก ในขณะที่แอปทั่วไปอาจถูกจำกัดด้วยสิ่งที่อยู่ในฐานข้อมูล

### ฉันสามารถสร้างอะไรกับแอปพลิเคชันสร้างข้อความได้บ้าง?

มีหลายสิ่งที่คุณสามารถสร้างได้ ตัวอย่างเช่น:

- **แชทบอท** แชทบอทที่ตอบคำถามเกี่ยวกับหัวข้อต่างๆ เช่น บริษัทของคุณและผลิตภัณฑ์ของมันอาจเป็นตัวเลือกที่ดี
- **ผู้ช่วย** LLMs เก่งในการสรุปข้อความ, ได้รับข้อมูลเชิงลึกจากข้อความ, ผลิตข้อความเช่นเรซูเม่ และอื่นๆ
- **ผู้ช่วยเขียนโค้ด** ขึ้นอยู่กับโมเดลภาษา คุณสามารถสร้างผู้ช่วยเขียนโค้ดที่ช่วยคุณเขียนโค้ดได้ ตัวอย่างเช่น คุณสามารถใช้ผลิตภัณฑ์เช่น GitHub Copilot รวมถึง ChatGPT เพื่อช่วยคุณเขียนโค้ด

## ฉันจะเริ่มต้นได้อย่างไร?

คุณต้องหาวิธีรวมเข้ากับ LLM ซึ่งมักจะมีสองวิธีดังนี้:

- ใช้ API คุณจะสร้างคำขอเว็บด้วย prompt ของคุณและได้รับข้อความที่สร้างขึ้นกลับมา
- ใช้ไลบรารี ไลบรารีช่วย encapsulate คำขอ API และทำให้ง่ายต่อการใช้งาน

## ไลบรารี/SDKs

มีไลบรารีที่รู้จักกันดีหลายตัวสำหรับทำงานกับ LLMs เช่น:

- **openai** ไลบรารีนี้ทำให้การเชื่อมต่อกับโมเดลของคุณและส่ง prompt ง่ายขึ้น

จากนั้นมีไลบรารีที่ทำงานในระดับสูงกว่าเช่น:

- **Langchain** Langchain เป็นที่รู้จักกันดีและรองรับ Python
- **Semantic Kernel** Semantic Kernel เป็นไลบรารีของ Microsoft ที่รองรับภาษา C#, Python และ Java

## แอปแรกโดยใช้ openai

มาดูกันว่าเราจะสร้างแอปแรกได้อย่างไร ไลบรารีที่เราต้องการ และอื่นๆ

### ติดตั้ง openai

มีไลบรารีหลายตัวสำหรับการโต้ตอบกับ OpenAI หรือ Azure OpenAI สามารถใช้ภาษาโปรแกรมหลายภาษาได้ เช่น C#, Python, JavaScript, Java และอื่นๆ เราเลือกใช้ไลบรารี Python `openai` ดังนั้นเราจะใช้ `pip` เพื่อติดตั้งมัน

```bash
pip install openai
```

### สร้างทรัพยากร

คุณต้องดำเนินการตามขั้นตอนต่อไปนี้:

- สร้างบัญชีบน Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)
- เข้าถึง Azure OpenAI ไปที่ [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) และขอการเข้าถึง

  > [!NOTE]
  > ณ เวลาที่เขียน คุณต้องสมัครเพื่อเข้าถึง Azure OpenAI

- ติดตั้ง Python <https://www.python.org/>
- สร้างทรัพยากร Azure OpenAI Service ดูคำแนะนำนี้สำหรับวิธี [สร้างทรัพยากร](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)

### ค้นหา API key และ endpoint

ในจุดนี้ คุณต้องบอกไลบรารี `openai` ของคุณว่าใช้ API key อะไร ในการค้นหา API key ของคุณ ไปที่ส่วน "Keys and Endpoint" ของทรัพยากร Azure OpenAI ของคุณและคัดลอกค่า "Key 1"

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

ตอนนี้คุณมีข้อมูลนี้แล้ว ให้เราบอกไลบรารีให้ใช้มัน

> [!NOTE]
> ควรแยก API key ออกจากโค้ดของคุณ คุณสามารถทำได้โดยใช้ environment variables
>
> - ตั้งค่า environment variable `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'`

### ตั้งค่าคอนฟิก Azure

ถ้าคุณใช้ Azure OpenAI นี่คือวิธีตั้งค่าคอนฟิก:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

ด้านบนเรากำลังตั้งค่าดังต่อไปนี้:

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

ในโค้ดด้านบน เราสร้างวัตถุ completion และส่งโมเดลที่เราต้องการใช้และ prompt จากนั้นเราพิมพ์ข้อความที่สร้างขึ้น

### การทำงานของ Chat

จนถึงตอนนี้ คุณได้เห็นวิธีที่เราใช้ `Completion` to generate text. But there's another class called `ChatCompletion` ที่เหมาะสมกว่าสำหรับแชทบอท นี่คือตัวอย่างการใช้มัน:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

เพิ่มเติมเกี่ยวกับฟังก์ชันนี้ในบทต่อไป

## แบบฝึกหัด - แอปพลิเคชันสร้างข้อความแรกของคุณ

ตอนนี้เราได้เรียนรู้วิธีตั้งค่าและกำหนดค่า openai แล้ว ถึงเวลาสร้างแอปพลิเคชันสร้างข้อความแรกของคุณ ในการสร้างแอปของคุณ ทำตามขั้นตอนเหล่านี้:

1. สร้างสภาพแวดล้อมเสมือนและติดตั้ง openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > ถ้าคุณใช้ Windows ให้พิมพ์ `venv\Scripts\activate` instead of `source venv/bin/activate`.

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
   > ถ้าคุณใช้ Azure OpenAI คุณต้องตั้งค่า `api_type` to `azure` and set the `api_key` ให้เป็น Azure OpenAI key ของคุณ

   คุณควรเห็นผลลัพธ์ดังต่อไปนี้:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## ประเภทต่างๆ ของ prompt สำหรับสิ่งต่างๆ

ตอนนี้คุณได้เห็นวิธีการสร้างข้อความโดยใช้ prompt แล้ว คุณยังมีโปรแกรมที่ทำงานอยู่ที่คุณสามารถแก้ไขและเปลี่ยนแปลงเพื่อสร้างข้อความประเภทต่างๆ ได้

Prompt สามารถใช้สำหรับงานต่างๆ ได้ ตัวอย่างเช่น:

- **สร้างประเภทของข้อความ** ตัวอย่างเช่น คุณสามารถสร้างบทกวี, คำถามสำหรับแบบทดสอบ ฯลฯ
- **ค้นหาข้อมูล** คุณสามารถใช้ prompt เพื่อค้นหาข้อมูล เช่น 'CORS หมายถึงอะไรในการพัฒนาเว็บ?'
- **สร้างโค้ด** คุณสามารถใช้ prompt เพื่อสร้างโค้ด เช่น การพัฒนา regular expression ที่ใช้ตรวจสอบอีเมล หรือแม้กระทั่งสร้างโปรแกรมทั้งหมด เช่น เว็บแอป

## กรณีการใช้งานที่เป็นประโยชน์มากขึ้น: ตัวสร้างสูตรอาหาร

ลองนึกภาพว่าคุณมีวัตถุดิบที่บ้านและต้องการทำอาหาร สำหรับนั้นคุณต้องการสูตรอาหาร วิธีหนึ่งในการค้นหาสูตรอาหารคือการใช้เครื่องมือค้นหาหรือคุณสามารถใช้ LLM

คุณสามารถเขียน prompt ได้ดังนี้:

> "แสดง 5 สูตรอาหารสำหรับจานที่มีส่วนผสมดังนี้: ไก่, มันฝรั่ง และแครอท ในแต่ละสูตรให้แสดงรายการส่วนผสมทั้งหมดที่ใช้"

จาก prompt ข้างต้น คุณอาจได้รับการตอบสนองคล้ายกับ:

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

ผลลัพธ์นี้ยอดเยี่ยม ฉันรู้ว่าควรทำอาหารอะไร ในจุดนี้ สิ่งที่อาจเป็นการปรับปรุงที่มีประโยชน์คือ:

- กรองส่วนผสมที่ฉันไม่ชอบหรือแพ้
- สร้างรายการช้อปปิ้งในกรณีที่ฉันไม่มีส่วนผสมทั้งหมดที่บ้าน

สำหรับกรณีข้างต้น ลองเพิ่ม prompt เพิ่มเติม:

> "กรุณาลบสูตรอาหารที่มีส่วนผสมกระเทียมเพราะฉันแพ้ และแทนที่ด้วยอย่างอื่น นอกจากนี้กรุณาสร้างรายการช้อปปิ้งสำหรับสูตรอาหารโดยพิจารณาว่าฉันมีไก่, มันฝรั่ง และแครอทที่บ้านแล้ว"

ตอนนี้คุณมีผลลัพธ์ใหม่คือ:

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

นั่นคือห้าสูตรอาหารของคุณ โดยไม่มีการกล่าวถึงกระเทียมและคุณยังมีรายการช้อปปิ้งที่พิจารณาสิ่งที่คุณมีอยู่แล้วที่บ้าน

## แบบฝึกหัด - สร้างตัวสร้างสูตรอาหาร

ตอนนี้เราได้เล่นสถานการณ์แล้ว ลองเขียนโค้ดให้ตรงกับสถานการณ์ที่แสดงออกมา ในการทำเช่นนั้น ทำตามขั้นตอนเหล่านี้:

1. ใช้ไฟล์ _app.py_ ที่มีอยู่เป็นจุดเริ่มต้น
1. ค้นหาตัวแปร `prompt` และเปลี่ยนโค้ดเป็นดังนี้:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   หากคุณรันโค้ดตอนนี้ คุณควรเห็นผลลัพธ์คล้ายกับ:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > หมายเหตุ, LLM ของคุณไม่แน่นอน ดังนั้นคุณอาจได้รับผลลัพธ์ที่แตกต่างกันทุกครั้งที่คุณรันโปรแกรม

   ยอดเยี่ยม ลองดูว่าเราสามารถปรับปรุงสิ่งต่างๆ ได้อย่างไร ในการปรับปรุงสิ่งต่างๆ เราต้องการให้โค้ดยืดหยุ่น ดังนั้นส่วนผสมและจำนวนสูตรสามารถปรับปรุงและเปลี่ยนแปลงได้

1. ลองเปลี่ยนโค้ดในวิธีดังนี้:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   การทดสอบโค้ดอาจดูเหมือนดังนี้:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### ปรับปรุงโดยการเพิ่มตัวกรองและรายการช้อปปิ้ง

เรามีแอปที่ทำงานได้สามารถผลิตสูตรอาหารและยืดหยุ่นได้เนื่องจากพึ่งพาข้อมูลจากผู้ใช้ทั้งในจำนวนสูตรและส่วนผสมที่ใช้

เพื่อปรับปรุงเพิ่มเติม เราต้องการเพิ่มสิ่งต่อไปนี้:

- **กรองส่วนผสม** เราต้องการความสามารถในการกรองส่วนผสมที่เราไม่ชอบหรือแพ้ ในการดำเนินการเปลี่ยนแปลงนี้ เราสามารถแก้ไข prompt ที่มีอยู่ของเราและเพิ่มเงื่อนไขการกรองที่ท้ายของมันดังนี้:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  ด้านบนเราเพิ่ม `{filter}` ที่ท้าย prompt และเรายังจับค่าตัวกรองจากผู้ใช้

  ตัวอย่างการป้อนข้อมูลของการรันโปรแกรมตอนนี้อาจดูดังนี้:

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

  ดังที่คุณเห็น สูตรใดๆ ที่มีนมอยู่ในนั้นถูกกรองออก แต่ถ้าคุณแพ้นม คุณอาจต้องการกรองสูตรที่มีชีสอยู่ในนั้นด้วย ดังนั้นจึงมีความจำเป็นต้องชัดเจน

- **สร้างรายการช้อปปิ้ง** เราต้องการสร้างรายการช้อปปิ้งโดยพิจารณาจากสิ่งที่เรามีอยู่แล้วที่บ้าน

  สำหรับฟังก์ชันนี้ เราอาจพยายามแก้ปัญหาทั้งหมดใน prompt เดียวหรือเราอาจแยกออกเป็นสอง prompt ลองใช้วิธีหลัง ที่นี่เราเสนอให้เพิ่ม prompt เพิ่มเติม แต่สำหรับให้มันทำงานได้ เราจำเป็นต้องเพิ่มผลลัพธ์จาก prompt แรกเป็นบริบทให้กับ prompt หลัง

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

  โปรดทราบสิ่งต่อไปนี้:

  1. เรากำลังสร้าง prompt ใหม่โดยเพิ่มผลลัพธ์จาก prompt แรกไปยัง prompt ใหม่:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. เราทำคำขอใหม่ แต่ยังพิจารณาจำนวน token ที่เราขอใน prompt แรก ดังนั้นคราวนี้เรากล่าวว่า `max_tokens` คือ 1200

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     การทดสอบโค้ดนี้เรามาถึงผลลัพธ์ดังนี้:

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

สิ่งที่เรามีจนถึงตอนนี้คือโค้ดที่ทำงานได้ แต่มีการปรับแต่งบางอย่างที่เราควรทำเพื่อปรับปรุงสิ่งต่างๆ ให้ดียิ่งขึ้น สิ่งที่เราควรทำคือ:

- **แยกความลับออกจากโค้ด** เช่น API key ความลับไม่ควรอยู่ในโค้ดและควรถูกเก็บไว้ในที่ปลอดภัย ในการแยกความลับออกจากโค้ด เราสามารถใช้ environment variables และไลบรารีเช่น `python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env` ไฟล์ที่มีเนื้อหาดังนี้:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > หมายเหตุ สำหรับ Azure คุณต้องตั้งค่า environment variables ดังนี้:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     ในโค้ด คุณจะโหลด environment variables ดังนี้:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **คำพูดเกี่ยวกับความยาวของ token** เราควรพิจารณาว่าจำเป็นต้องใช้ token เท่าไรเพื่อสร้างข้อความที่เราต้องการ Token มีค่าใช้จ่าย ดังนั้นที่ไหนที่เป็นไปได้ เราควรพยายามประหยัดจำนวน token ที่เราใช้ ตัวอย่างเช่น เราสามารถวาง prompt ในลักษณะที่เราสามารถใช้ token น้อยลงได้หรือไม่?

  ในการเปลี่ยน token ที่ใช้ คุณสามารถใช้พารามิเตอร์ `max_tokens` ตัวอย่างเช่น ถ้าคุณต้องการใช้ 100 token คุณจะทำดังนี้:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **ทดลองกับ temperature** Temperature เป็นสิ่งที่เราไม่ได้กล่าวถึงจนถึงตอนนี้ แต่เป็นบริบทที่สำคัญสำหรับการทำงานของโปรแกรมของเรา ค่ายิ่งสูงเท่าไร ผลลัพธ์ยิ่งสุ่มมากขึ้น ในทางกลับกัน ค่ายิ่งต่ำเท่าไร ผลล

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามอย่างเต็มที่เพื่อความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้บริการแปลภาษามนุษย์ที่เป็นมืออาชีพ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้