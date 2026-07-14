# ٹیکسٹ جنریشن ایپلیکیشنز بنانا

[![Building Text Generation Applications](../../../translated_images/ur/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(اس سبق کی ویڈیو دیکھنے کے لیے اوپر تصویر پر کلک کریں)_

آپ نے اب تک اس نصاب کے ذریعے دیکھا ہے کہ بنیادی تصورات جیسے پرامپٹس ہوتے ہیں اور یہاں تک کہ "پرومپٹ انجینئرنگ" کے نام سے ایک مکمل مضمون بھی ہے۔ بہت سے ٹولز جن کے ساتھ آپ تعامل کر سکتے ہیں جیسے کہ ChatGPT, Office 365, Microsoft Power Platform اور دیگر، آپ کو کچھ حاصل کرنے کے لیے پرومپٹس استعمال کرنے کی سہولت دیتے ہیں۔

ایک ایپ میں ایسی تجربے کو شامل کرنے کے لیے، آپ کو پرومپٹس، مکملات (completions) جیسے تصورات کو سمجھنا ہوگا اور کام کرنے کے لیے ایک لائبریری منتخب کرنی ہوگی۔ یہی کچھ آپ اس باب میں سیکھیں گے۔

## تعارف

اس باب میں، آپ:

- openai لائبریری اور اس کے بنیادی تصورات کے بارے میں سیکھیں گے۔
- openai کا استعمال کرتے ہوئے ایک ٹیکسٹ جنریشن ایپ بنائیں گے۔
- ٹیکسٹ جنریشن ایپ بنانے کے لیے پرامپٹ، درجہ حرارت (temperature)، اور ٹوکنز جیسے تصورات کو کیسے استعمال کریں، سمجھیں گے۔

## سیکھنے کے اہداف

اس سبق کے آخر میں، آپ قابل ہوں گے کہ:

- ٹیکسٹ جنریشن ایپ کیا ہے، بیان کریں۔
- openai کی مدد سے ٹیکسٹ جنریشن ایپ بنائیں۔
- زیادہ یا کم ٹوکنز استعمال کرنے کے لیے اپنی ایپ کو ترتیب دیں اور مختلف نتیجہ کے لیے درجہ حرارت (temperature) کو تبدیل کریں۔

## ٹیکسٹ جنریشن ایپ کیا ہے؟

عام طور پر جب آپ کوئی ایپ بناتے ہیں تو اس کے کچھ قسم کا انٹرفیس ہوتا ہے جیسے کہ:

- کمانڈ پر مبنی۔ کنسول ایپس عام ایپلیکیشنز ہوتی ہیں جہاں آپ کمانڈ ٹائپ کرتے ہیں اور یہ کام انجام دیتی ہے۔ مثال کے طور پر، `git` ایک کمانڈ پر مبنی ایپ ہے۔
- صارف کا انٹرفیس (UI). کچھ ایپلیکیشنز میں گرافیکل یوزر انٹرفیس (GUI) ہوتا ہے جہاں آپ بٹن کلک کرتے ہیں، ٹیکسٹ داخل کرتے ہیں، اختیارات منتخب کرتے ہیں اور مزید۔

### کنسول اور یو آئی ایپس محدود ہیں

اسے ایک کمانڈ پر مبنی ایپ سے موازنہ کریں جہاں آپ کمانڈ ٹائپ کرتے ہیں:

- **یہ محدود ہے**۔ آپ کوئی بھی کمانڈ ٹائپ نہیں کر سکتے، صرف وہی جو ایپ کی جانب سے سپورٹ کی جاتی ہیں۔
- **زبان مخصوص**۔ کچھ ایپلیکیشنز بہت سی زبانوں کی حمایت کرتی ہیں، لیکن بطور ڈیفالٹ ایپ مخصوص زبان کے لیے بنائی جاتی ہے، چاہے آپ اضافی زبان کی حمایت شامل کر سکیں۔

### ٹیکسٹ جنریشن ایپس کے فوائد

تو ٹیکسٹ جنریشن ایپ مختلف کیسے ہے؟

ٹیکسٹ جنریشن ایپ میں آپ کے پاس زیادہ لچک ہوتی ہے، آپ کسی مخصوص کمانڈ یا زبان تک محدود نہیں ہوتے۔ اس کی جگہ، آپ قدرتی زبان استعمال کرتے ہوئے ایپ के ساتھ بات چیت کر سکتے ہیں۔ ایک اور فائدہ یہ ہے کہ آپ پہلے ہی ایک ڈیٹا سورس کے ساتھ تعامل کر رہے ہیں جو وسیع معلومات پر مبنی ہے، جبکہ روایتی ایپ ممکنہ طور پر ڈیٹا بیس کی محدود معلومات رکھتی ہے۔

### ٹیکسٹ جنریشن ایپ سے میں کیا بنا سکتا ہوں؟

آپ بہت سی چیزیں بنا سکتے ہیں۔ مثلاً:

- **ایک چیٹ بوٹ**۔ ایک چیٹ بوٹ جو موضوعات جیسے آپ کی کمپنی اور اس کی مصنوعات کے بارے میں سوالات کے جواب دیتا ہو، ایک اچھا متبادل ہو سکتا ہے۔
- **ہیلپر**۔ LLMs متن کے خلاصے، متن سے بصیرت حاصل کرنے، ریزیومے جیسے ٹیکسٹ پیدا کرنے میں بہت اچھے ہیں۔
- **کوڈ اسسٹنٹ**۔ آپ استعمال کردہ زبان کے ماڈل کے مطابق کوڈ اسسٹنٹ بنا سکتے ہیں جو آپ کو کوڈ لکھنے میں مدد دے۔ مثال کے طور پر، آپ GitHub Copilot یا ChatGPT استعمال کر کے کوڈ لکھنے میں مدد لے سکتے ہیں۔

## میں کیسے شروع کر سکتا ہوں؟

آپ کو عام طور پر ایک LLM کے ساتھ انٹیگریٹ کرنے کا کوئی طریقہ تلاش کرنا ہوگا جس میں دو بنیادی طریقے شامل ہو سکتے ہیں:

- API استعمال کریں۔ یہاں آپ اپنے پرومپٹ کے ساتھ ویب ریکویسٹ تیار کرتے ہیں اور جنریٹڈ ٹیکسٹ واپس حاصل کرتے ہیں۔
- لائبریری استعمال کریں۔ لائبریریاں API کالز کو سمیٹنے میں مدد دیتی ہیں اور استعمال کو آسان بناتی ہیں۔

## لائبریریاں/SDKs

LLMs کے ساتھ کام کرنے کے لیے کچھ مشہور لائبریریاں موجود ہیں جیسے:

- **openai**، یہ لائبریری آپ کے ماڈل سے جڑنا اور پرومپٹ بھیجنا آسان بناتی ہے۔

پھر ایسی لائبریریاں بھی ہیں جو اعلیٰ سطح پر کام کرتی ہیں، مثلاً:

- **Langchain**۔ Langchain معروف ہے اور Python کی حمایت کرتا ہے۔
- **Semantic Kernel**۔ Semantic Kernel مائیکروسافٹ کی ایک لائبریری ہے جو C#, Python، اور Java زبانوں کی حمایت کرتی ہے۔

## openai کا استعمال کرتے ہوئے پہلی ایپ

آئیے دیکھیں کہ ہم اپنی پہلی ایپ کیسے بنا سکتے ہیں، کون سی لائبریریاں درکار ہیں، کتنی مقدار چاہیے وغیرہ۔

### openai انسٹال کریں

OpenAI یا Azure OpenAI کے ساتھ تعامل کے لیے کئی لائبریریاں دستیاب ہیں۔ آپ مختلف پروگرامنگ زبانیں استعمال کر سکتے ہیں جیسے C#, Python, JavaScript, Java وغیرہ۔ ہم نے `openai` Python لائبریری منتخب کی ہے، اس لیے ہم `pip` استعمال کریں گے اسے انسٹال کرنے کے لیے۔

```bash
pip install openai
```

### ایک ریسورس بنائیں

آپ کو درج ذیل مراحل پر عمل کرنا ہوگا:

- Azure پر ایک اکاؤنٹ بنائیں [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)۔
- Azure OpenAI تک رسائی حاصل کریں۔ جائیں [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) اور درخواست دیں۔

  > [!NOTE]
  > تحریر کے وقت، آپ کو Azure OpenAI تک رسائی کے لیے درخواست دینا ہوگی۔

- Python انسٹال کریں <https://www.python.org/>
- Azure OpenAI سروس ریسورس بنائیں۔ یہ گائیڈ دیکھیں کہ [ریسورس کیسے بنائیں](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)۔

### API کلید اور اینڈ پوائنٹ تلاش کریں

اس مقام پر، آپ کو `openai` لائبریری کو یہ بتانا ہوگا کہ کون سی API کلید استعمال کرنی ہے۔ اپنی API کلید حاصل کرنے کے لیے، اپنے Azure OpenAI ریسورس کے "Keys and Endpoint" سیکشن میں جائیں اور "Key 1" کی قدر کو کاپی کریں۔

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

جب آپ کے پاس یہ معلومات کاپی ہو چکی ہے، تو لائبریریوں کو اسے استعمال کرنے کی ہدایت دیں۔

> [!NOTE]
> اپنی API کلید کوڈ سے الگ رکھنا بہتر ہے۔ آپ اسے ماحول کے متغیرات استعمال کر کے کر سکتے ہیں۔
>
> - `OPENAI_API_KEY` ماحول کا متغیر اپنی API کلید پر سیٹ کریں۔
>   `export OPENAI_API_KEY='sk-...'`

### Azure کنفیگریشن سیٹ کریں

اگر آپ Azure OpenAI استعمال کر رہے ہیں (جو اب Microsoft Foundry کا حصہ ہے)، تو کنفیگریشن اس طرح سیٹ کریں۔ ہم معیاری `OpenAI` کلائنٹ استعمال کرتے ہیں جو Azure OpenAI کے `/openai/v1/` اینڈ پوائنٹ کی طرف اشارہ کرتا ہے، جو Responses API کے ساتھ کام کرتا ہے اور `api_version` کی ضرورت نہیں ہوتی:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

اوپر ہم درج ذیل سیٹ کر رہے ہیں:

- `api_key`، جو آپ کی API کلید ہے جو Azure پورٹل یا Microsoft Foundry پورٹل میں ہے۔
- `base_url`، جو آپ کے Foundry ریسورس اینڈ پوائنٹ کے ساتھ `/openai/v1/` لگایا ہوا ہے۔ یہ مستحکم v1 اینڈ پوائنٹ OpenAI اور Azure OpenAI دونوں کے لیے بغیر `api_version` مینجمنٹ کے کام کرتا ہے۔

> [!NOTE] > `os.environ` ماحول کے متغیرات کو پڑھتا ہے۔ آپ اسے `AZURE_OPENAI_API_KEY` اور `AZURE_OPENAI_ENDPOINT` جیسے متغیرات کو پڑھنے کے لیے استعمال کر سکتے ہیں۔ انہیں اپنے ٹرمینل میں یا `dotenv` جیسی لائبریری کے ذریعے سیٹ کریں۔

## ٹیکسٹ جنریٹ کریں

ٹیکسٹ جنریٹ کرنے کا طریقہ یہ ہے کہ Responses API کو `responses.create` میتھڈ کے ذریعے استعمال کریں۔ یہ ایک مثال ہے:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-4o-mini",  # یہ آپ کے ماڈل کی ڈیپلائمنٹ کا نام ہے
    input=prompt,
    store=False,
)
print(response.output_text)
```

اوپر کے کوڈ میں، ہم ایک ریسپانس بنا رہے ہیں اور ماڈل اور پرومپٹ پاس کر رہے ہیں۔ پھر ہم `response.output_text` کے ذریعے جنریٹ شدہ ٹیکسٹ پرنٹ کرتے ہیں۔

### ملٹی ٹرن بات چیت

Responses API دونوں سنگل ٹرن ٹیکسٹ جنریشن اور ملٹی ٹرن چیٹ بوٹس کے لیے موزوں ہے — آپ `input` میں پیغامات کی فہرست فراہم کرتے ہیں تاکہ بات چیت بنائی جا سکے:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-4o-mini", input="Hello world", store=False)
print(response.output_text)
```

اس فنکشن کی مزید تفصیل آنے والے باب میں دی جائے گی۔

## مشق - اپنی پہلی ٹیکسٹ جنریشن ایپ

اب جب کہ ہم نے openai کو سیٹ اپ اور کنفیگر کرنا سیکھ لیا ہے، وقت ہے کہ آپ کی پہلی ٹیکسٹ جنریشن ایپ بنائیں۔ اپنی ایپ بنانے کے لیے درج ذیل اقدامات کریں:

1. ایک ورچوئل ماحول بنائیں اور openai انسٹال کریں:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > اگر آپ ونڈوز استعمال کر رہے ہیں تو `source venv/bin/activate` کی جگہ `venv\Scripts\activate` ٹائپ کریں۔

   > [!NOTE]
   > اپنی Azure OpenAI کلید تلاش کرنے کے لیے [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) جائیں، `Open AI` تلاش کریں، `Open AI resource` منتخب کریں، پھر `Keys and Endpoint` منتخب کریں اور `Key 1` کی قدر کو کاپی کریں۔

1. _app.py_ فائل بنائیں اور اسے درج ذیل کوڈ دیں:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # اپنا مکمل کوڈ شامل کریں
   prompt = "Complete the following: Once upon a time there was a"

   # Responses API استعمال کرتے ہوئے ایک درخواست کریں
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # جواب پرنٹ کریں
   print(response.output_text)
   ```

   > [!NOTE]
   > اگر آپ عام OpenAI (Azure نہیں) استعمال کر رہے ہیں، تو `client = OpenAI(api_key="<اپنی OpenAI کلید یہاں رکھیں>")` استعمال کریں (کسی `base_url` کے بغیر) اور ڈپلائمنٹ نام کی جگہ `gpt-4o-mini` جیسے ماڈل نام پاس کریں۔

   آپ کو مندرجہ ذیل نتائج دیکھنے کو ملیں گے:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## مختلف قسم کے پرامپٹس، مختلف کاموں کے لیے

اب آپ نے دیکھا کہ ٹیکسٹ جنریٹ کرنے کے لیے پرامپٹ کیسے استعمال کرتے ہیں۔ آپ کے پاس ایک پروگرام بھی ہے جو چل رہا ہے جسے آپ تبدیل کر کے مختلف قسم کے ٹیکسٹ جنریٹ کر سکتے ہیں۔

پرامپٹس مختلف قسم کے کاموں کے لیے استعمال کیے جا سکتے ہیں۔ مثلاً:

- **کسی قسم کا متن تیار کرنا**۔ مثلاً، آپ نظم تیار کر سکتے ہیں، کوئز کے سوالات وغیرہ۔
- **معلومات تلاش کرنا**۔ آپ پرامپٹس کا استعمال معلومات تلاش کرنے کے لیے کر سکتے ہیں جیسے کہ 'ویب ڈیویلپمنٹ میں CORS کا مطلب کیا ہے؟'۔
- **کوڈ جنریٹ کرنا**۔ آپ پرامپٹس استعمال کر کے کوڈ جنریٹ کر سکتے ہیں، مثلاً ای میل کی تصدیق کے لیے ریگولر ایکسپریشن بنانا یا ایک پورے پروگرام جیسے ویب ایپ بنانا۔

## زیادہ عملی استعمال کا کیس: ایک ریسیپی جنریٹر

فرض کریں آپ کے پاس گھر پر اجزاء موجود ہیں اور آپ کچھ پکانا چاہتے ہیں۔ اس کے لیے آپ کو ایک نسخہ چاہیے۔ نسخے تلاش کرنے کا طریقہ سرچ انجن کا استعمال ہے یا آپ LLM کا استعمال بھی کر سکتے ہیں۔

آپ ایک پرامپٹ اس طرح لکھ سکتے ہیں:

> "مجھے درج ذیل اجزاء کے ساتھ ایک ڈش کے 5 نسخے دکھائیں: چکن، آلو، اور گاجر۔ ہر نسخے میں استعمال ہونے والے تمام اجزاء کی فہرست بنائیں"

اوپر والے پرامپٹ کے جواب میں آپ کو ممکنہ طور پر کچھ ایسا مل سکتا ہے:

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

یہ نتیجہ بہت اچھا ہے، مجھے پتہ چل گیا کیا بنانا ہے۔ اس موقع پر، مفید بہتریاں یہ ہو سکتی ہیں:

- ایسے اجزاء کو فلٹر کرنا جو مجھے پسند نہیں یا جن سے میں الرجک ہوں۔
- اگر میرے پاس تمام اجزاء نہیں ہیں تو ایک خریداری کی فہرست بنانا۔

اوپر والے کیسز کے لیے، ایک اضافی پرامپٹ شامل کرتے ہیں:

> "براہ کرم نسخے جن میں لہسن ہو، نکال دیں کیونکہ مجھے اس سے الرجی ہے اور اس کی جگہ کچھ اور رکھیں۔ ساتھ ہی، نسخوں کی ایک خریداری کی فہرست بنائیں، فرض کرتے ہوئے کہ میرے پاس پہلے سے چکن، آلو، اور گاجر موجود ہیں۔"

اب آپ کو ایک نیا نتیجہ ملے گا، یعنی:

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

یہ آپ کے پانچ نسخے ہیں، جس میں لہسن شامل نہیں اور آپ کے پاس خریداری کی فہرست بھی ہے جس میں وہ چیزیں شامل ہیں جو آپ کے پاس پہلے سے موجود ہیں۔

## مشق - ایک ریسیپی جنریٹر بنائیں

اب جب کہ ہم نے ایک منظر نامہ ادا کیا ہے، آئیے کوڈ لکھیں جو دکھائے گئے منظر نامے سے مطابقت رکھتا ہو۔ ایسا کرنے کے لیے درج ذیل اقدامات کریں:

1. موجودہ _app.py_ فائل کو شروع کرنے کا نقطہ کے طور پر استعمال کریں۔
1. `prompt` متغیر تلاش کریں اور اس کا کوڈ درج ذیل میں تبدیل کریں:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   اگر آپ اب کوڈ چلائیں تو آپ کو کچھ ایسا نتیجہ نظر آئے گا:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > نوٹ کریں، آپ کا LLM غیر متعین ہے، اس لیے ہر بار پروگرام چلانے پر مختلف نتائج آ سکتے ہیں۔

   بہت اچھا، آئیے دیکھیں کہ ہم چیزوں کو کیسے بہتر بنا سکتے ہیں۔ بہتری کے لیے، ہم چاہتے ہیں کہ کوڈ لچکدار ہو، تاکہ اجزاء اور نسخوں کی تعداد کو بہتر اور تبدیل کیا جا سکے۔

1. آئیے کوڈ کو درج ذیل طریقے سے تبدیل کریں:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # اجزاء اور نسخوں کی تعداد کو پرامپٹ میں شامل کریں
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   کوڈ کا ایک ٹیسٹ رن اس طرح ہو سکتا ہے:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### فلٹر اور خریداری کی فہرست شامل کر کے بہتر بنائیں

ہمارے پاس اب ایک کام کرنے والی ایپ ہے جو نسخے بنا سکتی ہے اور یہ لچکدار ہے کیونکہ یہ یوزر سے ان پٹ پر منحصر ہے، چاہے نسخوں کی تعداد ہو یا استعمال ہونے والے اجزاء۔

اسے مزید بہتر بنانے کے لیے ہم درج ذیل شامل کرنا چاہتے ہیں:

- **ناپسندیدہ اجزاء کو فلٹر کریں**۔ ہم چاہتے ہیں کہ ہم ان اجزاء کو فلٹر کر سکیں جو ہمیں پسند نہیں یا جن سے ہم الرجک ہیں۔ یہ تبدیلی کرنے کے لیے، ہم اپنا موجودہ پرامپٹ ایڈیٹ کریں گے اور آخر میں فلٹر کی شرط شامل کریں گے، جیسا کہ:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  اوپر، ہم پرامپٹ کے آخر میں `{filter}` شامل کرتے ہیں اور فلٹر ویلیو یوزر سے بھی حاصل کرتے ہیں۔

  پروگرام چلانے کی ایک مثال درج ذیل ہو سکتی ہے:

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

  جیسا کہ آپ دیکھ سکتے ہیں، دودھ والے نسخے فلٹر ہو چکے ہیں۔ لیکن اگر آپ لیکٹوز انٹالرنٹ ہیں، تو آپ پنیر والے نسخے بھی فلٹر کرنا چاہیں گے، اس لیے وضاحت ضروری ہے۔


- **خریداری کی فہرست تیار کریں**۔ ہم خریداری کی فہرست تیار کرنا چاہتے ہیں، اس بات کو مدنظر رکھتے ہوئے کہ ہمارے پاس پہلے سے گھر میں کیا موجود ہے۔

  اس فعالیت کے لیے، ہم سب کچھ ایک پرامپٹ میں حل کرنے کی کوشش کر سکتے ہیں یا اسے دو پرامپٹس میں تقسیم کر سکتے ہیں۔ آئیے بعد والے طریقہ کو آزماتے ہیں۔ یہاں ہم ایک اضافی پرامپٹ شامل کرنے کا مشورہ دے رہے ہیں، لیکن اس کے کام کرنے کے لیے ہمیں پہلے پرامپٹ کے نتیجے کو دوسرے پرامپٹ کے سیاق و سباق کے طور پر شامل کرنا ہوگا۔

  اس کوڈ کے حصے کو تلاش کریں جو پہلے پرامپٹ کے نتیجے کو پرنٹ کرتا ہے اور اس کے نیچے درج ذیل کوڈ شامل کریں:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # جواب پرنٹ کریں
  print("Shopping list:")
  print(response.output_text)
  ```

  درج ذیل باتوں کا دھیان رکھیں:

  1. ہم نئے پرامپٹ کی تعمیر کر رہے ہیں جس میں پہلے پرامپٹ کا نتیجہ شامل کیا جا رہا ہے:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. ہم نئی درخواست کر رہے ہیں، لیکن ساتھ ہی پہلے پرامپٹ میں مطلوبہ ٹوکن کی تعداد کو بھی مدنظر رکھتے ہیں، اس لیے اس بار ہم کہتے ہیں کہ `max_output_tokens` کی قدر 1200 ہے۔

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     اس کوڈ کو آزمانے کے بعد، ہمیں درج ذیل نتیجہ حاصل ہوتا ہے:

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

جو کچھ ہمارے پاس اب تک ہے وہ کام کرنے والا کوڈ ہے، لیکن کچھ ترمیمات ایسی ہیں جو چیزوں کو مزید بہتر بنانے کے لیے کی جانی چاہئیں۔ کچھ ایسی چیزیں جو ہمیں کرنی چاہئیں وہ ہیں:

- **راز کوڈ سے الگ رکھیں**، جیسے API کلید۔ راز کوڈ میں نہیں ہونے چاہئیں اور انہیں محفوظ جگہ پر ذخیرہ کرنا چاہیے۔ راز کو کوڈ سے الگ کرنے کے لیے، ہم ماحول کے متغیرات (environment variables) اور جیسے لائبریریاں استعمال کر سکتے ہیں `python-dotenv` جو انہیں فائل سے لوڈ کر سکیں۔ کوڈ میں یہ کچھ اس طرح نظر آئے گا:

  1. ایک `.env` فائل بنائیں جس میں درج ذیل مواد ہو:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > نوٹ کریں، مائیکروسافٹ فاؤنڈری میں Azure OpenAI کے لیے، آپ کو درج ذیل ماحول کے متغیرات سیٹ کرنے ہوں گے:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     کوڈ میں، آپ ماحول کے متغیرات کو اس طرح لوڈ کریں گے:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **ٹوکین کی لمبائی پر ایک بات**۔ ہمیں غور کرنا چاہیے کہ آپ جس متن کو پیدا کرنا چاہتے ہیں اس کے لیے کتنے ٹوکنز کی ضرورت ہے۔ ٹوکنز کی قیمت ہوتی ہے، لہٰذا جہاں ممکن ہو ہمیں استعمال ہونے والے ٹوکنز کی تعداد میں کفایت شعاری برتنی چاہیے۔ مثال کے طور پر، کیا ہم پرامپٹ کو اس طرح بنا سکتے ہیں کہ کم ٹوکنز استعمال ہوں؟

  ٹوکنز کی تعداد تبدیل کرنے کے لیے، آپ `max_output_tokens` پیرامیٹر استعمال کر سکتے ہیں۔ مثال کے طور پر، اگر آپ 100 ٹوکنز استعمال کرنا چاہتے ہیں، تو آپ یوں کریں گے:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **درجہ حرارت (temperature) کے ساتھ تجربہ کرنا**۔ temperature ایسی چیز ہے جس کا ابھی تک ذکر نہیں کیا گیا لیکن یہ ہمارے پروگرام کی کارکردگی کے لیے اہم ہے۔ جتنا temperature کی قدر زیادہ ہوگی اتنا ہی آؤٹ پٹ زیادہ بے ترتیب ہوگا۔ اس کے برعکس، جتنا temperature کی قدر کم ہوگی اتنا ہی آؤٹ پٹ زیادہ متوقع ہوگا۔ غور کریں کہ آپ کو اپنے آؤٹ پٹ میں تبدیلی چاہیئے یا نہیں۔

  temperature تبدیل کرنے کے لیے، آپ `temperature` پیرامیٹر استعمال کر سکتے ہیں۔ مثال کے طور پر، اگر آپ 0.5 temperature استعمال کرنا چاہتے ہیں، تو آپ یوں کریں گے:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > نوٹ کریں، جتنا 1.0 کے قریب ہوگا اتنا ہی آؤٹ پٹ میں زیادہ تغیر ہوگا۔

## اسائنمنٹ

اس اسائنمنٹ کے لیے، آپ منتخب کر سکتے ہیں کہ کیا بنانا ہے۔

یہاں کچھ تجاویز دی گئی ہیں:

- ترکیب تیار کرنے والی ایپ کو مزید بہتر بنانے کے لیے ترمیم کریں۔ temperature کی قدریں اور پرامپٹس کے ساتھ تجربہ کریں تاکہ دیکھ سکیں آپ کیا کچھ بنا سکتے ہیں۔
- ایک "مطالعہ ساتھی" بنائیں۔ یہ ایپ کسی موضوع، مثلاً Python، پر سوالات کے جواب دے سکتی ہے، جیسے پرامپٹس ہوسکتے ہیں "Python میں کسی مخصوص موضوع کا کیا مطلب ہے؟"، یا "کسی مخصوص موضوع کے لیے کوڈ دکھائیں" وغیرہ۔
- تاریخ کا بوٹ، تاریخ کو زندہ کریں، بوٹ کو ہدایت دیں کہ وہ کسی خاص تاریخی شخصیت کا کردار ادا کرے اور اس کی زندگی اور دور کے بارے میں سوالات کریں۔

## حل

### مطالعہ ساتھی

نیچے ایک ابتدائی پرامپٹ دیا گیا ہے، دیکھیں کہ آپ اسے کس طرح استعمال کر کے اپنی پسند کے مطابق ترمیم کر سکتے ہیں۔

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### تاریخ کا بوٹ

یہاں کچھ پرامپٹس دی گئی ہیں جو آپ استعمال کر سکتے ہیں:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## علم کا جائزہ

درجہ حرارت (temperature) کا تصور کیا کرتا ہے؟

1. یہ کنٹرول کرتا ہے کہ آؤٹ پٹ کتنا بے ترتیب ہے۔
1. یہ کنٹرول کرتا ہے کہ جواب کتنا بڑا ہے۔
1. یہ کنٹرول کرتا ہے کہ کتنے ٹوکنز استعمال ہوتے ہیں۔

## 🚀 چیلنج

اس اسائنمنٹ پر کام کرتے ہوئے، temperature کی قدر میں تبدیلی کرنے کی کوشش کریں، اسے 0، 0.5، اور 1 پر سیٹ کریں۔ یاد رکھیں 0 سب سے کم تغیر ہے اور 1 سب سے زیادہ۔ آپ کی ایپ کے لیے کونسی قدر سب سے بہترین کام کرتی ہے؟

## شاندار کام! اپنی تعلیم جاری رکھیں

اس سبق کو مکمل کرنے کے بعد، ہماری [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) دیکھیں تاکہ Generative AI کا علم مزید بڑھایا جا سکے!

سبق 7 کی طرف جائیں جہاں ہم دیکھیں گے کہ [چیٹ ایپلیکیشنز کیسے بنائیں](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->