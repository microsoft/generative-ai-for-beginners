<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:24:50+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "fa"
}
-->

> "تولید کد برای یک API وب پایتون"
اجرای دوباره پرامپت نتیجه زیر را به ما می‌دهد:

```python
#import necessary libraries
import flask
from flask import request, jsonify

#create a Flask app
app = flask.Flask(__name__)

#create a route for the API
@app.route('/api', methods=['GET'])
def api_call():
    #get the data from the request
    data = request.get_json()

    #process the data
    result = process_data(data)

    #return the result
    return jsonify(result)

#define the process_data function
def process_data(data):
    #do something with the data
    result = data + 1

    #return the result
    return result

#run the app
if __name__ == '__main__':
    app.run()

```

تنها تفاوت کوچکی بین این دو خروجی وجود دارد. این بار برعکس عمل می‌کنیم و دمای مدل را روی ۰.۹ تنظیم می‌کنیم:

```python
# Import necessary libraries
import flask
from flask import request, jsonify

# Create a Flask app
app = flask.Flask(__name__)

# Create a route for the API
@app.route('/api', methods=['GET'])
def api_call():
    # Get the data from the request
    data = request.args

    # Process the data
    result = process_data(data)

    # Return the result
    return jsonify(result)

# Function to process the data
def process_data(data):
    # Do something with the data
    result = data + 1

    # Return the result
    return result

# Run the app
if __name__ == '__main__':
    app.run()

```

و تلاش دوم با مقدار دمای ۰.۹:

```python
import flask
from flask import request, jsonify

# create the Flask app
app = flask.Flask(__name__)
app.config['DEBUG'] = True

# create some test data
books = [
    {'id': 0, 'title': 'A Fire Upon The Deep', 'author': 'Vernor Vinge', 'first_sentence': 'The coldsleep itself was dreamless.', 'year_published': '1992'},
    {'id': 1, 'title': 'The Ones Who Walk Away From Omelas', 'author': 'Ursula K. Le Guin', 'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.', 'published': '1973'},
    {'id': 2, 'title': 'Dhalgren', 'author': 'Samuel R. Delany', 'first_sentence': 'to wound the autumnal city.', 'published': '1975'}
]

# create an endpoint
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to our book API!</h1>'''

@app.route('/api/v1/resources/books

```

همان‌طور که می‌بینید، نتایج بسیار متنوع‌تر شده‌اند.

> توجه داشته باشید که پارامترهای بیشتری وجود دارند که می‌توانید برای تغییر خروجی تنظیم کنید، مانند top-k، top-p، جریمه تکرار، جریمه طول و جریمه تنوع، اما این موارد خارج از محدوده این دوره آموزشی هستند.

## روش‌های خوب

روش‌های زیادی وجود دارد که می‌توانید برای رسیدن به نتیجه دلخواه به کار ببرید. با استفاده بیشتر از پرامپت‌نویسی، سبک خودتان را پیدا خواهید کرد.

علاوه بر تکنیک‌هایی که بررسی کردیم، چند روش خوب وجود دارد که هنگام پرامپت دادن به یک مدل زبان بزرگ باید در نظر بگیرید.

در اینجا چند روش خوب برای در نظر گرفتن آورده شده است:

- **مشخص کردن زمینه**. زمینه اهمیت دارد، هرچه بتوانید حوزه، موضوع و غیره را دقیق‌تر مشخص کنید، بهتر است.
- خروجی را محدود کنید. اگر تعداد مشخصی آیتم یا طول خاصی می‌خواهید، آن را مشخص کنید.
- **مشخص کردن چه چیزی و چگونه**. به یاد داشته باشید هم آنچه می‌خواهید و هم نحوه ارائه آن را ذکر کنید، مثلاً «یک API وب پایتون با مسیرهای products و customers بساز، آن را به ۳ فایل تقسیم کن».
- **استفاده از قالب‌ها**. اغلب می‌خواهید پرامپت‌های خود را با داده‌های شرکتتان غنی کنید. از قالب‌ها برای این کار استفاده کنید. قالب‌ها می‌توانند متغیرهایی داشته باشند که با داده‌های واقعی جایگزین می‌شوند.
- **املای صحیح**. مدل‌های زبان بزرگ ممکن است پاسخ درستی بدهند، اما اگر املای شما درست باشد، پاسخ بهتری دریافت خواهید کرد.

## تمرین

در اینجا کدی به زبان پایتون است که نشان می‌دهد چگونه یک API ساده با استفاده از Flask بسازیم:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run()
```

از دستیار هوش مصنوعی مانند GitHub Copilot یا ChatGPT استفاده کنید و تکنیک «خوداصلاحی» را برای بهبود کد به کار ببرید.

## راه‌حل

لطفاً تلاش کنید با افزودن پرامپت‌های مناسب به کد، تمرین را حل کنید.

> [!TIP]
> پرامپتی بنویسید که درخواست بهبود کند، بهتر است تعداد بهبودها را محدود کنید. همچنین می‌توانید درخواست کنید بهبود در زمینه خاصی مثل معماری، عملکرد، امنیت و غیره انجام شود.

[راه‌حل](../../../05-advanced-prompts/python/aoai-solution.py)

## بررسی دانش

چرا باید از پرامپت زنجیره‌ای (chain-of-thought) استفاده کنم؟ یک پاسخ درست و دو پاسخ نادرست به من نشان بده.

1. برای آموزش مدل زبان بزرگ به نحوه حل مسئله.
1. ب، برای آموزش مدل به یافتن خطا در کد.
1. ج، برای دستور دادن به مدل برای ارائه راه‌حل‌های مختلف.

پاسخ: ۱، چون پرامپت زنجیره‌ای به مدل نشان می‌دهد چگونه مسئله را با ارائه یک سری مراحل و مسائل مشابه و نحوه حل آن‌ها حل کند.

## 🚀 چالش

شما همین الان از تکنیک خوداصلاحی در تمرین استفاده کردید. هر برنامه‌ای که ساخته‌اید را در نظر بگیرید و ببینید چه بهبودهایی می‌خواهید روی آن اعمال کنید. حالا از تکنیک خوداصلاحی برای اعمال تغییرات پیشنهادی استفاده کنید. فکر می‌کنید نتیجه بهتر شده یا بدتر؟

## کار عالی! یادگیری خود را ادامه دهید

پس از اتمام این درس، مجموعه [Generative AI Learning](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) را بررسی کنید تا دانش خود در زمینه هوش مصنوعی مولد را ارتقا دهید!

به درس ۶ بروید که در آن دانش مهندسی پرامپت را با [ساخت برنامه‌های تولید متن](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst) به کار خواهیم گرفت.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.