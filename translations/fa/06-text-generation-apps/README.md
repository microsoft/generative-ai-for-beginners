<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df027997f1448323d6159b78a1b669bf",
  "translation_date": "2025-10-17T23:06:52+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "fa"
}
-->
# ساخت برنامه‌های تولید متن

[![ساخت برنامه‌های تولید متن](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.fa.png)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(برای مشاهده ویدئوی این درس، روی تصویر بالا کلیک کنید)_

تا اینجا در این دوره آموزشی، مفاهیم اصلی مانند پرامپت‌ها و حتی یک رشته کامل به نام "مهندسی پرامپت" را دیده‌اید. بسیاری از ابزارهایی که می‌توانید با آن‌ها تعامل داشته باشید، مانند ChatGPT، Office 365، Microsoft Power Platform و موارد دیگر، از شما پشتیبانی می‌کنند تا با استفاده از پرامپت‌ها کاری را انجام دهید.

برای اینکه بتوانید چنین تجربه‌ای را به یک اپلیکیشن اضافه کنید، باید مفاهیمی مانند پرامپت‌ها، تکمیل‌ها و انتخاب یک کتابخانه برای کار را درک کنید. این دقیقاً چیزی است که در این فصل یاد خواهید گرفت.

## مقدمه

در این فصل، شما:

- با کتابخانه openai و مفاهیم اصلی آن آشنا خواهید شد.
- یک اپلیکیشن تولید متن با استفاده از openai خواهید ساخت.
- یاد خواهید گرفت که چگونه از مفاهیمی مانند پرامپت، دما و توکن‌ها برای ساخت یک اپلیکیشن تولید متن استفاده کنید.

## اهداف یادگیری

در پایان این درس، شما قادر خواهید بود:

- توضیح دهید که اپلیکیشن تولید متن چیست.
- یک اپلیکیشن تولید متن با استفاده از openai بسازید.
- اپلیکیشن خود را برای استفاده از تعداد بیشتر یا کمتر توکن‌ها و همچنین تغییر دما برای خروجی متنوع تنظیم کنید.

## اپلیکیشن تولید متن چیست؟

معمولاً وقتی یک اپلیکیشن می‌سازید، نوعی رابط دارد مانند موارد زیر:

- مبتنی بر فرمان. اپلیکیشن‌های کنسولی معمولاً اپلیکیشن‌هایی هستند که در آن‌ها یک فرمان تایپ می‌کنید و وظیفه‌ای انجام می‌شود. به عنوان مثال، `git` یک اپلیکیشن مبتنی بر فرمان است.
- رابط کاربری (UI). برخی اپلیکیشن‌ها دارای رابط‌های کاربری گرافیکی (GUI) هستند که در آن‌ها دکمه‌ها را کلیک می‌کنید، متن وارد می‌کنید، گزینه‌ها را انتخاب می‌کنید و موارد دیگر.

### محدودیت‌های اپلیکیشن‌های کنسولی و رابط کاربری

آن را با یک اپلیکیشن مبتنی بر فرمان که در آن یک فرمان تایپ می‌کنید مقایسه کنید:

- **محدود است**. نمی‌توانید هر فرمانی را تایپ کنید، فقط فرمان‌هایی که اپلیکیشن پشتیبانی می‌کند.
- **زبان خاص**. برخی اپلیکیشن‌ها از زبان‌های زیادی پشتیبانی می‌کنند، اما به طور پیش‌فرض اپلیکیشن برای یک زبان خاص ساخته شده است، حتی اگر بتوانید پشتیبانی زبان‌های بیشتری را اضافه کنید.

### مزایای اپلیکیشن‌های تولید متن

پس چگونه یک اپلیکیشن تولید متن متفاوت است؟

در یک اپلیکیشن تولید متن، شما انعطاف بیشتری دارید، محدود به مجموعه‌ای از فرمان‌ها یا یک زبان ورودی خاص نیستید. در عوض، می‌توانید از زبان طبیعی برای تعامل با اپلیکیشن استفاده کنید. مزیت دیگر این است که شما در حال تعامل با یک منبع داده هستید که بر اساس یک مجموعه وسیع از اطلاعات آموزش دیده است، در حالی که یک اپلیکیشن سنتی ممکن است محدود به آنچه در یک پایگاه داده است باشد.

### با یک اپلیکیشن تولید متن چه چیزی می‌توان ساخت؟

چیزهای زیادی وجود دارد که می‌توانید بسازید. به عنوان مثال:

- **یک چت‌بات**. یک چت‌بات که به سوالات درباره موضوعات مختلف، مانند شرکت شما و محصولات آن پاسخ می‌دهد، می‌تواند گزینه خوبی باشد.
- **دستیار**. مدل‌های زبانی بزرگ (LLM) در کارهایی مانند خلاصه‌سازی متن، دریافت بینش از متن، تولید متن مانند رزومه‌ها و موارد دیگر عالی هستند.
- **دستیار کدنویسی**. بسته به مدل زبانی که استفاده می‌کنید، می‌توانید یک دستیار کدنویسی بسازید که به شما در نوشتن کد کمک کند. به عنوان مثال، می‌توانید از محصولاتی مانند GitHub Copilot و همچنین ChatGPT برای کمک به نوشتن کد استفاده کنید.

## چگونه می‌توانم شروع کنم؟

خب، شما باید راهی برای ادغام با یک مدل زبانی بزرگ پیدا کنید که معمولاً شامل دو روش زیر است:

- استفاده از API. در اینجا شما درخواست‌های وب را با پرامپت خود می‌سازید و متن تولید شده را دریافت می‌کنید.
- استفاده از کتابخانه. کتابخانه‌ها به شما کمک می‌کنند تا تماس‌های API را کپسوله کنید و استفاده از آن‌ها را آسان‌تر کنید.

## کتابخانه‌ها/SDKها

چندین کتابخانه شناخته شده برای کار با مدل‌های زبانی بزرگ وجود دارد، مانند:

- **openai**، این کتابخانه اتصال به مدل شما و ارسال پرامپت‌ها را آسان می‌کند.

سپس کتابخانه‌هایی وجود دارند که در سطح بالاتری عمل می‌کنند، مانند:

- **Langchain**. Langchain شناخته شده است و از زبان پایتون پشتیبانی می‌کند.
- **Semantic Kernel**. Semantic Kernel یک کتابخانه از مایکروسافت است که از زبان‌های C#، پایتون و جاوا پشتیبانی می‌کند.

## اولین اپلیکیشن با استفاده از openai

بیایید ببینیم چگونه می‌توانیم اولین اپلیکیشن خود را بسازیم، چه کتابخانه‌هایی نیاز داریم، چقدر لازم است و غیره.

### نصب openai

کتابخانه‌های زیادی برای تعامل با OpenAI یا Azure OpenAI وجود دارد. امکان استفاده از زبان‌های برنامه‌نویسی مختلف مانند C#، پایتون، جاوااسکریپت، جاوا و موارد دیگر نیز وجود دارد. ما تصمیم گرفته‌ایم از کتابخانه پایتون `openai` استفاده کنیم، بنابراین از `pip` برای نصب آن استفاده خواهیم کرد.

```bash
pip install openai
```

### ایجاد یک منبع

شما باید مراحل زیر را انجام دهید:

- یک حساب کاربری در Azure ایجاد کنید [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- به Azure OpenAI دسترسی پیدا کنید. به [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) بروید و درخواست دسترسی دهید.

  > [!NOTE]
  > در زمان نوشتن این متن، شما باید برای دسترسی به Azure OpenAI درخواست دهید.

- پایتون را نصب کنید <https://www.python.org/>
- یک منبع سرویس Azure OpenAI ایجاد کنید. این راهنما را برای نحوه [ایجاد یک منبع](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst) ببینید.

### پیدا کردن کلید API و نقطه پایانی

در این مرحله، شما باید به کتابخانه `openai` خود بگویید که از کدام کلید API استفاده کند. برای پیدا کردن کلید API خود، به بخش "Keys and Endpoint" در منبع Azure OpenAI خود بروید و مقدار "Key 1" را کپی کنید.

![بخش Keys and Endpoint در Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

حالا که این اطلاعات را کپی کرده‌اید، بیایید به کتابخانه‌ها دستور دهیم که از آن استفاده کنند.

> [!NOTE]
> ارزش دارد که کلید API خود را از کد جدا کنید. می‌توانید این کار را با استفاده از متغیرهای محیطی انجام دهید.
>
> - متغیر محیطی `OPENAI_API_KEY` را به کلید API خود تنظیم کنید.
>   `export OPENAI_API_KEY='sk-...'`

### تنظیم پیکربندی Azure

اگر از Azure OpenAI استفاده می‌کنید، در اینجا نحوه تنظیم پیکربندی آمده است:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

در بالا، موارد زیر را تنظیم کرده‌ایم:

- `api_type` به `azure`. این به کتابخانه می‌گوید که از Azure OpenAI استفاده کند و نه OpenAI.
- `api_key`، این کلید API شما است که در Azure Portal پیدا می‌شود.
- `api_version`، این نسخه API است که می‌خواهید استفاده کنید. در زمان نوشتن این متن، آخرین نسخه `2023-05-15` است.
- `api_base`، این نقطه پایانی API است. می‌توانید آن را در Azure Portal در کنار کلید API خود پیدا کنید.

> [!NOTE] > `os.getenv` یک تابع است که متغیرهای محیطی را می‌خواند. می‌توانید از آن برای خواندن متغیرهای محیطی مانند `OPENAI_API_KEY` و `API_BASE` استفاده کنید. این متغیرهای محیطی را در ترمینال خود تنظیم کنید یا از کتابخانه‌ای مانند `dotenv` استفاده کنید.

## تولید متن

راه تولید متن استفاده از کلاس `Completion` است. در اینجا یک مثال آورده شده است:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

در کد بالا، یک شیء تکمیل ایجاد می‌کنیم و مدل مورد نظر و پرامپت را به آن می‌دهیم. سپس متن تولید شده را چاپ می‌کنیم.

### تکمیل‌های چت

تا اینجا، دیده‌اید که چگونه از `Completion` برای تولید متن استفاده کرده‌ایم. اما یک کلاس دیگر به نام `ChatCompletion` وجود دارد که برای چت‌بات‌ها مناسب‌تر است. در اینجا یک مثال از استفاده از آن آورده شده است:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

بیشتر درباره این قابلیت در فصل‌های آینده.

## تمرین - اولین اپلیکیشن تولید متن شما

حالا که یاد گرفتیم چگونه openai را تنظیم و پیکربندی کنیم، وقت آن است که اولین اپلیکیشن تولید متن خود را بسازیم. برای ساخت اپلیکیشن خود، مراحل زیر را دنبال کنید:

1. یک محیط مجازی ایجاد کنید و openai را نصب کنید:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > اگر از ویندوز استفاده می‌کنید، به جای `source venv/bin/activate` تایپ کنید `venv\Scripts\activate`.

   > [!NOTE]
   > کلید Azure OpenAI خود را با رفتن به [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) پیدا کنید و `Open AI` را جستجو کنید، سپس منبع `Open AI` را انتخاب کنید و سپس `Keys and Endpoint` را انتخاب کنید و مقدار `Key 1` را کپی کنید.

1. یک فایل _app.py_ ایجاد کنید و کد زیر را در آن قرار دهید:

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
   > اگر از Azure OpenAI استفاده می‌کنید، باید `api_type` را به `azure` تنظیم کنید و `api_key` را به کلید Azure OpenAI خود تنظیم کنید.

   شما باید خروجی‌ای مشابه زیر را مشاهده کنید:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## انواع مختلف پرامپت‌ها برای کارهای مختلف

حالا دیده‌اید که چگونه می‌توان با استفاده از یک پرامپت متن تولید کرد. شما حتی یک برنامه در حال اجرا دارید که می‌توانید آن را تغییر دهید و برای تولید انواع مختلف متن اصلاح کنید.

پرامپت‌ها می‌توانند برای انواع وظایف استفاده شوند. به عنوان مثال:

- **تولید نوعی متن**. به عنوان مثال، می‌توانید یک شعر، سوالات برای یک آزمون و غیره تولید کنید.
- **جستجوی اطلاعات**. می‌توانید از پرامپت‌ها برای جستجوی اطلاعات استفاده کنید، مانند مثال زیر: 'CORS در توسعه وب به چه معناست؟'.
- **تولید کد**. می‌توانید از پرامپت‌ها برای تولید کد استفاده کنید، به عنوان مثال توسعه یک عبارت منظم برای اعتبارسنجی ایمیل‌ها یا حتی تولید یک برنامه کامل، مانند یک اپلیکیشن وب.

## یک مورد استفاده عملی‌تر: تولید کننده دستور پخت

تصور کنید که در خانه مواد غذایی دارید و می‌خواهید چیزی بپزید. برای این کار، به یک دستور پخت نیاز دارید. یک راه برای پیدا کردن دستور پخت استفاده از موتور جستجو است یا می‌توانید از یک مدل زبانی بزرگ برای این کار استفاده کنید.

می‌توانید یک پرامپت به این صورت بنویسید:

> "5 دستور پخت برای یک غذا با مواد زیر: مرغ، سیب‌زمینی و هویج را نشان دهید. برای هر دستور پخت، تمام مواد استفاده شده را لیست کنید."

با توجه به پرامپت بالا، ممکن است پاسخی مشابه زیر دریافت کنید:

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

این نتیجه عالی است، حالا می‌دانم چه چیزی بپزم. در این مرحله، بهبودهای مفید می‌تواند شامل موارد زیر باشد:

- حذف مواد غذایی که دوست ندارم یا به آن‌ها حساسیت دارم.
- تولید یک لیست خرید، در صورتی که همه مواد غذایی را در خانه نداشته باشم.

برای موارد بالا، بیایید یک پرامپت اضافی اضافه کنیم:

> "لطفاً دستور پخت‌هایی که حاوی سیر هستند را حذف کنید چون به آن حساسیت دارم و آن را با چیز دیگری جایگزین کنید. همچنین، لطفاً یک لیست خرید برای دستور پخت‌ها تولید کنید، با توجه به اینکه من در خانه مرغ، سیب‌زمینی و هویج دارم."

حالا یک نتیجه جدید دارید، یعنی:

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

این پنج دستور پخت شما هستند، بدون ذکر سیر و همچنین یک لیست خرید دارید که مواد غذایی موجود در خانه را در نظر گرفته است.

## تمرین - ساخت یک تولید کننده دستور پخت

حالا که یک سناریو را بررسی کردیم، بیایید کدی بنویسیم که با سناریوی نشان داده شده مطابقت داشته باشد. برای این کار، مراحل زیر را دنبال کنید:

1. از فایل موجود _app.py_ به عنوان نقطه شروع استفاده کنید.
1. متغیر `prompt` را پیدا کنید و کد آن را به صورت زیر تغییر دهید:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   اگر اکنون کد را اجرا کنید، باید خروجی‌ای مشابه زیر را مشاهده کنید:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > توجه داشته باشید، مدل زبانی شما غیرقطعی است، بنابراین ممکن است هر بار که برنامه را اجرا می‌کنید نتایج متفاوتی دریافت کنید.

   عالی، بیایید ببینیم چگونه می‌توانیم چیزها را بهبود دهیم. برای بهبود، می‌خواهیم مطمئن شویم که کد انعطاف‌پذیر است، بنابراین مواد غذایی و تعداد دستور پخت‌ها می‌توانند بهبود یابند و تغییر کنند.

1. بیایید کد را به صورت زیر تغییر دهیم:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   اجرای آزمایشی کد می‌تواند به این صورت باشد:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### بهبود با افزودن فیلتر و لیست خرید

ما اکنون یک اپلیکیشن کاربردی داریم که قادر به تولید دستور پخت‌ها است و انعطاف‌پذیر است زیرا به ورودی‌های کاربر، هم در تعداد دستور پخت‌ها و هم مواد غذایی استفاده شده، وابسته است.

برای بهبود بیشتر، می‌خواهیم موارد زیر را اضافه کنیم:

- **حذف مواد غذایی**. می‌خواهیم بتوانیم مواد غذایی که دوست نداریم یا به آن‌ها حساسیت داریم را حذف کنیم. برای انجام این تغییر، می‌توانیم پرامپت موجود خود را ویرایش کنیم و یک شرط فیلتر به انتهای آن اضافه کنیم، مانند زیر:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  در بالا، `{filter}` را به انتهای پرامپت اضافه می‌کنیم و همچنین مقدار فیلتر را از کاربر دریافت می‌کنیم.

  یک ورودی نمونه از اجرای برنامه اکنون می‌تواند به این صورت باشد:

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

  همانطور که می‌بینید، هر دستور پختی که حاوی شیر باشد حذف شده است. اما، اگر شما به لاکتوز حساسیت دارید، ممکن است بخواهید دستور پخت‌هایی که حاوی پنیر هستند را نیز حذف کنید، بنابراین نیاز به وضوح بیشتری وجود دارد.

- **تولید لیست خرید**. می‌خواهیم یک لیست خرید تولید کنیم، با توجه به آنچه که در حال حاضر در خانه داریم.

  برای این قابلیت، می‌توانیم یا سعی کنیم همه چیز را در یک پرامپت حل کنیم یا آن را به دو پرامپت تقسیم کنیم. بیایید روش دوم را امتحان کنیم. در اینجا پیشنهاد می‌کنیم یک پرامپت اضافی اضافه کنیم، اما برای اینکه این کار انجام شود، باید نتیجه پرامپت قبلی را به عنوان زمینه به پرامپت بعدی اضافه کنیم.

  بخش کدی که نتیجه پرامپت اول را چاپ می‌کند پیدا کنید و کد زیر را در زیر آن اضافه کنید:
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

  به نکات زیر توجه کنید:

  1. ما یک درخواست جدید ایجاد می‌کنیم با اضافه کردن نتیجه درخواست اول به درخواست جدید:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. ما یک درخواست جدید می‌فرستیم، اما همچنین تعداد توکن‌هایی که در درخواست اول خواسته‌ایم را در نظر می‌گیریم، بنابراین این بار مقدار `max_tokens` را 1200 قرار می‌دهیم.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     با اجرای این کد، اکنون به خروجی زیر می‌رسیم:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## بهبود تنظیمات شما

آنچه تاکنون داریم کدی است که کار می‌کند، اما برخی تغییرات وجود دارد که باید انجام دهیم تا اوضاع را بهتر کنیم. برخی از کارهایی که باید انجام دهیم عبارتند از:

- **جدا کردن اطلاعات محرمانه از کد**، مانند کلید API. اطلاعات محرمانه نباید در کد قرار گیرند و باید در مکانی امن ذخیره شوند. برای جدا کردن اطلاعات محرمانه از کد، می‌توانیم از متغیرهای محیطی و کتابخانه‌هایی مانند `python-dotenv` استفاده کنیم تا آنها را از یک فایل بارگذاری کنیم. اینجا نحوه انجام این کار در کد آمده است:

  1. یک فایل `.env` با محتوای زیر ایجاد کنید:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > توجه داشته باشید، برای Azure، باید متغیرهای محیطی زیر را تنظیم کنید:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     در کد، شما متغیرهای محیطی را به این صورت بارگذاری می‌کنید:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **یک نکته درباره طول توکن‌ها**. باید در نظر بگیریم که برای تولید متن مورد نظرمان به چند توکن نیاز داریم. توکن‌ها هزینه دارند، بنابراین در صورت امکان باید سعی کنیم در استفاده از تعداد توکن‌ها اقتصادی عمل کنیم. به عنوان مثال، آیا می‌توانیم درخواست را به گونه‌ای بیان کنیم که از تعداد کمتری توکن استفاده کنیم؟

  برای تغییر تعداد توکن‌های استفاده شده، می‌توانید از پارامتر `max_tokens` استفاده کنید. به عنوان مثال، اگر می‌خواهید از 100 توکن استفاده کنید، می‌توانید این کار را انجام دهید:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **آزمایش با مقدار temperature**. مقدار temperature چیزی است که تاکنون به آن اشاره نکرده‌ایم اما در عملکرد برنامه ما اهمیت دارد. هرچه مقدار temperature بالاتر باشد، خروجی تصادفی‌تر خواهد بود. برعکس، هرچه مقدار temperature پایین‌تر باشد، خروجی قابل پیش‌بینی‌تر خواهد بود. بررسی کنید که آیا می‌خواهید تنوع در خروجی داشته باشید یا خیر.

  برای تغییر مقدار temperature، می‌توانید از پارامتر `temperature` استفاده کنید. به عنوان مثال، اگر می‌خواهید از مقدار temperature برابر با 0.5 استفاده کنید، می‌توانید این کار را انجام دهید:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > توجه داشته باشید، هرچه مقدار به 1.0 نزدیک‌تر باشد، خروجی متنوع‌تر خواهد بود.

## تکلیف

برای این تکلیف، می‌توانید انتخاب کنید که چه چیزی بسازید.

در اینجا چند پیشنهاد وجود دارد:

- برنامه تولید دستور غذا را بهبود دهید. با مقادیر temperature و درخواست‌ها بازی کنید تا ببینید چه چیزی می‌توانید ایجاد کنید.
- یک "همراه مطالعه" بسازید. این برنامه باید بتواند به سوالات مربوط به یک موضوع پاسخ دهد، به عنوان مثال پایتون. شما می‌توانید درخواست‌هایی مانند "یک موضوع خاص در پایتون چیست؟" داشته باشید، یا می‌توانید درخواست داشته باشید که بگوید، کدی برای یک موضوع خاص نشان بده و غیره.
- ربات تاریخ، تاریخ را زنده کنید، به ربات دستور دهید که نقش یک شخصیت تاریخی خاص را بازی کند و از او درباره زندگی و زمانش سوال کنید.

## راه‌حل

### همراه مطالعه

در زیر یک درخواست اولیه آمده است، ببینید چگونه می‌توانید از آن استفاده کنید و آن را به دلخواه خود تغییر دهید.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### ربات تاریخ

در اینجا چند درخواست وجود دارد که می‌توانید از آنها استفاده کنید:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## بررسی دانش

مفهوم temperature چه کاری انجام می‌دهد؟

1. میزان تصادفی بودن خروجی را کنترل می‌کند.
1. اندازه پاسخ را کنترل می‌کند.
1. تعداد توکن‌های استفاده شده را کنترل می‌کند.

## 🚀 چالش

هنگام کار بر روی تکلیف، سعی کنید مقدار temperature را تغییر دهید، آن را روی 0، 0.5 و 1 تنظیم کنید. به یاد داشته باشید که 0 کمترین تنوع و 1 بیشترین تنوع را دارد. چه مقداری برای برنامه شما بهتر عمل می‌کند؟

## کار عالی! یادگیری خود را ادامه دهید

پس از اتمام این درس، مجموعه [یادگیری هوش مصنوعی تولیدی](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ما را بررسی کنید تا دانش خود را در زمینه هوش مصنوعی تولیدی ارتقا دهید!

به درس 7 بروید، جایی که به بررسی نحوه [ساخت برنامه‌های چت](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst) خواهیم پرداخت!

---

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌ها باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیتی در قبال سوء تفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.