<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-06-25T13:58:18+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "fa"
}
-->
# ساخت برنامه‌های تولید متن

> _(برای مشاهده ویدئوی این درس، روی تصویر بالا کلیک کنید)_

تا کنون در این دوره آموزشی دیده‌اید که مفاهیم اصلی مانند "پرامپت‌ها" و حتی یک رشته کامل به نام "مهندسی پرامپت" وجود دارد. بسیاری از ابزارهایی که می‌توانید با آنها تعامل داشته باشید مانند ChatGPT، Office 365، Microsoft Power Platform و موارد دیگر، به شما امکان می‌دهند با استفاده از پرامپت‌ها کاری انجام دهید.

برای افزودن چنین تجربه‌ای به یک برنامه، باید مفاهیمی مانند پرامپت‌ها، تکمیل‌ها و انتخاب یک کتابخانه برای کار را درک کنید. این دقیقاً چیزی است که در این فصل یاد خواهید گرفت.

## مقدمه

در این فصل، شما:

- درباره کتابخانه openai و مفاهیم اصلی آن یاد خواهید گرفت.
- یک برنامه تولید متن با استفاده از openai خواهید ساخت.
- خواهید فهمید چگونه از مفاهیمی مانند پرامپت، دما و توکن‌ها برای ساخت یک برنامه تولید متن استفاده کنید.

## اهداف یادگیری

در پایان این درس، شما قادر خواهید بود:

- توضیح دهید که یک برنامه تولید متن چیست.
- یک برنامه تولید متن با استفاده از openai بسازید.
- برنامه خود را برای استفاده از توکن‌های بیشتر یا کمتر و همچنین تغییر دما برای خروجی متنوع‌تر تنظیم کنید.

## برنامه تولید متن چیست؟

به طور معمول، وقتی یک برنامه می‌سازید، نوعی رابط کاربری مانند موارد زیر دارد:

- مبتنی بر فرمان. برنامه‌های کنسولی برنامه‌های معمولی هستند که در آن‌ها یک فرمان تایپ می‌کنید و وظیفه‌ای انجام می‌شود. برای مثال، `git` یک برنامه مبتنی بر فرمان است.
- رابط کاربری (UI). برخی از برنامه‌ها دارای رابط کاربری گرافیکی (GUI) هستند که در آن‌ها دکمه‌ها را کلیک می‌کنید، متن وارد می‌کنید، گزینه‌ها را انتخاب می‌کنید و بیشتر.

### برنامه‌های کنسولی و UI محدود هستند

آن را با یک برنامه مبتنی بر فرمان که در آن فرمانی تایپ می‌کنید مقایسه کنید:

- **محدود است**. نمی‌توانید هر فرمانی را تایپ کنید، فقط آن‌هایی که برنامه پشتیبانی می‌کند.
- **زبان خاص**. برخی از برنامه‌ها از بسیاری از زبان‌ها پشتیبانی می‌کنند، اما به طور پیش‌فرض برنامه برای یک زبان خاص ساخته شده است، حتی اگر بتوانید پشتیبانی از زبان‌های بیشتری اضافه کنید.

### مزایای برنامه‌های تولید متن

پس چگونه یک برنامه تولید متن متفاوت است؟

در یک برنامه تولید متن، شما انعطاف‌پذیری بیشتری دارید، محدود به مجموعه‌ای از فرمان‌ها یا یک زبان ورودی خاص نیستید. در عوض، می‌توانید از زبان طبیعی برای تعامل با برنامه استفاده کنید. مزیت دیگر این است که چون شما قبلاً با یک منبع داده که بر روی یک مجموعه اطلاعات وسیع آموزش دیده است تعامل دارید، در حالی که یک برنامه سنتی ممکن است محدود به آنچه در یک پایگاه داده است باشد.

### چه چیزی می‌توانم با یک برنامه تولید متن بسازم؟

چیزهای زیادی وجود دارد که می‌توانید بسازید. برای مثال:

- **یک چت‌بات**. یک چت‌بات که به سوالات درباره موضوعاتی مانند شرکت شما و محصولات آن پاسخ می‌دهد، می‌تواند یک تطابق خوب باشد.
- **کمک‌کننده**. LLM‌ها در کارهایی مانند خلاصه‌سازی متن، به دست آوردن اطلاعات از متن، تولید متن مانند رزومه و موارد دیگر عالی هستند.
- **دستیار کد**. بسته به مدل زبان مورد استفاده، می‌توانید یک دستیار کد بسازید که به شما در نوشتن کد کمک کند. برای مثال، می‌توانید از محصولاتی مانند GitHub Copilot و همچنین ChatGPT برای کمک به نوشتن کد استفاده کنید.

## چگونه می‌توانم شروع کنم؟

خوب، شما باید راهی برای ادغام با یک LLM پیدا کنید که معمولاً شامل دو رویکرد زیر است:

- استفاده از API. در اینجا شما درخواست‌های وب را با پرامپت خود می‌سازید و متن تولید شده را دریافت می‌کنید.
- استفاده از کتابخانه. کتابخانه‌ها به ساده‌تر کردن تماس‌های API کمک می‌کنند.

## کتابخانه‌ها/SDKها

چند کتابخانه معروف برای کار با LLM‌ها وجود دارد مانند:

- **openai**، این کتابخانه اتصال به مدل شما و ارسال پرامپت‌ها را آسان می‌کند.

سپس کتابخانه‌هایی وجود دارند که در سطح بالاتر عمل می‌کنند مانند:

- **Langchain**. Langchain به خوبی شناخته شده است و از Python پشتیبانی می‌کند.
- **Semantic Kernel**. Semantic Kernel یک کتابخانه از مایکروسافت است که از زبان‌های C#، Python و Java پشتیبانی می‌کند.

## اولین برنامه با استفاده از openai

بیایید ببینیم چگونه می‌توانیم اولین برنامه خود را بسازیم، چه کتابخانه‌هایی نیاز داریم، چقدر لازم است و غیره.

### نصب openai

کتابخانه‌های زیادی برای تعامل با OpenAI یا Azure OpenAI وجود دارند. امکان استفاده از زبان‌های برنامه‌نویسی متعدد نیز وجود دارد مانند C#، Python، JavaScript، Java و بیشتر. ما تصمیم گرفته‌ایم از کتابخانه `openai` Python استفاده کنیم، بنابراین از `pip` برای نصب آن استفاده خواهیم کرد.

```bash
pip install openai
```

### ایجاد یک منبع

شما باید مراحل زیر را انجام دهید:

- ایجاد یک حساب کاربری در Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- دسترسی به Azure OpenAI را به دست آورید. به [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) بروید و درخواست دسترسی دهید.

  > [!NOTE]
  > در زمان نوشتن، شما باید برای دسترسی به Azure OpenAI درخواست دهید.

- نصب Python <https://www.python.org/>
- یک منبع سرویس Azure OpenAI ایجاد کرده باشید. این راهنما را برای چگونگی [ایجاد یک منبع](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst) ببینید.

### مکان‌یابی کلید API و نقطه پایانی

در این مرحله، شما باید به کتابخانه `openai` خود بگویید از چه کلید API استفاده کند. برای یافتن کلید API خود، به بخش "Keys and Endpoint" منبع Azure OpenAI خود بروید و مقدار "Key 1" را کپی کنید.

![صفحه منابع Keys and Endpoint در Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

اکنون که این اطلاعات را کپی کرده‌اید، بیایید به کتابخانه‌ها بگوییم از آن استفاده کنند.

> [!NOTE]
> ارزش دارد که کلید API خود را از کد جدا کنید. می‌توانید این کار را با استفاده از متغیرهای محیطی انجام دهید.
>
> - متغیر محیطی `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'` را تنظیم کنید.

### تنظیم پیکربندی Azure

اگر از Azure OpenAI استفاده می‌کنید، در اینجا نحوه تنظیم پیکربندی آمده است:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

در بالا، موارد زیر را تنظیم می‌کنیم:

- `api_type` to `azure`. This tells the library to use Azure OpenAI and not OpenAI.
- `api_key`, this is your API key found in the Azure Portal.
- `api_version`, this is the version of the API you want to use. At the time of writing, the latest version is `2023-05-15`.
- `api_base`, this is the endpoint of the API. You can find it in the Azure Portal next to your API key.

> [!NOTE] > `os.getenv` is a function that reads environment variables. You can use it to read environment variables like `OPENAI_API_KEY` and `API_BASE`. Set these environment variables in your terminal or by using a library like `dotenv`.

## Generate text

The way to generate text is to use the `Completion` class. Here's an example:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

در کد بالا، یک شیء تکمیل ایجاد می‌کنیم و مدل مورد نظر برای استفاده و پرامپت را به آن می‌دهیم. سپس متن تولید شده را چاپ می‌کنیم.

### تکمیل‌های چت

تا کنون، دیده‌اید که چگونه از `Completion` to generate text. But there's another class called `ChatCompletion` که بیشتر مناسب چت‌بات‌ها است استفاده کرده‌ایم. در اینجا یک مثال از استفاده از آن آمده است:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

بیشتر درباره این قابلیت در فصل آینده.

## تمرین - اولین برنامه تولید متن شما

اکنون که یاد گرفتیم چگونه openai را تنظیم و پیکربندی کنیم، وقت آن است که اولین برنامه تولید متن خود را بسازید. برای ساخت برنامه خود، مراحل زیر را دنبال کنید:

1. یک محیط مجازی ایجاد کنید و openai را نصب کنید:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > اگر از ویندوز استفاده می‌کنید، تایپ کنید `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1` value.

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

   باید خروجی‌ای مشابه زیر را ببینید:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## انواع مختلف پرامپت‌ها برای کارهای مختلف

اکنون دیده‌اید که چگونه می‌توان با استفاده از یک پرامپت متن تولید کرد. حتی یک برنامه در حال اجرا دارید که می‌توانید آن را تغییر دهید و تغییرات ایجاد کنید تا انواع مختلف متن تولید شود.

پرامپت‌ها می‌توانند برای انواع مختلف وظایف استفاده شوند. برای مثال:

- **تولید یک نوع متن**. برای مثال، می‌توانید یک شعر، سوالات برای یک آزمون و غیره تولید کنید.
- **جستجوی اطلاعات**. می‌توانید از پرامپت‌ها برای جستجوی اطلاعات مانند مثال زیر استفاده کنید 'CORS در توسعه وب چه معنایی دارد؟'.
- **تولید کد**. می‌توانید از پرامپت‌ها برای تولید کد استفاده کنید، برای مثال توسعه یک عبارت منظم برای اعتبارسنجی ایمیل‌ها یا حتی تولید یک برنامه کامل، مانند یک برنامه وب.

## یک مورد استفاده عملی‌تر: تولید کننده دستور غذا

تصور کنید که در خانه مواد غذایی دارید و می‌خواهید چیزی بپزید. برای این کار، به یک دستور غذا نیاز دارید. یکی از راه‌های یافتن دستور غذا استفاده از یک موتور جستجو است یا می‌توانید از یک LLM استفاده کنید.

می‌توانید یک پرامپت به این شکل بنویسید:

> "5 دستور غذا برای یک غذا با مواد زیر به من نشان بده: مرغ، سیب‌زمینی و هویج. برای هر دستور، تمام مواد استفاده شده را فهرست کن"

با توجه به پرامپت بالا، ممکن است پاسخی مشابه دریافت کنید:

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

این نتیجه عالی است، می‌دانم چه چیزی بپزم. در این مرحله، چه بهبودهای مفیدی می‌تواند باشد:

- حذف مواد غذایی که دوست ندارم یا به آن‌ها حساسیت دارم.
- تولید یک لیست خرید، در صورتی که همه مواد غذایی را در خانه نداشته باشم.

برای موارد بالا، بیایید یک پرامپت اضافی اضافه کنیم:

> "لطفاً دستورهای غذایی با سیر را حذف کن چون من به آن حساسیت دارم و با چیز دیگری جایگزین کن. همچنین لطفاً یک لیست خرید برای دستورهای غذایی تولید کن، با توجه به اینکه من قبلاً مرغ، سیب‌زمینی و هویج در خانه دارم."

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

این پنج دستور غذا شماست، بدون ذکر سیر و همچنین یک لیست خرید با توجه به آنچه قبلاً در خانه دارید.

## تمرین - ساخت یک تولید کننده دستور غذا

اکنون که یک سناریو را بازی کرده‌ایم، بیایید کدی بنویسیم که با سناریوی نشان داده شده مطابقت داشته باشد. برای انجام این کار، مراحل زیر را دنبال کنید:

1. از فایل موجود _app.py_ به عنوان نقطه شروع استفاده کنید
1. متغیر `prompt` را پیدا کنید و کد آن را به کد زیر تغییر دهید:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   اگر اکنون کد را اجرا کنید، باید خروجی‌ای مشابه زیر را ببینید:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE، LLM شما غیر قطعی است، بنابراین ممکن است هر بار که برنامه را اجرا کنید نتایج متفاوتی دریافت کنید.

   عالی، بیایید ببینیم چگونه می‌توانیم چیزها را بهبود بخشیم. برای بهبود چیزها، می‌خواهیم مطمئن شویم که کد انعطاف‌پذیر است، بنابراین مواد غذایی و تعداد دستورها می‌تواند بهبود و تغییر یابد.

1. بیایید کد را به شکل زیر تغییر دهیم:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   گرفتن کد برای یک آزمایش می‌تواند به این شکل باشد:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### بهبود با افزودن فیلتر و لیست خرید

اکنون یک برنامه کارآمد داریم که قادر به تولید دستورهای غذایی است و انعطاف‌پذیر است زیرا به ورودی‌های کاربر، هم در تعداد دستورها و هم در مواد غذایی استفاده شده، وابسته است.

برای بهبود بیشتر آن، می‌خواهیم موارد زیر را اضافه کنیم:

- **حذف مواد غذایی**. می‌خواهیم بتوانیم مواد غذایی را که دوست نداریم یا به آن‌ها حساسیت داریم حذف کنیم. برای انجام این تغییر، می‌توانیم پرامپت موجود خود را ویرایش کنیم و یک شرط فیلتر به انتهای آن اضافه کنیم به این شکل:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  در بالا، `{filter}` را به انتهای پرامپت اضافه می‌کنیم و همچنین مقدار فیلتر را از کاربر می‌گیریم.

  یک مثال ورودی از اجرای برنامه اکنون می‌تواند به این شکل باشد:

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

  همانطور که می‌بینید، هر دستور غذایی با شیر در آن حذف شده است. اما اگر شما به لاکتوز حساسیت دارید، ممکن است بخواهید دستورهای غذایی با پنیر را نیز حذف کنید، بنابراین نیاز به واضح بودن وجود دارد.

- **تولید لیست خرید**. می‌خواهیم یک لیست خرید تولید کنیم، با توجه به آنچه قبلاً در خانه داریم.

  برای این قابلیت، می‌توانیم همه چیز را در یک پرامپت حل کنیم یا می‌توانیم آن را به دو پرامپت تقسیم کنیم. بیایید رویکرد دوم را امتحان کنیم. در اینجا پیشنهاد می‌دهیم یک پرامپت اضافی اضافه کنیم، اما برای اینکه کار کند، باید نتیجه پرامپت اول را به عنوان زمینه به پرامپت دوم اضافه کنیم.

  قسمتی از کد که نتیجه پرامپت اول را چاپ می‌کند پیدا کنید و کد زیر را به پایین اضافه کنید:

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

  نکات زیر را توجه کنید:

  1. یک پرامپت جدید با افزودن نتیجه پرامپت اول به پرامپت جدید می‌سازیم:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. یک درخواست جدید می‌سازیم، اما همچنین تعداد توکن‌هایی که در پرامپت اول خواسته‌ایم را در نظر می‌گیریم، بنابراین این بار می‌گوییم `max_tokens` برابر با 1200 است.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     گرفتن این کد برای یک آزمایش، اکنون به خروجی زیر می‌رسیم:

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

آنچه تا کنون داریم کدی است که کار می‌کند، اما برخی تنظیمات باید انجام دهیم تا چیزها را بیشتر بهبود بخشیم. برخی چیزهایی که باید انجام دهیم عبارتند از:

- **جدا کردن اسرار از کد**، مانند کلید API. اسرار نباید در کد باشند و باید در یک مکان امن ذخیره شوند. برای جدا کردن اسرار از کد، می‌توانیم از متغیرهای محیطی و کتابخانه‌هایی مانند `python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env` file with the following content:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Note، برای Azure، باید متغیرهای محیطی زیر را تنظیم کنید:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     در کد، متغیرهای محیطی را به این شکل بارگذاری می‌کنید:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **یک کلمه درباره طول توکن**. باید در نظر بگیریم که برای تولید متنی که می‌خواهیم به چند توکن نیاز داریم. توکن‌ها هزینه دارند، بنابراین در صورت امکان، باید سعی کنیم با تعداد توکن‌هایی که استفاده می‌کنیم اقتصادی باشیم. برای مثال، آیا می‌توانیم پرامپت را به گونه‌ای بیان کنیم که بتوانیم از توکن‌های کمتر استفاده کنیم؟

  برای تغییر توکن‌های استفاده شده، می‌توانید از پارامتر `max_tokens` استفاده کنید. برای مثال، اگر می‌خواهید از 100 توکن استفاده کنید، این کار را انجام می‌دهید:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **آزمایش با دما**. دما چیزی است که تا کنون ذکر نکرده‌ایم اما یک زمینه مهم برای نحوه عملکرد برنامه ما است. هر چه مقدار دما بیشتر باشد، خروجی بیشتر تصادفی خواهد بود. برعکس، هر چه مقدار دما کمتر باشد، خروجی بیشتر قابل پیش‌بینی خواهد بود. در نظر بگیرید که آیا می‌خواهید در خروجی خود تنوع داشته باشید یا خیر.

  برای تغییر دما، می‌توانید از پارامتر `temperature` استفاده کنید. برای مثال، اگر می‌خواهید از دمای 0.5 استفاده کنید، این کار را انجام می‌دهید:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > Note، هر چه به 1.0 نزدیک‌تر باشد، خروجی بیشتر متنوع خواهد بود.

## تکلیف

برای این تکلیف، می‌توانید انتخاب کنید چه چیزی بسازید.

در اینجا چند پیشنهاد وجود دارد:

- برنامه تولید کننده دستور غذا را بیشتر بهبود دهید. با مقادیر دما

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌ها باشند. سند اصلی به زبان مادری آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئولیت هیچ گونه سوء تفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه را نمی‌پذیریم.