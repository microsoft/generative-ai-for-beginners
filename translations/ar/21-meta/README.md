<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-06-26T03:26:03+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "ar"
}
-->
# البناء باستخدام نماذج عائلة ميتا

## مقدمة

ستغطي هذه الدرس:

- استكشاف النموذجين الرئيسيين من عائلة ميتا - لاما 3.1 ولاما 3.2
- فهم حالات الاستخدام والسيناريوهات لكل نموذج
- مثال برمجي لعرض الميزات الفريدة لكل نموذج

## عائلة نماذج ميتا

في هذا الدرس، سنستكشف نموذجين من عائلة ميتا أو "قطيع لاما" - لاما 3.1 ولاما 3.2

تأتي هذه النماذج في إصدارات مختلفة ومتاحة في سوق النماذج على GitHub. إليك المزيد من التفاصيل حول استخدام نماذج GitHub [للتصميم الأولي باستخدام نماذج الذكاء الاصطناعي](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

إصدارات النماذج:
- لاما 3.1 - 70B إرشادي
- لاما 3.1 - 405B إرشادي
- لاما 3.2 - 11B رؤية إرشادية
- لاما 3.2 - 90B رؤية إرشادية

*ملاحظة: لاما 3 متاح أيضًا على نماذج GitHub ولكنه لن يُغطى في هذا الدرس*

## لاما 3.1

مع 405 مليار معلمة، ينتمي لاما 3.1 إلى فئة النماذج اللغوية الكبيرة مفتوحة المصدر.

هذا النموذج هو ترقية للإصدار السابق لاما 3 من خلال تقديم:

- نافذة سياق أكبر - 128 ألف رمز مقابل 8 آلاف رمز
- زيادة في الحد الأقصى لرموز الإخراج - 4096 مقابل 2048
- دعم لغوي متعدد أفضل - بفضل زيادة الرموز التدريبية

تمكن هذه الميزات لاما 3.1 من التعامل مع حالات استخدام أكثر تعقيدًا عند بناء تطبيقات الذكاء الاصطناعي التوليدي بما في ذلك:
- استدعاء الوظائف الأصلية - القدرة على استدعاء أدوات ووظائف خارج مسار عمل النموذج اللغوي الكبير
- أداء RAG أفضل - بفضل نافذة السياق الأكبر
- توليد البيانات الاصطناعية - القدرة على إنشاء بيانات فعالة لمهام مثل التخصيص الدقيق

### استدعاء الوظائف الأصلية

تم تحسين لاما 3.1 ليكون أكثر فعالية في إجراء استدعاءات الأدوات أو الوظائف. يحتوي أيضًا على أداتين مدمجتين يمكن للنموذج التعرف عليهما كأدوات تحتاج إلى استخدامها بناءً على الطلب من المستخدم. هذه الأدوات هي:

- **بحث بريف** - يمكن استخدامه للحصول على معلومات محدثة مثل الطقس من خلال إجراء بحث على الويب
- **وولفرام ألفا** - يمكن استخدامه لحسابات رياضية أكثر تعقيدًا بحيث لا تحتاج إلى كتابة وظائفك الخاصة.

يمكنك أيضًا إنشاء أدواتك المخصصة التي يمكن للنموذج اللغوي الكبير استدعاؤها.

في المثال البرمجي أدناه:

- نحدد الأدوات المتاحة (brave_search, wolfram_alpha) في طلب النظام.
- نرسل طلب مستخدم يسأل عن الطقس في مدينة معينة.
- سيرد النموذج اللغوي الكبير باستدعاء أداة بحث بريف الذي سيبدو كالتالي `<|python_tag|>brave_search.call(query="Stockholm weather")`

*ملاحظة: هذا المثال يقوم فقط باستدعاء الأداة، إذا كنت ترغب في الحصول على النتائج، ستحتاج إلى إنشاء حساب مجاني على صفحة Brave API وتحديد الوظيفة نفسها*

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

على الرغم من أنه نموذج لغوي كبير، إلا أن لاما 3.1 لديه قيود في تعددية الوسائط. أي القدرة على استخدام أنواع مختلفة من المدخلات مثل الصور كطلبات وتقديم استجابات. هذه القدرة هي واحدة من الميزات الرئيسية في لاما 3.2. تشمل هذه الميزات أيضًا:

- تعددية الوسائط - لديه القدرة على تقييم كل من النصوص والصور كطلبات
- تنويعات بحجم صغير إلى متوسط (11B و90B) - مما يوفر خيارات نشر مرنة،
- تنويعات نصية فقط (1B و3B) - مما يسمح بنشر النموذج على الأجهزة الطرفية / المحمولة ويوفر زمن انتقال منخفض

يمثل الدعم متعدد الوسائط خطوة كبيرة في عالم النماذج مفتوحة المصدر. المثال البرمجي أدناه يأخذ صورة ونص كطلب للحصول على تحليل للصورة من لاما 3.2 90B.

### الدعم متعدد الوسائط مع لاما 3.2

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

## التعلم لا يتوقف هنا، استمر في الرحلة

بعد إكمال هذا الدرس، اطلع على [مجموعة تعلم الذكاء الاصطناعي التوليدي](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) لمواصلة رفع مستوى معرفتك في الذكاء الاصطناعي التوليدي!

**إخلاء المسؤولية**:  
تمت ترجمة هذه الوثيقة باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار الوثيقة الأصلية بلغتها الأصلية المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ناتج عن استخدام هذه الترجمة.