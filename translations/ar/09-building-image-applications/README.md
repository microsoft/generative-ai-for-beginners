<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "238cde5c90363d70ecc939569378da51",
  "translation_date": "2025-10-17T12:58:58+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ar"
}
-->
# بناء تطبيقات توليد الصور

[![بناء تطبيقات توليد الصور](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.ar.png)](https://youtu.be/B5VP0_J7cs8?si=5P3L5o7F_uS_QcG9)

هناك أكثر من مجرد توليد النصوص في نماذج اللغة الكبيرة (LLMs). يمكن أيضًا توليد الصور من وصف النصوص. وجود الصور كوسيلة يمكن أن يكون مفيدًا للغاية في العديد من المجالات مثل التكنولوجيا الطبية، الهندسة المعمارية، السياحة، تطوير الألعاب والمزيد. في هذا الفصل، سنلقي نظرة على أكثر نماذج توليد الصور شهرة، DALL-E وMidjourney.

## المقدمة

في هذا الدرس، سنغطي:

- توليد الصور ولماذا هو مفيد.
- DALL-E وMidjourney، ما هما وكيف يعملان.
- كيفية بناء تطبيق لتوليد الصور.

## أهداف التعلم

بعد إكمال هذا الدرس، ستكون قادرًا على:

- بناء تطبيق لتوليد الصور.
- تحديد حدود لتطبيقك باستخدام الميتا برومبتس.
- العمل مع DALL-E وMidjourney.

## لماذا نبني تطبيق لتوليد الصور؟

تطبيقات توليد الصور هي طريقة رائعة لاستكشاف قدرات الذكاء الاصطناعي التوليدي. يمكن استخدامها، على سبيل المثال:

- **تحرير الصور وتوليفها**. يمكنك توليد صور لمجموعة متنوعة من الاستخدامات، مثل تحرير الصور وتوليف الصور.

- **تطبيقها على مجموعة متنوعة من الصناعات**. يمكن استخدامها أيضًا لتوليد صور لمجموعة متنوعة من الصناعات مثل التكنولوجيا الطبية، السياحة، تطوير الألعاب والمزيد.

## السيناريو: Edu4All

كجزء من هذا الدرس، سنواصل العمل مع شركتنا الناشئة، Edu4All. سيقوم الطلاب بإنشاء صور لتقييماتهم، نوع الصور يعود للطلاب، ولكن يمكن أن تكون رسومات لقصة خيالية خاصة بهم أو إنشاء شخصية جديدة لقصتهم أو مساعدتهم في تصور أفكارهم ومفاهيمهم.

إليك ما يمكن أن يولده طلاب Edu4All على سبيل المثال إذا كانوا يعملون في الفصل على المعالم:

![شركة Edu4All، فصل عن المعالم، برج إيفل](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.ar.png)

باستخدام برومبت مثل:

> "كلب بجانب برج إيفل في ضوء شمس الصباح الباكر"

## ما هو DALL-E وMidjourney؟

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) و[Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) هما من أكثر نماذج توليد الصور شهرة، حيث يسمحان لك باستخدام برومبتس لتوليد الصور.

### DALL-E

لنبدأ بـ DALL-E، وهو نموذج ذكاء اصطناعي توليدي يقوم بتوليد الصور من وصف النصوص.

> [DALL-E هو مزيج من نموذجين، CLIP والانتباه المنتشر](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**، هو نموذج يقوم بإنشاء تمثيلات رقمية للبيانات من الصور والنصوص.

- **الانتباه المنتشر**، هو نموذج يقوم بتوليد الصور من التمثيلات الرقمية. يتم تدريب DALL-E على مجموعة بيانات من الصور والنصوص ويمكن استخدامه لتوليد الصور من وصف النصوص. على سبيل المثال، يمكن استخدام DALL-E لتوليد صور لقطة ترتدي قبعة، أو كلب بتسريحة موهوك.

### Midjourney

يعمل Midjourney بطريقة مشابهة لـ DALL-E، حيث يقوم بتوليد الصور من برومبتس النصوص. يمكن أيضًا استخدام Midjourney لتوليد الصور باستخدام برومبتس مثل "قطة ترتدي قبعة"، أو "كلب بتسريحة موهوك".

![صورة مولدة بواسطة Midjourney، حمامة ميكانيكية](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_حقوق الصورة ويكيبيديا، الصورة مولدة بواسطة Midjourney_

## كيف يعمل DALL-E وMidjourney

أولاً، [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E هو نموذج ذكاء اصطناعي توليدي يعتمد على بنية المحول مع _محول ذاتي التراجع_.

المحول الذاتي التراجع يحدد كيفية توليد النموذج للصور من وصف النصوص، حيث يولد بكسل واحد في كل مرة، ثم يستخدم البكسلات المولدة لتوليد البكسل التالي. يمر عبر طبقات متعددة في الشبكة العصبية، حتى تكتمل الصورة.

من خلال هذه العملية، يتحكم DALL-E في السمات، الأشياء، الخصائص، والمزيد في الصورة التي يولدها. ومع ذلك، فإن DALL-E 2 و3 لديهما تحكم أكبر في الصورة المولدة.

## بناء أول تطبيق لتوليد الصور

إذن ما الذي يتطلبه بناء تطبيق لتوليد الصور؟ تحتاج إلى المكتبات التالية:

- **python-dotenv**، يُوصى بشدة باستخدام هذه المكتبة للحفاظ على أسرارك في ملف _.env_ بعيدًا عن الكود.
- **openai**، هذه المكتبة هي ما ستستخدمه للتفاعل مع واجهة برمجة التطبيقات OpenAI.
- **pillow**، للعمل مع الصور في Python.
- **requests**، لمساعدتك في إجراء طلبات HTTP.

## إنشاء ونشر نموذج Azure OpenAI

إذا لم يتم ذلك بالفعل، اتبع التعليمات على صفحة [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) لإنشاء مورد ونموذج Azure OpenAI. اختر DALL-E 3 كنموذج.

## إنشاء التطبيق

1. قم بإنشاء ملف _.env_ بالمحتوى التالي:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   ابحث عن هذه المعلومات في بوابة Azure OpenAI Foundry لموردك في قسم "النشر".

1. اجمع المكتبات المذكورة أعلاه في ملف يسمى _requirements.txt_ كالتالي:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. بعد ذلك، قم بإنشاء بيئة افتراضية وقم بتثبيت المكتبات:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   بالنسبة لنظام Windows، استخدم الأوامر التالية لإنشاء وتفعيل بيئتك الافتراضية:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. أضف الكود التالي في ملف يسمى _app.py_:

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

لنشرح هذا الكود:

- أولاً، نقوم باستيراد المكتبات التي نحتاجها، بما في ذلك مكتبة OpenAI، مكتبة dotenv، مكتبة requests، ومكتبة Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- بعد ذلك، نقوم بتحميل المتغيرات البيئية من ملف _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- بعد ذلك، نقوم بتكوين عميل خدمة Azure OpenAI.

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- بعد ذلك، نقوم بتوليد الصورة:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  الكود أعلاه يستجيب بجسم JSON يحتوي على رابط URL للصورة المولدة. يمكننا استخدام الرابط لتحميل الصورة وحفظها في ملف.

- أخيرًا، نقوم بفتح الصورة واستخدام عارض الصور القياسي لعرضها:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### المزيد من التفاصيل حول توليد الصورة

لنلقي نظرة على الكود الذي يولد الصورة بمزيد من التفصيل:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**، هو برومبت النص المستخدم لتوليد الصورة. في هذه الحالة، نستخدم البرومبت "أرنب على حصان، يحمل مصاصة، في مرج ضبابي حيث تنمو أزهار النرجس".
- **size**، هو حجم الصورة التي يتم توليدها. في هذه الحالة، نقوم بتوليد صورة بحجم 1024x1024 بكسل.
- **n**، هو عدد الصور التي يتم توليدها. في هذه الحالة، نقوم بتوليد صورتين.
- **temperature**، هو معلمة تتحكم في عشوائية مخرجات نموذج الذكاء الاصطناعي التوليدي. درجة الحرارة هي قيمة بين 0 و1 حيث 0 تعني أن المخرجات حتمية و1 تعني أن المخرجات عشوائية. القيمة الافتراضية هي 0.7.

هناك المزيد مما يمكنك القيام به مع الصور وسنغطي ذلك في القسم التالي.

## القدرات الإضافية لتوليد الصور

لقد رأيت حتى الآن كيف تمكنا من توليد صورة باستخدام بضعة أسطر في Python. ومع ذلك، هناك المزيد مما يمكنك القيام به مع الصور.

يمكنك أيضًا القيام بما يلي:

- **إجراء تعديلات**. من خلال تقديم صورة موجودة وقناع وبرومبت، يمكنك تعديل الصورة. على سبيل المثال، يمكنك إضافة شيء إلى جزء من الصورة. تخيل صورة الأرنب، يمكنك إضافة قبعة للأرنب. كيف يمكنك القيام بذلك هو تقديم الصورة، قناع (تحديد الجزء من المنطقة للتغيير) وبرومبت نصي لتحديد ما يجب القيام به.
> ملاحظة: هذا غير مدعوم في DALL-E 3.

إليك مثال باستخدام GPT Image:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  الصورة الأساسية ستحتوي فقط على الصالة مع المسبح ولكن الصورة النهائية ستحتوي على فلامنغو:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.ar.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.ar.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.ar.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **إنشاء تنويعات**. الفكرة هي أنك تأخذ صورة موجودة وتطلب إنشاء تنويعات لها. لإنشاء تنويع، تقدم صورة وبرومبت نصي وكود مثل هذا:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > ملاحظة، هذا مدعوم فقط على OpenAI.

## درجة الحرارة

درجة الحرارة هي معلمة تتحكم في عشوائية مخرجات نموذج الذكاء الاصطناعي التوليدي. درجة الحرارة هي قيمة بين 0 و1 حيث 0 تعني أن المخرجات حتمية و1 تعني أن المخرجات عشوائية. القيمة الافتراضية هي 0.7.

لنلقي نظرة على مثال كيف تعمل درجة الحرارة، من خلال تشغيل هذا البرومبت مرتين:

> برومبت: "أرنب على حصان، يحمل مصاصة، في مرج ضبابي حيث تنمو أزهار النرجس"

![أرنب على حصان يحمل مصاصة، النسخة الأولى](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.ar.png)

الآن لنقم بتشغيل نفس البرومبت فقط لنرى أننا لن نحصل على نفس الصورة مرتين:

![صورة مولدة لأرنب على حصان](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.ar.png)

كما ترى، الصور متشابهة، لكنها ليست نفسها. لنحاول تغيير قيمة درجة الحرارة إلى 0.1 ونرى ما يحدث:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### تغيير درجة الحرارة

لذلك دعونا نحاول جعل الاستجابة أكثر حتمية. يمكننا أن نلاحظ من الصورتين اللتين قمنا بتوليدهما أنه في الصورة الأولى، هناك أرنب وفي الصورة الثانية، هناك حصان، لذا الصور تختلف بشكل كبير.

لذلك دعونا نغير الكود الخاص بنا ونضبط درجة الحرارة إلى 0، مثل هذا:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

الآن عندما تقوم بتشغيل هذا الكود، تحصل على هاتين الصورتين:

- ![درجة الحرارة 0، النسخة الأولى](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.ar.png)
- ![درجة الحرارة 0، النسخة الثانية](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.ar.png)

هنا يمكنك أن ترى بوضوح كيف تتشابه الصور أكثر.

## كيفية تحديد حدود لتطبيقك باستخدام الميتا برومبتس

مع العرض التوضيحي الخاص بنا، يمكننا بالفعل توليد صور لعملائنا. ومع ذلك، نحتاج إلى إنشاء بعض الحدود لتطبيقنا.

على سبيل المثال، لا نريد توليد صور غير آمنة للعمل، أو غير مناسبة للأطفال.

يمكننا القيام بذلك باستخدام _الميتا برومبتس_. الميتا برومبتس هي برومبتس نصية تُستخدم للتحكم في مخرجات نموذج الذكاء الاصطناعي التوليدي. على سبيل المثال، يمكننا استخدام الميتا برومبتس للتحكم في المخرجات، وضمان أن الصور المولدة آمنة للعمل، أو مناسبة للأطفال.

### كيف تعمل؟

الآن، كيف تعمل الميتا برومبتس؟

الميتا برومبتس هي برومبتس نصية تُستخدم للتحكم في مخرجات نموذج الذكاء الاصطناعي التوليدي، يتم وضعها قبل البرومبت النصي، وتُستخدم للتحكم في مخرجات النموذج وتضمينها في التطبيقات للتحكم في مخرجات النموذج. تضمين مدخلات البرومبت ومدخلات الميتا برومبت في برومبت نصي واحد.

مثال على ميتا برومبت سيكون التالي:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

الآن، دعونا نرى كيف يمكننا استخدام الميتا برومبتس في العرض التوضيحي الخاص بنا.

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

من البرومبت أعلاه، يمكنك أن ترى كيف تأخذ جميع الصور التي يتم إنشاؤها في الاعتبار الميتا برومبت.

## المهمة - دعونا نمكن الطلاب

قدمنا Edu4All في بداية هذا الدرس. الآن حان الوقت لتمكين الطلاب من توليد صور لتقييماتهم.

سيقوم الطلاب بإنشاء صور لتقييماتهم تحتوي على معالم، نوع المعالم يعود للطلاب. يُطلب من الطلاب استخدام إبداعهم في هذه المهمة لوضع هذه المعالم في سياقات مختلفة.

## الحل

إليك أحد الحلول الممكنة:
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

## عمل رائع! واصل التعلم

بعد إكمال هذا الدرس، تحقق من [مجموعة تعلم الذكاء الاصطناعي التوليدي](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) لمواصلة تطوير معرفتك بالذكاء الاصطناعي التوليدي!

انتقل إلى الدرس 10 حيث سنستعرض كيفية [بناء تطبيقات الذكاء الاصطناعي باستخدام البرمجة منخفضة الكود](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.