# البناء باستخدام نماذج عائلة ميتا

## مقدمة

ستغطي هذه الدرس:

- استكشاف النموذجين الرئيسيين لعائلة ميتا - Llama 3.1 و Llama 3.2
- فهم حالات الاستخدام والسيناريوهات لكل نموذج
- مثال كود يوضح الميزات الفريدة لكل نموذج


## عائلة نماذج ميتا

في هذا الدرس، سوف نستكشف نموذجين من عائلة ميتا أو "قطيع اللاما" - Llama 3.1 و Llama 3.2.

تتوفر هذه النماذج في نسخ مختلفة وهي متاحة في [كتالوج نماذج Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **ملاحظة:** نماذج GitHub ستتوقف في نهاية يوليو 2026. إليكم المزيد من التفاصيل حول استخدام [نماذج Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) للنماذج الأولية مع نماذج الذكاء الاصطناعي.

نسخ النماذج:
- Llama 3.1 - 70B مع تعليمات
- Llama 3.1 - 405B مع تعليمات
- Llama 3.2 - 11B رؤية مع تعليمات
- Llama 3.2 - 90B رؤية مع تعليمات

*ملاحظة: Llama 3 متوفر أيضاً في نماذج Microsoft Foundry لكنه لن يُغطي في هذا الدرس*

## Llama 3.1

بوجود 405 مليار معلمة، يندرج Llama 3.1 ضمن فئة نماذج اللغة الكبيرة مفتوحة المصدر.

هذا النموذج هو ترقية للإصدار السابق Llama 3 من خلال تقديم:

- نافذة سياق أكبر - 128k رمز مقابل 8k رمز
- أقصى عدد رموز إخراج أكبر - 4096 مقابل 2048
- دعم متعدد اللغات أفضل - بسبب زيادة رموز التدريب

هذه التحديثات تمكن Llama 3.1 من التعامل مع حالات استخدام أكثر تعقيدًا عند بناء تطبيقات الذكاء الاصطناعي التوليدية بما في ذلك:
- استدعاء دوال مدمجة - القدرة على استدعاء أدوات ودوال خارج سير عمل النموذج اللغوي الكبير
- أداء RAG أفضل - بسبب نافذة السياق الأكبر
- توليد بيانات اصطناعية - القدرة على إنشاء بيانات فعالة لمهام مثل التخصيص الدقيق

### استدعاء الدوال المدمجة

تم ضبط Llama 3.1 ليكون أكثر فعالية في إجراء استدعاءات للدوال أو الأدوات. كما يحتوي على أداتين مدمجتين يمكن للنموذج التعرف عليهما كأدوات يجب استخدامها بناءً على مطالبة المستخدم. هذه الأدوات هي:

- **Brave Search** - يمكن استخدامه للحصول على معلومات محدثة مثل حالة الطقس من خلال إجراء بحث على الويب
- **Wolfram Alpha** - يمكن استخدامه لحسابات رياضية أكثر تعقيدًا بحيث لا تحتاج إلى كتابة الدوال الخاصة بك.

يمكنك أيضًا إنشاء أدوات مخصصة خاصة بك يمكن للنموذج اللغوي الكبير استدعاؤها.

في مثال الشيفرة التالي:

- نحدد الأدوات المتاحة (brave_search، wolfram_alpha) في مطالبة النظام.
- نرسل مطالبة مستخدم تسأل عن الطقس في مدينة معينة.
- سيرد النموذج بنداء أداة إلى أداة Brave Search والذي سيظهر هكذا `<|python_tag|>brave_search.call(query="Stockholm weather")`

*ملاحظة: هذا المثال يقوم فقط بنداء الأداة، إذا أردت الحصول على النتائج، ستحتاج إلى إنشاء حساب مجاني على صفحة Brave API وتعريف الدالة نفسها.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# احصل على هذه من صفحة "نظرة عامة" في مشروع Microsoft Foundry الخاص بك
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

## Llama 3.2

على الرغم من كونه نموذجًا لغويًا كبيرًا، فإن أحد قيود Llama 3.1 هو افتقاره للتعددية النمطية، أي عدم القدرة على استخدام أنواع مختلفة من المدخلات مثل الصور كمطالبات وتقديم ردود. هذه القدرة هي واحدة من السمات الأساسية لـ Llama 3.2. وتشمل هذه الميزات أيضًا:

- التعددية النمطية - القدرة على تقييم كل من مطالبات النص والصورة
- نسخ صغيرة إلى متوسطة الحجم (11B و 90B) - توفر خيارات نشر مرنة،
- نسخ النص فقط (1B و 3B) - تتيح نشر النموذج على الأجهزة الطرفية / المحمولة وتوفر زمن استجابة منخفض

يمثل الدعم المتعدد الأنماط خطوة كبيرة في عالم النماذج مفتوحة المصدر. يأخذ مثال الشيفرة أدناه كل من صورة ونصًا للحصول على تحليل للصورة من Llama 3.2 90B.


### دعم متعدد الأنماط مع Llama 3.2

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

# احصل على هذه من صفحة "نظرة عامة" لمشروع Microsoft Foundry الخاص بك
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

## التعلم لا يتوقف هنا، استمر في الرحلة

بعد إكمال هذا الدرس، تفقد مجموعتنا [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) لمواصلة رفع مستوى معرفتك في الذكاء الاصطناعي التوليدي!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->