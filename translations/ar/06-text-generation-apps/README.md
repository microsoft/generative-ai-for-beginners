<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-05-19T16:39:01+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "ar"
}
-->
# بناء تطبيقات توليد النصوص

> _(انقر على الصورة أعلاه لمشاهدة فيديو هذه الدرس)_

لقد رأيت حتى الآن من خلال هذا المنهج الدراسي أن هناك مفاهيم أساسية مثل المحفزات وحتى مجال كامل يسمى "هندسة المحفزات". العديد من الأدوات التي يمكنك التفاعل معها مثل ChatGPT و Office 365 و Microsoft Power Platform وغيرها، تدعمك باستخدام المحفزات لتحقيق شيء ما.

لإضافة مثل هذه التجربة إلى تطبيق، تحتاج إلى فهم مفاهيم مثل المحفزات، الإكمالات واختيار مكتبة للعمل معها. هذا بالضبط ما ستتعلمه في هذا الفصل.

## مقدمة

في هذا الفصل، سوف:

- تتعرف على مكتبة openai ومفاهيمها الأساسية.
- تبني تطبيق توليد نصوص باستخدام openai.
- تفهم كيفية استخدام مفاهيم مثل المحفز، الحرارة، والرموز لبناء تطبيق توليد نصوص.

## أهداف التعلم

في نهاية هذا الدرس، ستكون قادرًا على:

- شرح ما هو تطبيق توليد النصوص.
- بناء تطبيق توليد نصوص باستخدام openai.
- تكوين تطبيقك لاستخدام المزيد أو القليل من الرموز وأيضًا تغيير الحرارة، للحصول على نتائج متنوعة.

## ما هو تطبيق توليد النصوص؟

عادةً عندما تبني تطبيقًا، يكون لديه نوع من الواجهة مثل ما يلي:

- قائم على الأوامر. التطبيقات القائمة على وحدة التحكم هي تطبيقات تقليدية حيث تكتب أمرًا وينفذ مهمة. على سبيل المثال، `git` هو تطبيق قائم على الأوامر.
- واجهة المستخدم (UI). بعض التطبيقات لديها واجهات مستخدم رسومية (GUIs) حيث تضغط على الأزرار، تدخل النص، تختار الخيارات وأكثر.

### تطبيقات وحدة التحكم وواجهة المستخدم محدودة

قارنها بتطبيق قائم على الأوامر حيث تكتب أمرًا:

- **إنه محدود**. لا يمكنك كتابة أي أمر، فقط الأوامر التي يدعمها التطبيق.
- **محدد باللغة**. بعض التطبيقات تدعم العديد من اللغات، لكن افتراضيًا يتم بناء التطبيق للغة معينة، حتى إذا كان بإمكانك إضافة دعم للغات أخرى.

### فوائد تطبيقات توليد النصوص

إذًا، كيف يختلف تطبيق توليد النصوص؟

في تطبيق توليد النصوص، لديك المزيد من المرونة، لا تكون محدودًا بمجموعة من الأوامر أو لغة إدخال معينة. بدلاً من ذلك، يمكنك استخدام اللغة الطبيعية للتفاعل مع التطبيق. فائدة أخرى هي أنك تتفاعل بالفعل مع مصدر بيانات تم تدريبه على مجموعة كبيرة من المعلومات، بينما قد يكون التطبيق التقليدي محدودًا بما في قاعدة البيانات.

### ماذا يمكنني بناءه باستخدام تطبيق توليد النصوص؟

هناك العديد من الأشياء التي يمكنك بناءها. على سبيل المثال:

- **روبوت محادثة**. يمكن أن يكون روبوت محادثة يجيب على الأسئلة حول مواضيع، مثل شركتك ومنتجاتها، ملائمًا.
- **مساعد**. النماذج اللغوية الكبيرة (LLMs) رائعة في أشياء مثل تلخيص النصوص، الحصول على رؤى من النصوص، إنتاج نصوص مثل السير الذاتية وأكثر.
- **مساعد برمجي**. اعتمادًا على نموذج اللغة الذي تستخدمه، يمكنك بناء مساعد برمجي يساعدك في كتابة الشفرات. على سبيل المثال، يمكنك استخدام منتج مثل GitHub Copilot وكذلك ChatGPT لمساعدتك في كتابة الشفرات.

## كيف يمكنني البدء؟

حسنًا، تحتاج إلى إيجاد طريقة للاندماج مع نموذج لغوي كبير (LLM) الذي يتضمن عادةً النهجين التاليين:

- استخدام API. هنا تقوم ببناء طلبات ويب مع محفزك وتحصل على نص مولد.
- استخدام مكتبة. المكتبات تساعد في تغليف استدعاءات API وتجعلها أسهل في الاستخدام.

## المكتبات/حزم تطوير البرمجيات (SDKs)

هناك بعض المكتبات المعروفة للعمل مع النماذج اللغوية الكبيرة مثل:

- **openai**، هذه المكتبة تجعل من السهل الاتصال بنموذجك وإرسال المحفزات.

ثم هناك مكتبات تعمل على مستوى أعلى مثل:

- **Langchain**. لانغتشين معروفة وتدعم بايثون.
- **Semantic Kernel**. النواة الدلالية هي مكتبة من مايكروسوفت تدعم لغات C#، بايثون، وجافا.

## التطبيق الأول باستخدام openai

لنرى كيف يمكننا بناء تطبيقنا الأول، ما هي المكتبات التي نحتاجها، وما هو المطلوب وما إلى ذلك.

### تثبيت openai

هناك العديد من المكتبات للتفاعل مع OpenAI أو Azure OpenAI. من الممكن استخدام العديد من لغات البرمجة مثل C#، بايثون، جافا سكريبت، جافا وأكثر. لقد اخترنا استخدام مكتبة `openai` بايثون، لذلك سنستخدم `pip` لتثبيتها.

```bash
pip install openai
```

### إنشاء مورد

تحتاج إلى تنفيذ الخطوات التالية:

- إنشاء حساب على Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- الحصول على الوصول إلى Azure OpenAI. اذهب إلى [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) واطلب الوصول.

  > [!NOTE]
  > في وقت كتابة هذا، تحتاج إلى التقديم للحصول على الوصول إلى Azure OpenAI.

- تثبيت بايثون <https://www.python.org/>
- أنشئ مورد خدمة Azure OpenAI. راجع هذا الدليل لكيفية [إنشاء مورد](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### تحديد مفتاح API ونقطة النهاية

في هذه المرحلة، تحتاج إلى إخبار مكتبة `openai` الخاصة بك بمفتاح API الذي ستستخدمه. للعثور على مفتاح API الخاص بك، اذهب إلى قسم "المفاتيح ونقطة النهاية" في مورد Azure OpenAI الخاص بك ونسخ قيمة "المفتاح 1".

![لوحة موارد المفاتيح ونقطة النهاية في بوابة Azure](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

الآن بعد أن قمت بنسخ هذه المعلومات، دعنا نوجه المكتبات لاستخدامها.

> [!NOTE]
> من المفيد فصل مفتاح API الخاص بك عن الكود. يمكنك القيام بذلك باستخدام متغيرات البيئة.
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

أعلاه نقوم بتعيين ما يلي:

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

في الكود أعلاه، نقوم بإنشاء كائن إكمال ونمرر النموذج الذي نريد استخدامه والمحفز. ثم نطبع النص المولد.

### إكمالات الدردشة

حتى الآن، لقد رأيت كيف كنا نستخدم `Completion` to generate text. But there's another class called `ChatCompletion` الذي يناسب أكثر لروبوتات الدردشة. إليك مثال على استخدامه:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

المزيد حول هذه الوظيفة في فصل قادم.

## تمرين - تطبيقك الأول لتوليد النصوص

الآن بعد أن تعلمنا كيفية إعداد وتكوين openai، حان الوقت لبناء تطبيقك الأول لتوليد النصوص. لبناء تطبيقك، اتبع هذه الخطوات:

1. أنشئ بيئة افتراضية وقم بتثبيت openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > إذا كنت تستخدم ويندوز اكتب `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1` value.

1. أنشئ ملف _app.py_ وأعطه الكود التالي:

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
   > إذا كنت تستخدم Azure OpenAI، تحتاج إلى تعيين `api_type` to `azure` and set the `api_key` إلى مفتاح Azure OpenAI الخاص بك.

   يجب أن ترى ناتجًا يشبه ما يلي:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## أنواع مختلفة من المحفزات، لأشياء مختلفة

الآن لقد رأيت كيفية توليد النصوص باستخدام محفز. لديك حتى برنامج قيد التشغيل يمكنك تعديله وتغييره لتوليد أنواع مختلفة من النصوص.

يمكن استخدام المحفزات لمهام متنوعة. على سبيل المثال:

- **توليد نوع من النصوص**. على سبيل المثال، يمكنك توليد قصيدة، أسئلة لاختبار وغيرها.
- **البحث عن المعلومات**. يمكنك استخدام المحفزات للبحث عن معلومات مثل المثال التالي "ماذا يعني CORS في تطوير الويب؟".
- **توليد الشفرة**. يمكنك استخدام المحفزات لتوليد الشفرة، على سبيل المثال تطوير تعبير عادي يستخدم للتحقق من صحة البريد الإلكتروني أو لماذا لا تولد برنامجًا كاملًا، مثل تطبيق ويب؟

## حالة استخدام أكثر عملية: مولد الوصفات

تخيل أن لديك مكونات في المنزل وتريد طهي شيء ما. لذلك، تحتاج إلى وصفة. طريقة للعثور على الوصفات هي استخدام محرك بحث أو يمكنك استخدام نموذج لغوي كبير للقيام بذلك.

يمكنك كتابة محفز مثل:

> "أظهر لي 5 وصفات لطبق بالمكونات التالية: الدجاج، البطاطس، والجزر. لكل وصفة، قم بسرد جميع المكونات المستخدمة"

بالنظر إلى المحفز أعلاه، قد تحصل على استجابة مشابهة لـ:

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

هذه النتيجة رائعة، أعرف ما سأطبخه. في هذه المرحلة، ما يمكن أن يكون تحسينات مفيدة هي:

- تصفية المكونات التي لا أحبها أو لدي حساسية منها.
- إنتاج قائمة تسوق، في حالة عدم توفر جميع المكونات لدي في المنزل.

بالنسبة للحالات أعلاه، دعونا نضيف محفزًا إضافيًا:

> "يرجى إزالة الوصفات التي تحتوي على الثوم لأنني لدي حساسية واستبدالها بشيء آخر. أيضًا، يرجى إنتاج قائمة تسوق للوصفات، مع مراعاة أن لدي بالفعل الدجاج، البطاطس والجزر في المنزل."

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

هذه هي وصفاتك الخمس، بدون ذكر الثوم ولديك أيضًا قائمة تسوق بالنظر إلى ما لديك بالفعل في المنزل.

## تمرين - بناء مولد الوصفات

الآن بعد أن لعبنا سيناريو، دعونا نكتب كودًا لمطابقة السيناريو الموضح. للقيام بذلك، اتبع هذه الخطوات:

1. استخدم ملف _app.py_ الحالي كنقطة انطلاق
1. حدد موقع متغير `prompt` وقم بتغيير كوده إلى ما يلي:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   إذا قمت الآن بتشغيل الكود، يجب أن ترى ناتجًا مشابهًا لـ:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > ملاحظة، نموذج اللغة الخاص بك غير حتمي، لذا قد تحصل على نتائج مختلفة في كل مرة تقوم بتشغيل البرنامج.

   رائع، دعونا نرى كيف يمكننا تحسين الأمور. لتحسين الأمور، نريد التأكد من أن الكود مرن، بحيث يمكن تحسين وتغيير المكونات وعدد الوصفات.

1. دعونا نغير الكود بالطريقة التالية:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   يمكن أن تبدو عملية اختبار الكود مثل:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### تحسين بإضافة فلتر وقائمة تسوق

لدينا الآن تطبيق يعمل قادر على إنتاج الوصفات وهو مرن لأنه يعتمد على المدخلات من المستخدم، سواء في عدد الوصفات أو أيضًا في المكونات المستخدمة.

لتحسينه أكثر، نريد إضافة ما يلي:

- **تصفية المكونات**. نريد أن نكون قادرين على تصفية المكونات التي لا نحبها أو لدينا حساسية منها. لتحقيق هذا التغيير، يمكننا تعديل محفزنا الحالي وإضافة شرط فلتر إلى نهايته كما يلي:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  أعلاه، نضيف `{filter}` إلى نهاية المحفز ونلتقط أيضًا قيمة الفلتر من المستخدم.

  يمكن أن يبدو إدخال مثال لتشغيل البرنامج الآن مثل:

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

  كما ترى، أي وصفات تحتوي على الحليب تم تصفيتها. ولكن، إذا كنت تعاني من عدم تحمل اللاكتوز، فقد ترغب في تصفية الوصفات التي تحتوي على الجبن أيضًا، لذا هناك حاجة إلى الوضوح.

- **إنتاج قائمة تسوق**. نريد إنتاج قائمة تسوق، مع مراعاة ما لدينا بالفعل في المنزل.

  بالنسبة لهذه الوظيفة، يمكننا إما محاولة حل كل شيء في محفز واحد أو يمكننا تقسيمه إلى محفزين. دعونا نحاول النهج الأخير. هنا نقترح إضافة محفز إضافي، ولكن لكي يعمل ذلك، نحتاج إلى إضافة نتيجة المحفز السابق كجزء من السياق للمحفز اللاحق.

  حدد الجزء في الكود الذي يطبع النتيجة من المحفز الأول وأضف الكود التالي أدناه:

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

  1. نحن نقوم ببناء محفز جديد عن طريق إضافة نتيجة المحفز الأول إلى المحفز الجديد:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. نقوم بعمل طلب جديد، ولكن مع مراعاة عدد الرموز التي طلبناها في المحفز الأول، لذا نقول هذه المرة أن `max_tokens` هي 1200.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     عند اختبار هذا الكود، نصل الآن إلى الناتج التالي:

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

ما لدينا حتى الآن هو كود يعمل، ولكن هناك بعض التحسينات التي يجب أن نقوم بها لتحسين الأمور أكثر. بعض الأشياء التي يجب القيام بها هي:

- **فصل الأسرار عن الكود**، مثل مفتاح API. الأسرار لا تنتمي إلى الكود ويجب تخزينها في موقع آمن. لفصل الأسرار عن الكود، يمكننا استخدام متغيرات البيئة ومكتبات مثل `python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env` file مع المحتوى التالي:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > ملاحظة، بالنسبة لأزور، تحتاج إلى تعيين متغيرات البيئة التالية:

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

- **كلمة حول طول الرموز**. يجب أن نأخذ بعين الاعتبار عدد الرموز التي نحتاجها لتوليد النص الذي نريده. الرموز تكلف مالًا، لذا حيثما كان ذلك ممكنًا، يجب أن نحاول أن نكون اقتصاديين في عدد الرموز التي نستخدمها. على سبيل المثال، هل يمكننا صياغة المحفز بحيث يمكننا استخدام رموز أقل؟

  لتغيير الرموز المستخدمة، يمكنك استخدام المعلمة `max_tokens`. على سبيل المثال، إذا كنت تريد استخدام 100 رمز، يمكنك القيام بـ:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **التجربة مع الحرارة**. الحرارة هي شيء لم نذكره حتى الآن ولكنها سياق مهم لكيفية أداء برنامجنا. كلما زادت قيمة الحرارة، كلما كان الناتج عشوائيًا أكثر. وعلى العكس، كلما انخفضت قيمة الحرارة، كلما كان الناتج متوقعًا أكثر. فكر فيما إذا كنت تريد التنوع في الناتج أم لا.

  لتغيير الحرارة، يمكنك استخدام المعلمة `temperature`. على سبيل المثال، إذا كنت تريد استخدام حرارة بقيمة 0.5، يمكنك القيام بـ:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > ملاحظة، كلما اقتربت من 1.0، كلما كان الناتج أكثر تنوعًا.

## واجب

لهذا الواجب، يمكنك اختيار ما تريد بناءه.

إليك بعض الاقتراحات:

- تعديل تطبيق مولد الوصفات لتحسينه أكثر. جرب اللعب مع قيم الحرارة والمحفزات لترى ما يمكنك الخروج به.
- بناء "رفيق دراسة". يجب أن يكون هذا التطبيق قادرًا على الإجابة على الأسئلة حول موضوع معين مثل بايثون، يمكنك أن يكون لديك محفزات مثل "ما هو موضوع معين في بايثون؟"، أو يمكنك أن يكون لديك محفز يقول، أظهر لي شفرة لموضوع معين وغيرها.
- روبوت تاريخي، اجعل التاريخ ينبض بالحياة، وجه الروبوت للعب دور شخصية تاريخية معينة واطرح عليه الأسئلة حول حياته وأوقاته.

## الحل

### رفيق الدراسة

فيما يلي محفز بدء، انظر كيف يمكنك استخدامه وتعديله حسب رغبتك.

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

ماذا يفعل مفهوم الحرارة؟

1. يتحكم في مدى عشوائية الناتج.
1. يتحكم في حجم الاستجابة.
1. يتحكم في عدد الرموز المستخدمة.

## 🚀 تحدي

عند العمل على الواجب، حاول تنويع الحرارة، حاول ضبطها على 0، 0.5، و 1. تذكر أن 0 هو الأقل تنوعًا و1 هو الأكثر، ما هي القيمة التي تعمل بشكل أفضل لتطبيقك؟

## عمل رائع! تابع تعلمك

بعد إكمال هذا الدرس، تحقق من مجموعة [تعلم الذكاء الاصطناعي التوليدي](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) لمواصلة تعزيز معرفتك في الذكاء الاصطناعي التوليدي!

توجه إلى الدرس السابع حيث سننظر في كيفية [بناء تطبيقات الدردشة](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**إخلاء المسؤولية**:  
تمت ترجمة هذه الوثيقة باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى جاهدين لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار الوثيقة الأصلية بلغتها الأم هي المصدر الموثوق. للحصول على معلومات هامة، يوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ينشأ عن استخدام هذه الترجمة.