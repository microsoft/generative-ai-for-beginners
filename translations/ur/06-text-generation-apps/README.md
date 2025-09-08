<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ce8224073b86b728ed52b19bed7932fd",
  "translation_date": "2025-07-09T11:46:22+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "ur"
}
-->
# ٹیکسٹ جنریشن ایپلیکیشنز بنانا

[![Building Text Generation Applications](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.ur.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(اس سبق کی ویڈیو دیکھنے کے لیے اوپر تصویر پر کلک کریں)_

اب تک آپ نے اس نصاب میں دیکھا ہے کہ بنیادی تصورات جیسے prompts ہوتے ہیں اور ایک مکمل شعبہ "prompt engineering" بھی موجود ہے۔ بہت سے ٹولز جن سے آپ بات چیت کر سکتے ہیں جیسے ChatGPT، Office 365، Microsoft Power Platform اور دیگر، آپ کو prompts کے ذریعے کچھ حاصل کرنے میں مدد دیتے ہیں۔

اگر آپ اپنی ایپ میں ایسا تجربہ شامل کرنا چاہتے ہیں، تو آپ کو prompts، completions جیسے تصورات کو سمجھنا ہوگا اور کام کرنے کے لیے ایک لائبریری منتخب کرنی ہوگی۔ یہی کچھ آپ اس باب میں سیکھیں گے۔

## تعارف

اس باب میں آپ:

- openai لائبریری اور اس کے بنیادی تصورات کے بارے میں جانیں گے۔
- openai استعمال کرتے ہوئے ایک ٹیکسٹ جنریشن ایپ بنائیں گے۔
- سمجھیں گے کہ prompt، temperature، اور tokens جیسے تصورات کو کیسے استعمال کیا جاتا ہے تاکہ ٹیکسٹ جنریشن ایپ بنائی جا سکے۔

## سیکھنے کے مقاصد

اس سبق کے آخر میں، آپ قابل ہوں گے کہ:

- وضاحت کریں کہ ٹیکسٹ جنریشن ایپ کیا ہے۔
- openai استعمال کرتے ہوئے ٹیکسٹ جنریشن ایپ بنائیں۔
- اپنی ایپ کو اس طرح ترتیب دیں کہ وہ زیادہ یا کم tokens استعمال کرے اور temperature کو بھی تبدیل کرے، تاکہ مختلف نتائج حاصل ہوں۔

## ٹیکسٹ جنریشن ایپ کیا ہے؟

عام طور پر جب آپ کوئی ایپ بناتے ہیں تو اس کا کوئی نہ کوئی انٹرفیس ہوتا ہے جیسے:

- کمانڈ پر مبنی۔ Console ایپس عام طور پر ایسی ایپس ہوتی ہیں جہاں آپ کمانڈ ٹائپ کرتے ہیں اور وہ کوئی کام انجام دیتی ہے۔ مثال کے طور پر، `git` ایک کمانڈ پر مبنی ایپ ہے۔
- یوزر انٹرفیس (UI)۔ کچھ ایپس میں گرافیکل یوزر انٹرفیس (GUIs) ہوتے ہیں جہاں آپ بٹن کلک کرتے ہیں، ٹیکسٹ ان پٹ کرتے ہیں، آپشنز منتخب کرتے ہیں اور مزید۔

### Console اور UI ایپس محدود ہوتی ہیں

کسی کمانڈ پر مبنی ایپ سے موازنہ کریں جہاں آپ کمانڈ ٹائپ کرتے ہیں:

- **یہ محدود ہے**۔ آپ کوئی بھی کمانڈ نہیں ٹائپ کر سکتے، صرف وہی جو ایپ سپورٹ کرتی ہے۔
- **زبان مخصوص**۔ کچھ ایپس کئی زبانیں سپورٹ کرتی ہیں، لیکن ڈیفالٹ میں ایپ کسی مخصوص زبان کے لیے بنائی جاتی ہے، چاہے آپ مزید زبانوں کی سپورٹ شامل کر سکیں۔

### ٹیکسٹ جنریشن ایپس کے فوائد

تو ٹیکسٹ جنریشن ایپ کیسے مختلف ہے؟

ٹیکسٹ جنریشن ایپ میں آپ کو زیادہ لچک ملتی ہے، آپ کمانڈز یا مخصوص ان پٹ زبان تک محدود نہیں ہوتے۔ اس کے بجائے، آپ قدرتی زبان استعمال کر کے ایپ سے بات چیت کر سکتے ہیں۔ ایک اور فائدہ یہ ہے کہ چونکہ آپ پہلے ہی ایک ایسے ڈیٹا سورس سے بات کر رہے ہیں جو وسیع معلومات پر تربیت یافتہ ہے، جبکہ روایتی ایپ ڈیٹا بیس میں موجود مواد تک محدود ہو سکتی ہے۔

### میں ٹیکسٹ جنریشن ایپ سے کیا بنا سکتا ہوں؟

آپ بہت سی چیزیں بنا سکتے ہیں۔ مثال کے طور پر:

- **چیٹ بوٹ**۔ ایک چیٹ بوٹ جو آپ کی کمپنی اور اس کی مصنوعات کے بارے میں سوالات کے جواب دیتا ہو، ایک اچھا انتخاب ہو سکتا ہے۔
- **مددگار**۔ LLMs متن کا خلاصہ بنانے، متن سے بصیرت حاصل کرنے، ریزیومے جیسے متن تیار کرنے میں بہت اچھے ہیں۔
- **کوڈ اسسٹنٹ**۔ جس زبان کا ماڈل آپ استعمال کرتے ہیں، اس کے مطابق آپ ایک کوڈ اسسٹنٹ بنا سکتے ہیں جو کوڈ لکھنے میں مدد دے۔ مثال کے طور پر، آپ GitHub Copilot یا ChatGPT جیسے پروڈکٹس استعمال کر سکتے ہیں۔

## میں کیسے شروع کر سکتا ہوں؟

آپ کو LLM کے ساتھ انٹیگریٹ کرنے کا طریقہ تلاش کرنا ہوگا، جو عام طور پر درج ذیل دو طریقے ہوتے ہیں:

- API استعمال کریں۔ یہاں آپ اپنے prompt کے ساتھ ویب ریکویسٹ بناتے ہیں اور جنریٹ شدہ ٹیکسٹ واپس حاصل کرتے ہیں۔
- لائبریری استعمال کریں۔ لائبریریاں API کالز کو انکیپسولیٹ کرتی ہیں اور استعمال کو آسان بناتی ہیں۔

## لائبریریاں/SDKs

LLMs کے ساتھ کام کرنے کے لیے چند معروف لائبریریاں ہیں جیسے:

- **openai**، یہ لائبریری آپ کے ماڈل سے جڑنا اور prompts بھیجنا آسان بناتی ہے۔

پھر کچھ لائبریریاں ہیں جو اعلیٰ سطح پر کام کرتی ہیں جیسے:

- **Langchain**۔ Langchain معروف ہے اور Python کو سپورٹ کرتا ہے۔
- **Semantic Kernel**۔ Semantic Kernel مائیکروسافٹ کی لائبریری ہے جو C#, Python، اور Java زبانوں کو سپورٹ کرتی ہے۔

## openai استعمال کرتے ہوئے پہلی ایپ

آئیے دیکھتے ہیں کہ ہم اپنی پہلی ایپ کیسے بنا سکتے ہیں، کون سی لائبریریاں چاہیے، کتنی ضرورت ہے وغیرہ۔

### openai انسٹال کریں

OpenAI یا Azure OpenAI کے ساتھ بات چیت کے لیے بہت سی لائبریریاں موجود ہیں۔ آپ مختلف پروگرامنگ زبانیں بھی استعمال کر سکتے ہیں جیسے C#, Python, JavaScript, Java وغیرہ۔ ہم نے `openai` Python لائبریری منتخب کی ہے، اس لیے ہم `pip` سے اسے انسٹال کریں گے۔

```bash
pip install openai
```

### ایک resource بنائیں

آپ کو درج ذیل اقدامات کرنے ہوں گے:

- Azure پر اکاؤنٹ بنائیں [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)۔
- Azure OpenAI تک رسائی حاصل کریں۔ یہاں جائیں [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) اور رسائی کی درخواست کریں۔

  > [!NOTE]
  > تحریر کے وقت، آپ کو Azure OpenAI تک رسائی کے لیے درخواست دینی ہوتی ہے۔

- Python انسٹال کریں <https://www.python.org/>
- Azure OpenAI Service resource بنائیں۔ اس گائیڈ کو دیکھیں کہ [resource کیسے بنائیں](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)۔

### API key اور endpoint تلاش کریں

اب آپ کو اپنی `openai` لائبریری کو بتانا ہوگا کہ کون سی API key استعمال کرنی ہے۔ اپنی API key تلاش کرنے کے لیے، Azure OpenAI resource کے "Keys and Endpoint" سیکشن میں جائیں اور "Key 1" کی ویلیو کاپی کریں۔

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

اب جب یہ معلومات آپ کے پاس ہے، تو لائبریریوں کو اسے استعمال کرنے کی ہدایت دیں۔

> [!NOTE]
> بہتر ہے کہ آپ اپنی API key کوڈ سے الگ رکھیں۔ آپ یہ environment variables استعمال کر کے کر سکتے ہیں۔
>
> - environment variable `OPENAI_API_KEY` کو اپنی API key پر سیٹ کریں۔
>   `export OPENAI_API_KEY='sk-...'`

### Azure کی کنفیگریشن سیٹ اپ کریں

اگر آپ Azure OpenAI استعمال کر رہے ہیں، تو کنفیگریشن اس طرح کریں:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

اوپر ہم درج ذیل سیٹ کر رہے ہیں:

- `api_type` کو `azure` پر سیٹ کیا ہے۔ یہ لائبریری کو بتاتا ہے کہ Azure OpenAI استعمال کرنا ہے، OpenAI نہیں۔
- `api_key`، یہ آپ کی Azure Portal میں موجود API key ہے۔
- `api_version`، یہ API کا ورژن ہے جو آپ استعمال کرنا چاہتے ہیں۔ تحریر کے وقت، تازہ ترین ورژن `2023-05-15` ہے۔
- `api_base`، یہ API کا endpoint ہے۔ آپ اسے Azure Portal میں اپنی API key کے ساتھ پاس دیکھ سکتے ہیں۔

> [!NOTE] > `os.getenv` ایک فنکشن ہے جو environment variables پڑھتا ہے۔ آپ اسے `OPENAI_API_KEY` اور `API_BASE` جیسے environment variables پڑھنے کے لیے استعمال کر سکتے ہیں۔ ان environment variables کو اپنے ٹرمینل میں یا `dotenv` جیسی لائبریری کے ذریعے سیٹ کریں۔

## ٹیکسٹ جنریٹ کریں

ٹیکسٹ جنریٹ کرنے کا طریقہ `Completion` کلاس استعمال کرنا ہے۔ مثال درج ذیل ہے:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

اوپر کے کوڈ میں، ہم ایک completion object بناتے ہیں اور ماڈل اور prompt پاس کرتے ہیں۔ پھر جنریٹ شدہ ٹیکسٹ پرنٹ کرتے ہیں۔

### Chat completions

اب تک، آپ نے دیکھا کہ ہم `Completion` استعمال کر کے ٹیکسٹ جنریٹ کر رہے ہیں۔ لیکن ایک اور کلاس ہے جسے `ChatCompletion` کہتے ہیں جو چیٹ بوٹس کے لیے زیادہ موزوں ہے۔ اس کا استعمال کچھ یوں ہے:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

اس فنکشنالٹی پر مزید تفصیل آئندہ باب میں دی جائے گی۔

## مشق - آپ کی پہلی ٹیکسٹ جنریشن ایپ

اب جب ہم نے openai کو سیٹ اپ اور کنفیگر کرنا سیکھ لیا ہے، تو وقت ہے اپنی پہلی ٹیکسٹ جنریشن ایپ بنانے کا۔ اپنی ایپ بنانے کے لیے درج ذیل مراحل پر عمل کریں:

1. ایک virtual environment بنائیں اور openai انسٹال کریں:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > اگر آپ Windows استعمال کر رہے ہیں تو `source venv/bin/activate` کی جگہ `venv\Scripts\activate` ٹائپ کریں۔

   > [!NOTE]
   > اپنی Azure OpenAI key تلاش کرنے کے لیے [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) پر جائیں، `Open AI` تلاش کریں، `Open AI resource` منتخب کریں، پھر `Keys and Endpoint` میں جا کر `Key 1` کی ویلیو کاپی کریں۔

1. ایک _app.py_ فائل بنائیں اور اس میں درج ذیل کوڈ لکھیں:

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
   > اگر آپ Azure OpenAI استعمال کر رہے ہیں، تو `api_type` کو `azure` پر سیٹ کریں اور `api_key` کو اپنی Azure OpenAI key پر سیٹ کریں۔

   آپ کو مندرجہ ذیل جیسا آؤٹ پٹ نظر آئے گا:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## مختلف قسم کے prompts، مختلف کاموں کے لیے

اب آپ نے دیکھا کہ prompt استعمال کر کے ٹیکسٹ کیسے جنریٹ کیا جاتا ہے۔ آپ کے پاس ایک پروگرام بھی ہے جو چل رہا ہے اور آپ اسے تبدیل کر کے مختلف قسم کے ٹیکسٹ جنریٹ کر سکتے ہیں۔

Prompts مختلف کاموں کے لیے استعمال ہو سکتے ہیں۔ مثال کے طور پر:

- **کسی قسم کا ٹیکسٹ جنریٹ کریں**۔ مثلاً، آپ نظم، کوئز کے سوالات وغیرہ جنریٹ کر سکتے ہیں۔
- **معلومات تلاش کریں**۔ آپ prompts استعمال کر کے معلومات تلاش کر سکتے ہیں جیسے 'ویب ڈویلپمنٹ میں CORS کا کیا مطلب ہے؟'۔
- **کوڈ جنریٹ کریں**۔ آپ prompts استعمال کر کے کوڈ بنا سکتے ہیں، مثلاً ای میلز کی تصدیق کے لیے regular expression تیار کرنا یا پورا پروگرام، جیسے ویب ایپ، بنانا۔

## ایک زیادہ عملی مثال: recipe generator

فرض کریں آپ کے پاس گھر میں اجزاء موجود ہیں اور آپ کچھ پکانا چاہتے ہیں۔ اس کے لیے آپ کو recipe چاہیے۔ recipe تلاش کرنے کا ایک طریقہ سرچ انجن استعمال کرنا ہے یا آپ LLM استعمال کر سکتے ہیں۔

آپ prompt کچھ یوں لکھ سکتے ہیں:

> "مجھے ان اجزاء کے ساتھ 5 ڈشز کی recipes دکھائیں: chicken, potatoes, اور carrots۔ ہر recipe کے لیے تمام استعمال شدہ اجزاء کی فہرست بنائیں"

مندرجہ بالا prompt کے جواب میں آپ کو کچھ ایسا مل سکتا ہے:

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

یہ نتیجہ بہت اچھا ہے، مجھے پتہ چل گیا کہ کیا پکانا ہے۔ اس مرحلے پر، کچھ مفید بہتریاں ہو سکتی ہیں:

- وہ اجزاء فلٹر کریں جو مجھے پسند نہیں یا جن سے مجھے الرجی ہے۔
- ایک shopping list بنائیں، اگر میرے پاس گھر میں تمام اجزاء موجود نہیں ہیں۔

ان معاملات کے لیے، ایک اضافی prompt شامل کریں:

> "براہ کرم وہ recipes ہٹا دیں جن میں garlic ہو کیونکہ مجھے اس سے الرجی ہے اور اسے کسی اور چیز سے بدل دیں۔ نیز، recipes کے لیے shopping list بنائیں، یہ مدنظر رکھتے ہوئے کہ میرے پاس پہلے سے chicken, potatoes اور carrots موجود ہیں۔"

اب آپ کے پاس نیا نتیجہ ہوگا، یعنی:

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

یہ آپ کی پانچ recipes ہیں، جن میں garlic شامل نہیں اور آپ کے پاس shopping list بھی ہے جو آپ کے موجودہ اجزاء کو مدنظر رکھتی ہے۔

## مشق - recipe generator بنائیں

اب جب ہم نے ایک منظرنامہ دیکھا، تو آئیے اس کے مطابق کوڈ لکھیں۔ ایسا کرنے کے لیے درج ذیل مراحل پر عمل کریں:

1. موجودہ _app.py_ فائل کو بطور آغاز استعمال کریں۔
1. `prompt` ویریبل تلاش کریں اور اس کا کوڈ درج ذیل میں تبدیل کریں:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   اگر آپ اب کوڈ چلائیں، تو آپ کو کچھ ایسا آؤٹ پٹ نظر آئے گا:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE، آپ کا LLM nondeterministic ہے، اس لیے ہر بار پروگرام چلانے پر مختلف نتائج مل سکتے ہیں۔

   بہت اچھا، اب دیکھتے ہیں کہ ہم بہتری کیسے لا سکتے ہیں۔ بہتری کے لیے، ہم چاہتے ہیں کہ کوڈ لچکدار ہو، تاکہ اجزاء اور recipes کی تعداد کو آسانی سے بدلا جا سکے۔

1. کوڈ کو درج ذیل طریقے سے تبدیل کریں:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   ٹیسٹ رن کے لیے کوڈ کچھ یوں ہو سکتا ہے:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### فلٹر اور shopping list شامل کر کے بہتری

اب ہمارے پاس ایک کام کرنے والی ایپ ہے جو recipes تیار کر سکتی ہے اور یہ لچکدار ہے کیونکہ یہ صارف سے اجزاء اور recipes کی تعداد دونوں لے سکتی ہے۔

مزید بہتری کے لیے، ہم درج ذیل شامل کرنا چاہتے ہیں:

- **اجزاء کو فلٹر کریں**۔ ہم چاہتے ہیں کہ ہم وہ اجزاء فلٹر کر سکیں جو ہمیں پسند نہیں یا جن سے ہمیں الرجی ہے۔ اس تبدیلی کے لیے، ہم اپنے موجودہ prompt میں فلٹر کی شرط آخر میں شامل کر سکتے ہیں، کچھ یوں:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  اوپر، ہم `{filter}` کو prompt کے آخر میں شامل کرتے ہیں اور فلٹر کی ویلیو صارف سے لیتے ہیں۔

  پروگرام چلانے کی ایک مثال ان پٹ کچھ یوں ہو سکتی ہے:

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

  جیسا کہ آپ دیکھ سکتے ہیں، جن recipes میں milk ہے وہ فلٹر ہو چکی ہیں۔ لیکن اگر آپ lactose intolerant ہیں، تو آپ چاہیں گے کہ recipes جن میں cheese ہو وہ بھی فلٹر ہوں، اس لیے وضاحت ضروری ہے۔

- **shopping list تیار کریں**۔ ہم چاہتے ہیں کہ shopping list بنائی جائے، یہ مدنظر رکھتے ہوئے کہ ہمارے پاس گھر میں کیا موجود ہے۔

  اس فنکشنالٹی کے لیے، ہم یا تو سب کچھ ایک ہی prompt میں حل کرنے کی کوشش کر سکتے ہیں یا اسے دو prompts میں تقسیم کر سکتے ہیں۔ ہم دوسرا طریقہ آزما رہے ہیں۔ یہاں ہم ایک اضافی prompt شامل کرنے کی تجویز دے رہے ہیں، لیکن اس کے لیے ضروری ہے کہ پہلے prompt کا نتیجہ دوسرے prompt کے لیے context کے طور پر شامل کیا جائے۔

  کوڈ میں اس حصے کو تلاش کریں جو پہلے prompt کا نتیجہ پرنٹ کرتا ہے اور اس کے نیچے درج ذیل کوڈ شامل کریں:

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

  نوٹ کریں:

  1. ہم نیا prompt اس طرح بنا رہے ہیں کہ پہلے prompt کا نتیجہ نئے prompt میں شامل کر رہے ہیں:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```
1. ہم ایک نئی درخواست بناتے ہیں، لیکن پہلے پرامپٹ میں پوچھے گئے ٹوکنز کی تعداد کو بھی مدنظر رکھتے ہوئے، اس بار ہم کہتے ہیں کہ `max_tokens` کی قیمت 1200 ہے۔

```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

اس کوڈ کو آزمانے کے بعد، ہمیں درج ذیل نتیجہ ملتا ہے:

```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## اپنی ترتیب کو بہتر بنائیں

اب تک ہمارے پاس کام کرنے والا کوڈ ہے، لیکن کچھ تبدیلیاں ایسی ہیں جو ہمیں مزید بہتری کے لیے کرنی چاہئیں۔ کچھ چیزیں جو ہمیں کرنی چاہئیں وہ یہ ہیں:

- **رازوں کو کوڈ سے الگ کریں**، جیسے API کی۔ راز کوڈ میں نہیں ہونے چاہئیں اور انہیں محفوظ جگہ پر ذخیرہ کرنا چاہیے۔ رازوں کو کوڈ سے الگ کرنے کے لیے، ہم ماحول کے متغیرات (environment variables) اور `python-dotenv` جیسی لائبریریاں استعمال کر سکتے ہیں تاکہ انہیں فائل سے لوڈ کیا جا سکے۔ کوڈ میں یہ کچھ اس طرح نظر آئے گا:

  1. ایک `.env` فائل بنائیں جس میں درج ذیل مواد ہو:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     
> [!NOTE] Azure کے لیے، آپ کو درج ذیل ماحول کے متغیرات سیٹ کرنے ہوں گے:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     کوڈ میں، آپ ماحول کے متغیرات کو اس طرح لوڈ کریں گے:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **ٹوکن کی لمبائی پر ایک بات**۔ ہمیں غور کرنا چاہیے کہ ہمیں مطلوبہ متن پیدا کرنے کے لیے کتنے ٹوکنز کی ضرورت ہے۔ ٹوکنز کی قیمت ہوتی ہے، اس لیے جہاں ممکن ہو، ہمیں ٹوکنز کی تعداد میں کفایت شعاری کرنی چاہیے۔ مثال کے طور پر، کیا ہم پرامپٹ کو اس طرح ترتیب دے سکتے ہیں کہ کم ٹوکنز استعمال ہوں؟

  ٹوکنز کی تعداد تبدیل کرنے کے لیے، آپ `max_tokens` پیرامیٹر استعمال کر سکتے ہیں۔ مثال کے طور پر، اگر آپ 100 ٹوکنز استعمال کرنا چاہتے ہیں، تو آپ یوں کریں گے:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **temperature کے ساتھ تجربہ کرنا**۔ temperature ایک ایسا پیرامیٹر ہے جس کا ہم نے اب تک ذکر نہیں کیا، لیکن یہ ہمارے پروگرام کی کارکردگی کے لیے اہم ہے۔ جتنا temperature زیادہ ہوگا، آؤٹ پٹ اتنا ہی زیادہ بے ترتیب ہوگا۔ اس کے برعکس، جتنا temperature کم ہوگا، آؤٹ پٹ اتنا ہی زیادہ قابل پیش گوئی ہوگا۔ غور کریں کہ آپ اپنے آؤٹ پٹ میں تبدیلی چاہتے ہیں یا نہیں۔

  temperature کو تبدیل کرنے کے لیے، آپ `temperature` پیرامیٹر استعمال کر سکتے ہیں۔ مثال کے طور پر، اگر آپ temperature 0.5 استعمال کرنا چاہتے ہیں، تو آپ یوں کریں گے:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > [!NOTE] جتنا temperature 1.0 کے قریب ہوگا، آؤٹ پٹ اتنا ہی زیادہ متنوع ہوگا۔

## اسائنمنٹ

اس اسائنمنٹ کے لیے، آپ خود فیصلہ کر سکتے ہیں کہ کیا بنانا ہے۔

یہاں کچھ تجاویز ہیں:

- recipe generator ایپ کو مزید بہتر بنانے کے لیے اس میں تبدیلی کریں۔ temperature کی قدروں اور پرامپٹس کے ساتھ تجربہ کریں اور دیکھیں کہ آپ کیا نیا بنا سکتے ہیں۔
- ایک "study buddy" بنائیں۔ یہ ایپ کسی موضوع، مثلاً Python، کے بارے میں سوالات کے جواب دے سکے۔ آپ کے پاس ایسے پرامپٹس ہو سکتے ہیں جیسے "Python میں کسی خاص موضوع کی وضاحت کیا ہے؟" یا "کسی خاص موضوع کے لیے کوڈ دکھائیں" وغیرہ۔
- history bot بنائیں، تاریخ کو زندہ کریں، بوٹ کو کسی تاریخی شخصیت کا کردار ادا کرنے کی ہدایت دیں اور اس کی زندگی اور دور کے بارے میں سوالات پوچھیں۔

## حل

### Study buddy

نیچے ایک ابتدائی پرامپٹ دیا گیا ہے، دیکھیں کہ آپ اسے کیسے استعمال کر سکتے ہیں اور اپنی پسند کے مطابق اس میں تبدیلی کر سکتے ہیں۔

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### History bot

یہاں کچھ پرامپٹس ہیں جو آپ استعمال کر سکتے ہیں:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## علم کی جانچ

temperature کا تصور کیا کرتا ہے؟

1. یہ کنٹرول کرتا ہے کہ آؤٹ پٹ کتنا بے ترتیب ہو۔
1. یہ کنٹرول کرتا ہے کہ جواب کتنا بڑا ہو۔
1. یہ کنٹرول کرتا ہے کہ کتنے ٹوکنز استعمال ہوں۔

## 🚀 چیلنج

اسائنمنٹ پر کام کرتے ہوئے، temperature کو مختلف کریں، اسے 0، 0.5، اور 1 پر سیٹ کر کے دیکھیں۔ یاد رکھیں کہ 0 سب سے کم متنوع ہے اور 1 سب سے زیادہ۔ آپ کی ایپ کے لیے کون سی قیمت سب سے بہتر کام کرتی ہے؟

## شاندار کام! اپنی تعلیم جاری رکھیں

اس سبق کو مکمل کرنے کے بعد، ہمارے [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) کو دیکھیں تاکہ آپ اپنی Generative AI کی معلومات کو مزید بڑھا سکیں!

سبق 7 پر جائیں جہاں ہم دیکھیں گے کہ [چیٹ ایپلیکیشنز کیسے بنائیں](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔