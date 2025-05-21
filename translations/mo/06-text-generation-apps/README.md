<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-05-19T16:43:59+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "mo"
}
-->
# بناء تطبيقات توليد النصوص

[![بناء تطبيقات توليد النصوص](../../../translated_images/06-lesson-banner.90d8a665630e46b2990412d7c7d3d43c30f2441c95c0ee93e0763fb252734e83.mo.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(انقر على الصورة أعلاه لمشاهدة فيديو هذا الدرس)_

لقد رأيت حتى الآن من خلال هذه المناهج أن هناك مفاهيم أساسية مثل الإرشادات وحتى تخصص كامل يسمى "هندسة الإرشادات". العديد من الأدوات التي يمكنك التفاعل معها مثل ChatGPT وOffice 365 وMicrosoft Power Platform وغيرها، تدعمك في استخدام الإرشادات لتحقيق شيء ما.

لكي تضيف مثل هذه التجربة إلى تطبيق، تحتاج إلى فهم مفاهيم مثل الإرشادات، الإكمالات واختيار مكتبة للعمل بها. هذا بالضبط ما ستتعلمه في هذا الفصل.

## المقدمة

في هذا الفصل، سوف:

- تتعلم عن مكتبة openai ومفاهيمها الأساسية.
- تبني تطبيق لتوليد النصوص باستخدام openai.
- تفهم كيفية استخدام مفاهيم مثل الإرشادات، درجة الحرارة، والرموز لبناء تطبيق لتوليد النصوص.

## أهداف التعلم

في نهاية هذا الدرس، ستتمكن من:

- شرح ما هو تطبيق توليد النصوص.
- بناء تطبيق لتوليد النصوص باستخدام openai.
- تكوين تطبيقك لاستخدام المزيد أو الأقل من الرموز وأيضًا تغيير درجة الحرارة للحصول على نتائج متنوعة.

## ما هو تطبيق توليد النصوص؟

عادةً عندما تبني تطبيقًا يكون له نوع من الواجهة مثل ما يلي:

- يعتمد على الأوامر. التطبيقات القائمة على وحدة التحكم هي تطبيقات نموذجية حيث تقوم بكتابة أمر وتقوم بتنفيذ مهمة. على سبيل المثال، `git` هو تطبيق يعتمد على الأوامر.
- واجهة المستخدم (UI). بعض التطبيقات لديها واجهات مستخدم رسومية (GUIs) حيث يمكنك النقر على الأزرار، إدخال النص، اختيار الخيارات والمزيد.

### التطبيقات القائمة على وحدة التحكم وواجهة المستخدم محدودة

قارنها بتطبيق يعتمد على الأوامر حيث تقوم بكتابة أمر:

- **إنها محدودة**. لا يمكنك كتابة أي أمر، فقط الأوامر التي يدعمها التطبيق.
- **لغة محددة**. بعض التطبيقات تدعم العديد من اللغات، ولكن بشكل افتراضي يتم بناء التطبيق للغة معينة، حتى لو كان بإمكانك إضافة دعم للغات أخرى.

### فوائد تطبيقات توليد النصوص

كيف يختلف تطبيق توليد النصوص؟

في تطبيق توليد النصوص، لديك المزيد من المرونة، لا تكون مقيدًا بمجموعة من الأوامر أو لغة إدخال معينة. بدلاً من ذلك، يمكنك استخدام اللغة الطبيعية للتفاعل مع التطبيق. فائدة أخرى هي أنك تتفاعل بالفعل مع مصدر بيانات تم تدريبه على مجموعة واسعة من المعلومات، في حين أن التطبيق التقليدي قد يكون محدودًا بما هو موجود في قاعدة البيانات.

### ماذا يمكنني بناءه باستخدام تطبيق توليد النصوص؟

هناك العديد من الأشياء التي يمكنك بناءها. على سبيل المثال:

- **روبوت دردشة**. روبوت دردشة يجيب على الأسئلة حول موضوعات، مثل شركتك ومنتجاتها يمكن أن يكون مناسبًا جيدًا.
- **مساعد**. النماذج اللغوية الكبيرة (LLMs) ممتازة في أشياء مثل تلخيص النص، الحصول على رؤى من النص، إنتاج نص مثل السير الذاتية والمزيد.
- **مساعد كود**. اعتمادًا على نموذج اللغة الذي تستخدمه، يمكنك بناء مساعد كود يساعدك في كتابة الكود. على سبيل المثال، يمكنك استخدام منتج مثل GitHub Copilot وكذلك ChatGPT لمساعدتك في كتابة الكود.

## كيف يمكنني البدء؟

حسنًا، تحتاج إلى إيجاد طريقة للاندماج مع نموذج اللغة الكبير (LLM) والذي عادةً ما يتضمن النهجين التاليين:

- استخدام واجهة برمجة التطبيقات (API). هنا تقوم ببناء طلبات ويب مع الإرشادات الخاصة بك وتحصل على نص مولد.
- استخدام مكتبة. المكتبات تساعد في تغليف طلبات واجهة برمجة التطبيقات وتجعلها أسهل في الاستخدام.

## المكتبات/SDKs

هناك بعض المكتبات المعروفة للعمل مع نماذج اللغة الكبيرة مثل:

- **openai**، هذه المكتبة تجعل من السهل الاتصال بنموذجك وإرسال الإرشادات.

ثم هناك مكتبات تعمل على مستوى أعلى مثل:

- **Langchain**. Langchain معروف ويدعم Python.
- **Semantic Kernel**. Semantic Kernel هو مكتبة من Microsoft تدعم لغات C#، Python، وJava.

## التطبيق الأول باستخدام openai

لنرى كيف يمكننا بناء تطبيقنا الأول، ما المكتبات التي نحتاجها، كم هو مطلوب وما إلى ذلك.

### تثبيت openai

هناك العديد من المكتبات هناك للتفاعل مع OpenAI أو Azure OpenAI. من الممكن استخدام العديد من لغات البرمجة مثل C#، Python، JavaScript، Java والمزيد. لقد اخترنا استخدام مكتبة `openai` Python، لذلك سنستخدم `pip` لتثبيتها.

```bash
pip install openai
```

### إنشاء مورد

تحتاج إلى تنفيذ الخطوات التالية:

- إنشاء حساب على Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- الحصول على الوصول إلى Azure OpenAI. انتقل إلى [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) واطلب الوصول.

  > [!NOTE]
  > في وقت الكتابة، تحتاج إلى التقديم للحصول على الوصول إلى Azure OpenAI.

- تثبيت Python <https://www.python.org/>
- قم بإنشاء مورد خدمة Azure OpenAI. انظر هذا الدليل لكيفية [إنشاء مورد](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### تحديد مفتاح واجهة برمجة التطبيقات والنقطة النهائية

في هذه المرحلة، تحتاج إلى إخبار مكتبة `openai` الخاصة بك أي مفتاح واجهة برمجة التطبيقات يجب استخدامه. للعثور على مفتاح واجهة برمجة التطبيقات الخاص بك، انتقل إلى قسم "المفاتيح والنقطة النهائية" في مورد Azure OpenAI الخاص بك ونسخ قيمة "المفتاح 1".

![شاشة موارد المفاتيح والنقطة النهائية في بوابة Azure](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

الآن بعد أن حصلت على هذه المعلومات، دعنا نوجه المكتبات لاستخدامها.

> [!NOTE]
> من المفيد فصل مفتاح واجهة برمجة التطبيقات الخاص بك عن الكود. يمكنك القيام بذلك باستخدام متغيرات البيئة.
>
> - قم بتعيين متغير البيئة `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'`

### إعداد تكوين Azure

إذا كنت تستخدم Azure OpenAI، إليك كيفية إعداد التكوين:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

أعلاه نحن نحدد ما يلي:

- `api_type` to `azure`. This tells the library to use Azure OpenAI and not OpenAI.
- `api_key`, this is your API key found in the Azure Portal.
- `api_version`, this is the version of the API you want to use. At the time of writing, the latest version is `2023-05-15`.
- `api_base`, this is the endpoint of the API. You can find it in the Azure Portal next to your API key.

> [!NOTE] > `os.getenv` is a function that reads environment variables. You can use it to read environment variables like `OPENAI_API_KEY` and `API_BASE`. Set these environment variables in your terminal or by using a library like `dotenv`.

## Generate text

The way to generate text is to use the `Completion` class. إليك مثال:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

في الكود أعلاه، نقوم بإنشاء كائن إكمال ونمرر النموذج الذي نريد استخدامه والإرشادات. ثم نقوم بطباعة النص المولد.

### إكمالات الدردشة

حتى الآن، رأيت كيف كنا نستخدم `Completion` to generate text. But there's another class called `ChatCompletion` الذي يناسب أكثر روبوتات الدردشة. إليك مثال لاستخدامه:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

المزيد حول هذه الوظيفة في فصل قادم.

## تمرين - تطبيق توليد النصوص الأول الخاص بك

الآن بعد أن تعلمنا كيفية إعداد وتكوين openai، حان الوقت لبناء تطبيق توليد النصوص الأول الخاص بك. لبناء تطبيقك، اتبع هذه الخطوات:

1. قم بإنشاء بيئة افتراضية وتثبيت openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > إذا كنت تستخدم Windows، اكتب `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1` value.

1. قم بإنشاء ملف _app.py_ وأعطه الكود التالي:

   ```python
   import openai

   openai.api_key = "<replace this value with your open ai key or Azure OpenAI key>"

   openai.api_type = 'azure'
   openai.api_version = '2023-05-15'
   openai.api_base = "<endpoint found in Azure Portal where your API key is>"
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"
   messages = [{"role": "user", "content": prompt}]

   # make completion
   completion = openai.chat.completions.create(model=deployment_name, messages=messages)

   # print response
   print(completion.choices[0].message.content)
   ```

   > [!NOTE]
   > إذا كنت تستخدم Azure OpenAI، تحتاج إلى تعيين `api_type` to `azure` and set the `api_key` لمفتاح Azure OpenAI الخاص بك.

   يجب أن ترى إخراجًا مثل ما يلي:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## أنواع مختلفة من الإرشادات لأشياء مختلفة

الآن رأيت كيفية توليد النص باستخدام إرشادات. لديك حتى برنامج يعمل يمكنك تعديله وتغييره لتوليد أنواع مختلفة من النصوص.

يمكن استخدام الإرشادات لمهام مختلفة. على سبيل المثال:

- **توليد نوع من النص**. على سبيل المثال، يمكنك توليد قصيدة، أسئلة لاختبار وما إلى ذلك.
- **البحث عن معلومات**. يمكنك استخدام الإرشادات للبحث عن معلومات مثل المثال التالي "ماذا يعني CORS في تطوير الويب؟".
- **توليد الكود**. يمكنك استخدام الإرشادات لتوليد الكود، على سبيل المثال تطوير تعبير منتظم يستخدم للتحقق من صحة البريد الإلكتروني أو لماذا لا تولد برنامجًا كاملاً، مثل تطبيق ويب؟

## حالة استخدام أكثر عملية: مولد وصفات

تخيل أنك لديك مكونات في المنزل وتريد طهي شيء ما. لذلك، تحتاج إلى وصفة. إحدى الطرق للعثور على الوصفات هي استخدام محرك بحث أو يمكنك استخدام نموذج اللغة الكبير للقيام بذلك.

يمكنك كتابة إرشادات مثل:

> "أظهر لي 5 وصفات لطبق يحتوي على المكونات التالية: دجاج، بطاطس، وجزر. لكل وصفة، قم بإدراج جميع المكونات المستخدمة"

بالنظر إلى الإرشادات أعلاه، قد تحصل على استجابة مشابهة لـ:

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

هذه النتيجة رائعة، أعلم ماذا أطبخ. في هذه المرحلة، ما يمكن أن يكون تحسينات مفيدة هي:

- تصفية المكونات التي لا أحبها أو التي أعاني من حساسية تجاهها.
- إنتاج قائمة تسوق، في حالة عدم وجود جميع المكونات في المنزل.

للحالات المذكورة أعلاه، دعنا نضيف إرشادات إضافية:

> "يرجى إزالة الوصفات التي تحتوي على الثوم لأنني أعاني من حساسية واستبدالها بشيء آخر. أيضًا، يرجى إنتاج قائمة تسوق للوصفات، مع مراعاة أنني لدي بالفعل دجاج، بطاطس وجزر في المنزل."

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

هذه هي الوصفات الخمسة الخاصة بك، بدون ذكر الثوم ولديك أيضًا قائمة تسوق مع مراعاة ما لديك بالفعل في المنزل.

## تمرين - بناء مولد وصفات

الآن بعد أن لعبنا سيناريو، دعنا نكتب كودًا لمطابقة السيناريو الموضح. للقيام بذلك، اتبع هذه الخطوات:

1. استخدم الملف الحالي _app.py_ كنقطة بداية
1. حدد موقع متغير `prompt` وقم بتغيير الكود الخاص به إلى ما يلي:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   إذا قمت الآن بتشغيل الكود، يجب أن ترى إخراجًا مشابهًا لـ:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > ملاحظة، النموذج اللغوي الكبير غير محدد، لذا قد تحصل على نتائج مختلفة في كل مرة تقوم بتشغيل البرنامج.

   رائع، دعنا نرى كيف يمكننا تحسين الأمور. لتحسين الأمور، نريد التأكد من أن الكود مرن، لذلك يمكن تحسين وتغيير المكونات وعدد الوصفات.

1. دعنا نغير الكود بالطريقة التالية:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   يمكن أن يبدو اختبار الكود كما يلي:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### تحسين بإضافة فلتر وقائمة تسوق

لدينا الآن تطبيق يعمل قادر على إنتاج وصفات وهو مرن حيث يعتمد على مدخلات من المستخدم، سواء في عدد الوصفات ولكن أيضًا المكونات المستخدمة.

لتحسينه أكثر، نريد إضافة ما يلي:

- **تصفية المكونات**. نريد أن نكون قادرين على تصفية المكونات التي لا نحبها أو التي نعاني من حساسية تجاهها. لتحقيق هذا التغيير، يمكننا تعديل الإرشادات الحالية وإضافة شرط فلتر إلى نهايتها مثل:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  أعلاه، نضيف `{filter}` إلى نهاية الإرشادات ونلتقط أيضًا قيمة الفلتر من المستخدم.

  يمكن أن يبدو إدخال مثال لتشغيل البرنامج الآن كما يلي:

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

  كما ترى، تم تصفية أي وصفات تحتوي على الحليب. ولكن، إذا كنت تعاني من عدم تحمل اللاكتوز، فقد ترغب في تصفية الوصفات التي تحتوي على الجبن أيضًا، لذلك هناك حاجة إلى الوضوح.

- **إنتاج قائمة تسوق**. نريد إنتاج قائمة تسوق، مع مراعاة ما لدينا بالفعل في المنزل.

  لهذه الوظيفة، يمكننا إما محاولة حل كل شيء في إرشادات واحدة أو يمكننا تقسيمها إلى إرشاداتين. دعنا نحاول النهج الأخير. هنا نقترح إضافة إرشادات إضافية، ولكن لكي تعمل، نحتاج إلى إضافة نتيجة الإرشادات الأولى كالسياق للإرشادات الثانية.

  حدد الجزء في الكود الذي يطبع النتيجة من الإرشادات الأولى وأضف الكود التالي أدناه:

  ```python
  old_prompt_result = completion.choices[0].message.content
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  messages = [{"role": "user", "content": new_prompt}]
  completion = openai.Completion.create(engine=deployment_name, messages=messages, max_tokens=1200)

  # print response
  print("Shopping list:")
  print(completion.choices[0].message.content)
  ```

  لاحظ ما يلي:

  1. نحن نقوم ببناء إرشادات جديدة بإضافة النتيجة من الإرشادات الأولى إلى الإرشادات الجديدة:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. نقوم بعمل طلب جديد، ولكن أيضًا مع مراعاة عدد الرموز التي طلبناها في الإرشادات الأولى، لذلك هذه المرة نقول `max_tokens` هو 1200.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     أخذ هذا الكود لتجربة، الآن نصل إلى الإخراج التالي:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## تحسين الإعداد الخاص بك

ما لدينا حتى الآن هو كود يعمل، ولكن هناك بعض التعديلات التي يجب علينا القيام بها لتحسين الأمور أكثر. بعض الأشياء التي يجب علينا القيام بها هي:

- **فصل الأسرار عن الكود**، مثل مفتاح واجهة برمجة التطبيقات. الأسرار لا تنتمي إلى الكود ويجب تخزينها في مكان آمن. لفصل الأسرار عن الكود، يمكننا استخدام متغيرات البيئة والمكتبات مثل `python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env` file with the following content:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > ملاحظة، بالنسبة لـ Azure، تحتاج إلى تعيين متغيرات البيئة التالية:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     في الكود، يمكنك تحميل متغيرات البيئة كما يلي:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **كلمة حول طول الرموز**. يجب علينا مراعاة عدد الرموز التي نحتاجها لتوليد النص الذي نريده. الرموز تكلف مالاً، لذا حيثما أمكن، يجب علينا محاولة أن نكون اقتصاديين في عدد الرموز التي نستخدمها. على سبيل المثال، هل يمكننا صياغة الإرشادات بحيث يمكننا استخدام رموز أقل؟

  لتغيير الرموز المستخدمة، يمكنك استخدام معلمة `max_tokens`. على سبيل المثال، إذا كنت تريد استخدام 100 رمز، يمكنك القيام بـ:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **التجربة مع درجة الحرارة**. درجة الحرارة هي شيء لم نذكره حتى الآن ولكنها سياق مهم لأداء البرنامج الخاص بنا. كلما زادت قيمة درجة الحرارة، زادت عشوائية الإخراج. وعلى العكس، كلما قلت قيمة درجة الحرارة، كان الإخراج أكثر توقعًا. يجب مراعاة ما إذا كنت تريد تنوعًا في الإخراج أم لا.

  لتغيير درجة الحرارة، يمكنك استخدام معلمة `temperature`. على سبيل المثال، إذا كنت تريد استخدام درجة حرارة 0.5، يمكنك القيام بـ:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > ملاحظة، كلما اقتربت من 1.0، زاد تنوع الإخراج.

## الواجب

لهذا الواجب، يمكنك اختيار ما تريد بناءه.

إليك بعض الاقتراحات:

- قم بتعديل تطبيق مولد الوصفات لتحسينه أكثر. جرب اللعب بقيم درجة الحرارة، والإرشادات لترى ما يمكنك الخروج به.
- بناء "رفيق الدراسة". يجب أن يكون هذا التطبيق قادرًا على الإجابة عن الأسئلة حول موضوع مثل Python، يمكنك أن يكون لديك إرشادات مثل "ما هو موضوع معين في Python؟"، أو يمكنك أن يكون لديك إرشادات تقول، أرني كودًا لموضوع معين وما إلى ذلك.
- بوت التاريخ، اجعل التاريخ ينبض بالحياة، وجه البوت لتقمص شخصية تاريخية معينة واطرح عليه أسئلة حول حياته وأوقاته.

## الحل

### رفيق الدراسة

فيما يلي إرشادات البداية، انظر كيف يمكنك استخدامها وتعديلها حسب رغبتك.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### بوت التاريخ

إليك بعض الإرشادات التي يمكنك استخدامها:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## اختبار المعرفة

ماذا يفعل مفهوم درجة الحرارة؟

1. يتحكم في مدى عشوائية الإخراج.
1. يتحكم في مدى كبر الاستجابة.
1. يتحكم في عدد الرموز المستخدمة.

## 🚀 التحدي

عند العمل على الواجب، حاول تنويع درجة الحرارة، حاول ضبطها على 0، 0.5، و1. تذكر أن 0 هو الأقل تنوعًا و1 هو الأكثر، ما هي القيمة التي تعمل بشكل أفضل لتطبيقك؟

## عمل رائع! تابع تعلمك

بعد إكمال هذا الدرس، تحقق من [مجموعة تعلم الذكاء الاصطناعي التوليدي](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) لمواصلة تحسين معرفتك بالذكاء الاصطناعي التوليدي!

انتقل إلى الدرس 7 حيث سننظر في كيفية [بناء تطبيقات الدردشة](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

I'm sorry, but I'm not familiar with a language identified as "mo." Could you please specify the language you're referring to, or provide more context?