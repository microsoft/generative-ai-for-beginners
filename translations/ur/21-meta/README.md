<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:06:35+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "ur"
}
-->
# میٹا فیملی ماڈلز کے ساتھ تعمیر

## تعارف

اس سبق میں شامل ہے:

- میٹا فیملی کے دو اہم ماڈلز - Llama 3.1 اور Llama 3.2 کا جائزہ  
- ہر ماڈل کے استعمال کے کیسز اور حالات کو سمجھنا  
- ہر ماڈل کی منفرد خصوصیات دکھانے کے لیے کوڈ کا نمونہ  

## میٹا فیملی آف ماڈلز

اس سبق میں، ہم میٹا فیملی یا "Llama Herd" کے 2 ماڈلز کا جائزہ لیں گے - Llama 3.1 اور Llama 3.2

یہ ماڈلز مختلف اقسام میں دستیاب ہیں اور GitHub Model مارکیٹ پلیس پر موجود ہیں۔ GitHub Models کو [AI ماڈلز کے ساتھ پروٹوٹائپ بنانے](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst) کے لیے استعمال کرنے کی مزید تفصیلات یہ ہیں۔

ماڈل کی اقسام:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*نوٹ: Llama 3 بھی GitHub Models پر دستیاب ہے لیکن اس سبق میں شامل نہیں کیا جائے گا*

## Llama 3.1

405 ارب پیرامیٹرز کے ساتھ، Llama 3.1 اوپن سورس LLM کیٹیگری میں آتا ہے۔

یہ ماڈل پچھلے ورژن Llama 3 کی اپ گریڈ ہے جو درج ذیل خصوصیات فراہم کرتا ہے:

- بڑا کانٹیکسٹ ونڈو - 128k ٹوکنز بمقابلہ 8k ٹوکنز  
- زیادہ زیادہ آؤٹ پٹ ٹوکنز - 4096 بمقابلہ 2048  
- بہتر کثیر اللسانی سپورٹ - تربیتی ٹوکنز میں اضافے کی وجہ سے  

یہ خصوصیات Llama 3.1 کو زیادہ پیچیدہ استعمال کے کیسز سنبھالنے کے قابل بناتی ہیں، خاص طور پر GenAI ایپلیکیشنز بنانے میں، جیسے:  
- نیٹیو فنکشن کالنگ - LLM ورک فلو کے باہر بیرونی ٹولز اور فنکشنز کو کال کرنے کی صلاحیت  
- بہتر RAG پرفارمنس - زیادہ کانٹیکسٹ ونڈو کی وجہ سے  
- مصنوعی ڈیٹا جنریشن - فائن ٹیوننگ جیسے کاموں کے لیے مؤثر ڈیٹا بنانے کی صلاحیت  

### نیٹیو فنکشن کالنگ

Llama 3.1 کو فنکشن یا ٹول کالز کرنے میں زیادہ مؤثر بنانے کے لیے فائن ٹیون کیا گیا ہے۔ اس میں دو بلٹ ان ٹولز بھی شامل ہیں جنہیں ماڈل صارف کے پرامپٹ کی بنیاد پر استعمال کرنے کی ضرورت سمجھتا ہے۔ یہ ٹولز ہیں:

- **Brave Search** - ویب سرچ کے ذریعے تازہ ترین معلومات جیسے موسم کا حال معلوم کرنے کے لیے استعمال کیا جا سکتا ہے  
- **Wolfram Alpha** - زیادہ پیچیدہ ریاضیاتی حسابات کے لیے استعمال کیا جا سکتا ہے تاکہ آپ کو اپنے فنکشنز لکھنے کی ضرورت نہ پڑے  

آپ اپنے خود کے کسٹم ٹولز بھی بنا سکتے ہیں جنہیں LLM کال کر سکتا ہے۔

نیچے دیے گئے کوڈ کے نمونے میں:

- ہم دستیاب ٹولز (brave_search, wolfram_alpha) کو سسٹم پرامپٹ میں ڈیفائن کرتے ہیں۔  
- صارف کا پرامپٹ بھیجتے ہیں جو کسی خاص شہر کے موسم کے بارے میں پوچھتا ہے۔  
- LLM Brave Search ٹول کو کال کے ساتھ جواب دے گا جو کچھ اس طرح نظر آئے گا `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*نوٹ: یہ مثال صرف ٹول کال کرتی ہے، اگر آپ نتائج حاصل کرنا چاہتے ہیں تو آپ کو Brave API صفحہ پر مفت اکاؤنٹ بنانا ہوگا اور فنکشن خود ڈیفائن کرنا ہوگا*  

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

## Llama 3.2

اگرچہ یہ بھی ایک LLM ہے، Llama 3.1 کی ایک محدودیت ملٹی موڈالیٹی ہے۔ یعنی مختلف قسم کے ان پٹ جیسے تصاویر کو پرامپٹ کے طور پر استعمال کرنے اور جوابات دینے کی صلاحیت۔ یہ صلاحیت Llama 3.2 کی اہم خصوصیات میں سے ایک ہے۔ دیگر خصوصیات میں شامل ہیں:

- ملٹی موڈالیٹی - متن اور تصویر دونوں پرامپٹس کا تجزیہ کرنے کی صلاحیت  
- چھوٹے سے درمیانے سائز کی اقسام (11B اور 90B) - یہ لچکدار تعیناتی کے اختیارات فراہم کرتا ہے  
- صرف متن کی اقسام (1B اور 3B) - یہ ماڈل کو ایج / موبائل ڈیوائسز پر تعینات کرنے اور کم تاخیر فراہم کرنے کی اجازت دیتا ہے  

ملٹی موڈل سپورٹ اوپن سورس ماڈلز کی دنیا میں ایک بڑا قدم ہے۔ نیچے دیے گئے کوڈ کے نمونے میں ایک تصویر اور متن دونوں کو پرامپٹ کے طور پر لے کر Llama 3.2 90B سے تصویر کا تجزیہ حاصل کیا گیا ہے۔

### Llama 3.2 کے ساتھ ملٹی موڈل سپورٹ

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

اس سبق کو مکمل کرنے کے بعد، ہمارے [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) کو دیکھیں تاکہ آپ اپنی Generative AI کی معلومات کو مزید بڑھا سکیں!

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔