<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:26:32+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "ur"
}
-->
# میٹا فیملی ماڈلز کے ساتھ تعمیر کرنا

## تعارف

اس سبق میں شامل ہوں گے:

- میٹا فیملی کے دو اہم ماڈلز - لاما 3.1 اور لاما 3.2 کی تحقیق
- ہر ماڈل کے استعمال کے کیسز اور منظرنامے سمجھنا
- ہر ماڈل کی منفرد خصوصیات دکھانے کے لیے کوڈ نمونہ

## میٹا فیملی ماڈلز

اس سبق میں ہم میٹا فیملی یا "لاما ہیرڈ" کے 2 ماڈلز - لاما 3.1 اور لاما 3.2 کی تحقیق کریں گے۔

یہ ماڈلز مختلف ویریئنٹس میں دستیاب ہیں اور گٹ ہب ماڈل مارکیٹ پلیس پر دستیاب ہیں۔ گٹ ہب ماڈلز کا استعمال کرتے ہوئے [AI ماڈلز کے ساتھ پروٹو ٹائپ بنانے](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) پر مزید تفصیلات یہاں ہیں۔

ماڈل ویریئنٹس:
- لاما 3.1 - 70B انسٹرکٹ
- لاما 3.1 - 405B انسٹرکٹ
- لاما 3.2 - 11B ویژن انسٹرکٹ
- لاما 3.2 - 90B ویژن انسٹرکٹ

*نوٹ: لاما 3 بھی گٹ ہب ماڈلز پر دستیاب ہے لیکن اس سبق میں شامل نہیں ہوگا*

## لاما 3.1

405 بلین پیرا میٹرز کے ساتھ، لاما 3.1 اوپن سورس LLM کیٹیگری میں فٹ ہوتا ہے۔

یہ ماڈل پہلے جاری کردہ لاما 3 کی اپ گریڈ ہے، جو فراہم کرتا ہے:

- بڑا کانٹیکسٹ ونڈو - 128k ٹوکنز بمقابلہ 8k ٹوکنز
- بڑا میکس آؤٹ پٹ ٹوکنز - 4096 بمقابلہ 2048
- بہتر ملٹی لنگول سپورٹ - تربیتی ٹوکنز میں اضافے کی وجہ سے

یہ لاما 3.1 کو زیادہ پیچیدہ استعمال کے کیسز سنبھالنے کی اجازت دیتا ہے جب کہ GenAI ایپلی کیشنز بناتے ہوئے، شامل ہیں:
- نیٹیو فنکشن کالنگ - بیرونی ٹولز اور فنکشنز کو LLM ورک فلو کے باہر کال کرنے کی صلاحیت
- بہتر RAG کارکردگی - زیادہ کانٹیکسٹ ونڈو کی وجہ سے
- مصنوعی ڈیٹا جنریشن - مؤثر ڈیٹا بنانے کی صلاحیت جیسے کہ فائن ٹیوننگ کے لیے

### نیٹیو فنکشن کالنگ

لاما 3.1 کو فنکشن یا ٹول کالز کرنے میں زیادہ مؤثر ہونے کے لیے فائن ٹیون کیا گیا ہے۔ اس میں دو بلٹ ان ٹولز ہیں جنہیں ماڈل صارف کی طرف سے دی گئی پرامپٹ کی بنیاد پر استعمال کرنے کی ضرورت کو پہچان سکتا ہے۔ یہ ٹولز ہیں:

- **بریو سرچ** - ویب سرچ کرکے تازہ ترین معلومات حاصل کرنے کے لیے استعمال کیا جا سکتا ہے جیسے موسم
- **وولفرم الفا** - پیچیدہ ریاضیاتی حسابات کے لیے استعمال کیا جا سکتا ہے تاکہ اپنی فنکشنز لکھنے کی ضرورت نہ ہو۔

آپ اپنے کسٹم ٹولز بھی بنا سکتے ہیں جنہیں LLM کال کر سکتا ہے۔

نیچے دیئے گئے کوڈ مثال میں:

- ہم دستیاب ٹولز (brave_search, wolfram_alpha) کو سسٹم پرامپٹ میں تعریف کرتے ہیں۔
- صارف پرامپٹ بھیجتے ہیں جو کسی مخصوص شہر کے موسم کے بارے میں پوچھتا ہے۔
- LLM بریو سرچ ٹول کو کال کرے گا جو اس طرح نظر آئے گا `<|python_tag|>brave_search.call(query="Stockholm weather")`

*نوٹ: یہ مثال صرف ٹول کال کرتی ہے، اگر آپ نتائج حاصل کرنا چاہتے ہیں، تو آپ کو بریو API صفحہ پر مفت اکاؤنٹ بنانا ہوگا اور فنکشن کو خود تعریف کرنا ہوگا*

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

اگرچہ یہ ایک LLM ہے، لاما 3.1 کی ایک محدودیت ملٹی موڈالیٹی ہے۔ یعنی مختلف قسم کی ان پٹ جیسے تصاویر کو پرامپٹس کے طور پر استعمال کرنے اور جوابات فراہم کرنے کی صلاحیت۔ یہ صلاحیت لاما 3.2 کی اہم خصوصیات میں سے ایک ہے۔ ان خصوصیات میں شامل ہیں:

- ملٹی موڈالیٹی - ٹیکسٹ اور امیج پرامپٹس دونوں کا جائزہ لینے کی صلاحیت رکھتا ہے
- چھوٹے سے درمیانے سائز کی تبدیلیاں (11B اور 90B) - یہ لچکدار تعیناتی کے اختیارات فراہم کرتی ہیں،
- صرف ٹیکسٹ کی تبدیلیاں (1B اور 3B) - یہ ماڈل کو ایج / موبائل ڈیوائسز پر تعینات کرنے کی اجازت دیتی ہیں اور کم لیٹنسی فراہم کرتی ہیں

ملٹی موڈال سپورٹ اوپن سورس ماڈلز کی دنیا میں ایک بڑا قدم ہے۔ نیچے دی گئی کوڈ مثال ایک تصویر اور ٹیکسٹ پرامپٹ دونوں کو لاما 3.2 90B سے تصویر کا تجزیہ حاصل کرنے کے لیے استعمال کرتی ہے۔

### لاما 3.2 کے ساتھ ملٹی موڈال سپورٹ

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

## سیکھنے کا سفر یہاں ختم نہیں ہوتا، سفر جاری رکھیں

اس سبق کو مکمل کرنے کے بعد، ہماری [جنریٹو AI لرننگ کلیکشن](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) کو دیکھیں تاکہ جنریٹو AI کے علم کو بڑھانے کا سفر جاری رکھ سکیں!

**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ہم ذمہ دار نہیں ہیں۔