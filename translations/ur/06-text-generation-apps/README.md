# ٹیکسٹ جنریشن ایپلیکیشنز کی تعمیر

[![ٹیکسٹ جنریشن ایپلیکیشنز کی تعمیر](../../../translated_images/ur/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(اس سبق کی ویڈیو دیکھنے کے لیے اوپر تصویر پر کلک کریں)_

آپ نے اب تک اس نصاب کے ذریعے دیکھا ہے کہ کچھ بنیادی تصورات جیسے پرامپٹس اور ایک پورا میدان "prompt engineering" بھی ہے۔ بہت سے اوزار جن سے آپ بات چیت کر سکتے ہیں جیسے ChatGPT، Office 365، Microsoft Power Platform اور مزید، آپ کو کسی کام کو مکمل کرنے کے لیے پرامپٹس استعمال کرنے کی سہولت دیتے ہیں۔

آپ کو ایک ایپ میں ایسا تجربہ شامل کرنے کے لیے، آپ کو پرامپٹس، مکملات جیسے تصورات کو سمجھنا ہوگا اور کام کرنے کے لیے ایک لائبریری کا انتخاب کرنا ہوگا۔ یہ بالکل وہی ہے جو آپ اس باب میں سیکھیں گے۔

## تعارف

اس باب میں، آپ یہ کریں گے:

- openai لائبریری اور اس کے بنیادی تصورات کے بارے میں جانیں۔
- openai استعمال کرتے ہوئے ایک ٹیکسٹ جنریشن ایپ بنائیں۔
- پرامپٹ، درجہ حرارت، اور ٹوکنز جیسے تصورات کو سمجھیں تاکہ ایک ٹیکسٹ جنریشن ایپ بنائیں۔

## سیکھنے کے مقاصد

اس سبق کے آخر میں، آپ یہ کرنے کے قابل ہوں گے:

- ایک ٹیکسٹ جنریشن ایپ کیا ہے، اسے بیان کریں۔
- openai استعمال کرتے ہوئے ایک ٹیکسٹ جنریشن ایپ بنائیں۔
- اپنے ایپ کو زیادہ یا کم ٹوکنز استعمال کرنے کے لیے ترتیب دیں اور درجہ حرارت کو بھی تبدیل کریں، تاکہ نتیجہ مختلف ہو۔

## ٹیکسٹ جنریشن ایپ کیا ہے؟

عام طور پر جب آپ ایک ایپ بناتے ہیں تو اس میں کسی قسم کا انٹرفیس ہوتا ہے جیسا کہ ذیل میں ہے:

- کمانڈ پر مبنی۔ کونسول ایپس عام ایپس ہیں جہاں آپ کمانڈ ٹائپ کرتے ہیں اور یہ کام انجام دیتی ہے۔ مثال کے طور پر، `git` ایک کمانڈ پر مبنی ایپ ہے۔
- یوزر انٹرفیس (UI)۔ کچھ ایپس میں گرافیکل یوزر انٹرفیس (GUIs) ہوتے ہیں جہاں آپ بٹن کلک کرتے ہیں، متن درج کرتے ہیں، آپشن منتخب کرتے ہیں اور مزید۔

### کونسول اور یو آئی ایپس محدود ہیں

اسے اس کمانڈ پر مبنی ایپ سے موازنہ کریں جہاں آپ ایک کمانڈ ٹائپ کرتے ہیں:

- **یہ محدود ہے**۔ آپ کوئی بھی کمانڈ ٹائپ نہیں کر سکتے، صرف وہی جو ایپ سپورٹ کرتی ہے۔
- **زبان مخصوص**۔ کچھ ایپس بہت سی زبانوں کی حمایت کرتی ہیں، لیکن بذریعہِ ڈیفالٹ ایپ کسی مخصوص زبان کے لیے بنی ہوتی ہے، اگرچہ آپ مزید زبانوں کی حمایت شامل کر سکتے ہیں۔

### ٹیکسٹ جنریشن ایپس کے فوائد

تو ٹیکسٹ جنریشن ایپ کیسے مختلف ہے؟

ٹیکسٹ جنریشن ایپ میں، آپ کے پاس زیادہ لچک ہوتی ہے، آپ کمانڈز کے سیٹ یا مخصوص ان پٹ زبان تک محدود نہیں ہوتے۔ اس کے بجائے، آپ قدرتی زبان استعمال کر کے ایپ سے بات کر سکتے ہیں۔ ایک اور فائدہ یہ ہے کہ آپ پہلے سے ایک ڈیٹا سورس سے بات کر رہے ہیں جسے بہت زیادہ معلومات پر تربیت دی گئی ہے، جبکہ روایتی ایپ ڈیٹا بیس میں موجود معلومات تک محدود ہو سکتی ہے۔

### میں ٹیکسٹ جنریشن ایپ سے کیا بنا سکتا ہوں؟

بہت سی چیزیں بنا سکتے ہیں۔ مثال کے طور پر:

- **ایک چیٹ بوٹ**۔ ایک چیٹ بوٹ جو آپ کی کمپنی اور اس کی مصنوعات کے متعلق سوالات کے جواب دیتا ہو، ایک اچھا انتخاب ہو سکتا ہے۔
- **مددگار**۔ LLMs متن کو خلاصہ کرنے، متن سے بصیرت حاصل کرنے، ریزیومے جیسے متن تیار کرنے میں بہت اچھے ہیں۔
- **کوڈ اسسٹنٹ**۔ آپ جس زبان ماڈل کا استعمال کرتے ہیں اس پر منحصر ہے، آپ ایک کوڈ اسسٹنٹ بنا سکتے ہیں جو آپ کو کوڈ لکھنے میں مدد دے۔ مثال کے طور پر، آپ GitHub Copilot یا ChatGPT جیسے مصنوعات استعمال کر کے کوڈ لکھنے میں مدد حاصل کر سکتے ہیں۔

## میں کیسے شروع کر سکتا ہوں؟

آپ کو عام طور پر LLM کے ساتھ انٹیگریٹ کرنے کا طریقہ تلاش کرنا ہوگا جو عموماً دو طریقے شامل ہیں:

- API استعمال کریں۔ یہاں آپ اپنے پرامپٹ کے ساتھ ویب درخواستیں بناتے ہیں اور جنریٹ شدہ متن واپس حاصل کرتے ہیں۔
- لائبریری استعمال کریں۔ لائبریریاں API کالز کو بند کر دیتی ہیں اور انہیں استعمال کرنا آسان بناتی ہیں۔

## لائبریریاں/SDKs

LLMs کے ساتھ کام کرنے والی کچھ معروف لائبریریاں ہیں جیسے:

- **openai**، یہ لائبریری آپ کے ماڈل سے جڑنے اور پرامپٹس بھیجنے کو آسان بناتی ہے۔

پھر ایسی لائبریریاں بھی ہیں جو ایک اعلی سطح پر کام کرتی ہیں جیسے:

- **Langchain**۔ Langchain مشہور ہے اور Python کی حمایت کرتا ہے۔
- **Semantic Kernel**۔ Semantic Kernel مائیکروسافٹ کی ایک لائبریری ہے جو C#, Python، اور Java زبانوں کی حمایت کرتی ہے۔

## openai استعمال کرتے ہوئے پہلا ایپ

آئیے دیکھتے ہیں کہ ہم اپنی پہلی ایپ کیسے بنا سکتے ہیں، کونسی لائبریریاں چاہیے، کتنی ضرورت ہے اور اس طرح کی چیزیں۔

### openai انسٹال کریں

اوپن اے آئی یا Azure OpenAI کے ساتھ بات چیت کے لیے بہت سی لائبریریاں موجود ہیں۔ مختلف پروگرامنگ زبانیں بھی استعمال کی جا سکتی ہیں جیسے C#, Python, JavaScript, Java اور مزید۔ ہم نے Python کی `openai` لائبریری منتخب کی ہے، لہٰذا ہم `pip` استعمال کریں گے اسے انسٹال کرنے کے لیے۔

```bash
pip install openai
```

### ایک ریسورس بنائیں

آپ کو درج ذیل اقدامات کرنے ہوں گے:

- Azure پر اکاؤنٹ بنائیں [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)۔
- Azure OpenAI تک رسائی حاصل کریں۔ جائیں [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) اور رسائی کی درخواست کریں۔

  > [!NOTE]
  > لکھنے کے وقت، آپ کو Azure OpenAI کے لیے رسائی کے لیے درخواست دینی ہوگی۔

- Python انسٹال کریں <https://www.python.org/>
- Azure OpenAI سروس ریسورس بنائیں۔ یہ گائیڈ دیکھیں کہ کیسے [ریسورس بنائیں](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)۔

### API کلید اور اینڈ پوائنٹ تلاش کریں

اس وقت، آپ کو اپنی `openai` لائبریری کو بتانا ہوگا کہ کونسی API کلید استعمال کرنی ہے۔ اپنی API کلید تلاش کرنے کے لیے، Azure OpenAI ریسورس کے "Keys and Endpoint" سیکشن پر جائیں اور "Key 1" کی ویلیو کاپی کریں۔

![Azure پورٹل میں Keys and Endpoint ریسورس بلیڈ](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

اب جب آپ کے پاس یہ معلومات کاپی ہو چکی ہے، آئیے لائبریریوں کو اسے استعمال کرنے کا حکم دیتے ہیں۔

> [!NOTE]
> اپنے API کلید کو اپنے کوڈ سے الگ رکھنا بہتر ہوتا ہے۔ آپ ایسا انوائرنمنٹ ویری ایبلز استعمال کر کے کر سکتے ہیں۔
>
> - انوائرنمنٹ ویری ایبل `OPENAI_API_KEY` کو اپنی API کلید پر سیٹ کریں۔
>   `export OPENAI_API_KEY='sk-...'`

### Azure کنفیگریشن سیٹ اپ کریں

اگر آپ Azure OpenAI (جو اب Microsoft Foundry کا حصہ ہے) استعمال کر رہے ہیں، تو کنفیگریشن سیٹ اپ کرنے کا طریقہ یہ ہے۔ ہم معیاری `OpenAI` کلائنٹ استعمال کرتے ہیں جو Azure OpenAI کے `/openai/v1/` اینڈ پوائنٹ کی طرف اشارہ کرتا ہے، جو Responses API کے ساتھ کام کرتا ہے اور `api_version` کی ضرورت نہیں ہوتی:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

اوپر ہم درج ذیل سیٹ کر رہے ہیں:

- `api_key`, یہ آپ کی API کلید ہے جو Azure پورٹل یا Microsoft Foundry پورٹل میں ملی ہے۔
- `base_url`, یہ آپ کے Foundry ریسورس اینڈ پوائنٹ کے ساتھ `/openai/v1/` لگا ہوا ہے۔ مستحکم v1 اینڈ پوائنٹ OpenAI اور Azure OpenAI دونوں کے لیے کام کرتا ہے بغیر `api_version` کے انتظام کے۔

> [!NOTE] > `os.environ` انوائرنمنٹ ویری ایبلز کو پڑھتا ہے۔ آپ اسے `AZURE_OPENAI_API_KEY` اور `AZURE_OPENAI_ENDPOINT` جیسے ویری ایبلز پڑھنے کے لیے استعمال کر سکتے ہیں۔ ان انوائرنمنٹ ویری ایبلز کو اپنے ٹرمینل میں یا `dotenv` جیسی لائبریری استعمال کر کے سیٹ کریں۔

## متن تیار کریں

متن تیار کرنے کا طریقہ Responses API کے ذریعے `responses.create` میتھڈ استعمال کرنا ہے۔ مثال درج ذیل ہے:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # یہ آپ کے ماڈل کی تعیناتی کا نام ہے
    input=prompt,
    store=False,
)
print(response.output_text)
```

اوپر کوڈ میں، ہم ایک ریسپانس بناتے ہیں اور ماڈل اور پرامپٹ دیتے ہیں۔ پھر ہم `response.output_text` کے ذریعے تیار شدہ متن پرنٹ کرتے ہیں۔

### ملٹی ٹرن بات چیت

Responses API ایک ٹرن ٹیکسٹ جنریشن اور ملٹی ٹرن چیٹ بوٹس دونوں کے لیے موزوں ہے - آپ `input` میں پیغامات کی فہرست دیتے ہیں تاکہ ایک بات چیت تیار کی جا سکے:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

اس فیچر کے بارے میں مزید تفصیل آنے والے باب میں دی جائے گی۔

## مشق - آپ کی پہلی ٹیکسٹ جنریشن ایپ

اب جب ہم نے openai کو سیٹ اپ اور کنفیگر کرنا سیکھ لیا ہے، وقت ہے اپنی پہلی ٹیکسٹ جنریشن ایپ بنانے کا۔ اپنی ایپ بنانے کے لیے درج ذیل اقدامات کریں:

1. ایک ورچوئل انوائرنمنٹ بنائیں اور openai انسٹال کریں:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > اگر آپ Windows استعمال کر رہے ہیں تو `source venv/bin/activate` کی جگہ `venv\Scripts\activate` ٹائپ کریں۔

   > [!NOTE]
   > اپنی Azure OpenAI کلید تلاش کرنے کے لیے [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) پر جائیں، `Open AI` تلاش کریں، `Open AI resource` منتخب کریں پھر `Keys and Endpoint` منتخب کریں اور `Key 1` کی ویلیو کاپی کریں۔

1. _app.py_ فائل بنائیں اور درج ذیل کوڈ دیں:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # اپنا مکمل کرنے کا کوڈ شامل کریں
   prompt = "Complete the following: Once upon a time there was a"

   # Responses API کا استعمال کرتے ہوئے درخواست کریں
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # جواب پرنٹ کریں
   print(response.output_text)
   ```

   > [!NOTE]
   > اگر آپ plain OpenAI (Azure نہیں) استعمال کر رہے ہیں، تو `client = OpenAI(api_key="<replace this value with your OpenAI key>")` استعمال کریں (کوئی `base_url` نہیں) اور ماڈل کا نام `gpt-5-mini` جیسا پاس کریں بجائے کسی deployment نام کے۔

   آپ کو مندرجہ ذیل جیسا آؤٹ پٹ دیکھنا چاہیے:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## مختلف قسم کے پرامپٹس، مختلف چیزوں کے لیے

اب آپ نے پرامپٹ استعمال کر کے متن تیار کرنا سیکھ لیا ہے۔ آپ کے پاس ایک پروگرام بھی چل رہا ہے جسے آپ ترمیم کر کے مختلف قسم کے متن تیار کر سکتے ہیں۔

پرامپٹس ہر قسم کے کاموں کے لیے استعمال کیے جا سکتے ہیں۔ مثال کے طور پر:

- **متن کی کسی قسم کو جنریٹ کریں**۔ مثال کے طور پر، آپ نظم، کوئز کے سوالات وغیرہ تیار کر سکتے ہیں۔
- **معلومات تلاش کریں**۔ آپ پرامپٹس استعمال کر کے معلومات حاصل کر سکتے ہیں، مثلاً سوال 'web development میں CORS کا مطلب کیا ہے؟'۔
- **کوڈ تیار کریں**۔ آپ پرامپٹس استعمال کر کے کوڈ تیار کر سکتے ہیں، جیسے ای میلز کی ویلیڈیٹ کرنے والا regular expression بنانا، یا پورا پروگرام، جیسا کہ ویب ایپ تیار کرنا؟

## ایک زیادہ عملی استعمال: ترکیب جنریٹر

فرض کریں کہ آپ کے پاس گھر میں اجزاء ہیں اور آپ کچھ پکانا چاہتے ہیں۔ اس کے لیے آپ کو ترکیب درکار ہے۔ ترکیب تلاش کرنے کا طریقہ سرچ انجن استعمال کرنا ہو سکتا ہے یا آپ LLM استعمال کر سکتے ہیں۔

آپ ایسا پرامپٹ لکھ سکتے ہیں:

> "میرے لیے ان اجزاء کے ساتھ ۵ ترکیبیں دکھائیں: مرغی، آلو اور گاجر۔ ہر ترکیب کے لیے تمام استعمال شدہ اجزاء فہرست کریں"

مذکورہ پرامپٹ کے لیے، آپ کو مندرجہ ذیل جیسا جواب مل سکتا ہے:

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

یہ نتیجہ شاندار ہے، میں جانتا ہوں کہ کیا پکانا ہے۔ اس موقع پر، کچھ مفید بہتریاں ہو سکتی ہیں:

- وہ اجزاء نکالنا جو مجھے پسند نہیں یا جن سے میں الرجی ہوں۔
- خریداری کی فہرست تیار کرنا، اگر گھر میں میرے پاس تمام اجزاء نہیں ہیں۔

ان صورتوں کے لیے، آئیے ایک اضافی پرامپٹ شامل کریں:

> "براہ کرم وہ ترکیبیں ہٹا دیں جن میں لہسن ہو، کیونکہ مجھے اس سے الرجی ہے اور اس کی جگہ کچھ اور رکھیں۔ نیز، ترکیبوں کی خریداری کی فہرست بنائیں، یہ فرض کرتے ہوئے کہ میرے پاس پہلے سے مرغی، آلو اور گاجر گھر میں موجود ہیں۔"

اب آپ کے پاس ایک نیا نتیجہ ہے، یعنی:

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

یہ آپ کی پانچ ترکیبیں ہیں، جن میں لہسن شامل نہیں اور آپ کے گھر میں جو ہے اس کے لحاظ سے ایک خریداری کی فہرست بھی ہے۔

## مشق - ایک ترکیب جنریٹر بنائیں

اب جب ہم نے ایک منظرنامہ بنا لیا ہے، آئیے اس منظرنامے کے مطابق کوڈ لکھیں۔ ایسا کرنے کے لیے، درج ذیل اقدامات کریں:

1. موجودہ _app.py_ فائل کو بطور نقطہ آغاز استعمال کریں
1. `prompt` متغیر تلاش کریں اور اس کا کوڈ درج ذیل میں تبدیل کریں:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   اگر آپ اب کوڈ چلائیں، تو آپ کو مندرجہ ذیل جیسا نتیجہ دیکھنا چاہیے:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE، آپ کا LLM غیر یقینی ہے، اس لیے ہر بار پروگرام چلانے پر آپ کو مختلف نتائج مل سکتے ہیں۔

   بہت خوب، آئیے دیکھتے ہیں کہ ہم چیزوں کو کیسے بہتر بنا سکتے ہیں۔ چیزوں کو بہتر بنانے کے لیے، ہم چاہتے ہیں کہ کوڈ لچکدار ہو، تاکہ اجزاء اور ترکیبوں کی تعداد میں تبدیلی ممکن ہو۔

1. آئیے کوڈ کو درج ذیل طرح تبدیل کریں:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # اجزاء میں تعداد ترکیبوں کو تلقین کریں اور
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   کوڈ کا ایک ٹیسٹ رن یوں ہو سکتا ہے:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### فلٹر اور خریداری کی فہرست شامل کر کے بہتر بنائیں

ہمارے پاس اب ایک کام کرنے والی ایپ ہے جو ترکیبیں تیار کر سکتی ہے اور یہ اس لیے لچکدار ہے کیونکہ یہ صارف کی طرف سے تعداد اور اجزاء دونوں کو ان پٹ کے طور پر استعمال کرتی ہے۔

اسے مزید بہتر بنانے کے لیے، ہم درج ذیل شامل کرنا چاہتے ہیں:

- **اجزاء کو فلٹر کریں**۔ ہم اس قابل ہونا چاہتے ہیں کہ وہ اجزاء نکال سکیں جو ہمیں پسند نہیں یا جن سے ہمیں الرجی ہے۔ اس تبدیلی کے لیے، ہم اپنے پرامپٹ کو ایڈٹ کر سکتے ہیں اور اس کے آخر میں فلٹر کی شرط شامل کر سکتے ہیں، جیسا کہ:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  اوپر، ہم پرامپٹ کے آخر میں `{filter}` شامل کرتے ہیں اور ہم صارف سے فلٹر ویلیو بھی لیتے ہیں۔

  پروگرام چلانے کی ایک مثال یوں ہو سکتی ہے:

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

  جیسا کہ آپ دیکھ سکتے ہیں، کسی بھی ترکیب جس میں دودھ ہو وہ فلٹر ہو چکی ہے۔ لیکن، اگر آپ لیکٹوز برداشت نہیں کر سکتے، تو آپ شاید ایسی ترکیبیں بھی فلٹر کرنا چاہیں جن میں پنیر ہو، اس لیے وضاحت کی ضرورت ہے۔


- **خریداری کی فہرست تیار کریں**۔ ہم گھر میں پہلے سے موجود چیزوں کو مدنظر رکھتے ہوئے خریداری کی فہرست تیار کرنا چاہتے ہیں۔

  اس فنکشنلٹی کے لیے، ہم سب کچھ ایک پرومپٹ میں حل کرنے کی کوشش کر سکتے ہیں یا اسے دو پرومپٹس میں تقسیم کر سکتے ہیں۔ آئیے دوسرے طریقہ کو آزمانے کی کوشش کرتے ہیں۔ یہاں ہم اضافی پرومپٹ شامل کرنے کی تجویز دے رہے ہیں، لیکن اس کے کام کرنے کے لیے، ہمیں پہلے والے پرومپٹ کے نتیجے کو بعد والے پرومپٹ کے سیاق و سباق میں شامل کرنا ہوگا۔

  کوڈ کے اس حصے کو تلاش کریں جو پہلے پرومپٹ سے نتیجہ پرنٹ کرتا ہے اور اس کے نیچے درج ذیل کوڈ شامل کریں:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # جواب پرنٹ کریں
  print("Shopping list:")
  print(response.output_text)
  ```

  درج ذیل باتوں کو نوٹ کریں:

  1. ہم ایک نیا پرومپٹ بنا رہے ہیں جس میں پہلے پرومپٹ کا نتیجہ نئے پرومپٹ میں شامل کیا جا رہا ہے:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. ہم ایک نئی درخواست بھیج رہے ہیں، لیکن پہلے پرومپٹ میں مانگے گئے ٹوکنز کی تعداد کو بھی مدنظر رکھتے ہوئے، اس بار ہم کہتے ہیں کہ `max_output_tokens` 1200 ہے۔

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     اس کوڈ کو چلانے کے بعد، ہمیں مندرجہ ذیل آؤٹ پٹ حاصل ہوتا ہے:

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

جو کچھ ہمارے پاس اب تک ہے وہ کام کرنے والا کوڈ ہے، لیکن چیزوں کو مزید بہتر بنانے کے لیے کچھ تبدیلیاں کرنی چاہیئں۔ کچھ چیزیں جو ہمیں کرنی چاہئیں وہ ہیں:

- **سیکرٹس کو کوڈ سے الگ کریں**، جیسے API کی۔ سیکرٹس کوڈ میں نہیں ہونے چاہئیں اور انہیں ایک محفوظ مقام پر رکھنا چاہیے۔ سیکرٹس کو کوڈ سے الگ کرنے کے لیے، ہم ماحول کی متغیرات (environment variables) اور ایسی لائبریریز جیسے `python-dotenv` استعمال کر سکتے ہیں جو انہیں فائل سے لوڈ کر سکیں۔ کوڈ میں یہ کچھ اس طرح دکھائی دے گا:

  1. ایک `.env` فائل بنائیں جس میں درج ذیل مواد ہو:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > نوٹ کریں، Microsoft Foundry میں Azure OpenAI کے لیے آپ کو درج ذیل ماحول کی متغیرات ترتیب دینی ہوں گی بجائے اس کے:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     کوڈ میں، آپ ماحول کی متغیرات اس طرح لوڈ کریں گے:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **ٹوکن کی لمبائی پر ایک بات**۔ ہمیں یہ سوچنا چاہیے کہ ہم کتنے ٹوکنز چاہئیں تاکہ مطلوبہ متن تیار ہو سکے۔ ٹوکنز کی قیمت ہوتی ہے، اس لیے جہاں ممکن ہو، ہمیں استعمال کیے جانے والے ٹوکنز کی تعداد میں کفایت شعاری کرنی چاہیے۔ مثال کے طور پر، کیا ہم پرومپٹ اس طرح بنا سکتے ہیں کہ کم ٹوکنز استعمال ہوں؟

  استعمال ہونے والے ٹوکنز کی تعداد کو تبدیل کرنے کے لیے، آپ `max_output_tokens` پیرامیٹر استعمال کر سکتے ہیں۔ مثال کے طور پر، اگر آپ 100 ٹوکنز استعمال کرنا چاہتے ہیں، تو آپ یہ کریں گے:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **درجہ حرارت (temperature) کے ساتھ تجربہ کرنا**۔ temperature ایسا پیرامیٹر ہے جس کا ہم نے اب تک ذکر نہیں کیا لیکن پروگرام کی کارکردگی کے لیے اہم ہے۔ جتنا زیادہ temperature ہوگا، آؤٹ پٹ اتنا ہی زیادہ بے ترتیب ہوگا۔ اس کے برعکس، جتنا کم temperature ہوگا، آؤٹ پٹ اتنا ہی زیادہ قابل پیش گوئی ہوگا۔ غور کریں کہ آیا آپ اپنی آؤٹ پٹ میں تبدیلی چاہتے ہیں یا نہیں۔

  temperature کو تبدیل کرنے کے لیے، آپ `temperature` پیرامیٹر استعمال کر سکتے ہیں۔ مثال کے طور پر، اگر آپ 0.5 کا temperature استعمال کرنا چاہتے ہیں، تو آپ یہ کریں گے:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > نوٹ کریں، جتنا 1.0 کے قریب ہوگا، آؤٹ پٹ اتنا ہی زیادہ متنوع ہوگا۔

- **وجہ سمجھنے والے ماڈلز (Reasoning models) temperature استعمال نہیں کرتے**۔ یہ 2026 کا ایک اہم تبدیلی ہے۔ Microsoft Foundry پر موجود موجودہ، غیر منسوخ شدہ ماڈلز **reasoning models** ہیں (GPT-5 فیملی، o-series) - اور یہ **`temperature` یا `top_p` کو سپورٹ نہیں کرتے** (نہ ہی `max_tokens`؛ `max_output_tokens استعمال کریں`)۔ اگر آپ `gpt-5-mini` کو `temperature` بھیجیں گے تو "parameter not supported" کی خرابی آئے گی۔ اس لیے temperature کی مثال آزمانے کے لیے، ایسے ماڈل کا انتخاب کریں جو سیمپلنگ کنٹرولز کو سپورٹ کرتا ہو - مثلاً ایک اوپن **Llama** ماڈل جیسے `Llama-3.3-70B-Instruct` Microsoft Foundry ماڈل کیٹلاگ سے، جو Foundry Models / Azure AI Inference اینڈپوائنٹ کے ذریعے کال کیا جائے (جیسا کہ `githubmodels-*` مثالوں میں کیا گیا ہے)۔ GPT-5 جیسے reasoning models کے لیے آپ آؤٹ پٹ کو مختلف طریقے سے کنٹرول کرتے ہیں:
  - **پرومپٹ انجینئرنگ** - واضح ہدایات، مثالیں، اور منظم آؤٹ پٹ (سبق [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst) دیکھیں) وہ کام کرتے ہیں جو سیمپلنگ کنٹرولز کرتے تھے۔
  - **reasoning controls** - ایسے پیرامیٹرز جو reasoning کی کوشش/تفصیل کو دیر اور لاگت کے توازن کے ساتھ جوڑتے ہیں۔

  مختصر یہ کہ: `temperature`/`top_p` بہت سے ماڈلز (Llama, Mistral, Phi, اور GPT-4.x فیملی - البتہ GPT-4.x ختم ہو رہا ہے) پر اب بھی قابل قبول ہیں، لیکن سمت prompt engineering + reasoning controls کی طرف ہے reasoning models جیسے GPT-5 کے لیے۔

## اسائنمنٹ

اس اسائنمنٹ کے لیے، آپ خود فیصلہ کر سکتے ہیں کہ کیا بنانا ہے۔

یہاں کچھ تجاویز دی گئی ہیں:

- recipe generator ایپ کو مزید بہتر بنانے کے لیے اسے ایڈجسٹ کریں۔ temperature کی قدرات اور پرومپٹس کے ساتھ تجربہ کریں تاکہ آپ کو کیا بنا سکتے ہیں دیکھیں۔
- ایک "study buddy" بنائیں۔ یہ ایپ کسی موضوع پر سوالات کا جواب دے سکے، جیسے Python کے موضوع پر، آپ کے پاس ایسے پرومپٹس ہو سکتے ہیں جیسے "Python کا یہ موضوع کیا ہے؟"، یا آپ ایسی پرومپٹ دے سکتے ہیں جو کہتی ہو، مجھے کسی موضوع کے لیے کوڈ دکھائیں وغیرہ۔
- History bot، تاریخ کو زندہ کریں، بوٹ کو کسی تاریخی کردار کے طور پر ادا کرنے کی ہدایت دیں اور اس کی زندگی اور دور کے بارے میں سوالات پوچھیں۔

## حل

### Study buddy

نیچے ایک اسٹارٹر پرومپٹ دیا گیا ہے، دیکھیں آپ اسے کیسے استعمال کر سکتے ہیں اور اپنی مرضی کے مطابق ایڈجسٹ کر سکتے ہیں۔

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### History bot

آپ درج ذیل پرومپٹس استعمال کر سکتے ہیں:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## معلومات چیک کریں

temperature کا تصور کیا کرتا ہے؟

1. یہ کنٹرول کرتا ہے کہ آؤٹ پٹ کتنا بے ترتیب ہو۔
1. یہ کنٹرول کرتا ہے کہ جواب کتنا بڑا ہو۔
1. یہ کنٹرول کرتا ہے کہ کتنے ٹوکنز استعمال ہوتے ہیں۔

## 🚀 چیلنج

اس اسائنمنٹ پر کام کرتے ہوئے، temperature کی قیمتوں کو تبدیل کرنے کی کوشش کریں، اسے 0، 0.5، اور 1 پر سیٹ کریں۔ یاد رکھیں کہ 0 سب سے کم تبدیلی ہے اور 1 سب سے زیادہ۔ آپ کی ایپ کے لیے کون سی قیمت بہترین کام کرتی ہے؟

## زبردست کام! اپنی سیکھنے کا سلسلہ جاری رکھیں

اس سبق کو مکمل کرنے کے بعد، ہماری [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) دیکھیں تاکہ اپنی Generative AI کی معلومات کو مزید بڑھائیں!

سب سے آگے بڑھیں اور سبق 7 پر جائیں جہاں ہم دیکھیں گے کہ کیسے [chat applications بنائی جائیں](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->