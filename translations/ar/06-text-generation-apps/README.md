<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00e33cd3ff945511446ecda4a9f8a828",
  "translation_date": "2025-10-17T12:56:25+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "ar"
}
-->
# بناء تطبيقات توليد النصوص

[![بناء تطبيقات توليد النصوص](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.ar.png)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(اضغط على الصورة أعلاه لمشاهدة فيديو الدرس)_

لقد رأيت حتى الآن من خلال هذا المنهج أن هناك مفاهيم أساسية مثل المطالبات وحتى مجال كامل يسمى "هندسة المطالبات". العديد من الأدوات التي يمكنك التفاعل معها مثل ChatGPT، Office 365، Microsoft Power Platform وغيرها، تدعم استخدامك للمطالبات لتحقيق شيء ما.

لكي تضيف مثل هذه التجربة إلى تطبيق، تحتاج إلى فهم مفاهيم مثل المطالبات، الإكمالات واختيار مكتبة للعمل معها. هذا بالضبط ما ستتعلمه في هذا الفصل.

## المقدمة

في هذا الفصل، ستتعلم:

- عن مكتبة openai ومفاهيمها الأساسية.
- بناء تطبيق لتوليد النصوص باستخدام openai.
- فهم كيفية استخدام مفاهيم مثل المطالبات، درجة الحرارة، والرموز لبناء تطبيق لتوليد النصوص.

## أهداف التعلم

في نهاية هذا الدرس، ستكون قادرًا على:

- شرح ما هو تطبيق توليد النصوص.
- بناء تطبيق لتوليد النصوص باستخدام openai.
- ضبط تطبيقك لاستخدام عدد أكبر أو أقل من الرموز وتغيير درجة الحرارة للحصول على نتائج متنوعة.

## ما هو تطبيق توليد النصوص؟

عادةً عندما تبني تطبيقًا، يكون لديه نوع من الواجهة مثل التالي:

- يعتمد على الأوامر. التطبيقات القائمة على الكونسول هي تطبيقات نموذجية حيث تكتب أمرًا ويتم تنفيذ مهمة. على سبيل المثال، `git` هو تطبيق يعتمد على الأوامر.
- واجهة المستخدم (UI). بعض التطبيقات لديها واجهات مستخدم رسومية (GUIs) حيث تنقر على الأزرار، تدخل النصوص، تختار الخيارات والمزيد.

### التطبيقات القائمة على الكونسول وواجهة المستخدم محدودة

قارن ذلك بتطبيق يعتمد على الأوامر حيث تكتب أمرًا:

- **محدود**. لا يمكنك كتابة أي أمر، فقط الأوامر التي يدعمها التطبيق.
- **خاص باللغة**. بعض التطبيقات تدعم العديد من اللغات، ولكن بشكل افتراضي يتم بناء التطبيق بلغة محددة، حتى لو كان بإمكانك إضافة دعم للغات أخرى.

### فوائد تطبيقات توليد النصوص

إذن كيف يختلف تطبيق توليد النصوص؟

في تطبيق توليد النصوص، لديك المزيد من المرونة، فأنت لست محدودًا بمجموعة من الأوامر أو لغة إدخال محددة. بدلاً من ذلك، يمكنك استخدام اللغة الطبيعية للتفاعل مع التطبيق. فائدة أخرى هي أنك تتفاعل بالفعل مع مصدر بيانات تم تدريبه على مجموعة ضخمة من المعلومات، بينما قد يكون التطبيق التقليدي محدودًا بما هو موجود في قاعدة البيانات.

### ماذا يمكنني أن أبني باستخدام تطبيق توليد النصوص؟

هناك العديد من الأشياء التي يمكنك بناؤها. على سبيل المثال:

- **روبوت دردشة**. روبوت دردشة يجيب على الأسئلة حول مواضيع مثل شركتك ومنتجاتها يمكن أن يكون مناسبًا.
- **مساعد**. النماذج اللغوية الكبيرة (LLMs) رائعة في أشياء مثل تلخيص النصوص، الحصول على رؤى من النصوص، إنتاج نصوص مثل السير الذاتية والمزيد.
- **مساعد برمجي**. اعتمادًا على نموذج اللغة الذي تستخدمه، يمكنك بناء مساعد برمجي يساعدك في كتابة الكود. على سبيل المثال، يمكنك استخدام منتج مثل GitHub Copilot وكذلك ChatGPT لمساعدتك في كتابة الكود.

## كيف يمكنني البدء؟

حسنًا، تحتاج إلى إيجاد طريقة للتكامل مع نموذج لغوي كبير (LLM) والذي يتطلب عادةً النهجين التاليين:

- استخدام واجهة برمجة التطبيقات (API). هنا تقوم بإنشاء طلبات ويب مع مطالبتك وتحصل على نصوص مولدة.
- استخدام مكتبة. المكتبات تساعد في تغليف طلبات واجهة برمجة التطبيقات وتجعلها أسهل في الاستخدام.

## المكتبات/SDKs

هناك بعض المكتبات المعروفة للعمل مع النماذج اللغوية الكبيرة مثل:

- **openai**، هذه المكتبة تجعل من السهل الاتصال بنموذجك وإرسال المطالبات.

ثم هناك مكتبات تعمل على مستوى أعلى مثل:

- **Langchain**. Langchain معروفة وتدعم لغة Python.
- **Semantic Kernel**. Semantic Kernel هي مكتبة من Microsoft تدعم لغات C#، Python، وJava.

## أول تطبيق باستخدام openai

لنرى كيف يمكننا بناء أول تطبيق لنا، ما هي المكتبات التي نحتاجها، وما هو المطلوب.

### تثبيت openai

هناك العديد من المكتبات للتفاعل مع OpenAI أو Azure OpenAI. من الممكن استخدام العديد من لغات البرمجة مثل C#، Python، JavaScript، Java والمزيد. اخترنا استخدام مكتبة Python `openai`، لذا سنستخدم `pip` لتثبيتها.

```bash
pip install openai
```

### إنشاء مورد

تحتاج إلى تنفيذ الخطوات التالية:

- إنشاء حساب على Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- الحصول على الوصول إلى Azure OpenAI. انتقل إلى [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) واطلب الوصول.

  > [!NOTE]
  > في وقت كتابة هذا النص، تحتاج إلى التقدم للحصول على الوصول إلى Azure OpenAI.

- تثبيت Python <https://www.python.org/>
- إنشاء مورد خدمة Azure OpenAI. راجع هذا الدليل حول كيفية [إنشاء مورد](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### تحديد مفتاح API ونقطة النهاية

في هذه المرحلة، تحتاج إلى إخبار مكتبة `openai` بمفتاح API الذي ستستخدمه. للعثور على مفتاح API الخاص بك، انتقل إلى قسم "Keys and Endpoint" في مورد Azure OpenAI الخاص بك ونسخ قيمة "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

الآن بعد أن قمت بنسخ هذه المعلومات، دعنا نوجه المكتبات لاستخدامها.

> [!NOTE]
> من المفيد فصل مفتاح API الخاص بك عن الكود الخاص بك. يمكنك القيام بذلك باستخدام متغيرات البيئة.
>
> - قم بتعيين متغير البيئة `OPENAI_API_KEY` إلى مفتاح API الخاص بك.
>   `export OPENAI_API_KEY='sk-...'`

### إعداد تكوين Azure

إذا كنت تستخدم Azure OpenAI، إليك كيفية إعداد التكوين:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

في الأعلى، نحن نحدد التالي:

- `api_type` إلى `azure`. هذا يخبر المكتبة باستخدام Azure OpenAI وليس OpenAI.
- `api_key`، هذا هو مفتاح API الخاص بك الموجود في بوابة Azure.
- `api_version`، هذا هو إصدار API الذي تريد استخدامه. في وقت كتابة هذا النص، أحدث إصدار هو `2023-05-15`.
- `api_base`، هذا هو نقطة النهاية لـ API. يمكنك العثور عليه في بوابة Azure بجانب مفتاح API الخاص بك.

> [!NOTE] > `os.getenv` هي وظيفة تقرأ متغيرات البيئة. يمكنك استخدامها لقراءة متغيرات البيئة مثل `OPENAI_API_KEY` و`API_BASE`. قم بتعيين هذه المتغيرات في بيئة العمل الخاصة بك أو باستخدام مكتبة مثل `dotenv`.

## توليد النصوص

الطريقة لتوليد النصوص هي استخدام فئة `Completion`. إليك مثال:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

في الكود أعلاه، نقوم بإنشاء كائن إكمال ونمرر النموذج الذي نريد استخدامه والمطالبة. ثم نقوم بطباعة النص المولد.

### إكمالات الدردشة

حتى الآن، رأيت كيف نستخدم `Completion` لتوليد النصوص. ولكن هناك فئة أخرى تسمى `ChatCompletion` وهي أكثر ملاءمة لروبوتات الدردشة. إليك مثال على استخدامها:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

المزيد عن هذه الوظيفة في فصل قادم.

## تمرين - أول تطبيق لتوليد النصوص

الآن بعد أن تعلمنا كيفية إعداد وتكوين openai، حان الوقت لبناء أول تطبيق لتوليد النصوص. لبناء التطبيق، اتبع الخطوات التالية:

1. قم بإنشاء بيئة افتراضية وقم بتثبيت openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > إذا كنت تستخدم Windows، اكتب `venv\Scripts\activate` بدلاً من `source venv/bin/activate`.

   > [!NOTE]
   > حدد مفتاح Azure OpenAI الخاص بك بالانتقال إلى [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) وابحث عن `Open AI` واختر مورد `Open AI` ثم اختر `Keys and Endpoint` ونسخ قيمة `Key 1`.

1. قم بإنشاء ملف _app.py_ وأضف إليه الكود التالي:

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
   > إذا كنت تستخدم Azure OpenAI، تحتاج إلى تعيين `api_type` إلى `azure` وتعيين `api_key` إلى مفتاح Azure OpenAI الخاص بك.

   يجب أن ترى نتيجة مثل التالية:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## أنواع مختلفة من المطالبات لأغراض مختلفة

الآن رأيت كيفية توليد النصوص باستخدام مطالبة. لديك حتى برنامج يعمل يمكنك تعديله وتغييره لتوليد أنواع مختلفة من النصوص.

يمكن استخدام المطالبات لمهام متعددة. على سبيل المثال:

- **توليد نوع معين من النصوص**. على سبيل المثال، يمكنك توليد قصيدة، أسئلة لاختبار، إلخ.
- **البحث عن معلومات**. يمكنك استخدام المطالبات للبحث عن معلومات مثل المثال التالي "ما معنى CORS في تطوير الويب؟".
- **توليد الكود**. يمكنك استخدام المطالبات لتوليد الكود، على سبيل المثال تطوير تعبير منتظم يستخدم للتحقق من صحة البريد الإلكتروني أو حتى توليد برنامج كامل، مثل تطبيق ويب.

## استخدام عملي أكثر: مولد وصفات

تخيل أن لديك مكونات في المنزل وتريد طهي شيء ما. لهذا، تحتاج إلى وصفة. إحدى الطرق للعثور على الوصفات هي استخدام محرك بحث أو يمكنك استخدام نموذج لغوي كبير للقيام بذلك.

يمكنك كتابة مطالبة مثل:

> "أظهر لي 5 وصفات لطبق يحتوي على المكونات التالية: دجاج، بطاطس، وجزر. لكل وصفة، قم بإدراج جميع المكونات المستخدمة."

بالنظر إلى المطالبة أعلاه، قد تحصل على استجابة مشابهة لـ:

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

هذه النتيجة رائعة، الآن أعرف ماذا أطبخ. في هذه المرحلة، ما يمكن أن يكون تحسينات مفيدة هي:

- تصفية المكونات التي لا أحبها أو لدي حساسية منها.
- إنتاج قائمة تسوق، في حال لم يكن لدي جميع المكونات في المنزل.

بالنسبة للحالات أعلاه، دعنا نضيف مطالبة إضافية:

> "يرجى إزالة الوصفات التي تحتوي على الثوم لأنني لدي حساسية واستبداله بشيء آخر. أيضًا، يرجى إنتاج قائمة تسوق للوصفات، مع الأخذ في الاعتبار أنني لدي بالفعل دجاج، بطاطس وجزر في المنزل."

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

هذه هي الوصفات الخمس الخاصة بك، بدون ذكر الثوم، ولديك أيضًا قائمة تسوق تأخذ في الاعتبار ما لديك بالفعل في المنزل.

## تمرين - بناء مولد وصفات

الآن بعد أن قمنا بتوضيح سيناريو، دعنا نكتب كودًا يتوافق مع السيناريو الموضح. للقيام بذلك، اتبع الخطوات التالية:

1. استخدم ملف _app.py_ الحالي كنقطة انطلاق.
1. حدد متغير `prompt` وقم بتغيير الكود الخاص به إلى التالي:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   إذا قمت الآن بتشغيل الكود، يجب أن ترى نتيجة مشابهة لـ:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > ملاحظة، النموذج اللغوي الخاص بك غير حتمي، لذا قد تحصل على نتائج مختلفة في كل مرة تقوم فيها بتشغيل البرنامج.

   رائع، دعنا نرى كيف يمكننا تحسين الأمور. لتحسين الأمور، نريد التأكد من أن الكود مرن، بحيث يمكن تحسين وتغيير المكونات وعدد الوصفات.

1. دعنا نغير الكود بالطريقة التالية:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   تشغيل الكود لاختباره، قد يبدو كالتالي:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### تحسين بإضافة فلتر وقائمة تسوق

لدينا الآن تطبيق يعمل قادر على إنتاج الوصفات وهو مرن لأنه يعتمد على مدخلات المستخدم، سواء في عدد الوصفات أو المكونات المستخدمة.

لتحسينه أكثر، نريد إضافة التالي:

- **تصفية المكونات**. نريد أن نكون قادرين على تصفية المكونات التي لا نحبها أو لدينا حساسية منها. لتحقيق هذا التغيير، يمكننا تعديل المطالبة الحالية وإضافة شرط تصفية في نهايتها مثل التالي:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  أعلاه، نضيف `{filter}` إلى نهاية المطالبة ونلتقط أيضًا قيمة الفلتر من المستخدم.

  يمكن أن يبدو إدخال مثال لتشغيل البرنامج الآن كالتالي:

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

  كما ترى، تم تصفية أي وصفات تحتوي على الحليب. ولكن، إذا كنت تعاني من عدم تحمل اللاكتوز، قد ترغب في تصفية الوصفات التي تحتوي على الجبن أيضًا، لذا هناك حاجة إلى الوضوح.

- **إنتاج قائمة تسوق**. نريد إنتاج قائمة تسوق، مع الأخذ في الاعتبار ما لدينا بالفعل في المنزل.

  بالنسبة لهذه الوظيفة، يمكننا إما محاولة حل كل شيء في مطالبة واحدة أو يمكننا تقسيمها إلى مطالبتين. دعنا نجرب النهج الأخير. هنا نقترح إضافة مطالبة إضافية، ولكن لكي تعمل، نحتاج إلى إضافة نتيجة المطالبة السابقة كالسياق للمطالبة التالية.
ابحث عن الجزء في الكود الذي يطبع النتيجة من الطلب الأول وأضف الكود التالي أدناه:

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

1. نحن نقوم بإنشاء طلب جديد عن طريق إضافة النتيجة من الطلب الأول إلى الطلب الجديد:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

1. نقوم بعمل طلب جديد، ولكن مع الأخذ في الاعتبار عدد الرموز التي طلبناها في الطلب الأول، لذا هذه المرة نقول `max_tokens` هو 1200.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

عند تجربة هذا الكود، نحصل الآن على النتيجة التالية:

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

ما لدينا حتى الآن هو كود يعمل، ولكن هناك بعض التعديلات التي يجب أن نقوم بها لتحسين الأمور أكثر. بعض الأشياء التي يجب القيام بها هي:

- **فصل الأسرار عن الكود**، مثل مفتاح API. الأسرار لا تنتمي إلى الكود ويجب تخزينها في مكان آمن. لفصل الأسرار عن الكود، يمكننا استخدام متغيرات البيئة ومكتبات مثل `python-dotenv` لتحميلها من ملف. إليك كيف يبدو ذلك في الكود:

  1. قم بإنشاء ملف `.env` بالمحتوى التالي:

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

- **كلمة عن طول الرموز**. يجب أن نأخذ في الاعتبار عدد الرموز التي نحتاجها لإنشاء النص الذي نريده. الرموز تكلف المال، لذا حيثما أمكن، يجب أن نحاول أن نكون اقتصاديين في عدد الرموز التي نستخدمها. على سبيل المثال، هل يمكننا صياغة الطلب بحيث نستخدم عددًا أقل من الرموز؟

  لتغيير الرموز المستخدمة، يمكنك استخدام معامل `max_tokens`. على سبيل المثال، إذا كنت تريد استخدام 100 رمز، يمكنك القيام بذلك:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **التجربة مع درجة الحرارة**. درجة الحرارة هي شيء لم نذكره حتى الآن ولكنه سياق مهم لكيفية أداء برنامجنا. كلما زادت قيمة درجة الحرارة، كلما كان الناتج أكثر عشوائية. وعلى العكس، كلما قلت قيمة درجة الحرارة، كلما كان الناتج أكثر توقعًا. فكر فيما إذا كنت تريد تنوعًا في الناتج أم لا.

  لتغيير درجة الحرارة، يمكنك استخدام معامل `temperature`. على سبيل المثال، إذا كنت تريد استخدام درجة حرارة 0.5، يمكنك القيام بذلك:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > ملاحظة، كلما اقتربت من 1.0، كلما كان الناتج أكثر تنوعًا.

## المهمة

بالنسبة لهذه المهمة، يمكنك اختيار ما تريد بناءه.

إليك بعض الاقتراحات:

- قم بتعديل تطبيق مولد الوصفات لتحسينه أكثر. جرب قيم درجة الحرارة، والطلبات لترى ما يمكنك التوصل إليه.
- قم ببناء "زميل دراسة". يجب أن يكون هذا التطبيق قادرًا على الإجابة على أسئلة حول موضوع معين مثل Python، يمكنك أن تكون لديك طلبات مثل "ما هو موضوع معين في Python؟"، أو يمكنك أن يكون لديك طلب يقول، أرني الكود لموضوع معين إلخ.
- بوت التاريخ، اجعل التاريخ ينبض بالحياة، وجه البوت ليلعب دور شخصية تاريخية معينة واسأله أسئلة عن حياته وأوقاته.

## الحل

### زميل الدراسة

فيما يلي طلب بداية، انظر كيف يمكنك استخدامه وتعديله حسب رغبتك.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### بوت التاريخ

إليك بعض الطلبات التي يمكنك استخدامها:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## اختبار المعرفة

ما الذي تفعله فكرة درجة الحرارة؟

1. تتحكم في مدى عشوائية الناتج.
1. تتحكم في حجم الاستجابة.
1. تتحكم في عدد الرموز المستخدمة.

## 🚀 التحدي

أثناء العمل على المهمة، حاول تغيير درجة الحرارة، جرب ضبطها على 0، 0.5، و1. تذكر أن 0 هو الأقل تنوعًا و1 هو الأكثر. ما القيمة التي تعمل بشكل أفضل لتطبيقك؟

## عمل رائع! استمر في التعلم

بعد إكمال هذا الدرس، تحقق من [مجموعة تعلم الذكاء الاصطناعي التوليدي](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) لمواصلة تطوير معرفتك بالذكاء الاصطناعي التوليدي!

توجه إلى الدرس 7 حيث سننظر في كيفية [بناء تطبيقات الدردشة](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.