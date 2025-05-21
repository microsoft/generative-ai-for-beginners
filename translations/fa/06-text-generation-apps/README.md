<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-05-19T16:40:47+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "fa"
}
-->
# ساخت برنامه‌های تولید متن

> _(برای مشاهده ویدئوی این درس، روی تصویر بالا کلیک کنید)_

تا به حال در این دوره آموزشی، مفاهیم اصلی مانند پرسش‌ها و حتی یک رشته کامل به نام "مهندسی پرسش" را دیده‌اید. بسیاری از ابزارهایی که می‌توانید با آنها تعامل داشته باشید، مانند ChatGPT، Office 365، Microsoft Power Platform و غیره، از شما پشتیبانی می‌کنند تا با استفاده از پرسش‌ها به هدفی برسید.

برای اضافه کردن چنین تجربه‌ای به یک برنامه، باید مفاهیمی مانند پرسش‌ها، تکمیل‌ها و انتخاب یک کتابخانه برای کار را درک کنید. این دقیقاً چیزی است که در این فصل یاد خواهید گرفت.

## مقدمه

در این فصل، شما:

- با کتابخانه openai و مفاهیم اصلی آن آشنا خواهید شد.
- یک برنامه تولید متن با استفاده از openai خواهید ساخت.
- درک خواهید کرد که چگونه از مفاهیمی مانند پرسش، دما و توکن‌ها برای ساخت یک برنامه تولید متن استفاده کنید.

## اهداف یادگیری

در پایان این درس، قادر خواهید بود:

- توضیح دهید که برنامه تولید متن چیست.
- یک برنامه تولید متن با استفاده از openai بسازید.
- برنامه خود را پیکربندی کنید تا از توکن‌های بیشتر یا کمتر استفاده کند و همچنین دما را تغییر دهید تا خروجی متنوعی داشته باشید.

## برنامه تولید متن چیست؟

معمولاً وقتی یک برنامه می‌سازید، دارای نوعی رابط است مانند موارد زیر:

- مبتنی بر دستور. برنامه‌های کنسول، برنامه‌هایی هستند که در آن‌ها دستوری تایپ می‌کنید و وظیفه‌ای را انجام می‌دهند. به عنوان مثال، `git` یک برنامه مبتنی بر دستور است.
- رابط کاربری (UI). برخی برنامه‌ها دارای رابط‌های کاربری گرافیکی (GUI) هستند که در آن‌ها دکمه‌ها را کلیک می‌کنید، متن وارد می‌کنید، گزینه‌ها را انتخاب می‌کنید و غیره.

### برنامه‌های کنسول و رابط کاربری محدود هستند

آن را با یک برنامه مبتنی بر دستور که در آن یک دستور تایپ می‌کنید مقایسه کنید:

- **محدود است**. نمی‌توانید هر دستوری را تایپ کنید، فقط آن‌هایی که برنامه پشتیبانی می‌کند.
- **زبان خاص**. برخی برنامه‌ها از بسیاری از زبان‌ها پشتیبانی می‌کنند، اما به طور پیش‌فرض برنامه برای یک زبان خاص ساخته شده است، حتی اگر بتوانید پشتیبانی زبان بیشتری اضافه کنید.

### مزایای برنامه‌های تولید متن

پس چگونه یک برنامه تولید متن متفاوت است؟

در یک برنامه تولید متن، انعطاف‌پذیری بیشتری دارید، محدود به مجموعه‌ای از دستورات یا یک زبان ورودی خاص نیستید. در عوض، می‌توانید از زبان طبیعی برای تعامل با برنامه استفاده کنید. مزیت دیگر این است که چون در حال تعامل با یک منبع داده هستید که بر روی یک مجموعه بزرگ از اطلاعات آموزش دیده است، در حالی که یک برنامه سنتی ممکن است محدود به اطلاعات موجود در یک پایگاه داده باشد.

### با یک برنامه تولید متن چه چیزی می‌توانم بسازم؟

چیزهای زیادی وجود دارد که می‌توانید بسازید. به عنوان مثال:

- **یک چت‌بات**. یک چت‌بات که به سوالات در مورد موضوعاتی مانند شرکت شما و محصولات آن پاسخ می‌دهد می‌تواند یک تطابق خوب باشد.
- **کمک‌کننده**. مدل‌های زبانی بزرگ (LLM) در چیزهایی مانند خلاصه کردن متن، کسب بینش از متن، تولید متن مانند رزومه و موارد دیگر عالی هستند.
- **دستیار کد**. بسته به مدل زبانی که استفاده می‌کنید، می‌توانید یک دستیار کد بسازید که به شما در نوشتن کد کمک کند. به عنوان مثال، می‌توانید از محصولی مانند GitHub Copilot و همچنین ChatGPT برای کمک به نوشتن کد استفاده کنید.

## چگونه می‌توانم شروع کنم؟

خوب، شما باید راهی برای ادغام با یک LLM پیدا کنید که معمولاً شامل دو رویکرد زیر است:

- استفاده از API. در اینجا شما درخواست‌های وب را با پرسش خود ساخته و متن تولید شده را دریافت می‌کنید.
- استفاده از یک کتابخانه. کتابخانه‌ها به شما کمک می‌کنند تا تماس‌های API را بسته‌بندی کرده و استفاده از آنها را آسان‌تر کنند.

## کتابخانه‌ها/SDKها

چند کتابخانه معروف برای کار با LLMها وجود دارد مانند:

- **openai**، این کتابخانه اتصال به مدل شما و ارسال پرسش‌ها را آسان می‌کند.

سپس کتابخانه‌هایی وجود دارند که در سطح بالاتری عمل می‌کنند مانند:

- **Langchain**. Langchain معروف است و از پایتون پشتیبانی می‌کند.
- **Semantic Kernel**. Semantic Kernel یک کتابخانه توسط مایکروسافت است که از زبان‌های C#، پایتون و جاوا پشتیبانی می‌کند.

## اولین برنامه با استفاده از openai

بیایید ببینیم چگونه می‌توانیم اولین برنامه خود را بسازیم، به چه کتابخانه‌هایی نیاز داریم، چقدر نیاز است و غیره.

### نصب openai

کتابخانه‌های زیادی برای تعامل با OpenAI یا Azure OpenAI وجود دارد. امکان استفاده از زبان‌های برنامه‌نویسی مختلفی مانند C#، پایتون، جاوااسکریپت، جاوا و غیره نیز وجود دارد. ما انتخاب کرده‌ایم که از کتابخانه پایتون `openai` استفاده کنیم، بنابراین از `pip` برای نصب آن استفاده خواهیم کرد.

```bash
pip install openai
```

### ایجاد یک منبع

باید مراحل زیر را انجام دهید:

- ایجاد یک حساب کاربری در Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- دسترسی به Azure OpenAI را کسب کنید. به [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) بروید و درخواست دسترسی دهید.

  > [!NOTE]
  > در زمان نوشتن، شما باید برای دسترسی به Azure OpenAI درخواست کنید.

- پایتون را نصب کنید <https://www.python.org/>
- یک منبع سرویس Azure OpenAI ایجاد کرده‌اید. برای نحوه [ایجاد یک منبع](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst) به این راهنما مراجعه کنید.

### پیدا کردن کلید API و نقطه پایانی

در این مرحله، باید به کتابخانه `openai` خود بگویید که از چه کلید API استفاده کند. برای یافتن کلید API خود، به بخش "کلیدها و نقطه پایانی" از منبع Azure OpenAI خود بروید و مقدار "کلید 1" را کپی کنید.

![صفحه منابع کلیدها و نقطه پایانی در پورتال Azure](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

اکنون که این اطلاعات را کپی کرده‌اید، بیایید به کتابخانه‌ها دستور دهیم که از آن استفاده کنند.

> [!NOTE]
> ارزش دارد که کلید API خود را از کد جدا کنید. می‌توانید این کار را با استفاده از متغیرهای محیطی انجام دهید.
>
> - متغیر محیطی `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'` را تنظیم کنید

### پیکربندی تنظیمات Azure

اگر از Azure OpenAI استفاده می‌کنید، در اینجا نحوه پیکربندی تنظیمات:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

در بالا ما تنظیمات زیر را انجام می‌دهیم:

- `api_type` to `azure`. This tells the library to use Azure OpenAI and not OpenAI.
- `api_key`, this is your API key found in the Azure Portal.
- `api_version`, this is the version of the API you want to use. At the time of writing, the latest version is `2023-05-15`.
- `api_base`, this is the endpoint of the API. You can find it in the Azure Portal next to your API key.

> [!NOTE] > `os.getenv` is a function that reads environment variables. You can use it to read environment variables like `OPENAI_API_KEY` and `API_BASE`. Set these environment variables in your terminal or by using a library like `dotenv`.

## Generate text

The way to generate text is to use the `Completion` کلاس. اینجا یک مثال است:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

در کد بالا، ما یک شیء تکمیل ایجاد می‌کنیم و مدل مورد نظر خود و پرسش را به آن می‌دهیم. سپس متن تولید شده را چاپ می‌کنیم.

### تکمیل چت

تا به حال، دیده‌اید که چگونه از `Completion` to generate text. But there's another class called `ChatCompletion` استفاده کرده‌ایم که برای چت‌بات‌ها مناسب‌تر است. در اینجا یک مثال از استفاده از آن:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

بیشتر در مورد این قابلیت در فصل آینده.

## تمرین - اولین برنامه تولید متن شما

اکنون که یاد گرفتیم چگونه openai را راه‌اندازی و پیکربندی کنیم، زمان ساخت اولین برنامه تولید متن شماست. برای ساخت برنامه خود، این مراحل را دنبال کنید:

1. یک محیط مجازی ایجاد کنید و openai را نصب کنید:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > اگر از ویندوز استفاده می‌کنید تایپ کنید `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1` مقدار.

1. یک فایل _app.py_ ایجاد کنید و کد زیر را به آن بدهید:

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
   > اگر از Azure OpenAI استفاده می‌کنید، باید `api_type` to `azure` and set the `api_key` را به کلید Azure OpenAI خود تنظیم کنید.

   باید خروجی مشابه زیر را ببینید:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## انواع مختلف پرسش‌ها، برای کارهای مختلف

اکنون دیده‌اید که چگونه با استفاده از یک پرسش متن تولید کنید. حتی یک برنامه در حال اجرا دارید که می‌توانید آن را تغییر داده و تغییر دهید تا انواع مختلفی از متن تولید کند.

پرسش‌ها می‌توانند برای انواع کارها استفاده شوند. به عنوان مثال:

- **تولید نوعی متن**. به عنوان مثال، می‌توانید یک شعر، سوالات برای یک مسابقه و غیره تولید کنید.
- **جستجوی اطلاعات**. می‌توانید از پرسش‌ها برای جستجوی اطلاعات استفاده کنید مانند مثال زیر "CORS در توسعه وب به چه معناست؟".
- **تولید کد**. می‌توانید از پرسش‌ها برای تولید کد استفاده کنید، به عنوان مثال توسعه یک عبارت منظم که برای اعتبارسنجی ایمیل‌ها استفاده می‌شود یا چرا یک برنامه کامل تولید نکنید، مانند یک برنامه وب؟

## یک مورد استفاده عملی‌تر: تولید کننده دستور پخت

تصور کنید که در خانه مواد غذایی دارید و می‌خواهید چیزی بپزید. برای آن، به یک دستور پخت نیاز دارید. یک راه برای یافتن دستور پخت استفاده از یک موتور جستجو است یا می‌توانید از یک LLM برای این کار استفاده کنید.

می‌توانید یک پرسش مانند زیر بنویسید:

> "پنج دستور پخت برای یک غذا با مواد زیر به من نشان دهید: مرغ، سیب‌زمینی و هویج. برای هر دستور پخت، تمام مواد استفاده شده را فهرست کنید"

با توجه به پرسش بالا، ممکن است پاسخی مشابه زیر دریافت کنید:

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

این نتیجه عالی است، می‌دانم چه چیزی بپزم. در این مرحله، چه بهبودهایی می‌تواند مفید باشد:

- حذف مواد غذایی که دوست ندارم یا به آنها حساسیت دارم.
- تولید لیست خرید، در صورتی که تمام مواد را در خانه ندارم.

برای موارد بالا، بیایید یک پرسش اضافی اضافه کنیم:

> "لطفاً دستور پخت‌هایی که سیر دارند را حذف کنید چون به آن حساسیت دارم و آن را با چیزی دیگر جایگزین کنید. همچنین، لطفاً یک لیست خرید برای دستور پخت‌ها تولید کنید، با توجه به اینکه من در خانه مرغ، سیب‌زمینی و هویج دارم."

اکنون یک نتیجه جدید دارید، یعنی:

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

این پنج دستور پخت شماست، بدون ذکر سیر و همچنین یک لیست خرید دارید با توجه به آنچه در خانه دارید.

## تمرین - ساخت یک تولید کننده دستور پخت

اکنون که یک سناریو را بازی کرده‌ایم، بیایید کدی بنویسیم که با سناریوی نمایش داده شده مطابقت داشته باشد. برای انجام این کار، مراحل زیر را دنبال کنید:

1. از فایل موجود _app.py_ به عنوان نقطه شروع استفاده کنید
1. متغیر `prompt` را پیدا کنید و کد آن را به موارد زیر تغییر دهید:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   اگر اکنون کد را اجرا کنید، باید خروجی مشابه زیر را ببینید:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > توجه، LLM شما غیرقطعی است، بنابراین ممکن است هر بار که برنامه را اجرا می‌کنید نتایج متفاوتی بگیرید.

   عالی، بیایید ببینیم چگونه می‌توانیم چیزها را بهبود دهیم. برای بهبود چیزها، می‌خواهیم مطمئن شویم که کد انعطاف‌پذیر است، بنابراین مواد و تعداد دستور پخت‌ها می‌تواند بهبود یابد و تغییر کند.

1. بیایید کد را به روش زیر تغییر دهیم:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   اجرای کد می‌تواند به صورت زیر به نظر برسد:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### بهبود با اضافه کردن فیلتر و لیست خرید

اکنون یک برنامه کارآمد داریم که قادر به تولید دستور پخت است و انعطاف‌پذیر است زیرا به ورودی‌های کاربر متکی است، هم در تعداد دستور پخت‌ها و هم در مواد استفاده شده.

برای بهبود بیشتر آن، می‌خواهیم موارد زیر را اضافه کنیم:

- **فیلتر کردن مواد غذایی**. می‌خواهیم بتوانیم مواد غذایی را که دوست نداریم یا به آنها حساسیت داریم فیلتر کنیم. برای انجام این تغییر، می‌توانیم پرسش موجود خود را ویرایش کرده و یک شرط فیلتر به انتهای آن اضافه کنیم به این صورت:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  در بالا، `{filter}` را به انتهای پرسش اضافه می‌کنیم و همچنین مقدار فیلتر را از کاربر دریافت می‌کنیم.

  یک ورودی مثال از اجرای برنامه اکنون می‌تواند به صورت زیر به نظر برسد:

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

  همانطور که می‌بینید، هر دستور پختی که حاوی شیر باشد فیلتر شده است. اما اگر به لاکتوز حساسیت دارید، ممکن است بخواهید دستور پخت‌هایی که حاوی پنیر هستند را نیز فیلتر کنید، بنابراین نیاز به وضوح بیشتری دارید.

- **تولید لیست خرید**. می‌خواهیم یک لیست خرید تولید کنیم، با توجه به آنچه در خانه داریم.

  برای این قابلیت، می‌توانیم سعی کنیم همه چیز را در یک پرسش حل کنیم یا می‌توانیم آن را به دو پرسش تقسیم کنیم. بیایید رویکرد دوم را امتحان کنیم. در اینجا ما پیشنهاد می‌دهیم که یک پرسش اضافی اضافه کنیم، اما برای اینکه کار کند، باید نتیجه پرسش اول را به عنوان زمینه به پرسش دوم اضافه کنیم.

  بخش در کد که نتیجه پرسش اول را چاپ می‌کند پیدا کنید و کد زیر را در زیر آن اضافه کنید:

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

  به موارد زیر توجه کنید:

  1. یک پرسش جدید با افزودن نتیجه پرسش اول به پرسش جدید ایجاد می‌کنیم:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. یک درخواست جدید می‌دهیم، اما همچنین تعداد توکن‌هایی که در پرسش اول خواسته‌ایم را در نظر می‌گیریم، بنابراین این بار می‌گوییم `max_tokens` 1200 است.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     اجرای این کد، اکنون به خروجی زیر می‌رسد:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## بهبود تنظیمات خود

آنچه تا کنون داریم کدی است که کار می‌کند، اما برخی تغییرات باید انجام دهیم تا چیزها را بیشتر بهبود دهیم. برخی از چیزهایی که باید انجام دهیم عبارتند از:

- **جدا کردن اسرار از کد**، مانند کلید API. اسرار نباید در کد ذخیره شوند و باید در مکانی امن نگهداری شوند. برای جدا کردن اسرار از کد، می‌توانیم از متغیرهای محیطی و کتابخانه‌هایی مانند `python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env` استفاده کنیم با محتوای زیر:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > توجه، برای Azure، باید متغیرهای محیطی زیر را تنظیم کنید:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     در کد، می‌توانید متغیرهای محیطی را به صورت زیر بارگذاری کنید:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **یک کلمه درباره طول توکن‌ها**. باید در نظر بگیریم که به چه تعداد توکن نیاز داریم تا متنی که می‌خواهیم تولید کنیم. توکن‌ها هزینه دارند، بنابراین در صورت امکان، باید سعی کنیم با تعداد توکن‌هایی که استفاده می‌کنیم اقتصادی باشیم. به عنوان مثال، آیا می‌توانیم پرسش را به گونه‌ای بیان کنیم که بتوانیم از توکن‌های کمتری استفاده کنیم؟

  برای تغییر توکن‌های استفاده شده، می‌توانید از پارامتر `max_tokens` استفاده کنید. به عنوان مثال، اگر می‌خواهید از 100 توکن استفاده کنید، می‌توانید این کار را انجام دهید:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **آزمایش با دما**. دما چیزی است که تا کنون ذکر نکرده‌ایم اما یک زمینه مهم برای عملکرد برنامه ما است. هر چه مقدار دما بالاتر باشد، خروجی تصادفی‌تر خواهد بود. برعکس، هر چه مقدار دما پایین‌تر باشد، خروجی قابل پیش‌بینی‌تر خواهد بود. در نظر بگیرید که آیا می‌خواهید در خروجی خود تنوع داشته باشید یا خیر.

  برای تغییر دما، می‌توانید از پارامتر `temperature` استفاده کنید. به عنوان مثال، اگر می‌خواهید از دمای 0.5 استفاده کنید، می‌توانید این کار را انجام دهید:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > توجه، هر چه به 1.0 نزدیک‌تر باشد، خروجی متنوع‌تر خواهد بود.

## وظیفه

برای این وظی

**سلب مسئولیت**:  
این سند با استفاده از خدمات ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.