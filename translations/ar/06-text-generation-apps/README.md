# بناء تطبيقات توليد النصوص

[![بناء تطبيقات توليد النصوص](../../../translated_images/ar/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(انقر على الصورة أعلاه لمشاهدة فيديو هذا الدرس)_

لقد رأيت حتى الآن من خلال هذا المنهج أن هناك مفاهيم أساسية مثل المطالبات وحتى تخصص كامل يسمى "هندسة المطالبات". العديد من الأدوات التي يمكنك التفاعل معها مثل ChatGPT وOffice 365 وMicrosoft Power Platform والمزيد، تدعمك باستخدام المطالبات لإنجاز شيء ما.

لكي تضيف مثل هذه التجربة إلى تطبيق، تحتاج إلى فهم مفاهيم مثل المطالبات، والإكمالات واختيار مكتبة للعمل معها. هذا بالضبط ما ستتعلمه في هذا الفصل.

## مقدمة

في هذا الفصل، سوف:

- تتعلم عن مكتبة openai ومفاهيمها الأساسية.
- تبني تطبيق توليد نص باستخدام openai.
- تفهم كيفية استخدام مفاهيم مثل المطالبة، ودرجة الحرارة، والرموز لبناء تطبيق توليد نص.

## أهداف التعلم

في نهاية هذا الدرس، ستكون قادرًا على:

- شرح ما هو تطبيق توليد النصوص.
- بناء تطبيق توليد نص باستخدام openai.
- تكوين تطبيقك لاستخدام المزيد أو القليل من الرموز وأيضًا تغيير درجة الحرارة، للحصول على مخرجات متنوعة.

## ما هو تطبيق توليد النص؟

عادةً عندما تبني تطبيقًا يكون لديه نوع من الواجهة مثل التالية:

- قائم على الأوامر. تطبيقات وحدة التحكم هي تطبيقات نموذجية حيث تكتب أمرًا ويقوم بتنفيذ مهمة. على سبيل المثال، `git` هو تطبيق قائم على الأوامر.
- واجهة المستخدم (UI). بعض التطبيقات لديها واجهات مستخدم رسومية حيث تنقر على أزرار، تدخل نصًا، تختار خيارات والمزيد.

### تطبيقات وحدة التحكم وواجهة المستخدم محدودة

قارن ذلك بتطبيق قائم على الأمر حيث تكتب أمرًا:

- **إنه محدود**. لا يمكنك كتابة أي أمر، فقط الأوامر التي يدعمها التطبيق.
- **خاص بلغة معينة**. بعض التطبيقات تدعم عدة لغات، لكن بشكل افتراضي التطبيق مبني للغة محددة، حتى لو يمكنك إضافة دعم للغات أخرى.

### فوائد تطبيقات توليد النصوص

فما الفرق بين تطبيق توليد النصوص؟

في تطبيق توليد النصوص، لديك مرونة أكثر، لست مقيدًا بمجموعة أوامر أو لغة إدخال محددة. بدلاً من ذلك، يمكنك استخدام اللغة الطبيعية للتفاعل مع التطبيق. فائدة أخرى هي أنك تتفاعل بالفعل مع مصدر بيانات تم تدريبه على مجموعة ضخمة من المعلومات، في حين قد يكون التطبيق التقليدي محدودًا بما يوجد في قاعدة بيانات.

### ماذا يمكنني أن أبني باستخدام تطبيق توليد النصوص؟

هناك العديد من الأشياء التي يمكنك بناؤها. على سبيل المثال:

- **دردشة تلقائية**. دردشة ترد على أسئلة حول مواضيع مثل شركتك ومنتجاتها يمكن أن تكون ملائمة جدًا.
- **مساعد**. نماذج اللغة الكبيرة جيدة جدًا في أشياء مثل تلخيص النصوص، الحصول على رؤى من النص، إنتاج نصوص مثل السير الذاتية والمزيد.
- **مساعد برمجي**. اعتمادًا على نموذج اللغة الذي تستخدمه، يمكنك بناء مساعد برمجي يساعدك على كتابة الكود. على سبيل المثال، يمكنك استخدام منتج مثل GitHub Copilot بالإضافة إلى ChatGPT لمساعدتك في كتابة الكود.

## كيف يمكنني البدء؟

حسنًا، تحتاج إلى إيجاد طريقة للتكامل مع نموذج لغة كبير (LLM) والذي عادةً ما ينطوي على النهجين التاليين:

- استخدام API. هنا تبني طلبات ويب مع مطالبتك وتحصل على نص مولد كرد.
- استخدام مكتبة. المكتبات تساعد في تجميع استدعاءات الـ API وتجعل استخدامها أسهل.

## المكتبات وأدوات التطوير (SDKs)

هناك بعض المكتبات المعروفة للعمل مع نماذج اللغة الكبيرة مثل:

- **openai**، هذه المكتبة تجعل من السهل الاتصال بنموذجك وإرسال المطالبات.

ثم هناك مكتبات تعمل على مستوى أعلى مثل:

- **Langchain**. Langchain معروفة وتدعم Python.
- **Semantic Kernel**. Semantic Kernel هي مكتبة من Microsoft تدعم اللغات C# وPython وJava.

## التطبيق الأول باستخدام openai

لنر كيف يمكننا بناء تطبيقنا الأول، المكتبات التي نحتاجها، وكم المطلوب، وهكذا.

### تثبيت openai

هناك العديد من المكتبات المتاحة للتفاعل مع OpenAI أو Azure OpenAI. من الممكن استخدام عدة لغات برمجة مثل C# وPython وJavaScript وJava والمزيد. لقد اخترنا استخدام مكتبة `openai` للبايثون، لذا سنستخدم `pip` لتثبيتها.

```bash
pip install openai
```

### إنشاء مورد

عليك تنفيذ الخطوات التالية:

- إنشاء حساب على Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- الحصول على وصول إلى Azure OpenAI. اذهب إلى [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) واطلب الوصول.

  > [!NOTE]
  > في وقت كتابة هذا، تحتاج إلى التقديم للحصول على وصول إلى Azure OpenAI.

- تثبيت Python <https://www.python.org/>
- إنشاء مورد لخدمة Azure OpenAI. اطلع على هذا الدليل لكيفية [إنشاء مورد](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### العثور على مفتاح API ونقطة النهاية

في هذه المرحلة، تحتاج إلى إخبار مكتبة `openai` بمفتاح API الذي ستستخدمه. للعثور على مفتاح API الخاص بك، اذهب إلى قسم "المفاتيح ونقطة النهاية" في مورد Azure OpenAI الخاص بك ونسخ قيمة "المفتاح 1".

![لوحة مفاتيح ونقطة نهاية المورد في بوابة Azure](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

بعد أن قمت بنسخ هذه المعلومات، دعنا نوجه المكتبات لاستخدامها.

> [!NOTE]
> من المفيد فصل مفتاح API الخاص بك عن الكود. يمكنك القيام بذلك باستخدام متغيرات البيئة.
>
> - قم بتعيين متغير البيئة `OPENAI_API_KEY` إلى مفتاح API الخاص بك.
>   `export OPENAI_API_KEY='sk-...'`

### إعداد تكوين Azure

إذا كنت تستخدم Azure OpenAI (الذي أصبح الآن جزءًا من Microsoft Foundry)، في ما يلي كيفية إعداد التكوين. نستخدم عميل `OpenAI` القياسي الموجه إلى نقطة نهاية Azure OpenAI `/openai/v1/`، والتي تعمل مع Responses API ولا تحتاج إلى `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

أعلاه نحن نقوم بتعيين ما يلي:

- `api_key`، هذا هو مفتاح API الخاص بك الموجود في بوابة Azure أو بوابة Microsoft Foundry.
- `base_url`، هذه هي نقطة نهاية مورد Foundry الخاص بك مع إضافة `/openai/v1/` في النهاية. نقطة النهاية المستقرة v1 تعمل عبر OpenAI وAzure OpenAI بدون إدارة `api_version`.

> [!NOTE] > `os.environ` يقرأ متغيرات البيئة. يمكنك استخدامه لقراءة متغيرات البيئة مثل `AZURE_OPENAI_API_KEY` و `AZURE_OPENAI_ENDPOINT`. قم بتعيين هذه المتغيرات في الطرفية الخاصة بك أو باستخدام مكتبة مثل `dotenv`.

## توليد النص

طريقة توليد النص هي استخدام Responses API عبر طريقة `responses.create`. إليك مثالًا:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # هذا هو اسم نشر النموذج الخاص بك
    input=prompt,
    store=False,
)
print(response.output_text)
```

في الكود أعلاه، ننشئ ردًا ونمرر النموذج الذي نريد استخدامه والمطالبة. ثم نطبع النص المولد عبر `response.output_text`.

### المحادثات المتعددة الأدوار

Responses API مناسبة لكل من توليد النص في دور واحد والدردشات متعددة الأدوار - تقدم قائمة بالرسائل في `input` لبناء المحادثة:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

المزيد عن هذه الوظيفة في فصل قادم.

## تمرين - تطبيق توليد النص الأول الخاص بك

الآن بعد أن تعلمنا كيفية إعداد وتكوين openai، حان الوقت لبناء تطبيق توليد النص الأول الخاص بك. لبناء التطبيق، اتبع الخطوات التالية:

1. إنشاء بيئة افتراضية وتثبيت openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > إذا كنت تستخدم Windows اكتب `venv\Scripts\activate` بدلاً من `source venv/bin/activate`.

   > [!NOTE]
   > حدد موقع مفتاح Azure OpenAI الخاص بك بالذهاب إلى [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) وابحث عن `Open AI` واختر `Open AI resource` ثم اختر `Keys and Endpoint` ونسخ قيمة `Key 1`.

1. إنشاء ملف _app.py_ وأعطه الكود التالي:

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

   # قدم طلبًا باستخدام واجهة برمجة التطبيقات للردود
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # اطبع الاستجابة
   print(response.output_text)
   ```

   > [!NOTE]
   > إذا كنت تستخدم OpenAI العادي (ليس Azure)، استخدم `client = OpenAI(api_key="<استبدل هذه القيمة بمفتاح OpenAI الخاص بك>")` (بدون `base_url`) ومرر اسم النموذج مثل `gpt-4o-mini` بدلاً من اسم النشر.

   يجب أن ترى مخرجًا مثل التالي:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## أنواع مختلفة من المطالبات، لأغراض مختلفة

الآن بعد أن رأيت كيف تولد نصًا باستخدام مطالبة. لديك حتى برنامج يعمل يمكنك تعديله وتغييره لتوليد أنواع مختلفة من النصوص.

يمكن استخدام المطالبات في جميع أنواع المهام. على سبيل المثال:

- **توليد نوع من النص**. على سبيل المثال، يمكنك توليد قصيدة، أسئلة لاختبار، إلخ.
- **البحث عن معلومات**. يمكنك استخدام المطالبات للبحث عن معلومات مثل المثال التالي 'ماذا يعني CORS في تطوير الويب؟'.
- **توليد كود**. يمكنك استخدام المطالبات لتوليد كود، على سبيل المثال تطوير تعبير عادي يستخدم للتحقق من صحة البريد الإلكتروني أو لماذا لا تولد برنامجًا كاملاً، مثل تطبيق ويب؟

## حالة استخدام أكثر عملية: مولد وصفات

تخيل أن لديك مكونات في المنزل وتريد طهي شيء ما. لهذا تحتاج إلى وصفة. طريقة للعثور على الوصفات هي استخدام محرك بحث أو يمكنك استخدام نموذج لغة كبير للقيام بذلك.

يمكنك كتابة مطالبة مثل:

> "أرني 5 وصفات لطبق بالمكونات التالية: دجاج، بطاطا، وجزر. لكل وصفة، أدرج جميع المكونات المستخدمة"

بناءً على المطالبة أعلاه، قد تحصل على رد مشابه لـ:

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

هذه النتيجة رائعة، أعرف ما سأطبخ. في هذه المرحلة، ما قد يكون تحسينات مفيدة هو:

- تصفية المكونات التي لا أحبها أو التي أعاني من حساسية تجاهها.
- إنتاج قائمة تسوق، في حال لم يكن لدي كل المكونات في المنزل.

للحالات أعلاه، دعنا نضيف مطالبة إضافية:

> "يرجى إزالة الوصفات التي تحتوي على الثوم لأنني أعاني من حساسية واستبدلها بشيء آخر. وأيضًا، يرجى إعداد قائمة تسوق للوصفات، مع الأخذ في الاعتبار أنني لدي بالفعل دجاج، بطاطا وجزر في المنزل."

لديك الآن نتيجة جديدة، وهي:

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

هذه هي وصفاتك الخمسة، بدون ذكر الثوم ولديك أيضًا قائمة تسوق مع الأخذ بعين الاعتبار ما لديك بالفعل في المنزل.

## تمرين - بناء مولد وصفات

الآن بعد أن لعبنا السيناريو، دعنا نكتب كودًا يتطابق مع السيناريو المُوضح. للقيام بذلك، اتبع الخطوات التالية:

1. استخدم ملف _app.py_ الموجود كنقطة انطلاق
1. حدد موقع متغير `prompt` وغيّر كوده إلى ما يلي:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   إذا شغلت الكود الآن، يجب أن ترى مخرجًا مشابهًا لـ:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > ملاحظة، نموذج اللغة الكبير الخاص بك غير حتمى، لذا قد تحصل على نتائج مختلفة في كل مرة تشغل البرنامج فيها.

   رائع، دعنا نرى كيف يمكننا تحسين الأمور. للتحسين نريد التأكد من أن الكود مرن، بحيث يمكن تحسين وتغيير المكونات وعدد الوصفات.

1. دعنا نغير الكود كالآتي:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # أدخل عدد الوصفات في الموجه والمكونات
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   قد يبدو استخدام الكود في تجربة اختبارية هكذا:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### تحسين بإضافة فلتر وقائمة تسوق

لدينا الآن تطبيق يعمل قادر على إنتاج وصفات وهو مرن لأنه يعتمد على مدخلات من المستخدم، سواء بعدد الوصفات أو المكونات المستخدمة.

لتحسينه أكثر، نريد إضافة ما يلي:

- **تصفية المكونات**. نريد أن نتمكن من تصفية المكونات التي لا نحبها أو لدينا حساسية منها. لتحقيق هذا التغيير، يمكننا تعديل مطالبتنا الحالية وإضافة شرط فلترة في نهايتها مثل التالي:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  أعلاه، أضفنا `{filter}` في نهاية المطالبة ونحن كذلك نلتقط قيمة الفلتر من المستخدم.

  مثال على إدخال تشغيل البرنامج يمكن أن يكون كالتالي:

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

  كما ترى، أي وصفات تحتوي على الحليب تم تصفيتها. لكن، إذا كنت تعاني من عدم تحمل اللاكتوز، قد ترغب أيضًا في تصفية الوصفات التي تحتوي على الجبن، لذا هناك حاجة أن يكون الأمر واضحًا.


- **إنتاج قائمة تسوق**. نريد إنتاج قائمة تسوق، مع مراعاة ما لدينا بالفعل في المنزل.

  لهذه الوظيفة، يمكننا إما محاولة حل كل شيء في موجه واحد أو يمكننا تقسيمه إلى موجهين. دعنا نجرب النهج الأخير. هنا نقترح إضافة موجه إضافي، ولكن لكي يعمل ذلك، نحتاج إلى إضافة نتيجة الموجه الأول كسياق للموجه الثاني.

  حدد الجزء في الشفرة الذي يطبع النتيجة من الموجه الأول وأضف الشفرة التالية أدناه:

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

  1. نقوم بإنشاء موجه جديد عن طريق إضافة نتيجة الموجه الأول إلى الموجه الجديد:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. نقوم بطلب جديد، مع مراعاة عدد الرموز الذي طلبناه في الموجه الأول، لذا هذه المرة نقول `max_output_tokens` هو 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     باستخدام هذا الرمز، نصل الآن إلى المخرجات التالية:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## حسّن إعدادك

ما لدينا حتى الآن هو رمز يعمل، لكن هناك بعض التعديلات التي يجب علينا القيام بها لتحسين الأمور أكثر. بعض الأشياء التي يجب فعلها هي:

- **فصل الأسرار عن الشفرة**، مثل مفتاح API. لا تنتمي الأسرار إلى الشفرة ويجب تخزينها في مكان آمن. لفصل الأسرار عن الشفرة، يمكننا استخدام متغيرات البيئة ومكتبات مثل `python-dotenv` لتحميلها من ملف. وهذا كيف سيبدو في الشفرة:

  1. أنشئ ملف `.env` بالمحتوى التالي:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > ملاحظة، بالنسبة لـ Azure OpenAI في Microsoft Foundry، تحتاج إلى إعداد متغيرات البيئة التالية بدلاً من ذلك:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     في الشفرة، ستقوم بتحميل متغيرات البيئة كما يلي:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **كلمة حول طول الرموز**. يجب أن نأخذ في الاعتبار عدد الرموز التي نحتاجها لتوليد النص الذي نريده. الرموز تكلف مالاً، لذا حيثما أمكن، يجب أن نحاول أن نكون اقتصاديين مع عدد الرموز التي نستخدمها. على سبيل المثال، هل يمكننا صياغة الموجه بحيث نستخدم رموزًا أقل؟

  لتغيير الرموز المستخدمة، يمكنك استخدام معلمة `max_output_tokens`. على سبيل المثال، إذا أردت استخدام 100 رمز، ستفعل:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **التجربة مع درجة الحرارة**. درجة الحرارة شيء لم نذكره حتى الآن لكنه سياق مهم لكيفية أداء برنامجنا. كلما زادت قيمة درجة الحرارة، كلما كان الناتج أكثر عشوائية. والعكس صحيح، كلما انخفضت قيمة درجة الحرارة، كان الناتج أكثر قابلية للتوقع. فكر فيما إذا كنت تريد تنوعًا في الناتج أم لا.

  لتغيير درجة الحرارة، يمكنك استخدام معلمة `temperature`. على سبيل المثال، إذا أردت استخدام درجة حرارة 0.5، تفعل:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > ملاحظة، كلما اقتربت القيمة من 1.0، زاد تنوع الناتج.

## المهمة

بالنسبة لهذه المهمة، يمكنك اختيار ما تريد بناءه.

إليك بعض الاقتراحات:

- عدل تطبيق مولد الوصفات لتحسينه أكثر. جرب تغيير قيم درجة الحرارة والموجهات لترى ما يمكنك التوصل إليه.
- ابني "رفيق دراسة". يجب أن يكون هذا التطبيق قادرًا على الإجابة عن الأسئلة حول موضوع معين مثل بايثون، يمكنك أن يكون لديك موجهات مثل "ما هو موضوع معين في بايثون؟"، أو يمكنك أن يكون لديك موجه يعرض لي شفرة لموضوع معين إلخ.
- بوت التاريخ، اجعل التاريخ ينبض بالحياة، أعطِ تعليمات للبوت ليلعب دور شخصية تاريخية معينة واطرح عليه أسئلة حول حياته وأوقاته.

## الحل

### رفيق الدراسة

أدناه موجه بداية، شاهد كيف يمكنك استخدامه وتعديله حسب رغبتك.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### بوت التاريخ

إليك بعض الموجهات التي يمكنك استخدامها:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## اختبار المعرفة

ماذا تفعل فكرة درجة الحرارة؟

1. تتحكم في مدى عشوائية الناتج.
1. تتحكم في حجم الاستجابة.
1. تتحكم في عدد الرموز المستخدمة.

## 🚀 التحدي

عند العمل على المهمة، حاول تنويع درجة الحرارة، جرب تعيينها إلى 0، 0.5، و1. تذكر أن 0 هو الأقل تنوعًا و1 هو الأكثر. ما هي القيمة التي تعمل بشكل أفضل لتطبيقك؟

## عمل رائع! واصل تعلمك

بعد إكمال هذا الدرس، تحقق من [مجموعة تعلم الذكاء الاصطناعي التوليدي الخاصة بنا](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) لمواصلة رفع مستوى معرفتك في الذكاء الاصطناعي التوليدي!

توجه إلى الدرس 7 حيث سنلقي نظرة على كيفية [إنشاء تطبيقات الدردشة](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->