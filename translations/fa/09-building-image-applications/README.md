<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T18:58:43+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "fa"
}
-->
# ساخت برنامه‌های تولید تصویر

بیشتر از تولید متن با LLMها می‌توان انجام داد. همچنین می‌توان تصاویر را از توصیفات متنی تولید کرد. داشتن تصاویر به عنوان یک حالت می‌تواند در بسیاری از زمینه‌ها مانند فناوری پزشکی، معماری، گردشگری، توسعه بازی و بیشتر بسیار مفید باشد. در این فصل، به دو مدل تولید تصویر محبوب، DALL-E و Midjourney خواهیم پرداخت.

## مقدمه

در این درس، موارد زیر را پوشش خواهیم داد:

- تولید تصویر و دلیل مفید بودن آن.
- DALL-E و Midjourney، چه هستند و چگونه کار می‌کنند.
- چگونه می‌توانید یک برنامه تولید تصویر بسازید.

## اهداف یادگیری

پس از تکمیل این درس، قادر خواهید بود:

- یک برنامه تولید تصویر بسازید.
- مرزهای برنامه خود را با متا پرامپت‌ها تعریف کنید.
- با DALL-E و Midjourney کار کنید.

## چرا باید یک برنامه تولید تصویر بسازید؟

برنامه‌های تولید تصویر راهی عالی برای کشف قابلیت‌های هوش مصنوعی تولیدی هستند. می‌توانند برای مثال در موارد زیر استفاده شوند:

- **ویرایش و ترکیب تصویر**. می‌توانید تصاویر را برای موارد استفاده مختلف، مانند ویرایش تصویر و ترکیب تصویر تولید کنید.

- **کاربرد در صنایع مختلف**. همچنین می‌توانند برای تولید تصاویر در صنایع مختلف مانند فناوری پزشکی، گردشگری، توسعه بازی و بیشتر استفاده شوند.

## سناریو: Edu4All

به عنوان بخشی از این درس، به همکاری با استارتاپ خود، Edu4All، ادامه خواهیم داد. دانش‌آموزان تصاویر را برای ارزیابی‌های خود ایجاد خواهند کرد، دقیقاً چه تصاویری به عهده دانش‌آموزان است، اما می‌توانند تصاویری برای افسانه‌های خودشان یا ایجاد یک شخصیت جدید برای داستان خود یا کمک به تجسم ایده‌ها و مفاهیمشان ایجاد کنند.

این چیزی است که دانش‌آموزان Edu4All می‌توانند تولید کنند، برای مثال اگر در کلاس روی بناها کار می‌کنند:

با استفاده از پرامپتی مانند

> "سگی کنار برج ایفل در نور صبحگاهی"

## DALL-E و Midjourney چیست؟

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) و [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) دو مدل محبوب تولید تصویر هستند که به شما اجازه می‌دهند با استفاده از پرامپت‌ها تصاویر تولید کنید.

### DALL-E

بیایید با DALL-E شروع کنیم، که یک مدل هوش مصنوعی تولیدی است که تصاویر را از توصیفات متنی تولید می‌کند.

- **CLIP**، مدلی است که تعبیه‌ها را که نمایندگی‌های عددی داده‌ها هستند از تصاویر و متن تولید می‌کند.

- **توجه پراکنده**، مدلی است که تصاویر را از تعبیه‌ها تولید می‌کند. DALL-E بر روی مجموعه‌ای از تصاویر و متن آموزش دیده است و می‌تواند برای تولید تصاویر از توصیفات متنی استفاده شود. برای مثال، DALL-E می‌تواند تصاویر گربه‌ای با کلاه یا سگی با موهاوک تولید کند.

### Midjourney

Midjourney به روشی مشابه DALL-E کار می‌کند، تصاویر را از پرامپت‌های متنی تولید می‌کند. Midjourney همچنین می‌تواند برای تولید تصاویر با استفاده از پرامپت‌هایی مانند "گربه‌ای با کلاه" یا "سگی با موهاوک" استفاده شود.

## DALL-E و Midjourney چگونه کار می‌کنند

اول، [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E یک مدل هوش مصنوعی تولیدی مبتنی بر معماری ترانسفورمر با یک _ترانسفورمر خودبازگشتی_ است.

یک _ترانسفورمر خودبازگشتی_ نحوه تولید تصاویر از توصیفات متنی را تعریف می‌کند، یک پیکسل را در یک زمان تولید می‌کند و سپس از پیکسل‌های تولید شده برای تولید پیکسل بعدی استفاده می‌کند. از طریق چندین لایه در شبکه عصبی عبور می‌کند تا تصویر کامل شود.

با این فرآیند، DALL-E ویژگی‌ها، اشیاء، خصوصیات و موارد دیگر را در تصویری که تولید می‌کند کنترل می‌کند. با این حال، DALL-E 2 و 3 کنترل بیشتری بر روی تصویر تولید شده دارند.

## ساخت اولین برنامه تولید تصویر

پس چه چیزی برای ساخت یک برنامه تولید تصویر لازم است؟ به کتابخانه‌های زیر نیاز دارید:

- **python-dotenv**، توصیه می‌شود از این کتابخانه برای نگهداری اسرار خود در یک فایل _.env_ دور از کد استفاده کنید.
- **openai**، این کتابخانه چیزی است که برای تعامل با API OpenAI استفاده خواهید کرد.
- **pillow**، برای کار با تصاویر در پایتون.
- **requests**، برای کمک به انجام درخواست‌های HTTP.

1. یک فایل _.env_ با محتوای زیر ایجاد کنید:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   این اطلاعات را در پورتال Azure برای منبع خود در بخش "کلیدها و نقطه پایانی" پیدا کنید.

1. کتابخانه‌های فوق را در فایلی به نام _requirements.txt_ جمع‌آوری کنید:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. سپس، محیط مجازی ایجاد کنید و کتابخانه‌ها را نصب کنید:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   برای ویندوز، از دستورات زیر برای ایجاد و فعال کردن محیط مجازی خود استفاده کنید:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. کد زیر را در فایلی به نام _app.py_ اضافه کنید:

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

بیایید این کد را توضیح دهیم:

- ابتدا، کتابخانه‌هایی که نیاز داریم را وارد می‌کنیم، از جمله کتابخانه OpenAI، کتابخانه dotenv، کتابخانه requests و کتابخانه Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- سپس، متغیرهای محیطی را از فایل _.env_ بارگذاری می‌کنیم.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- بعد از آن، نقطه پایانی، کلید برای API OpenAI، نسخه و نوع را تنظیم می‌کنیم.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- سپس، تصویر را تولید می‌کنیم:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  کد بالا با یک شیء JSON پاسخ می‌دهد که حاوی URL تصویر تولید شده است. می‌توانیم از URL برای دانلود تصویر و ذخیره آن در یک فایل استفاده کنیم.

- در نهایت، تصویر را باز می‌کنیم و از نمایشگر استاندارد تصویر برای نمایش آن استفاده می‌کنیم:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### جزئیات بیشتر درباره تولید تصویر

بیایید به کدی که تصویر را تولید می‌کند با جزئیات بیشتری نگاه کنیم:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **پرامپت**، پرامپت متنی است که برای تولید تصویر استفاده می‌شود. در اینجا، از پرامپت "خرگوش بر روی اسب، نگه‌دارنده یک آب‌نبات، در یک چمنزار مه‌آلود که در آن نرگس‌ها رشد می‌کنند" استفاده می‌کنیم.
- **اندازه**، اندازه تصویری است که تولید می‌شود. در اینجا، تصویری که تولید می‌شود 1024x1024 پیکسل است.
- **n**، تعداد تصاویری است که تولید می‌شود. در اینجا، دو تصویر تولید می‌کنیم.
- **دما**، پارامتری است که تصادفی بودن خروجی یک مدل هوش مصنوعی تولیدی را کنترل می‌کند. دما مقداری بین 0 و 1 است که 0 به معنی خروجی قطعی و 1 به معنی خروجی تصادفی است. مقدار پیش‌فرض 0.7 است.

کارهای بیشتری می‌توانید با تصاویر انجام دهید که در بخش بعدی به آن‌ها خواهیم پرداخت.

## قابلیت‌های اضافی تولید تصویر

تا کنون دیده‌اید که چگونه توانستیم با چند خط کد در پایتون یک تصویر تولید کنیم. با این حال، کارهای بیشتری می‌توانید با تصاویر انجام دهید.

همچنین می‌توانید کارهای زیر را انجام دهید:

- **انجام ویرایش‌ها**. با ارائه یک تصویر موجود یک ماسک و یک پرامپت، می‌توانید یک تصویر را تغییر دهید. برای مثال، می‌توانید چیزی به بخشی از یک تصویر اضافه کنید. تصور کنید تصویر خرگوش ما، می‌توانید یک کلاه به خرگوش اضافه کنید. چگونه این کار را انجام می‌دهید با ارائه تصویر، یک ماسک (شناسایی بخشی از منطقه برای تغییر) و یک پرامپت متنی برای گفتن اینکه چه کاری باید انجام شود.

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

  تصویر پایه فقط خرگوش را شامل می‌شود اما تصویر نهایی کلاه را بر روی خرگوش خواهد داشت.

- **ایجاد واریاسیون‌ها**. ایده این است که یک تصویر موجود را بگیرید و درخواست کنید که واریاسیون‌هایی ایجاد شوند. برای ایجاد یک واریاسیون، یک تصویر و یک پرامپت متنی ارائه می‌دهید و کدی مانند زیر:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > توجه کنید، این فقط در OpenAI پشتیبانی می‌شود.

## دما

دما پارامتری است که تصادفی بودن خروجی یک مدل هوش مصنوعی تولیدی را کنترل می‌کند. دما مقداری بین 0 و 1 است که 0 به معنی خروجی قطعی و 1 به معنی خروجی تصادفی است. مقدار پیش‌فرض 0.7 است.

بیایید به مثالی از نحوه کار دما نگاه کنیم، با اجرای این پرامپت دو بار:

> پرامپت: "خرگوش بر روی اسب، نگه‌دارنده یک آب‌نبات، در یک چمنزار مه‌آلود که در آن نرگس‌ها رشد می‌کنند"

حالا بیایید همان پرامپت را اجرا کنیم تا ببینیم که دو بار تصویر یکسانی دریافت نمی‌کنیم:

همانطور که می‌بینید، تصاویر مشابه هستند، اما یکسان نیستند. بیایید سعی کنیم مقدار دما را به 0.1 تغییر دهیم و ببینیم چه اتفاقی می‌افتد:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### تغییر دما

پس بیایید سعی کنیم پاسخ را قطعی‌تر کنیم. می‌توانیم از دو تصویری که تولید کردیم مشاهده کنیم که در تصویر اول، یک خرگوش وجود دارد و در تصویر دوم، یک اسب، بنابراین تصاویر به شدت متفاوت هستند.

بنابراین بیایید کد خود را تغییر دهیم و دما را به 0 تنظیم کنیم، مانند زیر:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

حالا وقتی این کد را اجرا می‌کنید، این دو تصویر را دریافت می‌کنید:

در اینجا می‌توانید به وضوح ببینید که تصاویر بیشتر به یکدیگر شباهت دارند.

## چگونه مرزهایی برای برنامه خود با متا پرامپت‌ها تعریف کنیم

با دمو ما، می‌توانیم تصاویر را برای مشتریان خود تولید کنیم. با این حال، باید برخی مرزها برای برنامه خود ایجاد کنیم.

برای مثال، نمی‌خواهیم تصاویری تولید کنیم که برای کار ایمن نباشند یا برای کودکان مناسب نباشند.

می‌توانیم این کار را با _متا پرامپت‌ها_ انجام دهیم. متا پرامپت‌ها پرامپت‌های متنی هستند که برای کنترل خروجی یک مدل هوش مصنوعی تولیدی استفاده می‌شوند. برای مثال، می‌توانیم از متا پرامپت‌ها برای کنترل خروجی استفاده کنیم و اطمینان حاصل کنیم که تصاویر تولید شده برای کار ایمن هستند یا برای کودکان مناسب هستند.

### چگونه کار می‌کند؟

حالا، چگونه متا پرامپت‌ها کار می‌کنند؟

متا پرامپت‌ها پرامپت‌های متنی هستند که برای کنترل خروجی یک مدل هوش مصنوعی تولیدی استفاده می‌شوند، آن‌ها قبل از پرامپت متنی قرار می‌گیرند و برای کنترل خروجی مدل استفاده می‌شوند و در برنامه‌ها جاسازی می‌شوند تا خروجی مدل را کنترل کنند. پرامپت ورودی و متا پرامپت ورودی را در یک پرامپت متنی واحد محصور می‌کنند.

یک مثال از یک متا پرامپت می‌تواند به صورت زیر باشد:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

حالا، بیایید ببینیم چگونه می‌توانیم از متا پرامپت‌ها در دمو خود استفاده کنیم.

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

از پرامپت بالا می‌توانید ببینید که چگونه همه تصاویر تولید شده متا پرامپت را در نظر می‌گیرند.

## وظیفه - بیایید دانش‌آموزان را توانمند کنیم

ما در ابتدای این درس Edu4All را معرفی کردیم. حالا وقت آن است که دانش‌آموزان را توانمند کنیم تا تصاویر را برای ارزیابی‌هایشان تولید کنند.

دانش‌آموزان تصاویر را برای ارزیابی‌هایشان که شامل بناها است ایجاد خواهند کرد، دقیقاً چه بناهایی به عهده دانش‌آموزان است. از دانش‌آموزان خواسته می‌شود که در این وظیفه خلاقیت خود را به کار گیرند تا این بناها را در زمینه‌های مختلف قرار دهند.

## راه‌حل

اینجا یک راه‌حل ممکن است:

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

## کار عالی! ادامه یادگیری خود

پس از تکمیل این درس، مجموعه [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ما را بررسی کنید تا دانش خود را در زمینه هوش مصنوعی تولیدی ارتقا دهید!

به درس 10 بروید که در آن به نحوه [ساخت برنامه‌های هوش مصنوعی با کد کم](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) خواهیم پرداخت.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌ها باشند. سند اصلی به زبان مادری آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.