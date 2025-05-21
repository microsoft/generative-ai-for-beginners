<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T19:11:37+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "th"
}
-->
# การสร้างแอปพลิเคชันการสร้างภาพ

มีมากกว่าแค่การสร้างข้อความใน LLMs เพราะยังสามารถสร้างภาพจากคำบรรยายได้ด้วย การมีภาพเป็นสื่อสามารถมีประโยชน์มากในหลาย ๆ ด้าน เช่น เทคโนโลยีทางการแพทย์ สถาปัตยกรรม การท่องเที่ยว การพัฒนาเกม และอื่น ๆ ในบทนี้ เราจะมาดูโมเดลการสร้างภาพที่ได้รับความนิยมที่สุดสองตัวคือ DALL-E และ Midjourney

## บทนำ

ในบทเรียนนี้ เราจะครอบคลุม:

- การสร้างภาพและทำไมมันถึงมีประโยชน์
- DALL-E และ Midjourney คืออะไรและทำงานอย่างไร
- วิธีการสร้างแอปพลิเคชันการสร้างภาพ

## เป้าหมายการเรียนรู้

หลังจากจบบทเรียนนี้ คุณจะสามารถ:

- สร้างแอปพลิเคชันการสร้างภาพ
- กำหนดขอบเขตสำหรับแอปพลิเคชันของคุณด้วย meta prompts
- ทำงานร่วมกับ DALL-E และ Midjourney

## ทำไมต้องสร้างแอปพลิเคชันการสร้างภาพ?

แอปพลิเคชันการสร้างภาพเป็นวิธีที่ยอดเยี่ยมในการสำรวจความสามารถของ Generative AI มันสามารถใช้ในกรณีต่าง ๆ เช่น:

- **การแก้ไขและการสร้างภาพ** คุณสามารถสร้างภาพสำหรับการใช้งานที่หลากหลาย เช่น การแก้ไขภาพและการสร้างภาพ

- **ประยุกต์ใช้ในอุตสาหกรรมต่าง ๆ** สามารถใช้สร้างภาพสำหรับอุตสาหกรรมต่าง ๆ เช่น เทคโนโลยีทางการแพทย์ การท่องเที่ยว การพัฒนาเกม และอื่น ๆ

## สถานการณ์: Edu4All

ในบทเรียนนี้ เราจะทำงานร่วมกับสตาร์ทอัพของเรา Edu4All นักเรียนจะสร้างภาพสำหรับการประเมินของพวกเขา ภาพที่สร้างขึ้นขึ้นอยู่กับนักเรียน อาจเป็นภาพประกอบสำหรับนิทานของพวกเขาเองหรือสร้างตัวละครใหม่สำหรับเรื่องราวของพวกเขาหรือช่วยให้พวกเขาเห็นภาพแนวคิดและแนวคิดของพวกเขา

นี่คือตัวอย่างที่นักเรียนของ Edu4All อาจสร้างขึ้นหากพวกเขาทำงานในชั้นเรียนเกี่ยวกับอนุสาวรีย์:

ใช้ prompt เช่น

> "สุนัขอยู่ข้างหอไอเฟลในแสงแดดยามเช้า"

## DALL-E และ Midjourney คืออะไร?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) และ [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) เป็นโมเดลการสร้างภาพที่ได้รับความนิยมมากที่สุดสองตัวที่ให้คุณใช้ prompts เพื่อสร้างภาพ

### DALL-E

เริ่มต้นด้วย DALL-E ซึ่งเป็นโมเดล Generative AI ที่สร้างภาพจากคำบรรยาย

- **CLIP** เป็นโมเดลที่สร้าง embeddings ซึ่งเป็นการแสดงข้อมูลในรูปแบบตัวเลขจากภาพและข้อความ

- **Diffused attention** เป็นโมเดลที่สร้างภาพจาก embeddings DALL-E ถูกฝึกบนชุดข้อมูลของภาพและข้อความและสามารถใช้สร้างภาพจากคำบรรยายได้ ตัวอย่างเช่น DALL-E สามารถใช้สร้างภาพของแมวในหมวก หรือสุนัขกับโมฮอว์ก

### Midjourney

Midjourney ทำงานคล้ายกับ DALL-E โดยสร้างภาพจาก text prompts Midjourney ยังสามารถใช้สร้างภาพโดยใช้ prompts เช่น "แมวในหมวก" หรือ "สุนัขกับโมฮอว์ก"

## DALL-E และ Midjourney ทำงานอย่างไร

เริ่มต้นด้วย [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst) ซึ่งเป็นโมเดล Generative AI ที่อิงตามสถาปัตยกรรม transformer กับ _autoregressive transformer_

_autoregressive transformer_ กำหนดวิธีการที่โมเดลสร้างภาพจากคำบรรยาย โดยสร้างหนึ่งพิกเซลต่อครั้งและใช้พิกเซลที่สร้างขึ้นเพื่อสร้างพิกเซลถัดไป ผ่านหลายชั้นในเครือข่ายประสาทเทียมจนกว่าภาพจะสมบูรณ์

ด้วยกระบวนการนี้ DALL-E สามารถควบคุมคุณสมบัติ วัตถุ ลักษณะ และอื่น ๆ ในภาพที่สร้างขึ้นได้ อย่างไรก็ตาม DALL-E 2 และ 3 มีการควบคุมภาพที่สร้างขึ้นมากกว่า

## การสร้างแอปพลิเคชันการสร้างภาพครั้งแรกของคุณ

ต้องมีอะไรบ้างในการสร้างแอปพลิเคชันการสร้างภาพ? คุณต้องใช้ไลบรารีต่อไปนี้:

- **python-dotenv** แนะนำให้ใช้ไลบรารีนี้เพื่อเก็บข้อมูลลับในไฟล์ _.env_ แยกจากโค้ด
- **openai** ไลบรารีนี้ใช้ในการโต้ตอบกับ OpenAI API
- **pillow** เพื่อทำงานกับภาพใน Python
- **requests** เพื่อช่วยในการทำคำขอ HTTP

1. สร้างไฟล์ _.env_ ด้วยเนื้อหาต่อไปนี้:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   ค้นหาข้อมูลนี้ใน Azure Portal สำหรับทรัพยากรของคุณในส่วน "Keys and Endpoint"

1. รวบรวมไลบรารีด้านบนในไฟล์ที่เรียกว่า _requirements.txt_ ดังนี้:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. จากนั้นสร้างสภาพแวดล้อมเสมือนและติดตั้งไลบรารี:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   สำหรับ Windows ใช้คำสั่งต่อไปนี้เพื่อสร้างและเปิดใช้งานสภาพแวดล้อมเสมือนของคุณ:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. เพิ่มโค้ดต่อไปนี้ในไฟล์ที่เรียกว่า _app.py_:

   ```python
   import openai
   import os
   import requests
   from PIL import Image
   import dotenv

   # import dotenv
   dotenv.load_dotenv()

   # Get endpoint and key from environment variables
   openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
   openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

   # Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
   openai.api_version = '2023-06-01-preview'
   openai.api_type = 'azure'


   try:
       # Create an image by using the image generation API
       generation_response = openai.Image.create(
           prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
           size='1024x1024',
           n=2,
           temperature=0,
       )
       # Set the directory for the stored image
       image_dir = os.path.join(os.curdir, 'images')

       # If the directory doesn't exist, create it
       if not os.path.isdir(image_dir):
           os.mkdir(image_dir)

       # Initialize the image path (note the filetype should be png)
       image_path = os.path.join(image_dir, 'generated-image.png')

       # Retrieve the generated image
       image_url = generation_response["data"][0]["url"]  # extract image URL from response
       generated_image = requests.get(image_url).content  # download the image
       with open(image_path, "wb") as image_file:
           image_file.write(generated_image)

       # Display the image in the default image viewer
       image = Image.open(image_path)
       image.show()

   # catch exceptions
   except openai.InvalidRequestError as err:
       print(err)

   ```

อธิบายโค้ดนี้:

- ก่อนอื่นเรานำเข้าไลบรารีที่เราต้องการ รวมถึงไลบรารี OpenAI ไลบรารี dotenv ไลบรารี requests และไลบรารี Pillow

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- จากนั้นเราดึงค่าตัวแปรสิ่งแวดล้อมจากไฟล์ _.env_

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- หลังจากนั้นเราตั้งค่า endpoint, key สำหรับ OpenAI API, version และ type

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- จากนั้นเราสร้างภาพ:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  โค้ดด้านบนตอบสนองด้วยวัตถุ JSON ที่มี URL ของภาพที่สร้างขึ้น เราสามารถใช้ URL เพื่อดาวน์โหลดภาพและบันทึกลงในไฟล์

- สุดท้ายเราเปิดภาพและใช้โปรแกรมดูภาพมาตรฐานเพื่อแสดงมัน:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### รายละเอียดเพิ่มเติมเกี่ยวกับการสร้างภาพ

มาดูโค้ดที่สร้างภาพในรายละเอียดเพิ่มเติม:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt** เป็น text prompt ที่ใช้ในการสร้างภาพ ในกรณีนี้ เราใช้ prompt "กระต่ายบนม้า ถืออมยิ้ม บนทุ่งหมอกที่มีดอกแดฟโฟดิลขึ้น"
- **size** เป็นขนาดของภาพที่สร้างขึ้น ในกรณีนี้ เรากำลังสร้างภาพที่มีขนาด 1024x1024 พิกเซล
- **n** เป็นจำนวนภาพที่สร้างขึ้น ในกรณีนี้ เรากำลังสร้างสองภาพ
- **temperature** เป็นพารามิเตอร์ที่ควบคุมความสุ่มของผลลัพธ์ของโมเดล Generative AI ค่า temperature เป็นค่าระหว่าง 0 ถึง 1 โดยที่ 0 หมายถึงผลลัพธ์ที่เป็นเชิงกำหนดและ 1 หมายถึงผลลัพธ์ที่สุ่ม ค่าเริ่มต้นคือ 0.7

มีสิ่งอื่น ๆ ที่คุณสามารถทำได้กับภาพที่เราจะครอบคลุมในส่วนถัดไป

## ความสามารถเพิ่มเติมของการสร้างภาพ

คุณได้เห็นแล้วว่าเราสามารถสร้างภาพได้โดยใช้โค้ดไม่กี่บรรทัดใน Python อย่างไรก็ตาม ยังมีสิ่งอื่น ๆ ที่คุณสามารถทำได้กับภาพ

คุณยังสามารถทำสิ่งต่อไปนี้:

- **ทำการแก้ไข** โดยการให้ภาพที่มีอยู่แล้วพร้อมกับหน้ากากและ prompt คุณสามารถแก้ไขภาพได้ ตัวอย่างเช่น คุณสามารถเพิ่มบางสิ่งลงในส่วนหนึ่งของภาพได้ ลองจินตนาการถึงภาพกระต่ายของเรา คุณสามารถเพิ่มหมวกให้กระต่ายได้ วิธีที่คุณทำคือโดยการให้ภาพ หน้ากาก (ระบุส่วนของพื้นที่สำหรับการเปลี่ยนแปลง) และ text prompt เพื่อบอกว่าควรทำอะไร

  ```python
  response = openai.Image.create_edit(
    image=open("base_image.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="An image of a rabbit with a hat on its head.",
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  ภาพพื้นฐานจะมีเพียงกระต่าย แต่ภาพสุดท้ายจะมีหมวกบนกระต่าย

- **สร้างรูปแบบต่าง ๆ** แนวคิดคือคุณใช้ภาพที่มีอยู่แล้วและขอให้สร้างรูปแบบต่าง ๆ ในการสร้างรูปแบบ คุณให้ภาพและ text prompt และโค้ดดังนี้:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > หมายเหตุ นี่รองรับเฉพาะบน OpenAI

## Temperature

Temperature เป็นพารามิเตอร์ที่ควบคุมความสุ่มของผลลัพธ์ของโมเดล Generative AI ค่า temperature เป็นค่าระหว่าง 0 ถึง 1 โดยที่ 0 หมายถึงผลลัพธ์ที่เป็นเชิงกำหนดและ 1 หมายถึงผลลัพธ์ที่สุ่ม ค่าเริ่มต้นคือ 0.7

ลองดูตัวอย่างการทำงานของ temperature โดยการรัน prompt นี้สองครั้ง:

> Prompt: "กระต่ายบนม้า ถืออมยิ้ม บนทุ่งหมอกที่มีดอกแดฟโฟดิลขึ้น"

ตอนนี้ลองรัน prompt เดิมอีกครั้งเพื่อดูว่าเราจะไม่ได้ภาพเดียวกันสองครั้ง:

ตามที่คุณเห็น ภาพมีความคล้ายคลึงกัน แต่ไม่เหมือนกัน ลองเปลี่ยนค่า temperature เป็น 0.1 แล้วดูว่าเกิดอะไรขึ้น:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### การเปลี่ยนแปลงค่า temperature

ลองพยายามทำให้ผลลัพธ์เป็นเชิงกำหนดมากขึ้น เราสามารถสังเกตได้จากภาพสองภาพที่เราสร้างขึ้นว่าในภาพแรกมีกระต่ายและในภาพที่สองมีม้า ดังนั้นภาพจึงมีความแตกต่างกันมาก

ดังนั้นลองเปลี่ยนโค้ดของเราและตั้งค่า temperature เป็น 0 ดังนี้:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

ตอนนี้เมื่อคุณรันโค้ดนี้ คุณจะได้รับภาพสองภาพนี้:

ที่นี่คุณสามารถเห็นได้อย่างชัดเจนว่าภาพมีความคล้ายคลึงกันมากขึ้น

## วิธีการกำหนดขอบเขตสำหรับแอปพลิเคชันของคุณด้วย metaprompts

ด้วยการสาธิตของเรา เราสามารถสร้างภาพสำหรับลูกค้าของเราได้แล้ว อย่างไรก็ตาม เราจำเป็นต้องสร้างขอบเขตสำหรับแอปพลิเคชันของเรา

ตัวอย่างเช่น เราไม่ต้องการสร้างภาพที่ไม่ปลอดภัยสำหรับการทำงาน หรือไม่เหมาะสมสำหรับเด็ก

เราสามารถทำได้ด้วย _metaprompts_ Metaprompts เป็น text prompts ที่ใช้ในการควบคุมผลลัพธ์ของโมเดล Generative AI ตัวอย่างเช่น เราสามารถใช้ metaprompts เพื่อควบคุมผลลัพธ์ และรับรองว่าภาพที่สร้างขึ้นมีความปลอดภัยสำหรับการทำงาน หรือเหมาะสมสำหรับเด็ก

### มันทำงานอย่างไร?

แล้ว metaprompts ทำงานอย่างไร?

Metaprompts เป็น text prompts ที่ใช้ในการควบคุมผลลัพธ์ของโมเดล Generative AI โดยจะถูกวางก่อน text prompt และใช้ในการควบคุมผลลัพธ์ของโมเดลและฝังในแอปพลิเคชันเพื่อควบคุมผลลัพธ์ของโมเดล โดยการรวม prompt input และ meta prompt input ใน text prompt เดียว

ตัวอย่างหนึ่งของ metaprompt จะเป็นดังนี้:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

ตอนนี้มาดูวิธีที่เราสามารถใช้ metaprompts ในการสาธิตของเรา

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt =f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"{meta_prompt}
Create an image of a bunny on a horse, holding a lollipop"

# TODO add request to generate image
```

จาก prompt ด้านบน คุณสามารถเห็นว่าภาพทั้งหมดที่สร้างขึ้นพิจารณา metaprompt

## งานที่มอบหมาย - มาช่วยนักเรียนกันเถอะ

เราได้แนะนำ Edu4All ในตอนต้นของบทเรียนนี้ ตอนนี้ถึงเวลาที่จะช่วยให้นักเรียนสามารถสร้างภาพสำหรับการประเมินของพวกเขา

นักเรียนจะสร้างภาพสำหรับการประเมินของพวกเขาที่มีอนุสาวรีย์ อนุสาวรีย์ใดที่นักเรียนต้องการสร้างขึ้นอยู่กับพวกเขา นักเรียนถูกขอให้ใช้ความคิดสร้างสรรค์ในงานนี้เพื่อวางอนุสาวรีย์เหล่านี้ในบริบทที่แตกต่างกัน

## วิธีแก้ปัญหา

นี่คือวิธีแก้ปัญหาหนึ่งที่เป็นไปได้:

```python
import openai
import os
import requests
from PIL import Image
import dotenv

# import dotenv
dotenv.load_dotenv()

# Get endpoint and key from environment variables
openai.api_base = "<replace with endpoint>"
openai.api_key = "<replace with api key>"

# Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
openai.api_version = '2023-06-01-preview'
openai.api_type = 'azure'

disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}"""

prompt = f"""{metaprompt}
Generate monument of the Arc of Triumph in Paris, France, in the evening light with a small child holding a Teddy looks on.
""""

try:
    # Create an image by using the image generation API
    generation_response = openai.Image.create(
        prompt=prompt,    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    image_url = generation_response["data"][0]["url"]  # extract image URL from response
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
except openai.InvalidRequestError as err:
    print(err)
```

## ทำได้ดีมาก! เรียนรู้เพิ่มเติมต่อไป

หลังจากจบบทเรียนนี้ ตรวจสอบ [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ของเราเพื่อเรียนรู้เพิ่มเติมเกี่ยวกับ Generative AI

ไปที่บทเรียนที่ 10 ซึ่งเราจะดูวิธีการ [สร้างแอปพลิเคชัน AI ด้วย low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาด้วย AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้เกิดความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ แนะนำให้ใช้บริการแปลภาษามนุษย์มืออาชีพ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้