<<<<<<< HEAD
<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "063a2ac57d6b71bea0eaa880c68770d2",
  "translation_date": "2025-09-29T21:30:06+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ur"
}
-->
# تصویری تخلیق کی ایپلیکیشنز بنانا

[![تصویری تخلیق کی ایپلیکیشنز بنانا](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.ur.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLMs صرف متن تخلیق کرنے تک محدود نہیں ہیں۔ متن کی وضاحتوں سے تصاویر تخلیق کرنا بھی ممکن ہے۔ تصاویر کو ایک موڈیلٹی کے طور پر استعمال کرنا کئی شعبوں میں انتہائی مفید ہو سکتا ہے، جیسے MedTech، آرکیٹیکچر، سیاحت، گیم ڈیولپمنٹ اور مزید۔ اس باب میں، ہم دو سب سے مشہور تصویری تخلیق کے ماڈلز، DALL-E اور Midjourney کا جائزہ لیں گے۔

## تعارف

اس سبق میں ہم درج ذیل موضوعات کا احاطہ کریں گے:

- تصویری تخلیق اور اس کی افادیت۔
- DALL-E اور Midjourney، یہ کیا ہیں اور کیسے کام کرتے ہیں۔
- تصویری تخلیق کی ایپلیکیشن کیسے بنائی جائے۔

## سیکھنے کے اہداف

اس سبق کو مکمل کرنے کے بعد، آپ:

- تصویری تخلیق کی ایپلیکیشن بنا سکیں گے۔
- اپنی ایپلیکیشن کے لیے میٹا پرامپٹس کے ذریعے حدود مقرر کر سکیں گے۔
- DALL-E اور Midjourney کے ساتھ کام کر سکیں گے۔

## تصویری تخلیق کی ایپلیکیشن کیوں بنائیں؟

تصویری تخلیق کی ایپلیکیشنز جنریٹو AI کی صلاحیتوں کو دریافت کرنے کا ایک بہترین طریقہ ہیں۔ ان کا استعمال درج ذیل کے لیے کیا جا سکتا ہے:

- **تصویری ترمیم اور ترکیب**۔ آپ مختلف استعمال کے لیے تصاویر تخلیق کر سکتے ہیں، جیسے تصویری ترمیم اور تصویری ترکیب۔

- **مختلف صنعتوں میں اطلاق**۔ یہ مختلف صنعتوں جیسے MedTech، سیاحت، گیم ڈیولپمنٹ اور مزید کے لیے تصاویر تخلیق کرنے میں بھی استعمال ہو سکتی ہیں۔

## منظرنامہ: Edu4All

اس سبق کے حصے کے طور پر، ہم اپنے اسٹارٹ اپ، Edu4All کے ساتھ کام جاری رکھیں گے۔ طلباء اپنی اسیسمنٹس کے لیے تصاویر تخلیق کریں گے، تصاویر کی نوعیت طلباء پر منحصر ہے، لیکن وہ اپنی پریوں کی کہانی کے لیے تصاویر بنا سکتے ہیں، اپنے کہانی کے لیے نیا کردار تخلیق کر سکتے ہیں یا اپنے خیالات اور تصورات کو بصری شکل دے سکتے ہیں۔

یہاں ایک مثال ہے کہ Edu4All کے طلباء کلاس میں یادگاروں پر کام کرتے ہوئے کیا تخلیق کر سکتے ہیں:

![Edu4All اسٹارٹ اپ، کلاس میں یادگاروں پر کام، ایفل ٹاور](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.ur.png)

ایسے پرامپٹ کا استعمال کرتے ہوئے:

> "صبح کے وقت کی دھوپ میں ایفل ٹاور کے ساتھ ایک کتا"

## DALL-E اور Midjourney کیا ہیں؟

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) اور [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) دو سب سے مشہور تصویری تخلیق کے ماڈلز ہیں، جو آپ کو پرامپٹس کے ذریعے تصاویر تخلیق کرنے کی اجازت دیتے ہیں۔

### DALL-E

آئیے DALL-E سے شروع کرتے ہیں، جو ایک جنریٹو AI ماڈل ہے جو متن کی وضاحتوں سے تصاویر تخلیق کرتا ہے۔

> [DALL-E دو ماڈلز، CLIP اور diffused attention کا مجموعہ ہے](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)۔

- **CLIP**، ایک ماڈل ہے جو تصاویر اور متن سے ایمبیڈنگز تخلیق کرتا ہے، جو ڈیٹا کی عددی نمائندگی ہوتی ہیں۔

- **Diffused attention**، ایک ماڈل ہے جو ایمبیڈنگز سے تصاویر تخلیق کرتا ہے۔ DALL-E تصاویر اور متن کے ڈیٹا سیٹ پر تربیت یافتہ ہے اور متن کی وضاحتوں سے تصاویر تخلیق کرنے کے لیے استعمال کیا جا سکتا ہے۔ مثال کے طور پر، DALL-E ایک ٹوپی میں بلی یا ایک موہاک کے ساتھ کتا کی تصویر تخلیق کر سکتا ہے۔

### Midjourney

Midjourney بھی DALL-E کی طرح کام کرتا ہے، یہ متن کے پرامپٹس سے تصاویر تخلیق کرتا ہے۔ Midjourney کو بھی ایسے پرامپٹس کے ذریعے تصاویر تخلیق کرنے کے لیے استعمال کیا جا سکتا ہے جیسے "ایک ٹوپی میں بلی" یا "موہاک کے ساتھ کتا"۔

![Midjourney کے ذریعے تخلیق کردہ تصویر، میکینیکل کبوتر](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_تصویر کا کریڈٹ: ویکیپیڈیا، Midjourney کے ذریعے تخلیق کردہ تصویر_

## DALL-E اور Midjourney کیسے کام کرتے ہیں؟

سب سے پہلے، [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)۔ DALL-E ایک جنریٹو AI ماڈل ہے جو ٹرانسفارمر آرکیٹیکچر پر مبنی ہے اور ایک _آٹوریگریسیو ٹرانسفارمر_ کے ساتھ کام کرتا ہے۔

ایک _آٹوریگریسیو ٹرانسفارمر_ وضاحت کرتا ہے کہ ماڈل متن کی وضاحتوں سے تصاویر کیسے تخلیق کرتا ہے، یہ ایک وقت میں ایک پکسل تخلیق کرتا ہے، اور پھر تخلیق کردہ پکسلز کو اگلے پکسل تخلیق کرنے کے لیے استعمال کرتا ہے۔ یہ عمل نیورل نیٹ ورک کی متعدد تہوں سے گزرتا ہے، جب تک کہ تصویر مکمل نہ ہو جائے۔

اس عمل کے ساتھ، DALL-E تخلیق کردہ تصویر میں خصوصیات، اشیاء، خصوصیات، اور مزید کو کنٹرول کرتا ہے۔ تاہم، DALL-E 2 اور 3 تخلیق کردہ تصویر پر زیادہ کنٹرول فراہم کرتے ہیں۔

## اپنی پہلی تصویری تخلیق کی ایپلیکیشن بنانا

تو تصویری تخلیق کی ایپلیکیشن بنانے کے لیے آپ کو کیا چاہیے؟ آپ کو درج ذیل لائبریریاں درکار ہوں گی:

- **python-dotenv**، یہ لائبریری استعمال کرنے کی سختی سے سفارش کی جاتی ہے تاکہ آپ اپنی خفیہ معلومات کو _.env_ فائل میں کوڈ سے دور رکھ سکیں۔
- **openai**، یہ لائبریری آپ OpenAI API کے ساتھ تعامل کے لیے استعمال کریں گے۔
- **pillow**، Python میں تصاویر کے ساتھ کام کرنے کے لیے۔
- **requests**، HTTP درخواستیں بنانے میں مدد کے لیے۔

## Azure OpenAI ماڈل تخلیق اور تعینات کریں

اگر پہلے سے نہیں کیا گیا، تو [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) صفحہ پر دی گئی ہدایات پر عمل کریں
Azure OpenAI ریسورس اور ماڈل تخلیق کرنے کے لیے۔ DALL-E 3 کو ماڈل کے طور پر منتخب کریں۔

## ایپلیکیشن بنائیں

1. _.env_ فائل تخلیق کریں جس میں درج ذیل مواد ہو:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Azure OpenAI Foundry Portal میں اپنے ریسورس کے "Deployments" سیکشن میں یہ معلومات تلاش کریں۔

1. مذکورہ لائبریریوں کو _requirements.txt_ فائل میں جمع کریں، جیسے:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. اس کے بعد، ورچوئل ماحول تخلیق کریں اور لائبریریاں انسٹال کریں:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   ونڈوز کے لیے، ورچوئل ماحول تخلیق اور فعال کرنے کے لیے درج ذیل کمانڈز استعمال کریں:

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

آئیے اس کوڈ کی وضاحت کرتے ہیں:

- سب سے پہلے، ہم ان لائبریریوں کو درآمد کرتے ہیں جن کی ہمیں ضرورت ہے، جن میں OpenAI لائبریری، dotenv لائبریری، requests لائبریری، اور Pillow لائبریری شامل ہیں۔

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- اس کے بعد، ہم _.env_ فائل سے ماحول کے متغیرات لوڈ کرتے ہیں۔

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- اس کے بعد، ہم Azure OpenAI سروس کلائنٹ کو ترتیب دیتے ہیں۔

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- اس کے بعد، ہم تصویر تخلیق کرتے ہیں:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  مذکورہ کوڈ JSON آبجیکٹ کے ساتھ جواب دیتا ہے جس میں تخلیق کردہ تصویر کا URL شامل ہوتا ہے۔ ہم اس URL کو استعمال کرتے ہوئے تصویر ڈاؤنلوڈ کر سکتے ہیں اور اسے فائل میں محفوظ کر سکتے ہیں۔

- آخر میں، ہم تصویر کو کھولتے ہیں اور معیاری تصویر دیکھنے والے کے ذریعے اسے دکھاتے ہیں:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### تصویر تخلیق کرنے کی مزید تفصیلات

آئیے اس کوڈ کو دیکھتے ہیں جو تصویر تخلیق کرتا ہے:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**، وہ متن پرامپٹ ہے جو تصویر تخلیق کرنے کے لیے استعمال ہوتا ہے۔ اس صورت میں، ہم پرامپٹ "گھوڑے پر خرگوش، ہاتھ میں لولی پاپ، دھندلے میدان میں جہاں نرگس کے پھول اگتے ہیں" استعمال کر رہے ہیں۔
- **size**، تخلیق کردہ تصویر کا سائز ہے۔ اس صورت میں، ہم 1024x1024 پکسلز کی تصویر تخلیق کر رہے ہیں۔
- **n**، تخلیق کردہ تصاویر کی تعداد ہے۔ اس صورت میں، ہم دو تصاویر تخلیق کر رہے ہیں۔
- **temperature**، ایک پیرامیٹر ہے جو جنریٹو AI ماڈل کے آؤٹ پٹ کی بے ترتیبی کو کنٹرول کرتا ہے۔ temperature 0 اور 1 کے درمیان ایک قدر ہے جہاں 0 کا مطلب ہے کہ آؤٹ پٹ متعین ہے اور 1 کا مطلب ہے کہ آؤٹ پٹ بے ترتیب ہے۔ ڈیفالٹ قدر 0.7 ہے۔

تصاویر کے ساتھ مزید کام کرنے کے لیے مزید چیزیں ہیں جنہیں ہم اگلے سیکشن میں دیکھیں گے۔

## تصویری تخلیق کی اضافی صلاحیتیں

آپ نے دیکھا کہ ہم چند لائنز کے ذریعے Python میں تصویر تخلیق کرنے کے قابل تھے۔ تاہم، تصاویر کے ساتھ مزید کام بھی کیے جا سکتے ہیں۔

آپ درج ذیل بھی کر سکتے ہیں:

- **ترمیم کریں**۔ موجودہ تصویر، ماسک اور پرامپٹ فراہم کر کے، آپ تصویر میں تبدیلی کر سکتے ہیں۔ مثال کے طور پر، آپ تصویر کے کسی حصے میں کچھ شامل کر سکتے ہیں۔ تصور کریں کہ ہماری خرگوش کی تصویر، آپ خرگوش کو ایک ٹوپی پہنا سکتے ہیں۔ آپ یہ کیسے کریں گے؟ تصویر، ماسک (تبدیلی کے لیے علاقے کی شناخت) اور متن پرامپٹ فراہم کر کے۔
> نوٹ: یہ DALL-E 3 میں سپورٹ نہیں ہے۔

یہاں GPT Image کا استعمال کرتے ہوئے ایک مثال ہے:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  بنیادی تصویر میں صرف پول کے ساتھ لاؤنج ہوگا لیکن حتمی تصویر میں فلیمنگو ہوگا:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.ur.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.ur.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.ur.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **تغیرات تخلیق کریں**۔ خیال یہ ہے کہ آپ موجودہ تصویر لیں اور کہیں کہ تغیرات تخلیق کیے جائیں۔ تغیر تخلیق کرنے کے لیے، آپ تصویر اور متن پرامپٹ فراہم کرتے ہیں اور کوڈ کچھ اس طرح ہوتا ہے:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > نوٹ، یہ صرف OpenAI پر سپورٹ ہے۔

## Temperature

Temperature ایک پیرامیٹر ہے جو جنریٹو AI ماڈل کے آؤٹ پٹ کی بے ترتیبی کو کنٹرول کرتا ہے۔ temperature 0 اور 1 کے درمیان ایک قدر ہے جہاں 0 کا مطلب ہے کہ آؤٹ پٹ متعین ہے اور 1 کا مطلب ہے کہ آؤٹ پٹ بے ترتیب ہے۔ ڈیفالٹ قدر 0.7 ہے۔

آئیے دیکھتے ہیں کہ temperature کیسے کام کرتا ہے، اس پرامپٹ کو دو بار چلا کر:

> پرامپٹ: "گھوڑے پر خرگوش، ہاتھ میں لولی پاپ، دھندلے میدان میں جہاں نرگس کے پھول اگتے ہیں"

![گھوڑے پر خرگوش، ہاتھ میں لولی پاپ، ورژن 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.ur.png)

اب اسی پرامپٹ کو دوبارہ چلائیں تاکہ دیکھ سکیں کہ ہمیں ایک جیسی تصویر دوبارہ نہیں ملے گی:

![گھوڑے پر خرگوش کی تخلیق کردہ تصویر](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.ur.png)

جیسا کہ آپ دیکھ سکتے ہیں، تصاویر ملتی جلتی ہیں، لیکن ایک جیسی نہیں ہیں۔ آئیے temperature کی قدر کو 0.1 پر تبدیل کرتے ہیں اور دیکھتے ہیں کہ کیا ہوتا ہے:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Temperature تبدیل کرنا

تو آئیے آؤٹپٹ کو زیادہ متعین بنانے کی کوشش کرتے ہیں۔ ہم نے تخلیق کردہ دو تصاویر سے مشاہدہ کیا کہ پہلی تصویر میں خرگوش ہے اور دوسری تصویر میں گھوڑا ہے، لہذا تصاویر میں بہت زیادہ فرق ہے۔

آئیے اس لیے اپنے کوڈ کو تبدیل کرتے ہیں اور temperature کو 0 پر سیٹ کرتے ہیں، جیسے:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

اب جب آپ یہ کوڈ چلائیں گے، آپ کو یہ دو تصاویر ملیں گی:

- ![Temperature 0، v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.ur.png)
- ![Temperature 0، v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.ur.png)

یہاں آپ واضح طور پر دیکھ سکتے ہیں کہ تصاویر ایک دوسرے سے زیادہ مشابہت رکھتی ہیں۔

## اپنی ایپلیکیشن کے لیے حدود مقرر کرنے کے لیے میٹا پرامپٹس کا استعمال کیسے کریں

ہمارے ڈیمو کے ساتھ، ہم پہلے ہی اپنے کلائنٹس کے لیے تصاویر تخلیق کر سکتے ہیں۔ تاہم، ہمیں اپنی ایپلیکیشن کے لیے کچھ حدود مقرر کرنے کی ضرورت ہے۔

مثال کے طور پر، ہم ایسی تصاویر تخلیق نہیں کرنا چاہتے جو کام کے لیے محفوظ نہ ہوں، یا جو بچوں کے لیے مناسب نہ ہوں۔

ہم یہ _میٹا پرامپٹس_ کے ذریعے کر سکتے ہیں۔ میٹا پرامپٹس وہ متن پرامپٹس ہیں جو جنریٹو AI ماڈل کے آؤٹپٹ کو کنٹرول کرنے کے لیے استعمال کیے جاتے ہیں۔ مثال کے طور پر، ہم میٹا پرامپٹس کا استعمال آؤٹپٹ کو کنٹرول کرنے کے لیے کر سکتے ہیں، اور اس بات کو یقینی بنا سکتے ہیں کہ تخلیق کردہ تصاویر کام کے لیے محفوظ ہوں، یا بچوں کے لیے مناسب ہوں۔

### یہ کیسے کام کرتا ہے؟

اب، میٹا پرامپٹس کیسے کام کرتے ہیں؟

میٹا پرامپٹس وہ متن پرامپٹس ہیں جو جنریٹو AI ماڈل کے آؤٹپٹ کو کنٹرول کرنے کے لیے استعمال کیے جاتے ہیں، یہ متن پرامپٹ سے پہلے پوزیشن میں ہوتے ہیں، اور ماڈل کے آؤٹپٹ کو کنٹرول کرنے کے لیے استعمال کیے جاتے ہیں اور ایپلیکیشنز میں ماڈل کے آؤٹپٹ کو کنٹرول کرنے کے لیے شامل کیے جاتے ہیں۔ پرامپٹ انپٹ اور میٹا پرامپٹ انپٹ کو ایک متن پرامپٹ میں شامل کرتے ہوئے۔

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

اب، آئیے دیکھتے ہیں کہ ہم اپنے ڈیمو میں میٹا پرامپٹس کا استعمال کیسے کر سکتے ہیں۔

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

مذکورہ پرامپٹ سے، آپ دیکھ سکتے ہیں کہ تخلیق کردہ تمام تصاویر میٹا پرامپٹ کو مدنظر رکھتی ہیں۔

## اسائنمنٹ - طلباء کو فعال کریں

ہم نے اس سبق کے آغاز میں Edu4All کا تعارف کرایا۔ اب وقت ہے کہ طلباء کو ان کی اسیسمنٹس کے لیے تصاویر تخلیق کرنے کے قابل بنایا جائے۔

طلباء اپنی اسیسمنٹس کے لیے یادگاروں پر مشتمل تصاویر تخلیق کریں گے، یادگاروں کی نوعیت طلباء پر منحصر ہے۔ طلباء کو اس کام میں اپنی تخلیقی صلاحیتوں کا استعمال کرنے کے لیے کہا گیا ہے تاکہ ان یادگاروں کو مختلف سیاق و سباق میں رکھا جا سکے۔

## حل

یہاں ایک ممکنہ حل ہے:
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

## شاندار کام! اپنی تعلیم جاری رکھیں

اس سبق کو مکمل کرنے کے بعد، ہماری [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) دیکھیں تاکہ اپنی Generative AI کی معلومات کو مزید بہتر کریں!

سبق نمبر 10 پر جائیں جہاں ہم دیکھیں گے کہ [کم کوڈ کے ساتھ AI ایپلیکیشنز کیسے بنائیں](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔
=======
<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef74ad58fc01f7ad80788f79505f9816",
  "translation_date": "2025-08-26T14:28:32+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ur"
}
-->
# امیج جنریشن ایپلیکیشنز بنانا

[![امیج جنریشن ایپلیکیشنز بنانا](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.ur.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

LLMs صرف ٹیکسٹ جنریشن تک محدود نہیں ہیں۔ آپ ٹیکسٹ ڈسکرپشنز سے امیجز بھی بنا سکتے ہیں۔ امیجز کو ایک موڈیلٹی کے طور پر استعمال کرنا کئی شعبوں میں بہت فائدہ مند ثابت ہو سکتا ہے، جیسے میڈٹیک، آرکیٹیکچر، سیاحت، گیم ڈیولپمنٹ وغیرہ۔ اس باب میں ہم دو سب سے زیادہ مقبول امیج جنریشن ماڈلز، DALL-E اور Midjourney، کے بارے میں جانیں گے۔

## تعارف

اس سبق میں ہم یہ سیکھیں گے:

- امیج جنریشن کیا ہے اور یہ کیوں فائدہ مند ہے۔
- DALL-E اور Midjourney کیا ہیں اور یہ کیسے کام کرتے ہیں۔
- امیج جنریشن ایپ کیسے بنائی جاتی ہے۔

## سیکھنے کے مقاصد

اس سبق کو مکمل کرنے کے بعد آپ یہ کر سکیں گے:

- امیج جنریشن ایپلیکیشن بنانا۔
- اپنی ایپلیکیشن کے لیے میٹا پرامپٹس کے ذریعے حدود مقرر کرنا۔
- DALL-E اور Midjourney کے ساتھ کام کرنا۔

## امیج جنریشن ایپلیکیشن کیوں بنائیں؟

امیج جنریشن ایپلیکیشنز جنریٹو اے آئی کی صلاحیتوں کو دریافت کرنے کا بہترین طریقہ ہیں۔ ان کو مختلف مقاصد کے لیے استعمال کیا جا سکتا ہے، مثلاً:

- **امیج ایڈیٹنگ اور سنتھیسس**۔ آپ مختلف استعمالات کے لیے امیجز بنا سکتے ہیں، جیسے امیج ایڈیٹنگ یا امیج سنتھیسس۔

- **مختلف صنعتوں میں استعمال**۔ یہ ایپلیکیشنز میڈٹیک، سیاحت، گیم ڈیولپمنٹ اور دیگر شعبوں کے لیے امیجز بنانے میں بھی استعمال ہو سکتی ہیں۔

## منظرنامہ: Edu4All

اس سبق میں ہم اپنے اسٹارٹ اپ Edu4All کے ساتھ کام جاری رکھیں گے۔ طلبہ اپنی اسیسمنٹس کے لیے امیجز بنائیں گے، یہ امیجز کس نوعیت کے ہوں گے یہ طلبہ پر منحصر ہے، مثلاً وہ اپنی کہانی کے لیے کوئی کردار بنا سکتے ہیں یا اپنے خیالات اور تصورات کو امیج کی صورت میں پیش کر سکتے ہیں۔

مثال کے طور پر اگر Edu4All کے طلبہ کلاس میں یادگاروں پر کام کر رہے ہوں تو وہ کچھ اس طرح کی امیج بنا سکتے ہیں:

![Edu4All اسٹارٹ اپ، یادگاروں پر کلاس، ایفل ٹاور](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.ur.png)

ایسا پرامپٹ استعمال کرتے ہوئے

> "کتے کی تصویر ایفل ٹاور کے ساتھ، صبح کی نرم روشنی میں"

## DALL-E اور Midjourney کیا ہیں؟

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) اور [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) امیج جنریشن کے دو سب سے زیادہ مقبول ماڈلز ہیں، جو آپ کو پرامپٹس کے ذریعے امیجز بنانے کی سہولت دیتے ہیں۔

### DALL-E

سب سے پہلے DALL-E کی بات کرتے ہیں، یہ ایک جنریٹو اے آئی ماڈل ہے جو ٹیکسٹ ڈسکرپشنز سے امیجز بناتا ہے۔

> [DALL-E دو ماڈلز CLIP اور diffused attention کا مجموعہ ہے](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst)۔

- **CLIP** ایک ماڈل ہے جو امیجز اور ٹیکسٹ سے ایمبیڈنگز بناتا ہے، یعنی ڈیٹا کی عددی نمائندگی۔

- **Diffused attention** ایک ماڈل ہے جو ایمبیڈنگز سے امیجز بناتا ہے۔ DALL-E کو امیجز اور ٹیکسٹ کے ڈیٹا سیٹ پر ٹرین کیا گیا ہے اور یہ ٹیکسٹ ڈسکرپشنز سے امیجز بنا سکتا ہے۔ مثلاً DALL-E سے آپ "ٹوپی پہنے بلی" یا "موہاک والے کتے" کی امیج بنا سکتے ہیں۔

### Midjourney

Midjourney بھی DALL-E کی طرح کام کرتا ہے، یہ ٹیکسٹ پرامپٹس سے امیجز بناتا ہے۔ Midjourney سے بھی آپ "ٹوپی پہنے بلی" یا "موہاک والے کتے" جیسی امیجز بنا سکتے ہیں۔

![Midjourney سے بنی امیج، مکینیکل کبوتر](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_تصویری ماخذ: وکی پیڈیا، امیج Midjourney سے بنی_

## DALL-E اور Midjourney کیسے کام کرتے ہیں

سب سے پہلے [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst)۔ DALL-E ایک جنریٹو اے آئی ماڈل ہے جو ٹرانسفارمر آرکیٹیکچر پر مبنی ہے اور اس میں _آٹو ریگریسیو ٹرانسفارمر_ استعمال ہوتا ہے۔

_آٹو ریگریسیو ٹرانسفارمر_ یہ طے کرتا ہے کہ ماڈل ٹیکسٹ ڈسکرپشنز سے امیجز کیسے بناتا ہے، یہ ایک وقت میں ایک پکسل بناتا ہے اور پھر بنے ہوئے پکسلز کو استعمال کر کے اگلا پکسل بناتا ہے۔ یہ عمل نیورل نیٹ ورک کی کئی لیئرز سے گزرتا ہے، یہاں تک کہ امیج مکمل ہو جائے۔

اس طریقے سے DALL-E امیج میں مختلف خصوصیات، اشیاء اور دیگر عناصر کو کنٹرول کرتا ہے۔ تاہم DALL-E 2 اور 3 میں امیج پر مزید کنٹرول حاصل ہے۔

## اپنی پہلی امیج جنریشن ایپلیکیشن بنائیں

امیج جنریشن ایپ بنانے کے لیے آپ کو یہ لائبریریز درکار ہوں گی:

- **python-dotenv**، اس لائبریری کو استعمال کرنے کی سختی سے سفارش کی جاتی ہے تاکہ آپ اپنی سیکرٹس کو _.env_ فائل میں رکھ سکیں اور کوڈ سے الگ رہیں۔
- **openai**، اس لائبریری کے ذریعے آپ OpenAI API سے رابطہ کریں گے۔
- **pillow**، پائتھون میں امیجز کے ساتھ کام کرنے کے لیے۔
- **requests**، HTTP ریکویسٹ کرنے کے لیے۔

## Azure OpenAI ماڈل بنائیں اور ڈیپلائے کریں

اگر آپ نے پہلے سے نہیں کیا تو [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) صفحہ پر دی گئی ہدایات پر عمل کریں
تاکہ Azure OpenAI ریسورس اور ماڈل بنائیں۔ ماڈل کے طور پر DALL-E 3 منتخب کریں۔  

## ایپ بنائیں

1. _.env_ نامی فائل بنائیں اور اس میں یہ مواد لکھیں:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   یہ معلومات Azure OpenAI Foundry Portal میں اپنے ریسورس کے "Deployments" سیکشن میں تلاش کریں۔

1. اوپر دی گئی لائبریریز کو _requirements.txt_ نامی فائل میں اس طرح جمع کریں:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. اب ورچوئل انوائرمنٹ بنائیں اور لائبریریز انسٹال کریں:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   ونڈوز کے لیے ورچوئل انوائرمنٹ بنانے اور ایکٹیویٹ کرنے کے لیے یہ کمانڈز استعمال کریں:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. _app.py_ نامی فائل میں یہ کوڈ شامل کریں:

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

آئیے اس کوڈ کی وضاحت کرتے ہیں:

- سب سے پہلے ہم مطلوبہ لائبریریز امپورٹ کرتے ہیں، جن میں OpenAI، dotenv، requests اور Pillow شامل ہیں۔

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- اس کے بعد ہم _.env_ فائل سے انوائرمنٹ ویریبلز لوڈ کرتے ہیں۔

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- پھر Azure OpenAI سروس کلائنٹ کو کنفیگر کرتے ہیں

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- اس کے بعد امیج جنریٹ کرتے ہیں:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  یہ کوڈ ایک JSON آبجیکٹ ریٹرن کرتا ہے جس میں بنائی گئی امیج کا URL ہوتا ہے۔ ہم اس URL کو استعمال کر کے امیج ڈاؤن لوڈ کر کے فائل میں محفوظ کر سکتے ہیں۔

- آخر میں امیج کو اوپن کرتے ہیں اور اسٹینڈرڈ امیج ویوئر میں دکھاتے ہیں:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### امیج جنریٹ کرنے کی مزید تفصیل

آئیے اس کوڈ کو تفصیل سے دیکھتے ہیں جو امیج بناتا ہے:

    ```python
      generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                            )
    ```

- **prompt** وہ ٹیکسٹ پرامپٹ ہے جس سے امیج بنتی ہے۔ اس مثال میں ہم "گھوڑے پر خرگوش، ہاتھ میں لالی پاپ، کہر آلود میدان میں جہاں نرگس کے پھول ہیں" استعمال کر رہے ہیں۔
- **size** امیج کا سائز ہے جو بنائی جائے گی۔ یہاں 1024x1024 پکسلز کی امیج بن رہی ہے۔
- **n** امیجز کی تعداد ہے جو بنائی جائے گی۔ یہاں دو امیجز بن رہی ہیں۔
- **temperature** ایک پیرامیٹر ہے جو جنریٹو اے آئی ماڈل کے آؤٹ پٹ کی رینڈم نیس کو کنٹرول کرتا ہے۔ اس کی ویلیو 0 سے 1 کے درمیان ہوتی ہے، 0 پر آؤٹ پٹ ڈیٹرمنسٹک اور 1 پر رینڈم ہوتی ہے۔ ڈیفالٹ ویلیو 0.7 ہے۔

امیجز کے ساتھ مزید کام بھی کیا جا سکتا ہے، جسے ہم اگلے حصے میں دیکھیں گے۔

## امیج جنریشن کی اضافی صلاحیتیں

آپ نے دیکھا کہ ہم نے صرف چند لائنوں کے کوڈ سے امیج بنا لی۔ لیکن امیجز کے ساتھ اور بھی کام کیا جا سکتا ہے۔

آپ یہ بھی کر سکتے ہیں:

- **ایڈیٹس کرنا**۔ کسی موجودہ امیج، ماسک اور پرامپٹ دے کر امیج میں تبدیلی کی جا سکتی ہے۔ مثلاً آپ امیج کے کسی حصے میں کچھ شامل کر سکتے ہیں۔ فرض کریں ہمارے خرگوش کی امیج ہے، آپ اس میں خرگوش کو ٹوپی پہنا سکتے ہیں۔ اس کے لیے امیج، ماسک (جس حصے میں تبدیلی کرنی ہے) اور ٹیکسٹ پرامپٹ دینا ہوتا ہے۔
> نوٹ: یہ DALL-E 3 میں سپورٹڈ نہیں ہے۔ 
 
یہاں GPT Image کی مثال ہے:

    ```python
    response = client.images.edit(
        model="gpt-image-1",
        image=open("sunlit_lounge.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt="A sunlit indoor lounge area with a pool containing a flamingo"
    )
    image_url = response.data[0].url
    ```

  بیس امیج میں صرف لاؤنج اور پول ہوگا، لیکن فائنل امیج میں فلامنگو بھی ہوگا:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="./images/sunlit_lounge.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/mask.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/sunlit_lounge_result.png" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **ویری ایشنز بنانا**۔ اس کا مطلب ہے کہ آپ کسی موجودہ امیج سے مختلف انداز کی امیجز بنائیں۔ اس کے لیے امیج اور ٹیکسٹ پرامپٹ دے کر اس طرح کوڈ لکھیں:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > نوٹ، یہ صرف OpenAI پر سپورٹڈ ہے

## Temperature

Temperature ایک پیرامیٹر ہے جو جنریٹو اے آئی ماڈل کے آؤٹ پٹ کی رینڈم نیس کو کنٹرول کرتا ہے۔ اس کی ویلیو 0 سے 1 کے درمیان ہوتی ہے، 0 پر آؤٹ پٹ ڈیٹرمنسٹک اور 1 پر رینڈم ہوتی ہے۔ ڈیفالٹ ویلیو 0.7 ہے۔

آئیے دیکھتے ہیں کہ temperature کیسے کام کرتا ہے، اس پرامپٹ کو دو بار چلا کر:

> پرامپٹ: "گھوڑے پر خرگوش، ہاتھ میں لالی پاپ، کہر آلود میدان میں جہاں نرگس کے پھول ہیں"

![گھوڑے پر خرگوش، ہاتھ میں لالی پاپ، ورژن 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.ur.png)

اب یہی پرامپٹ دوبارہ چلائیں، آپ دیکھیں گے کہ امیج وہی نہیں آئے گی:

![گھوڑے پر خرگوش کی بنائی گئی امیج](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.ur.png)

جیسا کہ آپ دیکھ سکتے ہیں، امیجز ملتی جلتی ہیں لیکن ایک جیسی نہیں۔ اب temperature کی ویلیو 0.1 کر کے دیکھتے ہیں:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Temperature تبدیل کرنا

اب ہم آؤٹ پٹ کو مزید ڈیٹرمنسٹک بنانے کی کوشش کرتے ہیں۔ ہم نے جو دو امیجز بنائیں ان میں پہلی میں خرگوش ہے اور دوسری میں گھوڑا، یعنی کافی فرق ہے۔

اب ہم اپنا کوڈ تبدیل کرتے ہیں اور temperature کو 0 پر سیٹ کرتے ہیں:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

اب جب آپ یہ کوڈ چلائیں گے تو یہ دو امیجز ملیں گی:

- ![Temperature 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.ur.png)
- ![Temperature 0 , v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.ur.png)

یہاں آپ واضح طور پر دیکھ سکتے ہیں کہ امیجز ایک دوسرے سے زیادہ ملتی ہیں۔

## اپنی ایپلیکیشن کے لیے حدود کیسے مقرر کریں - میٹا پرامپٹس کے ذریعے

ہمارے ڈیمو میں ہم اپنے کلائنٹس کے لیے امیجز بنا سکتے ہیں۔ لیکن ہمیں اپنی ایپلیکیشن کے لیے کچھ حدود مقرر کرنا ہوں گی۔

مثلاً ہم نہیں چاہتے کہ کوئی ایسی امیج بنے جو کام کے لیے غیر محفوظ ہو یا بچوں کے لیے نامناسب ہو۔

یہ کام ہم _میٹا پرامپٹس_ کے ذریعے کر سکتے ہیں۔ میٹا پرامپٹس وہ ٹیکسٹ پرامپٹس ہیں جن کے ذریعے جنریٹو اے آئی ماڈل کے آؤٹ پٹ کو کنٹرول کیا جاتا ہے۔ مثلاً ہم میٹا پرامپٹس کے ذریعے آؤٹ پٹ کو کنٹرول کر سکتے ہیں اور اس بات کو یقینی بنا سکتے ہیں کہ بننے والی امیجز کام کے لیے محفوظ یا بچوں کے لیے مناسب ہوں۔

### یہ کیسے کام کرتے ہیں؟

اب، میٹا پرامپٹس کیسے کام کرتے ہیں؟

میٹا پرامپٹس وہ ٹیکسٹ پرامپٹس ہیں جو ماڈل کے آؤٹ پٹ کو کنٹرول کرنے کے لیے استعمال ہوتے ہیں، یہ اصل پرامپٹ سے پہلے دیے جاتے ہیں اور ایپلیکیشنز میں ماڈل کے آؤٹ پٹ کو کنٹرول کرنے کے لیے شامل کیے جاتے ہیں۔ اس طرح پرامپٹ اور میٹا پرامپٹ کو ایک ہی ٹیکسٹ پرامپٹ میں ضم کیا جاتا ہے۔

میٹا پرامپٹ کی ایک مثال یہ ہو سکتی ہے:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

اب دیکھتے ہیں کہ ہم اپنے ڈیمو میں میٹا پرامپٹس کیسے استعمال کر سکتے ہیں۔

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

اوپر دیے گئے پرامپٹ سے آپ دیکھ سکتے ہیں کہ بننے والی تمام امیجز میں میٹا پرامپٹ کو مدنظر رکھا گیا ہے۔

## اسائنمنٹ - طلبہ کو امیجز بنانے دیں

ہم نے سبق کے آغاز میں Edu4All کا تعارف کروایا تھا۔ اب وقت ہے کہ طلبہ اپنی اسیسمنٹس کے لیے امیجز بنائیں۔

طلبہ اپنی اسیسمنٹس کے لیے یادگاروں کی امیجز بنائیں گے، یہ یادگاریں کون سی ہوں گی یہ طلبہ پر منحصر ہے۔ طلبہ سے کہا گیا ہے کہ وہ اپنی تخلیقی صلاحیتوں کو استعمال کریں اور ان یادگاروں کو مختلف سیاق و سباق میں پیش کریں۔

## حل

یہ ایک ممکنہ حل ہے:

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

## شاندار! اپنی تعلیم جاری رکھیں
اس سبق کو مکمل کرنے کے بعد، ہماری [جنریٹیو اے آئی لرننگ کلیکشن](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) دیکھیں تاکہ آپ اپنی جنریٹیو اے آئی کی معلومات کو مزید بہتر بنا سکیں!

سبق نمبر 10 کی طرف جائیں جہاں ہم دیکھیں گے کہ کس طرح [کم کوڈ کے ساتھ اے آئی ایپلیکیشنز بنائی جا سکتی ہیں](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**اعلانِ دستبرداری**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی بھرپور کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگی ہو سکتی ہے۔ اصل دستاویز اپنی زبان میں مستند ماخذ سمجھی جائے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
>>>>>>> 584a21c5 (Please enter the commit message for your changes. Lines starting)
