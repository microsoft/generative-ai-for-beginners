# بناء تطبيقات توليد الصور

[![بناء تطبيقات توليد الصور](../../../translated_images/ar/09-lesson-banner.906e408c741f4411.webp)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

هناك المزيد في نماذج اللغات الكبيرة بخلاف توليد النصوص. من الممكن أيضًا توليد الصور من أوصاف نصية. وجود الصور كوسيط يمكن أن يكون مفيدًا جدًا في عدد من المجالات مثل التكنولوجيا الطبية، والهندسة المعمارية، والسياحة، وتطوير الألعاب والمزيد. في هذا الفصل، سوف نستعرض نموذجين من أكثر نماذج توليد الصور شهرة، DALL-E وMidjourney.

## مقدمة

في هذا الدرس، سوف نغطي:

- توليد الصور ولماذا هو مفيد.
- DALL-E وMidjourney، ما هما، وكيف يعملان.
- كيف تبني تطبيقًا لتوليد الصور.

## أهداف التعلم

بعد إتمام هذا الدرس، ستتمكن من:

- بناء تطبيق لتوليد الصور.
- تحديد حدود لتطبيقك باستخدام الموجهات الفوقية.
- العمل مع DALL-E وMidjourney.

## لماذا تبني تطبيق توليد الصور؟

تطبيقات توليد الصور هي طريقة رائعة لاستكشاف قدرات الذكاء الاصطناعي التوليدي. يمكن استخدامها، على سبيل المثال:

- **تعديل وتوليف الصور**. يمكنك توليد صور لمجموعة متنوعة من الاستخدامات، مثل تعديل الصور وتوليفها.

- **تُطبّق في صناعات متنوعة**. يمكن أيضًا استخدامها لتوليد صور لعدة صناعات مثل التكنولوجيا الطبية، السياحة، تطوير الألعاب والمزيد.

## سيناريو: Edu4All

كجزء من هذا الدرس، سنواصل العمل مع شركتنا الناشئة Edu4All. سيقوم الطلاب بإنشاء صور لتقييماتهم، الصور بالضبط تعتمد على الطلاب، لكن يمكن أن تكون رسومات لحكايتهم الخاصة أو إنشاء شخصية جديدة لقصة ما أو مساعدتهم في تصور أفكارهم ومفاهيمهم.

إليك ما يمكن لطلاب Edu4All توليده، على سبيل المثال إذا كانوا يعملون في الصف على المعالم:

![شركة Edu4All الناشئة، درس على المعالم، برج إيفل](../../../translated_images/ar/startup.94d6b79cc4bb3f5a.webp)

باستخدام موجه مثل

> "كلب بجانب برج إيفل في ضوء شمس الصباح الباكر"

## ما هو DALL-E وMidjourney؟

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) و[Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) هما من أشهر نماذج توليد الصور، يسمحان باستخدام الموجهات لتوليد الصور.

### DALL-E

لنبدأ بـ DALL-E، وهو نموذج للذكاء الاصطناعي التوليدي يولد الصور من أوصاف نصية.

> [DALL-E هو مزيج من نموذجين، CLIP والانتباه المشتت](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**، هو نموذج يولد تمثيلات رقمية (تضمينات) للبيانات من الصور والنصوص.

- **الانتباه المشتت**، هو نموذج يولد الصور من التضمينات. يتم تدريب DALL-E على مجموعة بيانات من الصور والنصوص ويمكن استخدامه لتوليد الصور من الأوصاف النصية. على سبيل المثال، يمكن استخدام DALL-E لتوليد صور لقطة ترتدي قبعة، أو كلب ذي موهوك.

### Midjourney

يعمل Midjourney بطريقة مشابهة لـ DALL-E، فهو يولد الصور من الموجهات النصية. يمكن استخدام Midjourney أيضًا لتوليد الصور باستخدام موجهات مثل "قطة في قبعة"، أو "كلب ذو موهوك".

![صورة مولدة بواسطة Midjourney، حمامة ميكانيكية](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_حقوق الصورة ويكيبيديا، صورة مولدة بواسطة Midjourney_

## كيف يعمل DALL-E وMidjourney

أولاً، [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E هو نموذج ذكاء اصطناعي توليدي يعتمد على هندسة المحول مع _محول ذاتي التكرار_.

يحدد _المحول الذاتي التكرار_ كيفية توليد النموذج للصور من الأوصاف النصية، حيث يولد بكسلًا واحدًا في كل مرة، ثم يستخدم البكسلات المولدة لتوليد البكسل التالي. ويمر ذلك عبر طبقات متعددة في شبكة عصبية حتى تكتمل الصورة.

بهذه العملية، يتحكم DALL-E في السمات، والأشياء، والخصائص، وأكثر في الصورة التي يولدها. ومع ذلك، فإن DALL-E 2 و3 يتمتعان بتحكم أكبر في الصورة المولدة.

## بناء أول تطبيق لتوليد الصور خاصتك

فما الذي يتطلبه بناء تطبيق لتوليد الصور؟ تحتاج إلى المكتبات التالية:

- **python-dotenv**، يُنصح بشدة باستخدام هذه المكتبة للاحتفاظ بسرية المفاتيح في ملف _.env_ بعيدًا عن الكود.
- **openai**، هذه المكتبة ما ستستخدمه للتفاعل مع واجهة برمجة التطبيقات OpenAI.
- **pillow**، للعمل مع الصور في Python.
- **requests**، لمساعدتك في إجراء طلبات HTTP.

## إنشاء ونشر نموذج Azure OpenAI

إذا لم يتم ذلك بعد، اتبع التعليمات على صفحة [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal&WT.mc_id=academic-105485-koreyst)
لإنشاء مورد و نموذج Azure OpenAI. اختر **gpt-image-1** كنموذج (نموذج الصور الحالي في Azure OpenAI؛ DALL-E 3 قديم ولم يعد متاحًا للنشر الجديد).

## إنشاء التطبيق

1. أنشئ ملف _.env_ بالمحتوى التالي:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="gpt-image-1"
   ```

   يمكن العثور على هذه المعلومات في بوابة Azure OpenAI Foundry لموردك في قسم "النشرات".

1. اجمع المكتبات المذكورة أعلاه في ملف يُسمى _requirements.txt_ هكذا:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. بعد ذلك، أنشئ بيئة افتراضية وقم بتثبيت المكتبات:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   بالنسبة لنظام ويندوز، استخدم الأوامر التالية لإنشاء وتفعيل البيئة الافتراضية:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. أضف الكود التالي في ملف يُسمى _app.py_:

    ```python
    import openai
    import os
    import requests
    from PIL import Image
    import dotenv
    from openai import OpenAI, AzureOpenAI
    
    # استيراد dotenv
    dotenv.load_dotenv()
    
    # تكوين عميل خدمة Azure OpenAI
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
    try:
        # إنشاء صورة باستخدام واجهة برمجة تطبيقات توليد الصور
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # تعيين الدليل للصورة المخزنة
        image_dir = os.path.join(os.curdir, 'images')

        # إذا لم يكن الدليل موجودًا، قم بإنشائه
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # تهيئة مسار الصورة (ملاحظة: يجب أن يكون نوع الملف png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # استرجاع الصورة المُولّدة
        image_url = generation_response.data[0].url  # استخراج عنوان URL للصورة من الاستجابة
        generated_image = requests.get(image_url).content  # تحميل الصورة
        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        # عرض الصورة في عارض الصور الافتراضي
        image = Image.open(image_path)
        image.show()

    # التقاط الاستثناءات
    except openai.BadRequestError as err:
        print(err)
   ```

لنشرح هذا الكود:

- أولًا، نستورد المكتبات التي نحتاجها، بما في ذلك مكتبة OpenAI، مكتبة dotenv، مكتبة requests، ومكتبة Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- بعد ذلك، نقوم بتحميل المتغيرات البيئية من ملف _.env_.

  ```python
  # استيراد dotenv
  dotenv.load_dotenv()
  ```

- بعد ذلك، نُهيئ عميل خدمة Azure OpenAI

  ```python
  # احصل على نقطة النهاية والمفتاح من متغيرات البيئة
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-10-21"
      )
  ```

- بعد ذلك، نقوم بتوليد الصورة:

  ```python
  # إنشاء صورة باستخدام واجهة برمجة تطبيقات توليد الصور
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  الكود أعلاه يرد بكائن JSON يحتوي على رابط الصورة المولدة. يمكننا استخدام الرابط لتحميل الصورة وحفظها في ملف.

- أخيرًا، نفتح الصورة ونستخدم عارض الصور الافتراضي لعرضها:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### المزيد من التفاصيل حول توليد الصورة

لنلقي نظرة مفصلة على الكود الذي يولد الصورة:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**، هو الموجه النصي المستخدم لتوليد الصورة. في هذه الحالة، نستخدم الموجه "أرنب على حصان، ممسك بحلوى على عصا، في مرج ضبابي ينمو فيه زنبق الوادي".
- **size**، هو حجم الصورة التي يتم توليدها. في هذه الحالة، نولد صورة بحجم 1024×1024 بكسل.
- **n**، هو عدد الصور التي يتم توليدها. في هذه الحالة، نولد صورتين.
- **temperature**، هو معامل يتحكم في عشوائية مخرجات نموذج الذكاء الاصطناعي التوليدي. حيث تكون القيمة بين 0 و1؛ حيث 0 تعني أن المخرجات حتمية، و1 تعني أن المخرجات عشوائية. القيمة الافتراضية هي 0.7.

هناك المزيد من الأمور التي يمكنك فعلها مع الصور سنغطيها في القسم التالي.

## قدرات إضافية لتوليد الصور

رأيت حتى الآن كيف استطعنا توليد صورة باستخدام بضعة أسطر في Python. ومع ذلك، هناك المزيد الذي يمكنك القيام به مع الصور.

يمكنك أيضًا القيام بما يلي:

- **إجراء تعديلات**. من خلال تقديم صورة موجودة وقناع وموجه نصي، يمكنك تعديل الصورة. على سبيل المثال، يمكنك إضافة شيء لجزء من الصورة. تخيل صورتنا للأرنب، يمكنك إضافة قبعة للأرنب. ذلك يتم بتوفير الصورة، قناعًا (يحدد الجزء الذي سيحدث فيه التغيير) وموجهًا نصيًا يحدد ما يجب عمله. 
> ملاحظة: هذا غير مدعوم في DALL-E 3.
 
هنا مثال باستخدام GPT Image:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  الصورة الأساسية ستحتوي فقط على الصالة مع المسبح لكن الصورة النهائية ستحتوي على فلامنغو:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/ar/sunlit_lounge.a75a0cb61749db0e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/ar/mask.1b2976ccec9e011e.webp" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/ar/sunlit_lounge_result.76ae02957c0bbeb8.webp" style="width: 30%; max-width: 200px; height: auto;">
</div>


- **إنشاء تغييرات**. الفكرة هي أن تأخذ صورة موجودة وتطلب إنشاء تغييرات لها. لإنشاء تغيير، تقدم صورة وموجهًا نصيًا وكودًا مثل:

  ```python
  response = client.images.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response.data[0].url
  ```

  > ملاحظة، هذا مدعوم فقط على نموذج DALL-E 2 من OpenAI، وليس gpt-image-1

## درجة الحرارة

درجة الحرارة هي معامل يتحكم في عشوائية مخرجات نموذج الذكاء الاصطناعي التوليدي. القيمة بين 0 و1، حيث 0 تعني أن المخرجات حتمية و1 تعني أن المخرجات عشوائية. القيمة الافتراضية هي 0.7.

لنلقي نظرة على مثال لكيفية عمل درجة الحرارة، من خلال تشغيل هذا الموجه مرتين:

> موجه : "أرنب على حصان، ممسك بحلوى على عصا، في مرج ضبابي ينمو فيه زنبق الوادي"

![أرنب على حصان ممسك بحلوى على عصا، النسخة 1](../../../translated_images/ar/v1-generated-image.a295cfcffa3c13c2.webp)

الآن لنشغل نفس الموجه مرة أخرى لنرى أننا لن نحصل على الصورة نفسها مرتين:

![صورة مولدة لأرنب على حصان](../../../translated_images/ar/v2-generated-image.33f55a3714efe61d.webp)

كما ترى، الصور متشابهة لكن ليست نفسها. دعنا نجرب تغيير القيمة إلى 0.1 ونرى ماذا يحدث:

```python
 generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # أدخل نص الموجه الخاص بك هنا
        size='1024x1024',
        n=2
    )
```

### تغيير درجة الحرارة

لنحاول جعل الرد أكثر حتمية. يمكننا ملاحظة من الصورتين اللتين ولدناهما أن في الأولى يوجد أرنب وفي الثانية حصان، فالصورتان تختلفان كثيرًا.

لذلك، دعنا نغير كودنا ونجعل درجة الحرارة 0، هكذا:

```python
generation_response = client.images.generate(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # أدخل نص التعليمات هنا
        size='1024x1024',
        n=2,
        temperature=0
    )
```

الآن عند تشغيل هذا الكود، ستحصل على هاتين الصورتين:

- ![درجة الحرارة 0، النسخة 1](../../../translated_images/ar/v1-temp-generated-image.a4346e1d2360a056.webp)
- ![درجة الحرارة 0، النسخة 2](../../../translated_images/ar/v2-temp-generated-image.871d0c920dbfb0f1.webp)

هنا يمكنك أن ترى بوضوح كيف أن الصور أصبحت أكثر شبهًا ببعضها.

## كيفية تحديد حدود لتطبيقك باستخدام موجهات فوقية

مع العرض التوضيحي لدينا، يمكننا بالفعل توليد صور لعملائنا. لكن علينا إنشاء بعض الحدود لتطبيقنا.

على سبيل المثال، لا نريد توليد صور غير مناسبة للعمل، أو غير مناسبة للأطفال.

يمكننا القيام بذلك باستخدام _الموجهات الفوقية_. الموجهات الفوقية هي موجهات نصية تُستخدم للتحكم في مخرجات نموذج الذكاء الاصطناعي التوليدي. على سبيل المثال، يمكننا استخدامها لضمان أن الصور المولدة آمنة للعمل أو مناسبة للأطفال.

### كيف تعمل؟

الآن، كيف تعمل الموجهات الفوقية؟

الموجهات الفوقية هي موجهات نصية تُستخدم للتحكم في مخرجات نموذج الذكاء الاصطناعي التوليدي، توضع قبل الموجه النصي، وتستخدم للتحكم بالمخرجات وتُدمج في التطبيقات للتحكم بالمخرجات. حيث تُغلف مدخلات الموجه والمدخلات الفوقية في موجه نصي واحد.

مثال على موجه فوقي سيكون كالتالي:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

الآن، لنر كيف يمكننا استخدام الموجهات الفوقية في العرض التوضيحي.

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

# TODO إضافة طلب لإنشاء صورة
```

من الموجه أعلاه، يمكنك أن ترى كيف أن جميع الصور التي تم إنشاؤها تأخذ بعين الاعتبار الموجه الفوقي.

## المهمة - لنمكن الطلاب

قدمنا Edu4All في بداية هذا الدرس. الآن حان الوقت لتمكين الطلاب من توليد صور لتقييماتهم.


سيقوم الطلاب بإنشاء صور لتقييماتهم تحتوي على معالم أثرية، والمعالم التي سيتم اختيارها تعود للطلاب. يُطلب من الطلاب استخدام إبداعهم في هذه المهمة لوضع هذه المعالم في سياقات مختلفة.

## الحل

إليكم أحد الحلول الممكنة:

```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# استيراد dotenv
dotenv.load_dotenv()

# الحصول على نقطة النهاية والمفتاح من متغيرات البيئة
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
    # إنشاء صورة باستخدام واجهة برمجة تطبيقات توليد الصور
    generation_response = client.images.generate(
        prompt=prompt,    # أدخل نص المطالبة هنا
        size='1024x1024',
        n=1,
    )
    # تعيين الدليل للصورة المخزنة
    image_dir = os.path.join(os.curdir, 'images')

    # إذا لم يكن الدليل موجودًا، قم بإنشائه
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # تهيئة مسار الصورة (ملاحظة: يجب أن يكون نوع الملف png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # استرداد الصورة المولدة
    image_url = generation_response.data[0].url  # استخراج رابط الصورة من الاستجابة
    generated_image = requests.get(image_url).content  # تنزيل الصورة
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # عرض الصورة في عارض الصور الافتراضي
    image = Image.open(image_path)
    image.show()

# التقاط الاستثناءات
except openai.BadRequestError as err:
    print(err)
```

## عمل رائع! استمر في التعلم

بعد إتمام هذا الدرس، اطلع على [مجموعة تعلم الذكاء الاصطناعي التوليدي](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) لمواصلة تعزيز معرفتك بالذكاء الاصطناعي التوليدي!

توجه إلى الدرس 10 حيث سنستعرض كيفية [بناء تطبيقات الذكاء الاصطناعي باستخدام الأكواد المنخفضة](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->