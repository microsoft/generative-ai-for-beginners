# بناء تطبيقات توليد النصوص

[![بناء تطبيقات توليد النصوص](../../../translated_images/ar/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(انقر على الصورة أعلاه لمشاهدة فيديو هذا الدرس)_

لقد رأيت حتى الآن من خلال هذا المنهج أنه توجد مفاهيم أساسية مثل المطالبات وحتى مجال كامل يُسمى "هندسة المطالبات". العديد من الأدوات التي يمكنك التفاعل معها مثل ChatGPT وOffice 365 ومنصة Microsoft Power وغيرها، تدعمك باستخدام المطالبات لإنجاز شيء ما.

لكي تضيف مثل هذه التجربة إلى تطبيق، تحتاج إلى فهم مفاهيم مثل المطالبات والاستكمالات واختيار مكتبة للعمل معها. هذا بالضبط ما ستتعلمه في هذا الفصل.

## المقدمة

في هذا الفصل، ستقوم بـ:

- التعرف على مكتبة openai ومفاهيمها الأساسية.
- بناء تطبيق توليد نص باستخدام openai.
- فهم كيفية استخدام مفاهيم مثل المطالبة، درجة الحرارة، والتوكنات لبناء تطبيق توليد نص.

## أهداف التعلم

في نهاية هذا الدرس، ستتمكن من:

- شرح ما هو تطبيق توليد النصوص.
- بناء تطبيق توليد نصوص باستخدام openai.
- ضبط تطبيقك لاستخدام عدد أكبر أو أقل من التوكنات وأيضًا تغيير درجة الحرارة، للحصول على مخرجات متنوعة.

## ما هو تطبيق توليد النصوص؟

عادةً عند بناء تطبيق يوجد له نوع من الواجهة مثل التالي:

- يعتمد على الأوامر. تطبيقات الكونسول هي تطبيقات نموذجية حيث تكتب أمرًا وينفذ مهمة. على سبيل المثال، `git` هو تطبيق يعتمد على الأوامر.
- واجهة المستخدم (UI). بعض التطبيقات لديها واجهات مستخدم رسومية (GUIs) حيث تنقر على الأزرار، تدخل نصوصًا، تختار خيارات والمزيد.

### تطبيقات الكونسول وواجهة المستخدم محدودة

قارنها بتطبيق يعتمد على الأوامر حيث تكتب أمرًا:

- **إنها محدودة**. لا يمكنك كتابة أي أمر، فقط الأوامر التي يدعمها التطبيق.
- **محددة بلغة معينة**. بعض التطبيقات تدعم العديد من اللغات، لكن بشكل افتراضي يُبنى التطبيق على لغة معينة، حتى لو يمكنك إضافة دعم للغات أخرى.

### فوائد تطبيقات توليد النصوص

فكيف يختلف تطبيق توليد النصوص؟

في تطبيق توليد النصوص، لديك المزيد من المرونة، لست مقيدًا بمجموعة من الأوامر أو لغة إدخال محددة. بدلاً من ذلك، يمكنك استخدام اللغة الطبيعية للتفاعل مع التطبيق. فائدة أخرى هي أنك تتفاعل بالفعل مع مصدر بيانات تم تدريبه على مجموعة ضخمة من المعلومات، بينما قد يكون التطبيق التقليدي محدودًا بما هو في قاعدة البيانات.

### ماذا يمكنني بناء بتطبيق توليد النصوص؟

هناك العديد من الأشياء التي يمكنك بناؤها. على سبيل المثال:

- **شات بوت**. شات بوت يجيب على أسئلة عن مواضيع، مثل شركتك ومنتجاتها قد يكون مناسبًا.
- **مساعد**. النماذج اللغوية الكبيرة (LLMs) ممتازة في أشياء مثل تلخيص النصوص، استخلاص الأفكار من النص، إنتاج نصوص مثل السير الذاتية والمزيد.
- **مساعد برمجي**. اعتمادًا على نموذج اللغة الذي تستخدمه، يمكنك بناء مساعد برمجي يساعدك في كتابة الكود. على سبيل المثال، يمكنك استخدام منتجات مثل GitHub Copilot وكذلك ChatGPT لمساعدتك في كتابة الكود.

## كيف يمكنني البدء؟

حسنًا، تحتاج إلى إيجاد طريقة للتكامل مع نموذج لغوي كبير (LLM) والذي غالبًا ما يتضمن النهجين التاليين:

- استخدام API. هنا تقوم بإنشاء طلبات ويب مع مطالبتك وتحصل على نص مولد كرد.
- استخدام مكتبة. المكتبات تساعد على تغليف استدعاءات API وتجعلها أسهل في الاستخدام.

## المكتبات / SDKs

هناك بعض المكتبات المعروفة للعمل مع النماذج اللغوية الكبيرة مثل:

- **openai**، هذه المكتبة تجعل من السهل الاتصال بالنموذج الخاص بك وإرسال المطالبات.

ثم هناك مكتبات تعمل على مستوى أعلى مثل:

- **Langchain**. Langchain معروفة وتدعم بايثون.
- **Semantic Kernel**. Semantic Kernel هي مكتبة من Microsoft تدعم لغات C# و Python و Java.

## أول تطبيق باستخدام openai

لنر كيف يمكننا بناء أول تطبيق لنا، ما المكتبات التي نحتاجها، كم هو مطلوب وهكذا.

### تثبيت openai

هناك العديد من المكتبات الموجودة للتفاعل مع OpenAI أو Azure OpenAI. من الممكن استخدام العديد من لغات البرمجة مثل C# و Python و JavaScript و Java والمزيد. لقد اخترنا استخدام مكتبة `openai` الخاصة ببايثون، لذا سنستخدم `pip` لتثبيتها.

```bash
pip install openai
```

### إنشاء مورد

تحتاج إلى إجراء الخطوات التالية:

- إنشاء حساب على Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- الحصول على وصول إلى Azure OpenAI. اذهب إلى [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) وقدم طلب وصول.

  > [!NOTE]
  > في وقت كتابة هذا، تحتاج إلى التقديم للحصول على وصول إلى Azure OpenAI.

- تثبيت بايثون <https://www.python.org/>
- إنشاء مورد خدمة Azure OpenAI. انظر هذا الدليل لكيفية [إنشاء مورد](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### تحديد مفتاح API ونقطة النهاية

في هذه المرحلة، تحتاج إلى إخبار مكتبة `openai` بمفتاح API الذي ستستخدمه. للعثور على مفتاح API الخاص بك، اذهب إلى قسم "Keys and Endpoint" في مورد Azure OpenAI الخاص بك ونسخ قيمة "Key 1".

![لوح مفاتيح ومورد نقطة النهاية في بوابة Azure](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

الآن بعد أن نسخت هذه المعلومات، دعنا نوجه المكتبات لاستخدامها.

> [!NOTE]
> من الأفضل فصل مفتاح API الخاص بك عن الكود. يمكنك فعل ذلك باستخدام متغيرات البيئة.
>
> - اضبط متغير البيئة `OPENAI_API_KEY` على مفتاح API الخاص بك.
>   `export OPENAI_API_KEY='sk-...'`

### إعداد تكوين Azure

إذا كنت تستخدم Azure OpenAI (الآن جزء من Microsoft Foundry)، إليك كيف تعد الإعداد. نستخدم عميل `OpenAI` القياسي موجه إلى نقطة نهاية Azure OpenAI `/openai/v1/`، الذي يعمل مع API الاستجابات ولا يحتاج `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

أعلاه نحن نحدد التالي:

- `api_key`، هذا هو مفتاح API الخاص بك الموجود في بوابة Azure أو بوابة Microsoft Foundry.
- `base_url`، هذه هي نقطة نهاية مورد Foundry الخاص بك مع `/openai/v1/` ملحقة. نقطة النهاية المستقرة v1 تعمل عبر OpenAI وAzure OpenAI بدون إدارة `api_version`.

> [!NOTE] > `os.environ` يقرأ متغيرات البيئة. يمكنك استخدامه لقراءة متغيرات البيئة مثل `AZURE_OPENAI_API_KEY` و`AZURE_OPENAI_ENDPOINT`. اضبط هذه المتغيرات في الطرفية أو باستخدام مكتبة مثل `dotenv`.

## توليد النص

طريقة توليد النص هي استخدام API الاستجابات عبر طريقة `responses.create`. إليك مثال:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

في الكود أعلاه، ننشئ استجابة ونمرر النموذج الذي نريد استخدامه والمطالبة. ثم نطبع النص المولد عن طريق `response.output_text`.

### المحادثات متعددة الدور

API الاستجابات ملائم لكل من توليد النص بدور واحد وشات بوت متعدد الدور - أنت تقدم قائمة بالرسائل في `input` لبناء المحادثة:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

المزيد عن هذه الوظيفة في فصل قادم.

## تمرين - أول تطبيق توليد نص لك

الآن بعد أن تعلمنا كيفية الإعداد والتكوين على openai، حان الوقت لبناء أول تطبيق توليد نص لك. لبناء تطبيقك، اتبع هذه الخطوات:

1. أنشئ بيئة افتراضية وثبت openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > إذا كنت تستخدم ويندوز، اكتب `venv\Scripts\activate` بدلًا من `source venv/bin/activate`.

   > [!NOTE]
   > حدد مفتاح Azure OpenAI الخاص بك بالذهاب إلى [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) وابحث عن `Open AI` واختر `Open AI resource` ثم اختر `Keys and Endpoint` وانسخ قيمة `Key 1`.

1. أنشئ ملف _app.py_ وأعطه الكود التالي:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"

   # make a request using the Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # print response
   print(response.output_text)
   ```

   > [!NOTE]
   > إذا كنت تستخدم OpenAI العادي (ليس Azure)، استخدم `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (بدون `base_url`) ومرر اسم نموذج مثل `gpt-5-mini` بدلًا من اسم نشر.

   يجب أن ترى مخرجات مثل التالية:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## أنواع مختلفة من المطالبات، لأغراض مختلفة

الآن شاهدت كيف تولد نص باستخدام مطلب. لديك برنامج يعمل ويمكنك تعديله وتغييره لتوليد أنواع مختلفة من النصوص.

يمكن استخدام المطالبات لمهام مختلفة. على سبيل المثال:

- **توليد نوع من النصوص**. على سبيل المثال، يمكنك توليد قصيدة، أسئلة لاختبار، إلخ.
- **البحث عن معلومات**. يمكنك استخدام المطالبات للبحث عن معلومات مثل المثال التالي "ماذا يعني CORS في تطوير الويب؟".
- **توليد كود**. يمكنك استخدام المطالبات لتوليد كود، مثل تطوير تعبير نمطي للتحقق من البريد الإلكتروني أو لماذا لا تولد برنامجًا كاملًا، مثل تطبيق ويب؟

## حالة استخدام أكثر عملية: مولد وصفات

تخيل أن لديك مكونات في المنزل وتريد طبخ شيء ما. لذلك، تحتاج إلى وصفة. يمكنك البحث عن وصفات باستخدام محرك بحث أو يمكنك استخدام نموذج لغوي كبير للقيام بذلك.

يمكنك كتابة مطلب مثل:

> "أرني 5 وصفات لطبق يحتوي على المكونات التالية: دجاج، بطاطا، وجزر. لكل وصفة، اذكر جميع المكونات المستخدمة"

بناءً على المطالبة أعلاه، قد تحصل على استجابة مشابهة لـ:

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

هذه النتيجة رائعة، أعلم ماذا أطبخ. في هذه المرحلة، ما قد يكون تحسينات مفيدة هو:

- تصفية المكونات التي لا أحبها أو لدي حساسية منها.
- إنتاج قائمة تسوق، في حالة عدم توفر جميع المكونات في المنزل.

للحالات أعلاه، دعنا نضيف مطلبًا إضافيًا:

> "يرجى إزالة الوصفات التي تحتوي على الثوم لأنني أعاني من حساسية منه واستبداله بشيء آخر. أيضًا، يرجى إنتاج قائمة تسوق للوصفات، مع الأخذ بعين الاعتبار أن لدي بالفعل دجاج، بطاطا وجزر في المنزل."

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

هذه هي الوصفات الخمسة الخاصة بك، بدون ذكر الثوم ولديك أيضًا قائمة تسوق مع الأخذ بعين الاعتبار ما لديك بالفعل في المنزل.

## تمرين - بناء مولد وصفات

الآن بعد أن عرضنا سيناريو، دعنا نكتب كودًا يطابق السيناريو المبين. للقيام بذلك، اتبع الخطوات التالية:

1. استخدم ملف _app.py_ الحالي كنقطة انطلاق
1. حدد متغير `prompt` وعدل الكود الخاص به إلى ما يلي:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   إذا شغلت الكود الآن، يجب أن ترى مخرجات مشابهة لـ:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > ملاحظة: نموذجك اللغوي غير حتمي، لذلك قد تحصل على نتائج مختلفة في كل مرة تشغل البرنامج.

   ممتاز، دعنا نرى كيف يمكننا تحسين الأمور. لتحسين الأمور، نريد التأكد من أن الكود مرن، بحيث يمكن تغيير المكونات وعدد الوصفات بسهولة.

1. دعنا نغير الكود بهذه الطريقة:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   يمكن أن يكون اختبار تشغيل هذا الكود مثل هذا:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### تحسين بإضافة الفلترة وقائمة التسوق

لدينا الآن تطبيق يعمل قادر على إنتاج وصفات وهو مرن لأنه يعتمد على مدخلات المستخدم، سواء على عدد الوصفات أو المكونات المستخدمة.

لتحسينه بشكل أكبر، نريد إضافة التالي:

- **تصفية المكونات**. نريد أن نتمكن من تصفية المكونات التي لا نحبها أو لدينا حساسية منها. لتحقيق هذا التغيير، يمكننا تعديل مطلبنا الحالي وإضافة شرط فلترة في نهايته مثل:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  أعلاه، أضفنا `{filter}` في نهاية المطالبة كما نلتقط قيمة الفلترة من المستخدم.

  مثال إدخال لتشغيل البرنامج قد يبدو الآن هكذا:

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

  كما ترى، تم تصفية أي وصفة تحتوي على الحليب. لكن، إذا كنت تعاني من حساسية اللاكتوز، قد ترغب في تصفية الوصفات التي تحتوي على الجبن أيضًا، لذلك يجب أن يكون هناك وضوح.

- **إنتاج قائمة تسوق**. نريد إنتاج قائمة تسوق، مع الأخذ بعين الاعتبار ما لدينا بالفعل في المنزل.

  لهذه الوظيفة، يمكننا محاولة حل كل شيء في مطلب واحد أو يمكننا تقسيمه إلى مطلبين. لنحاول النهج الثاني. هنا نقترح إضافة مطلب إضافي، ولكن لكي تعمل هذه الطريقة، نحتاج إلى إضافة نتيجة المطلب الأول كسياق للمطلب الثاني.

  حدد الجزء في الكود الذي يطبع نتيجة المطلب الأول وأضف الكود التالي تحته:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  لاحظ التالي:

  1. نحن ننشئ مطلبًا جديدًا بإضافة نتيجة المطلب الأول للمطلب الجديد:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. نقوم بإجراء طلب جديد، مع الأخذ بعين الاعتبار عدد التوكنات التي طلبناها في المطلب الأول، لذلك هذه المرة نحدد `max_output_tokens` كـ1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     تشغيل هذا الكود الآن يعطي الناتج التالي:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## حسن إعدادك

ما لدينا حتى الآن هو كود يعمل، لكن هناك بعض التعديلات التي يجب أن نقوم بها لتحسين الأمور أكثر. بعض الأشياء التي يجب علينا فعلها هي:

- **فصل الأسرار عن الكود**، مثل مفتاح API. لا تنتمي الأسرار إلى الكود ويجب تخزينها في مكان آمن. لفصل الأسرار عن الكود، يمكننا استخدام متغيرات البيئة ومكتبات مثل `python-dotenv` لتحميلها من ملف. هذا هو شكل ذلك في الكود:

  1. أنشئ ملف `.env` بالمحتوى التالي:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > ملاحظة، بالنسبة لـ Azure OpenAI في Microsoft Foundry، تحتاج إلى تعيين متغيرات البيئة التالية بدلاً من ذلك:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     في الكود، ستقوم بتحميل متغيرات البيئة كما يلي:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **كلمة حول طول التوكن**. يجب أن ننظر في عدد التوكنات التي نحتاجها لإنشاء النص الذي نريده. التوكنات تكلف مالًا، لذا حيثما أمكن، يجب أن نحاول أن نكون اقتصادين في عدد التوكنات التي نستخدمها. على سبيل المثال، هل يمكننا صياغة الأمر بطريقة نستخدم فيها توكنات أقل؟

  لتغيير عدد التوكنات المستخدمة، يمكنك استخدام معامل `max_output_tokens`. على سبيل المثال، إذا أردت استخدام 100 توكن، ستفعل كما يلي:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **التجربة مع درجة الحرارة**. درجة الحرارة هي أمر لم نذكره حتى الآن ولكنه سياق مهم لكيفية أداء برنامجنا. كلما زادت قيمة درجة الحرارة، كان الإخراج أكثر عشوائية. بالمقابل، كلما انخفضت قيمة درجة الحرارة، كان الإخراج أكثر قابلية للتنبؤ. فكر فيما إذا كنت تريد تنوعًا في إخراجك أم لا.

  لتغيير درجة الحرارة، يمكنك استخدام معامل `temperature`. على سبيل المثال، إذا أردت استخدام درجة حرارة 0.5، ستفعل كما يلي:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > ملاحظة، كلما اقتربت القيمة من 1.0، زاد تنوع الإخراج.

- **نماذج الاستدلال لا تستخدم `temperature`**. هذا تحول مهم في عام 2026. النماذج الحالية غير المهجورة في Microsoft Foundry هي **نماذج استدلال** (عائلة GPT-5، سلسلة o) - وهي **لا تدعم `temperature` أو `top_p`** (ولا `max_tokens`؛ استخدم `max_output_tokens`). إذا أرسلت `temperature` إلى `gpt-5-mini` ستحصل على خطأ "المعامل غير مدعوم". لذا لتجربة مثال درجة الحرارة أعلاه، وجّه الطلب إلى نموذج لا يزال يدعم ضوابط العينة - على سبيل المثال، نموذج Llama المفتوح مثل `Llama-3.3-70B-Instruct` من [كتالوج نماذج Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)، يستدعى عبر نقطة نهاية Foundry Models / Azure AI Inference (بنفس طريقة عينات `githubmodels-*`). بالنسبة لنماذج الاستدلال مثل GPT-5، توجه الإخراج بطريقة مختلفة:
  - **هندسة المحفزات** - تعليمات واضحة، أمثلة، وإخراج منظم (راجع الدرس [04 - هندسة المحفزات](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) تقوم بالعمل الذي كانت تقوم به أزرار العينة.
  - **ضوابط الاستدلال** - معلمات مثل جهد الاستدلال / الثرثرة توازن بين عمق الاستدلال مقابل التأخير والتكلفة.

  باختصار: `temperature`/`top_p` لا تزال صالحة على العديد من النماذج (Llama، Mistral، Phi، وعائلة GPT-4.x - رغم أن GPT-4.x في طريقه إلى التوقف)، ولكن الاتجاه هو هندسة المحفزات + ضوابط الاستدلال على نماذج الاستدلال مثل GPT-5.

## المهمة

في هذه المهمة، يمكنك اختيار ما تريد بناءه.

إليك بعض الاقتراحات:

- عدل تطبيق مولد الوصفات لتحسينه أكثر. جرب التغييرات في قيم درجة الحرارة، والمحركات لترى ماذا يمكنك أن تبتكر.
- أنشئ "رفيق دراسة". يجب أن يكون هذا التطبيق قادرًا على الإجابة عن أسئلة حول موضوع معين، مثل بايثون، يمكن أن تكون المحفزات مثل "ما هو موضوع معين في بايثون؟"، أو يمكنك أن تضع محركًا يقول، أرني كودًا لموضوع معين، وهكذا.
- روبوت تاريخي، اجعل التاريخ ينبض بالحياة، وجه الروبوت ليقوم بدور شخصية تاريخية معينة واسأله عن حياته وأزمنته.

## الحل

### رفيق الدراسة

أدناه محفز ابتدائي، انظر كيف يمكنك استخدامه وتعديله حسب رغبتك.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### الروبوت التاريخي

إليك بعض المحفزات التي يمكنك استخدامها:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## اختبار المعرفة

ماذا يفعل مفهوم درجة الحرارة؟

1. يتحكم في مدى عشوائية الإخراج.
1. يتحكم في حجم الرد.
1. يتحكم في عدد التوكنات المستخدمة.

## 🚀 التحدي

عند العمل على المهمة، حاول تغيير درجة الحرارة، جرب تعيينها إلى 0، 0.5، و1. تذكر أن 0 هو الأقل تنوعًا و1 هو الأكثر. ما هي القيمة التي تعمل بشكل أفضل لتطبيقك؟

## عمل رائع! واصل تعلمك

بعد إكمال هذا الدرس، تحقق من [مجموعة تعلم الذكاء الاصطناعي التوليدي](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) لمواصلة رفع مستوى معرفتك بالذكاء الاصطناعي التوليدي!

انتقل إلى الدرس 7 حيث سننظر في كيفية [بناء تطبيقات الدردشة](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->