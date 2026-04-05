# البناء باستخدام نماذج عائلة ميتا

## المقدمة

ستغطي هذه الدرس:

- استكشاف النموذجين الرئيسيين لعائلة ميتا - لاما 3.1 ولاما 3.2
- فهم حالات الاستخدام والسيناريوهات لكل نموذج
- مثال برمجي لعرض الميزات الفريدة لكل نموذج

## عائلة نماذج ميتا

في هذا الدرس، سنستكشف نموذجين من عائلة ميتا أو "قطيع لاما" - لاما 3.1 ولاما 3.2.

تأتي هذه النماذج في متغيرات مختلفة ومتاحة في سوق نماذج جيتهاب. إليك المزيد من التفاصيل حول استخدام نماذج جيتهاب لـ [النمذجة باستخدام نماذج الذكاء الاصطناعي](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

أنواع النماذج:
- لاما 3.1 - 70B Instruct
- لاما 3.1 - 405B Instruct
- لاما 3.2 - 11B Vision Instruct
- لاما 3.2 - 90B Vision Instruct

*ملاحظة: لاما 3 متاح أيضًا على نماذج جيتهاب لكنه لن يُغطى في هذا الدرس*

## لاما 3.1

بحجم 405 مليار معامل، يندرج لاما 3.1 ضمن فئة نماذج اللغة الكبيرة مفتوحة المصدر.

النموذج هو ترقية لإصدار لاما 3 السابق عبر توفير:

- نافذة سياق أكبر - 128k توكن مقابل 8k توكن
- أقصى عدد إخراج توكن أكبر - 4096 مقابل 2048
- دعم متعدد اللغات أفضل - بفضل زيادة عدد توكنات التدريب

هذه الميزات تتيح للاما 3.1 التعامل مع حالات استخدام أكثر تعقيدًا عند بناء تطبيقات الذكاء التوليدي، بما في ذلك:
- استدعاء الدوال الأصلية - القدرة على استدعاء أدوات ودوال خارج سير عمل النموذج اللغوي الكبير
- أداء أفضل في RAG - بفضل نافذة السياق الأكبر
- توليد بيانات اصطناعية - القدرة على إنشاء بيانات فعالة لمهام مثل ضبط النموذج الدقيق

### استدعاء الدوال الأصلية

تم ضبط لاما 3.1 بدقة ليكون أكثر فاعلية في إجراء استدعاءات الدوال أو الأدوات. كما لديه أداتان مدمجتان يمكن للنموذج التعرف عليهما باعتبارهما مطلوبتين للاستعمال بناءً على طلب المستخدم. هاتان الأداتان هما:

- **Brave Search** - يمكن استخدامها للحصول على معلومات محدثة مثل الطقس عن طريق إجراء بحث ويب
- **Wolfram Alpha** - يمكن استخدامها لحسابات رياضية أكثر تعقيدًا بحيث لا تحتاج إلى كتابة دوال خاصة بك

يمكنك أيضًا إنشاء أدوات مخصصة خاصة بك يمكن للنموذج اللغوي الكبير استدعاؤها.

في المثال البرمجي أدناه:

- نعرّف الأدوات المتاحة (brave_search، wolfram_alpha) في موجه النظام.
- نرسل طلب مستخدم يسأل عن حالة الطقس في مدينة معينة.
- سيستجيب النموذج باستدعاء أداة لـ Brave Search والتي ستبدو كالتالي `<|python_tag|>brave_search.call(query="Stockholm weather")`

*ملاحظة: هذا المثال يقوم فقط باستدعاء الأداة، إذا كنت ترغب في الحصول على النتائج، يجب إنشاء حساب مجاني على صفحة واجهة برمجة تطبيقات Brave وتعريف الدالة نفسها.

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

على الرغم من كونه نموذجًا لغويًا كبيرًا، فإن إحدى قيود لاما 3.1 هي افتقاره للتعددية النمطية. أي عدم القدرة على استخدام أنواع مختلفة من المدخلات مثل الصور كمطالبات وتوفير استجابات. هذه القدرة هي إحدى الميزات الرئيسية للاما 3.2. تشمل هذه الميزات أيضًا:

- التعددية النمطية - لديه القدرة على تقييم كل من النصوص والصور كمطالبات
- تنوعات صغيرة إلى متوسطة الحجم (11B و 90B) - مما يوفر خيارات نشر مرنة
- تنوعات نصية فقط (1B و 3B) - يسمح بنشر النموذج على الأجهزة الطرفية / المحمولة ويوفر زمن استجابة منخفض

يمثل الدعم التعددي خطوة كبيرة في عالم النماذج مفتوحة المصدر. يأخذ المثال البرمجي أدناه صورة ونصًا كمطالبات للحصول على تحليل للصورة من لاما 3.2 بحجم 90B.

### دعم التعددية النمطية مع لاما 3.2

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

## التعلم لا يتوقف هنا، واصل الرحلة

بعد إكمال هذا الدرس، تحقق من [مجموعة تعلم الذكاء التوليدي](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) لمواصلة تطوير معرفتك في الذكاء التوليدي!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم بأن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار الوثيقة الأصلية بلغتها الأصلية المصدر الرسمي والمعتمد. للمعلومات الحساسة أو الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->