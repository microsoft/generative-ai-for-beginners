<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T18:58:01+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ar"
}
-->
# بناء تطبيقات توليد الصور

هناك أكثر من مجرد توليد النصوص في LLMs. من الممكن أيضًا توليد الصور من أوصاف النصوص. يمكن أن يكون وجود الصور كوسيلة مفيدًا للغاية في عدد من المجالات مثل التكنولوجيا الطبية، والهندسة المعمارية، والسياحة، وتطوير الألعاب والمزيد. في هذا الفصل، سنلقي نظرة على النموذجين الأكثر شهرة في توليد الصور، DALL-E وMidjourney.

## مقدمة

في هذا الدرس، سنغطي:

- توليد الصور ولماذا هو مفيد.
- DALL-E وMidjourney، ما هما وكيف يعملا.
- كيف يمكنك بناء تطبيق لتوليد الصور.

## أهداف التعلم

بعد إكمال هذا الدرس، ستتمكن من:

- بناء تطبيق لتوليد الصور.
- تحديد حدود لتطبيقك باستخدام المطالبات الفوقية.
- العمل مع DALL-E وMidjourney.

## لماذا بناء تطبيق لتوليد الصور؟

تطبيقات توليد الصور هي وسيلة رائعة لاستكشاف قدرات الذكاء الاصطناعي التوليدي. يمكن استخدامها، على سبيل المثال:

- **تحرير الصور وتوليفها**. يمكنك توليد صور لمجموعة متنوعة من الاستخدامات، مثل تحرير الصور وتوليف الصور.

- **تطبيقها على مجموعة متنوعة من الصناعات**. يمكن استخدامها أيضًا لتوليد صور لمجموعة متنوعة من الصناعات مثل التكنولوجيا الطبية، والسياحة، وتطوير الألعاب والمزيد.

## سيناريو: Edu4All

كجزء من هذا الدرس، سنواصل العمل مع شركتنا الناشئة، Edu4All، في هذا الدرس. سيقوم الطلاب بإنشاء صور لتقييماتهم، ويعود لهم تحديد ما هي الصور، ولكن يمكن أن تكون رسومات لقصة خيالية خاصة بهم أو إنشاء شخصية جديدة لقصة لهم أو مساعدتهم في تصور أفكارهم ومفاهيمهم.

إليكم ما يمكن أن يولده طلاب Edu4All على سبيل المثال إذا كانوا يعملون في الفصل على المعالم:

![شركة Edu4All، فصل عن المعالم، برج إيفل](../../../translated_images/startup.ec211d74fef9f4175010c3334942b715514230415744b9dd0a69a19f4ad68786.ar.png)

باستخدام مطالبة مثل

> "كلب بجوار برج إيفل في ضوء الصباح الباكر"

## ما هو DALL-E وMidjourney؟

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) و[Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) هما من أكثر نماذج توليد الصور شهرة، حيث يتيحان لك استخدام المطالبات لتوليد الصور.

### DALL-E

لنبدأ مع DALL-E، وهو نموذج ذكاء اصطناعي توليدي يقوم بتوليد الصور من أوصاف النصوص.

> [DALL-E هو مزيج من نموذجين، CLIP والانتباه المنتشر](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**، هو نموذج يقوم بتوليد التضمينات، وهي تمثيلات رقمية للبيانات، من الصور والنصوص.

- **الانتباه المنتشر**، هو نموذج يقوم بتوليد الصور من التضمينات. يتم تدريب DALL-E على مجموعة بيانات من الصور والنصوص ويمكن استخدامه لتوليد الصور من أوصاف النصوص. على سبيل المثال، يمكن استخدام DALL-E لتوليد صور لقطة في قبعة، أو كلب بتسريحة موهوك.

### Midjourney

يعمل Midjourney بطريقة مشابهة لـ DALL-E، حيث يقوم بتوليد الصور من مطالبات النصوص. يمكن أيضًا استخدام Midjourney لتوليد الصور باستخدام مطالبات مثل "قطة في قبعة"، أو "كلب بتسريحة موهوك".

![صورة مولدة بواسطة Midjourney، حمامة ميكانيكية](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_حقوق الصورة ويكيبيديا، صورة مولدة بواسطة Midjourney_

## كيف يعمل DALL-E وMidjourney

أولاً، [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E هو نموذج ذكاء اصطناعي توليدي يعتمد على بنية المحول مع _المحول التلقائي الانحدار_.

المحول التلقائي الانحدار يحدد كيف يقوم النموذج بتوليد الصور من أوصاف النصوص، حيث يقوم بتوليد بكسل واحد في كل مرة، ثم يستخدم البكسلات المولدة لتوليد البكسل التالي. يمر عبر طبقات متعددة في شبكة عصبية، حتى تكتمل الصورة.

مع هذه العملية، يتحكم DALL-E في السمات، والكائنات، والخصائص، والمزيد في الصورة التي يولدها. ومع ذلك، فإن DALL-E 2 و3 لديهما مزيد من التحكم في الصورة المولدة.

## بناء تطبيقك الأول لتوليد الصور

إذًا، ماذا يتطلب بناء تطبيق لتوليد الصور؟ تحتاج إلى المكتبات التالية:

- **python-dotenv**، يوصى بشدة باستخدام هذه المكتبة للحفاظ على الأسرار في ملف _.env_ بعيدًا عن الكود.
- **openai**، هذه المكتبة هي ما ستستخدمه للتفاعل مع واجهة برمجة التطبيقات OpenAI.
- **pillow**، للعمل مع الصور في بايثون.
- **requests**، لمساعدتك في إجراء طلبات HTTP.

1. أنشئ ملفًا _.env_ بالمحتوى التالي:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   حدد هذه المعلومات في بوابة Azure لموردك في قسم "المفاتيح ونقطة النهاية".

1. اجمع المكتبات المذكورة أعلاه في ملف يسمى _requirements.txt_ على النحو التالي:

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

   لنظام Windows، استخدم الأوامر التالية لإنشاء وتفعيل بيئتك الافتراضية:

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

لنشرح هذا الكود:

- أولاً، نستورد المكتبات التي نحتاجها، بما في ذلك مكتبة OpenAI، ومكتبة dotenv، ومكتبة requests، ومكتبة Pillow.

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

- بعد ذلك، نحدد نقطة النهاية والمفتاح لواجهة برمجة التطبيقات OpenAI، الإصدار والنوع.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- بعد ذلك، نقوم بتوليد الصورة:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  يستجيب الكود أعلاه بكائن JSON يحتوي على عنوان URL للصورة المولدة. يمكننا استخدام عنوان URL لتنزيل الصورة وحفظها في ملف.

- أخيرًا، نفتح الصورة ونستخدم عارض الصور القياسي لعرضها:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### مزيد من التفاصيل حول توليد الصورة

لنلق نظرة على الكود الذي يولد الصورة بمزيد من التفاصيل:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**، هو النص الذي يُستخدم لتوليد الصورة. في هذه الحالة، نحن نستخدم المطالبة "أرنب على حصان، يحمل مصاصة، في مرج ضبابي حيث تنمو النرجس".
- **size**، هو حجم الصورة التي يتم توليدها. في هذه الحالة، نحن نولد صورة بحجم 1024x1024 بكسل.
- **n**، هو عدد الصور التي يتم توليدها. في هذه الحالة، نحن نولد صورتين.
- **temperature**، هو معلمة تتحكم في عشوائية مخرجات نموذج الذكاء الاصطناعي التوليدي. درجة الحرارة هي قيمة بين 0 و1 حيث تعني 0 أن المخرجات حتمية و1 تعني أن المخرجات عشوائية. القيمة الافتراضية هي 0.7.

هناك المزيد من الأشياء التي يمكنك القيام بها مع الصور والتي سنغطيها في القسم التالي.

## قدرات إضافية لتوليد الصور

لقد رأيت حتى الآن كيف تمكنا من توليد صورة باستخدام بضع أسطر في بايثون. ومع ذلك، هناك المزيد من الأشياء التي يمكنك القيام بها مع الصور.

يمكنك أيضًا القيام بما يلي:

- **إجراء تعديلات**. من خلال توفير صورة موجودة وقناع ومطالبة، يمكنك تغيير صورة. على سبيل المثال، يمكنك إضافة شيء إلى جزء من صورة. تخيل صورة الأرنب لدينا، يمكنك إضافة قبعة إلى الأرنب. كيف يمكنك القيام بذلك هو توفير الصورة، وقناع (لتحديد الجزء من المنطقة للتغيير) ومطالبة نصية لتوضيح ما يجب فعله.

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

  ستكون الصورة الأساسية تحتوي فقط على الأرنب ولكن الصورة النهائية سيكون لديها القبعة على الأرنب.

- **إنشاء تغييرات**. الفكرة هي أن تأخذ صورة موجودة وتطلب إنشاء تغييرات. لإنشاء تغيير، توفر صورة ومطالبة نصية وكود مثل:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > ملاحظة، هذا مدعوم فقط على OpenAI

## درجة الحرارة

درجة الحرارة هي معلمة تتحكم في عشوائية مخرجات نموذج الذكاء الاصطناعي التوليدي. درجة الحرارة هي قيمة بين 0 و1 حيث تعني 0 أن المخرجات حتمية و1 تعني أن المخرجات عشوائية. القيمة الافتراضية هي 0.7.

لنلق نظرة على مثال لكيفية عمل درجة الحرارة، عن طريق تشغيل هذه المطالبة مرتين:

> مطالبة: "أرنب على حصان، يحمل مصاصة، في مرج ضبابي حيث تنمو النرجس"

![أرنب على حصان يحمل مصاصة، النسخة 1](../../../translated_images/v1-generated-image.208ba0525ed6ae505504aa852e28d334c0440e9931b7c97f9508176a22d2dd54.ar.png)

الآن لنقم بتشغيل نفس المطالبة فقط لنرى أننا لن نحصل على نفس الصورة مرتين:

![صورة مولدة لأرنب على حصان](../../../translated_images/v2-generated-image.f0a88c05ef476e95f3682d4b21c9ba2f4807ae71cc29e9c05b42ebbf497cf61b.ar.png)

كما ترى، الصور متشابهة، لكنها ليست نفسها. لنحاول تغيير قيمة درجة الحرارة إلى 0.1 ونرى ماذا يحدث:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### تغيير درجة الحرارة

لذا دعونا نحاول جعل الاستجابة أكثر حتمية. يمكننا أن نلاحظ من الصورتين اللتين قمنا بتوليدهما أنه في الصورة الأولى، هناك أرنب وفي الصورة الثانية، هناك حصان، لذا تختلف الصور بشكل كبير.

لذلك دعونا نغير كودنا ونضبط درجة الحرارة إلى 0، كما يلي:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

الآن عندما تقوم بتشغيل هذا الكود، ستحصل على هاتين الصورتين:

- ![درجة الحرارة 0، النسخة 1](../../../translated_images/v1-temp-generated-image.d8557be792b5c81c2c6d2804cb7b210fe8b340106fe4ffcadf9cf7de1cd7b991.ar.png)
- ![درجة الحرارة 0، النسخة 2](../../../translated_images/v2-temp-generated-image.bd412fcfbd43379312b1382212a332aa311ca1a80ea692dea50a8b876a487c61.ar.png)

هنا يمكنك بوضوح رؤية كيف تتشابه الصور أكثر.

## كيفية تحديد حدود لتطبيقك باستخدام المطالبات الفوقية

مع عرضنا التوضيحي، يمكننا بالفعل توليد الصور لعملائنا. ومع ذلك، نحتاج إلى إنشاء بعض الحدود لتطبيقنا.

على سبيل المثال، لا نريد توليد صور غير آمنة للعمل، أو غير مناسبة للأطفال.

يمكننا القيام بذلك باستخدام _المطالبات الفوقية_. المطالبات الفوقية هي نصوص تستخدم للتحكم في مخرجات نموذج الذكاء الاصطناعي التوليدي. على سبيل المثال، يمكننا استخدام المطالبات الفوقية للتحكم في المخرجات، وضمان أن تكون الصور المولدة آمنة للعمل، أو مناسبة للأطفال.

### كيف تعمل؟

الآن، كيف تعمل المطالبات الفوقية؟

المطالبات الفوقية هي نصوص تستخدم للتحكم في مخرجات نموذج الذكاء الاصطناعي التوليدي، يتم وضعها قبل المطالبة النصية، وتستخدم للتحكم في مخرجات النموذج وتضمينها في التطبيقات للتحكم في مخرجات النموذج. تجمع بين إدخال المطالبة وإدخال المطالبة الفوقية في مطالبة نصية واحدة.

مثال على مطالبة فوقية سيكون كالتالي:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

الآن، دعونا نرى كيف يمكننا استخدام المطالبات الفوقية في عرضنا التوضيحي.

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

من المطالبة أعلاه، يمكنك أن ترى كيف تأخذ جميع الصور التي يتم إنشاؤها في الاعتبار المطالبة الفوقية.

## مهمة - دعونا نمكن الطلاب

قدمنا Edu4All في بداية هذا الدرس. الآن حان الوقت لتمكين الطلاب من توليد الصور لتقييماتهم.

سيقوم الطلاب بإنشاء صور لتقييماتهم تحتوي على معالم، ويعود للطلاب تحديد المعالم بالضبط. يُطلب من الطلاب استخدام إبداعهم في هذه المهمة لوضع هذه المعالم في سياقات مختلفة.

## الحل

إليك حل محتمل:

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

## عمل رائع! تابع تعلمك

بعد إكمال هذا الدرس، تحقق من [مجموعة تعلم الذكاء الاصطناعي التوليدي](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) لمواصلة تحسين معرفتك بالذكاء الاصطناعي التوليدي!

انتقل إلى الدرس 10 حيث سنلقي نظرة على كيفية [بناء تطبيقات الذكاء الاصطناعي باستخدام التعليمات البرمجية المنخفضة](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**إخلاء المسؤولية**:  
تمت ترجمة هذه الوثيقة باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار الوثيقة الأصلية بلغتها الأصلية هي المصدر الموثوق. للحصول على معلومات حساسة، يوصى بالترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.