<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-05-20T11:05:57+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "ar"
}
-->
# بناء باستخدام نماذج عائلة ميتا

## المقدمة

ستغطي هذه الدرس:

- استكشاف النموذجين الرئيسيين لعائلة ميتا - Llama 3.1 و Llama 3.2
- فهم حالات الاستخدام والسيناريوهات لكل نموذج
- مثال برمجي لعرض الميزات الفريدة لكل نموذج

## عائلة نماذج ميتا

في هذا الدرس، سنستكشف نموذجين من عائلة ميتا أو "قطيع اللاما" - Llama 3.1 و Llama 3.2

تأتي هذه النماذج في إصدارات مختلفة ومتاحة في سوق النماذج على GitHub. هنا مزيد من التفاصيل حول استخدام نماذج GitHub لـ [النمذجة باستخدام نماذج الذكاء الاصطناعي](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

إصدارات النماذج:
- Llama 3.1 - 70 مليار تعليمات
- Llama 3.1 - 405 مليار تعليمات
- Llama 3.2 - 11 مليار تعليمات الرؤية
- Llama 3.2 - 90 مليار تعليمات الرؤية

*ملاحظة: Llama 3 متاح أيضًا على نماذج GitHub ولكن لن يتم تغطيته في هذا الدرس*

## Llama 3.1

مع 405 مليار معلمة، ينتمي Llama 3.1 إلى فئة النماذج اللغوية الكبيرة مفتوحة المصدر.

يُعد هذا النموذج ترقية للإصدار السابق Llama 3 من خلال تقديم:

- نافذة سياق أكبر - 128 ألف رمز مقابل 8 آلاف رمز
- زيادة في الحد الأقصى لرموز المخرجات - 4096 مقابل 2048
- دعم متعدد اللغات أفضل - بفضل زيادة رموز التدريب

تُمكن هذه الميزات Llama 3.1 من التعامل مع حالات استخدام أكثر تعقيدًا عند بناء تطبيقات الذكاء الاصطناعي التوليدي، بما في ذلك:
- استدعاء الوظائف الأصلية - القدرة على استدعاء الأدوات والوظائف الخارجية خارج سير عمل النموذج اللغوي الكبير
- أداء أفضل لاسترجاع المعلومات - بفضل النافذة السياقية الأكبر
- توليد البيانات الاصطناعية - القدرة على إنشاء بيانات فعالة لمهام مثل التحسين الدقيق

### استدعاء الوظائف الأصلية

تم تحسين Llama 3.1 ليكون أكثر فعالية في إجراء استدعاءات الوظائف أو الأدوات. يحتوي أيضًا على أداتين مدمجتين يمكن للنموذج التعرف عليهما كأدوات تحتاج إلى استخدامها بناءً على توجيه المستخدم. هذه الأدوات هي:

- **Brave Search** - يمكن استخدامها للحصول على معلومات محدثة مثل الطقس من خلال إجراء بحث على الويب
- **Wolfram Alpha** - يمكن استخدامها لإجراء حسابات رياضية معقدة بحيث لا يتطلب الأمر كتابة وظائفك الخاصة.

يمكنك أيضًا إنشاء أدواتك المخصصة التي يمكن للنموذج اللغوي الكبير استدعاؤها.

في المثال البرمجي أدناه:

- نحدد الأدوات المتاحة (brave_search, wolfram_alpha) في توجيه النظام.
- نرسل توجيه المستخدم الذي يسأل عن الطقس في مدينة معينة.
- سيستجيب النموذج اللغوي الكبير باستدعاء أداة إلى أداة Brave Search التي ستبدو هكذا `<|python_tag|>brave_search.call(query="Stockholm weather")`

*ملاحظة: هذا المثال فقط يقوم باستدعاء الأداة، إذا كنت ترغب في الحصول على النتائج، ستحتاج إلى إنشاء حساب مجاني على صفحة Brave API وتحديد الوظيفة نفسها*

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

على الرغم من كونه نموذجًا لغويًا كبيرًا، إلا أن أحد القيود التي يعاني منها Llama 3.1 هو تعدد الوسائط. أي القدرة على استخدام أنواع مختلفة من المدخلات مثل الصور كتوجيهات وتقديم ردود. هذه القدرة هي واحدة من الميزات الرئيسية لـ Llama 3.2. تشمل هذه الميزات أيضًا:

- تعدد الوسائط - لديه القدرة على تقييم التوجيهات النصية والصورية
- اختلافات الحجم الصغير إلى المتوسط (11 مليار و 90 مليار) - يوفر خيارات نشر مرنة،
- اختلافات النص فقط (1 مليار و 3 مليار) - يسمح للنموذج بالنشر على الأجهزة الحافة / المحمولة ويوفر زمن استجابة منخفض

يمثل دعم تعدد الوسائط خطوة كبيرة في عالم النماذج مفتوحة المصدر. يأخذ المثال البرمجي أدناه كل من صورة وتوجيه نصي للحصول على تحليل للصورة من Llama 3.2 90 مليار.

### دعم تعدد الوسائط مع Llama 3.2

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

## التعلم لا يتوقف هنا، تابع الرحلة

بعد إكمال هذا الدرس، تحقق من [مجموعة تعلم الذكاء الاصطناعي التوليدي](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) لمواصلة تحسين معرفتك بالذكاء الاصطناعي التوليدي!

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يُرجى العلم بأن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية هو المصدر الموثوق. للمعلومات الحساسة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ينشأ عن استخدام هذه الترجمة.