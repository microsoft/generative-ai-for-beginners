<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "238cde5c90363d70ecc939569378da51",
  "translation_date": "2025-10-17T18:39:26+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "th"
}
-->
# การสร้างแอปพลิเคชันสร้างภาพ

[![การสร้างแอปพลิเคชันสร้างภาพ](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.th.png)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLMs ไม่ได้มีแค่การสร้างข้อความเท่านั้น แต่ยังสามารถสร้างภาพจากคำอธิบายข้อความได้อีกด้วย การมีภาพเป็นส่วนหนึ่งของการใช้งานสามารถเป็นประโยชน์ในหลายด้าน เช่น เทคโนโลยีทางการแพทย์ สถาปัตยกรรม การท่องเที่ยว การพัฒนาเกม และอื่นๆ ในบทนี้ เราจะมาดูโมเดลการสร้างภาพที่ได้รับความนิยมมากที่สุดสองตัว ได้แก่ DALL-E และ Midjourney

## บทนำ

ในบทเรียนนี้ เราจะครอบคลุม:

- การสร้างภาพและเหตุผลที่มันมีประโยชน์
- DALL-E และ Midjourney คืออะไรและทำงานอย่างไร
- วิธีการสร้างแอปพลิเคชันสร้างภาพ

## เป้าหมายการเรียนรู้

หลังจากจบบทเรียนนี้ คุณจะสามารถ:

- สร้างแอปพลิเคชันสร้างภาพ
- กำหนดขอบเขตสำหรับแอปพลิเคชันของคุณด้วย meta prompts
- ทำงานร่วมกับ DALL-E และ Midjourney

## ทำไมต้องสร้างแอปพลิเคชันสร้างภาพ?

แอปพลิเคชันสร้างภาพเป็นวิธีที่ยอดเยี่ยมในการสำรวจความสามารถของ Generative AI สามารถนำไปใช้ในกรณีต่างๆ เช่น:

- **การแก้ไขและการสังเคราะห์ภาพ** คุณสามารถสร้างภาพสำหรับการใช้งานหลากหลาย เช่น การแก้ไขภาพและการสังเคราะห์ภาพ

- **นำไปใช้ในหลากหลายอุตสาหกรรม** สามารถนำไปใช้สร้างภาพสำหรับอุตสาหกรรมต่างๆ เช่น เทคโนโลยีทางการแพทย์ การท่องเที่ยว การพัฒนาเกม และอื่นๆ

## สถานการณ์: Edu4All

ในบทเรียนนี้ เราจะทำงานร่วมกับสตาร์ทอัพของเรา Edu4All นักเรียนจะสร้างภาพสำหรับการประเมินของพวกเขา โดยภาพที่สร้างขึ้นขึ้นอยู่กับนักเรียน เช่น ภาพประกอบสำหรับนิทานของพวกเขา หรือสร้างตัวละครใหม่สำหรับเรื่องราว หรือช่วยให้พวกเขาเห็นภาพแนวคิดของพวกเขา

ตัวอย่างเช่น นักเรียนของ Edu4All อาจสร้างภาพในชั้นเรียนเกี่ยวกับอนุสรณ์สถาน:

![สตาร์ทอัพ Edu4All, ชั้นเรียนเกี่ยวกับอนุสรณ์สถาน, หอไอเฟล](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.th.png)

โดยใช้ prompt เช่น

> "สุนัขข้างหอไอเฟลในแสงแดดยามเช้า"

## DALL-E และ Midjourney คืออะไร?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) และ [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) เป็นโมเดลการสร้างภาพที่ได้รับความนิยมมากที่สุดสองตัว ซึ่งช่วยให้คุณใช้ prompt ในการสร้างภาพได้

### DALL-E

เริ่มต้นด้วย DALL-E ซึ่งเป็นโมเดล Generative AI ที่สร้างภาพจากคำอธิบายข้อความ

> [DALL-E เป็นการรวมกันของสองโมเดล CLIP และ diffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)

- **CLIP** เป็นโมเดลที่สร้าง embeddings ซึ่งเป็นการแสดงผลข้อมูลในรูปแบบตัวเลขจากภาพและข้อความ

- **Diffused attention** เป็นโมเดลที่สร้างภาพจาก embeddings DALL-E ได้รับการฝึกฝนด้วยชุดข้อมูลของภาพและข้อความ และสามารถใช้สร้างภาพจากคำอธิบายข้อความได้ เช่น DALL-E สามารถใช้สร้างภาพของแมวใส่หมวก หรือสุนัขที่มีทรงผมโมฮอว์ก

### Midjourney

Midjourney ทำงานในลักษณะเดียวกับ DALL-E โดยสร้างภาพจาก prompt ข้อความ Midjourney สามารถใช้สร้างภาพโดยใช้ prompt เช่น "แมวใส่หมวก" หรือ "สุนัขที่มีทรงผมโมฮอว์ก"

![ภาพที่สร้างโดย Midjourney, นกพิราบกลไก](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_เครดิตภาพ Wikipedia, ภาพที่สร้างโดย Midjourney_

## DALL-E และ Midjourney ทำงานอย่างไร

เริ่มต้นด้วย [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst) DALL-E เป็นโมเดล Generative AI ที่ใช้สถาปัตยกรรม transformer พร้อมกับ _autoregressive transformer_

_autoregressive transformer_ กำหนดวิธีที่โมเดลสร้างภาพจากคำอธิบายข้อความ โดยสร้างทีละพิกเซล และใช้พิกเซลที่สร้างขึ้นเพื่อสร้างพิกเซลถัดไป ผ่านหลายชั้นในเครือข่ายประสาทเทียมจนกระทั่งภาพเสร็จสมบูรณ์

ด้วยกระบวนการนี้ DALL-E สามารถควบคุมคุณลักษณะ วัตถุ ลักษณะ และอื่นๆ ในภาพที่สร้างขึ้น อย่างไรก็ตาม DALL-E 2 และ 3 มีการควบคุมภาพที่สร้างขึ้นได้มากกว่า

## การสร้างแอปพลิเคชันสร้างภาพครั้งแรกของคุณ

แล้วการสร้างแอปพลิเคชันสร้างภาพต้องใช้อะไรบ้าง? คุณต้องใช้ไลบรารีดังต่อไปนี้:

- **python-dotenv** ขอแนะนำให้ใช้ไลบรารีนี้เพื่อเก็บข้อมูลลับในไฟล์ _.env_ แยกจากโค้ด
- **openai** ไลบรารีนี้ใช้สำหรับโต้ตอบกับ OpenAI API
- **pillow** สำหรับทำงานกับภาพใน Python
- **requests** เพื่อช่วยในการทำ HTTP requests

## สร้างและปรับใช้โมเดล Azure OpenAI

หากยังไม่ได้ทำ ให้ทำตามคำแนะนำในหน้า [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) 
เพื่อสร้างทรัพยากรและโมเดล Azure OpenAI เลือก DALL-E 3 เป็นโมเดล  

## สร้างแอป

1. สร้างไฟล์ _.env_ ด้วยเนื้อหาดังนี้:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   ค้นหาข้อมูลนี้ใน Azure OpenAI Foundry Portal สำหรับทรัพยากรของคุณในส่วน "Deployments"

1. รวบรวมไลบรารีข้างต้นในไฟล์ _requirements.txt_ ดังนี้:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. จากนั้น สร้าง virtual environment และติดตั้งไลบรารี:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   สำหรับ Windows ใช้คำสั่งต่อไปนี้เพื่อสร้างและเปิดใช้งาน virtual environment:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. เพิ่มโค้ดต่อไปนี้ในไฟล์ชื่อ _app.py_:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # import dotenv
    dotenv.load_dotenv()
    
    # configure Azure OpenAI service client 
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
    try:
        # Create an image by using the image generation API
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # Set the directory for the stored image
        image_dir = os.path.join(os.curdir, 'images')

        # If the directory doesn't exist, create it
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Initialize the image path (note the filetype should be png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Retrieve the generated image
        image_url = generation_response.data[0].url  # extract image URL from response
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

- เริ่มต้น เรานำเข้าไลบรารีที่เราต้องการ รวมถึงไลบรารี OpenAI ไลบรารี dotenv ไลบรารี requests และไลบรารี Pillow

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- ต่อมา เราโหลดตัวแปรสภาพแวดล้อมจากไฟล์ _.env_

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- หลังจากนั้น เรากำหนดค่าลูกค้า Azure OpenAI service 

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- ต่อมา เราสร้างภาพ:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  โค้ดด้านบนตอบกลับด้วยวัตถุ JSON ที่มี URL ของภาพที่สร้างขึ้น เราสามารถใช้ URL เพื่อดาวน์โหลดภาพและบันทึกลงในไฟล์

- สุดท้าย เราเปิดภาพและใช้โปรแกรมดูภาพมาตรฐานเพื่อแสดงภาพ:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### รายละเอียดเพิ่มเติมเกี่ยวกับการสร้างภาพ

มาดูโค้ดที่สร้างภาพในรายละเอียดเพิ่มเติม:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt** คือข้อความที่ใช้ในการสร้างภาพ ในกรณีนี้ เราใช้ prompt "กระต่ายบนม้า ถืออมยิ้ม อยู่ในทุ่งหญ้าที่มีดอกแดฟโฟดิลขึ้นในหมอก"
- **size** คือขนาดของภาพที่สร้างขึ้น ในกรณีนี้ เราสร้างภาพที่มีขนาด 1024x1024 พิกเซล
- **n** คือจำนวนภาพที่สร้างขึ้น ในกรณีนี้ เราสร้างภาพสองภาพ
- **temperature** เป็นพารามิเตอร์ที่ควบคุมความสุ่มของผลลัพธ์ของโมเดล Generative AI ค่า temperature อยู่ระหว่าง 0 ถึง 1 โดยที่ 0 หมายถึงผลลัพธ์เป็นแบบกำหนดแน่นอน และ 1 หมายถึงผลลัพธ์เป็นแบบสุ่ม ค่าเริ่มต้นคือ 0.7

ยังมีสิ่งอื่นๆ ที่คุณสามารถทำได้กับภาพ ซึ่งเราจะครอบคลุมในส่วนถัดไป

## ความสามารถเพิ่มเติมของการสร้างภาพ

คุณได้เห็นแล้วว่าเราสามารถสร้างภาพได้ด้วยโค้ด Python เพียงไม่กี่บรรทัด อย่างไรก็ตาม ยังมีสิ่งอื่นๆ ที่คุณสามารถทำได้กับภาพ

คุณยังสามารถทำสิ่งต่อไปนี้:

- **แก้ไขภาพ** โดยการให้ภาพที่มีอยู่แล้ว หน้ากาก และ prompt คุณสามารถเปลี่ยนแปลงภาพได้ เช่น คุณสามารถเพิ่มบางสิ่งในส่วนหนึ่งของภาพ ลองนึกภาพกระต่ายของเรา คุณสามารถเพิ่มหมวกให้กระต่าย วิธีการทำคือการให้ภาพ หน้ากาก (ระบุส่วนที่ต้องการเปลี่ยนแปลง) และ prompt ข้อความเพื่อบอกว่าควรทำอะไร
> หมายเหตุ: ฟีเจอร์นี้ไม่รองรับใน DALL-E 3

ตัวอย่างเช่น การใช้ GPT Image:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  ภาพพื้นฐานจะมีเพียงเลานจ์ที่มีสระว่ายน้ำ แต่ภาพสุดท้ายจะมีนกฟลามิงโก:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.th.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.th.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.th.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **สร้างภาพแบบต่างๆ** แนวคิดคือการนำภาพที่มีอยู่แล้วและขอให้สร้างภาพแบบต่างๆ เพื่อสร้างภาพแบบต่างๆ คุณให้ภาพและ prompt ข้อความพร้อมโค้ดดังนี้:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > หมายเหตุ ฟีเจอร์นี้รองรับเฉพาะใน OpenAI

## Temperature

Temperature เป็นพารามิเตอร์ที่ควบคุมความสุ่มของผลลัพธ์ของโมเดล Generative AI ค่า temperature อยู่ระหว่าง 0 ถึง 1 โดยที่ 0 หมายถึงผลลัพธ์เป็นแบบกำหนดแน่นอน และ 1 หมายถึงผลลัพธ์เป็นแบบสุ่ม ค่าเริ่มต้นคือ 0.7

มาดูตัวอย่างว่า temperature ทำงานอย่างไร โดยการรัน prompt นี้สองครั้ง:

> Prompt : "กระต่ายบนม้า ถืออมยิ้ม อยู่ในทุ่งหญ้าที่มีดอกแดฟโฟดิลขึ้นในหมอก"

![กระต่ายบนม้าถืออมยิ้ม, เวอร์ชัน 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.th.png)

ตอนนี้ลองรัน prompt เดิมอีกครั้งเพื่อดูว่าเราจะไม่ได้ภาพเดิมสองครั้ง:

![ภาพที่สร้างของกระต่ายบนม้า](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.th.png)

คุณจะเห็นว่าภาพมีความคล้ายกัน แต่ไม่เหมือนกัน ลองเปลี่ยนค่า temperature เป็น 0.1 และดูผลลัพธ์:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### การเปลี่ยนแปลง temperature

ลองทำให้ผลลัพธ์มีความกำหนดแน่นอนมากขึ้น เราสามารถสังเกตจากภาพสองภาพที่เราสร้างขึ้นว่าในภาพแรกมีกระต่าย และในภาพที่สองมีม้า ดังนั้นภาพจึงแตกต่างกันมาก

ดังนั้นลองเปลี่ยนโค้ดของเราและตั้งค่า temperature เป็น 0 ดังนี้:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

เมื่อคุณรันโค้ดนี้ คุณจะได้ภาพสองภาพดังนี้:

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.th.png)
- ![Temperature 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.th.png)

คุณจะเห็นได้ชัดเจนว่าภาพมีความคล้ายกันมากขึ้น

## วิธีการกำหนดขอบเขตสำหรับแอปพลิเคชันของคุณด้วย metaprompts

ด้วยเดโมของเรา เราสามารถสร้างภาพให้ลูกค้าได้แล้ว อย่างไรก็ตาม เราจำเป็นต้องสร้างขอบเขตสำหรับแอปพลิเคชันของเรา

ตัวอย่างเช่น เราไม่ต้องการสร้างภาพที่ไม่เหมาะสมสำหรับการทำงาน หรือไม่เหมาะสมสำหรับเด็ก

เราสามารถทำได้ด้วย _metaprompts_ Metaprompts คือ prompt ข้อความที่ใช้ควบคุมผลลัพธ์ของโมเดล Generative AI ตัวอย่างเช่น เราสามารถใช้ metaprompts เพื่อควบคุมผลลัพธ์ และมั่นใจว่าภาพที่สร้างขึ้นเหมาะสมสำหรับการทำงาน หรือเหมาะสมสำหรับเด็ก

### มันทำงานอย่างไร?

แล้ว metaprompts ทำงานอย่างไร?

Metaprompts คือ prompt ข้อความที่ใช้ควบคุมผลลัพธ์ของโมเดล Generative AI โดยวางไว้ก่อน prompt ข้อความ และใช้ควบคุมผลลัพธ์ของโมเดล และฝังในแอปพลิเคชันเพื่อควบคุมผลลัพธ์ของโมเดล โดยรวม prompt ข้อความและ metaprompt ข้อความใน prompt เดียว

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

ตอนนี้มาดูวิธีการใช้ metaprompts ในเดโมของเรา

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

จาก prompt ด้านบน คุณจะเห็นว่าภาพทั้งหมดที่สร้างขึ้นพิจารณา metaprompt

## งาน - มาสนับสนุนนักเรียนกันเถอะ

เราได้แนะนำ Edu4All ในตอนต้นของบทเรียนนี้ ตอนนี้ถึงเวลาสนับสนุนนักเรียนให้สร้างภาพสำหรับการประเมินของพวกเขา

นักเรียนจะสร้างภาพสำหรับการประเมินของพวกเขาที่มีอนุสรณ์สถาน โดยอนุสรณ์สถานที่เลือกขึ้นอยู่กับนักเรียน นักเรียนถูกขอให้ใช้ความคิดสร้างสรรค์ในงานนี้เพื่อวางอนุสรณ์สถานเหล่านี้ในบริบทที่แตกต่างกัน

## วิธีแก้ไข

นี่คือตัวอย่างวิธีแก้ไขที่เป็นไปได้:
```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# import dotenv
dotenv.load_dotenv()

# Get endpoint and key from environment variables
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
  api_key=os.environ['AZURE_OPENAI_API_KEY'],
  api_version = "2024-02-01"
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
""""

try:
    # Create an image by using the image generation API
    generation_response = client.images.generate(
        prompt=prompt,    # Enter your prompt text here
        size='1024x1024',
        n=1,
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    image_url = generation_response.data[0].url  # extract image URL from response
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
except openai.BadRequestError as err:
    print(err)
```

## ยอดเยี่ยม! เรียนรู้เพิ่มเติมต่อไป

หลังจากจบบทเรียนนี้ ลองดู [คอลเลกชันการเรียนรู้ Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) เพื่อเพิ่มพูนความรู้เกี่ยวกับ Generative AI ของคุณ!

ไปที่บทเรียนที่ 10 ซึ่งเราจะมาดูวิธี [สร้างแอปพลิเคชัน AI ด้วย low-code](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้