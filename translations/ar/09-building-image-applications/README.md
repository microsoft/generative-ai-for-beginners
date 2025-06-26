<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-06-25T17:04:58+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ar"
}
-->
# بناء تطبيقات توليد الصور

هناك أكثر من مجرد توليد النصوص في نماذج اللغة الكبيرة (LLMs). من الممكن أيضًا توليد الصور من أوصاف النصوص. وجود الصور كوسيلة يمكن أن يكون مفيدًا جدًا في عدد من المجالات مثل التكنولوجيا الطبية، الهندسة المعمارية، السياحة، تطوير الألعاب والمزيد. في هذا الفصل، سنلقي نظرة على اثنين من أشهر نماذج توليد الصور، DALL-E وMidjourney.

## مقدمة

في هذا الدرس، سنغطي:

- توليد الصور ولماذا هو مفيد.
- DALL-E وMidjourney، ما هما وكيف يعملان.
- كيفية بناء تطبيق لتوليد الصور.

## أهداف التعلم

بعد إكمال هذا الدرس، ستكون قادرًا على:

- بناء تطبيق لتوليد الصور.
- تحديد حدود لتطبيقك باستخدام توجيهات ميتا.
- العمل مع DALL-E وMidjourney.

## لماذا نبني تطبيق لتوليد الصور؟

تطبيقات توليد الصور هي وسيلة رائعة لاستكشاف قدرات الذكاء الاصطناعي التوليدي. يمكن استخدامها، على سبيل المثال:

- **تحرير الصور وتوليفها**. يمكنك توليد الصور لمجموعة متنوعة من الاستخدامات، مثل تحرير الصور وتوليف الصور.

- **تطبيقها في مجموعة متنوعة من الصناعات**. يمكن استخدامها أيضًا لتوليد الصور لمجموعة متنوعة من الصناعات مثل التكنولوجيا الطبية، السياحة، تطوير الألعاب والمزيد.

## سيناريو: Edu4All

كجزء من هذا الدرس، سنواصل العمل مع شركتنا الناشئة، Edu4All، في هذا الدرس. سيقوم الطلاب بإنشاء صور لتقييماتهم، ويمكن أن تكون هذه الصور رسومات لقصتهم الخيالية أو إنشاء شخصية جديدة لقصتهم أو مساعدتهم في تصور أفكارهم ومفاهيمهم.

إليك ما يمكن لطلاب Edu4All توليده على سبيل المثال إذا كانوا يعملون في الصف على الآثار:

باستخدام توجيه مثل

> "كلب بجوار برج إيفل في ضوء شمس الصباح الباكر"

## ما هو DALL-E وMidjourney؟

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) و[Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) هما اثنان من أشهر نماذج توليد الصور، يسمحان لك باستخدام توجيهات لتوليد الصور.

### DALL-E

لنبدأ مع DALL-E، وهو نموذج ذكاء اصطناعي توليدي يقوم بتوليد الصور من أوصاف النصوص.

- **CLIP**، هو نموذج يقوم بتوليد التضمينات، وهي تمثيلات رقمية للبيانات، من الصور والنصوص.

- **الاهتمام المنتشر**، هو نموذج يقوم بتوليد الصور من التضمينات. يتم تدريب DALL-E على مجموعة بيانات من الصور والنصوص ويمكن استخدامه لتوليد الصور من أوصاف النصوص. على سبيل المثال، يمكن استخدام DALL-E لتوليد صور لقط في قبعة، أو كلب بتسريحة موهوك.

### Midjourney

يعمل Midjourney بطريقة مشابهة لـ DALL-E، حيث يقوم بتوليد الصور من توجيهات النصوص. يمكن استخدام Midjourney أيضًا لتوليد الصور باستخدام توجيهات مثل "قط في قبعة"، أو "كلب بتسريحة موهوك".

## كيف يعمل DALL-E وMidjourney

أولاً، [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E هو نموذج ذكاء اصطناعي توليدي يعتمد على بنية المحول مع _محول ذاتي الانحدار_.

_المحول الذاتي الانحدار_ يحدد كيفية توليد نموذج للصور من أوصاف النصوص، حيث يولد بكسل واحد في كل مرة، ثم يستخدم البكسلات المولدة لتوليد البكسل التالي. يمر عبر طبقات متعددة في شبكة عصبية، حتى تكتمل الصورة.

مع هذه العملية، يتحكم DALL-E في السمات، الكائنات، الخصائص، والمزيد في الصورة التي يولدها. ومع ذلك، فإن DALL-E 2 و3 لديهما تحكم أكبر في الصورة المولدة.

## بناء تطبيقك الأول لتوليد الصور

إذًا، ماذا يتطلب بناء تطبيق لتوليد الصور؟ تحتاج إلى المكتبات التالية:

- **python-dotenv**، يُوصى بشدة باستخدام هذه المكتبة للحفاظ على أسرارك في ملف _.env_ بعيدًا عن الشيفرة.
- **openai**، هذه المكتبة هي ما ستستخدمه للتفاعل مع واجهة برمجة تطبيقات OpenAI.
- **pillow**، للعمل مع الصور في بايثون.
- **requests**، لمساعدتك في إجراء طلبات HTTP.

1. أنشئ ملفًا _.env_ بالمحتوى التالي:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   حدد هذه المعلومات في بوابة Azure لموردك في قسم "المفاتيح ونقطة النهاية".

1. اجمع المكتبات المذكورة أعلاه في ملف يسمى _requirements.txt_ كالتالي:

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

   بالنسبة لـ Windows، استخدم الأوامر التالية لإنشاء وتفعيل بيئتك الافتراضية:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. أضف الشيفرة التالية في ملف يسمى _app.py_:

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

لنشرح هذه الشيفرة:

- أولاً، نستورد المكتبات التي نحتاجها، بما في ذلك مكتبة OpenAI، مكتبة dotenv، مكتبة requests، ومكتبة Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- بعد ذلك، نقوم بتحميل متغيرات البيئة من الملف _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- بعد ذلك، نحدد نقطة النهاية والمفتاح لواجهة برمجة تطبيقات OpenAI، الإصدار والنوع.

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

  يستجيب الكود أعلاه بجسم JSON يحتوي على عنوان URL للصورة المولدة. يمكننا استخدام عنوان URL لتنزيل الصورة وحفظها في ملف.

- أخيرًا، نقوم بفتح الصورة واستخدام عارض الصور القياسي لعرضها:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### مزيد من التفاصيل حول توليد الصورة

لنلقِ نظرة على الشيفرة التي تولد الصورة بمزيد من التفاصيل:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **التوجيه**، هو توجيه النص الذي يستخدم لتوليد الصورة. في هذه الحالة، نستخدم التوجيه "أرنب على حصان، يحمل مصاصة، في مرج ضبابي حيث تنمو النرجس".
- **الحجم**، هو حجم الصورة التي يتم توليدها. في هذه الحالة، نقوم بتوليد صورة بحجم 1024x1024 بكسل.
- **n**، هو عدد الصور التي يتم توليدها. في هذه الحالة، نقوم بتوليد صورتين.
- **درجة الحرارة**، هي معلمة تتحكم في عشوائية مخرجات نموذج الذكاء الاصطناعي التوليدي. درجة الحرارة هي قيمة بين 0 و1 حيث يعني 0 أن المخرجات حتمية و1 يعني أن المخرجات عشوائية. القيمة الافتراضية هي 0.7.

هناك المزيد من الأشياء التي يمكنك القيام بها مع الصور والتي سنغطيها في القسم التالي.

## القدرات الإضافية لتوليد الصور

لقد رأيت حتى الآن كيف تمكنا من توليد صورة باستخدام بضعة أسطر في بايثون. ومع ذلك، هناك المزيد من الأشياء التي يمكنك القيام بها مع الصور.

يمكنك أيضًا القيام بما يلي:

- **إجراء التعديلات**. من خلال توفير صورة موجودة وقناع وتوجيه، يمكنك تغيير صورة. على سبيل المثال، يمكنك إضافة شيء إلى جزء من الصورة. تخيل صورة الأرنب الخاصة بنا، يمكنك إضافة قبعة للأرنب. كيف تقوم بذلك هو عن طريق توفير الصورة، قناع (لتحديد الجزء من المنطقة للتغيير) وتوجيه نصي لتوضيح ما يجب فعله.

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

  ستكون الصورة الأساسية تحتوي فقط على الأرنب ولكن الصورة النهائية ستحتوي على القبعة على الأرنب.

- **إنشاء التغييرات**. الفكرة هي أنك تأخذ صورة موجودة وتطلب إنشاء تغييرات. لإنشاء تغيير، توفر صورة وتوجيه نصي وشيفرة كالتالي:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > ملاحظة، هذا مدعوم فقط في OpenAI

## درجة الحرارة

درجة الحرارة هي معلمة تتحكم في عشوائية مخرجات نموذج الذكاء الاصطناعي التوليدي. درجة الحرارة هي قيمة بين 0 و1 حيث يعني 0 أن المخرجات حتمية و1 يعني أن المخرجات عشوائية. القيمة الافتراضية هي 0.7.

لنلقِ نظرة على مثال لكيفية عمل درجة الحرارة، بتشغيل هذا التوجيه مرتين:

> توجيه: "أرنب على حصان، يحمل مصاصة، في مرج ضبابي حيث تنمو النرجس"

الآن دعونا نشغل نفس التوجيه لنرى أننا لن نحصل على نفس الصورة مرتين:

كما ترى، الصور متشابهة، ولكن ليست متطابقة. لنحاول تغيير قيمة درجة الحرارة إلى 0.1 ونرى ما سيحدث:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### تغيير درجة الحرارة

لذلك دعونا نحاول جعل الاستجابة أكثر حتمية. يمكننا ملاحظة من الصور التي قمنا بتوليدها أن في الصورة الأولى، هناك أرنب وفي الصورة الثانية، هناك حصان، لذا تختلف الصور بشكل كبير.

لذلك دعونا نغير شيفرتنا ونضبط درجة الحرارة على 0، كالتالي:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

الآن عندما تشغل هذه الشيفرة، ستحصل على هاتين الصورتين:

هنا يمكنك بوضوح رؤية كيف أن الصور تتشابه أكثر.

## كيفية تحديد الحدود لتطبيقك باستخدام التوجيهات الميتا

مع عرضنا التوضيحي، يمكننا بالفعل توليد الصور لعملائنا. ومع ذلك، نحتاج إلى إنشاء بعض الحدود لتطبيقنا.

على سبيل المثال، لا نريد توليد صور غير آمنة للعمل، أو غير مناسبة للأطفال.

يمكننا القيام بذلك باستخدام _التوجيهات الميتا_. التوجيهات الميتا هي توجيهات نصية تستخدم للتحكم في مخرجات نموذج الذكاء الاصطناعي التوليدي. على سبيل المثال، يمكننا استخدام التوجيهات الميتا للتحكم في المخرجات، وضمان أن الصور المولدة آمنة للعمل، أو مناسبة للأطفال.

### كيف تعمل؟

الآن، كيف تعمل التوجيهات الميتا؟

التوجيهات الميتا هي توجيهات نصية تستخدم للتحكم في مخرجات نموذج الذكاء الاصطناعي التوليدي، يتم وضعها قبل توجيه النص، وتستخدم للتحكم في مخرجات النموذج وتضمينها في التطبيقات للتحكم في مخرجات النموذج. تضمين إدخال التوجيه وإدخال التوجيه الميتا في توجيه نصي واحد.

مثال على توجيه ميتا سيكون كالتالي:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

الآن، دعونا نرى كيف يمكننا استخدام التوجيهات الميتا في عرضنا التوضيحي.

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

من التوجيه أعلاه، يمكنك رؤية كيف أن جميع الصور التي يتم إنشاؤها تأخذ في الاعتبار التوجيه الميتا.

## المهمة - دعونا نمكّن الطلاب

قدمنا Edu4All في بداية هذا الدرس. الآن حان الوقت لتمكين الطلاب من توليد الصور لتقييماتهم.

سيقوم الطلاب بإنشاء صور لتقييماتهم تحتوي على آثار، بالضبط ما هي الآثار متروك للطلاب. يُطلب من الطلاب استخدام إبداعهم في هذه المهمة لوضع هذه الآثار في سياقات مختلفة.

## الحل

إليك حل ممكن:

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

بعد إكمال هذا الدرس، تحقق من [مجموعة تعلم الذكاء الاصطناعي التوليدي](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) لمواصلة رفع مستوى معرفتك بالذكاء الاصطناعي التوليدي!

توجه إلى الدرس 10 حيث سنلقي نظرة على كيفية [بناء تطبيقات الذكاء الاصطناعي باستخدام البرمجة منخفضة الكود](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**إخلاء المسؤولية**:  
تمت ترجمة هذه الوثيقة باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى جاهدين لتحقيق الدقة، يرجى العلم بأن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار الوثيقة الأصلية بلغتها الأم المصدر الموثوق به. بالنسبة للمعلومات الحساسة، يُوصى بالترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ناتج عن استخدام هذه الترجمة.