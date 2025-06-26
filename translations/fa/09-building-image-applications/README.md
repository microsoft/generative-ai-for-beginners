<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-06-25T17:05:44+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "fa"
}
-->
# ساخت برنامه‌های تولید تصویر

در مدل‌های زبانی بزرگ (LLM) فقط تولید متن نیست که اهمیت دارد. همچنین می‌توان تصاویر را از توصیفات متنی تولید کرد. داشتن تصاویر به عنوان یک حالت می‌تواند در بسیاری از حوزه‌ها از جمله فناوری پزشکی، معماری، گردشگری، توسعه بازی و موارد دیگر بسیار مفید باشد. در این فصل، به بررسی دو مدل تولید تصویر محبوب، DALL-E و Midjourney خواهیم پرداخت.

## مقدمه

در این درس، به موارد زیر خواهیم پرداخت:

- تولید تصویر و دلایل اهمیت آن.
- DALL-E و Midjourney، چه هستند و چگونه کار می‌کنند.
- چگونه می‌توانید یک برنامه تولید تصویر بسازید.

## اهداف یادگیری

پس از تکمیل این درس، قادر خواهید بود:

- یک برنامه تولید تصویر بسازید.
- مرزهایی برای برنامه خود با متا پرامپت‌ها تعریف کنید.
- با DALL-E و Midjourney کار کنید.

## چرا یک برنامه تولید تصویر بسازیم؟

برنامه‌های تولید تصویر راهی عالی برای کشف قابلیت‌های هوش مصنوعی تولیدی هستند. می‌توانند برای مثال برای:

- **ویرایش و ترکیب تصاویر**. می‌توانید تصاویر را برای موارد استفاده مختلف، مانند ویرایش تصویر و ترکیب تصویر تولید کنید.

- **کاربرد در صنایع مختلف**. همچنین می‌توانند برای تولید تصاویر برای صنایع مختلفی مانند فناوری پزشکی، گردشگری، توسعه بازی و موارد دیگر استفاده شوند.

## سناریو: Edu4All

به عنوان بخشی از این درس، به همکاری با استارتاپ خود، Edu4All، ادامه خواهیم داد. دانش‌آموزان تصاویر را برای ارزیابی‌های خود ایجاد خواهند کرد، دقیقاً چه تصاویری به عهده دانش‌آموزان است، اما می‌توانند برای داستان‌های افسانه‌ای خود تصاویر ایجاد کنند یا شخصیت جدیدی برای داستان خود خلق کنند یا به آن‌ها کمک کنند تا ایده‌ها و مفاهیم خود را تجسم کنند.

در اینجا نمونه‌ای از آنچه دانش‌آموزان Edu4All می‌توانند تولید کنند اگر در کلاس روی بناهای تاریخی کار می‌کنند:

![استارتاپ Edu4All، کلاس درباره بناهای تاریخی، برج ایفل](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.fa.png)

با استفاده از پرامپتی مانند

> "سگ کنار برج ایفل در نور صبح زود"

## DALL-E و Midjourney چیستند؟

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) و [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) دو مدل تولید تصویر محبوب هستند که به شما اجازه می‌دهند با استفاده از پرامپت‌ها تصاویر تولید کنید.

### DALL-E

بیایید با DALL-E شروع کنیم، که یک مدل هوش مصنوعی تولیدی است که تصاویر را از توصیفات متنی تولید می‌کند.

> [DALL-E ترکیبی از دو مدل، CLIP و توجه پراکنده است](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**، مدلی است که تعبیه‌ها را تولید می‌کند، که نمایه‌های عددی از داده‌ها هستند، از تصاویر و متن.

- **توجه پراکنده**، مدلی است که تصاویر را از تعبیه‌ها تولید می‌کند. DALL-E بر روی یک مجموعه داده از تصاویر و متن آموزش دیده است و می‌تواند برای تولید تصاویر از توصیفات متنی استفاده شود. به عنوان مثال، DALL-E می‌تواند برای تولید تصاویر از یک گربه با کلاه، یا یک سگ با موهاوک استفاده شود.

### Midjourney

Midjourney به روشی مشابه DALL-E کار می‌کند، تصاویر را از پرامپت‌های متنی تولید می‌کند. Midjourney نیز می‌تواند برای تولید تصاویر با استفاده از پرامپت‌هایی مانند "یک گربه با کلاه" یا "یک سگ با موهاوک" استفاده شود.

![تصویری که توسط Midjourney تولید شده، کبوتر مکانیکی](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_اعتبار تصویر: ویکی‌پدیا، تصویر تولید شده توسط Midjourney_

## DALL-E و Midjourney چگونه کار می‌کنند؟

ابتدا، [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E یک مدل هوش مصنوعی تولیدی بر اساس معماری ترانسفورمر با یک _ترانسفورمر خودبازگشتی_ است.

یک _ترانسفورمر خودبازگشتی_ تعریف می‌کند که چگونه یک مدل تصاویر را از توصیفات متنی تولید می‌کند، یک پیکسل در هر زمان تولید می‌کند، و سپس از پیکسل‌های تولید شده برای تولید پیکسل بعدی استفاده می‌کند. از طریق لایه‌های متعدد در یک شبکه عصبی عبور می‌کند، تا زمانی که تصویر کامل شود.

با این فرآیند، DALL-E، ویژگی‌ها، اشیاء، خصوصیات و موارد دیگر را در تصویری که تولید می‌کند کنترل می‌کند. با این حال، DALL-E 2 و 3 کنترل بیشتری بر روی تصویر تولید شده دارند.

## ساخت اولین برنامه تولید تصویر

بنابراین برای ساخت یک برنامه تولید تصویر چه چیزی لازم است؟ به کتابخانه‌های زیر نیاز دارید:

- **python-dotenv**، اکیداً توصیه می‌شود از این کتابخانه برای نگهداری اطلاعات محرمانه خود در یک فایل _.env_ دور از کد استفاده کنید.
- **openai**، این کتابخانه چیزی است که برای تعامل با API OpenAI استفاده خواهید کرد.
- **pillow**، برای کار با تصاویر در پایتون.
- **requests**، برای کمک به انجام درخواست‌های HTTP.

1. یک فایل _.env_ با محتوای زیر ایجاد کنید:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   این اطلاعات را در پورتال Azure برای منبع خود در بخش "کلیدها و نقطه پایان" پیدا کنید.

1. کتابخانه‌های فوق را در یک فایل به نام _requirements.txt_ جمع‌آوری کنید به این صورت:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. سپس، محیط مجازی ایجاد کرده و کتابخانه‌ها را نصب کنید:

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

- ابتدا، کتابخانه‌هایی که نیاز داریم را وارد می‌کنیم، از جمله کتابخانه OpenAI، کتابخانه dotenv، کتابخانه requests، و کتابخانه Pillow.

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

- بعد از آن، نقطه پایان، کلید برای API OpenAI، نسخه و نوع را تنظیم می‌کنیم.

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

- در نهایت، تصویر را باز کرده و از بیننده تصویر استاندارد برای نمایش آن استفاده می‌کنیم:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### جزئیات بیشتر در مورد تولید تصویر

بیایید نگاهی دقیق‌تر به کدی که تصویر را تولید می‌کند بیندازیم:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **پرامپت**، پرامپت متنی است که برای تولید تصویر استفاده می‌شود. در این مورد، از پرامپت "خرگوش روی اسب، نگه‌دارنده آبنبات، در چمنزاری مه‌آلود که نرگس‌ها رشد می‌کنند" استفاده می‌کنیم.
- **اندازه**، اندازه تصویر تولید شده است. در این مورد، تصویری با اندازه 1024x1024 پیکسل تولید می‌کنیم.
- **n**، تعداد تصاویر تولید شده است. در این مورد، دو تصویر تولید می‌کنیم.
- **دمای**، پارامتری است که تصادفی بودن خروجی یک مدل هوش مصنوعی تولیدی را کنترل می‌کند. دما مقداری بین 0 و 1 است که 0 به معنای خروجی قطعی و 1 به معنای خروجی تصادفی است. مقدار پیش‌فرض 0.7 است.

کارهای بیشتری با تصاویر می‌توانید انجام دهید که در بخش بعدی به آن‌ها خواهیم پرداخت.

## قابلیت‌های اضافی تولید تصویر

تا کنون دیده‌اید که چگونه توانستیم با چند خط در پایتون یک تصویر تولید کنیم. با این حال، کارهای بیشتری می‌توانید با تصاویر انجام دهید.

همچنین می‌توانید کارهای زیر را انجام دهید:

- **انجام ویرایش‌ها**. با ارائه یک تصویر موجود، ماسک و یک پرامپت، می‌توانید تصویری را تغییر دهید. به عنوان مثال، می‌توانید چیزی به قسمتی از یک تصویر اضافه کنید. تصور کنید تصویر خرگوش ما، می‌توانید کلاهی به خرگوش اضافه کنید. چگونه این کار را انجام می‌دهید با ارائه تصویر، یک ماسک (شناسایی بخش ناحیه برای تغییر) و یک پرامپت متنی برای گفتن آنچه باید انجام شود.

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

- **ایجاد تنوع‌ها**. ایده این است که یک تصویر موجود را بگیرید و بخواهید که تنوع‌هایی ایجاد شود. برای ایجاد یک تنوع، یک تصویر و یک پرامپت متنی ارائه می‌دهید و کد به این صورت:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > توجه کنید، این فقط در OpenAI پشتیبانی می‌شود

## دما

دمای پارامتری است که تصادفی بودن خروجی یک مدل هوش مصنوعی تولیدی را کنترل می‌کند. دما مقداری بین 0 و 1 است که 0 به معنای خروجی قطعی و 1 به معنای خروجی تصادفی است. مقدار پیش‌فرض 0.7 است.

بیایید نگاهی به مثالی از چگونگی کارکرد دما بیندازیم، با اجرای این پرامپت دو بار:

> پرامپت: "خرگوش روی اسب، نگه‌دارنده آبنبات، در چمنزاری مه‌آلود که نرگس‌ها رشد می‌کنند"

![خرگوش روی اسب نگه‌دارنده آبنبات، نسخه 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.fa.png)

حالا بیایید همان پرامپت را اجرا کنیم تا ببینیم که دوباره تصویر یکسانی نخواهیم گرفت:

![تصویر تولید شده از خرگوش روی اسب](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.fa.png)

همان‌طور که می‌بینید، تصاویر مشابه هستند، اما یکسان نیستند. بیایید مقدار دما را به 0.1 تغییر دهیم و ببینیم چه اتفاقی می‌افتد:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### تغییر دما

پس بیایید سعی کنیم پاسخ را قطعی‌تر کنیم. می‌توانیم از دو تصویری که تولید کردیم مشاهده کنیم که در تصویر اول، خرگوش وجود دارد و در تصویر دوم، اسب، بنابراین تصاویر به شدت متفاوت هستند.

بنابراین بیایید کد خود را تغییر دهیم و دما را به 0 تنظیم کنیم، به این صورت:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

حالا وقتی این کد را اجرا می‌کنید، این دو تصویر را دریافت می‌کنید:

- ![دمای 0، نسخه 1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.fa.png)
- ![دمای 0، نسخه 2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.fa.png)

اینجا می‌توانید به وضوح ببینید که تصاویر بیشتر به هم شبیه هستند.

## چگونه مرزهایی برای برنامه خود با متا پرامپت‌ها تعریف کنید

با دموی خود، می‌توانیم تصاویر را برای مشتریان خود تولید کنیم. با این حال، باید مرزهایی برای برنامه خود ایجاد کنیم.

به عنوان مثال، نمی‌خواهیم تصاویر غیر مناسب برای کار یا غیر مناسب برای کودکان تولید کنیم.

می‌توانیم این کار را با _متا پرامپت‌ها_ انجام دهیم. متا پرامپت‌ها پرامپت‌های متنی هستند که برای کنترل خروجی یک مدل هوش مصنوعی تولیدی استفاده می‌شوند. به عنوان مثال، می‌توانیم از متا پرامپت‌ها برای کنترل خروجی و اطمینان از اینکه تصاویر تولید شده مناسب برای کار یا مناسب برای کودکان هستند، استفاده کنیم.

### چگونه کار می‌کند؟

حالا، متا پرامپت‌ها چگونه کار می‌کنند؟

متا پرامپت‌ها پرامپت‌های متنی هستند که برای کنترل خروجی یک مدل هوش مصنوعی تولیدی استفاده می‌شوند، آن‌ها قبل از پرامپت متنی قرار می‌گیرند و برای کنترل خروجی مدل استفاده می‌شوند و در برنامه‌ها برای کنترل خروجی مدل جاسازی می‌شوند. ورودی پرامپت و ورودی متا پرامپت را در یک پرامپت متنی واحد کپسوله می‌کنند.

یک نمونه از یک متا پرامپت به صورت زیر خواهد بود:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

حالا، بیایید ببینیم چگونه می‌توانیم از متا پرامپت‌ها در دموی خود استفاده کنیم.

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

از پرامپت بالا، می‌توانید ببینید که چگونه همه تصاویر ایجاد شده متا پرامپت را در نظر می‌گیرند.

## وظیفه - بیایید دانش‌آموزان را فعال کنیم

ما Edu4All را در ابتدای این درس معرفی کردیم. حالا وقت آن است که به دانش‌آموزان اجازه دهیم تصاویر را برای ارزیابی‌های خود تولید کنند.

دانش‌آموزان تصاویر را برای ارزیابی‌های خود که شامل بناهای تاریخی است ایجاد خواهند کرد، دقیقاً چه بناهایی به عهده دانش‌آموزان است. از دانش‌آموزان خواسته می‌شود تا در این وظیفه خلاقیت خود را به کار گیرند و این بناها را در زمینه‌های مختلف قرار دهند.

## راه حل

در اینجا یک راه حل ممکن آمده است:

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

## کار عالی! به یادگیری خود ادامه دهید

پس از تکمیل این درس، مجموعه [یادگیری هوش مصنوعی تولیدی](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ما را بررسی کنید تا به ارتقاء دانش خود در زمینه هوش مصنوعی تولیدی ادامه دهید!

به درس 10 بروید که در آن به چگونگی [ساخت برنامه‌های هوش مصنوعی با کد کم](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) خواهیم پرداخت.

**سلب مسئولیت**:  
این سند با استفاده از خدمات ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادقتی‌هایی باشند. سند اصلی به زبان مادری باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا سوء تعبیر ناشی از استفاده از این ترجمه مسئولیتی نداریم.