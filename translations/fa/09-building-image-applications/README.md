# ساخت برنامه‌های تولید تصویر

[![ساخت برنامه‌های تولید تصویر](../../../translated_images/fa/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

مدل‌های زبان بزرگ فقط برای تولید متن نیستند. همچنین امکان تولید تصاویر از توصیفات متنی وجود دارد. داشتن تصاویر به عنوان یک مدالیتی می‌تواند در زمینه‌های متعددی از جمله مدتک، معماری، گردشگری، توسعه بازی و غیره بسیار مفید باشد. در این فصل، به دو مدل محبوب تولید تصویر، DALL-E و Midjourney، می‌پردازیم.

## مقدمه

در این درس، موارد زیر را بررسی خواهیم کرد:

- تولید تصویر و دلیل مفید بودن آن.
- DALL-E و Midjourney، چی هستند و چگونه کار می‌کنند.
- چگونه یک برنامه تولید تصویر بسازید.

## اهداف یادگیری

پس از اتمام این درس، قادر خواهید بود:

- ساخت یک برنامه تولید تصویر.
- تعیین محدودیت‌ها برای برنامه خود با متا پرامپت‌ها.
- کار با DALL-E و Midjourney.

## چرا برنامه تولید تصویر بسازیم؟

برنامه‌های تولید تصویر راه بسیار خوبی برای کاوش قابلیت‌های هوش مصنوعی مولد هستند. آن‌ها می‌توانند برای مثال در زمینه‌های زیر استفاده شوند:

- **ویرایش و ترکیب تصویر**. می‌توانید تصاویر را برای کاربردهای مختلفی مانند ویرایش تصویر و ترکیب تصاویر تولید کنید.

- **کاربرد در صنایع مختلف**. همچنین می‌توانند برای تولید تصاویر در صنایع مختلف مانند مدتک، گردشگری، توسعه بازی و غیره استفاده شوند.

## سناریو: Edu4All

در این درس، همچنان با استارتاپ خود، Edu4All، کار خواهیم کرد. دانش‌آموزان برای ارزیابی‌های خود تصاویر ایجاد می‌کنند، اینکه چه تصاویری باشند به خود دانش‌آموزان بستگی دارد، اما می‌توانند تصاویر داستان خودشان، یا خلق شخصیت جدید برای داستانشان یا کمک به تجسم ایده‌ها و مفاهیمشان باشند.

این‌ها نمونه‌ای از تصاویری است که دانش‌آموزان Edu4All می‌توانند بسازند، فرض کنید در کلاس روی بناهای تاریخی کار می‌کنند:

![استارتاپ Edu4All، کلاس بنای تاریخی، برج ایفل](../../../translated_images/fa/startup.94d6b79cc4bb3f5a.webp)

با استفاده از پرامپتی مانند

> "سگی کنار برج ایفل در نور صبح زود"

## DALL-E و Midjourney چیستند؟

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) و [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) دو تا از محبوب‌ترین مدل‌های تولید تصویر هستند که به شما امکان می‌دهند با استفاده از پرامپت‌ها تصویر تولید کنید.

### DALL-E

ابتدا با DALL-E شروع می‌کنیم، که یک مدل هوش مصنوعی مولد است که تصاویر را از توصیفات متنی تولید می‌کند.

> [DALL-E ترکیبی از دو مدل، CLIP و attention منتشر شده است](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**، مدلی است که جاسازی‌ها یا نمایه‌های عددی داده‌ها را از تصاویر و متن تولید می‌کند.

- **attention منتشر شده**، مدلی است که تصاویر را از جاسازی‌ها تولید می‌کند. DALL-E آموزش دیده بر روی مجموعه‌ای از تصاویر و متن است و می‌تواند تصاویر را از توصیفات متنی تولید کند. برای مثال، DALL-E می‌تواند تصویر یک گربه با کلاه یا سگی با موهای بلند از بالا تولید کند.

### Midjourney

Midjourney به شکل مشابهی با DALL-E کار می‌کند، تصاویر را از پرامپت‌های متنی تولید می‌کند. Midjourney همچنین می‌تواند تصاویر را با پرامپت‌هایی مانند «گربه با کلاه» یا «سگی با موهای بلند» تولید کند.

![تصویری تولید شده توسط Midjourney، کبوتر مکانیکی](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_اعتبار تصویر: ویکی‌پدیا، تصویر تولید شده توسط Midjourney_

## DALL-E و Midjourney چگونه کار می‌کنند؟

ابتدا، [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E یک مدل هوش مصنوعی مولد است بر پایه معماری ترنسفورمر با یک _ترنسفورمر خودبازگشتی_.

یک _ترنسفورمر خودبازگشتی_ مشخص می‌کند یک مدل چگونه تصاویر را از توصیفات متنی تولید می‌کند، او پیکسل به پیکسل تصویر را تولید می‌کند و سپس از پیکسل‌های تولید شده برای تولید پیکسل بعدی استفاده می‌کند، عبور از لایه‌های متعدد در یک شبکه عصبی تا تصویر کامل شود.

با این فرایند، DALL-E کنترل ویژگی‌ها، اشیاء، خصوصیات و سایر موارد در تصویر تولید شده را دارد. اما DALL-E 2 و 3 کنترل بیشتری روی تصویر تولید شده دارند.

## ساخت اولین برنامه تولید تصویر خودتان

پس چه چیزی لازم است تا یک برنامه تولید تصویر بسازید؟ کتابخانه‌های زیر را نیاز دارید:

- **python-dotenv**، به شدت توصیه می‌شود از این کتابخانه استفاده کنید تا اسرار خود را در فایل _.env_ و دور از کد حفظ کنید.
- **openai**، این کتابخانه برای تعامل با API شرکت OpenAI استفاده می‌شود.
- **pillow**، برای کار با تصاویر در پایتون.
- **requests**، برای کمک به انجام درخواست‌های HTTP.

## ایجاد و استقرار مدل Azure OpenAI

اگر هنوز انجام نشده، دستورالعمل‌های صفحه [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst) را دنبال کنید
برای ایجاد منبع و مدل Azure OpenAI. مدل **gpt-image-1** را انتخاب کنید (مدل فعلی تولید تصویر Azure OpenAI؛ DALL-E 3 دیگر برای استقرارهای جدید در دسترس نیست).

## ساخت برنامه

1. فایلی به نام _.env_ با محتوای زیر بسازید:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   این اطلاعات را در پرتال Azure OpenAI Foundry برای منبع خود در بخش "Deployments" پیدا کنید.

1. کتابخانه‌های فوق را در فایلی به نام _requirements.txt_ جمع‌آوری کنید:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. سپس محیط مجازی ساخته و کتابخانه‌ها را نصب کنید:

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

1. کد زیر را در فایلی به نام _app.py_ اضافه کنید:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # وارد کردن dotenv
    dotenv.load_dotenv()
    
    # پیکربندی مشتری سرویس Azure OpenAI
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # ایجاد تصویر با استفاده از API تولید تصویر
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # تنظیم پوشه برای ذخیره تصویر
        image_dir = os.path.join(os.curdir, 'images')

        # اگر پوشه وجود نداشت، آن را ایجاد کن
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # مقداردهی اولیه مسیر تصویر (توجه داشته باشید که فرمت فایل باید png باشد)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # دریافت تصویر تولید شده
        image_url = generation_response.data[0].url  # استخراج URL تصویر از پاسخ
        generated_image = requests.get(image_url).content  # دانلود تصویر
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # نمایش تصویر در نمایشگر تصویر پیش‌فرض
        image = Image.open(image_path)
        image.show()

    # دریافت استثناها
    except openai.BadRequestError as err:
        print(err)
   ```

اجازه دهید این کد را توضیح دهیم:

- ابتدا، کتابخانه‌های مورد نیاز، شامل کتابخانه OpenAI، dotenv، requests و Pillow را وارد می‌کنیم.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- سپس، متغیرهای محیطی را از فایل _.env_ بارگذاری می‌کنیم.

  ```python
  # وارد کردن dotenv
  dotenv.load_dotenv()
  ```

- بعد، کلاینت سرویس Azure OpenAI را پیکربندی می‌کنیم 

  ```python
  # دریافت نقطه پایان و کلید از متغیرهای محیطی
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- سپس، تصویر را تولید می‌کنیم:

  ```python
  # ایجاد یک تصویر با استفاده از API تولید تصویر
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  کد بالا با یک شیء JSON پاسخ می‌دهد که شامل URL تصویر تولید شده است. می‌توانیم از این URL برای دانلود و ذخیره تصویر استفاده کنیم.

- در نهایت، تصویر را باز کرده و با نمایشگر تصویر معمولی نمایش می‌دهیم:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### جزئیات بیشتر درباره تولید تصویر

اجازه دهید کد تولید تصویر را با جزئیات بیشتری بررسی کنیم:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**، متنی است که برای تولید تصویر استفاده می‌شود. در این مورد، از پرامپت "خرگوش روی اسب، در دست گرفتن آب‌نبات، روی چمن‌زاری مه‌آلود که نرگس دارد" استفاده شده است.
- **size**، اندازه تصویر تولید شده است. در این مورد، تصویری به اندازه 1024x1024 پیکسل تولید می‌کنیم.
- **n**، تعداد تصاویر تولید شده است. در اینجا دو تصویر تولید می‌شود.
- **temperature**، پارامتری است که تصادفی بودن خروجی مدل هوش مصنوعی مولد را کنترل می‌کند. دما عددی بین 0 و 1 است که 0 به معنی خروجی قطعی و 1 به معنی خروجی تصادفی است. مقدار پیش‌فرض 0.7 است.

موارد بیشتری وجود دارد که می‌توانید با تصاویر انجام دهید و در بخش بعدی به آن‌ها خواهیم پرداخت.

## قابلیت‌های اضافی تولید تصویر

تاکنون دیدید که چگونه می‌توان با چند خط کد در پایتون تصویری تولید کرد. اما موارد بیشتر وجود دارد.

همچنین می‌توانید:

- **ویرایش انجام دهید**. با دادن تصویری موجود، یک ماسک و یک پرامپت، می‌توانید تصویر را تغییر دهید. برای مثال، می‌توانید چیزی به بخشی از تصویر اضافه کنید. تصور کنید تصویر خرگوش، می‌توانید به خرگوش کلاه اضافه کنید. این کار با دادن تصویر، یک ماسک (شناسایی ناحیه تغییر) و یک پرامپت متنی انجام می‌شود تا بگوید چه کاری باید انجام شود.
> توجه: این ویژگی در DALL-E 3 پشتیبانی نمی‌شود.
 
اینجا مثالی با استفاده از GPT Image آورده شده است:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  تصویر پایه فقط شامل سالن با استخر است اما تصویر نهایی شامل یک فلامینگو خواهد بود:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/fa/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/fa/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/fa/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **ایجاد تغییرات**. ایده این است که تصویری موجود گرفته شود و بخواهید تغییراتی از آن ساخته شود. برای ایجاد تغییر، تصویری و پرامپتی ارائه می‌دهید و کدی مانند زیر می‌نویسید:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > توجه، این فقط در مدل DALL-E 2 شرکت OpenAI پشتیبانی می‌شود، نه در gpt-image-1

## دما (Temperature)

دما پارامتری است که تصادفی بودن خروجی مدل هوش مصنوعی مولد را کنترل می‌کند. دما عددی بین 0 و 1 است که 0 به معنی خروجی قطعی و 1 به معنی خروجی تصادفی است. مقدار پیش‌فرض 0.7 است.

اجازه دهید مثالی از نحوه کار دما ببینیم، با اجرای این پرامپت دو بار:

> پرامپت: "خرگوش روی اسب، در دست گرفتن آب‌نبات، روی چمن‌زاری مه‌آلود که نرگس دارد"

![خرگوش روی اسب در حال در دست گرفتن آب‌نبات، نسخه 1](../../../translated_images/fa/v1-generated-image.a295cfcffa3c13c2.webp)

حالا اجازه دهید همان پرامپت را دوباره اجرا کنیم تا ببینیم دو تصویر مشابه به دست نمی‌آید:

![تصویری تولید شده از خرگوش روی اسب](../../../translated_images/fa/v2-generated-image.33f55a3714efe61d.webp)

همانطور که می‌بینید، تصاویر مشابه هستند اما یکسان نیستند. بگذارید مقدار دما را به 0.1 تغییر دهیم و ببینیم چه اتفاقی می‌افتد:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # متن درخواست خود را اینجا وارد کنید
        size='1024x1024',
        n=2
    )
```

### تغییر دما

پس بیایید پاسخ را قطعی‌تر کنیم. از دو تصویری که تولید کردیم مشاهده می‌کنیم که در تصویر اول خرگوش وجود دارد و در تصویر دوم اسب، بنابراین تصاویر بسیار متفاوت هستند.

پس کد خود را تغییر داده و دما را روی 0 تنظیم می‌کنیم، مانند این:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # متن درخواست خود را اینجا وارد کنید
        size='1024x1024',
        n=2,
        temperature=0
    )
```

اکنون وقتی این کد را اجرا می‌کنید، این دو تصویر را دریافت می‌کنید:

- ![دمای 0، نسخه 1](../../../translated_images/fa/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![دمای 0، نسخه 2](../../../translated_images/fa/v2-temp-generated-image.871d0c920dbfb0f1.webp)

اینجا واضح‌تر می‌بینید که تصاویر بیشتر شبیه هم هستند.

## چگونه برای برنامه خود با متاپرامپت‌ها محدودیت تعیین کنیم

با نسخه نمایشی خود، حالا می‌توانیم برای مشتریانمان تصویر تولید کنیم. اما باید برای برنامه‌ محدودیت‌هایی ایجاد کنیم.

برای مثال، نمی‌خواهیم تصاویر غیراخلاقی یا نامناسب برای کودکان تولید کنیم.

این کار را می‌توانیم با _متاپرامپت‌ها_ انجام دهیم. متاپرامپت‌ها متن‌هایی هستند که برای کنترل خروجی مدل هوش مصنوعی مولد استفاده می‌شوند. برای مثال، می‌توانیم از متاپرامپت‌ها برای کنترل خروجی استفاده کنیم و اطمینان حاصل کنیم که تصاویر تولید شده اخلاقی و مناسب کودکان هستند.

### چگونه کار می‌کند؟

حالا، متاپرامپت‌ها چگونه کار می‌کنند؟

متاپرامپت‌ها متن‌هایی هستند که قبل از پرامپت متنی قرار می‌گیرند و برای کنترل خروجی مدل و استفاده در برنامه‌ها به کار می‌روند. این کار با قرار دادن ورودی پرامپت و متاپرامپت در یک پرامپت متنی صورت می‌گیرد.

یک مثال از متاپرامپت به صورت زیر است:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

حالا بیایید ببینیم چگونه می‌توانیم متاپرامپت‌ها را در نسخه آزمایشی خود استفاده کنیم.

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

# انجام شد اضافه کردن درخواست برای تولید تصویر
```

از پرامپت بالا می‌بینید که تمام تصاویر تولید شده متاپرامپت را در نظر گرفته‌اند.

## تکلیف - فعال کردن دانش‌آموزان

ما Edu4All را در ابتدای این درس معرفی کردیم. حالا زمان آن است که به دانش‌آموزان امکان تولید تصویر برای ارزیابی‌هایشان را بدهیم.


دانش‌آموزان برای ارزیابی‌های خود تصاویری شامل بناهای یادبود خلق خواهند کرد، اینکه دقیقاً چه بناهایی باشد به عهده دانش‌آموزان است. از دانش‌آموزان خواسته شده است که در این کار از خلاقیت خود استفاده کنند تا این بناها را در زمینه‌های مختلف قرار دهند.

## راه‌حل

در اینجا یک راه‌حل ممکن آورده شده است:

```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# وارد کردن dotenv
dotenv.load_dotenv()

# دریافت نقطه پایان و کلید از متغیرهای محیطی
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
    # ایجاد تصویر با استفاده از API تولید تصویر
    generation_response = client.images.generate(
        prompt=prompt,    # متن درخواست خود را اینجا وارد کنید
        size='1024x1024',
        n=1,
    )
    # تعیین مسیر دایرکتوری برای ذخیره تصویر
    image_dir = os.path.join(os.curdir, 'images')

    # اگر دایرکتوری وجود نداشت، آن را ایجاد کن
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # مقداردهی اولیه مسیر تصویر (توجه داشته باشید که نوع فایل باید png باشد)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # دریافت تصویر تولید شده
    image_url = generation_response.data[0].url  # استخراج آدرس تصویر از پاسخ
    generated_image = requests.get(image_url).content  # دانلود تصویر
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # نمایش تصویر در نمایشگر پیش‌فرض تصویر
    image = Image.open(image_path)
    image.show()

# گرفتن استثناها
except openai.BadRequestError as err:
    print(err)
```

## کار عالی! به یادگیری خود ادامه دهید

پس از اتمام این درس، مجموعه [یادگیری هوش مصنوعی مولد](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ما را بررسی کنید تا دانش خود در زمینه هوش مصنوعی مولد را ارتقاء دهید!

به درس ۱۰ بروید که در آن نحوه [ساخت برنامه‌های هوش مصنوعی با کم‌کد](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst) را بررسی خواهیم کرد

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->