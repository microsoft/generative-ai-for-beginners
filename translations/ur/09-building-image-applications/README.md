# امیج جنریشن ایپلیکیشنز کی تعمیر

[![امیج جنریشن ایپلیکیشنز کی تعمیر](../../../translated_images/ur/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

LLMs صرف متن کی تخلیق تک محدود نہیں ہیں۔ متن کی وضاحتوں سے تصاویر پیدا کرنا بھی ممکن ہے۔ ایک موڈالٹی کے طور پر تصویریں مختلف شعبوں میں بے حد مفید ثابت ہو سکتی ہیں، جیسے MedTech, آرکیٹیکچر, سیاحت, گیم ڈیولپمنٹ اور بہت کچھ۔ اس باب میں، ہم دو سب سے مقبول امیج جنریشن ماڈلز، DALL-E اور Midjourney، کا جائزہ لیں گے۔

## تعارف

اس سبق میں، ہم درج ذیل موضوعات کا احاطہ کریں گے:

- تصویر بنانے اور اس کی اہمیت۔
- DALL-E اور Midjourney، کیا ہیں اور کیسے کام کرتے ہیں۔
- ایک امیج جنریشن ایپلیکیشن کیسے بنائی جاتی ہے۔

## سیکھنے کے مقاصد

اس سبق مکمل کرنے کے بعد، آپ کے قابل ہو جائیں گے:

- ایک امیج جنریشن ایپلیکیشن بنانا۔
- اپنے ایپلیکیشن کے لیے حدود میٹا پرامپٹس کی مدد سے مقرر کرنا۔
- DALL-E اور Midjourney کے ساتھ کام کرنا۔

## تصویر بنانے کی ایپلیکیشن کیوں بنائیں؟

تصویر بنانے والی ایپلیکیشنز Generative AI کی صلاحیتوں کو دریافت کرنے کا ایک عمدہ طریقہ ہیں۔ ان کا استعمال، مثلاً، درج ذیل مقاصد کے لیے کیا جا سکتا ہے:

- **تصویری ترمیم اور ترکیب**۔ آپ مختلف استعمال کے کیسز کے لیے تصاویر جنریٹ کر سکتے ہیں، جیسے تصویر کی ترمیم اور تصویر کا ترکیب کرنا۔

- **مختلف صنعتوں میں اطلاق**۔ یہ تصاویر مختلف صنعتوں جیسے Medtech، سیاحت، گیم ڈیولپمنٹ، اور دیگر کے لیے بھی جنریٹ کر سکتے ہیں۔

## منظر نامہ: Edu4All

اس سبق کے حصے کے طور پر، ہم اپنے اسٹارٹ اپ Edu4All کے ساتھ کام جاری رکھیں گے۔ طلباء اپنے اسائنمنٹس کے لیے تصاویر بنائیں گے، کہ کون سی تصاویر بنانی ہیں یہ طلباء کے اوپر ہے، لیکن وہ اپنی کہانی کے لیے مثلاً تصاویر، یا کہانی کے لیے نیا کردار تخلیق کر سکتے ہیں یا اپنی خیالات اور تصورات کو قابل دید بنا سکتے ہیں۔

مثال کے طور پر Edu4All کے طلباء کلاس میں یادگاروں پر کام کر رہے ہوں تو وہ مندرجہ ذیل تصاویر بنا سکتے ہیں:

![Edu4All startup, class on monuments, Eiffel Tower](../../../translated_images/ur/startup.94d6b79cc4bb3f5a.webp)

ایک پرامپٹ استعمال کرتے ہوئے

> "صبح سویرے سورج کی روشنی میں ایفل ٹاور کے پاس کتا"

## DALL-E اور Midjourney کیا ہیں؟

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) اور [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) دو انتہائی مقبول تصویر بنانے کے ماڈلز ہیں، جو پرامپٹس کی مدد سے تصاویر تخلیق کرنے کی سہولت دیتے ہیں۔

### DALL-E

آئیے DALL-E سے شروع کرتے ہیں، جو ایک Generative AI ماڈل ہے جو متن کی تفصیلات سے تصاویر پیدا کرتا ہے۔

> [DALL-E دو ماڈلز، CLIP اور diffused attention، کا مجموعہ ہے](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)۔

- **CLIP** ایک ایسا ماڈل ہے جو تصاویر اور متن سے ڈیٹا کی عددی نمائش کرنے والے embeddings تخلیق کرتا ہے۔

- **Diffused attention** ایک ایسا ماڈل ہے جو embeddings سے تصاویر بناتا ہے۔ DALL-E کو تصاویر اور متن کی ڈیٹاسیٹ پر تربیت دی گئی ہے اور یہ متن کی وضاحتوں سے تصاویر بنا سکتا ہے۔ مثلا، DALL-E سے بلی ٹوپی میں یا موہاک بالوں والے کتے کی تصویر بنوائی جا سکتی ہے۔

### Midjourney

Midjourney بھی DALL-E کی طرح کام کرتا ہے، یہ متن کے پرامپٹس کی بنیاد پر تصاویر تخلیق کرتا ہے۔ Midjourney کو بھی "ٹوپی میں بلی" یا "موہاک بالوں والا کتا" جیسے پرامپٹس سے تصاویر بنانے کے لیے استعمال کیا جا سکتا ہے۔

![Midjourney سے تخلیق کردہ تصویر، میکینیکل کبوتر](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_تصویر کا ماخذ وِکی پیڈیا، تصویر Midjourney نے تخلیق کی ہے_

## DALL-E اور Midjourney کیسے کام کرتے ہیں

پہلے، [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst) پر نظر ڈالتے ہیں۔ DALL-E ایک Generative AI ماڈل ہے جو transformer آرکیٹیکچر پر مبنی ہے اور _autoregressive transformer_ استعمال کرتا ہے۔

ایک _autoregressive transformer_ اس بات کی وضاحت کرتا ہے کہ ماڈل متن کی وضاحتوں سے تصاویر کیسے بناتا ہے، یہ ایک ایک پکسل تخلیق کرتا ہے، اور پھر بنائی گئی پکسلز کو اگلا پکسل بنانے کے لیے استعمال کرتا ہے۔ یہ عمل نیورل نیٹ ورک کی کئی تہوں سے گزرتا ہے یہاں تک کہ تصویر مکمل ہو جاتی ہے۔

اس عمل کی بدولت، DALL-E تصویر میں خصوصیات، اشیاء، خصوصیات وغیرہ کنٹرول کرتا ہے۔ تاہم، DALL-E 2 اور 3 میں تصویر پر زیادہ کنٹرول ہوتا ہے۔

## اپنی پہلی امیج جنریشن ایپلیکیشن بنانا

تو ایک امیج جنریشن ایپلیکیشن بنانے کے لیے کیا چاہیے؟ آپ کو درج ذیل لائبریریز کی ضرورت ہوگی:

- **python-dotenv**، اس لائبریری کو استعمال کرنا سختی سے تجویز کیا جاتا ہے تاکہ آپ کے سیکریٹس کو کوڈ سے دور _.env_ فائل میں رکھا جا سکے۔
- **openai**، یہ لائبریری OpenAI API کے ساتھ تعامل کے لیے استعمال ہوگی۔
- **pillow**، Python میں تصاویر کے ساتھ کام کرنے کے لیے۔
- **requests**، HTTP درخواستیں بنانے میں مدد دیتا ہے۔

## Azure OpenAI ماڈل بنائیں اور ڈیپلائے کریں

اگر ابھی تک نہیں کیا، تو [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) صفحہ پر ہدایات پر عمل کریں
ایک Azure OpenAI ریسورس اور ماڈل بنانے کے لیے۔ ماڈل کے طور پر **gpt-image-1** منتخب کریں (موجودہ نسل کا Azure OpenAI امیج ماڈل؛ DALL-E 3 پرانا ماڈل ہے اور نئی تعیناتیوں کے لیے دستیاب نہیں ہے)۔

## ایپ بنائیں

1. ایک _.env_ فائل بنائیں اور درج ذیل مواد لکھیں:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   Azure OpenAI Foundry پورٹل میں اپنی ریسورس کے "Deployments" سیکشن میں یہ معلومات تلاش کریں۔

1. اوپر دی گئی لائبریریز کو _requirements.txt_ نامی فائل میں جمع کریں، اس طرح:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. اب، ورچوئل انوائرنمنٹ بنائیں اور لائبریریز انسٹال کریں:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   ونڈوز کے لیے، اپنی ورچوئل انوائرنمنٹ بنانے اور فعال کرنے کے لیے درج ذیل کمانڈز استعمال کریں:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ نامی فائل میں درج ذیل کوڈ شامل کریں:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # dotenv کو درآمد کریں
    dotenv.load_dotenv()
    
    # Azure OpenAI سروس کلائنٹ کو ترتیب دیں
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # امیج جنریشن API کا استعمال کرکے ایک تصویر بنائیں
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # تصویر محفوظ کرنے کے لیے ڈائریکٹری مقرر کریں
        image_dir = os.path.join(os.curdir, 'images')

        # اگر ڈائریکٹری موجود نہیں ہے تو اسے بنائیں
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # تصویر کا راستہ مقرر کریں (نوٹ کریں کہ فائل کی قسم png ہونی چاہیے)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # بنائی گئی تصویر حاصل کریں
        image_url = generation_response.data[0].url  # ردعمل سے تصویر کا URL نکالیں
        generated_image = requests.get(image_url).content  # تصویر ڈاؤن لوڈ کریں
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # تصویر کو ڈیفالٹ امیج ویور میں دکھائیں
        image = Image.open(image_path)
        image.show()

    # استثنائی حالات پکڑیں
    except openai.BadRequestError as err:
        print(err)
   ```

آئیے اس کوڈ کی وضاحت کریں:

- سب سے پہلے، ہم اپنی ضرورت کی لائبریریز امپورٹ کرتے ہیں، جن میں OpenAI لائبریری، dotenv، requests، اور Pillow شامل ہیں۔

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- اگلا، ہم ماحولیاتی متغیرات _.env_ فائل سے لوڈ کرتے ہیں۔

  ```python
  # ڈاٹ انوی فائل سے سیٹنگز درآمد کریں
  dotenv.load_dotenv()
  ```

- اس کے بعد، ہم Azure OpenAI سروس کلائنٹ کو کنفیگر کرتے ہیں۔

  ```python
  # اینوائرمنٹ ویری ایبلز سے اینڈپوائنٹ اور کی حاصل کریں
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- پھر، ہم تصویر بناتے ہیں:

  ```python
  # تصویر بنانے کے لیے تصویر جنریشن API استعمال کریں
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  اوپر والا کوڈ ایک JSON آبجیکٹ کے ساتھ جواب دیتا ہے جس میں بنائی گئی تصویر کا URL شامل ہوتا ہے۔ ہم اس URL کو استعمال کر کے تصویر ڈاؤن لوڈ کر کے فائل میں محفوظ کر سکتے ہیں۔

- آخر میں، ہم تصویر کھولتے ہیں اور اسے دیکھنے کے لیے اسٹینڈرڈ امیج ویور استعمال کرتے ہیں:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### تصویر بنانے کی مزید تفصیلات

آئیے تصویر بنانے والے کوڈ کو مزید تفصیل سے دیکھتے ہیں:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**، وہ متن کا پرامپٹ ہے جو تصویر بنانے کے لیے استعمال ہوتا ہے۔ اس مثال میں، ہم "خرگوش گھوڑے پر، لولیپاپ پکڑے ہوئے، دھندلی گھاس میں جہاں نیلن کے پھول اُگتے ہیں" کا پرامپٹ استعمال کر رہے ہیں۔
- **size**، تصویر کا سائز ہے۔ اس مثال میں، ہم 1024x1024 پکسل کی تصویر بنا رہے ہیں۔
- **n**، تصاویر کی تعداد ہے جو بنائی جاتی ہیں۔ اس کیس میں، ہم دو تصاویر بنا رہے ہیں۔
- **temperature**، ایک پیرامیٹر ہے جو Generative AI ماڈل کے آؤٹ پٹ کی randomness کو کنٹرول کرتا ہے۔ temperature کی قیمت 0 سے 1 کے درمیان ہوتی ہے جہاں 0 کا مطلب deterministic یعنی متعین نتیجہ اور 1 کا مطلب بے ترتیب نتیجہ ہوتا ہے۔ ڈیفالٹ ویلیو 0.7 ہے۔

آپ کے لیے تصاویر کے ساتھ مزید کام کرنے کے بہت سے امکانات ہیں جن کا ذکر اگلے سیکشن میں کریں گے۔

## تصویر بنانے کی اضافی خصوصیات

آپ نے دیکھا کہ ہم نے چند لائنز Python کوڈ میں ایک تصویر بنائی۔ تاہم، آپ تصاویر کے ساتھ اور بھی کام کر سکتے ہیں۔

آپ درج ذیل کام بھی کر سکتے ہیں:

- **ترمیمات کریں**۔ موجودہ تصویر کو ماسک اور پرامپٹ فراہم کر کے آپ تصویر میں تبدیلی کر سکتے ہیں۔ مثلاً، ہم اپنی خرگوش کی تصویر میں ٹوپی شامل کر سکتے ہیں۔ یہ کرنے کے لیے آپ تصویر، ایک ماسک (جس میں تبدیلی والے حصے کی نشاندہی ہو) اور ایک ٹیکسٹ پرامپٹ دیں کہ کیا کرنا ہے۔
> نوٹ: یہ DALL-E 3 میں سپورٹڈ نہیں ہے۔
 
یہاں GPT Image کو استعمال کرنے کی ایک مثال ہے:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  بنیاد تصویر میں صرف پل کے ساتھ لانج ہوگی، لیکن آخری تصویر میں فلیمنگو بھی ہوگا:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/ur/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/ur/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/ur/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **متغیرات بنائیں**۔ خیال یہ ہے کہ آپ ایک موجودہ تصویر لے کر اس کی مختلف تغیرات بنائیں۔ تغیر بنانے کے لیے آپ ایک تصویر اور ٹیکسٹ پرامپٹ فراہم کریں اور کوڈ استعمال کریں:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > نوٹ کریں، یہ صرف OpenAI کے DALL-E 2 ماڈل پر ممکن ہے، gpt-image-1 پر نہیں۔

## درجہ حرارت (Temperature)

Temperature Generative AI ماڈل کے آؤٹ پٹ کی randomness کو کنٹرول کرنے والا پیرامیٹر ہے۔ temperature کی قیمت 0 سے 1 کے درمیان ہوتی ہے جہاں 0 کا مطلب deterministic (ایک جیسا نتیجہ) اور 1 کا مطلب random (بے ترتیب) ہوتا ہے۔ ڈیفالٹ ویلیو 0.7 ہے۔

آئیے دیکھتے ہیں کہ temperature کیسے کام کرتا ہے، اس پرامپٹ کو دو بار چلا کر:

> پرامپٹ: "خرگوش گھوڑے پر، لولیپاپ پکڑے ہوئے، دھندلی گھاس میں جہاں نیلن کے پھول اُگتے ہیں"

![خگوش گھوڑے پر لولیپاپ پکڑ رہا ہے، ورژن 1](../../../translated_images/ur/v1-generated-image.a295cfcffa3c13c2.webp)

اب اسی پرامپٹ کو دوبارہ چلاتے ہیں تاکہ دیکھیں کہ ہمیں ایک جیسی تصویر نہیں ملے گی:

![خرگوش گھوڑے پر، تخلیق شدہ تصویر](../../../translated_images/ur/v2-generated-image.33f55a3714efe61d.webp)

جیسا کہ آپ دیکھ سکتے ہیں، تصاویر ملتی جلتی ہیں مگر ایک جیسی نہیں ہیں۔ اب temperature کی ویلیو کو 0.1 کر کے دیکھتے ہیں کہ کیا ہوتا ہے:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # اپنا پرامپٹ متن یہاں درج کریں
        size='1024x1024',
        n=2
    )
```

### درجہ حرارت کی تبدیلی

لہذا ہم ردعمل کو زیادہ متعین بنانا چاہتے ہیں۔ پہلی تصویر میں خرگوش ہے اور دوسری میں گھوڑا، اس لیے تصاویر بہت مختلف ہیں۔

لہذا، ہم کوڈ میں تبدیلی کرتے ہیں اور temperature 0 سیٹ کرتے ہیں، یوں:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # اپنا حکم یہاں درج کریں
        size='1024x1024',
        n=2,
        temperature=0
    )
```

اب جب آپ اس کوڈ کو چلائیں گے، یہ دو تصاویر حاصل کریں گے:

- ![درجہ حرارت 0، ورژن 1](../../../translated_images/ur/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![درجہ حرارت 0، ورژن 2](../../../translated_images/ur/v2-temp-generated-image.871d0c920dbfb0f1.webp)

یہاں آپ واضح طور پر دیکھ سکتے ہیں کہ تصاویر ایک دوسرے سے زیادہ میل کھاتی ہیں۔

## اپنی ایپلیکیشن کے لیے میٹا پرامپٹس کے ذریعے حدود مقرر کرنا

ہماری ڈیمو سے، ہم پہلے ہی اپنے کلائنٹس کے لیے تصاویر بنا سکتے ہیں۔ لیکن ہمیں اپنی ایپلیکیشن کے لیے کچھ حدود مقرر کرنے کی ضرورت ہے۔

مثال کے طور پر، ہم ایسی تصاویر نہیں بنانا چاہتے جو کام کے لیے غیر محفوظ ہوں، یا بچوں کے لیے مناسب نہ ہوں۔

ہم یہ کام _metaprompts_ کے ذریعے کر سکتے ہیں۔ میٹا پرامپٹس وہ ٹیکسٹ پرامپٹس ہوتے ہیں جو Generative AI ماڈل کے آؤٹ پٹ کو کنٹرول کرنے کے لیے استعمال ہوتے ہیں۔ مثلاً، ہم میٹا پرامپٹس کا استعمال آؤٹ پٹ کو کنٹرول کرنے کے لیے کرتے ہیں، اور اس بات کو یقینی بناتے ہیں کہ بنائی گئی تصاویر کام کے لیے محفوظ ہوں یا بچوں کے لیے مناسب ہوں۔

### یہ کیسے کام کرتا ہے؟

میٹا پرامپٹس کیسے کام کرتے ہیں؟

میٹا پرامپٹس وہ ٹیکسٹ پرامپٹس ہیں جو Generative AI ماڈل کے آؤٹ پٹ کو کنٹرول کرتے ہیں۔ یہ ٹیکسٹ پرامپٹ سے پہلے رکھے جاتے ہیں، اور ماڈل کے آؤٹ پٹ کو کنٹرول کرنے کے لیے استعمال ہوتے ہیں۔ یہ ایپلیکیشنز میں امبیڈ کیے جاتے ہیں تاکہ ماڈل کے آؤٹ پٹ کو قابو میں رکھا جا سکے۔ پرامپٹ ان پٹ اور میٹا پرامپٹ ان پٹ کو ایک واحد ٹیکسٹ پرامپٹ میں لپیٹتے ہیں۔

میٹا پرامپٹ کی ایک مثال درج ذیل ہو سکتی ہے:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

اب دیکھتے ہیں کہ ہم اپنی ڈیمو میں میٹا پرامپٹس کو کیسے استعمال کر سکتے ہیں۔

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

# TODO تصویر بنانے کی درخواست شامل کریں
```

اوپر دیے گئے پرامپٹ سے آپ دیکھ سکتے ہیں کہ تخلیق کی گئی تمام تصاویر میٹا پرامپٹ کو مدنظر رکھتی ہیں۔

## اسائنمنٹ - طلباء کو قابل بنائیں

ہم نے اس سبق کے آغاز میں Edu4All کا تعارف کرایا تھا۔ اب وقت ہے کہ طلباء کو ان کے اسائنمنٹس کے لیے تصاویر بنانے کے قابل بنائیں۔


طلباء اپنے اسسمنٹس کے لیے تصاویر بنائیں گے جن میں یادگاریں ہوں گی، یہ یادگاریں کونسی ہوں گی اس کا فیصلہ طلباء پر ہے۔ طلباء سے کہا گیا ہے کہ وہ اس کام میں اپنی تخلیقی صلاحیتوں کا استعمال کریں تاکہ ان یادگاروں کو مختلف سیاق و سباق میں رکھا جا سکے۔

## حل

یہاں ایک ممکن حل پیش کیا گیا ہے:

```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# dotenv درآمد کریں
dotenv.load_dotenv()

# ماحول کے متغیرات سے اینڈپوائنٹ اور کلید حاصل کریں
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
    # تصویری تخلیقی API استعمال کرکے تصویر بنائیں
    generation_response = client.images.generate(
        prompt=prompt,    # اپنا پرامپٹ متن یہاں داخل کریں
        size='1024x1024',
        n=1,
    )
    # محفوظ شدہ تصویر کے لیے ڈائریکٹری سیٹ کریں
    image_dir = os.path.join(os.curdir, 'images')

    # اگر ڈائریکٹری موجود نہیں ہے تو اسے بنائیں
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # تصویر کا راستہ شروع کریں (نوٹ کریں کہ فائل کی قسم png ہونی چاہیے)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # پیدا کی گئی تصویر حاصل کریں
    image_url = generation_response.data[0].url  # جواب سے تصویر کا URL نکالیں
    generated_image = requests.get(image_url).content  # تصویر ڈاؤن لوڈ کریں
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # تصویر کو ڈیفالٹ امیج ویور میں دکھائیں
    image = Image.open(image_path)
    image.show()

# استثنا کو پکڑیں
except openai.BadRequestError as err:
    print(err)
```

## زبردست کام! اپنی تعلیم جاری رکھیں

اس سبق کو مکمل کرنے کے بعد، ہماری [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) دیکھیں تاکہ اپنی Generative AI کی معلومات میں اضافہ جاری رکھ سکیں!

سبق 10 پر جائیں جہاں ہم دیکھیں گے کہ [لو-کوڈ کے ساتھ AI ایپلیکیشنز کیسے بنائی جاتی ہیں](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->