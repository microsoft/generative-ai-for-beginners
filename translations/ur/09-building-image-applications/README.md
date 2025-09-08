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