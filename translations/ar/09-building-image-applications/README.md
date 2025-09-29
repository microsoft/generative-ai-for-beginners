<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "063a2ac57d6b71bea0eaa880c68770d2",
  "translation_date": "2025-09-29T21:13:58+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "ar"
}
-->
# بناء تطبيقات توليد الصور

[![بناء تطبيقات توليد الصور](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.ar.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

هناك أكثر من مجرد توليد النصوص في نماذج اللغة الكبيرة (LLMs). يمكن أيضًا توليد الصور من أوصاف نصية. وجود الصور كوسيلة يمكن أن يكون مفيدًا للغاية في العديد من المجالات مثل التكنولوجيا الطبية، الهندسة المعمارية، السياحة، تطوير الألعاب والمزيد. في هذا الفصل، سنستعرض اثنين من أشهر نماذج توليد الصور، DALL-E وMidjourney.

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

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) و[Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) هما من أشهر نماذج توليد الصور، حيث يسمحان باستخدام البرومبتس لتوليد الصور.

### DALL-E

لنبدأ بـ DALL-E، وهو نموذج ذكاء اصطناعي توليدي يقوم بتوليد الصور من أوصاف نصية.

> [DALL-E هو مزيج من نموذجين، CLIP وdiffused attention](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**، هو نموذج يقوم بإنشاء تمثيلات رقمية للبيانات من الصور والنصوص.

- **Diffused attention**، هو نموذج يقوم بتوليد الصور من التمثيلات الرقمية. يتم تدريب DALL-E على مجموعة بيانات من الصور والنصوص ويمكن استخدامه لتوليد الصور من أوصاف نصية. على سبيل المثال، يمكن استخدام DALL-E لتوليد صور لقطة ترتدي قبعة، أو كلب بتسريحة موهوك.

### Midjourney

Midjourney يعمل بطريقة مشابهة لـ DALL-E، حيث يقوم بتوليد الصور من البرومبتس النصية. يمكن أيضًا استخدام Midjourney لتوليد الصور باستخدام برومبتس مثل "قطة ترتدي قبعة"، أو "كلب بتسريحة موهوك".

![صورة مولدة بواسطة Midjourney، حمامة ميكانيكية](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_حقوق الصورة ويكيبيديا، الصورة مولدة بواسطة Midjourney_

## كيف يعمل DALL-E وMidjourney؟

أولاً، [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E هو نموذج ذكاء اصطناعي توليدي يعتمد على بنية المحول مع _محول ذاتي التراجع_.

المحول الذاتي التراجع يحدد كيفية توليد النموذج للصور من الأوصاف النصية، حيث يولد بكسلًا واحدًا في كل مرة، ثم يستخدم البكسلات المولدة لتوليد البكسل التالي. يمر عبر طبقات متعددة في الشبكة العصبية حتى تكتمل الصورة.

من خلال هذه العملية، يتحكم DALL-E في السمات، الأشياء، الخصائص، والمزيد في الصورة التي يولدها. ومع ذلك، فإن DALL-E 2 و3 يوفران تحكمًا أكبر في الصورة المولدة.

## بناء أول تطبيق لتوليد الصور

إذن، ما الذي تحتاجه لبناء تطبيق لتوليد الصور؟ تحتاج إلى المكتبات التالية:

- **python-dotenv**، يُوصى بشدة باستخدام هذه المكتبة للحفاظ على الأسرار في ملف _.env_ بعيدًا عن الكود.
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

1. اجمع المكتبات المذكورة أعلاه في ملف يسمى _requirements.txt_ كما يلي:

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

   بالنسبة لنظام Windows، استخدم الأوامر التالية لإنشاء وتفعيل البيئة الافتراضية:

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

لنلقِ نظرة على الكود الذي يولد الصورة بمزيد من التفصيل:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**، هو البرومبت النصي المستخدم لتوليد الصورة. في هذه الحالة، نستخدم البرومبت "أرنب على حصان، يحمل مصاصة، في مرج ضبابي حيث تنمو النرجس".
- **size**، هو حجم الصورة التي يتم توليدها. في هذه الحالة، نقوم بتوليد صورة بحجم 1024x1024 بكسل.
- **n**، هو عدد الصور التي يتم توليدها. في هذه الحالة، نقوم بتوليد صورتين.
- **temperature**، هو معلمة تتحكم في عشوائية مخرجات نموذج الذكاء الاصطناعي التوليدي. القيمة الافتراضية هي 0.7.

هناك المزيد مما يمكنك القيام به مع الصور وسنغطي ذلك في القسم التالي.

## القدرات الإضافية لتوليد الصور

لقد رأيت حتى الآن كيف تمكنا من توليد صورة باستخدام بضعة أسطر في Python. ومع ذلك، هناك المزيد مما يمكنك القيام به مع الصور.

يمكنك أيضًا القيام بما يلي:

- **إجراء تعديلات**. من خلال تقديم صورة موجودة وقناع وبرومبت، يمكنك تعديل الصورة. على سبيل المثال، يمكنك إضافة شيء إلى جزء من الصورة. تخيل صورة الأرنب، يمكنك إضافة قبعة للأرنب. يتم ذلك عن طريق تقديم الصورة، قناع (لتحديد الجزء الذي سيتم تغييره) وبرومبت نصي لتحديد ما يجب القيام به.
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
  <img src="./images/s
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

## عمل رائع! واصل تعلمك

بعد إكمال هذا الدرس، تحقق من [مجموعة تعلم الذكاء الاصطناعي التوليدي](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) لمواصلة تطوير معرفتك بالذكاء الاصطناعي التوليدي!

انتقل إلى الدرس 10 حيث سنستعرض كيفية [بناء تطبيقات الذكاء الاصطناعي باستخدام البرمجة منخفضة الكود](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.