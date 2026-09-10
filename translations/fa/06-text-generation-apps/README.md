# ساخت برنامه‌های تولید متن

[![Building Text Generation Applications](../../../translated_images/fa/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(برای مشاهده ویدئوی این درس روی تصویر بالا کلیک کنید)_

تا اینجا در این دوره دیده‌اید که مفاهیم اصلی‌ای مثل پرامپت‌ها و حتی حوزه‌ای به نام «مهندسی پرامپت» وجود دارد. ابزارهای زیادی مثل ChatGPT، Office 365، Microsoft Power Platform و غیره وجود دارند که با کمک پرامپت‌ها به شما در انجام کارها کمک می‌کنند.

برای اینکه چنین تجربه‌ای را به اپلیکیشن خود اضافه کنید، باید مفاهیمی مثل پرامپت‌ها، تکمیل‌ها را بفهمید و یک کتابخانه برای کار انتخاب کنید. دقیقا این موضوعات را در این فصل آموزش می‌بینید.

## معرفی

در این فصل، شما خواهید:

- درباره کتابخانه openai و مفاهیم اصلی آن یاد بگیرید.
- یک اپلیکیشن تولید متن با استفاده از openai بسازید.
- درک کنید چگونه از مفاهیمی مانند پرامپت، دما و توکن‌ها برای ساخت اپلیکیشن تولید متن استفاده کنید.

## اهداف یادگیری

در انتهای این درس، قادر خواهید بود:

- توضیح دهید اپ تولید متن چیست.
- با استفاده از openai یک اپ تولید متن بسازید.
- اپ خود را طوری تنظیم کنید که توکن‌های بیشتری یا کمتری استفاده کند و همچنین دما را برای خروجی متنوع تغییر دهید.

## اپ تولید متن چیست؟

معمولاً وقتی اپلیکیشنی می‌سازید، دارای نوعی رابط کاربری مانند موارد زیر است:

- مبتنی بر فرمان (Command-based). اپ‌های کنسولی معمولی هستند که در آن‌ها فرمانی تایپ می‌کنید و کاری انجام می‌شود. برای مثال، `git` یک اپ مبتنی بر فرمان است.
- رابط کاربری (UI). برخی اپ‌ها دارای رابط گرافیکی هستند که در آنجا دکمه کلیک می‌کنید، متن وارد می‌کنید، گزینه‌ها را انتخاب می‌کنید و غیره.

### اپ‌های کنسولی و رابط کاربری محدودیت دارند

آن را با اپ مبتنی بر فرمانی که شما فرمان می‌دهید مقایسه کنید:

- **محدود است**. نمی‌توانید هر فرمانی را تایپ کنید، فقط آن‌هایی که اپ پشتیبانی می‌کند.
- **مخصوص زبان خاص**. برخی اپ‌ها از زبان‌های زیادی پشتیبانی می‌کنند، اما به‌طور پیش‌فرض اپ برای یک زبان خاص ساخته شده است، حتی اگر بتوانید زبان‌های بیشتری اضافه کنید.

### مزایای اپ‌های تولید متن

پس اپ تولید متن چه تفاوتی دارد؟

در یک اپ تولید متن، انعطاف بیشتری دارید، محدود به مجموعه فرمان یا زبان ورودی خاص نیستید. در عوض، می‌توانید با زبان طبیعی با اپ تعامل کنید. یک مزیت دیگر این است که شما در حال تعامل با منبع داده‌ای هستید که روی مجموعه وسیعی از اطلاعات آموزش دیده است، در حالی که یک اپ سنتی ممکن است به داده‌های یک پایگاه داده محدود باشد.

### با اپ تولید متن چه می‌توان ساخت؟

می‌توانید چیزهای زیادی بسازید. برای مثال:

- **چت‌بات**. چت‌باتی که به پرسش‌ها درباره موضوعات مختلف مثل شرکت و محصولات شما پاسخ می‌دهد می‌تواند گزینه خوبی باشد.
- **دستیار**. مدل‌های زبان بزرگ (LLM) در کارهایی مانند خلاصه‌سازی متن، استخراج اطلاعات، تولید متنی مانند رزومه و غیره عالی هستند.
- **دستیار کد**. بسته به مدل زبانی که استفاده می‌کنید، می‌توانید دستیار کدی بسازید که در نوشتن کد به شما کمک کند. برای مثال، می‌توانید از محصولی مثل GitHub Copilot یا ChatGPT برای نوشتن کد کمک بگیرید.

## چگونه شروع کنم؟

خوب، باید روشی برای اتصال به یک مدل زبان بزرگ پیدا کنید که معمولاً شامل دو رویکرد زیر است:

- استفاده از API. اینجا شما درخواست‌های وب را با پرامپت خود می‌سازید و متن تولید شده را دریافت می‌کنید.
- استفاده از کتابخانه. کتابخانه‌ها فراخوانی‌های API را بسته‌بندی می‌کنند و استفاده از آن‌ها را آسان می‌کنند.

## کتابخانه‌ها / SDKها

چند کتابخانه شناخته شده برای کار با مدل‌های زبان بزرگ وجود دارد، مانند:

- **openai**، این کتابخانه اتصال به مدل شما و ارسال پرامپت‌ها را آسان می‌کند.

سپس کتابخانه‌هایی وجود دارند که در سطح بالاتر عمل می‌کنند، مانند:

- **Langchain**. لانگ‌چین معروف است و از زبان پایتون پشتیبانی می‌کند.
- **Semantic Kernel**. سماتیک کرنل کتابخانه‌ای از مایکروسافت است که از زبان‌های C#، پایتون و جاوا پشتیبانی می‌کند.

## اولین اپ با استفاده از openai

بیایید ببینیم چگونه اولین اپ خود را می‌سازیم، به چه کتابخانه‌هایی نیاز داریم و چه مقدار لازم است و غیره.

### نصب openai

کتابخانه‌های زیادی برای تعامل با OpenAI یا Azure OpenAI وجود دارد. ممکن است چندین زبان برنامه‌نویسی هم استفاده کنید مانند C#، پایتون، جاوااسکریپت، جاوا و غیره. ما انتخاب کردیم که از کتابخانه پایتون `openai` استفاده کنیم، پس از `pip` برای نصب آن استفاده می‌کنیم.

```bash
pip install openai
```

### ایجاد یک منبع

شما باید مراحل زیر را انجام دهید:

- یک حساب در Azure ایجاد کنید [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- به Azure OpenAI دسترسی پیدا کنید. به [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) بروید و درخواست دسترسی کنید.

  > [!NOTE]
  > در زمان نگارش، باید برای دسترسی به Azure OpenAI درخواست دهید.

- نصب پایتون <https://www.python.org/>
- یک منبع سرویس Azure OpenAI ساخته باشید. این راهنما را ببینید برای اینکه چگونه [یک منبع بسازید](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### پیدا کردن کلید API و نقطه پایانی

اکنون باید به کتابخانه `openai` بگویید از چه کلید API استفاده کند. برای یافتن کلید API خود، به بخش "Keys and Endpoint" منبع Azure OpenAI خود بروید و مقدار "Key 1" را کپی کنید.

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

اکنون که این اطلاعات را کپی کرده‌اید، بیایید به کتابخانه‌ها دستور دهیم که از آن استفاده کنند.

> [!NOTE]
> ارزش دارد کلید API خود را از کد جدا کنید. می‌توانید این کار را با استفاده از متغیرهای محیطی انجام دهید.
>
> - متغیر محیطی `OPENAI_API_KEY` را به کلید API خود تنظیم کنید.
>   `export OPENAI_API_KEY='sk-...'`

### پیکربندی Azure

اگر از Azure OpenAI (که اکنون بخشی از Microsoft Foundry است) استفاده می‌کنید، این‌گونه پیکربندی می‌کنید. ما از کلاینت استاندارد `OpenAI` استفاده می‌کنیم که به نقطه پایانی Azure OpenAI `/openai/v1/` اشاره دارد، که با Responses API کار می‌کند و نیازی به `api_version` ندارد:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

بالاتر موارد زیر را تنظیم می‌کنیم:

- `api_key`، این کلید API شما است که در پورتال Azure یا Microsoft Foundry پیدا می‌شود.
- `base_url`، این نقطه پایانی منبع Foundry شما است که با `/openai/v1/` اضافه شده است. نقطه پایانی پایدار v1 در OpenAI و Azure OpenAI بدون نیاز به مدیریت `api_version` کار می‌کند.

> [!NOTE] > `os.environ` متغیرهای محیطی را می‌خواند. می‌توانید از آن برای خواندن متغیرهای محیطی مانند `AZURE_OPENAI_API_KEY` و `AZURE_OPENAI_ENDPOINT` استفاده کنید. این متغیرها را در ترمینال یا با استفاده از کتابخانه‌ای مانند `dotenv` تنظیم کنید.

## تولید متن

روش تولید متن استفاده از Responses API از طریق متد `responses.create` است. مثال زیر را ببینید:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # این نام استقرار مدل شما است
    input=prompt,
    store=False,
)
print(response.output_text)
```

در کد بالا، پاسخ ایجاد می‌کنیم و مدل و پرامپت موردنظر را می‌دهیم. سپس متن تولید شده را با `response.output_text` چاپ می‌کنیم.

### مکالمات چندمرحله‌ای

Responses API برای تولید متن تک مرحله‌ای و چت‌بات‌های چندمرحله‌ای مناسب است - شما لیستی از پیام‌ها را در `input` می‌دهید تا یک مکالمه بسازید:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

درباره این قابلیت در فصل‌های بعد بیشتر توضیح داده خواهد شد.

## تمرین - اولین اپ تولید متن شما

حالا که یاد گرفتیم چگونه openai را راه‌اندازی و پیکربندی کنیم، وقت ساخت اولین اپ تولید متن شما است. برای ساخت اپ خود، مراحل زیر را دنبال کنید:

1. یک محیط مجازی بسازید و openai را نصب کنید:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > اگر از ویندوز استفاده می‌کنید، به جای `source venv/bin/activate` تایپ کنید `venv\Scripts\activate`.

   > [!NOTE]
   > کلید Azure OpenAI خود را با مراجعه به [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) پیدا کنید؛ جستجو کنید `Open AI`، گزینه `Open AI resource` را انتخاب کنید، سپس `Keys and Endpoint` را انتخاب کنید و مقدار `Key 1` را کپی کنید.

1. یک فایل _app.py_ بسازید و کد زیر را در آن قرار دهید:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # کد تکمیل خود را اضافه کنید
   prompt = "Complete the following: Once upon a time there was a"

   # درخواست با استفاده از API پاسخ‌ها ایجاد کنید
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # پاسخ را چاپ کنید
   print(response.output_text)
   ```

   > [!NOTE]
   > اگر از OpenAI معمولی (نه Azure) استفاده می‌کنید، از `client = OpenAI(api_key="<replace this value with your OpenAI key>")` استفاده کنید (بدون `base_url`) و به جای نام استقرار، نام مدل مانند `gpt-5-mini` بدهید.

   باید خروجی مشابه زیر ببینید:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## انواع مختلف پرامپت‌ها برای کارهای مختلف

اکنون دیدید چگونه با استفاده از یک پرامپت، متن تولید کنید. حتی یک برنامه دارید که اجرا می‌شود و می‌توانید آن را تغییر دهید تا انواع مختلف متن تولید کند.

پرامپت‌ها می‌توانند برای انواع کارها استفاده شوند. برای مثال:

- **تولید نوعی متن**. برای مثال می‌توانید شعر، سوالات یک آزمون و غیره تولید کنید.
- **جستجوی اطلاعات**. می‌توانید از پرامپت‌ها برای پرسش درباره اطلاعاتی مانند مثال زیر استفاده کنید: «CORS در توسعه وب چیست؟».
- **تولید کد**. می‌توانید از پرامپت‌ها برای تولید کد استفاده کنید، مثلا توسعه یک عبارت منظم برای اعتبارسنجی ایمیل‌ها یا حتی تولید یک برنامه کامل، مثل یک اپ وب.

## یک مورد کاربردی‌تر: تولید کننده دستور پخت

تصور کنید مواد اولیه‌ای در خانه دارید و می‌خواهید چیزی بپزید. برای این کار به دستور پخت نیاز دارید. یکی از راه‌ها استفاده از موتور جستجو است یا می‌توانید از یک مدل زبان بزرگ استفاده کنید.

می‌توانید پرامپتی مانند زیر بنویسید:

> «۵ دستور پخت برای غذایی با مواد زیر نشان بده: مرغ، سیب‌زمینی و هویج. برای هر دستور، همه مواد استفاده شده را فهرست کن»

با توجه به پرامپت بالا، ممکن است پاسخی شبیه به این دریافت کنید:

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

این نتیجه عالی است، من می‌دانم چه بپزم. در این نقطه، بهبودهای مفید می‌تواند اینها باشد:

- حذف موادی که دوست ندارم یا به آن‌ها حساسیت دارم.
- تولید لیست خرید، در صورتی که همه مواد را در خانه ندارم.

برای موارد بالا، بیایید یک پرامپت اضافی اضافه کنیم:

> «لطفاً دستور‌ پخت‌هایی که سیر دارند حذف کن چون به آن حساسیت دارم و آن را با چیز دیگری جایگزین کن. همچنین، لطفاً لیست خرید برای دستور‌ پخت‌ها تولید کن، با توجه به اینکه من قبلاً مرغ، سیب‌زمینی و هویج در خانه دارم.»

اکنون یک نتیجه جدید دارید، به این صورت:

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

این پنج دستور پخت شما است، بدون هیچ اشاره‌ای به سیر و همچنین لیست خرید با توجه به مواد موجود در خانه‌تان دارید.

## تمرین - ساخت تولید کننده دستور پخت

حال که این سناریو را اجرا کردیم، بیایید کد بنویسیم که با این سناریو مطابقت داشته باشد. برای این کار، مراحل زیر را دنبال کنید:

1. از فایل موجود _app.py_ به عنوان نقطه شروع استفاده کنید
1. متغیر `prompt` را پیدا کنید و کد آن را به شکل زیر تغییر دهید:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   اگر کد را اکنون اجرا کنید، باید خروجی‌ای مشابه زیر ببینید:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > توجه، مدل زبان شما غیرقطعی است، بنابراین ممکن است هر بار که برنامه را اجرا می‌کنید نتایج متفاوتی بگیرید.

   عالی، بیایید ببینیم چگونه می‌توانیم بهترش کنیم. برای بهبود می‌خواهیم مطمئن شویم کد انعطاف‌پذیر است، بنابراین تعداد دستور‌ پخت‌ها و مواد اولیه می‌توانند تغییر کنند.

1. کد را به شکل زیر تغییر دهیم:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # تعداد دستورهای آشپزی را در متن درخواست و مواد اولیه وارد کنید
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   کد برای اجرای آزمایشی می‌تواند چنین باشد:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### بهبود با اضافه کردن فیلتر و لیست خرید

اکنون یک اپ کاربردی داریم که می‌تواند دستور‌ پخت تولید کند و انعطاف‌پذیر است چون به ورودی کاربر وابسته است، هم در تعداد دستور پخت‌ها و هم مواد اولیه استفاده‌شده.

برای بهبود بیشتر، می‌خواهیم موارد زیر را اضافه کنیم:

- **حذف مواد دلخواه**. می‌خواهیم بتوانیم مواد غذایی را که دوست نداریم یا به آن حساسیت داریم حذف کنیم. برای انجام این تغییر، می‌توانیم پرامپت موجود خود را ویرایش کنیم و شرط فیلتر را به انتهای آن اضافه کنیم، به شکل زیر:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  در بالا، `{filter}` را به انتهای پرامپت اضافه می‌کنیم و همچنین مقدار فیلتر را از کاربر دریافت می‌کنیم.

  نمونه ورودی اجرای برنامه می‌تواند این‌گونه باشد:

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

  همان‌طور که می‌بینید، هر دستور‌ پختی که در آن شیر باشد حذف شده است. اما اگر به لاکتوز حساسیت دارید، ممکن است بخواهید دستور‌ پخت‌هایی که پنیر دارند را هم حذف کنید، بنابراین باید واضح باشد.


- **فهرست خرید تهیه کنید**. ما می‌خواهیم یک فهرست خرید تهیه کنیم، با در نظر گرفتن آنچه در خانه داریم.

  برای این عملکرد، می‌توانیم همه چیز را در یک درخواست حل کنیم یا آن را به دو درخواست تقسیم کنیم. بیایید روش دوم را امتحان کنیم. در اینجا پیشنهاد می‌کنیم یک درخواست اضافی اضافه کنیم، اما برای اینکه این کار کارآمد باشد، باید نتیجه درخواست اول را به عنوان زمینه به درخواست دوم اضافه کنیم.

  قسمت کدی را که نتیجه را از درخواست اول چاپ می‌کند پیدا کنید و کد زیر را زیر آن اضافه کنید:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # پاسخ را چاپ کن
  print("Shopping list:")
  print(response.output_text)
  ```

  توجه کنید به موارد زیر:

  1. ما با افزودن نتیجه درخواست اول به درخواست جدید، یک درخواست جدید می‌سازیم:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. یک درخواست جدید می‌فرستیم، اما همچنین تعداد توکن‌هایی را که در درخواست قبلی خواسته بودیم در نظر می‌گیریم، بنابراین این بار می‌گوییم `max_output_tokens` برابر با 1200 است.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     با اجرای این کد، به خروجی زیر می‌رسیم:

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

آنچه تاکنون داریم کدی است که کار می‌کند، اما برخی اصلاحات وجود دارد که باید برای بهبود بیشتر اعمال کنیم. برخی از کارهایی که باید انجام دهیم عبارتند از:

- **جدا کردن اسرار از کد**، مانند کلید API. اسرار نباید در کد باشند و باید در مکانی امن ذخیره شوند. برای جدا کردن اسرار از کد، می‌توانیم از متغیرهای محیطی و کتابخانه‌هایی مانند `python-dotenv` برای بارگذاری آنها از فایل استفاده کنیم. به این صورت در کد خواهد بود:

  1. یک فایل `.env` با محتوای زیر ایجاد کنید:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > توجه داشته باشید، برای Azure OpenAI در Microsoft Foundry، باید متغیرهای محیطی زیر را به جای آن تنظیم کنید:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     در کد، متغیرهای محیطی را به این صورت بارگذاری می‌کنید:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **یک نکته درباره طول توکن‌ها**. باید در نظر بگیریم که چه تعداد توکن برای تولید متن مورد نظر نیاز داریم. توکن‌ها هزینه دارند، بنابراین در صورت امکان باید در استفاده از تعداد توکن‌ها صرفه‌جویی کنیم. مثلا آیا می‌توانیم درخواست را طوری بیان کنیم که توکن کمتری مصرف شود؟

  برای تغییر تعداد توکن‌ها، می‌توانید از پارامتر `max_output_tokens` استفاده کنید. برای مثال، اگر می‌خواهید از 100 توکن استفاده کنید، به این شکل عمل کنید:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **آزمایش با پارامتر دما (temperature)**. دما چیزی است که تاکنون ذکر نکرده‌ایم اما زمینه مهمی برای عملکرد برنامه ما است. هرچه مقدار دما بالاتر باشد، خروجی تصادفی‌تر خواهد بود. برعکس، هرچه مقدار دما کمتر باشد، خروجی قابل پیش‌بینی‌تر خواهد بود. در نظر بگیرید که آیا می‌خواهید تنوع در خروجی داشته باشید یا خیر.

  برای تغییر دما، می‌توانید از پارامتر `temperature` استفاده کنید. برای مثال، اگر می‌خواهید دما را 0.5 قرار دهید، به این شکل عمل کنید:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > توجه کنید، هرچه نزدیکتر به 1.0 باشید، خروجی متنوع‌تر خواهد بود.

- **مدل‌های استدلالی از پارامتر `temperature` استفاده نمی‌کنند**. این یک تغییر مهم در سال 2026 است. مدل‌های فعلی غیر منسوخ شده در Microsoft Foundry **مدل‌های استدلالی** هستند (خانواده GPT-5، سری o) - و آنها **از `temperature` یا `top_p` پشتیبانی نمی‌کنند** (همچنین `max_tokens` را نیز استفاده نکنید؛ از `max_output_tokens` استفاده کنید). اگر به `gpt-5-mini` پارامتر `temperature` ارسال کنید، خطای "پارامتر پشتیبانی نمی‌شود" دریافت خواهید کرد. بنابراین برای آزمایش مثال دما بالا، از مدلی استفاده کنید که کنترل نمونه‌برداری را هنوز پشتیبانی می‌کند - برای مثال مدل باز **Llama** مانند `Llama-3.3-70B-Instruct` از [کاتالوگ مدل‌های Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst)، که از طریق Endpoint مدل‌های Foundry / Azure AI Inference فراخوانی می‌شود (همانند نمونه‌های `githubmodels-*`). برای مدل‌های استدلالی مانند GPT-5، خروجی را به روش متفاوتی هدایت می‌کنید:
  - **مهندسی درخواست (Prompt engineering)** - دستورالعمل‌های واضح، مثال‌ها و خروجی ساختاریافته (به درس [04 - مبانی مهندسی درخواست](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst) مراجعه کنید) کارها را انجام می‌دهد که قبلاً با تنظیمات نمونه‌برداری انجام می‌شد.
  - **کنترل‌های استدلال** - پارامترهایی مانند تلاش استدلال / verbosity عمق استدلال را در برابر تأخیر و هزینه متعادل می‌کنند.

  خلاصه: `temperature`/`top_p` هنوز در بسیاری از مدل‌ها (Llama، Mistral، Phi و خانواده GPT-4.x - هرچند GPT-4.x در حال منسوخ شدن است) معتبر هستند، اما روند حرکت به سمت مهندسی درخواست + کنترل‌های استدلالی در مدل‌های استدلالی مانند GPT-5 است.

## تمرین

برای این تمرین، می‌توانید انتخاب کنید چه چیزی بسازید.

در اینجا چند پیشنهاد آورده شده است:

- اپلیکیشن تولید کننده دستور غذا را بیشتر بهبود دهید. با مقادیر دما و درخواست‌ها بازی کنید و ببینید چه چیزهایی می‌توانید خلق کنید.
- یک "یار مطالعه" بسازید. این اپ باید بتواند به سوالات در مورد یک موضوع مثلا پایتون پاسخ دهد؛ می‌توانید درخواست‌هایی مانند "موضوع خاصی در پایتون چیست؟" داشته باشید، یا درخواستی که "کدی برای موضوع خاص نشان بده" بدهد و غیره.
- بات تاریخ، تاریخ را زنده کنید. بات را به ایفای نقش یک شخصیت تاریخی خاص وادارید و از او درباره زندگی و زمان‌هایش سوال کنید.

## راه حل

### یار مطالعه

در زیر یک درخواست شروع اولیه آمده است، ببینید چگونه می‌توانید از آن استفاده کنید و آن را به دلخواه خود تنظیم کنید.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### بات تاریخ

در اینجا چند درخواست آورده شده است که می‌توانید استفاده کنید:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## آزمون دانش

مفهوم دما (temperature) چه کاری انجام می‌دهد؟

1. کنترل می‌کند که خروجی چقدر تصادفی باشد.
1. کنترل می‌کند که پاسخ چقدر بزرگ باشد.
1. کنترل می‌کند که چه تعداد توکن استفاده شود.

## 🚀 چالش

هنگام کار بر روی تمرین، سعی کنید دما را تغییر دهید، آن را روی 0، 0.5 و 1 تنظیم کنید. به یاد داشته باشید که 0 کمترین تنوع و 1 بیشترین تنوع را دارد. کدام مقدار برای اپ شما بهترین کارکرد را دارد؟

## کار عالی! آموزش خود را ادامه دهید

پس از اتمام این درس، مجموعه [یادگیری هوش مصنوعی مولد](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) ما را بررسی کنید تا دانش هوش مصنوعی مولد خود را ارتقا دهید!

به درس 7 بروید که در آن می‌خواهیم ببینیم چگونه [اپلیکیشن‌های چت بسازیم](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان مادری خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما در قبال هرگونه سوء تفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه مسئولیتی نداریم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->