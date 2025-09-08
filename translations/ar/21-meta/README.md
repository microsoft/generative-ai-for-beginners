<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:06:13+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "ar"
}
-->
# البناء باستخدام نماذج عائلة Meta

## مقدمة

ستتناول هذه الدرس:

- استكشاف النموذجين الرئيسيين من عائلة Meta - Llama 3.1 و Llama 3.2  
- فهم حالات الاستخدام والسيناريوهات لكل نموذج  
- مثال برمجي لعرض الميزات الفريدة لكل نموذج  

## عائلة نماذج Meta

في هذا الدرس، سنستعرض نموذجين من عائلة Meta أو "قطيع Llama" - Llama 3.1 و Llama 3.2

تتوفر هذه النماذج في نسخ مختلفة ومتاحة على سوق نماذج GitHub. إليك المزيد من التفاصيل حول استخدام نماذج GitHub لـ [النمذجة الأولية باستخدام نماذج الذكاء الاصطناعي](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

أنواع النماذج:  
- Llama 3.1 - 70B Instruct  
- Llama 3.1 - 405B Instruct  
- Llama 3.2 - 11B Vision Instruct  
- Llama 3.2 - 90B Vision Instruct  

*ملاحظة: Llama 3 متوفر أيضًا على نماذج GitHub لكنه لن يُغطى في هذا الدرس*

## Llama 3.1

بـ 405 مليار معامل، يندرج Llama 3.1 ضمن فئة نماذج اللغة الكبيرة مفتوحة المصدر.

هذا النموذج هو ترقية للإصدار السابق Llama 3 من خلال تقديم:

- نافذة سياق أكبر - 128 ألف رمز مقابل 8 آلاف رمز  
- أقصى عدد رموز إخراج أكبر - 4096 مقابل 2048  
- دعم متعدد اللغات أفضل - بسبب زيادة عدد رموز التدريب  

تمكن هذه الميزات Llama 3.1 من التعامل مع حالات استخدام أكثر تعقيدًا عند بناء تطبيقات الذكاء الاصطناعي التوليدي، بما في ذلك:  
- استدعاء الوظائف الأصلية - القدرة على استدعاء أدوات ووظائف خارج سير عمل نموذج اللغة الكبير  
- أداء أفضل في RAG - بسبب نافذة السياق الأكبر  
- توليد بيانات تركيبية - القدرة على إنشاء بيانات فعالة لمهام مثل التخصيص الدقيق  

### استدعاء الوظائف الأصلية

تم تحسين Llama 3.1 ليكون أكثر فعالية في استدعاء الوظائف أو الأدوات. كما يحتوي على أداتين مدمجتين يمكن للنموذج التعرف على الحاجة لاستخدامهما بناءً على طلب المستخدم. هذه الأدوات هي:

- **Brave Search** - يمكن استخدامها للحصول على معلومات محدثة مثل الطقس من خلال إجراء بحث على الويب  
- **Wolfram Alpha** - يمكن استخدامها لإجراء حسابات رياضية معقدة بحيث لا تحتاج إلى كتابة وظائف خاصة بك  

يمكنك أيضًا إنشاء أدوات مخصصة خاصة بك يمكن للنموذج استدعاؤها.

في المثال البرمجي أدناه:

- نحدد الأدوات المتاحة (brave_search, wolfram_alpha) في موجه النظام.  
- نرسل طلبًا من المستخدم يسأل عن الطقس في مدينة معينة.  
- سيرد نموذج اللغة الكبير باستدعاء أداة Brave Search والذي سيبدو هكذا `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*ملاحظة: هذا المثال يقوم فقط باستدعاء الأداة، إذا كنت ترغب في الحصول على النتائج، ستحتاج إلى إنشاء حساب مجاني على صفحة واجهة برمجة تطبيقات Brave وتعريف الوظيفة نفسها*  

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

على الرغم من كونه نموذج لغة كبير، إلا أن أحد القيود التي يعاني منها Llama 3.1 هو تعدد الوسائط. أي القدرة على استخدام أنواع مختلفة من المدخلات مثل الصور كمدخلات وتقديم ردود عليها. هذه القدرة هي واحدة من الميزات الرئيسية في Llama 3.2. تشمل هذه الميزات أيضًا:

- تعدد الوسائط - القدرة على تقييم كل من النصوص والصور  
- نسخ بأحجام صغيرة إلى متوسطة (11B و 90B) - توفر خيارات نشر مرنة  
- نسخ نصية فقط (1B و 3B) - تسمح بنشر النموذج على الأجهزة الطرفية / المحمولة وتوفر زمن استجابة منخفض  

يمثل دعم تعدد الوسائط خطوة كبيرة في عالم النماذج مفتوحة المصدر. المثال البرمجي أدناه يأخذ كل من صورة ونصًا للحصول على تحليل للصورة من Llama 3.2 90B.

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

## التعلم لا يتوقف هنا، استمر في الرحلة

بعد إكمال هذا الدرس، اطلع على [مجموعة تعلم الذكاء الاصطناعي التوليدي](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) لمواصلة تطوير معرفتك في الذكاء الاصطناعي التوليدي!

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.