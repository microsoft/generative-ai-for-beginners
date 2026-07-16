[![نماذج المصدر المفتوح](../../../translated_images/ar/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## مقدمة

تمثل وكلاء الذكاء الاصطناعي تطورًا مثيرًا في الذكاء الاصطناعي التوليدي، مما يمكّن نماذج اللغة الكبيرة (LLMs) من التحول من مساعدين إلى وكلاء قادرين على اتخاذ إجراءات. تتيح أطر عمل وكلاء الذكاء الاصطناعي للمطورين إنشاء تطبيقات تمنح نماذج اللغة الكبيرة وصولاً إلى الأدوات وإدارة الحالة. كما تعزز هذه الأطر الرؤية، مما يسمح للمستخدمين والمطورين بمراقبة الإجراءات التي تخطط لها نماذج اللغة الكبيرة، وبالتالي تحسين إدارة التجربة.

ستغطي هذه الدرس المجالات التالية:

- فهم ما هو وكيل الذكاء الاصطناعي - ما هو بالضبط وكيل الذكاء الاصطناعي؟
- استكشاف خمسة أطر عمل مختلفة لوكلاء الذكاء الاصطناعي - ما الذي يميزها؟
- تطبيق هؤلاء الوكلاء على حالات استخدام مختلفة - متى يجب أن نستخدم وكلاء الذكاء الاصطناعي؟

## أهداف التعلم

بعد إتمام هذا الدرس، ستتمكن من:

- شرح ماهية وكلاء الذكاء الاصطناعي وكيف يمكن استخدامها.
- فهم الفروق بين بعض أطر عمل وكلاء الذكاء الاصطناعي المشهورة، وكيف تختلف.
- فهم كيفية عمل وكلاء الذكاء الاصطناعي لبناء تطبيقات باستخدامهم.

## ما هي وكلاء الذكاء الاصطناعي؟

وكلاء الذكاء الاصطناعي مجال مثير جدًا في عالم الذكاء الاصطناعي التوليدي. ومع هذا الحماس أحيانًا يحدث ارتباك في المصطلحات وتطبيقاتها. للحفاظ على الأمور بسيطة وشاملة لمعظم الأدوات التي تشير إلى وكلاء الذكاء الاصطناعي، سنستخدم هذا التعريف:

تمكّن وكلاء الذكاء الاصطناعي نماذج اللغة الكبيرة (LLMs) من أداء المهام من خلال منحهم الوصول إلى **الحالة** و **الأدوات**.

![ نموذج الوكيل](../../../translated_images/ar/what-agent.21f2893bdfd01e6a.webp)

لنحدد هذه المصطلحات:

**نماذج اللغة الكبيرة** - هذه هي النماذج المشار إليها طوال هذا المقرر مثل GPT-3.5، GPT-4، Llama-2، وما إلى ذلك.

**الحالة** - تشير إلى السياق الذي يعمل ضمنه نموذج اللغة الكبيرة. يستخدم النموذج سياق أفعاله السابقة والسياق الحالي لتوجيه اتخاذ القرار للإجراءات التالية. تمكن أطر عمل وكلاء الذكاء الاصطناعي المطورين من الحفاظ على هذا السياق بسهولة أكبر.

**الأدوات** - لإكمال المهمة التي طلبها المستخدم والتي خطط لها نموذج اللغة الكبيرة، يحتاج النموذج إلى وصول للأدوات. بعض أمثلة الأدوات قد تكون قاعدة بيانات، API، تطبيق خارجي أو حتى نموذج لغة كبيرة آخر!

نأمل أن تمنحك هذه التعريفات أساسًا قويًا للمضي قدمًا أثناء استكشاف كيفية تنفيذها. دعونا نستعرض بعض أطر عمل وكلاء الذكاء الاصطناعي المختلفة:

## وكلاء LangChain

[وكلاء LangChain](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) هو تنفيذ للتعريفات التي قدمناها أعلاه.

لإدارة **الحالة**، يستخدم وظيفة مدمجة تسمى `AgentExecutor`. تستقبل هذه الوظيفة الـ `agent` المحدد و`tools` المتاحة له.

كما يخزن `Agent Executor` تاريخ المحادثة لتوفير سياق المحادثة.

![وكلاء LangChain](../../../translated_images/ar/langchain-agents.edcc55b5d5c43716.webp)

تقدم LangChain [كتالوج الأدوات](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) التي يمكن استيرادها إلى تطبيقك والتي يمكن لنموذج اللغة الكبيرة الوصول إليها. هذه الأدوات مقدمة من المجتمع وفريق LangChain.

يمكنك بعد ذلك تعريف هذه الأدوات وتمريرها إلى `Agent Executor`.

الرؤية هي جانب مهم آخر عند الحديث عن وكلاء الذكاء الاصطناعي. من المهم لمطوري التطبيقات فهم الأداة التي يستخدمها النموذج ولماذا.. ولهذا طور فريق LangChain أداة LangSmith.

## AutoGen

إطار عمل وكيل الذكاء الاصطناعي التالي الذي سنناقشه هو [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). التركيز الأساسي لـ AutoGen هو المحادثات. الوكلاء هم **قابلون للمحادثة** و**قابلون للتخصيص**.

**قابلون للمحادثة -** يمكن لنماذج اللغة الكبيرة بدء ومواصلة محادثة مع نموذج آخر لإكمال مهمة. يتم ذلك بإنشاء `AssistantAgents` ومنحهم رسالة نظام محددة.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**قابلون للتخصيص** - يمكن تعريف الوكلاء ليس فقط كنماذج لغوية كبيرة ولكن أيضًا كمستخدم أو أداة. كمطور، يمكنك تعريف `UserProxyAgent` المسؤول عن التفاعل مع المستخدم لتلقي الملاحظات في إكمال مهمة. يمكن أن تستمر هذه الملاحظات في تنفيذ المهمة أو إيقافها.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### الحالة والأدوات

لتغيير وإدارة الحالة، يقوم وكيل المساعد بتوليد كود Python لإكمال المهمة.

إليك مثال على العملية:

![AutoGen](../../../translated_images/ar/autogen.dee9a25a45fde584.webp)

#### نموذج لغة كبير مع رسالة نظام

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

توجه رسالة النظام هذا النموذج المحدد إلى الوظائف ذات الصلة بمهمته. تذكر، مع AutoGen يمكنك أن تمتلك عدة AssistantAgents مع رسائل نظام مختلفة.

#### بدأت المحادثة بواسطة المستخدم

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

هذه الرسالة من user_proxy (البشري) هي ما سيبدأ عملية الوكيل لاستكشاف الوظائف المحتملة التي يجب تنفيذها.

#### تنفيذ الوظيفة

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

بمجرد معالجة المحادثة الأولية، سيرسل الوكيل الأداة المقترحة للاتصال بها. في هذه الحالة، هي وظيفة تسمى `get_weather`. حسب تكوينك، يمكن تنفيذ هذه الوظيفة تلقائيًا وقرائتها من قبل الوكيل أو يمكن تنفيذها بناءً على إدخال المستخدم.

يمكنك العثور على قائمة بـ [نماذج كود AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) لاستكشاف المزيد عن كيفية البدء في البناء.

## إطار عمل Microsoft Agent

[إطار عمل Microsoft Agent](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) هو مجموعة تطوير برمجيات مفتوحة المصدر من مايكروسوفت لبناء وكلاء الذكاء الاصطناعي وأنظمة الوكلاء المتعددة في كلاً من **Python** و **.NET**. يجمع بين نقاط القوة في مشروعي مايكروسوفت السابقين — ميزات المؤسسات في **Semantic Kernel** وتنظيم الوكلاء المتعدد في **AutoGen** — في إطار عمل واحد ومدعوم. إذا كنت تبدأ مشروع وكيل جديد اليوم، فهذا هو البديل الموصى به لـ AutoGen.

يمتد الإطار من وكيل دردشة واحد إلى سير عمل معقد لوكلاء متعددين، ويتكامل مباشرة مع Microsoft Foundry و Azure OpenAI و OpenAI. كما يوفر مراقبة مدمجة من خلال OpenTelemetry حتى تتمكن من تتبع ما يفعله وكلاؤك بدقة.

### الحالة والأدوات

**الحالة** - يدير الإطار سياق المحادثة من خلال **الخيوط**. يتتبع الوكيل تاريخ الرسائل (طلبات المستخدم، استدعاءات الأدوات، ونتائجها)، بحيث يبني كل دور على الدور السابق. يمكن أيضًا الاحتفاظ بالخيوط مما يسمح بإيقاف واستئناف المحادثة لاحقًا.

**الأدوات** - تمنح الوكيل أدوات بتمرير دوال Python عادية. يتم تلقائيًا تحويل الوسائط المعلّمة بالنوع إلى مخطط، فيعرف النموذج كيفية ووقت استدعائها (استدعاء الدوال). يدعم الإطار أيضًا خوادم Model Context Protocol (MCP) والأدوات المستضافة مثل مفسر الكود.

إليك مثال على وكيل واحد مع أداة مخصصة:

```python
import asyncio
from typing import Annotated

from pydantic import Field
from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient


def get_weather(
    location: Annotated[str, Field(description="The location to get the weather for.")],
) -> str:
    """Get the weather for a given location."""
    return f"The weather in {location} is sunny with a high of 22°C."


async def main():
    agent = Agent(
        client=OpenAIChatClient(),
        instructions="You are a helpful assistant that can answer weather questions.",
        tools=[get_weather],
    )

    response = await agent.run("What's the weather in Amsterdam?")
    print(response)


asyncio.run(main())
```

للاتصال بـ Azure OpenAI في Microsoft Foundry بدلاً من ذلك، مرر نقطة النهاية وبيانات الاعتماد إلى العميل:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-4o-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### سير عمل متعدد الوكلاء

حيث يبرز الإطار حقًا هو تنظيم عدة وكلاء معًا. على سبيل المثال، يمكنك تشغيل الوكلاء واحدًا تلو الآخر (كل منهم يمرر سياقه للاحق) أو التوسع إلى عدة وكلاء بالتوازي وتجميع نتائجهم:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# تشغيل الوكلاء بالتسلسل، مع تمرير سياق المحادثة عبر السلسلة
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# التفرع إلى الوكلاء بشكل متوازي، ثم تجميع ردودهم
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

لتثبيت الإطار وبدء الاستخدام:

```bash
pip install agent-framework-core
# تكاملات اختيارية
pip install agent-framework-openai       # أوبن إيه آي وأزور أوبن إيه آي
pip install agent-framework-foundry      # مايكروسوفت فاوندري
```

يمكنك استكشاف المزيد في [مستودع Microsoft Agent Framework](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) و[التوثيق الرسمي](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

الإطار التالي الذي سنستعرضه هو [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). يُعرف بأنه وكيل "كود-أول" لأنه بدلاً من العمل فقط مع `strings`، يمكنه العمل مع DataFrames في Python. هذا يصبح مفيدًا جدًا لمهام تحليل وتوليد البيانات. قد تكون هذه أشياء مثل إنشاء الرسوم البيانية والمخططات أو توليد أرقام عشوائية.

### الحالة والأدوات

لإدارة حالة المحادثة، يستخدم TaskWeaver مفهوم `Planner`. `Planner` هو نموذج لغة كبيرة يأخذ طلب المستخدم ويخطط للمهام التي يجب إكمالها لتحقيق هذا الطلب.

لتنفيذ المهام، يتعرض `Planner` لمجموعة الأدوات المسماة `Plugins`. يمكن أن تكون هذه فئات Python أو مفسر كود عام. تُخزن هذه الإضافات كتمثيلات متضمنة بحيث يمكن لنموذج اللغة الكبيرة البحث بشكل أفضل عن الإضافة الصحيحة.

![Taskweaver](../../../translated_images/ar/taskweaver.da8559999267715a.webp)

إليك مثال على إضافة للتعامل مع كشف الشذوذ:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

يتم التحقق من الكود قبل التنفيذ. ميزة أخرى لإدارة السياق في Taskweaver هي `experience`. تسمح الخبرة بتخزين سياق المحادثة على المدى الطويل في ملف YAML. يمكن تكوين ذلك بحيث يتحسن نموذج اللغة الكبيرة بمرور الوقت في مهام معينة بشرط أن يتعرض للمحادثات السابقة.

## JARVIS

الإطار الأخير الذي سنستعرضه هو [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). ما يجعل JARVIS فريدًا هو أنه يستخدم نموذج لغة كبيرة لإدارة `الحالة` في المحادثة و`الأدوات` هي نماذج ذكاء اصطناعي أخرى. كل نموذج ذكاء اصطناعي متخصص بأداء مهام معينة مثل اكتشاف الأشياء، النسخ أو وصف الصور.

![JARVIS](../../../translated_images/ar/jarvis.762ddbadbd1a3a33.webp)

يتلقى نموذج اللغة الكبيرة، كونه نموذجًا عامًا، الطلب من المستخدم ويحدد المهمة المحددة وأي بيانات/معطيات مطلوبة لاستكمال المهمة.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

يقوم نموذج اللغة الكبيرة بعد ذلك بتنسيق الطلب بطريقة يمكن للنموذج الذكي المتخصص تفسيرها، مثل JSON. بمجرد أن يعيد النموذج الذكي توقعه بناءً على المهمة، يستلم نموذج اللغة الكبيرة الاستجابة.

إذا تطلبت المهمة عدة نماذج، فسوف يفسر أيضًا الاستجابات من تلك النماذج قبل جمعها معًا لتوليد الرد للمستخدم.

المثال أدناه يوضح كيف سيعمل هذا عندما يطلب المستخدم وصفًا وعددًا للأشياء في صورة:

## مهمة

لمواصلة تعلمك عن وكلاء الذكاء الاصطناعي يمكنك البناء باستخدام إطار عمل Microsoft Agent:

- تطبيق يحاكي اجتماع عمل مع أقسام مختلفة لشركة ناشئة في مجال التعليم.
- إنشاء رسائل نظام ترشد نماذج اللغة الكبيرة لفهم الأدوار والأولويات المختلفة، وتمكين المستخدم من تقديم فكرة لمنتج جديد.
- يجب على نموذج اللغة الكبيرة بعد ذلك توليد أسئلة متابعة من كل قسم لصقل وتحسين العرض وفكرة المنتج

## التعلم لا يتوقف هنا، تابع الرحلة

بعد إتمام هذا الدرس، اطلع على [مجموعة تعلم الذكاء الاصطناعي التوليدي](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) لمواصلة رفع مستواك في معرفة الذكاء الاصطناعي التوليدي!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->