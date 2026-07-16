# میٹا فیملی ماڈلز کے ساتھ تعمیر 

## تعارف 

یہ سبق شامل کرے گا: 

- دو اہم میٹا فیملی ماڈلز کو دریافت کرنا - لما 3.1 اور لما 3.2 
- ہر ماڈل کے استعمال کے کیسز اور منظرناموں کو سمجھنا 
- ہر ماڈل کی منفرد خصوصیات دکھانے کے لیے کوڈ کا نمونہ 


## میٹا فیملی آف ماڈلز 

اس سبق میں، ہم میٹا فیملی یا "لما ہیرڈ" کے 2 ماڈلز کا جائزہ لیں گے - لما 3.1 اور لما 3.2۔

یہ ماڈلز مختلف اقسام میں دستیاب ہیں اور [Microsoft Foundry Models catalog](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) میں موجود ہیں۔

> **نوٹ:** GitHub Models جولائی 2026 کے آخر میں بند ہو رہا ہے۔ یہاں [Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) کے استعمال پر مزید تفصیلات ہیں تاکہ AI ماڈلز کے ساتھ پروٹوٹائپ بنایا جا سکے۔

ماڈل اقسام: 
- لما 3.1 - 70B انسٹرکٹ 
- لما 3.1 - 405B انسٹرکٹ 
- لما 3.2 - 11B ویژن انسٹرکٹ 
- لما 3.2 - 90B ویژن انسٹرکٹ 

*نوٹ: لما 3 مائیکروسافٹ فاؤنڈری ماڈلز میں بھی دستیاب ہے لیکن اس سبق میں شامل نہیں کی جائے گی*

## لما 3.1 

405 بلین پیرا میٹرز کے ساتھ، لما 3.1 اوپن سورس LLM کیٹیگری میں آتا ہے۔ 

یہ ماڈل پچھلے ورژن لما 3 کی اپگریڈ ہے جو پیش کرتا ہے: 

- بڑا کانٹیکسٹ ونڈو - 128k ٹوکنز بمقابلہ 8k ٹوکنز 
- زیادہ زیادہ آؤٹ پٹ ٹوکنز - 4096 بمقابلہ 2048 
- بہتر کثیر لسانی حمایت - تربیتی ٹوکنز میں اضافے کی وجہ سے 

یہ لما 3.1 کو مزید پیچیدہ استعمال کے کیسز کو سنبھالنے کے قابل بناتے ہیں جب GenAI ایپلیکیشنز بنا رہے ہوں جس میں شامل ہیں: 
- نیٹو فنکشن کالنگ - بیرونی آلات اور فنکشنز کو LLM ورک فلو کے باہر کال کرنے کی صلاحیت 
- بہتر RAG کارکردگی - بڑے کانٹیکسٹ ونڈو کی وجہ سے 
- مصنوعی ڈیٹا جنریشن - مفید ڈیٹا بنانے کی صلاحیت جیسے کہ فائن ٹیوننگ کے لئے 

### نیٹو فنکشن کالنگ 

لما 3.1 کو فنکشن یا ٹول کالز کرنے میں زیادہ موثر بنانے کے لیے فائن ٹیون کیا گیا ہے۔ اس میں دو بلٹ ان ٹولز بھی ہیں جنہیں ماڈل صارف کے پرامپٹ کی بنیاد پر استعمال کرنے کی ضرورت کو پہچان سکتا ہے۔ یہ ٹولز یہ ہیں: 

- **بریک سرچ** - تازہ ترین معلومات مثلاً موسم کی جانکاری کے لیے ویب سرچ استعمال کی جا سکتی ہے 
- **وولفرام الفا** - زیادہ پیچیدہ ریاضیاتی حسابات کے لیے استعمال کیا جا سکتا ہے تاکہ اپنی فنکشنز لکھنے کی ضرورت نہ ہو۔ 

آپ اپنی مرضی کے حسب ضرورت ٹولز بھی بنا سکتے ہیں جنہیں LLM کال کر سکتا ہے۔ 

نیچے دیے گئے کوڈ کے مثال میں: 

- ہم دستیاب ٹولز (brave_search, wolfram_alpha) کو سسٹم پرامپٹ میں تعریف کرتے ہیں۔ 
- صارف کا پرامپٹ بھیجیں جو کسی شہر کے موسم کے بارے میں پوچھتا ہے۔ 
- LLM جواب دے گا ایک ٹول کال کے ساتھ Brave Search ٹول کی طرف، جو کچھ اس طرح دکھائی دے گا `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*نوٹ: یہ مثال صرف ٹول کال کرتی ہے، اگر آپ نتائج حاصل کرنا چاہتے ہیں تو آپ کو Brave API صفحے پر ایک مفت اکاؤنٹ بنانا ہوگا اور فنکشن خود تعریف کرنا ہوگا۔

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# انہیں اپنے Microsoft Foundry پروجیکٹ کے "جائزہ" صفحے سے حاصل کریں
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

## لما 3.2 

اگرچہ یہ ایک LLM ہے، لما 3.1 کی ایک محدودیت اس کی کثیر وضعی صلاحیت کی کمی ہے۔ یعنی، مختلف اقسام کے ان پٹ مثلاً تصاویر کو پرامپٹ کے طور پر استعمال کرنے اور جوابات فراہم کرنے میں ناکامی۔ یہ صلاحیت لما 3.2 کی ایک اہم خصوصیت ہے۔ یہ خصوصیات بھی شامل ہیں: 

- کثیر وضعی - متن اور تصویر دونوں پرامپٹ کا جائزہ لینے کی صلاحیت 
- چھوٹے سے درمیانے سائز کی اقسام (11B اور 90B) - یہ لچکدار تعیناتی کے اختیارات فراہم کرتا ہے، 
- صرف متن کی اقسام (1B اور 3B) - یہ ماڈل کو ایج / موبائل ڈیوائسز پر تعینات کرنے کی اجازت دیتا ہے اور کم لیٹنسی فراہم کرتا ہے 

کثیر وضعی حمایت اوپن سورس ماڈلز کی دنیا میں ایک بڑا قدم ہے۔ نیچے دی گئی کوڈ مثال میں ایک تصویر اور متن دونوں کی پرامپٹ لی جاتی ہے تاکہ لما 3.2 90B سے تصویر کا تجزیہ حاصل کیا جا سکے۔ 


### لما 3.2 کے ساتھ کثیر وضعی حمایت

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

# انہیں اپنے مائیکروسافٹ فاؤنڈری پروجیکٹ کے "جائزہ" صفحہ سے حاصل کریں
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

## سیکھنا یہاں ختم نہیں ہوتا، سفر جاری رکھیں

اس سبق کو مکمل کرنے کے بعد، ہمارے [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) کو دیکھیں تاکہ اپنے جنریٹیو AI علم کو بڑھا سکیں!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->