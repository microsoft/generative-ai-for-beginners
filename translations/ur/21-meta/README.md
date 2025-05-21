<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:06:32+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "ur"
}
-->
# میٹا فیملی ماڈلز کے ساتھ تعمیر کرنا

## تعارف

یہ سبق شامل کرے گا:

- میٹا فیملی کے دو اہم ماڈلز - لاما 3.1 اور لاما 3.2 کی تحقیق
- ہر ماڈل کے استعمال کے کیسز اور منظرنامے کو سمجھنا
- ہر ماڈل کی منفرد خصوصیات دکھانے کے لیے کوڈ نمونہ

## میٹا فیملی کے ماڈلز

اس سبق میں، ہم میٹا فیملی یا "لاما ہیرڈ" سے 2 ماڈلز کی تحقیق کریں گے - لاما 3.1 اور لاما 3.2

یہ ماڈلز مختلف ورژنز میں آتے ہیں اور گٹ ہب ماڈل مارکیٹ پلیس پر دستیاب ہیں۔ یہاں گٹ ہب ماڈلز کا استعمال کرتے ہوئے [AI ماڈلز کے ساتھ پروٹوٹائپ بنانا](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) پر مزید تفصیلات ہیں۔

ماڈل ورژنز:
- لاما 3.1 - 70B انسٹرکٹ
- لاما 3.1 - 405B انسٹرکٹ
- لاما 3.2 - 11B وژن انسٹرکٹ
- لاما 3.2 - 90B وژن انسٹرکٹ

*نوٹ: لاما 3 بھی گٹ ہب ماڈلز پر دستیاب ہے لیکن اس سبق میں شامل نہیں کیا جائے گا*

## لاما 3.1

405 بلین پیرامیٹرز پر، لاما 3.1 اوپن سورس LLM کیٹیگری میں فٹ بیٹھتا ہے۔

یہ موڈ پہلے ریلیز لاما 3 کا اپگریڈ ہے، جو فراہم کرتا ہے:

- بڑا کانٹیکسٹ ونڈو - 128k ٹوکنز بمقابلہ 8k ٹوکنز
- زیادہ سے زیادہ آؤٹ پٹ ٹوکنز - 4096 بمقابلہ 2048
- بہتر ملٹی لنگوئل سپورٹ - تربیت ٹوکنز میں اضافے کی وجہ سے

یہ لاما 3.1 کو زیادہ پیچیدہ استعمال کے کیسز سنبھالنے کے قابل بناتے ہیں جب GenAI ایپلیکیشنز بناتے ہیں، بشمول:
- نیٹیو فنکشن کالنگ - LLM ورک فلو کے باہر خارجی ٹولز اور فنکشنز کو کال کرنے کی صلاحیت
- بہتر RAG پرفارمنس - زیادہ کانٹیکسٹ ونڈو کی وجہ سے
- مصنوعی ڈیٹا جنریشن - ایسے کاموں کے لیے مؤثر ڈیٹا تخلیق کرنے کی صلاحیت جیسے فائن ٹوننگ

### نیٹیو فنکشن کالنگ

لاما 3.1 کو فنکشن یا ٹول کالز کرنے میں زیادہ مؤثر بنانے کے لیے فائن ٹون کیا گیا ہے۔ اس میں دو بلٹ ان ٹولز ہیں جنہیں ماڈل صارف کی جانب سے دی گئی پرامپٹ کی بنیاد پر استعمال کرنے کی ضرورت کو پہچان سکتا ہے۔ یہ ٹولز ہیں:

- **بریو سرچ** - ویب سرچ انجام دے کر موسم جیسے تازہ ترین معلومات حاصل کرنے کے لیے استعمال کیا جا سکتا ہے
- **وولفرام الفا** - زیادہ پیچیدہ ریاضیاتی حسابات کے لیے استعمال کیا جا سکتا ہے، لہذا اپنے فنکشنز لکھنے کی ضرورت نہیں ہے۔

آپ اپنے خود کے کسٹم ٹولز بھی بنا سکتے ہیں جنہیں LLM کال کر سکتا ہے۔

نیچے دیے گئے کوڈ مثال میں:

- ہم سسٹم پرامپٹ میں دستیاب ٹولز (brave_search, wolfram_alpha) کو تعریف کرتے ہیں۔
- ایک صارف پرامپٹ بھیجتے ہیں جو کسی مخصوص شہر کے موسم کے بارے میں پوچھتا ہے۔
- LLM بریو سرچ ٹول کو کال کرنے کے ساتھ جواب دے گا جو کچھ اس طرح نظر آئے گا `<|python_tag|>brave_search.call(query="Stockholm weather")`

*نوٹ: یہ مثال صرف ٹول کال کرتی ہے، اگر آپ نتائج حاصل کرنا چاہتے ہیں، تو آپ کو بریو API صفحہ پر مفت اکاؤنٹ بنانا ہوگا اور فنکشن کی خود تعریف کرنی ہوگی*

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

لاما 3.1 کی ایک محدودیت ملٹی موڈالیٹی ہے، یعنی مختلف قسم کی انپٹ جیسے تصاویر کو پرامپٹس کے طور پر استعمال کرنے اور جوابات فراہم کرنے کی صلاحیت۔ یہ قابلیت لاما 3.2 کی اہم خصوصیات میں سے ایک ہے۔ یہ خصوصیات بھی شامل ہیں:

- ملٹی موڈالیٹی - متن اور تصویر پرامپٹس دونوں کا جائزہ لینے کی صلاحیت رکھتا ہے
- چھوٹے سے درمیانے سائز کی مختلف ورژنز (11B اور 90B) - یہ لچکدار تعیناتی کے اختیارات فراہم کرتی ہیں،
- صرف متن کی مختلف ورژنز (1B اور 3B) - یہ ماڈل کو ایج / موبائل ڈیوائسز پر تعینات کرنے کی اجازت دیتی ہیں اور کم لیٹینسی فراہم کرتی ہیں

ملٹی موڈال سپورٹ اوپن سورس ماڈلز کی دنیا میں ایک بڑا قدم ہے۔ نیچے دیے گئے کوڈ مثال میں ایک تصویر اور متن پرامپٹ دونوں کو استعمال کیا گیا ہے تاکہ لاما 3.2 90B سے تصویر کا تجزیہ حاصل کیا جا سکے۔

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

## سیکھنا یہاں ختم نہیں ہوتا، سفر جاری رکھیں

اس سبق کو مکمل کرنے کے بعد، ہمارے [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) کو دیکھیں تاکہ اپنی Generative AI معلومات کو بڑھانے کے سفر کو جاری رکھ سکیں!

**ڈس کلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کی کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ورانہ انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔