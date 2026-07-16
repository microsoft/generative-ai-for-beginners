# การสร้างแอปพลิเคชันสร้างภาพ

[![การสร้างแอปพลิเคชันสร้างภาพ](../../../translated_images/th/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

มีมากกว่าการสร้างข้อความที่ LLMs ทำได้ ยังสามารถสร้างภาพจากคำอธิบายข้อความได้ด้วย การมีภาพเป็นรูปแบบข้อมูลนั้นมีประโยชน์มากในหลาย ๆ ด้าน เช่น MedTech สถาปัตยกรรม การท่องเที่ยว การพัฒนาเกม และอื่น ๆ ในบทนี้ เราจะดูสองโมเดลสร้างภาพที่ได้รับความนิยมมากที่สุด คือ DALL-E และ Midjourney

## บทนำ

ในบทเรียนนี้ เราจะครอบคลุม:

- การสร้างภาพและเหตุผลว่าทำไมมันถึงมีประโยชน์
- DALL-E และ Midjourney คืออะไร และทำงานอย่างไร
- วิธีสร้างแอปพลิเคชันสร้างภาพ

## เป้าหมายการเรียนรู้

หลังจากเรียนบทนี้เสร็จ คุณจะสามารถ:

- สร้างแอปพลิเคชันสร้างภาพ
- กำหนดขอบเขตสำหรับแอปพลิเคชันของคุณด้วย meta prompts
- ใช้งานกับ DALL-E และ Midjourney

## ทำไมต้องสร้างแอปพลิเคชันสร้างภาพ?

แอปพลิเคชันสร้างภาพเป็นวิธีที่ยอดเยี่ยมในการสำรวจความสามารถของ Generative AI ตัวอย่างการใช้งานเช่น:

- **การแก้ไขและสังเคราะห์ภาพ** คุณสามารถสร้างภาพสำหรับกรณีใช้งานหลายรูปแบบ เช่น การแก้ไขภาพและการสังเคราะห์ภาพ

- **นำไปใช้กับหลายอุตสาหกรรม** ยังสามารถใช้สร้างภาพสำหรับอุตสาหกรรมต่าง ๆ เช่น Medtech การท่องเที่ยว การพัฒนาเกม และอื่น ๆ

## กรณีศึกษา: Edu4All

ในบทเรียนนี้ เราจะทำงานต่อกับสตาร์ทอัพของเรา Edu4All นักเรียนจะสร้างภาพสำหรับการมอบหมายงานของพวกเขา ภาพเหล่านี้จะเป็นอะไรขึ้นอยู่กับนักเรียน เช่น ภาพประกอบนิทานของตนเอง สร้างตัวละครใหม่สำหรับเรื่องราว หรือช่วยให้เห็นภาพแนวคิดและไอเดียของพวกเขา

ตัวอย่างที่นักเรียน Edu4All อาจสร้างเช่นเมื่อทำงานในชั้นเรียนเกี่ยวกับอนุสาวรีย์:

![สตาร์ทอัพ Edu4All, ชั้นเรียนเกี่ยวกับอนุสาวรีย์, หอไอเฟล](../../../translated_images/th/startup.94d6b79cc4bb3f5a.webp)

ใช้คำสั่งเช่น

> "สุนัขข้างหอไอเฟลในแสงแดดยามเช้า"

## DALL-E และ Midjourney คืออะไร?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) และ [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) เป็นโมเดลสร้างภาพที่ได้รับความนิยมสองตัว ซึ่งช่วยให้คุณใช้คำสั่งเพื่อสร้างภาพได้

### DALL-E

เรามาเริ่มต้นกับ DALL-E ซึ่งเป็นโมเดล Generative AI ที่สร้างภาพจากคำอธิบายข้อความ

> [DALL-E เป็นการรวมกันของสองโมเดล คือ CLIP และ diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)

- **CLIP** เป็นโมเดลที่สร้าง embeddings ซึ่งเป็นการแทนข้อมูลในรูปแบบตัวเลขจากภาพและข้อความ

- **Diffused attention** เป็นโมเดลที่สร้างภาพจาก embeddings DALL-E ถูกฝึกด้วยชุดข้อมูลภาพและข้อความ และใช้สร้างภาพจากคำอธิบายข้อความ ตัวอย่างเช่น DALL-E สามารถสร้างภาพแมวใส่หมวก หรือสุนัขมีทรงผม mohawk

### Midjourney

Midjourney ทำงานในลักษณะคล้ายกับ DALL-E โดยสร้างภาพจากคำสั่งข้อความ Midjourney ยังสามารถสร้างภาพด้วยคำสั่งเช่น “แมวใส่หมวก” หรือ “สุนัขมีทรงผม mohawk”

![ภาพที่สร้างโดย Midjourney, นกพิราบกลไก](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_เครดิตภาพ Wikipedia, ภาพที่สร้างโดย Midjourney_

## DALL-E และ Midjourney ทำงานอย่างไร

เริ่มต้นด้วย [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst) DALL-E เป็นโมเดล Generative AI ที่อิงกับสถาปัตยกรรม transformer โดยใช้ _autoregressive transformer_

_autoregressive transformer_ กำหนดวิธีที่โมเดลสร้างภาพจากคำอธิบายข้อความ โดยสร้างทีละพิกเซล จากนั้นใช้พิกเซลที่สร้างมาแล้วเพื่อสร้างพิกเซลถัดไป ผ่านเลเยอร์ต่าง ๆ ในเครือข่ายประสาท จนภาพสมบูรณ์

ด้วยกระบวนการนี้ DALL-E ควบคุมลักษณะ วัตถุ คุณสมบัติ และอื่น ๆ ในภาพที่สร้าง อย่างไรก็ตาม DALL-E 2 และ 3 มีการควบคุมภาพที่สร้างได้มากขึ้น

## สร้างแอปพลิเคชันสร้างภาพแอปแรกของคุณ

แล้วจะต้องใช้อะไรบ้างเพื่อสร้างแอปพลิเคชันสร้างภาพ? คุณต้องใช้ไลบรารีดังนี้:

- **python-dotenv** แนะนำอย่างสูงให้ใช้ไลบรารีนี้เพื่อเก็บความลับของคุณในไฟล์ _.env_ แยกจากโค้ด
- **openai** ไลบรารีนี้ใช้สำหรับติดต่อกับ OpenAI API
- **pillow** สำหรับจัดการกับภาพใน Python
- **requests** ช่วยให้ส่งคำขอ HTTP

## สร้างและปรับใช้โมเดล Azure OpenAI

หากยังไม่ได้ทำ ให้ทำตามคำแนะนำในหน้า [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)
เพื่อตั้งค่า Azure OpenAI resource และโมเดล เลือก **gpt-image-1** เป็นโมเดล (โมเดลภาพ Azure OpenAI รุ่นปัจจุบัน; DALL-E 3 เป็นรุ่นเก่าและไม่สามารถใช้งานสำหรับการปรับใช้ใหม่)

## สร้างแอป

1. สร้างไฟล์ _.env_ กับเนื้อหาดังนี้:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   ค้นหาข้อมูลนี้ใน Azure OpenAI Foundry Portal สำหรับ resource ของคุณในส่วน "Deployments"

1. รวบรวมไลบรารีข้างต้นลงในไฟล์ชื่อ _requirements.txt_ ดังนี้:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. ถัดไป สร้าง virtual environment และติดตั้งไลบรารี:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   สำหรับ Windows ใช้คำสั่งดังนี้เพื่อสร้างและเปิดใช้งาน virtual environment

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. เพิ่มโค้ดนี้ในไฟล์ชื่อ _app.py_:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # import dotenv
    dotenv.load_dotenv()
    
    # กำหนดค่าลูกค้าบริการ Azure OpenAI
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # สร้างภาพโดยใช้ API สำหรับการสร้างภาพ
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # ตั้งไดเร็กทอรีสำหรับเก็บภาพ
        image_dir = os.path.join(os.curdir, 'images')

        # หากไดเร็กทอรีไม่มีอยู่ ให้สร้างมันขึ้นมา
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # กำหนดค่าเส้นทางภาพ (โปรดทราบไฟล์ต้องเป็น png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # ดึงภาพที่สร้างขึ้นมา
        image_url = generation_response.data[0].url  # ดึง URL ภาพจากการตอบกลับ
        generated_image = requests.get(image_url).content  # ดาวน์โหลดภาพ
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # แสดงภาพในโปรแกรมดูภาพเริ่มต้น
        image = Image.open(image_path)
        image.show()

    # จับข้อผิดพลาด
    except openai.BadRequestError as err:
        print(err)
   ```

มาอธิบายโค้ดนี้:

- ก่อนอื่น นำเข้าไลบรารีที่ต้องการ รวมถึงไลบรารี OpenAI, dotenv, requests และ Pillow

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- จากนั้น โหลดตัวแปรแวดล้อมจากไฟล์ _.env_

  ```python
  # นำเข้า dotenv
  dotenv.load_dotenv()
  ```

- ต่อไป กำหนดค่า Azure OpenAI service client

  ```python
  # รับ endpoint และ key จากตัวแปรสภาพแวดล้อม
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- จากนั้น สร้างภาพ:

  ```python
  # สร้างภาพโดยใช้ API การสร้างภาพ
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  โค้ดข้างต้นตอบกลับเป็นอ็อบเจกต์ JSON ที่มี URL ของภาพที่สร้าง เราสามารถใช้ URL นี้ดาวน์โหลดภาพและบันทึกลงไฟล์ได้

- สุดท้าย เปิดภาพและใช้โปรแกรมดูภาพมาตรฐานเพื่อแสดงผล:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### รายละเอียดเพิ่มเติมเกี่ยวกับการสร้างภาพ

มาดูโค้ดที่ใช้สร้างภาพอย่างละเอียดขึ้น:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt** คือข้อความที่ใช้เพื่อสร้างภาพ ในกรณีนี้ เราใช้ข้อความว่า "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"
- **size** คือขนาดของภาพที่สร้าง ในกรณีนี้เราสร้างภาพขนาด 1024x1024 พิกเซล
- **n** คือจำนวนภาพที่สร้าง ในกรณีนี้เราสร้างสองภาพ
- **temperature** เป็นพารามิเตอร์ที่ควบคุมความสุ่มของผลลัพธ์ของโมเดล Generative AI ค่า temperature มีช่วง 0 ถึง 1 โดย 0 หมายถึงผลลัพธ์เป็นแบบกำหนดได้ และ 1 หมายถึงผลลัพธ์เป็นแบบสุ่ม ค่าเริ่มต้น 0.7

ยังมีสิ่งอื่น ๆ ที่คุณสามารถทำกับภาพอีกมาก ซึ่งเราจะพูดถึงในส่วนถัดไป

## ความสามารถเพิ่มเติมของการสร้างภาพ

คุณเห็นแล้วว่าเราสามารถสร้างภาพด้วยไม่กี่บรรทัดใน Python อย่างไรก็ตาม ยังมีสิ่งอื่นที่ทำได้กับภาพ

คุณยังสามารถทำสิ่งต่อไปนี้ได้:

- **แก้ไขภาพ** โดยให้ภาพเดิม หน้ากาก และคำสั่งข้อความ คุณสามารถแก้ไขภาพได้ เช่น เพิ่มสิ่งของในส่วนที่ต้องการของภาพ ลองจินตนาการภาพกระต่ายของเรา คุณสามารถเพิ่มหมวกให้กระต่าย วิธีทำคือให้ภาพ หน้ากาก (ระบุส่วนที่ต้องการแก้ไข) และข้อความคำสั่งอธิบายสิ่งที่ต้องการทำ
> หมายเหตุ: ฟังก์ชันนี้ไม่รองรับใน DALL-E 3
 
ตัวอย่างต่อไปนี้ใช้ GPT Image:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  ภาพพื้นฐานจะมีแค่เลานจ์กับสระว่ายน้ำ แต่ภาพสุดท้ายจะมีนกฟลามิงโก

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/th/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/th/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/th/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **สร้างความหลากหลาย** แนวคิดคือนำภาพที่มีอยู่แล้วและขอให้สร้างความหลากหลายของภาพนั้น วิธีสร้างความหลากหลายทำได้โดยให้ภาพและข้อความคำสั่ง พร้อมโค้ดดังนี้:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > หมายเหตุ: ฟังก์ชันนี้รองรับเฉพาะโมเดล DALL-E 2 ของ OpenAI เท่านั้น ไม่ได้ใช้กับ gpt-image-1

## อุณหภูมิ (Temperature)

อุณหภูมิเป็นพารามิเตอร์ที่ควบคุมความสุ่มของผลลัพธ์ของโมเดล Generative AI ค่าอุณหภูมิอยู่ระหว่าง 0 ถึง 1 ซึ่ง 0 หมายถึงผลลัพธ์เป็นแบบกำหนดได้ และ 1 หมายถึงผลลัพธ์เป็นแบบสุ่ม ค่าเริ่มต้นคือ 0.7

มาดูตัวอย่างของการทำงานของอุณหภูมิ โดยใช้คำสั่งนี้สองครั้ง:

> คำสั่ง : "Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils"

![กระต่ายบนหลังม้า ถืออมยิ้ม](../../../translated_images/th/v1-generated-image.a295cfcffa3c13c2.webp)

ลองรันคำสั่งเดียวกันอีกครั้งเพื่อดูว่าเราจะไม่ได้ภาพเหมือนกันสองครั้ง:

![ภาพที่สร้างของกระต่ายบนม้า](../../../translated_images/th/v2-generated-image.33f55a3714efe61d.webp)

ดังที่เห็น ภาพมีความคล้ายคลึงกันแต่ไม่เหมือนกัน ลองเปลี่ยนอุณหภูมิเป็น 0.1 และดูผลลัพธ์:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # ป้อนข้อความพร้อมท์ของคุณที่นี่
        size='1024x1024',
        n=2
    )
```

### การเปลี่ยนอุณหภูมิ

ลองทำให้ผลตอบกลับเป็นแบบกำหนดได้มากขึ้น เราสังเกตได้จากภาพสองภาพที่สร้างว่าในภาพแรกมีตัวกระต่ายและในภาพที่สองมีม้า ดังนั้นภาพจึงต่างกันมาก

ดังนั้นเราจึงเปลี่ยนโค้ดโดยตั้งค่าอุณหภูมิเป็น 0 ดังนี้:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # ป้อนข้อความพร้อมท์ของคุณที่นี่
        size='1024x1024',
        n=2,
        temperature=0
    )
```

เมื่อรันโค้ดนี้ คุณจะได้สองภาพนี้:

- ![อุณหภูมิ 0, v1](../../../translated_images/th/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![อุณหภูมิ 0 , v2](../../../translated_images/th/v2-temp-generated-image.871d0c920dbfb0f1.webp)

ที่นี่คุณจะเห็นได้ชัดว่าภาพทั้งสองคล้ายกันมากขึ้น

## วิธีการกำหนดขอบเขตแอปพลิเคชันของคุณด้วย metaprompts

กับเดโมของเรา เราสามารถสร้างภาพสำหรับลูกค้าได้แล้ว อย่างไรก็ตาม ต้องสร้างขอบเขตสำหรับแอปพลิเคชันของเรา

ตัวอย่างเช่น เราไม่ต้องการสร้างภาพที่ไม่เหมาะสำหรับการทำงาน หรือไม่เหมาะสำหรับเด็ก

เราสามารถทำได้ด้วย _metaprompts_ Metaprompts คือข้อความคำสั่งที่ใช้ควบคุมผลลัพธ์ของโมเดล Generative AI เช่น ใช้เมตาพรอมต์เพื่อควบคุมผลลัพธ์และให้แน่ใจว่าภาพที่สร้างปลอดภัยสำหรับการทำงาน หรือเหมาะสำหรับเด็ก

### มันทำงานอย่างไร?

ตอนนี้ metaprompts ทำงานอย่างไร?

Metaprompts คือข้อความคำสั่งที่ใช้ควบคุมผลลัพธ์ของโมเดล Generative AI โดยจะวางก่อนคำสั่งข้อความ และใช้ควบคุมผลลัพธ์ของโมเดล และฝังอยู่ในแอปพลิเคชันเพื่อควบคุมผลลัพธ์ของโมเดล รวมทั้งห่อคำสั่งป้อนเข้าและเมตาพรอมต์เข้าในคำสั่งเดียว

ตัวอย่างของ metaprompt เช่น:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

ตอนนี้ มาดูกันว่าเราจะใช้ metaprompts ในเดโมของเราได้อย่างไร

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

# TODO เพิ่มคำขอเพื่อสร้างภาพ
```

จากคำสั่งด้านบน คุณจะเห็นว่าเมื่อสร้างภาพทั้งหมดจะพิจารณา metaprompt ด้วย

## แบบฝึกหัด - มาเปิดโอกาสให้นักเรียน

เราแนะนำ Edu4All ตอนต้นบทเรียน ตอนนี้ถึงเวลาที่จะเปิดโอกาสให้นักเรียนสร้างภาพสำหรับงานประเมินของพวกเขา


นักเรียนจะสร้างภาพสำหรับการประเมินของพวกเขาที่ประกอบด้วยอนุสรณ์สถาน โดยอนุสรณ์สถานที่เลือกขึ้นอยู่กับนักเรียน นักเรียนจะได้รับการขอให้ใช้ความคิดสร้างสรรค์ในงานนี้เพื่อนำอนุสรณ์สถานเหล่านี้ไปวางในบริบทที่แตกต่างกัน

## วิธีแก้ปัญหา

นี่คือตัวอย่างวิธีแก้ปัญหาหนึ่ง:

```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# นำเข้า dotenv
dotenv.load_dotenv()

# ดึง endpoint และ key จากตัวแปรสภาพแวดล้อม
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
  api_key=os.environ['AZURE_OPENAI_API_KEY'],
  api_version = "2024-10-21"
  )


disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"""{meta_prompt}
Generate monument of the Arc of Triumph in Paris, France, in the evening light with a small child holding a Teddy looks on.
"""

try:
    # สร้างภาพโดยใช้ API การสร้างภาพ
    generation_response = client.images.generate(
        prompt=prompt,    # ป้อนข้อความ prompt ของคุณที่นี่
        size='1024x1024',
        n=1,
    )
    # ตั้งไดเรกทอรีสำหรับเก็บภาพ
    image_dir = os.path.join(os.curdir, 'images')

    # หากไดเรกทอรีไม่มีอยู่ ให้สร้างมันขึ้นมา
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # กำหนดเส้นทางภาพ (โปรดทราบว่าประเภทไฟล์ควรเป็น png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # ดึงภาพที่สร้างขึ้น
    image_url = generation_response.data[0].url  # ดึง URL ของภาพจากการตอบสนอง
    generated_image = requests.get(image_url).content  # ดาวน์โหลดภาพ
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # แสดงภาพในโปรแกรมดูภาพเริ่มต้น
    image = Image.open(image_path)
    image.show()

# ดักจับข้อผิดพลาด
except openai.BadRequestError as err:
    print(err)
```

## งานดีมาก! ดำเนินการเรียนรู้ต่อไป

หลังจากทำบทเรียนนี้เสร็จแล้ว ให้ตรวจสอบ [คอลเลกชันการเรียนรู้ Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ของเราเพื่อพัฒนาความรู้ด้าน Generative AI ของคุณต่อไป!

ไปที่บทเรียน 10 ซึ่งเราจะดูวิธีการ [สร้างแอปพลิเคชัน AI ด้วยโค้ดต่ำ](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ปฏิเสธความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ขณะที่เราพยายามให้ความถูกต้อง โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยมนุษย์มืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->