# بناء تطبيقات توليد النصوص

[![بناء تطبيقات توليد النصوص](../../../translated_images/ar/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(انقر على الصورة أعلاه لمشاهدة فيديو هذا الدرس)_

لقد رأيت حتى الآن خلال هذه المناهج أن هناك مفاهيم أساسية مثل التنبيهات وحتى تخصص كامل يسمى "هندسة التنبيهات". العديد من الأدوات التي يمكنك التفاعل معها مثل ChatGPT و Office 365 و Microsoft Power Platform والمزيد تدعمك باستخدام التنبيهات لتحقيق شيء ما.

لكي تضيف مثل هذه التجربة إلى تطبيق، تحتاج إلى فهم مفاهيم مثل التنبيهات، والإكمالات، واختيار مكتبة للعمل معها. هذا بالضبط ما ستتعلمه في هذا الفصل.

## مقدمة

في هذا الفصل، سوف:

- تتعلم عن مكتبة openai ومفاهيمها الأساسية.
- تبني تطبيق توليد نصوص باستخدام openai.
- تفهم كيفية استخدام مفاهيم مثل التنبيه، ودرجة الحرارة، والرموز لبناء تطبيق لتوليد النصوص.

## أهداف التعلم

في نهاية هذا الدرس، ستكون قادرًا على:

- شرح ما هو تطبيق توليد النصوص.
- بناء تطبيق توليد نصوص باستخدام openai.
- تكوين تطبيقك لاستخدام المزيد أو القليل من الرموز وكذلك تغيير درجة الحرارة، للحصول على مخرجات متنوعة.

## ما هو تطبيق توليد النصوص؟

عادةً عندما تبني تطبيقًا، يكون لديه نوع من الواجهة مثل التالي:

- قائم على الأوامر. تطبيقات وحدة التحكم هي تطبيقات نموذجية حيث تكتب أمرًا وينفذ مهمة ما. على سبيل المثال، `git` هو تطبيق قائم على الأوامر.
- واجهة مستخدم (UI). بعض التطبيقات لديها واجهات مستخدم رسومية (GUIs) حيث تنقر على أزرار، تدخل نصًا، تختار خيارات والمزيد.

### تطبيقات وحدة التحكم وواجهات المستخدم محدودة

قارنها بتطبيق قائم على الأوامر حيث تكتب أمرًا:

- **إنها محدودة**. لا يمكنك كتابة أي أمر، فقط الأوامر التي يدعمها التطبيق.
- **محددة اللغة**. بعض التطبيقات تدعم عدة لغات، لكن بشكل افتراضي التطبيق مبني للغة محددة، حتى إذا كان يمكنك إضافة دعم لغات أخرى.

### فوائد تطبيقات توليد النصوص

كيف يختلف تطبيق توليد النصوص؟

في تطبيق توليد النصوص، لديك المزيد من المرونة، أنت لست محدودًا بمجموعة أوامر أو لغة إدخال محددة. بدلاً من ذلك، يمكنك استخدام اللغة الطبيعية للتفاعل مع التطبيق. فائدة أخرى هي أنك تتفاعل بالفعل مع مصدر بيانات تم تدريبه على مجموعة ضخمة من المعلومات، بينما قد يكون التطبيق التقليدي محدودًا بما هو موجود في قاعدة بيانات.

### ماذا يمكنني أن أبني بتطبيق توليد النصوص؟

هناك أشياء كثيرة يمكنك بناؤها. على سبيل المثال:

- **روبوت دردشة**. روبوت دردشة يجيب عن أسئلة حول مواضيع، مثل شركتك ومنتجاتها يمكن أن يكون مناسبًا.
- **مساعد**. النماذج اللغوية الكبيرة ممتازة في أشياء مثل تلخيص النصوص، استخراج الأفكار من النصوص، إنتاج نصوص مثل السير الذاتية والمزيد.
- **مساعد برمجة**. حسب نموذج اللغة الذي تستخدمه، يمكنك بناء مساعد برمجة يساعدك في كتابة الكود. على سبيل المثال، يمكنك استخدام منتج مثل GitHub Copilot وكذلك ChatGPT لمساعدتك في كتابة الكود.

## كيف يمكنني البدء؟

حسنًا، تحتاج إلى إيجاد طريقة للاندماج مع نموذج لغة كبير، والذي عادة ما يتطلب أحد النهجين التاليين:

- استخدام واجهة برمجة التطبيقات (API). هنا تقوم ببناء طلبات ويب مع التنبيه الخاص بك وتحصل على النص المولد.
- استخدام مكتبة. تساعد المكتبات في تغليف استدعاءات API وتجعل استخدامها أسهل.

## المكتبات / مجموعات التطوير البرمجية

هناك بعض المكتبات المعروفة للعمل مع النماذج اللغوية الكبيرة مثل:

- **openai**، هذه المكتبة تسهل الاتصال بنموذجك وإرسال التنبيهات.

بعد ذلك، هناك مكتبات تعمل على مستوى أعلى مثل:

- **Langchain**. Langchain معروفة جيدًا وتدعم بايثون.
- **Semantic Kernel**. Semantic Kernel هي مكتبة من مايكروسوفت تدعم اللغات C#، بايثون، وجافا.

## أول تطبيق باستخدام openai

لنرَ كيف يمكننا بناء تطبيقنا الأول، وما المكتبات التي نحتاجها، وكم يتطلب الأمر، وما إلى ذلك.

### تثبيت openai

هناك العديد من المكتبات للتفاعل مع OpenAI أو Azure OpenAI. من الممكن استخدام لغات برمجة متعددة مثل C#، بايثون، جافا سكريبت، جافا والمزيد. لقد اخترنا استخدام مكتبة `openai` بلغة بايثون، لذا سنستخدم `pip` لتثبيتها.

```bash
pip install openai
```

### إنشاء مورد

تحتاج إلى تنفيذ الخطوات التالية:

- إنشاء حساب على Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- الحصول على الوصول إلى Azure OpenAI. انتقل إلى [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) وقدم طلبًا للحصول على الوصول.

  > [!NOTE]
  > في وقت كتابة هذا، تحتاج إلى التقديم للحصول على الوصول إلى Azure OpenAI.

- تثبيت بايثون <https://www.python.org/>
- إنشاء مورد خدمة Azure OpenAI. تحقق من هذا الدليل لكيفية [إنشاء مورد](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### تحديد مفتاح API ونقطة النهاية

في هذه المرحلة، تحتاج إلى إخبار مكتبة `openai` بمفتاح API الذي ستستخدمه. للعثور على مفتاح API الخاص بك، انتقل إلى قسم "Keys and Endpoint" في مورد Azure OpenAI الخاص بك ونسخ قيمة "Key 1".

![شاشة مفاتيح ونقطة نهاية المورد في بوابة Azure](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

الآن بعد أن نسخت هذه المعلومات، دعنا نوجه المكتبات لاستخدامها.

> [!NOTE]
> من الأفضل فصل مفتاح API الخاص بك عن الكود الخاص بك. يمكنك فعل ذلك باستخدام متغيرات البيئة.
>
> - قم بتعيين متغير البيئة `OPENAI_API_KEY` إلى مفتاح API الخاص بك.
>   `export OPENAI_API_KEY='sk-...'`

### إعداد تكوين Azure

إذا كنت تستخدم Azure OpenAI (الذي أصبح جزءًا من Microsoft Foundry)، إليك كيفية إعداد التكوين. نحن نستخدم العميل الافتراضي `OpenAI` الموجه إلى نقطة نهاية Azure OpenAI `/openai/v1/`، والتي تعمل مع واجهة برمجة تطبيقات Responses ولا تحتاج إلى `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

في الأعلى، نحن نحدد التالي:

- `api_key`، هذا هو مفتاح API الخاص بك الموجود في بوابة Azure أو بوابة Microsoft Foundry.
- `base_url`، هذه هي نقطة نهاية مورد Foundry الخاص بك مع الإضافة `/openai/v1/`. نقطة النهاية المستقرة v1 تعمل عبر OpenAI وAzure OpenAI بدون إدارة `api_version`.

> [!NOTE] > `os.environ` يقرأ متغيرات البيئة. يمكنك استخدامه لقراءة متغيرات البيئة مثل `AZURE_OPENAI_API_KEY` و `AZURE_OPENAI_ENDPOINT`. قم بتعيين هذه المتغيرات في الطرفية الخاصة بك أو باستخدام مكتبة مثل `dotenv`.

## توليد النص

الطريقة لتوليد النص هي استخدام واجهة برمجة تطبيقات Responses عبر طريقة `responses.create`. إليك مثالاً:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # هذا هو اسم نشر النموذج الخاص بك
    input=prompt,
    store=False,
)
print(response.output_text)
```

في الكود أعلاه، نقوم بإنشاء استجابة ونمرر النموذج الذي نريد استخدامه والتنبيه. ثم نطبع النص المولد عبر `response.output_text`.

### المحادثات متعددة الجولات

واجهة برمجة تطبيقات Responses مناسبة جيدًا لكل من توليد النص لجولة واحدة وروبوتات الدردشة متعددة الجولات - أنت تزود قائمة من الرسائل في `input` لبناء محادثة:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

المزيد عن هذه الوظيفة في فصل قادم.

## تمرين - تطبيقك الأول لتوليد النصوص

الآن بعد أن تعلمنا كيفية إعداد وتكوين openai، حان الوقت لبناء تطبيقك الأول لتوليد النصوص. لبناء تطبيقك، اتبع الخطوات التالية:

1. أنشئ بيئة افتراضية وثبت openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > إذا كنت تستخدم ويندوز، اكتب `venv\Scripts\activate` بدلًا من `source venv/bin/activate`.

   > [!NOTE]
   > حدد مفتاح Azure OpenAI الخاص بك بالذهاب إلى [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) وابحث عن `Open AI` واختر `مصدر Open AI` ثم اختر `Keys and Endpoint` ونسخ قيمة `Key 1`.

1. أنشئ ملف _app.py_ وامنحه الكود التالي:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # أضف رمز الإكمال الخاص بك
   prompt = "Complete the following: Once upon a time there was a"

   # قم بعمل طلب باستخدام واجهة برمجة تطبيقات الردود
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # اطبع الاستجابة
   print(response.output_text)
   ```

   > [!NOTE]
   > إذا كنت تستخدم OpenAI العادي (ليس Azure)، فاستخدم `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (بدون `base_url`) ومرر اسم نموذج مثل `gpt-5-mini` بدلًا من اسم النشر.

   يجب أن ترى مخرجات مثل التالية:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## أنواع مختلفة من التنبيهات، لأغراض مختلفة

الآن رأيت كيف تولد نصًا باستخدام تنبيه. لديك حتى برنامج يعمل يمكنك تعديله وتغييره لتوليد أنواع مختلفة من النصوص.

يمكن استخدام التنبيهات لجميع أنواع المهام. على سبيل المثال:

- **توليد نوع من النص**. على سبيل المثال، يمكنك توليد قصيدة، أسئلة لاختبار، وهكذا.
- **البحث عن معلومات**. يمكنك استخدام التنبيهات للبحث عن معلومات مثل المثال التالي "ماذا يعني CORS في تطوير الويب؟".
- **توليد كود**. يمكنك استخدام التنبيهات لتوليد كود، على سبيل المثال تطوير تعبير نمطي للتحقق من صحة الإيميلات أو لماذا لا تولد برنامجًا كاملاً، مثل تطبيق ويب؟

## حالة استخدام أكثر عملية: مولد وصفات

تخيل أن لديك مكونات في المنزل وتريد أن تطبخ شيئًا. لهذا تحتاج وصفة. إحدى الطرق لإيجاد وصفات هي استخدام محرك بحث أو يمكنك استخدام نموذج لغوي كبير للقيام بذلك.

يمكنك كتابة تنبيه مثل:

> "اعرض لي 5 وصفات لطبق بالمكونات التالية: دجاج، بطاطس، وجزر. لكل وصفة، أدرج جميع المكونات المستخدمة"

بناءً على التنبيه أعلاه، قد تحصل على استجابة مماثلة لـ:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 2 cloves garlic, minced
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
```

هذه النتيجة رائعة، أعرف ماذا أطبخ. في هذه المرحلة، ما قد يكون تحسينًا مفيدًا هو:

- تصفية المكونات التي لا أحبها أو لدي حساسية لها.
- إنتاج قائمة تسوق، في حال لم تكن أملك جميع المكونات في المنزل.

للحالات أعلاه، دعنا نضيف تنبيهًا إضافيًا:

> "يرجى إزالة الوصفات التي تحتوي على الثوم لأنني لدي حساسية واستبداله بشيء آخر. أيضًا، يرجى إعداد قائمة تسوق للوصفات، مع الأخذ بعين الاعتبار أنني أملك بالفعل الدجاج والبطاطس والجزر في المنزل."

الآن لديك نتيجة جديدة، وهي:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano

Shopping List:
- Olive oil
- Onion
- Thyme
- Oregano
- Salt
- Pepper
```

هذه هي خمس وصفاتك، بدون ذكر الثوم ولديك أيضًا قائمة تسوق مع الأخذ بعين الاعتبار ما لديك في المنزل.

## تمرين - بناء مولد وصفات

الآن بعد أن لعبنا سيناريو، دعنا نكتب كودًا يطابق السيناريو المعروض. للقيام بذلك، اتبع الخطوات التالية:

1. استخدم ملف _app.py_ الموجود كنقطة بداية.
1. حدد متغير `prompt` وغيّر كوده إلى التالي:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   إذا قمت الآن بتشغيل الكود، يجب أن ترى مخرجًا مشابهًا لـ:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > ملاحظة، نموذج لغتك كبير غير محدد النتائج بدقة، لذا قد تحصل على نتائج مختلفة في كل مرة تشغل البرنامج.

   رائع، دعنا نرى كيف يمكننا تحسين الأمور. للتحسين، نريد التأكد من أن الكود مرن، بحيث يمكن تحسين وتغيير المكونات وعدد الوصفات.

1. دعنا نغير الكود بالطريقة التالية:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # إدخال عدد الوصفات في الموجه والمكونات
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   أخذ الكود لتشغيل اختبار يمكن أن يبدو هكذا:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### تحسين بإضافة فلتر وقائمة تسوق

لدينا الآن تطبيق يعمل قادر على إنتاج وصفات وهو مرن لأنه يعتمد على مدخلات المستخدم، سواء على عدد الوصفات أو المكونات المستخدمة.

لتحسينه أكثر، نريد إضافة التالي:

- **تصفية المكونات**. نريد أن نتمكن من تصفية المكونات التي لا نحبها أو لدينا حساسية منها. لتحقيق هذا التغيير، يمكننا تعديل التنبيه الحالي لدينا وإضافة شرط الفلترة في نهايته هكذا:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  أعلاه، أضفنا `{filter}` إلى نهاية التنبيه ونحن نلتقط أيضًا قيمة الفلتر من المستخدم.

  يمكن أن يكون الإدخال التجريبي لتشغيل البرنامج الآن كما يلي:

  ```output
  No of recipes (for example, 5): 3
  List of ingredients (for example, chicken, potatoes, and carrots): onion,milk
  Filter (for example, vegetarian, vegan, or gluten-free): no milk

  1. French Onion Soup

  Ingredients:

  -1 large onion, sliced
  -3 cups beef broth
  -1 cup milk
  -6 slices french bread
  -1/4 cup shredded Parmesan cheese
  -1 tablespoon butter
  -1 teaspoon dried thyme
  -1/4 teaspoon salt
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add beef broth, milk, thyme, salt, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Place french bread slices on soup bowls.
  5. Ladle soup over bread.
  6. Sprinkle with Parmesan cheese.

  2. Onion and Potato Soup

  Ingredients:

  -1 large onion, chopped
  -2 cups potatoes, diced
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add potatoes, vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Serve hot.

  3. Creamy Onion Soup

  Ingredients:

  -1 large onion, chopped
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper
  -1/4 cup all-purpose flour
  -1/2 cup shredded Parmesan cheese

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. In a small bowl, whisk together flour and Parmesan cheese until smooth.
  5. Add to soup and simmer for an additional 5 minutes, or until soup has thickened.
  ```

  كما ترى، جميع الوصفات التي تحتوي على الحليب تم تصفيتها. لكن، إذا كنت تعاني من عدم تحمل اللاكتوز، قد ترغب أيضًا في تصفية الوصفات التي تحتوي على الجبن، لذا هناك حاجة لأن تكون صريحًا.


- **إنشاء قائمة تسوق**. نريد إنشاء قائمة تسوق، مع الأخذ في الاعتبار ما لدينا بالفعل في المنزل.

  لهذه الوظيفة، يمكننا إما محاولة حل كل شيء في موجه واحد أو يمكننا تقسيمها إلى اثنين من الموجهات. دعونا نجرب النهج الأخير. هنا نقترح إضافة موجه إضافي، ولكن لكي ينجح ذلك، نحتاج إلى إضافة نتيجة الموجه الأول كسياق للموجه الثاني.

  حدد الجزء في الكود الذي يطبع النتيجة من الموجه الأول وأضف الكود التالي تحته:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # طباعة الاستجابة
  print("Shopping list:")
  print(response.output_text)
  ```

  لاحظ ما يلي:

  1. نحن نبني موجهًا جديدًا بإضافة نتيجة الموجه الأول إلى الموجه الجديد:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. نرسل طلبًا جديدًا، مع الأخذ في الاعتبار عدد الرموز التي طلبناها في الموجه الأول، لذا في هذه المرة نقول `max_output_tokens` هو 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     بعد تجربة هذا الكود، وصلنا الآن إلى الإخراج التالي:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## تحسين إعدادك

ما لدينا حتى الآن هو كود يعمل، لكن هناك بعض التعديلات التي يجب علينا القيام بها لتحسين الأمور أكثر. بعض الأشياء التي يجب علينا فعلها هي:

- **فصل الأسرار عن الكود**، مثل مفتاح API. الأسرار لا ينبغي أن تكون ضمن الكود ويجب تخزينها في مكان آمن. لفصل الأسرار عن الكود، يمكننا استخدام متغيرات البيئة ومكتبات مثل `python-dotenv` لتحميلها من ملف. إليك كيف يبدو ذلك في الكود:

  1. إنشاء ملف `.env` بالمحتوى التالي:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > ملاحظة، بالنسبة لـ Azure OpenAI في Microsoft Foundry، تحتاج إلى تعيين متغيرات البيئة التالية بدلاً من ذلك:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     في الكود، يمكنك تحميل متغيرات البيئة كما يلي:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **كلمة عن طول الرموز**. يجب أن نأخذ في الاعتبار عدد الرموز التي نحتاجها لتوليد النص الذي نريده. الرموز تكلف مالاً، لذلك حيثما أمكن، يجب أن نحاول أن نكون اقتصاديين في عدد الرموز التي نستخدمها. على سبيل المثال، هل يمكننا صياغة الموجه بحيث نستخدم رموزًا أقل؟

  لتغيير عدد الرموز المستخدمة، يمكنك استخدام المعامل `max_output_tokens`. على سبيل المثال، إذا أردت استخدام 100 رمز، ستفعل:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **التجربة مع درجة الحرارة**. درجة الحرارة هي أمر لم نذكره حتى الآن لكنه سياق مهم لكيفية أداء برنامجنا. كلما زادت قيمة درجة الحرارة، كان الإخراج أكثر عشوائية. وعلى العكس، كلما كانت قيمة درجة الحرارة أقل، كان الإخراج أكثر توقعًا. فكر في ما إذا كنت تريد تنوعًا في الإخراج أم لا.

  لتغيير درجة الحرارة، يمكنك استخدام المعامل `temperature`. على سبيل المثال، إذا أردت استخدام درجة حرارة 0.5، ستفعل:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > ملاحظة، كلما اقتربت من 1.0، كان الإخراج أكثر تنوعًا.

- **نماذج الاستدلال لا تستخدم `temperature`**. هذا تحول مهم في 2026. النماذج الحالية غير المتقادمة في Microsoft Foundry هي **نماذج استدلال** (عائلة GPT-5، سلسلة o) - وهي **لا تدعم `temperature` أو `top_p`** (ولا `max_tokens`; استخدم `max_output_tokens`). إذا أرسلت `temperature` إلى `gpt-5-mini` ستحصل على خطأ "المعامل غير مدعوم". لذلك لتجربة مثال درجة الحرارة أعلاه، وجه الأمر إلى نموذج ما زال يدعم إعدادات العينة - على سبيل المثال نموذج مفتوح **Llama** مثل `Llama-3.3-70B-Instruct` من [كتالوج نماذج Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)، يتم مناداته عبر نقطة النهاية Foundry Models / Azure AI Inference (بنفس طريقة عينات `githubmodels-*`). بالنسبة لنماذج الاستدلال مثل GPT-5، يتم توجيه الإخراج بشكل مختلف:
  - **هندسة الموجه** - تعليمات واضحة، أمثلة، وإخراج منظم (انظر الدرس [04 - أساسيات هندسة الموجه](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) تقوم بالعمل الذي كانت إعدادات العينة تقوم به سابقًا.
  - **تحكمات الاستدلال** - معاملات مثل جهد الاستدلال/التفصيل تتوازن بين عمق الاستدلال مقابل الزمن والتكلفة.

  باختصار: `temperature`/`top_p` لا تزال صالحة على العديد من النماذج (Llama، Mistral، Phi، وعائلة GPT-4.x - رغم أن GPT-4.x في طور الاستغناء عنها)، لكن الاتجاه هو هندسة الموجه + تحكمات الاستدلال على نماذج الاستدلال مثل GPT-5.

## الواجب

في هذا الواجب، يمكنك اختيار ما تريد بناءه.

إليك بعض الاقتراحات:

- قم بتحسين تطبيق مولد الوصفات أكثر. جرب القيم المختلفة لدرجة الحرارة، والموجهات لترى ما يمكنك التوصل إليه.
- بناء "مساعد دراسي". يجب أن يكون هذا التطبيق قادرًا على إجابة الأسئلة حول موضوع معين مثل بايثون، يمكنك أن تضع موجهات مثل "ما هو موضوع معين في بايثون؟"، أو موجه يقول، أرني كودًا لموضوع معين إلخ.
- بوت تاريخي، اجعل التاريخ ينبض بالحياة، قم بإعطاء البوت تعليمات للعب دور شخصية تاريخية معينة واسأله أسئلة عن حياته وأزمنته.

## الحل

### مساعد دراسي

أدناه موجه للبدء، انظر كيف يمكنك استخدامه وتعديله حسب رغبتك.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### بوت تاريخي

هنا بعض الموجهات التي يمكن أن تستخدمها:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## اختبار المعرفة

ما هو دور مفهوم درجة الحرارة؟

1. يتحكم في مدى عشوائية الإخراج.
1. يتحكم في حجم الاستجابة.
1. يتحكم في عدد الرموز المستخدمة.

## 🚀 التحدي

أثناء العمل على الواجب، حاول تغيير درجة الحرارة، جرب تعيينها إلى 0، 0.5، و1. تذكر أن 0 هو الأقل تنوعًا و1 هو الأكثر. ما القيمة التي تناسب تطبيقك أفضل؟

## عمل رائع! واصل التعلم

بعد إكمال هذا الدرس، اطلع على [مجموعة تعلم الذكاء الاصطناعي التوليدي](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) للاستمرار في رفع مستوى معرفتك بالذكاء الاصطناعي التوليدي!

توجه إلى الدرس 7 حيث سننظر في كيفية [بناء تطبيقات الدردشة](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->