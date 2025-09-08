<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ef74ad58fc01f7ad80788f79505f9816",
  "translation_date": "2025-08-26T14:17:09+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "fa"
}
-->
# ساخت برنامه‌های تولید تصویر

[![ساخت برنامه‌های تولید تصویر](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.fa.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

مدل‌های زبانی بزرگ فقط برای تولید متن نیستند. امکان تولید تصویر از توضیحات متنی هم وجود دارد. داشتن تصویر به عنوان یک مدالیته می‌تواند در حوزه‌های مختلفی مثل فناوری پزشکی، معماری، گردشگری، توسعه بازی و غیره بسیار مفید باشد. در این فصل، به دو مدل محبوب تولید تصویر یعنی DALL-E و Midjourney می‌پردازیم.

## مقدمه

در این درس، موارد زیر را بررسی خواهیم کرد:

- تولید تصویر و دلایل اهمیت آن.
- DALL-E و Midjourney، چی هستند و چطور کار می‌کنند.
- چطور می‌توانید یک اپلیکیشن تولید تصویر بسازید.

## اهداف یادگیری

پس از پایان این درس، شما قادر خواهید بود:

- یک برنامه تولید تصویر بسازید.
- با استفاده از متاپرومت‌ها، مرزهای اپلیکیشن خود را تعریف کنید.
- با DALL-E و Midjourney کار کنید.

## چرا باید یک برنامه تولید تصویر بسازیم؟

برنامه‌های تولید تصویر راهی عالی برای کشف قابلیت‌های هوش مصنوعی مولد هستند. این برنامه‌ها می‌توانند برای مثال در موارد زیر استفاده شوند:

- **ویرایش و ترکیب تصویر**. می‌توانید برای کاربردهای مختلف مثل ویرایش یا ترکیب تصویر، تصاویر جدید تولید کنید.

- **قابل استفاده در صنایع مختلف**. همچنین می‌توانند برای تولید تصویر در صنایعی مثل فناوری پزشکی، گردشگری، توسعه بازی و غیره به کار روند.

## سناریو: Edu4All

در این درس، همچنان با استارتاپ خودمان یعنی Edu4All کار خواهیم کرد. دانش‌آموزان قرار است برای ارزیابی‌های خود تصویر بسازند. اینکه چه تصویری بسازند به خودشان بستگی دارد؛ مثلاً می‌توانند برای داستان خود تصویرسازی کنند، شخصیت جدیدی خلق کنند یا ایده‌ها و مفاهیم‌شان را تجسم کنند.

برای مثال، اگر دانش‌آموزان Edu4All در کلاس درباره بناهای تاریخی کار می‌کنند، می‌توانند چنین تصویری تولید کنند:

![استارتاپ Edu4All، کلاس درباره بناها، برج ایفل](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.fa.png)

با استفاده از پرامپتی مثل:

> "سگی کنار برج ایفل در نور آفتاب صبح زود"

## DALL-E و Midjourney چیستند؟

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) و [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) دو مدل بسیار محبوب تولید تصویر هستند که به شما اجازه می‌دهند با دادن پرامپت، تصویر بسازید.

### DALL-E

بیایید با DALL-E شروع کنیم؛ مدلی از هوش مصنوعی مولد که تصاویر را از توضیحات متنی تولید می‌کند.

> [DALL-E ترکیبی از دو مدل CLIP و diffused attention است](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**، مدلی است که از تصاویر و متن، embedding (نمایش عددی داده‌ها) تولید می‌کند.

- **Diffused attention**، مدلی است که از embeddingها تصویر می‌سازد. DALL-E روی دیتاستی از تصاویر و متن آموزش دیده و می‌تواند از توضیحات متنی، تصویر بسازد. مثلاً DALL-E می‌تواند تصویری از گربه‌ای با کلاه یا سگی با مدل موی موهاک بسازد.

### Midjourney

Midjourney هم مشابه DALL-E کار می‌کند و تصاویر را از پرامپت متنی تولید می‌کند. Midjourney هم می‌تواند با پرامپت‌هایی مثل "گربه‌ای با کلاه" یا "سگی با موهاک" تصویر بسازد.

![تصویر تولید شده توسط Midjourney، کبوتر مکانیکی](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_اعتبار تصویر: ویکی‌پدیا، تصویر تولید شده توسط Midjourney_

## DALL-E و Midjourney چطور کار می‌کنند

ابتدا [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E یک مدل هوش مصنوعی مولد مبتنی بر معماری ترنسفورمر با _ترنسفورمر خودبازگشتی_ است.

_ترنسفورمر خودبازگشتی_ تعیین می‌کند که مدل چطور از توضیحات متنی تصویر بسازد؛ یعنی پیکسل به پیکسل تصویر را تولید می‌کند و هر بار از پیکسل‌های قبلی برای تولید پیکسل بعدی استفاده می‌کند. این فرایند از لایه‌های مختلف شبکه عصبی عبور می‌کند تا تصویر کامل شود.

با این روش، DALL-E می‌تواند ویژگی‌ها، اشیا، خصوصیات و موارد دیگر را در تصویر کنترل کند. البته نسخه‌های DALL-E 2 و 3 کنترل بیشتری روی تصویر تولید شده دارند.

## ساخت اولین برنامه تولید تصویر

برای ساخت یک برنامه تولید تصویر به کتابخانه‌های زیر نیاز دارید:

- **python-dotenv**، توصیه می‌شود برای نگهداری اطلاعات محرمانه در فایل _.env_ از این کتابخانه استفاده کنید تا اطلاعات از کد جدا باشد.
- **openai**، این کتابخانه برای ارتباط با API اوپن‌ای‌آی استفاده می‌شود.
- **pillow**، برای کار با تصاویر در پایتون.
- **requests**، برای ارسال درخواست‌های HTTP.

## ساخت و استقرار مدل Azure OpenAI

اگر قبلاً این کار را نکرده‌اید، طبق راهنمای [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal)
یک منبع و مدل Azure OpenAI بسازید. مدل DALL-E 3 را انتخاب کنید.

## ساخت اپلیکیشن

1. یک فایل _.env_ با محتوای زیر بسازید:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   این اطلاعات را می‌توانید در Azure OpenAI Foundry Portal در بخش "Deployments" برای منبع خود پیدا کنید.

1. کتابخانه‌های بالا را در فایلی به نام _requirements.txt_ به این صورت وارد کنید:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. سپس محیط مجازی بسازید و کتابخانه‌ها را نصب کنید:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   برای ویندوز، از دستورات زیر برای ساخت و فعال‌سازی محیط مجازی استفاده کنید:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. کد زیر را در فایلی به نام _app.py_ قرار دهید:

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

بیایید این کد را توضیح دهیم:

- ابتدا کتابخانه‌های مورد نیاز را وارد می‌کنیم، از جمله openai، dotenv، requests و pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- سپس متغیرهای محیطی را از فایل _.env_ بارگذاری می‌کنیم.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- بعد از آن، کلاینت سرویس Azure OpenAI را پیکربندی می‌کنیم

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- سپس تصویر را تولید می‌کنیم:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  کد بالا یک شیء JSON برمی‌گرداند که شامل URL تصویر تولید شده است. می‌توانیم این URL را برای دانلود و ذخیره تصویر استفاده کنیم.

- در نهایت، تصویر را باز می‌کنیم و با نمایشگر استاندارد تصاویر نمایش می‌دهیم:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### جزئیات بیشتر درباره تولید تصویر

بیایید کد تولید تصویر را با جزئیات بیشتری بررسی کنیم:

    ```python
      generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                            )
    ```

- **prompt**، همان پرامپت متنی است که برای تولید تصویر استفاده می‌شود. در این مثال، پرامپت ما "خرگوشی روی اسب، آب‌نبات به دست، در چمنی مه‌آلود که نرگس در آن رشد می‌کند" است.
- **size**، اندازه تصویر تولید شده است. در این مثال، تصویری با ابعاد ۱۰۲۴ در ۱۰۲۴ پیکسل تولید می‌کنیم.
- **n**، تعداد تصاویر تولید شده است. در این مثال، دو تصویر تولید می‌کنیم.
- **temperature**، پارامتری است که میزان تصادفی بودن خروجی مدل هوش مصنوعی مولد را کنترل می‌کند. مقدار آن بین ۰ تا ۱ است؛ ۰ یعنی خروجی قطعی و ۱ یعنی خروجی کاملاً تصادفی. مقدار پیش‌فرض ۰.۷ است.

کارهای بیشتری هم می‌توانید با تصاویر انجام دهید که در بخش بعدی به آن‌ها می‌پردازیم.

## قابلیت‌های بیشتر تولید تصویر

تا اینجا دیدید که چطور با چند خط کد پایتون می‌توان تصویر تولید کرد. اما کارهای بیشتری هم می‌توانید با تصاویر انجام دهید.

همچنین می‌توانید:

- **ویرایش انجام دهید**. با دادن یک تصویر موجود، یک ماسک و یک پرامپت، می‌توانید تصویر را تغییر دهید. مثلاً می‌توانید چیزی به بخشی از تصویر اضافه کنید. فرض کنید تصویر خرگوش را داریم، می‌توانیم یک کلاه به خرگوش اضافه کنیم. برای این کار باید تصویر، ماسک (برای مشخص کردن بخش مورد نظر) و یک پرامپت متنی برای توضیح تغییر را وارد کنید.
> توجه: این قابلیت در DALL-E 3 پشتیبانی نمی‌شود.

در اینجا یک مثال با GPT Image آورده شده است:

    ```python
    response = client.images.edit(
        model="gpt-image-1",
        image=open("sunlit_lounge.png", "rb"),
        mask=open("mask.png", "rb"),
        prompt="A sunlit indoor lounge area with a pool containing a flamingo"
    )
    image_url = response.data[0].url
    ```

  تصویر پایه فقط شامل سالن با استخر است اما تصویر نهایی یک فلامینگو هم دارد:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="./images/sunlit_lounge.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/mask.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="./images/sunlit_lounge_result.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **ساخت واریاسیون**. ایده این است که یک تصویر موجود را گرفته و از آن واریاسیون‌های مختلف بسازید. برای این کار، تصویر و یک پرامپت متنی را وارد می‌کنید و کد به این صورت خواهد بود:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > توجه: این قابلیت فقط در OpenAI پشتیبانی می‌شود.

## دما (Temperature)

دما پارامتری است که میزان تصادفی بودن خروجی مدل هوش مصنوعی مولد را کنترل می‌کند. مقدار آن بین ۰ تا ۱ است؛ ۰ یعنی خروجی قطعی و ۱ یعنی خروجی کاملاً تصادفی. مقدار پیش‌فرض ۰.۷ است.

بیایید با یک مثال ببینیم دما چطور کار می‌کند. این پرامپت را دو بار اجرا می‌کنیم:

> پرامپت: "خرگوشی روی اسب، آب‌نبات به دست، در چمنی مه‌آلود که نرگس در آن رشد می‌کند"

![خرگوش روی اسب با آب‌نبات، نسخه ۱](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.fa.png)

حالا همان پرامپت را دوباره اجرا می‌کنیم تا ببینیم تصویر یکسانی نمی‌گیریم:

![تصویر تولید شده خرگوش روی اسب](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.fa.png)

همانطور که می‌بینید، تصاویر شبیه هم هستند اما یکسان نیستند. حالا مقدار دما را به ۰.۱ تغییر می‌دهیم و نتیجه را می‌بینیم:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### تغییر دما

بیایید سعی کنیم خروجی را قطعی‌تر کنیم. از دو تصویر قبلی می‌بینیم که در اولی خرگوش و در دومی اسب وجود دارد، پس تصاویر تفاوت زیادی دارند.

بنابراین کد را تغییر می‌دهیم و دما را روی ۰ می‌گذاریم:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

حالا با اجرای این کد، این دو تصویر را می‌گیرید:

- ![دما ۰، نسخه ۱](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.fa.png)
- ![دما ۰، نسخه ۲](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.fa.png)

اینجا به وضوح می‌بینید که تصاویر خیلی شبیه هم هستند.

## چطور با متاپرومت‌ها برای برنامه خود مرز تعریف کنیم

با دموی ما، می‌توانیم برای مشتریان تصویر تولید کنیم. اما باید برای برنامه خود مرزهایی تعیین کنیم.

مثلاً نمی‌خواهیم تصاویر نامناسب یا غیرقابل نمایش برای کودکان تولید کنیم.

این کار را می‌توانیم با _متاپرومت‌ها_ انجام دهیم. متاپرومت‌ها پرامپت‌های متنی هستند که برای کنترل خروجی مدل هوش مصنوعی مولد استفاده می‌شوند. مثلاً می‌توانیم با متاپرومت‌ها خروجی را کنترل کنیم و مطمئن شویم تصاویر تولید شده مناسب محیط کار یا کودکان هستند.

### چطور کار می‌کند؟

حالا متاپرومت‌ها چطور کار می‌کنند؟

متاپرومت‌ها پرامپت‌های متنی هستند که برای کنترل خروجی مدل هوش مصنوعی مولد استفاده می‌شوند. این پرامپت‌ها قبل از پرامپت اصلی قرار می‌گیرند و در اپلیکیشن‌ها برای کنترل خروجی مدل به کار می‌روند. پرامپت ورودی و متاپرومت را در یک پرامپت متنی ترکیب می‌کنیم.

یک مثال از متاپرومت می‌تواند این باشد:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

حالا ببینیم چطور می‌توانیم در دموی خود از متاپرومت استفاده کنیم.

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

از پرامپت بالا می‌بینید که همه تصاویر تولید شده متاپرومت را در نظر می‌گیرند.

## تمرین - بیایید دانش‌آموزان را توانمند کنیم

در ابتدای این درس Edu4All را معرفی کردیم. حالا وقت آن است که به دانش‌آموزان اجازه دهیم برای ارزیابی‌های خود تصویر تولید کنند.

دانش‌آموزان قرار است برای ارزیابی‌های خود تصاویری از بناهای تاریخی بسازند. اینکه چه بنایی را انتخاب کنند به خودشان بستگی دارد. از دانش‌آموزان خواسته می‌شود با خلاقیت خود این بناها را در زمینه‌های مختلف قرار دهند.

## راه‌حل

در اینجا یک راه‌حل ممکن آورده شده است:

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

## عالی بود! یادگیری خود را ادامه دهید
پس از اتمام این درس، مجموعه [یادگیری هوش مصنوعی مولد](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) را بررسی کنید تا دانش خود را در زمینه هوش مصنوعی مولد ارتقا دهید!

به درس ۱۰ بروید تا ببینیم چگونه می‌توانیم [برنامه‌های هوش مصنوعی را با کدنویسی کم بسازیم](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. اگرچه ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطا یا نادرستی باشند. نسخه اصلی سند به زبان بومی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما هیچ مسئولیتی در قبال سوء تفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه نداریم.