# البناء باستخدام نماذج عائلة Meta  

## المقدمة  

ستغطي هذه الدرس:  

- استكشاف النموذجين الرئيسيين لعائلة Meta - Llama 3.1 و Llama 3.2  
- فهم حالات الاستخدام والسيناريوهات لكل نموذج  
- مثال برمجي لعرض الميزات الفريدة لكل نموذج  


## عائلة نماذج Meta  

في هذا الدرس، سوف نستكشف نموذجين من عائلة Meta أو "قطيع Llama" - Llama 3.1 و Llama 3.2.

تتوفر هذه النماذج في إصدارات مختلفة وهي متاحة في [كتالوج نماذج Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **ملاحظة:** نماذج GitHub ستتوقف عن العمل في نهاية يوليو 2026. هنا المزيد من التفاصيل حول استخدام [نماذج Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) لتجربة النماذج الذكية.

إصدارات النماذج:  
- Llama 3.1 - 70 مليار للتعليمات  
- Llama 3.1 - 405 مليار للتعليمات  
- Llama 3.2 - 11 مليار لرؤية التعليمات  
- Llama 3.2 - 90 مليار لرؤية التعليمات  

*ملاحظة: Llama 3 متوفر أيضًا في نماذج Microsoft Foundry لكن لن يتم تغطيته في هذا الدرس*  

## Llama 3.1  

بوجود 405 مليار معلمة، يناسب Llama 3.1 فئة نماذج اللغة الكبيرة مفتوحة المصدر.  

النموذج هو ترقية للإصدار السابق Llama 3 من خلال تقديم:  

- نافذة سياق أكبر - 128 ألف رمز مقابل 8 آلاف رمز  
- عدد أكبر للحد الأقصى لرموز الإخراج - 4096 مقابل 2048  
- دعم متعدد اللغات أفضل - بسبب زيادة رموز التدريب  

هذه الإمكانيات تمكّن Llama 3.1 من التعامل مع حالات استخدام أكثر تعقيدًا عند بناء تطبيقات الذكاء التوليدي، بما في ذلك:  
- استدعاء الوظائف الأصلي - القدرة على استدعاء أدوات ووظائف خارج سير عمل نموذج اللغة  
- أداء RAG أفضل - بسبب نافذة السياق الأكبر  
- إنشاء بيانات تركيبية - القدرة على إنشاء بيانات فعالة لمهام مثل الضبط الدقيق  

### استدعاء الوظائف الأصلي  

تم تحسين Llama 3.1 ليكون أكثر فعالية في استدعاء الوظائف أو الأدوات. كما يحتوي على أداتين مدمجتين يمكن للنموذج التعرف على حاجتهما بناءً على مطالبة المستخدم. هذه الأدوات هي:  

- **Brave Search** - يمكن استخدامه للحصول على معلومات محدثة مثل الطقس من خلال إجراء بحث على الويب  
- **Wolfram Alpha** - يمكن استخدامه للحسابات الرياضية المعقدة بحيث لا تحتاج لكتابة وظائفك الخاصة  

يمكنك أيضًا إنشاء أدوات مخصصة خاصة بك يمكن للنموذج استدعاؤها.  

في المثال البرمجي أدناه:  

- نعرّف الأدوات المتاحة (brave_search، wolfram_alpha) في موجه النظام.  
- نرسل مطالبة مستخدم تسأل عن الطقس في مدينة معينة.  
- سيرد نموذج اللغة بنداء أداة إلى أداة Brave Search والتي ستبدو كالتالي `<|python_tag|>brave_search.call(query="Stockholm weather")`  

*ملاحظة: هذا المثال يقوم فقط بنداء الأداة، إذا أردت الحصول على النتائج، ستحتاج إلى إنشاء حساب مجاني على صفحة API الخاصة بـ Brave وتعريف الدالة نفسها.  

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

بالرغم من كونه نموذجًا للغة الكبيرة، فإن أحد قيود Llama 3.1 هو افتقاده للتعددية النمطية. أي عدم القدرة على استخدام أنواع مختلفة من المدخلات مثل الصور كمطالبات وتقديم ردود. وهذه القدرة هي من الميزات الرئيسية لـ Llama 3.2. وتشمل هذه الميزات أيضًا:  

- التعددية النمطية - القدرة على تقييم كل من نصوص ومطالبات الصور  
- تنويعات بحجوم صغيرة إلى متوسطة (11 مليار و 90 مليار) - ما يوفر خيارات نشر مرنة،  
- تنويعات نصية فقط (1 مليار و 3 مليار) - ما يسمح بنشر النموذج على أجهزة الحافة / الأجهزة المحمولة ويوفر زمن استجابة منخفض  

دعم التعددية النمطية يمثل خطوة كبيرة في عالم النماذج مفتوحة المصدر. يأخذ المثال البرمجي أدناه كل من صورة ومطالبة نصية للحصول على تحليل للصورة من Llama 3.2 90B.  


### دعم التعددية النمطية مع Llama 3.2  

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

بعد إكمال هذا الدرس، تحقق من [مجموعة تعلم الذكاء التوليدي](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) للاستمرار في رفع مستوى معرفتك في الذكاء التوليدي!  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->