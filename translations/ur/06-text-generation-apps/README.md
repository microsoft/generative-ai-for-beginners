<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-06-25T14:00:00+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "ur"
}
-->
# ٹیکسٹ جنریشن ایپلی کیشنز بنانا

آپ نے اس نصاب کے ذریعے اب تک دیکھا ہے کہ کچھ بنیادی تصورات جیسے پرومپٹس ہیں اور یہاں تک کہ "پرومپٹ انجینئرنگ" نامی ایک پوری ڈسپلن بھی ہے۔ بہت سے ٹولز جن کے ساتھ آپ تعامل کر سکتے ہیں جیسے ChatGPT، Office 365، Microsoft Power Platform وغیرہ، آپ کو پرومپٹس استعمال کرنے کی حمایت کرتے ہیں تاکہ کچھ حاصل کیا جا سکے۔

کسی ایپ میں اس طرح کا تجربہ شامل کرنے کے لیے، آپ کو پرومپٹس، کمپلیشنز جیسے تصورات کو سمجھنے کی ضرورت ہے اور کام کرنے کے لیے ایک لائبریری کا انتخاب کرنا ہوگا۔ یہی چیز آپ اس باب میں سیکھیں گے۔

## تعارف

اس باب میں، آپ:

- openai لائبریری اور اس کے بنیادی تصورات کے بارے میں سیکھیں گے۔
- openai کا استعمال کرتے ہوئے ایک ٹیکسٹ جنریشن ایپ بنائیں گے۔
- پرومپٹ، درجہ حرارت، اور ٹوکنز جیسے تصورات کو استعمال کرنے کا طریقہ سمجھیں گے تاکہ ایک ٹیکسٹ جنریشن ایپ بنائی جا سکے۔

## سیکھنے کے مقاصد

اس سبق کے آخر میں، آپ قابل ہوں گے:

- وضاحت کریں کہ ایک ٹیکسٹ جنریشن ایپ کیا ہے۔
- openai کا استعمال کرتے ہوئے ایک ٹیکسٹ جنریشن ایپ بنائیں۔
- اپنے ایپ کو زیادہ یا کم ٹوکنز استعمال کرنے کے لیے ترتیب دیں اور ساتھ ہی درجہ حرارت کو تبدیل کریں، مختلف نتائج کے لیے۔

## ٹیکسٹ جنریشن ایپ کیا ہے؟

عام طور پر جب آپ کوئی ایپ بناتے ہیں تو اس میں کچھ قسم کا انٹرفیس ہوتا ہے جیسے:

- کمانڈ پر مبنی۔ کونسول ایپس عام ایپس ہیں جہاں آپ ایک کمانڈ ٹائپ کرتے ہیں اور یہ ایک کام انجام دیتی ہے۔ مثال کے طور پر، `git` ایک کمانڈ پر مبنی ایپ ہے۔
- یوزر انٹرفیس (UI)۔ کچھ ایپس کے گرافیکل یوزر انٹرفیس (GUIs) ہوتے ہیں جہاں آپ بٹن کلک کرتے ہیں، متن داخل کرتے ہیں، اختیارات منتخب کرتے ہیں وغیرہ۔

### کونسول اور UI ایپس محدود ہیں

اسے کمانڈ پر مبنی ایپ سے موازنہ کریں جہاں آپ ایک کمانڈ ٹائپ کرتے ہیں:

- **یہ محدود ہے**۔ آپ صرف وہی کمانڈ ٹائپ نہیں کر سکتے، صرف وہی جو ایپ سپورٹ کرتی ہے۔
- **زبان مخصوص**۔ کچھ ایپس بہت سی زبانوں کی حمایت کرتی ہیں، لیکن ڈیفالٹ کے طور پر ایپ ایک مخصوص زبان کے لیے بنائی گئی ہے، چاہے آپ مزید زبان کی حمایت شامل کر سکیں۔

### ٹیکسٹ جنریشن ایپس کے فوائد

تو ایک ٹیکسٹ جنریشن ایپ مختلف کیسے ہے؟

ایک ٹیکسٹ جنریشن ایپ میں، آپ کے پاس زیادہ لچک ہوتی ہے، آپ کمانڈز کے سیٹ یا مخصوص ان پٹ زبان تک محدود نہیں ہوتے۔ اس کے بجائے، آپ قدرتی زبان کا استعمال کرتے ہوئے ایپ کے ساتھ تعامل کر سکتے ہیں۔ ایک اور فائدہ یہ ہے کہ کیونکہ آپ پہلے سے ہی ایک ڈیٹا سورس کے ساتھ تعامل کر رہے ہیں جو معلومات کے وسیع ذخیرے پر تربیت یافتہ ہے، جبکہ ایک روایتی ایپ ممکنہ طور پر ڈیٹا بیس میں موجود چیزوں تک محدود ہو سکتی ہے۔

### میں ٹیکسٹ جنریشن ایپ کے ساتھ کیا بنا سکتا ہوں؟

بہت سی چیزیں ہیں جنہیں آپ بنا سکتے ہیں۔ مثال کے طور پر:

- **ایک چیٹ بوٹ**۔ ایک چیٹ بوٹ جو آپ کی کمپنی اور اس کی مصنوعات جیسے موضوعات کے بارے میں سوالات کے جواب دے سکتا ہے۔
- **مددگار**۔ LLMs متن کو خلاصہ کرنے، متن سے بصیرت حاصل کرنے، ریزیومے جیسے متن تیار کرنے اور مزید چیزوں میں بہترین ہیں۔
- **کوڈ اسسٹنٹ**۔ اس زبان کے ماڈل پر منحصر ہے جسے آپ استعمال کرتے ہیں، آپ ایک کوڈ اسسٹنٹ بنا سکتے ہیں جو آپ کو کوڈ لکھنے میں مدد دے۔ مثال کے طور پر، آپ GitHub Copilot جیسے پروڈکٹ کے ساتھ ساتھ ChatGPT کو بھی کوڈ لکھنے میں مدد کے لیے استعمال کر سکتے ہیں۔

## میں کیسے شروع کر سکتا ہوں؟

ٹھیک ہے، آپ کو LLM کے ساتھ انٹیگریٹ کرنے کا ایک طریقہ تلاش کرنے کی ضرورت ہے جو عام طور پر درج ذیل دو طریقوں پر مشتمل ہوتا ہے:

- ایک API استعمال کریں۔ یہاں آپ اپنے پرومپٹ کے ساتھ ویب درخواستیں بنا رہے ہیں اور واپس جنریٹڈ ٹیکسٹ حاصل کر رہے ہیں۔
- ایک لائبریری استعمال کریں۔ لائبریریاں API کالز کو انکیپسولیٹ کرنے میں مدد کرتی ہیں اور انہیں استعمال میں آسان بناتی ہیں۔

## لائبریریاں/SDKs

LLMs کے ساتھ کام کرنے کے لیے کچھ مشہور لائبریریاں ہیں جیسے:

- **openai**، یہ لائبریری آپ کے ماڈل سے جڑنا اور پرومپٹس بھیجنا آسان بناتی ہے۔

پھر کچھ لائبریریاں ہیں جو اعلی سطح پر کام کرتی ہیں جیسے:

- **Langchain**۔ Langchain مشہور ہے اور Python کی حمایت کرتا ہے۔
- **Semantic Kernel**۔ Semantic Kernel Microsoft کی لائبریری ہے جو C#, Python، اور Java زبانوں کی حمایت کرتی ہے۔

## openai کا استعمال کرتے ہوئے پہلی ایپ

آئیے دیکھتے ہیں کہ ہم اپنی پہلی ایپ کیسے بنا سکتے ہیں، ہمیں کون سی لائبریریاں درکار ہیں، کتنا ضروری ہے وغیرہ۔

### openai انسٹال کریں

بہت سی لائبریریاں موجود ہیں جو OpenAI یا Azure OpenAI کے ساتھ تعامل کرتی ہیں۔ متعدد پروگرامنگ زبانوں کا استعمال ممکن ہے جیسے C#, Python, JavaScript, Java اور مزید۔ ہم نے `openai` Python لائبریری کا انتخاب کیا ہے، لہذا ہم `pip` کا استعمال کریں گے اسے انسٹال کرنے کے لیے۔

```bash
pip install openai
```

### ایک ریسورس بنائیں

آپ کو درج ذیل اقدامات کرنے کی ضرورت ہے:

- Azure پر ایک اکاؤنٹ بنائیں [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)۔
- Azure OpenAI تک رسائی حاصل کریں۔ [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) پر جائیں اور رسائی کی درخواست کریں۔

  > [!NOTE]
  > لکھنے کے وقت، آپ کو Azure OpenAI تک رسائی کے لیے درخواست دینے کی ضرورت ہے۔

- Python انسٹال کریں <https://www.python.org/>
- ایک Azure OpenAI سروس ریسورس بنایا ہو۔ اس گائیڈ کو دیکھیں کہ کیسے [ایک ریسورس بنائیں](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)۔

### API کلید اور اینڈ پوائنٹ کا پتہ لگائیں

اس وقت، آپ کو اپنی `openai` لائبریری کو بتانا ہوگا کہ کون سی API کلید استعمال کرنی ہے۔ اپنی API کلید تلاش کرنے کے لیے، اپنے Azure OpenAI ریسورس کے "Keys and Endpoint" سیکشن میں جائیں اور "Key 1" ویلیو کو کاپی کریں۔

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

اب جب کہ آپ نے یہ معلومات کاپی کر لی ہیں، آئیے لائبریریوں کو اسے استعمال کرنے کی ہدایت دیں۔

> [!NOTE]
> اپنی API کلید کو اپنے کوڈ سے الگ کرنا بہتر ہے۔ آپ ایسا ماحول کے متغیرات کا استعمال کرتے ہوئے کر سکتے ہیں۔
>
> - ماحول کے متغیر کو سیٹ کریں `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'`

### Azure کی تشکیل کا سیٹ اپ

اگر آپ Azure OpenAI استعمال کر رہے ہیں، تو یہاں آپ تشکیل کا سیٹ اپ کیسے کریں:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

اوپر ہم درج ذیل سیٹ کر رہے ہیں:

- `api_type` to `azure`. This tells the library to use Azure OpenAI and not OpenAI.
- `api_key`, this is your API key found in the Azure Portal.
- `api_version`, this is the version of the API you want to use. At the time of writing, the latest version is `2023-05-15`.
- `api_base`, this is the endpoint of the API. You can find it in the Azure Portal next to your API key.

> [!NOTE] > `os.getenv` is a function that reads environment variables. You can use it to read environment variables like `OPENAI_API_KEY` and `API_BASE`. Set these environment variables in your terminal or by using a library like `dotenv`.

## Generate text

The way to generate text is to use the `Completion` کلاس۔ یہاں ایک مثال ہے:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

اوپر کے کوڈ میں، ہم ایک کمپلیشن آبجیکٹ بناتے ہیں اور ماڈل کو پاس کرتے ہیں جسے ہم استعمال کرنا چاہتے ہیں اور پرومپٹ کو بھی۔ پھر ہم جنریٹڈ ٹیکسٹ کو پرنٹ کرتے ہیں۔

### چیٹ کمپلیشنز

اب تک، آپ نے دیکھا ہے کہ ہم `Completion` to generate text. But there's another class called `ChatCompletion` کا استعمال کر رہے ہیں جو چیٹ بوٹس کے لیے زیادہ موزوں ہے۔ یہاں اسے استعمال کرنے کی ایک مثال ہے:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

اس فعالیت کے بارے میں مزید معلومات ایک آنے والے باب میں۔

## مشق - آپ کی پہلی ٹیکسٹ جنریشن ایپ

اب جب کہ ہم نے openai کو سیٹ اپ اور کنفیگر کرنے کا طریقہ سیکھ لیا ہے، یہ آپ کی پہلی ٹیکسٹ جنریشن ایپ بنانے کا وقت ہے۔ اپنی ایپ بنانے کے لیے، ان اقدامات پر عمل کریں:

1. ایک ورچوئل ماحول بنائیں اور openai انسٹال کریں:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > اگر آپ Windows استعمال کر رہے ہیں تو ٹائپ کریں `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1` ویلیو۔

1. ایک _app.py_ فائل بنائیں اور اسے درج ذیل کوڈ دیں:

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
   > اگر آپ Azure OpenAI استعمال کر رہے ہیں، تو آپ کو `api_type` to `azure` and set the `api_key` کو اپنی Azure OpenAI کلید پر سیٹ کرنے کی ضرورت ہے۔

   آپ کو درج ذیل کے جیسا آؤٹ پٹ دیکھنا چاہیے:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## مختلف چیزوں کے لیے مختلف قسم کے پرومپٹس

اب آپ نے دیکھا ہے کہ کیسے ایک پرومپٹ کا استعمال کرتے ہوئے ٹیکسٹ جنریٹ کیا جا سکتا ہے۔ آپ کے پاس ایک پروگرام چل رہا ہے جسے آپ تبدیل کر سکتے ہیں اور مختلف قسم کے ٹیکسٹ جنریٹ کرنے کے لیے تبدیل کر سکتے ہیں۔

پرومپٹس مختلف قسم کے کاموں کے لیے استعمال کیے جا سکتے ہیں۔ مثال کے طور پر:

- **ٹیکسٹ کی ایک قسم جنریٹ کریں**۔ مثال کے طور پر، آپ ایک نظم، کوئز کے لیے سوالات وغیرہ جنریٹ کر سکتے ہیں۔
- **معلومات کی تلاش**۔ آپ پرومپٹس کا استعمال معلومات تلاش کرنے کے لیے کر سکتے ہیں جیسے درج ذیل مثال 'ویب ڈویلپمنٹ میں CORS کا کیا مطلب ہے؟'۔
- **کوڈ جنریٹ کریں**۔ آپ پرومپٹس کا استعمال کوڈ جنریٹ کرنے کے لیے کر سکتے ہیں، مثال کے طور پر ای میلز کی توثیق کرنے کے لیے استعمال ہونے والا ایک باقاعدہ اظہار تیار کرنا یا کیوں نہ ایک پورا پروگرام جنریٹ کریں، جیسے ایک ویب ایپ؟

## ایک زیادہ عملی استعمال: ایک ترکیب جنریٹر

تصور کریں کہ آپ کے پاس گھر میں اجزاء ہیں اور آپ کچھ پکانا چاہتے ہیں۔ اس کے لیے، آپ کو ایک ترکیب کی ضرورت ہے۔ ترکیبیں تلاش کرنے کا ایک طریقہ سرچ انجن کا استعمال ہے یا آپ ایسا کرنے کے لیے ایک LLM کا استعمال کر سکتے ہیں۔

آپ اس طرح ایک پرومپٹ لکھ سکتے ہیں:

> "مجھے درج ذیل اجزاء کے ساتھ ایک ڈش کے لیے 5 ترکیبیں دکھائیں: چکن، آلو، اور گاجر۔ ہر ترکیب کے لیے، استعمال ہونے والے تمام اجزاء کی فہرست بنائیں"

اوپر کے پرومپٹ کے پیش نظر، آپ کو ممکنہ طور پر درج ذیل جیسا جواب مل سکتا ہے:

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

یہ نتیجہ بہت اچھا ہے، مجھے معلوم ہے کہ کیا پکانا ہے۔ اس وقت، کیا مفید بہتری ہو سکتی ہے:

- وہ اجزاء فلٹر کرنا جو مجھے پسند نہیں ہیں یا جن سے مجھے الرجی ہے۔
- خریداری کی فہرست تیار کریں، اگر میرے پاس گھر میں تمام اجزاء نہیں ہیں۔

اوپر کے معاملات کے لیے، آئیے ایک اضافی پرومپٹ شامل کریں:

> "براہ کرم لہسن والی ترکیبیں ہٹا دیں کیونکہ مجھے اس سے الرجی ہے اور اسے کسی اور چیز سے بدل دیں۔ نیز، براہ کرم ترکیبوں کے لیے خریداری کی فہرست تیار کریں، اس بات کو مدنظر رکھتے ہوئے کہ میرے پاس پہلے سے ہی چکن، آلو اور گاجر گھر میں ہیں۔"

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

یہ آپ کی پانچ ترکیبیں ہیں، بغیر لہسن کا ذکر کیے اور آپ کے پاس ایک خریداری کی فہرست بھی ہے جس میں یہ بھی شامل ہے کہ آپ کے پاس گھر میں پہلے سے کیا موجود ہے۔

## مشق - ایک ترکیب جنریٹر بنائیں

اب جب کہ ہم نے ایک منظر نامہ کھیلا ہے، آئیے کوڈ لکھتے ہیں تاکہ مظاہرہ شدہ منظر نامے سے مطابقت ہو۔ ایسا کرنے کے لیے، ان اقدامات پر عمل کریں:

1. موجودہ _app.py_ فائل کو ایک نقطہ آغاز کے طور پر استعمال کریں
1. `prompt` ویریبل کو تلاش کریں اور اس کے کوڈ کو درج ذیل میں تبدیل کریں:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   اگر آپ اب کوڈ چلائیں تو آپ کو درج ذیل کے جیسا آؤٹ پٹ دیکھنا چاہیے:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > نوٹ، آپ کا LLM غیر متعین ہے، لہذا آپ کو ہر بار پروگرام چلانے پر مختلف نتائج مل سکتے ہیں۔

   زبردست، آئیے دیکھتے ہیں کہ ہم چیزوں کو کیسے بہتر بنا سکتے ہیں۔ چیزوں کو بہتر بنانے کے لیے، ہم چاہتے ہیں کہ کوڈ لچکدار ہو، تاکہ اجزاء اور ترکیبوں کی تعداد کو بہتر بنایا جا سکے اور تبدیل کیا جا سکے۔

1. آئیے کوڈ کو درج ذیل طریقے سے تبدیل کریں:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   کوڈ کو ٹیسٹ چلانے کے لیے لے جانا، اس طرح نظر آ سکتا ہے:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### فلٹر اور خریداری کی فہرست شامل کرکے بہتر بنائیں

اب ہمارے پاس ایک کام کرنے والی ایپ ہے جو ترکیبیں تیار کرنے کے قابل ہے اور یہ لچکدار ہے کیونکہ یہ صارف سے ان پٹ پر انحصار کرتی ہے، نہ صرف ترکیبوں کی تعداد پر بلکہ استعمال شدہ اجزاء پر بھی۔

اسے مزید بہتر بنانے کے لیے، ہم درج ذیل شامل کرنا چاہتے ہیں:

- **اجزاء کو فلٹر کریں**۔ ہم ان اجزاء کو فلٹر کرنے کے قابل ہونا چاہتے ہیں جنہیں ہم پسند نہیں کرتے یا جن سے ہمیں الرجی ہے۔ اس تبدیلی کو پورا کرنے کے لیے، ہم اپنے موجودہ پرومپٹ میں ترمیم کر سکتے ہیں اور اسے اس طرح کے فلٹر کنڈیشن کو آخر میں شامل کر سکتے ہیں:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  اوپر، ہم پرومپٹ کے آخر میں `{filter}` شامل کرتے ہیں اور ہم صارف سے فلٹر ویلیو کو بھی حاصل کرتے ہیں۔

  پروگرام چلانے کے لیے ایک مثال ان پٹ اب اس طرح نظر آ سکتا ہے:

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

  جیسا کہ آپ دیکھ سکتے ہیں، اس میں دودھ والی کوئی ترکیبیں فلٹر کی گئی ہیں۔ لیکن، اگر آپ کو لیکٹوز کی عدم برداشت ہے، تو آپ ممکنہ طور پر ایسی ترکیبوں کو بھی فلٹر کرنا چاہتے ہیں جن میں پنیر شامل ہو، لہذا واضح ہونے کی ضرورت ہے۔

- **خریداری کی فہرست تیار کریں**۔ ہم چاہتے ہیں کہ ایک خریداری کی فہرست تیار کی جائے، اس بات کو مدنظر رکھتے ہوئے کہ ہمارے پاس پہلے سے گھر میں کیا موجود ہے۔

  اس فعالیت کے لیے، ہم یا تو سب کچھ ایک پرومپٹ میں حل کرنے کی کوشش کر سکتے ہیں یا ہم اسے دو پرومپٹس میں تقسیم کر سکتے ہیں۔ آئیے دوسرے طریقہ کی کوشش کرتے ہیں۔ یہاں ہم ایک اضافی پرومپٹ شامل کرنے کی تجویز کر رہے ہیں، لیکن اس کے کام کرنے کے لیے، ہمیں پہلے پرومپٹ کے نتیجے کو دوسرے پرومپٹ کے لیے سیاق و سباق کے طور پر شامل کرنے کی ضرورت ہے۔

  کوڈ کے اس حصے کو تلاش کریں جو پہلے پرومپٹ کے نتیجے کو پرنٹ کرتا ہے اور اس کے نیچے درج ذیل کوڈ شامل کریں:

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

  درج ذیل باتوں کا نوٹ لیں:

  1. ہم پہلے پرومپٹ کے نتیجے کو نئے پرومپٹ میں شامل کر کے ایک نیا پرومپٹ بنا رہے ہیں:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. ہم ایک نئی درخواست بنا رہے ہیں، لیکن اس بار ہم کہتے ہیں `max_tokens` 1200 ہے، پہلے پرومپٹ میں ہم نے جتنے ٹوکن مانگے تھے۔

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     اس کوڈ کو چکر میں لے جانے کے لیے، اب ہم درج ذیل آؤٹ پٹ پر پہنچتے ہیں:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## اپنی سیٹ اپ کو بہتر بنائیں

اب تک ہمارے پاس کام کرنے والا کوڈ ہے، لیکن کچھ چیزیں ہیں جو ہمیں چیزوں کو مزید بہتر بنانے کے لیے کرنی چاہئیں۔ کچھ چیزیں جو ہمیں کرنی چاہئیں وہ ہیں:

- **کوڈ سے خفیہ معلومات کو الگ کریں**، جیسے API کلید۔ خفیہ معلومات کوڈ میں نہیں ہونی چاہئیں اور انہیں محفوظ جگہ پر ذخیرہ کیا جانا چاہیے۔ کوڈ سے خ

**دستبرداری**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا نقائص ہو سکتے ہیں۔ اصل دستاویز کو اس کی مقامی زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمہ کے استعمال سے پیدا ہونے والے کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔