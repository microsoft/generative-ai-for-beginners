# میٹا فیملی ماڈلز کے ساتھ تعمیر

## تعارف

یہ سبق درج ذیل موضوعات کا احاطہ کرے گا:

- میٹا فیملی کے دو اہم ماڈلز - لاما 3.1 اور لاما 3.2 کی دریافت
- ہر ماڈل کے استعمال کے مواقع اور منظرناموں کو سمجھنا
- ہر ماڈل کی منفرد خصوصیات کو ظاہر کرنے کے لیے کوڈ کا نمونہ

## میٹا فیملی آف ماڈلز

اس سبق میں، ہم میٹا فیملی یا "لاما ہیرڈ" کے دو ماڈلز - لاما 3.1 اور لاما 3.2 کی جانچ کریں گے۔

یہ ماڈلز مختلف اقسام میں دستیاب ہیں اور GitHub ماڈل مارکیٹ پلیس پر موجود ہیں۔ یہاں GitHub ماڈلز کو استعمال کرنے کی مزید تفصیلات ہیں تاکہ آپ [AI ماڈلز کے ساتھ پروٹوٹائپ بنا سکیں](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst)۔

ماڈل اقسام: 
- لاما 3.1 - 70B انسٹرکٹ
- لاما 3.1 - 405B انسٹرکٹ
- لاما 3.2 - 11B ویژن انسٹرکٹ
- لاما 3.2 - 90B ویژن انسٹرکٹ

*نوٹ: لاما 3 بھی GitHub ماڈلز پر دستیاب ہے لیکن اس سبق میں اس کا احاطہ نہیں کیا جائے گا*

## لاما 3.1

405 بلین پیرامیٹرز کے ساتھ، لاما 3.1 اوپن سورس LLM کیٹیگری میں آتا ہے۔

یہ ماڈل سابقہ ریلیز لاما 3 کی اپگریڈ ہے جو درج ذیل خصوصیات پیش کرتا ہے:

- بڑا کانٹیکسٹ ونڈو - 8k ٹوکنز کے مقابلے میں 128k ٹوکنز
- زیادہ میکس آؤٹ پٹ ٹوکنز - 2048 کے مقابلے میں 4096
- بہتر کثیراللسانی مدد - تربیتی ٹوکنز میں اضافہ کی وجہ سے

یہ خصوصیات لاما 3.1 کو زیادہ پیچیدہ استعمال کے کیسز کو سنبھالنے کے قابل بناتی ہیں، خاص طور پر GenAI ایپلیکیشنز کی تعمیر میں، جن میں شامل ہیں: 
- نیٹیو فنکشن کالنگ - LLM ورک فلو کے باہر خارجی ٹولز اور فنکشنز کو کال کرنے کی صلاحیت
- بہتر RAG پرفارمنس - کانٹیکسٹ ونڈو کی زیادہ مقدار کی بدولت
- مصنوعی ڈیٹا جنریشن - موثر ڈیٹا بنانے کی صلاحیت جیسے فائن ٹوننگ کے کاموں کے لیے

### نیٹیو فنکشن کالنگ

لاما 3.1 کو فنکشن یا ٹول کالز مؤثر طریقے سے کرنے کے لیے بہتر بنایا گیا ہے۔ اس میں دو بلٹ ان ٹولز بھی شامل ہیں جنہیں ماڈل صارف کے پرامپٹ کی بنیاد پر استعمال کرنے کی ضرورت کے طور پر شناخت کر سکتا ہے۔ یہ ٹولز ہیں:

- **بریو سرچ** - ویب سرچ کرکے موسمیاتی معلومات جیسی تازہ ترین معلومات حاصل کرنے کے لیے استعمال کیا جا سکتا ہے
- **وولفرام الفا** - زیادہ پیچیدہ ریاضیاتی حسابات کے لیے استعمال کیا جا سکتا ہے تاکہ خود کے فنکشن لکھنے کی ضرورت نہ ہو

آپ اپنے کسٹم ٹولز بھی بنا سکتے ہیں جنہیں LLM کال کر سکتا ہے۔

ذیل کے کوڈ نمونے میں:

- ہم سسٹم پرامپٹ میں دستیاب ٹولز (brave_search, wolfram_alpha) کی تعریف کرتے ہیں۔
- صارف کا پرامپٹ بھیجتے ہیں جو کسی مخصوص شہر کے موسم کے بارے میں سوال کرتا ہے۔
- LLM Brave Search ٹول کو کال کرنے کا جواب دے گا جو یوں نظر آئے گا `<|python_tag|>brave_search.call(query="Stockholm weather")`

*نوٹ: یہ مثال صرف ٹول کال کرتی ہے، اگر آپ نتائج حاصل کرنا چاہتے ہیں تو Brave API صفحہ پر مفت اکاؤنٹ بنانا ہوگا اور فنکشن کی خود تعریف کرنی ہوگی۔

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "meta-llama-3.1-405b-instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)


tool_prompt=f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Environment: ipython
Tools: brave_search, wolfram_alpha
Cutting Knowledge Date: December 2023
Today Date: 23 July 2024

You are a helpful assistant<|eot_id|>
"""

messages = [
    SystemMessage(content=tool_prompt),
    UserMessage(content="What is the weather in Stockholm?"),

]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```

## لاما 3.2

اگرچہ یہ ایک LLM ہے، لاما 3.1 کی ایک محدودیت اس کی ملٹی موڈیلٹی کی کمی ہے۔ یعنی، مختلف قسم کی ان پٹ جیسے تصاویر کو پرامپٹ کے طور پر استعمال کرنے اور جواب دینے کی صلاحیت نہیں ہے۔ یہ صلاحیت لاما 3.2 کی اہم خصوصیات میں سے ایک ہے۔ ان خصوصیات میں شامل ہیں:

- ملٹی موڈیلٹی - دونوں متن اور تصویر پرامپٹس کا جائزہ لینے کی صلاحیت ہے
- چھوٹے سے درمیانے سائز کے ویریئنٹس (11B اور 90B) - یہ لچکدار تعیناتی کے آپشنز فراہم کرتے ہیں
- صرف متن والے ویریئنٹس (1B اور 3B) - یہ ماڈل کو ایج / موبائل ڈیوائسز پر تعینات کرنے کی اجازت دیتے ہیں اور کم تاخیر فراہم کرتے ہیں

ملٹی موڈل سپورٹ اوپن سورس ماڈلز کی دنیا میں ایک بڑا قدم ہے۔ ذیل کا کوڈ نمونہ تصویر اور متن دونوں پرامپٹ لیتا ہے تاکہ لاما 3.2 90B سے تصویر کا تجزیہ حاصل کیا جا سکے۔

### لاما 3.2 کے ساتھ ملٹی موڈل سپورٹ

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    SystemMessage,
    UserMessage,
    TextContentItem,
    ImageContentItem,
    ImageUrl,
    ImageDetailLevel,
)
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "Llama-3.2-90B-Vision-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(
            content="You are a helpful assistant that describes images in details."
        ),
        UserMessage(
            content=[
                TextContentItem(text="What's in this image?"),
                ImageContentItem(
                    image_url=ImageUrl.load(
                        image_file="sample.jpg",
                        image_format="jpg",
                        detail=ImageDetailLevel.LOW)
                ),
            ],
        ),
    ],
    model=model_name,
)

print(response.choices[0].message.content)
```

## سیکھنا یہاں نہیں رکتا، اپنی سفر جاری رکھیں

اس سبق کو مکمل کرنے کے بعد، ہمارے [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) کو دیکھیں تاکہ آپ اپنی جنریٹو AI کی معلومات کو مزید بہتر بنا سکیں!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**جھوٹاپنا**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی کوشش کرتے ہیں، براہ مہربانی یاد رکھیں کہ خودکار ترجمے میں غلطیاں یا نقائص ہو سکتے ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تفسیر کے ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->