<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-05-19T15:08:53+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "mo"
}
-->
# أساسيات هندسة المطالبات

## مقدمة
يغطي هذا الجزء مفاهيم وتقنيات أساسية لإنشاء مطالبات فعالة في نماذج الذكاء الاصطناعي التوليدي. كيفية كتابة مطالبتك لنموذج اللغة الكبير (LLM) أمر مهم أيضًا. يمكن أن تحقق المطالبة المصممة بعناية استجابة ذات جودة أفضل. لكن ماذا تعني بالضبط مصطلحات مثل _المطالبة_ و_هندسة المطالبات_؟ وكيف يمكنني تحسين _إدخال_ المطالبة الذي أرسله إلى LLM؟ هذه هي الأسئلة التي سنحاول الإجابة عليها في هذا الفصل والفصل التالي.

_الذكاء الاصطناعي التوليدي_ قادر على إنشاء محتوى جديد (مثل النصوص، الصور، الصوت، الأكواد، إلخ) استجابة لطلبات المستخدم. يحقق ذلك باستخدام _نماذج اللغة الكبيرة_ مثل سلسلة GPT ("المحول المدرب التوليدي") من OpenAI التي تم تدريبها لاستخدام اللغة الطبيعية والأكواد.

يمكن للمستخدمين الآن التفاعل مع هذه النماذج باستخدام طرق مألوفة مثل الدردشة، دون الحاجة إلى أي خبرة تقنية أو تدريب. النماذج تعتمد على _المطالبات_ - يرسل المستخدمون إدخال نصي (مطالبة) ويحصلون على استجابة من الذكاء الاصطناعي (إكمال). يمكنهم بعد ذلك "الدردشة مع الذكاء الاصطناعي" بشكل متكرر، في محادثات متعددة الجولات، وتحسين مطالبتهم حتى تتطابق الاستجابة مع توقعاتهم.

تُعد "المطالبات" الآن الواجهة _البرمجية_ الأساسية لتطبيقات الذكاء الاصطناعي التوليدي، حيث تخبر النماذج بما يجب فعله وتؤثر على جودة الاستجابات التي يتم إرجاعها. "هندسة المطالبات" هو مجال دراسي سريع النمو يركز على _تصميم وتحسين_ المطالبات لتقديم استجابات متسقة وعالية الجودة على نطاق واسع.

## أهداف التعلم

في هذا الدرس، نتعلم ما هي هندسة المطالبات، ولماذا هي مهمة، وكيف يمكننا صياغة مطالبات أكثر فعالية لنموذج وهدف تطبيق معين. سنتعرف على المفاهيم الأساسية وأفضل الممارسات لهندسة المطالبات - ونتعرف على بيئة "صندوق الرمل" التفاعلية لـ Jupyter Notebooks حيث يمكننا رؤية هذه المفاهيم مطبقة على أمثلة حقيقية.

بنهاية هذا الدرس سنكون قادرين على:

1. شرح ما هي هندسة المطالبات ولماذا هي مهمة.
2. وصف مكونات المطالبة وكيفية استخدامها.
3. تعلم أفضل الممارسات والتقنيات لهندسة المطالبات.
4. تطبيق التقنيات المتعلمة على أمثلة حقيقية، باستخدام نقطة نهاية OpenAI.

## المصطلحات الأساسية

هندسة المطالبات: ممارسة تصميم وتحسين المدخلات لتوجيه نماذج الذكاء الاصطناعي نحو إنتاج المخرجات المطلوبة.
التقطيع: عملية تحويل النص إلى وحدات أصغر، تسمى الرموز، التي يمكن للنموذج فهمها ومعالجتها.
نماذج LLM المضبوطة على التعليمات: نماذج اللغة الكبيرة (LLMs) التي تم تحسينها بتعليمات محددة لتحسين دقة واستجابة استجاباتها.

## صندوق التعلم

هندسة المطالبات حاليًا تعتبر أكثر فنًا من كونها علمًا. أفضل طريقة لتحسين حدسنا لها هي _التدرب أكثر_ واتباع نهج التجربة والخطأ الذي يجمع بين خبرة مجال التطبيق والتقنيات الموصى بها والتحسينات الخاصة بالنموذج.

يوفر دفتر Jupyter المرفق بهذا الدرس بيئة _صندوق الرمل_ حيث يمكنك تجربة ما تتعلمه - أثناء التنقل أو كجزء من تحدي الكود في النهاية. لتنفيذ التمارين، ستحتاج إلى:

1. **مفتاح Azure OpenAI API** - نقطة النهاية للخدمة لنموذج LLM المنشور.
2. **بيئة تشغيل بايثون** - حيث يمكن تنفيذ الدفتر.
3. **متغيرات البيئة المحلية** - _أكمل خطوات [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) الآن لتكون جاهزًا_.

يأتي الدفتر مع تمارين _بداية_ - لكن يُشجعك على إضافة أقسام _Markdown_ (وصف) و_Code_ (طلبات المطالبة) الخاصة بك لتجربة المزيد من الأمثلة أو الأفكار - وبناء حدسك لتصميم المطالبات.

## دليل مصور

هل تريد الحصول على فكرة عامة عن ما يغطيه هذا الدرس قبل الغوص فيه؟ تحقق من هذا الدليل المصور، الذي يعطيك فكرة عن الموضوعات الرئيسية التي يغطيها الدرس والنقاط الرئيسية التي يجب التفكير فيها في كل منها. يأخذك خريطة الدرس من فهم المفاهيم والتحديات الأساسية إلى معالجتها بتقنيات هندسة المطالبات ذات الصلة وأفضل الممارسات. لاحظ أن قسم "التقنيات المتقدمة" في هذا الدليل يشير إلى المحتوى المغطى في الفصل _التالي_ من هذا المنهج.

## شركتنا الناشئة

الآن، دعونا نتحدث عن كيف يرتبط _هذا الموضوع_ بمهمتنا في الشركة الناشئة [لجلب الابتكار في الذكاء الاصطناعي إلى التعليم](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). نريد بناء تطبيقات تعتمد على الذكاء الاصطناعي للتعلم الشخصي - لذا دعونا نفكر في كيفية "تصميم" المطالبات من قبل المستخدمين المختلفين لتطبيقنا:

- **الإداريون** قد يطلبون من الذكاء الاصطناعي _تحليل بيانات المنهج لتحديد الفجوات في التغطية_. يمكن للذكاء الاصطناعي تلخيص النتائج أو تصورها باستخدام الأكواد.
- **المعلمين** قد يطلبون من الذكاء الاصطناعي _إنشاء خطة درس لجمهور مستهدف وموضوع معين_. يمكن للذكاء الاصطناعي بناء الخطة الشخصية في تنسيق محدد.
- **الطلاب** قد يطلبون من الذكاء الاصطناعي _تدريسهم في موضوع صعب_. يمكن للذكاء الاصطناعي الآن إرشاد الطلاب بالدروس، والنصائح والأمثلة المخصصة لمستواهم.

هذا مجرد غيض من فيض. تحقق من [مطالبات للتعليم](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - مكتبة مطالبات مفتوحة المصدر يتم تنسيقها من قبل خبراء التعليم - للحصول على فكرة أوسع عن الإمكانيات! _جرب تشغيل بعض تلك المطالبات في صندوق الرمل أو باستخدام OpenAI Playground لترى ما يحدث!_

## ما هي هندسة المطالبات؟

بدأنا هذا الدرس بتعريف **هندسة المطالبات** كعملية _تصميم وتحسين_ المدخلات النصية (المطالبات) لتقديم استجابات متسقة وعالية الجودة (إكمالات) لهدف تطبيق معين ونموذج. يمكننا التفكير في هذا كعملية من خطوتين:

- _تصميم_ المطالبة الأولية لنموذج وهدف معين
- _تحسين_ المطالبة بشكل متكرر لتحسين جودة الاستجابة

هذه عملية تجريبية بالضرورة تتطلب حدس المستخدم وجهوده للحصول على النتائج المثلى. فلماذا هي مهمة؟ للإجابة على هذا السؤال، نحتاج أولاً إلى فهم ثلاثة مفاهيم:

- _التقطيع_ = كيف "يرى" النموذج المطالبة
- _نماذج LLM الأساسية_ = كيف "يعالج" نموذج الأساس المطالبة
- _نماذج LLM المضبوطة على التعليمات_ = كيف يمكن للنموذج الآن رؤية "المهام"

### التقطيع

يرى LLM المطالبات كسلسلة من الرموز حيث يمكن للنماذج المختلفة (أو إصدارات النموذج) تقطيع نفس المطالبة بطرق مختلفة. نظرًا لأن LLMs يتم تدريبها على الرموز (وليس على النص الخام)، فإن الطريقة التي يتم بها تقطيع المطالبات لها تأثير مباشر على جودة الاستجابة المولدة.

للحصول على حدس حول كيفية عمل التقطيع، جرب أدوات مثل [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) الموضحة أدناه. انسخ مطالبتك - وانظر كيف يتم تحويلها إلى رموز، مع الانتباه إلى كيفية التعامل مع الأحرف البيضاء وعلامات الترقيم. لاحظ أن هذا المثال يظهر LLM قديم (GPT-3) - لذا فإن محاولة ذلك مع نموذج أحدث قد تنتج نتيجة مختلفة.

### مفهوم: نماذج الأساس

بمجرد تقطيع المطالبة، الوظيفة الأساسية لـ ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (أو نموذج الأساس) هي التنبؤ بالرمز في تلك السلسلة. نظرًا لأن LLMs يتم تدريبها على مجموعات بيانات نصية ضخمة، فإنها تتمتع بفهم جيد للعلاقات الإحصائية بين الرموز ويمكنها إجراء هذا التنبؤ بثقة معينة. لاحظ أنها لا تفهم _معنى_ الكلمات في المطالبة أو الرمز؛ إنها ترى فقط نمطًا يمكنها "إكماله" بتنبؤها التالي. يمكنها الاستمرار في التنبؤ بالسلسلة حتى يتم إنهاؤها بواسطة تدخل المستخدم أو شرط مسبق محدد.

هل تريد أن ترى كيف يعمل الإكمال القائم على المطالبات؟ أدخل المطالبة أعلاه في Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) بالإعدادات الافتراضية. تم تكوين النظام للتعامل مع المطالبات كطلبات للحصول على معلومات - لذا يجب أن ترى إكمالًا يرضي هذا السياق.

لكن ماذا لو أراد المستخدم رؤية شيء محدد يفي ببعض المعايير أو هدف المهمة؟ هنا تأتي نماذج LLM المضبوطة على التعليمات.

### مفهوم: نماذج LLM المضبوطة على التعليمات

يبدأ [نموذج LLM المضبوط على التعليمات](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) بنموذج الأساس ويقوم بضبطه باستخدام أمثلة أو أزواج إدخال/إخراج (مثل "الرسائل" متعددة الجولات) التي يمكن أن تحتوي على تعليمات واضحة - وتحاول الاستجابة من الذكاء الاصطناعي اتباع تلك التعليمات.

يستخدم ذلك تقنيات مثل التعلم المعزز مع ملاحظات البشر (RLHF) التي يمكن أن تدرب النموذج على _اتباع التعليمات_ و_التعلم من الملاحظات_ بحيث ينتج استجابات تكون أكثر ملاءمة للتطبيقات العملية وأكثر ملاءمة لأهداف المستخدم.

دعونا نجربها - عد إلى المطالبة أعلاه، ولكن الآن قم بتغيير _رسالة النظام_ لتوفير التعليمات التالية كسياق:

> _قم بتلخيص المحتوى الذي يتم توفيره لك لطلاب الصف الثاني. احتفظ بالنتيجة في فقرة واحدة مع 3-5 نقاط تعداد._

لاحظ كيف تم ضبط النتيجة الآن لتعكس الهدف والشكل المطلوبين؟ يمكن للمعلم الآن استخدام هذه الاستجابة مباشرة في شرائحه لتلك الحصة.

## لماذا نحتاج إلى هندسة المطالبات؟

الآن بعد أن عرفنا كيف تتم معالجة المطالبات بواسطة LLMs، دعونا نتحدث عن _لماذا_ نحتاج إلى هندسة المطالبات. يكمن الجواب في حقيقة أن LLMs الحالية تطرح عددًا من التحديات التي تجعل تحقيق _إكمالات موثوقة ومتسقة_ أكثر تحديًا دون بذل جهد في بناء المطالبة وتحسينها. على سبيل المثال:

1. **استجابات النموذج عشوائية.** من المحتمل أن تنتج _نفس المطالبة_ استجابات مختلفة مع نماذج أو إصدارات نماذج مختلفة. وقد تنتج أيضًا نتائج مختلفة مع _نفس النموذج_ في أوقات مختلفة. _يمكن أن تساعدنا تقنيات هندسة المطالبات في تقليل هذه الاختلافات من خلال توفير ضوابط أفضل_.

2. **النماذج يمكن أن تبتكر استجابات.** يتم تدريب النماذج على مجموعات بيانات _كبيرة ولكن محدودة_، مما يعني أنها تفتقر إلى المعرفة حول المفاهيم خارج نطاق التدريب هذا. ونتيجة لذلك، يمكنها إنتاج إكمالات غير دقيقة أو خيالية أو تتعارض مباشرة مع الحقائق المعروفة. _تساعد تقنيات هندسة المطالبات المستخدمين على تحديد وتخفيف هذه الابتكارات مثلًا، عن طريق طلب الاقتباسات أو المنطق من الذكاء الاصطناعي_.

3. **قدرات النماذج ستختلف.** النماذج الأحدث أو الأجيال الجديدة من النماذج ستكون لديها قدرات أغنى ولكنها ستجلب أيضًا ميزات فريدة وتنازلات في التكلفة والتعقيد. _يمكن أن تساعدنا هندسة المطالبات في تطوير أفضل الممارسات وعمليات العمل التي تتجاوز الاختلافات وتتكيف مع المتطلبات الخاصة بالنموذج بطرق قابلة للتطوير وسلسة_.

دعونا نرى ذلك في العمل في OpenAI أو Azure OpenAI Playground:

- استخدم نفس المطالبة مع نشرات LLM مختلفة (مثل OpenAI، Azure OpenAI، Hugging Face) - هل لاحظت الاختلافات؟
- استخدم نفس المطالبة بشكل متكرر مع نشر LLM _نفسه_ (مثل ملعب Azure OpenAI) - كيف اختلفت هذه الاختلافات؟

### مثال على الابتكارات

في هذا الدرس، نستخدم مصطلح **"الابتكار"** للإشارة إلى الظاهرة التي يحدث فيها أن تولد LLMs معلومات غير صحيحة بسبب قيود في تدريبها أو قيود أخرى. ربما سمعت أيضًا عن هذا في المقالات الشعبية أو الأبحاث تحت مصطلح _"الهلاوس"_. ومع ذلك، نوصي بشدة باستخدام مصطلح _"الابتكار"_ حتى لا ننسب بشكل غير مقصود سمة بشرية إلى نتيجة تقودها الآلة. يعزز ذلك أيضًا [إرشادات الذكاء الاصطناعي المسؤول](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) من منظور المصطلحات، بإزالة المصطلحات التي قد تعتبر مهينة أو غير شاملة في بعض السياقات.

هل تريد أن تفهم كيف تعمل الابتكارات؟ فكر في مطالبة توجه الذكاء الاصطناعي لإنشاء محتوى لموضوع غير موجود (لضمان عدم وجوده في مجموعة البيانات التدريبية). على سبيل المثال - جربت هذه المطالبة:

> **مطالبة:** أنشئ خطة درس عن حرب المريخ لعام 2076.

أظهرت لي عملية بحث عبر الإنترنت أن هناك حسابات خيالية (مثل المسلسلات التلفزيونية أو الكتب) عن حروب المريخ - لكن لا شيء في عام 2076. يخبرنا الفطرة السليمة أيضًا أن 2076 هو _في المستقبل_ وبالتالي، لا يمكن ربطه بحدث حقيقي.

إذن ماذا يحدث عندما نشغل هذه المطالبة مع موفري LLM المختلفين؟

كما هو متوقع، كل نموذج (أو إصدار نموذج) ينتج استجابات مختلفة قليلاً بفضل السلوك العشوائي وتنوع قدرات النموذج. على سبيل المثال، يوجه أحد النماذج لجمهور الصف الثامن بينما يفترض الآخر طالبًا في المدرسة الثانوية. لكن جميع النماذج الثلاثة أنتجت استجابات يمكن أن تقنع مستخدمًا غير مطلع بأن الحدث كان حقيقيًا.

تقنيات هندسة المطالبات مثل _التوجيه الفوقي_ و_تكوين درجة الحرارة_ قد تقلل من ابتكارات النموذج إلى حد ما. كما تدمج _الهندسات_ الجديدة لهندسة المطالبات أدوات وتقنيات جديدة بسلاسة في تدفق المطالبات، لتخفيف أو تقليل بعض هذه التأثيرات.

## دراسة حالة: GitHub Copilot

لنختتم هذا القسم بالحصول على فكرة عن كيفية استخدام هندسة المطالبات في الحلول الواقعية من خلال النظر في دراسة حالة واحدة: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot هو "مساعد البرمجة الثنائي بالذكاء الاصطناعي" الخاص بك - يحول المطالبات النصية إلى إكمالات للكود ويتم دمجه في بيئة التطوير الخاصة بك (مثل Visual Studio Code) لتجربة مستخدم سلسة. كما تم توثيقه في سلسلة المدونات أدناه، كان الإصدار الأولي يعتمد على نموذج OpenAI Codex - مع إدراك المهندسين بسرعة الحاجة إلى ضبط النموذج وتطوير تقنيات هندسة المطالبات الأفضل، لتحسين جودة الكود. في يوليو، [قدموا نموذج ذكاء اصطناعي محسّن يتجاوز Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) للحصول على اقتراحات أسرع.

اقرأ المنشورات بالترتيب، لمتابعة رحلتهم التعليمية.

- **مايو 2023** | [GitHub Copilot يتحسن في فهم كودك](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **مايو 2023** | [داخل GitHub: العمل مع LLMs وراء GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **يونيو 2023** | [كيفية كتابة مطالبات أفضل لـ GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **يوليو 2023** | [.. GitHub Copilot يتجاوز Codex مع نموذج ذكاء اصطناعي محسّن](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model
Finally, the true value of templates lies in the ability to create and publish _prompt libraries_ for specific application domains - where the prompt template is now _optimized_ to reflect application-specific context or examples that make the responses more relevant and accurate for the targeted user audience. The [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) repository is a great example of this approach, curating a library of prompts for the education domain with emphasis on key objectives like lesson planning, curriculum design, student tutoring etc.

## Supporting Content

If we think about prompt construction as having an instruction (task) and a target (primary content), then _secondary content_ is like additional context we provide to **influence the output in some way**. It could be tuning parameters, formatting instructions, topic taxonomies etc. that can help the model _tailor_ its response to suit the desired user objectives or expectations.

For example: Given a course catalog with extensive metadata (name, description, level, metadata tags, instructor etc.) on all the available courses in the curriculum:

- we can define an instruction to "summarize the course catalog for Fall 2023"
- we can use the primary content to provide a few examples of the desired output
- we can use the secondary content to identify the top 5 "tags" of interest.

Now, the model can provide a summary in the format shown by the few examples - but if a result has multiple tags, it can prioritize the 5 tags identified in secondary content.

---

## Prompting Best Practices

Now that we know how prompts can be _constructed_, we can start thinking about how to _design_ them to reflect best practices. We can think about this in two parts - having the right _mindset_ and applying the right _techniques_.

### Prompt Engineering Mindset

Prompt Engineering is a trial-and-error process so keep three broad guiding factors in mind:

1. **Domain Understanding Matters.** Response accuracy and relevance is a function of the _domain_ in which that application or user operates. Apply your intuition and domain expertise to **customize techniques** further. For instance, define _domain-specific personalities_ in your system prompts, or use _domain-specific templates_ in your user prompts. Provide secondary content that reflects domain-specific contexts, or use _domain-specific cues and examples_ to guide the model towards familiar usage patterns.

2. **Model Understanding Matters.** We know models are stochastic by nature. But model implementations can also vary in terms of the training dataset they use (pre-trained knowledge), the capabilities they provide (e.g., via API or SDK) and the type of content they are optimized for (e.g., code vs. images vs. text). Understand the strengths and limitations of the model you are using, and use that knowledge to _prioritize tasks_ or build _customized templates_ that are optimized for the model's capabilities.

3. **Iteration & Validation Matters.** Models are evolving rapidly, and so are the techniques for prompt engineering. As a domain expert, you may have other context or criteria _your_ specific application, that may not apply to the broader community. Use prompt engineering tools & techniques to "jump start" prompt construction, then iterate and validate the results using your own intuition and domain expertise. Record your insights and create a **knowledge base** (e.g., prompt libraries) that can be used as a new baseline by others, for faster iterations in the future.

## Best Practices

Now let's look at common best practices that are recommended by [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) and [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst) practitioners.

| What                              | Why                                                                                                                                                                                                                                               |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Evaluate the latest models.       | New model generations are likely to have improved features and quality - but may also incur higher costs. Evaluate them for impact, then make migration decisions.                                                                                |
| Separate instructions & context   | Check if your model/provider defines _delimiters_ to distinguish instructions, primary and secondary content more clearly. This can help models assign weights more accurately to tokens.                                                         |
| Be specific and clear             | Give more details about the desired context, outcome, length, format, style etc. This will improve both the quality and consistency of responses. Capture recipes in reusable templates.                                                          |
| Be descriptive, use examples      | Models may respond better to a "show and tell" approach. Start with a `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
| Use cues to jumpstart completions | Nudge it towards a desired outcome by giving it some leading words or phrases that it can use as a starting point for the response.                                                                                                               |
| Double Down                       | Sometimes you may need to repeat yourself to the model. Give instructions before and after your primary content, use an instruction and a cue, etc. Iterate & validate to see what works.                                                         |
| Order Matters                     | The order in which you present information to the model may impact the output, even in the learning examples, thanks to recency bias. Try different options to see what works best.                                                               |
| Give the model an “out”           | Give the model a _fallback_ completion response it can provide if it cannot complete the task for any reason. This can reduce chances of models generating false or fabricated responses.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

As with any best practice, remember that _your mileage may vary_ based on the model, the task and the domain. Use these as a starting point, and iterate to find what works best for you. Constantly re-evaluate your prompt engineering process as new models and tools become available, with a focus on process scalability and response quality.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Assignment

Congratulations! You made it to the end of the lesson! It's time to put some of those concepts and techniques to the test with real examples!

For our assignment, we'll be using a Jupyter Notebook with exercises you can complete interactively. You can also extend the Notebook with your own Markdown and Code cells to explore ideas and techniques on your own.

### To get started, fork the repo, then

- (Recommended) Launch GitHub Codespaces
- (Alternatively) Clone the repo to your local device and use it with Docker Desktop
- (Alternatively) Open the Notebook with your preferred Notebook runtime environment.

### Next, configure your environment variables

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` values. Come back to [Learning Sandbox section](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) to learn how.

### Next, open the Jupyter Notebook

- Select the runtime kernel. If using options 1 or 2, simply select the default Python 3.10.x kernel provided by the dev container.

You're all set to run the exercises. Note that there are no _right and wrong_ answers here - just exploring options by trial-and-error and building intuition for what works for a given model and application domain.

_For this reason there are no Code Solution segments in this lesson. Instead, the Notebook will have Markdown cells titled "My Solution:" that shows one example output for reference._

## Knowledge check

Which of the following is a good prompt following some reasonable best practices?

1. Show me an image of red car
2. Show me an image of red car of make Volvo and model XC90 parked by a cliff with the sun setting
3. Show me an image of red car of make Volvo and model XC90

A: 2, it's the best prompt as it provides details on "what" and goes into specifics (not just any car but a specific make and model) and it also describes the overall setting. 3 is next best as it also contains a lot of description.

## 🚀 Challenge

See if you can leverage the "cue" technique with the prompt: Complete the sentence "Show me an image of red car of make Volvo and ". What does it respond with, and how would you improve it?

## Great Work! Continue Your Learning

Want to learn more about different Prompt Engineering concepts? Go to the [continued learning page](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to find other great resources on this topic.

Head over to Lesson 5 where we will look at [advanced prompting techniques](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

It seems like you want the text translated into a language or dialect you referred to as "mo." However, "mo" is not a standard language code, so I need more context to provide an accurate translation. Could you please clarify which language you are referring to?