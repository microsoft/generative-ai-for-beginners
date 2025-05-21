<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T18:59:20+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ur"
}
-->
# امیج جنریشن ایپلیکیشنز بنانا

ایل ایل ایمز میں ٹیکسٹ جنریشن کے علاوہ بھی بہت کچھ ہے۔ ٹیکسٹ ڈسکرپشنز سے امیجز بنانا بھی ممکن ہے۔ امیجز کو ایک موڈیلٹی کے طور پر استعمال کرنا میڈٹیک، آرکیٹیکچر، سیاحت، گیم ڈیولپمنٹ اور دیگر کئی شعبوں میں انتہائی مفید ثابت ہو سکتا ہے۔ اس باب میں، ہم دو سب سے مشہور امیج جنریشن ماڈلز، DALL-E اور Midjourney کا جائزہ لیں گے۔

## تعارف

اس سبق میں، ہم کور کریں گے:

- امیج جنریشن اور یہ کیوں مفید ہے۔
- DALL-E اور Midjourney، یہ کیا ہیں اور کیسے کام کرتے ہیں۔
- آپ کیسے ایک امیج جنریشن ایپ بنائیں گے۔

## سیکھنے کے مقاصد

اس سبق کو مکمل کرنے کے بعد، آپ قابل ہوں گے:

- ایک امیج جنریشن ایپلیکیشن بنائیں۔
- میٹا پرامپٹس کے ساتھ اپنی ایپلیکیشن کے لیے حدود مقرر کریں۔
- DALL-E اور Midjourney کے ساتھ کام کریں۔

## امیج جنریشن ایپلیکیشن کیوں بنائیں؟

امیج جنریشن ایپلیکیشنز جنریٹو اے آئی کی صلاحیتوں کو دریافت کرنے کا ایک بہترین طریقہ ہیں۔ انہیں، مثال کے طور پر، استعمال کیا جا سکتا ہے:

- **امیج ایڈیٹنگ اور سنتھیسس**۔ آپ مختلف استعمال کے کیسز کے لیے امیجز بنا سکتے ہیں، جیسے کہ امیج ایڈیٹنگ اور امیج سنتھیسس۔

- **مختلف صنعتوں پر لاگو**۔ انہیں مختلف صنعتوں جیسے میڈٹیک، سیاحت، گیم ڈیولپمنٹ اور دیگر کے لیے امیجز بنانے کے لیے بھی استعمال کیا جا سکتا ہے۔

## منظرنامہ: Edu4All

اس سبق کے حصے کے طور پر، ہم اپنے اسٹارٹ اپ، Edu4All کے ساتھ کام جاری رکھیں گے۔ طلباء اپنی اسیسمنٹس کے لیے امیجز بنائیں گے، کون سی امیجز بنانی ہیں یہ طلباء پر منحصر ہے، لیکن یہ ان کی اپنی پریوں کی کہانی کے لیے تصویریں ہو سکتی ہیں یا ان کی کہانی کے لیے ایک نیا کردار بنا سکتے ہیں یا ان کے خیالات اور تصورات کو تصور کرنے میں ان کی مدد کر سکتے ہیں۔

یہاں Edu4All کے طلباء کیا بنا سکتے ہیں اگر وہ کلاس میں یادگاروں پر کام کر رہے ہیں:

![Edu4All اسٹارٹ اپ، کلاس آن مونیومنٹس، ایفل ٹاور](../../../translated_images/startup.ec211d74fef9f4175010c3334942b715514230415744b9dd0a69a19f4ad68786.ur.png)

ایک پرامپٹ جیسے

> "کتّا ایفل ٹاور کے ساتھ صبح کی روشنی میں"

## DALL-E اور Midjourney کیا ہیں؟

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) اور [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) دو سب سے مشہور امیج جنریشن ماڈلز ہیں، یہ آپ کو پرامپٹس کا استعمال کر کے امیجز بنانے کی اجازت دیتے ہیں۔

### DALL-E

آئیے DALL-E سے شروع کرتے ہیں، جو کہ ایک جنریٹو اے آئی ماڈل ہے جو ٹیکسٹ ڈسکرپشنز سے امیجز بناتا ہے۔

> [DALL-E دو ماڈلز، CLIP اور ڈفیوزڈ اٹینشن کا مجموعہ ہے](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)۔

- **CLIP**، ایک ماڈل ہے جو امیجز اور ٹیکسٹ سے ایمبیڈنگز، جو کہ ڈیٹا کی عددی نمائندگی ہوتی ہیں، بناتا ہے۔

- **ڈفیوزڈ اٹینشن**، ایک ماڈل ہے جو ایمبیڈنگز سے امیجز بناتا ہے۔ DALL-E امیجز اور ٹیکسٹ کے ڈیٹا سیٹ پر تربیت یافتہ ہے اور ٹیکسٹ ڈسکرپشنز سے امیجز بنانے کے لیے استعمال کیا جا سکتا ہے۔ مثال کے طور پر، DALL-E کو ٹوپی میں بلی یا موہاک والے کتے کی امیجز بنانے کے لیے استعمال کیا جا سکتا ہے۔

### Midjourney

Midjourney بھی DALL-E کی طرح کام کرتا ہے، یہ ٹیکسٹ پرامپٹس سے امیجز بناتا ہے۔ Midjourney کو بھی "ٹوپی میں بلی" یا "موہاک والا کتا" جیسے پرامپٹس کا استعمال کر کے امیجز بنانے کے لیے استعمال کیا جا سکتا ہے۔

![Midjourney کے ذریعے بنائی گئی امیج، مکینیکل کبوتر](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_تصویری کریڈٹ ویکیپیڈیا، Midjourney کے ذریعے بنائی گئی تصویر_

## DALL-E اور Midjourney کیسے کام کرتے ہیں

سب سے پہلے، [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)۔ DALL-E ایک جنریٹو اے آئی ماڈل ہے جو ٹرانسفارمر آرکیٹیکچر پر مبنی ہے جس میں ایک _آٹو ریگریسیو ٹرانسفارمر_ ہوتا ہے۔

ایک _آٹو ریگریسیو ٹرانسفارمر_ اس بات کی وضاحت کرتا ہے کہ ماڈل ٹیکسٹ ڈسکرپشنز سے امیجز کیسے بناتا ہے، یہ ایک وقت میں ایک پکسل بناتا ہے، اور پھر اگلے پکسل کو بنانے کے لیے بنائے گئے پکسلز کا استعمال کرتا ہے۔ ایک نیورل نیٹ ورک کی متعدد تہوں سے گزرتا ہے، جب تک کہ تصویر مکمل نہ ہو جائے۔

اس عمل کے ساتھ، DALL-E، امیج میں بنائے گئے صفات، اشیاء، خصوصیات اور مزید کو کنٹرول کرتا ہے۔ تاہم، DALL-E 2 اور 3 کو بنائی گئی تصویر پر زیادہ کنٹرول حاصل ہے۔

## اپنی پہلی امیج جنریشن ایپلیکیشن بنانا

تو ایک امیج جنریشن ایپلیکیشن بنانے کے لیے کیا درکار ہوتا ہے؟ آپ کو درج ذیل لائبریریوں کی ضرورت ہے:

- **python-dotenv**، آپ کو اپنی خفیہ معلومات کو _.env_ فائل میں کوڈ سے دور رکھنے کے لیے اس لائبریری کو استعمال کرنے کی سختی سے سفارش کی جاتی ہے۔
- **openai**، یہ لائبریری آپ OpenAI API کے ساتھ بات چیت کرنے کے لیے استعمال کریں گے۔
- **pillow**، Python میں امیجز کے ساتھ کام کرنے کے لیے۔
- **requests**، آپ کو HTTP درخواستیں بنانے میں مدد کرنے کے لیے۔

1. درج ذیل مواد کے ساتھ ایک فائل _.env_ بنائیں:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   اپنے وسائل کے لیے Azure پورٹل میں "Keys and Endpoint" سیکشن میں یہ معلومات تلاش کریں۔

1. مذکورہ لائبریریوں کو _requirements.txt_ نامی فائل میں جمع کریں جیسے:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. اگلا، ورچوئل ماحول بنائیں اور لائبریریاں انسٹال کریں:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   ونڈوز کے لیے، اپنے ورچوئل ماحول کو بنانے اور فعال کرنے کے لیے درج ذیل کمانڈز کا استعمال کریں:

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

آئیے اس کوڈ کی وضاحت کریں:

- پہلے، ہم ان لائبریریوں کو درآمد کرتے ہیں جن کی ہمیں ضرورت ہے، بشمول OpenAI لائبریری، dotenv لائبریری، requests لائبریری، اور Pillow لائبریری۔

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- اگلا، ہم _.env_ فائل سے ماحولیاتی متغیرات لوڈ کرتے ہیں۔

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- اس کے بعد، ہم OpenAI API کے لیے اینڈ پوائنٹ، کلید، ورژن اور قسم مرتب کرتے ہیں۔

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- اگلا، ہم امیج بناتے ہیں:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  مذکورہ بالا کوڈ ایک JSON آبجیکٹ کے ساتھ جواب دیتا ہے جس میں بنائی گئی امیج کا URL ہوتا ہے۔ ہم تصویر کو ڈاؤن لوڈ کرنے اور فائل میں محفوظ کرنے کے لیے URL استعمال کر سکتے ہیں۔

- آخر میں، ہم امیج کھولتے ہیں اور اسے دکھانے کے لیے معیاری امیج ویور استعمال کرتے ہیں:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### امیج بنانے کی مزید تفصیلات

آئیے اس کوڈ کو دیکھیں جو امیج کو مزید تفصیل سے بناتا ہے:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**، وہ ٹیکسٹ پرامپٹ ہے جو امیج بنانے کے لیے استعمال ہوتا ہے۔ اس صورت میں، ہم پرامپٹ "گھوڑے پر خرگوش، لولی پاپ پکڑے ہوئے، دھندلے میدان میں جہاں نرگس کے پھول اگتے ہیں" استعمال کر رہے ہیں۔
- **size**، بنائی گئی امیج کا سائز ہے۔ اس صورت میں، ہم ایک امیج بنا رہے ہیں جو 1024x1024 پکسلز کی ہے۔
- **n**، بنائی گئی امیجز کی تعداد ہے۔ اس صورت میں، ہم دو امیجز بنا رہے ہیں۔
- **temperature**، ایک پیرامیٹر ہے جو جنریٹو اے آئی ماڈل کے آؤٹ پٹ کی بے قاعدگی کو کنٹرول کرتا ہے۔ درجہ حرارت 0 اور 1 کے درمیان ایک قدر ہے جہاں 0 کا مطلب ہے کہ آؤٹ پٹ تعین شدہ ہے اور 1 کا مطلب ہے کہ آؤٹ پٹ بے قاعدہ ہے۔ ڈیفالٹ ویلیو 0.7 ہے۔

امیجز کے ساتھ کرنے کے لیے مزید چیزیں ہیں جو ہم اگلے سیکشن میں کور کریں گے۔

## امیج جنریشن کی اضافی صلاحیتیں

آپ نے دیکھا کہ ہم چند لائنوں میں Python میں امیج بنا سکتے ہیں۔ تاہم، امیجز کے ساتھ کرنے کے لیے مزید چیزیں ہیں۔

آپ یہ بھی کر سکتے ہیں:

- **ترمیمات انجام دیں**۔ ایک موجودہ امیج، ایک ماسک اور ایک پرامپٹ فراہم کر کے، آپ امیج کو تبدیل کر سکتے ہیں۔ مثال کے طور پر، آپ امیج کے کسی حصے میں کچھ شامل کر سکتے ہیں۔ ہمارے خرگوش کی امیج کا تصور کریں، آپ خرگوش پر ایک ٹوپی شامل کر سکتے ہیں۔ آپ یہ کیسے کریں گے کہ امیج، ایک ماسک (تبدیلی کے لیے علاقے کی شناخت کرنا) اور ایک ٹیکسٹ پرامپٹ فراہم کر کے کہا جائے کہ کیا کیا جانا چاہیے۔

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

  بنیادی امیج میں صرف خرگوش ہوگا لیکن حتمی امیج میں خرگوش پر ٹوپی ہوگی۔

- **تغیرات بنائیں**۔ خیال یہ ہے کہ آپ ایک موجودہ امیج لیں اور اس کی مختلف حالتیں بنوائیں۔ ایک تغیر پیدا کرنے کے لیے، آپ ایک امیج اور ایک ٹیکسٹ پرامپٹ فراہم کرتے ہیں اور کوڈ کچھ اس طرح ہوتا ہے:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > نوٹ کریں، یہ صرف OpenAI پر سپورٹڈ ہے

## درجہ حرارت

درجہ حرارت ایک پیرامیٹر ہے جو جنریٹو اے آئی ماڈل کے آؤٹ پٹ کی بے قاعدگی کو کنٹرول کرتا ہے۔ درجہ حرارت 0 اور 1 کے درمیان ایک قدر ہے جہاں 0 کا مطلب ہے کہ آؤٹ پٹ تعین شدہ ہے اور 1 کا مطلب ہے کہ آؤٹ پٹ بے قاعدہ ہے۔ ڈیفالٹ ویلیو 0.7 ہے۔

آئیے دیکھتے ہیں کہ درجہ حرارت کیسے کام کرتا ہے، اس پرامپٹ کو دو بار چلا کر:

> پرامپٹ: "گھوڑے پر خرگوش، لولی پاپ پکڑے ہوئے، دھندلے میدان میں جہاں نرگس کے پھول اگتے ہیں"

![گھوڑے پر لولی پاپ پکڑے ہوئے خرگوش، ورژن 1](../../../translated_images/v1-generated-image.208ba0525ed6ae505504aa852e28d334c0440e9931b7c97f9508176a22d2dd54.ur.png)

اب آئیے وہی پرامپٹ چلائیں تاکہ دیکھیں کہ ہمیں دو بار ایک ہی امیج نہیں ملے گی:

![گھوڑے پر خرگوش کی بنائی گئی امیج](../../../translated_images/v2-generated-image.f0a88c05ef476e95f3682d4b21c9ba2f4807ae71cc29e9c05b42ebbf497cf61b.ur.png)

جیسا کہ آپ دیکھ سکتے ہیں، امیجز ایک جیسی ہیں، لیکن ایک جیسی نہیں۔ آئیے درجہ حرارت کی قیمت کو 0.1 پر تبدیل کریں اور دیکھیں کہ کیا ہوتا ہے:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### درجہ حرارت کو تبدیل کرنا

تو آئیے جواب کو زیادہ تعین شدہ بنانے کی کوشش کریں۔ ہم نے جو دو امیجز بنائی ہیں ان سے ہم مشاہدہ کر سکتے ہیں کہ پہلی امیج میں ایک خرگوش ہے اور دوسری امیج میں ایک گھوڑا ہے، اس لیے امیجز میں کافی فرق ہے۔

آئیے اس لیے اپنا کوڈ تبدیل کریں اور درجہ حرارت کو 0 پر سیٹ کریں، جیسے:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

اب جب آپ یہ کوڈ چلاتے ہیں، تو آپ کو یہ دو امیجز ملتی ہیں:

- ![درجہ حرارت 0، v1](../../../translated_images/v1-temp-generated-image.d8557be792b5c81c2c6d2804cb7b210fe8b340106fe4ffcadf9cf7de1cd7b991.ur.png)
- ![درجہ حرارت 0، v2](../../../translated_images/v2-temp-generated-image.bd412fcfbd43379312b1382212a332aa311ca1a80ea692dea50a8b876a487c61.ur.png)

یہاں آپ واضح طور پر دیکھ سکتے ہیں کہ امیجز ایک دوسرے سے زیادہ ملتی جلتی ہیں۔

## اپنی ایپلیکیشن کے لیے میٹا پرامپٹس کے ساتھ حدود کیسے مقرر کریں

ہمارے ڈیمو کے ساتھ، ہم پہلے ہی اپنے کلائنٹس کے لیے امیجز بنا سکتے ہیں۔ تاہم، ہمیں اپنی ایپلیکیشن کے لیے کچھ حدود بنانی ہوں گی۔

مثال کے طور پر، ہم ایسی امیجز نہیں بنانا چاہتے جو کام کے لیے محفوظ نہ ہوں، یا جو بچوں کے لیے مناسب نہ ہوں۔

ہم یہ _میٹا پرامپٹس_ کے ساتھ کر سکتے ہیں۔ میٹا پرامپٹس وہ ٹیکسٹ پرامپٹس ہیں جو جنریٹو اے آئی ماڈل کے آؤٹ پٹ کو کنٹرول کرنے کے لیے استعمال ہوتے ہیں۔ مثال کے طور پر، ہم میٹا پرامپٹس کو آؤٹ پٹ کو کنٹرول کرنے کے لیے استعمال کر سکتے ہیں، اور اس بات کو یقینی بنا سکتے ہیں کہ بنائی گئی امیجز کام کے لیے محفوظ ہوں، یا بچوں کے لیے مناسب ہوں۔

### یہ کیسے کام کرتا ہے؟

اب، میٹا پرامپٹس کیسے کام کرتے ہیں؟

میٹا پرامپٹس وہ ٹیکسٹ پرامپٹس ہیں جو جنریٹو اے آئی ماڈل کے آؤٹ پٹ کو کنٹرول کرنے کے لیے استعمال ہوتے ہیں، انہیں ٹیکسٹ پرامپٹ سے پہلے رکھا جاتا ہے، اور ماڈل کے آؤٹ پٹ کو کنٹرول کرنے کے لیے استعمال ہوتے ہیں اور ماڈل کے آؤٹ پٹ کو کنٹرول کرنے کے لیے ایپلیکیشنز میں شامل ہوتے ہیں۔ پرامپٹ ان پٹ اور میٹا پرامپٹ ان پٹ کو ایک واحد ٹیکسٹ پرامپٹ میں شامل کرنا۔

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

اب، آئیے دیکھتے ہیں کہ ہم اپنے ڈیمو میں میٹا پرامپٹس کو کیسے استعمال کر سکتے ہیں۔

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

اوپر دیے گئے پرامپٹ سے، آپ دیکھ سکتے ہیں کہ بنائی جانے والی تمام امیجز میٹا پرامپٹ کو مدنظر رکھتی ہیں۔

## اسائنمنٹ - طلباء کو فعال کریں

ہم نے اس سبق کے آغاز میں Edu4All کا تعارف کرایا۔ اب وقت آگیا ہے کہ طلباء کو ان کی اسیسمنٹس کے لیے امیجز بنانے کے قابل بنایا جائے۔

طلباء اپنی اسیسمنٹس کے لیے امیجز بنائیں گے جن میں یادگاریں شامل ہوں گی، کون سی یادگاریں ہیں یہ طلباء پر منحصر ہے۔ طلباء سے کہا جاتا ہے کہ وہ اس کام میں اپنی تخلیقی صلاحیتوں کا استعمال کریں اور ان یادگاروں کو مختلف سیاق و سباق میں رکھیں۔

## حل

یہاں ایک ممکنہ حل ہے:

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

## زبردست کام! اپنی تعلیم جاری رکھیں

اس سبق کو مکمل کرنے کے بعد، ہماری [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) کو دیکھیں تاکہ اپنی جنریٹو اے آئی کی معلومات کو مزید بڑھا سکیں!

سبق 10 کی طرف بڑھیں جہاں ہم دیکھیں گے کہ [کم کوڈ کے ساتھ اے آئی ایپلیکیشنز کیسے بنائیں](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**دستبرداری**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشاں ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی مقامی زبان میں مستند ماخذ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔