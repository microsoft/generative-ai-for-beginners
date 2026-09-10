# میٹا فیملی ماڈلز کے ساتھ تعمیر 

## تعارف 

یہ سبق درج ذیل موضوعات کا احاطہ کرے گا: 

- میٹا فیملی کے دو اہم ماڈلز کی جانچ - لاما 3.1 اور لاما 3.2 
- ہر ماڈل کے استعمال کے کیسز اور منظرناموں کو سمجھنا 
- ہر ماڈل کی منفرد خصوصیات دکھانے کے لیے کوڈ نمونہ 


## میٹا فیملی آف ماڈلز 

اس سبق میں، ہم میٹا فیملی یا "لاما ہیرڈ" کے دو ماڈلز کا جائزہ لیں گے - لاما 3.1 اور لاما 3.2۔

یہ ماڈلز مختلف اقسام میں دستیاب ہیں اور [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) میں دستیاب ہیں۔

> **نوٹ:** GitHub Models جولائی 2026 کے آخر میں بند ہو رہا ہے۔ یہاں [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) کا استعمال کرتے ہوئے AI ماڈلز کے ساتھ پروٹوٹائپ بنانے کی مزید تفصیلات ہیں۔

ماڈل کی اقسام: 
- لاما 3.1 - 70B انسٹرکٹ 
- لاما 3.1 - 405B انسٹرکٹ 
- لاما 3.2 - 11B وژن انسٹرکٹ 
- لاما 3.2 - 90B وژن انسٹرکٹ 

*نوٹ: لاما 3 بھی Microsoft Foundry Models میں دستیاب ہے لیکن اس سبق میں شامل نہیں کیا گیا ہے*

## لاما 3.1 

405 ارب پیرامیٹرز کے ساتھ، لاما 3.1 اوپن سورس LLM زمرے میں آتا ہے۔ 

یہ ماڈل پہلے کے ورژن لاما 3 کی اپگریڈ ہے اور یہ خصوصیات پیش کرتا ہے: 

- بڑا کانٹیکسٹ ونڈو - 128k ٹوکنز بمقابلہ 8k ٹوکنز 
- زیادہ زیادہ آؤٹ پٹ ٹوکنز - 4096 بمقابلہ 2048 
- بہتر کثیرالزبانی سپورٹ - تربیتی ٹوکنز میں اضافے کی بدولت 

یہ لاما 3.1 کو زیادہ پیچیدہ استعمال کے کیسز سنبھالنے کے قابل بناتے ہیں، جن میں شامل ہیں: 
- نیٹو فنکشن کالنگ - LLM ورک فلو کے باہر بیرونی ٹولز اور فنکشن بلانے کی صلاحیت
- بہتر RAG کارکردگی - زیادہ کانٹیکسٹ ونڈو کی وجہ سے 
- مصنوعی ڈیٹا کی تیاری - جیسے کہ فائن ٹیوننگ کے کام کے لیے موثر ڈیٹا بنانا 

### نیٹو فنکشن کالنگ 

لاما 3.1 کو فنکشن یا ٹول کالز کرنے کے لیے زیادہ مؤثر بنانے کے لیے فائن ٹیون کیا گیا ہے۔ اس میں دو بلٹ ان ٹولز بھی شامل ہیں جنہیں ماڈل صارف کے پرامپٹ کی بنیاد پر استعمال کرنے کی ضرورت کو پہچان سکتا ہے۔ یہ ٹولز یہ ہیں: 

- **Brave Search** - تازہ ترین معلومات حاصل کرنے کے لیے ویب سرچ انجام دینے کے قابل، مثلاً موسم وغیرہ 
- **Wolfram Alpha** - زیادہ پیچیدہ ریاضیاتی حسابات کے لیے استعمال کیا جا سکتا ہے تاکہ اپنے فنکشنز لکھنے کی ضرورت نہ ہو۔ 

آپ اپنے خود کے کسٹم ٹولز بھی بنا سکتے ہیں جنہیں LLM کال کر سکتا ہے۔ 

نیچے دیے گئے کوڈ مثال میں: 

- ہم دستیاب ٹولز (brave_search، wolfram_alpha) کو سسٹم پرامپٹ میں تعریف کرتے ہیں۔ 
- ایک صارف کا پرامپٹ بھیجیں جو کسی مخصوص شہر کے موسم کے بارے میں سوال کرتا ہے۔ 
- LLM Brave Search ٹول کے لیے ایک ٹول کال کے ساتھ جواب دے گا جو اس طرح نظر آئے گا `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*نوٹ: یہ مثال صرف ٹول کال کرتی ہے، اگر آپ نتائج حاصل کرنا چاہتے ہیں تو آپکو Brave API صفحہ پر ایک مفت اکاؤنٹ بنانا اور فنکشن خود تعریف کرنا ہوگا۔*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# اپنے Microsoft Foundry پروجیکٹ کے "Overview" صفحے سے یہ حاصل کریں
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
model_name = "Meta-Llama-3.1-405B-Instruct"

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

لاما 3.1 ایک LLM ہونے کے باوجود، اس کی ایک حد اس کی کثیر النوعیت کی کمی ہے۔ یعنی، مختلف اقسام کی ان پٹ جیسے تصاویر کو پرامپٹ کے طور پر استعمال کرنے اور جوابات فراہم کرنے کی صلاحیت نہ ہونا۔ یہ صلاحیت لاما 3.2 کی ایک اہم خصوصیت ہے۔ ان خصوصیات میں شامل ہیں: 

- کثیر النوعیت - ٹیکسٹ اور تصویر دونوں کو پرامپٹ کے طور پر پرکھنے کی صلاحیت 
- چھوٹے سے درمیانے سائز کے مختلف ورژن (11B اور 90B) - یہ لچکدار تعیناتی کے اختیارات فراہم کرتا ہے، 
- صرف ٹیکسٹ والے ورژن (1B اور 3B) - یہ ماڈل کو ایج/موبائل ڈیوائسز پر تعینات کرنے اور کم تاخیر فراہم کرنے کی اجازت دیتا ہے 

کثیر النوعی سپورٹ اوپن سورس ماڈلز کی دنیا میں ایک بڑا قدم ہے۔ نیچے دیے گئے کوڈ مثال میں تصویر اور ٹیکسٹ دونوں پرامپٹ لے کر لاما 3.2 90B سے تصویر کا تجزیہ حاصل کیا گیا ہے۔ 


### لاما 3.2 کے ساتھ کثیر النوعی سپورٹ

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

# اپنے Microsoft Foundry پروجیکٹ کے "جائزہ" صفحہ سے یہ حاصل کریں
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
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

## سیکھنا یہاں نہیں رکتا، سفر جاری رکھیں

اس سبق کو مکمل کرنے کے بعد، ہماری [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) دیکھیں تاکہ اپنی جنریٹیو AI کی معلومات میں مزید بہتری لائیں!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->